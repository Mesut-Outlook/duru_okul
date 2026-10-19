/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 75 — §1.4 Lineair of exponentieel (extra 2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-52",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 75 — §1.4 Lineair of exponentieel (extra 2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal volgers van een account op t = 0, 1, 2, 3, 4: 215, 209, 203, 197, 191. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds −6 bij, dus lineair. De factoren (0,972, 0,971) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">215</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">209</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">203</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">197</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">191</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "zowel lineaire als exponentiële groei",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "geen van beide"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De tabel (120, 123, 126, …) hoort bij lineaire groei. Welk getal hoort op t = 5?",
      "antwoord": "135",
      "uitleg": "Lineair: er komt steeds 3 bij. 132 + 3 = 135.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 264 62\" width=\"264\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"262\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"237\" y1=\"1\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">120</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">123</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">126</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">129</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">132</text><line x1=\"237\" y1=\"31\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"250.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"263\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "De tabel (16, 48, 144, …) hoort bij exponentiële groei. Welk getal hoort op t = 5?",
      "antwoord": "3888",
      "uitleg": "Exponentieel: groeifactor 48 : 16 = 3. 1296 · 3 = 3888.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 256 62\" width=\"256\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"254\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"137\" y1=\"1\" x2=\"137\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"229\" y1=\"1\" x2=\"229\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">144</text><line x1=\"137\" y1=\"31\" x2=\"137\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1296</text><line x1=\"229\" y1=\"31\" x2=\"229\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"255\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal leden van een sportclub is nu 800 en neemt elk jaar met 120 af. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (120) af: lineair, A = begin − 120t.",
      "opties": [
        "A = 800 · 1,2ᵗ",
        "A = 800 · 120ᵗ",
        "A = 800 − 120t",
        "A = 120 − 800t"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Een bedrag neemt elk jaar met 9% toe. Dan is er sprake van exponentiële groei.",
      "antwoord": true,
      "uitleg": "Waar. Een vast percentage per jaar geeft een vaste groeifactor, dus exponentieel."
    },
    {
      "type": "invul",
      "vraag": "Het aantal vliegjes in een kas verandert exponentieel met groeifactor 1,25 per uur. Om 05.00 uur zijn er 2400 vliegjes. Hoeveel waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "1536",
      "uitleg": "Twee uur terug: twee keer delen door 1,25, dus 2400 : 1,25² ≈ 1536,0 → 1536.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een bioscoop vanaf 2018. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "0,96",
      "uitleg": "2400 : 2500 ≈ 0,96; ook 2304 : 2400 ≈ 0,96. De groeifactor is 0,96.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2018</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2500</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2400</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2304</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2212</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft de hoeveelheid medicijn in het bloed op t = 0, 1, 2, 3, 4: 128, 192, 288, 432, 648. Welk soort groei hoort bij de tabel?",
      "uitleg": "De factor is steeds 1,5 (192 : 128), dus exponentieel. De verschillen zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">192</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">288</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">648</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Het aantal verkochte cd's in een stad neemt al jaren met 20% per jaar af. In 2024 waren het er 1250. Hoeveel waren het er in 2023? Rond af op een geheel getal.",
      "antwoord": "1562",
      "uitleg": "Groeifactor 0,8. Een jaar terug: delen, 1250 : 0,8 ≈ 1562,5 → 1562. (Niet 1250 · 1,2!)",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel komt er steeds 35 bij. Dan hoort de tabel bij exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (1; 180) en (2; 90). Bereken de groeifactor g.",
      "antwoord": "0,5",
      "uitleg": "Van t = 1 naar t = 2 is één stap: g = 90 : 180 = 0,5.",
      "tolerantie": 0.0005
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp is nu 1200 en neemt elk jaar met 5% af. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Elk jaar een vast percentage: exponentieel met groeifactor 0,95 (95%). A = begin · 0,95ᵗ.",
      "opties": [
        "A = 1200 − 5t",
        "A = 1200 · 1,05ᵗ",
        "A = 1200 · 0,05ᵗ",
        "A = 1200 · 0,95ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 32, 48, 64, 80 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 16 bij: dat is lineair; de factoren (1,50, 1,33) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal bacteriën in een bakje op vier plekken. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×0,5). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 152\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"119\" y1=\"1\" x2=\"119\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"203\" y1=\"1\" x2=\"203\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">512</text><line x1=\"119\" y1=\"31\" x2=\"119\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"203\" y1=\"31\" x2=\"203\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"77\" y1=\"61\" x2=\"77\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">38</text><line x1=\"119\" y1=\"61\" x2=\"119\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">44</text><line x1=\"161\" y1=\"61\" x2=\"161\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">50</text><line x1=\"203\" y1=\"61\" x2=\"203\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">56</text><line x1=\"1\" y1=\"61\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"77\" y1=\"91\" x2=\"77\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"119\" y1=\"91\" x2=\"119\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"161\" y1=\"91\" x2=\"161\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"203\" y1=\"91\" x2=\"203\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"91\" x2=\"237\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"77\" y1=\"121\" x2=\"77\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"98.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">79</text><line x1=\"119\" y1=\"121\" x2=\"119\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"140.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">84</text><line x1=\"161\" y1=\"121\" x2=\"161\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">31</text><line x1=\"203\" y1=\"121\" x2=\"203\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">85</text><line x1=\"1\" y1=\"121\" x2=\"237\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel D",
        "tabel C",
        "tabel B",
        "tabel A"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Opa zet € 2000 op spaarrekening A en € 2000 op spaarrekening B. Bij A komt er elk jaar € 240 bij. Bij B groeit het bedrag elk jaar met 8% (groeifactor 1,08). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
      "antwoord": "11",
      "uitleg": "Maak een tabel. A = 2000 + 240t, B = 2000 · 1,08ᵗ. Na 10 jaar: A = 4400, B ≈ 4318; na 11 jaar: A = 4640, B ≈ 4663. Dus na 11 jaar."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (3; 135) en (4; 101,25). Bereken de beginwaarde b (de waarde op t = 0).",
      "antwoord": "320",
      "uitleg": "g = 101,25 : 135 = 0,75. Terug naar t = 0 is 3 stappen: b = 135 : 0,75³ = 320.",
      "tolerantie": 0.5
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel komt er steeds 9 bij. Dan hoort de tabel bij exponentiële groei.",
      "antwoord": false,
      "uitleg": "Onwaar. Steeds hetzelfde getal erbij is lineair; bij exponentieel vermenigvuldig je steeds met hetzelfde getal."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal bezoekers van een website) hoort bij een exponentieel verband met waarden 48 op t = 1 en 144 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "16",
      "uitleg": "Groeifactor: 144 : 48 = 3. Terug naar t = 0: 48 : 3 = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 222 62\" width=\"222\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"220\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">144</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">432</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1296</text><line x1=\"1\" y1=\"31\" x2=\"221\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal bacteriën in een bakje op t = 0, 1, 2, 3, 4: 315, 311, 307, 303, 299. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds −4 bij, dus lineair. De factoren (0,987, 0,987) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">315</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">311</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">307</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">303</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">299</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "geen van beide",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 1
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 64, 128, 256, 512 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 128 : 64 = 2, 256 : 128 = 2 … De factor is steeds gelijk (2), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 2."
    }
  ]
});
