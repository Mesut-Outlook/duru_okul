/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 54 — Foutentraining §1.1–§1.5 (5/5, eindniveau)
   Gericht op Duru's fouten in H1 §1.1–§1.5 (zie kop van het script); andere getallen dan eerdere toetsen.
   Gegenereerd met tools/gen_wiskunde_h1_foutentraining.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-44",
  "hoofdstuk": 1,
  "paragraaf": "mix",
  "titel": "Proeftoets 54 — Foutentraining §1.1–§1.5 (5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "🎯",
  "duurMin": 40,
  "vragen": [
    {
      "type": "open",
      "vraag": "Stel een formule op bij de lijn door de punten A(−5, 6) en B(−3, 0). Schrijf je antwoord als y = ax + b.",
      "modelantwoord": "y = −3x − 9",
      "sleutelwoorden": [
        "-3x/−3x",
        "- 9/-9/− 9"
      ],
      "minTreffers": 2,
      "uitleg": "rc = (0 − 6) / (−3 − (−5)) = −3. Invullen van A: 6 = 15 + b, dus b = −9. Formule: y = −3x − 9."
    },
    {
      "type": "invul",
      "vraag": "De lijn y = ax + b gaat door de punten (4, 7) en (6, 10). Bereken het startgetal b.",
      "antwoord": "1",
      "uitleg": "Eerst a = 3 / 2 = 1,5. Invullen van (4, 7): 7 = 1,5 · 4 + b, dus 7 = 6 + b en b = 1."
    },
    {
      "type": "mc",
      "vraag": "Lijn l gaat door A(−3, 5) en B(6, −22). Een leerling rekent: a = (−22 − 5) / (6 − 3) = −27 / 3 = −9. Wat is er fout?",
      "uitleg": "Min een negatief getal is plus: 6 − (−3) = 6 + 3 = 9. Dus a = −27 / 9 = −3. Let op: zet een negatieve coördinaat tussen haakjes.",
      "opties": [
        "Er is niets fout: de berekening klopt.",
        "Je moet toename x delen door toename y, dus a = 9 / −27.",
        "In de noemer moet 6 − (−3) = 9 staan, dus a = −27 / 9 = −3.",
        "In de teller moet 5 − (−22) staan."
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Lijn k: y = 5x − 1 en lijn m: y = 2x + 6. Welke lijn loopt het steilst omhoog, en waarom?",
      "uitleg": "Hoe groter de rc, hoe steiler de lijn omhoog loopt: 5 > 2, dus lijn k. Het startgetal zegt alleen waar de lijn de y-as snijdt, niet hoe steil hij is.",
      "opties": [
        "lijn m, want die snijdt de y-as hoger",
        "lijn k, want de richtingscoëfficiënt is groter (5 tegen 2)",
        "lijn m, want het startgetal is groter (6 tegen −1)",
        "ze zijn even steil, want het zijn allebei rechte lijnen"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Lijn p gaat door (0, 2) en lijn q door (0, 7). De lijnen snijden elkaar buiten de figuur. Stel bij beide lijnen een formule op en bereken de coördinaten van het snijpunt.",
      "uitleg": "Lijn p: y = 0,5x + 2. Lijn q: y = 7. Gelijkstellen: 0,5x + 2 = 7 geeft x = 10 en y = 7.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 304 268\" width=\"304\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"304\" height=\"268\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c38\"><rect x=\"40.0\" y=\"30.0\" width=\"234.0\" height=\"208.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"238.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"66.0\" y1=\"238.0\" x2=\"66.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"92.0\" y1=\"238.0\" x2=\"92.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"118.0\" y1=\"238.0\" x2=\"118.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"144.0\" y1=\"238.0\" x2=\"144.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"170.0\" y1=\"238.0\" x2=\"170.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"196.0\" y1=\"238.0\" x2=\"196.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"222.0\" y1=\"238.0\" x2=\"222.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"248.0\" y1=\"238.0\" x2=\"248.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"274.0\" y1=\"238.0\" x2=\"274.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"238.0\" x2=\"274.0\" y2=\"238.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"212.0\" x2=\"274.0\" y2=\"212.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"186.0\" x2=\"274.0\" y2=\"186.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"160.0\" x2=\"274.0\" y2=\"160.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"134.0\" x2=\"274.0\" y2=\"134.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"108.0\" x2=\"274.0\" y2=\"108.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"82.0\" x2=\"274.0\" y2=\"82.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"56.0\" x2=\"274.0\" y2=\"56.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"274.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"212.0\" x2=\"274.0\" y2=\"212.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"66.0\" y1=\"238.0\" x2=\"66.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"92.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"118.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"144.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"170.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"196.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"222.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"248.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">7</text><text x=\"274.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"middle\">8</text><text x=\"61.0\" y=\"242.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"61.0\" y=\"190.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"61.0\" y=\"164.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"61.0\" y=\"138.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"61.0\" y=\"112.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"61.0\" y=\"86.0\" fill=\"#333\" text-anchor=\"end\">10</text><text x=\"61.0\" y=\"60.0\" fill=\"#333\" text-anchor=\"end\">12</text><text x=\"61.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">14</text><text x=\"61.0\" y=\"227.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"280.0\" y=\"216.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"62.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><line clip-path=\"url(#w1c38)\" x1=\"14.0\" y1=\"199.0\" x2=\"300.0\" y2=\"127.5\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"264.4\" y=\"129.9\" fill=\"#c2185b\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">p</text><line clip-path=\"url(#w1c38)\" x1=\"14.0\" y1=\"121.0\" x2=\"300.0\" y2=\"121.0\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"264.4\" y=\"113.0\" fill=\"#0d9488\" font-weight=\"bold\" font-style=\"italic\" font-size=\"14\">q</text><circle cx=\"66.0\" cy=\"186.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"274.0\" cy=\"134.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"66.0\" cy=\"121.0\" r=\"3.5\" fill=\"#222\"/><circle cx=\"274.0\" cy=\"121.0\" r=\"3.5\" fill=\"#222\"/></svg>",
      "opties": [
        "(12, 8)",
        "(10, 7)",
        "(10, 0)",
        "(7, 10)"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van het snijpunt van de lijnen y = −4x + 64 en y = 12x − 128.",
      "antwoord": "16",
      "uitleg": "−4x + 64 = 12x − 128 geeft x = 12. Invullen: y = −4 · 12 + 64 = 16. Controle in de andere formule: 16."
    },
    {
      "type": "open",
      "vraag": "Beschrijf de stappen waarmee je het snijpunt van y = 4x + 22 en y = −5x + 13 berekent, en geef de coördinaten.",
      "modelantwoord": "Formules gelijkstellen: 4x + 22 = −5x + 13. Vergelijking oplossen: x = −1. Invullen in een van de formules: y = 18. Snijpunt (−1, 18).",
      "sleutelwoorden": [
        "gelijk",
        "vergelijking/oplossen/los",
        "invullen/invul/vul"
      ],
      "minTreffers": 2,
      "uitleg": "Gelijkstellen → x = −1 → invullen → y = 18. Het snijpunt is (−1, 18)."
    },
    {
      "type": "mc",
      "vraag": "Bereken de coördinaten van het snijpunt van de lijnen y = x − 16 en y = 9x − 24.",
      "uitleg": "Gelijkstellen: x − 16 = 9x − 24 → x = 1. Dan x invullen in een formule: y = 1 · 1 − 16 = −15. Let op: y is níet hetzelfde als x! Snijpunt (1, −15).",
      "opties": [
        "(−15, 1)",
        "(1, 9)",
        "(1, −15)",
        "(1, 1)"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Substitueer formule B in formule A en vereenvoudig het resultaat. A: d = 6z + 32   B: z = 7h + 1",
      "modelantwoord": "d = 42h + 38",
      "sleutelwoorden": [
        "42h/42h",
        "+ 38/+38"
      ],
      "minTreffers": 2,
      "uitleg": "d = 6(7h + 1) + 32 = 42h + 38."
    },
    {
      "type": "invul",
      "vraag": "Substitueer z = 2h + 19 in d = 3z − 1. Je krijgt d = …h + 56. Welk getal staat er vóór h?",
      "antwoord": "6",
      "uitleg": "d = 3(2h + 19) − 1. Vóór h: 3 · 2 = 6."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn A: w = −3s + 32 en B: s = 7r + 4. Een leerling substitueert B in A en krijgt w = −21r + 36. Wat is er fout gegaan?",
      "uitleg": "w = −3(7r + 4) + 32 = −21r − 12 + 32, dus w = −21r + 20. Alles binnen de haakjes wordt met −3 vermenigvuldigd, ook het losse getal.",
      "opties": [
        "−3 · 7 is niet −21; het moet 4 zijn.",
        "Bij het vereenvoudigen: 4 + 32 is niet 36.",
        "Er is niets fout gegaan.",
        "Haakjes vergeten: −3 moet ook met 4 vermenigvuldigd worden, dus w = −21r + 20."
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 3 − 5p substitueert in h = 3t + 1, krijg je h = −5p + 10.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 3(3 − 5p) + 1 = 9 − 15p + 1, dus h = −15p + 10. Zonder haakjes vergeet je 5p met 3 te vermenigvuldigen."
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 20% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 20%: je houdt 80% over, dus groeifactor 0,8.",
      "opties": [
        "0,2",
        "1,2",
        "2",
        "0,8"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 1,2 per uur. Om 04.00 uur zijn er 1500 muggen. Hoeveel muggen waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "1250",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 1500 : 1,2 ≈ 1250,0 → 1250 muggen. Let op: niet vermenigvuldigen met de groeifactor — dan reken je vooruit in plaats van terug.",
      "tolerantie": 1
    },
    {
      "type": "open",
      "vraag": "Ga na of de tabel t = 0, 1, 2, 3 met de waarden 1024, 2048, 4096, 8192 bij een exponentieel verband hoort. Leg uit hoe je dat controleert.",
      "modelantwoord": "Bereken telkens de factor: 2048 : 1024 = 2, 4096 : 2048 = 2 … De factor is steeds gelijk (2), dus het verband is exponentieel.",
      "sleutelwoorden": [
        "factor/delen/deel/gedeeld",
        "gelijk/hetzelfde/zelfde/steeds"
      ],
      "minTreffers": 2,
      "uitleg": "Deel steeds een waarde door de vorige. Is die factor (ongeveer) gelijk, dan is het exponentieel. Hier steeds 2."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,8 per halfjaar. Bereken de groeifactor per jaar.",
      "antwoord": "0,64",
      "uitleg": "Per jaar zijn er twee stappen: 0,8 · 0,8 = 0,8² = 0,64. Niet 2 · de groeifactor: elke stap vermenigvuldig je opnieuw.",
      "tolerantie": 0.0005
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,7 per jaar. Dan is de groeifactor per twee jaar gelijk aan 1,4.",
      "antwoord": false,
      "uitleg": "Onwaar. Twee stappen = twee keer vermenigvuldigen: 0,7 · 0,7 = 0,7² = 0,49. Niet 2 · 0,7 = 1,4: je vermenigvuldigt mét de factor, je telt hem niet op."
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 200 · 1,06ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 200 · 1,19ᵗ",
      "sleutelwoorden": [
        "1,19/1.19"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,06³ ≈ 1,19. De beginwaarde blijft 200: A = 200 · 1,19ᵗ."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,95 per uur. Nu is de hoeveelheid 15.000. Hoe groot was de hoeveelheid 3 uur eerder? Rond af op een geheel getal.",
      "antwoord": "17495",
      "uitleg": "Groeifactor per 3 uur: 0,95³. Terugrekenen = delen: 15.000 : 0,95³ ≈ 17495.",
      "tolerantie": 8
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 20 · 1,019ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "39,38",
      "uitleg": "Na 3 jaar is t = 36: W = 20 · 1,019³⁶ ≈ 39,38 dollar. Let op: t is in maanden, dus jaren eerst omrekenen (1 jaar = 12 maanden).",
      "tolerantie": 0.02
    }
  ]
});
