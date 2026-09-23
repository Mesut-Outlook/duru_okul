/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 56 — §7.2 Rekenen met energie
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-56",
  "hoofdstuk": 7,
  "paragraaf": "7.2",
  "titel": "Toets 56 — §7.2 Rekenen met energie",
  "vak": "Natuurkunde · HAVO 3 (H7)",
  "icoon": "🧮",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het vermogen van een apparaat?",
      "opties": [
        "De totale hoeveelheid energie die het apparaat ooit heeft gebruikt",
        "De hoeveelheid energie die het apparaat per seconde omzet",
        "Het rendement van het apparaat",
        "De prijs van het apparaat per kWh"
      ],
      "antwoord": 1,
      "uitleg": "Vermogen is de hoeveelheid energie die een apparaat per seconde omzet."
    },
    {
      "type": "mc",
      "vraag": "Wat is de eenheid van vermogen, gelijk aan J/s?",
      "opties": [
        "Kilowattuur (kWh)",
        "Joule (J)",
        "Newton (N)",
        "Watt (W)"
      ],
      "antwoord": 3,
      "uitleg": "1 watt is gelijk aan 1 joule per seconde."
    },
    {
      "type": "mc",
      "vraag": "Een lamp heeft een vermogen van 15 W en brandt 4 uur (14.400 s). Hoeveel energie gebruikt de lamp?",
      "opties": [
        "216.000 J",
        "21.600 J",
        "2.160 J",
        "2.400 J"
      ],
      "antwoord": 0,
      "uitleg": "E = P · t = 15 × 14.400 = 216.000 J."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel joule is 1 kWh?",
      "opties": [
        "3.600 J",
        "36.000 J",
        "3.600.000 J",
        "360.000 J"
      ],
      "antwoord": 2,
      "uitleg": "1 kWh = 1000 Wh = 1000 × 3600 Ws = 3.600.000 J."
    },
    {
      "type": "mc",
      "vraag": "Waarom heeft een ledlamp een hoger rendement dan een gloeilamp?",
      "opties": [
        "Een gloeilamp gebruikt minder energie dan een ledlamp",
        "Een ledlamp zet een groter deel van de energie om in licht in plaats van warmte",
        "Een ledlamp gebruikt helemaal geen elektriciteit",
        "Een ledlamp heeft geen vermogen"
      ],
      "antwoord": 1,
      "uitleg": "Een ledlamp zet een veel groter deel van de energie om in licht (rendement ~50%) dan een gloeilamp (5-10%)."
    },
    {
      "type": "mc",
      "vraag": "Wat is ongeveer het rendement van een gloeilamp?",
      "opties": [
        "5 tot 10%",
        "50%",
        "80%",
        "35 tot 40%"
      ],
      "antwoord": 0,
      "uitleg": "Een gloeilamp heeft een rendement van slechts 5 tot 10%, daarom is hij sinds 2013 uit de handel genomen."
    },
    {
      "type": "mc",
      "vraag": "Welke formule is de juiste formule voor rendement?",
      "opties": [
        "η = P × t",
        "η = E / t",
        "η = Etotaal / Enuttig × 100%",
        "η = Enuttig / Etotaal × 100%"
      ],
      "antwoord": 3,
      "uitleg": "Rendement bereken je met η = Enuttig / Etotaal × 100% (of met vermogens)."
    },
    {
      "type": "mc",
      "vraag": "Wat zegt de wet van behoud van energie?",
      "opties": [
        "Alleen nuttige energie telt mee bij een omzetting",
        "Energie kan bij een omzetting gedeeltelijk verdwijnen",
        "Nuttige en ongewenste energie samen zijn gelijk aan de totale gebruikte energie",
        "Het rendement van een apparaat is altijd 100%"
      ],
      "antwoord": 2,
      "uitleg": "De wet van behoud van energie zegt dat nuttige plus ongewenste energie gelijk is aan de totale gebruikte energie."
    },
    {
      "type": "mc",
      "vraag": "Een apparaat zet in 10 seconden 2000 J energie om. Wat is het vermogen van dit apparaat?",
      "opties": [
        "200 W",
        "20 W",
        "2 W",
        "2000 W"
      ],
      "antwoord": 0,
      "uitleg": "P = E / t = 2000 / 10 = 200 W."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met het rendement van een kerncentrale als de afvalwarmte via een warmtenet wordt gebruikt voor stadsverwarming?",
      "opties": [
        "Het rendement wordt 100%",
        "Het rendement wordt hoger, omdat de afvalwarmte nuttig wordt gebruikt",
        "Het rendement wordt lager",
        "Het rendement blijft precies gelijk"
      ],
      "antwoord": 1,
      "uitleg": "Als je de afvalwarmte nuttig gebruikt in een warmtenet, neemt het percentage nuttig gebruikte energie toe en wordt het rendement hoger."
    },
    {
      "type": "mc",
      "vraag": "Een apparaat heeft een totaal vermogen van 300 W. In 10 seconden levert het 1500 J nuttige energie. Wat is het rendement?",
      "opties": [
        "25%",
        "80%",
        "150%",
        "50%"
      ],
      "antwoord": 3,
      "uitleg": "Pnuttig = 1500/10 = 150 W. η = 150/300 × 100% = 50%."
    },
    {
      "type": "mc",
      "vraag": "Waarom is een rendement van 100% in de praktijk niet haalbaar?",
      "opties": [
        "Omdat de wet van behoud van energie dat verbiedt",
        "Omdat elektriciteit te duur is",
        "Omdat er altijd een deel van de energie wordt omgezet in ongewenste energie",
        "Omdat apparaten altijd stroom uit een stopcontact nodig hebben"
      ],
      "antwoord": 2,
      "uitleg": "Bij elke energieomzetting ontstaat altijd een deel ongewenste energie, waardoor 100% rendement niet haalbaar is."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een spaarlamp heeft een hoger rendement dan een gloeilamp.",
      "antwoord": true,
      "uitleg": "Waar: een spaarlamp heeft een rendement van 35-40%, een gloeilamp slechts 5-10%."
    },
    {
      "type": "waaronwaar",
      "vraag": "Rendement kun je alleen berekenen met energie, nooit met vermogen.",
      "antwoord": false,
      "uitleg": "Onwaar: rendement kun je zowel berekenen met energie (η = Enuttig/Etotaal) als met vermogen (η = Pnuttig/Ptotaal)."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 watt is gelijk aan 1 joule per seconde.",
      "antwoord": true,
      "uitleg": "Waar: de eenheid watt is per definitie gelijk aan joule per seconde."
    },
    {
      "type": "waaronwaar",
      "vraag": "Hoe lager het rendement van een apparaat, hoe minder energie er als ongewenste energie verloren gaat.",
      "antwoord": false,
      "uitleg": "Onwaar: bij een lager rendement gaat juist meer energie verloren als ongewenste energie."
    },
    {
      "type": "invul",
      "vraag": "Het deel van de energie dat nuttig wordt gebruikt, uitgedrukt in procenten, heet het ...",
      "antwoord": "rendement",
      "uitleg": "Dit percentage heet het rendement."
    },
    {
      "type": "invul",
      "vraag": "Een apparaat heeft een vermogen van 250 W en wordt 4 uur gebruikt. Bereken de energie in kWh.",
      "antwoord": "1|1,0",
      "uitleg": "E = P · t = 0,25 kW × 4 h = 1,0 kWh."
    },
    {
      "type": "invul",
      "vraag": "Een verwarmingselement gebruikt 900.000 J in 5 minuten (300 s). Bereken het vermogen in watt.",
      "antwoord": "3000",
      "uitleg": "P = E / t = 900.000 / 300 = 3000 W."
    },
    {
      "type": "open",
      "vraag": "Bereken hoeveel joule 2,5 kWh is.",
      "sleutelwoorden": [
        "9000000"
      ],
      "minTreffers": 1,
      "modelantwoord": "2,5 kWh = 2,5 × 3.600.000 J = 9000000 J.",
      "uitleg": "1 kWh is 3.600.000 J, dus 2,5 kWh is 2,5 × 3.600.000 = 9.000.000 J."
    }
  ]
});
