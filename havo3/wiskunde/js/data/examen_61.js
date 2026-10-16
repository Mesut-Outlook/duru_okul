/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 61 — §2.1 Bergparabool of dalparabool (1/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-1",
  "hoofdstuk": 2,
  "paragraaf": "2.1",
  "titel": "Proeftoets 61 — §2.1 Bergparabool of dalparabool (1/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = −6 − 5x + ½x² is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is ½: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x² − 7x + 9 is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is 1: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = x(2 − 4x) + 6x²?",
      "uitleg": "x(2 − 4x) = −4x² + 2x. Samen met 6x²: y = 2x² + 2x.",
      "opties": [
        "een rechte lijn, want er staan haakjes in de formule",
        "een bergparabool, want na haakjes wegwerken staat er −2x²",
        "een bergparabool, want de formule begint met een minteken",
        "een dalparabool, want na haakjes wegwerken staat er 2x²"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (2 − x)(2 + x) + 3x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "2",
      "uitleg": "(2 − x)(2 + x) = −x² + 4. Samen met 3x²: y = 2x² + 4. Het getal voor x² is 2, dus de grafiek is een dalparabool."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x(2 − 4x) + 3x² is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. x(2 − 4x) = −4x² + 2x. Samen met 3x²: y = −x² + 2x. Het getal voor x² is −1: een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een bergparabool met top (−1, −1). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een bergparabool is na het wegwerken van de haakjes het getal voor x² negatief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c7\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c7)\" points=\"40.0,1038.0 43.6,984.8 47.2,933.2 50.8,883.3 54.4,835.0 58.0,788.2 61.6,743.2 65.2,699.7 68.8,657.8 72.4,617.6 76.0,579.0 79.6,542.0 83.2,506.6 86.8,472.9 90.4,440.8 94.0,410.2 97.6,381.4 101.2,354.1 104.8,328.4 108.4,304.4 112.0,282.0 115.6,261.2 119.2,242.0 122.8,224.5 126.4,208.6 130.0,194.2 133.6,181.6 137.2,170.5 140.8,161.0 144.4,153.2 148.0,147.0 151.6,142.4 155.2,139.4 158.8,138.1 162.4,138.4 166.0,140.2 169.6,143.8 173.2,148.9 176.8,155.6 180.4,164.0 184.0,174.0 187.6,185.6 191.2,198.8 194.8,213.7 198.4,230.2 202.0,248.2 205.6,268.0 209.2,289.3 212.8,312.2 216.4,336.8 220.0,363.0 223.6,390.8 227.2,420.2 230.8,451.3 234.4,484.0 238.0,518.2 241.6,554.2 245.2,591.7 248.8,630.8 252.4,671.6 256.0,714.0 259.6,758.0 263.2,803.6 266.8,850.9 270.4,899.8 274.0,950.2 277.6,1002.4 281.2,1056.1 284.8,1111.4 288.4,1168.4 292.0,1227.0 295.6,1287.2 299.2,1349.0 302.8,1412.5 306.4,1477.6 310.0,1544.2 313.6,1612.6 317.2,1682.5 320.8,1754.0 324.4,1827.2 328.0,1902.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = (4 − x)(4 + x) + 3x²",
        "y = x(4 + 2x) − 4x²",
        "y = x(6 + 3x) + x²",
        "y = (3x + 1)(−3 + 2x) − 2x²"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = 3x² + 2x + 6 is een bergparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. Het getal voor x² is 3: positief, dus een dalparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x(5 − 3x) − 6x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-9",
      "uitleg": "x(5 − 3x) = −3x² + 5x. Samen met −6x²: y = −9x² + 5x. Het getal voor x² is −9, dus de grafiek is een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Een basketbalspeler gooit een bal vanaf 2 m hoogte richting het basket. Na 8 m horizontale afstand is de bal weer op 2 m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
      "uitleg": "Werk de haakjes weg. h = −0,3a(a − 8) + 2: h = −0,3a² + 2,4a + 2 — het getal voor a² is negatief, dus een bergparabool. Bij h = 0,3a(a − 8) + 2 en h = −0,3a(8 − a) + 2 is het getal voor a² positief (dalparabool); h = 0,3a² + 2 is ook een dalparabool.",
      "opties": [
        "h = −0,3a(a − 8) + 2",
        "h = −0,3a(8 − a) + 2",
        "h = 0,3a² + 2",
        "h = 0,3a(a − 8) + 2"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x(8 + 3x) + 3x² is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. x(8 + 3x) = 3x² + 8x. Samen met 3x²: y = 6x² + 8x. Het getal voor x² is 6: een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = x(8 + 3x) − 2x²?",
      "uitleg": "x(8 + 3x) = 3x² + 8x. Samen met −2x²: y = x² + 8x.",
      "opties": [
        "een bergparabool, want de formule begint met een minteken",
        "een bergparabool, want na haakjes wegwerken staat er −x²",
        "een dalparabool, want na haakjes wegwerken staat er x²",
        "een rechte lijn, want er staan haakjes in de formule"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x(3 − 3x) + 6x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "3",
      "uitleg": "x(3 − 3x) = −3x² + 3x. Samen met 6x²: y = 3x² + 3x. Het getal voor x² is 3, dus de grafiek is een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een dalparabool met top (3, −1). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een dalparabool is na het wegwerken van de haakjes het getal voor x² positief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c8\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c8)\" points=\"40.0,-2778.0 43.6,-2681.6 47.2,-2586.8 50.8,-2493.7 54.4,-2402.2 58.0,-2312.2 61.6,-2224.0 65.2,-2137.3 68.8,-2052.2 72.4,-1968.8 76.0,-1887.0 79.6,-1806.8 83.2,-1728.2 86.8,-1651.3 90.4,-1576.0 94.0,-1502.2 97.6,-1430.2 101.2,-1359.7 104.8,-1290.8 108.4,-1223.6 112.0,-1158.0 115.6,-1094.0 119.2,-1031.6 122.8,-970.9 126.4,-911.8 130.0,-854.2 133.6,-798.4 137.2,-744.1 140.8,-691.4 144.4,-640.4 148.0,-591.0 151.6,-543.2 155.2,-497.0 158.8,-452.5 162.4,-409.6 166.0,-368.2 169.6,-328.6 173.2,-290.5 176.8,-254.0 180.4,-219.2 184.0,-186.0 187.6,-154.4 191.2,-124.4 194.8,-96.1 198.4,-69.4 202.0,-44.2 205.6,-20.8 209.2,1.1 212.8,21.4 216.4,40.0 220.0,57.0 223.6,72.4 227.2,86.2 230.8,98.3 234.4,108.8 238.0,117.8 241.6,125.0 245.2,130.7 248.8,134.8 252.4,137.2 256.0,138.0 259.6,137.2 263.2,134.8 266.8,130.7 270.4,125.0 274.0,117.8 277.6,108.8 281.2,98.3 284.8,86.2 288.4,72.4 292.0,57.0 295.6,40.0 299.2,21.4 302.8,1.1 306.4,-20.8 310.0,-44.2 313.6,-69.4 317.2,-96.1 320.8,-124.4 324.4,-154.4 328.0,-186.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = (4x + 2)² + 12x²",
        "y = x(6 − 5x) − 2x²",
        "y = (2x + 2)(6 − 2x) − 2x²",
        "y = (3 − x)(3 + x) − 2x²"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = 6x − 3x² + 5 is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. Het getal voor x² is −3: negatief, dus een bergparabool. Let op: de volgorde van de termen maakt niet uit."
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (6 − x)(6 + x) − 3x² is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. (6 − x)(6 + x) = −x² + 36. Samen met −3x²: y = −4x² + 36. Het getal voor x² is −4: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (x + 2)² + 3x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "4",
      "uitleg": "(x + 2)² = (x + 2)(x + 2) = x² + 4x + 4. Samen met 3x²: y = 4x² + 4x + 4. Het getal voor x² is 4, dus de grafiek is een dalparabool."
    },
    {
      "type": "mc",
      "vraag": "Een volleyballer gooit een bal vanaf 2,1 m hoogte richting het net. Na 10 m horizontale afstand is de bal weer op 2,1 m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
      "uitleg": "Werk de haakjes weg. h = −0,4a(a − 10) + 2,1: h = −0,4a² + 4a + 2,1 — het getal voor a² is negatief, dus een bergparabool. Bij h = 0,4a(a − 10) + 2,1 en h = −0,4a(10 − a) + 2,1 is het getal voor a² positief (dalparabool); h = 0,4a² + 2,1 is ook een dalparabool.",
      "opties": [
        "h = −0,4a(10 − a) + 2,1",
        "h = 0,4a(a − 10) + 2,1",
        "h = 0,4a² + 2,1",
        "h = −0,4a(a − 10) + 2,1"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Wat voor grafiek hoort bij de formule y = (3x − 1)² − 18x²?",
      "uitleg": "(3x − 1)² = (3x − 1)(3x − 1) = 9x² − 6x + 1. Samen met −18x²: y = −9x² − 6x + 1.",
      "opties": [
        "een dalparabool, want na haakjes wegwerken staat er 9x²",
        "een dalparabool, want de formule begint met een plusteken",
        "een bergparabool, want na haakjes wegwerken staat er −9x²",
        "een rechte lijn, want er staan haakjes in de formule"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (9 − x)(9 + x) − 2x² is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. (9 − x)(9 + x) = −x² + 81. Samen met −2x²: y = −3x² + 81. Het getal voor x² is −3: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (−x + 5)(1 − x) − 4x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-3",
      "uitleg": "(−x + 5)(1 − x) = x² − 6x + 5. Samen met −4x²: y = −3x² − 6x + 5. Het getal voor x² is −3, dus de grafiek is een bergparabool."
    }
  ]
});
