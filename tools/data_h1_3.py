# -*- coding: utf-8 -*-
"""
Hoofdstuk 1 — §1.3 Kracht en versnelling (Toets 32, 33, 34)
"""

# -------------------------------------------------------------
# TOETS 32: §1.3 Kracht en versnelling — Toets A
# -------------------------------------------------------------
q32 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "Wat is de wiskundige formule van de tweede wet van Newton die het verband tussen kracht, massa en versnelling beschrijft?",
        "opties": [
            "Fres = m · a",
            "Fres = m / a",
            "Fres = a / m",
            "Fres = 1/2 · m · a²"
        ],
        "antwoord": 0,
        "uitleg": "De grondformule van de mechanica is Fres = m · a (blz. 22 in het theorieboek)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "In welke standaardeenheid (SI-eenheid) moet de massa m altijd worden ingevuld in de formule Fres = m · a?",
        "opties": [
            "Gram (g)",
            "Kilogram (kg)",
            "Ton (t)",
            "Milligram (mg)"
        ],
        "antwoord": 1,
        "uitleg": "In formules in het SI-stelsel moet massa altijd in kilogram (kg) worden ingevuld. Grammen moet je eerst delen door 1000."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Wat gebeurt er met de versnelling van een voorwerp als de resulterende kracht twee keer zo groot wordt, terwijl de massa gelijk blijft?",
        "opties": [
            "De versnelling wordt gehalveerd",
            "De versnelling blijft precies hetzelfde",
            "De versnelling wordt twee keer zo groot",
            "De versnelling wordt vier keer zo groot"
        ],
        "antwoord": 2,
        "uitleg": "Kracht en versnelling zijn recht evenredig bij een constante massa: als Fres verdubbelt, verdubbelt ook de versnelling a."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Wat gebeurt er met de versnelling als je dezelfde kracht uitoefent op een voorwerp met een twee keer zo grote massa?",
        "opties": [
            "De versnelling verdubbelt",
            "De versnelling blijft gelijk",
            "De versnelling wordt vier keer zo klein",
            "De versnelling wordt gehalveerd"
        ],
        "antwoord": 3,
        "uitleg": "Massa en versnelling zijn omgekeerd evenredig bij gelijke kracht: a = Fres / m. Een twee keer zo grote massa levert de helft van de versnelling op (blz. 22)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Een sprinter met een massa van 80 kg ondervindt bij de start een resulterende voorwaartse kracht van 320 N. Wat is zijn versnelling?",
        "opties": [
            "4,0 m/s²",
            "25 600 m/s²",
            "0,25 m/s²",
            "240 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "a = Fres / m = 320 N / 80 kg = 4,0 m/s²."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Een optrekkende trein heeft een massa van 50 000 kg. De motorkracht is 40 kN (40 000 N) en de tegenwerkende weerstandskracht is 5000 N. Hoe groot is de versnelling van de trein?",
        "opties": [
            "0,80 m/s²",
            "0,70 m/s²",
            "0,90 m/s²",
            "1,43 m/s²"
        ],
        "antwoord": 1,
        "uitleg": "Fres = Fmotor - Fw = 40 000 N - 5000 N = 35 000 N. a = Fres / m = 35 000 / 50 000 = 0,70 m/s² (voorbeeld 7 op blz. 22)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Hoe groot is de snelheid van deze trein na 6,0 seconden als hij eenparig versnelt met 0,70 m/s² vanuit stilstand?",
        "opties": [
            "2,1 m/s",
            "8,57 m/s",
            "4,2 m/s",
            "12,6 m/s"
        ],
        "antwoord": 2,
        "uitleg": "v = a · t = 0,70 m/s² × 6,0 s = 4,2 m/s (voorbeeld 7b)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Sid schopt met een kracht van 50 N tegen een voetbal met een massa van 370 g. Hoe reken je de versnelling van de bal correct uit?",
        "opties": [
            "a = 50 / 370 = 0,14 m/s²",
            "a = 50 × 0,370 = 18,5 m/s²",
            "a = 370 / 50 = 7,4 m/s²",
            "Eerst massa omrekenen naar 0,370 kg, dan a = 50 / 0,370 = 135 m/s²"
        ],
        "antwoord": 3,
        "uitleg": "Massa moet in kg: 370 g = 0,370 kg. Dan a = Fres / m = 50 / 0,370 = 135 m/s² (zie opdracht 36a uit het boek)."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Conny en Sarah duwen samen een bobslee vooruit. Beiden oefenen 200 N uit. De schuifwrijving is 50 N. De bobslee weegt 250 kg. Wat is de versnelling?",
        "opties": [
            "1,4 m/s²",
            "1,6 m/s²",
            "0,60 m/s²",
            "2,5 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "Fvooruit = 200 + 200 = 400 N. Fres = 400 - 50 = 350 N. a = Fres / m = 350 / 250 = 1,4 m/s² (opdracht 36b)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Waarom vegen curlingers met bezems het ijs vlak voor een glijdende curlingsteen schoon?",
        "opties": [
            "Om het ijs af te koelen zodat de steen sneller stopt",
            "Om de schuifwrijvingskracht te verminderen zodat de steen minder vertraagt en verder glijdt",
            "Om de steen magnetisch aan te trekken",
            "Om de massa van de curlingsteen lichter te maken"
        ],
        "antwoord": 1,
        "uitleg": "Door het vegen ontstaat een dun waterlaagje dat de wrijving verlaagt. De tegenwerkende wrijvingskracht wordt kleiner, waardoor de vertraging afneemt (blz. 21 figuur 1.14)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Een zware goederentrein van 700 000 kg rijdt met een motorkracht van 35 kN (35 000 N) een station uit (weerstand verwaarloosbaar). Wat is zijn versnelling?",
        "opties": [
            "0,50 m/s²",
            "0,20 m/s²",
            "0,05 m/s²",
            "2,0 m/s²"
        ],
        "antwoord": 2,
        "uitleg": "a = Fres / m = 35 000 N / 700 000 kg = 0,05 m/s² (opdracht 38a)."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Hoe groot is de snelheid van deze goederentrein na 60 seconden optrekken met a = 0,05 m/s²?",
        "opties": [
            "30 m/s",
            "12 m/s",
            "1,2 m/s",
            "3,0 m/s"
        ],
        "antwoord": 3,
        "uitleg": "v = a · t = 0,05 m/s² × 60 s = 3,0 m/s (ongeveer 10,8 km/h, opdracht 38b)."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Als de resulterende kracht in dezelfde richting wijst als de beweging, versnelt het voorwerp.",
        "antwoord": True,
        "uitleg": "Waar. Fres in de bewegingsrichting zorgt voor een toename van de snelheid."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Bij een zwaardere curlingsteen is een grotere spierkracht nodig om hem dezelfde beginsnelheid te geven.",
        "antwoord": True,
        "uitleg": "Waar. Meer massa vereist volgens F = m · a evenredig meer kracht om dezelfde versnelling te bereiken."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "In de formule Fres = m · a mag je de massa m ook direct in grammen invullen.",
        "antwoord": False,
        "uitleg": "Onwaar. Massa moet altijd in kilogram (kg) worden omgerekend, anders klopt de eenheid newton niet."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Kracht is precies hetzelfde begrip als versnelling.",
        "antwoord": False,
        "uitleg": "Onwaar. Kracht (in newton) is de oorzaak van de versnelling (in m/s²), gekoppeld via de massa van het voorwerp."
    },
    { # 17
        "type": "invul",
        "vraag": "Een doos met een massa van 5,0 kg wordt versneld met 4,0 m/s². De benodigde resulterende kracht is ... N.",
        "antwoord": "20",
        "uitleg": "Fres = m · a = 5,0 kg × 4,0 m/s² = 20 N."
    },
    { # 18
        "type": "invul",
        "vraag": "Een kracht van 125 N veroorzaakt een versnelling van 0,75 m/s². De massa van het voorwerp is afgerond ... kg.",
        "antwoord": "167",
        "uitleg": "m = Fres / a = 125 / 0,75 = 166,67 ≈ 167 kg (tabel opdracht 37)."
    },
    { # 19
        "type": "open",
        "vraag": "Leg uit waarom het met iemand achterop de fiets veel zwaarder is om vanuit stilstand weg te rijden dan wanneer je alleen op de fiets zit.",
        "sleutelwoorden": ["massa groter/meer gewicht", "grotere trapkracht nodig/meer kracht nodig"],
        "minTreffers": 2,
        "modelantwoord": "De totale massa is veel groter. Volgens F = m · a is er bij een grotere massa veel meer spierkracht nodig om dezelfde versnelling te krijgen.",
        "uitleg": "Een grotere massa vereist meer kracht om op gang te komen."
    },
    { # 20
        "type": "open",
        "vraag": "Een slee van 25 kg ondervindt 75 N netto voortstuwende trekkracht. Bereken de resulterende versnelling.",
        "sleutelwoorden": ["3 m/s²", "3,0", "3 meter per seconde kwadraat"],
        "minTreffers": 1,
        "modelantwoord": "a = Fres / m = 75 N / 25 kg = 3,0 m/s².",
        "uitleg": "a = F / m = 75 / 25 = 3,0 m/s²."
    }
]

# -------------------------------------------------------------
# TOETS 33: §1.3 Kracht en versnelling — Toets B
# -------------------------------------------------------------
q33 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "Schaatsster Salomi (massa 60 kg) schaatst met 8,0 m/s en remt af met een remkracht van 100 N voor een wak in het ijs. Hoe groot is haar vertraging?",
        "opties": [
            "1,67 m/s²",
            "0,60 m/s²",
            "6,0 m/s²",
            "4,8 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "a = Fres / m = 100 N / 60 kg = 1,67 m/s² (zie opdracht 39a uit het theorieboek)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Hoeveel seconden duurt het voordat Salomi volledig stilstaat (beginsnelheid 8,0 m/s, vertraging 1,67 m/s²)?",
        "opties": [
            "2,4 s",
            "4,8 s",
            "13,3 s",
            "8,0 s"
        ],
        "antwoord": 1,
        "uitleg": "t = Δv / a = 8,0 / 1,67 = 4,8 s (opdracht 39b)."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Wat is Salomi's remweg als haar gemiddelde snelheid tijdens het remmen 4,0 m/s bedraagt en de remtijd 4,8 s is?",
        "opties": [
            "8,0 m",
            "38,4 m",
            "19,2 m",
            "9,6 m"
        ],
        "antwoord": 2,
        "uitleg": "s = vgem · t = 4,0 m/s × 4,8 s = 19,2 m (opdracht 39d)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Een bal met een massa van 0,50 kg valt naar beneden. De zwaartekracht is Fz = m · g = 4,9 N en de gemiddelde luchtweerstand is 1,5 N. Wat is de versnelling van de bal?",
        "opties": [
            "9,81 m/s²",
            "3,0 m/s²",
            "12,8 m/s²",
            "6,8 m/s²"
        ],
        "antwoord": 3,
        "uitleg": "Fres = Fz - Fw = 4,9 N - 1,5 N = 3,4 N. a = Fres / m = 3,4 N / 0,50 kg = 6,8 m/s² (opdracht 40b)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Waarom staat in opdracht 40 dat de luchtweerstandskracht 'gemiddeld' 1,5 N is?",
        "opties": [
            "Omdat de luchtweerstand toeneemt naarmate de bal sneller valt",
            "Omdat de zwaartekracht tijdens de val steeds kleiner wordt",
            "Omdat de massa van de bal tijdens de val verandert",
            "Omdat de bal steeds van vorm verandert"
        ],
        "antwoord": 0,
        "uitleg": "Luchtweerstand hangt direct af van de snelheid. Als de bal versnelt, stijgt de luchtweerstand continu, vandaar de gemiddelde waarde (opdracht 40c)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Corey fietst met zijn fiets (gezamenlijke massa 70 kg) weg bij een stoplicht en bereikt in 5,0 s een snelheid van 18 km/h (5,0 m/s). Wat is de gemiddelde resulterende kracht?",
        "opties": [
            "350 N",
            "70 N",
            "14 N",
            "18 N"
        ],
        "antwoord": 1,
        "uitleg": "a = Δv / t = 5,0 / 5,0 = 1,0 m/s². Fres = m · a = 70 kg × 1,0 m/s² = 70 N (opdracht 41a)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Hoeveel meter legt Corey af tijdens deze 5,0 seconden van wegfietsen (vbegin = 0 m/s, veind = 5,0 m/s)?",
        "opties": [
            "25 m",
            "5,0 m",
            "12,5 m",
            "70 m"
        ],
        "antwoord": 2,
        "uitleg": "vgem = (0 + 5,0)/2 = 2,5 m/s. Afstand s = vgem · t = 2,5 m/s × 5,0 s = 12,5 m (opdracht 41c)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Gordon (80 kg) en Giada (60 kg) staan op glad ijs en duwen elkaar met een kracht van 50 N weg. Wat kun je zeggen over de krachten die zij op elkaar uitoefenen?",
        "opties": [
            "Gordon oefent meer kracht uit omdat hij zwaarder is",
            "Giada oefent meer kracht uit omdat ze harder wegschiet",
            "Er werkt alleen kracht op Giada",
            "De kracht op Gordon en de kracht op Giada zijn precies even groot (50 N)"
        ],
        "antwoord": 3,
        "uitleg": "Volgens de actie-is-reactiewet oefenen ze precies even grote krachten op elkaar uit (50 N), zie opdracht 42."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Wie krijgt de grootste versnelling als Gordon (80 kg) en Giada (60 kg) elkaar wegduwen?",
        "opties": [
            "Giada, want zij heeft minder massa waardoor a = F / m groter uitvalt",
            "Gordon, want hij heeft meer massa",
            "Ze krijgen precies dezelfde versnelling",
            "Geen van beiden beweegt omdat de krachten elkaar opheffen"
        ],
        "antwoord": 0,
        "uitleg": "a = F / m. Voor Giada: 50 / 60 = 0,83 m/s². Voor Gordon: 50 / 80 = 0,63 m/s². Giada heeft de kleinste massa en dus de grootste versnelling (opdracht 42a)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Wat is de snelheid van Giada na 2,0 seconden wegduwen met a = 0,83 m/s²?",
        "opties": [
            "1,25 m/s",
            "1,67 m/s",
            "0,83 m/s",
            "3,33 m/s"
        ],
        "antwoord": 1,
        "uitleg": "v = a · t = 0,83 m/s² × 2,0 s = 1,67 m/s (opdracht 42c)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Een auto van 1200 kg versnelt van 10 m/s naar 25 m/s in 6,0 seconden. Wat is de resulterende kracht op de auto?",
        "opties": [
            "1800 N",
            "2500 N",
            "3000 N",
            "5000 N"
        ],
        "antwoord": 2,
        "uitleg": "a = (25 - 10) / 6,0 = 15 / 6,0 = 2,5 m/s². Fres = m · a = 1200 kg × 2,5 m/s² = 3000 N (opdracht 43a/b)."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Als op deze auto tijdens het optrekken een luchtweerstand van 650 N werkt, hoe groot moet de motorkracht dan zijn?",
        "opties": [
            "2350 N",
            "3000 N",
            "650 N",
            "3650 N"
        ],
        "antwoord": 3,
        "uitleg": "Fres = Fmotor - Fw. Dus Fmotor = Fres + Fw = 3000 N + 650 N = 3650 N (opdracht 43b)."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Als twee voorwerpen elkaar wegduwen, oefenen ze altijd een even grote kracht op elkaar uit.",
        "antwoord": True,
        "uitleg": "Waar. Dit is de derde wet van Newton (actie = reactie)."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Een auto met een massa van 1000 kg heeft een twee keer zo grote remkracht nodig als een auto van 500 kg om dezelfde vertraging te behalen.",
        "antwoord": True,
        "uitleg": "Waar. F = m · a: bij gelijke versnelling a is de benodigde kracht recht evenredig met de massa."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Als er een constante resulterende kracht op een voorwerp werkt, beweegt het voorwerp met constante snelheid.",
        "antwoord": False,
        "uitleg": "Onwaar. Een constante resulterende kracht levert een constante versnelling op, waardoor de snelheid voortdurend toeneemt."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Om een zware vrachtwagen en een lichte brommer even snel te laten remmen is voor beide evenveel remkracht nodig.",
        "antwoord": False,
        "uitleg": "Onwaar. De vrachtwagen heeft een veel grotere massa en vereist volgens F = m · a veel meer remkracht voor dezelfde vertraging."
    },
    { # 17
        "type": "invul",
        "vraag": "Als een kracht van 60 N een voorwerp versnelt met 3,0 m/s², dan is de massa van het voorwerp ... kg.",
        "antwoord": "20",
        "uitleg": "m = F / a = 60 / 3,0 = 20 kg."
    },
    { # 18
        "type": "invul",
        "vraag": "Een bal van 0,20 kg krijgt bij het wegslaan een versnelling van 50 m/s². De uitgeoefende slagkracht is ... N.",
        "antwoord": "10",
        "uitleg": "F = m · a = 0,20 kg × 50 m/s² = 10 N."
    },
    { # 19
        "type": "open",
        "vraag": "Waarom beweegt bij het tegen elkaar wegduwen op het ijs de persoon met de kleinste massa sneller naar achteren dan de zwaardere persoon?",
        "sleutelwoorden": ["kracht gelijk/even groot", "versnelling groter bij kleine massa/omgekeerd evenredig"],
        "minTreffers": 2,
        "modelantwoord": "De kracht op beiden is gelijk (actie is reactie). Omdat versnelling omgekeerd evenredig is met de massa (a = F/m), krijgt degene met minder massa een grotere versnelling en dus meer snelheid.",
        "uitleg": "Gelijke kracht levert bij minder massa een grotere versnelling op."
    },
    { # 20
        "type": "open",
        "vraag": "Een motorblok levert 4500 N aandrijfkracht aan een racewagen van 900 kg. De totale tegenkrachten bedragen 900 N. Bepaal de versnelling.",
        "sleutelwoorden": ["4 m/s²", "4,0", "3600 N"],
        "minTreffers": 1,
        "modelantwoord": "Fres = 4500 - 900 = 3600 N. a = Fres / m = 3600 / 900 = 4,0 m/s².",
        "uitleg": "Fres = 3600 N. a = 3600 / 900 = 4,0 m/s²."
    }
]

# -------------------------------------------------------------
# TOETS 34: §1.3 Kracht en versnelling — Toets C
# -------------------------------------------------------------
q34 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "Andy Green verbrak in 1997 het wereldsnelheidsrecord op land met de ThrustSSC (1228 km/h). Waarom had zijn voertuig straalmotoren met enorme stuwkracht nodig?",
        "opties": [
            "Omdat bij 1228 km/h de tegenwerkende luchtweerstand gigantisch groot is en overwonnen moet worden",
            "Omdat de zwaartekracht op recordauto's twee keer zo zwaar drukt",
            "Omdat straalmotoren als enige geen rolweerstand ondervinden",
            "Omdat het voertuig anders direct zou opstijgen"
        ],
        "antwoord": 0,
        "uitleg": "Bij 1228 km/h is de luchtweerstand enorm. Om toch nog een resulterende voorwaartse kracht en versnelling te houden, zijn krachtige straalmotoren nodig (blz. 21)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Bij het honkballen (opdracht 44) oefent Jeff bij de worp 0,096 s lang een kracht uit op een bal van 145 g (0,145 kg). De bal bereikt een snelheid van 20 m/s. Wat is de versnelling van de bal tijdens de worp?",
        "opties": [
            "20 m/s²",
            "208 m/s²",
            "1,92 m/s²",
            "138 m/s²"
        ],
        "antwoord": 1,
        "uitleg": "a = Δv / t = 20 m/s / 0,096 s = 208,3 ≈ 208 m/s² (opdracht 44a)."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Hoe groot is de kracht die Jeff tijdens de worp op deze honkbal uitoefent (m = 0,145 kg, a = 208 m/s²)?",
        "opties": [
            "2,9 N",
            "145 N",
            "30,2 N",
            "43,5 N"
        ],
        "antwoord": 2,
        "uitleg": "F = m · a = 0,145 kg × 208,3 m/s² = 30,2 N (opdracht 44a)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "De slagman raakt de bal. De bal kwam aan met 22 m/s en vliegt met 20 m/s terug in tegenovergestelde richting. Hoe groot is de totale snelheidsverandering Δv van de bal?",
        "opties": [
            "2 m/s",
            "20 m/s",
            "22 m/s",
            "42 m/s"
        ],
        "antwoord": 3,
        "uitleg": "Omdat de bal omdraait van richting, verliest hij eerst 22 m/s tot nul en wint dan 20 m/s in de andere richting: Δv = 22 - (-20) = 42 m/s (opdracht 44c)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Als het slaan van de bal 0,10 s duurt en Δv = 42 m/s is, wat is dan de versnelling tijdens de slag?",
        "opties": [
            "420 m/s²",
            "4,2 m/s²",
            "42 m/s²",
            "840 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "a = Δv / t = 42 m/s / 0,10 s = 420 m/s² (opdracht 44d)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Hoeveel kracht oefent de knuppel uit op de bal van 0,145 kg tijdens de slag met a = 420 m/s²?",
        "opties": [
            "42 N",
            "60,9 N",
            "609 N",
            "145 N"
        ],
        "antwoord": 1,
        "uitleg": "F = m · a = 0,145 kg × 420 m/s² = 60,9 N (opdracht 44e)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Wat gebeurt er als de resulterende kracht loodrecht op de bewegingsrichting van een rijdend voorwerp staat?",
        "opties": [
            "De snelheid wordt nul",
            "De snelheid neemt direct toe",
            "De richting van de beweging verandert (het voorwerp gaat een bocht door)",
            "Het voorwerp vertraagt eenparig"
        ],
        "antwoord": 2,
        "uitleg": "Een kracht loodrecht op de snelheid verandert niet de grootte van de snelheid, maar wel de richting van de beweging (blz. 21)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Een vrachtwagen van 12 000 kg rijdt met 20 m/s. De chauffeur remt met een remkracht van 24 000 N. Wat is de vertraging van de vrachtwagen?",
        "opties": [
            "0,50 m/s²",
            "4,0 m/s²",
            "12 m/s²",
            "2,0 m/s²"
        ],
        "antwoord": 3,
        "uitleg": "a = Fres / m = 24 000 N / 12 000 kg = 2,0 m/s²."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Hoe lang duurt het voordat deze vrachtwagen stilstaat bij een beginsnelheid van 20 m/s en vertraging van 2,0 m/s²?",
        "opties": [
            "10 s",
            "40 s",
            "5 s",
            "20 s"
        ],
        "antwoord": 0,
        "uitleg": "t = Δv / a = 20 m/s / 2,0 m/s² = 10 s."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Wat is de remweg van deze vrachtwagen (beginsnelheid 20 m/s, remtijd 10 s)?",
        "opties": [
            "200 m",
            "100 m",
            "50 m",
            "40 m"
        ],
        "antwoord": 1,
        "uitleg": "vgem = 10 m/s. Remweg s = vgem · t = 10 m/s × 10 s = 100 m."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Waarom zorgt een lichte racefiets voor betere prestaties bergop dan een zware stadsfiets?",
        "opties": [
            "Omdat een lichte fiets geen bandenwrijving heeft",
            "Omdat de zwaartekracht op een lichte fiets omhoog wijst",
            "Omdat bij een kleinere massa volgens a = F / m dezelfde spierkracht een grotere versnelling oplevert",
            "Omdat een lichte fiets sneller zakt in het asfalt"
        ],
        "antwoord": 2,
        "uitleg": "Minder massa betekent bij dezelfde trapkracht meer versnelling en minder zwaartekrachtcomponent langs de helling."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Welke combinatie van grootheden geeft in het SI-stelsel precies 1 newton?",
        "opties": [
            "1 kg · m/s",
            "1 kg / m²",
            "1 N / kg",
            "1 kg · m/s²"
        ],
        "antwoord": 3,
        "uitleg": "Uit F = m · a volgt direct: 1 N = 1 kg × 1 m/s² = 1 kg·m/s²."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Om een rijdende auto een scherpe bocht naar links te laten maken, is een naar links gerichte resulterende kracht nodig.",
        "antwoord": True,
        "uitleg": "Waar. Voor elke richtingsverandering is een kracht nodig naar het middelpunt van de bocht."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Bij een parachutesprong met geopende parachute neemt de luchtweerstand af als de snelheid kleiner wordt.",
        "antwoord": True,
        "uitleg": "Waar. Luchtweerstand is rechtstreeks afhankelijk van de snelheid: trager bewegen betekent minder luchtweerstand."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Als je twee keer zo hard trapt op de fiets, wordt je massa twee keer zo klein.",
        "antwoord": False,
        "uitleg": "Onwaar. De massa van fietser en fiets verandert niet door harder te trappen."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Een versnelling van 0 m/s² betekent dat het voorwerp met de lichtsnelheid beweegt.",
        "antwoord": False,
        "uitleg": "Onwaar. a = 0 m/s² betekent dat de snelheid constant is of dat het voorwerp stilstaat."
    },
    { # 17
        "type": "invul",
        "vraag": "Een kracht van 40 N versnelt een voorwerp met 2,0 m/s². De massa van het voorwerp is ... kg.",
        "antwoord": "20",
        "uitleg": "m = F / a = 40 / 2,0 = 20 kg."
    },
    { # 18
        "type": "invul",
        "vraag": "Een scooterrijder met totale massa van 150 kg remt af met een vertraging van 3,0 m/s². De remkracht is ... N.",
        "antwoord": "450",
        "uitleg": "Fres = m · a = 150 kg × 3,0 m/s² = 450 N."
    },
    { # 19
        "type": "open",
        "vraag": "Noem de drie verschillende effecten die een resulterende kracht kan hebben op de beweging van een voorwerp.",
        "sleutelwoorden": ["versnelling/snelheid toename", "vertraging/afremmen", "richtingsverandering/bocht"],
        "minTreffers": 2,
        "modelantwoord": "De kracht kan zorgen voor een toename van de snelheid (versnelling), een afname van de snelheid (vertraging) of een verandering van richting (bocht).",
        "uitleg": "Kracht kan snelheid vergroten, verkleinen of de richting ombuigen."
    },
    { # 20
        "type": "open",
        "vraag": "Een auto van duizend kilogram accelereert in vijf seconden van stilstand naar twintig meter per seconde. Bereken de benodigde voorwaartse resulterende kracht.",
        "sleutelwoorden": ["4000 N", "4000 newton"],
        "minTreffers": 1,
        "modelantwoord": "a = 20 / 5 = 4,0 m/s². Fres = m · a = 1000 kg × 4,0 m/s² = 4000 N.",
        "uitleg": "a = 4,0 m/s², F = 1000 × 4 = 4000 newton."
    }
]
