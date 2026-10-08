/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 32 — §1.3 Formules substitueren (3/5, gemengd)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-22",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 32 — §1.3 Formules substitueren (3/5, gemengd)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: k = 27 − 4t en B: t = 2 + 2p. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "k = −4(2p + 2) + 27 = −8p − 8 + 27, dus k = −8p + 19. Let op de haakjes: alles binnen de haakjes wordt met −4 vermenigvuldigd.",
      "opties": [
        "k = −2p + 29",
        "k = −8p + 29",
        "k = −8p − 35",
        "k = −8p + 19"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Substitueer s = −2r − 4 in w = −4s + 35. Je krijgt w = …r + 51. Welk getal staat er vóór r?",
      "antwoord": "8",
      "uitleg": "w = −4(−2r − 4) + 35. Vóór r: −4 · −2 = 8."
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: N = 2a + 7 en B: a = 2q + 31. Substitueer B in A en vereenvoudig tot N = …q + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "69",
      "uitleg": "N = 2(2q + 31) + 7 = 4q + 62 + 7. Constante: 62 + 7 = 69."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 6a + 3q = 6 in de formule p = −2q + 7 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "3q = 6 − 6a, dus q = −2a + 2. Invullen: p = −2(−2a + 2) + 7 = 4a + 3.",
      "opties": [
        "p = 4a + 9",
        "p = 4a + 3",
        "p = −4a + 3",
        "p = −2a + 3"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 3 − 5p substitueert in h = 6t + 15, krijg je h = −30p + 33.",
      "antwoord": true,
      "uitleg": "Waar. h = 6(3 − 5p) + 15 = 18 − 30p + 15, dus h = −30p + 33. Zonder haakjes vergeet je 5p met 6 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 6x = 0 in de formule P = 19 − 3t.",
      "uitleg": "t − 6x = 0 geeft t = 6x. Dan P = 19 − 3 · 6x = 19 − 18x.",
      "opties": [
        "P = 18x + 19",
        "P = −3x + 13",
        "P = −18x + 13",
        "P = −18x + 19"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 400t apparaten na t weken. De kosten in euro's zijn k = 5a + 500. Bereken de kosten na 23 weken.",
      "antwoord": "46500",
      "uitleg": "Substitueer: k = 5 · 400t + 500 = 2000t + 500. Na 23 weken: k = 2000 · 23 + 500 = 46500 euro."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 16 − 0,006h. Na k kwartier wandelen is de hoogte h = 6k + 500. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 16 − 0,006(6k + 500) = 16 − 0,036k − 3 = 13 − 0,036k.",
      "opties": [
        "T = −484 − 0,036k",
        "T = 516 − 0,036k",
        "T = 13 − 0,036k",
        "T = 13 − 0,006k"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 22 − 0,008h en h = 10k + 250, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 16 kwartier.",
      "antwoord": "18,72",
      "uitleg": "h = 10 · 16 + 250 = 410. T = 22 − 0,008 · 410 = 18,72 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 2 − 2p substitueert in h = 2t + 4, krijg je h = −2p + 8.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 2(2 − 2p) + 4 = 4 − 4p + 4, dus h = −4p + 8. Zonder haakjes vergeet je 2p met 2 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Abel is drie keer zo oud als Berend (a = 3b). Ceciel is 3 jaar jonger dan Abel (c = a − 3). Samen zijn ze 25 jaar. Hoe oud is Berend?",
      "antwoord": "4",
      "uitleg": "a + b + c = 25. Substitueer a = 3b en c = 3b − 3: 3b + b + 3b − 3 = 25 → 7b = 28 → b = 4."
    },
    {
      "type": "invul",
      "vraag": "Op een balans liggen 3 appels en 4 bananen; samen wegen ze 1160 gram (dus 3a + 4b = 1160). Eén appel weegt 60 gram meer dan één banaan (a = b + 60). Bereken door te substitueren hoeveel gram één banaan weegt.",
      "antwoord": "140",
      "uitleg": "3(b + 60) + 4b = 1160 → 7b + 180 = 1160 → 7b = 980 → b = 140 gram (en een appel 200 gram)."
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 4t + 15. Het resultaat is y = 12x − 21. Bereken a.",
      "antwoord": "3",
      "uitleg": "y = 4(ax + b) + 15 = 4a·x + 4b + 15. Dus 4a = 12 → a = 3 (en 4b + 15 = −21 → b = −9)."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: N = 2a − 10 en B: a = 7q − 5. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "N = 2(7q − 5) − 10 = 14q − 10 − 10, dus N = 14q − 20. Let op de haakjes: alles binnen de haakjes wordt met 2 vermenigvuldigd.",
      "opties": [
        "N = 14q − 20",
        "N = 14q − 15",
        "N = 14q",
        "N = 9q − 15"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 5a + 5q = 15 in de formule p = 4q + 9 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "5q = 15 − 5a, dus q = −a + 3. Invullen: p = 4(−a + 3) + 9 = −4a + 21.",
      "opties": [
        "p = −4a + 12",
        "p = −a + 21",
        "p = 4a + 21",
        "p = −4a + 21"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 5 − 2p substitueert in h = 4t + 15, krijg je h = −2p + 35.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 4(5 − 2p) + 15 = 20 − 8p + 15, dus h = −8p + 35. Zonder haakjes vergeet je 2p met 4 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: w = 11s + 32 en B: s = 10 + 8r. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "w = 11(8r + 10) + 32 = 88r + 110 + 32, dus w = 88r + 142. Let op de haakjes: alles binnen de haakjes wordt met 11 vermenigvuldigd.",
      "opties": [
        "w = 88r + 78",
        "w = 88r + 142",
        "w = 19r + 42",
        "w = 88r + 42"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 3x = 0 in de formule y = 20 − 3t.",
      "uitleg": "t − 3x = 0 geeft t = 3x. Dan y = 20 − 3 · 3x = 20 − 9x.",
      "opties": [
        "y = −9x + 20",
        "y = −3x + 17",
        "y = 9x + 20",
        "y = −9x + 17"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 3 − 4p substitueert in h = 4t + 14, krijg je h = −16p + 26.",
      "antwoord": true,
      "uitleg": "Waar. h = 4(3 − 4p) + 14 = 12 − 16p + 14, dus h = −16p + 26. Zonder haakjes vergeet je 4p met 4 te vermenigvuldigen."
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: h = −3t − 16   B: t = −2p + 15",
      "modelantwoord": "h = 6p − 61",
      "sleutelwoorden": [
        "6p/6p",
        "- 61/-61/− 61"
      ],
      "minTreffers": 2,
      "uitleg": "h = −3(−2p + 15) − 16 = 6p − 61."
    }
  ]
});
