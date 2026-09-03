#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 4 (Veranstaltungen)
Exams: examen_16.js to examen_20.js
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

# ================= EXAM 16 =================
ex16 = {
  "id": "ex-h3-duits-16",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Veranstaltungen",
  "titel": "Proeftoets 16 — Evenementen, Uitnodigingen & der/ein-Gruppe",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 4",
  "icoon": "🎪",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de uitnodiging'?",
      "opties": ["die Einladung", "die Veranstaltung", "die Feier", "der Termin"],
      "antwoord": 0,
      "uitleg": "'Die Einladung' is de uitnodiging (van einladen)."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval mannelijk): 'Ich kaufe ____ (der Rock).'",
      "opties": ["den", "der", "das", "die"],
      "antwoord": 0,
      "uitleg": "In de 4e naamval verandert het mannelijke 'der' naar 'den'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Hast du Lust, mitzukommen?'",
      "opties": ["Heb je zin om mee te gaan?", "Hoe laat kom je aan?", "Waarom ga je niet mee?", "Heb je de kaartjes al gekocht?"],
      "antwoord": 0,
      "uitleg": "'Hast du Lust mitzukommen?' is de vaste vraag om iemand uit te nodigen."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (4e naamval mannelijk): 'Lukas sucht ____ (zijn sleutel - der Schlüssel).'",
      "opties": ["seinen Schlüssel", "sein Schlüssel", "seinem Schlüssel", "seiner Schlüssel"],
      "antwoord": 0,
      "uitleg": "Schlüssel is mannelijk (der), dus lijdend voorwerp = 'seinen Schlüssel'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'das Konzert'?",
      "opties": ["het concert", "het theater", "het festival", "de bioscoop"],
      "antwoord": 0,
      "uitleg": "'Das Konzert' is het concert."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval vrouwelijk): 'Wir besuchen ____ (die Ausstellung).'",
      "opties": ["die", "der", "den", "dem"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk blijft in de 4e naamval gewoon 'die'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je 'ch' uit in het Duitse woord 'ich' of 'nicht'?",
      "opties": ["Als een zachte Ich-klank voorin de mond", "Als een harde keelklank", "Als een 'k'", "Als een 's'"],
      "antwoord": 0,
      "uitleg": "Na e, i, ä, ö, ü klinkt de ch zacht (Ich-Laut)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het juiste voorzetsel bij de datum (bijv. 'op 15 mei')?",
      "opties": ["am 15. Mai", "im 15. Mai", "um 15. Mai", "zum 15. Mai"],
      "antwoord": 0,
      "uitleg": "Bij specifieke data gebruik je 'am' (am 15. Mai)."
    },
    {
      "type": "mc",
      "vraag": "Wat vieren mensen in Duitsland op 'Silvester'?",
      "opties": ["Oudjaarsavond (31 december)", "Kerstmis (25 december)", "Pasen", "Koningsdag"],
      "antwoord": 0,
      "uitleg": "Silvester is Oudjaarsavond."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Er hat ____ (geen broer - der Bruder).'",
      "opties": ["keinen Bruder", "kein Bruder", "keine Bruder", "keinem Bruder"],
      "antwoord": 0,
      "uitleg": "Bruder is mannelijk (der Bruder), dus 4e naamval = 'keinen Bruder'."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval (Akkusativ) verandert alleen het mannelijke lidwoord (der → den / ein → einen).",
      "antwoord": True,
      "uitleg": "Waar! Vrouwelijk, onzijdig en meervoud veranderen niet in de 4e naamval."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Fest' is mannelijk (der Fest).",
      "antwoord": False,
      "uitleg": "Onwaar! Het is onzijdig: 'das Fest'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het woord 'Kuchen' en 'Buch' spreek je de 'ch' uit als de harde Ach-Laut.",
      "antwoord": True,
      "uitleg": "Waar! Na de klinkers a, o, u en au klinkt de ch als de harde keelklank."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Oktoberfest in München begint altijd pas in december.",
      "antwoord": False,
      "uitleg": "Onwaar! Het Oktoberfest begint eind september en duurt tot begin oktober."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Film): 'Wir schauen ____ Film.'",
      "antwoord": "den",
      "uitleg": "Film is mannelijk (der Film). Lijdend voorwerp = 'den Film'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van ein Hund - mannelijk): 'Er möchte ____ Hund kaufen.'",
      "antwoord": "einen",
      "uitleg": "In de 4e naamval wordt ein → 'einen'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Ich habe heute einen wichtigen (afspraak).' → '... einen wichtigen ____.'",
      "antwoord": "Termin",
      "uitleg": "Een afspraak is 'der Termin'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voorzetsel in voor kloktijden: 'Das Konzert fängt ____ 20:00 Uhr an.'",
      "antwoord": "um",
      "uitleg": "Bij kloktijden gebruik je altijd 'um'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Welke twee lidwoorden veranderen in de 4e naamval (Akkusativ) als het zelfstandig naamwoord mannelijk is?",
      "modelantwoord": "Der wordt den en ein wordt einen.",
      "sleutelwoorden": ["den", "einen"],
      "minTreffers": 1,
      "uitleg": "Der verandert in den en ein verandert in einen."
    },
    {
      "type": "open",
      "vraag": "Hoe reageer je enthousiast op een Duitse uitnodiging voor een feest?",
      "modelantwoord": "Ja gerne! Das klingt toll! (of Ich komme gerne!)",
      "sleutelwoorden": ["Ja gerne", "Das klingt toll", "Ich komme"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'Ja gerne!' of 'Das klingt toll!'."
    }
  ]
}

# ================= EXAM 17 =================
ex17 = {
  "id": "ex-h3-duits-17",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Veranstaltungen",
  "titel": "Proeftoets 17 — Festiviteiten, Feestdagen & Lidwoorden",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 4",
  "icoon": "🎪",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat houdt de mededeling 'Eintritt frei' in bij een openluchtconcert?",
      "opties": ["Gratis toegang", "Toegang verboden", "Kaartjes uitverkocht", "Alleen voor leden"],
      "antwoord": 0,
      "uitleg": "'Eintritt frei' betekent gratis toegang."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Ich sehe ____ (jouw vader - der Vater).'",
      "opties": ["deinen Vater", "dein Vater", "deinem Vater", "deiner Vater"],
      "antwoord": 0,
      "uitleg": "Vater is mannelijk (der Vater), dus lijdend voorwerp = 'deinen Vater'."
    },
    {
      "type": "mc",
      "vraag": "Hoe heet het traditionele feest van Kerstmis in het Duits?",
      "opties": ["Weihnachten", "Ostern", "Silvester", "Pfingsten"],
      "antwoord": 0,
      "uitleg": "'Weihnachten' is Kerstmis."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Sie kauft ____ (een jurk - das Kleid).'",
      "opties": ["ein Kleid", "einen Kleid", "eine Kleid", "einem Kleid"],
      "antwoord": 0,
      "uitleg": "Kleid is onzijdig (das Kleid), dus blijft 'ein Kleid'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de feestkreet 'Kölle Alaaf'?",
      "opties": ["De carnavalsgroet in Keulen", "Proost op het nieuwe jaar", "Welkom in Beieren", "Fijne kerstdagen"],
      "antwoord": 0,
      "uitleg": "'Kölle Alaaf!' is de traditionele carnavalskreet in Keulen."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Wir haben ____ (geen zin - die Lust).'",
      "opties": ["keine Lust", "keinen Lust", "kein Lust", "keinem Lust"],
      "antwoord": 0,
      "uitleg": "Lust is vrouwelijk (die Lust), dus 'keine Lust'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je de lettercombinatie '-chs' uit in 'sechs' of 'Fuchs'?",
      "opties": ["Als 'ks' / 'x'", "Als 'ch-s'", "Als 's'", "Als 'k'"],
      "antwoord": 0,
      "uitleg": "'-chs' spreek je altijd uit als 'ks' (zoals in 'zes')."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'die Feier'?",
      "opties": ["het feest / de viering", "het vuurwerk", "de vakantie", "de uitnodiging"],
      "antwoord": 0,
      "uitleg": "'Die Feier' betekent het feest of de viering."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord: 'Kennt ihr ____ (die Band)?'",
      "opties": ["die", "den", "das", "der"],
      "antwoord": 0,
      "uitleg": "Band is vrouwelijk (die Band), dus 4e naamval blijft 'die'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent 'sich treffen'?",
      "opties": ["elkaar ontmoeten / afspreken", "iets vieren", "cadeaus geven", "afscheid nemen"],
      "antwoord": 0,
      "uitleg": "'Sich treffen' betekent elkaar ontmoeten."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'Ostern' voor Pasen.",
      "antwoord": True,
      "uitleg": "Waar! Ostern is het Duitse woord voor Pasen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het onzijdige lidwoord 'das' wordt in de 4e naamval 'des'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 4e naamval blijft 'das' gewoon 'das'. 'Des' is de 2e naamval (Genitiv)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De filmfeesten in Berlijn reiken jaarlijks de 'Goldene Bär' uit.",
      "antwoord": True,
      "uitleg": "Waar! De Gouden Beer is de hoofdprijs van de Berlinale."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking 'Ich lade dich ein' betekent 'Ik wijs jou af'.",
      "antwoord": False,
      "uitleg": "Onwaar! Het betekent 'Ik nodig jou uit' (einladen)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord van de 4e naamval in voor der Kuchen: 'Lukas isst ____ leckeren Kuchen.'",
      "antwoord": "den",
      "uitleg": "Kuchen is mannelijk (der Kuchen). 4e naamval = 'den Kuchen'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste bezittelijk voornaamwoord in (4e naamval van mein Freund - mannelijk): 'Ich besuche ____ Freund.'",
      "antwoord": "meinen",
      "uitleg": "Mannelijk lijdend voorwerp = 'meinen Freund'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Wir gehen auf ein großes (concert).' → '... ein großes ____.'",
      "antwoord": "Konzert",
      "uitleg": "Concert is 'das Konzert'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het feest: '(Oud en Nieuw / Oudjaarsavond)'",
      "antwoord": "Silvester",
      "uitleg": "Oudjaarsavond is 'Silvester'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe vraag je in het Duits hoe laat een feestje of concert begint?",
      "modelantwoord": "Um wie viel Uhr fängt die Party / das Konzert an?",
      "sleutelwoorden": ["Um wie viel Uhr", "fängt an", "Wann beginnt"],
      "minTreffers": 1,
      "uitleg": "Je vraagt 'Um wie viel Uhr fängt es an?'."
    },
    {
      "type": "open",
      "vraag": "Waarom verandert het lidwoord van 'die Musik' niet in de 4e naamval?",
      "modelantwoord": "Omdat vrouwelijke woorden in de 4e naamval hetzelfde blijven als in de 1e naamval (die blijft die).",
      "sleutelwoorden": ["vrouwelijk", "blijft hetzelfde/gelijk", "die blijft die"],
      "minTreffers": 1,
      "uitleg": "Vrouwelijke zelfstandige naamwoorden behouden het lidwoord 'die' in de 4e naamval."
    }
  ]
}

# ================= EXAM 18 =================
ex18 = {
  "id": "ex-h3-duits-18",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Veranstaltungen",
  "titel": "Proeftoets 18 — Partys, Tradities & Vaste Woordgroepen",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 4",
  "icoon": "🎪",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Ich feiere meinen sechzehnten Geburtstag'?",
      "opties": ["Ik vier mijn zestiende verjaardag.", "Ik ga naar een verjaardag van zestien vrienden.", "Mijn verjaardag is over zestien dagen.", "Ik organiseer een feest voor zestien personen."],
      "antwoord": 0,
      "uitleg": "'Meinen sechzehnten Geburtstag feiern' betekent mijn zestiende verjaardag vieren."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Er sucht ____ (zijn rugzak - der Rucksack).'",
      "opties": ["seinen Rucksack", "sein Rucksack", "seinem Rucksack", "seiner Rucksack"],
      "antwoord": 0,
      "uitleg": "Rucksack is mannelijk (der Rucksack), dus 'seinen Rucksack'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'der Gutschein'?",
      "opties": ["de cadeaubon / voucher", "het entreekaartje", "de uitnodiging", "het verlanglijstje"],
      "antwoord": 0,
      "uitleg": "'Der Gutschein' is een cadeaubon of tegoedbon."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord: 'Wir organisieren ____ (das Schulfest).'",
      "opties": ["das", "den", "die", "dem"],
      "antwoord": 0,
      "uitleg": "Schulfest is onzijdig (das), dus blijft 'das Schulfest'."
    },
    {
      "type": "mc",
      "vraag": "Wat is een traditioneel product op de Duitse kerstmarkten (Weihnachtsmärkte)?",
      "opties": ["Lebkuchen und Glühwein", "Sushi und Pizza", "Ostereier", "Krapfen"],
      "antwoord": 0,
      "uitleg": "Lebkuchen (peperkoek/speculaas) en Glühwein zijn typische kerstmarktlekkernijen."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Hast du ____ (een broer - der Bruder)?'",
      "opties": ["einen Bruder", "ein Bruder", "eine Bruder", "einem Bruder"],
      "antwoord": 0,
      "uitleg": "Bruder is mannelijk (der), dus lijdend voorwerp = 'einen Bruder'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Überraschung'?",
      "opties": ["de verrassing", "de teleurstelling", "het cadeau", "de afspraak"],
      "antwoord": 0,
      "uitleg": "'Die Überraschung' betekent de verrassing."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Ich habe ____ (geen kaartje - das Ticket).'",
      "opties": ["kein Ticket", "keinen Ticket", "keine Ticket", "keinem Ticket"],
      "antwoord": 0,
      "uitleg": "Ticket is onzijdig (das Ticket), dus 'kein Ticket'."
    },
    {
      "type": "mc",
      "vraag": "Wanneer begint het carnaval traditiegetrouw in Keulen?",
      "opties": ["Op 11 november om 11:11 uur ('Elfter im Elften')", "Op 1 januari om middernacht", "Op 1 april", "Op 25 december"],
      "antwoord": 0,
      "uitleg": "Het carnavalsseizoen begint officieel op 11-11 om 11:11 uur."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het werkwoord 'absagen' bij een afspraak?",
      "opties": ["afzeggen / annuleren", "bevestigen", "verzetten", "uitnodigen"],
      "antwoord": 0,
      "uitleg": "'Absagen' betekent afzeggen."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'Herzlichen Glückwunsch zum Geburtstag!' om iemand te feliciteren met zijn verjaardag.",
      "antwoord": True,
      "uitleg": "Waar! Dit is de vaste Duitse felicitatie voor een verjaardag."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval verandert 'mein' voor een mannelijk woord naar 'meinen'.",
      "antwoord": True,
      "uitleg": "Waar! Mannelijk krijgt in de 4e naamval altijd de uitgang -en."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lettercombinatie 'ch' klinkt na de klinker 'u' als een zachte Ich-Laut.",
      "antwoord": False,
      "uitleg": "Onwaar! Na 'u' (zoals in Buch) is het de harde Ach-Laut (keelklank)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Geschenk' betekent 'de uitnodiging'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das Geschenk' betekent het cadeau / geschenk."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Pullover): 'Ich kaufe ____ Pullover.'",
      "antwoord": "den",
      "uitleg": "Pullover is mannelijk (der). Lijdend voorwerp = 'den Pullover'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste bezittelijk voornaamwoord in (4e naamval van mein Hund - mannelijk): 'Er sucht ____ Hund.'",
      "antwoord": "meinen",
      "uitleg": "Mannelijk lijdend voorwerp = 'meinen Hund'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Hier ist dein (cadeau)!' → '... dein ____!'",
      "antwoord": "Geschenk",
      "uitleg": "Cadeau is 'das Geschenk'."
    },
    {
      "type": "invul",
      "vraag": "Wat is het Duitse woord voor 'het feest'?",
      "antwoord": "Fest",
      "uitleg": "Het feest is 'das Fest' of 'die Feier'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe feliciteer je iemand in het Duits van harte met zijn verjaardag?",
      "modelantwoord": "Herzlichen Glückwunsch zum Geburtstag! (of Alles Gute zum Geburtstag!)",
      "sleutelwoorden": ["Herzlichen Glückwunsch", "Alles Gute", "Geburtstag"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'Herzlichen Glückwunsch zum Geburtstag!' of 'Alles Gute zum Geburtstag!'."
    },
    {
      "type": "open",
      "vraag": "Welke twee lidwoorden horen bij de ein-Gruppe in de 1e naamval voor mannelijk en vrouwelijk?",
      "modelantwoord": "Ein voor mannelijk en eine voor vrouwelijk.",
      "sleutelwoorden": ["ein", "eine"],
      "minTreffers": 1,
      "uitleg": "Ein (mannelijk) en eine (vrouwelijk)."
    }
  ]
}

# ================= EXAM 19 =================
ex19 = {
  "id": "ex-h3-duits-19",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Veranstaltungen",
  "titel": "Proeftoets 19 — Tijdsplanning, Locaties & Grammatica-analyse",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 4",
  "icoon": "🎪",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de aankondiging: 'Einlass ab 19:00 Uhr, Beginn um 20:00 Uhr'?",
      "opties": ["Zaal open vanaf 19:00 uur, aanvang om 20:00 uur.", "Het concert duurt van 19:00 tot 20:00 uur.", "Kaartverkoop sluit om 19:00 uur.", "Einde van het feest om 20:00 uur."],
      "antwoord": 0,
      "uitleg": "'Einlass' is de zaalopening en 'Beginn' is de aanvangstijd."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Wir brauchen ____ (een tafel - der Tisch).'",
      "opties": ["einen Tisch", "ein Tisch", "eine Tisch", "einem Tisch"],
      "antwoord": 0,
      "uitleg": "Tisch is mannelijk (der Tisch), dus lijdend voorwerp = 'einen Tisch'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de betekenis van het Duitse werkwoord 'zusagen'?",
      "opties": ["bevestigen / toezeggen dat je komt", "afzeggen", "twijfelen", "te laat komen"],
      "antwoord": 0,
      "uitleg": "'Zusagen' betekent toezeggen / je komst bevestigen."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord: 'Siehst du ____ (die Sängerin)?'",
      "opties": ["die", "den", "das", "der"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk blijft in de 4e naamval 'die'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de datum: 'vom 5. bis zum 8. August'?",
      "opties": ["van 5 tot 8 augustus", "op 5 en 8 augustus", "na 8 augustus", "voor 5 augustus"],
      "antwoord": 0,
      "uitleg": "'Vom ... bis zum ...' betekent van ... tot ... ."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Er trägt ____ (zijn jas - der Mantel).'",
      "opties": ["seinen Mantel", "sein Mantel", "seinem Mantel", "seiner Mantel"],
      "antwoord": 0,
      "uitleg": "Mantel is mannelijk (der Mantel), dus 'seinen Mantel'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'der Veranstaltungsort'?",
      "opties": ["de evenementenlocatie", "de datum van het feest", "de organisator", "de toegangsprijs"],
      "antwoord": 0,
      "uitleg": "'Der Veranstaltungsort' is de plaats waar het evenement wordt gehouden."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Ich habe ____ (geen zuster - die Schwester).'",
      "opties": ["keine Schwester", "keinen Schwester", "kein Schwester", "keinem Schwester"],
      "antwoord": 0,
      "uitleg": "Schwester is vrouwelijk (die), dus 'keine Schwester'."
    },
    {
      "type": "mc",
      "vraag": "Hoe spreek je het Duitse woord 'Wachs' uit?",
      "opties": ["Als 'vaks' (met ks-klank)", "Als 'vacht'", "Als 'vasj'", "Als 'vak'"],
      "antwoord": 0,
      "uitleg": "'-chs' spreek je altijd uit als 'ks'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Passt es dir am Freitagabend?'",
      "opties": ["Schikt het jou op vrijdagavond?", "Wat doe je op vrijdagavond?", "Ben je vrijdagavond vrij?", "Is het feest op vrijdagavond?"],
      "antwoord": 0,
      "uitleg": "'Passt es dir?' betekent schikt het jou / komt het jou uit?"
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval verandert 'kein' voor een mannelijk woord naar 'keinen'.",
      "antwoord": True,
      "uitleg": "Waar! Mannelijk lijdend voorwerp = keinen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Termin' betekent 'de einddatum'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Termin' betekent de afspraak (bijv. een doktersafspraak of meeting)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De afkorting 'VVK' op posters staat voor 'Vorverkauf' (voorverkoop).",
      "antwoord": True,
      "uitleg": "Waar! VVK = Vorverkauf."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je 'Nacht' uit met de zachte Ich-Laut.",
      "antwoord": False,
      "uitleg": "Onwaar! Na de klinker 'a' klinkt 'ch' als de harde Ach-Laut."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Computer): 'Er kauft ____ Computer.'",
      "antwoord": "den",
      "uitleg": "Computer is mannelijk (der). Lijdend voorwerp = 'den Computer'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste onbepaalde lidwoord in (4e naamval mannelijk): 'Ich habe ____ Bruder.' (ein)",
      "antwoord": "einen",
      "uitleg": "4e naamval mannelijk = 'einen Bruder'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(Locatie / plaats)' van het evenement.",
      "antwoord": "Ort",
      "uitleg": "Plaats/locatie is 'der Ort' of 'der Veranstaltungsort'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voorzetsel in voor 'van ... tot ...': '____ Montag bis Freitag.'",
      "antwoord": "von",
      "uitleg": "'von Montag bis Freitag' = van maandag tot vrijdag."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe vraag je aan iemand of vrijdag voor hem of haar schikt voor een afspraak?",
      "modelantwoord": "Passt es dir am Freitag?",
      "sleutelwoorden": ["Passt es dir", "am Freitag", "Freitag"],
      "minTreffers": 1,
      "uitleg": "Je vraagt 'Passt es dir am Freitag?'."
    },
    {
      "type": "open",
      "vraag": "Wat is het verschil in uitspraak tussen de ch in 'ich' en de ch in 'Buch'?",
      "modelantwoord": "In ich is het de zachte Ich-Laut (voorin de mond) en in Buch is het de harde Ach-Laut (keelklank).",
      "sleutelwoorden": ["zacht", "hard/keelklank", "Ich-Laut", "Ach-Laut"],
      "minTreffers": 1,
      "uitleg": "Ich = zacht voorin; Buch = harde keelklank."
    }
  ]
}

# ================= EXAM 20 =================
ex20 = {
  "id": "ex-h3-duits-20",
  "hoofdstuk": 4,
  "hoofdstukTitel": "Veranstaltungen",
  "titel": "Proeftoets 20 — Eindtoets Hoofdstuk 4 (Alles gemixt)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 4",
  "icoon": "🎪",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke zin over het verjaardagsfeest en uitnodigingen is grammaticaal helemaal correct?",
      "opties": ["Ich lade meinen besten Freund zu meiner Party ein.", "Ich lade mein besten Freund zu mein Party ein.", "Ich lade meinem besten Freund zu meinen Party ein.", "Ich lade meiner besten Freund zu der Party ein."],
      "antwoord": 0,
      "uitleg": "'meinen besten Freund' (4e nv mannelijk) en 'zu meiner Party' (3e nv vrouwelijk) is correct."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord: 'Wir besuchen ____ (das Museum).'",
      "opties": ["das", "den", "die", "dem"],
      "antwoord": 0,
      "uitleg": "Museum is onzijdig (das Museum), dus blijft 'das'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Es tut mir leid, aber ich kann leider nicht kommen'?",
      "opties": ["Het spijt me, maar ik kan helaas niet komen.", "Ik kom zeker naar je feestje toe.", "Waarom heb je me niet uitgenodigd?", "Hoe laat begint het feest ook alweer?"],
      "antwoord": 0,
      "uitleg": "Dit is de beleefde afwijzing van een uitnodiging."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (4e naamval mannelijk): 'Er sucht ____ (zijn sleutel - der Schlüssel).'",
      "opties": ["seinen Schlüssel", "sein Schlüssel", "seinem Schlüssel", "seiner Schlüssel"],
      "antwoord": 0,
      "uitleg": "Mannelijk lijdend voorwerp = 'seinen Schlüssel'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'das Fest'?",
      "opties": ["die Feste", "die Festen", "die Fester", "die Fests"],
      "antwoord": 0,
      "uitleg": "Het meervoud van das Fest is 'die Feste'."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Hast du ____ (een hond - der Hund)?'",
      "opties": ["einen Hund", "ein Hund", "eine Hund", "einem Hund"],
      "antwoord": 0,
      "uitleg": "Hund is mannelijk (der), dus 'einen Hund'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Geburtstagsparty'?",
      "opties": ["het verjaardagsfeest", "het schoolfeest", "het examenfeest", "het buurtfeest"],
      "antwoord": 0,
      "uitleg": "'Die Geburtstagsparty' is het verjaardagsfeest."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord: 'Ich kenne ____ (die Lehrerin).'",
      "opties": ["die", "den", "das", "der"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk blijft in de 4e naamval 'die'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het wereldberoemde bierfestival in München?",
      "opties": ["Das Oktoberfest", "Die Berlinale", "Der Kölner Karneval", "Das Frühlingsfest"],
      "antwoord": 0,
      "uitleg": "Het Oktoberfest in München is het grootste volksfeest ter wereld."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het voegwoord 'denn'?",
      "opties": ["want", "omdat", "hoewel", "zodra"],
      "antwoord": 0,
      "uitleg": "'Denn' betekent want en verandert de normale woordvolgorde niet."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het mannelijke lidwoord 'der' verandert in de 4e naamval naar 'den'.",
      "antwoord": True,
      "uitleg": "Waar! Der wordt den in de 4e naamval."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval verandert het vrouwelijke lidwoord 'die' naar 'der'.",
      "antwoord": False,
      "uitleg": "Onwaar! Vrouwelijk blijft 'die' in de 4e naamval. 'Der' is de 3e naamval (Dativ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitdrukking 'Ich habe keine Zeit' betekent 'Ik heb geen tijd'.",
      "antwoord": True,
      "uitleg": "Waar! Zeit is vrouwelijk (die Zeit), dus 'keine Zeit'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Einladung' betekent 'de rekening'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Einladung' is de uitnodiging. De rekening is 'die Rechnung'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval mannelijk): 'Wir besuchen ____ Park.' (der Park)",
      "antwoord": "den",
      "uitleg": "Park is mannelijk (der Park). 4e naamval = 'den Park'."
    },
    {
      "type": "invul",
      "vraag": "Vul de juiste vorm van 'kein' in (4e naamval mannelijk): 'Er hat ____ Bruder.'",
      "antwoord": "keinen",
      "uitleg": "Mannelijk lijdend voorwerp = 'keinen Bruder'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de wens: '(Gefeliciteerd)!'",
      "antwoord": "Herzlichen Glückwunsch",
      "uitleg": "Gefeliciteerd = 'Herzlichen Glückwunsch'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voorzetsel in voor kloktijden: 'Das Fest beginnt ____ 19 Uhr.'",
      "antwoord": "um",
      "uitleg": "Bij kloktijden gebruik je 'um'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem de lidwoorden van de der-Gruppe in de 4e naamval voor mannelijk, vrouwelijk en onzijdig.",
      "modelantwoord": "Mannelijk: den; vrouwelijk: die; onzijdig: das.",
      "sleutelwoorden": ["den", "die", "das"],
      "minTreffers": 1,
      "uitleg": "Den (mannelijk), die (vrouwelijk), das (onzijdig)."
    },
    {
      "type": "open",
      "vraag": "In welke stad klinkt tijdens de optocht de bekende kreet 'Kölle Alaaf' en wat wordt er gevierd?",
      "modelantwoord": "Het is de traditionele carnavalsgroet in de stad Keulen (Köln).",
      "sleutelwoorden": ["Keulen/Köln", "carnaval/carnavalsgroet"],
      "minTreffers": 1,
      "uitleg": "Dit is de carnavalsgroet in Keulen."
    }
  ]
}

# Write H4 exams
write_exam("examen_16.js", ex16)
write_exam("examen_17.js", ex17)
write_exam("examen_18.js", ex18)
write_exam("examen_19.js", ex19)
write_exam("examen_20.js", ex20)

print("\n🎉 H4 Exams generated successfully!")
