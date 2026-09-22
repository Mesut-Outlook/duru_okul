/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 11 — §1.1 Lineaire formules opstellen
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.1–1.2 (met aantekeningen docent)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-1",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Proeftoets 11 — §1.1 Lineaire formules opstellen",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = 4 − 2/3x. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "opties": [
        "richtingscoëfficiënt 4 en startgetal −2/3",
        "richtingscoëfficiënt 2/3 en startgetal 4",
        "richtingscoëfficiënt −2/3 en startgetal −4",
        "richtingscoëfficiënt −2/3 en startgetal 4"
      ],
      "antwoord": 3,
      "uitleg": "Schrijf de formule in de vorm y = ax + b: y = −2/3x + 4. Het getal vóór x (met het minteken!) is de richtingscoëfficiënt: −2/3. Het losse getal is het startgetal: 4. De volgorde in de formule maakt niet uit."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = −x + 7. Hoe groot is de richtingscoëfficiënt? Vul in: a = ____",
      "antwoord": "-1|−1",
      "uitleg": "−x betekent −1 · x. De richtingscoëfficiënt is dus −1 (en het startgetal is 7)."
    },
    {
      "type": "mc",
      "vraag": "Welke uitspraak over de lijn bij de formule y = 0,4x − 6 is juist?",
      "opties": [
        "De lijn is stijgend en snijdt de y-as in (0, −6).",
        "De lijn is dalend en snijdt de y-as in (0, −6).",
        "De lijn is stijgend en snijdt de y-as in (0, 6).",
        "De lijn is dalend en snijdt de y-as in (0, 0,4)."
      ],
      "antwoord": 0,
      "uitleg": "De richtingscoëfficiënt 0,4 is positief, dus de lijn is stijgend. Het startgetal −6 is de y-coördinaat van het snijpunt met de y-as: (0, −6)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijn bij de formule y = 5 − 3x is een stijgende lijn, want het getal 5 is positief.",
      "antwoord": false,
      "uitleg": "Onwaar. Of een lijn stijgt of daalt hangt af van de richtingscoëfficiënt, niet van het startgetal. Hier is de richtingscoëfficiënt −3 (negatief), dus de lijn is dalend."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je lijn k. De zwarte stippen liggen op roosterpunten. Hoe groot is de richtingscoëfficiënt van lijn k?",
      "opties": [
        "2/3",
        "−3/2",
        "3/2",
        "3"
      ],
      "antwoord": 2,
      "uitleg": "Maak een trapje tussen (0, −2) en (2, 1): 2 naar rechts en 3 omhoog. Richtingscoëfficiënt = toename y / toename x = 3 / 2 = 1,5. Omhoog = positief.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 220 276\" width=\"220\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"220\" height=\"276\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"c-151\"><rect x=\"26\" y=\"26\" width=\"168\" height=\"224\"/></clipPath></defs><line x1=\"26\" y1=\"250\" x2=\"26\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"54\" y1=\"250\" x2=\"54\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"82\" y1=\"250\" x2=\"82\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"110\" y1=\"250\" x2=\"110\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"138\" y1=\"250\" x2=\"138\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"166\" y1=\"250\" x2=\"166\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"194\" y1=\"250\" x2=\"194\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"250\" x2=\"194\" y2=\"250\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"222\" x2=\"194\" y2=\"222\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"194\" x2=\"194\" y2=\"194\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"166\" x2=\"194\" y2=\"166\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"138\" x2=\"194\" y2=\"138\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"110\" x2=\"194\" y2=\"110\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"82\" x2=\"194\" y2=\"82\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"54\" x2=\"194\" y2=\"54\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"26\" x2=\"194\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"166\" x2=\"194\" y2=\"166\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"54\" y1=\"250\" x2=\"54\" y2=\"26\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"200\" y=\"170\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"50\" y=\"18\" fill=\"#222\" font-style=\"italic\">y</text><text x=\"26\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"82\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"110\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"138\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"166\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"194\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"49\" y=\"254\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"49\" y=\"226\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"49\" y=\"198\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"49\" y=\"142\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"49\" y=\"114\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"49\" y=\"86\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"49\" y=\"58\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"49\" y=\"30\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"50\" y=\"180\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><line clip-path=\"url(#c-151)\" x1=\"26\" y1=\"264\" x2=\"194\" y2=\"12\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"144\" y=\"90\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">k</text><circle cx=\"54\" cy=\"222\" r=\"3.5\" fill=\"#222\"/><circle cx=\"110\" cy=\"138\" r=\"3.5\" fill=\"#222\"/><circle cx=\"166\" cy=\"54\" r=\"3.5\" fill=\"#222\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij lijn l in de figuur? (De stippen liggen op roosterpunten.)",
      "opties": [
        "y = 1/2x + 4",
        "y = −1/2x + 4",
        "y = −2x + 4",
        "y = 4x − 1/2"
      ],
      "antwoord": 1,
      "uitleg": "Lijn l snijdt de y-as in (0, 4), dus b = 4. Van (0, 4) naar (6, 1): 6 naar rechts en 3 omlaag. a = −3 / 6 = −1/2. De lijn daalt, dus a is negatief: y = −1/2x + 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 276 220\" width=\"276\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"276\" height=\"220\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"c-151\"><rect x=\"26\" y=\"26\" width=\"224\" height=\"168\"/></clipPath></defs><line x1=\"26\" y1=\"194\" x2=\"26\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"54\" y1=\"194\" x2=\"54\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"82\" y1=\"194\" x2=\"82\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"110\" y1=\"194\" x2=\"110\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"138\" y1=\"194\" x2=\"138\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"166\" y1=\"194\" x2=\"166\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"194\" y1=\"194\" x2=\"194\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"222\" y1=\"194\" x2=\"222\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"250\" y1=\"194\" x2=\"250\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"194\" x2=\"250\" y2=\"194\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"166\" x2=\"250\" y2=\"166\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"138\" x2=\"250\" y2=\"138\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"110\" x2=\"250\" y2=\"110\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"82\" x2=\"250\" y2=\"82\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"54\" x2=\"250\" y2=\"54\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"26\" x2=\"250\" y2=\"26\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"26\" y1=\"166\" x2=\"250\" y2=\"166\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"54\" y1=\"194\" x2=\"54\" y2=\"26\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"256\" y=\"170\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"50\" y=\"18\" fill=\"#222\" font-style=\"italic\">y</text><text x=\"26\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"82\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"110\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"138\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"166\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"194\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"222\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"250\" y=\"181\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"49\" y=\"198\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"49\" y=\"142\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"49\" y=\"114\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"49\" y=\"86\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"49\" y=\"58\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"49\" y=\"30\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"50\" y=\"180\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><line clip-path=\"url(#c-151)\" x1=\"26\" y1=\"40\" x2=\"250\" y2=\"152\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"228\" y=\"132\" fill=\"#0d9488\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">l</text><circle cx=\"54\" cy=\"54\" r=\"3.5\" fill=\"#222\"/><circle cx=\"222\" cy=\"138\" r=\"3.5\" fill=\"#222\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten A(2, 5) en B(6, 17). Bereken de richtingscoëfficiënt. a = ____",
      "antwoord": "3",
      "uitleg": "a = toename tweede coördinaat / toename eerste coördinaat = (17 − 5) / (6 − 2) = 12 / 4 = 3."
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(−3, 8) en Q(1, −4). Bereken de richtingscoëfficiënt. a = ____",
      "antwoord": "−3|-3",
      "uitleg": "a = (−4 − 8) / (1 − (−3)) = −12 / 4 = −3. Let op: 1 − (−3) = 1 + 3 = 4."
    },
    {
      "type": "mc",
      "vraag": "Lijn l gaat door X(−1, 3) en Y(3, 11). Een leerling rekent: a = (11 − 3) / (3 − 1) = 8 / 2 = 4. Wat is er fout?",
      "opties": [
        "De teller moet 3 − 11 zijn, dus a = −4.",
        "Je moet toename x delen door toename y, dus a = 2 / 8.",
        "Er is niets fout: a = 4.",
        "In de noemer moet 3 − (−1) = 4 staan, dus a = 8 / 4 = 2."
      ],
      "antwoord": 3,
      "uitleg": "De eerste coördinaat van X is −1. Toename x = 3 − (−1) = 3 + 1 = 4. Dus a = 8 / 4 = 2. Een formule bij l is y = 2x + 5."
    },
    {
      "type": "invul",
      "vraag": "Een lijn heeft richtingscoëfficiënt −3 en gaat door het punt (4, −5). De formule is dus van de vorm y = −3x + b. Bereken b. b = ____",
      "antwoord": "7",
      "uitleg": "Vul x = 4 en y = −5 in: −5 = −3 × 4 + b, dus −5 = −12 + b. Dan is b = −5 + 12 = 7. Formule: y = −3x + 7."
    },
    {
      "type": "mc",
      "vraag": "Stel een formule op van de lijn door de punten (5, 20) en (9, 32).",
      "opties": [
        "y = 3x + 20",
        "y = 5x + 3",
        "y = 3x + 5",
        "y = 12x − 40"
      ],
      "antwoord": 2,
      "uitleg": "a = (32 − 20) / (9 − 5) = 12 / 4 = 3. Vul (5, 20) in bij y = 3x + b: 20 = 15 + b, dus b = 5. Formule: y = 3x + 5."
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten (0, −6) en (3, 6). Wat is het startgetal? b = ____",
      "antwoord": "−6|-6",
      "uitleg": "Het punt (0, −6) ligt op de y-as (x = 0). Daar snijdt de lijn de y-as, dus b = −6. (Controle: a = 12 / 3 = 4, y = 4x − 6.)"
    },
    {
      "type": "open",
      "vraag": "Een lijn gaat door de punten (0, −6) en (3, 6). Leg uit waarom je bij deze lijn niets hoeft in te vullen om b te vinden.",
      "sleutelwoorden": [
        "y-as/y as/x = 0/x=0/x is 0/x is nul/x-coördinaat 0/eerste coördinaat 0/eerste coördinaat is 0",
        "snijpunt/snijdt/snijden/begint/startgetal"
      ],
      "minTreffers": 1,
      "modelantwoord": "Het punt (0, −6) ligt op de y-as, want x = 0. Daar snijdt de lijn de y-as, dus het startgetal is meteen −6.",
      "uitleg": "Bij x = 0 geldt y = a · 0 + b = b. Een punt met eerste coördinaat 0 ligt op de y-as en geeft dus direct het startgetal."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (−9, 8) ligt op de lijn bij de formule y = 5 − 1/3x.",
      "antwoord": true,
      "uitleg": "Waar. Vul x = −9 in: y = 5 − 1/3 × (−9) = 5 + 3 = 8. Dat is precies de y-coördinaat van het punt, dus het punt ligt op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Welke van deze lijnen loopt het steilst omhoog?",
      "opties": [
        "y = 2x − 1",
        "y = 0,5x + 9",
        "y = 1,5x + 4",
        "y = −3x + 2"
      ],
      "antwoord": 0,
      "uitleg": "Een lijn loopt omhoog als de richtingscoëfficiënt positief is. Hoe groter de richtingscoëfficiënt, hoe steiler. Van 0,5, 1,5 en 2 is 2 het grootst. y = −3x + 2 is wel steil, maar dalend."
    },
    {
      "type": "mc",
      "vraag": "Lijn m loopt evenwijdig aan de lijn y = 3x + 7 en gaat door het punt (2, −1). Welke formule hoort bij lijn m?",
      "opties": [
        "y = 3x + 5",
        "y = 3x − 7",
        "y = 3x + 7",
        "y = −3x + 5"
      ],
      "antwoord": 1,
      "uitleg": "Evenwijdig betekent: dezelfde richtingscoëfficiënt, dus a = 3 en y = 3x + b. Vul (2, −1) in: −1 = 6 + b, dus b = −7. Lijn m: y = 3x − 7."
    },
    {
      "type": "invul",
      "vraag": "Lijn m loopt evenwijdig aan de lijn y = 1/2x + 5 en gaat door het punt (−4, −8). Bereken het startgetal van lijn m. b = ____",
      "antwoord": "−6|-6",
      "uitleg": "Evenwijdig, dus a = 1/2: y = 1/2x + b. Vul (−4, −8) in: −8 = 1/2 × (−4) + b = −2 + b, dus b = −6. Lijn m: y = 1/2x − 6."
    },
    {
      "type": "waaronwaar",
      "vraag": "Twee lijnen die evenwijdig lopen, hebben altijd hetzelfde startgetal.",
      "antwoord": false,
      "uitleg": "Onwaar. Evenwijdige lijnen hebben dezelfde richtingscoëfficiënt. Het startgetal is juist verschillend (anders zouden het dezelfde lijnen zijn)."
    },
    {
      "type": "mc",
      "vraag": "Stel een formule op van de lijn door de punten (−3, 5) en (8, 5).",
      "opties": [
        "x = 5",
        "y = 5x",
        "y = 5",
        "y = x + 5"
      ],
      "antwoord": 2,
      "uitleg": "a = (5 − 5) / (8 − (−3)) = 0 / 11 = 0. De formule wordt y = 0 · x + b = b. Beide punten hebben y = 5, dus y = 5: een horizontale lijn."
    },
    {
      "type": "mc",
      "vraag": "Bij een lineair verband hoort deze tabel:<br><table style=\"border-collapse:collapse;margin-top:6px\"><tr><td style=\"border:1px solid #999;padding:3px 10px\"><i>x</i></td><td style=\"border:1px solid #999;padding:3px 10px\">2</td><td style=\"border:1px solid #999;padding:3px 10px\">5</td><td style=\"border:1px solid #999;padding:3px 10px\">8</td><td style=\"border:1px solid #999;padding:3px 10px\">11</td></tr><tr><td style=\"border:1px solid #999;padding:3px 10px\"><i>y</i></td><td style=\"border:1px solid #999;padding:3px 10px\">23</td><td style=\"border:1px solid #999;padding:3px 10px\">14</td><td style=\"border:1px solid #999;padding:3px 10px\">5</td><td style=\"border:1px solid #999;padding:3px 10px\">−4</td></tr></table>Welke formule hoort bij de tabel?",
      "opties": [
        "y = 3x + 17",
        "y = −3x + 29",
        "y = −3x + 23",
        "y = −9x + 41"
      ],
      "antwoord": 1,
      "uitleg": "Neem twee kolommen, bijv. (2, 23) en (5, 14): a = (14 − 23) / (5 − 2) = −9 / 3 = −3. Vul (2, 23) in: 23 = −6 + b, dus b = 29. Controle met (11, −4): −33 + 29 = −4, klopt."
    }
  ]
});
