/* =========================================================
   Duru's Wiskunde (HAVO 3) — Onderwerp §2.1 Bergparabool of dalparabool
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.register({
  "id": "h2-parabolen-1",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Bergparabool of dalparabool",
  "korteUitleg": "Aan het getal voor x² zie je of de grafiek een bergparabool of een dalparabool is — soms pas na haakjes wegwerken.",
  "icoon": "⛰️",
  "kleur": "blauw",
  "theorie": "<h3>§2.1 Parabolen</h3>\n<p>Een formule waarin x² de hoogste macht is, heet een <b>kwadratische formule</b>, bijvoorbeeld y = x² − 4x − 8 of y = −2x² + 12. De grafiek bij zo'n formule heet een <b>parabool</b>. Een parabool is symmetrisch: links en rechts van de <b>top</b> zie je dezelfde vorm in spiegelbeeld.</p>\n<h4>Bergparabool of dalparabool?</h4>\n<div class=\"formule-box\">Getal voor x² <b>positief</b> → <b>dalparabool</b> (opening naar boven, de top is het laagste punt)<br>Getal voor x² <b>negatief</b> → <b>bergparabool</b> (opening naar beneden, de top is het hoogste punt)</div>\n<p>Voorbeelden: y = ½x² + 2 is een dalparabool (½ is positief). y = −½x² + 2x is een bergparabool. De volgorde van de termen maakt niet uit: bij y = −4x + 5x² staat er 5 voor x², dus een dalparabool. Let op: bij y = x² − 7x + 5 staat er een (onzichtbare) 1 voor x²; bij y = −x² + 12x + 7 een −1.</p>\n<h4>Eerst de haakjes wegwerken</h4>\n<p>Staan er haakjes in de formule, dan zie je het getal voor x² niet meteen. Schrijf de formule dan eerst <b>zonder haakjes</b> en tel de termen met x² bij elkaar op. Een <b>vermenigvuldigtabel</b> helpt om niets te vergeten.</p>\n<div class=\"formule-box\">Voorbeeld: y = (2x + 7)(3 − x) + 3x²<br>(2x + 7)(3 − x) = 6x − 2x² + 21 − 7x = −2x² − x + 21<br>y = −2x² − x + 21 + 3x² = x² − x + 21 → getal voor x² is 1 → <b>dalparabool</b></div>\n<p>Veelgemaakte fouten:</p><ul><li>(2x − 1)² is níet 4x² + 1, maar (2x − 1)(2x − 1) = 4x² − 4x + 1.</li><li>Bij −x(x − 8) wordt het −x² + 8x: het minteken gaat over beide termen.</li><li>Vergeet de losse term met x² achter de haakjes niet (bijvoorbeeld + 3x² of − 2x²).</li></ul>\n<h4>In context</h4><p>De baan van een geschoten of gegooide bal is een bergparabool. Bij h = −0,3a(a − 8) + 2,1 werk je de haakjes weg: h = −0,3a² + 2,4a + 2,1. Het getal voor a² is negatief, dus deze formule kan bij een bal horen. Bij h = 0,3a(a − 8) + 2,1 is het getal positief: een dalparabool, en dat past niet bij een bal.</p>",
  "vragen": [
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = ½x² + 9x − 8 is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is ½: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (4x − 1)² + 14x²?",
      "uitleg": "(4x − 1)² = (4x − 1)(4x − 1) = 16x² − 8x + 1. Samen met 14x²: y = 30x² − 8x + 1.",
      "opties": [
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −30x²",
        "een bergparabool, want de formule begint met een minteken",
        "een dalparabool, want na haakjes wegwerken staat er 30x²"
      ],
      "antwoord": 3
    },
    {
      "type": "invoer",
      "vraag": "Gegeven is de formule y = x(5 − 2x) − 5x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-7|−7",
      "uitleg": "x(5 − 2x) = −2x² + 5x. Samen met −5x²: y = −7x² + 5x. Het getal voor x² is −7, dus de grafiek is een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (3x − 5)² + 14x² is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. (3x − 5)² = (3x − 5)(3x − 5) = 9x² − 30x + 25. Samen met 14x²: y = 23x² − 30x + 25. Het getal voor x² is 23: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een dalparabool met top (−2, −4). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een dalparabool is na het wegwerken van de haakjes het getal voor x² positief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c1\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c1)\" points=\"40.0,-18.0 43.6,-3.9 47.2,9.7 50.8,22.8 54.4,35.3 58.0,47.2 61.6,58.7 65.2,69.6 68.8,79.9 72.4,89.7 76.0,99.0 79.6,107.7 83.2,115.9 86.8,123.6 90.4,130.7 94.0,137.2 97.6,143.3 101.2,148.8 104.8,153.7 108.4,158.1 112.0,162.0 115.6,165.3 119.2,168.1 122.8,170.4 126.4,172.1 130.0,173.2 133.6,173.9 137.2,174.0 140.8,173.5 144.4,172.5 148.0,171.0 151.6,168.9 155.2,166.3 158.8,163.2 162.4,159.5 166.0,155.2 169.6,150.5 173.2,145.2 176.8,139.3 180.4,132.9 184.0,126.0 187.6,118.5 191.2,110.5 194.8,102.0 198.4,92.9 202.0,83.2 205.6,73.1 209.2,62.4 212.8,51.1 216.4,39.3 220.0,27.0 223.6,14.1 227.2,0.7 230.8,-13.2 234.4,-27.7 238.0,-42.8 241.6,-58.3 245.2,-74.4 248.8,-91.1 252.4,-108.3 256.0,-126.0 259.6,-144.3 263.2,-163.1 266.8,-182.4 270.4,-202.3 274.0,-222.8 277.6,-243.7 281.2,-265.2 284.8,-287.3 288.4,-309.9 292.0,-333.0 295.6,-356.7 299.2,-380.9 302.8,-405.6 306.4,-430.9 310.0,-456.8 313.6,-483.1 317.2,-510.0 320.8,-537.5 324.4,-565.5 328.0,-594.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = (5 − x)(5 + x) − 3x²",
        "y = (3x − 1)(−3 + x) + x²",
        "y = (2x − 1)(−1 − 2x) − 4x²",
        "y = (8 − x)(8 + x) − x²"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −5 + 2x + 3x² is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is 3: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Een basketbalspeler gooit een bal vanaf 1,8 m hoogte richting het basket. Na 13 m horizontale afstand is de bal weer op 1,8 m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
      "uitleg": "Werk de haakjes weg. h = −0,2a(a − 13) + 1,8: h = −0,2a² + 2,6a + 1,8 — het getal voor a² is negatief, dus een bergparabool. Bij h = 0,2a(a − 13) + 1,8 en h = −0,2a(13 − a) + 1,8 is het getal voor a² positief (dalparabool); h = 0,2a² + 1,8 is ook een dalparabool.",
      "opties": [
        "h = 0,2a² + 1,8",
        "h = −0,2a(a − 13) + 1,8",
        "h = −0,2a(13 − a) + 1,8",
        "h = 0,2a(a − 13) + 1,8"
      ],
      "antwoord": 1
    },
    {
      "type": "invoer",
      "vraag": "Gegeven is de formule y = (4 − x)(4 + x) − x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-2|−2",
      "uitleg": "(4 − x)(4 + x) = −x² + 16. Samen met −x²: y = −2x² + 16. Het getal voor x² is −2, dus de grafiek is een bergparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x(7 − 2x) + 6x² is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. x(7 − 2x) = −2x² + 7x. Samen met 6x²: y = 4x² + 7x. Het getal voor x² is 4: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (−x − 5)(−5 − 2x) + 4x²?",
      "uitleg": "(−x − 5)(−5 − 2x) = 2x² + 15x + 25. Samen met 4x²: y = 6x² + 15x + 25.",
      "opties": [
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −6x²",
        "een dalparabool, want na haakjes wegwerken staat er 6x²",
        "een bergparabool, want de formule begint met een minteken"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een dalparabool met top (−2, −3). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een dalparabool is na het wegwerken van de haakjes het getal voor x² positief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c2)\" points=\"40.0,-222.0 43.6,-193.7 47.2,-166.6 50.8,-140.5 54.4,-115.4 58.0,-91.5 61.6,-68.6 65.2,-46.9 68.8,-26.2 72.4,-6.5 76.0,12.0 79.6,29.5 83.2,45.8 86.8,61.1 90.4,75.4 94.0,88.5 97.6,100.6 101.2,111.5 104.8,121.4 108.4,130.3 112.0,138.0 115.6,144.7 119.2,150.2 122.8,154.7 126.4,158.2 130.0,160.5 133.6,161.8 137.2,161.9 140.8,161.0 144.4,159.1 148.0,156.0 151.6,151.9 155.2,146.6 158.8,140.3 162.4,133.0 166.0,124.5 169.6,115.0 173.2,104.3 176.8,92.6 180.4,79.9 184.0,66.0 187.6,51.1 191.2,35.0 194.8,17.9 198.4,-0.2 202.0,-19.5 205.6,-39.8 209.2,-61.3 212.8,-83.8 216.4,-107.3 220.0,-132.0 223.6,-157.7 227.2,-184.6 230.8,-212.5 234.4,-241.4 238.0,-271.5 241.6,-302.6 245.2,-334.9 248.8,-368.2 252.4,-402.5 256.0,-438.0 259.6,-474.5 263.2,-512.2 266.8,-550.9 270.4,-590.6 274.0,-631.5 277.6,-673.4 281.2,-716.5 284.8,-760.6 288.4,-805.7 292.0,-852.0 295.6,-899.3 299.2,-947.8 302.8,-997.3 306.4,-1047.8 310.0,-1099.5 313.6,-1152.2 317.2,-1206.1 320.8,-1261.0 324.4,-1316.9 328.0,-1374.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = (2x + 2)² + 3x²",
        "y = (x + 1)(3 − 2x) − 3x²",
        "y = x(9 − 3x) − 6x²",
        "y = x(5 − 2x) − x²"
      ],
      "antwoord": 0
    },
    {
      "type": "invoer",
      "vraag": "Gegeven is de formule y = (6 − x)(6 + x) − x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-2|−2",
      "uitleg": "(6 − x)(6 + x) = −x² + 36. Samen met −x²: y = −2x² + 36. Het getal voor x² is −2, dus de grafiek is een bergparabool."
    }
  ]
});
