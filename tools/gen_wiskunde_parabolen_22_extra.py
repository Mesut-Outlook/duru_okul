"""Wiskunde H2 §2.2 Symmetrie en top — 5 extra proeftoetsen (2026-11-07):
ex-wiskunde-parabolen-22-6…10, examen_119…123. Vraagtypen uit tools/gen_wiskunde_h2_parabolen.py + 4 nieuwe
(twee punten zelfde hoogte → top, symmetrieas, gespiegeld punt, waar/onwaar top). Alle algebra met Fraction.
Gebruik: python3 tools/gen_wiskunde_parabolen_22_extra.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_wiskunde_h2_parabolen import *  # noqa: F401,F403  (q22_*, met_top, kw, n, pt, IN, MC, WO, sleutel, uitwerken, maak, F)

def q22_twee_punten(rng):
    xt = F(rng.randint(-8, 8), keuze(rng, [1, 1, 2])); d = rng.randint(2, 9); y = rng.randint(-40, 60)
    x1, x2 = xt - d, xt + d
    return IN(f"De punten {pt(x1, y)} en {pt(x2, y)} liggen op dezelfde parabool. Bereken de x-coördinaat van de top." +
              (" Een breuk of decimaal getal mag." if xt.denominator != 1 else ""),
              sleutel(xt), f"Beide punten hebben y = {n(y)}, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = ({n(x1)} + {hk(x2)}) / 2 = {n(xt)}.")

def q22_symmetrieas(rng):
    a, b, c, p, q = met_top(rng)
    return IN(f"Geef de formule van de symmetrieas van de parabool bij {kw(a, b, c)}. Vul in: x = …", sleutel(p),
              uitwerken(a, b, c) + f" De symmetrieas is de verticale lijn door de top: x = {n(p)}.")

def q22_spiegel(rng):
    a, b, c, p, q = met_top(rng)
    x1 = p + keuze(rng, [-5, -4, -3, -2, 2, 3, 4, 5]); y1 = val(a, b, c, x1); x2 = 2 * p - x1
    return IN(f"De parabool bij {kw(a, b, c)} heeft symmetrieas x = {n(p)}. Het punt {pt(x1, y1)} ligt op de parabool. "
              f"Er is nog een punt met y = {n(y1)}. Bereken de x-coördinaat van dat punt.",
              sleutel(x2), f"{n(x1)} ligt {n(abs(x1 - p))} van de as x = {n(p)}. Het gespiegelde punt ligt even ver aan de andere kant: x = {n(p)} {'+' if x1 < p else '−'} {n(abs(x1 - p))} = {n(x2)}.")

def q22_wo_top(rng, waar):
    a, b, c, p, q = met_top(rng)
    if p == 0: p = F(1); b, c = -2 * a, a + q
    toon = (p, q) if waar else keuze(rng, [(-p, q), (p, c), (q, p)])
    if not waar and toon == (p, q): toon = (-p, q)
    return WO(f"De top van de parabool bij {kw(a, b, c)} is {pt(*toon)}.", waar, uitwerken(a, b, c))

def snx_veilig(rng):   # q22_snijx heeft < 4 unieke opties als een nulpunt 0 is → opnieuw trekken
    while True:
        try: return q22_snijx(rng)
        except AssertionError: pass

def brug_net(rng):   # q22_hangbrug schrijft "− 1a" als m = 1
    v = q22_hangbrug(rng)
    return {k: x.replace("− 1a ", "− a ") if isinstance(x, str) else x for k, x in v.items()}

Q.update({"tp": q22_twee_punten, "sas": q22_symmetrieas, "spg": q22_spiegel, "snx": snx_veilig, "brug": brug_net})
WOQ["wo22"] = q22_wo_top

TOETSEN = [  # 20 vragen; 6/10 basis → 10/10 eindniveau (meer context, b zoeken, gefactoriseerd)
    ("6/10, basis",     ["zh", "tx", "ty", "tmc", "tp", "sas", "wo22:T", "gx", "snx", "spg", "tx", "tmc", "ty", "wo22:F", "zh", "gy", "tunB", "sas", "tmc", "bz"]),
    ("7/10, oefenen",   ["tp", "tmc", "zh", "ty", "gx", "snx", "wo22:F", "spg", "tx", "gy", "sas", "tmc", "tunH", "ty", "wo22:T", "bz", "zh", "brug", "tmc", "tx"]),
    ("8/10, gemengd",   ["tmc", "gy", "sas", "spg", "wo22:T", "tx", "snx", "zh", "tunB", "ty", "tp", "gx", "tmc", "bz", "wo22:F", "brug", "ty", "spg", "tmc", "gy"]),
    ("9/10, toetsniveau", ["gx", "tmc", "bz", "spg", "ty", "wo22:F", "tunH", "sas", "snx", "tmc", "zh", "brug", "tp", "gy", "tmc", "wo22:T", "bz", "tx", "tunB", "ty"]),
    ("10/10, eindniveau", ["bz", "tmc", "brug", "gy", "spg", "tunB", "wo22:T", "ty", "snx", "gx", "tmc", "tunH", "bz", "sas", "wo22:F", "tp", "tmc", "brug", "gy", "ty"]),
]

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for i, (sub, plan) in enumerate(TOETSEN):
        nr = 119 + i; rng = random.Random(22600 + i * 31)
        vragen = maak(plan, rng, GEZIEN, norm)
        titel = f"Proeftoets {nr} — §2.2 Symmetrie en top ({sub})"
        ex = {"id": f"ex-wiskunde-parabolen-22-{6 + i}", "hoofdstuk": 2, "paragraaf": "2.2", "titel": titel,
              "vak": "Wiskunde · Hoofdstuk 2 · Parabolen", "icoon": "⛰️", "duurMin": 30, "vragen": vragen}
        kop = (f"/* =========================================================\n   Duru's Wiskunde (HAVO 3) — {titel}\n"
               "   Bron: Noordhoff H2 Parabolen §2.2 (opgaven uit het boek met andere getallen)\n"
               "   Gegenereerd met tools/gen_wiskunde_parabolen_22_extra.py\n   ========================================================= */\n")
        with open(f"{OUT}/examen_{nr}.js", "w") as fh:
            fh.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: examen_119 … 123")
