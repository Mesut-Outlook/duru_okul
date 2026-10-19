/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 78 — §1.4 Lineair of exponentieel (extra 5/5, eindniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.4 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools/gen_wiskunde_h1_14_15_extra.py, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-55",
  "hoofdstuk": 1,
  "paragraaf": "1.4",
  "titel": "Proeftoets 78 — §1.4 Lineair of exponentieel (extra 5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal planten in een kas op t = 0, 1, 2, 3, 4: 53, 58, 73, 98, 133. Welk soort groei hoort bij de tabel?",
      "uitleg": "De verschillen (5, 15, 25) zijn niet gelijk en de factoren (1,094, 1,259) ook niet.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 62\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"204\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">53</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">58</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">73</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">98</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">133</text><line x1=\"1\" y1=\"31\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal",
        "geen van beide",
        "zowel lineaire als exponentiële groei"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De tabel (108, 102, 96, …) hoort bij lineaire groei. Welk getal hoort op t = 5?",
      "antwoord": "78",
      "uitleg": "Lineair: er komt steeds −6 bij. 84 − 6 = 78.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 240 62\" width=\"240\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"238\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"128.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"145\" y1=\"1\" x2=\"145\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"162.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"179\" y1=\"1\" x2=\"179\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"213\" y1=\"1\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"226.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">108</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">102</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"128.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">96</text><line x1=\"145\" y1=\"31\" x2=\"145\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"162.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">90</text><line x1=\"179\" y1=\"31\" x2=\"179\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"196.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">84</text><line x1=\"213\" y1=\"31\" x2=\"213\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"226.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"239\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "De tabel (256, 768, 2304, …) hoort bij exponentiële groei. Welk getal hoort op t = 5?",
      "antwoord": "62208",
      "uitleg": "Exponentieel: groeifactor 768 : 256 = 3. 20736 · 3 = 62208.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 296 62\" width=\"296\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"294\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"161\" y1=\"1\" x2=\"161\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"211\" y1=\"1\" x2=\"211\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"269\" y1=\"1\" x2=\"269\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"282.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">N</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">768</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"136.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2304</text><line x1=\"161\" y1=\"31\" x2=\"161\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"186.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6912</text><line x1=\"211\" y1=\"31\" x2=\"211\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">20736</text><line x1=\"269\" y1=\"31\" x2=\"269\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"282.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"295\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp is nu 800 en neemt elk jaar met 300 toe. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Er gaat elk jaar hetzelfde aantal (300) bij: lineair, A = begin + 300t.",
      "opties": [
        "A = 800 · 300ᵗ",
        "A = 800 · 3ᵗ",
        "A = 800 + 300t",
        "A = 300 + 800t"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "In een tabel wordt elke waarde 1,25 keer zo groot als de vorige. Dan hoort de tabel bij exponentiële groei met groeifactor 1,25.",
      "antwoord": true,
      "uitleg": "Waar. Steeds met hetzelfde getal vermenigvuldigen = exponentieel."
    },
    {
      "type": "invul",
      "vraag": "Het aantal vliegjes in een kas verandert exponentieel met groeifactor 0,8 per uur. Om 08.00 uur zijn er 2400 vliegjes. Hoeveel waren er om 06.00 uur? Rond af op een geheel getal.",
      "antwoord": "3750",
      "uitleg": "Twee uur terug: twee keer delen door 0,8, dus 2400 : 0,8² ≈ 3750,0 → 3750.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een museum vanaf 2019. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,08",
      "uitleg": "2700 : 2500 ≈ 1,08; ook 2916 : 2700 ≈ 1,08. De groeifactor is 1,08.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2500</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2700</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2916</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3149</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal konijnen op een eiland op t = 0, 1, 2, 3, 4: 44, 46, 52, 62, 76. Welk soort groei hoort bij de tabel?",
      "uitleg": "De verschillen (2, 6, 10) zijn niet gelijk en de factoren (1,045, 1,130) ook niet.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">44</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">46</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">52</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">62</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">76</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "geen van beide",
        "zowel lineaire als exponentiële groei",
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Het aantal klachten bij een bedrijf in een stad neemt al jaren met 20% per jaar af. In 2022 waren het er 1250. Hoeveel waren het er in 2021? Rond af op een geheel getal.",
      "antwoord": "1562",
      "uitleg": "Groeifactor 0,8. Een jaar terug: delen, 1250 : 0,8 ≈ 1562,5 → 1562. (Niet 1250 · 1,2!)",
      "tolerantie": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2 met waarden 200, 400, 600 hoort bij exponentiële groei met groeifactor 2.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 200 bij (lineair); de factoren zijn 2 en 1,5, niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (3; 45) en (4; 22,5). Bereken de groeifactor g.",
      "antwoord": "0,5",
      "uitleg": "Van t = 3 naar t = 4 is één stap: g = 22,5 : 45 = 0,5.",
      "tolerantie": 0.0005
    },
    {
      "type": "mc",
      "vraag": "Het aantal leden van een sportclub is nu 640 en neemt elk jaar met 5% toe. Welke formule hoort bij het aantal A na t jaar?",
      "uitleg": "Elk jaar een vast percentage: exponentieel met groeifactor 1,05 (105%). A = begin · 1,05ᵗ.",
      "opties": [
        "A = 640 · 0,05ᵗ",
        "A = 640 · 1,05ᵗ",
        "A = 640 + 5t",
        "A = 640 · 0,95ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2, 3 met de waarden 320, 960, 1600, 2240 hoort bij een exponentieel verband.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 640 bij: dat is lineair; de factoren (3,00, 1,67) zijn niet gelijk."
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal bezoekers van een website op vier plekken. Welke tabel hoort bij lineaire groei?",
      "uitleg": "Bij lineaire groei komt er steeds hetzelfde getal bij (+12). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 286 152\" width=\"286\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"284\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"77\" y1=\"1\" x2=\"77\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"127\" y1=\"1\" x2=\"127\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"177\" y1=\"1\" x2=\"177\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"227\" y1=\"1\" x2=\"227\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"256.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">41</text><line x1=\"77\" y1=\"31\" x2=\"77\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">53</text><line x1=\"127\" y1=\"31\" x2=\"127\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">65</text><line x1=\"177\" y1=\"31\" x2=\"177\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">77</text><line x1=\"227\" y1=\"31\" x2=\"227\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"256.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">89</text><line x1=\"1\" y1=\"31\" x2=\"285\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"77\" y1=\"61\" x2=\"77\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"127\" y1=\"61\" x2=\"127\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"177\" y1=\"61\" x2=\"177\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"227\" y1=\"61\" x2=\"227\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"256.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"61\" x2=\"285\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">1024</text><line x1=\"77\" y1=\"91\" x2=\"77\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">2048</text><line x1=\"127\" y1=\"91\" x2=\"127\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">4096</text><line x1=\"177\" y1=\"91\" x2=\"177\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">8192</text><line x1=\"227\" y1=\"91\" x2=\"227\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"256.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">16384</text><line x1=\"1\" y1=\"91\" x2=\"285\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"52.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">57</text><line x1=\"77\" y1=\"121\" x2=\"77\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"102.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">62</text><line x1=\"127\" y1=\"121\" x2=\"127\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"177\" y1=\"121\" x2=\"177\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"202.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">68</text><line x1=\"227\" y1=\"121\" x2=\"227\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"256.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">15</text><line x1=\"1\" y1=\"121\" x2=\"285\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel B",
        "tabel D",
        "tabel C",
        "tabel A"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Opa zet € 500 op spaarrekening A en € 500 op spaarrekening B. Bij A komt er elk jaar € 60 bij. Bij B groeit het bedrag elk jaar met 10% (groeifactor 1,10). Na hoeveel hele jaren staat er op B voor het eerst meer dan op A?",
      "antwoord": "5",
      "uitleg": "Maak een tabel. A = 500 + 60t, B = 500 · 1,10ᵗ. Na 4 jaar: A = 740, B ≈ 732; na 5 jaar: A = 800, B ≈ 805. Dus na 5 jaar."
    },
    {
      "type": "invul",
      "vraag": "De grafiek van een exponentieel verband N = b · gᵗ gaat door de punten (1; 240) en (2; 180). Bereken de beginwaarde b (de waarde op t = 0).",
      "antwoord": "320",
      "uitleg": "g = 180 : 240 = 0,75. Terug naar t = 0 is 1 stap: b = 240 : 0,75¹ = 320.",
      "tolerantie": 0.5
    },
    {
      "type": "waaronwaar",
      "vraag": "De tabel t = 0, 1, 2 met waarden 50, 100, 150 hoort bij exponentiële groei met groeifactor 2.",
      "antwoord": false,
      "uitleg": "Onwaar. Er komt steeds 50 bij (lineair); de factoren zijn 2 en 1,5, niet gelijk."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal planten in een kas) hoort bij een exponentieel verband met waarden 14 op t = 1 en 28 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "7",
      "uitleg": "Groeifactor: 28 : 14 = 2. Terug naar t = 0: 14 : 2 = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">14</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">56</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"176.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">112</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "De tabel geeft het aantal volgers van een account op t = 0, 1, 2, 3, 4: 186, 201, 216, 231, 246. Welk soort groei hoort bij de tabel?",
      "uitleg": "Er komt steeds 15 bij, dus lineair. De factoren (1,081, 1,075) zijn niet gelijk.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 62\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">186</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">201</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">216</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">231</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">246</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "lineaire groei: er komt steeds hetzelfde getal bij",
        "geen van beide",
        "zowel lineaire als exponentiële groei",
        "exponentiële groei: je vermenigvuldigt steeds met hetzelfde getal"
      ],
      "antwoord": 0
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 64, 96, 144, 216 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 96 : 64 = 1,5, 144 : 96 = 1,5 … De factor is steeds gelijk (1,5), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 1,5."
    }
  ]
});
