#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 1 (Umgebung & Wetter)
Exams: examen_1.js to examen_5.js
"""

import os
import json

BASE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/duits"
DATA_DIR = os.path.join(BASE_DIR, "js/data")

def balance_mc(questions):
    mc_indices = [i for i, q in enumerate(questions) if q.get("type") == "mc"]
    target_pattern = [0, 1, 2, 3] * (len(mc_indices) // 4 + 2)
    for idx, q_idx in enumerate(mc_indices):
        q = questions[q_idx]
        current_ans_idx = q["antwoord"]
        correct_text = q["opties"][current_ans_idx]
        new_ans_idx = target_pattern[idx] % len(q["opties"])
        if new_ans_idx != current_ans_idx:
            opts = [opt for i, opt in enumerate(q["opties"]) if i != current_ans_idx]
            opts.insert(new_ans_idx, correct_text)
            q["opties"] = opts
            q["antwoord"] = new_ans_idx

def write_exam(filename, data):
    balance_mc(data["vragen"])
    path = os.path.join(DATA_DIR, filename)
    content = f"""/* Proeftoets {data['id']} — {data['titel']}
   Neue Kontakte 3 HAVO Hoofdstuk {data['hoofdstuk']} */
DURU.registerExamen({json.dumps(data, indent=2, ensure_ascii=False)});
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [✓] Exam saved: {filename}")

# ================= EXAM 1 =================
ex1 = {
  "id": "ex-h3-duits-1",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Umgebung & Wetter",
  "titel": "Proeftoets 1 — Natuur, Weer & Sein/Haben",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 1",
  "icoon": "🌲",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de wolk'?",
      "opties": ["die Wolke", "der Wind", "der Nebel", "der Regen"],
      "antwoord": 0,
      "uitleg": "'Die Wolke' is de wolk. 'Der Wind' is wind en 'der Nebel' is mist."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste verleden tijdsvorm van sein: 'Gestern ____ das Wetter herrlich.'",
      "opties": ["war", "waren", "hatte", "wurde"],
      "antwoord": 0,
      "uitleg": "'Das Wetter' is enkelvoud (es), dus de verleden tijd is 'war'."
    },
    {
      "type": "mc",
      "vraag": "Welke zin betekent 'Het sneeuwt in de bergen'?",
      "opties": ["Es schneit in den Bergen.", "Es regnet auf den Bergen.", "Die Sonne scheint in den Bergen.", "Es friert an den Bergen."],
      "antwoord": 0,
      "uitleg": "'Schneien' is sneeuwen en 'in den Bergen' betekent in de bergen."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste vorm van 'haben' in de verleden tijd bij 'wir'?",
      "opties": ["wir hatten", "wir hattet", "wir waren", "wir habten"],
      "antwoord": 0,
      "uitleg": "De verleden tijd van haben bij 'wir' is 'hatten'."
    },
    {
      "type": "mc",
      "vraag": "Welk seizoen volgt direct op de winter?",
      "opties": ["der Frühling", "der Sommer", "der Herbst", "das Jahr"],
      "antwoord": 0,
      "uitleg": "Na de winter komt de lente: 'der Frühling'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'werden': 'Morgen ____ es stürmisch.'",
      "opties": ["wird", "werdet", "wirst", "werden"],
      "antwoord": 0,
      "uitleg": "Bij 'es' verandert werden naar 'wird' (met i)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de betekenis van het Duitse zelfstandig naamwoord 'der Wald'?",
      "opties": ["het bos", "het meer", "de berg", "het strand"],
      "antwoord": 0,
      "uitleg": "'Der Wald' betekent het bos (meervoud: die Wälder)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Letztes Wochenende ____ ihr in den Alpen, oder?' (sein)",
      "opties": ["wart", "waren", "warst", "hattet"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort de vorm 'wart' (zonder e)."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je 'in de herfst' in het Duits?",
      "opties": ["im Herbst", "am Herbst", "in die Herbst", "zum Herbst"],
      "antwoord": 0,
      "uitleg": "Bij seizoenen en maanden gebruik je 'im' (im Herbst)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het signaalwoord 'trotzdem'?",
      "opties": ["toch / desondanks", "daarom", "omdat", "plotseling"],
      "antwoord": 0,
      "uitleg": "'Trotzdem' betekent toch of desondanks."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zijn alle maanden mannelijk (der Januar, der Juli).",
      "antwoord": True,
      "uitleg": "Waar! Alle twaalf maanden hebben het mannelijke lidwoord 'der'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijdsvorm van haben bij 'ich' is 'ich hatte'.",
      "antwoord": True,
      "uitleg": "Waar! 'ich hatte' is de 1e persoon enkelvoud verleden tijd."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Gewitter' betekent 'de zonneschijn'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das Gewitter' betekent 'het onweer'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De Zugspitze is een rivier die door Hamburg stroomt.",
      "antwoord": False,
      "uitleg": "Onwaar! De Zugspitze is de hoogste berg van Duitsland in de Alpen."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sein' in de verleden tijd in: 'Ich ____ gestern krank zu Hause.'",
      "antwoord": "war",
      "uitleg": "De verleden tijd van sein bij 'ich' is 'war'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'haben' in de verleden tijd in: 'Wir ____ gestern viel Glück mit dem Wetter.'",
      "antwoord": "hatten",
      "uitleg": "Bij 'wir' hoort 'hatten'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Es gibt heute dichten (mist) auf den Straßen.'",
      "antwoord": "Nebel",
      "uitleg": "Mist is in het Duits 'der Nebel'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'werden' in: 'Du ____ sicher bald wieder gesund.'",
      "antwoord": "wirst",
      "uitleg": "Bij 'du' hoort de vorm 'wirst'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe beschrijf je in het Duits een typische stormachtige herfstdag qua temperatuur en wind?",
      "modelantwoord": "Es ist windig, stürmisch und kühl mit viel Regen.",
      "sleutelwoorden": ["windig/stürmisch", "kühl/kalt", "Regen"],
      "minTreffers": 1,
      "uitleg": "Gebruik Duitse weerbegrippen zoals windig, stürmisch of kühl."
    },
    {
      "type": "open",
      "vraag": "Wat gebeurt er met de klinker van het werkwoord 'werden' bij de personen du en er/sie/es in de tegenwoordige tijd?",
      "modelantwoord": "De klinker e verandert in een i (du wirst, er wird).",
      "sleutelwoorden": ["klinkerwisseling", "verandert in i", "naar i"],
      "minTreffers": 1,
      "uitleg": "De stamklinker e wisselt naar een i bij du en er/sie/es."
    }
  ]
}

# ================= EXAM 2 =================
ex2 = {
  "id": "ex-h3-duits-2",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Umgebung & Wetter",
  "titel": "Proeftoets 2 — Seizoenen, Maanden & Weersvoorspelling",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 1",
  "icoon": "🌲",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Am Nachmittag zieht ein Gewitter auf'?",
      "opties": ["In de middag komt er onweer opzetten.", "In de ochtend schijnt de zon volop.", "Het gaat vanavond hard sneeuwen.", "De wind gaat vanmiddag liggen."],
      "antwoord": 0,
      "uitleg": "'Ein Gewitter aufziehen' betekent dat er onweer op komst is."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Gestern ____ (hadden) die Schüler keine Schule.'",
      "opties": ["hatten", "hattet", "hatte", "waren"],
      "antwoord": 0,
      "uitleg": "'Die Schüler' is meervoud (sie), dus 'hatten'."
    },
    {
      "type": "mc",
      "vraag": "Welk Duits woord betekent 'de rivier'?",
      "opties": ["der Fluss", "der See", "das Meer", "der Wald"],
      "antwoord": 0,
      "uitleg": "'Der Fluss' is de rivier (bijv. der Rhein)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Wie ____ gestern das Wetter in München?' (sein)",
      "opties": ["war", "waren", "wurde", "hatte"],
      "antwoord": 0,
      "uitleg": "'Das Wetter' is 3e persoon enkelvoud (es), dus 'war'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de Duitse naam voor de maand augustus?",
      "opties": ["August", "Augst", "Augen", "Herbst"],
      "antwoord": 0,
      "uitleg": "Augustus is in het Duits 'der August'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent 'Es sind minus fünf Grad'?",
      "opties": ["Het is vijf graden onder nul.", "Het is vijf graden boven nul.", "Het regent al vijf uur.", "Het sneeuwt vijf centimeter."],
      "antwoord": 0,
      "uitleg": "'Minus fünf Grad' betekent -5 graden (onder nul)."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van werden: 'Wir ____ morgen nach Berlin fahren.'",
      "opties": ["werden", "wird", "werdet", "wirst"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' hoort 'werden'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je 'in de winter' naar het Duits?",
      "opties": ["im Winter", "am Winter", "in der Winter", "zum Winter"],
      "antwoord": 0,
      "uitleg": "Seizoenen krijgen het voorzetsel 'im' (im Winter)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het signaalwoord 'deshalb'?",
      "opties": ["daarom", "echter", "hoewel", "voordat"],
      "antwoord": 0,
      "uitleg": "'Deshalb' geeft een gevolg aan en betekent daarom."
    },
    {
      "type": "mc",
      "vraag": "Welke bergketen ligt in het zuiden van Beieren?",
      "opties": ["Die Alpen", "Der Harz", "Die Eifel", "Der Taunus"],
      "antwoord": 0,
      "uitleg": "In het zuiden van Beieren liggen de Alpen."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijd van werden is identiek aan sein (ich war).",
      "antwoord": False,
      "uitleg": "Onwaar! Werden heeft als verleden tijd 'wurde' (ich wurde), sein heeft 'war'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lettercombinatie 'eu' in 'heute' spreek je uit als 'oj'.",
      "antwoord": True,
      "uitleg": "Waar! In het Duits klinkt 'eu' en 'äu' altijd als 'oj'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Frühling' betekent 'de herfst'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Frühling' is de lente; herfst is 'der Herbst'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij 'ihr' is de vorm van sein in de verleden tijd 'wart'.",
      "antwoord": True,
      "uitleg": "Waar! 'ihr wart' is jullie waren."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'haben' (verleden tijd) in: 'Ich ____ gestern keine Zeit.'",
      "antwoord": "hatte",
      "uitleg": "Bij 'ich' hoort 'hatte'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sein' (verleden tijd) in: 'Wo ____ du gestern Nachmittag?'",
      "antwoord": "warst",
      "uitleg": "Bij 'du' hoort 'warst'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Die (zon) scheint den ganzen Tag.'",
      "antwoord": "Sonne",
      "uitleg": "De zon is 'die Sonne'."
    },
    {
      "type": "invul",
      "vraag": "Vul het Duitse woord voor 'zomer' in: 'Im ____ fahren wir oft ans Meer.'",
      "antwoord": "Sommer",
      "uitleg": "De zomer is 'der Sommer'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Welke twee Duitse woorden kun je gebruiken om te zeggen dat het weer zonnig en warm is?",
      "modelantwoord": "Sonnig en warm (of die Sonne scheint).",
      "sleutelwoorden": ["sonnig", "warm", "Sonne"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'sonnig' en 'warm'."
    },
    {
      "type": "open",
      "vraag": "Waarom schrijf je in het Duits 'im Sommer' en niet 'in de Sommer'?",
      "modelantwoord": "Omdat seizoenen mannelijk zijn (der Sommer) en in + dem samensmelt tot im.",
      "sleutelwoorden": ["mannelijk", "in dem/im", "der Sommer"],
      "minTreffers": 1,
      "uitleg": "Seizoenen zijn mannelijk en 'in dem' wordt samengetrokken tot 'im'."
    }
  ]
}

# ================= EXAM 3 =================
ex3 = {
  "id": "ex-h3-duits-3",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Umgebung & Wetter",
  "titel": "Proeftoets 3 — Duitse Landschappen, Rivieren & Grammatica",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 1",
  "icoon": "🌲",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke grote Duitse rivier ontspringt in het Zwarte Woud en stroomt naar de Zwarte Zee?",
      "opties": ["Die Donau", "Der Rhein", "Die Elbe", "Die Weser"],
      "antwoord": 0,
      "uitleg": "De Donau ontspringt in het Schwarzwald en stroomt oostwaarts."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'werden': 'Er ____ Tierarzt.'",
      "opties": ["wird", "werdet", "wirst", "werden"],
      "antwoord": 0,
      "uitleg": "Bij 'er' hoort 'wird'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de uitdrukking: 'Es schüttet wie aus Eimern'?",
      "opties": ["Het regent pijpenstelen (giet van de regen).", "De emmers zijn vol met water.", "Het sneeuwt heel zachtjes.", "De zon breekt door de wolken."],
      "antwoord": 0,
      "uitleg": "Dit is een bekende Duitse uitdrukking voor harde regen."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Letztes Jahr ____ wir ein schönes Ferienhaus in Österreich.' (haben)",
      "opties": ["hatten", "hattet", "hatte", "waren"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' hoort 'hatten'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het strand'?",
      "opties": ["der Strand", "das Meer", "der Sand", "die Küste"],
      "antwoord": 0,
      "uitleg": "'Der Strand' is het strand."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Ihr ____ gestern sehr pünktlich.' (sein)",
      "opties": ["wart", "waren", "warst", "war"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'wart'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je de 'ä' uit in het Duitse woord 'Wälder'?",
      "opties": ["Als een open 'è'", "Als een 'aa'", "Als een 'ie'", "Als een 'oe'"],
      "antwoord": 0,
      "uitleg": "De Umlaut 'ä' klinkt als de open Nederlandse 'è'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Es weht ein starker Wind aus Norden'?",
      "opties": ["Er waait een sterke wind uit het noorden.", "In het noorden schijnt de zon.", "De noordenwind gaat liggen.", "Het sneeuwt hevig in het noorden."],
      "antwoord": 0,
      "uitleg": "'Wehen' betekent waaien en 'starker Wind' is sterke wind."
    },
    {
      "type": "mc",
      "vraag": "Welke maand hoort bij de winter in Duitsland?",
      "opties": ["der Januar", "der Mai", "der Juli", "der September"],
      "antwoord": 0,
      "uitleg": "Januari (der Januar) is een wintermaand."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het voegwoord 'weil'?",
      "opties": ["omdat", "hoewel", "terwijl", "zodra"],
      "antwoord": 0,
      "uitleg": "'Weil' betekent omdat en zet de persoonsvorm achteraan."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'der See' voor een binnenmeer en 'das Meer' voor de oceaan/zee.",
      "antwoord": True,
      "uitleg": "Waar! 'Der See' = het meer, 'das Meer' = de zee."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitgang voor 'du' bij het werkwoord werden is 'du werdst'.",
      "antwoord": False,
      "uitleg": "Onwaar! De juiste vorm is 'du wirst' (met klinkerwisseling naar i)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Zwarte Woud (Schwarzwald) ligt in het noorden van Duitsland aan de zee.",
      "antwoord": False,
      "uitleg": "Onwaar! Het Schwarzwald ligt in het zuidwesten van Duitsland."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd hebben 'ich' en 'er/sie/es' bij sein en haben dezelfde uitgang.",
      "antwoord": True,
      "uitleg": "Waar! Zowel ich als er/sie/es hebben geen persoonlijke persoonsvormuitgang (war / hatte)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sein' in de verleden tijd in: 'Sie (meervoud) ____ gestern in Berlin.'",
      "antwoord": "waren",
      "uitleg": "Bij 'sie' meervoud hoort 'waren'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'haben' in de verleden tijd in: 'Lukas ____ gestern Geburtstag.'",
      "antwoord": "hatte",
      "uitleg": "Lukas is 'er', dus 'hatte'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Im Herbst fallen die Blätter der (bomen).' → '... der ____.'",
      "antwoord": "Bäume",
      "uitleg": "De bomen zijn 'die Bäume' (enkelvoud: der Baum)."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'werden' in: 'Es ____ dunkel.'",
      "antwoord": "wird",
      "uitleg": "Bij 'es' hoort 'wird'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe zeg je in het Duits dat het vandaag bewolkt is en tien graden?",
      "modelantwoord": "Heute ist es bewölkt und es sind zehn Grad.",
      "sleutelwoorden": ["bewölkt/wolkig", "zehn Grad", "Grad"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'bewölkt' en 'zehn Grad'."
    },
    {
      "type": "open",
      "vraag": "Wat is het verschil in betekenis tussen de Duitse woorden 'der See' en 'das Meer'?",
      "modelantwoord": "Der See is een meer (binnenwater) en das Meer is de zee/oceaan.",
      "sleutelwoorden": ["meer/binnenwater", "zee/oceaan"],
      "minTreffers": 1,
      "uitleg": "Der See = meer; das Meer = zee."
    }
  ]
}

# ================= EXAM 4 =================
ex4 = {
  "id": "ex-h3-duits-4",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Umgebung & Wetter",
  "titel": "Proeftoets 4 — Weerberichten, Seizoensactiviteiten & Werkwoorden",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 1",
  "icoon": "🌲",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is de juiste vertaling voor 'In de lente bloeien de bloemen'?",
      "opties": ["Im Frühling blühen die Blumen.", "Am Frühling blühen die Blumen.", "In die Frühling wachsen die Bäume.", "Im Sommer schneit es."],
      "antwoord": 0,
      "uitleg": "'Im Frühling' = in de lente en 'die Blumen blühen' = de bloemen bloeien."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Max und Tim ____ gestern im Schwimmbad.' (sein)",
      "opties": ["waren", "wart", "war", "hatten"],
      "antwoord": 0,
      "uitleg": "Max en Tim zijn samen 'sie' (meervoud), dus 'waren'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent 'Es herrscht Glatteis auf den Autobahnen'?",
      "opties": ["Er is ijzel/gladheid op de snelwegen.", "Er is veel file op de autosnelweg.", "De snelwegen zijn afgesloten wegens hitte.", "Het regent zachtjes op de weg."],
      "antwoord": 0,
      "uitleg": "'Glatteis' betekent ijzel of spiegelglad ijs op het wegdek."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van haben: 'Du ____ recht!' (verleden tijd)",
      "opties": ["hattest", "hatte", "hast", "hattet"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort de uitgang '-test': 'hattest'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse woord 'die Insel'?",
      "opties": ["het eiland", "het meer", "de bergtop", "het bos"],
      "antwoord": 0,
      "uitleg": "'Die Insel' betekent het eiland (bijv. die Insel Rügen)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Morgen ____ die Temperaturen steigen.' (werden)",
      "opties": ["werden", "wird", "werdet", "wirst"],
      "antwoord": 0,
      "uitleg": "'Die Temperaturen' is meervoud, dus 'werden'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de correcte uitspraak van de 'ö' in 'Österreich'?",
      "opties": ["Als de Nederlandse 'eu' in 'deur'", "Als de 'oo' in 'boot'", "Als de 'oe' in 'boek'", "Als de 'aa' in 'maan'"],
      "antwoord": 0,
      "uitleg": "De Umlaut 'ö' klinkt als 'eu' (zoals in 'deur')."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse woord 'die Küste'?",
      "opties": ["de kust", "de rivier", "de bergpas", "het dal"],
      "antwoord": 0,
      "uitleg": "'Die Küste' is de kustlijn aan zee."
    },
    {
      "type": "mc",
      "vraag": "Welke maand valt in het Duitse voorjaar (Frühling)?",
      "opties": ["der April", "der August", "der November", "der Januar"],
      "antwoord": 0,
      "uitleg": "April (der April) is een lentemaand."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het signaalwoord 'zuerst'?",
      "opties": ["eerst / als eerste", "uiteindelijk", "daarna", "nooit"],
      "antwoord": 0,
      "uitleg": "'Zuerst' betekent eerst."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je de 'ü' in 'über' uit als een 'oe'-klank.",
      "antwoord": False,
      "uitleg": "Onwaar! De 'ü' spreek je uit als de Nederlandse 'uu' in 'vuur'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De Waddeneilanden liggen aan de Duitse Nordseeküste.",
      "antwoord": True,
      "uitleg": "Waar! De Noord-Friese en Oost-Friese eilanden liggen aan de Noordzee."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij 'ihr' is de vorm van haben in de verleden tijd 'ihr hatten'.",
      "antwoord": False,
      "uitleg": "Onwaar! Bij 'ihr' is het 'ihr hattet'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Nebel' betekent 'de mist'.",
      "antwoord": True,
      "uitleg": "Waar! 'Der Nebel' betekent mist."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sein' in de verleden tijd in: 'Mein Bruder ____ gestern im Kino.'",
      "antwoord": "war",
      "uitleg": "Mein Bruder is 'er', dus 'war'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'haben' in de verleden tijd in: 'Ihr ____ gestern viel Spaß!'",
      "antwoord": "hattet",
      "uitleg": "Bij 'ihr' hoort 'hattet'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Im Winter fahren viele Menschen in die (bergen).' → '... in die ____.'",
      "antwoord": "Berge",
      "uitleg": "De bergen zijn 'die Berge'."
    },
    {
      "type": "invul",
      "vraag": "Vul het Duitse woord voor 'wolk' in: 'Am Himmel ist keine einzige ____.'",
      "antwoord": "Wolke",
      "uitleg": "Een wolk is 'die Wolke'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Welke twee hulpwerkwoorden worden in het Duits het vaakst gebruikt in de verleden tijd (Präteritum)?",
      "modelantwoord": "De werkwoorden sein en haben.",
      "sleutelwoorden": ["sein", "haben"],
      "minTreffers": 1,
      "uitleg": "Sein en haben zijn de meest gebruikte Präteritum-werkwoorden."
    },
    {
      "type": "open",
      "vraag": "Wat betekent de weersuitdrukking 'Es donnert und blitzt'?",
      "modelantwoord": "Het dondert en bliksemt (het onweert).",
      "sleutelwoorden": ["dondert en bliksemt", "onweert/onweer"],
      "minTreffers": 1,
      "uitleg": "Dit betekent dat het dondert en bliksemt tijdens onweer."
    }
  ]
}

# ================= EXAM 5 =================
ex5 = {
  "id": "ex-h3-duits-5",
  "hoofdstuk": 1,
  "hoofdstukTitel": "Umgebung & Wetter",
  "titel": "Proeftoets 5 — Eindtoets Hoofdstuk 1 (Alles gemixt)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 1",
  "icoon": "🌲",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke zin over het weer en het weekend is grammaticaal helemaal correct?",
      "opties": ["Gestern war es sonnig und wir hatten viel Spaß.", "Gestern waren es sonnig und wir habten viel Spaß.", "Gestern war es sonnig und wir waren viel Spaß.", "Gestern wurde es Regen und wir hattet Spaß."],
      "antwoord": 0,
      "uitleg": "'war' bij es en 'hatten' bij wir is correct."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: 'Wie ist die Wettervorhersage für das Wochenende?'",
      "opties": ["Wat is het weerbericht voor het weekend?", "Hoe was het weer vorig weekend?", "Gaat het regenen op maandag?", "Hoe warm is het in het buitenland?"],
      "antwoord": 0,
      "uitleg": "'Die Wettervorhersage' is de weersverwachting of het weerbericht."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van werden: 'Es ____ kälter in der Nacht.'",
      "opties": ["wird", "werdet", "wirst", "werden"],
      "antwoord": 0,
      "uitleg": "Bij 'es' hoort 'wird'."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Warum ____ ihr gestern nicht im Park?' (sein)",
      "opties": ["wart", "waren", "warst", "hattet"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'wart'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het weer'?",
      "opties": ["das Wetter", "der Wind", "die Wolke", "das Klima"],
      "antwoord": 0,
      "uitleg": "'Das Wetter' is het weer."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je 'in mei' naar het Duits?",
      "opties": ["im Mai", "am Mai", "in der Mai", "zum Mai"],
      "antwoord": 0,
      "uitleg": "Maanden krijgen altijd 'im' (im Mai)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Der Himmel ist wolkenlos'?",
      "opties": ["De lucht is strakblauw en onbewolkt.", "Het regent heel hard.", "De zon is achter de mist verdwenen.", "Er hangen donkere onweerswolken."],
      "antwoord": 0,
      "uitleg": "'Wolkenlos' betekent wolkenloos of onbewolkt."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Anna ____ gestern Kopfschmerzen.' (haben)",
      "opties": ["hatte", "hattest", "hattet", "war"],
      "antwoord": 0,
      "uitleg": "Anna is 'sie' (3e pers ev), dus 'hatte'."
    },
    {
      "type": "mc",
      "vraag": "Welke stad is de bondshoofdstad en regeringszetel van Duitsland?",
      "opties": ["Berlin", "München", "Frankfurt", "Hamburg"],
      "antwoord": 0,
      "uitleg": "Berlijn (Berlin) is de hoofdstad van Duitsland."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het signaalwoord 'danach'?",
      "opties": ["daarna / vervolgens", "daarom", "voordat", "ondertussen"],
      "antwoord": 0,
      "uitleg": "'Danach' betekent daarna of vervolgens."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits hebben alle vier de seizoenen het lidwoord 'der' (der Frühling, der Sommer, der Herbst, der Winter).",
      "antwoord": True,
      "uitleg": "Waar! Alle seizoenen zijn mannelijk."
    },
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijdsvorm voor 'wir' bij sein is 'wir wart'.",
      "antwoord": False,
      "uitleg": "Onwaar! Bij 'wir' is het 'wir waren'. 'wart' hoort bij 'ihr'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der See' betekent 'het meer'.",
      "antwoord": True,
      "uitleg": "Waar! 'Der See' = het meer."
    },
    {
      "type": "waaronwaar",
      "vraag": "De Zugspitze ligt in het noorden van Duitsland aan de Oostzee.",
      "antwoord": False,
      "uitleg": "Onwaar! De Zugspitze ligt in de Alpen in Zuid-Beieren."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sein' in de verleden tijd in: 'Wir ____ gestern sehr müde nach der Wanderung.'",
      "antwoord": "waren",
      "uitleg": "Bij 'wir' hoort 'waren'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'haben' in de verleden tijd in: 'Ich ____ gestern keine Hausaufgaben.'",
      "antwoord": "hatte",
      "uitleg": "Bij 'ich' hoort 'hatte'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Es schneit, überall liegt weißer (sneeuw).' → '... weißer ____.'",
      "antwoord": "Schnee",
      "uitleg": "Sneeuw is 'der Schnee'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'werden' in: 'Morgen ____ es wieder wärmer.'",
      "antwoord": "wird",
      "uitleg": "Bij 'es' hoort 'wird'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem twee Duitse voorzetselcombinaties voor tijd: één voor maanden/seizoenen en één voor kloktijden.",
      "modelantwoord": "Voor maanden/seizoenen gebruik je 'im' (bijv. im Sommer) en voor kloktijden 'um' (bijv. um acht Uhr).",
      "sleutelwoorden": ["im", "um"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'im' voor seizoenen/maanden en 'um' voor kloktijden."
    },
    {
      "type": "open",
      "vraag": "Hoe spreek je in het Duits de medeklinkers 'sp' en 'st' uit aan het begin van een woord?",
      "modelantwoord": "Als 'sjp' en 'sjt' (bijvoorbeeld Sport klinkt als sjport).",
      "sleutelwoorden": ["sjp", "sjt", "sj"],
      "minTreffers": 1,
      "uitleg": "Aan het begin van een woord klinken sp en st als sjp en sjt."
    }
  ]
}

# Write H1 exams
write_exam("examen_1.js", ex1)
write_exam("examen_2.js", ex2)
write_exam("examen_3.js", ex3)
write_exam("examen_4.js", ex4)
write_exam("examen_5.js", ex5)

print("\n🎉 H1 Exams generated successfully!")
