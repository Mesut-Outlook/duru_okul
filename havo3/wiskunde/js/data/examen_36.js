/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 36 — §1.4 Exponentiële groei (2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-26",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 36 — §1.4 Exponentiële groei (2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven de hoeveelheid medicijn in het bloed op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+6). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 246 152\" width=\"246\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"244\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"119\" y1=\"1\" x2=\"119\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"203\" y1=\"1\" x2=\"203\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">45</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">75</text><line x1=\"119\" y1=\"31\" x2=\"119\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"203\" y1=\"31\" x2=\"203\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">31</text><line x1=\"1\" y1=\"31\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">47</text><line x1=\"77\" y1=\"61\" x2=\"77\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">53</text><line x1=\"119\" y1=\"61\" x2=\"119\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">59</text><line x1=\"161\" y1=\"61\" x2=\"161\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">65</text><line x1=\"203\" y1=\"61\" x2=\"203\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">71</text><line x1=\"1\" y1=\"61\" x2=\"245\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"77\" y1=\"91\" x2=\"77\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"119\" y1=\"91\" x2=\"119\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">576</text><line x1=\"161\" y1=\"91\" x2=\"161\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"203\" y1=\"91\" x2=\"203\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">324</text><line x1=\"1\" y1=\"91\" x2=\"245\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"77\" y1=\"121\" x2=\"77\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"119\" y1=\"121\" x2=\"119\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"161\" y1=\"121\" x2=\"161\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"203\" y1=\"121\" x2=\"203\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"224.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"121\" x2=\"245\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel C",
        "tabel B",
        "tabel D"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een bioscoop vanaf 2019. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,12",
      "uitleg": "336.000 : 300.000 ≈ 1,12; ook 376.320 : 336.000 ≈ 1,12. De groeifactor is 1,12.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 364 62\" width=\"364\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"362\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"141\" y1=\"1\" x2=\"141\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">300.000</text><line x1=\"141\" y1=\"31\" x2=\"141\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">336.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">376.320</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">421.478</text><line x1=\"1\" y1=\"31\" x2=\"363\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bacteriën in een bakje (A) op tijdstip t, te beginnen met 48. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 48 (beginwaarde). Elke stap ×3 (144 : 48 = 3). Dus A = 48 · 3ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 246 62\" width=\"246\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"244\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">144</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1296</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3888</text><line x1=\"1\" y1=\"31\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 144 · 3ᵗ",
        "A = 48 + 96t",
        "A = 48 · 1/3ᵗ",
        "A = 48 · 3ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,8 per uur. Om 06.00 uur zijn er 3000 muggen. Hoeveel muggen waren er om 05.00 uur? Rond af op een geheel getal.",
      "antwoord": "3750",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 3000 : 0,8 ≈ 3750,0 → 3750 muggen.",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 160, 480, 1440, 4320 hoort bij een exponentieel verband.",
      "antwoord": true,
      "uitleg": "Waar. De factor is steeds 3."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 15% af. Om 10.00 uur zijn er 800 downloads. Bereken het aantal downloads om 14.00 uur. Rond af op een geheel getal.",
      "antwoord": "418",
      "uitleg": "Groeifactor 0,85. Na 4 uur: 800 · 0,85⁴ ≈ 417,6 → 418.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 3% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 3%: je houdt 103% over, dus groeifactor 1,03.",
      "opties": [
        "0,3",
        "0,97",
        "0,03",
        "1,03"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 20% af. Om het aantal één uur eerder te berekenen, vermenigvuldig je het huidige aantal met 1,2.",
      "antwoord": false,
      "uitleg": "Onwaar. Je moet delen door de groeifactor 0,8. Vermenigvuldigen met 1,2 geeft een ander (te klein) antwoord, want 20% van een kleiner getal is minder."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal konijnen op een eiland) hoort bij een exponentieel verband met waarden 14 op t = 1 en 28 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "7",
      "uitleg": "Groeifactor: 28 : 14 = 2. Terug naar t = 0: 14 : 2 = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">14</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">56</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">112</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft het aantal downloads van een spel (N), met 1600 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 400. Van t = 0 naar t = 1: 800 : 400 = 2. Dus N = 400 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 312\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"312\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c39\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"238.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"268.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"268.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"268.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"268.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">1000</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">1500</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">2000</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">2500</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">3000</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">3500</text><text x=\"35.0\" y=\"283.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"272.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"304.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c39)\" points=\"40.0,240.8 41.7,239.8 43.4,238.8 45.1,237.8 46.8,236.8 48.5,235.7 50.2,234.5 51.9,233.3 53.6,232.1 55.3,230.8 57.0,229.5 58.7,228.2 60.4,226.8 62.1,225.3 63.8,223.8 65.5,222.3 67.2,220.6 68.9,219.0 70.6,217.2 72.3,215.5 74.0,213.6 75.7,211.7 77.4,209.7 79.1,207.6 80.8,205.5 82.5,203.3 84.2,201.0 85.9,198.7 87.6,196.2 89.3,193.7 91.0,191.1 92.7,188.4 94.4,185.5 96.1,182.6 97.8,179.6 99.5,176.5 101.2,173.3 102.9,169.9 104.6,166.5 106.3,162.9 108.0,159.2 109.7,155.4 111.4,151.4 113.1,147.3 114.8,143.0 116.5,138.6 118.2,134.1 119.9,129.3 121.6,124.4 123.3,119.4 125.0,114.1 126.7,108.7 128.4,103.1 130.1,97.3 131.8,91.3 133.5,85.0 135.2,78.6 136.9,71.9 138.6,65.0 140.3,57.8 142.0,50.4 143.7,42.7 145.4,34.8 147.1,26.6 148.8,18.0 150.5,9.2 152.2,0.1 153.9,-9.3 155.6,-19.1 157.3,-29.3 159.0,-39.7 160.7,-50.6 162.4,-61.8 164.1,-73.5 165.8,-85.5 167.5,-98.0 169.2,-110.9 170.9,-124.2 172.6,-138.1 174.3,-152.4 176.0,-167.2\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"240.8\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"234.8\" fill=\"#222\" font-size=\"11\">(0, 400)</text><circle cx=\"74.0\" cy=\"213.6\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"207.6\" fill=\"#222\" font-size=\"11\">(1, 800)</text><circle cx=\"108.0\" cy=\"159.2\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"153.2\" fill=\"#222\" font-size=\"11\">(2, 1600)</text><circle cx=\"142.0\" cy=\"50.4\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"44.4\" fill=\"#222\" font-size=\"11\">(3, 3200)</text></svg>",
      "opties": [
        "N = 400 · 0,5ᵗ",
        "N = 800 · 2ᵗ",
        "N = 400 · 2ᵗ",
        "N = 400 + 400t"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De bevolking van een land groeit exponentieel: in 2000 waren er 3,60 miljoen en in 2005 3,76 miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
      "antwoord": "1,046",
      "uitleg": "4,11 : 3,93 ≈ 1,046. (De andere stappen geven ongeveer hetzelfde: 1,044, 1,045.)",
      "tolerantie": 0.002,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 340 62\" width=\"340\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"338\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2000</text><line x1=\"189\" y1=\"1\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2005</text><line x1=\"239\" y1=\"1\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2010</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2015</text><rect x=\"1\" y=\"31\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">bevolking (mln)</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3,60</text><line x1=\"189\" y1=\"31\" x2=\"189\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3,76</text><line x1=\"239\" y1=\"31\" x2=\"239\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3,93</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4,11</text><line x1=\"1\" y1=\"31\" x2=\"339\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 32, 96, 160, 224 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 64 bij: dat is lineair; de factoren (3,00, 1,67) zijn niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,75 per uur. Om 06.00 uur zijn er 1500 muggen. Hoeveel muggen waren er om 05.00 uur? Rond af op een geheel getal.",
      "antwoord": "2000",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1500 : 0,75 ≈ 2000,0 → 2000 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal planten in een kas op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+12). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 152\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">42</text><line x1=\"129\" y1=\"61\" x2=\"129\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">54</text><line x1=\"171\" y1=\"61\" x2=\"171\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">66</text><line x1=\"1\" y1=\"61\" x2=\"213\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"129\" y1=\"91\" x2=\"129\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"171\" y1=\"91\" x2=\"171\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"1\" y1=\"91\" x2=\"213\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">47</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">71</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">50</text><line x1=\"129\" y1=\"121\" x2=\"129\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">19</text><line x1=\"171\" y1=\"121\" x2=\"171\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">44</text><line x1=\"1\" y1=\"121\" x2=\"213\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel B",
        "tabel D",
        "tabel C"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 4% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 4%: je houdt 96% over, dus groeifactor 0,96.",
      "opties": [
        "0,96",
        "1,04",
        "0,04",
        "0,4"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 10% af. Om het aantal één uur eerder te berekenen, deel je het huidige aantal door 0,9.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,9."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 5% toe. Om 10.00 uur zijn er 4500 downloads. Bereken het aantal downloads om 13.00 uur. Rond af op een geheel getal.",
      "antwoord": "5209",
      "uitleg": "Groeifactor 1,05. Na 3 uur: 4500 · 1,05³ ≈ 5209,3 → 5209.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal vissen in een vijver (A) op tijdstip t, te beginnen met 2048. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 2048 (beginwaarde). Elke stap ×0,5 (1024 : 2048 = 0,5). Dus A = 2048 · 0,5ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 254 62\" width=\"254\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"252\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"148.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"169\" y1=\"1\" x2=\"169\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"190.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"211\" y1=\"1\" x2=\"211\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"232.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2048</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"148.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">512</text><line x1=\"169\" y1=\"31\" x2=\"169\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"190.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"211\" y1=\"31\" x2=\"211\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"232.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"1\" y1=\"31\" x2=\"253\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 2048 · 0,5ᵗ",
        "A = 2048 · 2ᵗ",
        "A = 1024 · 0,5ᵗ",
        "A = 2048 + −1024t"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal volgers van een account) hoort bij een exponentieel verband met waarden 96 op t = 1 en 144 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "64",
      "uitleg": "Groeifactor: 144 : 96 = 1,5. Terug naar t = 0: 96 : 1,5 = 64.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">96</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">144</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">216</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">324</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 128, 384, 1152, 3456 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 384 : 128 = 3, 1152 : 384 = 3 … De factor is steeds gelijk (3), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 3."
    }
  ]
});
