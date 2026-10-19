/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 77 — §1.4 Lineair of exponentieel (extra 4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-54",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 77 — §1.4 Lineair of exponentieel (extra 4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal vissen in een vijver op t = 0, 1, 2, 3, 4: 135, 147, 159, 171, 183. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds 12 bij, dus lineair. De factoren (1,089, 1,082) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">135</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">147</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">159</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">171</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">183</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De tabel (257, 261, 265, …) hoort bij lineaire groei. Welk getal hoort op t = 5?",
      "antwoord": "277",
      "uitleg": "Lineair: er komt steeds 4 bij. 273 + 4 = 277.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 264 62\" width=\"264\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"262\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"237\" y1=\"1\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">257</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">261</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">265</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">269</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">273</text><line x1=\"237\" y1=\"31\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"263\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "De tabel (160, 80, 40, …) hoort bij exponentiële groei. Welk getal hoort op t = 5?",
      "antwoord": "5",
      "uitleg": "Exponentieel: groeifactor 80 : 160 = 0,5. 10 · 0,5 = 5.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 232 62\" width=\"232\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"230\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"86.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"137\" y1=\"1\" x2=\"137\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"188.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"205\" y1=\"1\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"218.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">160</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"86.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">40</text><line x1=\"137\" y1=\"31\" x2=\"137\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"188.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"205\" y1=\"31\" x2=\"205\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"218.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"231\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp is nu 15.000 en neemt elk jaar met 8% toe. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Elk jaar een vast percentage: exponentieel met groeifactor 1,08 (108%). A = begin · 1,08ᵗ.",
      "opties": [
        "A = 15.000 · 1,08ᵗ",
        "A = 15.000 · 0,08ᵗ",
        "A = 15.000 + 8t",
        "A = 15.000 · 0,92ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel wordt elke waarde 0,6 keer zo groot als de vorige. Dan hoort de tabel bij exponentiële groei met groeifactor 0,6.",
      "antwoord": true,
      "uitleg": "Waar. Steeds met hetzelfde getal vermenigvuldigen = exponentieel."
    },
    {
      "type": "invul",
      "vraag": "Het aantal vliegjes in een kas verandert exponentieel met groeifactor 1,2 per uur. Om 10.00 uur zijn er 960 vliegjes. Hoeveel waren er om 08.00 uur? Rond af op een geheel getal.",
      "antwoord": "667",
      "uitleg": "Twee uur terug: twee keer delen door 1,2, dus 960 : 1,2² ≈ 666,7 → 667.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een festival vanaf 2020. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,04",
      "uitleg": "312.000 : 300.000 ≈ 1,04; ook 324.480 : 312.000 ≈ 1,04. De groeifactor is 1,04.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 364 62\" width=\"364\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"362\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"141\" y1=\"1\" x2=\"141\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">300.000</text><line x1=\"141\" y1=\"31\" x2=\"141\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">312.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">324.480</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">337.459</text><line x1=\"1\" y1=\"31\" x2=\"363\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bacteriën in een bakje op t = 0, 1, 2, 3, 4: 28, 33, 48, 73, 108. Welk soort groei hoort bij de tabel?",
      "uitleg": "De verschillen (5, 15, 25) zijn niet gelijk en de factoren (1,179, 1,455) ook niet.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 62\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"204\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">33</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">73</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">108</text><line x1=\"1\" y1=\"31\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "geen van beide",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "zowel lineaire als exponentiële groei",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Het aantal fietsdiefstallen in een stad neemt al jaren met 20% per jaar af. In 2021 waren het er 736. Hoeveel waren het er in 2020? Rond af op een geheel getal.",
      "antwoord": "920",
      "uitleg": "Groeifactor 0,8. Een jaar terug: delen, 736 : 0,8 ≈ 920,0 → 920. (Niet 736 · 1,2!)",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel komt er steeds 12 bij. Dan hoort de tabel bij exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (1; 96) en (2; 144). Bereken de groeifactor g.",
      "antwoord": "1,5",
      "uitleg": "Van t = 1 naar t = 2 is één stap: g = 144 : 96 = 1,5.",
      "tolerantie": 0.0005
    },
    {
      "type": "mc",
      "vraag": "Het aantal leden van een sportclub is nu 5000 en neemt elk jaar met 40 toe. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (40) bij: lineair, A = begin + 40t.",
      "opties": [
        "A = 5000 · 40ᵗ",
        "A = 5000 · 1,4ᵗ",
        "A = 40 + 5000t",
        "A = 5000 + 40t"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 32, 64, 96, 128 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 32 bij: dat is lineair; de factoren (2,00, 1,50) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal downloads van een spel op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×0,5). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 152\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"129\" y1=\"61\" x2=\"129\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">8</text><line x1=\"163\" y1=\"61\" x2=\"163\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"1\" y1=\"61\" x2=\"197\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">73</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">77</text><line x1=\"129\" y1=\"91\" x2=\"129\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">54</text><line x1=\"163\" y1=\"91\" x2=\"163\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">72</text><line x1=\"1\" y1=\"91\" x2=\"197\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">13</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">19</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">25</text><line x1=\"129\" y1=\"121\" x2=\"129\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">31</text><line x1=\"163\" y1=\"121\" x2=\"163\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">37</text><line x1=\"1\" y1=\"121\" x2=\"197\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel C",
        "tabel B",
        "tabel A",
        "tabel D"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Opa zet € 5000 op spaarrekening A en € 5000 op spaarrekening B. Bij A komt er elk jaar € 400 bij. Bij B groeit het bedrag elk jaar met 6% (groeifactor 1,06). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
      "antwoord": "11",
      "uitleg": "Maak een tabel. A = 5000 + 400t, B = 5000 · 1,06ᵗ. Na 10 jaar: A = 9000, B ≈ 8954; na 11 jaar: A = 9400, B ≈ 9491. Dus na 11 jaar."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (3; 320) en (4; 256). Bereken de beginwaarde b (de waarde op t = 0).",
      "antwoord": "625",
      "uitleg": "g = 256 : 320 = 0,8. Terug naar t = 0 is 3 stappen: b = 320 : 0,8³ = 625.",
      "tolerantie": 0.5
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel komt er steeds 7 bij. Dan hoort de tabel bij exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal vissen in een vijver) hoort bij een exponentieel verband met waarden 96 op t = 1 en 192 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "48",
      "uitleg": "Groeifactor: 192 : 96 = 2. Terug naar t = 0: 96 : 2 = 48.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 62\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">96</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">384</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal vissen in een vijver op t = 0, 1, 2, 3, 4: 12, 17, 32, 57, 92. Welk soort groei hoort bij de tabel?",
      "uitleg": "De verschillen (5, 15, 25) zijn niet gelijk en de factoren (1,417, 1,882) ook niet.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">57</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">92</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 1
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 256, 384, 576, 864 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 384 : 256 = 1,5, 576 : 384 = 1,5 … De factor is steeds gelijk (1,5), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 1,5."
    }
  ]
});
