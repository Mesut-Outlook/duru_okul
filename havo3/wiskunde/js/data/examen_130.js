/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 130 — Gemengd H2 + H1 + herhaling (2/3)
   Bron: Noordhoff H2 (11 vragen), H1 §1.1–§1.5 (7), Statistiek-herhaling MAVO 2 (2); andere getallen
   Gegenereerd met tools/gen_wiskunde_gemengd_20261120.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-gemengd-20261120-2",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 130 — Gemengd H2 + H1 + herhaling (2/3)",
  "vak": "Wiskunde · H2 Parabolen + H1 Lineair & exponentieel + Herhaling",
  "icoon": "🔀",
  "duurMin": 40,
  "vragen": [
    {
      "type": "invul",
      "vraag": "De baan van een bal is h = −0,2(a − 3)² + 1,8 (h en a in meters). Het hoogste punt is de top. Hoeveel cm hoog komt de bal maximaal?",
      "antwoord": "180",
      "uitleg": "In y = a(x − p)² + q is q de y-coördinaat van de top. Hier: top (3, 1,8), dus 1,8 m = 180 cm (meter × 100). Het getal bij a is geen hoogte."
    },
    {
      "type": "invul",
      "vraag": "De hoogte h in cm van een speer is h = -6t² + 36t + 150, met t de tijd in seconden. Hoe hoog komt de speer maximaal (in cm)?",
      "antwoord": "204",
      "uitleg": "t = 0 geeft h = 150. -6t² + 36t = 0 → t = 0 of t = 6; midden t = 3. h = -6 · 3² + 36 · 3 + 150 = 204 cm."
    },
    {
      "type": "invul",
      "vraag": "De formule h = 2,4a − 0,6a² hoort bij de hoogte van een tunnelboog. Hierin is h de hoogte in meters en a de horizontale afstand in meters vanaf de linkermuur. Hoeveel meter is de tunnel breed op de grond?",
      "antwoord": "4",
      "uitleg": "2,4a − 0,6a² = 0 → a(2,4 − 0,6a) = 0 → a = 0 of a = 2,4 / 0,6 = 4. De tunnel is 4 m breed. Midden: a = 2, h = 2,4 · 2 − 0,6 · 2² = 2,4 m."
    },
    {
      "type": "invul",
      "vraag": "Het totaal aantal gespeelde partijen op een schaakwebsite nam exponentieel toe met groeifactor 1,04 per maand. Op 1 december waren er in totaal 75.800 partijen gespeeld. Hoeveel waren dat er op 1 juli? Rond af op een geheel getal.",
      "antwoord": "62302",
      "uitleg": "1 juli is 5 maanden eerder. Delen door de groeifactor per 5 maanden: 75.800 : 1,04⁵ ≈ 62.302.",
      "tolerantie": 31
    },
    {
      "type": "invul",
      "vraag": "Bereken de mediaan van de getallen: 3, 10, 6, 13, 9, 13. Een decimaal getal mag.",
      "antwoord": "9,5",
      "uitleg": "Gesorteerd: 3, 6, 9, 10, 13, 13. Even aantal: het gemiddelde van de twee middelste getallen (9 en 10) = 9,5."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (3, 14) en (9, 32)?",
      "uitleg": "a = (32 − 14) / (9 − 3) = 3. Invullen van (3, 14) geeft 14 = 9 + b, dus b = 5. De formule is y = 3x + 5.",
      "opties": [
        "y = −3x + 5",
        "y = 3x + 14",
        "y = 3x + 5",
        "y = 3x − 5"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Een bevolking groeit met 1,5% per jaar. Met hoeveel procent groeit de bevolking in 10 jaar? Rond af op één decimaal.",
      "antwoord": "16,1",
      "uitleg": "Groeifactor per jaar 1,015. Per 10 jaar: 1,015¹⁰ ≈ 1,161, dus ongeveer 16,1% groei (niet 15%).",
      "tolerantie": 0.15
    },
    {
      "type": "mc",
      "vraag": "Wat is de modus van de getallen: 6, 7, 10, 6, 8, 6, 11, 5, 11?",
      "uitleg": "De modus is het getal dat het vaakst voorkomt: 6 komt 3 keer voor.",
      "opties": [
        "7",
        "6",
        "11",
        "5"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x + 3)(x + 9) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-36",
      "uitleg": "(x + 3)(x + 9) = x² + 12x + 27; keer −3 geeft y = −3x² − 36x − 81, dus b = −36."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van de top van de parabool bij de formule y = −x² + 2x − 7.",
      "antwoord": "-6",
      "uitleg": "1 Uit x = 0 volgt y = −7. 2 −x² + 2x − 7 = −7 → −x² + 2x = 0 → x(−x + 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = −1² + 2 · 1 − 7 = −6. 5 De top is (1, −6)."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (x + 6)(5 − 2x) − 4x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-6",
      "uitleg": "(x + 6)(5 − 2x) = −2x² − 7x + 30. Samen met −4x²: y = −6x² − 7x + 30. Het getal voor x² is −6, dus de grafiek is een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −3x² + 30x − 74 snijdt de y-as in (0, −74). Er is nog een punt op de parabool met y = −74. Bereken de x-coördinaat van dat punt.",
      "antwoord": "10",
      "uitleg": "−3x² + 30x − 74 = −74 → −3x² + 30x = 0 → x(−3x + 30) = 0 → x = 0 of x = 10. Het andere punt is (10, −74)."
    },
    {
      "type": "invul",
      "vraag": "De lijnen l: y = 2x + 28 en m: y = −5x − 14 snijden elkaar in punt S. Bereken de x-coördinaat van S.",
      "antwoord": "-6",
      "uitleg": "Stel gelijk: 2x + 28 = −5x − 14 → 7x = −42 → x = −6."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −(x − 2)² − 1 in de vorm y = ax² + bx + c. Hoe groot is c?",
      "antwoord": "-5",
      "uitleg": "(x − 2)² = x² − 4x + 4; keer −1 → −x² + 4x − 4; − 1 → y = −x² + 4x − 5. Dus c = −5."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule -5a + 5q = 30 in de formule p = 2q + 5 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "5q = 30 − -5a, dus q = a + 6. Invullen: p = 2(a + 6) + 5 = 2a + 17.",
      "opties": [
        "p = 2a + 11",
        "p = 2a + 17",
        "p = −2a + 17",
        "p = a + 17"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (1, −1). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = −3. 2 −2x² + 4x − 3 = −3 → −2x² + 4x = 0 → x(−2x + 4) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = −2·1² + 4 · 1 − 3 = −1. 5 De top is (1, −1). Bij de andere formules ligt de top ergens anders of is het een dalparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c3\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c3)\" points=\"40.0,1314.0 43.6,1264.1 47.2,1215.4 50.8,1167.7 54.4,1121.0 58.0,1075.5 61.6,1031.0 65.2,987.7 68.8,945.4 72.4,904.1 76.0,864.0 79.6,824.9 83.2,787.0 86.8,750.1 90.4,714.2 94.0,679.5 97.6,645.8 101.2,613.3 104.8,581.8 108.4,551.3 112.0,522.0 115.6,493.7 119.2,466.6 122.8,440.5 126.4,415.4 130.0,391.5 133.6,368.6 137.2,346.9 140.8,326.2 144.4,306.5 148.0,288.0 151.6,270.5 155.2,254.2 158.8,238.9 162.4,224.6 166.0,211.5 169.6,199.4 173.2,188.5 176.8,178.6 180.4,169.7 184.0,162.0 187.6,155.3 191.2,149.8 194.8,145.3 198.4,141.8 202.0,139.5 205.6,138.2 209.2,138.1 212.8,139.0 216.4,140.9 220.0,144.0 223.6,148.1 227.2,153.4 230.8,159.7 234.4,167.0 238.0,175.5 241.6,185.0 245.2,195.7 248.8,207.4 252.4,220.1 256.0,234.0 259.6,248.9 263.2,265.0 266.8,282.1 270.4,300.2 274.0,319.5 277.6,339.8 281.2,361.3 284.8,383.8 288.4,407.3 292.0,432.0 295.6,457.7 299.2,484.6 302.8,512.5 306.4,541.4 310.0,571.5 313.6,602.6 317.2,634.9 320.8,668.2 324.4,702.5 328.0,738.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"208.0\" cy=\"138.0\" r=\"3.5\" fill=\"#222\"/><text x=\"214.0\" y=\"132.0\" fill=\"#222\" font-size=\"11\">(1, −1)</text></svg>",
      "opties": [
        "y = −2x² + 4x − 1",
        "y = −2x² − 4x − 3",
        "y = 2x² − 4x + 3",
        "y = −2x² + 4x − 3"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Het snijpunt van de lijnen y = 3x + 59 en y = 9x − 12 valt buiten een schets. Ligt het snijpunt links of rechts van de lijn x = 29?",
      "uitleg": "Gelijkstellen: 3x + 59 = 9x − 12 → x ≈ 11,8. Dat is minder dan 29, dus links.",
      "opties": [
        "links van de lijn x = 29",
        "precies op de lijn x = 29",
        "rechts van de lijn x = 29",
        "de lijnen snijden elkaar niet"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (−1, −1). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = −3. 2 −2x² − 4x − 3 = −3 → −2x² − 4x = 0 → x(−2x − 4) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = −2·(−1)² − 4 · (−1) − 3 = −1. 5 De top is (−1, −1). Bij de andere formules ligt de top ergens anders of is het een dalparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c4\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c4)\" points=\"40.0,738.0 43.6,702.5 47.2,668.2 50.8,634.9 54.4,602.6 58.0,571.5 61.6,541.4 65.2,512.5 68.8,484.6 72.4,457.7 76.0,432.0 79.6,407.3 83.2,383.8 86.8,361.3 90.4,339.8 94.0,319.5 97.6,300.2 101.2,282.1 104.8,265.0 108.4,248.9 112.0,234.0 115.6,220.1 119.2,207.4 122.8,195.7 126.4,185.0 130.0,175.5 133.6,167.0 137.2,159.7 140.8,153.4 144.4,148.1 148.0,144.0 151.6,140.9 155.2,139.0 158.8,138.1 162.4,138.2 166.0,139.5 169.6,141.8 173.2,145.3 176.8,149.8 180.4,155.3 184.0,162.0 187.6,169.7 191.2,178.6 194.8,188.5 198.4,199.4 202.0,211.5 205.6,224.6 209.2,238.9 212.8,254.2 216.4,270.5 220.0,288.0 223.6,306.5 227.2,326.2 230.8,346.9 234.4,368.6 238.0,391.5 241.6,415.4 245.2,440.5 248.8,466.6 252.4,493.7 256.0,522.0 259.6,551.3 263.2,581.8 266.8,613.3 270.4,645.8 274.0,679.5 277.6,714.2 281.2,750.1 284.8,787.0 288.4,824.9 292.0,864.0 295.6,904.1 299.2,945.4 302.8,987.7 306.4,1031.0 310.0,1075.5 313.6,1121.0 317.2,1167.7 320.8,1215.4 324.4,1264.1 328.0,1314.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"160.0\" cy=\"138.0\" r=\"3.5\" fill=\"#222\"/><text x=\"166.0\" y=\"132.0\" fill=\"#222\" font-size=\"11\">(−1, −1)</text></svg>",
      "opties": [
        "y = −2x² − 4x − 3",
        "y = −2x² + 4x − 3",
        "y = 2x² + 4x + 3",
        "y = −2x² − 4x − 1"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De punten (−11, −10) en (5, −10) liggen op dezelfde parabool. Bereken de x-coördinaat van de top.",
      "antwoord": "-3",
      "uitleg": "Beide punten hebben y = −10, dus ze liggen symmetrisch t.o.v. de symmetrieas. De top ligt midden tussen: x = (−11 + 5) / 2 = −3."
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 64, 80, 100, 125 hoort bij een exponentieel verband.",
      "antwoord": true,
      "uitleg": "Waar. De factor is steeds 1,25."
    }
  ]
});
