#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting — begrippenlijst (onderwerp) + begrippentoets.
Schrijft havo3/biologie/js/data/h11_begrippen.js + examen_18.js (ex-h3-biologie-18).
Begrippen komen uit de BEGRIPPEN-lijsten van tools/gen_biologie_h11_{1..4}.py (bron: Nectar 2-3 FLEX p. 128–151).
⚠️ Zodra Duru de toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_biologie_h11_1 import BEGRIPPEN as B1, plaats, langste_aandeel, schrijf, O
from gen_biologie_h11_2 import BEGRIPPEN as B2
from gen_biologie_h11_3 import BEGRIPPEN as B3
from gen_biologie_h11_4 import BEGRIPPEN as B4

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'biologie', 'js', 'data')
PARAGRAFEN = [("11.1", "Man en vrouw", B1), ("11.2", "Bevruchting", B2),
              ("11.3", "Zwangerschap", B3), ("11.4", "Je lijkt op …", B4)]
ALLE = [(p, t, d) for p, _, lijst in PARAGRAFEN for t, d in lijst]

# Twee open vragen, met de hand: verband tussen begrippen uit verschillende paragrafen.
OPEN = [
    O("Wat is het verschil tussen een <b>embryo</b> en een <b>foetus</b>? Noem wanneer de grens ligt en wat er in elke fase gebeurt.",
      ["twaalf/12", "organ", "groei"], 2,
      "De eerste twaalf weken heet het kindje een embryo: dan ontstaan alle organen. Daarna heet het een foetus en groeit het alleen nog.",
      "§11.3: in de embryonale fase (eerste twaalf weken) ontstaan alle organen; vanaf dan groeit het kindje alleen nog en heet het een foetus."),
    O("Wat is het verschil tussen een <b>eeneiige</b> en een <b>twee-eiige</b> tweeling? Noem bij elk hoe hij ontstaat.",
      ["één eicel/1 eicel/een bevruchte eicel/splitst/deelt", "twee eicellen/2 eicellen"], 2,
      "Een eeneiige tweeling ontstaat uit één bevruchte eicel die zich splitst; een twee-eiige tweeling ontstaat uit twee eicellen die elk door een andere zaadcel worden bevrucht.",
      "Eeneiig: één bevruchte eicel splitst in twee (zelfde erfelijke eigenschappen). Twee-eiig: twee eicellen, twee zaadcellen."),
]


def stam(term):
    w = re.sub(r"^(de|het|een) ", "", term.lower())
    return w[:6] if len(w) > 6 else w


def zonder_term(term, tekst):
    return stam(term) not in tekst.lower()


def mc_vraag(term, defin, pool, rng):
    fout = rng.sample([t for t, _ in pool if t != term], 3)
    return {"type": "mc", "vraag": f"Welk begrip hoort bij deze omschrijving?<br><i>{defin}</i>",
            "_goed": term, "_fout": fout, "uitleg": f"{term}: {defin}"}


def wo_vraag(term, defin, ander_def, waar):
    if waar:
        return {"type": "waaronwaar", "vraag": f"<b>{term}</b> — {defin}", "antwoord": True,
                "uitleg": f"Waar. {term}: {defin}"}
    return {"type": "waaronwaar", "vraag": f"<b>{term}</b> — {ander_def}", "antwoord": False,
            "uitleg": f"Niet waar. Dat is de omschrijving van een ander begrip. {term}: {defin}"}


def varianten(term):
    """'foetaal alcohol syndroom (FAS)' → basis, afkorting, zonder spaties/koppeltekens; nakijken = substring na normaliseren."""
    t = re.sub(r"^(de|het|een) ", "", term.lower())
    m = re.match(r"(.*?)\s*\((.+)\)$", t)
    basis = [m.group(1), m.group(2)] if m else [t]
    alts = []
    for b in basis:
        for v in (b, b.replace("-", " "), b.replace("-", ""), b.replace(" ", "")):
            if v and v not in alts:
                alts.append(v)
    return "|".join(alts)


def vul_vraag(term, defin, typ):
    return {"type": typ, "vraag": f"{defin}<br>Hoe heet dit begrip? ____", "antwoord": varianten(term),
            "uitleg": f"{term}: {defin}"}


def theorie():
    h = ["<h3>Begrippenlijst Hoofdstuk 11 — Voortplanting</h3>",
         "<p>Alle begrippen uit <b>§11.1 t/m §11.4</b> op een rij. Ken ze zo dat je ze kunt <i>uitleggen</i> en "
         "herkent in een vraag. Leer per paragraaf: dek de rechterkolom af en zeg de betekenis hardop.</p>"]
    for p, titel, lijst in PARAGRAFEN:
        h.append(f'<h4>§{p} {titel}</h4>\n<table>\n<tr><th>Begrip</th><th>Betekenis</th></tr>')
        h += [f"<tr><td><b>{t}</b></td><td>{d}</td></tr>" for t, d in lijst]
        h.append("</table>")
    h.append('<div class="info-box tip"><span class="kop">Tip</span> Veel begrippen horen in een rij bij elkaar: '
             'zaadcel → zaadleider → zaadlozing, eicel → eileider → bevruchting → innesteling → embryo → foetus → bevalling.</div>')
    return "\n".join(h)


def main():
    rng = random.Random('bio_h11_begrippen')
    termen = ALLE[:]
    rng.shuffle(termen)
    pool_van = {p: lijst for p, _, lijst in PARAGRAFEN}
    gebruikt = iter(termen)
    gehad = {t.lower() for _, t, _ in ALLE if t.lower() in re.sub(r"<[^>]+>", "", " ".join(v["vraag"].lower() for v in OPEN))}

    def volgende(filter_=lambda t, d: True):
        # elk begrip één keer (sommige staan in twee paragrafen), en niet als het al in een open vraag staat
        for p, t, d in gebruikt:
            if t.lower() not in gehad and filter_(t, d):
                gehad.add(t.lower())
                return p, t, d
        raise SystemExit("te weinig begrippen")

    # onderwerp: 6 mc, 4 waaronwaar (2 onwaar), 2 invoer
    ov = []
    for _ in range(6):
        p, t, d = volgende()
        mv = mc_vraag(t, d, pool_van[p] if len(pool_van[p]) >= 4 else [(x, y) for _, x, y in ALLE], rng)
        mv["niveau"] = 1
        ov.append(mv)
    for i in range(4):
        p, t, d = volgende()
        ander = rng.choice([y for x, y in pool_van[p] if x != t])
        ov.append(wo_vraag(t, d, ander, waar=i % 2 == 0))
    for _ in range(2):
        p, t, d = volgende(zonder_term)
        ov.append(dict(vul_vraag(t, d, "invoer"), niveau=1))
    ov = plaats(ov, rng)

    # begrippentoets: 10 mc, 4 waaronwaar (2 onwaar), 4 invul, 2 open
    ev = []
    for _ in range(10):
        p, t, d = volgende()
        ev.append(mc_vraag(t, d, pool_van[p] if len(pool_van[p]) >= 4 else [(x, y) for _, x, y in ALLE], rng))
    for i in range(4):
        p, t, d = volgende()
        ander = rng.choice([y for x, y in pool_van[p] if x != t])
        ev.append(wo_vraag(t, d, ander, waar=i % 2 == 1))
    for _ in range(4):
        p, t, d = volgende(zonder_term)
        ev.append(vul_vraag(t, d, "invul"))
    ev += [dict(v) for v in OPEN]
    ev = plaats(ev, rng)
    assert len(ev) == 20
    n, tot = langste_aandeel(ev)
    assert n / tot <= 0.4, f"juiste optie {n}/{tot} keer langste"

    onderwerp = {"id": "bio-h11-begrippen", "hoofdstuk": 11, "paragraaf": "11.1–11.4",
                 "titel": "Begrippen Hoofdstuk 11 — Voortplanting",
                 "korteUitleg": "Alle begrippen uit §11.1 t/m §11.4 met hun betekenis.",
                 "icoon": "📖", "kleur": "h11-thema", "theorie": theorie(), "vragen": ov}
    schrijf(os.path.join(ROOT, 'h11_begrippen.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 begrippen) — gegenereerd door tools/gen_biologie_h11_begrippen.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    ex = {"id": "ex-h3-biologie-18", "hoofdstuk": 11, "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
          "paragraaf": "begrippen", "titel": "Toets 18 — Begrippentoets H11 Voortplanting",
          "vak": "Biologie · HAVO 3 (H11)", "icoon": "📖", "duurMin": 20, "vragen": ev}
    schrijf(os.path.join(ROOT, 'examen_18.js'),
            "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 begrippentoets) — gegenereerd door tools/gen_biologie_h11_begrippen.py */\n",
            "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print(f"{len(ALLE)} begrippen; onderwerp {len(ov)} vragen; examen_18: 20 vragen, langste {n}/{tot}")


if __name__ == '__main__':
    main()
