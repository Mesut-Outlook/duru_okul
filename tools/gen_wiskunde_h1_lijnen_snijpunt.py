"""Wiskunde H1: Lijnentoets (2×) en Snijpunttoets (2×) in het format van het Duru_Matematik-project
(ex-wiskunde-h1-45…50, examen_55…60). Elke opgave = één figuur (rooster −6…6) met lijnen door twee stippen.
- Lijnentoets: 10 opgaven × (hellingsgetal a, startgetal b) = 20 vragen; 4 basis (hele a), 4 breuken, 2 uitdaging
  (b niet op het rooster → invullen). Minstens de helft dalend: Duru vergeet het minteken.
- Snijpunttoets: 10 opgaven × (formule l, formule m, x en y van S), gesplitst in a (1–5) en b (6–10) van elk 20 vragen
  (gate: proeftoets = 20); l rood, m blauw. T1 hele hellingen (1–7 S op roosterpunt, één horizontale lijn; 8–10 S tussen
  roosterpunten), T2 breuken (1–5 S op roosterpunt / 6–10 S met breuken).
Breuken mogen als antwoord (exams.js leest 3/2 als 1,5); niet-afbrekende waarden krijgen sleutel "2/3|0,67".
Gebruik: python3 tools/gen_wiskunde_h1_lijnen_snijpunt.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, math, os, random, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_wiskunde_h1_paragraaf_exams import fmt, lin, expr, hk, pt, svg_graph, MC, IN, num_ans, mc_volgorde

R = 6  # rooster −R…R
ROOD, BLAUW = "#dc2626", "#2563eb"
BREUK = " (Een breuk mag, bijvoorbeeld 3/2 of −3/4.)"

def sleutel(x):
    return num_ans(x) or f"{x.numerator}/{x.denominator}|{fmt(x, 2).replace('−', '-')}"

def lijn(rng, a_ok, b_ok, verboden=()):
    """Twee roosterpunten P, Q (|Δx| ≥ 2) → (a, b, P, Q) met a_ok(a) en b_ok(b)."""
    for _ in range(20000):
        P = (F(rng.randint(-R + 1, R - 1)), F(rng.randint(-R + 1, R - 1)))
        Q = (F(rng.randint(-R + 1, R - 1)), F(rng.randint(-R + 1, R - 1)))
        if Q[0] - P[0] < 2 or P in verboden or Q in verboden: continue
        a = (Q[1] - P[1]) / (Q[0] - P[0]); b = P[1] - a * P[0]
        if a_ok(a) and b_ok(b): return a, b, P, Q
    raise RuntimeError("geen lijn")

def figuur(lijnen, punten):
    return svg_graph(-R, R, -R, R, eenheid=24, lijnen=[(float(a), float(b), n) for a, b, n in lijnen],
                     punten=[(float(x), float(y), "") for x, y in punten], kleuren=[ROOD, BLAUW])

def rc_uitleg(a, P, Q):
    return (f"Δy ÷ Δx = ({fmt(Q[1])} − {hk(P[1])}) ÷ ({fmt(Q[0])} − {hk(P[0])}) = {fmt(Q[1] - P[1])} ÷ {fmt(Q[0] - P[0])} = {fmt(a)}."
            + (" De lijn daalt, dus a is negatief." if a < 0 else " De lijn stijgt, dus a is positief." if a > 0 else " De lijn is horizontaal, dus a = 0."))

def b_uitleg(a, b, P):
    return f"Invullen van {pt(*P)} in y = {fmt(a)}x + b: {fmt(P[1])} = {fmt(a)} · {hk(P[0])} + b = {fmt(a * P[0])} + b, dus b = {fmt(P[1])} − {hk(a * P[0])} = {fmt(b)}."

# ---------- Lijnentoets ----------
NIVEAUS = ["basis"] * 4 + ["breuken"] * 4 + ["uitdaging"] * 2

def lijnen_opgave(rng, niveau, dalend):
    teken = (lambda a: a < 0) if dalend else (lambda a: a > 0)
    if niveau == "basis":
        a_ok = lambda a: teken(a) and a.denominator == 1 and abs(a) <= 3; b_ok = lambda b: b.denominator == 1 and abs(b) <= 5
    elif niveau == "breuken":
        a_ok = lambda a: teken(a) and a.denominator in (2, 3, 4) and abs(a) <= 3; b_ok = lambda b: b.denominator == 1 and abs(b) <= 5
    else:
        a_ok = lambda a: teken(a) and a.denominator in (1, 2, 3, 4) and abs(a) <= 3; b_ok = lambda b: b.denominator != 1 and abs(b) <= 5
    a, b, P, Q = lijn(rng, a_ok, b_ok)
    f = figuur([(a, b, "l")], [P, Q])
    stip = f"Lijn l gaat door de stippen {pt(*P)} en {pt(*Q)}."
    bvr = (" Het snijpunt met de y-as ligt níet op een roosterpunt: bereken b door een punt in te vullen." if niveau == "uitdaging"
           else " Lees b af of bereken het door een punt in te vullen.")
    b_eerst = f"De lijn snijdt de y-as in (0, {fmt(b)}). " if b.denominator == 1 else ""
    return [IN(f"{stip} De formule is y = ax + b. Bereken het hellingsgetal a." + (BREUK if a.denominator != 1 else ""), sleutel(a), rc_uitleg(a, P, Q), f),
            IN(f"{stip} Het hellingsgetal is a = {fmt(a)}. Wat is het startgetal b?{bvr}" + (BREUK if b.denominator != 1 else ""), sleutel(b), b_eerst + b_uitleg(a, b, P), f)]

# ---------- Snijpunttoets ----------
HEEL = [F(a) for a in (-3, -2, -1, 1, 2, 3)]
BREUKEN = [F(p, q) * t for q in (2, 3, 4) for p in range(1, 3 * q) if math.gcd(p, q) == 1 for t in (1, -1)]

def roosterpunten(rng, a, b, verboden):
    """Twee roosterpunten op y = ax + b binnen het rooster, |Δx| ≥ 2, niet in verboden."""
    ps = [(F(x), a * x + b) for x in range(-R + 1, R) if (a * x + b).denominator == 1 and abs(a * x + b) < R]
    ps = [p for p in ps if p not in verboden]
    paren = [(P, Q) for P in ps for Q in ps if Q[0] - P[0] >= 2]
    return rng.choice(paren) if paren else None

def snij_opgave(rng, toets, k):
    heel = toets == 1
    S_rooster = k < (7 if heel else 5)
    for _ in range(200000):
        if heel:
            a1 = rng.choice(HEEL); a2 = F(0) if k == 2 else rng.choice(HEEL)
        else:
            a1 = rng.choice(HEEL + BREUKEN); a2 = rng.choice(BREUKEN)
        b1, b2 = F(rng.randint(-5, 5)), F(rng.randint(-5, 5))
        if a1 == a2: continue
        hoek = abs(math.degrees(math.atan(float(a1)) - math.atan(float(a2))))
        if min(hoek, 180 - hoek) < 25: continue  # geen bijna-evenwijdige lijnen
        x0 = (b2 - b1) / (a1 - a2); y0 = a1 * x0 + b1
        if abs(x0) > R - 1 or abs(y0) > R - 1: continue
        if S_rooster != (x0.denominator == 1 and y0.denominator == 1): continue
        if not S_rooster and (x0.denominator > 4 or y0.denominator > 4 or x0.denominator == 1): continue
        pl = roosterpunten(rng, a1, b1, {(x0, y0)})
        pm = pl and roosterpunten(rng, a2, b2, {(x0, y0), *pl})
        if pm: break
    else: raise RuntimeError("geen paar")
    L, M = (a1, b1, *pl), (a2, b2, *pm)
    S = (x0, y0)
    f = figuur([(a1, b1, "l"), (a2, b2, "m")], [L[2], L[3], M[2], M[3]])
    kop = f"Lijn l (rood) gaat door {pt(*L[2])} en {pt(*L[3])}, lijn m (blauw) door {pt(*M[2])} en {pt(*M[3])}."

    def formule_mc(n, a, b, P, Q):
        fout = [lin(-a, b), lin(a, -b), lin(a, P[1] + a * P[0])]
        if a != 0 and 1 / a != a: fout.insert(1, lin(1 / a, b))
        fout += [lin(a, b + 1), lin(a, b - 1), lin(-a, -b)]
        return MC(f"{kop} Welke formule hoort bij lijn {n}?", lin(a, b), fout, rc_uitleg(a, P, Q) + " " + b_uitleg(a, b, P) + f" Formule: {lin(a, b)}.", f)

    stappen = (f"l: {lin(a1, b1)}, m: {lin(a2, b2)}. Gelijkstellen: {expr(a1, b1)} = {expr(a2, b2)} → "
               f"{fmt(a1 - a2)}x = {fmt(b2 - b1)} → x = {fmt(b2 - b1)} ÷ {hk(a1 - a2)} = {fmt(x0)}. Invullen in l: y = {fmt(a1)} · {hk(x0)} + {hk(b1)} = {fmt(y0)}. S{pt(*S)}.")
    return [formule_mc("l", a1, b1, L[2], L[3]), formule_mc("m", a2, b2, M[2], M[3]),
            IN(f"{kop} Bereken de x-coördinaat van het snijpunt S van l en m." + (BREUK if x0.denominator != 1 else ""), sleutel(x0), stappen, f),
            IN(f"{kop} Bereken de y-coördinaat van het snijpunt S van l en m." + (BREUK if y0.denominator != 1 else ""), sleutel(y0), stappen, f)]

TOETSEN = [  # (titel, paragraaf, maker, duurMin)
    ("Lijnentoets 1 — formule y = ax + b uit de grafiek", "1.1", lambda rng: [v for k, n in enumerate(NIVEAUS) for v in lijnen_opgave(rng, n, k % 2 == 0)], 25),
    ("Lijnentoets 2 — formule y = ax + b uit de grafiek", "1.1", lambda rng: [v for k, n in enumerate(NIVEAUS) for v in lijnen_opgave(rng, n, k % 2 == 1 or k == 8)], 25),
    ("Snijpunttoets 1a — twee lijnen en hun snijpunt (hele hellingen, S op het rooster)", "1.2", lambda rng: [v for k in range(5) for v in snij_opgave(rng, 1, k)], 25),
    ("Snijpunttoets 1b — twee lijnen en hun snijpunt (hele hellingen, S ook tussen roosterpunten)", "1.2", lambda rng: [v for k in range(5, 10) for v in snij_opgave(rng, 1, k)], 25),
    ("Snijpunttoets 2a — twee lijnen en hun snijpunt (breuken, S op het rooster)", "1.2", lambda rng: [v for k in range(5) for v in snij_opgave(rng, 2, k)], 25),
    ("Snijpunttoets 2b — twee lijnen en hun snijpunt (breuken, S met breuken)", "1.2", lambda rng: [v for k in range(5, 10) for v in snij_opgave(rng, 2, k)], 25),
]

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for i, (naam, par, maak, duur) in enumerate(TOETSEN):
        nr = 55 + i; fid = 45 + i; rng = random.Random(5500 + i * 37)
        vragen = maak(rng)
        for v in vragen:
            assert norm(v["vraag"]) not in GEZIEN, v["vraag"]; GEZIEN.add(norm(v["vraag"]))
        mcs = [v for v in vragen if v["type"] == "mc"]; pos = iter(mc_volgorde(rng, len(mcs)) if mcs else [])
        for v in mcs:
            o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
        titel = f"Proeftoets {nr} — {naam}"
        ex = {"id": f"ex-wiskunde-h1-{fid}", "hoofdstuk": 1, "paragraaf": par, "titel": titel,
              "vak": "Wiskunde · H1 Lineaire en exponentiële formules", "icoon": "📈", "duurMin": duur, "vragen": vragen}
        with open(f"{OUT}/examen_{nr}.js", "w") as fh:
            fh.write("/* =========================================================\n"
                     f"   Duru's Wiskunde (HAVO 3) — {titel}\n"
                     "   Format uit het Duru_Matematik-project (elke opgave een rooster −6…6 met stippen; breuken toegestaan)\n"
                     "   Gegenereerd met tools/gen_wiskunde_h1_lijnen_snijpunt.py\n"
                     "   ========================================================= */\n")
            fh.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: 55 … 60")
