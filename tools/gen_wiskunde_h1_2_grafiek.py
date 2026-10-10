"""Wiskunde H1 §1.2 Lijnen snijden: 5 proeftoetsen waarin ELKE vraag een figuur heeft
(ex-wiskunde-h1-35…39, examen_45…49). Naar boekopgaven 10, 11, 12, 13, 14, O11, U4 en "Leerdoelen bereikt?".
Gebruik: python3 tools/gen_wiskunde_h1_2_grafiek.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, os, random, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_wiskunde_h1_paragraaf_exams import fmt, term, lin, expr, pt, svg_graph, MC, WO, IN, OP, num_ans, mc_volgorde

NAMEN = [("p", "q"), ("k", "l"), ("m", "n"), ("r", "s"), ("a", "b")]
VENSTERS = [  # (xmin, xmax, ymin, ymax, ystap)
    (-1, 9, -2, 7, 1), (-1, 9, -2, 14, 2), (-1, 9, -12, 12, 4), (-1, 6, -4, 24, 4), (-6, 4, -4, 4, 1), (-1, 9, -2, 22, 2)]

def kort(x):  # decimaal of breuk, voor uitleg
    return fmt(x)

def lijn_in(rng, v, rcs=None, noemers=(1, 2, 4)):
    xmin, xmax, ymin, ymax, ys = v
    while True:
        x1 = rng.randint(xmin, xmax - 2); x2 = rng.randint(x1 + 2, xmax)
        y1 = ys * rng.randint(-(-ymin // ys), ymax // ys); y2 = ys * rng.randint(-(-ymin // ys), ymax // ys)
        if y1 == y2: continue
        a = F(y2 - y1, x2 - x1); b = y1 - a * x1
        if a.denominator not in noemers or (rcs and a not in rcs) or abs(a) > 6: continue
        return a, b, (F(x1), F(y1)), (F(x2), F(y2))

def paar(rng, v, eis="decimaal", binnen=None, noemers=(1, 2, 4)):
    """Twee lijnen in venster v met snijpunt; eis: 'heel' | 'decimaal'; binnen: True/False/None (S in beeld?)."""
    xmin, xmax, ymin, ymax, _ = v
    for _ in range(5000):
        a1, b1, P1, P2 = lijn_in(rng, v, noemers=noemers); a2, b2, Q1, Q2 = lijn_in(rng, v, noemers=noemers)
        if a1 == a2 or a1 * a2 > 0 and abs(a1 - a2) < F(1, 3): continue
        x0 = (b2 - b1) / (a1 - a2); y0 = a1 * x0 + b1
        if eis == "heel" and (x0.denominator != 1 or y0.denominator != 1): continue
        if eis == "decimaal" and (num_ans(x0) is None or num_ans(y0) is None or len(fmt(x0)) > 5 or len(fmt(y0)) > 6): continue
        zicht = xmin < x0 < xmax and ymin < y0 < ymax
        ver_weg = not (xmin - 1 <= x0 <= xmax + 1 and ymin - v[4] <= y0 <= ymax + v[4])
        if binnen is True and not zicht: continue
        if binnen is False and not ver_weg: continue
        if (x0, y0) in {P1, P2, Q1, Q2}: continue
        if binnen is False and abs(x0) > 40: continue
        if {P1, P2} & {Q1, Q2}: continue
        return (a1, b1, P1, P2), (a2, b2, Q1, Q2), (x0, y0)
    raise RuntimeError("geen paar")

def fig(v, lijnen, punten, S=None, **kw):
    xmin, xmax, ymin, ymax, ys = v
    pts = [(float(x), float(y), (pt(x, y) if lab else "")) for x, y, lab in punten]
    if S is not None: pts.append((float(S[0]), float(S[1]), "S"))
    return svg_graph(xmin, xmax, ymin, ymax, ystap=ys, lijnen=[(float(a), float(b), n) for a, b, n in lijnen], punten=pts,
                     eenheid=26 if (ymax - ymin) / ys > 10 else 28, rechts=34, **kw)

def lab(v): return v[4] != 1   # bij een geschaalde as de coördinaten erbij zetten

# ---------- vraagtypen ----------
def rc_lezen(rng):
    v = keuze(rng, VENSTERS); a, b, P, Q = lijn_in(rng, v, noemers=(1, 2, 4))
    n = keuze(rng, "pqklm")
    f = fig(v, [(a, b, n)], [(P[0], P[1], lab(v)), (Q[0], Q[1], lab(v))])
    return IN(f"Lijn {n} gaat door de stippen {pt(*P)} en {pt(*Q)}. Laat met een berekening zien hoe groot de richtingscoëfficiënt van lijn {n} is."
              + (" Geef je antwoord als decimaal getal." if a.denominator != 1 else ""),
              num_ans(a), f"rc = toename y / toename x = ({fmt(Q[1])} − {fmt(P[1])}) / ({fmt(Q[0])} − {fmt(P[0])}) = {fmt(Q[1] - P[1])} / {fmt(Q[0] - P[0])} = {fmt(a)}.", f)

def formule_lezen(rng):
    v = keuze(rng, VENSTERS); a, b, P, Q = lijn_in(rng, v)
    n = keuze(rng, "pqklmn")
    f = fig(v, [(a, b, n)], [(P[0], P[1], lab(v)), (Q[0], Q[1], lab(v))])
    fout = [lin(-a, b), lin(a, -b) if b else lin(a, 2), lin(a, b + (Q[1] - P[1])), lin(1 / a, b)]
    return MC(f"Lijn {n} gaat onder andere door {pt(*Q)}. Welke formule hoort bij lijn {n}?", lin(a, b), fout,
              f"rc = ({fmt(Q[1])} − {fmt(P[1])}) / ({fmt(Q[0])} − {fmt(P[0])}) = {fmt(a)}. Invullen van {pt(*P)}: {fmt(P[1])} = {fmt(a * P[0])} + b, dus b = {fmt(b)}. Formule: {lin(a, b)}.", f)

def _twee(rng, eis="decimaal", binnen=None, v=None):
    v = v or keuze(rng, VENSTERS)
    L1, L2, S = paar(rng, v, eis, binnen)
    n1, n2 = keuze(rng, NAMEN)
    punten = [(L1[2][0], L1[2][1], lab(v)), (L1[3][0], L1[3][1], lab(v)), (L2[2][0], L2[2][1], lab(v)), (L2[3][0], L2[3][1], lab(v))]
    return v, L1, L2, S, n1, n2, punten

def stappen(L1, L2, S, n1, n2):
    (a1, b1, P1, P2), (a2, b2, Q1, Q2) = L1, L2
    return (f"Lijn {n1}: rc = {fmt(P2[1] - P1[1])} / {fmt(P2[0] - P1[0])} = {fmt(a1)}, dus {lin(a1, b1)}. "
            f"Lijn {n2}: rc = {fmt(Q2[1] - Q1[1])} / {fmt(Q2[0] - Q1[0])} = {fmt(a2)}, dus {lin(a2, b2)}. "
            f"Gelijkstellen: {expr(a1, b1)} = {expr(a2, b2)} → x = {fmt(S[0])}; invullen: y = {fmt(S[1])}.")

def snij_x(rng):
    v, L1, L2, S, n1, n2, punten = _twee(rng, binnen=rng.random() < 0.6)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    return IN(f"Lijn {n1} gaat door {pt(*L1[2])} en {pt(*L1[3])}, lijn {n2} door {pt(*L2[2])} en {pt(*L2[3])}. Bereken de x-coördinaat van het snijpunt van {n1} en {n2}."
              + (" Geef je antwoord als decimaal getal." if S[0].denominator != 1 else ""), num_ans(S[0]), stappen(L1, L2, S, n1, n2), f)

def snij_y(rng):
    v, L1, L2, S, n1, n2, punten = _twee(rng, binnen=rng.random() < 0.6)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    return IN(f"In de figuur zie je de lijnen {n1} (door {pt(*L1[2])}) en {n2} (door {pt(*L2[2])}). Bereken de y-coördinaat van hun snijpunt."
              + (" Geef je antwoord als decimaal getal." if S[1].denominator != 1 else ""), num_ans(S[1]), stappen(L1, L2, S, n1, n2), f)

def snij_S(rng, binnen=None):
    v, L1, L2, S, n1, n2, punten = _twee(rng, binnen=binnen)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    x0, y0 = S
    fout = [pt(y0, x0), pt(x0, y0 + 1), pt(x0 + 1, L1[0] * (x0 + 1) + L1[1]), pt(-x0, y0), pt(x0, L2[1])]
    tekst = (f"De lijnen {n1} en {n2} snijden elkaar buiten de figuur. Lijn {n1} gaat door {pt(*L1[2])}." if not (v[0] < x0 < v[1] and v[2] < y0 < v[3])
             else f"Lijn {n1} gaat door {pt(*L1[2])} en {pt(*L1[3])}.")
    return MC(tekst + f" Bereken de coördinaten van het snijpunt van {n1} en {n2}.", pt(x0, y0), fout, stappen(L1, L2, S, n1, n2), f)

def vergelijking(rng):
    v, L1, L2, S, n1, n2, punten = _twee(rng)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten, S=S if v[0] < S[0] < v[1] and v[2] < S[1] < v[3] else None)
    e1, e2 = expr(L1[0], L1[1]), expr(L2[0], L2[1])
    return MC(f"Lijn {n1} gaat door {pt(*L1[2])} en lijn {n2} door {pt(*L2[3])}. Met welke vergelijking bereken je de x-coördinaat van het snijpunt?",
              f"{e1} = {e2}", [f"{expr(L1[0], L2[1])} = {expr(L2[0], L1[1])}", f"{e1} = 0", f"{expr(-L1[0], L1[1])} = {e2}", f"{expr(L1[0], -L1[1])} = {e2}"],
              f"Stel eerst de formules op: {lin(L1[0], L1[1])} en {lin(L2[0], L2[1])}. Op het snijpunt is y gelijk, dus {e1} = {e2}.", f)

def ligging(rng):
    a = F(keuze(rng, [-2, -1, 2, 3, F(1, 2), F(-1, 2)])); b = F(rng.randint(1, 4))
    f = svg_graph(-3, 5, -4, 7, lijnen=[(float(a), float(b), lin(a, b))], punten=[(0, float(b), "")])
    soort = rng.randrange(3)
    if soort == 0:
        c = b + keuze(rng, [-2, -1, 1, 2, 3])
        goed = f"evenwijdig, {fmt(abs(c - b))} {'hoger' if c > b else 'lager'} (de y-as in (0, {fmt(c)}))"
        fout = [f"door hetzelfde punt (0, {fmt(b)}), maar steiler", f"evenwijdig, {fmt(abs(c - b))} {'lager' if c > b else 'hoger'}", "loodrecht op de geschetste lijn"]
        q = lin(a, c)
        u = f"Dezelfde rc ({fmt(a)}) → evenwijdig. Startgetal {fmt(c)} in plaats van {fmt(b)} → {fmt(abs(c - b))} {'hoger' if c > b else 'lager'}."
    else:
        c = keuze(rng, [x for x in [-3, -1, 1, 4, F(1, 2), -2] if F(x) != a])
        q = lin(c, b)
        goed = f"door hetzelfde punt (0, {fmt(b)}), met een andere helling"
        fout = [f"evenwijdig, {fmt(abs(F(c) - a))} hoger", "evenwijdig, maar door de oorsprong", f"ze snijden elkaar in ({fmt(b)}, 0)"]
        u = f"Hetzelfde startgetal ({fmt(b)}) → beide lijnen gaan door (0, {fmt(b)}). De rc is anders ({fmt(c)} tegen {fmt(a)}), dus ze snijden elkaar daar."
    return MC(f"De geschetste lijn hoort bij de formule {lin(a, b)}. Hoe ligt de lijn {q} ten opzichte van de geschetste lijn?", goed, fout, u, f)

def welke_lijn(rng):
    v = (-1, 7, -4, 8, 1)
    while True:
        lijnen = [(F(keuze(rng, [-2, -1, F(-1, 2), F(1, 2), 1, 2, 3])), F(rng.randint(-3, 6))) for _ in range(4)]
        if len(set(lijnen)) == 4 and len({x[0] for x in lijnen}) >= 3: break
    namen = ["a", "b", "c", "d"]; i = rng.randrange(4); a, b = lijnen[i]
    f = svg_graph(-1, 7, -4, 8, lijnen=[(float(x), float(y), namen[j]) for j, (x, y) in enumerate(lijnen)])
    return MC(f"In de figuur zie je vier lijnen. Welke lijn hoort bij de formule {lin(a, b)}?", f"lijn {namen[i]}",
              [f"lijn {n}" for n in namen if n != namen[i]],
              f"Startgetal {fmt(b)}: de lijn snijdt de y-as in (0, {fmt(b)}). rc {fmt(a)}: {'stijgend' if a > 0 else 'dalend'}, {fmt(abs(a))} omhoog/omlaag per stap naar rechts. Dat is lijn {namen[i]}.", f)

def credits(rng):
    for _ in range(5000):
        x1, x2 = rng.randint(0, 2), rng.randint(9, 14); y1 = rng.randint(1, 3); y2 = y1 + rng.randint(6, 14)
        a1 = F(y2 - y1, x2 - x1); b1 = y1 - a1 * x1
        d1, d2 = 2, rng.choice([6, 8, 10]); a2 = a1 + F(rng.randint(1, 8), 4)
        b2 = F(rng.choice([-2, -1, F(-1, 2), 0]))
        if a2 <= a1: continue
        t = (b2 - b1) / (a1 - a2)
        v1, v2 = a2 * d1 + b2, a2 * d2 + b2
        if t.denominator == 1 and 2 <= t <= 30 and v1 > 0 and (v1 * 10).denominator == 1 and (v2 * 10).denominator == 1: break
    n1, n2 = keuze(rng, [("Cleon", "Martijn"), ("Ayla", "Noor"), ("Sem", "Daan"), ("Lina", "Mees")])
    f = svg_graph(0, 16, 0, 20, ystap=2, eenheid=20, lijnen=[(float(a1), float(b1), n1)], punten=[(x1, y1, pt(x1, y1)), (x2, y2, pt(x2, y2))],
                  xlabel="tijd in dagen", ylabel="credits in miljoenen", rechts=40)
    mil = lambda x: fmt(x * 1000000, dui=True)
    return IN(f"In de figuur zie je hoe het aantal credits van {n1} toeneemt. {n2} begint op hetzelfde moment en spaart elke dag evenveel: na {d1} dagen heeft {n2} {mil(v1)} credits en na {d2} dagen {mil(v2)} credits. Na hoeveel dagen hebben ze evenveel credits?",
              num_ans(t), f"{n1}: rc = ({y2} − {y1}) / ({x2} − {x1}) = {fmt(a1)}, formule c = {expr(a1, b1).replace('x', 't')}. {n2} (in miljoenen): rc = ({fmt(v2)} − {fmt(v1)}) / ({d2} − {d1}) = {fmt(a2)}, b = {fmt(b2)}. Gelijkstellen geeft t = {fmt(t)}.", f)

def o11(rng):
    v = (-1, 9, -2, 22, 2)
    L1, L2, S = paar(rng, v, eis="decimaal", binnen=False)
    n1, n2 = keuze(rng, NAMEN)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], [(L1[2][0], L1[2][1], True), (L1[3][0], L1[3][1], True), (L2[2][0], L2[2][1], True), (L2[3][0], L2[3][1], True)])
    return IN(f"Lijn {n1} gaat door de punten {pt(*L1[2])} en {pt(*L1[3])}. Stel bij beide lijnen een formule op en bereken de x-coördinaat van het snijpunt."
              + (" Geef je antwoord als decimaal getal." if S[0].denominator != 1 else ""), num_ans(S[0]), stappen(L1, L2, S, n1, n2), f)

def u4(rng):
    v = (-1, 9, -14, 4, 2)
    for _ in range(5000):
        ak, bk, P, Q = lijn_in(rng, v, noemers=(1, 2))
        x0 = F(-rng.randint(2, 9))
        b = (ak * x0 + bk) / (2 * x0 + 1)
        if b != 0 and (2 * b).denominator in (1, 2) and abs(2 * b) <= 12: break
    f = fig(v, [(ak, bk, "k")], [(P[0], P[1], True), (Q[0], Q[1], True)])
    return IN(f"Lijn k is getekend. Bij lijn l is de richtingscoëfficiënt twee keer zo groot als het startgetal. De x-coördinaat van het snijpunt van k en l is x = {fmt(x0)}. Bereken de richtingscoëfficiënt van lijn l."
              + (" Geef je antwoord als decimaal getal." if (2 * b).denominator != 1 else ""), num_ans(2 * b),
              f"Lijn k: {lin(ak, bk)}. Lijn l: y = 2b·x + b. Op x = {fmt(x0)}: {fmt(ak)} · {fmt(x0)} + {fmt(bk)} = 2b · {fmt(x0)} + b → {fmt(ak * x0 + bk)} = {fmt(2 * x0 + 1)}b → b = {fmt(b)}, dus rc = {fmt(2 * b)}.", f)

def leerdoel(rng):
    v = (-6, 4, -4, 4, 1)
    return snij_S_v(rng, v)

def snij_S_v(rng, v):
    L1, L2, S = paar(rng, v, eis="decimaal")
    n1, n2 = "k", "l"
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], [(L1[2][0], L1[2][1], False), (L1[3][0], L1[3][1], False), (L2[2][0], L2[2][1], False), (L2[3][0], L2[3][1], False)])
    x0, y0 = S
    return MC(f"Lijn k gaat door {pt(*L1[2])} en lijn l door {pt(*L2[2])} (zie figuur). Bereken de coördinaten van het snijpunt van k en l.", pt(x0, y0),
              [pt(y0, x0), pt(x0, -y0) if y0 else pt(x0, 1), pt(x0 - 1, L1[0] * (x0 - 1) + L1[1]), pt(-x0, y0) if x0 else pt(1, y0)], stappen(L1, L2, S, n1, n2), f)

def wo_rechts(rng, waar):
    v, L1, L2, S, n1, n2, punten = _twee(rng, binnen=False)
    g = rng.randint(int(S[0]) - 6, int(S[0]) + 6)
    if g == S[0]: g += 1
    rechts = S[0] > g
    zeg = "rechts" if rechts == waar else "links"
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    return WO(f"Lijn {n1} gaat door {pt(*L1[2])} en lijn {n2} door {pt(*L2[2])}. Het snijpunt van {n1} en {n2} ligt {zeg} van de lijn x = {fmt(g)}.", waar,
              f"{lin(L1[0], L1[1])} en {lin(L2[0], L2[1])} gelijkstellen geeft x = {fmt(S[0])}; dat is {'rechts' if rechts else 'links'} van x = {fmt(g)}.", f)

def wo_evenwijdig(rng, waar):
    v = keuze(rng, VENSTERS[:3])
    a, b, P, Q = lijn_in(rng, v, noemers=(1, 2))
    n1, n2 = keuze(rng, NAMEN)
    if waar:
        a2 = a; d = v[4] * rng.choice([-3, -2, 2, 3])
    else:
        a2 = a + keuze(rng, [F(1, 2), F(-1, 2), F(1), F(-1)]); d = v[4] * rng.choice([-2, 2])
    b2 = b + d
    P2 = (P[0], a2 * P[0] + b2)
    f = fig(v, [(a, b, n1), (a2, b2, n2)], [(P[0], P[1], lab(v)), (Q[0], Q[1], lab(v)), (P2[0], P2[1], lab(v))])
    return WO(f"Lijn {n1} gaat door {pt(*P)} en {pt(*Q)}. Lijn {n2} gaat door {pt(*P2)} en heeft richtingscoëfficiënt {fmt(a2)}. De lijnen {n1} en {n2} hebben geen snijpunt.", waar,
              f"Lijn {n1} heeft rc {fmt(a)}. " + ("Gelijke rc en ander startgetal: evenwijdig, dus geen snijpunt." if waar else f"De rc's verschillen ({fmt(a)} en {fmt(a2)}), dus ze snijden elkaar wel."), f)

def wo_snijpunt(rng, waar):
    v, L1, L2, S, n1, n2, punten = _twee(rng)
    T = S if waar else keuze(rng, [(S[1], S[0]), (S[0], S[1] + v[4]), (S[0] + 1, S[1])])
    if not waar and T == S: T = (S[0], S[1] + 1)
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    return WO(f"Lijn {n1} gaat door {pt(*L1[2])} en {pt(*L1[3])}, lijn {n2} door {pt(*L2[2])} en {pt(*L2[3])}. Het snijpunt van {n1} en {n2} is {pt(*T)}.", waar,
              stappen(L1, L2, S, n1, n2) + f" Het snijpunt is {pt(*S)}.", f)

def open_snij(rng):
    v, L1, L2, S, n1, n2, punten = _twee(rng, eis="heel")
    f = fig(v, [(L1[0], L1[1], n1), (L2[0], L2[1], n2)], punten)
    return OP(f"Lijn {n1} gaat door {pt(*L1[2])} en lijn {n2} door {pt(*L2[3])}. Beschrijf in stappen hoe je het snijpunt van {n1} en {n2} berekent en geef het snijpunt.",
              f"1 Formules opstellen: {lin(L1[0], L1[1])} en {lin(L2[0], L2[1])}. 2 Gelijkstellen: {expr(L1[0], L1[1])} = {expr(L2[0], L2[1])}. 3 Oplossen: x = {fmt(S[0])}. 4 Invullen: y = {fmt(S[1])}. Snijpunt {pt(*S)}.",
              ["formule/rc/richtingsco", "gelijk", "vergelijking/oplossen/los", "invullen/invul/vul"], 3, stappen(L1, L2, S, n1, n2)) | {"figuur": f}

def keuze(rng, l): return l[rng.randrange(len(l))]

T = {"rc": rc_lezen, "formule": formule_lezen, "x": snij_x, "y": snij_y, "S": snij_S, "Sbuiten": lambda r: snij_S(r, False),
     "verg": vergelijking, "ligging": ligging, "welke": welke_lijn, "credits": credits, "o11": o11, "u4": u4, "leerdoel": leerdoel,
     "open": open_snij}
WOT = {"rechts": wo_rechts, "even": wo_evenwijdig, "snij": wo_snijpunt}
PLANNEN = [
    ("basis",       ["rc", "formule", "verg", "S", "welke", "ligging", "formule", "S", "leerdoel", "verg", "even:T", "snij:F", "rechts:F", "snij:T", "rc", "x", "y", "credits", "x", "open"]),
    ("oefenen",     ["formule", "verg", "S", "Sbuiten", "welke", "ligging", "leerdoel", "S", "formule", "verg", "snij:T", "even:F", "rechts:T", "snij:F", "rc", "x", "o11", "y", "credits", "open"]),
    ("gemengd",     ["S", "Sbuiten", "formule", "welke", "ligging", "verg", "leerdoel", "S", "welke", "formule", "rechts:F", "snij:T", "even:T", "snij:F", "x", "y", "o11", "credits", "rc", "open"]),
    ("toetsniveau", ["Sbuiten", "S", "verg", "formule", "ligging", "leerdoel", "Sbuiten", "welke", "S", "ligging", "even:F", "rechts:T", "snij:F", "snij:T", "o11", "u4", "x", "credits", "y", "open"]),
    ("eindniveau",  ["Sbuiten", "leerdoel", "S", "ligging", "verg", "Sbuiten", "formule", "welke", "S", "verg", "snij:F", "rechts:F", "even:T", "snij:T", "u4", "o11", "credits", "x", "y", "open"]),
]

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for i, (niveau, plan) in enumerate(PLANNEN):
        nr = 45 + i; fid = 35 + i; rng = random.Random(4500 + i * 17); vragen = []
        assert len(plan) == 20
        for slot in plan:
            naam, _, tf = slot.partition(":")
            for _ in range(300):
                v = WOT[naam](rng, tf == "T") if tf else T[naam](rng)
                if norm(v["vraag"]) not in GEZIEN: break
            else: raise SystemExit("geen unieke vraag: " + slot)
            GEZIEN.add(norm(v["vraag"]))
            if v["type"] == "invul": assert v["antwoord"], v
            vragen.append(v)
        mcs = [v for v in vragen if v["type"] == "mc"]; pos = iter(mc_volgorde(rng, len(mcs)))
        for v in mcs:
            o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
        titel = f"Proeftoets {nr} — §1.2 Lijnen snijden met grafieken ({i + 1}/5, {niveau})"
        ex = {"id": f"ex-wiskunde-h1-{fid}", "hoofdstuk": 1, "paragraaf": "1.2", "titel": titel,
              "vak": "Wiskunde · H1 Lineaire en exponentiële formules", "icoon": "📈", "duurMin": 30, "vragen": vragen}
        with open(f"{OUT}/examen_{nr}.js", "w") as f:
            f.write("/* =========================================================\n"
                    f"   Duru's Wiskunde (HAVO 3) — {titel}\n"
                    "   Bron: Noordhoff H1 §1.2 opdracht 10–14, O11, U4, Leerdoelen (elke vraag met figuur; andere getallen)\n"
                    "   Gegenereerd met tools/gen_wiskunde_h1_2_grafiek.py\n"
                    "   ========================================================= */\n")
            f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: 45 … 49")
