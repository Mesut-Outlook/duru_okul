/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 4 — Temperatuurschalen & Trajecten
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h1-4",
  "hoofdstuk": 1,
  "titel": "Toets 4 — Temperatuurschalen (°C & Kelvin) en Kook-/Smelttrajecten",
  "vak": "Scheikunde · HAVO 3 (H1.3)",
  "icoon": "🌡️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het <b>absolute nulpunt</b> in graden Celsius en in Kelvin?",
      "opties": [
        "0 K = -273 °C",
        "0 °C = 0 K",
        "-100 °C = 0 K",
        "273 K = 0 °C (dit is het vriespunt van water, niet het absolute nulpunt)"
      ],
      "antwoord": 0,
      "uitleg": "Het absolute nulpunt is 0 Kelvin = -273 °C. Dit is de laagst mogelijke temperatuur in het heelal."
    },
    {
      "type": "mc",
      "vraag": "Hoe reken je een temperatuur in <b>graden Celsius (°C)</b> om naar <b>Kelvin (K)</b>?",
      "opties": [
        "Trek 273 af van de temperatuur in °C",
        "Tel 273 op bij de temperatuur in °C (T(K) = T(°C) + 273)",
        "Vermenigvuldig met 273",
        "Deel door 273"
      ],
      "antwoord": 1,
      "uitleg": "Om van Celsius naar Kelvin te gaan, tel je 273 op: T(K) = T(°C) + 273."
    },
    {
      "type": "mc",
      "vraag": "Hoe reken je een temperatuur in <b>Kelvin (K)</b> om naar <b>graden Celsius (°C)</b>?",
      "opties": [
        "Tel 273 op bij de temperatuur in Kelvin",
        "Deel door 100",
        "Trek 273 af van de temperatuur in Kelvin (T(°C) = T(K) - 273)",
        "Vermenigvuldig met 1,8"
      ],
      "antwoord": 2,
      "uitleg": "Om van Kelvin naar Celsius te gaan, trek je 273 af: T(°C) = T(K) - 273."
    },
    {
      "type": "invul",
      "vraag": "De temperatuur van kokend water is 100 °C. Hoeveel Kelvin (K) is dit?",
      "antwoord": "373|373 K|373K",
      "uitleg": "100 °C + 273 = 373 K."
    },
    {
      "type": "invul",
      "vraag": "De temperatuur van een smeltend ijsblokje is 0 °C. Hoeveel Kelvin (K) is dit?",
      "antwoord": "273|273 K|273K",
      "uitleg": "0 °C + 273 = 273 K."
    },
    {
      "type": "invul",
      "vraag": "In een laboratorium wordt een gas gekoeld tot 140 K. Hoeveel graden Celsius (°C) is dat?",
      "antwoord": "-133|-133 °C|-133°C|-133 C",
      "uitleg": "140 K - 273 = -133 °C."
    },
    {
      "type": "invul",
      "vraag": "Een normale menselijke lichaamstemperatuur is 37 °C. Hoeveel Kelvin is dat (afgerond op een heel getal)?",
      "antwoord": "310|310 K|310K",
      "uitleg": "37 + 273 = 310 K."
    },
    {
      "type": "mc",
      "vraag": "In welke fase bevindt een stof zich als de temperatuur <b>lager is dan het smeltpunt</b>?",
      "opties": [
        "Vloeibare fase (l)",
        "Gasvormige fase (g)",
        "Gecondenseerde fase",
        "Vaste fase (s)"
      ],
      "antwoord": 3,
      "uitleg": "Onder het smeltpunt is de stof nog niet gesmolten en dus vast (s)."
    },
    {
      "type": "mc",
      "vraag": "In welke fase bevindt een stof zich als de temperatuur <b>tussen het smeltpunt en het kookpunt</b> ligt?",
      "opties": [
        "Vloeibare fase (l)",
        "Vaste fase (s)",
        "Gasvormige fase (g)",
        "Opgeloste fase (aq)"
      ],
      "antwoord": 0,
      "uitleg": "Tussen het smeltpunt en het kookpunt is de stof vloeibaar (l)."
    },
    {
      "type": "mc",
      "vraag": "In welke fase bevindt een stof zich als de temperatuur <b>hoger is dan het kookpunt</b>?",
      "opties": [
        "Vloeibare fase (l)",
        "Gasvormige fase (g)",
        "Vaste fase (s)",
        "Kristallijn"
      ],
      "antwoord": 1,
      "uitleg": "Boven het kookpunt is de hele stof verdampt en bevindt zich in de gasfase (g)."
    },
    {
      "type": "mc",
      "vraag": "Kwik heeft een smeltpunt van 234 K (-39 °C) en een kookpunt van 630 K (357 °C). In welke fase bevindt kwik zich bij kamertemperatuur (293 K / 20 °C)?",
      "opties": [
        "Vast (s)",
        "Gasvormig (g)",
        "Vloeibaar (l) — kwik is het enige vloeibare metaal bij kamertemperatuur",
        "Sublimerend"
      ],
      "antwoord": 2,
      "uitleg": "293 K ligt tussen het smeltpunt (234 K) en het kookpunt (630 K), dus is kwik vloeibaar."
    },
    {
      "type": "mc",
      "vraag": "Zuurstof heeft een smeltpunt van 54 K (-219 °C) en een kookpunt van 90 K (-183 °C). In welke fase bevindt zuurstof zich bij kamertemperatuur (20 °C / 293 K)?",
      "opties": [
        "Vloeibaar (l)",
        "Vast (s)",
        "Gecondenseerd",
        "Gasvormig (g)"
      ],
      "antwoord": 3,
      "uitleg": "20 °C (293 K) ligt ver boven het kookpunt (-183 °C / 90 K), dus is zuurstof gasvormig (g)."
    },
    {
      "type": "mc",
      "vraag": "Hoe herken je een <b>zuivere stof</b> in een temperatuur-tijd diagram tijdens het verwarmen?",
      "opties": [
        "Er is een duidelijke horizontale lijn (plateau) tijdens het smelten en koken: de temperatuur blijft constant zolang de faseovergang duurt",
        "De temperatuurlijn stijgt onafgebroken zonder enige pauze",
        "De lijn daalt plotseling naar beneden",
        "De lijn maakt een cirkel"
      ],
      "antwoord": 0,
      "uitleg": "Een zuivere stof heeft een vast smeltpunt en kookpunt; tijdens de faseovergang blijft de temperatuur exact constant (horizontaal plateau)."
    },
    {
      "type": "mc",
      "vraag": "Hoe herken je een <b>mengsel</b> in een temperatuur-tijd diagram tijdens het koken?",
      "opties": [
        "De temperatuur blijft perfect horizontaal stilstaan",
        "De temperatuur blijft niet constant, maar loopt tijdens het koken geleidelijk op (kooktraject)",
        "De temperatuur daalt direct naar 0 °C",
        "Er is geen thermometer die een mengsel kan meten"
      ],
      "antwoord": 1,
      "uitleg": "Een mengsel heeft een kooktraject: de kooktemperatuur stijgt geleidelijk omdat de makkelijkst verdampende componenten eerst verdampen."
    },
    {
      "type": "mc",
      "vraag": "Wat is het verschil tussen een <b>smeltpunt</b> en een <b>smelttraject</b>?",
      "opties": [
        "Een smeltpunt is in Kelvin en een smelttraject is in Celsius",
        "Een smeltpunt geldt voor vloeistoffen en een smelttraject voor gassen",
        "Een smeltpunt is één vaste temperatuur (bij een zuivere stof); een smelttraject is een temperatuurgebied tussen begin en einde van het smelten (bij een mengsel)",
        "Er is geen enkel verschil"
      ],
      "antwoord": 2,
      "uitleg": "Zuivere stoffen hebben een smeltpunt (één temperatuur), mengsels hebben een smelttraject (een bereik van temperaturen)."
    },
    {
      "type": "mc",
      "vraag": "Kerosine (vliegtuigbrandstof) kookt tussen 150 °C en 280 °C. Heeft kerosine een kookpunt of een kooktraject?",
      "opties": [
        "Een kookpunt van 150 °C",
        "Een kookpunt van 280 °C",
        "Een kooktraject, want kerosine is een mengsel van tientallen verschillende koolwaterstoffen",
        "Geen van beide"
      ],
      "antwoord": 2,
      "uitleg": "Omdat kerosine een mengsel is, kookt het over een temperatuurtraject (150 °C tot 280 °C)."
    },
    {
      "type": "mc",
      "vraag": "Hoe werken <b>Phase Change Materials (PCM)</b> in geavanceerde wintersportjassen?",
      "opties": [
        "Bij zware inspanning smelten de microbolletjes en nemen ze overtollige lichaamswarmte op; bij rust stollen ze en geven ze warmte terug aan het lichaam",
        "Ze branden langzaam op om vuurwarmte te maken",
        "Ze verdampen door de stof heen naar buiten",
        "Ze koelen het lichaam continu af tot onder 0 °C"
      ],
      "antwoord": 0,
      "uitleg": "Smelten kost warmte (koeling bij inspanning) en stollen levert warmte op (opwarming bij rust), waardoor de temperatuur comfortabel constant blijft."
    },
    {
      "type": "waaronwaar",
      "vraag": "Tijdens het stollen van een zuivere stof daalt de temperatuur voortdurend.",
      "antwoord": false,
      "uitleg": "Niet waar: bij een zuivere stof blijft de temperatuur tijdens het stollen constant op het stolpunt totdat alle vloeistof gestold is."
    },
    {
      "type": "mc",
      "vraag": "Stof X heeft een smeltpunt van 80 °C en kookt bij 218 °C. Wat is de fase van stof X bij 100 °C?",
      "opties": [
        "Vast (s)",
        "Vloeibaar (l)",
        "Gasvormig (g)",
        "Opgelost (aq)"
      ],
      "antwoord": 1,
      "uitleg": "100 °C ligt tussen 80 °C (smeltpunt) en 218 °C (kookpunt), dus stof X is vloeibaar."
    },
    {
      "type": "invul",
      "vraag": "De temperatuur van vloeibaar helium is 4 K. Hoeveel graden Celsius (°C) is dat?",
      "antwoord": "-269|-269 °C|-269°C|-269 C",
      "uitleg": "4 K - 273 = -269 °C."
    }
  ]
});
