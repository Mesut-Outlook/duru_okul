"""Wiskunde H1 §1.1–§1.5: 5 'foutentraining'-proeftoetsen (ex-wiskunde-h1-40…44, examen_50…54).
Gebouwd op Duru's eigen fouten (cloud-data 2026-10-11, 144 fout/deels in H1):
  §1.1 formule door twee punten leeg gelaten, min-teken in de noemer, begrippen (oorsprong, eerste coördinaat)
  §1.2 snijpunt: x goed, daarna y = x geschreven ("(9, 9)" i.p.v. "(9, 15)"); snijden met y = c; stappen beschrijven
  §1.3 substitueren zonder haakjes (6(x + 3) → 6x + 3), negatieve getallen, "waarom haakjes?"
  §1.4 afname → 0,97 (niet 1,03), een uur eerder = delen, tabel controleren met quotiënten
  §1.5 groeifactor per 2 weken = g² (zij: 2·g), per uur uit 20 min = g³, jaren → maanden, terugrekenen = delen
  overal: groeifactor zonder komma getypt ("1021" i.p.v. 1,021)
Toets 1 heeft tips, toets 5 niet; toets 1–3 herinneren aan de komma.
Gebruik: python3 tools/gen_wiskunde_h1_foutentraining.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, os, random, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_wiskunde_h1_paragraaf_exams as G
from gen_wiskunde_h1_paragraaf_exams import fmt, lin, expr, pt, hk, term, MC, WO, IN, OP, num_ans, sleutel_term, sleutel_const, mc_volgorde, keuze, macht

# ---------- §1.1 ----------
def f11_noemer_fout(rng):
    while True:
        a = F(rng.choice([2, 3, -2, -3, 4])); x1 = -rng.randint(1, 4); x2 = rng.randint(2, 6); b = F(rng.randint(-6, 9))
        y1, y2 = a * x1 + b, a * x2 + b
        fout_n = x2 + x1   # leerling: x2 − |x1|
        if fout_n not in (0, x2 - x1) and (y2 - y1) % fout_n == 0: break
    X, Y = keuze(rng, [("X", "Y"), ("P", "Q"), ("A", "B")])
    return MC(f"Lijn l gaat door {X}{pt(x1, y1)} en {Y}{pt(x2, y2)}. Een leerling rekent: a = ({fmt(y2)} − {hk(y1)}) / ({x2} − {abs(x1)}) = {fmt(y2 - y1)} / {fout_n} = {fmt(F(y2 - y1, fout_n))}. Wat is er fout?",
              f"In de noemer moet {x2} − ({fmt(x1)}) = {x2 - x1} staan, dus a = {fmt(y2 - y1)} / {x2 - x1} = {fmt(a)}.",
              [f"Je moet toename x delen door toename y, dus a = {x2 - x1} / {fmt(y2 - y1)}.",
               f"In de teller moet {fmt(y1)} − {hk(y2)} staan.",
               "Er is niets fout: de berekening klopt.",
               f"Je moet de x-coördinaten optellen: a = {fmt(y2 - y1)} / {x2 + abs(x1)}."],
              f"Min een negatief getal is plus: {x2} − ({fmt(x1)}) = {x2} + {abs(x1)} = {x2 - x1}. Dus a = {fmt(y2 - y1)} / {x2 - x1} = {fmt(a)}. Let op: zet een negatieve coördinaat tussen haakjes.")

BEGRIPPEN = [
    lambda: MC("Hoe heet het punt (0, 0), waar de x-as en de y-as elkaar snijden?", "de oorsprong",
               ["het startgetal", "het snijpunt met de x-as", "het nulpunt van de lijn"],
               "Het punt (0, 0) heet de oorsprong. 'Snijpunt' is te algemeen: twee lijnen kunnen elkaar overal snijden."),
    lambda: MC("Wat is de eerste coördinaat van het punt (7, −4)?", "7 (de x-coördinaat)",
               ["−4 (de y-coördinaat)", "7 (de y-coördinaat)", "−4 (de x-coördinaat)"],
               "Bij (x, y) staat eerst x en dan y. De eerste coördinaat is de x-coördinaat: 7."),
    lambda: MC("De lijnen y = 3x + 2 en y = −x + 2 hebben hetzelfde startgetal. Wat weet je dan?", "ze snijden elkaar op de y-as, in (0, 2)",
               ["ze lopen evenwijdig", "ze snijden elkaar op de x-as, in (2, 0)", "ze hebben geen snijpunt"],
               "Het startgetal is de y-coördinaat van het snijpunt met de y-as. Allebei 2 → beide lijnen gaan door (0, 2), daar snijden ze elkaar. Evenwijdig zou dezelfde rc betekenen."),
    lambda: MC("Wat bedoel je met de 'toename van y' tussen de punten (1, 4) en (5, 10)?", "het verschil van de y-coördinaten: 10 − 4 = 6",
               ["dat de lijn stijgt", "het verschil van de x-coördinaten: 5 − 1 = 4", "de y-coördinaat van het hoogste punt: 10"],
               "Toename = nieuwe waarde − oude waarde. Voor y: 10 − 4 = 6. Voor x: 5 − 1 = 4. De rc is 6 / 4 = 1,5."),
    lambda: MC("Lijn k: y = 5x − 1 en lijn m: y = 2x + 6. Welke lijn loopt het steilst omhoog, en waarom?", "lijn k, want de richtingscoëfficiënt is groter (5 tegen 2)",
               ["lijn m, want het startgetal is groter (6 tegen −1)", "lijn m, want die snijdt de y-as hoger", "ze zijn even steil, want het zijn allebei rechte lijnen"],
               "Hoe groter de rc, hoe steiler de lijn omhoog loopt: 5 > 2, dus lijn k. Het startgetal zegt alleen waar de lijn de y-as snijdt, niet hoe steil hij is."),
]

# ---------- §1.2 ----------
def f12_S_xx(rng):
    while True:
        a1, b1, a2, b2, x0, y0 = G.twee_lijnen(rng)
        if x0 != y0 and y0 != -x0: break
    return MC(f"Bereken de coördinaten van het snijpunt van de lijnen {lin(a1, b1)} en {lin(a2, b2)}.", pt(x0, y0),
              [pt(x0, x0), pt(y0, x0), pt(x0, a2 * x0), pt(x0, y0 + a1)],
              f"Gelijkstellen: {expr(a1, b1)} = {expr(a2, b2)} → x = {fmt(x0)}. Dan x invullen in een formule: y = {fmt(a1)} · {hk(x0)} {'+' if b1 > 0 else '−'} {fmt(abs(b1))} = {fmt(y0)}. "
              f"Let op: y is níet hetzelfde als x! Snijpunt {pt(x0, y0)}.")

def f12_y_na_x(rng):
    a1, b1, a2, b2, x0, y0 = G.twee_lijnen(rng)
    return IN(f"De lijnen {lin(a1, b1)} en {lin(a2, b2)} snijden elkaar. Je hebt al berekend dat x = {fmt(x0)}. Bereken nu de y-coördinaat van het snijpunt.",
              num_ans(y0), f"Vul x = {fmt(x0)} in bij een van de formules: y = {fmt(a1)} · {hk(x0)} {'+' if b1 > 0 else '−'} {fmt(abs(b1))} = {fmt(y0)}. Controle met de andere: {fmt(a2)} · {hk(x0)} {'+' if b2 > 0 else '−'} {fmt(abs(b2))} = {fmt(a2 * x0 + b2)}.")

def f12_buiten(rng):
    # Snijpunt met x = y zou Duru's fout ("(9, 9)") belonen — overslaan.
    while True:
        v = G.q12_grafiek(rng)
        x, y = v["_opts"][0].strip("()").split(", ")
        if x != y: return v

def f12_evenwijdig_open(rng):
    a = F(rng.choice([2, 3, 4, -2, -3, 5])); b1 = F(rng.randint(-8, 9) or 1); b2 = b1 + rng.choice([-7, -4, 3, 6])
    return OP(f"Waarom hebben de lijnen {lin(a, b1)} en {lin(a, b2)} geen snijpunt? Leg uit.",
              f"Ze hebben dezelfde richtingscoëfficiënt ({fmt(a)}), dus ze lopen evenwijdig. Omdat het startgetal anders is ({fmt(b1)} en {fmt(b2)}), vallen ze niet samen en snijden ze elkaar nooit.",
              ["richtingsco/rc/hellingsgetal/zelfde a/dezelfde a/even steil", "evenwijdig/parallel"], 2,
              f"Twee dingen noemen: dezelfde rc ({fmt(a)}) → evenwijdig. Alleen 'het startgetal is anders' is niet genoeg: lijnen met een ander startgetal en een andere rc snijden elkaar wél.")

# ---------- §1.3 ----------
def f13_foutzoek(rng):
    A, T, P, a, b, c, d = G.subs(rng)
    if a in (1, -1) or d == 0: return f13_foutzoek(rng)
    goed = lin(a * c, a * d + b, A, P)
    fout = lin(a * c, d + b, A, P)
    if fout == goed: return f13_foutzoek(rng)
    return MC(f"Gegeven zijn A: {lin(a, b, A, T)} en B: {lin(c, d, T, P)}. Een leerling substitueert B in A en krijgt {fout}. Wat is er fout gegaan?",
              f"Haakjes vergeten: {fmt(a)} moet ook met {fmt(d)} vermenigvuldigd worden, dus {goed}.",
              [f"Bij het vereenvoudigen: {fmt(d)} + {hk(b)} is niet {fmt(d + b)}.",
               f"{fmt(a)} · {fmt(c)} is niet {fmt(a * c)}; het moet {fmt(a + c)} zijn.",
               "Er is niets fout gegaan."],
              f"{A} = {fmt(a)}({expr(c, d).replace('x', P)}) {'+' if b > 0 else '−'} {fmt(abs(b))} = {term(a * c, P)} {'+' if a * d >= 0 else '−'} {fmt(abs(a * d))} {'+' if b > 0 else '−'} {fmt(abs(b))}, dus {goed}. "
              f"Alles binnen de haakjes wordt met {fmt(a)} vermenigvuldigd, ook het losse getal.")

def f13_waarom(rng):
    a = F(rng.choice([2, 3, 4, 5, 6])); c = F(rng.randint(2, 9)); d = F(rng.choice([2, 3, 4, 5])); e = F(rng.randint(1, 15))
    goed = lin(-a * d, a * c + e, "h", "p")
    return OP(f"Je vult t = {fmt(c)} − {fmt(d)}p in bij h = {fmt(a)}t + {fmt(e)}. Waarom moet je {fmt(c)} − {fmt(d)}p tussen haakjes zetten? Geef ook de formule die je krijgt.",
              f"De {fmt(a)} moet met de hele uitdrukking {fmt(c)} − {fmt(d)}p vermenigvuldigd worden: h = {fmt(a)}({fmt(c)} − {fmt(d)}p) + {fmt(e)} = {fmt(a * c)} − {fmt(a * d)}p + {fmt(e)}, dus {goed}.",
              ["hele/alles/allebei/beide/heel", sleutel_term(-a * d, "p")], 2,
              f"Zonder haakjes vermenigvuldig je alleen {fmt(c)} met {fmt(a)}, en {fmt(d)}p niet. Met haakjes: {goed}.")

# ---------- §1.4 / §1.5 ----------
def f14_procent_af(rng):
    while True:
        v = G.q14_procent(rng)
        if " af." in v["vraag"]: return v

def f14_terug(rng):
    v = G.q14_terug(rng)
    v["uitleg"] += " Let op: niet vermenigvuldigen met de groeifactor — dan reken je vooruit in plaats van terug."
    return v

def f14_fout(rng, waar):
    p = rng.choice([3, 4, 6, 7, 15, 25, 30]); eenh = rng.choice(["dag", "week", "maand"])
    ding = keuze(rng, ["Het aantal vissen in een vijver", "De hoeveelheid medicijn in het bloed", "Het aantal volgers van een account", "De waarde van een scooter"])
    g = F(100 - p, 100)
    if waar:
        return WO(f"{ding} neemt per {eenh} met {p}% af. De waarde van één {eenh} eerder bereken je door de huidige waarde te delen door {fmt(g)}.", True,
                  f"Afname {p}% → groeifactor {fmt(g)}. Terug in de tijd: delen door {fmt(g)}.")
    return WO(f"{ding} neemt per {eenh} met {p}% af. De waarde van één {eenh} eerder bereken je door de huidige waarde te vermenigvuldigen met {fmt(1 + F(p, 100))}.", False,
              f"Afname {p}% → groeifactor {fmt(g)}. Terug in de tijd deel je door {fmt(g)}. Vermenigvuldigen met {fmt(1 + F(p, 100))} is iets anders: dat geeft een te klein antwoord.")

def f15_dubbel(rng, waar):
    g = F(rng.choice(["0.8", "1.3", "1.2", "0.9", "1.5", "0.7"]))
    eenh = rng.choice([("week", "twee weken"), ("uur", "twee uur"), ("jaar", "twee jaar")])
    claim = g * g if waar else 2 * g
    return WO(f"Een hoeveelheid groeit exponentieel met groeifactor {fmt(g)} per {eenh[0]}. Dan is de groeifactor per {eenh[1]} gelijk aan {fmt(claim)}.", waar,
              f"Twee stappen = twee keer vermenigvuldigen: {fmt(g)} · {fmt(g)} = {macht(g, 2)} = {fmt(g * g)}." + ("" if waar else f" Niet 2 · {fmt(g)} = {fmt(2 * g)}: je vermenigvuldigt mét de factor, je telt hem niet op."))

def f15_kwadraat(rng):
    v = G.q15_kwadraat(rng)
    v["uitleg"] += " Niet 2 · de groeifactor: elke stap vermenigvuldig je opnieuw."
    return v

def f15_waarde(rng):
    v = G.q15_waarde(rng)
    v["uitleg"] += " Let op: t is in maanden, dus jaren eerst omrekenen (1 jaar = 12 maanden)."
    return v

T = {
    "rc_punten": G.q11_rc_punten, "b_punten": G.q11_b_punten, "formule_punten": G.q11_formule_punten, "grafiek_rc": G.q11_grafiek_rc,
    "open11": G.q11_open, "noemer": f11_noemer_fout,
    "S_xx": f12_S_xx, "y_na_x": f12_y_na_x, "y": G.q12_y, "horizontaal": G.q12_grafiek_formule, "buiten": f12_buiten,
    "open12": G.q12_open, "evenwijdig": f12_evenwijdig_open,
    "sub": G.q13_sub, "coef": G.q13_coef, "const": G.q13_const, "open13": G.q13_open, "foutzoek13": f13_foutzoek, "waarom": f13_waarom,
    "procent_af": f14_procent_af, "terug14": f14_terug, "open14": G.q14_open, "grafiek14": G.q14_grafiek, "welke": G.q14_welke, "bevolking": G.q14_bevolking,
    "kwadraat": f15_kwadraat, "macht": G.q15_macht, "formule15": G.q15_formule, "terug15": G.q15_terug, "waarde": f15_waarde,
    "tabel3": G.q15_tabel3, "grafiek15": G.q15_grafiek, "open15": G.q15_open,
}
WOT = {"haakjes": G.q13_haakjes, "fout14": f14_fout, "dubbel": f15_dubbel, "lex": G.q15_lex}

# Tips alleen in toets 1 en 2 (steigers die daarna wegvallen).
TIPS = {
    "open11": "Tip: bereken eerst a = toename y / toename x; vul daarna een punt in om b te vinden.",
    "open12": "Tip: wat weet je over y in het snijpunt? Vind eerst x, daarna y.",
    "S_xx": "Tip: na x moet je y nog uitrekenen door x in een formule in te vullen.",
    "open13": "Tip: zet formule B tussen haakjes en werk de haakjes weg.",
    "kwadraat": "Tip: twee stappen = twee keer vermenigvuldigen met de groeifactor.",
    "open14": "Tip: met welk getal vermenigvuldig je van de ene waarde naar de volgende?",
    "terug15": "Tip: terugrekenen in de tijd = delen.",
}
KOMMA = " Schrijf je antwoord met een komma, bijvoorbeeld 1,05."

PLANNEN = [  # 4 × §1.1, 4 × §1.2, 4 × §1.3, 3 × §1.4, 5 × §1.5
    ("basis",       ["rc_punten", "b_punten", "noemer", "B",  "y_na_x", "S_xx", "horizontaal", "open12",
                     "haakjes:T", "coef", "foutzoek13", "sub",  "procent_af", "fout14:F", "open14",
                     "kwadraat", "dubbel:F", "terug15", "waarde", "macht"]),
    ("oefenen",     ["grafiek_rc", "formule_punten", "b_punten", "B",  "S_xx", "y", "horizontaal", "evenwijdig",
                     "sub", "const", "haakjes:F", "waarom",  "grafiek14", "terug14", "bevolking",
                     "kwadraat", "tabel3", "formule15", "dubbel:T", "grafiek15"]),
    ("gemengd",     ["open11", "noemer", "grafiek_rc", "B",  "S_xx", "buiten", "y", "open12",
                     "coef", "open13", "foutzoek13", "haakjes:T",  "procent_af", "welke", "open14",
                     "kwadraat", "macht", "terug15", "waarde", "lex:F"]),
    ("toetsniveau", ["formule_punten", "open11", "grafiek_rc", "B",  "buiten", "S_xx", "horizontaal", "evenwijdig",
                     "sub", "const", "waarom", "open13",  "grafiek14", "fout14:T", "bevolking",
                     "tabel3", "open15", "kwadraat", "grafiek15", "formule15"]),
    ("eindniveau",  ["open11", "b_punten", "noemer", "B",  "buiten", "y", "open12", "S_xx",
                     "open13", "coef", "foutzoek13", "haakjes:F",  "procent_af", "terug14", "open14",
                     "kwadraat", "dubbel:F", "open15", "terug15", "waarde"]),
]

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for i, (niveau, plan) in enumerate(PLANNEN):
        nr = 50 + i; fid = 40 + i; rng = random.Random(5000 + i * 31); vragen = []
        assert len(plan) == 20
        for slot in plan:
            naam, _, tf = slot.partition(":")
            for _ in range(300):
                if naam == "B": v = BEGRIPPEN[i]()
                elif tf: v = WOT[naam](rng, tf == "T")
                else:
                    try: v = T[naam](rng)
                    except StopIteration: continue   # nette_as() in de bibliotheek kan grote grafieken niet schalen
                if i < 2 and naam in TIPS: v["vraag"] += " " + TIPS[naam]
                if i < 3 and v["type"] == "invul" and "," in (v["antwoord"] or "") and "komma" not in v["vraag"]: v["vraag"] += KOMMA
                if norm(v["vraag"]) not in GEZIEN: break
            else: raise SystemExit("geen unieke vraag: " + slot)
            GEZIEN.add(norm(v["vraag"]))
            if v["type"] == "invul": assert v["antwoord"], v
            vragen.append(v)
        mcs = [v for v in vragen if v["type"] == "mc"]; pos = iter(mc_volgorde(rng, len(mcs)))
        for v in mcs:
            o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
        titel = f"Proeftoets {nr} — Foutentraining §1.1–§1.5 ({i + 1}/5, {niveau})"
        ex = {"id": f"ex-wiskunde-h1-{fid}", "hoofdstuk": 1, "paragraaf": "mix", "titel": titel,
              "vak": "Wiskunde · H1 Lineaire en exponentiële formules", "icoon": "🎯", "duurMin": 40, "vragen": vragen}
        with open(f"{OUT}/examen_{nr}.js", "w") as f:
            f.write("/* =========================================================\n"
                    f"   Duru's Wiskunde (HAVO 3) — {titel}\n"
                    "   Gericht op Duru's fouten in H1 §1.1–§1.5 (zie kop van het script); andere getallen dan eerdere toetsen.\n"
                    "   Gegenereerd met tools/gen_wiskunde_h1_foutentraining.py\n"
                    "   ========================================================= */\n")
            f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: 50 … 54")
