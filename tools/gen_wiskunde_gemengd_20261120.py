"""Wiskunde gemengd (2026-11-20): 3 proeftoetsen ex-wiskunde-gemengd-20261120-1…3, examen_129…131.
Per toets: 11 vragen H2 (zwakke punten: context-parabool start/cm/top, zelfde-y, top-figuur, haakjes wegwerken),
7 vragen H1 §1.1–§1.5 (ctx-lineair, snijpunt, groeifactor/tijdseenheid), 2 vragen Statistiek (Herhaling MAVO 2).
Gebruik: python3 tools/gen_wiskunde_gemengd_20261120.py havo3/wiskunde/js/data <vragen.json>  (lijst van bestaande vraagteksten)
Nieuwe ids/bestanden alleen; bestaande toetsen worden niet aangeraakt."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_wiskunde_h1_paragraaf_exams as H1
import gen_wiskunde_h1_14_15_extra as H1X
import gen_wiskunde_parabolen_22_extra as H2X
from gen_wiskunde_h2_parabolen import *  # noqa: F401,F403  (kw, n, IN, MC, sleutel, F, keuze, ...)
from gen_wiskunde_h1_paragraaf_exams import MC as MC1

def sc(x): return sleutel(F(x))

# ---- nieuwe kleine contextstappen (beginhoogte / hoogste punt in cm) ----
def ctx_begin(rng):
    k = keuze(rng, [F(-1, 5), F(-3, 10), F(-2, 5), F(-1, 2)]); a0 = keuze(rng, [1, 2, 3]); c = keuze(rng, [F(3, 10), F(1, 2), F(6, 5), F(1, 5)])
    b = -2 * k * a0
    if b.denominator > 10: return ctx_begin(rng)
    f = kw(k, b, c, "a", "h")
    return IN(f"Een bal wordt weggeschoten volgens {f}. Hierin is h de hoogte in meters en a de horizontale afstand in meters. "
              f"Stap 1: vul a = 0 in. Op welke hoogte in meters begint de bal?", sc(c),
              f"a = 0 invullen: h = {n(k)} · 0² + {n(b)} · 0 + {n(c)} = {n(c)}. Het getal c is dus de beginhoogte: {n(c)} m.")

def ctx_vorm(rng):
    k = keuze(rng, [F(-1, 5), F(-1, 4), F(-1, 2), F(-1, 10)]); p = keuze(rng, [2, 3, 4, 5]); q = keuze(rng, [F(3, 2), F(2), F(5, 2), F(9, 5)])
    return IN(f"De baan van een bal is h = {n(k)}(a − {p})² + {n(q)} (h en a in meters). Het hoogste punt is de top. Hoeveel cm hoog komt de bal maximaal?",
              sc(q * 100), f"In y = a(x − p)² + q is q de y-coördinaat van de top. Hier: top ({p}, {n(q)}), dus {n(q)} m = {n(q * 100)} cm (meter × 100). Het getal bij a is geen hoogte.")

# ---- Statistiek (Herhaling MAVO 2) ----
def lijst(rng, k): return [rng.randint(2, 15) for _ in range(k)]
def st_gem(rng):
    while True:
        l = lijst(rng, 5)
        if sum(l) % 5 == 0 and len(set(l)) > 2: break
    return IN(f"Bereken het gemiddelde van de getallen: {', '.join(map(str, l))}.", str(sum(l) // 5), f"Som = {' + '.join(map(str, l))} = {sum(l)}; delen door 5 geeft {sum(l) // 5}.")
def st_med(rng):
    while True:
        l = lijst(rng, 7); s = sorted(l)
        if len(set(l)) >= 5 and l[3] != s[3] and s[2] != s[3] != s[4]: break
    m = s[3]
    fout = [l[3], s[2], s[4], s[1]]
    return MC1(f"Wat is de mediaan van de getallen: {', '.join(map(str, l))}?", str(m), [str(x) for x in fout],
               f"Eerst sorteren: {', '.join(map(str, s))}. Het middelste (4e) getal is {m}. Het middelste getal van de ongesorteerde rij ({l[3]}) telt niet.")
def st_mod(rng):
    while True:
        l = [rng.randint(3, 12) for _ in range(9)]
        c = sorted(((l.count(x), x) for x in set(l)), reverse=True)
        if c[0][0] >= 3 and c[0][0] > c[1][0] and len(set(l)) >= 5: break
    m = c[0][1]; fout = [x for x in sorted(set(l)) if x != m]
    rng.shuffle(fout)
    return MC1(f"Wat is de modus van de getallen: {', '.join(map(str, l))}?", str(m), [str(x) for x in fout[:4]],
               f"De modus is het getal dat het vaakst voorkomt: {m} komt {c[0][0]} keer voor.")
def st_med_even(rng):
    while True:
        s = sorted(lijst(rng, 6))
        if s[2] != s[3]: break
    l = s[:]; rng.shuffle(l); m = F(s[2] + s[3], 2)
    return IN(f"Bereken de mediaan van de getallen: {', '.join(map(str, l))}. Een decimaal getal mag.", sc(m),
              f"Gesorteerd: {', '.join(map(str, s))}. Even aantal: het gemiddelde van de twee middelste getallen ({s[2]} en {s[3]}) = {n(m)}.")

BR = {"ctx_begin": ctx_begin, "ctx_vorm": ctx_vorm, "st_gem": st_gem, "st_med": st_med, "st_mod": st_mod, "st_med_even": st_med_even}

def bouw_slot(slot, rng):
    bron, _, rest = slot.partition("|")
    if bron == "H1":
        naam, _, arg = rest.partition(":")
        fn = getattr(H1X, naam, None) or getattr(H1, naam)
        return fn(rng) if not arg else fn(rng, arg == "T")
    if rest in BR: return BR[rest](rng)
    return H2X.bouw(rest, rng)

# per toets: (context-stappen eerst, rest H2 (11 totaal), H1 (7), statistiek (2))
TESTEN = [
    (["H2|ctx_begin", "H2|spC", "H2|hmL"], ["H2|wf", "H2|wf", "H2|zh", "H2|spg", "H2|pmc", "H2|pb", "H2|gmc", "H2|tx"],
     ["H1|q11_sparen", "H1|q12_S", "H1|q12_credits", "H1|q13_coef", "H1|q14_factor", "H1|q15_per_n", "H1|q15_formule_lang"], ["H2|st_gem", "H2|st_med"]),
    (["H2|ctx_vorm", "H2|speer", "H2|tunB"], ["H2|wf", "H2|wf", "H2|zh", "H2|tp", "H2|h21", "H2|pc", "H2|gb", "H2|ty"],
     ["H1|q11_formule_punten", "H1|q12_x", "H1|q12_links_rechts", "H1|q13_herleid", "H1|q14_isexp:T", "H1|q15_terug_maand", "H1|q15_procent_periode"], ["H2|st_mod", "H2|st_med_even"]),
    (["H2|ctx_begin", "H2|spA", "H2|brug"], ["H2|wf", "H2|wf", "H2|zh", "H2|spg", "H2|pmc", "H2|gc", "H2|h21", "H2|tmc"],
     ["H1|q11_rc_start", "H1|q12_y", "H1|q12_vergelijking", "H1|q13_sub", "H1|q14_formule", "H1|q15_per_n", "H1|q15_waarde"], ["H2|st_med", "H2|st_gem"]),
]

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for k, (eerst, rest, h1, st) in enumerate(TESTEN):
        nr = 129 + k; rng = random.Random(129000 + k * 71)
        rest = rest + h1 + st; rng.shuffle(rest); slots = eerst + rest
        vragen = []
        for slot in slots:
            for _ in range(400):
                try: v = bouw_slot(slot, rng)
                except AssertionError: continue
                if norm(v["vraag"]) not in GEZIEN: break
            else: raise SystemExit(f"geen unieke vraag: {slot}")
            GEZIEN.add(norm(v["vraag"]))
            if v["type"] == "invul": assert v["antwoord"], v
            vragen.append(v)
        mcs = [v for v in vragen if v["type"] == "mc"]
        pos = iter(H1.mc_volgorde(rng, len(mcs)) if len(mcs) >= 5 else rng.sample(range(4), len(mcs)))
        for v in mcs:
            o = v.pop("_opts"); rst = o[1:]; rng.shuffle(rst); j = next(pos); rst.insert(j, o[0]); v["opties"] = rst; v["antwoord"] = j
        titel = f"Proeftoets {nr} — Gemengd H2 + H1 + herhaling ({k + 1}/3)"
        ex = {"id": f"ex-wiskunde-gemengd-20261120-{k + 1}", "hoofdstuk": 2, "paragraaf": "mix", "titel": titel,
              "vak": "Wiskunde · H2 Parabolen + H1 Lineair & exponentieel + Herhaling", "icoon": "🔀", "duurMin": 40, "vragen": vragen}
        kop = (f"/* =========================================================\n   Duru's Wiskunde (HAVO 3) — {titel}\n"
               "   Bron: Noordhoff H2 (11 vragen), H1 §1.1–§1.5 (7), Statistiek-herhaling MAVO 2 (2); andere getallen\n"
               "   Gegenereerd met tools/gen_wiskunde_gemengd_20261120.py\n   ========================================================= */\n")
        with open(f"{OUT}/examen_{nr}.js", "w") as fh:
            fh.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: examen_129 … 131")
