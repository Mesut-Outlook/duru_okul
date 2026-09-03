#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 5 (Zukunft & Berufe)
Exams: examen_21.js to examen_25.js
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

# ================= EXAM 21 =================
ex21 = {
  "id": "ex-h3-duits-21",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Zukunft & Berufe",
  "titel": "Proeftoets 21 — Beroepen, Opleidingen & Sterke Werkwoorden (a→ä)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 5",
  "icoon": "💼",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het beroep'?",
      "opties": ["der Beruf", "die Arbeit", "die Ausbildung", "das Praktikum"],
      "antwoord": 0,
      "uitleg": "'Der Beruf' is het beroep. Meervoud: die Berufe."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'fahren': 'Du ____ morgen mit dem Bus.'",
      "opties": ["fährst", "fahrst", "fahrt", "fährt"],
      "antwoord": 0,
      "uitleg": "Bij 'du' krijgt de stamklinker a een Umlaut: 'du fährst'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van 'der Verkäufer' (de verkoper)?",
      "opties": ["die Verkäuferin", "die Verkäufer", "die Verkäufern", "die Frau Verkäufer"],
      "antwoord": 0,
      "uitleg": "Vrouwelijke beroepen krijgen de uitgang -in: 'die Verkäuferin'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'schlafen': 'Das Baby ____ schon fest.'",
      "opties": ["schläft", "schlaft", "schläfst", "schlafen"],
      "antwoord": 0,
      "uitleg": "Bij 'er/sie/es' krijgt schlafen een Umlaut: 'er schläft'."
    },
    {
      "type": "mc",
      "vraag": "Hoe zeg je in correct Duits: 'Ik wil als journalist werken'?",
      "opties": ["Ich möchte als Journalist arbeiten.", "Ich will wie ein Journalist arbeiten.", "Ich möchte als der Journalist arbeiten.", "Ich will arbeiten als einen Journalist."],
      "antwoord": 0,
      "uitleg": "In het Duits gebruik je 'als + beroep' zonder lidwoord."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Ihr ____ (rijden) sehr vorsichtig.'",
      "opties": ["fahrt", "fährt", "fahrst", "fähren"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' is er GEEN Umlaut: gewoon stam + t = 'ihr fahrt'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Ausbildung' in Duitsland?",
      "opties": ["de beroepsopleiding / het leertraject", "het eindexamen", "het basisonderwijs", "de universiteit"],
      "antwoord": 0,
      "uitleg": "'Die Ausbildung' is de beroepsopleiding in het Duitse schoolsysteem."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'tragen': 'Er ____ eine schwere Tasche.'",
      "opties": ["trägt", "tragt", "trägst", "tragen"],
      "antwoord": 0,
      "uitleg": "Bij 'er' krijgt tragen een Umlaut: 'er trägt'."
    },
    {
      "type": "mc",
      "vraag": "Welk cijfer staat in het Duitse rapport- en beoordelingssysteem voor 'sehr gut'?",
      "opties": ["1 (sehr gut)", "10 (uitmuntend)", "6 (sehr gut)", "5 (voldoende)"],
      "antwoord": 0,
      "uitleg": "In Duitsland is 1 het beste cijfer en 6 het slechtste cijfer."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je de 'g' aan het begin van 'Garten' uit?",
      "opties": ["Als een harde 'g' (zoals in good of goal)", "Als een zachte Nederlandse keelklank", "Als een 'k'", "Als een 'j'"],
      "antwoord": 0,
      "uitleg": "De Duitse g klinkt altijd als een harde g (zoals in goal)."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Bij sterke werkwoorden met a→ä krijgt 'ihr' ook een Umlaut (bijv. ihr fährt).",
      "antwoord": False,
      "uitleg": "Onwaar! De Umlaut geldt alleen voor 'du' (fährst) en 'er/sie/es' (fährt). Bij 'ihr' is het gewoon 'ihr fahrt'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het diploma 'Abitur' geeft in Duitsland toegang tot een universitaire studie.",
      "antwoord": True,
      "uitleg": "Waar! Het Abitur is het diploma van het Duitse Gymnasium."
    },
    {
      "type": "waaronwaar",
      "vraag": "De vrouwelijke vorm van 'der Arzt' is 'die Arztin' zonder Umlaut.",
      "antwoord": False,
      "uitleg": "Onwaar! Het is 'die Ärztin' (met Umlaut)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord 'laufen' krijgt bij 'er' een Umlaut: 'er läuft'.",
      "antwoord": True,
      "uitleg": "Waar! Laufen wordt 'du läufst' en 'er läuft'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'fahren' in: 'Lukas ____ jeden Morgen mit dem Fahrrad.'",
      "antwoord": "fährt",
      "uitleg": "Bij 'er' (Lukas) krijgt fahren een Umlaut: 'fährt'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'schlafen' in: '____ du am Wochenende lange?' (du)",
      "antwoord": "Schläfst",
      "uitleg": "Bij 'du' hoort 'schläfst'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Mein Bruder sucht einen (bijbaantje).' → '... einen ____.'",
      "antwoord": "Nebenjob",
      "uitleg": "Een bijbaantje is 'der Nebenjob'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de vrouwelijke beroepsnaam: 'de lerares'",
      "antwoord": "Lehrerin",
      "uitleg": "De lerares is 'die Lehrerin'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem twee sterke Duitse werkwoorden die bij 'du' en 'er/sie/es' een klinkerwisseling van a naar ä krijgen.",
      "modelantwoord": "Fahren, schlafen, tragen of waschen.",
      "sleutelwoorden": ["fahren", "schlafen", "tragen", "waschen", "laufen"],
      "minTreffers": 1,
      "uitleg": "Je kunt fahren, schlafen, tragen, waschen of laufen noemen."
    },
    {
      "type": "open",
      "vraag": "Waarvoor gebruik je het werkwoord 'studieren' in tegenstelling tot 'lernen'?",
      "modelantwoord": "Studieren gebruik je alleen voor een studie aan een hogeschool/universiteit; lernen gebruik je voor schoolwerk of woordjes leren.",
      "sleutelwoorden": ["universiteit/hogeschool", "schoolwerk/huiswerk", "hoger onderwijs"],
      "minTreffers": 1,
      "uitleg": "Studieren = hogeschool/universiteit; lernen = schoolwerk."
    }
  ]
}

# ================= EXAM 22 =================
ex22 = {
  "id": "ex-h3-duits-22",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Zukunft & Berufe",
  "titel": "Proeftoets 22 — Solliciteren, Werkplek & Sterke Werkwoorden (e→i/ie)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 5",
  "icoon": "💼",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is de betekenis van het Duitse woord 'die Bewerbung'?",
      "opties": ["de sollicitatie(brief)", "het arbeidscontract", "het ontslag", "het loonstrookje"],
      "antwoord": 0,
      "uitleg": "'Die Bewerbung' betekent de sollicitatie."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'helfen': 'Er ____ mir bei der Arbeit.'",
      "opties": ["hilft", "helft", "helfen", "hilfst"],
      "antwoord": 0,
      "uitleg": "Bij 'er' verandert de e in een i: 'er hilft'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'lesen': 'Du ____ sehr schnell.'",
      "opties": ["liest", "lest", "leset", "leest"],
      "antwoord": 0,
      "uitleg": "Bij 'du' verandert de lange e in 'ie': 'du liest'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de uitdrukking 'Geld verdienen'?",
      "opties": ["geld verdienen", "geld uitgeven", "geld sparen", "geld lenen"],
      "antwoord": 0,
      "uitleg": "'Geld verdienen' betekent geld verdienen door te werken."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'sprechen': 'Sie (zij enkelvoud) ____ fließend Deutsch.'",
      "opties": ["spricht", "sprecht", "sprechen", "sprichst"],
      "antwoord": 0,
      "uitleg": "Bij 'sie' (3e pers ev) wordt de stamklinker een i: 'sie spricht'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het cv' (curriculum vitae)?",
      "opties": ["der Lebenslauf", "die Bewerbung", "das Zeugnis", "der Abschluss"],
      "antwoord": 0,
      "uitleg": "'Der Lebenslauf' is het curriculum vitae (cv)."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'sehen': 'Lukas ____ den Chef im Büro.'",
      "opties": ["sieht", "seht", "siehst", "sehen"],
      "antwoord": 0,
      "uitleg": "Bij 'er' verandert de e in 'ie': 'er sieht'."
    },
    {
      "type": "mc",
      "vraag": "Wat houdt het 'Duale System' in Duitsland in?",
      "opties": ["Theorielessen op de Berufsschule combineren met betaalde praktijkervaring in een bedrijf.", "Twee universitaire studies tegelijk volgen.", "Een jaar werken in het buitenland.", "Online onderwijs in het weekend."],
      "antwoord": 0,
      "uitleg": "Het duaal systeem combineert beroepsonderwijs met praktijkleren."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Ihr ____ (helpen) euren Kollegen.'",
      "opties": ["helft", "hilft", "helfen", "hilfst"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' is er GEEN klinkerwisseling: 'ihr helft'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je het woordeinde '-ig' uit in 'fleißig' of 'richtig'?",
      "opties": ["Als een zachte 'ich'-klank", "Als 'ik'", "Als 'ing'", "Als 'isj'"],
      "antwoord": 0,
      "uitleg": "In het Standaardduits klinkt '-ig' aan het einde als '-ich'."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Bij het werkwoord 'geben' verandert de stam bij 'er' in 'er gibt'.",
      "antwoord": True,
      "uitleg": "Waar! Geben heeft een e→i klinkerwisseling (du gibst, er gibt)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland is cijfer 6 op school een uitmuntend resultaat.",
      "antwoord": False,
      "uitleg": "Onwaar! Cijfer 6 is het allerslechtste cijfer (ungenügend = zeer slecht)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord 'treffen' heeft bij 'du' de vorm 'du triffst'.",
      "antwoord": True,
      "uitleg": "Waar! Treffen krijgt een e→i wisseling: du triffst."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Praktikum' betekent 'het theorie-examen'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das Praktikum' is de stage."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'geben' in: 'Der Lehrer ____ den Schülern die Noten.'",
      "antwoord": "gibt",
      "uitleg": "Bij 'er' (der Lehrer) verandert de stam naar i: 'gibt'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'lesen' in: 'Er ____ gern Romane.'",
      "antwoord": "liest",
      "uitleg": "Bij 'er' verandert de e naar ie: 'liest'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Ich mache ein (stage) bei BMW.' → '... ein ____ bei BMW.'",
      "antwoord": "Praktikum",
      "uitleg": "Stage is 'das Praktikum'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Sollicitatie / sollicitatiebrief)'",
      "antwoord": "Bewerbung",
      "uitleg": "Sollicitatie is 'die Bewerbung'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat is de vervoeging van het werkwoord 'sprechen' bij de personen 'du' en 'er'?",
      "modelantwoord": "Du sprichst en er spricht.",
      "sleutelwoorden": ["sprichst", "spricht"],
      "minTreffers": 1,
      "uitleg": "Du sprichst en er spricht (met e→i klinkerwisseling)."
    },
    {
      "type": "open",
      "vraag": "Welke twee documenten stuur je traditioneel mee bij een Duitse sollicitatie?",
      "modelantwoord": "Het cv (der Lebenslauf) en de sollicitatiebrief (das Anschreiben / die Bewerbung).",
      "sleutelwoorden": ["Lebenslauf", "Bewerbung/Anschreiben", "cv"],
      "minTreffers": 1,
      "uitleg": "Der Lebenslauf en die Bewerbung."
    }
  ]
}

# ================= EXAM 23 =================
ex23 = {
  "id": "ex-h3-duits-23",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Zukunft & Berufe",
  "titel": "Proeftoets 23 — Schooltype, Universiteit & Alle Werkwoordsvormen",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 5",
  "icoon": "💼",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welk schooltype in Duitsland bereidt leerlingen rechtstreeks voor op het Gymnasium en de universiteit?",
      "opties": ["Das Gymnasium (met het Abitur)", "Die Grundschule", "Die Hauptschule", "Die Realschule"],
      "antwoord": 0,
      "uitleg": "Het Gymnasium leidt op tot het Abitur en de universiteit."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'essen': 'Er ____ jeden Tag in der Schulkantine.'",
      "opties": ["isst", "esst", "esset", "eest"],
      "antwoord": 0,
      "uitleg": "Bij 'er' verandert e in i: 'er isst'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de leraar' en 'de lerares'?",
      "opties": ["der Lehrer / die Lehrerin", "der Arzt / die Ärztin", "der Bäcker / die Bäckerin", "der Student / die Studentin"],
      "antwoord": 0,
      "uitleg": "Der Lehrer / die Lehrerin."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'waschen': 'Du ____ dein Auto.'",
      "opties": ["wäschst", "waschst", "wascht", "wäscht"],
      "antwoord": 0,
      "uitleg": "Bij 'du' krijgt waschen een Umlaut: 'du wäschst'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'der Traumberuf'?",
      "opties": ["het droomberoep", "de vakantiebaan", "het nachtwerk", "het eindexamen"],
      "antwoord": 0,
      "uitleg": "'Der Traumberuf' is het droomberoep."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Wir ____ (lezen) das Buch gemeinsam.'",
      "opties": ["lesen", "liest", "lest", "leset"],
      "antwoord": 0,
      "uitleg": "Bij 'wir' is er GEEN klinkerwisseling: 'wir lesen'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Ich interessiere mich für Sprachen und Geschichte'?",
      "opties": ["Ik interesseer me voor talen en geschiedenis.", "Ik vind wiskunde en biologie leuk.", "Ik wil leraar aardrijkskunde worden.", "Ik spreek vier verschillende talen."],
      "antwoord": 0,
      "uitleg": "'Sich interessieren für' betekent zich interesseren voor."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'treffen': 'Lukas ____ heute seine Freunde.'",
      "opties": ["trifft", "trefft", "treffen", "triffst"],
      "antwoord": 0,
      "uitleg": "Bij 'er' (Lukas) verandert e naar i: 'er trifft'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de universiteit'?",
      "opties": ["die Universität / die Uni", "die Berufsschule", "die Grundschule", "das Gymnasium"],
      "antwoord": 0,
      "uitleg": "'Die Universität' (of Uni) is de universiteit."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse schoolcijfer 'befriedigend' (cijfer 3)?",
      "opties": ["voldoende (ongeveer een 6,5 tot 7)", "uitmuntend (een 10)", "onvoldoende (een 4)", "zeer slecht (een 1)"],
      "antwoord": 0,
      "uitleg": "Cijfer 3 (befriedigend) is een normale voldoende."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'Ich möchte als Bäcker arbeiten' zonder het lidwoord 'ein'.",
      "antwoord": True,
      "uitleg": "Waar! Bij beroepen laat je het lidwoord weg na 'als'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij 'wir' krijgt het werkwoord fahren een Umlaut (wir fähren).",
      "antwoord": False,
      "uitleg": "Onwaar! Bij 'wir' blijft de stam altijd 'fahren'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De 'Berufsschule' is de vakschool binnen het Duitse beroepsonderwijs.",
      "antwoord": True,
      "uitleg": "Waar! De Berufsschule verzorgt het theoretische deel van de vakopleiding."
    },
    {
      "type": "waaronwaar",
      "vraag": "De letter 'j' in het Duitse woord 'Jahr' klinkt als de Engelse 'dj'.",
      "antwoord": False,
      "uitleg": "Onwaar! De Duitse 'j' klinkt altijd als de Nederlandse 'j' in 'jaar'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sehen' in: '____ du das Plakat an der Wand?' (du)",
      "antwoord": "Siehst",
      "uitleg": "Bij 'du' verandert e naar ie: 'siehst'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'helfen' in: 'Wer ____ mir bei dieser Aufgabe?' (er/sie)",
      "antwoord": "hilft",
      "uitleg": "Bij 3e pers ev hoort 'hilft'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De toekomst)'",
      "antwoord": "Zukunft",
      "uitleg": "De toekomst is 'die Zukunft'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De universiteit)'",
      "antwoord": "Universität",
      "uitleg": "De universiteit is 'die Universität'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem de cijferschaal van het Duitse schoolsysteem (beste cijfer en slechtste cijfer).",
      "modelantwoord": "Cijfer 1 is het beste cijfer (sehr gut) en cijfer 6 is het slechtste cijfer (ungenügend).",
      "sleutelwoorden": ["1", "6", "sehr gut", "ungenügend"],
      "minTreffers": 1,
      "uitleg": "1 is het beste cijfer en 6 is het slechtste cijfer."
    },
    {
      "type": "open",
      "vraag": "Wat is het meervoud van vrouwelijke beroepen zoals 'Lehrerin' of 'Ärztin'?",
      "modelantwoord": "Die Lehrerinnen en die Ärztinnen (met de uitgang -nen).",
      "sleutelwoorden": ["Lehrerinnen", "Ärztinnen", "-innen/-nen"],
      "minTreffers": 1,
      "uitleg": "Het meervoud eindigt op -innen (Lehrerinnen, Ärztinnen)."
    }
  ]
}

# ================= EXAM 24 =================
ex24 = {
  "id": "ex-h3-duits-24",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Zukunft & Berufe",
  "titel": "Proeftoets 24 — Carrièrekeuzes, Talen & Werkwoordvervoeging",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 5",
  "icoon": "💼",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de vraag: 'Welche Schulfächer machen dir am meisten Spaß?'",
      "opties": ["Welke schoolvakken vind je het leukst?", "Hoe laat zijn je lessen afgelopen?", "Welke cijfers heb je gehaald?", "Op welke school zit jij?"],
      "antwoord": 0,
      "uitleg": "'Schulfächer' zijn schoolvakken en 'Spaß machen' is leuk vinden."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'laufen': 'Er ____ jeden Morgen im Park.'",
      "opties": ["läuft", "lauft", "läufst", "laufen"],
      "antwoord": 0,
      "uitleg": "Bij 'er' krijgt laufen een Umlaut: 'er läuft'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de vrouwelijke vorm van 'der Polizist'?",
      "opties": ["die Polizistin", "die Polizist", "die Polizisten", "die Polizisterin"],
      "antwoord": 0,
      "uitleg": "De vrouwelijke vorm is 'die Polizistin'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'geben': 'Du ____ mir immer gute Ratschläge.'",
      "opties": ["gibst", "gebst", "giebst", "gebest"],
      "antwoord": 0,
      "uitleg": "Bij 'du' verandert e naar i: 'du gibst'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'das Gehalt'?",
      "opties": ["het salaris / maandsalaris", "de stagevergoeding", "de belasting", "het spaargeld"],
      "antwoord": 0,
      "uitleg": "'Das Gehalt' is het salaris."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Lukas ____ (lezen) sehr viele Bücher.'",
      "opties": ["liest", "lest", "leset", "leest"],
      "antwoord": 0,
      "uitleg": "Bij 'er' (Lukas) hoort 'liest'."
    },
    {
      "type": "mc",
      "vraag": "Wat is een 'Realschulabschluss' in Duitsland?",
      "opties": ["Het diploma van de Realschule (ongeveer MAVO/HAVO-onderbouw niveau)", "Het eindexamen van het Gymnasium", "Het diploma van de basisschool", "Een universitair masterdiploma"],
      "antwoord": 0,
      "uitleg": "De Realschulabschluss (Mittlere Reife) is het diploma van de Realschule."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Ihr ____ (eten) zu Mittag.'",
      "opties": ["esst", "isst", "esset", "essen"],
      "antwoord": 0,
      "uitleg": "Bij 'ihr' is er GEEN klinkerwisseling: 'ihr esst'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Er arbeitet als Informatiker bei Siemens'?",
      "opties": ["Hij werkt als IT-specialist bij Siemens.", "Hij studeert informatica aan de universiteit.", "Hij zoekt een stageplek bij Siemens.", "Zijn vader is directeur bij Siemens."],
      "antwoord": 0,
      "uitleg": "'Informatiker' is de IT-specialist / softwareontwikkelaar."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het diploma'?",
      "opties": ["das Zeugnis / der Abschluss", "die Bewerbung", "der Lebenslauf", "die Prüfung"],
      "antwoord": 0,
      "uitleg": "'Das Zeugnis' (rapport/getuigschrift) of 'der Abschluss' (diploma)."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits verandert de stamklinker van sterke werkwoorden NOOIT bij 'ich', 'wir', 'ihr' en 'sie/Sie'.",
      "antwoord": True,
      "uitleg": "Waar! De klinkerwisseling geldt uitsluitend voor 'du' en 'er/sie/es'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse schoolcijfer 4 (ausreichend) betekent dat je de toets niet hebt gehaald.",
      "antwoord": False,
      "uitleg": "Onwaar! Cijfer 4 (ausreichend) is net voldoende (een 5,5). Pas bij cijfer 5 is het onvoldoende."
    },
    {
      "type": "waaronwaar",
      "vraag": "Vrouwelijke beroepen zoals 'Lehrerin' krijgen in het meervoud de uitgang '-innen' (die Lehrerinnen).",
      "antwoord": True,
      "uitleg": "Waar! Meervoud van -in is altijd -innen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord 'studieren' gebruik je als je voor een proefwerk Duits leert.",
      "antwoord": False,
      "uitleg": "Onwaar! Daarvoor gebruik je 'lernen'. Studieren is voor universiteit/hogeschool."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'sprechen' in: '____ du auch Spanisch?' (du)",
      "antwoord": "Sprichst",
      "uitleg": "Bij 'du' hoort 'sprichst'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'schlafen' in: 'Er ____ am Sonntag bis 10 Uhr.'",
      "antwoord": "schläft",
      "uitleg": "Bij 'er' hoort 'schläft'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Het beroep)'",
      "antwoord": "Beruf",
      "uitleg": "Beroep is 'der Beruf'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Het cv / curriculum vitae)'",
      "antwoord": "Lebenslauf",
      "uitleg": "Het cv is 'der Lebenslauf'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe zeg je in het Duits dat je later arts wilt worden?",
      "modelantwoord": "Ich möchte später Arzt (of Ärztin) werden.",
      "sleutelwoorden": ["Arzt werden", "Ärztin werden", "möchte später"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'Ich möchte Arzt/Ärztin werden'."
    },
    {
      "type": "open",
      "vraag": "Wat betekent de term 'das Zeugnis' op een Duitse school?",
      "modelantwoord": "Het schoolrapport of getuigschrift/diploma.",
      "sleutelwoorden": ["rapport", "getuigschrift", "diploma"],
      "minTreffers": 1,
      "uitleg": "Das Zeugnis is het rapport of getuigschrift."
    }
  ]
}

# ================= EXAM 25 =================
ex25 = {
  "id": "ex-h3-duits-25",
  "hoofdstuk": 5,
  "hoofdstukTitel": "Zukunft & Berufe",
  "titel": "Proeftoets 25 — Eindtoets Hoofdstuk 5 (Alles gemixt)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 5",
  "icoon": "💼",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke zin met sterke werkwoorden (lezen en talen spreken) is grammaticaal helemaal correct?",
      "opties": ["Er liest gern Bücher und spricht drei Fremdsprachen.", "Er lest gern Bücher und sprecht drei Fremdsprachen.", "Er liest gern Bücher und sprechen drei Fremdsprachen.", "Er leest gern Bücher und sprichst Fremdsprachen."],
      "antwoord": 0,
      "uitleg": "'liest' (van lesen) en 'spricht' (van sprechen) met klinkerwisseling bij 'er' is correct."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'fahren': 'Mein Vater ____ jeden Tag mit dem Zug zur Arbeit.'",
      "opties": ["fährt", "fahrt", "fährst", "fahren"],
      "antwoord": 0,
      "uitleg": "Bij 'er' (mein Vater) hoort 'fährt'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de verpleegkundige' (vrouwelijk)?",
      "opties": ["die Krankenschwester / Krankenpflegerin", "die Ärztin", "die Verkäuferin", "die Polizistin"],
      "antwoord": 0,
      "uitleg": "'Die Krankenschwester' of 'Krankenpflegerin' is de verpleegster."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'geben': 'Er ____ mir seine Telefonnummer.'",
      "opties": ["gibt", "gebt", "gebest", "geben"],
      "antwoord": 0,
      "uitleg": "Bij 'er' hoort 'gibt'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'der Nebenjob'?",
      "opties": ["het bijbaantje", "het hoofdberoep", "het vrijwilligerswerk", "de stage"],
      "antwoord": 0,
      "uitleg": "'Der Nebenjob' is het bijbaantje."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'sehen': 'Siehst du den Lehrer? Ja, ich ____ ihn.'",
      "opties": ["sehe", "sieht", "siehst", "seht"],
      "antwoord": 0,
      "uitleg": "Bij 'ich' is er GEEN klinkerwisseling: 'ich sehe'."
    },
    {
      "type": "mc",
      "vraag": "Hoe vertaal je het begrip 'de toekomst' naar het Duits?",
      "opties": ["die Zukunft", "die Vergangenheit", "die Gegenwart", "das Jahr"],
      "antwoord": 0,
      "uitleg": "'Die Zukunft' is de toekomst."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'helfen': 'Du ____ mir immer so gut!'",
      "opties": ["hilfst", "helfst", "hilft", "helfen"],
      "antwoord": 0,
      "uitleg": "Bij 'du' hoort 'hilfst'."
    },
    {
      "type": "mc",
      "vraag": "Welk Duits rapportcijfer komt overeen met een 'uitmuntend' / 'sehr gut'?",
      "opties": ["1", "10", "6", "5"],
      "antwoord": 0,
      "uitleg": "In Duitsland is 1 het allerbeste cijfer (sehr gut)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'die Grundschule'?",
      "opties": ["de basisschool (groep 1 t/m 4)", "de middelbare school", "de universiteit", "de vakschool"],
      "antwoord": 0,
      "uitleg": "'Die Grundschule' is de basisschool in Duitsland."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Bij het werkwoord 'tragen' verandert de klinker bij 'er' in 'er trägt'.",
      "antwoord": True,
      "uitleg": "Waar! Tragen krijgt een Umlaut: er trägt."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitgang voor vrouwelijke beroepen in het Duits is '-er'.",
      "antwoord": False,
      "uitleg": "Onwaar! Vrouwelijke beroepen eindigen op '-in' (bijv. Lehrerin)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Abitur' is het vwo-eindexamendiploma.",
      "antwoord": True,
      "uitleg": "Waar! Het Abitur geeft toegang tot de universiteit."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je 'fertig' uit als 'fertik' met een harde k.",
      "antwoord": False,
      "uitleg": "Onwaar! In het Standaardduits klinkt '-ig' aan het einde als '-ich' (fertich)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'lesen' in: 'Lukas ____ einen spannenden Artikel.'",
      "antwoord": "liest",
      "uitleg": "Bij 'er' hoort 'liest'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'fahren' in: '____ du morgen mit nach Köln?' (du)",
      "antwoord": "Fährst",
      "uitleg": "Bij 'du' hoort 'fährst'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De stage)'",
      "antwoord": "Praktikum",
      "uitleg": "Stage is 'das Praktikum'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Het eindexamendiploma van het Gymnasium)'",
      "antwoord": "Abitur",
      "uitleg": "Het diploma is 'das Abitur'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem twee verschillende beroepen in het Duits in de mannelijke en vrouwelijke vorm.",
      "modelantwoord": "Der Lehrer / die Lehrerin en der Arzt / die Ärztin (of der Polizist / die Polizistin).",
      "sleutelwoorden": ["Lehrer / Lehrerin", "Arzt / Ärztin", "Polizist / Polizistin", "Verkäufer"],
      "minTreffers": 1,
      "uitleg": "Bijvoorbeeld Lehrer/Lehrerin en Arzt/Ärztin."
    },
    {
      "type": "open",
      "vraag": "Wat betekent het begrip 'Duales System' in het Duitse onderwijs?",
      "modelantwoord": "Leren op school (Berufsschule) combineren met betaald praktijkwerk in een bedrijf.",
      "sleutelwoorden": ["school en bedrijf", "theorie en praktijk", "Berufsschule"],
      "minTreffers": 1,
      "uitleg": "Het combineren van theorie op de vakschool met praktijkwerk bij een leerbedrijf."
    }
  ]
}

# Write H5 exams
write_exam("examen_21.js", ex21)
write_exam("examen_22.js", ex22)
write_exam("examen_23.js", ex23)
write_exam("examen_24.js", ex24)
write_exam("examen_25.js", ex25)

print("\n🎉 H5 Exams generated successfully!")
