#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 5 new proeftoetsen (examen_6 to examen_10) for Wiskunde HAVO 3, Hoofdstuk 2 Statistiek.
Based on:
Moderne Wiskunde 2 havo-vwo - Hoofdstuk 2 Statistiek.pdf
Each exam has exactly 20 questions: 12 mc, 4 waaronwaar, 2 invul, 2 open.
Quality gate compliant:
- Balanced mc answers (<= 40% per letter)
- At least 35% onwaar in waaronwaar
- No 'invoer' in exam mode
- Explanations >= 15 chars
- No question number prefixes
- No sleutelwoord leaks
"""

import json, os, re

exams = [
    {
        "id": "ex-wiskunde-h2-6",
        "hoofdstuk": 2,
        "titel": "Proeftoets 6 — Verhoudingen, Procenten & Kruistabellen",
        "vak": "Wiskunde · H2 Statistiek",
        "icoon": "✖️",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Een paar merksneakers kostte oorspronkelijk € 120,- en is nu afgeprijsd naar € 90,-. Wat is het kortingspercentage?",
                "opties": [
                    "25%",
                    "20%",
                    "30%",
                    "33,3%"
                ],
                "antwoord": 0,
                "uitleg": "Korting = ((90 - 120) / 120) × 100% = (-30 / 120) × 100% = -25% (25% korting)."
            },
            {
                "type": "mc",
                "vraag": "Voor een recept voor 4 personen heb je 300 gram bloem nodig. Hoeveel gram bloem heb je nodig voor 7 personen volgens de verhoudingstabel?",
                "opties": [
                    "525 gram",
                    "450 gram",
                    "500 gram",
                    "600 gram"
                ],
                "antwoord": 0,
                "uitleg": "(7 × 300) / 4 = 2100 / 4 = 525 gram bloem."
            },
            {
                "type": "mc",
                "vraag": "De benzineprijs stijgt van € 1,80 naar € 1,98 per liter. Met welk percentage is de prijs gestegen?",
                "opties": [
                    "10%",
                    "8%",
                    "12%",
                    "18%"
                ],
                "antwoord": 0,
                "uitleg": "((1,98 - 1,80) / 1,80) × 100% = (0,18 / 1,80) × 100% = 10% stijging."
            },
            {
                "type": "mc",
                "vraag": "Een bedrag van € 450,- neemt toe met 8%. Met welke vermenigvuldigingsfactor (groeifactor) kun je het nieuwe bedrag in één keer berekenen?",
                "opties": [
                    "1,08",
                    "1,80",
                    "0,92",
                    "0,08"
                ],
                "antwoord": 0,
                "uitleg": "100% + 8% = 108% = 1,08."
            },
            {
                "type": "mc",
                "vraag": "Op een winterjas van € 160,- krijg je 35% korting. Wat is de nieuwe verkoopprijs van de jas?",
                "opties": [
                    "€ 104,-",
                    "€ 96,-",
                    "€ 112,-",
                    "€ 125,-"
                ],
                "antwoord": 0,
                "uitleg": "Nieuwe prijs = 160 × (1 - 0,35) = 160 × 0,65 = € 104,-."
            },
            {
                "type": "mc",
                "vraag": "In een verhoudingstabel staan bovenin de getallen 6 en 15, en onderin het getal 14 en x. Wat is de waarde van x bij kruislings vermenigvuldigen?",
                "opties": [
                    "35",
                    "30",
                    "28",
                    "42"
                ],
                "antwoord": 0,
                "uitleg": "x = (15 × 14) / 6 = 210 / 6 = 35."
            },
            {
                "type": "mc",
                "vraag": "Van de 850 leerlingen op een school komt 68% op de fiets. Hoeveel leerlingen komen er op de fiets naar school?",
                "opties": [
                    "578 leerlingen",
                    "544 leerlingen",
                    "612 leerlingen",
                    "595 leerlingen"
                ],
                "antwoord": 0,
                "uitleg": "0,68 × 850 = 578 leerlingen."
            },
            {
                "type": "mc",
                "vraag": "Een bioscoopticket wordt 15% duurder en kost nu € 13,80. Wat was de oorspronkelijke prijs vóór de verhoging?",
                "opties": [
                    "€ 12,00",
                    "€ 11,50",
                    "€ 12,50",
                    "€ 11,73"
                ],
                "antwoord": 0,
                "uitleg": "Oud = Nieuw / 1,15 = 13,80 / 1,15 = € 12,00."
            },
            {
                "type": "mc",
                "vraag": "In een sportvereniging met 400 leden zijn er 140 jeugdleden. Welk percentage van de leden is jeugdlid?",
                "opties": [
                    "35%",
                    "28%",
                    "40%",
                    "32%"
                ],
                "antwoord": 0,
                "uitleg": "(140 / 400) × 100% = 0,35 × 100% = 35%."
            },
            {
                "type": "mc",
                "vraag": "De bevolking van een dorp daalt in vijf jaar tijd van 5.000 naar 4.600 inwoners. Wat is de procentuele afname?",
                "opties": [
                    "8%",
                    "4%",
                    "9,2%",
                    "10%"
                ],
                "antwoord": 0,
                "uitleg": "((4600 - 5000) / 5000) × 100% = (-400 / 5000) × 100% = -8%."
            },
            {
                "type": "mc",
                "vraag": "Een scooter rijdt 135 km op 3 liter benzine. Hoeveel kilometer kan de scooter rijden op een volle tank van 8 liter?",
                "opties": [
                    "360 km",
                    "320 km",
                    "405 km",
                    "270 km"
                ],
                "antwoord": 0,
                "uitleg": "(135 / 3) × 8 = 45 × 8 = 360 km."
            },
            {
                "type": "mc",
                "vraag": "Een tablet kost € 363,- inclusief 21% btw. Wat is de prijs exclusief btw?",
                "opties": [
                    "€ 300,-",
                    "€ 286,77",
                    "€ 315,-",
                    "€ 290,-"
                ],
                "antwoord": 0,
                "uitleg": "Prijs excl. btw = 363 / 1,21 = € 300,-."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij een korting van 20% bereken je de nieuwe prijs door de oude prijs te vermenigvuldigen met 0,80.",
                "antwoord": True,
                "uitleg": "Waar: 100% - 20% = 80% = factor 0,80."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als een prijs eerst met 10% stijgt en daarna met 10% daalt, is de prijs weer exact gelijk aan de beginprijs.",
                "antwoord": False,
                "uitleg": "Onwaar: 100 × 1,10 = 110. Vervolgens 110 × 0,90 = 99 (de prijs is 1% lager dan het begin)."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een verhoudingstabel mag je getallen aan de boven- en onderkant met elkaar optellen om een nieuw evenredig paar te maken.",
                "antwoord": True,
                "uitleg": "Waar: kolommen in een verhoudingstabel mogen bij elkaar worden opgeteld."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een stijging van 200 naar 300 is een stijging van 100%.",
                "antwoord": False,
                "uitleg": "Onwaar: de toename is 100 op de 200, dat is (100 / 200) × 100% = 50% stijging."
            },
            {
                "type": "invul",
                "vraag": "De algemene formule voor procentuele toename of afname is: ([nieuw - oud|nieuw-oud]) gedeeld door oud vermenigvuldigd met 100%.",
                "antwoord": "nieuw - oud|nieuw-oud",
                "uitleg": "De formule luidt: ((Nieuw - Oud) / Oud) × 100%."
            },
            {
                "type": "invul",
                "vraag": "Een product van € 80,- stijgt in prijs naar € 100,-. De procentuele toename is [25|25%|25 procent].",
                "antwoord": "25|25%|25 procent",
                "uitleg": "((100 - 80) / 80) × 100% = (20 / 80) × 100% = 25%."
            },
            {
                "type": "open",
                "vraag": "Een abonnement kostte vorig jaar € 25,- per maand en kost dit jaar € 28,50 per maand. Bereken de procentuele toename en laat de berekening zien.",
                "sleutelwoorden": [
                    "28,50 - 25 = 3,50",
                    "3,50 / 25",
                    "14|14%"
                ],
                "minTreffers": 1,
                "modelantwoord": "Verschil = 28,50 - 25 = € 3,50. Procentuele stijging = (3,50 / 25) × 100% = 14% toename.",
                "uitleg": "((Nieuw - Oud) / Oud) × 100% = (3,50 / 25) × 100% = 14%."
            },
            {
                "type": "open",
                "vraag": "Op een smartphone van € 320,- wordt een korting van 15% gegeven. Toon aan dat de nieuwe verkoopprijs € 272,- bedraagt.",
                "sleutelwoorden": [
                    "320 * 0,15 = 48",
                    "320 - 48 = 272",
                    "320 * 0,85"
                ],
                "minTreffers": 1,
                "modelantwoord": "Korting = 0,15 × € 320 = € 48,-. Nieuwe prijs = € 320 - € 48 = € 272,- (of direct: 320 × 0,85 = € 272,-).",
                "uitleg": "320 × 0,85 = € 272,-."
            }
        ]
    },
    {
        "id": "ex-wiskunde-h2-7",
        "hoofdstuk": 2,
        "titel": "Proeftoets 7 — Cirkeldiagrammen, Middelpuntshoeken & Sectoren",
        "vak": "Wiskunde · H2 Statistiek",
        "icoon": "🥧",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Hoeveel graden is de sectorhoek van een categorie die precies 15% van een cirkeldiagram beslaat?",
                "opties": [
                    "54°",
                    "45°",
                    "60°",
                    "36°"
                ],
                "antwoord": 0,
                "uitleg": "15 × 3,6° = 54° (of 0,15 × 360° = 54°)."
            },
            {
                "type": "mc",
                "vraag": "In een klas van 24 leerlingen kiezen 6 leerlingen voor Spaans. Welke sectorhoek hoort bij Spaans in het cirkeldiagram?",
                "opties": [
                    "90°",
                    "60°",
                    "75°",
                    "120°"
                ],
                "antwoord": 0,
                "uitleg": "(6 / 24) × 360° = 0,25 × 360° = 90°."
            },
            {
                "type": "mc",
                "vraag": "Een sector in een cirkeldiagram heeft een middelpuntshoek van 126°. Welk percentage van het totaal hoort bij deze sector?",
                "opties": [
                    "35%",
                    "30%",
                    "40%",
                    "42%"
                ],
                "antwoord": 0,
                "uitleg": "(126° / 360°) × 100% = 35% (of 126 / 3,6 = 35%)."
            },
            {
                "type": "mc",
                "vraag": "Hoeveel graden telt 1 procent (1%) in een cirkeldiagram altijd exact?",
                "opties": [
                    "3,6°",
                    "1,8°",
                    "3,0°",
                    "4,5°"
                ],
                "antwoord": 0,
                "uitleg": "360° / 100% = 3,6° per procent."
            },
            {
                "type": "mc",
                "vraag": "Een school telt 600 leerlingen. In het cirkeldiagram over vervoer heeft de sector 'Trein' een hoek van 48°. Hoeveel leerlingen komen met de trein?",
                "opties": [
                    "80 leerlingen",
                    "60 leerlingen",
                    "100 leerlingen",
                    "72 leerlingen"
                ],
                "antwoord": 0,
                "uitleg": "(48° / 360°) × 600 = (2 / 15) × 600 = 80 leerlingen."
            },
            {
                "type": "mc",
                "vraag": "Drie vrienden verdelen een cirkeldiagram in vier sectoren. De eerste drie hoeken zijn 110°, 85° en 75°. Hoe groot moet de vierde hoek zijn?",
                "opties": [
                    "90°",
                    "80°",
                    "95°",
                    "100°"
                ],
                "antwoord": 0,
                "uitleg": "De som van een cirkel is 360°. Vierde hoek = 360° - (110° + 85° + 75°) = 360° - 270° = 90°."
            },
            {
                "type": "mc",
                "vraag": "Welke sectorhoek hoort bij een aandeel van 62,5% in een cirkeldiagram?",
                "opties": [
                    "225°",
                    "210°",
                    "240°",
                    "200°"
                ],
                "antwoord": 0,
                "uitleg": "62,5 × 3,6° = 225° (of 0,625 × 360° = 225°)."
            },
            {
                "type": "mc",
                "vraag": "Bij een onderzoek onder 90 personen antwoorden 18 personen 'Ja'. Wat is de hoek van de sector 'Ja' in graden?",
                "opties": [
                    "72°",
                    "60°",
                    "80°",
                    "90°"
                ],
                "antwoord": 0,
                "uitleg": "(18 / 90) × 360° = 0,2 × 360° = 72°."
            },
            {
                "type": "mc",
                "vraag": "Wat is het belangrijkste doel van een cirkeldiagram?",
                "opties": [
                    "Laten zien hoe een totaal (100%) is verdeeld over verschillende categorieën.",
                    "Het verband tussen twee meetwaarden in de tijd weergeven.",
                    "Precies de spreiding en kwartielen van getallen tonen.",
                    "Het gemiddelde berekenen van een frequentieverdeling."
                ],
                "antwoord": 0,
                "uitleg": "Een cirkeldiagram toont de verhouding van de delen ten opzichte van het geheel (100%)."
            },
            {
                "type": "mc",
                "vraag": "Een sectorhoek is 18°. Hoeveel procent van het geheel vertegenwoordigt deze sector?",
                "opties": [
                    "5%",
                    "10%",
                    "8%",
                    "2,5%"
                ],
                "antwoord": 0,
                "uitleg": "18° / 3,6° = 5% (of (18 / 360) × 100% = 5%)."
            },
            {
                "type": "mc",
                "vraag": "In een sportkantine zijn 120 drankjes verkocht: 60 water, 30 sap en 30 frisdrank. Welke sectorhoek hoort bij de categorie 'sap'?",
                "opties": [
                    "90°",
                    "180°",
                    "60°",
                    "120°"
                ],
                "antwoord": 0,
                "uitleg": "(30 / 120) × 360° = 0,25 × 360° = 90°."
            },
            {
                "type": "mc",
                "vraag": "Als een sector een hoek heeft van 270°, welk deel van de cirkel beslaat deze sector dan?",
                "opties": [
                    "Driekwart (75%)",
                    "De helft (50%)",
                    "Tweederde (66,7%)",
                    "Vier vijfde (80%)"
                ],
                "antwoord": 0,
                "uitleg": "270° / 360° = 3/4 = 75%."
            },
            {
                "type": "waaronwaar",
                "vraag": "De som van alle sectorhoeken in een cirkeldiagram is altijd precies 360 graden.",
                "antwoord": True,
                "uitleg": "Waar: een volle cirkel omvat altijd exact 360°."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een categorie die 50% van de data omvat heeft in een cirkeldiagram een sectorhoek van 90 graden.",
                "antwoord": False,
                "uitleg": "Onwaar: 50% van 360° is 180° (een halve cirkel), niet 90°."
            },
            {
                "type": "waaronwaar",
                "vraag": "Om van een percentage naar een sectorhoek om te rekenen vermenigvuldig je het percentage met 3,6.",
                "antwoord": True,
                "uitleg": "Waar: omdat 1% gelijk is aan 3,6°, geldt: percentage × 3,6 = sectorhoek in graden."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een cirkeldiagram kun je ook negatieve percentages weergeven met een negatieve sectorhoek.",
                "antwoord": False,
                "uitleg": "Onwaar: sectorhoeken en percentages in een cirkeldiagram zijn altijd positief."
            },
            {
                "type": "invul",
                "vraag": "De hoek van een categorie die een derde (1/3) van het totaal vormt is precies [120|120°|120 graden].",
                "antwoord": "120|120°|120 graden",
                "uitleg": "(1 / 3) × 360° = 120°."
            },
            {
                "type": "invul",
                "vraag": "Een sectorhoek van 108 graden komt overeen met een percentage van [30|30%|30 procent].",
                "antwoord": "30|30%|30 procent",
                "uitleg": "108° / 3,6° = 30%."
            },
            {
                "type": "open",
                "vraag": "In een klas van 32 leerlingen spelen 8 leerlingen een muziekinstrument. Bereken de grootte van de sectorhoek voor een cirkeldiagram en toon de berekening.",
                "sleutelwoorden": [
                    "8/32",
                    "90|90°|90 graden"
                ],
                "minTreffers": 1,
                "modelantwoord": "Berekening: (8 / 32) × 360° = 0,25 × 360° = 90°.",
                "uitleg": "Deel gedeeld door geheel vermenigvuldigd met 360 graden geeft 90°."
            },
            {
                "type": "open",
                "vraag": "Leg in één duidelijke zin uit waarom de som van alle percentages in een cirkeldiagram altijd 100% moet zijn.",
                "sleutelwoorden": [
                    "hele cirkel/volledige cirkel/alles",
                    "totaal/alle waarnemingen samen"
                ],
                "minTreffers": 1,
                "modelantwoord": "Omdat de cirkel alle waarnemingen samen voorstelt en de som van alle delen daarom precies gelijk moet zijn aan het geheel (100%).",
                "uitleg": "De cirkel stelt het geheel (100%) voor."
            }
        ]
    },
    {
        "id": "ex-wiskunde-h2-8",
        "hoofdstuk": 2,
        "titel": "Proeftoets 8 — Frequentietabellen, Klassen & Relatieve Frequentie",
        "vak": "Wiskunde · H2 Statistiek",
        "icoon": "📋",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Wat is het verschil tussen absolute frequentie en relatieve frequentie?",
                "opties": [
                    "Absolute frequentie is het werkelijke aantal; relatieve frequentie is het percentage van het totaal.",
                    "Absolute frequentie is altijd in graden; relatieve frequentie is in euro's.",
                    "Relatieve frequentie is altijd groter dan 100.",
                    "Er is geen verschil; het zijn twee woorden voor hetzelfde begrip."
                ],
                "antwoord": 0,
                "uitleg": "Absoluut = geteld aantal. Relatief = aandeel of percentage van het totale aantal."
            },
            {
                "type": "mc",
                "vraag": "In een onderzoek hebben 12 van de 40 respondenten gekozen voor optie B. Wat is de relatieve frequentie van optie B?",
                "opties": [
                    "30%",
                    "25%",
                    "12%",
                    "35%"
                ],
                "antwoord": 0,
                "uitleg": "(12 / 40) × 100% = 0,30 × 100% = 30%."
            },
            {
                "type": "mc",
                "vraag": "Wat is het klassenmidden van de klasse 50 - < 70?",
                "opties": [
                    "60",
                    "55",
                    "65",
                    "20"
                ],
                "antwoord": 0,
                "uitleg": "Klassenmidden = (50 + 70) / 2 = 120 / 2 = 60."
            },
            {
                "type": "mc",
                "vraag": "Wat is de klassenbreedte van de klasse 165 - < 175?",
                "opties": [
                    "10",
                    "5",
                    "170",
                    "15"
                ],
                "antwoord": 0,
                "uitleg": "Klassenbreedte = Bovengrens - Ondergrens = 175 - 165 = 10."
            },
            {
                "type": "mc",
                "vraag": "In welke klasse valt een waarneming met de exacte waarde 80 bij de indeling: 70 - < 80 en 80 - < 90?",
                "opties": [
                    "In de klasse 80 - < 90.",
                    "In de klasse 70 - < 80.",
                    "In beide klassen tegelijk.",
                    "In geen van beide klassen."
                ],
                "antwoord": 0,
                "uitleg": "Het teken '<' betekent 'kleiner dan'. 80 hoort dus bij de klasse vanaf 80: 80 - < 90."
            },
            {
                "type": "mc",
                "vraag": "In een frequentietabel staan de scores 5, 6, 7 en 8 met respectievelijk frequenties 3, 7, 6 en 4. Hoeveel waarnemingen zijn er in totaal gedaan?",
                "opties": [
                    "20 waarnemingen",
                    "26 waarnemingen",
                    "18 waarnemingen",
                    "24 waarnemingen"
                ],
                "antwoord": 0,
                "uitleg": "Totale frequentie = 3 + 7 + 6 + 4 = 20."
            },
            {
                "type": "mc",
                "vraag": "Wat is het gewogen gemiddelde van de scores uit de vorige vraag (waarde × frequentie: 5×3, 6×7, 7×6, 8×4 met totaal frequentie 20)?",
                "opties": [
                    "6,55",
                    "6,40",
                    "6,80",
                    "7,00"
                ],
                "antwoord": 0,
                "uitleg": "Som = (5×3) + (6×7) + (7×6) + (8×4) = 15 + 42 + 42 + 32 = 131. Gemiddelde = 131 / 20 = 6,55."
            },
            {
                "type": "mc",
                "vraag": "Wat stelt de cumulatieve frequentie bij een score voor?",
                "opties": [
                    "De som van alle frequenties vanaf de laagste waarde tot en met die score.",
                    "Het verschil tussen de hoogste en laagste frequentie.",
                    "Het gemiddelde van de frequenties.",
                    "De frequentie vermenigvuldigd met 100%."
                ],
                "antwoord": 0,
                "uitleg": "Cumulatief betekent opgeteld: de doorlopende optelling van frequenties."
            },
            {
                "type": "mc",
                "vraag": "Een klas van 25 leerlingen heeft voor een proefwerk 4 onvoldoendes (cijfer lager dan 5,5). Wat is de relatieve frequentie van onvoldoendes?",
                "opties": [
                    "16%",
                    "20%",
                    "12%",
                    "84%"
                ],
                "antwoord": 0,
                "uitleg": "(4 / 25) × 100% = 16%."
            },
            {
                "type": "mc",
                "vraag": "Waarom gebruik je bij een grote dataset met veel verschillende waarden (zoals lengtes van 500 scholieren) een klassenindeling?",
                "opties": [
                    "Om overzicht te creëren en patronen in de data zichtbaar te maken.",
                    "Omdat een computer anders geen gemiddelde kan berekenen.",
                    "Om alle uitschieters automatisch te wissen.",
                    "Omdat frequentietabellen maximaal 5 rijen mogen bevatten."
                ],
                "antwoord": 0,
                "uitleg": "Gegroepeerde data in klassen zorgt voor overzicht bij grote hoeveelheden verschillende metingen."
            },
            {
                "type": "mc",
                "vraag": "Wat is het klassenmidden van de klasse 12 - < 18?",
                "opties": [
                    "15",
                    "14",
                    "16",
                    "6"
                ],
                "antwoord": 0,
                "uitleg": "(12 + 18) / 2 = 30 / 2 = 15."
            },
            {
                "type": "mc",
                "vraag": "Als in een frequentietabel de som van de relatieve frequenties wordt berekend, wat moet de uitkomst dan altijd zijn?",
                "opties": [
                    "100% (of 1,00)",
                    "360%",
                    "Gelijk aan het aantal waarnemingen",
                    "50%"
                ],
                "antwoord": 0,
                "uitleg": "De som van alle delen bij elkaar opgeteld is altijd precies het geheel: 100%."
            },
            {
                "type": "waaronwaar",
                "vraag": "Bij de klasse 10 - < 20 telt het getal 20 wél mee in deze klasse.",
                "antwoord": False,
                "uitleg": "Onwaar: '< 20' betekent strikt kleiner dan 20. Het getal 20 valt in de volgende klasse (20 - < 30)."
            },
            {
                "type": "waaronwaar",
                "vraag": "De relatieve frequentie is altijd een getal tussen 0% en 100%.",
                "antwoord": True,
                "uitleg": "Waar: een aandeel kan nooit kleiner dan 0% of groter dan 100% zijn."
            },
            {
                "type": "waaronwaar",
                "vraag": "De klassenbreedte bereken je door de ondergrens bij de bovengrens op te tellen.",
                "antwoord": False,
                "uitleg": "Onwaar: klassenbreedte is het VERSCHIL (Bovengrens minus Ondergrens)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Als 8 van de 32 leerlingen een bril dragen, is de relatieve frequentie 25%.",
                "antwoord": True,
                "uitleg": "Waar: (8 / 32) × 100% = 0,25 × 100% = 25%."
            },
            {
                "type": "invul",
                "vraag": "Het werkelijke aantal keren dat een waarneming voorkomt noemen we de [absolute frequentie].",
                "antwoord": "absolute frequentie",
                "uitleg": "Absolute frequentie is het zuivere getelde aantal waarnemingen."
            },
            {
                "type": "invul",
                "vraag": "Het exacte gemiddelde van de ondergrens en bovengrens van een klasse heet het [klassenmidden].",
                "antwoord": "klassenmidden",
                "uitleg": "Klassenmidden = (Ondergrens + Bovengrens) / 2."
            },
            {
                "type": "open",
                "vraag": "In een sportteam hebben 5 spelers schoenmaat 41, 8 spelers maat 42, 5 spelers maat 43 en 2 spelers maat 44. Bereken de gemiddelde schoenmaat van dit team.",
                "sleutelwoorden": [
                    "20 spelers",
                    "844 / 20",
                    "42,2|42.2"
                ],
                "minTreffers": 1,
                "modelantwoord": "Totaal aantal spelers = 5 + 8 + 5 + 2 = 20. Som = (5×41) + (8×42) + (5×43) + (2×44) = 205 + 336 + 215 + 88 = 844. Gemiddelde = 844 / 20 = 42,2.",
                "uitleg": "Gewogen gemiddelde = totale som gedeeld door totale frequentie (844 / 20 = 42,2)."
            },
            {
                "type": "open",
                "vraag": "Geef de definitie van de relatieve frequentie en noem de formule om deze in procenten te berekenen.",
                "sleutelwoorden": [
                    "deel van het totaal/aandeel",
                    "absolute frequentie / totaal",
                    "* 100%"
                ],
                "minTreffers": 1,
                "modelantwoord": "Definitie: Het aandeel van een bepaalde waarneming ten opzichte van het totaal. Formule: Relatieve frequentie = (Absolute frequentie / Totaal aantal waarnemingen) × 100%.",
                "uitleg": "(Aantal / Totaal) × 100%."
            }
        ]
    },
    {
        "id": "ex-wiskunde-h2-9",
        "hoofdstuk": 2,
        "titel": "Proeftoets 9 — Centrummaten: Gemiddelde, Mediaan & Modus",
        "vak": "Wiskunde · H2 Statistiek",
        "icoon": "🎯",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "Gegeven is de getallenrij: 3, 4, 7, 9, 12. Wat is de mediaan van deze getallen?",
                "opties": [
                    "7",
                    "4",
                    "9",
                    "7,0"
                ],
                "antwoord": 0,
                "uitleg": "De 5 getallen staan op volgorde; het 3e getal is precies het middelste: 7."
            },
            {
                "type": "mc",
                "vraag": "Gegeven is de getallenrij met een even aantal getallen: 4, 6, 8, 10, 12, 14. Wat is de mediaan?",
                "opties": [
                    "9",
                    "8",
                    "10",
                    "8,5"
                ],
                "antwoord": 0,
                "uitleg": "De twee middelste getallen zijn 8 en 10. De mediaan is het gemiddelde: (8 + 10) / 2 = 9."
            },
            {
                "type": "mc",
                "vraag": "Wat is de modus van de getallenreeks: 5, 7, 8, 8, 9, 11, 11, 11, 14?",
                "opties": [
                    "11",
                    "8",
                    "9",
                    "Er is geen modus"
                ],
                "antwoord": 0,
                "uitleg": "Het getal 11 komt het vaakst voor (3 keer) en is dus de modus."
            },
            {
                "type": "mc",
                "vraag": "Wat is het rekenkundig gemiddelde van de cijfers: 6, 7, 8, 8, 9, 10?",
                "opties": [
                    "8,0",
                    "7,5",
                    "8,2",
                    "8,5"
                ],
                "antwoord": 0,
                "uitleg": "Som = 6 + 7 + 8 + 8 + 9 + 10 = 48. Gemiddelde = 48 / 6 = 8,0."
            },
            {
                "type": "mc",
                "vraag": "Wanneer heeft een getallenreeks GEEN modus?",
                "opties": [
                    "Wanneer alle getallen even vaak voorkomen (bijvoorbeeld allemaal 1 keer).",
                    "Wanneer het aantal getallen oneven is.",
                    "Wanneer het gemiddelde gelijk is aan de mediaan.",
                    "Wanneer er negatieve getallen in de reeks voorkomen."
                ],
                "antwoord": 0,
                "uitleg": "Als geen enkel getal vaker voorkomt dan de rest, is er geen unieke hoogste frequentie en dus geen modus."
            },
            {
                "type": "mc",
                "vraag": "Een leerling haalt voor vier toetsen de cijfers 6,5; 7,0; 8,0 en 8,5. Welk cijfer moet hij voor de vijfde toets halen om precies een 7,5 gemiddeld te staan?",
                "opties": [
                    "7,5",
                    "7,0",
                    "8,0",
                    "6,5"
                ],
                "antwoord": 0,
                "uitleg": "Voor een gemiddelde van 7,5 over 5 toetsen is een totaalsom van 5 × 7,5 = 37,5 nodig. Huidige som = 6,5 + 7 + 8 + 8,5 = 30. Benodigd cijfer = 37,5 - 30 = 7,5."
            },
            {
                "type": "mc",
                "vraag": "Gegeven zijn de getallen: 14, 8, 22, 11, 19. Wat moet je ALTIJD eerst doen voordat je de mediaan kunt bepalen?",
                "opties": [
                    "De getallen op volgorde van klein naar groot zetten.",
                    "Het gemiddelde van de getallen uitrekenen.",
                    "Het kleinste getal van het grootste getal aftrekken.",
                    "Alle getallen vermenigvuldigen met elkaar."
                ],
                "antwoord": 0,
                "uitleg": "De mediaan is het middelste getal van een GEORDENDE reeks (8, 11, 14, 19, 22 → mediaan is 14)."
            },
            {
                "type": "mc",
                "vraag": "Welke centrummaat is het MEEST gevoelig voor één extreme uitschieter (bijvoorbeeld een extreem hoog of laag getal)?",
                "opties": [
                    "Het gemiddelde",
                    "De mediaan",
                    "De modus",
                    "Zowel de mediaan als de modus"
                ],
                "antwoord": 0,
                "uitleg": "Het gemiddelde telt elke waarde mee in de som en verschuift sterk bij een extreme uitschieter. De mediaan blijft op zijn plek."
            },
            {
                "type": "mc",
                "vraag": "In een straat wonen 5 gezinnen met de volgende aantallen huisdieren: 0, 1, 1, 2, 6. Wat is de mediaan van het aantal huisdieren?",
                "opties": [
                    "1 huisdier",
                    "2 huisdieren",
                    "0 huisdieren",
                    "2,5 huisdieren"
                ],
                "antwoord": 0,
                "uitleg": "De 5 getallen staan op volgorde (0, 1, 1, 2, 6). Het 3e getal is 1."
            },
            {
                "type": "mc",
                "vraag": "Wat is de modus van de schoenmaten: 38, 39, 40, 40, 41, 42, 42, 43?",
                "opties": [
                    "Er zijn twee modi: 40 en 42 (bimodaal).",
                    "De modus is 40,5.",
                    "Er is geen modus.",
                    "De modus is 41."
                ],
                "antwoord": 0,
                "uitleg": "Zowel 40 als 42 komen elk 2 keer voor en delen de hoogste frequentie. Er zijn twee modi."
            },
            {
                "type": "mc",
                "vraag": "Drie proefwerken tellen elk 1 keer mee en een grote eindtoets telt 2 keer mee (gewicht 2). Een leerling haalt voor de proefwerken een 6, 7 en 8, en voor de eindtoets een 9. Wat is het gewogen gemiddelde?",
                "opties": [
                    "7,8",
                    "7,5",
                    "8,0",
                    "7,6"
                ],
                "antwoord": 0,
                "uitleg": "Som = (6×1) + (7×1) + (8×1) + (9×2) = 6 + 7 + 8 + 18 = 39. Totale weging = 1 + 1 + 1 + 2 = 5. Gemiddelde = 39 / 5 = 7,8."
            },
            {
                "type": "mc",
                "vraag": "Als een reeks uit 15 geordende getallen bestaat, op welke positie bevindt zich dan de mediaan?",
                "opties": [
                    "Het 8e getal",
                    "Het 7e getal",
                    "Het 7,5e getal",
                    "Het 9e getal"
                ],
                "antwoord": 0,
                "uitleg": "(n + 1) / 2 = (15 + 1) / 2 = 16 / 2 = 8e getal."
            },
            {
                "type": "waaronwaar",
                "vraag": "De mediaan van een getallenreeks is altijd gelijk aan het rekenkundig gemiddelde van die reeks.",
                "antwoord": False,
                "uitleg": "Onwaar: gemiddelde en mediaan zijn meestal verschillend, zeker bij scheve verdelingen of uitschieters."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een getallenrij kan meerdere modi hebben als meerdere getallen dezelfde hoogste frequentie delen.",
                "antwoord": True,
                "uitleg": "Waar: delen twee waarden de hoogste frequentie, dan spreken we van twee modi (bimodaal)."
            },
            {
                "type": "waaronwaar",
                "vraag": "Om de mediaan van 10 getallen te berekenen neem je het gemiddelde van het 5e en 6e getal (mits geordend).",
                "antwoord": True,
                "uitleg": "Waar: bij een even aantal getallen neem je het gemiddelde van de twee middelste getallen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De modus is de som van alle getallen gedeeld door het aantal getallen.",
                "antwoord": False,
                "uitleg": "Onwaar: dat is de definitie van het gemiddelde. De modus is de waarde die het vaakst voorkomt."
            },
            {
                "type": "invul",
                "vraag": "Het getal dat in een statistische dataset het vaakst voorkomt noemen we de [modus].",
                "antwoord": "modus",
                "uitleg": "De modus is de waarneming met de hoogste frequentie."
            },
            {
                "type": "invul",
                "vraag": "De middelste waarde van een op volgorde gezette getallenreeks heet de [mediaan].",
                "antwoord": "mediaan",
                "uitleg": "De mediaan verdeelt de geordende dataset precies in twee gelijke helften van 50%."
            },
            {
                "type": "open",
                "vraag": "Gegeven zijn de cijfers: 4, 9, 6, 7, 9, 8, 6, 7, 7. Bepaal het gemiddelde, de mediaan en de modus van deze cijfers.",
                "sleutelwoorden": [
                    "gemiddelde = 7|gemiddelde 7",
                    "mediaan = 7|mediaan 7",
                    "modus = 7|modus 7"
                ],
                "minTreffers": 1,
                "modelantwoord": "Geordend: 4, 6, 6, 7, 7, 7, 8, 9, 9 (n = 9). Som = 63. Gemiddelde = 63 / 9 = 7. Mediaan = 5e getal = 7. Modus = 7 (komt 3 keer voor).",
                "uitleg": "Som is 63 / 9 = 7; middelste getal is 7; meest voorkomende getal is 7."
            },
            {
                "type": "open",
                "vraag": "Leg uit waarom een makelaar bij huizenprijzen in een wijk liever de mediaan vermeldt dan het gemiddelde.",
                "sleutelwoorden": [
                    "uitschieter/villa/miljoenenwoning/duur huis",
                    "gemiddelde omhoog trekt/vertekend beeld/mediaan betrouwbaarder"
                ],
                "minTreffers": 1,
                "modelantwoord": "Als er in een wijk één extreem duur landhuis van 3 miljoen euro staat, trekt dat het gemiddelde enorm omhoog. De mediaan trekt zich niets aan van die ene uitschieter en geeft een veel betrouwbaarder beeld van wat een 'normale' woning in die wijk kost.",
                "uitleg": "De mediaan is ongevoelig voor extreme uitschieters."
            }
        ]
    },
    {
        "id": "ex-wiskunde-h2-10",
        "hoofdstuk": 2,
        "titel": "Proeftoets 10 — Steel-bladdiagram, Spreidingsbreedte & Kwartielen",
        "vak": "Wiskunde · H2 Statistiek",
        "icoon": "🌳",
        "duurMin": 20,
        "vragen": [
            {
                "type": "mc",
                "vraag": "In een steel-bladdiagram staat in de steel het getal 5 en bij de bladeren 1, 4, 4, 9. De legenda vermeldt: 5 | 1 = 51. Welke getallen worden hier weergegeven?",
                "opties": [
                    "51, 54, 54, 59",
                    "15, 45, 45, 95",
                    "5, 1, 4, 4, 9",
                    "51449"
                ],
                "antwoord": 0,
                "uitleg": "De steel geeft de tientallen weer; gecombineerd met de bladeren levert dit 51, 54, 54 en 59 op."
            },
            {
                "type": "mc",
                "vraag": "Wat is de definitie van de 'spreidingsbreedte' van een statistische dataset?",
                "opties": [
                    "Het verschil tussen de hoogste en de laagste waarneming (Maximum - Minimum).",
                    "Het gemiddelde van het eerste en derde kwartiel.",
                    "De breedte van de meest voorkomende klasse in een histogram.",
                    "Het totale aantal waarnemingen in de steekproef."
                ],
                "antwoord": 0,
                "uitleg": "Spreidingsbreedte (range) = Maximum - Minimum."
            },
            {
                "type": "mc",
                "vraag": "In een groep scholieren is de langste leerling 194 cm en de kortste 158 cm. Wat is de spreidingsbreedte van de lengte?",
                "opties": [
                    "36 cm",
                    "46 cm",
                    "34 cm",
                    "176 cm"
                ],
                "antwoord": 0,
                "uitleg": "Spreidingsbreedte = 194 - 158 = 36 cm."
            },
            {
                "type": "mc",
                "vraag": "Wat stelt het eerste kwartiel (Q₁) van een geordende dataset voor?",
                "opties": [
                    "De mediaan van de eerste (linker) helft van de waarnemingsgetallen (de grens van de eerste 25%).",
                    "Het minimum van de dataset.",
                    "Een kwart van de totale som van alle getallen.",
                    "De modus van de eerste helft van de getallen."
                ],
                "antwoord": 0,
                "uitleg": "Q₁ is de mediaan van de linkerhelft en markeert de eerste 25% van de waarnemingen."
            },
            {
                "type": "mc",
                "vraag": "Gegeven zijn de kwartielen: Q₁ = 18 en Q₃ = 31. Wat is de kwartielafstand van deze dataset?",
                "opties": [
                    "13",
                    "49",
                    "24,5",
                    "15"
                ],
                "antwoord": 0,
                "uitleg": "Kwartielafstand = Q₃ - Q₁ = 31 - 18 = 13."
            },
            {
                "type": "mc",
                "vraag": "Gegeven is de geordende reeks met 11 getallen: 12, 14, 15, 17, 19, 21, 24, 26, 28, 30, 35. Wat is het eerste kwartiel Q₁?",
                "opties": [
                    "15",
                    "14",
                    "17",
                    "21"
                ],
                "antwoord": 0,
                "uitleg": "De mediaan (Q₂) is 21 (het 6e getal). De linkerhelft bestaat uit 12, 14, 15, 17, 19. Het middelste getal daarvan is 15. Dus Q₁ = 15."
            },
            {
                "type": "mc",
                "vraag": "Wat is het derde kwartiel Q₃ van de getallenreeks uit de vorige vraag (rechterhelft: 24, 26, 28, 30, 35)?",
                "opties": [
                    "28",
                    "26",
                    "30",
                    "35"
                ],
                "antwoord": 0,
                "uitleg": "De rechterhelft is 24, 26, 28, 30, 35. Het middelste getal daarvan is 28. Dus Q₃ = 28."
            },
            {
                "type": "mc",
                "vraag": "Wat is een groot voordeel van een steel-bladdiagram boven een histogram?",
                "opties": [
                    "In een steel-bladdiagram blijven alle oorspronkelijke individuele meetwaarden zichtbaar en bewaard.",
                    "Een steel-bladdiagram kan alleen met een passer worden getekend.",
                    "Er kunnen nooit uitschieters in een steel-bladdiagram voorkomen.",
                    "Een steel-bladdiagram berekent automatisch de standaarddeviatie."
                ],
                "antwoord": 0,
                "uitleg": "In een histogram zie je alleen staafhoogtes en gaan individuele getallen verloren; in een steel-bladdiagram blijven alle exacte cijfers leesbaar."
            },
            {
                "type": "mc",
                "vraag": "In een steel-bladdiagram staat bij de legenda: 3 | 8 = 3,8 meter. Wat betekent een rij met steel 6 en bladeren 0, 2, 5?",
                "opties": [
                    "6,0 meter; 6,2 meter en 6,5 meter",
                    "60 meter; 62 meter en 65 meter",
                    "0,6 meter; 2,6 meter en 5,6 meter",
                    "6025 meter"
                ],
                "antwoord": 0,
                "uitleg": "Volgens de legenda stelt het blad decimalen voor: 6,0; 6,2 en 6,5 meter."
            },
            {
                "type": "mc",
                "vraag": "Welk percentage van alle waarnemingen ligt altijd tussen het eerste kwartiel Q₁ en het derde kwartiel Q₃?",
                "opties": [
                    "50%",
                    "25%",
                    "75%",
                    "100%"
                ],
                "antwoord": 0,
                "uitleg": "Tussen 25% (Q₁) en 75% (Q₃) ligt precies de middelste 50% van de waarnemingen."
            },
            {
                "type": "mc",
                "vraag": "In een steel-bladdiagram telt een onderzoeker in totaal 28 cijfers bij de bladeren. Hoeveel waarnemingen bevat deze dataset?",
                "opties": [
                    "28 waarnemingen",
                    "14 waarnemingen",
                    "56 waarnemingen",
                    "Dat hangt af van het aantal stelen"
                ],
                "antwoord": 0,
                "uitleg": "Elk blad vertegenwoordigt precies één afzonderlijke waarneming. 28 bladeren = 28 waarnemingen."
            },
            {
                "type": "mc",
                "vraag": "Gegeven zijn minimum = 12, Q₁ = 18, mediaan = 24, Q₃ = 32 en maximum = 45. Wat is de spreidingsbreedte van deze verdeling?",
                "opties": [
                    "33",
                    "14",
                    "27",
                    "21"
                ],
                "antwoord": 0,
                "uitleg": "Spreidingsbreedte = Maximum - Minimum = 45 - 12 = 33."
            },
            {
                "type": "waaronwaar",
                "vraag": "In een steel-bladdiagram moeten de cijfers in elk blad altijd op volgorde van klein naar groot worden genoteerd.",
                "antwoord": True,
                "uitleg": "Waar: bladeren horen netjes geordend van klein naar groot te staan zodat je direct de mediaan kunt aflezen."
            },
            {
                "type": "waaronwaar",
                "vraag": "De kwartielafstand is gelijk aan het maximum minus het minimum.",
                "antwoord": False,
                "uitleg": "Onwaar: dat is de spreidingsbreedte. De kwartielafstand is Q₃ - Q₁."
            },
            {
                "type": "waaronwaar",
                "vraag": "Het tweede kwartiel Q₂ is exact hetzelfde als de mediaan van de totale dataset.",
                "antwoord": True,
                "uitleg": "Waar: Q₂ deelt de dataset in twee helften van 50% en is dus precies de mediaan."
            },
            {
                "type": "waaronwaar",
                "vraag": "Een steel in een steel-bladdiagram mag worden overgeslagen als er geen waarnemingen in dat tiental zijn.",
                "antwoord": False,
                "uitleg": "Onwaar: alle opeenvolgende stelen tussen minimum en maximum moeten vermeld worden (met een leeg blad) om gaten in de spreiding te tonen."
            },
            {
                "type": "invul",
                "vraag": "De formule voor de kwartielafstand luidt: derde kwartiel ([Q3|Q₃]) minus eerste kwartiel ([Q1|Q₁]).",
                "antwoord": "Q3 - Q1|Q₃ - Q₁",
                "uitleg": "Kwartielafstand = Q₃ - Q₁."
            },
            {
                "type": "invul",
                "vraag": "De maat die het verschil tussen de hoogste en laagste waarneming aangeeft heet de [spreidingsbreedte].",
                "antwoord": "spreidingsbreedte",
                "uitleg": "Spreidingsbreedte = Maximum - Minimum."
            },
            {
                "type": "open",
                "vraag": "Gegeven zijn de meetwaarden: 5, 8, 12, 14, 17, 20, 25. Bepaal het minimum, het maximum, de spreidingsbreedte en de kwartielafstand van deze reeks.",
                "sleutelwoorden": [
                    "spreidingsbreedte = 20|spreidingsbreedte 20",
                    "kwartielafstand = 12|kwartielafstand 12"
                ],
                "minTreffers": 1,
                "modelantwoord": "Minimum = 5, Maximum = 25. Spreidingsbreedte = 25 - 5 = 20. Mediaan (Q₂) = 14. Q₁ = 8, Q₃ = 20. Kwartielafstand = Q₃ - Q₁ = 20 - 8 = 12.",
                "uitleg": "Spreidingsbreedte = 25 - 5 = 20; Kwartielafstand = 20 - 8 = 12."
            },
            {
                "type": "open",
                "vraag": "Leg uit waarom de legenda bij een steel-bladdiagram onmisbaar is.",
                "sleutelwoorden": [
                    "betekenis van de getallen/eenheden",
                    "tiental of decimaal/kommagetal"
                ],
                "minTreffers": 1,
                "modelantwoord": "Zonder legenda weet de lezer niet of bijvoorbeeld '4 | 7' staat voor het getal 47, voor 4,7 of voor 470. De legenda geeft aan wat de steel en het blad precies betekenen.",
                "uitleg": "De legenda bepaalt de schaal en decimale waarde van de cijfers."
            }
        ]
    }
]

# Balance mc options in each exam
for ex in exams:
    mc_idx = 0
    for v in ex["vragen"]:
        if v["type"] == "mc":
            opts = v["opties"]
            ans = v["antwoord"]
            target = mc_idx % len(opts)
            mc_idx += 1
            if target != ans:
                correct = opts[ans]
                other = opts[target]
                opts[target] = correct
                opts[ans] = other
                v["antwoord"] = target

base_dir = "havo3/wiskunde/js/data"
for i, ex in enumerate(exams, start=6):
    fn = f"{base_dir}/examen_{i}.js"
    content = f"/* =========================================================\n" \
              f"   Duru's Wiskunde (HAVO 3) — {ex['titel']}\n" \
              f"   ========================================================= */\n" \
              f"DURU.registerExamen(\n" + json.dumps(ex, indent=2, ensure_ascii=False) + "\n);\n"
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {fn} ({len(ex['vragen'])} vragen)")

