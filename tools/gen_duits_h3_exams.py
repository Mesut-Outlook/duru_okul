#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 3 (Unterwegs)
Exams: examen_11.js to examen_15.js
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

# ================= EXAM 11 =================
ex11 = {
  "id": "ex-h3-duits-11",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unterwegs",
  "titel": "Proeftoets 11 — Vervoer, Station & Modale Hulpwerkwoorden",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 3",
  "icoon": "🚆",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het treinstation'?",
      "opties": ["der Bahnhof", "der Flughafen", "die Haltestelle", "das Gleis"],
      "antwoord": 0,
      "uitleg": "'Der Bahnhof' is het station. 'Der Flughafen' is het vliegveld."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'können' (verleden tijd): 'Gestern ____ ich nicht kommen.'",
      "opties": ["konnte", "könnte", "kann", "konntest"],
      "antwoord": 0,
      "uitleg": "Verleden tijd van können bij 'ich' is 'konnte' (zonder Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: 'Muss ich in Hannover umsteigen?'",
      "opties": ["Moet ik in Hannover overstappen?", "Komt de trein in Hannover aan?", "Moet ik in Hannover uitstappen?", "Waar kan ik in Hannover een kaartje kopen?"],
      "antwoord": 0,
      "uitleg": "'Umsteigen' betekent overstappen op een andere trein of bus."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'müssen' (verleden tijd): 'Wir ____ lange warten.'",
      "opties": ["mussten", "müssten", "musstet", "musste"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' hoort 'mussten'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de juiste Duitse vertaling voor 'rechtdoor gaan'?",
      "opties": ["geradeaus gehen", "nach links abbiegen", "nach rechts gehen", "zurückkommen"],
      "antwoord": 0,
      "uitleg": "'Geradeaus' betekent rechtdoor."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van dürfen): 'Die Kinder ____ nicht draußen spielen.'",
      "opties": ["durften", "dürften", "darfen", "durftet"],
      "antwoord": 0,
      "uitleg": "'Die Kinder' is meervoud (sie), dus 'durften'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Abfahrt' op het station?",
      "opties": ["het vertrek", "de aankomst", "de vertraging", "het spoor"],
      "antwoord": 0,
      "uitleg": "'Die Abfahrt' is het vertrek. Aankomst is 'die Ankunft'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'wollen' (verleden tijd): 'Er ____ nach Berlin fahren.'",
      "opties": ["wollte", "will", "wolltest", "wolltet"],
      "antwoord": 0,
      "uitleg": "Bij 'er' hoort 'wollte'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je 'sp' uit in 'spielen'?",
      "opties": ["Als 'sjp'", "Als een gewone 's'", "Als 'kp'", "Als 'zp'"],
      "antwoord": 0,
      "uitleg": "Aan het begin van een woord klinkt 'sp' als 'sjp'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de uitdrukking: 'Der Zug hat zehn Minuten Verspätung'?",
      "opties": ["De trein heeft tien minuten vertraging.", "De trein vertrekt over tien minuten.", "De rit duurt tien minuten korter.", "Het spoor is tien meter lang."],
      "antwoord": 0,
      "uitleg": "'Verspätung' betekent vertraging."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd verliezen modale werkwoorden (können, müssen, dürfen) altijd hun Umlaut.",
      "antwoord": True,
      "uitleg": "Waar! In het Präteritum wordt können → konnte, müssen → musste, dürfen → durfte."
    },
    {
      "type": "waaronwaar",
      "vraag": "De afkorting 'DB' staat voor Deutsche Bahn.",
      "antwoord": True,
      "uitleg": "Waar! DB is de nationale spoorwegmaatschappij van Duitsland."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Gleis' betekent 'de bushalte'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das Gleis' is het treinspoor. Een bushalte is 'die Haltestelle'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijd van 'wissen' bij 'ich' is 'ich weisste'.",
      "antwoord": False,
      "uitleg": "Onwaar! De juiste vorm is 'ich wusste'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'können' in de verleden tijd in: 'Wir ____ die Fahrkarten nicht finden.'",
      "antwoord": "konnten",
      "uitleg": "Bij 'wir' hoort 'konnten'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'müssen' in de verleden tijd in: 'Er ____ früh aufstehen.'",
      "antwoord": "musste",
      "uitleg": "Bij 'er' hoort 'musste'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de richting: 'Sla bij het stoplicht naar (rechts) af.' → '... nach ____ abbiegen.'",
      "antwoord": "rechts",
      "uitleg": "Rechts is in het Duits 'rechts'."
    },
    {
      "type": "invul",
      "vraag": "Wat is het Duitse woord voor het centraal treinstation (afgekort Hbf)?",
      "antwoord": "Hauptbahnhof",
      "uitleg": "Het centraal station is 'der Hauptbahnhof'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe vraag je in het Duits beleefd de weg naar het station?",
      "modelantwoord": "Entschuldigung, wie komme ich zum Bahnhof?",
      "sleutelwoorden": ["wie komme ich", "zum Bahnhof", "Bahnhof"],
      "minTreffers": 1,
      "uitleg": "De vaste vraag is 'Entschuldigung, wie komme ich zum Bahnhof?'."
    },
    {
      "type": "open",
      "vraag": "Welke verleden tijdsvormen hebben de modale werkwoorden 'können' en 'müssen' bij de persoon 'ich'?",
      "modelantwoord": "Ich konnte en ich musste.",
      "sleutelwoorden": ["konnte", "musste"],
      "minTreffers": 1,
      "uitleg": "Konnte en musste."
    }
  ]
}

# ================= EXAM 12 =================
ex12 = {
  "id": "ex-h3-duits-12",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unterwegs",
  "titel": "Proeftoets 12 — Wegwijzen, Openbaar Vervoer & Verleden Tijd",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 3",
  "icoon": "🚆",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de route-instructie: 'Überqueren Sie die Brücke und biegen Sie links ab'?",
      "opties": ["Steek de brug over en sla linksaf.", "Rijd onder het viaduct door naar rechts.", "Ga rechtdoor tot aan de kruising.", "Neem de eerste straat rechts na de brug."],
      "antwoord": 0,
      "uitleg": "'Die Brücke überqueren' is de brug oversteken en 'links abbiegen' is linksaf slaan."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'wissen' in de verleden tijd: 'Ich ____ das wirklich nicht.'",
      "opties": ["wusste", "wusstest", "weisste", "wies"],
      "antwoord": 0,
      "uitleg": "Bij 'ich' hoort 'wusste'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het stoplicht'?",
      "opties": ["die Ampel", "die Kreuzung", "die Brücke", "das Schild"],
      "antwoord": 0,
      "uitleg": "'Die Ampel' is het verkeerslicht / stoplicht."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Ihr ____ (mochten) gestern nicht ins Kino gehen.' (dürfen)",
      "opties": ["durftet", "dürftet", "durften", "darftet"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'durftet' (zonder Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Hoe vraag je om een retourtje naar Berlijn?",
      "opties": ["Einmal Berlin hin und zurück, bitte.", "Einmal Berlin einfach, bitte.", "Nur nach Berlin, danke.", "Berlin ohne Rückfahrt."],
      "antwoord": 0,
      "uitleg": "'Hin und zurück' betekent retour."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'wollen': 'Was ____ du gestern machen?'",
      "opties": ["wolltest", "wolltet", "wollte", "willst"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort 'wolltest'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Kreuzung'?",
      "opties": ["de kruising / het kruispunt", "de rotonde", "het stoplicht", "de brug"],
      "antwoord": 0,
      "uitleg": "'Die Kreuzung' is de kruising."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van müssen): 'Lisa ____ ihre Fahrkarte zeigen.'",
      "opties": ["musste", "musstest", "mussten", "müsste"],
      "antwoord": 0,
      "uitleg": "Lisa is 'sie' (3e pers ev), dus 'musste'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je 'st' uit in het Duitse woord 'Straße'?",
      "opties": ["Als 'sjt'", "Als een Nederlandse 's'", "Als 'kt'", "Als 'zt'"],
      "antwoord": 0,
      "uitleg": "'st' aan het begin van een woord spreek je uit als 'sjt'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de hogesnelheidstrein van Duitsland?",
      "opties": ["Der ICE (Intercity Express)", "Der TGV", "Der Thalys", "Der Eurostar"],
      "antwoord": 0,
      "uitleg": "De ICE is de Duitse hogesnelheidstrein."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'einfach' betekent bij treinkaartjes 'enkele reis'.",
      "antwoord": True,
      "uitleg": "Waar! 'Eine Fahrkarte einfach' is een enkele reis."
    },
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijd van 'können' bij 'du' is 'du konntest'.",
      "antwoord": True,
      "uitleg": "Waar! 'du konntest' is de 2e persoon enkelvoud."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Flughafen' betekent 'het treinstation'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Flughafen' is de luchthaven (het vliegveld)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin 'Wir wollten nach Hause fahren' staat het hele werkwoord 'fahren' vooraan in de zin.",
      "antwoord": False,
      "uitleg": "Onwaar! Het hele werkwoord staat helemaal aan het einde van de zin."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'können' in de verleden tijd in: 'Er ____ nicht schlafen.'",
      "antwoord": "konnte",
      "uitleg": "Bij 'er' hoort 'konnte'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'wollen' in de verleden tijd in: 'Wir ____ pünktlich ankommen.'",
      "antwoord": "wollten",
      "uitleg": "Bij 'wir' hoort 'wollten'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de richting: 'Sla bij het stoplicht naar (links) af.' → '... nach ____ abbiegen.'",
      "antwoord": "links",
      "uitleg": "Links is in het Duits 'links'."
    },
    {
      "type": "invul",
      "vraag": "Wat is het Duitse woord voor het treinkaartje?",
      "antwoord": "Fahrkarte",
      "uitleg": "Een treinkaartje is 'die Fahrkarte' of 'das Ticket'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat is het verschil in het Duits tussen 'einsteigen', 'aussteigen' en 'umsteigen'?",
      "modelantwoord": "Einsteigen = instappen; aussteigen = uitstappen; umsteigen = overstappen.",
      "sleutelwoorden": ["instappen", "uitstappen", "overstappen"],
      "minTreffers": 1,
      "uitleg": "Einsteigen (in), aussteigen (uit), umsteigen (over)."
    },
    {
      "type": "open",
      "vraag": "Welke drie landen vormen samen de DACH-regio?",
      "modelantwoord": "Duitsland (Deutschland), Oostenrijk (Österreich) en Zwitserland (Schweiz).",
      "sleutelwoorden": ["Deutschland/Duitsland", "Österreich/Oostenrijk", "Schweiz/Zwitserland"],
      "minTreffers": 1,
      "uitleg": "Duitsland, Oostenrijk en Zwitserland."
    }
  ]
}

# ================= EXAM 13 =================
ex13 = {
  "id": "ex-h3-duits-13",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unterwegs",
  "titel": "Proeftoets 13 — Dienstregeling, Reizen in de Alpen & Grammatica",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 3",
  "icoon": "🚆",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de melding: 'Der Zug fährt heute von Gleis 7 ab'?",
      "opties": ["De trein vertrekt vandaag van spoor 7.", "De trein heeft 7 minuten vertraging.", "De trein rijdt 7 wagons achter elkaar.", "De trein stopt op perron 7."],
      "antwoord": 0,
      "uitleg": "'Abfahren von Gleis 7' betekent vertrekken van spoor 7."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'müssen' (verleden tijd): 'Ihr ____ gestern lernen.'",
      "opties": ["musstet", "müsstet", "mussten", "musste"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'musstet'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'das Fahrrad' (de fiets)?",
      "opties": ["die Fahrräder", "die Fahrräden", "die Fahrraden", "die Fahrrads"],
      "antwoord": 0,
      "uitleg": "Het meervoud van das Fahrrad is 'die Fahrräder' (met Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van wissen): '____ ihr die Telefonnummer des Hotels?'",
      "opties": ["Wusstet", "Wussten", "Weisstet", "Wusst"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'wusstet'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent 'zu Fuß gehen'?",
      "opties": ["te voet gaan / lopen", "met de bus gaan", "snel rennen", "op blote voeten lopen"],
      "antwoord": 0,
      "uitleg": "'Zu Fuß' betekent te voet."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'dürfen' (verleden tijd): 'Ich ____ früher nicht alleine reisen.'",
      "opties": ["durfte", "dürfte", "darf", "durftest"],
      "antwoord": 0,
      "uitleg": "Bij 'ich' hoort 'durfte'."
    },
    {
      "type": "mc",
      "vraag": "Welke historische stad aan de Donau is de hoofdstad van Oostenrijk?",
      "opties": ["Wien", "Salzburg", "Innsbruck", "Graz"],
      "antwoord": 0,
      "uitleg": "Wenen (Wien) is de hoofdstad van Oostenrijk."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van können): 'Du ____ wirklich gut Deutsch sprechen!'",
      "opties": ["konntest", "könntest", "konnte", "kannst"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort 'konntest'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de bordtekst 'Kein Zutritt' op een perron?",
      "opties": ["Geen toegang / Verboden toegang", "Kaartjesautomaat defect", "Roken toegestaan", "Uitgang naar de stad"],
      "antwoord": 0,
      "uitleg": "'Kein Zutritt' betekent geen toegang."
    },
    {
      "type": "mc",
      "vraag": "Wat is de nationale spoorwegmaatschappij van Oostenrijk?",
      "opties": ["ÖBB", "DB", "SBB", "NS"],
      "antwoord": 0,
      "uitleg": "ÖBB staat voor Österreichische Bundesbahnen."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "De SBB is de spoorwegmaatschappij van Zwitserland.",
      "antwoord": True,
      "uitleg": "Waar! SBB (Schweizerische Bundesbahnen) is de Zwitserse spoorwegen."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd is de vorm van 'wollen' bij 'ich' 'ich willte'.",
      "antwoord": False,
      "uitleg": "Onwaar! De juiste vorm is 'ich wollte'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Straßenbahn' betekent 'de tram'.",
      "antwoord": True,
      "uitleg": "Waar! 'Die Straßenbahn' (of Tram) is de tram."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Oostenrijk is de officiële taal Italiaans.",
      "antwoord": False,
      "uitleg": "Onwaar! In Oostenrijk is Duits de officiële landstaal."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'müssen' in de verleden tijd in: 'Wir ____ um 6 Uhr aufstehen.'",
      "antwoord": "mussten",
      "uitleg": "Bij 'wir' hoort 'mussten'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'wissen' in de verleden tijd in: 'Er ____ nicht, wo das Gleis war.'",
      "antwoord": "wusste",
      "uitleg": "Bij 'er' hoort 'wusste'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Das (vliegtuig) landet um 14:00 Uhr.' → 'Das ____ landet...' ",
      "antwoord": "Flugzeug",
      "uitleg": "Het vliegtuig is 'das Flugzeug'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de term: '(Vertrek)' op een treinschema.",
      "antwoord": "Abfahrt",
      "uitleg": "Vertrek is 'die Abfahrt'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe zeg je in het Duits dat je met de bus naar school reist?",
      "modelantwoord": "Ich fahre mit dem Bus zur Schule.",
      "sleutelwoorden": ["mit dem Bus", "fahre mit dem Bus"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'mit dem Bus'."
    },
    {
      "type": "open",
      "vraag": "Waarom zeg je 'mit dem Zug' en niet 'mit den Zug' in het Duits?",
      "modelantwoord": "Omdat het voorzetsel mit altijd de 3e naamval (Dativ) regeert.",
      "sleutelwoorden": ["3e naamval", "Dativ", "voorzetsel mit"],
      "minTreffers": 1,
      "uitleg": "Het voorzetsel mit eist altijd de 3e naamval (Dativ)."
    }
  ]
}

# ================= EXAM 14 =================
ex14 = {
  "id": "ex-h3-duits-14",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unterwegs",
  "titel": "Proeftoets 14 — Reisplannen, Boekingen & Modale Werkwoorden",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 3",
  "icoon": "🚆",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: 'Haben Sie eine BahnCard?'",
      "opties": ["Heeft u een kortingskaart voor de Duitse trein?", "Wilt u betalen met creditcard?", "Heeft u een bankpasje?", "Wilt u een plattegrond van het station?"],
      "antwoord": 0,
      "uitleg": "De BahnCard is de populaire kortingskaart van de Deutsche Bahn."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Gestern ____ (wilden) wir eine Radtour machen.' (wollen)",
      "opties": ["wollten", "wolltet", "wollte", "wolltest"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' hoort 'wollten'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het verkeer'?",
      "opties": ["der Verkehr", "die Straße", "der Stau", "das Auto"],
      "antwoord": 0,
      "uitleg": "'Der Verkehr' is het verkeer."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van dürfen): 'Hier ____ man früher nicht parken.'",
      "opties": ["durfte", "dürfte", "darf", "durften"],
      "antwoord": 0,
      "uitleg": "Bij 'man' (3e pers ev) hoort 'durfte'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'der Stau' op de snelweg?",
      "opties": ["de file", "het ongeval", "het stoplicht", "het benzinestation"],
      "antwoord": 0,
      "uitleg": "'Der Stau' betekent de file."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'können' (verleden tijd): 'Ihr ____ gestern früher gehen.'",
      "opties": ["konntet", "könntet", "konnten", "konnte"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' hoort 'konntet'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Wir haben den Anschluss verpasst'?",
      "opties": ["We hebben de aansluiting (overstaptrein) gemist.", "We zijn op het verkeerde perron ingestapt.", "De trein had geen vertraging.", "We hebben onze kaartjes kwijtgeraakt."],
      "antwoord": 0,
      "uitleg": "'Den Anschluss verpassen' betekent de overstapaansluiting missen."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van müssen): 'Du ____ gestern die Fahrkarten kaufen.'",
      "opties": ["musstest", "müsstest", "musste", "musst"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort 'musstest'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de hoofdstad van Zwitserland?",
      "opties": ["Bern", "Zürich", "Genf", "Basel"],
      "antwoord": 0,
      "uitleg": "Bern is de hoofdstad van Zwitserland."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse woord 'die Fußgängerzone'?",
      "opties": ["het voetgangersgebied / de autovrije winkelstraat", "de oversteekplaats", "het busstation", "de fietstunnel"],
      "antwoord": 0,
      "uitleg": "'Die Fußgängerzone' is de autovrije voetgangerszone."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijdsvorm voor 'ich' en 'er/sie/es' bij modale werkwoorden is altijd hetzelfde (ich konnte, er konnte).",
      "antwoord": True,
      "uitleg": "Waar! 1e en 3e persoon enkelvoud zijn altijd gelijk in het Präteritum."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland mag je op alle snelwegen (Autobahnen) altijd zo hard rijden als je wilt.",
      "antwoord": False,
      "uitleg": "Onwaar! Hoewel sommige stukken geen snelheidslimiet hebben (Richtgeschwindigkeit 130 km/h), gelden op veel trajecten strikte limieten."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Haltestelle' betekent 'het spoornummer'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Haltestelle' is de halte (bus/tram); het spoor is 'das Gleis'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitspraak van 'sch' in 'Schule' klinkt als 'sj'.",
      "antwoord": True,
      "uitleg": "Waar! 'sch' klinkt altijd als 'sj'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'wollen' in de verleden tijd in: 'Ich ____ gestern mit dem Bus fahren.'",
      "antwoord": "wollte",
      "uitleg": "Bij 'ich' hoort 'wollte'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'können' in de verleden tijd in: 'Sie (zij enkelvoud) ____ kein Ticket kaufen.'",
      "antwoord": "konnte",
      "uitleg": "Bij 'sie' (ev) hoort 'konnte'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Wir stehen im (file).' → 'Wir stehen im ____.'",
      "antwoord": "Stau",
      "uitleg": "File is 'der Stau'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de richting: 'Ga altijd (rechtdoor).' → 'Gehen Sie immer ____.'",
      "antwoord": "geradeaus",
      "uitleg": "Rechtdoor is 'geradeaus'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe vraag je op het station naar de vertrektijd van de trein naar München?",
      "modelantwoord": "Wann fährt der Zug nach München ab?",
      "sleutelwoorden": ["Wann fährt", "Zug nach München", "ab"],
      "minTreffers": 1,
      "uitleg": "Je vraagt 'Wann fährt der Zug nach München ab?'."
    },
    {
      "type": "open",
      "vraag": "Wat betekent de Duitse reisterm 'hin und zurück'?",
      "modelantwoord": "Heen en terug (een retourtje).",
      "sleutelwoorden": ["retour/retourtje", "heen en terug"],
      "minTreffers": 1,
      "uitleg": "Dit betekent een retourticket (heen en terug)."
    }
  ]
}

# ================= EXAM 15 =================
ex15 = {
  "id": "ex-h3-duits-15",
  "hoofdstuk": 3,
  "hoofdstukTitel": "Unterwegs",
  "titel": "Proeftoets 15 — Eindtoets Hoofdstuk 3 (Alles gemixt)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 3",
  "icoon": "🚆",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke zin over de treinreis en overstappen is grammaticaal helemaal correct?",
      "opties": ["Wir mussten gestern umsteigen, weil der Zug Verspätung hatte.", "Wir müssten gestern umsteigen, weil der Zug Verspätung hatte.", "Wir mussten gestern umgestiegen, weil der Zug Verspätung war.", "Wir gemusst gestern umsteigen."],
      "antwoord": 0,
      "uitleg": "'mussten' (zonder Umlaut) en het hele werkwoord 'umsteigen' achteraan is correct."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'wissen' in de verleden tijd: '____ du das schon?'",
      "opties": ["Wusstest", "Wusste", "Weisst", "Wiesst"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort 'wusstest'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Biegen Sie an der Kreuzung rechts ab'?",
      "opties": ["Sla bij het kruispunt rechtsaf.", "Ga bij het stoplicht rechtdoor.", "Rijd over de brug naar links.", "Stop voor de rotonde."],
      "antwoord": 0,
      "uitleg": "'Kreuzung' is kruispunt en 'rechts abbiegen' is rechtsaf slaan."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'dürfen' (verleden tijd): 'Wir ____ nicht mitfahren.'",
      "opties": ["durften", "dürften", "darfen", "durftet"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' hoort 'durften'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het perron / het spoor'?",
      "opties": ["das Gleis", "die Haltestelle", "der Fahrplan", "die Ampel"],
      "antwoord": 0,
      "uitleg": "'Das Gleis' is het spoor."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (verleden tijd van wollen): 'Er ____ gestern nicht mitkommen.'",
      "opties": ["wollte", "will", "wolltest", "wolltet"],
      "antwoord": 0,
      "uitleg": "Bij 'er' hoort 'wollte'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Sitzplatzreservierung'?",
      "opties": ["de stoelreservering / zitplaatsreservering", "het treinkaartje", "de bagageruimte", "de restauratiewagen"],
      "antwoord": 0,
      "uitleg": "'Sitzplatzreservierung' is het reserveren van een vaste zitplaats in de trein."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'können' (verleden tijd): 'Ich ____ den Weg nicht finden.'",
      "opties": ["konnte", "könnte", "kann", "konntest"],
      "antwoord": 0,
      "uitleg": "Bij 'ich' hoort 'konnte'."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel officiële talen heeft Zwitserland?",
      "opties": ["4 (Duits, Frans, Italiaans, Retoromaans)", "1 (alleen Duits)", "2 (Duits en Frans)", "3 (Duits, Engels, Frans)"],
      "antwoord": 0,
      "uitleg": "Zwitserland heeft 4 officiële talen."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'die Verspätung'?",
      "opties": ["de vertraging", "het vertrek", "de aankomst", "de overstap"],
      "antwoord": 0,
      "uitleg": "'Die Verspätung' is de vertraging."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Bahnhof' betekent het treinstation.",
      "antwoord": True,
      "uitleg": "Waar! Der Bahnhof is het station."
    },
    {
      "type": "waaronwaar",
      "vraag": "De verleden tijd van müssen bij 'er' is 'er musste'.",
      "antwoord": True,
      "uitleg": "Waar! Er musste = hij moest."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je 'Sport' uit als een zachte Nederlandse s-klank.",
      "antwoord": False,
      "uitleg": "Onwaar! 'sp' aan het begin klinkt als 'sjp' (Sjport)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De afkorting 'Hbf' staat voor Havenbedrijf Frankfurt.",
      "antwoord": False,
      "uitleg": "Onwaar! Hbf staat voor Hauptbahnhof (Centraal Station)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'können' in de verleden tijd in: 'Wir ____ nicht pünktlich ankommen.'",
      "antwoord": "konnten",
      "uitleg": "Bij 'wir' hoort 'konnten'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'müssen' in de verleden tijd in: 'Ich ____ lange auf den Bus warten.'",
      "antwoord": "musste",
      "uitleg": "Bij 'ich' hoort 'musste'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Auf welchem (spoor) fährt der ICE ab?' → 'Auf welchem ____ ...'",
      "antwoord": "Gleis",
      "uitleg": "Spoor is 'das Gleis'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Aankomst)' op een treintabel.",
      "antwoord": "Ankunft",
      "uitleg": "Aankomst is 'die Ankunft'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem twee verschillende Duitse woorden voor verkeerssituaties (bijvoorbeeld kruising of stoplicht).",
      "modelantwoord": "Die Ampel (stoplicht), die Kreuzung (kruising) of die Brücke (brug).",
      "sleutelwoorden": ["Ampel", "Kreuzung", "Brücke"],
      "minTreffers": 1,
      "uitleg": "Je kunt Ampel, Kreuzung of Brücke noemen."
    },
    {
      "type": "open",
      "vraag": "Wat gebeurt er met de klinkers ö en ü van modale werkwoorden in de verleden tijd?",
      "modelantwoord": "Ze verliezen hun Umlaut (ö wordt o, ü wordt u).",
      "sleutelwoorden": ["verliezen Umlaut", "zonder Umlaut", "geen Umlaut"],
      "minTreffers": 1,
      "uitleg": "De Umlaut verdwijnt in de verleden tijd (können → konnte, müssen → musste)."
    }
  ]
}

# Write H3 exams
write_exam("examen_11.js", ex11)
write_exam("examen_12.js", ex12)
write_exam("examen_13.js", ex13)
write_exam("examen_14.js", ex14)
write_exam("examen_15.js", ex15)

print("\n🎉 H3 Exams generated successfully!")
