/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 23 — §1.1 Lineaire formules opstellen (4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.1 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-13",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Proeftoets 23 — §1.1 Lineaire formules opstellen (4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = −x − 3. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = −x − 3. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: −1. Het losse getal is het startgetal: −3.",
      "opties": [
        "richtingscoëfficiënt −3 en startgetal −1",
        "richtingscoëfficiënt 1 en startgetal −3",
        "richtingscoëfficiënt −1 en startgetal 3",
        "richtingscoëfficiënt −1 en startgetal −3"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(1, −10) en Q(5, −30). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-5",
      "uitleg": "rc = toename y / toename x = (−30 − (−10)) / (5 − 1) = −20 / 4 = −5."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (1, −5) en (6, −15)?",
      "uitleg": "a = (−15 − (−5)) / (6 − 1) = −2. Invullen van (1, −5) geeft −5 = −2 + b, dus b = −3. De formule is y = −2x − 3.",
      "opties": [
        "y = 2x − 3",
        "y = −2x + 3",
        "y = −2x − 3",
        "y = −2x − 5"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Lijn l in de figuur gaat onder andere door het punt (4, −3). Welke formule hoort bij lijn l?",
      "uitleg": "Lijn l snijdt de y-as in (0, 3), dus het startgetal is 3. Tussen de stippen (0, 3) en (4, −3): rc = −6 / 4 = −1,5. Dus y = −1,5x + 3.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c9\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c9)\" x1=\"2.0\" y1=\"30.0\" x2=\"282.0\" y2=\"450.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"173.2\" y=\"269.8\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">l</text><circle cx=\"58.0\" cy=\"114.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"170.0\" cy=\"282.0\" r=\"3.5\" fill=\"#222\"/></svg>",
      "opties": [
        "y = −2/3x + 3",
        "y = −1,5x − 3",
        "y = −1,5x + 3",
        "y = 1,5x + 3"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (−6, 7) ligt op de lijn y = 0,5x + 10.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = −6: y = 0,5 · (−6) + 10 = 7. Dat is gelijk aan 7, dus het punt ligt op de lijn."
    },
    {
      "type": "invul",
      "vraag": "Lijn k gaat door de punten (0, 1) en (2, 4) (zie figuur). Lees af hoe groot de richtingscoëfficiënt van lijn k is. Geef je antwoord als decimaal getal.",
      "antwoord": "1,5",
      "uitleg": "Van (0, 1) naar (2, 4): 2 naar rechts en 3 omhoog. rc = 3 / 2 = 1,5.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c10\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c10)\" x1=\"2.0\" y1=\"254.0\" x2=\"282.0\" y2=\"-166.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"145.2\" y=\"40.2\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">k</text><circle cx=\"58.0\" cy=\"170.0\" r=\"3.5\" fill=\"#222\"/><text x=\"64.0\" y=\"164.0\" fill=\"#222\" font-size=\"11\">(0, 1)</text><circle cx=\"114.0\" cy=\"86.0\" r=\"3.5\" fill=\"#222\"/><text x=\"120.0\" y=\"80.0\" fill=\"#222\" font-size=\"11\">(2, 4)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (4, 13) en loopt evenwijdig aan lijn l: y = −4x − 11. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = −4. Invullen van (4, 13): 13 = −4 · 4 + b = −16 + b, dus b = 29. Lijn m: y = −4x + 29.",
      "opties": [
        "y = 4x − 3",
        "y = −4x − 3",
        "y = −4x + 13",
        "y = −4x + 29"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De lijn y = ax + b gaat door de punten (4, −4) en (13, −22). Bereken het startgetal b.",
      "antwoord": "4",
      "uitleg": "Eerst a = −18 / 9 = −2. Invullen van (4, −4): −4 = −2 · 4 + b, dus −4 = −8 + b en b = 4."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijn bij de formule y = −3x + 7 is stijgend.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc is −3; die is negatief, dus de lijn is dalend."
    },
    {
      "type": "mc",
      "vraag": "Aylin spaart voor een scooter. Met de formule s = 250 + 8w berekent Aylin het bedrag s in euro's na w weken. Daan begint op hetzelfde moment, heeft nog niets gespaard en spaart per week drie keer zoveel als Aylin. Welke formule hoort bij Daan?",
      "uitleg": "Daan begint bij 0 euro (startgetal 0) en spaart drie keer 8 = 24 euro per week (rc 24). Dus s = 24w.",
      "opties": [
        "s = 750 + 8w",
        "s = 24w",
        "s = 750 + 24w",
        "s = 250 + 24w"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Bij de tabel hoort een lineair verband (x loopt van 2 tot 14). Welke formule hoort bij de tabel?",
      "uitleg": "Per 3 stappen in x verandert y met 9, dus rc = 9 / 3 = 3. Invullen van (2, 21): b = 21 − 6 = 15.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">8</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">11</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">14</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">21</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">30</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">39</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">48</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">57</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "y = 3x + 21",
        "y = −3x + 15",
        "y = 9x + 15",
        "y = 3x + 15"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Lijn m loopt evenwijdig aan de lijn y = 3x + 9 en gaat door het punt (−5, 2). Een formule bij m is y = 3x + b. Bereken b.",
      "antwoord": "17",
      "uitleg": "2 = 3 · (−5) + b → 2 = −15 + b → b = 17."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij lijn k door de punten (−3, −6) en (6, −6)?",
      "uitleg": "De y-coördinaat is bij beide punten −6: de toename van y is 0, dus rc = 0. De lijn is horizontaal: y = −6.",
      "opties": [
        "y = x − 6",
        "x = −6",
        "y = −6",
        "y = −6x"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (10, −42) ligt op de lijn y = −4x − 4.",
      "antwoord": false,
      "uitleg": "Onwaar. Invullen van x = 10: y = −4 · 10 − 4 = −44. Dat is niet −42, dus het punt ligt niet op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de stijgende lijnen y = 1,5x + 1; y = 3x − 6; y = 4x + 1; y = 6x + 5. Welke lijn loopt het steilst?",
      "uitleg": "Hoe groter de richtingscoëfficiënt, hoe steiler de lijn. De grootste rc is 6. Het startgetal maakt voor de steilheid niet uit.",
      "opties": [
        "y = 6x + 5",
        "y = 3x − 6",
        "y = 4x + 1",
        "y = 1,5x + 1"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = 3x − 6 en y = −1 + 3x lopen evenwijdig.",
      "antwoord": true,
      "uitleg": "Waar. Evenwijdige lijnen hebben dezelfde richtingscoëfficiënt. Hier: 3 en 3, gelijk."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (5, 17) en (8, 23)?",
      "uitleg": "a = (23 − 17) / (8 − 5) = 2. Invullen van (5, 17) geeft 17 = 10 + b, dus b = 7. De formule is y = 2x + 7.",
      "opties": [
        "y = 2x − 7",
        "y = −2x + 7",
        "y = 2x + 17",
        "y = 2x + 7"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (−5, 11) en loopt evenwijdig aan lijn l: y = −2x + 8. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = −2. Invullen van (−5, 11): 11 = −2 · (−5) + b = 10 + b, dus b = 1. Lijn m: y = −2x + 1.",
      "opties": [
        "y = −2x + 1",
        "y = −2x + 11",
        "y = −2x + 21",
        "y = 2x + 21"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(3, 22) en Q(8, 37). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "3",
      "uitleg": "rc = toename y / toename x = (37 − 22) / (8 − 3) = 15 / 5 = 3."
    },
    {
      "type": "open",
      "vraag": "Stel een formule op bij de lijn door de punten A(5, −17) en B(9, −25). Schrijf je antwoord als y = ax + b.",
      "modelantwoord": "y = −2x − 7",
      "sleutelwoorden": [
        "-2x/−2x",
        "- 7/-7/− 7"
      ],
      "minTreffers": 2,
      "uitleg": "rc = (−25 − (−17)) / (9 − 5) = −2. Invullen van A: −17 = −10 + b, dus b = −7. Formule: y = −2x − 7."
    }
  ]
});
