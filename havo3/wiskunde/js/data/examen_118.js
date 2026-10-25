/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 118 — §2.5 Drie vormen van kwadratische formules (5/5, eindniveau)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-5",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 118 — §2.5 Drie vormen van kwadratische formules (5/5, eindniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 2(x − 7)(x − 1) zonder haakjes.",
      "uitleg": "Eerst (x − 7)(x − 1) = x² − 8x + 7. Dan elke term keer 2: y = 2x² − 16x + 14.",
      "opties": [
        "y = 2x² − 8x + 7",
        "y = 2x² + 16x + 14",
        "y = 2x² − 16x − 14",
        "y = 2x² − 16x + 14"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 4(x + 6)² − 16 zonder haakjes.",
      "uitleg": "(x + 6)² = x² + 12x + 36 (niet x² + 36!). Keer 4: 4x² + 48x + 144. Daarna − 16: y = 4x² + 48x + 128.",
      "opties": [
        "y = 4x² + 48x + 128",
        "y = 4x² + 128",
        "y = 4x² + 48x + 144",
        "y = 4x² + 48x + 80"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ½(x − 4)(x + 6) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "1",
      "uitleg": "(x − 4)(x + 6) = x² + 2x − 24; keer 0,5 geeft y = ½x² + x − 12, dus b = 1."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x + 2)² − 3 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-12",
      "uitleg": "(x + 2)² = x² + 4x + 4; keer −3 → −3x² − 12x − 12; − 3 → y = −3x² − 12x − 15. Dus b = −12."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x + 9)(x + 2) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "72",
      "uitleg": "(x + 9)(x + 2) = x² + 11x + 18; keer 4 geeft y = 4x² + 44x + 72, dus c = 72."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x + 3)² − 1 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "35",
      "uitleg": "(x + 3)² = x² + 6x + 9; keer 4 → 4x² + 24x + 36; − 1 → y = 4x² + 24x + 35. Dus c = 35."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 3(x + 5)(x − 2) is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan 3: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = ¼(x − 6)² − 4 is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan ¼: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = ½x(x − 6) is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan ½: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = ¼(x − 4)² + 7?",
      "uitleg": "Bij x = 4 is (x − 4)² = 0; dat is de kleinste (of grootste) waarde van de term met x. Dan is y = 7. De top is (4, 7).",
      "opties": [
        "(4, 7)",
        "(−4, −7)",
        "(4, −7)",
        "(−4, 7)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = ½(x − 7)(x + 7).",
      "antwoord": "0",
      "uitleg": "De snijpunten met de x-as zijn x = 7 en x = −7. De top ligt precies in het midden: x = (7 + (−7)) : 2 = 0."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = (x + 9)(x − 5).",
      "antwoord": "-49",
      "uitleg": "De top heeft x = −2. Vul dit in de formule in: y =  · (−2 − (−9))(−2 − 5) = −49."
    },
    {
      "type": "invul",
      "vraag": "Voor een onderneming geldt de winstformule W = −0,5(q − 200)(q − 440), waarbij W de winst in euro is bij q verkochte artikelen. Wat is de maximale winst in euro?",
      "antwoord": "7200",
      "uitleg": "Snijpunten met de horizontale as: q = 200 en q = 440. Midden: q = 320. W = −0,5 · (320 − 200)(320 − 440) = 7200 euro."
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,3(a − 2,5)² + 0,5. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "50",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,5 m = 50 cm. Bij de boom (a = 0): h = 0,3 · 2,5² + 0,5 = 2,375 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt volgens h = 0,2(a − 2)² + 0,35 (h en a in meters, a vanaf de linkerboom, symmetrisch tussen de bomen). Hoeveel meter staan de bomen uit elkaar?",
      "antwoord": "4",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,35 m = 35 cm. Bij de boom (a = 0): h = 0,2 · 2² + 0,35 = 1,15 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,5(x − 15)² + 11, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "11",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (15, 11), dus de maximale hoogte is 11 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = (x + 1)(x − 1) met de x-as?",
      "uitleg": "Stel y = 0: (x + 1)(x − 1) = 0. Dit levert direct x = −1 en x = 1. De snijpunten met de x-as zijn (−1, 0) en (1, 0).",
      "opties": [
        "(1, 0) en (−1, 0)",
        "(0, −1) en (0, 1)",
        "(−1, 0) en (1, 0)",
        "(0, 1) en (0, −1)"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van de symmetrieas van de parabool bij y = 2(x + 2)² + 12?",
      "uitleg": "De symmetrieas is een verticale lijn door de top (p, q), dus heeft als vergelijking x = −2.",
      "opties": [
        "x = 12",
        "x = −2",
        "y = 12",
        "x = 2"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −½(x + 3)(x − 1) zonder haakjes.",
      "uitleg": "Eerst (x + 3)(x − 1) = x² + 2x − 3. Dan elke term keer −0,5: y = −½x² − x + 1,5.",
      "opties": [
        "y = −½x² − x − 1,5",
        "y = −½x² − x + 1,5",
        "y = −½x² + 2x − 3",
        "y = −½x² + x + 1,5"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −½(x − 6)² + 14 zonder haakjes.",
      "uitleg": "(x − 6)² = x² − 12x + 36 (niet x² + 36!). Keer −0,5: −½x² + 6x − 18. Daarna + 14: y = −½x² + 6x − 4.",
      "opties": [
        "y = −½x² + 6x − 18",
        "y = −½x² − 4",
        "y = −½x² + 6x − 4",
        "y = −½x² + 6x − 25"
      ],
      "antwoord": 2
    }
  ]
});
