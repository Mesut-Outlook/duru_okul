"""Wiskunde H1 §1.1–§1.5: 5 proeftoetsen per paragraaf (25), opgaven naar het boek met andere getallen.
Alle antwoorden worden berekend (Fraction), figuren als inline SVG.
Gebruik: python3 tools/gen_wiskunde_h1_paragraaf_exams.py havo3/wiskunde/js/data <bestaande-vragen.json>
(bestaande-vragen.json = JSON-lijst van alle vraagteksten die al bestaan, om dubbele vragen te voorkomen).
⚠️ Niet opnieuw draaien op gepubliceerde ids (ex-wiskunde-h1-10…34): inhoud van een gemaakte toets mag niet veranderen."""
import json, random, sys
from fractions import Fraction as F

OUT = sys.argv[1]
BESTAAND = set(json.load(open(sys.argv[2])))
GEZIEN = set(BESTAAND)
FIG = [0]

# ---------- opmaak ----------
def fmt(x, dec=None, dui=False):
    if dec is not None:
        s = f"{float(x):.{dec}f}"
    else:
        x = F(x)
        if x.denominator == 1:
            s = str(x.numerator)
        else:
            d = x.denominator; e2 = e5 = 0
            while d % 2 == 0: d //= 2; e2 += 1
            while d % 5 == 0: d //= 5; e5 += 1
            s = f"{float(x):.{max(e2, e5)}f}" if d == 1 else f"{x.numerator}/{x.denominator}"
    neg = s.startswith('-'); s = s.lstrip('-')
    ip, _, fp = s.partition('.')
    if dui and len(ip) > 4:
        ip = f"{int(ip):,}".replace(',', '.')
    s = ip + (',' + fp if fp else '')
    return ('−' if neg else '') + s

def term(a, v):
    a = F(a)
    if a == 1: return v
    if a == -1: return '−' + v
    return fmt(a) + v

def lin(a, b, y='y', x='x', omgekeerd=False):
    a, b = F(a), F(b)
    if a == 0: return f"{y} = {fmt(b)}"
    if b == 0: return f"{y} = {term(a, x)}"
    if omgekeerd:
        t = term(abs(a), x)
        return f"{y} = {fmt(b)} {'+' if a > 0 else '−'} {t}"
    return f"{y} = {term(a, x)} {'+' if b > 0 else '−'} {fmt(abs(b))}"

def expr(a, b, x='x'):
    return lin(a, b).split(' = ', 1)[1].replace('x', x) if x != 'x' else lin(a, b).split(' = ', 1)[1]

def hk(x): return f"({fmt(x)})" if F(x) < 0 else fmt(x)

def gs(g): return fmt(F(str(g)))

def pt(x, y): return f"({fmt(x)}, {fmt(y)})"

SUP = str.maketrans('0123456789t', '⁰¹²³⁴⁵⁶⁷⁸⁹ᵗ')
def macht(g, e='t', dec=None): return f"{fmt(g, dec)}{str(e).translate(SUP)}"

def keuze(rng, lst): return lst[rng.randrange(len(lst))]

# ---------- SVG ----------
def svg_graph(xmin, xmax, ymin, ymax, xstap=1, ystap=1, lijnen=(), krommen=(), punten=(), xlabel=None, ylabel=None, eenheid=28):
    FIG[0] += 1; cid = f"w1c{FIG[0]}"
    m = 30; bl = 40 if ylabel or ystap != 1 else m
    W = bl + (xmax - xmin) / xstap * eenheid + m
    H = m + (ymax - ymin) / ystap * eenheid + (44 if xlabel else m)
    X = lambda x: bl + (x - xmin) / xstap * eenheid
    Y = lambda y: m + (ymax - y) / ystap * eenheid
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" style="max-width:100%;height:auto" font-family="sans-serif" font-size="12">',
         f'<rect x="0" y="0" width="{W:.0f}" height="{H:.0f}" rx="12" fill="#ffffff"/>',
         f'<defs><clipPath id="{cid}"><rect x="{X(xmin)}" y="{Y(ymax)}" width="{X(xmax)-X(xmin)}" height="{Y(ymin)-Y(ymax)}"/></clipPath></defs>']
    x = xmin
    while x <= xmax + 1e-9:
        o.append(f'<line x1="{X(x):.1f}" y1="{Y(ymin):.1f}" x2="{X(x):.1f}" y2="{Y(ymax):.1f}" stroke="#d6dbe4" stroke-width="1"/>'); x += xstap
    y = ymin
    while y <= ymax + 1e-9:
        o.append(f'<line x1="{X(xmin):.1f}" y1="{Y(y):.1f}" x2="{X(xmax):.1f}" y2="{Y(y):.1f}" stroke="#d6dbe4" stroke-width="1"/>'); y += ystap
    ax0 = 0 if ymin <= 0 <= ymax else ymin
    ay0 = 0 if xmin <= 0 <= xmax else xmin
    o.append(f'<line x1="{X(xmin)}" y1="{Y(ax0):.1f}" x2="{X(xmax)}" y2="{Y(ax0):.1f}" stroke="#222" stroke-width="1.6"/>')
    o.append(f'<line x1="{X(ay0):.1f}" y1="{Y(ymin)}" x2="{X(ay0):.1f}" y2="{Y(ymax)}" stroke="#222" stroke-width="1.6"/>')
    x = xmin
    while x <= xmax + 1e-9:
        if x != ay0 or ax0 != 0:
            o.append(f'<text x="{X(x):.1f}" y="{Y(ax0)+15:.1f}" fill="#333" text-anchor="middle">{fmt(F(x).limit_denominator(100))}</text>')
        x += xstap
    y = ymin
    while y <= ymax + 1e-9:
        if y != ax0 or ay0 != 0:
            o.append(f'<text x="{X(ay0)-5:.1f}" y="{Y(y)+4:.1f}" fill="#333" text-anchor="end">{fmt(F(y).limit_denominator(100))}</text>')
        y += ystap
    if ax0 == 0 and ay0 == 0:
        o.append(f'<text x="{X(0)-5:.1f}" y="{Y(0)+15:.1f}" fill="#333" text-anchor="end" font-style="italic">O</text>')
    o.append(f'<text x="{X(xmax)+6:.1f}" y="{Y(ax0)+4:.1f}" fill="#222" font-style="italic">{"" if xlabel else "x"}</text>')
    o.append(f'<text x="{X(ay0)-4:.1f}" y="{Y(ymax)-10:.1f}" fill="#222" font-style="italic">{"" if ylabel else "y"}</text>')
    if xlabel: o.append(f'<text x="{(X(xmin)+X(xmax))/2:.1f}" y="{H-8:.1f}" fill="#222" text-anchor="middle">{xlabel} →</text>')
    if ylabel: o.append(f'<text x="{X(xmin):.1f}" y="{Y(ymax)-12:.1f}" fill="#222">↑ {ylabel}</text>')
    kleuren = ['#c2185b', '#0d9488', '#1d4ed8', '#b45309']
    for i, (a, b, naam) in enumerate(lijnen):
        k = kleuren[i % 4]
        x1, x2 = xmin - 1, xmax + 1
        o.append(f'<line clip-path="url(#{cid})" x1="{X(x1):.1f}" y1="{Y(a*x1+b):.1f}" x2="{X(x2):.1f}" y2="{Y(a*x2+b):.1f}" stroke="{k}" stroke-width="2.6"/>')
        # label: rechts in beeld
        for xs in [xmax - 0.6 - j * 0.5 for j in range(int((xmax - xmin) * 2))]:
            ys = a * xs + b
            if ymin + 0.6 <= ys <= ymax - 0.6:
                o.append(f'<text x="{X(xs)+6:.1f}" y="{Y(ys)-8:.1f}" fill="{k}" font-weight="bold" font-style="italic" font-size="14">{naam}</text>'); break
    for i, f in enumerate(krommen):
        k = kleuren[i % 4]; n = 80
        pts = " ".join(f"{X(xmin+(xmax-xmin)*j/n):.1f},{Y(f(xmin+(xmax-xmin)*j/n)):.1f}" for j in range(n + 1))
        o.append(f'<polyline clip-path="url(#{cid})" points="{pts}" fill="none" stroke="{k}" stroke-width="2.6"/>')
    for (px, py, lab) in punten:
        o.append(f'<circle cx="{X(px):.1f}" cy="{Y(py):.1f}" r="3.5" fill="#222"/>')
        if lab: o.append(f'<text x="{X(px)+6:.1f}" y="{Y(py)-6:.1f}" fill="#222" font-size="11">{lab}</text>')
    o.append('</svg>')
    return "".join(o)

def svg_tabel(rijen):
    """rijen: lijst van lijsten met strings; eerste kolom = kop."""
    kw = [max(len(r[i]) for r in rijen) * 8 + 18 for i in range(len(rijen[0]))]
    rh = 30; W = sum(kw) + 2; H = rh * len(rijen) + 2
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" style="max-width:100%;height:auto" font-family="sans-serif" font-size="13">',
         f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="8" fill="#ffffff" stroke="#9aa3b2"/>']
    for j, r in enumerate(rijen):
        x = 1
        for i, c in enumerate(r):
            if i == 0: o.append(f'<rect x="{x}" y="{1+j*rh}" width="{kw[0]}" height="{rh}" fill="#fde7ef"/>')
            o.append(f'<text x="{x+kw[i]/2}" y="{1+j*rh+20}" text-anchor="middle" fill="#222"{" font-weight=\"bold\"" if i == 0 else ""}>{c}</text>')
            x += kw[i]
            if i < len(r) - 1: o.append(f'<line x1="{x}" y1="{1+j*rh}" x2="{x}" y2="{1+(j+1)*rh}" stroke="#9aa3b2"/>')
        if j: o.append(f'<line x1="1" y1="{1+j*rh}" x2="{W-1}" y2="{1+j*rh}" stroke="#9aa3b2"/>')
    o.append('</svg>')
    return "".join(o)

def nette_as(top):
    stap = next(st for st in (5, 10, 20, 25, 50, 100, 150, 200, 250, 500) if top / st <= 9)
    return -(-top // stap) * stap, stap

# ---------- vraagbouwers ----------
def MC(vraag, goed, fout, uitleg, figuur=None):
    opts = [goed] + [f for f in dict.fromkeys(fout) if f != goed]
    assert len(opts) >= 4, (vraag, opts)
    d = {"type": "mc", "vraag": vraag, "_opts": opts[:4], "uitleg": uitleg}
    if figuur: d["figuur"] = figuur
    return d

def WO(vraag, waar, uitleg, figuur=None):
    d = {"type": "waaronwaar", "vraag": vraag, "antwoord": waar, "uitleg": ("Waar. " if waar else "Onwaar. ") + uitleg}
    if figuur: d["figuur"] = figuur
    return d

def IN(vraag, antwoord, uitleg, figuur=None, tol=None):
    d = {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}
    if tol is not None: d["tolerantie"] = tol
    if figuur: d["figuur"] = figuur
    return d

def OP(vraag, model, sleutels, mint, uitleg):
    return {"type": "open", "vraag": vraag, "modelantwoord": model, "sleutelwoorden": sleutels, "minTreffers": mint, "uitleg": uitleg}

def num_ans(x, dec=None):
    s = fmt(x, dec).replace('−', '-')
    return s if '/' not in s else None

def sleutel_term(a, v='x'):
    t = term(a, v).replace('−', '-')
    return f"{t}/{t.replace('-', '−')}"

def sleutel_const(b):
    v = fmt(abs(b))
    return f"+ {v}/+{v}" if b > 0 else f"- {v}/-{v}/− {v}"

# ================= §1.1 Lineaire formules opstellen =================
RC_NET = [F(-3), F(-2), F(-1), F(-1, 2), F(1, 2), F(2), F(3), F(4), F(-4), F(3, 2), F(-3, 2), F(5), F(-5)]

def lijn_door_punten(rng, rcs=RC_NET, heel=False):
    while True:
        a = keuze(rng, rcs); b = F(rng.randint(-12, 15))
        x1 = rng.randint(-6, 6); x2 = x1 + rng.randint(2, 9)
        if heel and a.denominator != 1: continue
        y1, y2 = a * x1 + b, a * x2 + b
        if y1.denominator == 1 and y2.denominator == 1 and b != 0 and x1 != 0 and x2 != 0:
            return a, b, (x1, y1), (x2, y2)

def q11_rc_start(rng):
    a = keuze(rng, [F(-3), F(-2, 3), F(1, 4), F(0.4), F(-1, 2), F(5), F(-7), F(3, 4), F(-1), F(6)])
    b = F(rng.choice([i for i in range(-9, 10) if i not in (0,)]))
    if abs(b) == abs(a): b += 2
    om = rng.random() < 0.5
    f = lin(a, b, omgekeerd=om)
    r = lambda A, B: f"richtingscoëfficiënt {fmt(A)} en startgetal {fmt(B)}"
    return MC(f"Gegeven is de formule {f}. Wat zijn de richtingscoëfficiënt en het startgetal?",
              r(a, b), [r(b, a), r(-a, b), r(a, -b), r(-a, -b)],
              f"Schrijf de formule als y = ax + b: {lin(a, b)}. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: {fmt(a)}. Het losse getal is het startgetal: {fmt(b)}.")

def q11_rc_punten(rng):
    a, b, (x1, y1), (x2, y2) = lijn_door_punten(rng)
    return IN(f"Een lijn gaat door de punten P{pt(x1, y1)} en Q{pt(x2, y2)}. Bereken de richtingscoëfficiënt van de lijn." + (" Geef je antwoord als decimaal getal." if a.denominator != 1 else ""),
              num_ans(a), f"rc = toename y / toename x = ({fmt(y2)} − {hk(y1)}) / ({fmt(x2)} − {hk(x1)}) = {fmt(y2 - y1)} / {fmt(x2 - x1)} = {fmt(a)}.")

def q11_b_punten(rng):
    a, b, (x1, y1), (x2, y2) = lijn_door_punten(rng)
    return IN(f"De lijn y = ax + b gaat door de punten {pt(x1, y1)} en {pt(x2, y2)}. Bereken het startgetal b.",
              num_ans(b), f"Eerst a = {fmt(y2 - y1)} / {fmt(x2 - x1)} = {fmt(a)}. Invullen van {pt(x1, y1)}: {fmt(y1)} = {fmt(a)} · {hk(x1)} + b, dus {fmt(y1)} = {fmt(a * x1)} + b en b = {fmt(b)}.")

def q11_formule_punten(rng):
    a, b, (x1, y1), (x2, y2) = lijn_door_punten(rng)
    fout = [lin(a, -b), lin(-a, b), lin(a, y1)]
    if abs(a) != 1: fout.append(lin(1 / a, b))
    fout.append(lin(a, b + a))
    return MC(f"Welke formule hoort bij de lijn door de punten {pt(x1, y1)} en {pt(x2, y2)}?", lin(a, b), fout,
              f"a = ({fmt(y2)} − {hk(y1)}) / ({fmt(x2)} − {hk(x1)}) = {fmt(a)}. Invullen van {pt(x1, y1)} geeft {fmt(y1)} = {fmt(a * x1)} + b, dus b = {fmt(b)}. De formule is {lin(a, b)}.")

def grafiek_lijn(rng, rcs=(F(-2), F(-1), F(-1, 2), F(1, 2), F(1), F(2), F(3), F(3, 2), F(-3, 2), F(2, 3), F(-1, 3))):
    while True:
        a = keuze(rng, rcs); b = F(rng.randint(-3, 4))
        pts = [(x, a * x + b) for x in range(-1, 8) if (a * x + b).denominator == 1 and -4 <= a * x + b <= 6]
        if len(pts) >= 2 and b != 0 and abs(pts[-1][0] - pts[0][0]) >= 2:
            return a, b, [pts[0], pts[-1]]

def q11_grafiek_formule(rng):
    a, b, pts = grafiek_lijn(rng)
    fig = svg_graph(-1, 7, -4, 6, lijnen=[(float(a), float(b), 'l')], punten=[(float(x), float(y), '') for x, y in pts])
    fout = [lin(-a, b), lin(a, -b), lin(1 / a, b), lin(a, b + 1)]
    return MC(f"Lijn l in de figuur gaat onder andere door het punt {pt(*pts[1])}. Welke formule hoort bij lijn l?", lin(a, b), fout,
              f"Lijn l snijdt de y-as in (0, {fmt(b)}), dus het startgetal is {fmt(b)}. Tussen de stippen {pt(*pts[0])} en {pt(*pts[1])}: rc = {fmt(pts[1][1] - pts[0][1])} / {fmt(pts[1][0] - pts[0][0])} = {fmt(a)}. Dus {lin(a, b)}.", fig)

def q11_grafiek_rc(rng):
    a, b, pts = grafiek_lijn(rng, (F(-2), F(-1, 2), F(1, 2), F(2), F(3), F(3, 2), F(-3, 2), F(-1), F(1)))
    fig = svg_graph(-1, 7, -4, 6, lijnen=[(float(a), float(b), 'k')], punten=[(float(x), float(y), pt(x, y)) for x, y in pts])
    return IN(f"Lijn k gaat door de punten {pt(*pts[0])} en {pt(*pts[1])} (zie figuur). Lees af hoe groot de richtingscoëfficiënt van lijn k is." + (" Geef je antwoord als decimaal getal." if a.denominator != 1 else ""),
              num_ans(a), f"Van {pt(*pts[0])} naar {pt(*pts[1])}: {fmt(pts[1][0] - pts[0][0])} naar rechts en {fmt(pts[1][1] - pts[0][1])} omhoog. rc = {fmt(pts[1][1] - pts[0][1])} / {fmt(pts[1][0] - pts[0][0])} = {fmt(a)}.", fig)

def evenwijdig(rng):
    a = keuze(rng, [F(-3), F(-2), F(2), F(4), F(-5), F(3), F(6), F(-4), F(1, 2), F(-1, 2)])
    c = F(rng.randint(-15, 18)); p = rng.choice([-6, -5, -4, -2, 2, 3, 4, 5, 6, 8]); q = F(rng.randint(-12, 16))
    if (a * p).denominator != 1: p *= 2
    b = q - a * p
    if b == 0 or b == c or c == 0: return evenwijdig(rng)
    return a, c, p, q, b

def q11_evenwijdig(rng):
    a, c, p, q, b = evenwijdig(rng)
    return MC(f"Lijn m gaat door het punt {pt(p, q)} en loopt evenwijdig aan lijn l: {lin(a, c)}. Welke formule hoort bij lijn m?",
              lin(a, b), [lin(a, q), lin(a, q + a * p), lin(-a, q + a * p), lin(a, c + q), lin(-a, b)],
              f"Evenwijdig betekent dezelfde rc: a = {fmt(a)}. Invullen van {pt(p, q)}: {fmt(q)} = {fmt(a)} · {hk(p)} + b = {fmt(a * p)} + b, dus b = {fmt(b)}. Lijn m: {lin(a, b)}.")

def q11_evenwijdig_b(rng):
    a, c, p, q, b = evenwijdig(rng)
    return IN(f"Lijn m loopt evenwijdig aan de lijn {lin(a, c)} en gaat door het punt {pt(p, q)}. Een formule bij m is y = {term(a, 'x')} + b. Bereken b.",
              num_ans(b), f"{fmt(q)} = {fmt(a)} · {hk(p)} + b → {fmt(q)} = {fmt(a * p)} + b → b = {fmt(b)}.")

def q11_op_lijn(rng, waar):
    a = F(rng.choice([-4, -3, -2, 2, 3, 5, F(1, 2), F(-1, 2)])); b = F(rng.randint(-10, 12))
    p = rng.choice([-12, -8, -6, -4, 4, 6, 8, 10, 12])
    q = a * p + b + (0 if waar else rng.choice([-2, -1, 1, 2]))
    return WO(f"Het punt {pt(p, q)} ligt op de lijn {lin(a, b)}.", waar,
              f"Invullen van x = {fmt(p)}: y = {fmt(a)} · {hk(p)} {'+' if b >= 0 else '−'} {fmt(abs(b))} = {fmt(a * p + b)}. " + ("Dat is gelijk aan " + fmt(q) + ", dus het punt ligt op de lijn." if waar else f"Dat is niet {fmt(q)}, dus het punt ligt niet op de lijn."))

def q11_stijgend(rng, waar):
    a = F(rng.choice([-7, -3, -2, F(-1, 4), F(1, 3), 2, 4, F(3, 5)])); b = F(rng.randint(-9, 9) or 4)
    soort = rng.choice(['stijgend', 'dalend'])
    echt = 'stijgend' if a > 0 else 'dalend'
    if (soort == echt) != waar: soort = 'dalend' if soort == 'stijgend' else 'stijgend'
    return WO(f"De lijn bij de formule {lin(a, b, omgekeerd=rng.random() < 0.4)} is {soort}.", waar,
              f"De rc is {fmt(a)}; die is {'positief, dus de lijn is stijgend' if a > 0 else 'negatief, dus de lijn is dalend'}.")

def q11_evenwijdig_wo(rng, waar):
    a = F(rng.choice([-3, -2, 2, 3, 4, 5, F(1, 2)])); b1 = F(rng.randint(-9, 9)); b2 = b1 + rng.choice([-7, -4, 3, 5, 8])
    a2 = a if waar else -a
    return WO(f"De lijnen {lin(a, b1)} en {lin(a2, b2, omgekeerd=True)} lopen evenwijdig.", waar,
              f"Evenwijdige lijnen hebben dezelfde richtingscoëfficiënt. Hier: {fmt(a)} en {fmt(a2)}" + (", gelijk." if waar else ", niet gelijk."))

NAMEN = [("Nienke", "Xu Yan"), ("Sem", "Lotte"), ("Aylin", "Daan"), ("Noah", "Fenna"), ("Mila", "Yusuf"), ("Bram", "Sara")]

def q11_sparen(rng):
    n1, n2 = keuze(rng, NAMEN); S = rng.choice([80, 120, 150, 200, 250, 300]); p = rng.choice([8, 10, 12, 15, 20, 25]); k = rng.choice([2, 3])
    keer = {2: "twee", 3: "drie"}[k]
    return MC(f"{n1} spaart voor een scooter. Met de formule s = {S} + {p}w berekent {n1} het bedrag s in euro's na w weken. {n2} begint op hetzelfde moment, heeft nog niets gespaard en spaart per week {keer} keer zoveel als {n1}. Welke formule hoort bij {n2}?",
              f"s = {k * p}w", [f"s = {S} + {k * p}w", f"s = {k * S} + {p}w", f"s = {k * S} + {k * p}w", f"s = {p + k}w"],
              f"{n2} begint bij 0 euro (startgetal 0) en spaart {keer} keer {p} = {k * p} euro per week (rc {k * p}). Dus s = {k * p}w.")

def q11_tabel(rng):
    a = F(rng.choice([-3, -2, 2, 3, 4, F(-2, 3), F(4, 3)])); d = 3 if a.denominator == 3 else rng.choice([2, 3, 4])
    x0 = rng.choice([1, 2, 4, 5]); b = F(rng.randint(-6, 20))
    xs = [x0 + i * d for i in range(5)]; ys = [a * x + b for x in xs]
    if any(y.denominator != 1 for y in ys) or b == 0: return q11_tabel(rng)
    fig = svg_tabel([["x"] + [fmt(x) for x in xs], ["y"] + [fmt(y) for y in ys]])
    return MC(f"Bij de tabel hoort een lineair verband (x loopt van {fmt(xs[0])} tot {fmt(xs[-1])}). Welke formule hoort bij de tabel?", lin(a, b),
              [lin(ys[1] - ys[0], b), lin(a, ys[0]), lin(-a, b), lin(a, b + a)],
              f"Per {d} stappen in x verandert y met {fmt(ys[1] - ys[0])}, dus rc = {fmt(ys[1] - ys[0])} / {d} = {fmt(a)}. Invullen van ({fmt(xs[0])}, {fmt(ys[0])}): b = {fmt(ys[0])} − {fmt(a * xs[0])} = {fmt(b)}.", fig)

def q11_horizontaal(rng):
    c = F(rng.choice([-6, -5, -4, -3, 3, 4, 7])); x1 = rng.choice([-8, -5, -3]); x2 = rng.choice([6, 9, 10])
    return MC(f"Welke formule hoort bij lijn k door de punten {pt(x1, c)} en {pt(x2, c)}?", f"y = {fmt(c)}",
              [f"x = {fmt(c)}", f"y = {term(c, 'x')}", f"y = x {'+' if c > 0 else '−'} {fmt(abs(c))}", f"y = {fmt(c)}x + {fmt(abs(x1))}"],
              f"De y-coördinaat is bij beide punten {fmt(c)}: de toename van y is 0, dus rc = 0. De lijn is horizontaal: y = {fmt(c)}.")

def q11_steilst(rng):
    vals = rng.sample([F(1, 2), F(2), F(3), F(4), F(3, 2), F(5), F(2, 3), F(6)], 4)
    bs = [rng.randint(-6, 9) or 1 for _ in vals]
    best = max(vals)
    return MC(f"Gegeven zijn de stijgende lijnen {'; '.join(lin(v, bb) for v, bb in zip(vals, bs))}. Welke lijn loopt het steilst?", lin(best, bs[vals.index(best)]),
              [lin(v, bb) for v, bb in zip(vals, bs) if v != best],
              f"Hoe groter de richtingscoëfficiënt, hoe steiler de lijn. De grootste rc is {fmt(best)}. Het startgetal maakt voor de steilheid niet uit.")

def q11_open(rng):
    a, b, (x1, y1), (x2, y2) = lijn_door_punten(rng, heel=True, rcs=[F(-3), F(-2), F(2), F(3), F(4), F(-4), F(5)])
    return OP(f"Stel een formule op bij de lijn door de punten A{pt(x1, y1)} en B{pt(x2, y2)}. Schrijf je antwoord als y = ax + b.",
              lin(a, b), [sleutel_term(a), sleutel_const(b)], 2,
              f"rc = ({fmt(y2)} − {hk(y1)}) / ({fmt(x2)} − {hk(x1)}) = {fmt(a)}. Invullen van A: {fmt(y1)} = {fmt(a * x1)} + b, dus b = {fmt(b)}. Formule: {lin(a, b)}.")

P11 = ["rc_start", "rc_punten", "formule_punten", "grafiek_formule", "op_lijn:T", "grafiek_rc", "evenwijdig", "b_punten",
       "stijgend:F", "sparen", "tabel", "evenwijdig_b", "horizontaal", "op_lijn:F", "steilst", "evenwijdig_wo:T", "formule_punten",
       "evenwijdig", "rc_punten", "open"]

# ================= §1.2 Lijnen snijden =================
def twee_lijnen(rng, heel=True):
    while True:
        x0 = rng.randint(-6, 12); y0 = rng.randint(-15, 30)
        a1, a2 = rng.sample([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12], 2)
        b1, b2 = y0 - a1 * x0, y0 - a2 * x0
        if b1 and b2 and x0 and y0 and b1 != b2:
            return F(a1), F(b1), F(a2), F(b2), F(x0), F(y0)

def q12_x(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    return IN(f"De lijnen l: {lin(a1, b1)} en m: {lin(a2, b2, omgekeerd=rng.random() < 0.3)} snijden elkaar in punt S. Bereken de x-coördinaat van S.",
              num_ans(x0), f"Stel gelijk: {expr(a1, b1)} = {expr(a2, b2)} → {term(a1 - a2, 'x')} = {fmt(b2 - b1)} → x = {fmt(x0)}.")

def q12_y(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    return IN(f"Bereken de y-coördinaat van het snijpunt van de lijnen {lin(a1, b1)} en {lin(a2, b2)}.",
              num_ans(y0), f"{expr(a1, b1)} = {expr(a2, b2)} geeft x = {fmt(x0)}. Invullen: y = {fmt(a1)} · {hk(x0)} {'+' if b1 > 0 else '−'} {fmt(abs(b1))} = {fmt(y0)}. Controle in de andere formule: {fmt(a2 * x0 + b2)}.")

def q12_S(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    return MC(f"Bereken de coördinaten van het snijpunt van de grafieken van {lin(a1, b1)} en {lin(a2, b2)}.", pt(x0, y0),
              [pt(y0, x0), pt(-x0, a1 * -x0 + b1), pt(x0, a1 * x0 - b1), pt(x0 + 1, a1 * (x0 + 1) + b1), pt(x0, y0 + a1)],
              f"{expr(a1, b1)} = {expr(a2, b2)} → {term(a1 - a2, 'x')} = {fmt(b2 - b1)} → x = {fmt(x0)}; y = {fmt(y0)}. Snijpunt {pt(x0, y0)}.")

def q12_vergelijking(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    e1, e2 = expr(a1, b1), expr(a2, b2)
    return MC(f"De lijnen {lin(a1, b1)} en {lin(a2, b2)} snijden elkaar in S. Met welke vergelijking bereken je de x-coördinaat van S?",
              f"{e1} = {e2}", [f"{e1} = 0", f"{expr(a1, b2)} = {expr(a2, b1)}", f"{e1} = −({e2})", f"{e2} = {fmt(b1)}"],
              "Op het snijpunt hebben beide lijnen dezelfde y. Stel daarom de twee formules aan elkaar gelijk.")

def q12_grafiek(rng):
    # twee lijnen door roosterpunten; snijpunt buiten beeld (x > 8) zoals in het boek
    while True:
        p1 = (0, F(rng.randint(-3, 4))); ap = F(rng.choice([1, 2, 3, F(3, 2), F(1, 2)]))
        q1 = (0, F(rng.randint(6, 12))); aq = F(rng.choice([F(1, 2), 1, F(-1, 2), F(1, 4), 0]))
        if ap == aq: continue
        x0 = (q1[1] - p1[1]) / (ap - aq); y0 = ap * x0 + p1[1]
        if x0.denominator == 1 and y0.denominator == 1 and 9 <= x0 <= 30: break
    def roosterpt(a, b):
        return [(F(x), a * x + b) for x in range(1, 9) if (a * x + b).denominator == 1 and -2 <= a * x + b <= 14]
    pp, qq = roosterpt(ap, p1[1]), roosterpt(aq, q1[1])
    fig = svg_graph(-1, 8, -2, 14, ystap=2, eenheid=26, lijnen=[(float(ap), float(p1[1]), 'p'), (float(aq), float(q1[1]), 'q')],
                    punten=[(float(x), float(y), '') for x, y in [p1, pp[-1], q1, qq[-1]]])
    return MC(f"Lijn p gaat door {pt(*p1)} en lijn q door {pt(*q1)}. De lijnen snijden elkaar buiten de figuur. Stel bij beide lijnen een formule op en bereken de coördinaten van het snijpunt.", pt(x0, y0),
              [pt(y0, x0), pt(x0, aq * x0), pt(x0 + 2, ap * (x0 + 2) + p1[1]), pt(x0, y0 + 2)],
              f"Lijn p: {lin(ap, p1[1])}. Lijn q: {lin(aq, q1[1])}. Gelijkstellen: {expr(ap, p1[1])} = {expr(aq, q1[1])} geeft x = {fmt(x0)} en y = {fmt(y0)}.", fig)

def q12_grafiek_formule(rng):
    a, b, pts = grafiek_lijn(rng, (F(-2), F(-1), F(1, 2), F(2), F(3), F(-3, 2)))
    fig = svg_graph(-1, 7, -4, 6, lijnen=[(float(a), float(b), 'p')], punten=[(float(x), float(y), pt(x, y)) for x, y in pts])
    c = F(rng.choice([-3, -2, 2, 5]))
    x0 = (c - b) / a
    if num_ans(x0) is None or c == b: return q12_grafiek_formule(rng)
    return IN(f"De lijn y = {fmt(c)} snijdt lijn p uit de figuur. Bereken de x-coördinaat van het snijpunt." + (" Geef je antwoord als decimaal getal." if x0.denominator != 1 else ""),
              num_ans(x0), f"Lijn p: {lin(a, b)}. Gelijkstellen: {expr(a, b)} = {fmt(c)} → {term(a, 'x')} = {fmt(c - b)} → x = {fmt(x0)}.", fig)

def q12_geen(rng, waar):
    a = F(rng.choice([-4, -2, 2, 3, 5, 7])); b1 = F(rng.randint(-8, 8) or 3); b2 = b1 + rng.choice([-6, 4, 9])
    if waar:
        return WO(f"De lijnen {lin(a, b1)} en {lin(a, b2)} hebben geen snijpunt.", True,
                  f"Beide lijnen hebben rc {fmt(a)} maar een ander startgetal: ze lopen evenwijdig en snijden elkaar nooit.")
    return WO(f"De lijnen {lin(a, b1)} en {lin(-a, b1)} hebben geen snijpunt.", False,
              f"De rc's zijn verschillend ({fmt(a)} en {fmt(-a)}), dus de lijnen snijden elkaar wel: in (0, {fmt(b1)}), want ze hebben hetzelfde startgetal.")

def q12_check(rng, waar):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    S = (x0, y0) if waar else rng.choice([(y0, x0), (x0, y0 + 2), (-x0, y0)])
    if not waar and S == (x0, y0): S = (x0, y0 + 1)
    return WO(f"Het snijpunt van de lijnen {lin(a1, b1)} en {lin(a2, b2)} is {pt(*S)}.", waar,
              f"Gelijkstellen geeft x = {fmt(x0)} en y = {fmt(y0)}; het snijpunt is {pt(x0, y0)}.")

def q12_credits(rng):
    while True:
        s1 = rng.choice([0, 1, 2]); r1 = rng.choice([F(1, 2), 1, F(3, 2), 2]); r2 = r1 + rng.choice([F(1, 2), 1, F(3, 2)])
        s2 = rng.choice([-2, -1, 0]) if s1 == 0 else rng.choice([0, F(-1, 2)])
        s1, s2, r1, r2 = F(s1), F(s2), F(r1), F(r2); t = (s1 - s2) / (r2 - r1)
        if t.denominator == 1 and 2 <= t <= 20 and s1 != s2: break
    n1, n2 = keuze(rng, NAMEN)
    d1, d2 = 2, rng.choice([6, 8, 10])
    v1, v2 = s2 + r2 * d1, s2 + r2 * d2
    if v1 <= 0: return q12_credits(rng)
    return IN(f"In een spel spaar je credits. {n1} heeft op dag 0 {fmt(s1) + ' miljoen credits' if s1 else 'nog geen credits'} en krijgt er elke dag {fmt(r1)} miljoen bij. {n2} begint op hetzelfde moment en spaart ook elke dag hetzelfde aantal: na {d1} dagen heeft {n2} {fmt(v1)} miljoen credits en na {d2} dagen {fmt(v2)} miljoen. Na hoeveel dagen hebben ze evenveel credits?",
              num_ans(t), f"{n1}: c = {expr(r1, s1, 't').replace('x', 't')}. {n2}: rc = ({fmt(v2)} − {fmt(v1)}) / ({d2} − {d1}) = {fmt(r2)}, b = {fmt(v1)} − {fmt(r2 * d1)} = {fmt(s2)}. Gelijkstellen geeft t = {fmt(t)} dagen.")

def q12_links_rechts(rng):
    while True:
        a1, a2 = rng.sample([3, 4, 5, 6, 7, 9], 2); b1 = rng.randint(20, 60); b2 = -rng.randint(5, 30)
        x0 = F(b2 - b1, a1 - a2)
        g = rng.randint(10, 40)
        if x0 > 0 and x0 != g and abs(x0 - g) >= 2: break
    kant = "rechts" if x0 > g else "links"
    return MC(f"Het snijpunt van de lijnen {lin(a1, b1)} en {lin(a2, b2)} valt buiten een schets. Ligt het snijpunt links of rechts van de lijn x = {g}?",
              f"{kant} van de lijn x = {g}", [f"{'links' if kant == 'rechts' else 'rechts'} van de lijn x = {g}", f"precies op de lijn x = {g}", "de lijnen snijden elkaar niet"],
              f"Gelijkstellen: {expr(a1, b1)} = {expr(a2, b2)} → x {'=' if num_ans(x0) else '≈'} {fmt(x0) if num_ans(x0) else fmt(x0, 1)}. Dat is {'meer' if x0 > g else 'minder'} dan {g}, dus {kant}.")

def q12_mix(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    xa = x0 + rng.choice([-5, -3, 2, 4]); xb = xa + rng.choice([2, 3, 4])
    return IN(f"De formule {lin(a1, b1)} hoort bij lijn k. Lijn l gaat door de punten {pt(xa, a2 * xa + b2)} en {pt(xb, a2 * xb + b2)}. Bereken de x-coördinaat van het snijpunt van k en l.",
              num_ans(x0), f"Lijn l: rc = {fmt(a2 * (xb - xa))} / {fmt(xb - xa)} = {fmt(a2)}, b = {fmt(b2)}, dus {lin(a2, b2)}. Gelijkstellen met k: x = {fmt(x0)} (en y = {fmt(y0)}).")

def q12_yas(rng, waar):
    b = F(rng.randint(-9, 9) or 5); a1, a2 = rng.sample([-3, -1, 2, 4, 6], 2)
    b2 = b if waar else b + rng.choice([-3, 2])
    return WO(f"De lijnen {lin(a1, b)} en {lin(a2, b2)} snijden elkaar op de y-as.", waar,
              f"Op de y-as is x = 0. Daar is de eerste y = {fmt(b)} en de tweede y = {fmt(b2)}" + (": gelijk, dus ze snijden elkaar in (0, " + fmt(b) + ")." if waar else ": verschillend, dus niet op de y-as."))

def q12_open(rng):
    a1, b1, a2, b2, x0, y0 = twee_lijnen(rng)
    return OP(f"Beschrijf de stappen waarmee je het snijpunt van {lin(a1, b1)} en {lin(a2, b2)} berekent, en geef de coördinaten.",
              f"Formules gelijkstellen: {expr(a1, b1)} = {expr(a2, b2)}. Vergelijking oplossen: x = {fmt(x0)}. Invullen in een van de formules: y = {fmt(y0)}. Snijpunt {pt(x0, y0)}.",
              ["gelijk", "vergelijking/oplossen/los", "invullen/invul/vul"], 2,
              f"Gelijkstellen → x = {fmt(x0)} → invullen → y = {fmt(y0)}. Het snijpunt is {pt(x0, y0)}.")

P12 = ["x", "y", "S", "vergelijking", "grafiek", "geen:T", "grafiek_formule", "check:F", "credits", "links_rechts",
       "mix", "yas:T", "S", "x", "geen:F", "vergelijking", "S", "y", "grafiek", "open"]

# ================= §1.3 Formules substitueren =================
VARSETS = [("k", "t", "p"), ("h", "t", "p"), ("b", "t", "p"), ("y", "t", "x"), ("N", "a", "q"), ("w", "s", "r"), ("d", "z", "h")]

def subs(rng):
    A, T, P = keuze(rng, VARSETS)
    a = F(rng.choice([-7, -5, -4, -3, 2, 3, 4, 5, 6, 8, 11])); b = F(rng.randint(-20, 40) or 9)
    c = F(rng.choice([-5, -3, -2, 2, 3, 4, 7, 8])); d = F(rng.randint(-10, 35) or 3)
    return A, T, P, a, b, c, d

def q13_sub(rng):
    A, T, P, a, b, c, d = subs(rng)
    fa = lin(a, b, A, T, omgekeerd=rng.random() < 0.4); fb = lin(c, d, T, P, omgekeerd=rng.random() < 0.4)
    goed = lin(a * c, a * d + b, A, P)
    return MC(f"Gegeven zijn de formules A: {fa} en B: {fb}. Substitueer formule B in formule A en vereenvoudig het resultaat.", goed,
              [lin(a * c, d + b, A, P), lin(a * c, a * d - b, A, P), lin(a + c, d + b, A, P), lin(a * c, a * d + b + 1, A, P), lin(c, a * d + b, A, P)],
              f"{A} = {fmt(a)}({expr(c, d).replace('x', P)}) {'+' if b > 0 else '−'} {fmt(abs(b))} = {term(a * c, P)} {'+' if a * d >= 0 else '−'} {fmt(abs(a * d))} {'+' if b > 0 else '−'} {fmt(abs(b))}, dus {goed}. Let op de haakjes: alles binnen de haakjes wordt met {fmt(a)} vermenigvuldigd.")

def q13_coef(rng):
    A, T, P, a, b, c, d = subs(rng)
    return IN(f"Substitueer {lin(c, d, T, P)} in {lin(a, b, A, T)}. Je krijgt {A} = …{P} {'+' if a * d + b >= 0 else '−'} {fmt(abs(a * d + b))}. Welk getal staat er vóór {P}?",
              num_ans(a * c), f"{A} = {fmt(a)}({expr(c, d).replace('x', P)}) {'+' if b > 0 else '−'} {fmt(abs(b))}. Vóór {P}: {fmt(a)} · {fmt(c)} = {fmt(a * c)}.")

def q13_const(rng):
    A, T, P, a, b, c, d = subs(rng)
    return IN(f"Gegeven: A: {lin(a, b, A, T)} en B: {lin(c, d, T, P)}. Substitueer B in A en vereenvoudig tot {A} = …{P} + …. Welk getal is het losse getal (de constante)?",
              num_ans(a * d + b), f"{A} = {fmt(a)}({expr(c, d).replace('x', P)}) {'+' if b > 0 else '−'} {fmt(abs(b))} = {term(a * c, P)} {'+' if a * d >= 0 else '−'} {fmt(abs(a * d))} {'+' if b > 0 else '−'} {fmt(abs(b))}. Constante: {fmt(a * d)} + {fmt(b)} = {fmt(a * d + b)}.")

def q13_herleid(rng):
    while True:
        s = rng.choice([2, 3, 4, 5]); r = s * rng.choice([1, 2, -1]) if rng.random() < 0.5 else rng.choice([2, 4, 6, 8, 10])
        if r % s: continue
        Tq = s * rng.randint(1, 8); m = F(rng.choice([2, 3, -2, 4, 5])); n = F(rng.randint(-12, 12) or -7)
        k = F(r, s); c0 = F(Tq, s)  # q = c0 - k a
        break
    pv = rng.choice(["p", "N", "w"])
    goed = lin(-m * k, m * c0 + n, pv, "a")
    return MC(f"Substitueer de formule {r}a + {s}q = {Tq} in de formule {lin(m, n, pv, 'q')} en vereenvoudig. (Herleid eerst de eerste formule naar q = …)", goed,
              [lin(m * k, m * c0 + n, pv, "a"), lin(-m * k, c0 + n, pv, "a"), lin(-k, m * c0 + n, pv, "a"), lin(-m * r, m * Tq + n, pv, "a")],
              f"{s}q = {Tq} − {r}a, dus q = {expr(-k, c0).replace('x', 'a')}. Invullen: {pv} = {fmt(m)}({expr(-k, c0).replace('x', 'a')}) {'+' if n > 0 else '−'} {fmt(abs(n))} = {goed.split(' = ')[1]}.")

def q13_nul(rng):
    k = F(rng.choice([2, 3, 4, 5, 6])); c = F(rng.randint(3, 30)); d = F(rng.choice([2, 3, 4, 5]))
    v = rng.choice(["y", "r", "P"])
    goed = lin(-d * k, c, v, "x")
    return MC(f"Substitueer de formule t − {fmt(k)}x = 0 in de formule {v} = {fmt(c)} − {fmt(d)}t.", goed,
              [lin(-d, c - k, v, "x"), lin(d * k, c, v, "x"), lin(-d * k, c - k, v, "x"), lin(-(d + k), c, v, "x")],
              f"t − {fmt(k)}x = 0 geeft t = {fmt(k)}x. Dan {v} = {fmt(c)} − {fmt(d)} · {fmt(k)}x = {fmt(c)} − {fmt(d * k)}x.")

def q13_fabriek(rng):
    m = rng.choice([200, 250, 400, 500, 600]); c = rng.choice([3, 5, 7, 9, 12]); vk = rng.choice([500, 800, 1200, 1500]); t = rng.randint(6, 30)
    return IN(f"Een fabrikant verkoopt a = {m}t apparaten na t weken. De kosten in euro's zijn k = {c}a + {vk}. Bereken de kosten na {t} weken.",
              str(c * m * t + vk), f"Substitueer: k = {c} · {m}t + {vk} = {c * m}t + {vk}. Na {t} weken: k = {c * m} · {t} + {vk} = {c * m * t + vk} euro.")

def berg(rng):
    T0 = F(rng.choice([14, 16, 18, 20, 22])); r = F(rng.choice(["0.006", "0.005", "0.0065", "0.008"])); v = F(rng.choice([6, 8, 10, 12, 15])); h0 = F(rng.choice([100, 200, 250, 400, 500]))
    return T0, r, v, h0, T0 - r * h0, r * v

def q13_berg(rng):
    T0, r, v, h0, c, s = berg(rng)
    goed = lin(-s, c, "T", "k", omgekeerd=True)
    return MC(f"De temperatuur T (°C) op een berg op hoogte h meter is T = {fmt(T0)} − {fmt(r)}h. Na k kwartier wandelen is de hoogte h = {fmt(v)}k + {fmt(h0)}. Welke formule geeft T uitgedrukt in k?", goed,
              [lin(-s, T0 + h0, "T", "k", omgekeerd=True), lin(-s, T0 - h0, "T", "k", omgekeerd=True), lin(-r, c, "T", "k", omgekeerd=True), lin(s, c, "T", "k", omgekeerd=True)],
              f"T = {fmt(T0)} − {fmt(r)}({fmt(v)}k + {fmt(h0)}) = {fmt(T0)} − {fmt(s)}k − {fmt(r * h0)} = {fmt(c)} − {fmt(s)}k.")

def q13_berg_waarde(rng):
    T0, r, v, h0, c, s = berg(rng); k = rng.choice([8, 10, 12, 16, 20])
    w = c - s * k
    return IN(f"Gegeven: T = {fmt(T0)} − {fmt(r)}h en h = {fmt(v)}k + {fmt(h0)}, met k het aantal kwartieren wandelen. Bereken de temperatuur T na {k} kwartier.",
              num_ans(w), f"h = {fmt(v)} · {k} + {fmt(h0)} = {fmt(v * k + h0)}. T = {fmt(T0)} − {fmt(r)} · {fmt(v * k + h0)} = {fmt(w)} °C.")

def q13_haakjes(rng, waar):
    a = F(rng.choice([2, 3, 4, 5, 6])); c = F(rng.randint(2, 9)); d = F(rng.choice([2, 3, 4, 5])); e = F(rng.randint(1, 15))
    goed = lin(-a * d, a * c + e, "h", "p")
    fout = lin(-d, a * c + e, "h", "p")
    return WO(f"Als je t = {fmt(c)} − {fmt(d)}p substitueert in h = {fmt(a)}t + {fmt(e)}, krijg je {goed if waar else fout}.", waar,
              f"h = {fmt(a)}({fmt(c)} − {fmt(d)}p) + {fmt(e)} = {fmt(a * c)} − {fmt(a * d)}p + {fmt(e)}, dus {goed}. Zonder haakjes vergeet je {fmt(d)}p met {fmt(a)} te vermenigvuldigen.")

def q13_leeftijd(rng):
    b = rng.randint(3, 9); m = rng.choice([2, 3]); n = rng.choice([1, 2, 3])
    a = m * b; c = a - n; S = a + b + c
    namen = keuze(rng, [("Abel", "Berend", "Ceciel"), ("Iris", "Jesse", "Kiki"), ("Omar", "Pim", "Quinty")])
    return IN(f"{namen[0]} is {['', '', 'twee', 'drie'][m]} keer zo oud als {namen[1]} (a = {m}b). {namen[2]} is {n} jaar jonger dan {namen[0]} (c = a − {n}). Samen zijn ze {S} jaar. Hoe oud is {namen[1]}?",
              str(b), f"a + b + c = {S}. Substitueer a = {m}b en c = {m}b − {n}: {m}b + b + {m}b − {n} = {S} → {2 * m + 1}b = {S + n} → b = {b}.")

def q13_balans(rng):
    while True:
        bb = rng.choice([110, 120, 130, 140, 150]); D = rng.choice([20, 30, 40, 50, 60]); aa = bb + D
        na, nb = rng.choice([(3, 2), (2, 3), (4, 3), (3, 4)])
        W = na * aa + nb * bb; break
    return IN(f"Op een balans liggen {na} appels en {nb} bananen; samen wegen ze {W} gram (dus {na}a + {nb}b = {W}). Eén appel weegt {D} gram meer dan één banaan (a = b + {D}). Bereken door te substitueren hoeveel gram één banaan weegt.",
              str(bb), f"{na}(b + {D}) + {nb}b = {W} → {na + nb}b + {na * D} = {W} → {na + nb}b = {W - na * D} → b = {bb} gram (en een appel {aa} gram).")

def q13_terug(rng):
    c = F(rng.choice([2, 3, 4, 5])); a = F(rng.choice([2, 3, -2, 4, 5])); b = F(rng.randint(-20, 10) or -6); e = F(rng.randint(-9, 15) or 9)
    return IN(f"De formule t = ax + b wordt gesubstitueerd in de formule y = {fmt(c)}t {'+' if e > 0 else '−'} {fmt(abs(e))}. Het resultaat is {lin(c * a, c * b + e)}. Bereken a.",
              num_ans(a), f"y = {fmt(c)}(ax + b) {'+' if e > 0 else '−'} {fmt(abs(e))} = {fmt(c)}a·x + {fmt(c)}b {'+' if e > 0 else '−'} {fmt(abs(e))}. Dus {fmt(c)}a = {fmt(c * a)} → a = {fmt(a)} (en {fmt(c)}b {'+' if e > 0 else '−'} {fmt(abs(e))} = {fmt(c * b + e)} → b = {fmt(b)}).")

def q13_open(rng):
    A, T, P, a, b, c, d = subs(rng)
    if abs(a * c) == 1 or a * d + b == 0: return q13_open(rng)
    goed = lin(a * c, a * d + b, A, P)
    return OP(f"Substitueer formule B in formule A en vereenvoudig het resultaat. A: {lin(a, b, A, T)}   B: {lin(c, d, T, P)}",
              goed, [sleutel_term(a * c, P), sleutel_const(a * d + b)], 2,
              f"{A} = {fmt(a)}({expr(c, d).replace('x', P)}) {'+' if b > 0 else '−'} {fmt(abs(b))} = {goed.split(' = ')[1]}.")

P13 = ["sub", "coef", "const", "herleid", "haakjes:T", "nul", "fabriek", "berg", "berg_waarde", "haakjes:F",
       "leeftijd", "balans", "terug", "sub", "herleid", "haakjes:F", "sub", "nul", "haakjes:T", "open"]

# ================= §1.4 Exponentiële groei =================
CTX = ["het aantal vissen in een vijver", "het aantal volgers van een account", "het aantal planten in een kas", "het aantal bezoekers van een website", "het aantal bacteriën in een bakje", "de hoeveelheid medicijn in het bloed", "het aantal konijnen op een eiland", "het aantal downloads van een spel"]
def exp_rij(rng, g=None, n=5):
    while True:
        g = g or F(rng.choice(["0.8", "0.9", "1.1", "1.2", "1.25", "1.5", "0.75", "2", "0.5", "3"]))
        b = F(rng.choice([16, 32, 48, 64, 80, 128, 160, 256, 320, 640, 1024, 2048]))
        rij = [b * g ** i for i in range(n)]
        if all(x.denominator == 1 for x in rij): return b, g, rij
        g = None

def q14_welke(rng):
    b, g, rij = exp_rij(rng)
    d = F(rng.choice([4, 6, 8, 12])); s = F(rng.randint(10, 60))
    lin_r = [s + d * i for i in range(5)]
    kw = [F(i * i + rng.choice([1, 2, 3])) for i in range(1, 6)]
    wis = [F(x) for x in rng.sample(range(10, 90), 5)]
    tabellen = [rij, lin_r, kw, wis]; namen = ["A", "B", "C", "D"]
    volg = list(range(4)); rng.shuffle(volg)
    rijen = [["t", "0", "1", "2", "3", "4"]] + [[namen[j]] + [fmt(x) for x in tabellen[volg[j]]] for j in range(4)]
    vraag_lin = rng.random() < 0.35
    doel = 1 if vraag_lin else 0
    juist = namen[volg.index(doel)]
    ctx = keuze(rng, CTX)
    return MC(f"De tabellen A t/m D geven {ctx} op vier plekken. Welke tabel hoort bij {'lineaire' if vraag_lin else 'exponentiële'} groei?", f"tabel {juist}",
              [f"tabel {n}" for n in namen if n != juist],
              ("Bij lineaire groei komt er steeds hetzelfde getal bij (+" + fmt(d) + ")." if vraag_lin else f"Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×{fmt(g)}).") + f" Dat is tabel {juist}.",
              svg_tabel(rijen))

def q14_factor(rng):
    b = rng.choice([300000, 120000, 45000, 8000, 2500, 600]); g = F(rng.choice(["0.9", "0.85", "1.04", "1.15", "0.96", "1.08", "0.92", "1.12"]))
    jaar = rng.choice([2018, 2019, 2020])
    rij = [round(b * float(g) ** i) for i in range(4)]
    fig = svg_tabel([["jaar"] + [str(jaar + i) for i in range(4)], ["aantal"] + [fmt(x, dui=True) for x in rij]])
    plek = keuze(rng, ["een zwembad", "een museum", "een dierentuin", "een pretpark", "een bioscoop", "een bibliotheek", "een festival"])
    return IN(f"In de tabel zie je het aantal bezoekers van {plek} vanaf {jaar}. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
              fmt(g, 2).replace('−', '-'), f"{fmt(rij[1], dui=True)} : {fmt(rij[0], dui=True)} ≈ {fmt(rij[1] / rij[0], 2)}; ook {fmt(rij[2], dui=True)} : {fmt(rij[1], dui=True)} ≈ {fmt(rij[2] / rij[1], 2)}. De groeifactor is {fmt(g, 2)}.", fig, tol=0.006)

def q14_formule(rng):
    b, g, rij = exp_rij(rng)
    fig = svg_tabel([["t", "0", "1", "2", "3", "4"], ["A"] + [fmt(x) for x in rij]])
    goed = f"A = {fmt(b)} · {macht(g)}"
    return MC(f"De tabel geeft {keuze(rng, CTX)} (A) op tijdstip t, te beginnen met {fmt(rij[0])}. Welke formule hoort bij de tabel?", goed,
              [f"A = {fmt(rij[1])} · {macht(g)}", f"A = {fmt(b)} · {macht(1 / g if g != 1 else 2)}", f"A = {fmt(b)} + {fmt(rij[1] - rij[0])}t", f"A = {fmt(g)} · {macht(b)}"],
              f"Op t = 0 is A = {fmt(b)} (beginwaarde). Elke stap ×{fmt(g)} ({fmt(rij[1])} : {fmt(rij[0])} = {fmt(g)}). Dus {goed}.", fig)

def q14_terug(rng):
    g = F(rng.choice(["0.85", "0.8", "0.9", "1.2", "1.25", "0.75"])); N = rng.choice([1200, 1500, 2400, 3000, 960, 4800])
    tijd = rng.choice(["04.00", "06.00", "08.00", "10.00"]); h = int(tijd[:2]) - 1
    w = F(N) / g
    return IN(f"Het aantal muggen verandert exponentieel met groeifactor {fmt(g)} per uur. Om {tijd} uur zijn er {N} muggen. Hoeveel muggen waren er om {h:02d}.00 uur? Rond af op een geheel getal.",
              str(round(w)), f"Terug in de tijd: delen door de groeifactor. {N} : {fmt(g)} ≈ {fmt(w, 1)} → {round(w)} muggen.", tol=1)

def q14_vooruit(rng):
    p = rng.choice([5, 8, 10, 12, 15, 20]); af = rng.random() < 0.6; N = rng.choice([4500, 2000, 3600, 800, 12000]); k = rng.choice([2, 3, 4])
    g = F(100 + (-p if af else p), 100)
    w = N * g ** k
    return IN(f"Het aantal downloads van een app neemt per uur met {p}% {'af' if af else 'toe'}. Om 10.00 uur zijn er {fmt(N, dui=True)} downloads. Bereken het aantal downloads om {10 + k}.00 uur. Rond af op een geheel getal.",
              str(round(w)), f"Groeifactor {fmt(g)}. Na {k} uur: {fmt(N, dui=True)} · {macht(g, k)} ≈ {fmt(w, 1)} → {round(w)}.", tol=1)

def q14_procent(rng):
    p = rng.choice([3, 4, 6, 8, 12, 15, 20, 25]); af = rng.random() < 0.5
    g = F(100 + (-p if af else p), 100)
    return MC(f"Een hoeveelheid neemt elk jaar met {p}% {'af' if af else 'toe'}. Hoe groot is de groeifactor per jaar?", fmt(g),
              [fmt(F(100 + (p if af else -p), 100)), fmt(F(p, 100)), fmt(F(p, 10)), fmt(1 + F(p, 10))],
              f"{'Afname' if af else 'Toename'} van {p}%: je houdt {100 + (-p if af else p)}% over, dus groeifactor {fmt(g)}.")

def q14_fout(rng, waar):
    p = rng.choice([5, 8, 10, 12, 20])
    g = F(100 - p, 100)
    if waar:
        return WO(f"Het aantal neemt per uur met {p}% af. Om het aantal één uur eerder te berekenen, deel je het huidige aantal door {fmt(g)}.", True,
                  f"Terug in de tijd deel je door de groeifactor; die is {fmt(g)}.")
    return WO(f"Het aantal neemt per uur met {p}% af. Om het aantal één uur eerder te berekenen, vermenigvuldig je het huidige aantal met {fmt(1 + F(p, 100))}.", False,
              f"Je moet delen door de groeifactor {fmt(g)}. Vermenigvuldigen met {fmt(1 + F(p, 100))} geeft een ander (te klein) antwoord, want {p}% van een kleiner getal is minder.")

def q14_isexp(rng, waar):
    if waar:
        b, g, rij = exp_rij(rng, n=4)
    else:
        b, g, rij = exp_rij(rng, n=4); rij = [rij[0] + i * abs(rij[1] - rij[0]) for i in range(4)]
    return WO(f"De tabel t = 0, 1, 2, 3 met de waarden {', '.join(fmt(x) for x in rij)} hoort bij een exponentieel verband.", waar,
              (f"De factor is steeds {fmt(rij[1] / rij[0])}." if waar else f"Er komt steeds {fmt(rij[1] - rij[0])} bij: dat is lineair; de factoren ({fmt(rij[1] / rij[0], 2)}, {fmt(rij[2] / rij[1], 2)}) zijn niet gelijk."))

def q14_t0(rng):
    g = F(rng.choice([2, 3, F(3, 2), F(5, 4), 4])); b = F(rng.choice([7, 12, 16, 32, 64, 48]))
    rij = [b * g ** i for i in range(1, 5)]
    if any(x.denominator != 1 for x in rij) or b.denominator != 1: return q14_t0(rng)
    fig = svg_tabel([["t", "0", "1", "2", "3", "4"], ["a", "…"] + [fmt(x) for x in rij]])
    return IN(f"De tabel ({keuze(rng, CTX)}) hoort bij een exponentieel verband met waarden {fmt(rij[0])} op t = 1 en {fmt(rij[1])} op t = 2. Bereken de waarde van a op t = 0.", num_ans(b),
              f"Groeifactor: {fmt(rij[1])} : {fmt(rij[0])} = {fmt(g)}. Terug naar t = 0: {fmt(rij[0])} : {fmt(g)} = {fmt(b)}.", fig)

def q14_grafiek(rng):
    b = rng.choice([100, 200, 400, 800]); g = F(rng.choice([2, F(1, 2), F(3, 2)]))
    ys = [b * g ** i for i in range(4)]
    top, stap = nette_as(max(ys))
    fig = svg_graph(0, 4, 0, float(top), ystap=float(stap), krommen=[lambda t: b * float(g) ** t],
                    punten=[(i, float(y), pt(i, y)) for i, y in enumerate(ys)], xlabel="t", ylabel="N", eenheid=34)
    goed = f"N = {b} · {macht(g)}"
    return MC(f"De grafiek geeft {keuze(rng, CTX)} (N), met {fmt(ys[2])} op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?", goed,
              [f"N = {fmt(ys[1])} · {macht(g)}", f"N = {b} · {macht(1 / g)}", f"N = {b} + {fmt(ys[1] - ys[0])}t", f"N = {fmt(g)} · {macht(b)}"],
              f"Op t = 0 is N = {b}. Van t = 0 naar t = 1: {fmt(ys[1])} : {b} = {fmt(g)}. Dus {goed}.", fig)

def q14_bevolking(rng):
    b = F(rng.choice(["4.40", "6.20", "2.80", "8.50", "3.60", "5.10", "12.40"])); g = rng.choice([1.034, 1.045, 1.06, 0.97, 1.021])
    rij = [round(float(b) * g ** i, 2) for i in range(4)]
    fig = svg_tabel([["jaar", "2000", "2005", "2010", "2015"], ["bevolking (mln)"] + [fmt(x, 2) for x in rij]])
    f = rij[3] / rij[2]
    return IN(f"De bevolking van een land groeit exponentieel: in 2000 waren er {fmt(rij[0], 2)} miljoen en in 2005 {fmt(rij[1], 2)} miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
              fmt(f, 3).replace('−', '-'), f"{fmt(rij[3], 2)} : {fmt(rij[2], 2)} ≈ {fmt(f, 3)}. (De andere stappen geven ongeveer hetzelfde: {fmt(rij[1] / rij[0], 3)}, {fmt(rij[2] / rij[1], 3)}.)", fig, tol=0.002)

def q14_open(rng):
    b, g, rij = exp_rij(rng, n=4)
    return OP(f"Ga na of de tabel t = 0, 1, 2, 3 met de waarden {', '.join(fmt(x) for x in rij)} bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
              f"Bereken telkens de factor: {fmt(rij[1])} : {fmt(rij[0])} = {fmt(g)}, {fmt(rij[2])} : {fmt(rij[1])} = {fmt(g)} … De factor is steeds gelijk ({fmt(g)}), dus het verband is exponentieel.",
              ["factor/delen/deel/gedeeld", "gelijk/hetzelfde/zelfde/steeds"], 2,
              f"Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds {fmt(g)}.")

P14 = ["welke", "factor", "formule", "terug", "isexp:T", "vooruit", "procent", "fout:F", "t0", "grafiek",
       "bevolking", "isexp:F", "terug", "welke", "procent", "fout:T", "vooruit", "formule", "t0", "open"]

# ================= §1.5 Groeifactor en tijd =================
def q15_kwadraat(rng):
    g = F(rng.choice(["2.4", "1.3", "1.5", "0.8", "1.1", "0.9", "1.2"])); eenh = rng.choice([("half uur", "uur"), ("week", "twee weken"), ("halfjaar", "jaar")])
    return IN(f"Een hoeveelheid groeit exponentieel met groeifactor {fmt(g)} per {eenh[0]}. Bereken de groeifactor per {eenh[1]}.",
              num_ans(g * g), f"Per {eenh[1]} zijn er twee stappen: {fmt(g)} · {fmt(g)} = {macht(g, 2)} = {fmt(g * g)}.", tol=0.0005)

def q15_macht(rng):
    g = F(rng.choice(["1.2", "1.1", "0.9", "1.3", "0.8", "1.05"])); n = rng.choice([4, 3, 6])
    eenh = {4: ("kwartier", "uur"), 3: ("twintig minuten", "uur"), 6: ("tien minuten", "uur")}[n]
    w = float(g) ** n
    return IN(f"In de formule A = 10 · {macht(g)} is t de tijd in {'kwartieren' if n == 4 else 'eenheden van ' + eenh[0]}. Bereken de groeifactor per {eenh[1]}. Rond af op twee decimalen.",
              fmt(w, 2).replace('−', '-'), f"In een uur passen {n} keer {eenh[0]}. Groeifactor per uur: {macht(g, n)} ≈ {fmt(w, 4)} ≈ {fmt(w, 2)}.", tol=0.006)

def q15_jaar(rng):
    g = rng.choice([1.019, 1.012, 1.025, 0.985, 1.03, 0.97, 1.015, 0.98])
    w = g ** 12
    return MC(f"De waarde van {keuze(rng, ['een postzegelverzameling', 'een schilderij', 'een oude auto', 'een aandeel', 'een stripboek'])} groeit met groeifactor {fmt(g, 3)} per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
              fmt(w, 3), [fmt(1 + 12 * (g - 1), 3), fmt(g * 12, 3), fmt(g ** 4, 3), fmt(g ** (1 / 12), 3)],
              f"Een jaar = 12 maanden: {fmt(g, 3)}¹² ≈ {fmt(w, 3)}. Je mag de procenten niet zomaar met 12 vermenigvuldigen.")

def q15_formule(rng):
    b = rng.choice([500, 200, 1000, 80]); g = rng.choice([1.06, 1.1, 1.04, 0.95, 0.9]); n = rng.choice([3, 4])
    eenh = {3: "twintig minuten", 4: "kwartieren"}[n]
    w = g ** n
    goed = f"A = {b} · {fmt(w, 2)}ᵗ"
    return MC(f"Een algensoort groeit volgens A = {b} · {fmt(g, 2)}ᵗ, met t in {'eenheden van ' + eenh if n == 3 else eenh}. Welke formule hoort bij t in uren?", goed,
              [f"A = {b} · {fmt(g * n, 2)}ᵗ", f"A = {b * n} · {fmt(g, 2)}ᵗ", f"A = {fmt(b * w, 0)} · {fmt(w, 2)}ᵗ", f"A = {b} · {fmt(g ** (1 / n), 2)}ᵗ"],
              f"In een uur passen {n} tijdseenheden: groeifactor per uur {fmt(g, 2)}{str(n).translate(SUP)} ≈ {fmt(w, 2)}. De beginwaarde ({b}) blijft hetzelfde.")

def q15_terug(rng):
    g = rng.choice([1.07, 1.025, 1.12, 1.05, 0.95, 1.1]); N = rng.choice([2000, 254200, 320000, 15000, 8000]); n = rng.choice([3, 4, 5])
    eenh = rng.choice(["uur", "maand", "jaar"])
    w = N / g ** n
    return IN(f"Een hoeveelheid groeit exponentieel met groeifactor {gs(g)} per {eenh}. Nu is de hoeveelheid {fmt(N, dui=True)}. Hoe groot was de hoeveelheid {n} {eenh if eenh != 'maand' else 'maanden'} eerder? Rond af op een geheel getal.",
              str(round(w)), f"Groeifactor per {n} {eenh if eenh != 'maand' else 'maanden'}: {gs(g)}{str(n).translate(SUP)}. Terugrekenen = delen: {fmt(N, dui=True)} : {gs(g)}{str(n).translate(SUP)} ≈ {round(w)}.", tol=max(1, round(w) // 2000))

def q15_procent(rng):
    g = F(rng.choice(["1.019", "1.035", "1.12", "0.96", "0.88", "1.008"]))
    p = (g - 1) * 100
    toe = p > 0
    return MC(f"De waarde W van een vaas wordt berekend met W = 20 · {macht(g)}, met t in maanden. Wat gebeurt er per maand met de waarde?",
              f"{'+' if toe else '−'}{fmt(abs(p))}% per maand",
              [f"{'+' if toe else '−'}{fmt(abs(p) * 10)}% per maand", f"{'+' if toe else '−'}{fmt(abs(p) / 10)}% per maand", f"{'−' if toe else '+'}{fmt(abs(p))}% per maand", f"+{fmt(g * 100)}% per maand"],
              f"Groeifactor {fmt(g)} = {fmt(g * 100)}%, dus {'toename' if toe else 'afname'} van {fmt(abs(p))}% per maand.")

def q15_lex(rng, waar):
    if waar:
        g = rng.choice(["1,07", "0,95", "1,3", "2,4"]); n = rng.choice([2, 3, 5])
        return WO(f"Als de groeifactor per jaar {g} is, dan is de groeifactor per {n} jaar gelijk aan {g}{str(n).translate(SUP)}.", True,
                  f"Elk jaar vermenigvuldig je met {g}; na {n} jaar dus {n} keer: {g}{str(n).translate(SUP)}.")
    p = rng.choice([2, 3, 5, 10]); n = rng.choice([10, 20])
    return WO(f"{keuze(rng, ['Een spaarbedrag', 'De bevolking', 'Een hoeveelheid', 'Het aantal leden van een club'])} groeit met {p}% per jaar. Dat is hetzelfde als een groei van {p * n}% in {n} jaar.", False,
              f"De groeifactor per {n} jaar is {fmt(1 + F(p, 100))}{str(n).translate(SUP)} ≈ {fmt((1 + p / 100) ** n, 3)}, dus ongeveer {fmt(((1 + p / 100) ** n - 1) * 100, 1)}% groei, niet {p * n}%.")

def q15_grafiek(rng):
    b = rng.choice([1000, 800, 1600, 1200, 2400, 60, 50, 40, 30]); g = F(1, 2) if b >= 800 else F(2)
    ys = [b * g ** i for i in range(5)]
    top, stap = nette_as(max(ys))
    fig = svg_graph(0, 5, 0, float(top), ystap=float(stap), krommen=[lambda t: b * float(g) ** t],
                    punten=[(i, float(y), pt(i, y)) for i, y in enumerate(ys) if i < 3], xlabel="tijd in kwartieren", ylabel="aantal bacteriën", eenheid=36)
    vraag_uur = rng.random() < 0.5
    w = g ** (4 if vraag_uur else 2)
    return IN(f"De grafiek laat de {'afname' if g < 1 else 'groei'} van een aantal bacteriën zien; op t = 0 zijn het er {b}. Bereken de groeifactor per {'uur' if vraag_uur else 'half uur'}." + (" Geef je antwoord als decimaal getal." if w.denominator != 1 else ""),
              num_ans(w), f"Per kwartier: {fmt(ys[1])} : {fmt(ys[0])} = {fmt(g)}. Een {'uur is 4' if vraag_uur else 'half uur is 2'} kwartier: {macht(g, 4 if vraag_uur else 2)} = {fmt(w)}.", fig)

def q15_tabel3(rng):
    b = rng.choice([6400, 25600, 12800]); g = F(rng.choice([F(3, 4), F(5, 4), F(1, 2)]))
    rij = [b * g ** i for i in range(4)]
    fig = svg_tabel([["jaar", "2020", "2021", "2022", "2023"], ["inwoners"] + [fmt(x, dui=True) for x in rij]])
    w = g ** 3
    return MC(f"Het aantal inwoners van een dorp verandert exponentieel: {fmt(rij[0], dui=True)} in 2020 en {fmt(rij[1], dui=True)} in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?", fmt(w),
              [fmt(3 * g), fmt(g), fmt(1 + 3 * (g - 1)), fmt(g ** 2)],
              f"Groeifactor per jaar: {fmt(rij[1], dui=True)} : {fmt(rij[0], dui=True)} = {fmt(g)}. Per drie jaar: {macht(g, 3)} = {fmt(w)}.", fig)

def q15_waarde(rng):
    b = rng.choice([20, 50, 120, 300]); g = rng.choice([1.019, 1.012, 1.025]); m = rng.choice([24, 36, 18])
    w = b * g ** m
    return IN(f"De waarde W in dollars van een vaas is W = {b} · {fmt(g, 3)}ᵗ, met t in maanden. Hoeveel dollar is de vaas na {m // 12 if m % 12 == 0 else m} {'jaar' if m % 12 == 0 else 'maanden'} waard? Rond af op twee decimalen.",
              fmt(w, 2).replace('−', '-'), f"{'Na ' + str(m // 12) + ' jaar is t = ' + str(m) if m % 12 == 0 else 't = ' + str(m)}: W = {b} · {fmt(g, 3)}{str(m).translate(SUP)} ≈ {fmt(w, 2)} dollar.", tol=0.02)

def q15_sneller(rng):
    gA = rng.choice([1.9, 1.6, 1.4, 1.5]); gB = rng.choice([19, 12, 8, 30])
    perA = gA ** 6
    sn = "soort A" if perA > gB else "soort B"
    return MC(f"Soort A groeit met groeifactor {fmt(gA, 1)} per 10 minuten, soort B met groeifactor {gB} per uur. Welke soort groeit het snelst?", sn,
              ["soort B" if sn == "soort A" else "soort A", "ze groeien even snel", "dat kun je niet vergelijken"],
              f"Zet A om naar een uur (6 × 10 minuten): {fmt(gA, 1)}⁶ ≈ {fmt(perA, 1)}. Vergelijk met {gB}: {sn} groeit het snelst.")

def q15_open(rng):
    b = rng.choice([500, 200, 1000]); g = rng.choice([1.06, 1.1, 1.04, 0.9]); n = 3
    w = g ** n
    s = fmt(w, 2)
    return OP(f"Een hoeveelheid groeit volgens A = {b} · {fmt(g, 2)}ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
              f"A = {b} · {s}ᵗ", [f"{s}/{s.replace(',', '.')}"], 1,
              f"In een uur passen 3 eenheden van twintig minuten: {fmt(g, 2)}³ ≈ {s}. De beginwaarde blijft {b}: A = {b} · {s}ᵗ.")

P15 = ["kwadraat", "macht", "jaar", "formule", "lex:F", "terug", "procent", "grafiek", "tabel3", "lex:T",
       "waarde", "sneller", "kwadraat", "macht", "lex:F", "terug", "formule", "grafiek", "jaar", "open"]

PARAS = [
    ("1.1", "Lineaire formules opstellen", "q11", P11),
    ("1.2", "Lijnen snijden", "q12", P12),
    ("1.3", "Formules substitueren", "q13", P13),
    ("1.4", "Exponentiële groei", "q14", P14),
    ("1.5", "Groeifactor en tijd", "q15", P15),
]
NIVEAU = ["basis", "oefenen", "gemengd", "toetsniveau", "eindniveau"]

def mc_volgorde(rng, n):
    while True:
        p = [rng.randrange(4) for _ in range(n)]
        if max(p.count(k) for k in range(4)) > 0.4 * n: continue
        if sum((b - a) % 4 == 1 for a, b in zip(p, p[1:])) >= 0.5 * (n - 1): continue
        if any(p[i:i + per] == p[i + per:i + 2 * per] for per in (2, 3, 4) for i in range(n - 2 * per + 1)): continue
        return p

def bouw(slot, prefix, rng):
    naam, _, tf = slot.partition(':')
    fn = globals()[f"{prefix}_{naam}"]
    if tf: return fn(rng, tf == "T")
    return fn(rng)

nr = 20; fid = 10; manifest = []
for pi, (par, ptitel, prefix, plan) in enumerate(PARAS):
    for k in range(5):
        rng = random.Random(1000 * pi + k * 37 + 11)
        vragen = []
        for slot in plan:
            for poging in range(200):
                v = bouw(slot, prefix, rng)
                if v["vraag"] not in GEZIEN:
                    break
            else:
                raise SystemExit(f"geen unieke vraag voor {slot}")
            GEZIEN.add(v["vraag"]); vragen.append(v)
        mcs = [v for v in vragen if v["type"] == "mc"]
        pos = iter(mc_volgorde(rng, len(mcs)))
        for v in mcs:
            opts = v.pop("_opts"); goed = opts[0]; rest = opts[1:]; rng.shuffle(rest)
            i = next(pos); rest.insert(i, goed)
            v["opties"] = rest; v["antwoord"] = i
        for v in vragen:
            if v["type"] == "invul": assert v["antwoord"], v
        ex = {"id": f"ex-wiskunde-h1-{fid}", "hoofdstuk": 1, "paragraaf": par,
              "titel": f"Proeftoets {nr} — §{par} {ptitel} ({k + 1}/5, {NIVEAU[k]})",
              "vak": "Wiskunde · H1 Lineaire en exponentiële formules", "icoon": "📈", "duurMin": 30, "vragen": vragen}
        with open(f"{OUT}/examen_{nr}.js", "w") as f:
            f.write("/* =========================================================\n"
                    f"   Duru's Wiskunde (HAVO 3) — {ex['titel']}\n"
                    f"   Bron: Noordhoff H1 Lineaire en exponentiële formules, §{par} (opgaven uit het boek met andere getallen;\n"
                    "   antwoorden berekend door tools-script, figuren als inline SVG)\n"
                    "   ========================================================= */\n")
            f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        manifest.append(nr); nr += 1; fid += 1
print("geschreven:", manifest[0], "…", manifest[-1])
