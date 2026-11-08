/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 69 — §2.5 Drie vormen van kwadratische formules (1/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-9",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 69 — §2.5 Drie vormen van kwadratische formules (1/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x + 5)(x − 3) zonder haakjes.",
      "uitleg": "Eerst (x + 5)(x − 3) = x² + 2x − 15. Dan elke term keer −2: y = −2x² − 4x + 30.",
      "opties": [
        "y = −2x² + 4x + 30",
        "y = −2x² + 2x − 15",
        "y = −2x² − 4x + 30",
        "y = −2x² − 4x − 30"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Herleid de tweeterm-formule y = (6x + 1)² − 19x² door de uitdrukking te schrijven zonder haakjes. Welk coëfficiënt-getal staat er uiteindelijk voor x²?",
      "antwoord": "17",
      "uitleg": "Stap 1: Werk het kwadraat uit:\n(6x + 1)² = 36x² + 12x + 1.\nStap 2: Trek 19x² af:\ny = 36x² + 12x + 1 − 19x² = 17x² + 12x + 1.\nVoor x² staat het getal 17."
    },
    {
      "type": "invul",
      "vraag": "De gebogen doorgang van een spoorwegtunnel volgt h = −0,4x² + 2,4x, waarin h de hoogte in meters is en x de afstand over het wegdek. Bereken de hoogte van het hoogste punt van de tunnel (in meters).",
      "antwoord": "3,6",
      "uitleg": "Stap 1: Bereken de x-coördinaat van de top:\nx = −2,4 / (2 · −0,4) = 3 meter.\nStap 2: Vul x = 3 in de formule in:\nh = −0,4 · 3² + 2,4 · 3 = −3,6 + 7,2 = 3,6 meter."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −(x + 1)² − 7 zonder haakjes.",
      "uitleg": "(x + 1)² = (x + 1)(x + 1) = x² + 2x + 1 (niet x² + 1!). Keer −1: −x² − 2x − 1. Daarna − 7: y = −x² − 2x − 8.",
      "opties": [
        "y = −x² − 2x − 8",
        "y = −x² − 2x − 1",
        "y = −x² − 2x + 6",
        "y = −x² − 8"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x − 6)² + 18 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "36",
      "uitleg": "(x − 6)² = x² − 12x + 36; keer −3 → −3x² + 36x − 108; + 18 → y = −3x² + 36x − 90. Dus b = 36."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x − 6)² + 5 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "113",
      "uitleg": "(x − 6)² = x² − 12x + 36; keer 3 → 3x² − 36x + 108; + 5 → y = 3x² − 36x + 113. Dus c = 113."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −(x + 6)² − 11?",
      "uitleg": "Bij x = −6 is (x + 6)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = −11. Top (−6, −11). Let op: bij (x − 6) hoort x = 6, bij (x + 6) hoort x = −6.",
      "opties": [
        "(6, −11)",
        "(6, 11)",
        "(−6, 11)",
        "(−6, −11)"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −3(x − 5)² + 13 is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan −3: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x + 6)(x − 1) zonder haakjes.",
      "uitleg": "Eerst (x + 6)(x − 1) = x² + 5x − 6. Dan elke term keer −2: y = −2x² − 10x + 12.",
      "opties": [
        "y = −2x² + 5x − 6",
        "y = −2x² + 10x + 12",
        "y = −2x² − 10x + 12",
        "y = −2x² − 10x − 12"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −(x + 6)(x − 8) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "48",
      "uitleg": "(x + 6)(x − 8) = x² − 2x − 48; keer −1 geeft y = −x² + 2x + 48, dus c = 48."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x − 2)² − 3 zonder haakjes.",
      "uitleg": "(x − 2)² = (x − 2)(x − 2) = x² − 4x + 4 (niet x² + 4!). Keer −2: −2x² + 8x − 8. Daarna − 3: y = −2x² + 8x − 11.",
      "opties": [
        "y = −2x² + 8x − 11",
        "y = −2x² + 8x − 2",
        "y = −2x² − 11",
        "y = −2x² + 8x − 8"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ¼(x + 2)² + 3 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "1",
      "uitleg": "(x + 2)² = x² + 4x + 4; keer 0,25 → ¼x² + x + 1; + 3 → y = ¼x² + x + 4. Dus b = 1."
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,5(a − 2,4)² + 0,6. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "60",
      "uitleg": "Het laagste punt is de top (a = 2,4): h = 0,6 m = 60 cm. Bij de boom (a = 0): h = 0,5 · 2,4² + 0,6 = 3,48 m. De andere boom staat even ver aan de andere kant: a = 4,8 m."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −2(x − 5)(x − 8) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −2: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Een getekende dalparabool met top (5, −6) passeert de verticale as in (0, 19). Welke formule heeft de vorm y = ax² + bx + c? Bereken de waarde van b.",
      "antwoord": "-10",
      "uitleg": "Stap 1: Gebruik de topvorm met top (5, −6):\ny = a(x − 5)² − 6.\nStap 2: Vul (0, 19) in:\n19 = 25a − 6 → 25a = 25 → a = 1.\nStap 3: Werk de haakjes uit:\ny = 1(x² − 10x + 25) − 6 = x² − 10x + 19.\nVoor x staat het getal b = −10."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x − 3)² − 5 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-32",
      "uitleg": "(x − 3)² = x² − 6x + 9; keer −3 → −3x² + 18x − 27; − 5 → y = −3x² + 18x − 32. Dus c = −32."
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,5(q − 300)(q − 450). Bereken de maximale winst in euro.",
      "antwoord": "2812,5",
      "uitleg": "Snijpunten met de horizontale as: q = 300 en q = 450. Midden: q = 375. W = −0,5 · (375 − 300)(375 − 450) = 2812,5 euro."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 4(x − 4)² − 12?",
      "uitleg": "Bij x = 4 is (x − 4)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = −12. Top (4, −12). Let op: bij (x − 4) hoort x = 4, bij (x + 4) hoort x = −4.",
      "opties": [
        "(4, 12)",
        "(4, −12)",
        "(−4, −12)",
        "(−4, 12)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt volgens h = 0,2(a − 2)² + 0,5 (h en a in meters, a vanaf de linkerboom). Op welke hoogte in meters is de hangmat aan de boom vastgeknoopt?",
      "antwoord": "1,3",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,5 m = 50 cm. Bij de boom (a = 0): h = 0,2 · 2² + 0,5 = 1,3 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x − 2)(x + 4) zonder haakjes.",
      "uitleg": "Eerst (x − 2)(x + 4) = x² + 2x − 8. Dan elke term keer −2: y = −2x² − 4x + 16.",
      "opties": [
        "y = −2x² + 2x − 8",
        "y = −2x² − 4x + 16",
        "y = −2x² − 4x − 16",
        "y = −2x² + 4x + 16"
      ],
      "antwoord": 1
    }
  ]
});
