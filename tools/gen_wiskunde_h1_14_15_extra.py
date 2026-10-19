"""Wiskunde H1: 5 extra proeftoetsen §1.4 (lineair of exponentieel) + 5 extra §1.5 (groeifactor en tijd).
ex-wiskunde-h1-51…60 = examen_74…83. Hergebruikt de vraagbouwers van gen_wiskunde_h1_paragraaf_exams.py
en voegt nieuwe types toe (lineair vs exponentieel, twee stappen terug, formule uit twee punten,
"wanneer voor het eerst", procent per periode). Antwoorden berekend, ontdubbeld tegen alle bestaande vragen.
Gebruik: python3 tools/gen_wiskunde_h1_14_15_extra.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: inhoud van een gemaakte toets mag niet veranderen."""
import json, random, sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(__file__))
import gen_wiskunde_h1_paragraaf_exams as G
from gen_wiskunde_h1_paragraaf_exams import MC, WO, IN, OP, fmt, macht, keuze, svg_tabel, num_ans, exp_rij, CTX, SUP

def kort(x): return fmt(F(str(round(x, 4))))  # 0.96 → '0,96', 1.04 → '1,04' (geen nullen achteraan)

# ================= §1.4 lineair of exponentieel =================
LIN_TXT = "lineaire groei: er komt steeds hetzelfde getal bij"
EXP_TXT = "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
GEEN_TXT = "geen van beide"
BEIDE_TXT = "zowel lineaire als exponentiële groei"

def lin_rij(rng, n=5):
    s = F(rng.randint(20, 400)); d = F(rng.choice([3, 4, 6, 8, 12, 15, 25, -3, -4, -6, -5]))
    if s + d * (n - 1) <= 0: d = -d
    return s, d, [s + d * i for i in range(n)]

def q14_linexp(rng):
    soort = rng.choice(["lin", "exp", "exp", "geen", "lin"])
    if soort == "lin": _, d, rij = lin_rij(rng)
    elif soort == "exp": _, g, rij = exp_rij(rng)
    else:
        s = rng.randint(10, 60); c = rng.choice([2, 3, 5]); rij = [F(s + c * i * i) for i in range(5)]
    goed = {"lin": LIN_TXT, "exp": EXP_TXT, "geen": GEEN_TXT}[soort]
    uitleg = {"lin": f"Er komt steeds {fmt(rij[1] - rij[0])} bij, dus lineair. De factoren ({fmt(rij[1] / rij[0], 3)}, {fmt(rij[2] / rij[1], 3)}) zijn niet gelijk.",
              "exp": f"De factor is steeds {fmt(rij[1] / rij[0])} ({fmt(rij[1])} : {fmt(rij[0])}), dus exponentieel. De verschillen zijn niet gelijk.",
              "geen": f"De verschillen ({fmt(rij[1] - rij[0])}, {fmt(rij[2] - rij[1])}, {fmt(rij[3] - rij[2])}) zijn niet gelijk en de factoren ({fmt(rij[1] / rij[0], 3)}, {fmt(rij[2] / rij[1], 3)}) ook niet."}[soort]
    return MC(f"De tabel geeft {keuze(rng, CTX)} op t = 0, 1, 2, 3, 4: {', '.join(fmt(x) for x in rij)}. Welk soort groei hoort bij de tabel?", goed,
              [LIN_TXT, EXP_TXT, GEEN_TXT, BEIDE_TXT], uitleg,
              svg_tabel([["t", "0", "1", "2", "3", "4"], ["A"] + [fmt(x) for x in rij]]))

def q14_ontbrekend(rng, soort):
    if soort == "L":
        _, d, rij = lin_rij(rng, 6)
        uit = f"Lineair: er komt steeds {fmt(d)} bij. {fmt(rij[4])} {'+' if d > 0 else '−'} {fmt(abs(d))} = {fmt(rij[5])}."
    else:
        _, g, rij = exp_rij(rng, n=6)
        uit = f"Exponentieel: groeifactor {fmt(rij[1])} : {fmt(rij[0])} = {fmt(g)}. {fmt(rij[4])} · {fmt(g)} = {fmt(rij[5])}."
    fig = svg_tabel([["t", "0", "1", "2", "3", "4", "5"], ["N"] + [fmt(x) for x in rij[:5]] + ["…"]])
    return IN(f"De tabel ({fmt(rij[0])}, {fmt(rij[1])}, {fmt(rij[2])}, …) hoort bij {'lineaire' if soort == 'L' else 'exponentiële'} groei. Welk getal hoort op t = 5?",
              num_ans(rij[5]), uit, fig)

def q14_contextformule(rng):
    b = rng.choice([800, 1200, 2500, 5000, 640, 15000]); wat = keuze(rng, ["leden van een sportclub", "volgers van een vlog", "inwoners van een dorp", "bezoekers van een museum", "abonnees van een krant"])
    if rng.random() < 0.5:
        d = rng.choice([40, 50, 120, 250, 300]); af = rng.random() < 0.4
        goed = f"A = {fmt(b, dui=True)} {'−' if af else '+'} {d}t"
        fout = [f"A = {fmt(b, dui=True)} · {macht(d)}", f"A = {d} {'−' if af else '+'} {fmt(b, dui=True)}t", f"A = {fmt(b, dui=True)} · {macht(F(100 + (-d if af else d), 100) if d < 100 else F(d, 100))}"]
        tekst = f"Het aantal {wat} is nu {fmt(b, dui=True)} en neemt elk jaar met {d} {'af' if af else 'toe'}."
        uit = f"Er gaat elk jaar hetzelfde aantal ({d}) {'af' if af else 'bij'}: lineair, A = begin {'−' if af else '+'} {d}t."
    else:
        p = rng.choice([4, 5, 6, 8, 12, 15]); af = rng.random() < 0.4; g = F(100 + (-p if af else p), 100)
        goed = f"A = {fmt(b, dui=True)} · {macht(g)}"
        fout = [f"A = {fmt(b, dui=True)} {'−' if af else '+'} {p}t", f"A = {fmt(b, dui=True)} · {macht(F(p, 100))}", f"A = {fmt(b, dui=True)} · {macht(F(100 + (p if af else -p), 100))}"]
        tekst = f"Het aantal {wat} is nu {fmt(b, dui=True)} en neemt elk jaar met {p}% {'af' if af else 'toe'}."
        uit = f"Elk jaar een vast percentage: exponentieel met groeifactor {fmt(g)} ({100 + (-p if af else p)}%). A = begin · {macht(g)}."
    return MC(f"{tekst} Welke formule hoort bij het aantal A na t jaar?", goed, fout, uit)

def q14_terug2(rng):
    g = F(rng.choice(["0.85", "0.8", "0.9", "1.2", "1.25", "0.75", "1.1"])); N = rng.choice([1200, 1500, 2400, 3000, 960, 4800, 6000])
    u = rng.choice([5, 6, 8, 10, 14]); w = F(N) / g ** 2
    return IN(f"Het aantal vliegjes in een kas verandert exponentieel met groeifactor {fmt(g)} per uur. Om {u:02d}.00 uur zijn er {fmt(N, dui=True)} vliegjes. Hoeveel waren er om {u - 2:02d}.00 uur? Rond af op een geheel getal.",
              str(round(w)), f"Twee uur terug: twee keer delen door {fmt(g)}, dus {fmt(N, dui=True)} : {macht(g, 2)} ≈ {fmt(w, 1)} → {round(w)}.", tol=1)

def q14_procent_terug(rng):
    p = rng.choice([4, 5, 8, 10, 12, 20]); af = rng.random() < 0.7; N = rng.choice([180, 460, 1250, 2300, 736, 5520]); j = rng.choice([2021, 2022, 2023, 2024])
    g = F(100 + (-p if af else p), 100); w = F(N) / g
    wat = keuze(rng, ["fietsdiefstallen", "woninginbraken", "verkeersongelukken", "klachten bij een bedrijf", "verkochte cd's"])
    return IN(f"Het aantal {wat} in een stad neemt al jaren met {p}% per jaar {'af' if af else 'toe'}. In {j} waren het er {N}. Hoeveel waren het er in {j - 1}? Rond af op een geheel getal.",
              str(round(w)), f"Groeifactor {fmt(g)}. Een jaar terug: delen, {N} : {fmt(g)} ≈ {fmt(w, 1)} → {round(w)}. (Niet {N} · {fmt(1 + F(p, 100) if af else 1 - F(p, 100))}!)", tol=1)

def q14_wolin(rng, waar):
    if waar:
        k = rng.choice([
            lambda: (f"In een tabel wordt elke waarde {fmt(g := F(rng.choice(['1.5', '2', '3', '0.8', '1.25', '0.6'])))} keer zo groot als de vorige. Dan hoort de tabel bij exponentiële groei met groeifactor {fmt(g)}.", "Steeds met hetzelfde getal vermenigvuldigen = exponentieel."),
            lambda: (f"In een tabel komt er steeds {rng.choice([7, 12, 35, 140, 9])} bij. Dan hoort de tabel bij lineaire groei.", "Steeds hetzelfde getal erbij = lineair."),
            lambda: (f"Een bedrag neemt elk jaar met {rng.choice([3, 6, 9, 11])}% toe. Dan is er sprake van exponentiële groei.", "Een vast percentage per jaar geeft een vaste groeifactor, dus exponentieel."),
        ])
    else:
        k = rng.choice([
            lambda: (f"In een tabel komt er steeds {rng.choice([7, 12, 35, 140, 9])} bij. Dan hoort de tabel bij exponentiële groei.", "Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."),
            lambda: (f"Een bedrag neemt elk jaar met {(e := rng.choice([150, 40, 75, 220]))} euro toe. Dan is er sprake van exponentiële groei.", f"Elk jaar hetzelfde bedrag ({e} euro) erbij is lineair."),
            lambda: (f"De tabel t = 0, 1, 2 met waarden {(s := rng.choice([100, 200, 50]))}, {s * 2}, {s * 3} hoort bij exponentiële groei met groeifactor 2.", f"Er komt steeds {s} bij (lineair); de factoren zijn 2 en 1,5, niet gelijk."),
        ])
    v, u = k()
    return WO(v, waar, u)

def q14_vergelijk(rng):
    while True:
        b = rng.choice([1000, 2000, 500, 5000]); g = rng.choice([1.05, 1.08, 1.1, 1.12, 1.06]); d = round(b * rng.choice([0.08, 0.1, 0.12, 0.15]))
        t = next(t for t in range(1, 60) if b * g ** t > b + d * t)
        marge = (b * g ** t) / (b + d * t) - 1
        if 3 <= t <= 12 and marge > 0.004 and 1 - (b * g ** (t - 1)) / (b + d * (t - 1)) > 0.004: break
    return IN(f"Opa zet € {fmt(b, dui=True)} op spaarrekening A en € {fmt(b, dui=True)} op spaarrekening B. Bij A komt er elk jaar € {d} bij. Bij B groeit het bedrag elk jaar met {fmt((g - 1) * 100, 0)}% (groeifactor {fmt(g, 2)}). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
              str(t), f"Maak een tabel. A = {b} + {d}t, B = {b} · {fmt(g, 2)}ᵗ. Na {t - 1} jaar: A = {fmt(b + d * (t - 1), 0)}, B ≈ {fmt(b * g ** (t - 1), 0)}; na {t} jaar: A = {fmt(b + d * t, 0)}, B ≈ {fmt(b * g ** t, 0)}. Dus na {t} jaar.")

TWEE = [(F(3, 4), 160), (F(3, 2), 64), (F(2), 15), (F(5, 4), 256), (F(4, 5), 625), (F(1, 2), 360), (F(3, 4), 320), (F(3, 2), 40), (F(5, 4), 128)]
def q14_twee_punten(rng, wat):
    g, b = keuze(rng, TWEE)
    x1 = rng.choice([1, 2, 3]); y2, y3 = b * g ** x1, b * g ** (x1 + 1)
    vraag = f"De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten ({x1}; {fmt(y2)}) en ({x1 + 1}; {fmt(y3)}). "
    if wat == "g":
        return IN(vraag + "Bereken de groeifactor g.", num_ans(g), f"Van t = {x1} naar t = {x1 + 1} is één stap: g = {fmt(y3)} : {fmt(y2)} = {fmt(g)}.", tol=0.0005)
    return IN(vraag + "Bereken de beginwaarde b (de waarde op t = 0).", num_ans(b),
              f"g = {fmt(y3)} : {fmt(y2)} = {fmt(g)}. Terug naar t = 0 is {x1} stap{'pen' if x1 > 1 else ''}: b = {fmt(y2)} : {macht(g, x1)} = {fmt(b)}.", tol=0.5)

P14X = ["linexp", "ontbrekend:L", "ontbrekend:E", "contextformule", "wolin:T", "terug2", "factor", "linexp", "procent_terug", "wolin:F",
        "twee_punten:g", "contextformule", "isexp:F", "welke", "vergelijk", "twee_punten:b", "wolin:F", "t0", "linexp", "open"]

# ================= §1.5 groeifactor en tijd =================
def q15_procent_periode(rng):
    p = rng.choice([1.5, 1.8, 2, 2.5, 3, 4, 6]); n = rng.choice([10, 20, 25, 50, 100])
    w = ((1 + p / 100) ** n - 1) * 100
    return IN(f"Een bevolking groeit met {fmt(p, 1 if p % 1 else None)}% per jaar. Met hoeveel procent groeit de bevolking in {n} jaar? Rond af op één decimaal.",
              fmt(w, 1).replace('−', '-'), f"Groeifactor per jaar {kort(1 + p / 100)}. Per {n} jaar: {kort(1 + p / 100)}{str(n).translate(SUP)} ≈ {fmt((1 + p / 100) ** n, 3)}, dus ongeveer {fmt(w, 1)}% groei (niet {kort(p * n)}%).", tol=0.15)

def q15_eerst(rng):
    while True:
        b = rng.choice([2.5, 4, 12, 800, 2400]); p = rng.choice([1.8, 3, 4, 6, 8, 10, 15, 20]); af = rng.random() < 0.35
        g = 1 - p / 100 if af else 1 + p / 100
        doel = b * (0.5 if af else rng.choice([1.5, 2, 3]))
        t = next(t for t in range(1, 500) if (b * g ** t < doel if af else b * g ** t > doel))
        if t <= 40 and abs(b * g ** t / doel - 1) > 0.003 and abs(b * g ** (t - 1) / doel - 1) > 0.003: break
    eenh = "miljoen mensen" if b < 20 else "dieren"
    return IN(f"In een gebied leven {fmt(b, 1 if b % 1 else None)} {eenh}. Dat aantal neemt elk jaar met {fmt(p, 1 if p % 1 else None)}% {'af' if af else 'toe'}. Na hoeveel hele jaren is het aantal voor het eerst {'minder dan de helft' if af else 'meer dan ' + fmt(doel) + ' ' + eenh}?",
              str(t), f"Groeifactor {kort(g)}. Probeer t: na {t - 1} jaar {fmt(b * g ** (t - 1), d := 2 if b < 20 else 0)}, na {t} jaar {fmt(b * g ** t, d)} (grens {fmt(doel)}). Dus na {t} jaar.")

def q15_kwart(rng, waar):
    while True:
        g = rng.choice([0.917, 0.93, 0.95, 0.9, 0.88, 0.96, 0.85]); n = rng.choice([2, 3, 4, 5, 6])
        P = 100 * g ** n
        if (P < 75) == waar and abs(P - 75) > 1: break
    return WO(f"Van een medicijn is na t dagen nog P = 100 · {kort(g)}ᵗ procent werkzaam. Na {n} dagen is er al meer dan een kwart van het medicijn verdwenen.", waar,
              f"P = 100 · {kort(g)}{str(n).translate(SUP)} ≈ {fmt(P, 1)}%. Er is dus {fmt(100 - P, 1)}% verdwenen, {'meer' if waar else 'minder'} dan een kwart (25%).")

def q15_per_n(rng):
    g = rng.choice([0.917, 0.93, 1.6, 1.15, 0.85, 1.07, 0.96]); n = rng.choice([2, 3, 4, 6])
    eenh = keuze(rng, [("dagen", "dag"), ("jaren", "jaar"), ("weken", "week")])
    w = g ** n
    return IN(f"Gegeven is P = 100 · {kort(g)}ᵗ met t in {eenh[0]}. Bereken de groeifactor per {n} {'jaar' if eenh[0] == 'jaren' else eenh[0]}. Rond af op drie decimalen.",
              fmt(w, 3).replace('−', '-'), f"{n} {'jaar' if eenh[0] == 'jaren' else eenh[0]} = {n} stappen: {kort(g)}{str(n).translate(SUP)} ≈ {fmt(w, 3)}.", tol=0.0015)

MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
def q15_terug_maand(rng):
    g = rng.choice([1.025, 1.04, 1.015, 1.06, 1.03]); N = rng.choice([254200, 182000, 96500, 412000, 75800]); k = rng.choice([3, 4, 5, 6, 9])
    m = rng.choice([9, 10, 11]); w = N / g ** k
    return IN(f"Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor {kort(g)} per maand. Op 1 {MAANDEN[m]} waren er in totaal {fmt(N, dui=True)} partijen gespeeld. Hoeveel waren dat er op 1 {MAANDEN[m - k]}? Rond af op een geheel getal.",
              str(round(w)), f"1 {MAANDEN[m - k]} is {k} maanden eerder. Delen door de groeifactor per {k} maanden: {fmt(N, dui=True)} : {kort(g)}{str(k).translate(SUP)} ≈ {fmt(round(w), dui=True)}.", tol=max(1, round(w) // 2000))

def q15_formule_lang(rng):
    b = rng.choice([112000, 5000, 840, 25000]); g = rng.choice([0.95, 1.04, 1.08, 0.92, 1.03]); n = rng.choice([2, 5, 10])
    w = g ** n
    goed = f"N = {fmt(b, dui=True)} · {fmt(w, 3)}ᵗ"
    return MC(f"Het aantal bezoekers is N = {fmt(b, dui=True)} · {fmt(g, 2)}ᵗ met t in jaren. Welke formule hoort bij t in perioden van {n} jaar? (groeifactor in drie decimalen)", goed,
              [f"N = {fmt(b, dui=True)} · {fmt(1 + n * (g - 1), 3)}ᵗ", f"N = {fmt(b * n, dui=True)} · {fmt(g, 2)}ᵗ", f"N = {fmt(b, dui=True)} · {fmt(g ** (1 / n), 3)}ᵗ"],
              f"Per {n} jaar: {fmt(g, 2)}{str(n).translate(SUP)} ≈ {fmt(w, 3)}. De beginwaarde {fmt(b, dui=True)} blijft hetzelfde.")

def q15_park(rng):
    g = rng.choice([0.95, 0.97, 1.04, 0.93, 1.06]); B = rng.choice([112000, 86000, 240000, 54000]); n = rng.choice([5, 10]); vooruit = rng.random() < 0.5
    w = B * g ** n if vooruit else B / g ** n
    return IN(f"Het aantal bezoekers van een attractiepark verandert al jaren exponentieel met groeifactor {fmt(g, 2)} per jaar. In 2020 kwamen er {fmt(B, dui=True)} bezoekers. Bereken het aantal bezoekers in {2020 + n if vooruit else 2020 - n}. Rond af op een geheel getal.",
              str(round(w)), f"Groeifactor per {n} jaar: {fmt(g, 2)}{str(n).translate(SUP)} ≈ {fmt(g ** n, 4)}. {'Vooruit: vermenigvuldigen' if vooruit else 'Terug: delen'}: {fmt(B, dui=True)} {'·' if vooruit else ':'} {fmt(g ** n, 4)} ≈ {fmt(round(w), dui=True)}.", tol=max(2, round(w) // 1000))

P15X = ["procent_periode", "per_n", "kwadraat", "terug_maand", "kwart:T", "formule_lang", "macht", "eerst", "park", "kwart:F",
        "waarde", "jaar", "procent_periode", "lex:F", "terug", "sneller", "per_n", "eerst", "park", "open"]

PARAS = [("1.4", "Lineair of exponentieel", "q14", P14X), ("1.5", "Groeifactor en tijd", "q15", P15X)]

def bouw(slot, prefix, rng):
    naam, _, arg = slot.partition(':')
    fn = globals().get(f"{prefix}_{naam}") or getattr(G, f"{prefix}_{naam}")
    if not arg: return fn(rng)
    return fn(rng, arg == "T") if arg in "TF" else fn(rng, arg)

if __name__ == "__main__":
    OUT = sys.argv[1]
    GEZIEN = set(json.load(open(sys.argv[2])))
    nr = 74; fid = 51
    for pi, (par, ptitel, prefix, plan) in enumerate(PARAS):
        for k in range(5):
            rng = random.Random(7000 + 100 * pi + k * 13)
            vragen = []
            for slot in plan:
                for _ in range(300):
                    v = bouw(slot, prefix, rng)
                    if v["vraag"] not in GEZIEN: break
                else:
                    raise SystemExit(f"geen unieke vraag voor {slot}")
                GEZIEN.add(v["vraag"]); vragen.append(v)
            mcs = [v for v in vragen if v["type"] == "mc"]
            pos = iter(G.mc_volgorde(rng, len(mcs)))
            for v in mcs:
                opts = v.pop("_opts"); goed = opts[0]; rest = opts[1:]; rng.shuffle(rest)
                i = next(pos); rest.insert(i, goed)
                v["opties"] = rest; v["antwoord"] = i
            for v in vragen:
                if v["type"] == "invul": assert v["antwoord"], v
            ex = {"id": f"ex-wiskunde-h1-{fid}", "hoofdstuk": 1, "paragraaf": par,
                  "titel": f"Proeftoets {nr} — §{par} {ptitel} (extra {k + 1}/5, {G.NIVEAU[k]})",
                  "vak": "Wiskunde · H1 Lineaire en exponentiële formules", "icoon": "📈", "duurMin": 30, "vragen": vragen}
            with open(f"{OUT}/examen_{nr}.js", "w") as f:
                f.write("/* =========================================================\n"
                        f"   Duru's Wiskunde (HAVO 3) — {ex['titel']}\n"
                        f"   Bron: Noordhoff H1 Lineaire en exponentiële formules, §{par} (opgaven uit het boek met andere getallen;\n"
                        "   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)\n"
                        "   ========================================================= */\n")
                f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
            nr += 1; fid += 1
    print("geschreven: examen_74 … examen_83")
