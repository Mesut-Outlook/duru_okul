/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 129 — Gemengd H2 + H1 + herhaling (1/3)
   Bron: Noordhoff H2 (11 vragen), H1 §1.1–§1.5 (7), Statistiek-herhaling MAVO 2 (2); andere getallen
   Gegenereerd met tools/gen_wiskunde_gemengd_20261120.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-gemengd-20261120-1",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 129 — Gemengd H2 + H1 + herhaling (1/3)",
  "vak": "Wiskunde · H2 Parabolen + H1 Lineair & exponentieel + Herhaling",
  "icoon": "🔀",
  "duurMin": 40,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een bal wordt weggeschoten volgens h = −½a² + a + 0,3. Hierin is h de hoogte in meters en a de horizontale afstand in meters. Stap 1: vul a = 0 in. Op welke hoogte in meters begint de bal?",
      "antwoord": "0,3",
      "uitleg": "a = 0 invullen: h = −0,5 · 0² + 1 · 0 + 0,3 = 0,3. Het getal c is dus de beginhoogte: 0,3 m."
    },
    {
      "type": "invul",
      "vraag": "Bij de waterstraal van een tuinsproeier hoort de formule h = −0,2a² + 1,2a + ½. Hierin is h de hoogte in meters en a de horizontale afstand tot de sproeier in meters. Hoeveel cm hoog is de sproeier zelf (a = 0)?",
      "antwoord": "50",
      "uitleg": "a = 0 geeft h = 0,5 m = 50 cm. Top: −0,2a² + 1,2a = 0 → a = 0 of a = 6, midden a = 3; h = 2,3 m."
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,5(a − 2)² + 0,6. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "60",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,6 m = 60 cm. Bij de boom (a = 0): h = 0,5 · 2² + 0,6 = 2,6 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = −2(x − 3)² + 9 zonder haakjes.",
      "uitleg": "(x − 3)² = (x − 3)(x − 3) = x² − 6x + 9 (niet x² + 9!). Keer −2: −2x² + 12x − 18. Daarna + 9: y = −2x² + 12x − 9.",
      "opties": [
        "y = −2x² + 12x − 9",
        "y = −2x² + 12x − 18",
        "y = −2x² − 9",
        "y = −2x² + 12x − 36"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een bibliotheek vanaf 2018. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,96",
      "uitleg": "288.000 : 300.000 ≈ 0,96; ook 276.480 : 288.000 ≈ 0,96. De groeifactor is 0,96.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 364 62\" width=\"364\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"362\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2018</text><line x1=\"141\" y1=\"1\" x2=\"141\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">300.000</text><line x1=\"141\" y1=\"31\" x2=\"141\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">288.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">276.480</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">265.421</text><line x1=\"1\" y1=\"31\" x2=\"363\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Wat is de mediaan van de getallen: 13, 15, 3, 13, 12, 11, 10?",
      "uitleg": "Eerst sorteren: 3, 10, 11, 12, 13, 13, 15. Het middelste (4e) getal is 12. Het middelste getal van de ongesorteerde rij (13) telt niet.",
      "opties": [
        "11",
        "12",
        "10",
        "13"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken het gemiddelde van de getallen: 6, 11, 4, 5, 14.",
      "antwoord": "8",
      "uitleg": "Som = 6 + 11 + 4 + 5 + 14 = 40; delen door 5 geeft 8."
    },
    {
      "type": "invul",
      "vraag": "Substitueer t = 3p + 10 in h = 6t + 40. Je krijgt h = …p + 100. Welk getal staat er vóór p?",
      "antwoord": "18",
      "uitleg": "h = 6(3p + 10) + 40. Vóór p: 6 · 3 = 18."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −3(x − 2)² + 17 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "12",
      "uitleg": "(x − 2)² = x² − 4x + 4; keer −3 → −3x² + 12x − 12; + 17 → y = −3x² + 12x + 5. Dus b = 12."
    },
    {
      "type": "invul",
      "vraag": "In een spel spaar je credits. Noah heeft op dag 0 2 miljoen credits en krijgt er elke dag 2 miljoen bij. Fenna begint op hetzelfde moment en spaart ook elke dag hetzelfde aantal: na 2 dagen heeft Fenna 6 miljoen credits en na 6 dagen 18 miljoen. Na hoeveel dagen hebben ze evenveel credits?",
      "antwoord": "2",
      "uitleg": "Noah: c = 2t + 2. Fenna: rc = (18 − 6) / (6 − 2) = 3, b = 6 − 6 = 0. Gelijkstellen geeft t = 2 dagen."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is P = 100 · 1,07ᵗ met t in weken. Bereken de groeifactor per 2 weken. Rond af op drie decimalen.",
      "antwoord": "1,145",
      "uitleg": "2 weken = 2 stappen: 1,07² ≈ 1,145.",
      "tolerantie": 0.0015
    },
    {
      "type": "mc",
      "vraag": "Bereken de coördinaten van het snijpunt van de grafieken van y = −x − 8 en y = 5x + 4.",
      "uitleg": "−x − 8 = 5x + 4 → −6x = 12 → x = −2; y = −6. Snijpunt (−2, −6).",
      "opties": [
        "(−2, 10)",
        "(−2, −6)",
        "(−6, −2)",
        "(2, −10)"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Noah spaart voor een scooter. Met de formule s = 250 + 10w berekent Noah het bedrag s in euro's na w weken. Fenna begint op hetzelfde moment, heeft nog niets gespaard en spaart per week drie keer zoveel als Noah. Welke formule hoort bij Fenna?",
      "uitleg": "Fenna begint bij 0 euro (startgetal 0) en spaart drie keer 10 = 30 euro per week (rc 30). Dus s = 30w.",
      "opties": [
        "s = 750 + 30w",
        "s = 250 + 30w",
        "s = 30w",
        "s = 750 + 10w"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (1, 3). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = 4. 2 x² − 2x + 4 = 4 → x² − 2x = 0 → x(x − 2) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = 1² − 2 · 1 + 4 = 3. 5 De top is (1, 3). Bij de andere formules ligt de top ergens anders of is het een bergparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c1\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c1)\" points=\"40.0,-498.0 43.6,-473.1 47.2,-448.7 50.8,-424.8 54.4,-401.5 58.0,-378.8 61.6,-356.5 65.2,-334.8 68.8,-313.7 72.4,-293.1 76.0,-273.0 79.6,-253.5 83.2,-234.5 86.8,-216.0 90.4,-198.1 94.0,-180.8 97.6,-163.9 101.2,-147.6 104.8,-131.9 108.4,-116.7 112.0,-102.0 115.6,-87.9 119.2,-74.3 122.8,-61.2 126.4,-48.7 130.0,-36.8 133.6,-25.3 137.2,-14.4 140.8,-4.1 144.4,5.7 148.0,15.0 151.6,23.7 155.2,31.9 158.8,39.6 162.4,46.7 166.0,53.2 169.6,59.3 173.2,64.8 176.8,69.7 180.4,74.1 184.0,78.0 187.6,81.3 191.2,84.1 194.8,86.4 198.4,88.1 202.0,89.2 205.6,89.9 209.2,90.0 212.8,89.5 216.4,88.5 220.0,87.0 223.6,84.9 227.2,82.3 230.8,79.2 234.4,75.5 238.0,71.2 241.6,66.5 245.2,61.2 248.8,55.3 252.4,48.9 256.0,42.0 259.6,34.5 263.2,26.5 266.8,18.0 270.4,8.9 274.0,-0.8 277.6,-10.9 281.2,-21.6 284.8,-32.9 288.4,-44.7 292.0,-57.0 295.6,-69.9 299.2,-83.3 302.8,-97.2 306.4,-111.7 310.0,-126.8 313.6,-142.3 317.2,-158.4 320.8,-175.1 324.4,-192.3 328.0,-210.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"208.0\" cy=\"90.0\" r=\"3.5\" fill=\"#222\"/><text x=\"214.0\" y=\"84.0\" fill=\"#222\" font-size=\"11\">(1, 3)</text></svg>",
      "opties": [
        "y = x² − 2x + 4",
        "y = −x² + 2x − 4",
        "y = x² − 2x + 6",
        "y = x² + 2x + 4"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de x-coördinaat van de top van de parabool bij de formule y = −2x² + 16x − 32.",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = −32. 2 −2x² + 16x − 32 = −32 → −2x² + 16x = 0 → x(−2x + 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −2·4² + 16 · 4 − 32 = 0. 5 De top is (4, 0)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 2x² + 16x + 37 snijdt de y-as in (0, 37). Er is nog een punt op de parabool met y = 37. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-8",
      "uitleg": "2x² + 16x + 37 = 37 → 2x² + 16x = 0 → x(2x + 16) = 0 → x = 0 of x = −8. Het andere punt is (−8, 37)."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = x² + 8x + 14 heeft symmetrieas x = −4. Het punt (1, 23) ligt op de parabool. Er is nog een punt met y = 23. Bereken de x-coördinaat van dat punt.",
      "antwoord": "-9",
      "uitleg": "1 ligt 5 van de as x = −4. Het gespiegelde punt ligt even ver aan de andere kant: x = −4 − 5 = −9."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (−3, 5). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = −4. 2 −x² − 6x − 4 = −4 → −x² − 6x = 0 → x(−x − 6) = 0 → x = 0 of x = −6. 3 De x-coördinaat van de top ligt midden tussen 0 en −6: x = −3. 4 y = −(−3)² − 6 · (−3) − 4 = 5. 5 De top is (−3, 5). Bij de andere formules ligt de top ergens anders of is het een dalparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c2)\" points=\"40.0,174.0 43.6,163.5 47.2,153.5 50.8,144.0 54.4,135.1 58.0,126.8 61.6,118.9 65.2,111.6 68.8,104.9 72.4,98.7 76.0,93.0 79.6,87.9 83.2,83.3 86.8,79.2 90.4,75.7 94.0,72.8 97.6,70.3 101.2,68.4 104.8,67.1 108.4,66.3 112.0,66.0 115.6,66.3 119.2,67.1 122.8,68.4 126.4,70.3 130.0,72.8 133.6,75.7 137.2,79.2 140.8,83.3 144.4,87.9 148.0,93.0 151.6,98.7 155.2,104.9 158.8,111.6 162.4,118.9 166.0,126.8 169.6,135.1 173.2,144.0 176.8,153.5 180.4,163.5 184.0,174.0 187.6,185.1 191.2,196.7 194.8,208.8 198.4,221.5 202.0,234.8 205.6,248.5 209.2,262.8 212.8,277.7 216.4,293.1 220.0,309.0 223.6,325.5 227.2,342.5 230.8,360.0 234.4,378.1 238.0,396.8 241.6,415.9 245.2,435.6 248.8,455.9 252.4,476.7 256.0,498.0 259.6,519.9 263.2,542.3 266.8,565.2 270.4,588.7 274.0,612.8 277.6,637.3 281.2,662.4 284.8,688.1 288.4,714.3 292.0,741.0 295.6,768.3 299.2,796.1 302.8,824.4 306.4,853.3 310.0,882.8 313.6,912.7 317.2,943.2 320.8,974.3 324.4,1005.9 328.0,1038.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"112.0\" cy=\"66.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"60.0\" fill=\"#222\" font-size=\"11\">(−3, 5)</text></svg>",
      "opties": [
        "y = −x² + 6x − 4",
        "y = −x² − 6x − 2",
        "y = x² + 6x + 4",
        "y = −x² − 6x − 4"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Schrijf de formule y = 2(x + 1)(x − 3) zonder haakjes.",
      "uitleg": "Eerst (x + 1)(x − 3) = x² − 2x − 3. Dan elke term keer 2: y = 2x² − 4x − 6.",
      "opties": [
        "y = 2x² − 4x + 6",
        "y = 2x² − 2x − 3",
        "y = 2x² + 4x − 6",
        "y = 2x² − 4x − 6"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers is N = 25.000 · 0,95ᵗ met t in jaren. Welke formule hoort bij t in perioden van 5 jaar? (groeifactor in drie decimalen)",
      "uitleg": "Per 5 jaar: 0,95⁵ ≈ 0,774. De beginwaarde 25.000 blijft hetzelfde.",
      "opties": [
        "N = 25.000 · 0,774ᵗ",
        "N = 25.000 · 0,750ᵗ",
        "N = 125.000 · 0,95ᵗ",
        "N = 25.000 · 0,990ᵗ"
      ],
      "antwoord": 0
    }
  ]
});
