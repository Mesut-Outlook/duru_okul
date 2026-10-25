/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 88 — Gemengd H1 — Lineaire en exponentiële formules (5/10)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-gemengd-5",
  "hoofdstuk": 1,
  "titel": "Proeftoets 88 — Gemengd H1 — Lineaire en exponentiële formules (5/10)",
  "vak": "Wiskunde · Hoofdstuk 1 · Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (4, 13) en (8, 25)?",
      "uitleg": "a = (25 − 13) / (8 − 4) = 3. Invullen van (4, 13) geeft 13 = 12 + b, dus b = 1. De formule is y = 3x + 1.",
      "opties": [
        "y = −3x + 1",
        "y = 3x − 1",
        "y = 3x + 13",
        "y = 3x + 1"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (3, −3) en loopt evenwijdig aan lijn l: y = −4x + 7. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = −4. Invullen van (3, −3): −3 = −4 · 3 + b = −12 + b, dus b = 9. Lijn m: y = −4x + 9.",
      "opties": [
        "y = −4x − 15",
        "y = −4x + 9",
        "y = 4x − 15",
        "y = −4x − 3"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(1, −16) en Q(10, −61). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-5",
      "uitleg": "rc = toename y / toename x = (−61 − (−16)) / (10 − 1) = −45 / 9 = −5."
    },
    {
      "type": "open",
      "vraag": "Stel een formule op bij de lijn door de punten A(3, 14) en B(11, 46). Schrijf je antwoord als y = ax + b.",
      "modelantwoord": "y = 4x + 2",
      "sleutelwoorden": [
        "4x/4x",
        "+ 2/+2"
      ],
      "minTreffers": 2,
      "uitleg": "rc = (46 − 14) / (11 − 3) = 4. Invullen van A: 14 = 12 + b, dus b = 2. Formule: y = 4x + 2."
    },
    {
      "type": "invul",
      "vraag": "De lijnen l: y = −x + 20 en m: y = 8x + 11 snijden elkaar in punt S. Bereken de x-coördinaat van S.",
      "antwoord": "1",
      "uitleg": "Stel gelijk: −x + 20 = 8x + 11 → −9x = −9 → x = 1."
    },
    {
      "type": "mc",
      "vraag": "Bereken de coördinaten van het snijpunt van de grafieken van y = −2x + 2 en y = 2x + 10.",
      "uitleg": "−2x + 2 = 2x + 10 → −4x = 8 → x = −2; y = 6. Snijpunt (−2, 6).",
      "opties": [
        "(−2, 2)",
        "(2, −2)",
        "(−2, 6)",
        "(6, −2)"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = 2x + 4 en y = 2x − 2 hebben geen snijpunt.",
      "antwoord": true,
      "uitleg": "Waar. Beide lijnen hebben rc 2 maar een ander startgetal: ze lopen evenwijdig en snijden elkaar nooit."
    },
    {
      "type": "invul",
      "vraag": "De lijn y = −4 snijdt lijn p uit de figuur. Bereken de x-coördinaat van het snijpunt.",
      "antwoord": "6",
      "uitleg": "Lijn p: y = −0,5x − 1. Gelijkstellen: −0,5x − 1 = −4 → −0,5x = −3 → x = 6.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c12\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c12)\" x1=\"2.0\" y1=\"198.0\" x2=\"282.0\" y2=\"338.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"187.2\" y=\"279.6\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">p</text><circle cx=\"58.0\" cy=\"226.0\" r=\"3.5\" fill=\"#222\"/><text x=\"64.0\" y=\"220.0\" fill=\"#222\" font-size=\"11\">(0, −1)</text><circle cx=\"226.0\" cy=\"310.0\" r=\"3.5\" fill=\"#222\"/><text x=\"232.0\" y=\"304.0\" fill=\"#222\" font-size=\"11\">(6, −4)</text></svg>"
    },
    {
      "type": "invul",
      "vraag": "Gegeven: A: N = 2a + 22 en B: a = −3q + 25. Substitueer B in A en vereenvoudig tot N = …q + …. Welk getal is het losse getal (de constante)?",
      "antwoord": "72",
      "uitleg": "N = 2(−3q + 25) + 22 = −6q + 50 + 22. Constante: 50 + 22 = 72."
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 8a + 2q = 12 in de formule N = 3q + 3 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "2q = 12 − 8a, dus q = −4a + 6. Invullen: N = 3(−4a + 6) + 3 = −12a + 21.",
      "opties": [
        "N = −12a + 21",
        "N = 12a + 21",
        "N = −12a + 9",
        "N = −4a + 21"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een fabrikant verkoopt a = 500t apparaten na t weken. De kosten in euro's zijn k = 12a + 1200. Bereken de kosten na 18 weken.",
      "antwoord": "109200",
      "uitleg": "Substitueer: k = 12 · 500t + 1200 = 6000t + 1200. Na 18 weken: k = 6000 · 18 + 1200 = 109200 euro."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 8 − 4p substitueert in h = 3t + 12, krijg je h = −4p + 36.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 3(8 − 4p) + 12 = 24 − 12p + 12, dus h = −12p + 36. Zonder haakjes vergeet je 4p met 3 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "De tabel (de hoeveelheid medicijn in het bloed) hoort bij een exponentieel verband met waarden 64 op t = 1 en 128 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "32",
      "uitleg": "Groeifactor: 128 : 64 = 2. Terug naar t = 0: 64 : 2 = 32.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">512</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft het aantal downloads van een spel (N), met 225 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 100. Van t = 0 naar t = 1: 150 : 100 = 1,5. Dus N = 100 · 1,5ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 312\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"312\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c13\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"238.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"268.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"268.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"268.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"268.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">50</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">150</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">250</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">350</text><text x=\"35.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"272.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"304.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c13)\" points=\"40.0,200.0 41.7,198.6 43.4,197.2 45.1,195.7 46.8,194.3 48.5,192.7 50.2,191.2 51.9,189.6 53.6,188.0 55.3,186.4 57.0,184.7 58.7,183.0 60.4,181.3 62.1,179.5 63.8,177.7 65.5,175.8 67.2,173.9 68.9,172.0 70.6,170.1 72.3,168.0 74.0,166.0 75.7,163.9 77.4,161.8 79.1,159.6 80.8,157.4 82.5,155.1 84.2,152.8 85.9,150.4 87.6,148.0 89.3,145.6 91.0,143.1 92.7,140.5 94.4,137.9 96.1,135.2 97.8,132.5 99.5,129.7 101.2,126.9 102.9,124.0 104.6,121.1 106.3,118.1 108.0,115.0 109.7,111.9 111.4,108.7 113.1,105.4 114.8,102.1 116.5,98.7 118.2,95.2 119.9,91.7 121.6,88.1 123.3,84.4 125.0,80.6 126.7,76.8 128.4,72.9 130.1,68.9 131.8,64.8 133.5,60.6 135.2,56.4 136.9,52.0 138.6,47.6 140.3,43.1 142.0,38.5 143.7,33.8 145.4,29.0 147.1,24.1 148.8,19.1 150.5,14.0 152.2,8.8 153.9,3.5 155.6,-1.9 157.3,-7.4 159.0,-13.1 160.7,-18.8 162.4,-24.7 164.1,-30.7 165.8,-36.8 167.5,-43.1 169.2,-49.4 170.9,-55.9 172.6,-62.6 174.3,-69.3 176.0,-76.2\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"200.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"194.0\" fill=\"#222\" font-size=\"11\">(0, 100)</text><circle cx=\"74.0\" cy=\"166.0\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"160.0\" fill=\"#222\" font-size=\"11\">(1, 150)</text><circle cx=\"108.0\" cy=\"115.0\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"109.0\" fill=\"#222\" font-size=\"11\">(2, 225)</text><circle cx=\"142.0\" cy=\"38.5\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"32.5\" fill=\"#222\" font-size=\"11\">(3, 337,5)</text></svg>",
      "opties": [
        "N = 150 · 1,5ᵗ",
        "N = 100 + 50t",
        "N = 100 · 2/3ᵗ",
        "N = 100 · 1,5ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De bevolking van een land groeit exponentieel: in 2000 waren er 6,20 miljoen en in 2005 6,57 miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
      "antwoord": "1,059",
      "uitleg": "7,38 : 6,97 ≈ 1,059. (De andere stappen geven ongeveer hetzelfde: 1,060, 1,061.)",
      "tolerantie": 0.002,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 340 62\" width=\"340\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"338\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2000</text><line x1=\"189\" y1=\"1\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2005</text><line x1=\"239\" y1=\"1\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2010</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2015</text><rect x=\"1\" y=\"31\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">bevolking (mln)</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,20</text><line x1=\"189\" y1=\"31\" x2=\"189\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,57</text><line x1=\"239\" y1=\"31\" x2=\"239\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,97</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">7,38</text><line x1=\"1\" y1=\"31\" x2=\"339\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 128, 160, 192, 224 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 32 bij: dat is lineair; de factoren (1,25, 1,20) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,7 per 15 minuten, soort B met groeifactor 18 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (4 × 15 minuten): 1,7⁴ ≈ 8,4. Vergelijk met 18: soort B groeit het snelst.",
      "opties": [
        "soort B",
        "dat kun je niet vergelijken",
        "soort A",
        "ze groeien even snel"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,3 per half uur. Bereken de groeifactor per uur.",
      "antwoord": "1,69",
      "uitleg": "Per uur zijn er twee stappen: 1,3 · 1,3 = 1,3² = 1,69.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,1ᵗ is t de tijd in eenheden van half uur. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,21",
      "uitleg": "In een uur passen 2 keer half uur. Groeifactor per uur: 1,1² ≈ 1,2100 ≈ 1,21.",
      "tolerantie": 0.006
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per jaar. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 5 jaar eerder? Rond af op een geheel getal.",
      "antwoord": "181577",
      "uitleg": "Groeifactor per 5 jaar: 1,12⁵. Terugrekenen = delen: 320.000 : 1,12⁵ ≈ 181577.",
      "tolerantie": 90
    }
  ]
});
