/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 114 — §2.5 Drie vormen van kwadratische formules (1/5, basis)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-1",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 114 — §2.5 Drie vormen van kwadratische formules (1/5, basis)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "In welke vorm staat de kwadratische formule y = −(x − 3)(x − 7)?",
      "uitleg": "y = −(x − 3)(x − 7) is geschreven als product van factoren (x − s)(x − t), dus de ontbonden vorm.",
      "opties": [
        "de lineaire vorm van de formule: y = ax + b",
        "de topvorm van de parabool: y = a(x − p)² + q",
        "de algemene vorm: y = ax² + bx + c",
        "de ontbonden vorm: y = a(x − s)(x − t)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x − 1)(x − 9) met de x-as?",
      "uitleg": "Stel y = 0: 2(x − 1)(x − 9) = 0. Dit levert direct x = 1 en x = 9. De snijpunten met de x-as zijn (1, 0) en (9, 0).",
      "opties": [
        "(−1, 0) en (−9, 0)",
        "(0, −1) en (0, −9)",
        "(0, 1) en (0, 9)",
        "(1, 0) en (9, 0)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 4(x − 2)² − 15?",
      "uitleg": "Bij x = 2 is (x − 2)² = 0; dat is de kleinste (of grootste) waarde van de term met x. Dan is y = −15. De top is (2, −15).",
      "opties": [
        "(2, −15)",
        "(−2, 15)",
        "(−2, −15)",
        "(2, 15)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de parabool bij y = 4(x + 6)² + 18. Wat is de x-coördinaat van de top?",
      "antwoord": "-6",
      "uitleg": "Bij de topvorm y = a(x − p)² + q is de top (p, q). Hier is p = −6, dus de x-coördinaat van de top is −6."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de parabool bij y = −½(x − 2)² + 19. Wat is de y-coördinaat van de top?",
      "antwoord": "19",
      "uitleg": "Bij de topvorm y = a(x − p)² + q is de top (p, q). Hier is q = 19, dus de y-coördinaat van de top is 19."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 2x(x + 2) is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan 2: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −2(x − 5)² + 17 is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −2: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2(x − 2)(x + 6) snijdt de x-as in twee punten. Wat is de kleinste x-coördinaat van deze twee snijpunten?",
      "antwoord": "-6",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = 2 of x = −6. De kleinste x-coördinaat hiervan is −6."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2(x + 3)(x + 5) snijdt de x-as in twee punten. Wat is de grootste x-coördinaat van deze twee snijpunten?",
      "antwoord": "-3",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = −3 of x = −5. De grootste x-coördinaat hiervan is −3."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x + 9)(x + 6) zonder haakjes.",
      "uitleg": "Eerst (x + 9)(x + 6) = x² + 15x + 54. Dan elke term keer 3: y = 3x² + 45x + 162.",
      "opties": [
        "y = 3x² + 45x + 162",
        "y = 3x² + 45x − 162",
        "y = 3x² − 45x + 162",
        "y = 3x² + 15x + 54"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −x(x − 2) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "2",
      "uitleg": "x(x − 2) = x² − 2x; keer −1 geeft y = −x² + 2x, dus b = 2."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x + 9)(x + 7) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "189",
      "uitleg": "(x + 9)(x + 7) = x² + 16x + 63; keer 3 geeft y = 3x² + 48x + 189, dus c = 189."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x + 4)² + 16 zonder haakjes.",
      "uitleg": "(x + 4)² = x² + 8x + 16 (niet x² + 16!). Keer −2: −2x² − 16x − 32. Daarna + 16: y = −2x² − 16x − 16.",
      "opties": [
        "y = −2x² − 16x − 32",
        "y = −2x² − 16x − 64",
        "y = −2x² − 16x − 16",
        "y = −2x² − 16"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x − 1)² + 14 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "6",
      "uitleg": "(x − 1)² = x² − 2x + 1; keer −3 → −3x² + 6x − 3; + 14 → y = −3x² + 6x + 11. Dus b = 6."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x − 4)² + 15 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "63",
      "uitleg": "(x − 4)² = x² − 8x + 16; keer 3 → 3x² − 24x + 48; + 15 → y = 3x² − 24x + 63. Dus c = 63."
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van de symmetrieas van de parabool bij y = −(x + 4)² − 11?",
      "uitleg": "De symmetrieas is een verticale lijn door de top (p, q), dus heeft als vergelijking x = −4.",
      "opties": [
        "y = −11",
        "x = −4",
        "x = 4",
        "x = −11"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt tussen twee bomen volgens h = 0,2(a − 2,4)² + 0,35 (h en a in meters). Hoeveel centimeter boven de grond bevindt zich het laagste punt van de hangmat?",
      "antwoord": "35",
      "uitleg": "Het laagste punt is de top (a = 2,4): h = 0,35 m = 35 cm. Bij de boom (a = 0): h = 0,2 · 2,4² + 0,35 = 1,502 m. De andere boom staat even ver aan de andere kant: a = 4,8 m."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,25(x − 10)² + 17, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "17",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (10, 17), dus de maximale hoogte is 17 meter."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −(x − 7)(x + 4) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −1: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ½(x − 8)(x + 8) zonder haakjes.",
      "uitleg": "Eerst (x − 8)(x + 8) = x² − 64. Dan elke term keer 0,5: y = ½x² − 32.",
      "opties": [
        "y = ½x² + 32",
        "y = ½x² − 32",
        "y = x² − 32",
        "y = ½x² − 64"
      ],
      "antwoord": 1
    }
  ]
});
