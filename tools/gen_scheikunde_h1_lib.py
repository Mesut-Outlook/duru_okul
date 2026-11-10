#!/usr/bin/env python3
"""Gedeeld schrijfdeel voor scheikunde H1 zwakte-toetsen (examen_h1_45…58, TASK-43) — gen_scheikunde_h1_{e,d,f}.py."""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_extra import M, W, I, O, plaats, langste_aandeel  # noqa: F401 (M/W/I/O voor de data-scripts)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'scheikunde', 'js', 'data')
KORT = " <i>(Eén korte zin is genoeg.)</i>"
GETAL = " <i>(Alleen het getal.)</i>"


def schrijf(examens, seed):
    """examens = {nr: (paragraaf, titel, icoon, [vragen])}; schrijft examen_h1_<nr>.js."""
    rng = random.Random(seed)
    for nr, (par, titel, icoon, vr) in examens.items():
        t = [v["type"] for v in vr]
        assert (t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")) == (10, 5, 4, 1), (nr, t)
        assert sum(v["type"] == "waaronwaar" and v["antwoord"] is False for v in vr) >= 2, nr
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_h1_{nr}: juiste optie {n}/{tot} keer langste"
        for i, v in enumerate(vr, 1):
            vr[i - 1] = {"id": f"sch-h1-{nr}_v{i}", **v}
        ex = {
            "id": f"ex-h3-sch-h1-{nr}",
            "titel": titel,
            "vak": "Scheikunde · HAVO 3 (H1)",
            "hoofdstuk": 1,
            "paragraaf": par,
            "icoon": icoon,
            "duurMin": 25,
            "vragen": vr,
        }
        kop = f"/* =========================================================\n   Duru's Scheikunde (HAVO 3) — {titel}\n   ========================================================= */\n"
        with open(os.path.join(ROOT, f"examen_h1_{nr}.js"), 'w', encoding='utf-8') as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_h1_{nr}: 20 vragen, juiste optie langste {n}/{tot}")
