/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 31 — §1.3 Formules substitueren (2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.3 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-21",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 31 — §1.3 Formules substitueren (2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: b = 5t + 13 en B: t = 7p + 23. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "b = 5(7p + 23) + 13 = 35p + 115 + 13, dus b = 35p + 128. Let op de haakjes: alles binnen de haakjes wordt met 5 vermenigvuldigd.",
      "opties": [
        "b = 12p + 36",
        "b = 35p + 102",
        "b = 35p + 128",
        "b = 35p + 36"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Substitueer s = −5r − 3 in w = −3s + 1. Je krijgt w = …r + 10. Welk getal staat er vóór r?",
      "antwoord": "15",
      "uitleg": "w = −3(−5r − 3) + 1. Vóór r: −3 · −5 = 15."
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: N = −7a − 12 en B: a = −3q + 31. Substitueer B in A en vereenvoudig tot N = …q + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "-229",
      "uitleg": "N = −7(−3q + 31) − 12 = 21q − 217 − 12. Constante: −217 + −12 = −229."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 6a + 3q = 24 in de formule p = 4q + 7 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "3q = 24 − 6a, dus q = −2a + 8. Invullen: p = 4(−2a + 8) + 7 = −8a + 39.",
      "opties": [
        "p = −2a + 39",
        "p = −8a + 39",
        "p = −8a + 15",
        "p = 8a + 39"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 5p substitueert in h = 2t + 4, krijg je h = −10p + 12.",
      "antwoord": true,
      "uitleg": "Waar. h = 2(4 − 5p) + 4 = 8 − 10p + 4, dus h = −10p + 12. Zonder haakjes vergeet je 5p met 2 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 2x = 0 in de formule r = 19 − 4t.",
      "uitleg": "t − 2x = 0 geeft t = 2x. Dan r = 19 − 4 · 2x = 19 − 8x.",
      "opties": [
        "r = 8x + 19",
        "r = −4x + 17",
        "r = −8x + 17",
        "r = −8x + 19"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 400t apparaten na t weken. De kosten in euro's zijn k = 5a + 800. Bereken de kosten na 25 weken.",
      "antwoord": "50800",
      "uitleg": "Substitueer: k = 5 · 400t + 800 = 2000t + 800. Na 25 weken: k = 2000 · 25 + 800 = 50800 euro."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 16 − 0,008h. Na k kwartier wandelen is de hoogte h = 6k + 100. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 16 − 0,008(6k + 100) = 16 − 0,048k − 0,8 = 15,2 − 0,048k.",
      "opties": [
        "T = 15,2 − 0,048k",
        "T = −84 − 0,048k",
        "T = 15,2 − 0,008k",
        "T = 116 − 0,048k"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 14 − 0,006h en h = 8k + 500, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 10 kwartier.",
      "antwoord": "10,52",
      "uitleg": "h = 8 · 10 + 500 = 580. T = 14 − 0,006 · 580 = 10,52 °C."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 5 − 2p substitueert in h = 2t + 9, krijg je h = −2p + 19.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 2(5 − 2p) + 9 = 10 − 4p + 9, dus h = −4p + 19. Zonder haakjes vergeet je 2p met 2 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Abel is drie keer zo oud als Berend (a = 3b). Ceciel is 1 jaar jonger dan Abel (c = a − 1). Samen zijn ze 34 jaar. Hoe oud is Berend?",
      "antwoord": "5",
      "uitleg": "a + b + c = 34. Substitueer a = 3b en c = 3b − 1: 3b + b + 3b − 1 = 34 → 7b = 35 → b = 5."
    },
    {
      "type": "invul",
      "vraag": "Op een balans liggen 3 appels en 2 bananen; samen wegen ze 760 gram (dus 3a + 2b = 760). Eén appel weegt 20 gram meer dan één banaan (a = b + 20). Bereken door te substitueren hoeveel gram één banaan weegt.",
      "antwoord": "140",
      "uitleg": "3(b + 20) + 2b = 760 → 5b + 60 = 760 → 5b = 700 → b = 140 gram (en een appel 160 gram)."
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 5t − 8. Het resultaat is y = 10x − 38. Bereken a.",
      "antwoord": "2",
      "uitleg": "y = 5(ax + b) − 8 = 5a·x + 5b − 8. Dus 5a = 10 → a = 2 (en 5b − 8 = −38 → b = −6)."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: w = 7 − 4s en B: s = 33 + 3r. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "w = −4(3r + 33) + 7 = −12r − 132 + 7, dus w = −12r − 125. Let op de haakjes: alles binnen de haakjes wordt met −4 vermenigvuldigd.",
      "opties": [
        "w = −12r + 40",
        "w = −r + 40",
        "w = −12r − 125",
        "w = −12r − 139"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 8a + 2q = 4 in de formule N = −2q − 3 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "2q = 4 − 8a, dus q = −4a + 2. Invullen: N = −2(−4a + 2) − 3 = 8a − 7.",
      "opties": [
        "N = −8a − 7",
        "N = 8a − 1",
        "N = −4a − 7",
        "N = 8a − 7"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 5p substitueert in h = 3t + 4, krijg je h = −5p + 16.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 3(4 − 5p) + 4 = 12 − 15p + 4, dus h = −15p + 16. Zonder haakjes vergeet je 5p met 3 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: h = −3t + 33 en B: t = 8p + 20. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "h = −3(8p + 20) + 33 = −24p − 60 + 33, dus h = −24p − 27. Let op de haakjes: alles binnen de haakjes wordt met −3 vermenigvuldigd.",
      "opties": [
        "h = −24p − 93",
        "h = −24p − 27",
        "h = 5p + 53",
        "h = −24p + 53"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule t − 2x = 0 in de formule P = 15 − 2t.",
      "uitleg": "t − 2x = 0 geeft t = 2x. Dan P = 15 − 2 · 2x = 15 − 4x.",
      "opties": [
        "P = −4x + 13",
        "P = −2x + 13",
        "P = −4x + 15",
        "P = 4x + 15"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 4 − 4p substitueert in h = 2t + 15, krijg je h = −8p + 23.",
      "antwoord": true,
      "uitleg": "Waar. h = 2(4 − 4p) + 15 = 8 − 8p + 15, dus h = −8p + 23. Zonder haakjes vergeet je 4p met 2 te vermenigvuldigen."
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: b = 3t − 20   B: t = 4p + 10",
      "modelantwoord": "b = 12p + 10",
      "sleutelwoorden": [
        "12p/12p",
        "+ 10/+10"
      ],
      "minTreffers": 2,
      "uitleg": "b = 3(4p + 10) − 20 = 12p + 10."
    }
  ]
});
