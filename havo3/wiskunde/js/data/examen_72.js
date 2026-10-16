/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 72 — Gemengd H2 — oefenproefwerk-niveau (1/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-12",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 72 — Gemengd H2 — oefenproefwerk-niveau (1/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = (x − 5)(−5 − 2x) − x² is een dalparabool.",
      "antwoord": false,
      "uitleg": "Onwaar. (x − 5)(−5 − 2x) = −2x² + 5x + 25. Samen met −x²: y = −3x² + 5x + 25. Het getal voor x² is −3: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x(2 − 3x) − 2x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-5",
      "uitleg": "x(2 − 3x) = −3x² + 2x. Samen met −2x²: y = −5x² + 2x. Het getal voor x² is −5, dus de grafiek is een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = x² − 4x + 10?",
      "uitleg": "1 Uit x = 0 volgt y = 10. 2 x² − 4x + 10 = 10 → x² − 4x = 0 → x(x − 4) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = 2² − 4 · 2 + 10 = 6. 5 De top is (2, 6).",
      "opties": [
        "(2, 22)",
        "(2, 10)",
        "(−2, 6)",
        "(2, 6)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = 2x² + 16x + 36.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = 36. 2 2x² + 16x + 36 = 36 → 2x² + 16x = 0 → x(2x + 16) = 0 → x = 0 of x = −8. 3 De x-coördinaat van de top ligt midden tussen 0 en −8: x = −4. 4 y = 2·(−4)² + 16 · (−4) + 36 = 4. 5 De top is (−4, 4)."
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij y = 2x(x + 3). Een breuk of decimaal getal mag.",
      "antwoord": "-1,5",
      "uitleg": "2x(x + 3) = 0 → x = 0 of x = −3: de snijpunten met de x-as zijn (0, 0) en (−3, 0). De top ligt midden tussen x = 0 en x = −3: x = (0 + (−3)) / 2 = −1,5. y = 2 · (−1,5 − 0)(−1,5 − (−3)) = −4,5. Top (−1,5, −4,5)."
    },
    {
      "type": "invul",
      "vraag": "Voor de parabool bij y = x² − 6x + 18 is de tabel gemaakt rondom de top (3, 9). Welk getal hoort in de tabel bij x = 5?",
      "antwoord": "13",
      "uitleg": "y = 5² − 6 · 5 + 18 = 13.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 210 62\" width=\"210\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"208\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"66.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"79\" y1=\"1\" x2=\"79\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"105\" y1=\"1\" x2=\"105\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"118.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"131\" y1=\"1\" x2=\"131\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"144.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"157\" y1=\"1\" x2=\"157\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"183\" y1=\"1\" x2=\"183\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">6</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"66.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"79\" y1=\"31\" x2=\"79\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"105\" y1=\"31\" x2=\"105\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"118.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">9</text><line x1=\"131\" y1=\"31\" x2=\"131\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"144.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"157\" y1=\"31\" x2=\"157\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"183\" y1=\"31\" x2=\"183\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"209\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (2, −2). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = −6. 2 −x² + 4x − 6 = −6 → −x² + 4x = 0 → x(−x + 4) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = −2² + 4 · 2 − 6 = −2. 5 De top is (2, −2). Bij de andere formules ligt de top ergens anders of is het een dalparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c27\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c27)\" points=\"40.0,918.0 43.6,889.5 47.2,861.5 50.8,834.0 54.4,807.1 58.0,780.8 61.6,754.9 65.2,729.6 68.8,704.9 72.4,680.7 76.0,657.0 79.6,633.9 83.2,611.3 86.8,589.2 90.4,567.7 94.0,546.8 97.6,526.3 101.2,506.4 104.8,487.1 108.4,468.3 112.0,450.0 115.6,432.3 119.2,415.1 122.8,398.4 126.4,382.3 130.0,366.8 133.6,351.7 137.2,337.2 140.8,323.3 144.4,309.9 148.0,297.0 151.6,284.7 155.2,272.9 158.8,261.6 162.4,250.9 166.0,240.8 169.6,231.1 173.2,222.0 176.8,213.5 180.4,205.5 184.0,198.0 187.6,191.1 191.2,184.7 194.8,178.8 198.4,173.5 202.0,168.8 205.6,164.5 209.2,160.8 212.8,157.7 216.4,155.1 220.0,153.0 223.6,151.5 227.2,150.5 230.8,150.0 234.4,150.1 238.0,150.8 241.6,151.9 245.2,153.6 248.8,155.9 252.4,158.7 256.0,162.0 259.6,165.9 263.2,170.3 266.8,175.2 270.4,180.7 274.0,186.8 277.6,193.3 281.2,200.4 284.8,208.1 288.4,216.3 292.0,225.0 295.6,234.3 299.2,244.1 302.8,254.4 306.4,265.3 310.0,276.8 313.6,288.7 317.2,301.2 320.8,314.3 324.4,327.9 328.0,342.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"232.0\" cy=\"150.0\" r=\"3.5\" fill=\"#222\"/><text x=\"238.0\" y=\"144.0\" fill=\"#222\" font-size=\"11\">(2, −2)</text></svg>",
      "opties": [
        "y = −x² + 4x − 4",
        "y = x² − 4x + 6",
        "y = −x² − 4x − 6",
        "y = −x² + 4x − 6"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "In de figuur staan vier parabolen. Welke parabool hoort bij de formule y = x² + 3?",
      "uitleg": "y = x² + 3: dalparabool, top op de y-as in (0, 3). Dat past alleen bij parabool 2.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 330 252\" width=\"330\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"330\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c29\"><rect x=\"40.0\" y=\"30.0\" width=\"240.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"280.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"280.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"280.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"280.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"280.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"280.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"280.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"184.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"155.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"155.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"155.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"155.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"155.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"155.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"155.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"155.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"155.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"286.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"156.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c29)\" points=\"40.0,390.0 43.0,375.2 46.0,360.8 49.0,346.7 52.0,333.0 55.0,319.7 58.0,306.8 61.0,294.2 64.0,282.0 67.0,270.2 70.0,258.8 73.0,247.7 76.0,237.0 79.0,226.7 82.0,216.8 85.0,207.2 88.0,198.0 91.0,189.2 94.0,180.8 97.0,172.7 100.0,165.0 103.0,157.7 106.0,150.8 109.0,144.2 112.0,138.0 115.0,132.2 118.0,126.8 121.0,121.7 124.0,117.0 127.0,112.7 130.0,108.8 133.0,105.2 136.0,102.0 139.0,99.2 142.0,96.8 145.0,94.7 148.0,93.0 151.0,91.7 154.0,90.8 157.0,90.2 160.0,90.0 163.0,90.2 166.0,90.8 169.0,91.7 172.0,93.0 175.0,94.7 178.0,96.8 181.0,99.2 184.0,102.0 187.0,105.2 190.0,108.8 193.0,112.7 196.0,117.0 199.0,121.7 202.0,126.8 205.0,132.2 208.0,138.0 211.0,144.2 214.0,150.8 217.0,157.7 220.0,165.0 223.0,172.7 226.0,180.8 229.0,189.2 232.0,198.0 235.0,207.2 238.0,216.8 241.0,226.7 244.0,237.0 247.0,247.7 250.0,258.8 253.0,270.2 256.0,282.0 259.0,294.2 262.0,306.8 265.0,319.7 268.0,333.0 271.0,346.7 274.0,360.8 277.0,375.2 280.0,390.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"95.0\" y=\"202.0\" fill=\"#c2185b\" font-weight=\"bold\" font-size=\"14\">1</text><polyline clip-path=\"url(#w1c29)\" points=\"40.0,-210.0 43.0,-195.2 46.0,-180.8 49.0,-166.7 52.0,-153.0 55.0,-139.7 58.0,-126.8 61.0,-114.2 64.0,-102.0 67.0,-90.2 70.0,-78.8 73.0,-67.7 76.0,-57.0 79.0,-46.7 82.0,-36.8 85.0,-27.2 88.0,-18.0 91.0,-9.2 94.0,-0.8 97.0,7.3 100.0,15.0 103.0,22.3 106.0,29.2 109.0,35.8 112.0,42.0 115.0,47.8 118.0,53.2 121.0,58.3 124.0,63.0 127.0,67.3 130.0,71.2 133.0,74.8 136.0,78.0 139.0,80.8 142.0,83.2 145.0,85.3 148.0,87.0 151.0,88.3 154.0,89.2 157.0,89.8 160.0,90.0 163.0,89.8 166.0,89.2 169.0,88.3 172.0,87.0 175.0,85.3 178.0,83.2 181.0,80.8 184.0,78.0 187.0,74.8 190.0,71.2 193.0,67.3 196.0,63.0 199.0,58.3 202.0,53.2 205.0,47.8 208.0,42.0 211.0,35.8 214.0,29.2 217.0,22.3 220.0,15.0 223.0,7.3 226.0,-0.8 229.0,-9.2 232.0,-18.0 235.0,-27.2 238.0,-36.8 241.0,-46.7 244.0,-57.0 247.0,-67.7 250.0,-78.8 253.0,-90.2 256.0,-102.0 259.0,-114.2 262.0,-126.8 265.0,-139.7 268.0,-153.0 271.0,-166.7 274.0,-180.8 277.0,-195.2 280.0,-210.0\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.6\"/><text x=\"198.2\" y=\"73.7\" fill=\"#2563eb\" font-weight=\"bold\" font-size=\"14\">2</text><polyline clip-path=\"url(#w1c29)\" points=\"40.0,-294.0 43.0,-276.2 46.0,-258.8 49.0,-241.7 52.0,-225.0 55.0,-208.7 58.0,-192.8 61.0,-177.2 64.0,-162.0 67.0,-147.2 70.0,-132.8 73.0,-118.7 76.0,-105.0 79.0,-91.7 82.0,-78.8 85.0,-66.2 88.0,-54.0 91.0,-42.2 94.0,-30.8 97.0,-19.7 100.0,-9.0 103.0,1.3 106.0,11.2 109.0,20.8 112.0,30.0 115.0,38.8 118.0,47.2 121.0,55.3 124.0,63.0 127.0,70.3 130.0,77.2 133.0,83.8 136.0,90.0 139.0,95.8 142.0,101.2 145.0,106.3 148.0,111.0 151.0,115.3 154.0,119.2 157.0,122.8 160.0,126.0 163.0,128.8 166.0,131.2 169.0,133.3 172.0,135.0 175.0,136.3 178.0,137.2 181.0,137.8 184.0,138.0 187.0,137.8 190.0,137.2 193.0,136.3 196.0,135.0 199.0,133.3 202.0,131.2 205.0,128.8 208.0,126.0 211.0,122.8 214.0,119.2 217.0,115.3 220.0,111.0 223.0,106.3 226.0,101.2 229.0,95.8 232.0,90.0 235.0,83.8 238.0,77.2 241.0,70.3 244.0,63.0 247.0,55.3 250.0,47.2 253.0,38.8 256.0,30.0 259.0,20.8 262.0,11.2 265.0,1.3 268.0,-9.0 271.0,-19.7 274.0,-30.8 277.0,-42.2 280.0,-54.0\" fill=\"none\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"255.8\" y=\"54.5\" fill=\"#0d9488\" font-weight=\"bold\" font-size=\"14\">3</text><polyline clip-path=\"url(#w1c29)\" points=\"40.0,546.0 43.0,528.2 46.0,510.8 49.0,493.7 52.0,477.0 55.0,460.7 58.0,444.8 61.0,429.2 64.0,414.0 67.0,399.2 70.0,384.8 73.0,370.7 76.0,357.0 79.0,343.7 82.0,330.8 85.0,318.2 88.0,306.0 91.0,294.2 94.0,282.8 97.0,271.7 100.0,261.0 103.0,250.7 106.0,240.8 109.0,231.2 112.0,222.0 115.0,213.2 118.0,204.8 121.0,196.7 124.0,189.0 127.0,181.7 130.0,174.8 133.0,168.2 136.0,162.0 139.0,156.2 142.0,150.8 145.0,145.7 148.0,141.0 151.0,136.7 154.0,132.8 157.0,129.2 160.0,126.0 163.0,123.2 166.0,120.8 169.0,118.7 172.0,117.0 175.0,115.7 178.0,114.8 181.0,114.2 184.0,114.0 187.0,114.2 190.0,114.8 193.0,115.7 196.0,117.0 199.0,118.7 202.0,120.8 205.0,123.2 208.0,126.0 211.0,129.2 214.0,132.8 217.0,136.7 220.0,141.0 223.0,145.7 226.0,150.8 229.0,156.2 232.0,162.0 235.0,168.2 238.0,174.8 241.0,181.7 244.0,189.0 247.0,196.7 250.0,204.8 253.0,213.2 256.0,222.0 259.0,231.2 262.0,240.8 265.0,250.7 268.0,261.0 271.0,271.7 274.0,282.8 277.0,294.2 280.0,306.0\" fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.6\"/><text x=\"239.0\" y=\"166.0\" fill=\"#b45309\" font-weight=\"bold\" font-size=\"14\">4</text></svg>",
      "opties": [
        "parabool 4",
        "parabool 2",
        "parabool 1",
        "parabool 3"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −¼x² − 7x − 2, y = −¼x² + 2x − 6, y = −½x² − 8x − 6 en y = 4x² − 8. Bij welke formule ligt de top van de parabool op de y-as?",
      "uitleg": "Ligt de top op de y-as, dan is b = 0: de formule heeft de vorm y = ax² + c. Dat is y = 4x² − 8.",
      "opties": [
        "y = −¼x² − 7x − 2",
        "y = 4x² − 8",
        "y = −¼x² + 2x − 6",
        "y = −½x² − 8x − 6"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −½x² − 7x + 4, y = −¼x² + x + 7, y = −x² − 7x − 4 en y = 2x² − 5x + 7. Bij welke formule is de parabool het smalst?",
      "uitleg": "Vergelijk de getallen voor x²: −½, −¼, −1, 2. Het verst van 0 ligt 2, dus die parabool is het smalst.",
      "opties": [
        "y = −¼x² + x + 7",
        "y = −x² − 7x − 4",
        "y = 2x² − 5x + 7",
        "y = −½x² − 7x + 4"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 2(x + 4)(x + 8) zonder haakjes.",
      "uitleg": "Eerst (x + 4)(x + 8) = x² + 12x + 32. Dan elke term keer 2: y = 2x² + 24x + 64.",
      "opties": [
        "y = 2x² − 24x + 64",
        "y = 2x² + 12x + 32",
        "y = 2x² + 24x + 64",
        "y = 2x² + 24x − 64"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 4(x − 1)² + 2 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "6",
      "uitleg": "(x − 1)² = x² − 2x + 1; keer 4 → 4x² − 8x + 4; + 2 → y = 4x² − 8x + 6. Dus c = 6."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 4(x − 4)² + 11?",
      "uitleg": "Bij x = 4 is (x − 4)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = 11. Top (4, 11). Let op: bij (x − 4) hoort x = 4, bij (x + 4) hoort x = −4.",
      "opties": [
        "(4, −11)",
        "(−4, 11)",
        "(−4, −11)",
        "(4, 11)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Bij de waterstraal van een tuinsproeier hoort de formule h = −0,2a² + 0,4a + 0,2 (h en a in meters). Hoeveel meter hoog komt de waterstraal maximaal?",
      "antwoord": "0,4",
      "uitleg": "a = 0 geeft h = 0,2 m = 20 cm. Top: −0,2a² + 0,4a = 0 → a = 0 of a = 2, midden a = 1; h = 0,4 m."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 7,2a − 0,6a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "12",
      "uitleg": "7,2a − 0,6a² = 0 → a(7,2 − 0,6a) = 0 → a = 0 of a = 7,2 / 0,6 = 12. De tunnel is 12 m breed. Midden: a = 6, h = 7,2 · 6 − 0,6 · 6² = 21,6 m."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −x² − 6x, y = ½x² + 2x + 7, y = −4x² − x + 5 en y = 3x² + 2x − 6. Bij welke formule gaat de parabool door de oorsprong?",
      "uitleg": "Gaat de parabool door de oorsprong, dan is c = 0: bij x = 0 hoort y = 0. Dat is y = −x² − 6x.",
      "opties": [
        "y = −x² − 6x",
        "y = 3x² + 2x − 6",
        "y = ½x² + 2x + 7",
        "y = −4x² − x + 5"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 2. De x-coördinaat van de top van de parabool is −3. Bereken b.",
      "antwoord": "6",
      "uitleg": "De parabool snijdt de y-as in (0, 2). Het andere punt met y = 2 ligt even ver aan de andere kant van de top: x = 2 · (−3) = −6. Invullen: (−6)² + b · (−6) + 2 = 2 → 36 + −6b = 0 → b = 6."
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,2(a − 2,5)² + 0,6. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "60",
      "uitleg": "Het laagste punt is de top (a = 2,5): h = 0,6 m = 60 cm. Bij de boom (a = 0): h = 0,2 · 2,5² + 0,6 = 1,85 m. De andere boom staat even ver aan de andere kant: a = 5 m."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = x² + 10x + 20. Vul in: x = …",
      "antwoord": "-5",
      "uitleg": "1 Uit x = 0 volgt y = 20. 2 x² + 10x + 20 = 20 → x² + 10x = 0 → x(x + 10) = 0 → x = 0 of x = −10. 3 De x-coördinaat van de top ligt midden tussen 0 en −10: x = −5. 4 y = (−5)² + 10 · (−5) + 20 = −5. 5 De top is (−5, −5). De symmetrieas is de lijn x = −5."
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,4(q − 200)(q − 400). Bereken de maximale winst in euro.",
      "antwoord": "4000",
      "uitleg": "Snijpunten met de horizontale as: q = 200 en q = 400. Midden: q = 300. W = −0,4 · (300 − 200)(300 − 400) = 4000 euro."
    }
  ]
});
