"""
Duru's Schoolhub — lokale server + score-API.

  GET  /            → statische bestanden (SimpleHTTPRequestHandler)
  GET  /api/score   → lijst met één record per sleutel (laatste, samengevoegde staat)
  POST /api/score   → {key, val, timestamp} — wordt SAMENGEVOEGD in de staat

Opslagvorm (v2, sinds 2026-09-04)
---------------------------------
scores.json was een append-only lijst van momentopnames: elke setItem in de
examenmotor schreef de volledige dataset opnieuw weg. Dat gaf 723 records over
slechts 7 sleutels — 12,2 MB, en elke POST dwong een volledige herschrijving.

Nu: scores.json = {"version": 2, "keys": {<sleutel>: <record>}}. Per sleutel
bewaren we één record, en bij binnenkomst voegen we de geschiedenis SAMEN
(union op attemptId). Daarmee blijft het herstelgedrag van restoreScores()
intact — een oude poging die alleen op één apparaat stond gaat niet verloren —
terwijl het bestand niet meer groeit.

De losse gebeurtenissen komen in events.jsonl: één regel per nieuwe poging,
~100 bytes, append-only. Dat is de historie voor later, zonder parse-kosten.

Een v1-lijst wordt bij de eerste aanraking automatisch gemigreerd; er wordt
eerst een backup weggeschreven.
"""

import sys
import os
import json
import shutil
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer

BASIS = os.path.dirname(os.path.abspath(__file__))
SCORES_BESTAND = os.path.join(BASIS, 'scores.json')
EVENTS_BESTAND = os.path.join(BASIS, 'events.jsonl')
LOG_BESTAND    = os.path.join(BASIS, 'scores_log.txt')


# ── Poging-identiteit ─────────────────────────────────────
# Zelfde regels als restoreScores() in js/landing.js, zodat client en server
# dezelfde pogingen als "dezelfde" zien.

def poging_id(att):
    if not isinstance(att, dict):
        return json.dumps(att, sort_keys=True, ensure_ascii=False)
    if att.get('attemptId'):
        return str(att['attemptId'])
    return '{}_{}_{}'.format(att.get('examId', ''), att.get('datum', ''), att.get('pct', ''))


def bl_poging_id(att):
    if not isinstance(att, dict):
        return json.dumps(att, sort_keys=True, ensure_ascii=False)
    if att.get('timestamp'):
        return str(att['timestamp'])
    return '{}_{}_{}'.format(att.get('startingText', ''), att.get('grade', ''), att.get('score', ''))


def poging_tijd(att):
    """Sorteersleutel: nieuwste eerst. Spiegelt parseAttemptDate() in landing.js."""
    if not isinstance(att, dict):
        return 0
    aid = att.get('attemptId')
    if isinstance(aid, str) and aid.startswith('att_'):
        try:
            return int(aid[4:])
        except ValueError:
            pass
    datum = att.get('datum')
    if isinstance(datum, str):
        try:
            d, t = datum.replace(',', '').split(' ')[:2]
            dag, maand, jaar = d.split('-')
            uur, minuut = t.split(':')[:2]
            return int(datetime.datetime(int(jaar), int(maand), int(dag),
                                         int(uur), int(minuut)).timestamp() * 1000)
        except Exception:
            pass
    return 0


# ── Samenvoegen ───────────────────────────────────────────

def voeg_samen(key, oude_val, nieuwe_val):
    """Geeft (samengevoegde_waarde, nieuwe_pogingen) terug."""

    # 1. Begrijpend lezen: platte lijst met pogingen
    if isinstance(nieuwe_val, list):
        oud = oude_val if isinstance(oude_val, list) else []
        gezien = {bl_poging_id(a): a for a in oud}
        vers = []
        for a in nieuwe_val:
            i = bl_poging_id(a)
            if i not in gezien:
                vers.append(a)
            gezien[i] = a
        samen = list(gezien.values())
        samen.sort(key=lambda a: str(a.get('timestamp', '')) if isinstance(a, dict) else '',
                   reverse=True)
        return samen, vers

    # 2. Examens: {beste, laatste, history}
    if isinstance(nieuwe_val, dict) and isinstance(nieuwe_val.get('history'), list):
        oude_hist = oude_val.get('history') if isinstance(oude_val, dict) else None
        oude_hist = oude_hist if isinstance(oude_hist, list) else []

        gezien = {poging_id(a): a for a in oude_hist}
        vers = []
        for a in nieuwe_val['history']:
            i = poging_id(a)
            if i not in gezien:
                vers.append(a)
            gezien[i] = a

        hist = list(gezien.values())
        hist.sort(key=poging_tijd, reverse=True)

        beste, laatste = {}, {}
        for a in hist:
            if not isinstance(a, dict):
                continue
            eid = a.get('examId')
            if not eid:
                continue
            pct = a.get('pct') or 0
            if eid not in laatste:
                laatste[eid] = pct
            if eid not in beste or pct > beste[eid]:
                beste[eid] = pct

        # Waarden die de client kent maar die niet in de history staan, blijven staan.
        for veld, doel in (('beste', beste), ('laatste', laatste)):
            van_client = nieuwe_val.get(veld)
            if isinstance(van_client, dict):
                for eid, pct in van_client.items():
                    if veld == 'beste':
                        if eid not in doel or (pct or 0) > doel[eid]:
                            doel[eid] = pct
                    else:
                        doel.setdefault(eid, pct)

        samen = dict(nieuwe_val)
        samen['history'] = hist
        samen['beste'] = beste
        samen['laatste'] = laatste
        return samen, vers

    # 3. Oefenvoortgang (xp, badges, pogingen…): laatste schrijver wint.
    return nieuwe_val, []


# ── Staat lezen / schrijven ───────────────────────────────

def _migreer_v1(lijst):
    """Oude append-only lijst → staat per sleutel, met samenvoeging."""
    staat = {}
    for record in lijst:
        if not isinstance(record, dict):
            continue
        key = record.get('key')
        if not key:
            continue
        bestaand = staat.get(key)
        oude_val = bestaand.get('val') if bestaand else None
        samen, _ = voeg_samen(key, oude_val, record.get('val'))
        staat[key] = {
            'key': key,
            'val': samen,
            'timestamp': record.get('timestamp', ''),
            'received_at': record.get('received_at', ''),
            'client_ip': record.get('client_ip', ''),
        }
    return staat


def lees_staat():
    if not os.path.exists(SCORES_BESTAND):
        return {}
    try:
        with open(SCORES_BESTAND, 'r', encoding='utf-8') as f:
            rauw = json.load(f)
    except Exception as e:
        print(f"⚠️  scores.json onleesbaar ({e}) — er wordt met een lege staat verder gegaan.", flush=True)
        return {}

    if isinstance(rauw, dict) and rauw.get('version') == 2:
        keys = rauw.get('keys')
        return keys if isinstance(keys, dict) else {}

    if isinstance(rauw, list):
        backup = os.path.join(BASIS, 'scores_v1_backup_%s.json'
                              % datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
        try:
            shutil.copy2(SCORES_BESTAND, backup)
            print(f"📦 v1-backup: {os.path.basename(backup)}", flush=True)
        except Exception as e:
            print(f"⚠️  backup mislukt ({e}) — migratie afgebroken, niets aangeraakt.", flush=True)
            return _migreer_v1(rauw)
        staat = _migreer_v1(rauw)
        schrijf_staat(staat)
        print(f"✅ scores.json gemigreerd naar v2: {len(rauw)} records → {len(staat)} sleutels", flush=True)
        return staat

    return {}


def schrijf_staat(staat):
    """Atomisch: eerst temp, dan vervangen — nooit een half bestand."""
    tmp = SCORES_BESTAND + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump({'version': 2, 'keys': staat}, f, indent=2, ensure_ascii=False)
    os.replace(tmp, SCORES_BESTAND)


def schrijf_events(key, pogingen, ontvangen_op):
    """Eén dunne regel per nieuwe poging. Append-only, geen parse nodig."""
    if not pogingen:
        return
    with open(EVENTS_BESTAND, 'a', encoding='utf-8') as f:
        for a in pogingen:
            if not isinstance(a, dict):
                continue
            f.write(json.dumps({
                'ts': ontvangen_op,
                'key': key,
                'examId': a.get('examId', ''),
                'titel': a.get('examTitel') or a.get('startingText') or '',
                'goed': a.get('goed') if a.get('goed') is not None else a.get('score'),
                'totaal': a.get('totaal') if a.get('totaal') is not None else a.get('total'),
                'pct': a.get('pct'),
                'datum': a.get('datum') or a.get('timestamp', ''),
            }, ensure_ascii=False) + '\n')


def leesbare_samenvatting(key, val, tijdstip, ip, aantal_nieuw):
    regel = f"[{tijdstip}] IP: {ip} | Key: {key}\n"
    if isinstance(val, dict) and 'history' in val:
        hist = val.get('history') or []
        if hist:
            a = hist[0]
            regel += (f"  📝 EXAM: {a.get('examTitel', '')} | "
                      f"{a.get('pct', 0)}% ({a.get('goed', 0)}/{a.get('totaal', 0)}) | "
                      f"{aantal_nieuw} nieuw\n")
    elif isinstance(val, dict) and 'pts' in val:
        regel += f"  💎 XP: {val.get('pts', 0)} | Badges: {len(val.get('badges', []))}\n"
    elif isinstance(val, dict) and 'beste' in val:
        regel += f"  🏆 {len(val.get('beste', {}))} beste scores bijgewerkt\n"
    elif isinstance(val, list) and val and isinstance(val[0], dict):
        a = val[0]
        regel += (f"  📖 LEZEN: {a.get('startingText', '')} | "
                  f"{a.get('score', 0)}/{a.get('total', 0)} | {aantal_nieuw} nieuw\n")
    else:
        regel += "  💾 voortgang bijgewerkt\n"
    return regel


class CustomHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path != '/api/score':
            self.send_response(404)
            self.end_headers()
            return

        try:
            lengte = int(self.headers.get('Content-Length', 0))
            data = json.loads(self.rfile.read(lengte).decode('utf-8'))

            key = data.get('key', '')
            if not key:
                raise ValueError('record zonder key')

            ip = self.client_address[0]
            nu = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            staat = lees_staat()
            bestaand = staat.get(key)
            oude_val = bestaand.get('val') if bestaand else None

            samen, nieuwe_pogingen = voeg_samen(key, oude_val, data.get('val'))

            staat[key] = {
                'key': key,
                'val': samen,
                'timestamp': data.get('timestamp', ''),
                'received_at': nu,
                'client_ip': ip,
            }
            schrijf_staat(staat)
            schrijf_events(key, nieuwe_pogingen, nu)

            samenvatting = leesbare_samenvatting(key, samen, nu, ip, len(nieuwe_pogingen))
            with open(LOG_BESTAND, 'a', encoding='utf-8') as f:
                f.write(samenvatting + '\n')
            print(samenvatting, end='', flush=True)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'success',
                'sleutels': len(staat),
                'nieuw': len(nieuwe_pogingen),
            }).encode('utf-8'))

        except Exception as e:
            print(f"Error handling /api/score: {e}", flush=True)
            self.send_response(500)
            self.end_headers()

    def do_GET(self):
        if self.path.startswith('/api/score'):
            try:
                staat = lees_staat()
                # Lijstvorm blijft behouden: js/landing.js → restoreScores(data)
                # verwacht een array van {key, val, …}-records.
                lichaam = json.dumps(list(staat.values()), ensure_ascii=False).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Pragma', 'no-cache')
                self.send_header('Expires', '0')
                self.end_headers()
                self.wfile.write(lichaam)
            except Exception as e:
                print(f"Error reading scores: {e}", flush=True)
                self.send_response(500)
                self.end_headers()
            return

        super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


def run(port=8125):
    os.chdir(BASIS)
    httpd = HTTPServer(('0.0.0.0', port), CustomHandler)
    staat = lees_staat()
    grootte = os.path.getsize(SCORES_BESTAND) / 1e6 if os.path.exists(SCORES_BESTAND) else 0
    print("======================================================", flush=True)
    print(f"🏫 Duru's School Server — poort {port}", flush=True)
    print(f"   scores.json: {len(staat)} sleutels · {grootte:.2f} MB", flush=True)
    print("======================================================", flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.", flush=True)


if __name__ == '__main__':
    port = 8125
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    run(port)
