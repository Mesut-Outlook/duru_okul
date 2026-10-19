/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 76 — §1.4 Lineair of exponentieel (extra 3/5, gemengd)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-53",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 76 — §1.4 Lineair of exponentieel (extra 3/5, gemengd)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabel geeft de hoeveelheid medicijn in het bloed op t = 0, 1, 2, 3, 4: 1024, 1536, 2304, 3456, 5184. Welk soort groei hoort bij de tabel?",
      "uitleg": "De factor is steeds 1,5 (1536 : 1024), dus exponentieel. De verschillen zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 278 62\" width=\"278\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"276\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"177\" y1=\"1\" x2=\"177\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"227\" y1=\"1\" x2=\"227\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1536</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2304</text><line x1=\"177\" y1=\"31\" x2=\"177\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3456</text><line x1=\"227\" y1=\"31\" x2=\"227\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">5184</text><line x1=\"1\" y1=\"31\" x2=\"277\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "zowel lineaire als exponentiële groei",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "lineaire groei: er komt steeds hetzelfde getal bij"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De tabel (207, 222, 237, …) hoort bij lineaire groei. Welk getal hoort op t = 5?",
      "antwoord": "282",
      "uitleg": "Lineair: er komt steeds 15 bij. 267 + 15 = 282.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 264 62\" width=\"264\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"262\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"237\" y1=\"1\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">207</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">222</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">237</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">252</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">267</text><line x1=\"237\" y1=\"31\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"263\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "De tabel (48, 144, 432, …) hoort bij exponentiële groei. Welk getal hoort op t = 5?",
      "antwoord": "11664",
      "uitleg": "Exponentieel: groeifactor 144 : 48 = 3. 3888 · 3 = 11664.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 272 62\" width=\"272\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"270\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"245\" y1=\"1\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">144</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1296</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3888</text><line x1=\"245\" y1=\"31\" x2=\"245\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"271\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal leden van een sportclub is nu 640 en neemt elk jaar met 40 af. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (40) af: lineair, A = begin − 40t.",
      "opties": [
        "A = 640 · 40ᵗ",
        "A = 40 − 640t",
        "A = 640 − 40t",
        "A = 640 · 0,6ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Een bedrag neemt elk jaar met 3% toe. Dan is er sprake van exponentiële groei.",
      "antwoord": true,
      "uitleg": "Waar. Een vast percentage per jaar geeft een vaste groeifactor, dus exponentieel."
    },
    {
      "type": "invul",
      "vraag": "Het aantal vliegjes in een kas verandert exponentieel met groeifactor 1,25 per uur. Om 14.00 uur zijn er 6000 vliegjes. Hoeveel waren er om 12.00 uur? Rond af op een geheel getal.",
      "antwoord": "3840",
      "uitleg": "Twee uur terug: twee keer delen door 1,25, dus 6000 : 1,25² ≈ 3840,0 → 3840.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een pretpark vanaf 2019. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,96",
      "uitleg": "576 : 600 ≈ 0,96; ook 553 : 576 ≈ 0,96. De groeifactor is 0,96.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">600</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">576</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">553</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">531</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal downloads van een spel op t = 0, 1, 2, 3, 4: 119, 115, 111, 107, 103. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds −4 bij, dus lineair. De factoren (0,966, 0,965) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">119</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">115</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">111</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">107</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">103</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Het aantal woninginbraken in een stad neemt al jaren met 4% per jaar af. In 2024 waren het er 5520. Hoeveel waren het er in 2023? Rond af op een geheel getal.",
      "antwoord": "5750",
      "uitleg": "Groeifactor 0,96. Een jaar terug: delen, 5520 : 0,96 ≈ 5750,0 → 5750. (Niet 5520 · 1,04!)",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2 met waarden 100, 200, 300 hoort bij exponentiële groei met groeifactor 2.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 100 bij (lineair); de factoren zijn 2 en 1,5, niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (2; 90) en (3; 45). Bereken de groeifactor g.",
      "antwoord": "0,5",
      "uitleg": "Van t = 2 naar t = 3 is één stap: g = 45 : 90 = 0,5.",
      "tolerantie": 0.0005
    },
    {
      "type": "mc",
      "vraag": "Het aantal bezoekers van een museum is nu 1200 en neemt elk jaar met 120 toe. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (120) bij: lineair, A = begin + 120t.",
      "opties": [
        "A = 1200 + 120t",
        "A = 120 + 1200t",
        "A = 1200 · 1,2ᵗ",
        "A = 1200 · 120ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 16, 48, 80, 112 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 32 bij: dat is lineair; de factoren (3,00, 1,67) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal vissen in een vijver op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+8). Dat is tabel B.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 152\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">19</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">55</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">63</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">71</text><line x1=\"129\" y1=\"61\" x2=\"129\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">79</text><line x1=\"163\" y1=\"61\" x2=\"163\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">87</text><line x1=\"1\" y1=\"61\" x2=\"197\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">24</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"129\" y1=\"91\" x2=\"129\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"163\" y1=\"91\" x2=\"163\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"1\" y1=\"91\" x2=\"197\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">38</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"129\" y1=\"121\" x2=\"129\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"163\" y1=\"121\" x2=\"163\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">89</text><line x1=\"1\" y1=\"121\" x2=\"197\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
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
      "vraag": "Opa zet € 1000 op spaarrekening A en € 1000 op spaarrekening B. Bij A komt er elk jaar € 120 bij. Bij B groeit het bedrag elk jaar met 10% (groeifactor 1,10). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
      "antwoord": "5",
      "uitleg": "Maak een tabel. A = 1000 + 120t, B = 1000 · 1,10ᵗ. Na 4 jaar: A = 1480, B ≈ 1464; na 5 jaar: A = 1600, B ≈ 1611. Dus na 5 jaar."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (1; 120) en (2; 90). Bereken de beginwaarde b (de waarde op t = 0).",
      "antwoord": "160",
      "uitleg": "g = 90 : 120 = 0,75. Terug naar t = 0 is 1 stap: b = 120 : 0,75¹ = 160.",
      "tolerantie": 0.5
    },
    {
      "type": "waaronwaar",
      "vraag": "Een bedrag neemt elk jaar met 40 euro toe. Dan is er sprake van exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Elk jaar hetzelfde bedrag (40 euro) erbij is lineair."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal vissen in een vijver) hoort bij een exponentieel verband met waarden 14 op t = 1 en 28 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "7",
      "uitleg": "Groeifactor: 28 : 14 = 2. Terug naar t = 0: 14 : 2 = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">14</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">56</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">112</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal vissen in een vijver op t = 0, 1, 2, 3, 4: 64, 192, 576, 1728, 5184. Welk soort groei hoort bij de tabel?",
      "uitleg": "De factor is steeds 3 (192 : 64), dus exponentieel. De verschillen zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 246 62\" width=\"246\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"244\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"103\" y1=\"1\" x2=\"103\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"82.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"103\" y1=\"31\" x2=\"103\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"124.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">576</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"170.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1728</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">5184</text><line x1=\"1\" y1=\"31\" x2=\"245\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 1
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 320, 960, 2880, 8640 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 960 : 320 = 3, 2880 : 960 = 3 … De factor is steeds gelijk (3), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 3."
    }
  ]
});
