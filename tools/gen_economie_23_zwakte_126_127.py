#!/usr/bin/env python3
"""Economie HAVO 3 (Pincode) · §2.3 Koopkracht — 2 zwakte-toetsen 126–127 (Opus, 2026-11-12).

116–125 zijn gemaakt. Het zwakst was examen_122: lonen én prijzen dalen (−1 − (−4) → 5 ingevuld),
"60% van de inflatie" (→ −50) en de formule omdraaien (nominaal = reëel + inflatie). Ook richting
van de koopkracht (examen_123) en "lagere inflatie ≠ goedkoper" / bestedingsinflatie (examen_125).
Andere aanpak: kleinere stappen (eerst alleen de som, dan het rekenen met min-min).

- 126: Min min wordt plus — stap voor stap
- 127: De formule omdraaien en de richting van de koopkracht
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_economie_toetsen_96_115 import M, W, I, O, plaats, langste_aandeel, kortste_aandeel  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'economie', 'js', 'data')

EXAMENS = {
126: (2, "2.3", "Proeftoets 126: Min min wordt plus — stap voor stap", "➖", [
    M("Een bakkerij verlaagt de lonen met 2%; in de winkels dalen de prijzen met 5%. Welke som hoort bij het reëel inkomen?",
      "−2 − (−5)",
      ["−5 − (−2)", "2 − 5", "−2 − 5"],
      "Reëel = nominaal − inflatie. Nominaal is −2, inflatie is −5. Dus −2 − (−5), en dat is −2 + 5 = +3."),
    M("Reken uit zonder rekenmachine: 3 − (−4) = ?",
      "7",
      ["−1", "−7", "1"],
      "Min een min is plus: 3 − (−4) = 3 + 4 = 7."),
    M("Hoeveel komt eruit bij −6 min min 2, dus −6 − (−2)?",
      "−4",
      ["−8", "4", "8"],
      "−6 − (−2) = −6 + 2 = −4."),
    M("Wat is de uitkomst als je −1 aftrekt van −1?",
      "0",
      ["−2", "2", "1"],
      "−1 − (−1) = −1 + 1 = 0."),
    M("Op het eiland Kaap verdienen de vissers 5% minder, en de prijzen in de haven zakken met 8%. Kunnen de vissers meer of minder kopen?",
      "Meer: −5 − (−8) = +3%",
      ["Minder: −5 − 8 = −13%", "Minder: −8 − (−5) = −3%", "Evenveel, want lonen en prijzen dalen allebei"],
      "Reëel = −5 − (−8) = −5 + 8 = +3%. De prijzen dalen harder dan hun loon."),
    M("Het loon van Noor bij de ijssalon zakt 6%, de prijzen zakken 1%. Wat gebeurt er met haar koopkracht?",
      "−5%",
      ["+5%", "−7%", "+7%"],
      "−6 − (−1) = −6 + 1 = −5%. Haar loon daalt harder dan de prijzen."),
    M("De prijzen stijgen 10%. Het loon stijgt met de helft daarvan. Met hoeveel procent stijgt het loon?",
      "Met 5%",
      ["Met 50%", "Met 60%", "Met −40%"],
      "De helft (50%) van 10% is 0,5 × 10% = 5%."),
    M("Werknemers krijgen 75% van de inflatie van 8% erbij als loon. Hoeveel is hun loonstijging?",
      "6%, want 0,75 × 8%",
      ["75%, want dat staat in de cao", "83%, want 75 + 8", "−67%, want 8 − 75"],
      "75% van 8% = 0,75 × 8% = 6%."),
    M("Die werknemers krijgen dus 6% meer loon bij 8% inflatie. Hoe verandert hun koopkracht?",
      "−2%",
      ["+2%", "+14%", "−14%"],
      "Loonstijging 6% min inflatie 8% = −2%. Ze kunnen dus 2% minder kopen."),
    M("Wat betekent '60% van het inflatiepercentage' bij een inflatie van 10%?",
      "0,6 × 10% = 6%",
      ["10% − 60% = −50%", "60% − 10% = 50%", "10% + 60% = 70%"],
      "'60% van' betekent keer 0,6. Je trekt niets af. 0,6 × 10% = 6% loonstijging."),
    M("Je hebt de som −2% − (−7%) opgeschreven. Wat is de verandering van het reëel inkomen?",
      "+5%",
      ["−9%", "−5%", "+9%"],
      "−2 − (−7) = −2 + 7 = +5%."),
    W("−3 − (−3) = 0", True,
      "Waar. −3 + 3 = 0. Lonen en prijzen dalen evenveel: de koopkracht blijft gelijk."),
    W("Als de lonen 1% dalen en de prijzen 4% dalen, stijgt de koopkracht met 5%.", False,
      "Niet waar. −1 − (−4) = −1 + 4 = +3%, niet 5%."),
    W("Bij 40% van een inflatie van 5% stijgt het loon met 2%.", True,
      "Waar. 0,4 × 5% = 2%."),
    W("Als het loon minder hard daalt dan de prijzen, gaat de koopkracht omhoog.", True,
      "Waar. Bijvoorbeeld −1 − (−3) = +2%."),
    I("Bij de busmaatschappij gaan de lonen 3% omlaag. In dezelfde periode worden de boodschappen 7% goedkoper. Het reëel inkomen van de chauffeurs verandert met ____ %.",
      "4|+4|4,0",
      "−3 − (−7) = −3 + 7 = +4%."),
    I("De inflatie is 4%. Het loon stijgt met 50% van de inflatie. De koopkracht verandert met ____ %.",
      "-2|−2|-2,0",
      "50% van 4% = 2% loonstijging. 2% − 4% = −2%."),
    I("Reken uit: −5 − (−2) = ____",
      "-3|−3",
      "−5 − (−2) = −5 + 2 = −3. Min een min wordt plus."),
    O("Jamal zegt: 'Lonen −2%, prijzen −6%. Ik reken −2 − 6 = −8%, dus ik ga erop achteruit.' Wat doet hij fout?",
      ["plus/vooruit/min een min/min min/haakjes/+4/4%"], 1,
      "Hij moet −2 − (−6) doen; min een min is plus, dus −2 + 6 = +4%: hij gaat erop vooruit.",
      "−2 − (−6) = +4%. Jamal vergeet dat je de −6 aftrekt, en min een min is plus."),
    O("Leg in je eigen woorden uit wanneer je koopkracht stijgt terwijl je loon daalt.",
      ["prijzen/prijs", "harder/meer/sneller/sterker"], 2,
      "Als de prijzen harder dalen dan je loon.",
      "Bijvoorbeeld loon −2%, prijzen −5%: −2 − (−5) = +3%."),
]),

127: (2, "2.3", "Proeftoets 127: De formule omdraaien en de richting van de koopkracht", "🔀", [
    M("Je kent de formule reëel = nominaal − inflatie. Welke schrijfwijze klopt als je juist het nominaal inkomen zoekt?",
      "nominaal = reëel + inflatie",
      ["nominaal = reëel − inflatie", "nominaal = inflatie − reëel", "nominaal = reëel × inflatie"],
      "Je zet de inflatie aan de andere kant: dan wordt min plus."),
    M("Je weet de verandering van het nominaal en van het reëel inkomen. Hoe vind je de inflatie?",
      "inflatie = nominaal − reëel",
      ["inflatie = reëel − nominaal", "inflatie = nominaal + reëel", "inflatie = reëel × nominaal"],
      "Uit reëel = nominaal − inflatie volgt: inflatie = nominaal − reëel."),
    M("Het reëel inkomen van Merel stijgt 2%. De inflatie is 3%. Hoe veranderde haar nominaal inkomen?",
      "+5%",
      ["+1%", "−1%", "+6%"],
      "Nominaal = reëel + inflatie = 2% + 3% = 5%. Controle: 5% − 3% = 2%."),
    M("Kevin gaat er reëel 1% op achteruit (−1%). De inflatie is 4%. Hoe veranderde zijn nominaal inkomen?",
      "+3%",
      ["+5%", "−5%", "−3%"],
      "Nominaal = −1% + 4% = +3%. Controle: 3% − 4% = −1%."),
    M("Bij een schoonmaker stijgt het loon 7% en zijn koopkracht 3%. Hoe hoog was de inflatie?",
      "4%",
      ["10%", "−4%", "3%"],
      "Inflatie = nominaal − reëel = 7% − 3% = 4%."),
    M("Een kassamedewerker kreeg 1% loonsverhoging, maar haar reëel inkomen ging 2% omlaag. Hoe hoog was de inflatie?",
      "3%",
      ["−1%", "−3%", "1%"],
      "Inflatie = 1 − (−2) = 1 + 2 = 3%. Controle: 1% − 3% = −2%."),
    M("Lieke gaat minder uren werken en verdient daardoor minder. De winkelprijzen veranderen niet. Wat gebeurt er met wat ze kan kopen?",
      "Ze kan minder kopen",
      ["Ze kan meer kopen", "Ze kan evenveel kopen, want de prijzen blijven gelijk",
       "Dat hangt alleen af van de inflatie in het buitenland"],
      "Minder inkomen bij dezelfde prijzen = minder koopkracht."),
    M("Bij welke situatie blijft de koopkracht precies gelijk?",
      "Loon +3%, prijzen +3%",
      ["Loon +3%, prijzen 0%", "Loon 0%, prijzen +3%", "Loon +3%, prijzen −3%"],
      "3% − 3% = 0%. De andere geven +3%, −3% en +6%."),
    M("Het zakgeld van Fleur gaat van € 20 naar € 25. Met hoeveel procent stijgt het?",
      "25%",
      ["20%", "5%", "125%"],
      "5 / 20 × 100% = 25%. Je deelt door het oude bedrag (€ 20), niet door het nieuwe."),
    M("In 2024 was de inflatie lager dan in 2023. Wat betekent dat voor de prijzen in 2024?",
      "Ze stegen nog, maar minder snel",
      ["Ze daalden ten opzichte van 2023", "Ze bleven precies gelijk", "Ze stegen sneller dan in 2023"],
      "Een lagere inflatie is nog steeds een prijsstijging, alleen een kleinere."),
    M("Een speelgoedwinkel krijgt veel meer klanten, maar de fabriek maakt zonder moeite extra speelgoed. Wat geldt?",
      "Er ontstaat geen bestedingsinflatie, want het aanbod groeit mee",
      ["De prijzen stijgen zeker, want meer vraag geeft altijd inflatie",
       "Er ontstaat kosteninflatie door de extra klanten in de winkel",
       "De prijzen dalen altijd vanzelf als er meer klanten komen"],
      "Bestedingsinflatie ontstaat pas als bedrijven niet voldoende kunnen produceren voor de extra vraag."),
    W("Wie er reëel 2% op vooruitgaat bij 2% prijsstijging, kreeg in totaal 4% meer loon.", True,
      "Waar. Nominaal = 2% + 2% = 4%."),
    W("Om de inflatie te vinden, trek je het nominale van het reële inkomen af.", False,
      "Niet waar. Het is andersom: inflatie = nominaal − reëel."),
    W("Als je inkomen daalt en de prijzen gelijk blijven, daalt je koopkracht.", True,
      "Waar. Je hebt minder geld voor dezelfde prijzen."),
    W("Als de inflatie zakt van 6% naar 2%, worden de producten goedkoper.", False,
      "Niet waar. De prijzen stijgen dan nog 2%, alleen minder hard dan eerst."),
    I("Reëel +1,5% en inflatie 2,5%. Het nominaal inkomen veranderde met ____ %.",
      "4|+4|4,0",
      "1,5% + 2,5% = 4%."),
    I("Nominaal +2% en reëel −3%. De inflatie was ____ %.",
      "5|5,0",
      "2 − (−3) = 2 + 3 = 5%."),
    I("Opa's pensioen stijgt van € 1.500 naar € 1.545 per maand. Dat is een stijging van ____ %.",
      "3|+3|3,0",
      "45 / 1.500 × 100% = 3%."),
    O("Hoe bereken je de inflatie als je weet hoeveel het nominaal en het reëel inkomen veranderen?",
      ["aftrekken/afhalen/eraf/verschil/minus"], 1,
      "Je trekt de verandering van het reëel inkomen af van die van het nominaal inkomen; je neemt het verschil.",
      "Inflatie = nominaal − reëel."),
    O("Waarom ontstaat er geen bestedingsinflatie als bedrijven makkelijk extra kunnen maken?",
      ["genoeg/voldoende/aanbod/tekort"], 1,
      "Omdat er dan genoeg aanbod is voor de extra vraag; er is geen tekort, dus prijzen hoeven niet te stijgen.",
      "Bestedingsinflatie = te veel vraag die bedrijven niet kunnen bijhouden."),
]),
}

def main():
    rng = random.Random("economie_23_zwakte_126_127")
    for nr in sorted(EXAMENS):
        hfd, par, titel, icoon, vr = EXAMENS[nr]
        assert len(vr) == 20, f"examen_{nr}: {len(vr)} vragen"
        t = [v["type"] for v in vr]
        vr = plaats([dict(v) for v in vr], rng)
        n_lang, tot = langste_aandeel(vr)
        n_kort, _ = kortste_aandeel(vr)
        print(f"examen_{nr}: {len(vr)} vragen, {t.count('mc')} mc / {t.count('waaronwaar')} w-o / "
              f"{t.count('invul')} invul / {t.count('open')} open · langste {n_lang}/{tot}, kortste {n_kort}/{tot}")
        assert n_lang / tot <= 0.4 and n_kort / tot <= 0.4, f"examen_{nr}: juiste optie te vaak langste/kortste"
        ex = {"id": f"ex-h3-economie-{nr}", "hoofdstuk": hfd, "paragraaf": par, "titel": titel,
              "vak": "Economie · HAVO 3 (Pincode)", "icoon": icoon, "duurMin": 20, "vragen": vr}
        kop = f"/* =========================================================\n   Duru's Economie (HAVO 3) — {titel}\n   ========================================================= */\n"
        with open(os.path.join(ROOT, f"examen_{nr}.js"), "w", encoding="utf-8") as f:
            f.write(kop + "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")


if __name__ == "__main__":
    main()
