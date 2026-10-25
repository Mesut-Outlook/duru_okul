#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_natuurkunde_h1_toetsen_61_65.py
Generates 5 new comprehensive tests for Natuurkunde HAVO 3 Hoofdstuk 1:
- examen_61.js: Toets 61 — §1.4 Veiligheid, Remweg & Stopafstand — Toets A (20 vragen)
- examen_62.js: Toets 62 — §1.4 Veiligheid, Remweg & Stopafstand — Toets B (20 vragen)
- examen_63.js: Toets 63 — §1.5 Arbeid en Energieomzetting — Toets A (20 vragen)
- examen_64.js: Toets 64 — §1.5 Arbeid en Energieomzetting — Toets B (20 vragen)
- examen_65.js: Toets 65 — Integrale Examentraining Hoofdstuk 1 (Mix §1.1 t/m §1.5) (20 vragen)
"""

import os
import json
import re

DATA_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/natuurkunde/js/data"
os.makedirs(DATA_DIR, exist_ok=True)

def apply_mc_pattern(vragen, pattern):
    mc_questions = [v for v in vragen if v["type"] == "mc"]
    assert len(mc_questions) == len(pattern), f"MC questions {len(mc_questions)} != pattern {len(pattern)}"
    for q, target_idx in zip(mc_questions, pattern):
        curr_idx = q["antwoord"]
        if curr_idx != target_idx:
            correct_val = q["opties"][curr_idx]
            other_opts = [opt for i, opt in enumerate(q["opties"]) if i != curr_idx]
            other_opts.insert(target_idx, correct_val)
            q["opties"] = other_opts
            q["antwoord"] = target_idx

# Helper function to validate and write an exam
def validate_and_save_exam(exam_data, filename, mc_pattern=None):
    if mc_pattern:
        apply_mc_pattern(exam_data["vragen"], mc_pattern)
    vragen = exam_data["vragen"]

    assert len(vragen) == 20, f"{filename}: moet exact 20 vragen hebben, heeft {len(vragen)}"
    
    mc_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    ww_counts = {True: 0, False: 0}
    type_counts = {}
    longest_mc_count = 0
    
    for idx, v in enumerate(vragen):
        t = v["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
        assert "vraag" in v and v["vraag"], f"{filename} vraag {idx+1}: geen vraag tekst"
        assert not re.match(r'^\s*\d+\.\s', v["vraag"]), f"{filename} vraag {idx+1}: vraag start met nummer"
        assert "uitleg" in v and len(v["uitleg"].strip()) >= 15, f"{filename} vraag {idx+1}: uitleg te kort"
        
        # Check LaTeX
        latex_pat = r'\$[^$]*(?:\\[a-zA-Z]+|[_^]\{)[^$]*\$|\\(?:frac|text|cdot|times|Delta|approx)\b'
        assert not re.search(latex_pat, v["vraag"]), f"{filename} vraag {idx+1}: LaTeX in vraag"
        assert not re.search(latex_pat, v["uitleg"]), f"{filename} vraag {idx+1}: LaTeX in uitleg"
        
        if t == "mc":
            assert len(v["opties"]) == 4, f"{filename} vraag {idx+1}: mc moet 4 opties hebben"
            ans = v["antwoord"]
            assert ans in [0, 1, 2, 3], f"{filename} vraag {idx+1}: ongeldig mc antwoord {ans}"
            mc_counts[ans] += 1
            
            # Check duplicate options
            clean_opts = [re.sub(r'<[^>]+>', '', str(opt)).lower().strip() for opt in v["opties"]]
            assert len(set(clean_opts)) == 4, f"{filename} vraag {idx+1}: dubbele opties {v['opties']}"
            
            # Check longest option
            opt_lens = [len(opt) for opt in v["opties"]]
            max_len = max(opt_lens)
            if opt_lens[ans] == max_len and opt_lens.count(max_len) == 1:
                longest_mc_count += 1
                
        elif t == "waaronwaar":
            ans = v["antwoord"]
            assert isinstance(ans, bool), f"{filename} vraag {idx+1}: waaronwaar moet boolean zijn"
            ww_counts[ans] += 1
            u = v["uitleg"].strip().lower()
            if ans is True:
                assert not u.startswith(("onwaar", "niet waar", "fout", "incorrect")), f"{filename} vraag {idx+1}: antwoord is True maar uitleg zegt onwaar"
                assert u.startswith(("waar", "juist", "correct")), f"{filename} vraag {idx+1}: uitleg moet beginnen met Waar"
            else:
                assert not u.startswith(("waar", "juist", "correct")) or u.startswith(("waarom", "waarde")), f"{filename} vraag {idx+1}: antwoord is False maar uitleg zegt waar"
                assert u.startswith(("onwaar", "niet waar", "fout")), f"{filename} vraag {idx+1}: uitleg moet beginnen met Onwaar / Niet waar"
                
        elif t == "invul":
            assert "antwoord" in v and len(str(v["antwoord"]).strip()) > 0, f"{filename} vraag {idx+1}: invul antwoord ontbreekt"
            # Ensure answer is not leaked in brackets
            assert not re.search(r'\[[^\]]+\]', v["vraag"]), f"{filename} vraag {idx+1}: brackets [..] in vraag"
            
        elif t == "open":
            assert "sleutelwoorden" in v and len(v["sleutelwoorden"]) >= 1, f"{filename} vraag {idx+1}: open mist sleutelwoorden"
            assert "minTreffers" in v and v["minTreffers"] <= len(v["sleutelwoorden"]), f"{filename} vraag {idx+1}: minTreffers > sleutelwoorden"
            assert "modelantwoord" in v and len(v["modelantwoord"].strip()) >= 15, f"{filename} vraag {idx+1}: modelantwoord te kort"
            for sw in v["sleutelwoorden"]:
                for alt in sw.split("/"):
                    alt_clean = alt.strip().lower()
                    if len(alt_clean) > 4:
                        assert alt_clean not in v["vraag"].lower(), f"{filename} vraag {idx+1}: sleutelwoord '{alt_clean}' komt voor in de vraag!"
        else:
            raise ValueError(f"{filename}: ongeldig type {t}")

    assert type_counts.get("mc", 0) == 12, f"{filename}: moet 12 mc hebben, heeft {type_counts.get('mc')}"
    assert type_counts.get("waaronwaar", 0) == 4, f"{filename}: moet 4 waaronwaar hebben, heeft {type_counts.get('waaronwaar')}"
    assert type_counts.get("invul", 0) == 2, f"{filename}: moet 2 invul hebben, heeft {type_counts.get('invul')}"
    assert type_counts.get("open", 0) == 2, f"{filename}: moet 2 open hebben, heeft {type_counts.get('open')}"
    
    # Check MC balance (exactly 3 of each)
    for opt, cnt in mc_counts.items():
        assert cnt == 3, f"{filename}: mc antwoord {opt} komt {cnt} keer voor (moet exact 3 zijn)"
        
    # Check waaronwaar (exactly 2 False, 2 True)
    assert ww_counts[False] == 2, f"{filename}: waaronwaar moet 2 False hebben, heeft {ww_counts[False]}"
    assert ww_counts[True] == 2, f"{filename}: waaronwaar moet 2 True hebben, heeft {ww_counts[True]}"
    
    # Check longest option rule (<= 50% = max 6 out of 12)
    assert longest_mc_count <= 6, f"{filename}: correcte optie is te vaak de langste ({longest_mc_count}/12)"
    
    filepath = os.path.join(DATA_DIR, filename)
    content = f"""/* =========================================================
   Duru's Natuurkunde (HAVO 3) — {exam_data['titel']}
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({json.dumps(exam_data, ensure_ascii=False, indent=2)});
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Succesvol aangemaakt: {filename} (20 vragen: 12 MC balanced, 4 WOW, 2 Invul, 2 Open)")

# -------------------------------------------------------------
# TOETS 61: §1.4 Veiligheid, Remweg & Stopafstand — Toets A
# -------------------------------------------------------------
toets_61 = {
  "id": "ex-h3-natuurkunde-61",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Toets 61 — §1.4 Veiligheid, Remweg & Stopafstand — Toets A",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚗",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat wordt in de natuurkunde precies verstaan onder de <b>reactietijd</b> van een bestuurder?",
      "opties": [
        "De tijdsduur tussen het zien van het gevaar en het intrappen van het rempedaal",
        "De totale tijd die nodig is om een voertuig vanaf topsnelheid stil te zetten",
        "De tijd waarin de remmen van het voertuig maximale remkracht uitoefenen",
        "De tijd waarin het voertuig een eenparig vertraagde beweging uitvoert"
      ],
      "antwoord": 0,
      "uitleg": "De reactietijd is de tijd tussen het waarnemen van een onverwachte gebeurtenis en het daadwerkelijk beginnen met remmen."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met een snelheid van 72 km/h. Wat is deze snelheid uitgedrukt in meter per seconde (m/s)?",
      "opties": [
        "25 m/s",
        "20 m/s",
        "15 m/s",
        "7,2 m/s"
      ],
      "antwoord": 1,
      "uitleg": "Om te rekenen van km/h naar m/s deel je de snelheid door 3,6: 72 / 3,6 = 20 m/s."
    },
    {
      "type": "mc",
      "vraag": "Welke bewegingssoort voert een auto uit tijdens de <b>reactietijd</b> vóórdat de bestuurder remt?",
      "opties": [
        "Een eenparig versnelde beweging met constante versnelling",
        "Een eenparig vertraagde beweging doordat het gas wordt losgelaten",
        "Een eenparige beweging met constante snelheid",
        "Een willekeurige beweging met afnemende kinetische energie"
      ],
      "antwoord": 2,
      "uitleg": "Tijdens de reactietijd raakt de bestuurder de remmen nog niet aan, waardoor de auto met onverminderde, constante snelheid doorrijdt."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de <b>remweg</b> van een auto als de rijsnelheid verdubbelt (van v naar 2v)?",
      "opties": [
        "De remweg verdubbelt eveneens",
        "De remweg blijft exact gelijk",
        "De remweg wordt drie keer zo lang",
        "De remweg wordt vier keer zo lang"
      ],
      "antwoord": 3,
      "uitleg": "De remweg is evenredig met het kwadraat van de snelheid: (2)² = 4 keer zo lang."
    },
    {
      "type": "mc",
      "vraag": "Uit welke twee afstanden is de totale <b>stopafstand</b> van een auto opgebouwd?",
      "opties": [
        "De reactieafstand opgeteld bij de remweg",
        "De remweg verminderd met de kreukelzone-afstand",
        "De remweg vermenigvuldigd met de reactietijd",
        "De reactieafstand gedeeld door de remtijd"
      ],
      "antwoord": 0,
      "uitleg": "De stopafstand is de totale afstand vanaf het moment van zien tot volledige stilstand: s_stop = s_reactie + s_rem."
    },
    {
      "type": "mc",
      "vraag": "Welke factor heeft <b>geen enkele directe invloed</b> op de lengte van de remweg van een auto?",
      "opties": [
        "De toestand van het wegdek (droog asfalt of natte klinkers)",
        "Het vasthouden van een smartphone door de bestuurder",
        "De profieldiepte en spanning van de autobanden",
        "De massa van de auto inclusief bagage en passagiers"
      ],
      "antwoord": 1,
      "uitleg": "Afleiding door een telefoon vergroot de reactietijd en reactieafstand, maar verandert niets aan de technische remweg van het voertuig zelf."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste natuurkundige doel van een <b>kreukelzone</b> aan de voorzijde van een moderne auto?",
      "opties": [
        "De massa van de auto aanzienlijk vergroten tijdens een botsing",
        "De auto na de botsing sneller in tegengestelde richting terug laten veren",
        "De botstijd (Δt) verlengen waardoor de resulterende botskracht op de inzittenden afneemt",
        "De zwaartekracht op de auto ombuigen naar een voorwaartse stuwkracht"
      ],
      "antwoord": 2,
      "uitleg": "Door gecontroleerd te vervormen verlengt de kreukelzone de botstijd. Volgens F = m · Δv / Δt wordt de uitgeoefende kracht daardoor veel kleiner."
    },
    {
      "type": "mc",
      "vraag": "Een auto rijdt met 10 m/s en remt eenparig af tot stilstand in 4,0 seconden. Hoe groot is de gemiddelde snelheid tijdens het remmen?",
      "opties": [
        "10 m/s",
        "2,5 m/s",
        "0 m/s",
        "5,0 m/s"
      ],
      "antwoord": 3,
      "uitleg": "Bij een eenparig vertraagde beweging tot stilstand is de gemiddelde snelheid: v_gem = (v_begin + v_eind) / 2 = (10 + 0) / 2 = 5,0 m/s."
    },
    {
      "type": "mc",
      "vraag": "Een automobilist rijdt met 15 m/s. Zijn reactietijd bedraagt 0,80 seconde. Hoeveel meter legt hij af tijdens zijn reactietijd?",
      "opties": [
        "12 meter",
        "18,75 meter",
        "15 meter",
        "9,6 meter"
      ],
      "antwoord": 0,
      "uitleg": "De reactieafstand bereken je met s_reactie = v · t_r = 15 m/s · 0,80 s = 12 m."
    },
    {
      "type": "mc",
      "vraag": "Waarom mag de <b>veiligheidskooi</b> (het passagierscompartiment) van een auto juist <b>niet</b> vervormen of kreukelen?",
      "opties": [
        "Omdat de deuren anders niet meer met de autosleutel geopend kunnen worden",
        "Om de overlevingsruimte voor de inzittenden te behouden en beknelling te voorkomen",
        "Omdat een stijve kooi ervoor zorgt dat de airbags sneller kunnen leeglopen",
        "Om te voorkomen dat de autoruit beslaat door temperatuurverschillen"
      ],
      "antwoord": 1,
      "uitleg": "De veiligheidskooi moet extreem sterk en vormvast zijn zodat de inzittenden niet worden geplet en beschermd blijven tegen binnendringende onderdelen."
    },
    {
      "type": "mc",
      "vraag": "Een bromfietser rijdt met 36 km/h (10 m/s) en heeft een remweg van 6,0 meter. Wat wordt de remweg als hij zijn snelheid opvoert naar 72 km/h (20 m/s)?",
      "opties": [
        "12 meter",
        "18 meter",
        "24 meter",
        "36 meter"
      ],
      "antwoord": 2,
      "uitleg": "De snelheid verdubbelt (van 10 naar 20 m/s). De remweg schaalt kwadratisch: (2)² = 4 keer zo groot. Dus 6,0 m · 4 = 24 m."
    },
    {
      "type": "mc",
      "vraag": "Hoe helpt het elastisch meerekken van een veiligheidsgordel bij een frontale aanrijding?",
      "opties": [
        "Het zorgt ervoor dat de passagier direct naar de achterbank schuift",
        "Het vermindert het totale gewicht van de passagier tijdens de klap",
        "Het activeert automatisch het antiblokkeersysteem (ABS) van de wielen",
        "Het verlengt de afremweg van het lichaam waardoor de piekbelasting daalt"
      ],
      "antwoord": 3,
      "uitleg": "Doordat de gordel gecontroleerd een klein stukje meerekt, wordt de afremtijd van het lichaam verlengd en de piekkracht op de borstkas aanzienlijk verlaagd."
    },
    {
      "type": "waaronwaar",
      "vraag": "Op een nat of beijzeld wegdek is de remweg van een auto aanzienlijk langer doordat de maximale wrijvingskracht tussen banden en wegdek veel kleiner is.",
      "antwoord": True,
      "uitleg": "Waar: Gladheid vermindert de wrijving drastisch, waardoor de wielen minder remkracht kunnen leveren en de remweg fors toeneemt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer een bestuurder vermoeid is of alcohol heeft gedronken, wordt zijn remweg langer.",
      "antwoord": False,
      "uitleg": "Onwaar: Alcohol en vermoeidheid verlengen de reactietijd en reactieafstand, maar hebben geen invloed op de mechanische remweg van de auto."
    },
    {
      "type": "waaronwaar",
      "vraag": "De binnenkant van een fietshelm bevat een harde schuimlaag (EPS) die bij een val blijvend indeukt om de botstijd van het hoofd te verlengen.",
      "antwoord": True,
      "uitleg": "Waar: Het samendrukken van het schuim absorbeert energie en verlengt de vertragingstijd, waardoor gevaarlijke piekversnellingen van de hersenen worden voorkomen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een auto een noodstop maakt met constante vertraging, is de remtijd omgekeerd evenredig met de beginsnelheid.",
      "antwoord": False,
      "uitleg": "Onwaar: Bij constante remkracht en vertraging is de remtijd juist recht evenredig met de beginsnelheid: twee keer zo snel betekent twee keer zo lang remmen."
    },
    {
      "type": "invul",
      "vraag": "Een scooter rijdt met een snelheid van 12 m/s. De bestuurder heeft een reactietijd van 0,75 s. Hoeveel meter bedraagt de reactieafstand?",
      "antwoord": "9|9 m|9 meter",
      "uitleg": "s_reactie = v · t_r = 12 m/s · 0,75 s = 9 meter."
    },
    {
      "type": "invul",
      "vraag": "Een auto heeft bij een noodstop een reactieafstand van 14 meter en een remweg van 26 meter. Wat is de totale stopafstand in meters?",
      "antwoord": "40|40 m|40 meter",
      "uitleg": "s_stop = s_reactie + s_rem = 14 m + 26 m = 40 meter."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de remweg van een auto vier keer zo lang wordt als de rijsnelheid slechts twee keer zo hoog is.",
      "modelantwoord": "De bewegingsenergie (kinetische energie) van een voorwerp hangt kwadratisch af van de snelheid (E_k = 0,5 · m · v²). Bij een dubbele snelheid heeft de auto vier keer zoveel energie die door de remmen moet worden weggewerkt. Omdat de maximale remkracht gelijk blijft en arbeid W = F · s is, moet de afstand (de remweg) vier keer zo groot worden.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "kwadratisch/kwadraat",
        "kinetische energie/bewegingsenergie"
      ],
      "uitleg": "De kinetische energie hangt af van het kwadraat van de snelheid; om 4× zoveel bewegingsenergie met gelijke remkracht om te zetten is 4× zoveel remafstand nodig."
    },
    {
      "type": "open",
      "vraag": "Benoem twee voorzieningen in een auto die ervoor zorgen dat de vertragingstijd tijdens een botsing wordt verlengd.",
      "modelantwoord": "1. De kreukelzone (die gecontroleerd indeukt).\n2. De veiligheidsgordel (die gecontroleerd meeveert/uitrekt) of de airbag.",
      "minTreffers": 2,
      "sleutelwoorden": [
        "kreukelzone/kreukel",
        "veiligheidsgordel/gordel/airbag"
      ],
      "uitleg": "Zowel de kreukelzone aan de carrosserie als de veiligheidsgordels en airbags zorgen voor een langere botstijd Δt waardoor de piekbelasting F daalt."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 62: §1.4 Veiligheid, Remweg & Stopafstand — Toets B
# -------------------------------------------------------------
toets_62 = {
  "id": "ex-h3-natuurkunde-62",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Toets 62 — §1.4 Veiligheid, Remweg & Stopafstand — Toets B",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚦",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een auto rijdt met 108 km/h op de snelweg. Hoeveel meter legt deze auto per seconde af?",
      "opties": [
        "30 m/s",
        "25 m/s",
        "36 m/s",
        "10,8 m/s"
      ],
      "antwoord": 0,
      "uitleg": "Omrekenen van km/h naar m/s: 108 / 3,6 = 30 m/s."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de <b>reactieafstand</b> als de snelheid van een voertuig verdrievoudigt bij gelijkblijvende reactietijd?",
      "opties": [
        "De reactieafstand wordt negen keer zo groot",
        "De reactieafstand wordt drie keer zo groot",
        "De reactieafstand blijft ongewijzigd",
        "De reactieafstand verdubbelt"
      ],
      "antwoord": 1,
      "uitleg": "De reactieafstand s_reactie = v · t_r is recht evenredig met de snelheid: als v 3× zo groot wordt, wordt s_reactie ook 3× zo groot."
    },
    {
      "type": "mc",
      "vraag": "Twee identieke auto's rijden op een droge asfaltweg. Auto A rijdt 40 km/h en auto B rijdt 80 km/h. Wat is de verhouding tussen hun remwegen?",
      "opties": [
        "De remweg van B is twee keer zo lang als die van A",
        "De remweg van B is drie keer zo lang als die van A",
        "De remweg van B is vier keer zo lang als die van A",
        "De remweg van B is acht keer zo lang als die van A"
      ],
      "antwoord": 2,
      "uitleg": "De snelheid van B is 2× zo groot als die van A. De remweg schaalt kwadratisch: (2)² = 4 keer zo lang."
    },
    {
      "type": "mc",
      "vraag": "In een (v,t)-diagram stelt de grafieklijn tijdens een noodstop een rechte dalende lijn naar de tijdsas voor. Wat betekent dit voor de versnelling?",
      "opties": [
        "De vertraging neemt iedere seconde toe",
        "De snelheid blijft tijdens het remmen constant",
        "De vertraging is nul doordat de wielen blokkeren",
        "De vertraging is constant (eenparig vertraagd)"
      ],
      "antwoord": 3,
      "uitleg": "Een rechte schuine lijn in een (v,t)-diagram betekent dat de snelheid iedere seconde met een vaste hoeveelheid afneemt: een constante negatieve versnelling (eenparige vertraging)."
    },
    {
      "type": "mc",
      "vraag": "Een vrachtwagen met een massa van 18 000 kg heeft bij dezelfde snelheid een langere remweg dan een kleine personenauto van 1200 kg. Waardoor komt dit?",
      "opties": [
        "De vrachtwagen heeft door zijn grote massa veel meer traagheid en kinetische energie",
        "De vrachtwagen ondervindt tijdens het rijden minder rolweerstand op de banden",
        "De banden van een vrachtwagen hebben minder contactoppervlak met het wegdek",
        "De vrachtwagenchauffeur heeft altijd een veel langere biologische reactietijd"
      ],
      "antwoord": 0,
      "uitleg": "Een grotere massa bezit meer traagheid en meer bewegingsenergie. Om deze energie om te zetten is aanzienlijk meer remafstand nodig."
    },
    {
      "type": "mc",
      "vraag": "Wat is het effect van gladde winterse omstandigheden (ijzel en sneeuw) op de stopafstand van een voertuig?",
      "opties": [
        "Alleen de reactieafstand neemt sterk toe",
        "De remweg neemt enorm toe doordat de maximale remkracht daalt",
        "Zowel de reactietijd als de remweg blijven gelijk",
        "De remweg halveert doordat de wielen gaan glijden"
      ],
      "antwoord": 1,
      "uitleg": "Door het gebrek aan grip kunnen de banden veel minder wrijvingskracht leveren, waardoor de remweg vele malen langer wordt."
    },
    {
      "type": "mc",
      "vraag": "Een bestuurder rijdt met 20 m/s en ziet een plotseling obstakel. Na 1,0 s reactietijd remt hij met een constante vertraging van 5,0 m/s². Hoeveel seconden duurt het remmen?",
      "opties": [
        "2,0 seconden",
        "3,0 seconden",
        "4,0 seconden",
        "5,0 seconden"
      ],
      "antwoord": 2,
      "uitleg": "De remtijd bereken je met t_rem = Δv / a = 20 m/s / 5,0 m/s² = 4,0 s."
    },
    {
      "type": "mc",
      "vraag": "Welke rol speelt een <b>airbag</b> bij een zware botsing?",
      "opties": [
        "De airbag blaast direct lucht naar de remleidingen om sneller te stoppen",
        "De airbag voorkomt dat de auto vlam vat door vonkvorming af te sluiten",
        "De airbag zorgt ervoor dat de auto na de klap automatisch ontgrendelt",
        "De airbag verdeelt de kracht over een groter lichaamsoppervlak en verlengt de remweg van het hoofd"
      ],
      "antwoord": 3,
      "uitleg": "De airbag vangt het hoofd en bovenlichaam geleidelijk op, verdeelt de impact over borst en hoofd en verlengt de remtijd waardoor letsel vermindert."
    },
    {
      "type": "mc",
      "vraag": "Een fietser rijdt met 5,0 m/s en remt eenparig af over een afstand van 5,0 meter. Wat was zijn remtijd?",
      "opties": [
        "2,0 seconden",
        "1,0 seconde",
        "0,5 seconde",
        "4,0 seconden"
      ],
      "antwoord": 0,
      "uitleg": "De gemiddelde snelheid tijdens het remmen is v_gem = (5,0 + 0) / 2 = 2,5 m/s. De remtijd is t_rem = s_rem / v_gem = 5,0 m / 2,5 m/s = 2,0 s."
    },
    {
      "type": "mc",
      "vraag": "Als de remweg bij 50 km/h gelijk is aan 15 meter, hoe lang is de remweg dan bij 100 km/h onder dezelfde wegomstandigheden?",
      "opties": [
        "30 meter",
        "60 meter",
        "45 meter",
        "75 meter"
      ],
      "antwoord": 1,
      "uitleg": "De snelheid verdubbelt (van 50 naar 100 km/h). De remweg wordt 2² = 4 keer zo lang: 15 m · 4 = 60 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de uitgeoefende botskracht op een inzittende als de botstijd Δt door een goede kreukelzone 3 keer zo groot wordt?",
      "opties": [
        "De botskracht wordt 3 keer zo groot",
        "De botskracht blijft exact gelijk",
        "De botskracht wordt 3 keer zo klein",
        "De botskracht daalt naar 0 Newton"
      ],
      "antwoord": 2,
      "uitleg": "Volgens F = m · Δv / Δt is de uitgeoefende kracht omgekeerd evenredig met de botstijd: 3× zo lange tijd levert 3× zo kleine kracht op."
    },
    {
      "type": "mc",
      "vraag": "Welke maatregel vergroot de reactietijd van een bestuurder?",
      "opties": [
        "Het monteren van bredere banden met dieper profiel",
        "Het inschakelen van mistverlichting bij dichte mist",
        "Het gebruik van antiblokkeer-remsystemen (ABS)",
        "Het beantwoorden van een tekstbericht tijdens het rijden"
      ],
      "antwoord": 3,
      "uitleg": "Afleiding door een telefoon vertraagt de reactiesnelheid van de hersenen en vergroot daarmee de reactietijd aanzienlijk."
    },
    {
      "type": "waaronwaar",
      "vraag": "De oppervlakte onder een (v,t)-diagram tijdens het afremmen van een voertuig stelt de afgelegde remweg voor.",
      "antwoord": True,
      "uitleg": "Waar: De oppervlakte onder de lijn in een snelheid-tijddiagram komt altijd overeen met de afgelegde afstand s."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een veiligheidsgordel moet van stug, volledig onrekbaar staaldraad worden gemaakt om de bestuurder direct muurvast op zijn stoel te fixeren.",
      "antwoord": False,
      "uitleg": "Onwaar: Een gordel moet juist een klein beetje gecontroleerd meegeven om de vertragingstijd te verlengen en dodelijke piekbelasting op de ribbenkast te voorkomen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de remweg bij 30 km/h gelijk is aan 4,5 meter, dan is de remweg bij 90 km/h gelijk aan 40,5 meter.",
      "antwoord": True,
      "uitleg": "Waar: De snelheid wordt 3 keer zo groot (90 / 30 = 3). De remweg wordt (3)² = 9 keer zo groot: 4,5 m · 9 = 40,5 m."
    },
    {
      "type": "waaronwaar",
      "vraag": "De totale stopafstand van een auto kan worden berekend door de reactieafstand te vermenigvuldigen met de remweg.",
      "antwoord": False,
      "uitleg": "Onwaar: De stopafstand is de som (optelling) van de twee afstanden: s_stop = s_reactie + s_rem."
    },
    {
      "type": "invul",
      "vraag": "Een automobilist rijdt met 25 m/s (90 km/h). Zijn reactietijd is 1,2 seconde. Hoeveel meter legt hij af tijdens zijn reactietijd?",
      "antwoord": "30|30 m|30 meter",
      "uitleg": "s_reactie = v · t_r = 25 m/s · 1,2 s = 30 meter."
    },
    {
      "type": "invul",
      "vraag": "Een fietser remt eenparig af vanaf 6,0 m/s tot stilstand in 3,0 seconden. Bereken de afgelegde remweg in meters.",
      "antwoord": "9|9,0|9 m|9 meter",
      "uitleg": "v_gem = (6,0 + 0) / 2 = 3,0 m/s. De remweg is s_rem = v_gem · t_rem = 3,0 m/s · 3,0 s = 9,0 meter."
    },
    {
      "type": "open",
      "vraag": "Noem twee verschillende factoren die uitsluitend de remweg van een voertuig beïnvloeden en de reactieafstand ongemoeid laten.",
      "modelantwoord": "1. De toestand van het wegdek (bijvoorbeeld nat, beijzeld of droog asfalt).\n2. De staat van de banden (profieldiepte/spanning) of de massa van het voertuig.",
      "minTreffers": 2,
      "sleutelwoorden": [
        "wegdek/asfalt/ijzel/gladheid",
        "banden/profieldiepte/remmen/massa"
      ],
      "uitleg": "Wegdek, bandenprofiel, remkracht en voertuigmassa beïnvloeden de wrijving en remweg, terwijl reactieafstand puur door snelheid en bestuurder wordt bepaald."
    },
    {
      "type": "open",
      "vraag": "Leg aan de hand van de formule F = m · Δv / Δt uit hoe een helm hoofdletsel bij een val vermindert.",
      "modelantwoord": "De kreukellaag (het schuim) in de helm deukt tijdens de klap gecontroleerd in. Hierdoor wordt de botsduur (Δt) aanzienlijk verlengd. Omdat de snelheidsverandering (Δv) en de massa (m) gelijk blijven, wordt de resulterende botskracht (F) op de schedel en hersenen veel kleiner.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "botsduur/botstijd/tijd verlengen",
        "kracht kleiner/kleinere kracht/veel kleiner"
      ],
      "uitleg": "Het indeuken van het helmschuim vergroot de remtijd Δt, waardoor de vertragingskracht F op het hoofd sterk afneemt."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 63: §1.5 Arbeid en Energieomzetting — Toets A
# -------------------------------------------------------------
toets_63 = {
  "id": "ex-h3-natuurkunde-63",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Toets 63 — §1.5 Arbeid en Energieomzetting — Toets A",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "⚙️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke natuurkundige formule gebruik je om de mechanische <b>arbeid</b> (W) te berekenen?",
      "opties": [
        "W = F · s",
        "W = F / s",
        "W = m · g · s²",
        "W = P / t"
      ],
      "antwoord": 0,
      "uitleg": "Arbeid is het product van kracht en verplaatsing in de bewegingsrichting: W = F · s."
    },
    {
      "type": "mc",
      "vraag": "Wat is de officiële SI-eenheid van arbeid en energie?",
      "opties": [
        "Watt (W)",
        "Joule (J)",
        "Newton (N)",
        "Pascal (Pa)"
      ],
      "antwoord": 1,
      "uitleg": "De SI-eenheid van arbeid en energie is Joule (J), wat gelijk is aan Newton-meter (N·m)."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel Joule (J) is gelijk aan <b>4,5 kilojoule (kJ)</b>?",
      "opties": [
        "45 J",
        "450 J",
        "4500 J",
        "45 000 J"
      ],
      "antwoord": 2,
      "uitleg": "Kilo staat voor duizend: 4,5 kJ = 4,5 · 1000 = 4500 Joule."
    },
    {
      "type": "mc",
      "vraag": "In welke van de volgende situaties verricht een uitgeoefende kracht <b>geen arbeid</b> (W = 0 J)?",
      "opties": [
        "Een paard dat een zware ploeg door de akker trekt",
        "Een kogel die door de zwaartekracht naar beneden valt",
        "Een fietser die tegen de wind in vooruit fietst",
        "Iemand die met grote spierkracht tegen een onbeweeglijke stenen muur duwt"
      ],
      "antwoord": 3,
      "uitleg": "Er is alleen sprake van arbeid als er een verplaatsing is (s > 0). Als de muur niet beweegt is s = 0 m en dus W = F · 0 = 0 J."
    },
    {
      "type": "mc",
      "vraag": "Een doos wordt over de vloer geduwd met een horizontale duwkracht van 60 N over een afstand van 4,0 meter. Hoeveel arbeid is er verricht?",
      "opties": [
        "240 Joule",
        "15 Joule",
        "64 Joule",
        "24 Joule"
      ],
      "antwoord": 0,
      "uitleg": "W = F · s = 60 N · 4,0 m = 240 J."
    },
    {
      "type": "mc",
      "vraag": "Wanneer spreken we in de natuurkunde van <b>positieve arbeid</b>?",
      "opties": [
        "Wanneer de kracht loodrecht op de bewegingsrichting staat",
        "Wanneer de uitgeoefende kracht meewerkt in de richting van de beweging",
        "Wanneer de wrijvingskracht een voorwerp tot stilstand brengt",
        "Wanneer er geen enkele energie wordt omgezet in warmte"
      ],
      "antwoord": 1,
      "uitleg": "Als de kracht in dezelfde richting werkt als de verplaatsing, is de arbeid positief en neemt de bewegingsenergie toe."
    },
    {
      "type": "mc",
      "vraag": "Wat doet een tegenwerkende wrijvings- of remkracht met de energie van een rijdende auto?",
      "opties": [
        "Het voegt extra potentiële energie toe aan het voertuig",
        "Het zet elektrische stroom om in chemische energie",
        "Het verricht negatieve arbeid en zet kinetische energie om in warmte",
        "Het verhoogt de gemiddelde snelheid van de auto"
      ],
      "antwoord": 2,
      "uitleg": "Tegenwerkende krachten werken tegen de verplaatsing in (negatieve arbeid) en zetten bewegingsenergie om in thermische energie (warmte in de remmen en banden)."
    },
    {
      "type": "mc",
      "vraag": "Een bouwvakker tilt een zak cement van 25 kg verticaal 2,0 meter omhoog (neem g = 10 N/kg). Hoeveel arbeid verricht hij tegen de zwaartekracht?",
      "opties": [
        "50 Joule",
        "125 Joule",
        "250 Joule",
        "500 Joule"
      ],
      "antwoord": 3,
      "uitleg": "De zwaartekracht is F_z = m · g = 25 kg · 10 N/kg = 250 N. De verrichte arbeid is W = F_z · h = 250 N · 2,0 m = 500 Joule."
    },
    {
      "type": "mc",
      "vraag": "Waarom verricht de <b>zwaartekracht</b> geen arbeid op een karretje dat zuiver horizontaal over een vlakke tafel rolt?",
      "opties": [
        "Omdat de zwaartekracht loodrecht (onder een hoek van 90°) op de verplaatsing staat",
        "Omdat de zwaartekracht binnenshuis wordt opgeheven door het dak",
        "Omdat een karretje op wielen geen zwaartekracht ondervindt",
        "Omdat de verplaatsing van het karretje gelijk is aan nul"
      ],
      "antwoord": 0,
      "uitleg": "Een kracht die loodrecht op de verplaatsingsrichting staat, werkt niet mee en niet tegen in de bewegingsrichting en verricht daardoor 0 J arbeid."
    },
    {
      "type": "mc",
      "vraag": "Een elektrische lier hijst een last omhoog over een hoogte van 8,0 meter. De lier verricht daarbij 1600 J aan nuttige arbeid. Hoe zwaar was de last in Newton?",
      "opties": [
        "12 800 N",
        "200 N",
        "1608 N",
        "800 N"
      ],
      "antwoord": 1,
      "uitleg": "W = F · s, dus F = W / s = 1600 J / 8,0 m = 200 N."
    },
    {
      "type": "mc",
      "vraag": "Een wandelaarster draagt een rugzak van 80 N op haar rug en loopt 500 meter over een volkomen horizontaal pad. Hoeveel arbeid verricht haar spierkracht in verticale richting op de rugzak?",
      "opties": [
        "40 000 Joule",
        "6,25 Joule",
        "0 Joule",
        "400 Joule"
      ],
      "antwoord": 2,
      "uitleg": "De verticale draagkracht staat loodrecht op de horizontale verplaatsing. In verticale richting is er geen verplaatsing (h = 0 m), dus W = 0 J."
    },
    {
      "type": "mc",
      "vraag": "Welke energieomzetting vindt er plaats wanneer een rijdende trein krachtig remt met mechanische remblokken?",
      "opties": [
        "Chemische energie wordt omgezet in zwaarte-energie",
        "Elektrische energie wordt omgezet in kernenergie",
        "Warmte wordt omgezet in kinetische energie",
        "Kinetische energie wordt omgezet in warmte"
      ],
      "antwoord": 3,
      "uitleg": "Door de wrijving tussen de remblokken en de wielen wordt de bewegingsenergie (kinetische energie) van de trein omgezet in warmte."
    },
    {
      "type": "waaronwaar",
      "vraag": "De eenheid Newton-meter (N·m) is natuurkundig gezien exact gelijk aan de eenheid Joule (J).",
      "antwoord": True,
      "uitleg": "Waar: 1 Joule is gedefinieerd als de arbeid die wordt verricht wanneer een kracht van 1 Newton een voorwerp over 1 meter verplaatst (1 J = 1 N·m)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer je een zware koffer van 20 kg minutenlang stil opgetild houdt zonder te bewegen, verricht je natuurkundig gezien veel arbeid.",
      "antwoord": False,
      "uitleg": "Onwaar: Hoewel het biologisch veel spierinspanning kost, is de natuurkundige verplaatsing s = 0 m en is de arbeid W = F · 0 = 0 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "De wrijvingskracht verricht altijd negatieve arbeid op een voorwerp dat over een ruwe ondergrond glijdt.",
      "antwoord": True,
      "uitleg": "Waar: Omdat de wrijvingskracht altijd tegengesteld gericht is aan de bewegingsrichting, onttrekt zij energie aan de beweging (negatieve arbeid)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je een voorwerp twee keer zo hoog optilt, is er vier keer zoveel arbeid nodig.",
      "antwoord": False,
      "uitleg": "Onwaar: Arbeid W = F · h is recht evenredig met de hoogte; twee keer zo hoog betekent twee keer zoveel arbeid."
    },
    {
      "type": "invul",
      "vraag": "Een paard trekt een wagen voort met een constante spankracht van 400 N over een afstand van 50 meter. Bereken de verrichte arbeid in Joule.",
      "antwoord": "20000|20.000|20000 J|20 000 J|20 kJ",
      "uitleg": "W = F · s = 400 N · 50 m = 20 000 Joule (20 kJ)."
    },
    {
      "type": "invul",
      "vraag": "Een doos wordt over de grond verschoven. De wrijvingskracht bedraagt 35 N. Hoeveel Joule aan warmte ontstaat er over een afstand van 6,0 meter?",
      "antwoord": "210|210 J|210 Joule",
      "uitleg": "W = F · s = 35 N · 6,0 m = 210 Joule."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom een gewichtheffer die een halter van 100 kg gedurende 5 seconden roerloos boven zijn hoofd houdt, natuurkundig gezien geen arbeid verricht.",
      "modelantwoord": "In de natuurkunde is arbeid gedefinieerd als W = F · s. Omdat de halter stilstaat, is de verplaatsing s gelijk aan 0 meter. Daardoor is de verrichte arbeid exact 0 Joule, ongeacht hoe zwaar de halter is.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "stilstaat/geen verplaatsing/0 meter",
        "0 joule/nul joule/formule"
      ],
      "uitleg": "Omdat er geen verplaatsing plaatsvindt (s = 0 m), is de arbeid volgens W = F · s gelijk aan 0 Joule."
    },
    {
      "type": "open",
      "vraag": "Geef het verschil aan tussen positieve en negatieve arbeid bij een rijdende auto.",
      "modelantwoord": "Positieve arbeid wordt geleverd door de motorkracht die in de rijrichting meewerkt en kinetische energie toevoegt (de auto versnelt of houdt snelheid). Negatieve arbeid wordt geleverd door de rem- en wrijvingskrachten die tegen de rijrichting in werken en kinetische energie omzetten in warmte (de auto vertraagt).",
      "minTreffers": 2,
      "sleutelwoorden": [
        "motorkracht/meewerkt/versnelt",
        "remkracht/tegenwerkt/warmte"
      ],
      "uitleg": "Kracht in de bewegingsrichting verricht positieve arbeid (energie toevoegen); kracht tegen de bewegingsrichting in verricht negatieve arbeid (energie onttrekken)."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 64: §1.5 Arbeid en Energieomzetting — Toets B
# -------------------------------------------------------------
toets_64 = {
  "id": "ex-h3-natuurkunde-64",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Toets 64 — §1.5 Arbeid en Energieomzetting — Toets B",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🏋️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een kraan tilt een betonnen heipaal van 1200 kg recht omhoog over een afstand van 15 meter (neem g = 10 N/kg). Hoeveel arbeid verricht de hijskabel?",
      "opties": [
        "180 kJ",
        "18 kJ",
        "120 kJ",
        "1800 J"
      ],
      "antwoord": 0,
      "uitleg": "F_z = m · g = 1200 kg · 10 N/kg = 12 000 N. De arbeid is W = F_z · h = 12 000 N · 15 m = 180 000 J = 180 kJ."
    },
    {
      "type": "mc",
      "vraag": "Een fietser fietst met constante snelheid over een vlakke weg. De voorwaartse trapkracht is 80 N. Welke arbeid verricht de fietser over een rit van 250 meter?",
      "opties": [
        "3,125 kJ",
        "20 kJ",
        "200 J",
        "0 J"
      ],
      "antwoord": 1,
      "uitleg": "W = F · s = 80 N · 250 m = 20 000 J = 20 kJ."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met alle arbeid die de remmen verrichten tijdens het stoppen van een auto?",
      "opties": [
        "De arbeid verdwijnt spoorloos uit het universum",
        "De arbeid wordt volledig opgeslagen in de accu van de auto",
        "De arbeid wordt omgezet in thermische energie (warmte in remmen en omgeving)",
        "De arbeid verandert in potentiële zwaarte-energie van de carrosserie"
      ],
      "antwoord": 2,
      "uitleg": "Volgens de wet van behoud van energie wordt de remarbeid (kinetische energie) omgezet in warmte van de remschijven, remblokken en lucht."
    },
    {
      "type": "mc",
      "vraag": "Een loper duwt een zware slee over sneeuw over een afstand van 30 meter. De wrijvingskracht is 150 N. Hoeveel negatieve arbeid verricht de wrijving?",
      "opties": [
        "5,0 J",
        "450 J",
        "45 kJ",
        "4,5 kJ"
      ],
      "antwoord": 3,
      "uitleg": "W = F · s = 150 N · 30 m = 4500 Joule = 4,5 kJ (negatieve arbeid: -4,5 kJ)."
    },
    {
      "type": "mc",
      "vraag": "Welk verband bestaat er tussen de eenheden Joule (J), Watt (W) en seconde (s)?",
      "opties": [
        "1 Joule = 1 Watt · seconde (1 J = 1 W · s)",
        "1 Joule = 1 Watt / seconde",
        "1 Joule = 1 seconde / Watt",
        "1 Joule = 1 Watt² · seconde"
      ],
      "antwoord": 0,
      "uitleg": "Vermogen is arbeid per tijdseenheid (P = W / t), dus W = P · t: 1 Joule = 1 Watt · 1 seconde."
    },
    {
      "type": "mc",
      "vraag": "Een speelgoedautootje met een massa van 0,50 kg wordt over een afstand van 2,0 meter geduwd met een kracht van 3,0 N. Wat is de verrichte arbeid?",
      "opties": [
        "1,5 Joule",
        "6,0 Joule",
        "1,0 Joule",
        "0,75 Joule"
      ],
      "antwoord": 1,
      "uitleg": "W = F · s = 3,0 N · 2,0 m = 6,0 J. De massa van het autootje heb je voor deze directe berekening niet nodig."
    },
    {
      "type": "mc",
      "vraag": "Waarom is traplopen vermoeiender dan horizontaal wandelen over dezelfde afstand?",
      "opties": [
        "Omdat de wrijving tussen schoenzolen en traptreden veel groter is",
        "Omdat de luchtdruk op de trap drastisch lager is",
        "Omdat je bij traplopen continu arbeid moet verrichten tegen de zwaartekracht in",
        "Omdat de spieren op een trap minder zuurstof uit het bloed kunnen opnemen"
      ],
      "antwoord": 2,
      "uitleg": "Bij traplopen verplaats je je eigen lichaamsgewicht verticaal omhoog: W = F_z · h. Bij horizontaal lopen is er geen hoogteverschil."
    },
    {
      "type": "mc",
      "vraag": "Een heftruck verricht 15 000 J arbeid om een pallet 3,0 meter omhoog te tillen. Hoe groot was de opwaartse tilkracht?",
      "opties": [
        "45 000 N",
        "500 N",
        "15 000 N",
        "5000 N"
      ],
      "antwoord": 3,
      "uitleg": "W = F · s, dus F = W / s = 15 000 J / 3,0 m = 5000 N."
    },
    {
      "type": "mc",
      "vraag": "Een parachutist daalt met constante eindsnelheid naar beneden. Welke uitspraak over de krachten en arbeid is juist?",
      "opties": [
        "De zwaartekracht verricht positieve arbeid en de luchtweerstand negatieve arbeid",
        "Beide krachten verrichten positieve arbeid waardoor de parachutist sneller valt",
        "Er wordt helemaal geen arbeid verricht omdat de snelheid constant is",
        "De luchtweerstand verricht positieve arbeid en de zwaartekracht negatieve arbeid"
      ],
      "antwoord": 0,
      "uitleg": "De zwaartekracht werkt naar beneden (mee met de valrichting: positieve arbeid). De luchtweerstand werkt omhoog (tegen de valrichting in: negatieve arbeid)."
    },
    {
      "type": "mc",
      "vraag": "Een doos glijdt over een helling naar beneden. Welke kracht verricht hierbij negatieve arbeid op de doos?",
      "opties": [
        "De component van de zwaartekracht langs de helling",
        "De wrijvingskracht tussen de doos en de helling",
        "De normaalkracht die loodrecht op de helling staat",
        "De voorwaartse stuwkracht van de helling"
      ],
      "antwoord": 1,
      "uitleg": "De wrijvingskracht wijst langs de helling omhoog, tegen de glijrichting in, en verricht daardoor negatieve arbeid."
    },
    {
      "type": "mc",
      "vraag": "Iemand trekt een kar met een trekkracht van 50 N schuin omhoog. Slechts 40 N hiervan werkt in de horizontale rijrichting. Welke kracht gebruik je om de arbeid bij 10 meter verplaatsing te berekenen?",
      "opties": [
        "De totale kracht van 50 N",
        "De verticale component van 30 N",
        "De kracht in de verplaatsingsrichting van 40 N",
        "Het gemiddelde van beide krachten (45 N)"
      ],
      "antwoord": 2,
      "uitleg": "Alleen de krachtcomponent die evenwijdig werkt aan de verplaatsing verricht nuttige mechanische arbeid: W = F_horizontaal · s = 40 N · 10 m = 400 J."
    },
    {
      "type": "mc",
      "vraag": "Een elektrische motor met een vermogen van 500 Watt draait gedurende 10 seconden. Hoeveel arbeid/energie heeft de motor geleverd?",
      "opties": [
        "50 Joule",
        "500 Joule",
        "2500 Joule",
        "5000 Joule"
      ],
      "antwoord": 3,
      "uitleg": "W = P · t = 500 W · 10 s = 5000 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Wanneer een voorwerp met constante snelheid beweegt onder invloed van een motorkracht en gelijke wrijvingskrachten, is de totale resulterende arbeid op het voorwerp gelijk aan nul.",
      "antwoord": True,
      "uitleg": "Waar: De positieve arbeid van de motor is exact gelijk aan de negatieve arbeid van de wrijving, waardoor de kinetische energie niet verandert (W_res = 0 J)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het horizontaal dragen van een zware rugzak over een afstand van 100 meter verricht de zwaartekracht 1000 J arbeid.",
      "antwoord": False,
      "uitleg": "Onwaar: Omdat de zwaartekracht loodrecht staat op de horizontale beweging, is de verrichte arbeid door de zwaartekracht 0 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 Megajoule (MJ) is gelijk aan 1 000 000 Joule.",
      "antwoord": True,
      "uitleg": "Waar: Het voorvoegsel Mega (M) staat voor één miljoen (10⁶)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de uitgeoefende kracht op een karretje halveert maar de afstand verdubbelt, halveert de totale verrichte arbeid.",
      "antwoord": False,
      "uitleg": "Onwaar: W = (0,5 · F) · (2 · s) = F · s; de verrichte arbeid blijft in dit geval precies gelijk."
    },
    {
      "type": "invul",
      "vraag": "Een atleet met een gewicht van 700 N loopt een trap op met een verticale hoogte van 4,0 meter. Hoeveel Joule arbeid verricht hij tegen de zwaartekracht?",
      "antwoord": "2800|2800 J|2800 Joule|2,8 kJ",
      "uitleg": "W = F_z · h = 700 N · 4,0 m = 2800 Joule."
    },
    {
      "type": "invul",
      "vraag": "Een hijskraan hijst een last van 500 N omhoog. De verrichte arbeid bedraagt 3500 J. Hoeveel meter hoog is de last gehesen?",
      "antwoord": "7|7,0|7 m|7 meter",
      "uitleg": "s = W / F = 3500 J / 500 N = 7,0 meter."
    },
    {
      "type": "open",
      "vraag": "Waarom warmen de remschijven van een raceauto enorm op tijdens het hard afremmen voor een bocht?",
      "modelantwoord": "Tijdens het remmen verrichten de remblokken negatieve arbeid op de beweging van de auto. Volgens de wet van behoud van energie wordt de bewegingsenergie (kinetische energie) van de auto door de mechanische wrijving direct omgezet in warmte (thermische energie) in de remschijven.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "kinetische energie/bewegingsenergie",
        "wrijving/warmte/omzetting"
      ],
      "uitleg": "De wrijvingskracht verricht remarbeid die de kinetische energie omzet in thermische energie (warmte)."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de zwaartekracht op een satelliet in een cirkelbaan om de aarde een totale arbeid van 0 Joule oplevert.",
      "modelantwoord": "In een cirkelbaan staat de zwaartekracht naar het middelpunt van de aarde gericht, wat exact loodrecht (onder een hoek van 90 graden) is op de voorwaartse vliegrichting van de satelliet. Een kracht die loodrecht op de verplaatsingsrichting staat, verricht geen mechanische arbeid.",
      "minTreffers": 1,
      "sleutelwoorden": [
        "loodrecht/haaks/90 graden",
        "verplaatsing/hoek"
      ],
      "uitleg": "Omdat de zwaartekracht loodrecht staat op de baanverplaatsing, is de verrichte arbeid exact nul."
    }
  ]
}

# -------------------------------------------------------------
# TOETS 65: Integrale Examentraining Hoofdstuk 1 (Mix §1.1 t/m §1.5)
# -------------------------------------------------------------
toets_65 = {
  "id": "ex-h3-natuurkunde-65",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Toets 65 — Integrale Examentraining Hoofdstuk 1 (Mix §1.1 t/m §1.5)",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🎯",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een auto rijdt met constante snelheid op de snelweg. De motorkracht is 1500 N. Hoe groot is de totale tegenwerkende kracht van rol- en luchtweerstand?",
      "opties": [
        "Exact 1500 N",
        "0 N",
        "Minder dan 1500 N",
        "3000 N"
      ],
      "antwoord": 0,
      "uitleg": "Bij constante snelheid is de versnelling a = 0 m/s² en dus de resulterende kracht Fres = 0 N. De tegenwerkende krachten moeten de motorkracht exact opheffen: F_tegen = 1500 N."
    },
    {
      "type": "mc",
      "vraag": "Wat lees je af aan de <b>steilheid (helling)</b> van de grafieklijn in een <b>(s,t)-diagram</b>?",
      "opties": [
        "De versnelling van het voorwerp",
        "De snelheid van het voorwerp",
        "De resulterende kracht op het voorwerp",
        "De totale verrichte arbeid"
      ],
      "antwoord": 1,
      "uitleg": "In een afstand-tijddiagram is de helling Δs / Δt gelijk aan de snelheid. Hoe steiler de lijn, hoe groter de snelheid."
    },
    {
      "type": "mc",
      "vraag": "Een voorwerp met een massa van 4,0 kg ondervindt een resulterende kracht van 12 N. Hoe groot is de versnelling?",
      "opties": [
        "48 m/s²",
        "0,33 m/s²",
        "3,0 m/s²",
        "16 m/s²"
      ],
      "antwoord": 2,
      "uitleg": "Volgens de tweede wet van Newton geldt Fres = m · a, dus a = Fres / m = 12 N / 4,0 kg = 3,0 m/s²."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je de afgelegde afstand uit een <b>(v,t)-diagram</b>?",
      "opties": [
        "Door de helling van de lijn te delen door de tijd",
        "Door de eindsnelheid te vermenigvuldigen met de versnelling",
        "Door de verticale aswaarde op t = 0 af te lezen",
        "Door de oppervlakte onder de grafieklijn te bepalen"
      ],
      "antwoord": 3,
      "uitleg": "De oppervlakte onder de grafieklijn in een (v,t)-diagram is gelijk aan de afgelegde afstand s (snelheid × tijd = afstand)."
    },
    {
      "type": "mc",
      "vraag": "Een scooterrijder rijdt met 10 m/s en remt af tot stilstand met een constante vertraging in 4,0 s. Wat is de afgelegde remweg?",
      "opties": [
        "20 meter",
        "40 meter",
        "10 meter",
        "2,5 meter"
      ],
      "antwoord": 0,
      "uitleg": "v_gem = (10 + 0) / 2 = 5,0 m/s. De remweg is s_rem = v_gem · t_rem = 5,0 m/s · 4,0 s = 20 meter."
    },
    {
      "type": "mc",
      "vraag": "Een hijskraan tilt een vracht van 500 kg over 6,0 meter hoogte omhoog (neem g = 10 N/kg). Hoeveel arbeid verricht de kraan?",
      "opties": [
        "3000 Joule",
        "30 kilojoule",
        "50 kilojoule",
        "83,3 Joule"
      ],
      "antwoord": 1,
      "uitleg": "F_z = m · g = 500 kg · 10 N/kg = 5000 N. Arbeid W = F · s = 5000 N · 6,0 m = 30 000 J = 30 kJ."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de remweg als een automobilist zijn snelheid verhoogt van 40 km/h naar 120 km/h?",
      "opties": [
        "De remweg wordt 3 keer zo lang",
        "De remweg wordt 6 keer zo lang",
        "De remweg wordt 9 keer zo lang",
        "De remweg wordt 16 keer zo lang"
      ],
      "antwoord": 2,
      "uitleg": "De snelheid wordt 3 keer zo groot (120 / 40 = 3). De remweg schaalt kwadratisch: (3)² = 9 keer zo lang."
    },
    {
      "type": "mc",
      "vraag": "Waarom blijft een hockeybal op glad ijs veel langer doorglijden dan op een grasveld?",
      "opties": [
        "Omdat de zwaartekracht op ijs veel minder sterk is",
        "Omdat de wrijvingskracht op ijs groter is dan de motorkracht",
        "Omdat de bal op ijs een veel grotere massa krijgt",
        "Omdat de tegenwerkende wrijvingskracht op glad ijs zeer klein is"
      ],
      "antwoord": 3,
      "uitleg": "Volgens de eerste wet van Newton behoudt een voorwerp zijn snelheid zolang er geen netto tegenkracht werkt; op glad ijs is de wrijving nagenoeg verwaarloosbaar."
    },
    {
      "type": "mc",
      "vraag": "Een auto heeft een massa van 1000 kg en accelereert met 2,5 m/s². De wrijvingskrachten bedragen samen 400 N. Hoe groot is de voorwaartse motorkracht?",
      "opties": [
        "2900 N",
        "2500 N",
        "2100 N",
        "400 N"
      ],
      "antwoord": 0,
      "uitleg": "Fres = m · a = 1000 kg · 2,5 m/s² = 2500 N. Omdat Fres = F_motor - F_wrijving, geldt F_motor = Fres + F_wrijving = 2500 N + 400 N = 2900 N."
    },
    {
      "type": "mc",
      "vraag": "Welke passieve veiligheidsvoorziening zorgt ervoor dat de vertragingstijd van het menselijk lichaam tijdens een crash wordt verlengd?",
      "opties": [
        "De stijve veiligheidskooi rond de passagiersruimte",
        "De kreukelzone en de meerekende veiligheidsgordel",
        "Het antiblokkeersysteem (ABS) van de remmen",
        "De achteruitrijcamera op de achterklep"
      ],
      "antwoord": 1,
      "uitleg": "Kreukelzones, meerekende gordels en airbags vervormen gecontroleerd, waardoor de botstijd Δt toeneemt en de kracht F daalt."
    },
    {
      "type": "mc",
      "vraag": "Een hardloper rent 400 meter in 50 seconden. Wat is zijn gemiddelde snelheid in kilometer per uur?",
      "opties": [
        "8,0 km/h",
        "20 km/h",
        "28,8 km/h",
        "32,4 km/h"
      ],
      "antwoord": 2,
      "uitleg": "v_gem = s / t = 400 m / 50 s = 8,0 m/s. Omrekenen naar km/h: 8,0 · 3,6 = 28,8 km/h."
    },
    {
      "type": "mc",
      "vraag": "In welke situatie wordt er natuurkundig gezien <b>negatieve arbeid</b> verricht?",
      "opties": [
        "Wanneer een raketmotor een ruimteschip versnelt",
        "Wanneer een kraan een container omhoog hijst",
        "Wanneer een appel uit een boom naar beneden valt",
        "Wanneer een parachutist wordt afgeremd door de luchtweerstand"
      ],
      "antwoord": 3,
      "uitleg": "De luchtweerstand werkt omhoog terwijl de parachutist naar beneden beweegt; de kracht werkt tegen de beweging in en verricht dus negatieve arbeid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de resulterende kracht op een bewegend voorwerp nul is, komt het voorwerp binnen enkele seconden tot stilstand.",
      "antwoord": False,
      "uitleg": "Onwaar: Als Fres = 0 N, blijft de snelheid onveranderd en beweegt het voorwerp met constante snelheid in een rechte lijn door (eerste wet van Newton)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De totale stopafstand van een auto is gelijk aan de reactieafstand plus de remweg.",
      "antwoord": True,
      "uitleg": "Waar: De totale afstand vanaf het zien van een gevaar tot volledige stilstand is de som van reactieafstand en remweg: s_stop = s_reactie + s_rem."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kracht die onder een hoek van 90° (loodrecht) op de bewegingsrichting staat, verricht geen mechanische arbeid.",
      "antwoord": True,
      "uitleg": "Waar: Omdat de krachtcomponent in de bewegingsrichting nul is, is de verrichte arbeid exact 0 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een zware vrachtwagen en een lichte bromfiets hebben bij dezelfde snelheid en gelijke remkracht exact dezelfde remweg.",
      "antwoord": False,
      "uitleg": "Onwaar: De vrachtwagen heeft door zijn grote massa veel meer traagheid (a = F/m is kleiner) en veel meer kinetische energie, waardoor de remweg veel langer is."
    },
    {
      "type": "invul",
      "vraag": "Een kracht van 45 N verplaatst een kist over een afstand van 8,0 meter in de richting van de kracht. Bereken de verrichte arbeid in Joule.",
      "antwoord": "360|360 J|360 Joule",
      "uitleg": "W = F · s = 45 N · 8,0 m = 360 Joule."
    },
    {
      "type": "invul",
      "vraag": "Een scooter rijdt met 15 m/s. De bestuurder heeft een reactietijd van 0,8 s. Hoeveel meter legt de scooter af tijdens de reactietijd?",
      "antwoord": "12|12 m|12 meter",
      "uitleg": "s_reactie = v · t_r = 15 m/s · 0,8 s = 12 meter."
    },
    {
      "type": "open",
      "vraag": "Beschrijf wat er gebeurt met de snelheid van een voorwerp wanneer de resulterende kracht in dezelfde richting werkt als de beweging.",
      "modelantwoord": "Wanneer de resulterende kracht in de bewegingsrichting werkt, versnelt het voorwerp (de snelheid neemt toe) volgens de tweede wet van Newton (Fres = m · a).",
      "minTreffers": 1,
      "sleutelwoorden": [
        "versnelt/versnelling/toeneemt",
        "fres = m/newton"
      ],
      "uitleg": "Een resulterende kracht in de bewegingsrichting levert een positieve versnelling waardoor de snelheid toeneemt."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom het dragen van een veiligheidsgordel in combinatie met een kreukelzone de kans op ernstig letsel verkleint.",
      "modelantwoord": "De kreukelzone en de meerekende gordel verlengen samen de vertragingstijd (de botstijd Δt) van het lichaam. Omdat F = m · Δv / Δt daalt de piekbelasting (kracht) op de inzittenden aanzienlijk. Bovendien voorkomt de gordel dat de inzittende hard tegen het stuur of de voorruit slaat.",
      "minTreffers": 2,
      "sleutelwoorden": [
        "vertragingstijd/botstijd/tijd verlengen",
        "piekbelasting/kracht daalt/kleinere kracht"
      ],
      "uitleg": "Door de verlengde vertragingstijd Δt daalt de uitgeoefende impactkracht F volgens F = m · Δv / Δt en wordt doorschieten voorkomen."
    }
  ]
}

# -------------------------------------------------------------
# Execute writing and validating
# -------------------------------------------------------------
if __name__ == "__main__":
    print("Natuurkunde toetsen 61 t/m 65 genereren...")
    p61 = [1, 3, 0, 2, 0, 3, 1, 2, 3, 0, 2, 1]
    p62 = [2, 0, 3, 1, 3, 2, 0, 1, 0, 2, 1, 3]
    p63 = [0, 2, 1, 3, 1, 0, 3, 2, 2, 3, 0, 1]
    p64 = [3, 1, 2, 0, 2, 1, 0, 3, 1, 0, 3, 2]
    p65 = [1, 0, 3, 2, 0, 2, 1, 3, 3, 1, 2, 0]
    
    validate_and_save_exam(toets_61, "examen_61.js", p61)
    validate_and_save_exam(toets_62, "examen_62.js", p62)
    validate_and_save_exam(toets_63, "examen_63.js", p63)
    validate_and_save_exam(toets_64, "examen_64.js", p64)
    validate_and_save_exam(toets_65, "examen_65.js", p65)
    print("Alle 5 toetsen succesvol gevalideerd en opgeslagen!")

