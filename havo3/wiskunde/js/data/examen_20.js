/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 20 — §1.1 Lineaire formules opstellen (1/5, basis)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.1 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-10",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Proeftoets 20 — §1.1 Lineaire formules opstellen (1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = 0,75x + 9. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = 0,75x + 9. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: 0,75. Het losse getal is het startgetal: 9.",
      "opties": [
        "richtingscoëfficiënt 0,75 en startgetal 9",
        "richtingscoëfficiënt 0,75 en startgetal −9",
        "richtingscoëfficiënt 9 en startgetal 0,75",
        "richtingscoëfficiënt −0,75 en startgetal 9"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(1, −3) en Q(6, −28). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-5",
      "uitleg": "rc = toename y / toename x = (−28 − (−3)) / (6 − 1) = −25 / 5 = −5."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (2, 11) en (11, 2)?",
      "uitleg": "a = (2 − 11) / (11 − 2) = −1. Invullen van (2, 11) geeft 11 = −2 + b, dus b = 13. De formule is y = −x + 13.",
      "opties": [
        "y = x + 13",
        "y = −x + 11",
        "y = −x − 13",
        "y = −x + 13"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Lijn l in de figuur gaat onder andere door het punt (6, −3). Welke formule hoort bij lijn l?",
      "uitleg": "Lijn l snijdt de y-as in (0, −1), dus het startgetal is −1. Tussen de stippen (0, −1) en (6, −3): rc = −2 / 6 = −1/3. Dus y = −1/3x − 1.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c1\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c1)\" x1=\"2.0\" y1=\"207.3\" x2=\"282.0\" y2=\"300.7\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"243.2\" y=\"277.7\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">l</text><circle cx=\"58.0\" cy=\"226.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"226.0\" cy=\"282.0\" r=\"3.5\" fill=\"#222\"/></svg>",
      "opties": [
        "y = −3x − 1",
        "y = −1/3x + 1",
        "y = 1/3x − 1",
        "y = −1/3x − 1"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (4, −8) ligt op de lijn y = −3x + 4.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = 4: y = −3 · 4 + 4 = −8. Dat is gelijk aan −8, dus het punt ligt op de lijn."
    },
    {
      "type": "invul",
      "vraag": "Lijn k gaat door de punten (0, −2) en (6, 1) (zie figuur). Lees af hoe groot de richtingscoëfficiënt van lijn k is. Geef je antwoord als decimaal getal.",
      "antwoord": "0,5",
      "uitleg": "Van (0, −2) naar (6, 1): 6 naar rechts en 3 omhoog. rc = 3 / 6 = 0,5.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c2)\" x1=\"2.0\" y1=\"282.0\" x2=\"282.0\" y2=\"142.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"243.2\" y=\"156.4\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">k</text><circle cx=\"58.0\" cy=\"254.0\" r=\"3.5\" fill=\"#222\"/><text x=\"64.0\" y=\"248.0\" fill=\"#222\" font-size=\"11\">(0, −2)</text><circle cx=\"226.0\" cy=\"170.0\" r=\"3.5\" fill=\"#222\"/><text x=\"232.0\" y=\"164.0\" fill=\"#222\" font-size=\"11\">(6, 1)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (8, 0) en loopt evenwijdig aan lijn l: y = 0,5x − 13. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = 0,5. Invullen van (8, 0): 0 = 0,5 · 8 + b = 4 + b, dus b = −4. Lijn m: y = 0,5x − 4.",
      "opties": [
        "y = −0,5x + 4",
        "y = 0,5x − 4",
        "y = 0,5x",
        "y = 0,5x + 4"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De lijn y = ax + b gaat door de punten (5, 28) en (9, 44). Bereken het startgetal b.",
      "antwoord": "8",
      "uitleg": "Eerst a = 16 / 4 = 4. Invullen van (5, 28): 28 = 4 · 5 + b, dus 28 = 20 + b en b = 8."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijn bij de formule y = 7 − 7x is stijgend.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc is −7; die is negatief, dus de lijn is dalend."
    },
    {
      "type": "mc",
      "vraag": "Sem spaart voor een scooter. Met de formule s = 120 + 20w berekent Sem het bedrag s in euro's na w weken. Lotte begint op hetzelfde moment, heeft nog niets gespaard en spaart per week twee keer zoveel als Sem. Welke formule hoort bij Lotte?",
      "uitleg": "Lotte begint bij 0 euro (startgetal 0) en spaart twee keer 20 = 40 euro per week (rc 40). Dus s = 40w.",
      "opties": [
        "s = 40w",
        "s = 120 + 40w",
        "s = 240 + 20w",
        "s = 240 + 40w"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Bij de tabel hoort een lineair verband (x loopt van 2 tot 18). Welke formule hoort bij de tabel?",
      "uitleg": "Per 4 stappen in x verandert y met 12, dus rc = 12 / 4 = 3. Invullen van (2, 16): b = 16 − 6 = 10.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 198 62\" width=\"198\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"196\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">14</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">18</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">28</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">40</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">52</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"1\" y1=\"31\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "y = 12x + 10",
        "y = −3x + 10",
        "y = 3x + 10",
        "y = 3x + 16"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Lijn m loopt evenwijdig aan de lijn y = 4x + 3 en gaat door het punt (5, −12). Een formule bij m is y = 4x + b. Bereken b.",
      "antwoord": "-32",
      "uitleg": "−12 = 4 · 5 + b → −12 = 20 + b → b = −32."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij lijn k door de punten (−8, 4) en (9, 4)?",
      "uitleg": "De y-coördinaat is bij beide punten 4: de toename van y is 0, dus rc = 0. De lijn is horizontaal: y = 4.",
      "opties": [
        "y = 4x",
        "y = x + 4",
        "y = 4",
        "x = 4"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (12, 37) ligt op de lijn y = 3x + 3.",
      "antwoord": false,
      "uitleg": "Onwaar. Invullen van x = 12: y = 3 · 12 + 3 = 39. Dat is niet 37, dus het punt ligt niet op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de stijgende lijnen y = 1,5x + 3; y = 3x − 6; y = 2x − 4; y = 6x − 3. Welke lijn loopt het steilst?",
      "uitleg": "Hoe groter de richtingscoëfficiënt, hoe steiler de lijn. De grootste rc is 6. Het startgetal maakt voor de steilheid niet uit.",
      "opties": [
        "y = 6x − 3",
        "y = 3x − 6",
        "y = 2x − 4",
        "y = 1,5x + 3"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = 3x − 6 en y = −3 + 3x lopen evenwijdig.",
      "antwoord": true,
      "uitleg": "Waar. Evenwijdige lijnen hebben dezelfde richtingscoëfficiënt. Hier: 3 en 3, gelijk."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (−6, −28) en (−4, −22)?",
      "uitleg": "a = (−22 − (−28)) / (−4 − (−6)) = 3. Invullen van (−6, −28) geeft −28 = −18 + b, dus b = −10. De formule is y = 3x − 10.",
      "opties": [
        "y = −3x − 10",
        "y = 3x − 10",
        "y = 3x + 10",
        "y = 3x − 28"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (−6, 3) en loopt evenwijdig aan lijn l: y = 4x − 2. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = 4. Invullen van (−6, 3): 3 = 4 · (−6) + b = −24 + b, dus b = 27. Lijn m: y = 4x + 27.",
      "opties": [
        "y = −4x − 21",
        "y = 4x + 27",
        "y = 4x − 21",
        "y = 4x + 3"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(4, −2) en Q(9, −12). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-2",
      "uitleg": "rc = toename y / toename x = (−12 − (−2)) / (9 − 4) = −10 / 5 = −2."
    },
    {
      "type": "open",
      "vraag": "Stel een formule op bij de lijn door de punten A(−2, −1) en B(5, 34). Schrijf je antwoord als y = ax + b.",
      "modelantwoord": "y = 5x + 9",
      "sleutelwoorden": [
        "5x/5x",
        "+ 9/+9"
      ],
      "minTreffers": 2,
      "uitleg": "rc = (34 − (−1)) / (5 − (−2)) = 5. Invullen van A: −1 = −10 + b, dus b = 9. Formule: y = 5x + 9."
    }
  ]
});
