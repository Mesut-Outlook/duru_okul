/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 38 — §1.4 Exponentiële groei (4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-28",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 38 — §1.4 Exponentiële groei (4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal vissen in een vijver op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×1,25). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 278 152\" width=\"278\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"276\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"177\" y1=\"1\" x2=\"177\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"227\" y1=\"1\" x2=\"227\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">39</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">47</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">55</text><line x1=\"177\" y1=\"31\" x2=\"177\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">63</text><line x1=\"227\" y1=\"31\" x2=\"227\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">71</text><line x1=\"1\" y1=\"31\" x2=\"277\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">2048</text><line x1=\"77\" y1=\"61\" x2=\"77\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">2560</text><line x1=\"127\" y1=\"61\" x2=\"127\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">3200</text><line x1=\"177\" y1=\"61\" x2=\"177\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">4000</text><line x1=\"227\" y1=\"61\" x2=\"227\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">5000</text><line x1=\"1\" y1=\"61\" x2=\"277\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">72</text><line x1=\"77\" y1=\"91\" x2=\"77\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">51</text><line x1=\"127\" y1=\"91\" x2=\"127\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"177\" y1=\"91\" x2=\"177\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">46</text><line x1=\"227\" y1=\"91\" x2=\"227\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"1\" y1=\"91\" x2=\"277\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"77\" y1=\"121\" x2=\"77\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"127\" y1=\"121\" x2=\"127\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"177\" y1=\"121\" x2=\"177\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"227\" y1=\"121\" x2=\"227\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"121\" x2=\"277\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
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
      "vraag": "In de tabel zie je het aantal bezoekers van een zwembad vanaf 2018. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,85",
      "uitleg": "2125 : 2500 ≈ 0,85; ook 1806 : 2125 ≈ 0,85. De groeifactor is 0,85.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2018</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2500</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2125</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1806</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1535</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bezoekers van een website (A) op tijdstip t, te beginnen met 320. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 320 (beginwaarde). Elke stap ×0,5 (160 : 320 = 0,5). Dus A = 320 · 0,5ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"128.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"162.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">320</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">160</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"128.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"162.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">40</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 160 · 0,5ᵗ",
        "A = 320 + −160t",
        "A = 320 · 0,5ᵗ",
        "A = 320 · 2ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,9 per uur. Om 04.00 uur zijn er 1500 muggen. Hoeveel muggen waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "1667",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1500 : 0,9 ≈ 1666,7 → 1667 muggen.",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 128, 256, 512, 1024 hoort bij een exponentieel verband.",
      "antwoord": true,
      "uitleg": "Waar. De factor is steeds 2."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 10% af. Om 10.00 uur zijn er 4500 downloads. Bereken het aantal downloads om 13.00 uur. Rond af op een geheel getal.",
      "antwoord": "3280",
      "uitleg": "Groeifactor 0,9. Na 3 uur: 4500 · 0,9³ ≈ 3280,5 → 3280.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 12% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 12%: je houdt 112% over, dus groeifactor 1,12.",
      "opties": [
        "1,12",
        "0,12",
        "1,2",
        "0,88"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 5% af. Om het aantal één uur eerder te berekenen, vermenigvuldig je het huidige aantal met 1,05.",
      "antwoord": false,
      "uitleg": "Onwaar. Je moet delen door de groeifactor 0,95. Vermenigvuldigen met 1,05 geeft een ander (te klein) antwoord, want 5% van een kleiner getal is minder."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal bacteriën in een bakje) hoort bij een exponentieel verband met waarden 96 op t = 1 en 192 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "48",
      "uitleg": "Groeifactor: 192 : 96 = 2. Terug naar t = 0: 96 : 2 = 48.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">96</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">384</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft het aantal bacteriën in een bakje (N), met 400 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 100. Van t = 0 naar t = 1: 200 : 100 = 2. Dus N = 100 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 346\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"346\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c41\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"272.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"302.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"302.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"302.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"302.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"302.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"176.0\" y2=\"302.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"176.0\" y2=\"302.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"272.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"306.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"338.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c41)\" points=\"40.0,268.0 41.7,266.8 43.4,265.6 45.1,264.3 46.8,262.9 48.5,261.6 50.2,260.1 51.9,258.7 53.6,257.1 55.3,255.6 57.0,253.9 58.7,252.2 60.4,250.5 62.1,248.6 63.8,246.8 65.5,244.8 67.2,242.8 68.9,240.7 70.6,238.6 72.3,236.3 74.0,234.0 75.7,231.6 77.4,229.1 79.1,226.5 80.8,223.9 82.5,221.1 84.2,218.3 85.9,215.3 87.6,212.3 89.3,209.1 91.0,205.8 92.7,202.4 94.4,198.9 96.1,195.3 97.8,191.5 99.5,187.6 101.2,183.6 102.9,179.4 104.6,175.1 106.3,170.6 108.0,166.0 109.7,161.2 111.4,156.2 113.1,151.1 114.8,145.8 116.5,140.3 118.2,134.6 119.9,128.7 121.6,122.5 123.3,116.2 125.0,109.7 126.7,102.9 128.4,95.9 130.1,88.6 131.8,81.1 133.5,73.3 135.2,65.2 136.9,56.9 138.6,48.2 140.3,39.3 142.0,30.0 143.7,20.4 145.4,10.5 147.1,0.2 148.8,-10.4 150.5,-21.5 152.2,-32.9 153.9,-44.7 155.6,-56.9 157.3,-69.6 159.0,-82.7 160.7,-96.2 162.4,-110.3 164.1,-124.8 165.8,-139.9 167.5,-155.4 169.2,-171.6 170.9,-188.3 172.6,-205.6 174.3,-223.5 176.0,-242.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"268.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"262.0\" fill=\"#222\" font-size=\"11\">(0, 100)</text><circle cx=\"74.0\" cy=\"234.0\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"228.0\" fill=\"#222\" font-size=\"11\">(1, 200)</text><circle cx=\"108.0\" cy=\"166.0\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"160.0\" fill=\"#222\" font-size=\"11\">(2, 400)</text><circle cx=\"142.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(3, 800)</text></svg>",
      "opties": [
        "N = 100 + 100t",
        "N = 100 · 2ᵗ",
        "N = 200 · 2ᵗ",
        "N = 100 · 0,5ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De bevolking van een land groeit exponentieel: in 2000 waren er 8,50 miljoen en in 2005 8,68 miljoen inwoners (zie tabel). Bereken de groeifactor per vijf jaar met de waarden van 2010 en 2015. Rond af op drie decimalen.",
      "antwoord": "1,021",
      "uitleg": "9,05 : 8,86 ≈ 1,021. (De andere stappen geven ongeveer hetzelfde: 1,021, 1,021.)",
      "tolerantie": 0.002,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 340 62\" width=\"340\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"338\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2000</text><line x1=\"189\" y1=\"1\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2005</text><line x1=\"239\" y1=\"1\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2010</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2015</text><rect x=\"1\" y=\"31\" width=\"138\" height=\"30\" fill=\"#fde7ef\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">bevolking (mln)</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"164.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8,50</text><line x1=\"189\" y1=\"31\" x2=\"189\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8,68</text><line x1=\"239\" y1=\"31\" x2=\"239\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"264.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8,86</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">9,05</text><line x1=\"1\" y1=\"31\" x2=\"339\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 80, 120, 160, 200 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 40 bij: dat is lineair; de factoren (1,50, 1,33) zijn niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,9 per uur. Om 10.00 uur zijn er 3000 muggen. Hoeveel muggen waren er om 09.00 uur? Rond af op een geheel getal.",
      "antwoord": "3333",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 3000 : 0,9 ≈ 3333,3 → 3333 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal volgers van een account op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+12). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 152\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">58</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">70</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">82</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">94</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">106</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">72</text><line x1=\"129\" y1=\"61\" x2=\"129\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">108</text><line x1=\"171\" y1=\"61\" x2=\"171\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">162</text><line x1=\"1\" y1=\"61\" x2=\"213\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"129\" y1=\"91\" x2=\"129\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"171\" y1=\"91\" x2=\"171\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"1\" y1=\"91\" x2=\"213\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">69</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">84</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"129\" y1=\"121\" x2=\"129\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"171\" y1=\"121\" x2=\"171\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">59</text><line x1=\"1\" y1=\"121\" x2=\"213\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel D",
        "tabel A",
        "tabel C",
        "tabel B"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 3% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 3%: je houdt 97% over, dus groeifactor 0,97.",
      "opties": [
        "0,03",
        "1,03",
        "0,3",
        "0,97"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per uur met 20% af. Om het aantal één uur eerder te berekenen, deel je het huidige aantal door 0,8.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,8."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 5% toe. Om 10.00 uur zijn er 2000 downloads. Bereken het aantal downloads om 12.00 uur. Rond af op een geheel getal.",
      "antwoord": "2205",
      "uitleg": "Groeifactor 1,05. Na 2 uur: 2000 · 1,05² ≈ 2205,0 → 2205.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal konijnen op een eiland (A) op tijdstip t, te beginnen met 16. Welke formule hoort bij de tabel?",
      "uitleg": "Op t = 0 is A = 16 (beginwaarde). Elke stap ×2 (32 : 16 = 2). Dus A = 16 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "A = 16 + 16t",
        "A = 32 · 2ᵗ",
        "A = 16 · 2ᵗ",
        "A = 16 · 0,5ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De tabel (de hoeveelheid medicijn in het bloed) hoort bij een exponentieel verband met waarden 24 op t = 1 en 36 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "16",
      "uitleg": "Groeifactor: 36 : 24 = 1,5. Terug naar t = 0: 24 : 1,5 = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 190 62\" width=\"190\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"188\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">24</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">36</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">54</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">81</text><line x1=\"1\" y1=\"31\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 256, 512, 1024, 2048 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 512 : 256 = 2, 1024 : 512 = 2 … De factor is steeds gelijk (2), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 2."
    }
  ]
});
