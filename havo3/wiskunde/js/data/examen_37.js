/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 37 — §1.4 Exponentiële groei (3/5, gemengd)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-27",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 37 — §1.4 Exponentiële groei (3/5, gemengd)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal downloads van een spel op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+12). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 246 152\" width=\"246\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"244\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">49</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">62</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"1\" y1=\"31\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">22</text><line x1=\"69\" y1=\"61\" x2=\"69\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">34</text><line x1=\"111\" y1=\"61\" x2=\"111\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">46</text><line x1=\"153\" y1=\"61\" x2=\"153\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">58</text><line x1=\"195\" y1=\"61\" x2=\"195\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">70</text><line x1=\"1\" y1=\"61\" x2=\"245\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"69\" y1=\"91\" x2=\"69\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">384</text><line x1=\"111\" y1=\"91\" x2=\"111\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">576</text><line x1=\"153\" y1=\"91\" x2=\"153\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">864</text><line x1=\"195\" y1=\"91\" x2=\"195\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">1296</text><line x1=\"1\" y1=\"91\" x2=\"245\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"69\" y1=\"121\" x2=\"69\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"111\" y1=\"121\" x2=\"111\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"153\" y1=\"121\" x2=\"153\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"195\" y1=\"121\" x2=\"195\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"121\" x2=\"245\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel D",
        "tabel B",
        "tabel C"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een bibliotheek vanaf 2020. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,92",
      "uitleg": "7360 : 8000 ≈ 0,92; ook 6771 : 7360 ≈ 0,92. De groeifactor is 0,92.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8000</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">7360</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6771</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6230</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bezoekers van een website (A) op tijdstip t, te beginnen met 32. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 32 (beginwaarde). Elke stap ×2 (64 : 32 = 2). Dus A = 32 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 222 62\" width=\"222\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"220\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"137\" y1=\"1\" x2=\"137\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"137\" y1=\"31\" x2=\"137\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">512</text><line x1=\"1\" y1=\"31\" x2=\"221\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 32 · 2ᵗ",
        "A = 32 + 32t",
        "A = 32 · 0,5ᵗ",
        "A = 64 · 2ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,85 per uur. Om 06.00 uur zijn er 1500 muggen. Hoeveel muggen waren er om 05.00 uur? Rond af op een geheel getal.",
      "antwoord": "1765",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1500 : 0,85 ≈ 1764,7 → 1765 muggen.",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 80, 120, 180, 270 hoort bij een exponentieel verband.",
      "antwoord": true,
      "uitleg": "Waar. De factor is steeds 1,5."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 12% af. Om 10.00 uur zijn er 3600 downloads. Bereken het aantal downloads om 14.00 uur. Rond af op een geheel getal.",
      "antwoord": "2159",
      "uitleg": "Groeifactor 0,88. Na 4 uur: 3600 · 0,88⁴ ≈ 2158,9 → 2159.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 12% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 12%: je houdt 88% over, dus groeifactor 0,88.",
      "opties": [
        "1,12",
        "0,88",
        "1,2",
        "0,12"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 12% af. Om het aantal één uur eerder te berekenen, vermenigvuldig je het huidige aantal met 1,12.",
      "antwoord": false,
      "uitleg": "Onwaar. Je moet delen door de groeifactor 0,88. Vermenigvuldigen met 1,12 geeft een ander (te klein) antwoord, want 12% van een kleiner getal is minder."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal vissen in een vijver) hoort bij een exponentieel verband met waarden 28 op t = 1 en 112 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "7",
      "uitleg": "Groeifactor: 112 : 28 = 4. Terug naar t = 0: 28 : 4 = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 222 62\" width=\"222\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"220\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">112</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">448</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1792</text><line x1=\"1\" y1=\"31\" x2=\"221\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft het aantal planten in een kas (N), met 450 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 200. Van t = 0 naar t = 1: 300 : 200 = 1,5. Dus N = 200 · 1,5ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 312\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"312\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c40\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"238.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"268.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"268.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"268.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"268.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"272.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"304.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c40)\" points=\"40.0,200.0 41.7,198.6 43.4,197.2 45.1,195.7 46.8,194.3 48.5,192.7 50.2,191.2 51.9,189.6 53.6,188.0 55.3,186.4 57.0,184.7 58.7,183.0 60.4,181.3 62.1,179.5 63.8,177.7 65.5,175.8 67.2,173.9 68.9,172.0 70.6,170.1 72.3,168.0 74.0,166.0 75.7,163.9 77.4,161.8 79.1,159.6 80.8,157.4 82.5,155.1 84.2,152.8 85.9,150.4 87.6,148.0 89.3,145.6 91.0,143.1 92.7,140.5 94.4,137.9 96.1,135.2 97.8,132.5 99.5,129.7 101.2,126.9 102.9,124.0 104.6,121.1 106.3,118.1 108.0,115.0 109.7,111.9 111.4,108.7 113.1,105.4 114.8,102.1 116.5,98.7 118.2,95.2 119.9,91.7 121.6,88.1 123.3,84.4 125.0,80.6 126.7,76.8 128.4,72.9 130.1,68.9 131.8,64.8 133.5,60.6 135.2,56.4 136.9,52.0 138.6,47.6 140.3,43.1 142.0,38.5 143.7,33.8 145.4,29.0 147.1,24.1 148.8,19.1 150.5,14.0 152.2,8.8 153.9,3.5 155.6,-1.9 157.3,-7.4 159.0,-13.1 160.7,-18.8 162.4,-24.7 164.1,-30.7 165.8,-36.8 167.5,-43.1 169.2,-49.4 170.9,-55.9 172.6,-62.6 174.3,-69.3 176.0,-76.2\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"200.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"194.0\" fill=\"#222\" font-size=\"11\">(0, 200)</text><circle cx=\"74.0\" cy=\"166.0\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"160.0\" fill=\"#222\" font-size=\"11\">(1, 300)</text><circle cx=\"108.0\" cy=\"115.0\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"109.0\" fill=\"#222\" font-size=\"11\">(2, 450)</text><circle cx=\"142.0\" cy=\"38.5\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"32.5\" fill=\"#222\" font-size=\"11\">(3, 675)</text></svg>",
      "opties": [
        "N = 200 · 2/3ᵗ",
        "N = 200 + 100t",
        "N = 300 · 1,5ᵗ",
        "N = 200 · 1,5ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De bevolking van een land groeit exponentieel: in 2000 waren er 8,50 miljoen en in 2005 8,88 miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
      "antwoord": "1,045",
      "uitleg": "9,70 : 9,28 ≈ 1,045. (De andere stappen geven ongeveer hetzelfde: 1,045, 1,045.)",
      "tolerantie": 0.002,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 340 62\" width=\"340\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"338\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2000</text><line x1=\"189\" y1=\"1\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2005</text><line x1=\"239\" y1=\"1\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2010</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2015</text><rect x=\"1\" y=\"31\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">bevolking (mln)</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8,50</text><line x1=\"189\" y1=\"31\" x2=\"189\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8,88</text><line x1=\"239\" y1=\"31\" x2=\"239\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">9,28</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">9,70</text><line x1=\"1\" y1=\"31\" x2=\"339\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 128, 192, 256, 320 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 64 bij: dat is lineair; de factoren (1,50, 1,33) zijn niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 1,25 per uur. Om 10.00 uur zijn er 3000 muggen. Hoeveel muggen waren er om 09.00 uur? Rond af op een geheel getal.",
      "antwoord": "2400",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 3000 : 1,25 ≈ 2400,0 → 2400 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal bacteriën in een bakje op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+8). Dat is tabel D.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 270 152\" width=\"270\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"268\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"211\" y1=\"1\" x2=\"211\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">53</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">86</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">68</text><line x1=\"211\" y1=\"31\" x2=\"211\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">14</text><line x1=\"1\" y1=\"31\" x2=\"269\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"69\" y1=\"61\" x2=\"69\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"111\" y1=\"61\" x2=\"111\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"161\" y1=\"61\" x2=\"161\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">19</text><line x1=\"211\" y1=\"61\" x2=\"211\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"61\" x2=\"269\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"69\" y1=\"91\" x2=\"69\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"111\" y1=\"91\" x2=\"111\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">2304</text><line x1=\"161\" y1=\"91\" x2=\"161\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">6912</text><line x1=\"211\" y1=\"91\" x2=\"211\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">20736</text><line x1=\"1\" y1=\"91\" x2=\"269\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">51</text><line x1=\"69\" y1=\"121\" x2=\"69\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">59</text><line x1=\"111\" y1=\"121\" x2=\"111\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">67</text><line x1=\"161\" y1=\"121\" x2=\"161\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">75</text><line x1=\"211\" y1=\"121\" x2=\"211\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">83</text><line x1=\"1\" y1=\"121\" x2=\"269\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel B",
        "tabel C",
        "tabel D",
        "tabel A"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 6% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 6%: je houdt 106% over, dus groeifactor 1,06.",
      "opties": [
        "0,06",
        "1,06",
        "0,6",
        "0,94"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 8% af. Om het aantal één uur eerder te berekenen, deel je het huidige aantal door 0,92.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,92."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 8% af. Om 10.00 uur zijn er 3600 downloads. Bereken het aantal downloads om 13.00 uur. Rond af op een geheel getal.",
      "antwoord": "2803",
      "uitleg": "Groeifactor 0,92. Na 3 uur: 3600 · 0,92³ ≈ 2803,3 → 2803.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft de hoeveelheid medicijn in het bloed (A) op tijdstip t, te beginnen met 2048. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 2048 (beginwaarde). Elke stap ×3 (6144 : 2048 = 3). Dus A = 2048 · 3ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 310 62\" width=\"310\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"308\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"156.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"185\" y1=\"1\" x2=\"185\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"243\" y1=\"1\" x2=\"243\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"276.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2048</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6144</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"156.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">18432</text><line x1=\"185\" y1=\"31\" x2=\"185\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">55296</text><line x1=\"243\" y1=\"31\" x2=\"243\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"276.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">165888</text><line x1=\"1\" y1=\"31\" x2=\"309\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 2048 · 3ᵗ",
        "A = 6144 · 3ᵗ",
        "A = 2048 · 1/3ᵗ",
        "A = 2048 + 4096t"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal volgers van een account) hoort bij een exponentieel verband met waarden 21 op t = 1 en 63 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "7",
      "uitleg": "Groeifactor: 63 : 21 = 3. Terug naar t = 0: 21 : 3 = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 62\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"204\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">21</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">63</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">189</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">567</text><line x1=\"1\" y1=\"31\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 64, 80, 100, 125 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 80 : 64 = 1,25, 100 : 80 = 1,25 … De factor is steeds gelijk (1,25), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 1,25."
    }
  ]
});
