/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 115 — §2.5 Drie vormen van kwadratische formules (2/5, oefenen)
   Bron: Noordhoff H2 Parabolen (§2.5)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-25-2",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Proeftoets 115 — §2.5 Drie vormen van kwadratische formules (2/5, oefenen)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x + 1)(x + 5) zonder haakjes.",
      "uitleg": "Eerst (x + 1)(x + 5) = x² + 6x + 5. Dan elke term keer −2: y = −2x² − 12x − 10.",
      "opties": [
        "y = −2x² + 12x − 10",
        "y = −2x² − 12x + 10",
        "y = −2x² + 6x + 5",
        "y = −2x² − 12x − 10"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ½x(x + 2) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "1",
      "uitleg": "(x + 2)x = x² + 2x; keer 0,5 geeft y = ½x² + x, dus b = 1."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −2(x − 5)(x + 3) in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "30",
      "uitleg": "(x − 5)(x + 3) = x² − 2x − 15; keer −2 geeft y = −2x² + 4x + 30, dus c = 30."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 4(x + 3)² − 13 zonder haakjes.",
      "uitleg": "(x + 3)² = x² + 6x + 9 (niet x² + 9!). Keer 4: 4x² + 24x + 36. Daarna − 13: y = 4x² + 24x + 23.",
      "opties": [
        "y = 4x² + 24x + 36",
        "y = 4x² + 23",
        "y = 4x² + 24x + 23",
        "y = 4x² + 24x − 16"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = ¼(x + 4)² − 11 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "2",
      "uitleg": "(x + 4)² = x² + 8x + 16; keer 0,25 → ¼x² + 2x + 4; − 11 → y = ¼x² + 2x − 7. Dus b = 2."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x − 4)² − 10 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "54",
      "uitleg": "(x − 4)² = x² − 8x + 16; keer 4 → 4x² − 32x + 64; − 10 → y = 4x² − 32x + 54. Dus c = 54."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = ½(x − 9)(x + 3) is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Zonder haakjes is het getal voor x² gelijk aan ½: een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 3(x + 2)² + 8 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan 3: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −½(x + 6)² − 7?",
      "uitleg": "Bij x = −6 is (x + 6)² = 0; dat is de kleinste (of grootste) waarde van de term met x. Dan is y = −7. De top is (−6, −7).",
      "opties": [
        "(6, 7)",
        "(−6, 7)",
        "(−6, −7)",
        "(6, −7)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de parabool bij y = ½(x − 2)² − 17. Wat is de x-coördinaat van de top?",
      "antwoord": "2",
      "uitleg": "Bij de topvorm y = a(x − p)² + q is de top (p, q). Hier is p = 2, dus de x-coördinaat van de top is 2."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de parabool bij y = −2(x − 6)² + 12. Wat is de y-coördinaat van de top?",
      "antwoord": "12",
      "uitleg": "Bij de topvorm y = a(x − p)² + q is de top (p, q). Hier is q = 12, dus de y-coördinaat van de top is 12."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de snijpunten van de parabool bij y = ½(x + 7)(x − 3) met de x-as?",
      "uitleg": "Stel y = 0: ½(x + 7)(x − 3) = 0. Dit levert direct x = −7 en x = 3. De snijpunten met de x-as zijn (−7, 0) en (3, 0).",
      "opties": [
        "(7, 0) en (−3, 0)",
        "(−7, 0) en (3, 0)",
        "(0, −7) en (0, 3)",
        "(0, 7) en (0, −3)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = −(x + 1)(x + 2).",
      "antwoord": "-1,5",
      "uitleg": "De snijpunten met de x-as zijn x = −1 en x = −2. De top ligt precies in het midden: x = (−1 + (−2)) : 2 = −1,5."
    },
    {
      "type": "mc",
      "vraag": "Wat is de formule van de symmetrieas van de parabool bij y = ¼(x − 6)² − 14?",
      "uitleg": "De symmetrieas is een verticale lijn door de top (p, q), dus heeft als vergelijking x = 6.",
      "opties": [
        "x = 6",
        "x = −6",
        "x = −14",
        "y = −14"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt tussen twee bomen volgens h = 0,25(a − 3,6)² + 0,55 (h en a in meters). Hoeveel centimeter boven de grond bevindt zich het laagste punt van de hangmat?",
      "antwoord": "55",
      "uitleg": "Het laagste punt is de top (a = 3,6): h = 0,55 m = 55 cm. Bij de boom (a = 0): h = 0,25 · 3,6² + 0,55 = 3,79 m. De andere boom staat even ver aan de andere kant: a = 7,2 m."
    },
    {
      "type": "invul",
      "vraag": "Een hangmat hangt volgens h = 0,2(a − 3)² + 0,65 (h en a in meters, a vanaf de linkerboom). Op welke hoogte in meters is de hangmat aan de boom vastgeknoopt?",
      "antwoord": "2,45",
      "uitleg": "Het laagste punt is de top (a = 3): h = 0,65 m = 65 cm. Bij de boom (a = 0): h = 0,2 · 3² + 0,65 = 2,45 m. De andere boom staat even ver aan de andere kant: a = 6 m."
    },
    {
      "type": "invul",
      "vraag": "De boog van een brug heeft de vorm h = −0,1(x − 5)² + 12, met h en x in meters. Wat is de maximale hoogte van de brug in meters?",
      "antwoord": "12",
      "uitleg": "Dit is een bergparabool in de topvorm. De top is (5, 12), dus de maximale hoogte is 12 meter."
    },
    {
      "type": "invul",
      "vraag": "Voor een onderneming geldt de winstformule W = −0,5(q − 50)(q − 150), waarbij W de winst in euro is bij q verkochte artikelen. Wat is de maximale winst in euro?",
      "antwoord": "1250",
      "uitleg": "Snijpunten met de horizontale as: q = 50 en q = 150. Midden: q = 100. W = −0,5 · (100 − 50)(100 − 150) = 1250 euro."
    },
    {
      "type": "mc",
      "vraag": "In welke vorm staat de kwadratische formule y = −3(x − 4)² − 6?",
      "uitleg": "y = −3(x − 4)² − 6 bevat een kwadraat van een tweeterm met een constante erachter, dus de topvorm.",
      "opties": [
        "de ontbonden vorm: y = a(x − s)(x − t)",
        "de topvorm van de parabool: y = a(x − p)² + q",
        "de lineaire vorm van de formule: y = ax + b",
        "de algemene vorm: y = ax² + bx + c"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −(x − 5)² + 16 zonder haakjes.",
      "uitleg": "(x − 5)² = x² − 10x + 25 (niet x² + 25!). Keer −1: −x² + 10x − 25. Daarna + 16: y = −x² + 10x − 9.",
      "opties": [
        "y = −x² + 10x − 41",
        "y = −x² − 9",
        "y = −x² + 10x − 25",
        "y = −x² + 10x − 9"
      ],
      "antwoord": 3
    }
  ]
});
