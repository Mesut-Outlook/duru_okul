/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 15 — 1.3 Temperatuur, smelt- en kookpunt
   Hoofdstuk 1 (Scheikunde is overal), §1.3 Faseveranderingen — omrekenen tussen °C en K, smelt- en kookpunt, fase bij een gegeven temperatuur
   20 vragen · 30 minuten. Gebaseerd op de stof van het boek (eigen voorbeelden en formuleringen).
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h1-15",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Toets 15 — 1.3 Temperatuur, smelt- en kookpunt",
  "vak": "Scheikunde · HAVO 3 (H1 — Scheikunde is overal)",
  "icoon": "🧪",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Het is buiten 25 °C. Hoeveel kelvin is dat?",
      "opties": [
        "298 K",
        "248 K",
        "275 K",
        "25 K"
      ],
      "antwoord": 0,
      "uitleg": "Je rekent °C om naar K door 273 op te tellen: 25 + 273 = 298 K."
    },
    {
      "type": "mc",
      "vraag": "In een lab wordt een temperatuur van 310 K gemeten. Hoeveel °C is dat?",
      "opties": [
        "583 °C",
        "−37 °C",
        "37 °C",
        "47 °C"
      ],
      "antwoord": 2,
      "uitleg": "Je rekent K om naar °C door 273 af te trekken: 310 − 273 = 37 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het omrekenen van °C naar K kan de uitkomst nooit negatief zijn.",
      "antwoord": true,
      "uitleg": "Waar. Het absolute nulpunt is −273 °C = 0 K. Kouder dan 0 K kan niet, dus een temperatuur in kelvin is nooit negatief."
    },
    {
      "type": "mc",
      "vraag": "Vloeibare stikstof heeft een temperatuur van −196 °C. Hoeveel kelvin is dat?",
      "opties": [
        "469 K",
        "77 K",
        "196 K",
        "−77 K"
      ],
      "antwoord": 1,
      "uitleg": "−196 + 273 = 77 K."
    },
    {
      "type": "mc",
      "vraag": "Benzeen heeft een smeltpunt van 279 K. Hoeveel °C is dat?",
      "opties": [
        "552 °C",
        "−6 °C",
        "279 °C",
        "6 °C"
      ],
      "antwoord": 3,
      "uitleg": "279 − 273 = 6 °C."
    },
    {
      "type": "invul",
      "vraag": "Reken 98 °C om naar kelvin.",
      "antwoord": "371",
      "uitleg": "98 + 273 = 371 K."
    },
    {
      "type": "mc",
      "vraag": "Azijnzuur heeft een kookpunt van 391 K. Hoeveel °C is dat?",
      "opties": [
        "664 °C",
        "−118 °C",
        "391 °C",
        "118 °C"
      ],
      "antwoord": 3,
      "uitleg": "391 − 273 = 118 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van 150 K is gelijk aan 123 °C.",
      "antwoord": false,
      "uitleg": "Onwaar. 150 − 273 = −123 °C. De uitkomst is negatief, geen +123 °C."
    },
    {
      "type": "mc",
      "vraag": "Lood heeft een smeltpunt van 328 °C. Hoeveel kelvin is dat?",
      "opties": [
        "601 K",
        "55 K",
        "655 K",
        "328 K"
      ],
      "antwoord": 0,
      "uitleg": "328 + 273 = 601 K."
    },
    {
      "type": "mc",
      "vraag": "Een leerling rekent 50 °C om: 50 − 273 = −223 K. Wat is er fout aan deze berekening?",
      "opties": [
        "Er is niets fout, kelvin kan wel negatief zijn.",
        "Je moet 100 optellen, dus het antwoord is 150 K.",
        "Je moet 273 optellen: 50 + 273 = 323 K.",
        "Je moet met 273 vermenigvuldigen."
      ],
      "antwoord": 2,
      "uitleg": "Van °C naar K tel je 273 op. Aftrekken doe je juist van K naar °C. Bovendien is een negatieve temperatuur in kelvin onmogelijk."
    },
    {
      "type": "mc",
      "vraag": "Ethanol heeft een smeltpunt van −114 °C en een kookpunt van 78 °C. In welke fase is ethanol bij 300 K?",
      "opties": [
        "vast",
        "vloeibaar",
        "gasvormig",
        "vast en gasvormig tegelijk"
      ],
      "antwoord": 1,
      "uitleg": "300 K is 300 − 273 = 27 °C. Dat ligt tussen −114 °C en 78 °C, dus ethanol is vloeibaar."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een stof met een smeltpunt van 300 K is bij 20 °C vloeibaar.",
      "antwoord": false,
      "uitleg": "Onwaar. 20 °C is 293 K. Dat is lager dan het smeltpunt van 300 K, dus de stof is vast."
    },
    {
      "type": "invul",
      "vraag": "Reken 500 K om naar graden Celsius.",
      "antwoord": "227",
      "uitleg": "500 − 273 = 227 °C."
    },
    {
      "type": "mc",
      "vraag": "Zwaveldioxide heeft een smeltpunt van −75 °C en een kookpunt van −10 °C. In welke fase is zwaveldioxide bij 230 K?",
      "opties": [
        "vloeibaar",
        "vast",
        "gasvormig",
        "vast en vloeibaar tegelijk"
      ],
      "antwoord": 0,
      "uitleg": "−10 °C is 263 K. −75 °C is 198 K. 230 K ligt tussen 198 K en 263 K, dus zwaveldioxide is vloeibaar."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een stof met een kookpunt van 350 K is bij 100 °C gasvormig.",
      "antwoord": true,
      "uitleg": "Waar. 100 °C is 373 K. Dat is hoger dan het kookpunt van 350 K, dus de stof is gasvormig."
    },
    {
      "type": "mc",
      "vraag": "Kamfer heeft een smeltpunt van 180 °C en een kookpunt van 204 °C. In welke fase is kamfer bij 480 K?",
      "opties": [
        "vloeibaar",
        "vast",
        "vast en vloeibaar tegelijk",
        "gasvormig"
      ],
      "antwoord": 3,
      "uitleg": "480 K is 480 − 273 = 207 °C. Dat is hoger dan het kookpunt van 204 °C, dus kamfer is gasvormig."
    },
    {
      "type": "mc",
      "vraag": "Welke van deze temperaturen is de laagste?",
      "opties": [
        "250 K",
        "−20 °C",
        "−30 °C",
        "0 °C"
      ],
      "antwoord": 2,
      "uitleg": "250 K is 250 − 273 = −23 °C. Rangschik je alles in °C, dan is −30 °C het laagst."
    },
    {
      "type": "invul",
      "vraag": "Kwik kookt bij 357 °C. Hoeveel kelvin is dat?",
      "antwoord": "630",
      "uitleg": "357 + 273 = 630 K."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van −300 °C komt voor als je een stof maar sterk genoeg afkoelt.",
      "antwoord": false,
      "uitleg": "Onwaar. Het absolute nulpunt is −273 °C (0 K). Kouder dan dat kan een stof niet worden."
    },
    {
      "type": "open",
      "vraag": "Stof A heeft een smeltpunt van 250 K en een kookpunt van 400 K. Bepaal met een berekening in welke fase stof A zich bevindt op een kamertemperatuur van 20 °C.",
      "sleutelwoorden": [
        "293",
        "vloeibaar/vloeistof",
        "tussen"
      ],
      "minTreffers": 2,
      "modelantwoord": "20 °C is 20 + 273 = 293 K. Dat ligt tussen het smeltpunt (250 K) en het kookpunt (400 K), dus stof A is vloeibaar.",
      "uitleg": "Reken eerst om naar dezelfde eenheid als het smelt- en kookpunt, vergelijk dan."
    }
  ]
});
