#!/usr/bin/env python3
"""Aardrijkskunde HAVO 3 · H1 Wereldhandel in beweging — begrippen §1.4 + §1.5 (onderwerp) + begrippentoets.
Schrijft havo3/aardrijkskunde/js/data/h1_45_begrippen.js + examen_97.js (ex-h3-ak-97).
Begrippen komen uit de BEGRIPPEN-lijsten van tools/gen_aardrijkskunde_h1_{4,5}.py (bron: boek p. 38-49, begrippenlijst p. 52).
Begrippen die officieel bij §1.1/§1.3 horen (al in begrippentoetsen 67-71) zijn weggelaten.
⚠️ Zodra Duru de toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_aardrijkskunde_h1_4 import BEGRIPPEN as B4, plaats, langste_aandeel, schrijf
from gen_aardrijkskunde_h1_5 import BEGRIPPEN as B5

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'aardrijkskunde', 'js', 'data')
NIET = {"handelsbelemmering", "vrijhandel", "multipolaire wereldeconomie", "gini-coëfficiënt"}  # §1.1 / §1.3
PARAGRAFEN = [("1.4", "Rol van Europa in de wereldhandel", [b for b in B4 if b[0].lower() not in NIET]),
              ("1.5", "Rol van Nederland in de wereldhandel", [b for b in B5 if b[0].lower() not in NIET])]
ALLE = [(p, t, d) for p, _, lijst in PARAGRAFEN for t, d in lijst]


def O(vraag, sleutels, min_, model, uitleg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg}


# Twee open vragen, met de hand: twee begrippen naast elkaar zetten.
OPEN = [
    O("Wat is het verschil tussen een <b>mainport</b> en een <b>brainport</b>? Noem van elk een Nederlands voorbeeld.",
      ["haven/luchthaven", "rotterdam/schiphol", "kennis/hightech/universiteit", "eindhoven"], 3,
      "Een mainport is een belangrijke haven of luchthaven voor de internationale handel, zoals de haven van Rotterdam of Schiphol. "
      "Een brainport is een gebied met veel kennis: hightechbedrijven, universiteiten en onderzoeksinstituten, zoals de regio Eindhoven.",
      "Mainport = haven/luchthaven voor wereldhandel (Rotterdam, Schiphol); brainport = kenniseconomie met hightechbedrijven (Eindhoven). (boek p. 42, 52)"),
    O("Wat is het verschil tussen een <b>lidstaat</b> en een <b>kandidaat-lidstaat</b> van de EU? Noem ook drie dingen waar zo'n land eerst aan moet voldoen.",
      ["wil/willen/nog niet", "financiën/financien/geld", "corruptie", "democratie"], 3,
      "Een lidstaat is al lid van de EU. Een kandidaat-lidstaat wil lid worden maar is het nog niet. "
      "Daarvoor moet het land eerst voldoen aan strenge regels op het gebied van financiën, corruptie en democratie.",
      "Kandidaat-lidstaten moeten voldoen aan strenge regels op het gebied van financiën, corruptie en democratie. (boek p. 38)"),
]
PAGINA = {"1.4": "38–41", "1.5": "42–49"}


def stam(term):
    w = re.sub(r"^(de|het|een) ", "", term.lower())
    return w[:6] if len(w) > 6 else w


def zonder_term(term, tekst):
    return stam(term) not in tekst.lower()


def bron(p):
    return f"(boek p. {PAGINA[p]})"


def mc_vraag(p, term, defin, pool, rng):
    fout = rng.sample([t for t, _ in pool if t != term], 3)
    return {"type": "mc", "vraag": f"Welk begrip hoort bij deze omschrijving?<br><i>{defin}</i>",
            "_goed": term, "_fout": fout, "uitleg": f"{term}: {defin} {bron(p)}"}


def wo_vraag(p, term, defin, ander_def, waar):
    if waar:
        return {"type": "waaronwaar", "vraag": f"<b>{term}</b> — {defin}", "antwoord": True,
                "uitleg": f"Waar. {term}: {defin} {bron(p)}"}
    return {"type": "waaronwaar", "vraag": f"<b>{term}</b> — {ander_def}", "antwoord": False,
            "uitleg": f"Niet waar. Dat is de omschrijving van een ander begrip. {term}: {defin} {bron(p)}"}


def varianten(term):
    t = re.sub(r"^(de|het|een) ", "", term.lower())
    alts = []
    for v in (t, t.replace("-", " "), t.replace("-", ""), t.replace(" ", "")):
        if v and v not in alts:
            alts.append(v)
    return "|".join(alts)


def vul_vraag(p, term, defin, typ):
    return {"type": typ, "vraag": f"{defin}<br>Hoe heet dit begrip? ____", "antwoord": varianten(term),
            "uitleg": f"{term}: {defin} {bron(p)}"}


def theorie():
    h = ["<h3>Begrippenlijst §1.4 en §1.5 — Europa en Nederland in de wereldhandel</h3>",
         "<p>Alle begrippen uit <b>§1.4</b> en <b>§1.5</b> op een rij. Ken ze zo dat je ze kunt <i>uitleggen</i> en "
         "herkent in een vraag. Dek de rechterkolom af en zeg de betekenis hardop.</p>"]
    for p, titel, lijst in PARAGRAFEN:
        h.append(f'<h4>§{p} {titel}</h4>\n<table>\n<tr><th>Begrip</th><th>Betekenis</th></tr>')
        h += [f"<tr><td><b>{t}</b></td><td>{d}</td></tr>" for t, d in lijst]
        h.append("</table>")
    h.append('<div class="info-box tip"><span class="kop">Tip</span> De begrippen <b>afzetmarkt</b>, <b>brainport</b> en '
             '<b>globaliseringsindex</b> staan in de officiële begrippenlijst van het boek (p. 52): die moet je zeker kennen. '
             'Begrippen als vrijhandel en handelsbelemmering horen bij §1.1 — die oefen je bij de begrippentoetsen van §1.1–§1.3.</div>')
    return "\n".join(h)


def main():
    rng = random.Random('ak_h1_45_begrippen')
    pool_van = {p: lijst for p, _, lijst in PARAGRAFEN}
    open_tekst = re.sub(r"<[^>]+>", "", " ".join(v["vraag"].lower() for v in OPEN))
    in_open = {t.lower() for _, t, _ in ALLE if t.lower() in open_tekst}

    # begrippentoets: 10 mc, 5 waaronwaar (2 onwaar), 3 invul, 2 open; elk begrip één keer
    termen = [x for x in ALLE if x[1].lower() not in in_open]
    rng.shuffle(termen)
    it = iter(termen)
    type_van = {}

    def volgende(filter_=lambda t, d: True):
        for p, t, d in it:
            if filter_(t, d):
                return p, t, d
        raise SystemExit("te weinig begrippen")

    ev = []
    for _ in range(10):
        p, t, d = volgende()
        ev.append(mc_vraag(p, t, d, pool_van[p], rng)); type_van[t] = "mc"
    for i in range(5):
        p, t, d = volgende()
        ander = rng.choice([y for x, y in pool_van[p] if x != t])
        ev.append(wo_vraag(p, t, d, ander, waar=i % 2 == 1)); type_van[t] = "waaronwaar"
    for _ in range(3):
        p, t, d = volgende(zonder_term)
        ev.append(vul_vraag(p, t, d, "invul")); type_van[t] = "invul"
    ev += [dict(v) for v in OPEN]
    ev = plaats(ev, rng)
    assert len(ev) == 20
    n, tot = langste_aandeel(ev)
    assert n / tot <= 0.4, f"juiste optie {n}/{tot} keer langste"

    # onderwerp: 6 mc, 4 waaronwaar (2 onwaar), 2 invoer — een begrip niet in hetzelfde vraagtype als in de toets
    rest = ALLE[:]
    rng.shuffle(rest)
    gehad = set()

    def kies(typ, filter_=lambda t, d: True):
        for p, t, d in rest:
            if t not in gehad and type_van.get(t) != typ and filter_(t, d):
                gehad.add(t)
                return p, t, d
        raise SystemExit("te weinig begrippen (onderwerp)")

    ov = []
    for _ in range(6):
        p, t, d = kies("mc")
        ov.append(dict(mc_vraag(p, t, d, pool_van[p], rng), niveau=1))
    for i in range(4):
        p, t, d = kies("waaronwaar")
        ander = rng.choice([y for x, y in pool_van[p] if x != t])
        ov.append(wo_vraag(p, t, d, ander, waar=i % 2 == 0))
    for _ in range(2):
        p, t, d = kies("invul", zonder_term)
        ov.append(dict(vul_vraag(p, t, d, "invoer"), niveau=1))
    ov = plaats(ov, rng)

    onderwerp = {"id": "ak-h1-45-begrippen", "hoofdstuk": 1, "paragraaf": "1.4–1.5",
                 "titel": "Begrippen §1.4 en §1.5 — Europa en Nederland",
                 "korteUitleg": "Alle begrippen uit §1.4 en §1.5 met hun betekenis.",
                 "icoon": "📖", "kleur": "h1-thema", "theorie": theorie(), "vragen": ov}
    schrijf(os.path.join(ROOT, 'h1_45_begrippen.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 · begrippen §1.4–§1.5) — gegenereerd door tools/gen_aardrijkskunde_h1_45_begrippen.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    ex = {"id": "ex-h3-ak-97", "hoofdstuk": 1, "paragraaf": "begrippen",
          "hoofdstukTitel": "Hoofdstuk 1 — Wereldhandel in beweging",
          "titel": "Proeftoets 97 — Begrippentoets §1.4 en §1.5", "vak": "Aardrijkskunde · HAVO 3 (H1)",
          "icoon": "📖", "duurMin": 20, "vragen": ev}
    schrijf(os.path.join(ROOT, 'examen_97.js'),
            "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Aardrijkskunde H1 · begrippentoets §1.4–§1.5) — gegenereerd door tools/gen_aardrijkskunde_h1_45_begrippen.py */\n",
            "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
    print(f"{len(ALLE)} begrippen; onderwerp {len(ov)} vragen; examen_97: 20 vragen, langste {n}/{tot}")


if __name__ == '__main__':
    main()
