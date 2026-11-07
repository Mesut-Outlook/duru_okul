"""Wiskunde gemengd H1 + H2 — 5 proeftoetsen (2026-11-07): ex-wiskunde-h1h2-gemengd-1…5, examen_124…128.
Per toets 20 vragen: 2 per paragraaf §1.1–§1.5 (H1-generator) + 2 per paragraaf §2.1–§2.5 (H2-generator), door elkaar.
hoofdstuk = 2 (laatste stof; de toets staat op de site onder H2), paragraaf = "mix".
Gebruik: python3 tools/gen_wiskunde_h1_h2_gemengd.py havo3/wiskunde/js/data <bestaande-vragen.json>
⚠️ Niet opnieuw draaien op gepubliceerde ids: de inhoud van een gemaakte toets mag niet veranderen."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_wiskunde_h1_paragraaf_exams as H1
import gen_wiskunde_parabolen_22_extra as H2X   # H2-generator + veilige snx/brug + nieuwe §2.2-typen
H2 = H2X  # star-import: bouw/Q/WOQ van gen_wiskunde_h2_parabolen, met de overrides

# (bron, slot): H1 = (prefix, slot) · H2 = slot uit Q/WOQ. Per toets 2 per paragraaf.
H1_POOL = {
    "q11": ["rc_start", "rc_punten", "formule_punten", "grafiek_formule", "op_lijn:T", "op_lijn:F", "evenwijdig", "b_punten", "sparen", "stijgend:F"],
    "q12": ["x", "y", "S", "vergelijking", "grafiek", "geen:T", "geen:F", "credits", "links_rechts", "check:F"],
    "q13": ["sub", "coef", "const", "herleid", "haakjes:T", "haakjes:F", "nul", "berg", "leeftijd", "terug"],
    "q14": ["factor", "formule", "terug", "isexp:T", "isexp:F", "vooruit", "procent", "t0", "grafiek"],
    "q15": ["kwadraat", "macht", "jaar", "formule", "lex:F", "lex:T", "terug", "procent", "waarde", "grafiek"],
}
H2_POOL = {
    "2.1": ["wo21:T", "wo21:F", "mc21", "h21", "hwo21:T", "hwo21:F", "fig21", "ctx21"],
    "2.2": ["tx", "ty", "tmc", "zh", "gx", "gy", "snx", "bz", "tunB", "brug", "sas", "spg"],
    "2.3": ["tw", "ts", "sa", "wf", "tab:T", "tab:F", "spC", "speer"],
    "2.4": ["sm:T", "sm:F", "smal", "breed", "yas", "oors", "syas", "topy", "kop", "lig:T", "lig:F"],
    "2.5": ["gmc", "gb", "gc", "pmc", "pb", "pc", "ptop", "bd25:T", "bd25:F", "hmL", "winst"],
}

def plan(rng):
    slots = [("H1", p, s) for p, l in H1_POOL.items() for s in rng.sample(l, 2)]
    slots += [("H2", p, s) for p, l in H2_POOL.items() for s in rng.sample(l, 2)]
    rng.shuffle(slots)
    return slots

def maak_een(bron, prefix, slot, rng):
    return H1.bouw(slot, prefix, rng) if bron == "H1" else H2.bouw(slot, rng)

if __name__ == "__main__":
    OUT = sys.argv[1]
    norm = lambda t: " ".join(t.lower().split())
    GEZIEN = {norm(t) for t in json.load(open(sys.argv[2]))}
    for k in range(5):
        nr = 124 + k; rng = random.Random(124000 + k * 53)
        vragen = []
        for bron, prefix, slot in plan(rng):
            for _ in range(400):
                v = maak_een(bron, prefix, slot, rng)
                if norm(v["vraag"]) not in GEZIEN: break
            else: raise SystemExit(f"geen unieke vraag: {bron} {slot}")
            GEZIEN.add(norm(v["vraag"]))
            if v["type"] == "invul": assert v["antwoord"], v
            vragen.append(v)
        mcs = [v for v in vragen if v["type"] == "mc"]
        pos = iter(H1.mc_volgorde(rng, len(mcs)) if len(mcs) >= 5 else rng.sample(range(4), len(mcs)))
        for v in mcs:
            o = v.pop("_opts"); rest = o[1:]; rng.shuffle(rest); j = next(pos); rest.insert(j, o[0]); v["opties"] = rest; v["antwoord"] = j
        titel = f"Proeftoets {nr} — Gemengd H1 + H2 ({k + 1}/5)"
        ex = {"id": f"ex-wiskunde-h1h2-gemengd-{k + 1}", "hoofdstuk": 2, "paragraaf": "mix", "titel": titel,
              "vak": "Wiskunde · H1 Lineair & exponentieel + H2 Parabolen", "icoon": "🔀", "duurMin": 40, "vragen": vragen}
        kop = (f"/* =========================================================\n   Duru's Wiskunde (HAVO 3) — {titel}\n"
               "   Bron: Noordhoff H1 §1.1–§1.5 + H2 §2.1–§2.5 (2 vragen per paragraaf, andere getallen)\n"
               "   Gegenereerd met tools/gen_wiskunde_h1_h2_gemengd.py\n   ========================================================= */\n")
        with open(f"{OUT}/examen_{nr}.js", "w") as fh:
            fh.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print("geschreven: examen_124 … 128")
