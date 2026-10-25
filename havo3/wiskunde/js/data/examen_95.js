/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 95 — §2.1 Bergparabool of dalparabool (2/5, oefenen)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-21-2",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Proeftoets 95 — §2.1 Bergparabool of dalparabool (2/5, oefenen)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = 3 − 9x + 3x². Welk getal staat voor x²?",
      "antwoord": "3",
      "uitleg": "Kijk naar de term met x² in y = 3 − 9x + 3x²: die is 3x². Het getal voor x² is dus 3. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −x² + 2x − 8 is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is −1: negatief, dus een bergparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Heeft de parabool bij de formule y = 6 − 5x − ¼x² de opening naar boven of naar beneden gericht?",
      "uitleg": "In y = 6 − 5x − ¼x² is het getal voor x² gelijk aan −0,25. Omdat dit negatief is, is het een bergparabool met de opening naar beneden.",
      "opties": [
        "opening naar boven gericht (dalparabool)",
        "opening naar beneden gericht (bergparabool)",
        "opening naar rechts gericht (geen functie)",
        "opening naar links gericht (geen functie)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (2x + 4)² + 3x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "7",
      "uitleg": "(2x + 4)² = (2x + 4)(2x + 4) = 4x² + 16x + 16. Samen met 3x²: y = 7x² + 16x + 16. Het getal voor x² is 7, dus de grafiek is een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = 7x + ½x² + 1 is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is ½: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = −5x² + 6x + 8. Welk getal staat voor x²?",
      "antwoord": "-5",
      "uitleg": "Kijk naar de term met x² in y = −5x² + 6x + 8: die is −5x². Het getal voor x² is dus −5. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "mc",
      "vraag": "Is de top van de parabool bij de formule y = ½x² + 5 een maximum (hoogste punt) of een minimum (laagste punt)?",
      "uitleg": "Het getal voor x² is 0,5. Omdat dit positief is, is de grafiek een dalparabool. Bij een dalparabool is de top het laagste punt (minimum).",
      "opties": [
        "een minimum (laagste punt), want het is een dalparabool",
        "een maximum (hoogste punt), want het is een bergparabool",
        "een maximum (hoogste punt), want de formule heeft positieve termen",
        "noch een maximum noch een minimum, maar een buigpunt van de grafiek"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x(2 − 4x) + 6x² is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. x(2 − 4x) = −4x² + 2x. Samen met 6x²: y = 2x² + 2x. Het getal voor x² is 2: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (8 − x)(8 + x) + 3x²?",
      "uitleg": "(8 − x)(8 + x) = −x² + 64. Samen met 3x²: y = 2x² + 64.",
      "opties": [
        "een dalparabool, want na haakjes wegwerken staat er 2x²",
        "een bergparabool, want de formule begint met een minteken",
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −2x²"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −7x + 2x² + 1 is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is 2: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (x − 3)(−1 + 2x) + 2x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "4",
      "uitleg": "(x − 3)(−1 + 2x) = 2x² − 7x + 3. Samen met 2x²: y = 4x² − 7x + 3. Het getal voor x² is 4, dus de grafiek is een dalparabool."
    },
    {
      "type": "invul",
      "vraag": "Schrijf de formule y = ((x − 5))((x + 2)) − 1 zonder haakjes. Wat is het losse getal c (zonder x)?",
      "antwoord": "-11",
      "uitleg": "Werk de haakjes uit: ((x − 5))((x + 2)) = y = x² − 3x − 10. Samen met -1: y = x² − 3x − 11. Het losse getal zonder x is dus −11."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (9 − x)(9 + x) − x² is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. (9 − x)(9 + x) = −x² + 81. Samen met −x²: y = −2x² + 81. Het getal voor x² is −2: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = 9x − ¼x² − 5. Welk getal staat voor x²?",
      "antwoord": "-0,25",
      "uitleg": "Kijk naar de term met x² in y = 9x − ¼x² − 5: die is −¼x². Het getal voor x² is dus −0,25. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (3 − x)(3 + x) − 4x²?",
      "uitleg": "(3 − x)(3 + x) = −x² + 9. Samen met −4x²: y = −5x² + 9.",
      "opties": [
        "een dalparabool, want na haakjes wegwerken staat er 5x²",
        "een dalparabool, want de formule begint met een plusteken",
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −5x²"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −8 − ¼x² is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is −¼: negatief, dus een bergparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (2 − x)(2 + x) − x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-2",
      "uitleg": "(2 − x)(2 + x) = −x² + 4. Samen met −x²: y = −2x² + 4. Het getal voor x² is −2, dus de grafiek is een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (7 − x)(7 + x) − 4x² is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. (7 − x)(7 + x) = −x² + 49. Samen met −4x²: y = −5x² + 49. Het getal voor x² is −5: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een dalparabool met top (−4, −4) die de y-as snijdt in (0, 12). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een dalparabool is na het wegwerken van de haakjes het getal voor x² positief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 474 300\" width=\"474\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"474\" height=\"300\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"40.0\" y=\"30.0\" width=\"384.0\" height=\"240.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"270.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"270.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"270.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"270.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"270.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"270.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"270.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"270.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"270.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"270.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"270.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"270.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"270.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"352.0\" y1=\"270.0\" x2=\"352.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"376.0\" y1=\"270.0\" x2=\"376.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"400.0\" y1=\"270.0\" x2=\"400.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"424.0\" y1=\"270.0\" x2=\"424.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"270.0\" x2=\"424.0\" y2=\"270.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"424.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"424.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"424.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"424.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"424.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"424.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"424.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"424.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"424.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"424.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"424.0\" y2=\"150.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"232.0\" y1=\"270.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−8</text><text x=\"64.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−7</text><text x=\"88.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"112.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"136.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"160.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"184.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"208.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"256.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"280.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"304.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"328.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"352.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"376.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"400.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"424.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">8</text><text x=\"227.0\" y=\"274.0\" fill=\"#333\" text-anchor=\"end\">−10</text><text x=\"227.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"227.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"227.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"227.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"227.0\" y=\"130.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"227.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"227.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"227.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"227.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">10</text><text x=\"227.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"430.0\" y=\"154.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"228.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c2)\" points=\"40.0,6.0 44.8,24.7 49.6,42.5 54.4,59.3 59.2,75.1 64.0,90.0 68.8,103.9 73.6,116.9 78.4,128.9 83.2,139.9 88.0,150.0 92.8,159.1 97.6,167.3 102.4,174.5 107.2,180.7 112.0,186.0 116.8,190.3 121.6,193.7 126.4,196.1 131.2,197.5 136.0,198.0 140.8,197.5 145.6,196.1 150.4,193.7 155.2,190.3 160.0,186.0 164.8,180.7 169.6,174.5 174.4,167.3 179.2,159.1 184.0,150.0 188.8,139.9 193.6,128.9 198.4,116.9 203.2,103.9 208.0,90.0 212.8,75.1 217.6,59.3 222.4,42.5 227.2,24.7 232.0,6.0 236.8,-13.7 241.6,-34.3 246.4,-55.9 251.2,-78.5 256.0,-102.0 260.8,-126.5 265.6,-151.9 270.4,-178.3 275.2,-205.7 280.0,-234.0 284.8,-263.3 289.6,-293.5 294.4,-324.7 299.2,-356.9 304.0,-390.0 308.8,-424.1 313.6,-459.1 318.4,-495.1 323.2,-532.1 328.0,-570.0 332.8,-608.9 337.6,-648.7 342.4,-689.5 347.2,-731.3 352.0,-774.0 356.8,-817.7 361.6,-862.3 366.4,-907.9 371.2,-954.5 376.0,-1002.0 380.8,-1050.5 385.6,-1099.9 390.4,-1150.3 395.2,-1201.7 400.0,-1254.0 404.8,-1307.3 409.6,-1361.5 414.4,-1416.7 419.2,-1472.9 424.0,-1530.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = x(2 − 4x) + 3x²",
        "y = x(5 + 3x) − 2x²",
        "y = (7 − x)(7 + x) − 2x²",
        "y = x(4 − 5x) − 2x²"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een volleyballer gooit de bal vanaf 2,5 m hoogte richting de netrand. Na 20 m horizontale afstand is de bal weer op 2,5 m hoogte. Neem h voor de hoogte in meters en a voor de afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte horen?",
      "uitleg": "Werk de haakjes weg. h = −¼a(a − 20) + 2,5: h = −¼a² + 5a + 2,5 — het getal voor a² is negatief, dus een bergparabool. Bij h = ¼a(a − 20) + 2,5 en h = −¼a(20 − a) + 2,5 is het getal voor a² positief (dalparabool); h = ¼a² + 2,5 is eveneens een dalparabool.",
      "opties": [
        "h = ¼a² + 2,5",
        "h = ¼a(a − 20) + 2,5",
        "h = −¼a(20 − a) + 2,5",
        "h = −¼a(a − 20) + 2,5"
      ],
      "antwoord": 3
    }
  ]
});
