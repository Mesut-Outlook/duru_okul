# -*- coding: utf-8 -*-
"""
Hoofdstuk 1 — §1.2 Soorten beweging & Diagrammen (Toets 29, 30, 31)
"""

# -------------------------------------------------------------
# TOETS 29: §1.2 Soorten beweging & Diagrammen — Toets A
# -------------------------------------------------------------
q29 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "Met welke formule bereken je de gemiddelde snelheid (vgem) als de afstand s en de tijdsduur t bekend zijn?",
        "opties": [
            "vgem = s / t",
            "vgem = s · t",
            "vgem = t / s",
            "vgem = 1/2 · s · t²"
        ],
        "antwoord": 0,
        "uitleg": "De gemiddelde snelheid is de afstand gedeeld door de tijd: vgem = s / t (blz. 14 in het theorieboek)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Hoe reken je een snelheid van kilometer per uur (km/h) correct om naar meter per seconde (m/s)?",
        "opties": [
            "Vermenigvuldigen met 3,6",
            "Delen door 3,6",
            "Vermenigvuldigen met 1000",
            "Delen door 60"
        ],
        "antwoord": 1,
        "uitleg": "Omdat 1 km = 1000 m en 1 uur = 3600 s, geldt: 3600 / 1000 = 3,6. Van km/h naar m/s moet je dus altijd delen door 3,6."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Een auto rijdt met 72 km/h over een provinciale weg. Hoeveel meter legt deze auto per seconde af?",
        "opties": [
            "7,2 m/s",
            "259,2 m/s",
            "20 m/s",
            "25 m/s"
        ],
        "antwoord": 2,
        "uitleg": "72 km/h omrekenen naar m/s: 72 / 3,6 = 20 m/s (zie opdracht 23a)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Wat betekent de steilheid (helling) van de grafiek in een (s,t)-diagram?",
        "opties": [
            "De totale massa van het voertuig",
            "De resulterende tegenwerkende kracht",
            "De verstreken tijd tot aan de finish",
            "De snelheid van het voorwerp op dat moment"
        ],
        "antwoord": 3,
        "uitleg": "In een (s,t)-diagram geldt: hoe steiler de lijn loopt, des te meer meters er per seconde worden afgelegd. De steilheid stelt dus de snelheid voor (blz. 14)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Het Formule 1-circuit van Zandvoort is 4259 m lang. Max Verstappen rijdt een ronde in 1 minuut en 20,4 seconden (80,4 s). Wat is zijn gemiddelde snelheid?",
        "opties": [
            "53,0 m/s (ongeveer 191 km/h)",
            "34,2 m/s (ongeveer 123 km/h)",
            "80,4 m/s (ongeveer 289 km/h)",
            "12,5 m/s (ongeveer 45 km/h)"
        ],
        "antwoord": 0,
        "uitleg": "vgem = s / t = 4259 m / 80,4 s = 52,97 m/s ≈ 53,0 m/s (voorbeeld in theorieboek op blz. 14)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Hoe herken je stilstand in een (s,t)-diagram?",
        "opties": [
            "Een stijgende rechte lijn vanuit de oorsprong",
            "Een horizontale rechte lijn (de afstand s verandert niet)",
            "Een dalende rechte lijn naar de tijdas",
            "Een kromme lijn die steeds steiler wordt"
        ],
        "antwoord": 1,
        "uitleg": "Als de afstand s gedurende een tijdinterval gelijk blijft (horizontale lijn), beweegt het voorwerp niet: het staat stil (snelheid v = 0)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Wat stelt de oppervlakte onder de grafiek in een (v,t)-diagram voor?",
        "opties": [
            "De gemiddelde versnelling in m/s²",
            "De benodigde motorkracht in newton",
            "De afgelegde afstand (s) in meters",
            "Het brandstofverbruik in liters"
        ],
        "antwoord": 2,
        "uitleg": "Omdat snelheid × tijd = afstand (m/s × s = m), stelt de oppervlakte onder de grafiek in een (v,t)-diagram precies de afgelegde afstand s voor (blz. 15)."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Een scooter rijdt gedurende 8,0 seconden met een constante snelheid van 6,0 m/s. Hoeveel afstand legt de scooter af?",
        "opties": [
            "14 m",
            "24 m",
            "1,33 m",
            "48 m"
        ],
        "antwoord": 3,
        "uitleg": "Bij constante snelheid bereken je de oppervlakte van de rechthoek: s = v · t = 6,0 m/s × 8,0 s = 48 m."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Een fietser versnelt eenparig vanuit stilstand (0 m/s) in 6,0 seconden naar een eindsnelheid van 8,0 m/s. Hoe bereken je de afgelegde afstand met de oppervlaktemethode?",
        "opties": [
            "Oppervlakte driehoek = 1/2 × basis × hoogte = 1/2 × 6,0 × 8,0 = 24 m",
            "Oppervlakte rechthoek = 6,0 × 8,0 = 48 m",
            "Afstand = eindsnelheid / tijd = 8,0 / 6,0 = 1,33 m",
            "Afstand = 6,0 + 8,0 = 14 m"
        ],
        "antwoord": 0,
        "uitleg": "Bij eenparige versnelling vanuit stilstand vormt de grafiek een driehoek met basis t = 6,0 s en hoogte v = 8,0 m/s: s = 1/2 × 6,0 × 8,0 = 24 m (of s = vgem · t = 4,0 × 6,0 = 24 m)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Wat is sneller: een fietser die 10 m/s rijdt of een brommer die 30 km/h rijdt?",
        "opties": [
            "De brommer met 30 km/h is sneller",
            "De fietser met 10 m/s is sneller (want 10 m/s = 36 km/h)",
            "Ze gaan precies even snel",
            "Dat kun je niet vergelijken omdat de eenheden anders zijn"
        ],
        "antwoord": 1,
        "uitleg": "10 m/s omrekenen naar km/h: 10 × 3,6 = 36 km/h. 36 km/h is sneller dan 30 km/h (zie opdracht 21 uit het boek)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Welke eenheid hoort bij de grootheid versnelling (a)?",
        "opties": [
            "Meter per seconde (m/s)",
            "Newton per kilogram (N/kg)",
            "Meter per seconde kwadraat (m/s²)",
            "Kilometer per uur (km/h)"
        ],
        "antwoord": 2,
        "uitleg": "Versnelling geeft aan hoeveel m/s de snelheid per seconde verandert: (m/s) / s = m/s² (blz. 16)."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Een hardloper rent 1500 m in 5 minuten (300 s). Wat is zijn gemiddelde snelheid in m/s?",
        "opties": [
            "300 m/s",
            "10 m/s",
            "3 m/s",
            "5 m/s"
        ],
        "antwoord": 3,
        "uitleg": "vgem = s / t = 1500 m / 300 s = 5,0 m/s."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "In een (s,t)-diagram stelt een schuine rechte lijn een beweging met constante snelheid voor.",
        "antwoord": True,
        "uitleg": "Waar. Omdat de steilheid constant is, legt het voorwerp in elk gelijk tijdsinterval evenveel meters af."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "De oppervlakte onder een (v,t)-diagram is gelijk aan de afgelegde afstand s.",
        "antwoord": True,
        "uitleg": "Waar. Dit is een fundamentele rekenregel in de natuurkunde: oppervlakte onder (v,t) = afstand."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Om van m/s naar km/h om te rekenen, moet je de waarde delen door 3,6.",
        "antwoord": False,
        "uitleg": "Onwaar. Van m/s naar km/h moet je vermenigvuldigen met 3,6 (bijvoorbeeld 10 m/s × 3,6 = 36 km/h)."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Een horizontale lijn in een (s,t)-diagram betekent dat het voorwerp met constante snelheid doorrijdt.",
        "antwoord": False,
        "uitleg": "Onwaar. In een (s,t)-diagram betekent een horizontale lijn dat de afstand niet verandert: het voorwerp staat stil."
    },
    { # 17
        "type": "invul",
        "vraag": "Reken om: een snelheid van 54 km/h is gelijk aan ... m/s.",
        "antwoord": "15",
        "uitleg": "54 / 3,6 = 15 m/s."
    },
    { # 18
        "type": "invul",
        "vraag": "Een auto rijdt 4,0 seconden met een constante snelheid van 25 m/s. De afgelegde afstand is ... meter.",
        "antwoord": "100",
        "uitleg": "s = v · t = 25 m/s × 4,0 s = 100 m."
    },
    { # 19
        "type": "open",
        "vraag": "Leg uit waarom de omrekenfactor tussen meter per seconde en kilometer per uur precies 3,6 is.",
        "sleutelwoorden": ["1000 meter", "3600 seconden", "delen/verhouding"],
        "minTreffers": 2,
        "modelantwoord": "In één kilometer zit 1000 meter en in één uur zitten 3600 seconden. De verhouding is 3600 / 1000 = 3,6.",
        "uitleg": "1 km = 1000 m en 1 h = 3600 s. Dus 3600 / 1000 = 3,6."
    },
    { # 20
        "type": "open",
        "vraag": "Een wandelaar legt 1800 meter af in 20 minuten tijd. Bereken zijn gemiddelde snelheid in m/s.",
        "sleutelwoorden": ["1,5", "1200 seconden"],
        "minTreffers": 1,
        "modelantwoord": "20 minuten = 20 × 60 = 1200 seconden. vgem = s / t = 1800 m / 1200 s = 1,5 m/s.",
        "uitleg": "Tijd omrekenen naar seconden (1200 s) en dan delen: 1800 / 1200 = 1,5 m/s."
    }
]

# -------------------------------------------------------------
# TOETS 30: §1.2 Soorten beweging & Diagrammen — Toets B
# -------------------------------------------------------------
q30 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "Met welke formule bereken je de versnelling (a) bij een eenparig veranderende snelheid?",
        "opties": [
            "a = Δv / t = (veind - vbegin) / t",
            "a = vgem · t",
            "a = s / t²",
            "a = Δv · t"
        ],
        "antwoord": 0,
        "uitleg": "Versnelling is de snelheidsverandering gedeeld door de benodigde tijd: a = Δv / t = (veind - vbegin) / t (blz. 16)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Een elektrische auto trekt op van 0 naar 100 km/h in 9,0 seconden. Hoe groot is zijn versnelling (neem 100 km/h = 27,8 m/s)?",
        "opties": [
            "11,1 m/s²",
            "3,1 m/s²",
            "0,32 m/s²",
            "27,8 m/s²"
        ],
        "antwoord": 1,
        "uitleg": "Δv = 27,8 - 0 = 27,8 m/s. a = Δv / t = 27,8 / 9,0 = 3,09 ≈ 3,1 m/s² (voorbeeld 6 uit het boek)."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Pieter rijdt op zijn fiets met 1,6 m/s. Op t = 0 s versnelt hij eenparig gedurende 6,0 s tot een snelheid van 7,0 m/s. Wat is Pieters versnelling?",
        "opties": [
            "1,17 m/s²",
            "5,4 m/s²",
            "0,90 m/s²",
            "0,27 m/s²"
        ],
        "antwoord": 2,
        "uitleg": "Δv = veind - vbegin = 7,0 - 1,6 = 5,4 m/s. a = Δv / t = 5,4 / 6,0 = 0,90 m/s² (opdracht 28b)."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "Hoeveel afstand heeft Pieter afgelegd tijdens deze versnelling van 6,0 s (vbegin = 1,6 m/s, veind = 7,0 m/s)?",
        "opties": [
            "9,6 m",
            "16,2 m",
            "42 m",
            "25,8 m"
        ],
        "antwoord": 3,
        "uitleg": "Oppervlakte rechthoek (1,6 × 6 = 9,6 m) + driehoek (1/2 × 6 × 5,4 = 16,2 m) = 9,6 + 16,2 = 25,8 m (of via vgem = (1,6 + 7,0)/2 = 4,3 m/s; s = 4,3 × 6 = 25,8 m)."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "In figuur 1.12a uit het boek remt een voorwerp af van 6,0 m/s naar 2,0 m/s in 6,0 s. Wat is de vertraging van dit voorwerp?",
        "opties": [
            "0,67 m/s²",
            "4,0 m/s²",
            "1,0 m/s²",
            "0,33 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "Δv = veind - vbegin = 2,0 - 6,0 = -4,0 m/s. a = -4,0 / 6,0 = -0,67 m/s². De vertraging is dus 0,67 m/s² (zie voorbeeld 5 op blz. 17)."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "In een (s,t)-diagram zie je een kromme lijn die steeds minder steil omhoog loopt. Wat voor beweging stelt dit voor?",
        "opties": [
            "Een versnelde beweging",
            "Een vertraagde beweging (de snelheid neemt af)",
            "Een eenparige beweging",
            "Een voorwerp dat achteruit rijdt"
        ],
        "antwoord": 1,
        "uitleg": "Omdat de helling van de (s,t)-grafiek steeds vlakker (minder steil) wordt, worden er per seconde steeds minder meters afgelegd: de snelheid neemt af (vertraagd)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Reken 90 km/h om naar m/s.",
        "opties": [
            "324 m/s",
            "9 m/s",
            "25 m/s",
            "30 m/s"
        ],
        "antwoord": 2,
        "uitleg": "90 / 3,6 = 25 m/s."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Een vliegtuig vliegt met 900 km/h op 10 km hoogte. Waarom vliegen verkeersvliegtuigen bij voorkeur op zo'n grote hoogte?",
        "opties": [
            "Omdat de zwaartekracht daar nul is",
            "Omdat de motoren daar warmer blijven",
            "Omdat de aarde daar sneller onder het vliegtuig doordraait",
            "Omdat de lucht daar ijler is, waardoor de luchtweerstand veel kleiner is en brandstof wordt bespaard"
        ],
        "antwoord": 3,
        "uitleg": "Op 10 km hoogte is de dichtheid van de lucht veel kleiner (ijlere lucht). Daardoor is de luchtweerstandskracht veel kleiner en kan met minder brandstof snel worden gevlogen (zie opdracht 30b)."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "In een (v,t)-diagram is de grafiek een rechte lijn van (t = 0 s, v = 0 m/s) naar (t = 6 s, v = 24 m/s). Wat is de versnelling?",
        "opties": [
            "4,0 m/s²",
            "144 m/s²",
            "0,25 m/s²",
            "24 m/s²"
        ],
        "antwoord": 0,
        "uitleg": "a = Δv / t = (24 - 0) / 6 = 4,0 m/s² (opdracht 25b)."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Hoeveel afstand heeft het voorwerp uit de vorige vraag na 6,0 seconden afgelegd?",
        "opties": [
            "144 m",
            "72 m",
            "24 m",
            "48 m"
        ],
        "antwoord": 1,
        "uitleg": "Oppervlakte onder de driehoek = 1/2 × basis × hoogte = 1/2 × 6,0 s × 24 m/s = 72 m (opdracht 25c)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Als een voorwerp een constante snelheid heeft, wat is dan de waarde van zijn versnelling a?",
        "opties": [
            "Gelijk aan de lichtsnelheid",
            "Gelijk aan 9,81 m/s²",
            "a = 0 m/s²",
            "Dat hangt af van het gewicht van het voorwerp"
        ],
        "antwoord": 2,
        "uitleg": "Bij een constante snelheid is er geen snelheidsverandering (Δv = 0). De versnelling a = Δv / t is dus altijd 0 m/s²."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Een trein rijdt 180 km in 1,5 uur tijd. Wat is zijn gemiddelde snelheid?",
        "opties": [
            "270 km/h",
            "60 km/h",
            "90 km/h",
            "120 km/h"
        ],
        "antwoord": 3,
        "uitleg": "vgem = s / t = 180 km / 1,5 h = 120 km/h."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "Een versnelling van 2,5 m/s² betekent dat de snelheid van het voorwerp elke seconde met 2,5 m/s toeneemt.",
        "antwoord": True,
        "uitleg": "Waar. Dit is de exacte natuurkundige betekenis van de eenheid m/s²: meter per seconde toename per seconde."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Als de eindsnelheid kleiner is dan de beginsnelheid, is de snelheidsverandering Δv negatief en is er sprake van vertraging.",
        "antwoord": True,
        "uitleg": "Waar. Δv = veind - vbegin < 0 duidt op afremmen of vertraging."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Bij een eenparig versnelde beweging vanuit stilstand bereken je de afstand door simpelweg veind met t te vermenigvuldigen.",
        "antwoord": False,
        "uitleg": "Onwaar. Dan neem je de oppervlakte van een rechthoek. Bij versnelling vanuit stilstand vormt de grafiek een driehoek: s = 1/2 · veind · t."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Een snelheid van 20 m/s is langzamer dan een snelheid van 50 km/h.",
        "antwoord": False,
        "uitleg": "Onwaar. 20 m/s = 20 × 3,6 = 72 km/h. 72 km/h is aanzienlijk sneller dan 50 km/h."
    },
    { # 17
        "type": "invul",
        "vraag": "Een motorrijder accelereert in 4,0 seconden van stilstand naar 28 m/s. Zijn versnelling is ... m/s².",
        "antwoord": "7",
        "uitleg": "a = Δv / t = 28 / 4,0 = 7,0 m/s²."
    },
    { # 18
        "type": "invul",
        "vraag": "Reken om: 120 km/h is gelijk aan ... m/s (afgerond op één decimaal).",
        "antwoord": "33,3",
        "uitleg": "120 / 3,6 = 33,33... ≈ 33,3 m/s."
    },
    { # 19
        "type": "open",
        "vraag": "Geef de twee formules waarmee je de afgelegde afstand kunt berekenen bij een eenparig versnelde beweging vanuit rust.",
        "sleutelwoorden": ["1/2 * basis * hoogte/oppervlakte driehoek", "vgem * t/gemiddelde snelheid"],
        "minTreffers": 1,
        "modelantwoord": "s = 1/2 · t · veind (oppervlakte van de driehoek) of s = vgem · t (waarbij vgem = 1/2 · veind).",
        "uitleg": "Beide methodes zijn gelijkwaardig en leveren dezelfde afstand op."
    },
    { # 20
        "type": "open",
        "vraag": "Een auto remt af van 24 m/s naar stilstand in een tijdsduur van 6,0 seconden. Bereken hoe sterk de auto afremt (de snelheidsvermindering per seconde) en noteer de bijbehorende eenheid.",
        "sleutelwoorden": ["4 m/s²", "4,0", "vertraging"],
        "minTreffers": 1,
        "modelantwoord": "a = (24 - 0) / 6,0 = 4,0 m/s².",
        "uitleg": "Snelheidsvermindering van 24 m/s gedeeld door 6,0 s levert een vertraging van 4,0 m/s² op."
    }
]

# -------------------------------------------------------------
# TOETS 31: §1.2 Soorten beweging & Diagrammen — Toets C
# -------------------------------------------------------------
q31 = [
    { # 1 (A)
        "type": "mc",
        "vraag": "In figuur 1.7 van het boek bestaat een beweging uit twee delen: interval 1 (0 tot 2 s, van 0 naar 10 m) en interval 2 (2 tot 6 s, van 10 naar 15 m). Wat is de snelheid in interval 1?",
        "opties": [
            "5,0 m/s",
            "1,25 m/s",
            "10 m/s",
            "2,5 m/s"
        ],
        "antwoord": 0,
        "uitleg": "v1 = s / t = 10 m / 2,0 s = 5,0 m/s (zie voorbeeld 3 op blz. 15 van het theorieboek)."
    },
    { # 2 (B)
        "type": "mc",
        "vraag": "Wat is de snelheid van dezelfde beweging in interval 2 (van 2 tot 6 s, waarin de afstand toeneemt van 10 naar 15 m)?",
        "opties": [
            "5,0 m/s",
            "1,25 m/s",
            "3,75 m/s",
            "0,80 m/s"
        ],
        "antwoord": 1,
        "uitleg": "Δs = 15 - 10 = 5,0 m en Δt = 6,0 - 2,0 = 4,0 s. v2 = 5,0 / 4,0 = 1,25 m/s (voorbeeld 3b)."
    },
    { # 3 (C)
        "type": "mc",
        "vraag": "Wat is de totale gemiddelde snelheid over de gehele beweging van 0 tot 6,0 seconden (totale afstand 15 m)?",
        "opties": [
            "3,13 m/s",
            "5,0 m/s",
            "2,5 m/s",
            "1,25 m/s"
        ],
        "antwoord": 2,
        "uitleg": "vgem,totaal = stotaal / ttotaal = 15 m / 6,0 s = 2,5 m/s."
    },
    { # 4 (D)
        "type": "mc",
        "vraag": "In opdracht 26 fietsen Peter en Yvonne naar hun werk. Peter fietst met 18 m/s en Yvonne met 13 m/s. Wat moet je als eerste doen als de tijd op de x-as in minuten is gegeven?",
        "opties": [
            "De snelheid delen door 60",
            "De afstand direct schatten zonder omrekenen",
            "De snelheid vermenigvuldigen met 3,6",
            "De tijd in minuten omrekenen naar seconden (vermenigvuldigen met 60)"
        ],
        "antwoord": 3,
        "uitleg": "Omdat de snelheid in meter per seconde (m/s) staat, moet de tijd in seconden staan: 1 minuut = 60 s."
    },
    { # 5 (A)
        "type": "mc",
        "vraag": "Een sprinter trekt in 2,5 seconden op van 0 naar 10 m/s. Hoeveel meter legt hij in deze 2,5 seconden af?",
        "opties": [
            "12,5 m",
            "25 m",
            "4 m",
            "8 m"
        ],
        "antwoord": 0,
        "uitleg": "s = 1/2 · t · veind = 1/2 × 2,5 s × 10 m/s = 12,5 m."
    },
    { # 6 (B)
        "type": "mc",
        "vraag": "Waarom is de grafiek van een optrekkende auto in een (s,t)-diagram een kromme lijn die steeds steiler omhoog buigt?",
        "opties": [
            "Omdat de auto steeds zwaarder wordt",
            "Omdat de snelheid toeneemt, waardoor er per seconde steeds meer meters worden afgelegd",
            "Omdat de wrijving met het asfalt toeneemt",
            "Omdat de klok sneller gaat lopen"
        ],
        "antwoord": 1,
        "uitleg": "In een (s,t)-diagram is de steilheid de snelheid. Als de auto versnelt, wordt de snelheid groter en dus wordt de grafiek steeds steiler (blz. 16)."
    },
    { # 7 (C)
        "type": "mc",
        "vraag": "Een auto rijdt met 108 km/h. Hoeveel meter legt deze auto af in 0,80 seconden reactietijd?",
        "opties": [
            "86,4 m",
            "30 m",
            "24 m",
            "18 m"
        ],
        "antwoord": 2,
        "uitleg": "108 km/h = 108 / 3,6 = 30 m/s. Afstand s = v · t = 30 m/s × 0,80 s = 24 m."
    },
    { # 8 (D)
        "type": "mc",
        "vraag": "Wat gebeurt er met de versnelling als de snelheid van een voorwerp in een (v,t)-diagram volgens een rechte stijgende lijn toeneemt?",
        "opties": [
            "De versnelling neemt elke seconde toe",
            "De versnelling neemt elke seconde af",
            "De versnelling is exact gelijk aan nul",
            "De versnelling is constant"
        ],
        "antwoord": 3,
        "uitleg": "Een rechte lijn in een (v,t)-diagram betekent dat de helling constant is. De versnelling a is dus constant (eenparig versneld)."
    },
    { # 9 (A)
        "type": "mc",
        "vraag": "Een goederentrein remt af met een constante vertraging van 0,50 m/s². De beginsnelheid is 20 m/s. Hoeveel seconden duurt het voordat de trein stilstaat?",
        "opties": [
            "40 s",
            "10 s",
            "20 s",
            "5 s"
        ],
        "antwoord": 0,
        "uitleg": "t = Δv / a = 20 m/s / 0,50 m/s² = 40 s."
    },
    { # 10 (B)
        "type": "mc",
        "vraag": "Welke afstand legt deze goederentrein af tijdens het remmen (beginsnelheid 20 m/s, remtijd 40 s tot stilstand)?",
        "opties": [
            "800 m",
            "400 m",
            "200 m",
            "100 m"
        ],
        "antwoord": 1,
        "uitleg": "Oppervlakte driehoek = 1/2 × basis × hoogte = 1/2 × 40 s × 20 m/s = 400 m (of vgem = 10 m/s; s = 10 × 40 = 400 m)."
    },
    { # 11 (C)
        "type": "mc",
        "vraag": "Welke van de onderstaande snelheden is het grootst?",
        "opties": [
            "18 km/h",
            "12 m/s",
            "15 m/s",
            "50 km/h"
        ],
        "antwoord": 2,
        "uitleg": "Omrekenen naar km/h: 18 km/h; 12 m/s = 43,2 km/h; 50 km/h; 15 m/s = 15 × 3,6 = 54 km/h. 15 m/s is dus de grootste snelheid."
    },
    { # 12 (D)
        "type": "mc",
        "vraag": "Wat voor lijn zie je in een (v,t)-diagram van een voorwerp dat stilstaat?",
        "opties": [
            "Een verticale lijn langs de y-as",
            "Een stijgende lijn onder een hoek van 45 graden",
            "Een horizontale lijn op hoogte v = 1",
            "Een lijn die precies op de horizontale tijdas ligt (v = 0)"
        ],
        "antwoord": 3,
        "uitleg": "Bij stilstand is v = 0 m/s voor elk tijdstip; de grafiek valt precies samen met de horizontale tijdas."
    },
    { # 13 (Waar)
        "type": "waaronwaar",
        "vraag": "De gemiddelde snelheid van een voorwerp kan berekend worden door de totale afstand te delen door de totale tijd.",
        "antwoord": True,
        "uitleg": "Waar. vgem = stotaal / ttotaal."
    },
    { # 14 (Waar)
        "type": "waaronwaar",
        "vraag": "Bij een eenparig vertraagde beweging tot stilstand is de gemiddelde snelheid gelijk aan de helft van de beginsnelheid.",
        "antwoord": True,
        "uitleg": "Waar. vgem = (vbegin + veind) / 2 = (vbegin + 0) / 2 = 1/2 · vbegin."
    },
    { # 15 (Onwaar)
        "type": "waaronwaar",
        "vraag": "Een voorwerp met een negatieve versnelling beweegt altijd achteruit.",
        "antwoord": False,
        "uitleg": "Onwaar. Een negatieve versnelling betekent dat de voorwaartse snelheid afneemt (vertraging), het voorwerp beweegt nog steeds voorwaarts."
    },
    { # 16 (Onwaar)
        "type": "waaronwaar",
        "vraag": "In een (s,t)-diagram geeft de oppervlakte onder de lijn de versnelling aan.",
        "antwoord": False,
        "uitleg": "Onwaar. In een (s,t)-diagram heeft de oppervlakte onder de lijn geen natuurkundige betekenis; de helling is de snelheid."
    },
    { # 17
        "type": "invul",
        "vraag": "Een fietser rijdt in 2,0 uur een afstand van 36 km. Zijn gemiddelde snelheid is ... km/h.",
        "antwoord": "18",
        "uitleg": "vgem = 36 / 2,0 = 18 km/h."
    },
    { # 18
        "type": "invul",
        "vraag": "Een auto versnelt in 5,0 seconden van 10 m/s naar 25 m/s. De versnelling is ... m/s².",
        "antwoord": "3",
        "uitleg": "a = (25 - 10) / 5,0 = 15 / 5,0 = 3,0 m/s²."
    },
    { # 19
        "type": "open",
        "vraag": "Leg uit hoe je aan de vorm van een lijn in een afstand-tijd-grafiek kunt zien of een beweging eenparig versneld is.",
        "sleutelwoorden": ["steiler omhoog/steeds steiler", "parabool/kromme lijn"],
        "minTreffers": 1,
        "modelantwoord": "De grafiek is een kromme lijn die steeds steiler omhoog loopt omdat de snelheid per seconde toeneemt.",
        "uitleg": "Een toenemende helling betekent een toenemende snelheid."
    },
    { # 20
        "type": "open",
        "vraag": "Een wielrenner fietst met 36 km/h. Bepaal hoeveel meter hij aflegt in tien seconden tijd.",
        "sleutelwoorden": ["100 meter", "100 m"],
        "minTreffers": 1,
        "modelantwoord": "36 km/h = 10 m/s. s = v · t = 10 m/s × 10 s = 100 meter.",
        "uitleg": "Eerst omrekenen naar 10 m/s en dan vermenigvuldigen met 10 s."
    }
]
