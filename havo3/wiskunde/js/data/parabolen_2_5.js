/* =========================================================
   Duru's Wiskunde (HAVO 3) — Onderwerp §2.5 Drie vormen van kwadratische formules
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.register({
  "id": "h2-parabolen-5",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Drie vormen van kwadratische formules",
  "korteUitleg": "Schrijf y = a(x − s)(x − t) en y = a(x − p)² + q in de vorm y = ax² + bx + c.",
  "icoon": "⛰️",
  "kleur": "blauw",
  "theorie": "<h3>§2.5 Drie vormen van kwadratische formules</h3>\n<p>Een kwadratische formule kan op drie manieren geschreven zijn:</p>\n<div class=\"formule-box\">y = ax² + bx + c — algemene vorm: snijpunt met de y-as (0, c)<br>y = a(x − s)(x − t) — snijpunten met de x-as (s, 0) en (t, 0)<br>y = a(x − p)² + q — top (p, q)</div>\n<p>In alle drie de vormen is a hetzelfde getal: het bepaalt berg/dal en smal/breed.</p>\n<h4>Van y = a(x − s)(x − t) naar de algemene vorm</h4>\n<p>Werk eerst de haakjes (x − s)(x − t) weg met een vermenigvuldigtabel. Vermenigvuldig daarna <b>elke term</b> met a.</p>\n<div class=\"formule-box\">y = −2(x + 3)(x − 4)<br>(x + 3)(x − 4) = x² − 4x + 3x − 12 = x² − x − 12<br>y = −2(x² − x − 12) = −2x² + 2x + 24</div>\n<h4>Van y = a(x − p)² + q naar de algemene vorm</h4>\n<p>(x − p)² betekent (x − p)(x − p). Werk dat uit, vermenigvuldig elke term met a en tel q er pas daarna bij op.</p>\n<div class=\"formule-box\">y = 2(x + 3)² + 4<br>(x + 3)² = x² + 6x + 9<br>y = 2(x² + 6x + 9) + 4 = 2x² + 12x + 18 + 4 = 2x² + 12x + 22</div>\n<p>Veelgemaakte fouten: (x + 3)² = x² + 9 (de middelste term 6x vergeten); alleen x² met a vermenigvuldigen; q óók met a vermenigvuldigen. Controleer je antwoord door een getal in te vullen, bijvoorbeeld x = 0 of x = 1, in beide formules.</p>\n<h4>In context</h4><p>Bij een hangmat met h = 0,25(a − 2,4)² + 0,5 lees je de top direct af: het laagste punt ligt bij a = 2,4 op 0,5 m = 50 cm hoogte. Bij een winstformule W = −0,6(q − 300)(q − 450) zijn q = 300 en q = 450 de aantallen waarbij de winst 0 is; de maximale winst hoort bij q = 375.</p>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −3x(x + 4) zonder haakjes.",
      "uitleg": "Eerst (x + 4)x = x² + 4x. Dan elke term keer −3: y = −3x² − 12x.",
      "opties": [
        "y = x² − 12x",
        "y = −3x² + 4x",
        "y = −3x² − 12x",
        "y = −3x² + 12x"
      ],
      "antwoord": 2
    },
    {
      "type": "invoer",
      "vraag": "Schrijf y = −3(x + 6)(x + 8) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-42|−42",
      "uitleg": "(x + 6)(x + 8) = x² + 14x + 48; keer −3 geeft y = −3x² − 42x − 144, dus b = −42."
    },
    {
      "type": "invoer",
      "vraag": "Schrijf y = −3(x + 6)(x + 8) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-144|−144",
      "uitleg": "(x + 6)(x + 8) = x² + 14x + 48; keer −3 geeft y = −3x² − 42x − 144, dus c = −144."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x − 4)² + 6 zonder haakjes.",
      "uitleg": "(x − 4)² = (x − 4)(x − 4) = x² − 8x + 16 (niet x² + 16!). Keer −2: −2x² + 16x − 32. Daarna + 6: y = −2x² + 16x − 26.",
      "opties": [
        "y = −2x² + 16x − 26",
        "y = −2x² + 16x − 32",
        "y = −2x² + 16x − 44",
        "y = −2x² − 26"
      ],
      "antwoord": 0
    },
    {
      "type": "invoer",
      "vraag": "Schrijf y = −½(x − 6)² + 4 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "6",
      "uitleg": "(x − 6)² = x² − 12x + 36; keer −0,5 → −½x² + 6x − 18; + 4 → y = −½x² + 6x − 14. Dus b = 6."
    },
    {
      "type": "invoer",
      "vraag": "Schrijf y = −3(x − 3)² − 10 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-37|−37",
      "uitleg": "(x − 3)² = x² − 6x + 9; keer −3 → −3x² + 18x − 27; − 10 → y = −3x² + 18x − 37. Dus c = −37."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2(x + 2)² + 3?",
      "uitleg": "Bij x = −2 is (x + 2)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = 3. Top (−2, 3). Let op: bij (x − 2) hoort x = 2, bij (x + 2) hoort x = −2.",
      "opties": [
        "(2, 3)",
        "(−2, 3)",
        "(2, −3)",
        "(−2, −3)"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 4(x − 4)² − 9 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan 4: een dalparabool."
    },
    {
      "type": "invoer",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,25(a − 2,5)² + 0,6. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "60",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,6 m = 60 cm. Bij de boom (a = 0): h = 0,25 · 2,5² + 0,6 = 2,1625 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "invoer",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,4(q − 100)(q − 200). Bereken de maximale winst in euro.",
      "antwoord": "1000",
      "uitleg": "Snijpunten met de horizontale as: q = 100 en q = 200. Midden: q = 150. W = −0,4 · (150 − 100)(150 − 200) = 1000 euro."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x + 2)(x − 8) zonder haakjes.",
      "uitleg": "Eerst (x + 2)(x − 8) = x² − 6x − 16. Dan elke term keer −2: y = −2x² + 12x + 32.",
      "opties": [
        "y = −2x² − 6x − 16",
        "y = −2x² + 12x − 32",
        "y = −2x² − 12x + 32",
        "y = −2x² + 12x + 32"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 4(x + 1)² − 18 zonder haakjes.",
      "uitleg": "(x + 1)² = (x + 1)(x + 1) = x² + 2x + 1 (niet x² + 1!). Keer 4: 4x² + 8x + 4. Daarna − 18: y = 4x² + 8x − 14.",
      "opties": [
        "y = 4x² + 8x − 68",
        "y = 4x² + 8x − 14",
        "y = 4x² − 14",
        "y = 4x² + 8x + 4"
      ],
      "antwoord": 1
    }
  ]
});
