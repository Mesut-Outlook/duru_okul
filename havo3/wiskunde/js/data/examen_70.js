/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 70 — §2.5 Drie vormen van kwadratische formules (2/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-10",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 70 — §2.5 Drie vormen van kwadratische formules (2/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x − 1)² − 15 zonder haakjes.",
      "uitleg": "(x − 1)² = (x − 1)(x − 1) = x² − 2x + 1 (niet x² + 1!). Keer 3: 3x² − 6x + 3. Daarna − 15: y = 3x² − 6x − 12.",
      "opties": [
        "y = 3x² − 6x − 42",
        "y = 3x² − 6x + 3",
        "y = 3x² − 6x − 12",
        "y = 3x² − 12"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 2(x + 9)(x + 7) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "126",
      "uitleg": "(x + 9)(x + 7) = x² + 16x + 63; keer 2 geeft y = 2x² + 32x + 126, dus c = 126."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x + 1)² + 8 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "8",
      "uitleg": "(x + 1)² = x² + 2x + 1; keer 4 → 4x² + 8x + 4; + 8 → y = 4x² + 8x + 12. Dus b = 8."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −3(x + 8)(x + 2) zonder haakjes.",
      "uitleg": "Eerst (x + 8)(x + 2) = x² + 10x + 16. Dan elke term keer −3: y = −3x² − 30x − 48.",
      "opties": [
        "y = −3x² + 30x − 48",
        "y = −3x² − 30x + 48",
        "y = −3x² − 30x − 48",
        "y = −3x² + 10x + 16"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3(x − 6)² − 18?",
      "uitleg": "Bij x = 6 is (x − 6)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = −18. Top (6, −18). Let op: bij (x − 6) hoort x = 6, bij (x + 6) hoort x = −6.",
      "opties": [
        "(6, −18)",
        "(6, 18)",
        "(−6, 18)",
        "(−6, −18)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x − 5)(x − 3) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-24",
      "uitleg": "(x − 5)(x − 3) = x² − 8x + 15; keer 3 geeft y = 3x² − 24x + 45, dus b = −24."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ½(x + 2)² + 2 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "4",
      "uitleg": "(x + 2)² = x² + 4x + 4; keer 0,5 → ½x² + 2x + 2; + 2 → y = ½x² + 2x + 4. Dus c = 4."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 3(x − 9)(x − 3) is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan 3: een dalparabool."
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt volgens h = 0,5(a − 2)² + 0,6 (h en a in meters, a vanaf de linkerboom, symmetrisch tussen de bomen). Hoeveel meter staan de bomen uit elkaar?",
      "antwoord": "4",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,6 m = 60 cm. Bij de boom (a = 0): h = 0,5 · 2² + 0,6 = 2,6 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x + 4)² + 9 zonder haakjes.",
      "uitleg": "(x + 4)² = (x + 4)(x + 4) = x² + 8x + 16 (niet x² + 16!). Keer 3: 3x² + 24x + 48. Daarna + 9: y = 3x² + 24x + 57.",
      "opties": [
        "y = 3x² + 24x + 75",
        "y = 3x² + 24x + 48",
        "y = 3x² + 57",
        "y = 3x² + 24x + 57"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ½x(x + 4) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "2",
      "uitleg": "x(x + 4) = x² + 4x; keer 0,5 geeft y = ½x² + 2x, dus b = 2."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −2(x − 1)(x − 7) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-14",
      "uitleg": "(x − 1)(x − 7) = x² − 8x + 7; keer −2 geeft y = −2x² + 16x − 14, dus c = −14."
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,5(q − 200)(q − 400). Bereken de maximale winst in euro.",
      "antwoord": "5000",
      "uitleg": "Snijpunten met de horizontale as: q = 200 en q = 400. Midden: q = 300. W = −0,5 · (300 − 200)(300 − 400) = 5000 euro."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −2(x − 2)(x + 6) is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan −2: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x + 2)² − 1 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "15",
      "uitleg": "(x + 2)² = x² + 4x + 4; keer 4 → 4x² + 16x + 16; − 1 → y = 4x² + 16x + 15. Dus c = 15."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −½(x − 1)(x − 9) zonder haakjes.",
      "uitleg": "Eerst (x − 1)(x − 9) = x² − 10x + 9. Dan elke term keer −0,5: y = −½x² + 5x − 4,5.",
      "opties": [
        "y = −½x² − 5x − 4,5",
        "y = −½x² + 5x + 4,5",
        "y = −½x² − 10x + 9",
        "y = −½x² + 5x − 4,5"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,5(a − 2,5)² + 0,5. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "50",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,5 m = 50 cm. Bij de boom (a = 0): h = 0,5 · 2,5² + 0,5 = 3,625 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x − 2)² − 4?",
      "uitleg": "Bij x = 2 is (x − 2)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = −4. Top (2, −4). Let op: bij (x − 2) hoort x = 2, bij (x + 2) hoort x = −2.",
      "opties": [
        "(2, 4)",
        "(2, −4)",
        "(−2, 4)",
        "(−2, −4)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x − 1)² − 1 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-8",
      "uitleg": "(x − 1)² = x² − 2x + 1; keer 4 → 4x² − 8x + 4; − 1 → y = 4x² − 8x + 3. Dus b = −8."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ½(x + 6)² − 13 zonder haakjes.",
      "uitleg": "(x + 6)² = (x + 6)(x + 6) = x² + 12x + 36 (niet x² + 36!). Keer 0,5: ½x² + 6x + 18. Daarna − 13: y = ½x² + 6x + 5.",
      "opties": [
        "y = ½x² + 6x + 11,5",
        "y = ½x² + 6x + 5",
        "y = ½x² + 6x + 18",
        "y = ½x² + 5"
      ],
      "antwoord": 1
    }
  ]
});
