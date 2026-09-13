/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 32 — Toets 32 — §1.3 Kracht en versnelling — Toets A
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-32",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Toets 32 — §1.3 Kracht en versnelling — Toets A",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚀",
  "duurMin": 30,
  "vragen": [
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
        "type": "waaronwaar",
        "vraag": "Als de resulterende kracht in dezelfde richting wijst als de beweging, versnelt het voorwerp.",
        "antwoord": true,
        "uitleg": "Waar. Fres in de bewegingsrichting zorgt voor een toename van de snelheid."
    },
    {
        "type": "waaronwaar",
        "vraag": "Bij een zwaardere curlingsteen is een grotere spierkracht nodig om hem dezelfde beginsnelheid te geven.",
        "antwoord": true,
        "uitleg": "Waar. Meer massa vereist volgens F = m · a evenredig meer kracht om dezelfde versnelling te bereiken."
    },
    {
        "type": "waaronwaar",
        "vraag": "In de formule Fres = m · a mag je de massa m ook direct in grammen invullen.",
        "antwoord": false,
        "uitleg": "Onwaar. Massa moet altijd in kilogram (kg) worden omgerekend, anders klopt de eenheid newton niet."
    },
    {
        "type": "waaronwaar",
        "vraag": "Kracht is precies hetzelfde begrip als versnelling.",
        "antwoord": false,
        "uitleg": "Onwaar. Kracht (in newton) is de oorzaak van de versnelling (in m/s²), gekoppeld via de massa van het voorwerp."
    },
    {
        "type": "invul",
        "vraag": "Een doos met een massa van 5,0 kg wordt versneld met 4,0 m/s². De benodigde resulterende kracht is ... N.",
        "antwoord": "20",
        "uitleg": "Fres = m · a = 5,0 kg × 4,0 m/s² = 20 N."
    },
    {
        "type": "invul",
        "vraag": "Een kracht van 125 N veroorzaakt een versnelling van 0,75 m/s². De massa van het voorwerp is afgerond ... kg.",
        "antwoord": "167",
        "uitleg": "m = Fres / a = 125 / 0,75 = 166,67 ≈ 167 kg (tabel opdracht 37)."
    },
    {
        "type": "open",
        "vraag": "Leg uit waarom het met iemand achterop de fiets veel zwaarder is om vanuit stilstand weg te rijden dan wanneer je alleen op de fiets zit.",
        "sleutelwoorden": [
            "massa/grotere massa/meer gewicht",
            "spierkracht/meer kracht nodig/grotere trapkracht"
        ],
        "minTreffers": 2,
        "modelantwoord": "De totale massa is veel groter. Volgens F = m · a is er bij een grotere massa veel meer spierkracht nodig om dezelfde versnelling te krijgen.",
        "uitleg": "Een grotere massa vereist meer kracht om op gang te komen."
    },
    {
        "type": "open",
        "vraag": "Een slee van 25 kg ondervindt 75 N netto voortstuwende trekkracht. Bereken de resulterende versnelling.",
        "sleutelwoorden": [
            "3 m/s²",
            "3,0",
            "fres/a = fres/berekening"
        ],
        "minTreffers": 1,
        "modelantwoord": "a = Fres / m = 75 N / 25 kg = 3,0 m/s².",
        "uitleg": "a = F / m = 75 / 25 = 3,0 m/s²."
    }
]
});
