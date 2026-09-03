#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 2 (Gesundheit & Körper)
Exams: examen_6.js to examen_10.js
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

# ================= EXAM 6 =================
ex6 = {
  "id": "ex-h3-duits-6",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Gesundheit & Körper",
  "titel": "Proeftoets 6 — Lichaamsdelen, Pijn & Klachten",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 2",
  "icoon": "🩺",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het oog'?",
      "opties": ["das Auge", "das Ohr", "die Nase", "der Mund"],
      "antwoord": 0,
      "uitleg": "'Das Auge' is het oog (meervoud: die Augen)."
    },
    {
      "type": "mc",
      "vraag": "Vul het juiste persoonlijke voornaamwoord in: 'Hallo Thomas, wie geht es ____ (jou) heute?'",
      "opties": ["dir", "dich", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Bij de vaste uitdrukking 'Wie geht es...?' hoort de 3e naamval: 'dir'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de klacht: 'Mein Hals tut weh'?",
      "opties": ["Mijn keel doet pijn.", "Mijn hoofd doet pijn.", "Mijn buik doet pijn.", "Mijn rug doet pijn."],
      "antwoord": 0,
      "uitleg": "'Der Hals' is de keel of hals. 'Tut weh' = doet pijn."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van er): 'Der Arzt untersucht ____.'",
      "opties": ["ihn", "ihm", "er", "sein"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp (4e naamval) van 'er' is 'ihn'."
    },
    {
      "type": "mc",
      "vraag": "Wat wens je iemand die ziek is in het Duits?",
      "opties": ["Gute Besserung!", "Herzlichen Glückwunsch!", "Viel Erfolg!", "Schöne Ferien!"],
      "antwoord": 0,
      "uitleg": "'Gute Besserung!' betekent van harte beterschap."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval van ich): 'Kannst du ____ helfen?'",
      "opties": ["mir", "mich", "ich", "mein"],
      "antwoord": 0,
      "uitleg": "'Helfen' krijgt altijd de 3e naamval: 'mir'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'das Bein' (het been)?",
      "opties": ["die Beine", "die Beiner", "die Beinen", "die Beins"],
      "antwoord": 0,
      "uitleg": "Het meervoud van 'das Bein' is 'die Beine'."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van du): 'Ich rufe ____ heute Abend an.'",
      "opties": ["dich", "dir", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp van 'du' is 'dich'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'die Erkältung'?",
      "opties": ["de verkoudheid", "de buikgriep", "de botbreuk", "de hoofdpijn"],
      "antwoord": 0,
      "uitleg": "'Die Erkältung' betekent de verkoudheid."
    },
    {
      "type": "mc",
      "vraag": "Waar ga je in Duitsland heen om medicijnen op recept op te halen?",
      "opties": ["In die Apotheke", "In den Supermarkt", "In die Bäckerei", "In die Drogerie"],
      "antwoord": 0,
      "uitleg": "Receptgeneesmiddelen haal je in Duitsland uitsluitend bij de Apotheke."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zeg je 'Ich habe Kopfschmerzen' als je hoofdpijn hebt.",
      "antwoord": True,
      "uitleg": "Waar! 'Kopfschmerzen' betekent hoofdpijn."
    },
    {
      "type": "waaronwaar",
      "vraag": "De 4e naamval (Akkusativ) van 'wir' is 'uns'.",
      "antwoord": True,
      "uitleg": "Waar! Zowel in de 3e als 4e naamval is het voornaamwoord voor wij 'uns'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De letter 'z' in het Duitse woord 'Zahn' spreek je uit als een zachte Nederlandse 'z'.",
      "antwoord": False,
      "uitleg": "Onwaar! De Duitse 'z' spreek je altijd uit als een scherpe 'ts'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het alarmnummer voor de ambulance in Duitsland is 110.",
      "antwoord": False,
      "uitleg": "Onwaar! 110 is voor de politie; ambulance en brandweer bel je met 112."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van ich): 'Mir geht es gut, und wie geht es ____?' (du)",
      "antwoord": "dir",
      "uitleg": "De 3e naamval van 'du' is 'dir'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van ich): 'Siehst du ____?'",
      "antwoord": "mich",
      "uitleg": "Het lijdend voorwerp (4e naamval) van 'ich' is 'mich'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Mein (buik) tut weh.' → 'Mein ____ tut weh.'",
      "antwoord": "Bauch",
      "uitleg": "De buik is 'der Bauch'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Er liegt mit 39 Grad (koorts) im Bett.'",
      "antwoord": "Fieber",
      "uitleg": "Koorts is 'das Fieber'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat is het verschil in functie tussen de 4e naamval (Akkusativ) en de 3e naamval (Dativ)?",
      "modelantwoord": "De 4e naamval is het lijdend voorwerp en de 3e naamval is het meewerkend voorwerp.",
      "sleutelwoorden": ["lijdend voorwerp", "meewerkend voorwerp"],
      "minTreffers": 1,
      "uitleg": "4e naamval = lijdend voorwerp; 3e naamval = meewerkend voorwerp."
    },
    {
      "type": "open",
      "vraag": "Welke twee voornaamwoorden gebruik je voor 'hem' (als lijdend voorwerp en als meewerkend voorwerp)?",
      "modelantwoord": "Ihn voor de 4e naamval en ihm voor de 3e naamval.",
      "sleutelwoorden": ["ihn", "ihm"],
      "minTreffers": 1,
      "uitleg": "Ihn (4e nv) en ihm (3e nv)."
    }
  ]
}

# ================= EXAM 7 =================
ex7 = {
  "id": "ex-h3-duits-7",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Gesundheit & Körper",
  "titel": "Proeftoets 7 — Bij de Dokter, Ziekenhuis & Medicatie",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 2",
  "icoon": "🩺",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat vraagt de arts met de zin: 'Was fehlt Ihnen denn?'",
      "opties": ["Wat scheelt eraan? / Waar heeft u last van?", "Hoe laat heeft u een afspraak?", "Heeft u uw verzekeringspas mee?", "Wilt u een kop thee drinken?"],
      "antwoord": 0,
      "uitleg": "'Was fehlt Ihnen?' is de standaardvraag van de Duitse arts."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval van sie enkelvoud): 'Der Arzt gibt ____ ein Rezept.'",
      "opties": ["ihr", "sie", "ihn", "ihnen"],
      "antwoord": 0,
      "uitleg": "Meewerkend voorwerp (aan haar) is 'ihr'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het Duitse woord 'das Pflaster'?",
      "opties": ["de pleister", "het gips", "de rolstoel", "het verband"],
      "antwoord": 0,
      "uitleg": "'Das Pflaster' is de pleister."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van ihr): 'Wir laden ____ herzlich ein.'",
      "opties": ["euch", "ihr", "uns", "ihnen"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp van 'ihr' (jullie) is 'euch'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het ziekenhuis'?",
      "opties": ["das Krankenhaus", "die Praxis", "die Apotheke", "die Schule"],
      "antwoord": 0,
      "uitleg": "'Das Krankenhaus' is het ziekenhuis."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval van u): 'Ich danke ____ sehr für Ihre Hilfe.'",
      "opties": ["Ihnen", "Sie", "Ihr", "euch"],
      "antwoord": 0,
      "uitleg": "Bij beleefd u (Sie) is de 3e naamval 'Ihnen' (met hoofdletter)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het doktersadvies: 'Sie müssen Bettruhe halten'?",
      "opties": ["U moet in bed blijven rusten.", "U moet gaan sporten.", "U mag weer gaan werken.", "U moet veel wandelen."],
      "antwoord": 0,
      "uitleg": "'Bettruhe halten' betekent strikte bedrust houden."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval van wir): 'Das schmeckt ____ gut.'",
      "opties": ["uns", "wir", "euch", "ihnen"],
      "antwoord": 0,
      "uitleg": "De 3e naamval van 'wir' is 'uns'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'das Ohr' (het oor)?",
      "opties": ["die Ohren", "die Öhre", "die Ohre", "die Ohrsen"],
      "antwoord": 0,
      "uitleg": "Het meervoud van das Ohr is 'die Ohren'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de medische instructie: 'Vor dem Essen einnehmen'?",
      "opties": ["Innemen vóór de maaltijd.", "Innemen na de maaltijd.", "Tijdens het slapen innemen.", "Oplossen in koud water."],
      "antwoord": 0,
      "uitleg": "'Vor dem Essen' betekent vóór het eten/de maaltijd."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "De 3e naamval van 'er' (hij) is 'ihm'.",
      "antwoord": True,
      "uitleg": "Waar! De 3e naamval van er is 'ihm' (aan hem)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland schrijf je het beleefde voornaamwoord 'Ihnen' met een kleine letter.",
      "antwoord": False,
      "uitleg": "Onwaar! De beleefdheidsvormen Sie en Ihnen schrijf je altijd met een hoofdletter."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Rücken' betekent 'de buik'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Rücken' betekent de rug; de buik is 'der Bauch'."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Medikament' betekent het geneesmiddel.",
      "antwoord": True,
      "uitleg": "Waar! Das Medikament = het medicijn."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van er): 'Ich gebe ____ die Medizin.'",
      "antwoord": "ihm",
      "uitleg": "Aan hem (3e naamval) = 'ihm'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van du): 'Ich vermisse ____ sehr.'",
      "antwoord": "dich",
      "uitleg": "Lijdend voorwerp van 'du' = 'dich'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Er hat Schmerzen in der rechten (hand).' → '... in der rechten ____.'",
      "antwoord": "Hand",
      "uitleg": "De hand is 'die Hand'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Der Arzt schreibt ein (recept).' → '... ein ____.'",
      "antwoord": "Rezept",
      "uitleg": "Een doktersrecept is 'das Rezept'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe vraag je in het Duits aan een vriend hoe het met hem of haar gaat?",
      "modelantwoord": "Wie geht es dir? (of Wie geht's?)",
      "sleutelwoorden": ["Wie geht es dir", "Wie geht's", "dir"],
      "minTreffers": 1,
      "uitleg": "De vaste vraag is 'Wie geht es dir?'."
    },
    {
      "type": "open",
      "vraag": "Noem twee verschillende lichaamsdelen in het Duits die horen bij het gezicht.",
      "modelantwoord": "Die Nase, das Auge, das Ohr of der Mund.",
      "sleutelwoorden": ["Nase", "Auge", "Mund", "Ohr"],
      "minTreffers": 1,
      "uitleg": "Je kunt Nase, Auge, Ohr of Mund noemen."
    }
  ]
}

# ================= EXAM 8 =================
ex8 = {
  "id": "ex-h3-duits-8",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Gesundheit & Körper",
  "titel": "Proeftoets 8 — Gezonde Leefstijl, Sport & Voornaamwoorden",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 2",
  "icoon": "🩺",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent het advies: 'Du solltest dich mehr bewegen'?",
      "opties": ["Je zou meer moeten bewegen / sporten.", "Je moet minder slapen.", "Je mag niet meer wandelen.", "Je moet op dieet gaan."],
      "antwoord": 0,
      "uitleg": "'Sich bewegen' betekent bewegen of sportief actief zijn."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van sie enkelvoud): 'Kennst du ____?'",
      "opties": ["sie", "ihr", "ihnen", "ihn"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp van 'sie' enkelvoud blijft 'sie'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de tandarts'?",
      "opties": ["der Zahnarzt", "der Hausarzt", "der Tierarzt", "der Augenarzt"],
      "antwoord": 0,
      "uitleg": "'Der Zahnarzt' is de tandarts (der Zahn = de tand)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan: 'Das Buch gefällt ____ sehr gut.' (du / 3e naamval)",
      "opties": ["dir", "dich", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Gefallen krijgt altijd de 3e naamval: 'dir'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Ernährung'?",
      "opties": ["de voeding", "de ontspanning", "de blessure", "de training"],
      "antwoord": 0,
      "uitleg": "'Die Ernährung' betekent de voeding / het voedingspatroon."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval van ihr): 'Ich wünsche ____ viel Glück.'",
      "opties": ["euch", "ihr", "uns", "ihnen"],
      "antwoord": 0,
      "uitleg": "De 3e naamval van 'ihr' (jullie) is 'euch'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de voet'?",
      "opties": ["der Fuß", "das Bein", "der Arm", "die Hand"],
      "antwoord": 0,
      "uitleg": "'Der Fuß' is de voet (meervoud: die Füße)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (4e naamval van wir): 'Der Lehrer sieht ____ im Flur.'",
      "opties": ["uns", "wir", "euch", "ihnen"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp van 'wir' is 'uns'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Er hat sich das linke Knie verletzt'?",
      "opties": ["Hij heeft zijn linkerknie geblesseerd/bezeerd.", "Hij heeft hoofdpijn aan de linkerkant.", "Zijn rechterbeen is gebroken.", "Hij heeft pijn aan zijn schouder."],
      "antwoord": 0,
      "uitleg": "'Das Knie' is de knie en 'verletzen' is blesseren/verwonden."
    },
    {
      "type": "mc",
      "vraag": "Wat is een 'Kurort' in Duitsland?",
      "opties": ["Een officieel erkend herstel- en kuuroord met thermale baden.", "Een ziekenhuis voor spoedeisende hulp.", "Een sportacademie voor topsporters.", "Een apotheek in het centrum."],
      "antwoord": 0,
      "uitleg": "Een Kurort is een kuuroord gericht op gezondheidsherstel."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval (Dativ) is het voornaamwoord voor 'zij (meervoud)' 'ihnen'.",
      "antwoord": True,
      "uitleg": "Waar! 'ihnen' (met kleine i) betekent aan hen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'das Auge' betekent 'het oor'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das Auge' is het oog. Het oor is 'das Ohr'."
    },
    {
      "type": "waaronwaar",
      "vraag": "De uitgang voor de 4e naamval van 'ich' is 'mich'.",
      "antwoord": True,
      "uitleg": "Waar! 'mich' is het lijdend voorwerp van ich."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je de letter 's' voor een klinker uit als een scherpe 'ts'.",
      "antwoord": False,
      "uitleg": "Onwaar! De 's' voor een klinker klinkt als een zachte 'z' (zoals in Sonne). De 'z' klinkt als 'ts'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van ich): 'Das tut ____ weh.'",
      "antwoord": "mir",
      "uitleg": "Aan mij doet het pijn = 'mir'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van er): 'Ich frage ____.'",
      "antwoord": "ihn",
      "uitleg": "Lijdend voorwerp mannelijk = 'ihn'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Er öffnet den (mond).' → '... den ____.'",
      "antwoord": "Mund",
      "uitleg": "De mond is 'der Mund'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Sie nimmt dreimal täglich eine (tablet).' → '... eine ____.'",
      "antwoord": "Tablette",
      "uitleg": "Een tablet is 'die Tablette'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Welke twee Duitse werkwoorden gebruik je om aan te geven dat je ergens pijn hebt?",
      "modelantwoord": "Weh tun (tut weh) en Schmerzen haben.",
      "sleutelwoorden": ["weh tun", "Schmerzen haben", "Schmerzen"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'weh tun' of 'Schmerzen haben'."
    },
    {
      "type": "open",
      "vraag": "Wat betekent de Duitse term 'die Krankenkasse' in het zorgsysteem?",
      "modelantwoord": "De zorgverzekeraar of het ziekenfonds.",
      "sleutelwoorden": ["zorgverzekeraar", "ziekenfonds", "verzekering"],
      "minTreffers": 1,
      "uitleg": "Die Krankenkasse is de Duitse zorgverzekeraar."
    }
  ]
}

# ================= EXAM 9 =================
ex9 = {
  "id": "ex-h3-duits-9",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Gesundheit & Körper",
  "titel": "Proeftoets 9 — Diagnose, Behandeling & Grammaticatraining",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 2",
  "icoon": "🩺",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Kies de juiste combinatie voor 'aan ons' (3e naamval) en 'ons' (4e naamval):",
      "opties": ["uns en uns", "uns en euch", "wir en uns", "ihnen en uns"],
      "antwoord": 0,
      "uitleg": "Voor 'wir' is de vorm in zowel de 3e als 4e naamval 'uns'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Der Arzt misst den Blutdruck'?",
      "opties": ["De arts meet de bloeddruk.", "De arts schrijft medicijnen voor.", "De arts luistert naar de longen.", "De arts bekijkt de röntgenfoto."],
      "antwoord": 0,
      "uitleg": "'Den Blutdruck messen' betekent de bloeddruk meten."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord: 'Ich habe eine Frage an ____.' (du / 4e naamval)",
      "opties": ["dich", "dir", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Na het voorzetsel 'an' met richting/vraag hoort de 4e naamval: 'dich'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de schouder'?",
      "opties": ["die Schulter", "der Arm", "der Hals", "die Brust"],
      "antwoord": 0,
      "uitleg": "'Die Schulter' is de schouder."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval van er): 'Der Arzt verschreibt ____ Hustensaft.'",
      "opties": ["ihm", "ihn", "er", "sein"],
      "antwoord": 0,
      "uitleg": "De arts schrijft hem (meewerkend voorwerp = 3e nv) hoestdrank voor: 'ihm'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de medische term 'die Grippe'?",
      "opties": ["de griep", "de verkoudheid", "de keelontsteking", "de allergie"],
      "antwoord": 0,
      "uitleg": "'Die Grippe' is de griep (influenza)."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval van sie enkelvoud): 'Wir vertrauen ____.'",
      "opties": ["ihr", "sie", "ihn", "ihnen"],
      "antwoord": 0,
      "uitleg": "'Vertrauen' krijgt de 3e naamval: 'ihr'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de instructie: 'Gute Besserung und schone dich!'?",
      "opties": ["Beterschap en doe rustig aan / spaar jezelf!", "Veel succes met je examen!", "Ga direct weer aan het werk!", "Neem contact op met de politie!"],
      "antwoord": 0,
      "uitleg": "'Sich schonen' betekent rustig aan doen en jezelf sparen."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'die Hand'?",
      "opties": ["die Hände", "die Handen", "die Händer", "die Hands"],
      "antwoord": 0,
      "uitleg": "Het meervoud van die Hand is 'die Hände' (met Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Kannst du ____ (mij / 4e naamval) verstehen?'",
      "opties": ["mich", "mir", "ich", "mein"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp = 'mich'."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "De 3e naamval van 'du' is 'dir'.",
      "antwoord": True,
      "uitleg": "Waar! 'dir' is de 3e naamval van du."
    },
    {
      "type": "waaronwaar",
      "vraag": "In het Duits spreek je 'Husten' uit als 'hoesten' met een Nederlandse oe-klank.",
      "antwoord": False,
      "uitleg": "Onwaar! De 'u' in Husten spreek je uit als een 'oe'-klank (zoals in 'koe')."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'die Nase' betekent 'de mond'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Die Nase' is de neus. De mond is 'der Mund'."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin 'Ich helfe dir' is 'dir' het meewerkend voorwerp in de 3e naamval.",
      "antwoord": True,
      "uitleg": "Waar! Helfen vereist altijd de 3e naamval (dir)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van ihr): 'Ich habe ____ gestern gesehen.'",
      "antwoord": "euch",
      "uitleg": "Lijdend voorwerp van ihr (jullie) = 'euch'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van u): 'Wie kann ich ____ helfen?'",
      "antwoord": "Ihnen",
      "uitleg": "Beleefde 3e naamval = 'Ihnen'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Mein (rug) tut weh.' → 'Mein ____ tut weh.'",
      "antwoord": "Rücken",
      "uitleg": "De rug is 'der Rücken'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord tussen haakjes: 'Er hustet stark und hat starken (hoest).' → '... starken ____.'",
      "antwoord": "Husten",
      "uitleg": "Hoest is 'der Husten'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe zeg je in het Duits dat je je helemaal niet lekker voelt?",
      "modelantwoord": "Ich fühle mich gar nicht wohl (of mir ist schlecht).",
      "sleutelwoorden": ["fühle mich", "nicht wohl", "schlecht"],
      "minTreffers": 1,
      "uitleg": "Je gebruikt 'Ich fühle mich nicht wohl' of 'Mir ist schlecht'."
    },
    {
      "type": "open",
      "vraag": "Wat is het meervoud van 'das Auge' (het oog) in het Duits?",
      "modelantwoord": "Die Augen.",
      "sleutelwoorden": ["Augen", "die Augen"],
      "minTreffers": 1,
      "uitleg": "Het meervoud is 'die Augen'."
    }
  ]
}

# ================= EXAM 10 =================
ex10 = {
  "id": "ex-h3-duits-10",
  "hoofdstuk": 2,
  "hoofdstukTitel": "Gesundheit & Körper",
  "titel": "Proeftoets 10 — Eindtoets Hoofdstuk 2 (Alles gemixt)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 2",
  "icoon": "🩺",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Welke zin over het doktersbezoek is grammaticaal helemaal correct?",
      "opties": ["Der Arzt hilft mir und untersucht meinen Bauch.", "Der Arzt hilft mich und untersucht mein Bauch.", "Der Arzt helfe mir und untersucht meiner Bauch.", "Der Arzt hilft dir und untersuche den Bauch."],
      "antwoord": 0,
      "uitleg": "'hilft mir' (3e nv) en 'untersucht meinen Bauch' (4e nv mannelijk) is correct."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (3e naamval van ich): 'Es geht ____ heute viel besser.'",
      "opties": ["mir", "mich", "ich", "mein"],
      "antwoord": 0,
      "uitleg": "Bij 'Es geht...' hoort de 3e naamval: 'mir'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Er hat sich den Arm gebrochen'?",
      "opties": ["Hij heeft zijn arm gebroken.", "Hij heeft spierpijn in zijn arm.", "Zijn been zit in het gips.", "Hij heeft een wond aan zijn hand."],
      "antwoord": 0,
      "uitleg": "'Den Arm brechen' betekent de arm breken."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van er): 'Kennst du ____ schon lange?'",
      "opties": ["ihn", "ihm", "er", "sein"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp mannelijk = 'ihn'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het alarmnummer voor de politie in Duitsland?",
      "opties": ["110", "112", "911", "100"],
      "antwoord": 0,
      "uitleg": "Het politienummer is 110."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval van sie meervoud): 'Ich schenke ____ Blumen.'",
      "opties": ["ihnen", "sie", "ihr", "euch"],
      "antwoord": 0,
      "uitleg": "Meewerkend voorwerp meervoud (aan hen) = 'ihnen'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Notaufnahme' in een ziekenhuis?",
      "opties": ["De eerste hulp / spoedeisende hulp (SEH)", "De receptie voor bezoekers", "Het laboratorium voor bloedonderzoek", "De apotheek op de begane grond"],
      "antwoord": 0,
      "uitleg": "'Die Notaufnahme' is de spoedeisende hulp."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste voornaamwoord (4e naamval van du): 'Ich liebe ____.'",
      "opties": ["dich", "dir", "du", "dein"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp van du = 'dich'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de tanden'?",
      "opties": ["die Zähne", "die Zahnen", "die Zähner", "die Zahns"],
      "antwoord": 0,
      "uitleg": "Het meervoud van der Zahn is 'die Zähne'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de doktersinstructie: 'Nehmen Sie die Tropfen dreimal täglich'?",
      "opties": ["Neem de druppels driemaal per dag.", "Drink drie glazen water per dag.", "Blijf drie dagen thuis.", "Kom over drie weken terug."],
      "antwoord": 0,
      "uitleg": "'Die Tropfen' zijn druppels en 'dreimal täglich' is driemaal per dag."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Hals' betekent zowel 'keel' als 'hals'.",
      "antwoord": True,
      "uitleg": "Waar! Der Hals wordt voor zowel de keel (Halsschmerzen) als de hals gebruikt."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval verandert 'sie' (zij enkelvoud) naar 'ihr'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 4e naamval blijft het 'sie'. 'ihr' is de 3e naamval."
    },
    {
      "type": "waaronwaar",
      "vraag": "De letter 'ß' (Eszett) klinkt als een scherpe 's'-klank.",
      "antwoord": True,
      "uitleg": "Waar! De Eszett is altijd een stemloze scherpe s."
    },
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland kun je antibiotica zonder recept in de supermarkt kopen.",
      "antwoord": False,
      "uitleg": "Onwaar! Medicijnen zijn alleen verkrijgbaar bij de apotheek op doktersrecept."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (3e naamval van du): 'Ich danke ____ herzlich.'",
      "antwoord": "dir",
      "uitleg": "Danken krijgt de 3e naamval: 'dir'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste voornaamwoord in (4e naamval van ich): 'Er ruft ____ an.'",
      "antwoord": "mich",
      "uitleg": "Lijdend voorwerp van ich = 'mich'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het lichaamsdeel naar het Duits: 'Er hat sich das rechte (been) verletzt.' → '... das rechte ____.'",
      "antwoord": "Bein",
      "uitleg": "Het been is 'das Bein'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de wens: '(Beterschap)!'",
      "antwoord": "Gute Besserung",
      "uitleg": "Beterschap = 'Gute Besserung'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat zijn de twee Duitse noodnummers en waarvoor bel je elk nummer?",
      "modelantwoord": "112 voor ambulance en brandweer; 110 voor de politie.",
      "sleutelwoorden": ["112", "110", "Polizei", "Feuerwehr"],
      "minTreffers": 1,
      "uitleg": "112 voor brandweer/ambulance en 110 voor politie."
    },
    {
      "type": "open",
      "vraag": "Welke vorm heeft het persoonlijk voornaamwoord 'wij' in de 1e, 3e en 4e naamval?",
      "modelantwoord": "1e naamval: wir; 3e naamval: uns; 4e naamval: uns.",
      "sleutelwoorden": ["wir", "uns"],
      "minTreffers": 1,
      "uitleg": "Wir (1e nv) en uns (3e en 4e nv)."
    }
  ]
}

# Write H2 exams
write_exam("examen_6.js", ex6)
write_exam("examen_7.js", ex7)
write_exam("examen_8.js", ex8)
write_exam("examen_9.js", ex9)
write_exam("examen_10.js", ex10)

print("\n🎉 H2 Exams generated successfully!")
