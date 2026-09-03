#!/usr/bin/env python3
"""
Generates 5 Full Exams (20 questions each = 100 questions) for Duits HAVO 3 Hoofdstuk 6 (In Aktion)
Exams: examen_26.js to examen_30.js
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

# ================= EXAM 26 =================
ex26 = {
  "id": "ex-h3-duits-26",
  "hoofdstuk": 6,
  "hoofdstukTitel": "In Aktion",
  "titel": "Proeftoets 26 — Hulpdiensten, Noodgevallen & Het 3-Naamvallensysteem",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 6",
  "icoon": "🚑",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Hoe noem je de hulpdienst die branden blust in het Duits?",
      "opties": ["die Feuerwehr", "die Polizei", "der Rettungsdienst", "das Krankenhaus"],
      "antwoord": 0,
      "uitleg": "'Die Feuerwehr' is de brandweer."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval mannelijk): 'Der Feuerwehrmann hilft ____ (der Mann).'",
      "opties": ["dem", "den", "der", "des"],
      "antwoord": 0,
      "uitleg": "Helfen krijgt de 3e naamval: 'dem Mann'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'ehrenamtlich' in Duitsland?",
      "opties": ["vrijwillig / als vrijwilliger", "betaald overwerk", "in overheidsdienst", "als parttime baan"],
      "antwoord": 0,
      "uitleg": "'Ehrenamtlich' betekent vrijwilligerswerk doen."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval mannelijk): 'Die Polizei sucht ____ (der Zeuge).'",
      "opties": ["den", "dem", "der", "die"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp mannelijk = 'den Zeugen'."
    },
    {
      "type": "mc",
      "vraag": "Welk alarmnummer toets je in Duitsland in als je dringend de politie nodig hebt?",
      "opties": ["110", "112", "911", "100"],
      "antwoord": 0,
      "uitleg": "Politie is 110 (brandweer/ambulance is 112)."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval vrouwelijk): 'Ich danke ____ (die Ärztin).' (die → ...)",
      "opties": ["der", "die", "den", "dem"],
      "antwoord": 0,
      "uitleg": "In de 3e naamval (Dativ) verandert 'die' in 'der'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Es gab einen schweren Unfall'?",
      "opties": ["Er was een zwaar ongeluk.", "Er was een grote brand.", "Er was een overstroming.", "Er was een zware storm."],
      "antwoord": 0,
      "uitleg": "'Der Unfall' betekent het ongeluk."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval onzijdig): 'Der Polizist hilft ____ (das Kind).'",
      "opties": ["dem", "das", "den", "der"],
      "antwoord": 0,
      "uitleg": "Onzijdig in de 3e naamval = 'dem Kind'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Technisches Hilfswerk (THW)?",
      "opties": ["De Duitse federale rampenbestrijdingsdienst met blauwe wagens.", "Een particuliere beveiligingsdienst.", "De Duitse grensbewaking.", "Een autoclub voor pechhulp."],
      "antwoord": 0,
      "uitleg": "Het THW is de federale civiele beschermings- en rampendienst."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval onzijdig): 'Die Helfer retten ____ (das Kind).'",
      "opties": ["das", "den", "dem", "der"],
      "antwoord": 0,
      "uitleg": "Onzijdig blijft in de 4e naamval gewoon 'das'."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval (Dativ) krijgen zowel mannelijke als onzijdige woorden het lidwoord 'dem'.",
      "antwoord": True,
      "uitleg": "Waar! Mannelijk en onzijdig zijn in de 3e naamval beide 'dem' (einem)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bijna 99% van de medewerkers van het Duitse THW werkt als vrijwilliger.",
      "antwoord": True,
      "uitleg": "Waar! Het THW draait vrijwel geheel op vrijwillige inzet."
    },
    {
      "type": "waaronwaar",
      "vraag": "De Duitse term 'der Unfall' betekent 'de sportieve overwinning'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Der Unfall' betekent het ongeluk."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval verandert het lidwoord van 'die Frau' naar 'den Frau'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 3e naamval wordt vrouwelijk 'der Frau' (einer Frau)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (3e naamval van der Fahrer): 'Die Polizei hilft ____ Fahrer.'",
      "antwoord": "dem",
      "uitleg": "3e naamval mannelijk = 'dem Fahrer'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Verletzte): 'Die Sanitäter tragen ____ Verletzten.'",
      "antwoord": "den",
      "uitleg": "4e naamval mannelijk = 'den'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de naam van de blusdienst: '(De brandweer)'",
      "antwoord": "Feuerwehr",
      "uitleg": "De brandweer is 'die Feuerwehr'."
    },
    {
      "type": "invul",
      "vraag": "Wat is het alarmnummer voor de ambulance en brandweer in Duitsland?",
      "antwoord": "112",
      "uitleg": "Het alarmnummer is 112."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem de lidwoorden van de der-Gruppe in de 3e naamval (Dativ) voor mannelijk, vrouwelijk en onzijdig.",
      "modelantwoord": "Mannelijk: dem; vrouwelijk: der; onzijdig: dem.",
      "sleutelwoorden": ["dem", "der", "dem"],
      "minTreffers": 1,
      "uitleg": "Dem (mannelijk), der (vrouwelijk), dem (onzijdig)."
    },
    {
      "type": "open",
      "vraag": "Welke 5 W-vragen stel je bij het melden van een noodgeval via 112?",
      "modelantwoord": "Wo? Was? Wie viele? Welche Verletzungen? Warten auf Rückfragen!",
      "sleutelwoorden": ["Wo", "Was", "Wie viele", "Warten"],
      "minTreffers": 1,
      "uitleg": "Wo, Was, Wie viele, Welche, Warten."
    }
  ]
}

# ================= EXAM 27 =================
ex27 = {
  "id": "ex-h3-duits-27",
  "hoofdstuk": 6,
  "hoofdstukTitel": "In Aktion",
  "titel": "Proeftoets 27 — Eerste Hulp, Vrijwilligerswerk & Naamvallenoverzicht",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 6",
  "icoon": "🚑",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de kreet: 'Hilfe! Rufen Sie sofort einen Krankenwagen!'?",
      "opties": ["Help! Bel direct een ambulance!", "Help! De politie is onderweg!", "Pas op voor de brandweer!", "Waar is het dichtstbijzijnde ziekenhuis?"],
      "antwoord": 0,
      "uitleg": "'Einen Krankenwagen rufen' betekent een ambulance bellen."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval meervoud): 'Wir danken ____ (die Helfer - meervoud).'",
      "opties": ["den", "die", "der", "dem"],
      "antwoord": 0,
      "uitleg": "Meervoud in de 3e naamval krijgt het lidwoord 'den' (+n aan het zelfstandig naamwoord)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'het goede doel / de hulporganisatie'?",
      "opties": ["die Hilfsorganisation / die Spendenorganisation", "die Firma", "die Behörde", "das Ministerium"],
      "antwoord": 0,
      "uitleg": "'Die Hilfsorganisation' is de hulporganisatie."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval vrouwelijk): 'Die Feuerwehr löscht ____ (die Flamme).'",
      "opties": ["die", "den", "der", "dem"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk blijft in de 4e naamval 'die'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het werkwoord 'spenden'?",
      "opties": ["doneren / geld schenken aan een goed doel", "sparen op de bank", "lenen van een vriend", "investeren in aandelen"],
      "antwoord": 0,
      "uitleg": "'Spenden' betekent geld of goederen doneren."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval mannelijk): 'Er gibt ____ (ein Polizist) seinen Ausweis.'",
      "opties": ["einem Polizisten", "einen Polizisten", "einer Polizist", "ein Polizist"],
      "antwoord": 0,
      "uitleg": "3e naamval mannelijk van ein = 'einem'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Die Rettungskräfte sind vor Ort eingetroffen'?",
      "opties": ["De hulpdiensten zijn ter plaatse aangekomen.", "De politie zoekt naar getuigen.", "Het ongeval is voorbij.", "De ambulance staat in de file."],
      "antwoord": 0,
      "uitleg": "'Vor Ort eintreffen' betekent ter plaatse arriveren."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval mannelijk): 'Wir rufen ____ (der Notarzt).'",
      "opties": ["den", "dem", "der", "die"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp mannelijk = 'den Notarzt'."
    },
    {
      "type": "mc",
      "vraag": "Op welke manier spreek je de Duitse plofklanken 'p', 't' en 'k' uit?",
      "opties": ["Geaspireerd (met een lichte ademstoot/h-klank)", "Volledig stemhebbend zoals b/d/g", "Zacht en onhoorbaar", "Als nasale klanken"],
      "antwoord": 0,
      "uitleg": "De Duitse plofklanken p, t en k zijn geaspireerd (met ademstoot)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'die Umwelt schützen'?",
      "opties": ["het milieu beschermen", "het weer voorspellen", "in de natuur wandelen", "bomen kappen"],
      "antwoord": 0,
      "uitleg": "'Die Umwelt schützen' betekent het milieu beschermen."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse Rode Kruis heet 'DRK' (Deutsches Rotes Kreuz).",
      "antwoord": True,
      "uitleg": "Waar! DRK staat voor Deutsches Rotes Kreuz."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval meervoud krijgt het lidwoord de vorm 'der'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 3e naamval meervoud is het lidwoord 'den' (den Kindern)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het werkwoord 'retten' betekent 'redden'.",
      "antwoord": True,
      "uitleg": "Waar! Retten = redden."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het alarmnummer 112 is in heel Duitsland gratis bereikbaar vanaf mobiel en vast netwerk.",
      "antwoord": True,
      "uitleg": "Waar! 112 is overal gratis bereikbaar."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (3e naamval van die Frau): 'Der Sanitäter hilft ____ Frau.'",
      "antwoord": "der",
      "uitleg": "Vrouwelijk in de 3e naamval = 'der'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Hund): 'Die Feuerwehr rettet ____ Hund.'",
      "antwoord": "den",
      "uitleg": "Mannelijk lijdend voorwerp = 'den'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De ambulance / ziekenwagen)'",
      "antwoord": "Krankenwagen",
      "uitleg": "Ambulance is 'der Krankenwagen' of 'der Rettungswagen'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het werkwoord 'redden' naar het Duits: 'Wir wollen Menschen ____.'",
      "antwoord": "retten",
      "uitleg": "Redden is 'retten'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat is het meervoudslidwoord in de 1e, 3e en 4e naamval in het Duits?",
      "modelantwoord": "1e naamval: die; 3e naamval: den; 4e naamval: die.",
      "sleutelwoorden": ["die", "den", "die"],
      "minTreffers": 1,
      "uitleg": "Die (1e nv), den (3e nv), die (4e nv)."
    },
    {
      "type": "open",
      "vraag": "Wat betekent de afkorting 'DRK' in Duitsland?",
      "modelantwoord": "Deutsches Rotes Kreuz (Duitse Rode Kruis).",
      "sleutelwoorden": ["Deutsches Rotes Kreuz", "Rode Kruis"],
      "minTreffers": 1,
      "uitleg": "Het Deutsches Rotes Kreuz."
    }
  ]
}

# ================= EXAM 28 =================
ex28 = {
  "id": "ex-h3-duits-28",
  "hoofdstuk": 6,
  "hoofdstukTitel": "In Aktion",
  "titel": "Proeftoets 28 — Brandbestrijding, THW & Naamvalstoepassingen",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 6",
  "icoon": "🚑",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Die Feuerwehr löschte den Brand in wenigen Minuten'?",
      "opties": ["De brandweer bluste de brand in enkele minuten.", "De brandweer kwam na enkele minuten aan.", "De brand breidde zich in enkele minuten uit.", "Het vuur laaide na enkele minuten weer op."],
      "antwoord": 0,
      "uitleg": "'Löschen' is blussen en 'der Brand' is de brand."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval van das Kind): 'Die Polizistin gibt ____ Kind einen Teddybären.'",
      "opties": ["dem", "das", "den", "der"],
      "antwoord": 0,
      "uitleg": "3e naamval onzijdig = 'dem Kind'."
    },
    {
      "type": "mc",
      "vraag": "Wat is een 'Freiwillige Feuerwehr' in Duitsland?",
      "opties": ["Een vrijwillig brandweerkorps bestaande uit getrainde dorpsbewoners/burgers.", "Een brandweeracademie voor studenten.", "Een museum over historische brandspuiten.", "Een particuliere verzekeringsmaatschappij."],
      "antwoord": 0,
      "uitleg": "In de meeste Duitse gemeenten draait de brandweer op vrijwillige burgers."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval mannelijk): 'Der Rettungswagen bringt ____ (der Patient) ins Krankenhaus.'",
      "opties": ["den", "dem", "der", "die"],
      "antwoord": 0,
      "uitleg": "Lijdend voorwerp mannelijk = 'den Patienten'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Ursache' van een brand?",
      "opties": ["de oorzaak", "de schade", "het gevolg", "de melder"],
      "antwoord": 0,
      "uitleg": "'Die Ursache' betekent de oorzaak."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (3e naamval mannelijk): 'Wir danken ____ (unser Lehrer) für die Unterstützung.'",
      "opties": ["unserem Lehrer", "unseren Lehrer", "unser Lehrer", "unserer Lehrer"],
      "antwoord": 0,
      "uitleg": "3e naamval mannelijk = 'unserem Lehrer'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent het woord 'der Rauch' bij een brand?",
      "opties": ["de rook", "de as", "het vuur", "het bluswater"],
      "antwoord": 0,
      "uitleg": "'Der Rauch' is de rook."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (4e naamval vrouwelijk): 'Die Organisation schützt ____ (die Natur).'",
      "opties": ["die", "den", "der", "dem"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk blijft in de 4e naamval 'die'."
    },
    {
      "type": "mc",
      "vraag": "Wat is de kleur van de hulpverleningsvoertuigen van het THW?",
      "opties": ["Blauw met witte belettering", "Rood met gele strepen", "Groen met zilver", "Geel met rood"],
      "antwoord": 0,
      "uitleg": "THW-voertuigen zijn traditioneel felblauw."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent 'Erste Hilfe leisten'?",
      "opties": ["Eerste hulp verlenen (EHBO)", "Een noodoproep plaatsen", "Naar de dokter gaan", "Geld doneren"],
      "antwoord": 0,
      "uitleg": "'Erste Hilfe leisten' is EHBO/eerste hulp verlenen."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Brand' betekent 'de brand'.",
      "antwoord": True,
      "uitleg": "Waar! Der Brand = de brand."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 3e naamval krijgt 'ein' voor een onzijdig woord de vorm 'einen'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 3e naamval is het 'einem' (einem Kind). 'Einen' is de 4e naamval mannelijk."
    },
    {
      "type": "waaronwaar",
      "vraag": "De plofklank 't' in het Duitse woord 'Tag' spreek je uit met een lichte ademstoot.",
      "antwoord": True,
      "uitleg": "Waar! De Duitse 't' is geaspireerd (klinkt als t-h-ag)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De term 'Sachschaden' betekent het aantal gewonde mensen.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Sachschaden' is materiële zaakschade aan gebouwen of auto's."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (3e naamval van der Fahrer): 'Die Helfer bringen ____ Fahrer Wasser.'",
      "antwoord": "dem",
      "uitleg": "3e naamval mannelijk = 'dem'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van die Straße): 'Die Polizei sperrt ____ Straße ab.'",
      "antwoord": "die",
      "uitleg": "Vrouwelijk in de 4e naamval = 'die'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De rook)'",
      "antwoord": "Rauch",
      "uitleg": "De rook is 'der Rauch'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het werkwoord 'blussen': 'Die Feuerwehr muss das Feuer ____.'",
      "antwoord": "löschen",
      "uitleg": "Blussen is 'löschen'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Hoe zeg je in het Duits dat niemand gewond is geraakt bij een ongeluk?",
      "modelantwoord": "Niemand wurde verletzt (of Niemand ist verletzt).",
      "sleutelwoorden": ["Niemand wurde verletzt", "Niemand ist verletzt", "verletzt"],
      "minTreffers": 1,
      "uitleg": "Je zegt 'Niemand wurde verletzt'."
    },
    {
      "type": "open",
      "vraag": "Wat is het verschil in lidwoord in de 3e naamval tussen een mannelijk woord (der Mann) en een vrouwelijk woord (die Frau)?",
      "modelantwoord": "Mannelijk wordt 'dem Mann' en vrouwelijk wordt 'der Frau'.",
      "sleutelwoorden": ["dem", "der"],
      "minTreffers": 1,
      "uitleg": "Dem Mann (mannelijk) en der Frau (vrouwelijk)."
    }
  ]
}

# ================= EXAM 29 =================
ex29 = {
  "id": "ex-h3-duits-29",
  "hoofdstuk": 6,
  "hoofdstukTitel": "In Aktion",
  "titel": "Proeftoets 29 — Maatschappelijke Betrokkenheid & Grammaticale Analyse",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 6",
  "icoon": "🚑",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "In de zin 'Der Junge hilft dem alten Mann' is 'dem alten Mann':",
      "opties": ["Meewerkend voorwerp (3e naamval - Dativ)", "Lijdend voorwerp (4e naamval - Akkusativ)", "Onderwerp (1e naamval - Nominativ)", "Bijvoeglijke bepaling"],
      "antwoord": 0,
      "uitleg": "'Helfen' vereist altijd het meewerkend voorwerp in de 3e naamval (dem Mann)."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de zin: 'Sie engagiert sich für den Tierschutz'?",
      "opties": ["Zij zet zich in voor de dierenbescherming.", "Zij heeft een hond gekocht.", "Zij werkt als dierenarts in de dierentuin.", "Zij spaart voor een nieuw huisdier."],
      "antwoord": 0,
      "uitleg": "'Sich engagieren für' betekent zich inzetten voor."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval vrouwelijk): 'Ich danke ____ (die Mutter) für das Essen.'",
      "opties": ["der", "die", "den", "dem"],
      "antwoord": 0,
      "uitleg": "In de 3e naamval wordt die → 'der Mutter'."
    },
    {
      "type": "mc",
      "vraag": "Vul aan (4e naamval mannelijk): 'Wir haben ____ (een zwerfhond - ein Hund) gefunden.'",
      "opties": ["einen Hund", "ein Hund", "einem Hund", "einer Hund"],
      "antwoord": 0,
      "uitleg": "4e naamval mannelijk = 'einen Hund'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het Duitse woord voor 'de vrijwilliger'?",
      "opties": ["der Freiwillige / die Freiwillige", "der Angestellte", "der Arbeiter", "der Beamte"],
      "antwoord": 0,
      "uitleg": "'Der Freiwillige' is de vrijwilliger."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval meervoud): 'Der Bürgermeister dankt ____ (die Bürger - meervoud).'",
      "opties": ["den", "die", "der", "dem"],
      "antwoord": 0,
      "uitleg": "3e naamval meervoud = 'den Bürgern'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de oproep: 'Wir sammeln Spenden für das Kinderheim'?",
      "opties": ["We zamelen donaties / geld in voor het kindertehuis.", "We organiseren een kinderfeestje.", "We bouwen een nieuwe speeltuin.", "We adopteren een kind."],
      "antwoord": 0,
      "uitleg": "'Spenden sammeln' betekent donaties inzamelen."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (1e naamval onderwerp onzijdig): '____ (het kind) ruft um Hilfe.'",
      "opties": ["Das", "Dem", "Den", "Die"],
      "antwoord": 0,
      "uitleg": "Onderwerp onzijdig in de 1e naamval is gewoon 'Das Kind'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'die Rettungsgasse' op de Duitse snelweg?",
      "opties": ["De vrije doorgangsstrook tussen twee rijstroken voor ambulances en brandweer bij file.", "De vluchtstrook voor pechgevallen.", "De afrit naar het ziekenhuis.", "De busbaan in de stad."],
      "antwoord": 0,
      "uitleg": "Een Rettungsgasse is de verplichte vrije noodcorridor bij filevorming op de Autobahn."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm: 'Der Polizist hilft ____ (mij / 3e naamval).'",
      "opties": ["mir", "mich", "ich", "mein"],
      "antwoord": 0,
      "uitleg": "Meewerkend voorwerp bij helfen = 'mir'."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In Duitsland zijn automobilisten bij filevorming wettelijk verplicht om een 'Rettungsgasse' te vormen.",
      "antwoord": True,
      "uitleg": "Waar! Bij file moet tussen de linker- en middelste rijstrook altijd een Rettungsgasse vrijgemaakt worden."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de zin 'Ich sehe den Hund' staat 'den Hund' in de 3e naamval.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Den Hund' is het lijdend voorwerp (wie zie ik?), dus de 4e naamval (Akkusativ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het Duitse woord 'der Tierschutz' betekent de bescherming van dieren.",
      "antwoord": True,
      "uitleg": "Waar! Der Tierschutz = dierenbescherming."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het lidwoord 'das' verandert in de 3e naamval naar 'den'.",
      "antwoord": False,
      "uitleg": "Onwaar! In de 3e naamval wordt onzijdig 'dem' (dem Kind)."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (3e naamval van der Polizist): 'Der Zeuge antwortet ____ Polizisten.'",
      "antwoord": "dem",
      "uitleg": "Antworten krijgt de 3e naamval: 'dem'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval van der Ausweis): 'Zeigen Sie bitte ____ Ausweis.'",
      "antwoord": "den",
      "uitleg": "Ausweis is mannelijk (der Ausweis). Lijdend voorwerp = 'den Ausweis'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De vrijwilliger)'",
      "antwoord": "Freiwillige",
      "uitleg": "Vrijwilliger is 'der Freiwillige'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De noodoproep)'",
      "antwoord": "Notruf",
      "uitleg": "Noodoproep is 'der Notruf'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Wat is een 'Rettungsgasse' op de Duitse snelweg en waarvoor dient deze?",
      "modelantwoord": "Een vrije doorgang tussen rijstroken bij file zodat hulpdiensten (ambulance/brandweer) er snel door kunnen.",
      "sleutelwoorden": ["vrije doorgang", "hulpdiensten/ambulance", "file"],
      "minTreffers": 1,
      "uitleg": "Een vrije doorgangsstrook voor hulpdiensten bij file."
    },
    {
      "type": "open",
      "vraag": "Welke lidwoorden van de ein-Gruppe horen bij de 3e naamval voor mannelijk en vrouwelijk?",
      "modelantwoord": "Einem voor mannelijk en einer voor vrouwelijk.",
      "sleutelwoorden": ["einem", "einer"],
      "minTreffers": 1,
      "uitleg": "Einem (mannelijk) en einer (vrouwelijk)."
    }
  ]
}

# ================= EXAM 30 =================
ex30 = {
  "id": "ex-h3-duits-30",
  "hoofdstuk": 6,
  "hoofdstukTitel": "In Aktion",
  "titel": "Proeftoets 30 — Grote Eindexamentoets Duits 3 HAVO (Compleet Overzicht)",
  "duurMin": 20,
  "vak": "Duits HAVO 3 — Hoofdstuk 6",
  "icoon": "🚑",
  "vragen": [
    # 10 MC
    {
      "type": "mc",
      "vraag": "In de zin 'Der Feuerwehrmann gibt dem Kind einen Teddybären' staat 'einen Teddybären' in de:",
      "opties": ["4e naamval (Akkusativ - lijdend voorwerp)", "3e naamval (Dativ - meewerkend voorwerp)", "1e naamval (Nominativ - onderwerp)", "2e naamval (Genitiv)"],
      "antwoord": 0,
      "uitleg": "Wie/wat geeft hij? Een teddybeer = lijdend voorwerp = 4e naamval (einen Teddybären)."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste combinatie voor 'helfen': 'Ich helfe ____ (jou / 3e nv) und du hilfst ____ (mij / 3e nv).'",
      "opties": ["dir en mir", "dich en mich", "du en ich", "dir en mich"],
      "antwoord": 0,
      "uitleg": "Helfen krijgt altijd de 3e naamval: 'dir' en 'mir'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de medische instructie: 'Nehmen Sie die Tabletten nach dem Essen'?",
      "opties": ["Neem de tabletten na de maaltijd in.", "Neem de tabletten voor het slapen in.", "Slik de tabletten nuchter in.", "Los de tabletten op in heet water."],
      "antwoord": 0,
      "uitleg": "'Nach dem Essen' betekent na het eten."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'fahren' in de verleden tijd: 'Wir ____ gestern mit dem Zug.' (sein)",
      "opties": ["sind gefahren / waren", "waren gefahren", "hatten gefahren", "wurden gefahren"],
      "antwoord": 0,
      "uitleg": "Reizen met beweging gaat met sein: 'wir waren' of 'wir sind gefahren'."
    },
    {
      "type": "mc",
      "vraag": "Wat is het meervoud van 'der Notfall'?",
      "opties": ["die Notfälle", "die Notfallen", "die Notfaller", "die Notfalls"],
      "antwoord": 0,
      "uitleg": "Het meervoud van der Notfall is 'die Notfälle' (met Umlaut)."
    },
    {
      "type": "mc",
      "vraag": "Kies het juiste lidwoord (3e naamval vrouwelijk): 'Er schenkt ____ (seine Schwester) ein Buch.'",
      "opties": ["seiner Schwester", "seine Schwester", "seinen Schwester", "seinem Schwester"],
      "antwoord": 0,
      "uitleg": "Vrouwelijk in de 3e naamval krijgt de uitgang -er: 'seiner Schwester'."
    },
    {
      "type": "mc",
      "vraag": "Welk cijfer is in Duitsland het allerbeste toetscijfer?",
      "opties": ["1", "10", "6", "5"],
      "antwoord": 0,
      "uitleg": "1 is het beste cijfer in Duitsland (sehr gut)."
    },
    {
      "type": "mc",
      "vraag": "Kies de juiste vorm van 'können' in de verleden tijd: 'Ich ____ gestern nicht schlafen.'",
      "opties": ["konnte", "könnte", "kann", "konntest"],
      "antwoord": 0,
      "uitleg": "Verleden tijd van können bij 'ich' is 'konnte'."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de treinterm 'die Verspätung' op een Duits vertrekbord?",
      "opties": ["de vertraging", "het vertrek", "de aankomst", "de overstap"],
      "antwoord": 0,
      "uitleg": "'Die Verspätung' is de vertraging."
    },
    {
      "type": "mc",
      "vraag": "Wat is de naam van de Duitse hoofdstad?",
      "opties": ["Berlin", "München", "Hamburg", "Köln"],
      "antwoord": 0,
      "uitleg": "Berlijn is de hoofdstad van Duitsland."
    },
    # 4 Waar/Onwaar
    {
      "type": "waaronwaar",
      "vraag": "In het Duits zijn de lidwoorden voor de 3e naamval (Dativ): dem (m), der (v), dem (o), den (mv).",
      "antwoord": True,
      "uitleg": "Waar! Dit is het correcte rijtje voor de 3e naamval (Dativ)."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de verleden tijd houden werkwoorden zoals müssen en können altijd hun Umlaut.",
      "antwoord": False,
      "uitleg": "Onwaar! In het Präteritum verliezen ze hun Umlaut (musste, konnte, durfte)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het alarmnummer voor de brandweer en ambulance in Duitsland is 112.",
      "antwoord": True,
      "uitleg": "Waar! 112 is het alarmnummer voor brandweer en ambulance."
    },
    {
      "type": "waaronwaar",
      "vraag": "In de 4e naamval verandert het onzijdige lidwoord 'das' naar 'den'.",
      "antwoord": False,
      "uitleg": "Onwaar! 'Das' blijft 'das' in de 4e naamval. Alleen mannelijk verandert in 'den'."
    },
    # 4 Invul
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (3e naamval mannelijk): 'Der Arzt hilft ____ Patienten.' (der Patient)",
      "antwoord": "dem",
      "uitleg": "3e naamval mannelijk = 'dem'."
    },
    {
      "type": "invul",
      "vraag": "Vul het juiste lidwoord in (4e naamval mannelijk): 'Ich kaufe ____ Pullover.' (der Pullover)",
      "antwoord": "den",
      "uitleg": "4e naamval mannelijk = 'den'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal het woord: '(De politie)'",
      "antwoord": "Polizei",
      "uitleg": "De politie is 'die Polizei'."
    },
    {
      "type": "invul",
      "vraag": "Vertaal de Duitse hulpdienst die uitrukt bij brand: '(De brandweer)'",
      "antwoord": "Feuerwehr",
      "uitleg": "De brandweer is 'die Feuerwehr'."
    },
    # 2 Open
    {
      "type": "open",
      "vraag": "Noem het stappenplan in 3 vragen om te bepalen welke naamval je in een Duitse zin moet gebruiken.",
      "modelantwoord": "1. Wie doet het? (1e naamval - onderwerp). 2. Wie/wat ondergaat het? (4e naamval - lijdend voorwerp). 3. Aan wie/voor wie? (3e naamval - meewerkend voorwerp).",
      "sleutelwoorden": ["onderwerp", "lijdend voorwerp", "meewerkend voorwerp", "1e", "3e", "4e"],
      "minTreffers": 1,
      "uitleg": "Onderwerp (1e nv), lijdend voorwerp (4e nv), meewerkend voorwerp (3e nv)."
    },
    {
      "type": "open",
      "vraag": "Noem de drie Duitstalige DACH-landen en hun hoofdsteden.",
      "modelantwoord": "Duitsland (Berlijn), Oostenrijk (Wenen) en Zwitserland (Bern).",
      "sleutelwoorden": ["Berlin/Berlijn", "Wien/Wenen", "Bern"],
      "minTreffers": 1,
      "uitleg": "Duitsland (Berlijn), Oostenrijk (Wenen), Zwitserland (Bern)."
    }
  ]
}

# Write H6 exams
write_exam("examen_26.js", ex26)
write_exam("examen_27.js", ex27)
write_exam("examen_28.js", ex28)
write_exam("examen_29.js", ex29)
write_exam("examen_30.js", ex30)

print("\n🎉 H6 Exams generated successfully!")
