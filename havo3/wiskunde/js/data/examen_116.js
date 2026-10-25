/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 116 — §2.5 Drie vormen van kwadratische formules (3/5, gemengd)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-3",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 116 — §2.5 Drie vormen van kwadratische formules (3/5, gemengd)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x − 3)(x − 4) zonder haakjes.",
      "uitleg": "Eerst (x − 3)(x − 4) = x² − 7x + 12. Dan elke term keer 3: y = 3x² − 21x + 36.",
      "opties": [
        "y = 3x² + 21x + 36",
        "y = 3x² − 21x − 36",
        "y = 3x² − 21x + 36",
        "y = 3x² − 7x + 12"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ½(x − 2)² − 12 zonder haakjes.",
      "uitleg": "(x − 2)² = x² − 4x + 4 (niet x² + 4!). Keer 0,5: ½x² − 2x + 2. Daarna − 12: y = ½x² − 2x − 10.",
      "opties": [
        "y = ½x² − 2x − 4",
        "y = ½x² − 2x + 2",
        "y = ½x² − 2x − 10",
        "y = ½x² − 10"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x + 1)(x + 5) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "24",
      "uitleg": "(x + 1)(x + 5) = x² + 6x + 5; keer 4 geeft y = 4x² + 24x + 20, dus b = 24."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −(x − 6)² + 8 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "12",
      "uitleg": "(x − 6)² = x² − 12x + 36; keer −1 → −x² + 12x − 36; + 8 → y = −x² + 12x − 28. Dus b = 12."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −2(x − 1)(x + 9) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "18",
      "uitleg": "(x − 1)(x + 9) = x² + 8x − 9; keer −2 geeft y = −2x² − 16x + 18, dus c = 18."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 2(x + 5)² − 8 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "42",
      "uitleg": "(x + 5)² = x² + 10x + 25; keer 2 → 2x² + 20x + 50; − 8 → y = 2x² + 20x + 42. Dus c = 42."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −½(x + 8)(x − 6) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −½: een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = ¼(x − 4)² − 10 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan ¼: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −(x + 3)(x + 7) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −1: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2(x + 4)² + 20?",
      "uitleg": "Bij x = −4 is (x + 4)² = 0; dat is de kleinste (of grootste) waarde van de term met x. Dan is y = 20. De top is (−4, 20).",
      "opties": [
        "(−4, 20)",
        "(−4, −20)",
        "(4, −20)",
        "(4, 20)"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x − 9)(x − 5).",
      "antwoord": "7",
      "uitleg": "De snijpunten met de x-as zijn x = 9 en x = 5. De top ligt precies in het midden: x = (9 + 5) : 2 = 7."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −(x + 8)(x + 4).",
      "antwoord": "4",
      "uitleg": "De top heeft x = −6. Vul dit in de formule in: y = − · (−6 − (−8))(−6 − (−4)) = 4."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = (x + 5)(x + 3) snijdt de x-as in twee punten. Wat is de kleinste x-coördinaat van deze twee snijpunten?",
      "antwoord": "-5",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = −5 of x = −3. De kleinste x-coördinaat hiervan is −5."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = ½(x + 6)(x − 6) snijdt de x-as in twee punten. Wat is de grootste x-coördinaat van deze twee snijpunten?",
      "antwoord": "6",
      "uitleg": "De snijpunten met de x-as vind je via y = 0: x = −6 of x = 6. De grootste x-coördinaat hiervan is 6."
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van de symmetrieas van de parabool bij y = −(x − 6)² − 4?",
      "uitleg": "De symmetrieas is een verticale lijn door de top (p, q), dus heeft als vergelijking x = 6.",
      "opties": [
        "x = 6",
        "y = −4",
        "x = −6",
        "x = −4"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Tussen twee bomen hangt een hangmat volgens de formule h = 0,3(a − 2)² + 0,65 (h en a in meters, a vanaf de linkerboom). Wat is de hoogte van het laagste punt in cm boven de grond?",
      "antwoord": "65",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,65 m = 65 cm. Bij de boom (a = 0): h = 0,3 · 2² + 0,65 = 1,85 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "invul",
      "vraag": "Tussen twee bomen hangt een hangmat symmetrisch volgens h = 0,5(a − 2,5)² + 0,45 (h en a in meters, a gemeten vanaf de linkerboom). Wat is de afstand tussen de twee bomen in meters?",
      "antwoord": "5",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,45 m = 45 cm. Bij de boom (a = 0): h = 0,5 · 2,5² + 0,45 = 3,575 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,4(q − 300)(q − 400). Bereken de maximale winst in euro.",
      "antwoord": "1000",
      "uitleg": "Snijpunten met de horizontale as: q = 300 en q = 400. Midden: q = 350. W = −0,4 · (350 − 300)(350 − 400) = 1000 euro."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,2(x − 8)² + 13, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "13",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (8, 13), dus de maximale hoogte is 13 meter."
    },
    {
      "type": "mc",
      "vraag": "In welke vorm staat de kwadratische formule y = 2(x − 2)² − 20?",
      "uitleg": "y = 2(x − 2)² − 20 bevat een kwadraat van een tweeterm met een constante erachter, dus de topvorm.",
      "opties": [
        "de algemene vorm: y = ax² + bx + c",
        "de lineaire vorm van de formule: y = ax + b",
        "de ontbonden vorm: y = a(x − s)(x − t)",
        "de topvorm van de parabool: y = a(x − p)² + q"
      ],
      "antwoord": 3
    }
  ]
});
