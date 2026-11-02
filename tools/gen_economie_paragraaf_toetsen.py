#!/usr/bin/env python3
"""Economie HAVO 3 (Pincode) · Paragraaf proeftoetsen 78–95 en begrippen §4.1/§4.2.
Onderdeel van TASK-34 (Opus -> agy, 2026-11-01).

- Examen 78 (§2.3): Proeftoets 78: Wat is inflatie en hoe meet het CBS dat?
- Examen 79 (§2.3): Proeftoets 79: Kosteninflatie of bestedingsinflatie herkennen
- Examen 80 (§2.3): Proeftoets 80: Redeneren met prijzen, inkomen en koopkracht
- Examen 81 (§2.3): Proeftoets 81: Koopkrachtplaatjes en verschillen tussen groepen
- Examen 82 (§2.3): Proeftoets 82: Rekenen met nominaal en reëel inkomen
- Examen 83 (§2.3): Proeftoets 83: Tabellen en grafieken over inflatie en koopkracht
- Examen 84 (§4.1): Proeftoets 84: Produceren, consumeren en de kringloop
- Examen 85 (§4.1): Proeftoets 85: Bedrijfskolom en toegevoegde waarde berekenen
- Examen 86 (§4.1): Proeftoets 86: De vier productiefactoren toepassen
- Examen 87 (§4.1): Proeftoets 87: Productieonderneming, handelsonderneming of dienstverlener
- Examen 88 (§4.1): Proeftoets 88: Mechanisatie, automatisering en robotisering
- Examen 89 (§4.1): Proeftoets 89: Arbeidsproductiviteit berekenen
- Examen 90 (§4.2): Proeftoets 90: Inkoopwaarde van de omzet of bedrijfskosten
- Examen 91 (§4.2): Proeftoets 91: Constante of variabele kosten herkennen
- Examen 92 (§4.2): Proeftoets 92: Rekenen met constante en variabele kosten
- Examen 93 (§4.2): Proeftoets 93: Soorten bedrijfskosten (loon, huisvesting, verkoop, rente)
- Examen 94 (§4.2): Proeftoets 94: Kapitaalgoederen, afschrijven en restwaarde
- Examen 95 (§4.2): Proeftoets 95: Afschrijvingskosten berekenen

Schrijft:
- havo3/economie/js/data/examen_78..95.js (ex-h3-economie-78..95)
- havo3/economie/js/data/h4_1_begrippen.js (h4-1-begrippen)
- havo3/economie/js/data/h4_2_begrippen.js (h4-2-begrippen)
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gen_economie_data_2_3 import EXAMENS_2_3
from gen_economie_data_4_1 import EXAMENS_4_1
from gen_economie_data_4_2 import EXAMENS_4_2
from gen_economie_data_begrippen import H4_1_THEORIE, H4_2_THEORIE, H4_1_VRAGEN, H4_2_VRAGEN

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'economie', 'js', 'data')


def plaats(vragen, rng):
    """Schud mc-opties tot: <=40% op een index, geen periode 2-4, <60% '+1'-stappen."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(5000):
        pos = [rng.randrange(len(v["_fout"]) + 1) for v in mcs]
        if max(pos.count(i) for i in set(pos)) / len(pos) > 0.4:
            continue
        if len(pos) < 6:
            break
        if any(all(a == pos[i - p] for i, a in enumerate(pos) if i >= p) for p in (2, 3, 4)):
            continue
        n = max(len(v["_fout"]) + 1 for v in mcs)
        if sum(pos[i + 1] == (pos[i] + 1) % n for i in range(len(pos) - 1)) / (len(pos) - 1) >= 0.6:
            continue
        break
    else:
        raise SystemExit("geen geldige volgorde gevonden")
    for v, p in zip(mcs, pos):
        opties = list(v["_fout"])
        rng.shuffle(opties)
        opties.insert(p, v["_goed"])
        v["opties"], v["antwoord"] = opties, p
        del v["_goed"]
        del v["_fout"]
    return vragen


def langste_aandeel(vragen):
    mcs = [v for v in vragen if v["type"] == "mc"]
    n = sum(all(len(o) < len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
    return n, len(mcs)


def schrijf_begrippen():
    """Schrijft h4_1_begrippen.js en h4_2_begrippen.js."""
    rng = random.Random('begrippen_4_seed_99')

    begrippen = [
        ("h4_1_begrippen.js", {
            "id": "h4-1-begrippen",
            "hoofdstuk": 4,
            "paragraaf": "4.1",
            "titel": "Begrippen §4.1 Productie",
            "korteUitleg": "Alle begrippen van §4.1: produceren, consumeren, zelfvoorziening, kringloop, bedrijfskolom, toegevoegde waarde, productiefactoren en arbeidsproductiviteit.",
            "icoon": "🔑",
            "kleur": "roze",
            "theorie": H4_1_THEORIE,
            "vragen": [dict(v) for v in H4_1_VRAGEN]
        }),
        ("h4_2_begrippen.js", {
            "id": "h4-2-begrippen",
            "hoofdstuk": 4,
            "paragraaf": "4.2",
            "titel": "Begrippen §4.2 Kosten",
            "korteUitleg": "Alle begrippen van §4.2: inkoopwaarde van de omzet, bedrijfskosten, constante en variabele kosten, soorten kosten en afschrijven.",
            "icoon": "🔑",
            "kleur": "roze",
            "theorie": H4_2_THEORIE,
            "vragen": [dict(v) for v in H4_2_VRAGEN]
        })
    ]

    for fname, data in begrippen:
        assert len(data["theorie"]) >= 1500, f"{fname} theorie te kort ({len(data['theorie'])} < 1500)"
        assert len(data["vragen"]) == 8, f"{fname} moet exact 8 vragen hebben"
        for q in data["vragen"]:
            assert q["type"] in ("mc", "waaronwaar"), f"{fname} mag alleen mc of waaronwaar bevatten (geen open/invul)"
        pad = os.path.join(ROOT, fname)
        kop = f"/* =========================================================\n" \
              f"   Duru's Economie (HAVO 3) — Onderwerp {data['paragraaf']}: {data['titel']}\n" \
              f"   ========================================================= */\n"
        inhoud = kop + f"DURU.register(" + json.dumps(data, ensure_ascii=False, indent=2) + ");\n"
        with open(pad, 'w', encoding='utf-8') as f:
            f.write(inhoud)
        print(f"Aangemaakt: {fname} (theorie {len(data['theorie'])} tekens, {len(data['vragen'])} vragen)")


def main():
    rng = random.Random('economie_paragraaf_seed_7895')
    examens = {}
    examens.update(EXAMENS_2_3)
    examens.update(EXAMENS_4_1)
    examens.update(EXAMENS_4_2)

    assert len(examens) == 18, f"Verwacht 18 examens (78 t/m 95), gevonden: {len(examens)}"

    for nr in sorted(examens):
        hfd, par, titel, icoon, vr = examens[nr]
        assert len(vr) == 20, f"examen_{nr} heeft {len(vr)} vragen i.p.v. 20"
        t = [v["type"] for v in vr]
        mc_c, wow_c, inv_c, op_c = t.count("mc"), t.count("waaronwaar"), t.count("invul"), t.count("open")
        assert (mc_c, wow_c, inv_c, op_c) == (10, 5, 3, 2), f"examen_{nr} type mismatch: {mc_c, wow_c, inv_c, op_c}"
        onwaar_c = sum(1 for v in vr if v["type"] == "waaronwaar" and v["antwoord"] is False)
        assert onwaar_c >= 2, f"examen_{nr} heeft te weinig onwaar ({onwaar_c}/5)"

        vr_geplaatst = plaats([dict(v) for v in vr], rng)
        n_lang, tot_mc = langste_aandeel(vr_geplaatst)
        print(f"examen_{nr} (§{par}): {len(vr_geplaatst)} vragen, juiste optie langste {n_lang}/{tot_mc}")
        assert n_lang / tot_mc <= 0.4, f"examen_{nr}: juiste optie {n_lang}/{tot_mc} keer langste"

        ex = {
            "id": f"ex-h3-economie-{nr}",
            "hoofdstuk": hfd,
            "paragraaf": par,
            "titel": titel,
            "vak": "Economie · HAVO 3 (Pincode)",
            "icoon": icoon,
            "duurMin": 20,
            "vragen": vr_geplaatst
        }
        pad = os.path.join(ROOT, f"examen_{nr}.js")
        kop = f"/* =========================================================\n" \
              f"   Duru's Economie (HAVO 3) — {titel}\n" \
              f"   ========================================================= */\n"
        inhoud = kop + f"DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n"
        with open(pad, 'w', encoding='utf-8') as f:
            f.write(inhoud)

    schrijf_begrippen()
    print("Alle 18 examens (78-95) en 2 begrippen-onderwerpen succesvol gegenereerd!")


if __name__ == '__main__':
    main()
