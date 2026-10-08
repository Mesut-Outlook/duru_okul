/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 34 — §1.3 Formules substitueren (5/5, eindniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-24",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 34 — §1.3 Formules substitueren (5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: b = 38 + 11t en B: t = 27 − 5p. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "b = 11(−5p + 27) + 38 = −55p + 297 + 38, dus b = −55p + 335. Let op de haakjes: alles binnen de haakjes wordt met 11 vermenigvuldigd.",
      "opties": [
        "b = −55p + 259",
        "b = −55p + 335",
        "b = 6p + 65",
        "b = −55p + 65"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Substitueer t = 4p + 35 in k = −7t + 19. Je krijgt k = …p − 226. Welk getal staat er vóór p?",
      "antwoord": "-28",
      "uitleg": "k = −7(4p + 35) + 19. Vóór p: −7 · 4 = −28."
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: h = 2t + 9 en B: t = 3p + 16. Substitueer B in A en vereenvoudig tot h = …p + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "41",
      "uitleg": "h = 2(3p + 16) + 9 = 6p + 32 + 9. Constante: 32 + 9 = 41."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 4a + 2q = 16 in de formule p = 3q − 9 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "2q = 16 − 4a, dus q = −2a + 8. Invullen: p = 3(−2a + 8) − 9 = −6a + 15.",
      "opties": [
        "p = −6a − 1",
        "p = 6a + 15",
        "p = −2a + 15",
        "p = −6a + 15"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 9 − 5p substitueert in h = 4t + 4, krijg je h = −20p + 40.",
      "antwoord": true,
      "uitleg": "Waar. h = 4(9 − 5p) + 4 = 36 − 20p + 4, dus h = −20p + 40. Zonder haakjes vergeet je 5p met 4 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 4x = 0 in de formule r = 13 − 3t.",
      "uitleg": "t − 4x = 0 geeft t = 4x. Dan r = 13 − 3 · 4x = 13 − 12x.",
      "opties": [
        "r = 12x + 13",
        "r = −12x + 13",
        "r = −3x + 9",
        "r = −12x + 9"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 250t apparaten na t weken. De kosten in euro's zijn k = 7a + 500. Bereken de kosten na 21 weken.",
      "antwoord": "37250",
      "uitleg": "Substitueer: k = 7 · 250t + 500 = 1750t + 500. Na 21 weken: k = 1750 · 21 + 500 = 37250 euro."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 20 − 0,0065h. Na k kwartier wandelen is de hoogte h = 6k + 200. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 20 − 0,0065(6k + 200) = 20 − 0,039k − 1,3 = 18,7 − 0,039k.",
      "opties": [
        "T = 18,7 − 0,039k",
        "T = 220 − 0,039k",
        "T = 18,7 − 0,0065k",
        "T = −180 − 0,039k"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 20 − 0,0065h en h = 8k + 500, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 16 kwartier.",
      "antwoord": "15,918",
      "uitleg": "h = 8 · 16 + 500 = 628. T = 20 − 0,0065 · 628 = 15,918 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 4p substitueert in h = 5t + 4, krijg je h = −4p + 24.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 5(4 − 4p) + 4 = 20 − 20p + 4, dus h = −20p + 24. Zonder haakjes vergeet je 4p met 5 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Omar is drie keer zo oud als Pim (a = 3b). Quinty is 2 jaar jonger dan Omar (c = a − 2). Samen zijn ze 26 jaar. Hoe oud is Pim?",
      "antwoord": "4",
      "uitleg": "a + b + c = 26. Substitueer a = 3b en c = 3b − 2: 3b + b + 3b − 2 = 26 → 7b = 28 → b = 4."
    },
    {
      "type": "invul",
      "vraag": "Op een balans liggen 4 appels en 3 bananen; samen wegen ze 970 gram (dus 4a + 3b = 970). Eén appel weegt 50 gram meer dan één banaan (a = b + 50). Bereken door te substitueren hoeveel gram één banaan weegt.",
      "antwoord": "110",
      "uitleg": "4(b + 50) + 3b = 970 → 7b + 200 = 970 → 7b = 770 → b = 110 gram (en een appel 160 gram)."
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 3t − 2. Het resultaat is y = 9x − 26. Bereken a.",
      "antwoord": "3",
      "uitleg": "y = 3(ax + b) − 2 = 3a·x + 3b − 2. Dus 3a = 9 → a = 3 (en 3b − 2 = −26 → b = −8)."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: w = 3 + 4s en B: s = −5r + 12. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "w = 4(−5r + 12) + 3 = −20r + 48 + 3, dus w = −20r + 51. Let op de haakjes: alles binnen de haakjes wordt met 4 vermenigvuldigd.",
      "opties": [
        "w = −r + 15",
        "w = −20r + 51",
        "w = −20r + 45",
        "w = −20r + 15"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 8a + 4q = 16 in de formule w = 2q + 7 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "4q = 16 − 8a, dus q = −2a + 4. Invullen: w = 2(−2a + 4) + 7 = −4a + 15.",
      "opties": [
        "w = 4a + 15",
        "w = −4a + 11",
        "w = −2a + 15",
        "w = −4a + 15"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 3 − 2p substitueert in h = 4t + 12, krijg je h = −2p + 24.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 4(3 − 2p) + 12 = 12 − 8p + 12, dus h = −8p + 24. Zonder haakjes vergeet je 2p met 4 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: y = −14 + 11t en B: t = 7x + 9. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "y = 11(7x + 9) − 14 = 77x + 99 − 14, dus y = 77x + 85. Let op de haakjes: alles binnen de haakjes wordt met 11 vermenigvuldigd.",
      "opties": [
        "y = 77x − 5",
        "y = 77x + 113",
        "y = 18x − 5",
        "y = 77x + 85"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 4x = 0 in de formule P = 16 − 2t.",
      "uitleg": "t − 4x = 0 geeft t = 4x. Dan P = 16 − 2 · 4x = 16 − 8x.",
      "opties": [
        "P = −8x + 16",
        "P = −2x + 12",
        "P = −8x + 12",
        "P = 8x + 16"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 8 − 3p substitueert in h = 2t + 4, krijg je h = −6p + 20.",
      "antwoord": true,
      "uitleg": "Waar. h = 2(8 − 3p) + 4 = 16 − 6p + 4, dus h = −6p + 20. Zonder haakjes vergeet je 3p met 2 te vermenigvuldigen."
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: y = 6t − 11   B: t = 4x + 3",
      "modelantwoord": "y = 24x + 7",
      "sleutelwoorden": [
        "24x/24x",
        "+ 7/+7"
      ],
      "minTreffers": 2,
      "uitleg": "y = 6(4x + 3) − 11 = 24x + 7."
    }
  ]
});
