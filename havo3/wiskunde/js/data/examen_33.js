/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 33 — §1.3 Formules substitueren (4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-23",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 33 — §1.3 Formules substitueren (4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: y = 38 + 5t en B: t = 2x − 5. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "y = 5(2x − 5) + 38 = 10x − 25 + 38, dus y = 10x + 13. Let op de haakjes: alles binnen de haakjes wordt met 5 vermenigvuldigd.",
      "opties": [
        "y = 10x + 33",
        "y = 10x − 63",
        "y = 7x + 33",
        "y = 10x + 13"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Substitueer s = 3r + 13 in w = 8s − 14. Je krijgt w = …r + 90. Welk getal staat er vóór r?",
      "antwoord": "24",
      "uitleg": "w = 8(3r + 13) − 14. Vóór r: 8 · 3 = 24."
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: h = 11t + 20 en B: t = 7p − 1. Substitueer B in A en vereenvoudig tot h = …p + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "9",
      "uitleg": "h = 11(7p − 1) + 20 = 77p − 11 + 20. Constante: −11 + 20 = 9."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 5a + 5q = 20 in de formule N = −2q − 10 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "5q = 20 − 5a, dus q = −a + 4. Invullen: N = −2(−a + 4) − 10 = 2a − 18.",
      "opties": [
        "N = 2a − 6",
        "N = −2a − 18",
        "N = 2a − 18",
        "N = −a − 18"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 5p substitueert in h = 2t + 9, krijg je h = −10p + 17.",
      "antwoord": true,
      "uitleg": "Waar. h = 2(4 − 5p) + 9 = 8 − 10p + 9, dus h = −10p + 17. Zonder haakjes vergeet je 5p met 2 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 2x = 0 in de formule r = 11 − 2t.",
      "uitleg": "t − 2x = 0 geeft t = 2x. Dan r = 11 − 2 · 2x = 11 − 4x.",
      "opties": [
        "r = 4x + 11",
        "r = −2x + 9",
        "r = −4x + 11",
        "r = −4x + 9"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 250t apparaten na t weken. De kosten in euro's zijn k = 5a + 1200. Bereken de kosten na 23 weken.",
      "antwoord": "29950",
      "uitleg": "Substitueer: k = 5 · 250t + 1200 = 1250t + 1200. Na 23 weken: k = 1250 · 23 + 1200 = 29950 euro."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 16 − 0,008h. Na k kwartier wandelen is de hoogte h = 12k + 250. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 16 − 0,008(12k + 250) = 16 − 0,096k − 2 = 14 − 0,096k.",
      "opties": [
        "T = 266 − 0,096k",
        "T = −234 − 0,096k",
        "T = 14 − 0,096k",
        "T = 14 − 0,008k"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 16 − 0,008h en h = 8k + 100, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 8 kwartier.",
      "antwoord": "14,688",
      "uitleg": "h = 8 · 8 + 100 = 164. T = 16 − 0,008 · 164 = 14,688 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 2p substitueert in h = 6t + 9, krijg je h = −2p + 33.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 6(4 − 2p) + 9 = 24 − 12p + 9, dus h = −12p + 33. Zonder haakjes vergeet je 2p met 6 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Omar is drie keer zo oud als Pim (a = 3b). Quinty is 3 jaar jonger dan Omar (c = a − 3). Samen zijn ze 53 jaar. Hoe oud is Pim?",
      "antwoord": "8",
      "uitleg": "a + b + c = 53. Substitueer a = 3b en c = 3b − 3: 3b + b + 3b − 3 = 53 → 7b = 56 → b = 8."
    },
    {
      "type": "invul",
      "vraag": "Op een balans liggen 2 appels en 3 bananen; samen wegen ze 790 gram (dus 2a + 3b = 790). Eén appel weegt 20 gram meer dan één banaan (a = b + 20). Bereken door te substitueren hoeveel gram één banaan weegt.",
      "antwoord": "150",
      "uitleg": "2(b + 20) + 3b = 790 → 5b + 40 = 790 → 5b = 750 → b = 150 gram (en een appel 170 gram)."
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 5t + 14. Het resultaat is y = 10x + 39. Bereken a.",
      "antwoord": "2",
      "uitleg": "y = 5(ax + b) + 14 = 5a·x + 5b + 14. Dus 5a = 10 → a = 2 (en 5b + 14 = 39 → b = 5)."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: w = 8s + 31 en B: s = −3r + 13. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "w = 8(−3r + 13) + 31 = −24r + 104 + 31, dus w = −24r + 135. Let op de haakjes: alles binnen de haakjes wordt met 8 vermenigvuldigd.",
      "opties": [
        "w = −24r + 135",
        "w = 5r + 44",
        "w = −24r + 73",
        "w = −24r + 44"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 3a + 3q = 18 in de formule N = −2q + 2 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "3q = 18 − 3a, dus q = −a + 6. Invullen: N = −2(−a + 6) + 2 = 2a − 10.",
      "opties": [
        "N = −a − 10",
        "N = 2a − 10",
        "N = −2a − 10",
        "N = 2a + 8"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 5p substitueert in h = 6t + 12, krijg je h = −5p + 36.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 6(4 − 5p) + 12 = 24 − 30p + 12, dus h = −30p + 36. Zonder haakjes vergeet je 5p met 6 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: k = 32 + 11t en B: t = 4p + 27. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "k = 11(4p + 27) + 32 = 44p + 297 + 32, dus k = 44p + 329. Let op de haakjes: alles binnen de haakjes wordt met 11 vermenigvuldigd.",
      "opties": [
        "k = 15p + 59",
        "k = 44p + 59",
        "k = 44p + 265",
        "k = 44p + 329"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 4x = 0 in de formule y = 29 − 5t.",
      "uitleg": "t − 4x = 0 geeft t = 4x. Dan y = 29 − 5 · 4x = 29 − 20x.",
      "opties": [
        "y = 20x + 29",
        "y = −20x + 29",
        "y = −5x + 25",
        "y = −20x + 25"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 5 − 2p substitueert in h = 3t + 1, krijg je h = −6p + 16.",
      "antwoord": true,
      "uitleg": "Waar. h = 3(5 − 2p) + 1 = 15 − 6p + 1, dus h = −6p + 16. Zonder haakjes vergeet je 2p met 3 te vermenigvuldigen."
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: N = −3a + 32   B: a = −2q + 11",
      "modelantwoord": "N = 6q − 1",
      "sleutelwoorden": [
        "6q/6q",
        "- 1/-1/− 1"
      ],
      "minTreffers": 2,
      "uitleg": "N = −3(−2q + 11) + 32 = 6q − 1."
    }
  ]
});
