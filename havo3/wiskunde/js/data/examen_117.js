/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 117 — §2.5 Drie vormen van kwadratische formules (4/5, toetsniveau)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-4",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 117 — §2.5 Drie vormen van kwadratische formules (4/5, toetsniveau)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 3(x − 3)(x − 5) zonder haakjes.",
      "uitleg": "Eerst (x − 3)(x − 5) = x² − 8x + 15. Dan elke term keer 3: y = 3x² − 24x + 45.",
      "opties": [
        "y = 3x² − 24x − 45",
        "y = 3x² + 24x + 45",
        "y = 3x² − 24x + 45",
        "y = 3x² − 8x + 15"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ¼(x − 4)² + 11 zonder haakjes.",
      "uitleg": "(x − 4)² = x² − 8x + 16 (niet x² + 16!). Keer 0,25: ¼x² − 2x + 4. Daarna + 11: y = ¼x² − 2x + 15.",
      "opties": [
        "y = ¼x² − 2x + 15",
        "y = ¼x² + 15",
        "y = ¼x² − 2x + 6,75",
        "y = ¼x² − 2x + 4"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −½(x + 3)(x + 1) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-2",
      "uitleg": "(x + 3)(x + 1) = x² + 4x + 3; keer −0,5 geeft y = −½x² − 2x − 1,5, dus b = −2."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x − 4)(x − 6) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "72",
      "uitleg": "(x − 4)(x − 6) = x² − 10x + 24; keer 3 geeft y = 3x² − 30x + 72, dus c = 72."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ½(x + 6)² − 4 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "6",
      "uitleg": "(x + 6)² = x² + 12x + 36; keer 0,5 → ½x² + 6x + 18; − 4 → y = ½x² + 6x + 14. Dus b = 6."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x + 1)² − 4 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-7",
      "uitleg": "(x + 1)² = x² + 2x + 1; keer −3 → −3x² − 6x − 3; − 4 → y = −3x² − 6x − 7. Dus c = −7."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −½(x − 9)(x − 3) is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan −½: een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = −(x + 7)(x − 7) is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan −1: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 4(x − 5)² − 11?",
      "uitleg": "Bij x = 5 is (x − 5)² = 0; dat is de kleinste (of grootste) waarde van de term met x. Dan is y = −11. De top is (5, −11).",
      "opties": [
        "(−5, −11)",
        "(5, 11)",
        "(−5, 11)",
        "(5, −11)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = 2(x + 3)(x − 7) met de x-as?",
      "uitleg": "Stel y = 0: 2(x + 3)(x − 7) = 0. Dit levert direct x = −3 en x = 7. De snijpunten met de x-as zijn (−3, 0) en (7, 0).",
      "opties": [
        "(3, 0) en (−7, 0)",
        "(−3, 0) en (7, 0)",
        "(0, 3) en (0, −7)",
        "(0, −3) en (0, 7)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −2(x − 7)(x − 4).",
      "antwoord": "5,5",
      "uitleg": "De snijpunten met de x-as zijn x = 7 en x = 4. De top ligt precies in het midden: x = (7 + 4) : 2 = 5,5."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij y = −2(x − 4)(x + 1).",
      "antwoord": "12,5",
      "uitleg": "De top heeft x = 1,5. Vul dit in de formule in: y = −2 · (1,5 − 4)(1,5 − (−1)) = 12,5."
    },
    {
      "type": "invul",
      "vraag": "Voor een onderneming geldt de winstformule W = −0,5(q − 100)(q − 300), waarbij W de winst in euro is bij q verkochte artikelen. Wat is de maximale winst in euro?",
      "antwoord": "5000",
      "uitleg": "Snijpunten met de horizontale as: q = 100 en q = 300. Midden: q = 200. W = −0,5 · (200 − 100)(200 − 300) = 5000 euro."
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt volgens h = 0,25(a − 2,8)² + 0,45 (h en a in meters, a vanaf de linkerboom). Op welke hoogte in meters is de hangmat aan de boom vastgeknoopt?",
      "antwoord": "2,41",
      "uitleg": "Het laagste punt is de top (a = 2,8): h = 0,45 m = 45 cm. Bij de boom (a = 0): h = 0,25 · 2,8² + 0,45 = 2,41 m. De andere boom staat even ver aan de andere kant: a = 5,6 m."
    },
    {
      "type": "invul",
      "vraag": "Tussen twee bomen hangt een hangmat symmetrisch volgens h = 0,2(a − 2)² + 0,3 (h en a in meters, a gemeten vanaf de linkerboom). Wat is de afstand tussen de twee bomen in meters?",
      "antwoord": "4",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,3 m = 30 cm. Bij de boom (a = 0): h = 0,2 · 2² + 0,3 = 1,1 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,5(x − 14)² + 6, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "6",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (14, 6), dus de maximale hoogte is 6 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van de symmetrieas van de parabool bij y = −2(x + 3)² − 7?",
      "uitleg": "De symmetrieas is een verticale lijn door de top (p, q), dus heeft als vergelijking x = −3.",
      "opties": [
        "x = −7",
        "x = 3",
        "x = −3",
        "y = −7"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "In welke vorm staat de kwadratische formule y = −4x² + 3x + 1?",
      "uitleg": "y = −4x² + 3x + 1 is geschreven als afzonderlijke termen ax² + bx + c, dus de algemene vorm.",
      "opties": [
        "de lineaire vorm van de formule: y = ax + b",
        "de ontbonden vorm: y = a(x − s)(x − t)",
        "de algemene vorm: y = ax² + bx + c",
        "de topvorm van de parabool: y = a(x − p)² + q"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = ½(x − 9)(x − 5) zonder haakjes.",
      "uitleg": "Eerst (x − 9)(x − 5) = x² − 14x + 45. Dan elke term keer 0,5: y = ½x² − 7x + 22,5.",
      "opties": [
        "y = ½x² − 7x + 22,5",
        "y = ½x² − 7x − 22,5",
        "y = ½x² + 7x + 22,5",
        "y = ½x² − 14x + 45"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 4(x − 6)² + 1 zonder haakjes.",
      "uitleg": "(x − 6)² = x² − 12x + 36 (niet x² + 36!). Keer 4: 4x² − 48x + 144. Daarna + 1: y = 4x² − 48x + 145.",
      "opties": [
        "y = 4x² − 48x + 144",
        "y = 4x² + 145",
        "y = 4x² − 48x + 148",
        "y = 4x² − 48x + 145"
      ],
      "antwoord": 3
    }
  ]
});
