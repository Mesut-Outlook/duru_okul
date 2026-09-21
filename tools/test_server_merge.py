#!/usr/bin/env python3
"""tools/test_server_merge.py — regressietest voor server.py -> voeg_samen()

Waarom dit bestaat: op 2026-09-20 overschreef de client-merger Duru's voortgang
in plaats van hem samen te voegen (865 XP en 5 medailles werden 95 XP en 1
medaille). server.py had DEZELFDE fout in tak 3: "laatste schrijver wint" voor
xp/badges/pogingen. Juist scores.json op schijf was de bron waaruit het herstel
kwam, dus die mag nooit kunnen krimpen.

De regel die deze test bewaakt: SAMENVOEGEN MAG GROEIEN, NOOIT KRIMPEN.

Gebruik:  python3 tools/test_server_merge.py
Exit 0 = alles goed, exit 1 = merger is kapot.
Zie CLAUDE.md -> "Bulut senkron & birlestirme degismezi" en
tools/test_score_merge.js voor de clientkant.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from server import voeg_samen  # noqa: E402

fail = 0


def ok(naam, gekregen, verwacht):
    global fail
    goed = gekregen == verwacht
    if not goed:
        fail += 1
        print('FAIL %s  beklenen=%r gelen=%r' % (naam, verwacht, gekregen))
    else:
        print('PASS %s' % naam)


# ── 1) voortgang: rijke oude staat, arme nieuwe POST ──
rijk = {'xp': 865, 'streak': 11, 'badges': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
        'beste': {'t1': 90}, 'gedaan': {'t1': True}, 'pogingen': {'t1': 7}, 'titels': {'t1': 'x'}}
arm = {'xp': 95, 'streak': 1, 'badges': {'a': 1},
       'beste': {'t1': 40}, 'gedaan': {}, 'pogingen': {'t1': 1}, 'titels': {}}

samen, vers = voeg_samen('duru_2627_natuurkunde_v1', rijk, arm)
ok('XP krimpt niet', samen['xp'], 865)
ok('streak krimpt niet', samen['streak'], 11)
ok('medailles krimpen niet', len(samen['badges']), 5)
ok('beste krimpt niet', samen['beste']['t1'], 90)
ok('pogingen krimpen niet', samen['pogingen']['t1'], 7)
ok('titels blijven', samen['titels'], {'t1': 'x'})

# ── 2) nieuwe waarde die WEL groter is, wordt overgenomen ──
samen, _ = voeg_samen('duru_2627_natuurkunde_v1', rijk,
                      {'xp': 1200, 'badges': {'z': 9}, 'pogingen': {'t1': 12}})
ok('hogere XP wordt overgenomen', samen['xp'], 1200)
ok('nieuwe medaille komt erbij', len(samen['badges']), 6)
ok('hogere pogingen overgenomen', samen['pogingen']['t1'], 12)

# ── 3) lege oude staat: nieuwe waarde blijft intact ──
samen, _ = voeg_samen('duru_2627_duits_v1', None, {'xp': 50, 'badges': {}})
ok('lege oude staat', samen['xp'], 50)

# ── 4) examens: history-union blijft werken (tak 2, niet aangeraakt) ──
oud_ex = {'history': [{'attemptId': 'att_1', 'examId': 'ex-1', 'pct': 80},
                      {'attemptId': 'att_2', 'examId': 'ex-2', 'pct': 60}]}
nieuw_ex = {'history': [{'attemptId': 'att_3', 'examId': 'ex-3', 'pct': 40}]}
samen, vers = voeg_samen('duru_2627_frans_examens_v1', oud_ex, nieuw_ex)
ok('history union', len(samen['history']), 3)
ok('nieuwe poging geteld', len(vers), 1)
ok('beste herberekend', samen['beste']['ex-1'], 80)

# ── 5) niet-voortgang (thema als string) blijft ongemoeid ──
samen, _ = voeg_samen('duru_hub_theme', 'light', 'dark')
ok('string-waarde ongemoeid', samen, 'dark')

# ── 6) dict die GEEN voortgang is, krijgt geen xp/badges aangeplakt ──
samen, _ = voeg_samen('iets_anders', {'a': 1}, {'b': 2})
ok('vreemde dict onaangeraakt', samen, {'b': 2})

print('\nTUM TESTLER GECTI' if fail == 0 else '\n%d TEST BASARISIZ' % fail)
sys.exit(1 if fail else 0)
