/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 94 — §2.1 Bergparabool of dalparabool (1/5, basis)
   Bron: Noordhoff H2 Parabolen (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h2_parabolen.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-21-1",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Proeftoets 94 — §2.1 Bergparabool of dalparabool (1/5, basis)",
  "vak": "Wiskunde · Hoofdstuk 2 · Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat voor soort formule is y = 4x + 8?",
      "uitleg": "In de formule y = 4x + 8 komt x alleen tot de eerste macht voor (geen x²), dus het is een lineaire formule.",
      "opties": [
        "een exponentiële formule (groeifactor)",
        "een kwadratische formule (parabool)",
        "een omgekeerd evenredige formule (hyperbool)",
        "een lineaire formule (rechte lijn)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = 5 − x − 3x². Welk getal staat voor x²?",
      "antwoord": "-3",
      "uitleg": "Kijk naar de term met x² in y = 5 − x − 3x²: die is −3x². Het getal voor x² is dus −3. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = 5x + 2x² − 7 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is 2: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = 1 − 6x − 3x² is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is −3: negatief, dus een bergparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Heeft de parabool bij de formule y = ½x² + x − 3 de opening naar boven of naar beneden gericht?",
      "uitleg": "In y = ½x² + x − 3 is het getal voor x² gelijk aan 0,5. Omdat dit positief is, is het een dalparabool met de opening naar boven.",
      "opties": [
        "opening naar links gericht (geen functie)",
        "opening naar rechts gericht (geen functie)",
        "opening naar beneden gericht (bergparabool)",
        "opening naar boven gericht (dalparabool)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = −2x² + 3x. Welk getal staat voor x²?",
      "antwoord": "-2",
      "uitleg": "Kijk naar de term met x² in y = −2x² + 3x: die is −2x². Het getal voor x² is dus −2. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "mc",
      "vraag": "Is de top van de parabool bij de formule y = −3x² + x − 5 een maximum (hoogste punt) of een minimum (laagste punt)?",
      "uitleg": "Het getal voor x² is −3. Omdat dit negatief is, is de grafiek een bergparabool. Bij een bergparabool is de top het hoogste punt (maximum).",
      "opties": [
        "een minimum (laagste punt), want het is een dalparabool",
        "noch een maximum noch een minimum, maar een buigpunt van de grafiek",
        "een maximum (hoogste punt), want het is een bergparabool",
        "een minimum (laagste punt), want het getal voor x² is negatief"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −5x² + 8 is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is −5: negatief, dus een bergparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x(2 − 3x) − 3x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-6",
      "uitleg": "x(2 − 3x) = −3x² + 2x. Samen met −3x²: y = −6x² + 2x. Het getal voor x² is −6, dus de grafiek is een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat voor soort formule is y = 5 · 2ˣ?",
      "uitleg": "In de formule y = 5 · 2ˣ staat de variabele x in de macht (exponent), dus het is een exponentiële formule.",
      "opties": [
        "een lineaire formule (rechte lijn)",
        "een kwadratische formule (parabool)",
        "een exponentiële formule (groeifactor)",
        "een omgekeerd evenredige formule (hyperbool)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = −7 + ½x² + 3x. Welk getal staat voor x²?",
      "antwoord": "0,5",
      "uitleg": "Kijk naar de term met x² in y = −7 + ½x² + 3x: die is ½x². Het getal voor x² is dus 0,5. Let op: de volgorde van de termen maakt niet uit!"
    },
    {
      "type": "mc",
      "vraag": "Heeft de parabool bij de formule y = 1 + 2x + 4x² de opening naar boven of naar beneden gericht?",
      "uitleg": "In y = 1 + 2x + 4x² is het getal voor x² gelijk aan 4. Omdat dit positief is, is het een dalparabool met de opening naar boven.",
      "opties": [
        "opening naar rechts gericht (geen functie)",
        "opening naar beneden gericht (bergparabool)",
        "opening naar links gericht (geen functie)",
        "opening naar boven gericht (dalparabool)"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −2 − 4x + 2x² is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is 2: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Is de top van de parabool bij de formule y = −½x² − 6x + 3 een maximum (hoogste punt) of een minimum (laagste punt)?",
      "uitleg": "Het getal voor x² is −0,5. Omdat dit negatief is, is de grafiek een bergparabool. Bij een bergparabool is de top het hoogste punt (maximum).",
      "opties": [
        "een minimum (laagste punt), want het getal voor x² is negatief",
        "een maximum (hoogste punt), want het is een bergparabool",
        "een minimum (laagste punt), want het is een dalparabool",
        "noch een maximum noch een minimum, maar een buigpunt van de grafiek"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (x + 3)(−2 − 2x) + 4x²?",
      "uitleg": "(x + 3)(−2 − 2x) = −2x² − 8x − 6. Samen met 4x²: y = 2x² − 8x − 6.",
      "opties": [
        "een bergparabool, want de formule begint met een minteken",
        "een dalparabool, want na haakjes wegwerken staat er 2x²",
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −2x²"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (3x + 4)² − 18x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-9",
      "uitleg": "(3x + 4)² = (3x + 4)(3x + 4) = 9x² + 24x + 16. Samen met −18x²: y = −9x² + 24x + 16. Het getal voor x² is −9, dus de grafiek is een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Een voetballer schopt een bal weg. De baan wordt beschreven door de formule h = −0,05a² + 1,2a + 2, met h en a in meters. Vanaf welke hoogte (a = 0) vertrekt het voorwerp?",
      "antwoord": "2",
      "uitleg": "Vul a = 0 in de formule in: h = −0,05 · 0² + 1,2 · 0 + 2 = 2 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (9 − x)(9 + x) + 4x²?",
      "uitleg": "(9 − x)(9 + x) = −x² + 81. Samen met 4x²: y = 3x² + 81.",
      "opties": [
        "een rechte lijn, want er staan haakjes in de formule",
        "een dalparabool, want na haakjes wegwerken staat er 3x²",
        "een bergparabool, want de formule begint met een minteken",
        "een bergparabool, want na haakjes wegwerken staat er −3x²"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij een bergparabool? (Werk de haakjes weg en kijk alleen naar het teken van het getal voor x².)",
      "uitleg": "Bij een bergparabool is na het wegwerken van de haakjes het getal voor x² negatief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 474 300\" width=\"474\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"474\" height=\"300\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c1\"><rect x=\"40.0\" y=\"30.0\" width=\"384.0\" height=\"240.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"270.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"270.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"270.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"270.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"270.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"270.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"270.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"270.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"270.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"270.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"270.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"270.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"270.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"352.0\" y1=\"270.0\" x2=\"352.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"376.0\" y1=\"270.0\" x2=\"376.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"400.0\" y1=\"270.0\" x2=\"400.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"424.0\" y1=\"270.0\" x2=\"424.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"270.0\" x2=\"424.0\" y2=\"270.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"424.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"424.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"424.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"424.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"424.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"424.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"424.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"424.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"424.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"424.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"424.0\" y2=\"150.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"232.0\" y1=\"270.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−8</text><text x=\"64.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−7</text><text x=\"88.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"112.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"136.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"160.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"184.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"208.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"256.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"280.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"304.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"328.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"352.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"376.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"400.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"424.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"middle\">8</text><text x=\"227.0\" y=\"274.0\" fill=\"#333\" text-anchor=\"end\">−10</text><text x=\"227.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"227.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"227.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"227.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"227.0\" y=\"130.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"227.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"227.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"227.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"227.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">10</text><text x=\"227.0\" y=\"165.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"430.0\" y=\"154.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"228.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c1)\" points=\"40.0,3786.0 44.8,3643.4 49.6,3503.8 54.4,3367.0 59.2,3233.0 64.0,3102.0 68.8,2973.8 73.6,2848.6 78.4,2726.2 83.2,2606.6 88.0,2490.0 92.8,2376.2 97.6,2265.4 102.4,2157.4 107.2,2052.2 112.0,1950.0 116.8,1850.6 121.6,1754.2 126.4,1660.6 131.2,1569.8 136.0,1482.0 140.8,1397.0 145.6,1315.0 150.4,1235.8 155.2,1159.4 160.0,1086.0 164.8,1015.4 169.6,947.8 174.4,883.0 179.2,821.0 184.0,762.0 188.8,705.8 193.6,652.6 198.4,602.2 203.2,554.6 208.0,510.0 212.8,468.2 217.6,429.4 222.4,393.4 227.2,360.2 232.0,330.0 236.8,302.6 241.6,278.2 246.4,256.6 251.2,237.8 256.0,222.0 260.8,209.0 265.6,199.0 270.4,191.8 275.2,187.4 280.0,186.0 284.8,187.4 289.6,191.8 294.4,199.0 299.2,209.0 304.0,222.0 308.8,237.8 313.6,256.6 318.4,278.2 323.2,302.6 328.0,330.0 332.8,360.2 337.6,393.4 342.4,429.4 347.2,468.2 352.0,510.0 356.8,554.6 361.6,602.2 366.4,652.6 371.2,705.8 376.0,762.0 380.8,821.0 385.6,883.0 390.4,947.8 395.2,1015.4 400.0,1086.0 404.8,1159.4 409.6,1235.8 414.4,1315.0 419.2,1397.0 424.0,1482.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = x(4 − 4x) + 5x²",
        "y = (4x − 1)² + 4x²",
        "y = (7 − x)(7 + x) − 3x²",
        "y = x(7 − 3x) + 4x²"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Een basketbalspeler gooit de bal vanaf 1 m hoogte richting de basket. Na 21 m horizontale afstand is de bal weer op 1 m hoogte. Neem h voor de hoogte in meters en a voor de afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte horen?",
      "uitleg": "Werk de haakjes weg. h = −¼a(a − 21) + 1: h = −¼a² + 5,25a + 1 — het getal voor a² is negatief, dus een bergparabool. Bij h = ¼a(a − 21) + 1 en h = −¼a(21 − a) + 1 is het getal voor a² positief (dalparabool); h = ¼a² + 1 is eveneens een dalparabool.",
      "opties": [
        "h = −¼a(21 − a) + 1",
        "h = ¼a² + 1",
        "h = −¼a(a − 21) + 1",
        "h = ¼a(a − 21) + 1"
      ],
      "antwoord": 2
    }
  ]
});
