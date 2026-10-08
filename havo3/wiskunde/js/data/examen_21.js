/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 21 — §1.1 Lineaire formules opstellen (2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.1 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-11",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Proeftoets 21 — §1.1 Lineaire formules opstellen (2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = 2 − x. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = −x + 2. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: −1. Het losse getal is het startgetal: 2.",
      "opties": [
        "richtingscoëfficiënt −1 en startgetal −2",
        "richtingscoëfficiënt −1 en startgetal 2",
        "richtingscoëfficiënt 2 en startgetal −1",
        "richtingscoëfficiënt 1 en startgetal 2"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(−2, −5) en Q(3, 20). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "5",
      "uitleg": "rc = toename y / toename x = (20 − (−5)) / (3 − (−2)) = 25 / 5 = 5."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (4, 9) en (7, 6)?",
      "uitleg": "a = (6 − 9) / (7 − 4) = −1. Invullen van (4, 9) geeft 9 = −4 + b, dus b = 13. De formule is y = −x + 13.",
      "opties": [
        "y = −x − 13",
        "y = −x + 13",
        "y = x + 13",
        "y = −x + 9"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Lijn l in de figuur gaat onder andere door het punt (6, 2). Welke formule hoort bij lijn l?",
      "uitleg": "Lijn l snijdt de y-as in (0, −1), dus het startgetal is −1. Tussen de stippen (0, −1) en (6, 2): rc = 3 / 6 = 0,5. Dus y = 0,5x − 1.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c3\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c3)\" x1=\"2.0\" y1=\"254.0\" x2=\"282.0\" y2=\"114.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"243.2\" y=\"128.4\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">l</text><circle cx=\"58.0\" cy=\"226.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"226.0\" cy=\"142.0\" r=\"3.5\" fill=\"#222\"/></svg>",
      "opties": [
        "y = 0,5x − 1",
        "y = −0,5x − 1",
        "y = 2x − 1",
        "y = 0,5x + 1"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (−12, 2) ligt op de lijn y = −0,5x − 4.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = −12: y = −0,5 · (−12) − 4 = 2. Dat is gelijk aan 2, dus het punt ligt op de lijn."
    },
    {
      "type": "invul",
      "vraag": "Lijn k gaat door de punten (0, 3) en (6, 0) (zie figuur). Lees af hoe groot de richtingscoëfficiënt van lijn k is. Geef je antwoord als decimaal getal.",
      "antwoord": "-0,5",
      "uitleg": "Van (0, 3) naar (6, 0): 6 naar rechts en −3 omhoog. rc = −3 / 6 = −0,5.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c4\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c4)\" x1=\"2.0\" y1=\"86.0\" x2=\"282.0\" y2=\"226.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"243.2\" y=\"195.6\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">k</text><circle cx=\"58.0\" cy=\"114.0\" r=\"3.5\" fill=\"#222\"/><text x=\"64.0\" y=\"108.0\" fill=\"#222\" font-size=\"11\">(0, 3)</text><circle cx=\"226.0\" cy=\"198.0\" r=\"3.5\" fill=\"#222\"/><text x=\"232.0\" y=\"192.0\" fill=\"#222\" font-size=\"11\">(6, 0)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (5, 9) en loopt evenwijdig aan lijn l: y = −2x − 7. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = −2. Invullen van (5, 9): 9 = −2 · 5 + b = −10 + b, dus b = 19. Lijn m: y = −2x + 19.",
      "opties": [
        "y = −2x − 1",
        "y = −2x + 19",
        "y = 2x − 1",
        "y = −2x + 9"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De lijn y = ax + b gaat door de punten (−1, 8) en (2, 14). Bereken het startgetal b.",
      "antwoord": "10",
      "uitleg": "Eerst a = 6 / 3 = 2. Invullen van (−1, 8): 8 = 2 · (−1) + b, dus 8 = −2 + b en b = 10."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijn bij de formule y = −0,25x − 1 is stijgend.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc is −0,25; die is negatief, dus de lijn is dalend."
    },
    {
      "type": "mc",
      "vraag": "Mila spaart voor een scooter. Met de formule s = 150 + 25w berekent Mila het bedrag s in euro's na w weken. Yusuf begint op hetzelfde moment, heeft nog niets gespaard en spaart per week twee keer zoveel als Mila. Welke formule hoort bij Yusuf?",
      "uitleg": "Yusuf begint bij 0 euro (startgetal 0) en spaart twee keer 25 = 50 euro per week (rc 50). Dus s = 50w.",
      "opties": [
        "s = 150 + 50w",
        "s = 50w",
        "s = 300 + 50w",
        "s = 300 + 25w"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Bij de tabel hoort een lineair verband (x loopt van 5 tot 21). Welke formule hoort bij de tabel?",
      "uitleg": "Per 4 stappen in x verandert y met 8, dus rc = 8 / 4 = 2. Invullen van (5, 9): b = 9 − 10 = −1.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 190 62\" width=\"190\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"188\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">9</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">13</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">21</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">9</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">25</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">33</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"172.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">41</text><line x1=\"1\" y1=\"31\" x2=\"189\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "y = 2x + 9",
        "y = −2x − 1",
        "y = 2x − 1",
        "y = 8x − 1"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Lijn m loopt evenwijdig aan de lijn y = 4x + 10 en gaat door het punt (8, −4). Een formule bij m is y = 4x + b. Bereken b.",
      "antwoord": "-36",
      "uitleg": "−4 = 4 · 8 + b → −4 = 32 + b → b = −36."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij lijn k door de punten (−5, −6) en (6, −6)?",
      "uitleg": "De y-coördinaat is bij beide punten −6: de toename van y is 0, dus rc = 0. De lijn is horizontaal: y = −6.",
      "opties": [
        "y = −6",
        "y = −6x",
        "y = x − 6",
        "x = −6"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (4, 22) ligt op de lijn y = 3x + 8.",
      "antwoord": false,
      "uitleg": "Onwaar. Invullen van x = 4: y = 3 · 4 + 8 = 20. Dat is niet 22, dus het punt ligt niet op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de stijgende lijnen y = 2x − 2; y = 2/3x + 4; y = 0,5x + 9; y = 6x + 4. Welke lijn loopt het steilst?",
      "uitleg": "Hoe groter de richtingscoëfficiënt, hoe steiler de lijn. De grootste rc is 6. Het startgetal maakt voor de steilheid niet uit.",
      "opties": [
        "y = 2/3x + 4",
        "y = 0,5x + 9",
        "y = 2x − 2",
        "y = 6x + 4"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = 0,5x + 4 en y = −3 + 0,5x lopen evenwijdig.",
      "antwoord": true,
      "uitleg": "Waar. Evenwijdige lijnen hebben dezelfde richtingscoëfficiënt. Hier: 0,5 en 0,5, gelijk."
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (6, −42) en (13, −77)?",
      "uitleg": "a = (−77 − (−42)) / (13 − 6) = −5. Invullen van (6, −42) geeft −42 = −30 + b, dus b = −12. De formule is y = −5x − 12.",
      "opties": [
        "y = 5x − 12",
        "y = −5x + 12",
        "y = −5x − 42",
        "y = −5x − 12"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (3, −12) en loopt evenwijdig aan lijn l: y = 6x + 11. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = 6. Invullen van (3, −12): −12 = 6 · 3 + b = 18 + b, dus b = −30. Lijn m: y = 6x − 30.",
      "opties": [
        "y = 6x − 30",
        "y = 6x + 6",
        "y = −6x + 6",
        "y = 6x − 12"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(4, −14) en Q(12, −54). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-5",
      "uitleg": "rc = toename y / toename x = (−54 − (−14)) / (12 − 4) = −40 / 8 = −5."
    },
    {
      "type": "open",
      "vraag": "Stel een formule op bij de lijn door de punten A(3, 10) en B(9, 28). Schrijf je antwoord als y = ax + b.",
      "modelantwoord": "y = 3x + 1",
      "sleutelwoorden": [
        "3x/3x",
        "+ 1/+1"
      ],
      "minTreffers": 2,
      "uitleg": "rc = (28 − 10) / (9 − 3) = 3. Invullen van A: 10 = 9 + b, dus b = 1. Formule: y = 3x + 1."
    }
  ]
});
