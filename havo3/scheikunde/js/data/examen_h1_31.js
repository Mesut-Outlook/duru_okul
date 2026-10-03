/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 31 — 1.3 Celsius en kelvin
   Hoofdstuk 1, §1.3: omrekenen tussen graden Celsius en kelvin (°C + 273 = K) en het absolute nulpunt.
   20 vragen · 30 minuten. Gebaseerd op de stof van het boek (eigen voorbeelden en formuleringen).
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h1-31",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Toets 31 — 1.3 Celsius en kelvin",
  "vak": "Scheikunde · HAVO 3 (H1 §1.3 — Faseveranderingen)",
  "icoon": "🧪",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De temperatuur in een vriezer is −18 °C. Hoeveel kelvin is dat?",
      "opties": [
        "291 K",
        "−291 K",
        "18 K",
        "255 K"
      ],
      "antwoord": 3,
      "uitleg": "−18 + 273 = 255 K."
    },
    {
      "type": "mc",
      "vraag": "Een experiment wordt uitgevoerd bij −40 °C. Hoeveel kelvin is dat?",
      "opties": [
        "313 K",
        "233 K",
        "−313 K",
        "−233 K"
      ],
      "antwoord": 1,
      "uitleg": "−40 + 273 = 233 K."
    },
    {
      "type": "mc",
      "vraag": "In een oven is de temperatuur 1000 K. Hoeveel graden Celsius is dat?",
      "opties": [
        "727 °C",
        "1273 °C",
        "−727 °C",
        "373 °C"
      ],
      "antwoord": 0,
      "uitleg": "1000 − 273 = 727 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van 0 K is gelijk aan −273 °C.",
      "antwoord": true,
      "uitleg": "Waar. Dat is het absolute nulpunt: kouder dan −273 °C (0 K) kan een stof niet worden."
    },
    {
      "type": "mc",
      "vraag": "Een leerling rekent 400 K om met 400 + 273 = 673 °C. Wat is er fout?",
      "opties": [
        "Bij het omrekenen van K naar °C moet je 273 vermenigvuldigen: 400 × 273",
        "Het antwoord is goed, want je telt altijd 273 op",
        "Bij het omrekenen van K naar °C moet je 273 aftrekken: 127 °C",
        "Je moet 100 aftrekken in plaats van 273"
      ],
      "antwoord": 2,
      "uitleg": "Van kelvin naar graden Celsius trek je 273 af: 400 − 273 = 127 °C. Optellen doe je bij het omrekenen van °C naar K."
    },
    {
      "type": "invul",
      "vraag": "Reken 85 °C om naar kelvin.",
      "antwoord": "358",
      "uitleg": "85 + 273 = 358 K."
    },
    {
      "type": "mc",
      "vraag": "Welke temperatuur is de hoogste?",
      "opties": [
        "25 °C",
        "290 K",
        "15 °C",
        "300 K"
      ],
      "antwoord": 3,
      "uitleg": "Reken alles om naar °C: 300 K = 27 °C, 290 K = 17 °C, 25 °C en 15 °C. De hoogste temperatuur is dus 300 K (27 °C)."
    },
    {
      "type": "mc",
      "vraag": "Welke temperatuur is de laagste?",
      "opties": [
        "−20 °C",
        "240 K",
        "250 K",
        "−25 °C"
      ],
      "antwoord": 1,
      "uitleg": "In °C: 240 K = −33 °C, 250 K = −23 °C, −20 °C en −25 °C. De laagste is 240 K."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om een temperatuur van kelvin om te rekenen naar graden Celsius moet je 273 optellen.",
      "antwoord": false,
      "uitleg": "Onwaar. Van kelvin naar °C trek je 273 af; van °C naar kelvin tel je 273 op."
    },
    {
      "type": "mc",
      "vraag": "Kamfer heeft een smeltpunt van 180 °C. Hoeveel kelvin is dat?",
      "opties": [
        "453 K",
        "−93 K",
        "93 K",
        "473 K"
      ],
      "antwoord": 0,
      "uitleg": "180 + 273 = 453 K."
    },
    {
      "type": "mc",
      "vraag": "Kamfer heeft een kookpunt van 204 °C. Hoeveel kelvin is dat?",
      "opties": [
        "−69 K",
        "69 K",
        "477 K",
        "497 K"
      ],
      "antwoord": 2,
      "uitleg": "204 + 273 = 477 K."
    },
    {
      "type": "invul",
      "vraag": "Zwaveldioxide heeft een smeltpunt van −75 °C. Hoeveel kelvin is dat?",
      "antwoord": "198",
      "uitleg": "−75 + 273 = 198 K."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van 300 K is lager dan 0 °C.",
      "antwoord": false,
      "uitleg": "Onwaar. 300 K is 27 °C en dus hoger dan 0 °C (= 273 K)."
    },
    {
      "type": "mc",
      "vraag": "Het kookpunt van benzeen is 353 K en dat van water is 100 °C. Welke stof kookt bij de laagste temperatuur?",
      "opties": [
        "Benzeen, want 353 K is 80 °C",
        "Water, want 100 is kleiner dan 353",
        "Beide even, want ze zijn allebei vloeibaar",
        "Water, want 100 °C is 173 K"
      ],
      "antwoord": 0,
      "uitleg": "353 K = 353 − 273 = 80 °C. Dat is lager dan 100 °C, dus benzeen kookt bij de laagste temperatuur."
    },
    {
      "type": "invul",
      "vraag": "Lood kookt bij 1749 °C. Hoeveel kelvin is dat?",
      "antwoord": "2022",
      "uitleg": "1749 + 273 = 2022 K."
    },
    {
      "type": "mc",
      "vraag": "Wat is de eenheid die je in de wetenschap vaak voor temperatuur gebruikt, met het symbool K?",
      "opties": [
        "Kilo",
        "Kelvin",
        "Kilogram",
        "Kalorie"
      ],
      "antwoord": 1,
      "uitleg": "In de wetenschap geef je temperatuur vaak aan in kelvin (K) in plaats van in graden Celsius (°C)."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel kelvin is 273 °C?",
      "opties": [
        "0 K",
        "−546 K",
        "273 K",
        "546 K"
      ],
      "antwoord": 3,
      "uitleg": "273 + 273 = 546 K."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het getal bij een temperatuur in kelvin is altijd groter dan het getal bij dezelfde temperatuur in °C.",
      "antwoord": true,
      "uitleg": "Waar. Je telt 273 op bij de waarde in °C om de waarde in K te krijgen, dus het getal in K is altijd 273 groter."
    },
    {
      "type": "open",
      "vraag": "Een leerling zegt: \"Water kookt bij 100 K.\" Leg uit wat hij fout doet en geef de juiste waarde in kelvin.",
      "sleutelwoorden": [
        "°C/graden Celsius",
        "273",
        "373",
        "optellen"
      ],
      "minTreffers": 3,
      "modelantwoord": "Water kookt bij 100 °C, niet bij 100 K. Om te rekenen in kelvin tel je 273 op: 100 + 273 = 373 K.",
      "uitleg": "Het kookpunt van water is 100 °C = 373 K."
    },
    {
      "type": "open",
      "vraag": "Wat is het absolute nulpunt? Geef de waarde in °C en in K en leg uit wat het betekent voor de temperatuur van stoffen.",
      "sleutelwoorden": [
        "−273",
        "0 K",
        "kouder/lager",
        "niet"
      ],
      "minTreffers": 3,
      "modelantwoord": "Het absolute nulpunt is −273 °C, oftewel 0 K. Stoffen kunnen nooit kouder worden dan dit nulpunt.",
      "uitleg": "−273 °C is gelijk aan 0 K; een lagere temperatuur bestaat niet."
    }
  ]
});
