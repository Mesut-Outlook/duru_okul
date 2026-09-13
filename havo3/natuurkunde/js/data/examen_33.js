/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 33 — Toets 33 — §1.3 Kracht en versnelling — Toets B
   Gebaseerd op Overal Natuurkunde 3 HAVO (Hoofdstuk 1 Kracht en beweging)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-33",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Toets 33 — §1.3 Kracht en versnelling — Toets B",
  "vak": "Natuurkunde · HAVO 3 (H1)",
  "icoon": "🚀",
  "duurMin": 30,
  "vragen": [
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
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
    {
        "type": "waaronwaar",
        "vraag": "Als twee voorwerpen elkaar wegduwen, oefenen ze altijd een even grote kracht op elkaar uit.",
        "antwoord": true,
        "uitleg": "Waar. Dit is de derde wet van Newton (actie = reactie)."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een auto met een massa van 1000 kg heeft een twee keer zo grote remkracht nodig als een auto van 500 kg om dezelfde vertraging te behalen.",
        "antwoord": true,
        "uitleg": "Waar. F = m · a: bij gelijke versnelling a is de benodigde kracht recht evenredig met de massa."
    },
    {
        "type": "waaronwaar",
        "vraag": "Als er een constante resulterende kracht op een voorwerp werkt, beweegt het voorwerp met constante snelheid.",
        "antwoord": false,
        "uitleg": "Onwaar. Een constante resulterende kracht levert een constante versnelling op, waardoor de snelheid voortdurend toeneemt."
    },
    {
        "type": "waaronwaar",
        "vraag": "Om een zware vrachtwagen en een lichte brommer even snel te laten remmen is voor beide evenveel remkracht nodig.",
        "antwoord": false,
        "uitleg": "Onwaar. De vrachtwagen heeft een veel grotere massa en vereist volgens F = m · a veel meer remkracht voor dezelfde vertraging."
    },
    {
        "type": "invul",
        "vraag": "Als een kracht van 60 N een voorwerp versnelt met 3,0 m/s², dan is de massa van het voorwerp ... kg.",
        "antwoord": "20",
        "uitleg": "m = F / a = 60 / 3,0 = 20 kg."
    },
    {
        "type": "invul",
        "vraag": "Een bal van 0,20 kg krijgt bij het wegslaan een versnelling van 50 m/s². De uitgeoefende slagkracht is ... N.",
        "antwoord": "10",
        "uitleg": "F = m · a = 0,20 kg × 50 m/s² = 10 N."
    },
    {
        "type": "open",
        "vraag": "Waarom beweegt bij het tegen elkaar wegduwen op het ijs de persoon met de kleinste massa sneller naar achteren dan de zwaardere persoon?",
        "sleutelwoorden": [
            "is gelijk/kracht gelijk/even groot",
            "versnelling groter bij kleine massa/omgekeerd evenredig"
        ],
        "minTreffers": 2,
        "modelantwoord": "De kracht op beiden is gelijk (actie is reactie). Omdat versnelling omgekeerd evenredig is met de massa (a = F/m), krijgt degene met minder massa een grotere versnelling en dus meer snelheid.",
        "uitleg": "Gelijke kracht levert bij minder massa een grotere versnelling op."
    },
    {
        "type": "open",
        "vraag": "Een motorblok levert 4500 N aandrijfkracht aan een racewagen van 900 kg. De totale tegenkrachten bedragen 900 N. Bepaal de versnelling.",
        "sleutelwoorden": [
            "4 m/s²",
            "4,0",
            "3600 N"
        ],
        "minTreffers": 1,
        "modelantwoord": "Fres = 4500 - 900 = 3600 N. a = Fres / m = 3600 / 900 = 4,0 m/s².",
        "uitleg": "Fres = 3600 N. a = 3600 / 900 = 4,0 m/s²."
    }
]
});
