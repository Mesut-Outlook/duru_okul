/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 30 — §1.3 Formules substitueren (1/5, basis)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-20",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 30 — §1.3 Formules substitueren (1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: N = 38 + 6a en B: a = 2q + 9. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "N = 6(2q + 9) + 38 = 12q + 54 + 38, dus N = 12q + 92. Let op de haakjes: alles binnen de haakjes wordt met 6 vermenigvuldigd.",
      "opties": [
        "N = 12q + 16",
        "N = 12q + 92",
        "N = 12q + 47",
        "N = 8q + 47"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Substitueer s = 3r + 3 in w = 3s − 19. Je krijgt w = …r − 10. Welk getal staat er vóór r?",
      "antwoord": "9",
      "uitleg": "w = 3(3r + 3) − 19. Vóór r: 3 · 3 = 9."
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: d = −3z + 24 en B: z = −5h − 7. Substitueer B in A en vereenvoudig tot d = …h + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "45",
      "uitleg": "d = −3(−5h − 7) + 24 = 15h + 21 + 24. Constante: 21 + 24 = 45."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule -3a + 3q = 24 in de formule p = 5q − 12 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "3q = 24 − -3a, dus q = a + 8. Invullen: p = 5(a + 8) − 12 = 5a + 28.",
      "opties": [
        "p = −5a + 28",
        "p = 5a + 28",
        "p = 5a − 4",
        "p = a + 28"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 8 − 3p substitueert in h = 4t + 7, krijg je h = −12p + 39.",
      "antwoord": true,
      "uitleg": "Waar. h = 4(8 − 3p) + 7 = 32 − 12p + 7, dus h = −12p + 39. Zonder haakjes vergeet je 3p met 4 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 6x = 0 in de formule P = 19 − 4t.",
      "uitleg": "t − 6x = 0 geeft t = 6x. Dan P = 19 − 4 · 6x = 19 − 24x.",
      "opties": [
        "P = 24x + 19",
        "P = −24x + 13",
        "P = −4x + 13",
        "P = −24x + 19"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 250t apparaten na t weken. De kosten in euro's zijn k = 12a + 800. Bereken de kosten na 25 weken.",
      "antwoord": "75800",
      "uitleg": "Substitueer: k = 12 · 250t + 800 = 3000t + 800. Na 25 weken: k = 3000 · 25 + 800 = 75800 euro."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 14 − 0,006h. Na k kwartier wandelen is de hoogte h = 8k + 500. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 14 − 0,006(8k + 500) = 14 − 0,048k − 3 = 11 − 0,048k.",
      "opties": [
        "T = 11 − 0,048k",
        "T = −486 − 0,048k",
        "T = 514 − 0,048k",
        "T = 11 − 0,006k"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 14 − 0,008h en h = 12k + 500, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 20 kwartier.",
      "antwoord": "8,08",
      "uitleg": "h = 12 · 20 + 500 = 740. T = 14 − 0,008 · 740 = 8,08 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 9 − 5p substitueert in h = 5t + 15, krijg je h = −5p + 60.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 5(9 − 5p) + 15 = 45 − 25p + 15, dus h = −25p + 60. Zonder haakjes vergeet je 5p met 5 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Omar is twee keer zo oud als Pim (a = 2b). Quinty is 2 jaar jonger dan Omar (c = a − 2). Samen zijn ze 18 jaar. Hoe oud is Pim?",
      "antwoord": "4",
      "uitleg": "a + b + c = 18. Substitueer a = 2b en c = 2b − 2: 2b + b + 2b − 2 = 18 → 5b = 20 → b = 4."
    },
    {
      "type": "invul",
      "vraag": "Op een balans liggen 3 appels en 4 bananen; samen wegen ze 930 gram (dus 3a + 4b = 930). Eén appel weegt 30 gram meer dan één banaan (a = b + 30). Bereken door te substitueren hoeveel gram één banaan weegt.",
      "antwoord": "120",
      "uitleg": "3(b + 30) + 4b = 930 → 7b + 90 = 930 → 7b = 840 → b = 120 gram (en een appel 150 gram)."
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 2t + 13. Het resultaat is y = 8x + 25. Bereken a.",
      "antwoord": "4",
      "uitleg": "y = 2(ax + b) + 13 = 2a·x + 2b + 13. Dus 2a = 8 → a = 4 (en 2b + 13 = 25 → b = 6)."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: h = 14 + 3t en B: t = −6 + 2p. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "h = 3(2p − 6) + 14 = 6p − 18 + 14, dus h = 6p − 4. Let op de haakjes: alles binnen de haakjes wordt met 3 vermenigvuldigd.",
      "opties": [
        "h = 5p + 8",
        "h = 6p − 32",
        "h = 6p − 4",
        "h = 6p + 8"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule -4a + 4q = 16 in de formule p = 4q + 8 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "4q = 16 − -4a, dus q = a + 4. Invullen: p = 4(a + 4) + 8 = 4a + 24.",
      "opties": [
        "p = −4a + 24",
        "p = 4a + 12",
        "p = a + 24",
        "p = 4a + 24"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 6 − 5p substitueert in h = 6t + 11, krijg je h = −5p + 47.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 6(6 − 5p) + 11 = 36 − 30p + 11, dus h = −30p + 47. Zonder haakjes vergeet je 5p met 6 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: N = −5a + 2 en B: a = 9 + 8q. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "N = −5(8q + 9) + 2 = −40q − 45 + 2, dus N = −40q − 43. Let op de haakjes: alles binnen de haakjes wordt met −5 vermenigvuldigd.",
      "opties": [
        "N = 3q + 11",
        "N = −40q − 47",
        "N = −40q + 11",
        "N = −40q − 43"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 2x = 0 in de formule r = 17 − 2t.",
      "uitleg": "t − 2x = 0 geeft t = 2x. Dan r = 17 − 2 · 2x = 17 − 4x.",
      "opties": [
        "r = 4x + 17",
        "r = −2x + 15",
        "r = −4x + 17",
        "r = −4x + 15"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 5 − 3p substitueert in h = 3t + 8, krijg je h = −9p + 23.",
      "antwoord": true,
      "uitleg": "Waar. h = 3(5 − 3p) + 8 = 15 − 9p + 8, dus h = −9p + 23. Zonder haakjes vergeet je 3p met 3 te vermenigvuldigen."
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: N = 4a + 37   B: a = 7q + 29",
      "modelantwoord": "N = 28q + 153",
      "sleutelwoorden": [
        "28q/28q",
        "+ 153/+153"
      ],
      "minTreffers": 2,
      "uitleg": "N = 4(7q + 29) + 37 = 28q + 153."
    }
  ]
});
