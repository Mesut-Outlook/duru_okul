/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 39 — §1.4 Exponentiële groei (5/5, eindniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-29",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 39 — §1.4 Exponentiële groei (5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven de hoeveelheid medicijn in het bloed op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×2). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 294 152\" width=\"294\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"292\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"177\" y1=\"1\" x2=\"177\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"206.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"235\" y1=\"1\" x2=\"235\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">85</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">43</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">73</text><line x1=\"177\" y1=\"31\" x2=\"177\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"206.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">35</text><line x1=\"235\" y1=\"31\" x2=\"235\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"1\" y1=\"31\" x2=\"293\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">2048</text><line x1=\"77\" y1=\"61\" x2=\"77\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">4096</text><line x1=\"127\" y1=\"61\" x2=\"127\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">8192</text><line x1=\"177\" y1=\"61\" x2=\"177\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"206.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">16384</text><line x1=\"235\" y1=\"61\" x2=\"235\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">32768</text><line x1=\"1\" y1=\"61\" x2=\"293\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">46</text><line x1=\"77\" y1=\"91\" x2=\"77\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">50</text><line x1=\"127\" y1=\"91\" x2=\"127\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">54</text><line x1=\"177\" y1=\"91\" x2=\"177\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"206.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">58</text><line x1=\"235\" y1=\"91\" x2=\"235\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">62</text><line x1=\"1\" y1=\"91\" x2=\"293\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"77\" y1=\"121\" x2=\"77\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"127\" y1=\"121\" x2=\"127\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"177\" y1=\"121\" x2=\"177\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"206.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"235\" y1=\"121\" x2=\"235\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"121\" x2=\"293\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel D",
        "tabel C",
        "tabel B"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een museum vanaf 2020. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,92",
      "uitleg": "7360 : 8000 ≈ 0,92; ook 6771 : 7360 ≈ 0,92. De groeifactor is 0,92.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8000</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">7360</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6771</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6230</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bezoekers van een website (A) op tijdstip t, te beginnen met 128. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 128 (beginwaarde). Elke stap ×3 (384 : 128 = 3). Dus A = 128 · 3ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 270 62\" width=\"270\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"268\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"211\" y1=\"1\" x2=\"211\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">384</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1152</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3456</text><line x1=\"211\" y1=\"31\" x2=\"211\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">10368</text><line x1=\"1\" y1=\"31\" x2=\"269\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 384 · 3ᵗ",
        "A = 128 · 1/3ᵗ",
        "A = 128 · 3ᵗ",
        "A = 128 + 256t"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,85 per uur. Om 04.00 uur zijn er 1500 muggen. Hoeveel muggen waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "1765",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1500 : 0,85 ≈ 1764,7 → 1765 muggen.",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 32, 16, 8, 4 hoort bij een exponentieel verband.",
      "antwoord": true,
      "uitleg": "Waar. De factor is steeds 0,5."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 15% af. Om 10.00 uur zijn er 4500 downloads. Bereken het aantal downloads om 12.00 uur. Rond af op een geheel getal.",
      "antwoord": "3251",
      "uitleg": "Groeifactor 0,85. Na 2 uur: 4500 · 0,85² ≈ 3251,2 → 3251.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 4% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 4%: je houdt 104% over, dus groeifactor 1,04.",
      "opties": [
        "0,4",
        "1,04",
        "0,04",
        "0,96"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 10% af. Om het aantal één uur eerder te berekenen, vermenigvuldig je het huidige aantal met 1,1.",
      "antwoord": false,
      "uitleg": "Onwaar. Je moet delen door de groeifactor 0,9. Vermenigvuldigen met 1,1 geeft een ander (te klein) antwoord, want 10% van een kleiner getal is minder."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal bezoekers van een website) hoort bij een exponentieel verband met waarden 64 op t = 1 en 256 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "16",
      "uitleg": "Groeifactor: 256 : 64 = 4. Terug naar t = 0: 64 : 4 = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 230 62\" width=\"230\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"228\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4096</text><line x1=\"1\" y1=\"31\" x2=\"229\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft het aantal bacteriën in een bakje (N), met 1600 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 400. Van t = 0 naar t = 1: 800 : 400 = 2. Dus N = 400 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 312\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"312\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c42\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"238.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"268.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"268.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"268.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"268.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">1000</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">1500</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">2000</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">2500</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">3000</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">3500</text><text x=\"35.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"272.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"304.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c42)\" points=\"40.0,240.8 41.7,239.8 43.4,238.8 45.1,237.8 46.8,236.8 48.5,235.7 50.2,234.5 51.9,233.3 53.6,232.1 55.3,230.8 57.0,229.5 58.7,228.2 60.4,226.8 62.1,225.3 63.8,223.8 65.5,222.3 67.2,220.6 68.9,219.0 70.6,217.2 72.3,215.5 74.0,213.6 75.7,211.7 77.4,209.7 79.1,207.6 80.8,205.5 82.5,203.3 84.2,201.0 85.9,198.7 87.6,196.2 89.3,193.7 91.0,191.1 92.7,188.4 94.4,185.5 96.1,182.6 97.8,179.6 99.5,176.5 101.2,173.3 102.9,169.9 104.6,166.5 106.3,162.9 108.0,159.2 109.7,155.4 111.4,151.4 113.1,147.3 114.8,143.0 116.5,138.6 118.2,134.1 119.9,129.3 121.6,124.4 123.3,119.4 125.0,114.1 126.7,108.7 128.4,103.1 130.1,97.3 131.8,91.3 133.5,85.0 135.2,78.6 136.9,71.9 138.6,65.0 140.3,57.8 142.0,50.4 143.7,42.7 145.4,34.8 147.1,26.6 148.8,18.0 150.5,9.2 152.2,0.1 153.9,-9.3 155.6,-19.1 157.3,-29.3 159.0,-39.7 160.7,-50.6 162.4,-61.8 164.1,-73.5 165.8,-85.5 167.5,-98.0 169.2,-110.9 170.9,-124.2 172.6,-138.1 174.3,-152.4 176.0,-167.2\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"240.8\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"234.8\" fill=\"#222\" font-size=\"11\">(0, 400)</text><circle cx=\"74.0\" cy=\"213.6\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"207.6\" fill=\"#222\" font-size=\"11\">(1, 800)</text><circle cx=\"108.0\" cy=\"159.2\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"153.2\" fill=\"#222\" font-size=\"11\">(2, 1600)</text><circle cx=\"142.0\" cy=\"50.4\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"44.4\" fill=\"#222\" font-size=\"11\">(3, 3200)</text></svg>",
      "opties": [
        "N = 400 · 2ᵗ",
        "N = 400 · 0,5ᵗ",
        "N = 800 · 2ᵗ",
        "N = 400 + 400t"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De bevolking van een land groeit exponentieel: in 2000 waren er 6,20 miljoen en in 2005 6,33 miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
      "antwoord": "1,022",
      "uitleg": "6,60 : 6,46 ≈ 1,022. (De andere stappen geven ongeveer hetzelfde: 1,021, 1,021.)",
      "tolerantie": 0.002,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 340 62\" width=\"340\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"338\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2000</text><line x1=\"189\" y1=\"1\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2005</text><line x1=\"239\" y1=\"1\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2010</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2015</text><rect x=\"1\" y=\"31\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">bevolking (mln)</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,20</text><line x1=\"189\" y1=\"31\" x2=\"189\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,33</text><line x1=\"239\" y1=\"31\" x2=\"239\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,46</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6,60</text><line x1=\"1\" y1=\"31\" x2=\"339\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 1024, 1280, 1536, 1792 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 256 bij: dat is lineair; de factoren (1,25, 1,20) zijn niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 1,25 per uur. Om 06.00 uur zijn er 1200 muggen. Hoeveel muggen waren er om 05.00 uur? Rond af op een geheel getal.",
      "antwoord": "960",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1200 : 1,25 ≈ 960,0 → 960 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal volgers van een account op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×2). Dat is tabel C.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 152\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"166.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"187\" y1=\"1\" x2=\"187\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"212.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">52</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">61</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"166.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">56</text><line x1=\"187\" y1=\"31\" x2=\"187\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"212.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">81</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">24</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"103\" y1=\"61\" x2=\"103\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">36</text><line x1=\"145\" y1=\"61\" x2=\"145\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"166.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">42</text><line x1=\"187\" y1=\"61\" x2=\"187\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"212.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"1\" y1=\"61\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">160</text><line x1=\"103\" y1=\"91\" x2=\"103\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">320</text><line x1=\"145\" y1=\"91\" x2=\"145\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"166.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">640</text><line x1=\"187\" y1=\"91\" x2=\"187\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"212.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">1280</text><line x1=\"1\" y1=\"91\" x2=\"237\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"103\" y1=\"121\" x2=\"103\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"145\" y1=\"121\" x2=\"145\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"166.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"187\" y1=\"121\" x2=\"187\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"212.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"121\" x2=\"237\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel B",
        "tabel C",
        "tabel D"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 15% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 15%: je houdt 115% over, dus groeifactor 1,15.",
      "opties": [
        "0,85",
        "1,5",
        "0,15",
        "1,15"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 5% af. Om het aantal één uur eerder te berekenen, deel je het huidige aantal door 0,95.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,95."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 8% toe. Om 10.00 uur zijn er 12.000 downloads. Bereken het aantal downloads om 13.00 uur. Rond af op een geheel getal.",
      "antwoord": "15117",
      "uitleg": "Groeifactor 1,08. Na 3 uur: 12.000 · 1,08³ ≈ 15116,5 → 15117.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal volgers van een account (A) op tijdstip t, te beginnen met 640. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 640 (beginwaarde). Elke stap ×1,5 (960 : 640 = 1,5). Dus A = 640 · 1,5ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 262 62\" width=\"262\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"260\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"211\" y1=\"1\" x2=\"211\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"236.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">640</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">960</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1440</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2160</text><line x1=\"211\" y1=\"31\" x2=\"211\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"236.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3240</text><line x1=\"1\" y1=\"31\" x2=\"261\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 640 · 1,5ᵗ",
        "A = 640 · 2/3ᵗ",
        "A = 960 · 1,5ᵗ",
        "A = 640 + 320t"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal bacteriën in een bakje) hoort bij een exponentieel verband met waarden 256 op t = 1 en 1024 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "64",
      "uitleg": "Groeifactor: 1024 : 256 = 4. Terug naar t = 0: 256 : 4 = 64.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 254 62\" width=\"254\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"252\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"74.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"74.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4096</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16384</text><line x1=\"1\" y1=\"31\" x2=\"253\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 160, 480, 1440, 4320 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 480 : 160 = 3, 1440 : 480 = 3 … De factor is steeds gelijk (3), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 3."
    }
  ]
});
