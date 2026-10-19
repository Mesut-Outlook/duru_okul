/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 74 — §1.4 Lineair of exponentieel (extra 1/5, basis)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-51",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 74 — §1.4 Lineair of exponentieel (extra 1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal konijnen op een eiland op t = 0, 1, 2, 3, 4: 64, 192, 576, 1728, 5184. Welk soort groei hoort bij de tabel?",
      "uitleg": "De factor is steeds 3 (192 : 64), dus exponentieel. De verschillen zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 246 62\" width=\"246\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"244\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">576</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1728</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">5184</text><line x1=\"1\" y1=\"31\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "geen van beide",
        "zowel lineaire als exponentiële groei",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De tabel (290, 293, 296, …) hoort bij lineaire groei. Welk getal hoort op t = 5?",
      "antwoord": "305",
      "uitleg": "Lineair: er komt steeds 3 bij. 302 + 3 = 305.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 264 62\" width=\"264\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"262\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"237\" y1=\"1\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">290</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">293</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">296</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">299</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">302</text><line x1=\"237\" y1=\"31\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"263\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "De tabel (80, 240, 720, …) hoort bij exponentiële groei. Welk getal hoort op t = 5?",
      "antwoord": "19440",
      "uitleg": "Exponentieel: groeifactor 240 : 80 = 3. 6480 · 3 = 19440.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 272 62\" width=\"272\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"270\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"245\" y1=\"1\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">240</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">720</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2160</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6480</text><line x1=\"245\" y1=\"31\" x2=\"245\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"271\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal leden van een sportclub is nu 5000 en neemt elk jaar met 50 af. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (50) af: lineair, A = begin − 50t.",
      "opties": [
        "A = 5000 · 0,5ᵗ",
        "A = 50 − 5000t",
        "A = 5000 · 50ᵗ",
        "A = 5000 − 50t"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel wordt elke waarde 0,8 keer zo groot als de vorige. Dan hoort de tabel bij exponentiële groei met groeifactor 0,8.",
      "antwoord": true,
      "uitleg": "Waar. Steeds met hetzelfde getal vermenigvuldigen = exponentieel."
    },
    {
      "type": "invul",
      "vraag": "Het aantal vliegjes in een kas verandert exponentieel met groeifactor 1,25 per uur. Om 05.00 uur zijn er 960 vliegjes. Hoeveel waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "614",
      "uitleg": "Twee uur terug: twee keer delen door 1,25, dus 960 : 1,25² ≈ 614,4 → 614.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een museum vanaf 2018. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,15",
      "uitleg": "345.000 : 300.000 ≈ 1,15; ook 396.750 : 345.000 ≈ 1,15. De groeifactor is 1,15.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 364 62\" width=\"364\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"362\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2018</text><line x1=\"141\" y1=\"1\" x2=\"141\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">300.000</text><line x1=\"141\" y1=\"31\" x2=\"141\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">345.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">396.750</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">456.262</text><line x1=\"1\" y1=\"31\" x2=\"363\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal planten in een kas op t = 0, 1, 2, 3, 4: 64, 32, 16, 8, 4. Welk soort groei hoort bij de tabel?",
      "uitleg": "De factor is steeds 0,5 (32 : 64), dus exponentieel. De verschillen zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 182 62\" width=\"182\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"180\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"168.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"168.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"1\" y1=\"31\" x2=\"181\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "geen van beide",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "zowel lineaire als exponentiële groei",
        "lineaire groei: er komt steeds hetzelfde getal bij"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Het aantal fietsdiefstallen in een stad neemt al jaren met 10% per jaar toe. In 2023 waren het er 460. Hoeveel waren het er in 2022? Rond af op een geheel getal.",
      "antwoord": "418",
      "uitleg": "Groeifactor 1,1. Een jaar terug: delen, 460 : 1,1 ≈ 418,2 → 418. (Niet 460 · 0,9!)",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Een bedrag neemt elk jaar met 150 euro toe. Dan is er sprake van exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Elk jaar hetzelfde bedrag (150 euro) erbij is lineair."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (3; 216) en (4; 324). Bereken de groeifactor g.",
      "antwoord": "1,5",
      "uitleg": "Van t = 3 naar t = 4 is één stap: g = 324 : 216 = 1,5.",
      "tolerantie": 0.0005
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers van een museum is nu 5000 en neemt elk jaar met 120 af. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (120) af: lineair, A = begin − 120t.",
      "opties": [
        "A = 5000 · 120ᵗ",
        "A = 120 − 5000t",
        "A = 5000 − 120t",
        "A = 5000 · 1,2ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 2048, 2560, 3072, 3584 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 512 bij: dat is lineair; de factoren (1,25, 1,20) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal bezoekers van een website op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×2). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 222 152\" width=\"222\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"220\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"137\" y1=\"1\" x2=\"137\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">96</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"137\" y1=\"31\" x2=\"137\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">384</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"1\" y1=\"31\" x2=\"221\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">33</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">37</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">41</text><line x1=\"137\" y1=\"61\" x2=\"137\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">45</text><line x1=\"179\" y1=\"61\" x2=\"179\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">49</text><line x1=\"1\" y1=\"61\" x2=\"221\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">41</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">77</text><line x1=\"137\" y1=\"91\" x2=\"137\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">52</text><line x1=\"179\" y1=\"91\" x2=\"179\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">36</text><line x1=\"1\" y1=\"91\" x2=\"221\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"137\" y1=\"121\" x2=\"137\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"179\" y1=\"121\" x2=\"179\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"200.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"121\" x2=\"221\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel A",
        "tabel C",
        "tabel B",
        "tabel D"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Opa zet € 5000 op spaarrekening A en € 5000 op spaarrekening B. Bij A komt er elk jaar € 750 bij. Bij B groeit het bedrag elk jaar met 12% (groeifactor 1,12). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
      "antwoord": "5",
      "uitleg": "Maak een tabel. A = 5000 + 750t, B = 5000 · 1,12ᵗ. Na 4 jaar: A = 8000, B ≈ 7868; na 5 jaar: A = 8750, B ≈ 8812. Dus na 5 jaar."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (3; 67,5) en (4; 50,625). Bereken de beginwaarde b (de waarde op t = 0).",
      "antwoord": "160",
      "uitleg": "g = 50,625 : 67,5 = 0,75. Terug naar t = 0 is 3 stappen: b = 67,5 : 0,75³ = 160.",
      "tolerantie": 0.5
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel komt er steeds 140 bij. Dan hoort de tabel bij exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal planten in een kas) hoort bij een exponentieel verband met waarden 24 op t = 1 en 36 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "16",
      "uitleg": "Groeifactor: 36 : 24 = 1,5. Terug naar t = 0: 24 : 1,5 = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 190 62\" width=\"190\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"188\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">24</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">36</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">54</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">81</text><line x1=\"1\" y1=\"31\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal konijnen op een eiland op t = 0, 1, 2, 3, 4: 100, 95, 90, 85, 80. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds −5 bij, dus lineair. De factoren (0,950, 0,947) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 62\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"204\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"86.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"137\" y1=\"1\" x2=\"137\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"188.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">100</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"86.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">95</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"120.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">90</text><line x1=\"137\" y1=\"31\" x2=\"137\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"154.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">85</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"188.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"1\" y1=\"31\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "geen van beide",
        "zowel lineaire als exponentiële groei",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 48, 96, 192, 384 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 96 : 48 = 2, 192 : 96 = 2 … De factor is steeds gelijk (2), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 2."
    }
  ]
});
