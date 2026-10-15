/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 50 — Foutentraining §1.1–§1.5 (1/5, basis)
   Gericht op Duru's fouten in H1 §1.1–§1.5 (zie kop van het script); andere getallen dan eerdere toetsen.
   Gegenereerd met tools/gen_wiskunde_h1_foutentraining.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-40",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Proeftoets 50 — Foutentraining §1.1–§1.5 (1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "🎯",
  "duurMin": 40,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(6, −4) en Q(14, −8). Bereken de richtingscoëfficiënt van de lijn. Geef je antwoord als decimaal getal. Schrijf je antwoord met een komma, bijvoorbeeld 1,05.",
      "antwoord": "-0,5",
      "uitleg": "rc = toename y / toename x = (−8 − (−4)) / (14 − 6) = −4 / 8 = −0,5."
    },
    {
      "type": "invul",
      "vraag": "De lijn y = ax + b gaat door de punten (2, −1) en (10, 31). Bereken het startgetal b.",
      "antwoord": "-9",
      "uitleg": "Eerst a = 32 / 8 = 4. Invullen van (2, −1): −1 = 4 · 2 + b, dus −1 = 8 + b en b = −9."
    },
    {
      "type": "mc",
      "vraag": "Lijn l gaat door A(−3, −4) en B(5, 12). Een leerling rekent: a = (12 − (−4)) / (5 − 3) = 16 / 2 = 8. Wat is er fout?",
      "uitleg": "Min een negatief getal is plus: 5 − (−3) = 5 + 3 = 8. Dus a = 16 / 8 = 2. Let op: zet een negatieve coördinaat tussen haakjes.",
      "opties": [
        "In de teller moet −4 − 12 staan.",
        "In de noemer moet 5 − (−3) = 8 staan, dus a = 16 / 8 = 2.",
        "Je moet toename x delen door toename y, dus a = 8 / 16.",
        "Er is niets fout: de berekening klopt."
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Hoe heet het punt (0, 0), waar de x-as en de y-as elkaar snijden?",
      "uitleg": "Het punt (0, 0) heet de oorsprong. 'Snijpunt' is te algemeen: twee lijnen kunnen elkaar overal snijden.",
      "opties": [
        "het startgetal",
        "de oorsprong",
        "het nulpunt van de lijn",
        "het snijpunt met de x-as"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De lijnen y = 3x + 1 en y = 8x + 21 snijden elkaar. Je hebt al berekend dat x = −4. Bereken nu de y-coördinaat van het snijpunt.",
      "antwoord": "-11",
      "uitleg": "Vul x = −4 in bij een van de formules: y = 3 · (−4) + 1 = −11. Controle met de andere: 8 · (−4) + 21 = −11."
    },
    {
      "type": "mc",
      "vraag": "Bereken de coördinaten van het snijpunt van de lijnen y = 8x − 26 en y = −5x + 52. Tip: na x moet je y nog uitrekenen door x in een formule in te vullen.",
      "uitleg": "Gelijkstellen: 8x − 26 = −5x + 52 → x = 6. Dan x invullen in een formule: y = 8 · 6 − 26 = 22. Let op: y is níet hetzelfde als x! Snijpunt (6, 22).",
      "opties": [
        "(22, 6)",
        "(6, 6)",
        "(6, 22)",
        "(6, −30)"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De lijn y = 2 snijdt lijn p uit de figuur. Bereken de x-coördinaat van het snijpunt.",
      "antwoord": "-2",
      "uitleg": "Lijn p: y = −2x − 2. Gelijkstellen: −2x − 2 = 2 → −2x = 4 → x = −2.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 340\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"284\" height=\"340\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c5\"><rect x=\"30.0\" y=\"30.0\" width=\"224.0\" height=\"280.0\"/></clipPath></defs><line x1=\"30.0\" y1=\"310.0\" x2=\"30.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"86.0\" y1=\"310.0\" x2=\"86.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"114.0\" y1=\"310.0\" x2=\"114.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"310.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"310.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"198.0\" y1=\"310.0\" x2=\"198.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"226.0\" y1=\"310.0\" x2=\"226.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"254.0\" y1=\"310.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"310.0\" x2=\"254.0\" y2=\"310.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"282.0\" x2=\"254.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"254.0\" x2=\"254.0\" y2=\"254.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"226.0\" x2=\"254.0\" y2=\"226.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"170.0\" x2=\"254.0\" y2=\"170.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"142.0\" x2=\"254.0\" y2=\"142.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"114.0\" x2=\"254.0\" y2=\"114.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"86.0\" x2=\"254.0\" y2=\"86.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"58.0\" x2=\"254.0\" y2=\"58.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"30.0\" x2=\"254.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"30.0\" y1=\"198.0\" x2=\"254.0\" y2=\"198.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"58.0\" y1=\"310.0\" x2=\"58.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"30.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"86.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"114.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"198.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"226.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"254.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"53.0\" y=\"314.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"53.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">−3</text><text x=\"53.0\" y=\"258.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"53.0\" y=\"230.0\" fill=\"#333\" text-anchor=\"end\">−1</text><text x=\"53.0\" y=\"174.0\" fill=\"#333\" text-anchor=\"end\">1</text><text x=\"53.0\" y=\"146.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"53.0\" y=\"118.0\" fill=\"#333\" text-anchor=\"end\">3</text><text x=\"53.0\" y=\"90.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"53.0\" y=\"62.0\" fill=\"#333\" text-anchor=\"end\">5</text><text x=\"53.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"53.0\" y=\"213.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"260.0\" y=\"202.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"54.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c5)\" x1=\"2.0\" y1=\"142.0\" x2=\"282.0\" y2=\"702.0\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"75.2\" y=\"268.4\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">p</text><circle cx=\"30.0\" cy=\"198.0\" r=\"3.5\" fill=\"#222\"/><text x=\"36.0\" y=\"192.0\" fill=\"#222\" font-size=\"11\">(−1, 0)</text><circle cx=\"86.0\" cy=\"310.0\" r=\"3.5\" fill=\"#222\"/><text x=\"92.0\" y=\"304.0\" fill=\"#222\" font-size=\"11\">(1, −4)</text></svg>"
    },
    {
      "type": "open",
      "vraag": "Beschrijf de stappen waarmee je het snijpunt van y = 6x + 12 en y = 3x + 9 berekent, en geef de coördinaten. Tip: wat weet je over y in het snijpunt? Vind eerst x, daarna y.",
      "modelantwoord": "Formules gelijkstellen: 6x + 12 = 3x + 9. Vergelijking oplossen: x = −1. Invullen in een van de formules: y = 6. Snijpunt (−1, 6).",
      "sleutelwoorden": [
        "gelijk",
        "vergelijking/oplossen/los",
        "invullen/invul/vul"
      ],
      "minTreffers": 2,
      "uitleg": "Gelijkstellen → x = −1 → invullen → y = 6. Het snijpunt is (−1, 6)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 8 − 2p substitueert in h = 5t + 5, krijg je h = −10p + 45.",
      "antwoord": true,
      "uitleg": "Waar. h = 5(8 − 2p) + 5 = 40 − 10p + 5, dus h = −10p + 45. Zonder haakjes vergeet je 2p met 5 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Substitueer t = 7p + 32 in h = 3t − 8. Je krijgt h = …p + 88. Welk getal staat er vóór p?",
      "antwoord": "21",
      "uitleg": "h = 3(7p + 32) − 8. Vóór p: 3 · 7 = 21."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn A: k = 2t − 16 en B: t = 3p + 13. Een leerling substitueert B in A en krijgt k = 6p − 3. Wat is er fout gegaan?",
      "uitleg": "k = 2(3p + 13) − 16 = 6p + 26 − 16, dus k = 6p + 10. Alles binnen de haakjes wordt met 2 vermenigvuldigd, ook het losse getal.",
      "opties": [
        "2 · 3 is niet 6; het moet 5 zijn.",
        "Er is niets fout gegaan.",
        "Haakjes vergeten: 2 moet ook met 13 vermenigvuldigd worden, dus k = 6p + 10.",
        "Bij het vereenvoudigen: 13 + (−16) is niet −3."
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules A: k = 6t + 28 en B: t = 19 + 7p. Substitueer formule B in formule A en vereenvoudig het resultaat.",
      "uitleg": "k = 6(7p + 19) + 28 = 42p + 114 + 28, dus k = 42p + 142. Let op de haakjes: alles binnen de haakjes wordt met 6 vermenigvuldigd.",
      "opties": [
        "k = 42p + 142",
        "k = 13p + 47",
        "k = 42p + 47",
        "k = 42p + 86"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 25% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 25%: je houdt 75% over, dus groeifactor 0,75.",
      "opties": [
        "0,75",
        "1,25",
        "2,5",
        "0,25"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal volgers van een account neemt per dag met 6% af. De waarde van één dag eerder bereken je door de huidige waarde te vermenigvuldigen met 1,06.",
      "antwoord": false,
      "uitleg": "Onwaar. Afname 6% → groeifactor 0,94. Terug in de tijd deel je door 0,94. Vermenigvuldigen met 1,06 is iets anders: dat geeft een te klein antwoord."
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 2048, 2560, 3200, 4000 bij een exponentieel verband hoort. Leg uit hoe je dat controleert. Tip: met welk getal vermenigvuldig je van de ene waarde naar de volgende?",
      "modelantwoord": "Bereken telkens de factor: 2560 : 2048 = 1,25, 3200 : 2560 = 1,25 … De factor is steeds gelijk (1,25), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 1,25."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,1 per half uur. Bereken de groeifactor per uur. Tip: twee stappen = twee keer vermenigvuldigen met de groeifactor. Schrijf je antwoord met een komma, bijvoorbeeld 1,05.",
      "antwoord": "1,21",
      "uitleg": "Per uur zijn er twee stappen: 1,1 · 1,1 = 1,1² = 1,21. Niet 2 · de groeifactor: elke stap vermenigvuldig je opnieuw.",
      "tolerantie": 0.0005
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,3 per uur. Dan is de groeifactor per twee uur gelijk aan 2,6.",
      "antwoord": false,
      "uitleg": "Onwaar. Twee stappen = twee keer vermenigvuldigen: 1,3 · 1,3 = 1,3² = 1,69. Niet 2 · 1,3 = 2,6: je vermenigvuldigt mét de factor, je telt hem niet op."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,05 per maand. Nu is de hoeveelheid 2000. Hoe groot was de hoeveelheid 5 maanden eerder? Rond af op een geheel getal. Tip: terugrekenen in de tijd = delen.",
      "antwoord": "1567",
      "uitleg": "Groeifactor per 5 maanden: 1,05⁵. Terugrekenen = delen: 2000 : 1,05⁵ ≈ 1567.",
      "tolerantie": 1
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 20 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 2 jaar waard? Rond af op twee decimalen. Schrijf je antwoord met een komma, bijvoorbeeld 1,05.",
      "antwoord": "36,17",
      "uitleg": "Na 2 jaar is t = 24: W = 20 · 1,025²⁴ ≈ 36,17 dollar. Let op: t is in maanden, dus jaren eerst omrekenen (1 jaar = 12 maanden).",
      "tolerantie": 0.02
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,9ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen. Schrijf je antwoord met een komma, bijvoorbeeld 1,05.",
      "antwoord": "0,53",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 0,9⁶ ≈ 0,5314 ≈ 0,53.",
      "tolerantie": 0.006
    }
  ]
});
