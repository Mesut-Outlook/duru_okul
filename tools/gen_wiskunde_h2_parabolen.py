"""Wiskunde H2 Parabolen (HAVO 3, Noordhoff): 6 onderwerpen (§2.1–§2.5 + begrippen) en 13 proeftoetsen
(ex-wiskunde-parabolen-1…13, examen_61…73): per paragraaf 2 toetsen, 1 begrippentoets, 2 gemengd (oefenproefwerk-niveau).
Naar boekopdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8 met andere getallen; alle algebra met Fraction berekend.
Gebruik: python3 tools/gen_wiskunde_h2_parabolen.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, os, random, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_wiskunde_h1_paragraaf_exams import fmt, svg_graph, svg_tabel, MC, WO, IN, num_ans, mc_volgorde
from gen_wiskunde_h1_lijnen_snijpunt import sleutel

KLEUREN = ["#c2185b", "#2563eb", "#0d9488", "#b45309"]
GLYPH = {F(1, 2): "½", F(1, 3): "⅓", F(2, 3): "⅔", F(1, 4): "¼", F(3, 4): "¾"}

# ---------- notatie ----------
def co(x):
    x = F(x); s = GLYPH.get(abs(x)) or fmt(abs(x))
    return ("−" if x < 0 else "") + s

def n(x): return fmt(F(x))            # getal in tekst: 2,5 / −3 / 1/3
def hk(x): return f"({n(x)})" if F(x) < 0 else n(x)

def term(c, v):
    if v == "": return co(c)
    if abs(c) == 1: return ("−" if c < 0 else "") + v
    return co(c) + v

def poly(termen, lhs="y"):
    termen = [(F(c), v) for c, v in termen if c != 0]
    if not termen: return f"{lhs} = 0"
    s = term(*termen[0])
    for c, v in termen[1:]:
        s += (" + " if c > 0 else " − ") + term(abs(c), v)
    return f"{lhs} = {s}" if lhs else s

def kw(a, b, c, x="x", lhs="y"): return poly([(a, x + "²"), (b, x), (c, "")], lhs)
def rechts(a, b, c, x="x"): return kw(a, b, c, x, lhs="")

def fac(s, x="x"):
    s = F(s)
    return x if s == 0 else f"({x} − {co(s)})" if s > 0 else f"({x} + {co(-s)})"

def voor(a): return "" if a == 1 else "−" if a == -1 else co(a)

def gefact(a, s, t, x="x", lhs="y"):   # y = a(x − s)(x − t)
    f1, f2 = fac(s, x), fac(t, x)
    if t == 0: f1, f2 = f2, f1          # x(x − 4), niet (x − 4)x
    return f"{lhs} = {voor(a)}{f1}{f2}"

def topvorm(a, p, q, x="x", lhs="y"):   # y = a(x − p)² + q
    kern = f"{voor(a)}{fac(p, x)}²" if p != 0 else f"{voor(a)}{x}²"
    return f"{lhs} = {kern}" + ("" if q == 0 else (" + " if q > 0 else " − ") + co(abs(F(q))))

def pt(x, y): return f"({n(x)}, {n(y)})"
def okey(x):   # oefen-invoer: decimaal of breuk, met beide mintekens
    s = num_ans(F(x)) or f"{F(x).numerator}/{F(x).denominator}"
    return s + ("|" + s.replace("-", "−") if "-" in s else "")

def val(a, b, c, x): return a * x * x + b * x + c
def top_van(a, b, c): xt = F(-b) / (2 * a); return xt, val(a, b, c, xt)
def keuze(rng, l): return l[rng.randrange(len(l))]

def figuur(krommen, xmin, xmax, ymin, ymax, ystap=1, punten=(), kleuren=KLEUREN, **kw_):
    return svg_graph(xmin, xmax, ymin, ymax, ystap=ystap, eenheid=24 if (ymax - ymin) / ystap <= 14 else 20,
                     krommen=krommen, punten=punten, kleuren=kleuren, rechts=20, **kw_)

def para(a, b, c): a, b, c = float(a), float(b), float(c); return lambda x: a * x * x + b * x + c

# nette parabool met top (p, q) en hele b en c
A_HEEL = [F(1), F(-1), F(2), F(-2), F(3), F(-3)]
A_ALLE = A_HEEL + [F(1, 2), F(-1, 2)]
def met_top(rng, a_set=A_ALLE, prange=(-5, 5), qrange=(-9, 9), b0=False, halve_p=False):
    while True:
        a = keuze(rng, a_set)
        p = F(rng.randint(*prange)) + (F(1, 2) if halve_p and rng.random() < 0.5 else 0)
        q = F(rng.randint(*qrange))
        b, c = -2 * a * p, a * p * p + q
        if b.denominator != 1 or c.denominator != 1: continue
        if not b0 and b == 0: continue
        return a, b, c, p, q

def uitwerken(a, b, c):
    """Uitleg volgens de aanpak van §2.2 (snijpunt y-as → zelfde hoogte → midden)."""
    xt, yt = top_van(a, b, c); x2 = -F(b) / a
    return (f"1 Uit x = 0 volgt y = {n(c)}. 2 {rechts(a, b, c)} = {n(c)} → {rechts(a, b, 0)} = 0 → x({rechts(0, a, b)}) = 0 → "
            f"x = 0 of x = {n(x2)}. 3 De x-coördinaat van de top ligt midden tussen 0 en {n(x2)}: x = {n(xt)}. "
            f"4 y = {term_inv(a, b, c, xt)} = {n(yt)}. 5 De top is {pt(xt, yt)}.")

def term_inv(a, b, c, x):
    s = f"{co(a) if abs(a) != 1 else ('−' if a < 0 else '')}{'·' if abs(a) != 1 else ''}{hk(x)}²"
    if b: s += (" + " if b > 0 else " − ") + f"{co(abs(b))} · {hk(x)}"
    if c: s += (" + " if c > 0 else " − ") + n(abs(c))
    return s

# =====================================================================
# §2.1 Bergparabool of dalparabool
# =====================================================================
def haakjesformule(rng):
    """(formule-tekst, a, b, c, uitleg) — formule met haakjes die je eerst moet uitwerken."""
    soort = rng.randrange(4)
    if soort == 0:   # (px + q)(r + sx) + kx²
        p, q, r, s = keuze(rng, [1, 2, 3, -1]), rng.randint(-6, 6) or 1, rng.randint(-6, 6) or 2, keuze(rng, [1, -1, 2, -2])
        k = keuze(rng, [x for x in range(-4, 5) if x and x != -p * s])
        a, b, c = p * s + k, p * r + q * s, q * r
        tekst = f"y = ({rechts(0, p, q)})({poly([(r, ''), (s, 'x')], '')}) {'+' if k > 0 else '−'} {term(abs(k), 'x²')}"
        uit = f"({rechts(0, p, q)})({poly([(r, ''), (s, 'x')], '')}) = {rechts(p * s, p * r + q * s, q * r)}. Samen met {term(k, 'x²')}: {kw(a, b, c)}."
    elif soort == 1:  # x(p − qx) + kx²
        p, q = rng.randint(2, 9), keuze(rng, [2, 3, 4, 5, -2, -3])
        k = keuze(rng, [x for x in range(-6, 7) if x and x != q])
        a, b, c = -q + k, p, 0
        tekst = f"y = x({poly([(p, ''), (-q, 'x')], '')}) {'+' if k > 0 else '−'} {term(abs(k), 'x²')}"
        uit = f"x({poly([(p, ''), (-q, 'x')], '')}) = {rechts(-q, p, 0)}. Samen met {term(k, 'x²')}: {kw(a, b, c)}."
    elif soort == 2:  # (px + q)² − kx²
        p, q = keuze(rng, [1, 2, 3, 4]), keuze(rng, [-5, -3, -1, 1, 2, 4])
        k = keuze(rng, [x for x in range(-18, 19) if x and x != -p * p and abs(x) > 1])
        a, b, c = p * p + k, 2 * p * q, q * q
        tekst = f"y = ({rechts(0, p, q)})² {'+' if k > 0 else '−'} {term(abs(k), 'x²')}"
        uit = f"({rechts(0, p, q)})² = ({rechts(0, p, q)})({rechts(0, p, q)}) = {rechts(p * p, 2 * p * q, q * q)}. Samen met {term(k, 'x²')}: {kw(a, b, c)}."
    else:  # (p − x)(p + x) + kx²  (ezelsbrug: geeft −x²)
        p = rng.randint(2, 9); k = keuze(rng, [x for x in range(-4, 5) if x and x != 1])
        a, b, c = -1 + k, 0, p * p
        tekst = f"y = ({p} − x)({p} + x) {'+' if k > 0 else '−'} {term(abs(k), 'x²')}"
        uit = f"({p} − x)({p} + x) = {rechts(-1, 0, p * p)}. Samen met {term(k, 'x²')}: {kw(a, b, c)}."
    if a == 0: return haakjesformule(rng)
    return tekst, F(a), F(b), F(c), uit

def bd(a): return "dalparabool" if a > 0 else "bergparabool"

def q21_wo_los(rng, waar):
    a = keuze(rng, A_ALLE + [F(-1, 4), F(5), F(-5)]); b, c = F(rng.randint(-9, 9)), F(rng.randint(-9, 9))
    vorm = keuze(rng, [kw(a, b, c), poly([(c, ""), (b, "x"), (a, "x²")]), poly([(b, "x"), (a, "x²"), (c, "")])])
    zeg = bd(a) if waar else bd(-a)
    return WO(f"De grafiek bij de formule {vorm} is een {zeg}.", waar,
              f"Het getal voor x² is {co(a)}: {'positief' if a > 0 else 'negatief'}, dus een {bd(a)}. Let op: de volgorde van de termen maakt niet uit.")

def q21_haakjes_a(rng):
    t, a, b, c, uit = haakjesformule(rng)
    return IN(f"Gegeven is de formule {t}. Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?", sleutel(a),
              uit + f" Het getal voor x² is {n(a)}, dus de grafiek is een {bd(a)}.")

def q21_haakjes_wo(rng, waar):
    t, a, b, c, uit = haakjesformule(rng)
    return WO(f"De grafiek bij de formule {t} is een {bd(a) if waar else bd(-a)}.", waar, uit + f" Het getal voor x² is {n(a)}: een {bd(a)}.")

def q21_mc_soort(rng):
    t, a, b, c, uit = haakjesformule(rng)
    goed = f"een {bd(a)}, want na haakjes wegwerken staat er {term(a, 'x²')}"
    fout = [f"een {bd(-a)}, want na haakjes wegwerken staat er {term(-a, 'x²')}",
            f"een {bd(-a)}, want de formule begint met een {'plus' if a < 0 else 'min'}teken",
            f"een rechte lijn, want er staan haakjes in de formule"]
    return MC(f"Wat voor grafiek hoort bij de formule {t}?", goed, fout, uit)

def q21_figuur(rng):
    a, b, c, p, q = met_top(rng, prange=(-3, 3), qrange=(-4, 4))
    f = figuur([para(a, b, c)], -6, 6, -8, 8, ystap=2)
    vormen = []
    for _ in range(40):
        t, a2, b2, c2, _u = haakjesformule(rng)
        vormen.append((t, a2))
    goed = next(t for t, x in vormen if (x > 0) == (a > 0))
    fout = [t for t, x in vormen if (x > 0) != (a > 0)]
    fout = list(dict.fromkeys(fout))[:3]
    return MC(f"In de figuur zie je een {bd(a)} met top {pt(p, q)}. Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)", goed, fout,
              f"Bij een {bd(a)} is na het wegwerken van de haakjes het getal voor x² {'positief' if a > 0 else 'negatief'}. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².", f)

def q21_context(rng):
    k = keuze(rng, [F(3, 10), F(1, 5), F(2, 5), F(1, 10)]); L = rng.randint(6, 14); s = keuze(rng, [F(21, 10), F(2), F(9, 5), F(5, 2)])
    wie, wat = keuze(rng, [("Een basketbalspeler", "basket"), ("Een volleyballer", "net"), ("Een handballer", "doel")])
    goed = f"h = {voor(-k)}a(a − {L}) + {n(s)}"
    fout = [f"h = {voor(k)}a(a − {L}) + {n(s)}", f"h = {voor(-k)}a({L} − a) + {n(s)}", f"h = {co(k)}a² + {n(s)}"]
    return MC(f"{wie} gooit een bal vanaf {n(s)} m hoogte richting het {wat}. Na {L} m horizontale afstand is de bal weer op {n(s)} m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
              goed, fout, f"Werk de haakjes weg. {goed}: {kw(-k, k * L, s, 'a', 'h')} — het getal voor a² is negatief, dus een bergparabool. "
              f"Bij {fout[0]} en {fout[1]} is het getal voor a² positief (dalparabool); h = {co(k)}a² + {n(s)} is ook een dalparabool.")

# =====================================================================
# §2.2 Symmetrie en top
# =====================================================================
def q22_top_x(rng):
    a, b, c, p, q = met_top(rng)
    return IN(f"Bereken de x-coördinaat van de top van de parabool bij de formule {kw(a, b, c)}.", sleutel(p), uitwerken(a, b, c))

def q22_top_y(rng):
    a, b, c, p, q = met_top(rng)
    return IN(f"Bereken de y-coördinaat van de top van de parabool bij de formule {kw(a, b, c)}.", sleutel(q), uitwerken(a, b, c))

def q22_top_mc(rng):
    a, b, c, p, q = met_top(rng, prange=(-5, 5))
    if p == 0: p = F(2)
    a, b, c = a, -2 * a * p, a * p * p + q
    fout = [pt(-p, q), pt(p, c), pt(p, val(a, b, c, -p)), pt(-p, val(a, b, c, -p)), pt(2 * p, c)]
    return MC(f"Wat zijn de coördinaten van de top van de parabool bij {kw(a, b, c)}?", pt(p, q), fout, uitwerken(a, b, c))

def q22_zelfde_hoogte(rng):
    a, b, c, p, q = met_top(rng)
    x2 = -b / a
    return IN(f"De parabool bij {kw(a, b, c)} snijdt de y-as in (0, {n(c)}). Er is nog een punt op de parabool met y = {n(c)}. Bereken de x-coördinaat van dat punt.",
              sleutel(x2), f"{rechts(a, b, c)} = {n(c)} → {rechts(a, b, 0)} = 0 → x({rechts(0, a, b)}) = 0 → x = 0 of x = {n(x2)}. Het andere punt is ({n(x2)}, {n(c)}).")

def gefact_param(rng, a_set=(F(1), F(-1), F(2), F(-2), F(1, 2))):
    while True:
        a = keuze(rng, a_set); s, t = rng.randint(-9, 9), rng.randint(-9, 9)
        if s == t or s == 0 and t == 0: continue
        if (s + t) % 2 and rng.random() < 0.6: continue
        xt = F(s + t, 2); yt = a * (xt - s) * (xt - t)
        if yt.denominator > 4 or abs(yt) > 60: continue
        return a, F(s), F(t), xt, yt

def gefact_uitleg(a, s, t, xt, yt):
    return (f"{voor(a)}{fac(s)}{fac(t)} = 0 → x = {n(s)} of x = {n(t)}: de snijpunten met de x-as zijn ({n(s)}, 0) en ({n(t)}, 0). "
            f"De top ligt midden tussen x = {n(s)} en x = {n(t)}: x = ({n(s)} + {hk(t)}) / 2 = {n(xt)}. "
            f"y = {voor(a) + ' · ' if voor(a) not in ('', '−') else voor(a)}({n(xt)} − {hk(s)})({n(xt)} − {hk(t)}) = {n(yt)}. Top {pt(xt, yt)}.")

def q22_gef_x(rng):
    a, s, t, xt, yt = gefact_param(rng)
    return IN(f"Bereken de x-coördinaat van de top van de parabool bij {gefact(a, s, t)}." + (" Een breuk of decimaal getal mag." if xt.denominator != 1 else ""),
              sleutel(xt), gefact_uitleg(a, s, t, xt, yt))

def q22_gef_y(rng):
    a, s, t, xt, yt = gefact_param(rng)
    return IN(f"Bereken de y-coördinaat van de top van de parabool bij {gefact(a, s, t)}." + (" Een breuk of decimaal getal mag." if yt.denominator != 1 else ""),
              sleutel(yt), gefact_uitleg(a, s, t, xt, yt))

def q22_snijx(rng):
    a, s, t, xt, yt = gefact_param(rng)
    lo, hi = min(s, t), max(s, t)
    return MC(f"Wat zijn de snijpunten van de parabool bij {gefact(a, s, t)} met de x-as?", f"({n(lo)}, 0) en ({n(hi)}, 0)",
              [f"({n(-lo)}, 0) en ({n(-hi)}, 0)", f"(0, {n(lo)}) en (0, {n(hi)})", f"({n(lo)}, 0) en ({n(-hi)}, 0)", f"({n(-lo)}, 0) en ({n(hi)}, 0)"],
              f"Los {voor(a)}{fac(s)}{fac(t)} = 0 op: {fac(s)} = 0 of {fac(t)} = 0, dus x = {n(s)} of x = {n(t)}. Let op het teken: bij (x + 3) hoort x = −3.")

def q22_b_zoeken(rng):
    xt = keuze(rng, [-4, -3, -2, -1, 1, 2, 3, 4]); k = keuze(rng, [x for x in range(-12, 13) if x])
    b = -2 * xt
    return IN(f"Gegeven is de formule y = x² + bx {'+' if k >= 0 else '−'} {abs(k)}. De x-coördinaat van de top van de parabool is {n(xt)}. Bereken b.",
              sleutel(b), f"De parabool snijdt de y-as in (0, {k}). Het andere punt met y = {k} ligt even ver aan de andere kant van de top: x = 2 · {hk(xt)} = {n(2 * xt)}. "
              f"Invullen: {hk(2 * xt)}² + b · {hk(2 * xt)} + {hk(k)} = {k} → {n(4 * xt * xt)} + {n(2 * xt)}b = 0 → b = {n(b)}.")

def q22_tunnel(rng, vraag):
    s = keuze(rng, [F(4, 5), F(1, 2), F(2, 5), F(1, 4), F(3, 5)]); W = keuze(rng, [4, 6, 8, 10, 12])
    r = s * W; H = s * F(W, 2) ** 2
    if r.denominator > 10 or H.denominator > 100: return q22_tunnel(rng, vraag)
    f = f"h = {n(r)}a − {n(s)}a²"
    uit = f"{n(r)}a − {n(s)}a² = 0 → a({n(r)} − {n(s)}a) = 0 → a = 0 of a = {n(r)} / {n(s)} = {W}. De tunnel is {W} m breed. Midden: a = {n(F(W, 2))}, h = {n(r)} · {n(F(W, 2))} − {n(s)} · {n(F(W, 2))}² = {n(H)} m."
    if vraag == "breed":
        return IN(f"De formule {f} hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?", sleutel(W), uit)
    return IN(f"De formule {f} hoort bij de hoogte van een tunnelboog (h in meters, a in meters vanaf de linkermuur). Hoeveel meter hoog is de tunnel in het midden?", sleutel(H), uit)

def q22_hangbrug(rng):
    while True:
        k = keuze(rng, [F(1, 40), F(1, 20), F(1, 25), F(1, 50)]); d = keuze(rng, [20, 24, 30, 40, 50]); n0 = rng.randint(15, 40)
        m = k * d; mn = n0 - k * F(d, 2) ** 2
        if mn > 2 and m.denominator <= 100: break
    return IN(f"Bij een hangbrug hoort de formule h = {n(k)}a² − {n(m)}a + {n0}. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
              sleutel(mn), f"P ligt op hoogte {n0}. Zelfde hoogte: {n(k)}a² − {n(m)}a = 0 → a = 0 of a = {n(m)} / {n(k)} = {d}. Laagste punt in het midden: a = {n(F(d, 2))}, h = {n(mn)} m.")

# =====================================================================
# §2.3 Parabolen tekenen
# =====================================================================
def q23_tabelwaarde(rng):
    a, b, c, p, q = met_top(rng, a_set=A_HEEL)
    xs = [p + d for d in range(-3, 4)]; k = keuze(rng, [0, 1, 2, 4, 5, 6])
    rij_y = ["…" if i == k else (n(q) if i == 3 else "") for i in range(7)]
    f = svg_tabel([["x"] + [n(x) for x in xs], ["y"] + [r or "…" for r in rij_y]])
    return IN(f"Voor de parabool bij {kw(a, b, c)} is de tabel gemaakt rondom de top ({n(p)}, {n(q)}). Welk getal hoort in de tabel bij x = {n(xs[k])}?",
              sleutel(val(a, b, c, xs[k])), f"y = {term_inv(a, b, c, xs[k])} = {n(val(a, b, c, xs[k]))}.", f)

def q23_symmetrie_tabel(rng):
    a, b, c, p, q = met_top(rng, a_set=A_HEEL)
    d = rng.randint(1, 3); x1, x2 = p - d, p + d; y1 = val(a, b, c, x1)
    return IN(f"De parabool bij {kw(a, b, c)} heeft als top ({n(p)}, {n(q)}). Bij x = {n(x1)} hoort y = {n(y1)}. Bij welke andere x-waarde hoort ook y = {n(y1)}?",
              sleutel(x2), f"De parabool is symmetrisch in de lijn x = {n(p)}. x = {n(x1)} ligt {d} links van de symmetrieas, dus ook {d} rechts: x = {n(x2)}.")

def q23_symmetrieas(rng):
    a, b, c, p, q = met_top(rng)
    return IN(f"Geef de formule van de symmetrieas van de parabool bij {kw(a, b, c)}. Vul in: x = …", sleutel(p), uitwerken(a, b, c) + f" De symmetrieas is de lijn x = {n(p)}.")

def q23_welke_formule(rng):
    a, b, c, p, q = met_top(rng, a_set=[F(1), F(-1), F(2), F(-2)], prange=(-3, 3), qrange=(-5, 5))
    f = figuur([para(a, b, c)], -6, 6, -8, 8, ystap=2, punten=[(float(p), float(q), pt(p, q))])
    fout = [kw(a, 2 * a * p, a * p * p + q), kw(-a, -b, -c), kw(a, b, c + 2 if c + 2 != 0 else c + 3), kw(a, -b, c), kw(2 * a, b, c)]
    return MC(f"In de figuur zie je een parabool met top {pt(p, q)}. Welke formule hoort bij deze parabool?", kw(a, b, c), fout,
              uitwerken(a, b, c) + " Bij de andere formules ligt de top ergens anders of is het een " + ("bergparabool." if a > 0 else "dalparabool."), f)

def q23_tabel_juist(rng, waar):
    a, b, c, p, q = met_top(rng, a_set=A_HEEL)
    x = p + keuze(rng, [-2, -1, 1, 2]); y = val(a, b, c, x)
    zeg = y if waar else y + keuze(rng, [-2, 2, -a * 2, 4])
    if not waar and zeg == y: zeg = y + 1
    return WO(f"Bij de formule {kw(a, b, c)} hoort het punt ({n(x)}, {n(zeg)}).", waar, f"x = {n(x)} invullen: y = {term_inv(a, b, c, x)} = {n(y)}.")

def q23_sproeier(rng, vraag):
    while True:
        k = keuze(rng, [F(-2, 5), F(-1, 2), F(-1, 5), F(-3, 10)]); a0 = keuze(rng, [1, 2, 3]); h0 = keuze(rng, [F(3, 10), F(1, 2), F(1, 5), F(2, 5)])
        b = -2 * k * a0; top = h0 - k * a0 * a0
        if b.denominator <= 10: break
    f = kw(k, b, h0, "a", "h")
    uit = f"a = 0 geeft h = {n(h0)} m = {n(h0 * 100)} cm. Top: {rechts(k, b, 0, 'a')} = 0 → a = 0 of a = {n(2 * a0)}, midden a = {a0}; h = {n(top)} m."
    if vraag == "cm":
        return IN(f"Bij de waterstraal van een tuinsproeier hoort de formule {f}. Hierin is h de hoogte in meters en a de horizontale afstand tot de sproeier in meters. Hoeveel cm hoog is de sproeier zelf (a = 0)?", sleutel(h0 * 100), uit)
    if vraag == "a":
        return IN(f"Bij de waterstraal van een tuinsproeier hoort de formule {f} (h en a in meters). Op welke afstand a bereikt de waterstraal zijn hoogste punt?", sleutel(a0), uit)
    return IN(f"Bij de waterstraal van een tuinsproeier hoort de formule {f} (h en a in meters). Hoeveel meter hoog komt de waterstraal maximaal?", sleutel(top), uit)

def q23_speer(rng):
    k = keuze(rng, [-5, -4, -6]); t0 = keuze(rng, [2, 3, 4]); h0 = keuze(rng, [150, 180, 200, 120])
    b = -2 * k * t0; mx = h0 - k * t0 * t0
    return IN(f"De hoogte h in cm van een speer is h = {k}t² + {b}t + {h0}, met t de tijd in seconden. Hoe hoog komt de speer maximaal (in cm)?",
              sleutel(mx), f"t = 0 geeft h = {h0}. {k}t² + {b}t = 0 → t = 0 of t = {2 * t0}; midden t = {t0}. h = {k} · {t0}² + {b} · {t0} + {h0} = {mx} cm.")

# =====================================================================
# §2.4 De vorm en de ligging van de parabool
# =====================================================================
def los_formule(rng, a=None, b=None, c=None):
    a = a if a is not None else keuze(rng, A_ALLE + [F(-1, 4), F(4), F(-4)])
    b = b if b is not None else F(rng.randint(-9, 9))
    c = c if c is not None else F(rng.randint(-9, 9))
    return a, b, c

def q24_smaller(rng, waar):
    while True:
        a1, b1, c1 = los_formule(rng); a2, b2, c2 = los_formule(rng)
        if abs(a1) != abs(a2): break
    if (abs(a1) > abs(a2)) != waar: (a1, b1, c1), (a2, b2, c2) = (a2, b2, c2), (a1, b1, c1)
    smaller = abs(a1) > abs(a2)
    return WO(f"De parabool bij {kw(a1, b1, c1)} is smaller dan de parabool bij {kw(a2, b2, c2)}.", smaller,
              f"Kijk naar het getal voor x²: {co(a1)} en {co(a2)}. Hoe verder van 0, hoe smaller. {co(a1)} ligt {'verder van' if smaller else 'dichter bij'} 0 dan {co(a2)}, dus de eerste parabool is {'smaller' if smaller else 'breder'}.")

def vier_breedtes(rng):
    while True:
        al = [keuze(rng, [F(1, 4), F(1, 2), F(1), F(2), F(3), F(5), F(1, 3), F(4)]) * keuze(rng, [1, -1]) for _ in range(4)]
        if len({abs(a) for a in al}) == 4: return [(a, F(rng.randint(-8, 8)), F(rng.randint(-8, 8))) for a in al]

def q24_smalst(rng, breedst=False):
    fs = vier_breedtes(rng)
    k = min if breedst else max
    goed = k(fs, key=lambda f: abs(f[0]))
    lijst = ", ".join(kw(*f) for f in fs[:3]) + " en " + kw(*fs[3])
    return MC(f"Gegeven zijn de formules {lijst}. Bij welke formule is de parabool het {'breedst' if breedst else 'smalst'}?", kw(*goed), [kw(*f) for f in fs if f != goed],
              f"Vergelijk de getallen voor x²: {', '.join(co(f[0]) for f in fs)}. {'Het dichtst bij' if breedst else 'Het verst van'} 0 ligt {co(goed[0])}, dus die parabool is het {'breedst' if breedst else 'smalst'}.")

def q24_eigenschap(rng, wat):
    """wat: 'yas' (b = 0, top op y-as) of 'oorsprong' (c = 0)."""
    while True:
        fs = [los_formule(rng) for _ in range(4)]
        if all(f[1] and f[2] for f in fs): break
    i = rng.randrange(4); a, b, c = fs[i]
    fs[i] = (a, F(0), c) if wat == "yas" else (a, b, F(0))
    lijst = ", ".join(kw(*f) for f in fs[:3]) + " en " + kw(*fs[3])
    vraag = f"Gegeven zijn de formules {lijst}. " + ("Bij welke formule ligt de top van de parabool op de y-as?" if wat == "yas" else "Bij welke formule gaat de parabool door de oorsprong?")
    uit = ("Ligt de top op de y-as, dan is b = 0: de formule heeft de vorm y = ax² + c." if wat == "yas"
           else "Gaat de parabool door de oorsprong, dan is c = 0: bij x = 0 hoort y = 0.")
    return MC(vraag, kw(*fs[i]), [kw(*f) for j, f in enumerate(fs) if j != i], uit + f" Dat is {kw(*fs[i])}.")

def q24_snijpunt_yas(rng):
    if rng.random() < 0.5:
        a, b, c = los_formule(rng); c = c or F(5)
        return IN(f"Geef de y-coördinaat van het snijpunt van de parabool bij {kw(a, b, c)} met de y-as.", sleutel(c),
                  f"Bij x = 0 blijft alleen c over: het snijpunt met de y-as is (0, {n(c)}).")
    a, s, t, xt, yt = gefact_param(rng); c = a * s * t
    return IN(f"Geef de y-coördinaat van het snijpunt van de parabool bij {gefact(a, s, t)} met de y-as.", sleutel(c),
              f"Vul x = 0 in: y = {voor(a) + ' · ' if voor(a) not in ('', '−') else voor(a)}(0 − {hk(s)})(0 − {hk(t)}) = {n(c)}. Het snijpunt is (0, {n(c)}).")

def q24_top_yas(rng):
    a = keuze(rng, A_ALLE + [F(-1, 4)]); c = F(rng.randint(-9, 9)) or F(3)
    vorm = keuze(rng, [kw(a, 0, c), poly([(c, ""), (a, "x²")])])
    return MC(f"Wat zijn de coördinaten van de top van de parabool bij {vorm}?", f"(0, {n(c)})", [f"({n(c)}, 0)", f"(0, {n(-c)})", f"({n(a)}, {n(c)})", f"(0, {n(a)})"],
              f"Er is geen term met x (b = 0), dus de top ligt op de y-as: (0, {n(c)}).")

def q24_wo_ligging(rng, waar):
    soort = rng.randrange(3)
    a, b, c = los_formule(rng)
    if soort == 0:
        cc = F(0) if waar else (c or F(4))
        return WO(f"De parabool bij {kw(a, b or F(3), cc)} gaat door de oorsprong.", waar, "Door de oorsprong ⇔ c = 0: bij x = 0 moet y = 0 zijn." + (" Hier is c = 0." if waar else f" Hier is c = {n(cc)}."))
    if soort == 1:
        bb = F(0) if waar else (b or F(-4))
        return WO(f"De top van de parabool bij {kw(a, bb, c or F(2))} ligt op de y-as.", waar, "Top op de y-as ⇔ b = 0 (geen term met x)." + (" Hier is b = 0." if waar else f" Hier is b = {n(bb)}."))
    aa = abs(a) if waar else -abs(a)
    return WO(f"Uit de formule {kw(aa, b, c)} volgt dat de grafiek een dalparabool is.", waar, f"a = {co(aa)} is {'positief → dalparabool' if aa > 0 else 'negatief → bergparabool'}.")

def label_x(fs, xmin, xmax, ymin, ymax, ystap):
    """Per kromme de x van het label: waar de kromme in beeld is, ver van de andere krommen en van de andere labels.
    Afstand in roostereenheden (y gedeeld door ystap), zodat een label nooit tussen twee krommen in staat."""
    xs = [xmin + 0.4 + k * 0.1 for k in range(int((xmax - xmin - 1.2) * 10))]
    gekozen = []
    for i, f in enumerate(fs):
        best, bx = -1, None
        for x in xs:
            y = f(x)
            if not (ymin + 0.8 * ystap <= y <= ymax - 0.8 * ystap): continue
            d_kr = min((abs(g(x) - y) / ystap for j, g in enumerate(fs) if j != i), default=9)
            d_lab = min((((x - gx) ** 2 + ((y - gy) / ystap) ** 2) ** 0.5 for gx, gy in gekozen), default=9)
            d_as = min(abs(x), abs(y) / ystap)          # niet tussen de getallen langs de assen
            score = min(d_kr, 1.5) * 2 + min(d_lab, 2.5) + min(d_as, 1.2) * 1.5
            if score > best: best, bx = score, x
        gekozen.append((bx, f(bx))); 
    return [x for x, _ in gekozen]

def q24_koppel(rng):
    """Vier parabolen in één figuur, elk herkenbaar aan berg/dal, b = 0 of c = 0 en de breedte."""
    sjablonen = [lambda: (F(1), F(0), F(rng.randint(1, 4))), lambda: (F(-1), F(0), F(rng.randint(2, 5))), lambda: (F(1), F(-rng.choice([2, 4])), F(0)),
                 lambda: (F(-1), F(rng.choice([2, 4])), F(0)), lambda: (F(3), F(0), F(-rng.randint(1, 3))), lambda: (F(-2), F(0), F(-1))]
    while True:
        idx = rng.sample(range(6), 4); fs = [sjablonen[i]() for i in idx]
        if len({(f[0], f[2]) for f in fs if f[1] == 0}) == sum(1 for f in fs if f[1] == 0): break
    fig = figuur([(para(*f), str(j + 1), x) for j, (f, x) in enumerate(zip(fs, label_x([para(*f) for f in fs], -5, 5, -8, 8, 2)))], -5, 5, -8, 8, ystap=2)
    k = rng.randrange(4); a, b, c = fs[k]
    eig = [("dalparabool" if a > 0 else "bergparabool")]
    if b == 0: eig.append(f"top op de y-as in (0, {n(c)})")
    if c == 0: eig.append("door de oorsprong")
    if abs(a) != 1: eig.append(f"{'smaller' if abs(a) > 1 else 'breder'} dan y = x²")
    return MC(f"In de figuur staan vier parabolen. Welke parabool hoort bij de formule {kw(a, b, c)}?", f"parabool {k + 1}",
              [f"parabool {j + 1}" for j in range(4) if j != k], f"{kw(a, b, c)}: " + ", ".join(eig) + f". Dat past alleen bij parabool {k + 1}.", fig)

# =====================================================================
# §2.5 Drie vormen van kwadratische formules
# =====================================================================
def q25_gef_mc(rng):
    a, s, t, xt, yt = gefact_param(rng, a_set=(F(2), F(-2), F(3), F(-3), F(-1), F(1, 2), F(-1, 2)))
    A, B, C = a, -a * (s + t), a * s * t
    fout = [kw(A, -(s + t), s * t), kw(A, a * (s + t), C), kw(A, B, -C), kw(F(1), B, C), kw(A, -a * (s - t), -C)]
    return MC(f"Schrijf de formule {gefact(a, s, t)} zonder haakjes.", kw(A, B, C), fout,
              f"Eerst {fac(s)}{fac(t)} = {rechts(1, -(s + t), s * t)}. Dan elke term keer {n(a)}: {kw(A, B, C)}.")

def q25_gef_coef(rng, welke):
    a, s, t, xt, yt = gefact_param(rng, a_set=(F(2), F(-2), F(3), F(-3), F(-1), F(-1, 2), F(1, 2), F(4)))
    A, B, C = a, -a * (s + t), a * s * t
    w = {"b": B, "c": C}[welke]
    if w == 0: return q25_gef_coef(rng, "c" if welke == "b" else "b")
    return IN(f"Schrijf {gefact(a, s, t)} in de vorm y = ax² + bx + c. Hoe groot is {welke}?", sleutel(w),
              f"{fac(s)}{fac(t)} = {rechts(1, -(s + t), s * t)}; keer {n(a)} geeft {kw(A, B, C)}, dus {welke} = {n(w)}.")

def topvorm_param(rng):
    while True:
        a = keuze(rng, [F(2), F(-2), F(3), F(-3), F(-1), F(1, 2), F(-1, 2), F(4), F(1, 4)]); p = F(rng.randint(-6, 6)); q = F(rng.randint(-20, 20))
        if p == 0: continue
        if (a * p * p + q).denominator == 1 and (2 * a * p).denominator == 1: return a, p, q

def q25_top_mc(rng):
    a, p, q = topvorm_param(rng)
    A, B, C = a, -2 * a * p, a * p * p + q
    fout = [kw(A, 0, a * p * p + q), kw(A, B, a * p * p), kw(A, B, a * (p * p + q)), kw(A, -p * 2, p * p + q), kw(A, -B, C)]
    return MC(f"Schrijf de formule {topvorm(a, p, q)} zonder haakjes.", kw(A, B, C), fout,
              f"{fac(p)}² = {fac(p)}{fac(p)} = {rechts(1, -2 * p, p * p)} (niet x² + {n(p * p)}!). Keer {n(a)}: {rechts(a, -2 * a * p, a * p * p)}. Daarna {'+' if q >= 0 else '−'} {n(abs(q))}: {kw(A, B, C)}.")

def q25_top_coef(rng, welke):
    a, p, q = topvorm_param(rng)
    A, B, C = a, -2 * a * p, a * p * p + q
    w = {"b": B, "c": C}[welke]
    return IN(f"Schrijf {topvorm(a, p, q)} in de vorm y = ax² + bx + c. Hoe groot is {welke}?", sleutel(w),
              f"{fac(p)}² = {rechts(1, -2 * p, p * p)}; keer {n(a)} → {rechts(a, -2 * a * p, a * p * p)}; {'+' if q >= 0 else '−'} {n(abs(q))} → {kw(A, B, C)}. Dus {welke} = {n(w)}.")

def q25_topvorm_top(rng):
    a, p, q = topvorm_param(rng)
    return MC(f"Wat zijn de coördinaten van de top van de parabool bij {topvorm(a, p, q)}?", pt(p, q), [pt(-p, q), pt(p, -q), pt(-p, -q), pt(q, p)],
              f"Bij x = {n(p)} is {fac(p)}² = 0; dat is de kleinste (of grootste) waarde. Dan is y = {n(q)}. Top {pt(p, q)}. Let op: bij (x − {n(abs(p))}) hoort x = {n(abs(p))}, bij (x + {n(abs(p))}) hoort x = −{n(abs(p))}.")

def q25_hangmat(rng, vraag):
    k = keuze(rng, [F(1, 4), F(1, 5), F(1, 2)]); m = keuze(rng, [F(12, 5), F(2), F(5, 2), F(3)]); q = keuze(rng, [F(1, 2), F(2, 5), F(3, 5)])
    h0 = k * m * m + q
    f = f"h = {n(k)}(a − {n(m)})² + {n(q)}"
    uit = f"Het laagste punt is de top (a = {n(m)}): h = {n(q)} m = {n(q * 100)} cm. Bij de boom (a = 0): h = {n(k)} · {n(m)}² + {n(q)} = {n(h0)} m. De andere boom staat even ver aan de andere kant: a = {n(2 * m)} m."
    if vraag == "laag":
        return IN(f"De vorm van een hangmat tussen twee bomen past bij de formule {f}. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?", sleutel(q * 100), uit)
    if vraag == "boom":
        return IN(f"Een hangmat hangt volgens {f} (h en a in meters, a vanaf de linkerboom). Op welke hoogte in meters is de hangmat aan de boom vastgeknoopt?", sleutel(h0), uit)
    return IN(f"Een hangmat hangt volgens {f} (h en a in meters, a vanaf de linkerboom, symmetrisch tussen de bomen). Hoeveel meter staan de bomen uit elkaar?", sleutel(2 * m), uit)

def q25_winst(rng):
    k = keuze(rng, [F(-3, 5), F(-1, 2), F(-2, 5), F(-1, 5)]); s = keuze(rng, [100, 200, 300]); t = s + keuze(rng, [100, 150, 200])
    mid = F(s + t, 2); W = k * (mid - s) * (mid - t)
    return IN(f"De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = {n(k)}(q − {s})(q − {t}). Bereken de maximale winst in euro.", sleutel(W),
              f"Snijpunten met de horizontale as: q = {s} en q = {t}. Midden: q = {n(mid)}. W = {n(k)} · ({n(mid)} − {s})({n(mid)} − {t}) = {n(W)} euro.")

def q25_bergdal(rng, waar):
    if rng.random() < 0.5:
        a, p, q = topvorm_param(rng); vorm = topvorm(a, p, q)
    else:
        a, s, t, _, _ = gefact_param(rng, a_set=(F(2), F(-2), F(-1), F(1, 2), F(-1, 2), F(3))); vorm = gefact(a, s, t)
    return WO(f"De grafiek bij {vorm} is een {bd(a) if waar else bd(-a)}.", waar, f"Zonder haakjes is het getal voor x² gelijk aan {co(a)}: een {bd(a)}.")

# =====================================================================
# Begrippen
# =====================================================================
BEGRIP_MC = [
    ("Hoe heet de grafiek bij een kwadratische formule?", "een parabool", ["een rechte lijn", "een hyperbool", "een exponentiële kromme"], "De grafiek bij een kwadratische formule zoals y = x² − 4x + 1 is een parabool."),
    ("Wanneer is de grafiek bij y = ax² + bx + c een dalparabool?", "als a positief is", ["als a negatief is", "als c positief is", "als b gelijk is aan 0"], "a > 0: dalparabool (opening naar boven). a < 0: bergparabool."),
    ("Wat is de top van een bergparabool?", "het hoogste punt van de parabool", ["het laagste punt van de parabool", "het snijpunt met de y-as", "het snijpunt met de x-as"], "Bij een bergparabool is de top het hoogste punt, bij een dalparabool het laagste punt."),
    ("Wat is de symmetrieas van een parabool?", "de verticale lijn door de top", ["de horizontale lijn door de top", "de y-as", "de lijn door de snijpunten met de x-as"], "De parabool is symmetrisch in de verticale lijn door de top: x = x-coördinaat van de top."),
    ("Wat is de algemene vorm van een kwadratische formule?", "y = ax² + bx + c", ["y = ax + b", "y = a(x − p)² + q", "y = b · gᵗ"], "y = ax² + bx + c is de algemene vorm. De vormen y = a(x − s)(x − t) en y = a(x − p)² + q kun je daarin omschrijven."),
    ("Wat geeft het getal c in y = ax² + bx + c aan?", "het snijpunt met de y-as is (0, c)", ["de top is (0, c)", "het snijpunt met de x-as is (c, 0)", "hoe breed de parabool is"], "Bij x = 0 blijft y = c over: het snijpunt met de y-as is (0, c)."),
    ("Wat weet je als in y = ax² + bx + c geldt b = 0?", "de top ligt op de y-as", ["de parabool gaat door de oorsprong", "de grafiek is een rechte lijn", "de parabool is een bergparabool"], "b = 0 geeft y = ax² + c; de top is (0, c) en ligt op de y-as."),
    ("Wat weet je als in y = ax² + bx + c geldt c = 0?", "de parabool gaat door (0, 0)", ["de top van de parabool ligt op de y-as", "de parabool raakt de x-as nergens", "de top van de parabool ligt op de x-as"], "c = 0 geeft y = ax² + bx; bij x = 0 is y = 0, dus de parabool gaat door (0, 0)."),
    ("Welke parabool is het smalst?", "y = −4x² + 1", ["y = 2x² + 1", "y = −½x² + 1", "y = x² + 1"], "Hoe verder a van 0 af ligt, hoe smaller. −4 ligt het verst van 0."),
    ("Wat betekent ‘haakjes wegwerken’?", "alles met elkaar vermenigvuldigen tot er geen haakjes meer staan", ["de haakjes weglaten en de getallen laten staan zoals ze zijn", "de formule ontbinden in factoren, dus juist haakjes maken", "x = 0 invullen en uitrekenen wat er overblijft"], "Bijvoorbeeld (x + 3)(x − 4) = x² − 4x + 3x − 12 = x² − x − 12. Een vermenigvuldigtabel helpt."),
    ("Bij welke formule kun je de snijpunten met de x-as direct aflezen?", "y = a(x − s)(x − t)", ["y = ax² + bx + c", "y = a(x − p)² + q", "y = ax² + c"], "Uit a(x − s)(x − t) = 0 volgt x = s of x = t: de snijpunten (s, 0) en (t, 0)."),
    ("Bij welke formule kun je de top direct aflezen?", "y = a(x − p)² + q", ["y = a(x − s)(x − t)", "y = ax² + bx + c", "y = ax² + bx"], "De top van y = a(x − p)² + q is (p, q)."),
    ("Hoe vind je met de snijpunten met de x-as de x-coördinaat van de top?", "neem het getal midden tussen de twee x-coördinaten", ["tel de twee x-coördinaten op", "neem de grootste x-coördinaat", "vul x = 0 in"], "De top ligt op de symmetrieas, precies midden tussen de twee snijpunten met de x-as."),
    ("Wat is een kwadratische formule?", "een formule met x² als hoogste macht", ["een formule waarin x² niet voorkomt, alleen x", "een formule van de vorm y = ax + b, een rechte lijn", "een formule met een groeifactor, zoals y = 3 · 2ˣ"], "Kwadratisch: x² is de hoogste macht, bijvoorbeeld y = 3x² − x + 2."),
    ("Wat zijn de snijpunten van een parabool met de x-as?", "de punten waar y = 0", ["de punten waar x = 0", "de top en het snijpunt met de y-as", "de punten waar x = y"], "Op de x-as is y = 0. Los dus de vergelijking y = 0 op."),
    ("Wat is een vermenigvuldigtabel?", "een schema om haakjes weg te werken", ["een tabel met x- en y-waarden om een grafiek te tekenen", "een tabel waarin je de coördinaten van de top afleest", "een tabel met de tafels van vermenigvuldiging van 1 tot 10"], "In het schema zet je bijvoorbeeld x en +3 tegen x en −4: x², −4x, +3x en −12."),
    ("Wat betekent ‘ontbinden in factoren’ bij x² − 6x?", "schrijven als x(x − 6)", ["de haakjes wegwerken tot er geen haakjes meer staan", "x = 6 invullen en uitrekenen", "schrijven als x² + 6x, met een plusteken"], "Ontbinden is het omgekeerde van haakjes wegwerken: x² − 6x = x(x − 6)."),
    ("Waarom moet een parabool bij de top vloeiend (rond) lopen?", "omdat een parabool geen hoeken heeft", ["omdat de top van een parabool altijd op de y-as ligt", "omdat je anders de symmetrieas van de parabool niet ziet", "omdat de y-waarden in de tabel dan precies kloppen"], "Een parabool is een gladde kromme; verbind de punten bij de top niet met rechte stukjes."),
    ("Hoe bereken je de y-coördinaat van de top als je de x-coördinaat weet?", "vul de x-coördinaat in de formule in", ["deel de x-coördinaat van de top door 2", "neem het getal c uit de formule y = ax² + bx + c", "los de vergelijking y = 0 op met ontbinden in factoren"], "Stap 4 van de aanpak: x-coördinaat van de top invullen in de formule."),
]
BEGRIP_IN = [
    ("Hoe heet het hoogste of laagste punt van een parabool? (één woord)", "top|de top", "Het hoogste punt van een bergparabool en het laagste punt van een dalparabool heet de top."),
    ("Een parabool met de opening naar boven (laagste punt = top) heet een …parabool. Vul in.", "dal|dalparabool|een dalparabool", "Opening naar boven: dalparabool (a > 0)."),
    ("Een parabool met de opening naar beneden heet een …parabool. Vul in.", "berg|bergparabool|een bergparabool", "Opening naar beneden: bergparabool (a < 0)."),
    ("Hoe heet de lijn waarin een parabool symmetrisch is? (één woord)", "symmetrieas|de symmetrieas", "De symmetrieas is de verticale lijn door de top."),
    ("Het punt (0, 0) heet de …", "oorsprong|de oorsprong", "(0, 0) is de oorsprong. Bij c = 0 gaat de parabool erdoor."),
]

def q_begrip_mc(rng, i):
    v, g, f, u = BEGRIP_MC[i]; return MC(v, g, f, u)
def q_begrip_in(rng, i):
    v, a, u = BEGRIP_IN[i]; return IN(v, a, u)
def q_begrip_wo(rng, i):
    stellingen = [("Bij y = −3x² + 6x hoort een dalparabool.", False, "a = −3 is negatief: een bergparabool."),
                  ("Bij y = ½x² − 4 ligt de top op de y-as.", True, "b = 0, dus de top is (0, −4) op de y-as."),
                  ("De parabool bij y = 2x² − 8x gaat door de oorsprong.", True, "c = 0: bij x = 0 is y = 0."),
                  ("De parabool bij y = 5x² + 1 is breder dan die bij y = x² + 1.", False, "5 ligt verder van 0 dan 1, dus y = 5x² + 1 is smaller."),
                  ("De symmetrieas van een parabool gaat door de top.", True, "De symmetrieas is de verticale lijn door de top."),
                  ("(x + 4)² is hetzelfde als x² + 16.", False, "(x + 4)² = (x + 4)(x + 4) = x² + 8x + 16. De term 8x vergeet je snel."),
                  ("De top van y = 3(x − 2)² + 5 is (2, 5).", True, "y = a(x − p)² + q heeft top (p, q) = (2, 5)."),
                  ("Bij y = (x − 3)(x + 6) snijdt de parabool de x-as in (−3, 0) en (6, 0).", False, "(x − 3) = 0 geeft x = 3 en (x + 6) = 0 geeft x = −6: (3, 0) en (−6, 0).")]
    v, w, u = stellingen[i]; return WO(v, w, u)

# =====================================================================
# Theorie (onderwerpen)
# =====================================================================
FB = '<div class="formule-box">'
THEORIE = {
"2.1": ("Bergparabool of dalparabool", "Aan het getal voor x² zie je of de grafiek een bergparabool of een dalparabool is — soms pas na haakjes wegwerken.",
"<h3>§2.1 Parabolen</h3>\n<p>Een formule waarin x² de hoogste macht is, heet een <b>kwadratische formule</b>, bijvoorbeeld y = x² − 4x − 8 of y = −2x² + 12. "
"De grafiek bij zo'n formule heet een <b>parabool</b>. Een parabool is symmetrisch: links en rechts van de <b>top</b> zie je dezelfde vorm in spiegelbeeld.</p>\n"
"<h4>Bergparabool of dalparabool?</h4>\n" + FB + "Getal voor x² <b>positief</b> → <b>dalparabool</b> (opening naar boven, de top is het laagste punt)<br>"
"Getal voor x² <b>negatief</b> → <b>bergparabool</b> (opening naar beneden, de top is het hoogste punt)</div>\n"
"<p>Voorbeelden: y = ½x² + 2 is een dalparabool (½ is positief). y = −½x² + 2x is een bergparabool. De volgorde van de termen maakt niet uit: bij y = −4x + 5x² staat er 5 voor x², dus een dalparabool. "
"Let op: bij y = x² − 7x + 5 staat er een (onzichtbare) 1 voor x²; bij y = −x² + 12x + 7 een −1.</p>\n"
"<h4>Eerst de haakjes wegwerken</h4>\n<p>Staan er haakjes in de formule, dan zie je het getal voor x² niet meteen. Schrijf de formule dan eerst <b>zonder haakjes</b> en tel de termen met x² bij elkaar op. "
"Een <b>vermenigvuldigtabel</b> helpt om niets te vergeten.</p>\n" + FB + "Voorbeeld: y = (2x + 7)(3 − x) + 3x²<br>(2x + 7)(3 − x) = 6x − 2x² + 21 − 7x = −2x² − x + 21<br>"
"y = −2x² − x + 21 + 3x² = x² − x + 21 → getal voor x² is 1 → <b>dalparabool</b></div>\n"
"<p>Veelgemaakte fouten:</p><ul><li>(2x − 1)² is níet 4x² + 1, maar (2x − 1)(2x − 1) = 4x² − 4x + 1.</li><li>Bij −x(x − 8) wordt het −x² + 8x: het minteken gaat over beide termen.</li>"
"<li>Vergeet de losse term met x² achter de haakjes niet (bijvoorbeeld + 3x² of − 2x²).</li></ul>\n"
"<h4>In context</h4><p>De baan van een geschoten of gegooide bal is een bergparabool. Bij h = −0,3a(a − 8) + 2,1 werk je de haakjes weg: h = −0,3a² + 2,4a + 2,1. "
"Het getal voor a² is negatief, dus deze formule kan bij een bal horen. Bij h = 0,3a(a − 8) + 2,1 is het getal positief: een dalparabool, en dat past niet bij een bal.</p>"),
"2.2": ("Symmetrie en top", "Bereken de coördinaten van de top met het snijpunt met de y-as en de symmetrie, of met de snijpunten met de x-as.",
"<h3>§2.2 Symmetrie en top</h3>\n<p>De <b>top</b> van een parabool ligt op de <b>symmetrieas</b>, de verticale lijn door de top. Twee punten van de parabool met dezelfde y-coördinaat liggen even ver links en rechts van de symmetrieas. "
"Daarom ligt de top precies <b>midden</b> tussen twee van zulke punten.</p>\n<h4>Aanpak: coördinaten van de top berekenen</h4>\n<ol><li>Bereken de y-coördinaat van het snijpunt met de y-as (vul x = 0 in: dat geeft c).</li>"
"<li>Er is een ander punt met dezelfde y-coördinaat. Stel de vergelijking op en los hem op.</li><li>De x-coördinaat van de top ligt midden tussen de twee oplossingen.</li>"
"<li>Vul de x-coördinaat van de top in de formule in: dat geeft de y-coördinaat.</li><li>Schrijf de coördinaten van de top op.</li></ol>\n"
+ FB + "Voorbeeld: y = x² + 8x − 3<br>1 x = 0 → y = −3<br>2 x² + 8x − 3 = −3 → x² + 8x = 0 → x(x + 8) = 0 → x = 0 of x = −8<br>3 midden tussen 0 en −8: x = −4<br>4 y = (−4)² + 8 · −4 − 3 = −19<br>5 top (−4, −19)</div>\n"
"<h4>Snijpunten met de x-as gebruiken</h4>\n<p>Staat de formule in de vorm y = (x − 3)(x + 7), dan is het handiger om de snijpunten met de x-as te gebruiken: (x − 3)(x + 7) = 0 geeft x = 3 of x = −7. "
"De top ligt midden tussen 3 en −7, dus bij x = (3 + −7) / 2 = −2. Invullen: y = (−2 − 3)(−2 + 7) = −5 · 5 = −25. Top (−2, −25).</p>\n"
"<p><b>Let op het teken:</b> bij de factor (x + 7) hoort x = −7, niet 7.</p>\n<h4>In context</h4><p>Bij een tunnel met h = 4,8a − 0,8a² los je 4,8a − 0,8a² = 0 op: a(4,8 − 0,8a) = 0, dus a = 0 of a = 6. "
"De tunnel is 6 meter breed en in het midden (a = 3) is hij h = 4,8 · 3 − 0,8 · 9 = 7,2 meter hoog.</p>"),
"2.3": ("Parabolen tekenen", "Teken een parabool met de top en een tabel met hele getallen rondom de x-coördinaat van de top.",
"<h3>§2.3 Parabolen tekenen</h3>\n<p>Een mooie, symmetrische parabool teken je niet met een willekeurige tabel: kies je x = −3 tot en met 3 terwijl de top bij x = 5 ligt, dan zie je de top niet eens. Kies de x-waarden zó dat de top in het midden van de tabel staat.</p>\n"
"<h4>Aanpak: een parabool tekenen</h4>\n<ol><li>Bereken de coördinaten van de top (zie §2.2).</li><li>Maak een tabel: kies voor x opeenvolgende hele getallen rondom de x-coördinaat van de top. Neem indien mogelijk ook het snijpunt met de y-as op.</li>"
"<li>Teken de punten en verbind ze met een vloeiende kromme. Zorg dat de parabool bij de top <b>rond</b> loopt, niet met een punt.</li></ol>\n"
+ FB + "Voorbeeld: y = 2x² − 4x − 8<br>x = 0 → y = −8; 2x² − 4x = 0 → x = 0 of x = 2; top bij x = 1: y = 2 − 4 − 8 = −10 → top (1, −10)<br>"
"tabel: x = −2, −1, 0, 1, 2, 3, 4 → y = 8, −2, −8, −10, −8, −2, 8</div>\n"
"<h4>Symmetrie in de tabel</h4><p>In een goede tabel zie je de symmetrie terug: links en rechts van de top staan dezelfde y-waarden. Ligt de top bij x = 3 en hoort bij x = 1 de waarde y = 7, dan hoort bij x = 5 ook y = 7. "
"Zo kun je je tabel controleren of sneller invullen.</p>\n<h4>Symmetrieas</h4><p>De symmetrieas is de lijn x = x-coördinaat van de top, bijvoorbeeld x = 1. Je geeft hem als formule: <b>x = 1</b>.</p>\n"
"<h4>In context</h4><p>Bij een tuinsproeier met h = −0,4a² + 1,6a + 0,3 geeft a = 0 de hoogte van de sproeier zelf: 0,3 m = 30 cm. "
"Uit −0,4a² + 1,6a = 0 volgt a = 0 of a = 4, dus het hoogste punt van de waterstraal is bij a = 2: h = −1,6 + 3,2 + 0,3 = 1,9 m.</p>"),
"2.4": ("De vorm en de ligging van de parabool", "Uit a, b en c in y = ax² + bx + c lees je af: berg of dal, smal of breed, top op de y-as, door de oorsprong.",
"<h3>§2.4 De vorm en de ligging van de parabool</h3>\n<p>De formule <b>y = ax² + bx + c</b> heet de <b>algemene vorm</b> van een kwadratische formule. Zonder te tekenen kun je uit de getallen a, b en c al veel over de parabool zeggen.</p>\n"
"<h4>De vorm: kijk naar a</h4>\n" + FB + "a &gt; 0 → dalparabool, a &lt; 0 → bergparabool<br>Hoe <b>verder a van 0</b> af ligt, hoe <b>smaller</b> de parabool. Hoe <b>dichter a bij 0</b>, hoe <b>breder</b>.</div>\n"
"<p>Voorbeeld: y = −2x² + 3 is smaller dan y = x² − 4x, want −2 ligt verder van 0 dan 1. En y = ½x² + 2x + 2 is breder dan y = 4x² + x, want ½ ligt dichter bij 0 dan 4. "
"Het teken telt hierbij niet mee: −3 en 3 geven even brede parabolen.</p>\n<h4>De ligging: kijk naar b en c</h4>\n<ul><li>Het snijpunt met de y-as is altijd <b>(0, c)</b> (vul x = 0 in).</li>"
"<li>Is <b>b = 0</b>, dan is de formule y = ax² + c. De top ligt dan <b>op de y-as</b>: de top is (0, c). Voorbeeld: y = 2x² − 5 heeft top (0, −5).</li>"
"<li>Is <b>c = 0</b>, dan is de formule y = ax² + bx. De parabool gaat dan <b>door de oorsprong</b> (0, 0). Voorbeeld: y = 4x² − 8x.</li></ul>\n"
"<h4>Parabolen herkennen</h4><p>Moet je bij een figuur met meerdere parabolen de juiste formule zoeken, werk dan stap voor stap: berg of dal (teken van a)? Top op de y-as (b = 0)? Door de oorsprong (c = 0)? Waar snijdt hij de y-as (c)? "
"Smal of breed (grootte van a)? Meestal blijft er dan maar één parabool over.</p>\n<p>Ook in context werkt dit: twee ballen met h = −0,75a² + … en h = −0,9a² + … — de tweede baan is smaller, want −0,9 ligt verder van 0.</p>"),
"2.5": ("Drie vormen van kwadratische formules", "Schrijf y = a(x − s)(x − t) en y = a(x − p)² + q in de vorm y = ax² + bx + c.",
"<h3>§2.5 Drie vormen van kwadratische formules</h3>\n<p>Een kwadratische formule kan op drie manieren geschreven zijn:</p>\n" + FB +
"y = ax² + bx + c — algemene vorm: snijpunt met de y-as (0, c)<br>y = a(x − s)(x − t) — snijpunten met de x-as (s, 0) en (t, 0)<br>y = a(x − p)² + q — top (p, q)</div>\n"
"<p>In alle drie de vormen is a hetzelfde getal: het bepaalt berg/dal en smal/breed.</p>\n<h4>Van y = a(x − s)(x − t) naar de algemene vorm</h4>\n<p>Werk eerst de haakjes (x − s)(x − t) weg met een vermenigvuldigtabel. Vermenigvuldig daarna <b>elke term</b> met a.</p>\n"
+ FB + "y = −2(x + 3)(x − 4)<br>(x + 3)(x − 4) = x² − 4x + 3x − 12 = x² − x − 12<br>y = −2(x² − x − 12) = −2x² + 2x + 24</div>\n"
"<h4>Van y = a(x − p)² + q naar de algemene vorm</h4>\n<p>(x − p)² betekent (x − p)(x − p). Werk dat uit, vermenigvuldig elke term met a en tel q er pas daarna bij op.</p>\n"
+ FB + "y = 2(x + 3)² + 4<br>(x + 3)² = x² + 6x + 9<br>y = 2(x² + 6x + 9) + 4 = 2x² + 12x + 18 + 4 = 2x² + 12x + 22</div>\n"
"<p>Veelgemaakte fouten: (x + 3)² = x² + 9 (de middelste term 6x vergeten); alleen x² met a vermenigvuldigen; q óók met a vermenigvuldigen. "
"Controleer je antwoord door een getal in te vullen, bijvoorbeeld x = 0 of x = 1, in beide formules.</p>\n<h4>In context</h4><p>Bij een hangmat met h = 0,25(a − 2,4)² + 0,5 lees je de top direct af: het laagste punt ligt bij a = 2,4 op 0,5 m = 50 cm hoogte. "
"Bij een winstformule W = −0,6(q − 300)(q − 450) zijn q = 300 en q = 450 de aantallen waarbij de winst 0 is; de maximale winst hoort bij q = 375.</p>"),
}
THEORIE_BEGRIP = ("<h3>Begrippen H2 · Parabolen</h3>\n<p>Alle begrippen uit hoofdstuk 2 op een rij. Ken je ze, dan begrijp je de opdrachten in de toets meteen.</p>\n"
"<ul><li><b>kwadratische formule</b> — formule met x² als hoogste macht, zoals y = x² − 4x + 1.</li><li><b>parabool</b> — de grafiek bij een kwadratische formule.</li>"
"<li><b>dalparabool</b> — opening naar boven; het getal voor x² is positief; de top is het laagste punt.</li><li><b>bergparabool</b> — opening naar beneden; het getal voor x² is negatief; de top is het hoogste punt.</li>"
"<li><b>top</b> — het hoogste (bergparabool) of laagste (dalparabool) punt van de parabool.</li><li><b>symmetrieas</b> — de verticale lijn door de top, bijvoorbeeld x = 3.</li>"
"<li><b>snijpunt met de y-as</b> — het punt (0, c); je vindt het door x = 0 in te vullen.</li><li><b>snijpunten met de x-as</b> — punten (…, 0); je vindt ze door y = 0 te stellen en de vergelijking op te lossen.</li>"
"<li><b>oorsprong</b> — het punt (0, 0). Bij c = 0 gaat de parabool erdoor.</li><li><b>algemene vorm</b> — y = ax² + bx + c.</li>"
"<li><b>vorm y = a(x − s)(x − t)</b> — hieruit lees je de snijpunten met de x-as af: (s, 0) en (t, 0).</li><li><b>vorm y = a(x − p)² + q</b> — hieruit lees je de top (p, q) af.</li>"
"<li><b>smaller / breder</b> — hoe verder a van 0, hoe smaller; hoe dichter bij 0, hoe breder.</li><li><b>haakjes wegwerken</b> — een formule zonder haakjes schrijven, bijvoorbeeld met een <b>vermenigvuldigtabel</b>.</li>"
"<li><b>ontbinden in factoren</b> — het omgekeerde: x² + 8x = x(x + 8). Handig om ax² + bx = 0 op te lossen.</li><li><b>kwadratische vergelijking</b> — vergelijking met x², bijvoorbeeld x² − 6x = 0 of (x − 3)(x + 7) = 0.</li></ul>\n"
"<h4>De aanpak voor de top in vijf stappen</h4><ol><li>Snijpunt met de y-as: x = 0 → y = c.</li><li>Ander punt met y = c: los ax² + bx = 0 op.</li><li>x-coördinaat van de top = midden tussen de oplossingen.</li>"
"<li>y-coördinaat: x-coördinaat invullen.</li><li>Coördinaten opschrijven.</li></ol>")

# =====================================================================
# Plannen
# =====================================================================
Q = {
    "wo21": q21_wo_los, "h21": q21_haakjes_a, "hwo21": q21_haakjes_wo, "mc21": q21_mc_soort, "fig21": q21_figuur, "ctx21": q21_context,
    "tx": q22_top_x, "ty": q22_top_y, "tmc": q22_top_mc, "zh": q22_zelfde_hoogte, "gx": q22_gef_x, "gy": q22_gef_y, "snx": q22_snijx,
    "bz": q22_b_zoeken, "tunB": lambda r: q22_tunnel(r, "breed"), "tunH": lambda r: q22_tunnel(r, "hoog"), "brug": q22_hangbrug,
    "tw": q23_tabelwaarde, "ts": q23_symmetrie_tabel, "sa": q23_symmetrieas, "wf": q23_welke_formule,
    "spC": lambda r: q23_sproeier(r, "cm"), "spA": lambda r: q23_sproeier(r, "a"), "spH": lambda r: q23_sproeier(r, "h"), "speer": q23_speer,
    "smal": q24_smalst, "breed": lambda r: q24_smalst(r, True), "yas": lambda r: q24_eigenschap(r, "yas"), "oors": lambda r: q24_eigenschap(r, "oorsprong"),
    "syas": q24_snijpunt_yas, "topy": q24_top_yas, "kop": q24_koppel,
    "gmc": q25_gef_mc, "gb": lambda r: q25_gef_coef(r, "b"), "gc": lambda r: q25_gef_coef(r, "c"), "pmc": q25_top_mc,
    "pb": lambda r: q25_top_coef(r, "b"), "pc": lambda r: q25_top_coef(r, "c"), "ptop": q25_topvorm_top,
    "hmL": lambda r: q25_hangmat(r, "laag"), "hmB": lambda r: q25_hangmat(r, "boom"), "hmA": lambda r: q25_hangmat(r, "afstand"), "winst": q25_winst,
}
WOQ = {"wo21": q21_wo_los, "hwo21": q21_haakjes_wo, "tab": q23_tabel_juist, "sm": q24_smaller, "lig": q24_wo_ligging, "bd25": q25_bergdal}

TOETSEN = [  # (paragraaf, naam, plan)
    ("2.1", "§2.1 Bergparabool of dalparabool (1/2)", ["wo21:T", "wo21:F", "mc21", "h21", "hwo21:F", "fig21", "wo21:F", "h21", "ctx21", "hwo21:T", "mc21", "h21", "fig21", "wo21:T", "hwo21:F", "h21", "ctx21", "mc21", "hwo21:T", "h21"]),
    ("2.1", "§2.1 Bergparabool of dalparabool (2/2)", ["h21", "fig21", "hwo21:T", "mc21", "wo21:F", "h21", "ctx21", "hwo21:F", "fig21", "h21", "wo21:T", "mc21", "h21", "hwo21:T", "ctx21", "h21", "fig21", "hwo21:F", "mc21", "h21"]),
    ("2.2", "§2.2 Symmetrie en top (1/2)", ["zh", "tx", "ty", "tmc", "snx", "gx", "gy", "tx", "tmc", "zh", "ty", "gx", "snx", "tunB", "tunH", "tmc", "gy", "bz", "brug", "ty"]),
    ("2.2", "§2.2 Symmetrie en top (2/2)", ["tmc", "ty", "gx", "snx", "zh", "tx", "gy", "tmc", "bz", "tunH", "ty", "gy", "snx", "tx", "brug", "tmc", "gx", "tunB", "bz", "ty"]),
    ("2.3", "§2.3 Parabolen tekenen (1/2)", ["tw", "ts", "sa", "wf", "tab:T", "tw", "tab:F", "wf", "sa", "ts", "spC", "tw", "wf", "tab:F", "spA", "ts", "sa", "spH", "speer", "tw"]),
    ("2.3", "§2.3 Parabolen tekenen (2/2)", ["wf", "tw", "tab:F", "ts", "sa", "wf", "tw", "spH", "tab:T", "ts", "speer", "wf", "sa", "tw", "spC", "tab:F", "ts", "spA", "wf", "tw"]),
    ("2.4", "§2.4 De vorm en de ligging van de parabool (1/2)", ["sm:T", "smal", "yas", "oors", "syas", "topy", "kop", "lig:T", "breed", "sm:F", "kop", "syas", "lig:F", "yas", "oors", "smal", "topy", "kop", "lig:T", "syas"]),
    ("2.4", "§2.4 De vorm en de ligging van de parabool (2/2)", ["kop", "breed", "oors", "sm:F", "syas", "yas", "lig:F", "smal", "kop", "topy", "sm:T", "syas", "oors", "lig:T", "breed", "kop", "yas", "lig:F", "smal", "syas"]),
    ("2.5", "§2.5 Drie vormen van kwadratische formules (1/2)", ["gmc", "gb", "gc", "pmc", "pb", "pc", "ptop", "bd25:T", "gmc", "gc", "pmc", "pb", "hmL", "bd25:F", "gb", "pc", "winst", "ptop", "hmB", "gmc"]),
    ("2.5", "§2.5 Drie vormen van kwadratische formules (2/2)", ["pmc", "gc", "pb", "gmc", "ptop", "gb", "pc", "bd25:F", "hmA", "pmc", "gb", "gc", "winst", "bd25:T", "pc", "gmc", "hmL", "ptop", "pb", "pmc"]),
    ("begrippen", "Begrippentoets H2 Parabolen", None),
    ("mix", "Gemengd H2 — oefenproefwerk-niveau (1/2)", ["hwo21:F", "h21", "tmc", "ty", "gx", "tw", "wf", "kop", "yas", "smal", "gmc", "pc", "ptop", "spH", "tunB", "oors", "bz", "hmL", "sa", "winst"]),
    ("mix", "Gemengd H2 — oefenproefwerk-niveau (2/2)", ["mc21", "fig21", "tx", "gy", "snx", "ts", "wf", "kop", "breed", "syas", "pmc", "gb", "hwo21:T", "brug", "speer", "lig:F", "topy", "pb", "hmB", "tmc"]),
]
ONDERWERP_PLAN = {
    "2.1": ["wo21:T", "mc21", "h21", "hwo21:F", "fig21", "wo21:F", "ctx21", "h21", "hwo21:T", "mc21", "fig21", "h21"],
    "2.2": ["zh", "tx", "ty", "tmc", "gx", "snx", "gy", "tmc", "tunB", "bz", "brug", "ty"],
    "2.3": ["tw", "ts", "sa", "wf", "tab:T", "tw", "tab:F", "wf", "spC", "spA", "speer", "ts"],
    "2.4": ["sm:T", "smal", "yas", "oors", "syas", "topy", "kop", "lig:F", "breed", "kop", "lig:T", "syas"],
    "2.5": ["gmc", "gb", "gc", "pmc", "pb", "pc", "ptop", "bd25:T", "hmL", "winst", "gmc", "pmc"],
}

def bouw(slot, rng):
    naam, _, tf = slot.partition(":")
    if naam.startswith("bmc"): return q_begrip_mc(rng, int(naam[3:]))
    if naam.startswith("bin"): return q_begrip_in(rng, int(naam[3:]))
    if naam.startswith("bwo"): return q_begrip_wo(rng, int(naam[3:]))
    if tf: return WOQ[naam](rng, tf == "T")
    return Q[naam](rng)

def maak(plan, rng, GEZIEN, norm):
    vragen = []
    for slot in plan:
        for _ in range(400):
            v = bouw(slot, rng)
            if norm(v["vraag"]) not in GEZIEN: break
        else: raise SystemExit("geen unieke vraag: " + slot)
        GEZIEN.add(norm(v["vraag"]))
        if v["type"] == "invul": assert v["antwoord"], v
        vragen.append(v)
    mcs = [v for v in vragen if v["type"] == "mc"]
    # mc_volgorde eist ≤40 % per letter: bij 1–2 vragen onmogelijk → dan gewoon verschillende posities
    pos = iter(mc_volgorde(rng, len(mcs)) if len(mcs) >= 5 else rng.sample(range(4), len(mcs)))
    for v in mcs:
        o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
    return vragen

def naar_oefen(v):
    if v["type"] == "invul":
        a = v["antwoord"].split("|")[0]
        try: x = F(a.replace(",", "."))
        except ValueError: return dict(v, type="invoer")          # tekstantwoord (begrippen)
        # engine.js leest het eerste alternatief als getal → eerst het decimale getal, dan de breuk letterlijk
        dec = num_ans(x) or fmt(x, 2).replace("−", "-")
        alts = [dec, dec.replace("-", "−")] + ([a, a.replace("-", "−")] if "/" in a else [])
        v = dict(v, type="invoer", antwoord="|".join(dict.fromkeys(alts)))
    return v

KOP = ("/* =========================================================\n   Duru's Wiskunde (HAVO 3) — {t}\n"
       "   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)\n"
       "   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py\n   ========================================================= */\n")

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    # onderwerpen
    for i, (par, (titel, kort, theorie)) in enumerate(THEORIE.items()):
        rng = random.Random(7100 + i * 13)
        vragen = [naar_oefen(v) for v in maak(ONDERWERP_PLAN[par], rng, GEZIEN, norm)]
        o = {"id": f"h2-parabolen-{i + 1}", "hoofdstuk": 2, "paragraaf": par, "titel": titel, "korteUitleg": kort, "icoon": "⛰️", "kleur": "blauw",
             "theorie": theorie, "vragen": vragen}
        with open(f"{OUT}/parabolen_{par.replace('.', '_')}.js", "w") as fh:
            fh.write(KOP.format(t=f"Onderwerp §{par} {titel}") + "DURU.register(" + json.dumps(o, ensure_ascii=False, indent=2) + ");\n")
    rng = random.Random(7199)
    bplan = [f"bmc{i}" for i in (0, 2, 4, 6, 8, 10, 12)] + [f"bin{i}" for i in (0, 3)] + [f"bwo{i}" for i in (0, 2, 5)]
    vragen = [naar_oefen(v) for v in maak(bplan, rng, GEZIEN, norm)]
    o = {"id": "h2-parabolen-begrippen", "hoofdstuk": 2, "paragraaf": "begrippen", "titel": "Begrippen & Kernconcepten — Parabolen",
         "korteUitleg": "Parabool, berg- en dalparabool, top, symmetrieas, de drie vormen en wat a, b en c je vertellen.", "icoon": "📖", "kleur": "blauw",
         "theorie": THEORIE_BEGRIP, "vragen": vragen}
    with open(f"{OUT}/parabolen_begrippen.js", "w") as fh:
        fh.write(KOP.format(t="Begrippen H2 Parabolen") + "DURU.register(" + json.dumps(o, ensure_ascii=False, indent=2) + ");\n")
    # proeftoetsen
    for i, (par, naam, plan) in enumerate(TOETSEN):
        nr = 61 + i; rng = random.Random(6100 + i * 29)
        if plan is None:   # begrippentoets: alle begrippen, ook de oefenvragen (andere formulering niet nodig: toets ≠ oefening)
            GB = set()
            plan = [f"bmc{k}" for k in range(1, 19, 2)] + [f"bmc{k}" for k in (14, 16, 18)] + [f"bin{k}" for k in (1, 2, 4)] + [f"bwo{k}" for k in (1, 3, 4, 6, 7)]
            vragen = maak(plan, rng, GB, norm)
        else:
            vragen = maak(plan, rng, GEZIEN, norm)
        titel = f"Proeftoets {nr} — {naam}"
        ex = {"id": f"ex-wiskunde-parabolen-{i + 1}", "hoofdstuk": 2, "paragraaf": par, "titel": titel,
              "vak": "Wiskunde · H2 Parabolen", "icoon": "⛰️", "duurMin": 30, "vragen": vragen}
        with open(f"{OUT}/examen_{nr}.js", "w") as fh:
            fh.write(KOP.format(t=titel) + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: 6 onderwerpen, examen_61 … 73")
