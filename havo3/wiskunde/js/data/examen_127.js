/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 127 — Gemengd H1 + H2 (4/5)
   Bron: Noordhoff H1 §1.1–§1.5 + H2 §2.1–§2.5 (2 vragen per paragraaf, andere getallen)
   Gegenereerd met tools/gen_wiskunde_h1_h2_gemengd.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1h2-gemengd-4",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 127 — Gemengd H1 + H2 (4/5)",
  "vak": "Wiskunde · H1 Lineair & exponentieel + H2 Parabolen",
  "icoon": "🔀",
  "duurMin": 40,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3x² − 6x + 2?",
      "uitleg": "1 Uit x = 0 volgt y = 2. 2 3x² − 6x + 2 = 2 → 3x² − 6x = 0 → x(3x − 6) = 0 → x = 0 of x = 2. 3 De x-coördinaat van de top ligt midden tussen 0 en 2: x = 1. 4 y = 3·1² − 6 · 1 + 2 = −1. 5 De top is (1, −1).",
      "opties": [
        "(−1, −1)",
        "(1, 2)",
        "(1, 11)",
        "(1, −1)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = 0,25x + 2. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = 0,25x + 2. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: 0,25. Het losse getal is het startgetal: 2.",
      "opties": [
        "richtingscoëfficiënt 2 en startgetal 0,25",
        "richtingscoëfficiënt −0,25 en startgetal 2",
        "richtingscoëfficiënt 0,25 en startgetal −2",
        "richtingscoëfficiënt 0,25 en startgetal 2"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = −4x − 8 en y = 4x − 8 hebben geen snijpunt.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc's zijn verschillend (−4 en 4), dus de lijnen snijden elkaar wel: in (0, −8), want ze hebben hetzelfde startgetal."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (2x + 1)² − 13x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-9",
      "uitleg": "(2x + 1)² = (2x + 1)(2x + 1) = 4x² + 4x + 1. Samen met −13x²: y = −9x² + 4x + 1. Het getal voor x² is −9, dus de grafiek is een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "De lijnen y = −2x + 22 en y = 7x − 68 snijden elkaar in S. Met welke vergelijking bereken je de x-coördinaat van S?",
      "uitleg": "Op het snijpunt hebben beide lijnen dezelfde y. Stel daarom de twee formules aan elkaar gelijk.",
      "opties": [
        "−2x + 22 = 7x − 68",
        "−2x + 22 = 0",
        "−2x − 68 = 7x + 22",
        "−2x + 22 = −(7x − 68)"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 6% af. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Afname van 6%: je houdt 94% over, dus groeifactor 0,94.",
      "opties": [
        "0,06",
        "0,6",
        "0,94",
        "1,06"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 1,12ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 1,12 = 112%, dus toename van 12% per maand.",
      "opties": [
        "−12% per maand",
        "+1,2% per maand",
        "+120% per maand",
        "+12% per maand"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = 3x² + 9 ligt op de y-as.",
      "antwoord": true,
      "uitleg": "Waar. Top op de y-as ⇔ b = 0 (geen term met x). Hier is b = 0."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (−8, 5) ligt op de lijn y = −0,5x + 1.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = −8: y = −0,5 · (−8) + 1 = 5. Dat is gelijk aan 5, dus het punt ligt op de lijn."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −2x² − 8x − 12. Vul in: x = …",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = −12. 2 −2x² − 8x − 12 = −12 → −2x² − 8x = 0 → x(−2x − 8) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −2·(−2)² − 8 · (−2) − 12 = −4. 5 De top is (−2, −4). De symmetrieas is de verticale lijn door de top: x = −2."
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = 3(x − 6)² − 14 in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-36",
      "uitleg": "(x − 6)² = x² − 12x + 36; keer 3 → 3x² − 36x + 108; − 14 → y = 3x² − 36x + 94. Dus b = −36."
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een zwembad vanaf 2020. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,04",
      "uitleg": "8320 : 8000 ≈ 1,04; ook 8653 : 8320 ≈ 1,04. De groeifactor is 1,04.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 268 62\" width=\"268\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"266\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"117\" y1=\"1\" x2=\"117\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"167\" y1=\"1\" x2=\"167\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"217\" y1=\"1\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8000</text><line x1=\"117\" y1=\"31\" x2=\"117\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8320</text><line x1=\"167\" y1=\"31\" x2=\"167\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8653</text><line x1=\"217\" y1=\"31\" x2=\"217\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"242.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">8999</text><line x1=\"1\" y1=\"31\" x2=\"267\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "Abel is twee keer zo oud als Berend (a = 2b). Ceciel is 1 jaar jonger dan Abel (c = a − 1). Samen zijn ze 14 jaar. Hoe oud is Berend?",
      "antwoord": "3",
      "uitleg": "a + b + c = 14. Substitueer a = 2b en c = 2b − 1: 2b + b + 2b − 1 = 14 → 5b = 15 → b = 3."
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,1ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,33",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 1,1³ ≈ 1,3310 ≈ 1,33.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 4a + 2q = 16 in de formule N = −2q + 9 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "2q = 16 − 4a, dus q = −2a + 8. Invullen: N = −2(−2a + 8) + 9 = 4a − 7.",
      "opties": [
        "N = −4a − 7",
        "N = 4a − 7",
        "N = 4a + 17",
        "N = −2a − 7"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De weekwinst W in euro van een bedrijf dat q producten verkoopt is W = −0,5(q − 300)(q − 500). Bereken de maximale winst in euro.",
      "antwoord": "5000",
      "uitleg": "Snijpunten met de horizontale as: q = 300 en q = 500. Midden: q = 400. W = −0,5 · (400 − 300)(400 − 500) = 5000 euro."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = 2x² + 6x − 4, y = −½x² − 7x + 3, y = x² − 5x + 8 en y = ⅓x² + 1. Bij welke formule is de parabool het smalst?",
      "uitleg": "Vergelijk de getallen voor x²: 2, −½, 1, ⅓. Het verst van 0 ligt 2, dus die parabool is het smalst.",
      "opties": [
        "y = −½x² − 7x + 3",
        "y = 2x² + 6x − 4",
        "y = x² − 5x + 8",
        "y = ⅓x² + 1"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een bergparabool met top (−3, 0). Welke formule kan bij deze parabool horen? (Kijk alleen of het een berg- of dalparabool is.)",
      "uitleg": "Bij een bergparabool is na het wegwerken van de haakjes het getal voor x² negatief. Werk bij elke formule de haakjes weg en kijk naar het getal voor x².",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c6\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c6)\" points=\"40.0,234.0 43.6,223.5 47.2,213.5 50.8,204.0 54.4,195.1 58.0,186.8 61.6,178.9 65.2,171.6 68.8,164.9 72.4,158.7 76.0,153.0 79.6,147.9 83.2,143.3 86.8,139.2 90.4,135.7 94.0,132.8 97.6,130.3 101.2,128.4 104.8,127.1 108.4,126.3 112.0,126.0 115.6,126.3 119.2,127.1 122.8,128.4 126.4,130.3 130.0,132.8 133.6,135.7 137.2,139.2 140.8,143.3 144.4,147.9 148.0,153.0 151.6,158.7 155.2,164.9 158.8,171.6 162.4,178.9 166.0,186.8 169.6,195.1 173.2,204.0 176.8,213.5 180.4,223.5 184.0,234.0 187.6,245.1 191.2,256.7 194.8,268.8 198.4,281.5 202.0,294.8 205.6,308.5 209.2,322.8 212.8,337.7 216.4,353.1 220.0,369.0 223.6,385.5 227.2,402.5 230.8,420.0 234.4,438.1 238.0,456.8 241.6,475.9 245.2,495.6 248.8,515.9 252.4,536.7 256.0,558.0 259.6,579.9 263.2,602.3 266.8,625.2 270.4,648.7 274.0,672.8 277.6,697.3 281.2,722.4 284.8,748.1 288.4,774.3 292.0,801.0 295.6,828.3 299.2,856.1 302.8,884.4 306.4,913.3 310.0,942.8 313.6,972.7 317.2,1003.2 320.8,1034.3 324.4,1065.9 328.0,1098.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/></svg>",
      "opties": [
        "y = (4x − 1)² − 9x²",
        "y = (2x + 5)(4 + x) − 3x²",
        "y = (8 − x)(8 + x) + 4x²",
        "y = (2 − x)(2 + x) + 2x²"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De hoogte h in cm van een speer is h = -5t² + 40t + 200, met t de tijd in seconden. Hoe hoog komt de speer maximaal (in cm)?",
      "antwoord": "280",
      "uitleg": "t = 0 geeft h = 200. -5t² + 40t = 0 → t = 0 of t = 8; midden t = 4. h = -5 · 4² + 40 · 4 + 200 = 280 cm."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = −3x² + 24x − 55 heeft als top (4, −7). Bij x = 2 hoort y = −19. Bij welke andere x-waarde hoort ook y = −19?",
      "antwoord": "6",
      "uitleg": "De parabool is symmetrisch in de lijn x = 4. x = 2 ligt 2 links van de symmetrieas, dus ook 2 rechts: x = 6."
    }
  ]
});
