/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 124 — Gemengd H1 + H2 (1/5)
   Bron: Noordhoff H1 §1.1–§1.5 + H2 §2.1–§2.5 (2 vragen per paragraaf, andere getallen)
   Gegenereerd met tools/gen_wiskunde_h1_h2_gemengd.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1h2-gemengd-1",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 124 — Gemengd H1 + H2 (1/5)",
  "vak": "Wiskunde · H1 Lineair & exponentieel + H2 Parabolen",
  "icoon": "🔀",
  "duurMin": 40,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Bij een hangbrug hoort de formule h = 0,02a² − a + 20. Hierin is h de hoogte boven de grond in meters en a de afstand in meters vanaf punt P (a = 0). Hoeveel meter hangt de brug minimaal boven de grond?",
      "antwoord": "7,5",
      "uitleg": "P ligt op hoogte 20. Zelfde hoogte: 0,02a² − a = 0 → a = 0 of a = 1 / 0,02 = 50. Laagste punt in het midden: a = 25, h = 7,5 m."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 120 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "291,90",
      "uitleg": "Na 3 jaar is t = 36: W = 120 · 1,025³⁶ ≈ 291,90 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "invul",
      "vraag": "In de tabel zie je het aantal bezoekers van een pretpark vanaf 2018. Bereken de groeifactor per jaar. Rond af op twee decimalen.",
      "antwoord": "1,12",
      "uitleg": "336.000 : 300.000 ≈ 1,12; ook 376.320 : 336.000 ≈ 1,12. De groeifactor is 1,12.",
      "tolerantie": 0.006,
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 364 62\" width=\"364\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"362\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"67\" y1=\"1\" x2=\"67\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2018</text><line x1=\"141\" y1=\"1\" x2=\"141\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2019</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"289\" y1=\"1\" x2=\"289\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><rect x=\"1\" y=\"31\" width=\"66\" height=\"30\" fill=\"#fde7ef\"/><text x=\"34.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">aantal</text><line x1=\"67\" y1=\"31\" x2=\"67\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">300.000</text><line x1=\"141\" y1=\"31\" x2=\"141\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">336.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"252.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">376.320</text><line x1=\"289\" y1=\"31\" x2=\"289\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"326.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">421.478</text><line x1=\"1\" y1=\"31\" x2=\"363\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 4a + 2q = 12 in de formule w = 3q + 3 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "2q = 12 − 4a, dus q = −2a + 6. Invullen: w = 3(−2a + 6) + 3 = −6a + 21.",
      "opties": [
        "w = −2a + 21",
        "w = −6a + 9",
        "w = −6a + 21",
        "w = 6a + 21"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = −2(x + 4)² + 11?",
      "uitleg": "Bij x = −4 is (x + 4)² = 0; dat is de kleinste (of grootste) waarde. Dan is y = 11. Top (−4, 11). Let op: bij (x − 4) hoort x = 4, bij (x + 4) hoort x = −4.",
      "opties": [
        "(4, −11)",
        "(−4, −11)",
        "(4, 11)",
        "(−4, 11)"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Abel is drie keer zo oud als Berend (a = 3b). Ceciel is 3 jaar jonger dan Abel (c = a − 3). Samen zijn ze 39 jaar. Hoe oud is Berend?",
      "antwoord": "6",
      "uitleg": "a + b + c = 39. Substitueer a = 3b en c = 3b − 3: 3b + b + 3b − 3 = 39 → 7b = 42 → b = 6."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (−2, −2). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = 6. 2 2x² + 8x + 6 = 6 → 2x² + 8x = 0 → x(2x + 8) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = 2·(−2)² + 8 · (−2) + 6 = −2. 5 De top is (−2, −2). Bij de andere formules ligt de top ergens anders of is het een bergparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c1\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c1)\" points=\"40.0,-234.0 43.6,-205.7 47.2,-178.6 50.8,-152.5 54.4,-127.4 58.0,-103.5 61.6,-80.6 65.2,-58.9 68.8,-38.2 72.4,-18.5 76.0,0.0 79.6,17.5 83.2,33.8 86.8,49.1 90.4,63.4 94.0,76.5 97.6,88.6 101.2,99.5 104.8,109.4 108.4,118.3 112.0,126.0 115.6,132.7 119.2,138.2 122.8,142.7 126.4,146.2 130.0,148.5 133.6,149.8 137.2,149.9 140.8,149.0 144.4,147.1 148.0,144.0 151.6,139.9 155.2,134.6 158.8,128.3 162.4,121.0 166.0,112.5 169.6,103.0 173.2,92.3 176.8,80.6 180.4,67.9 184.0,54.0 187.6,39.1 191.2,23.0 194.8,5.9 198.4,-12.2 202.0,-31.5 205.6,-51.8 209.2,-73.3 212.8,-95.8 216.4,-119.3 220.0,-144.0 223.6,-169.7 227.2,-196.6 230.8,-224.5 234.4,-253.4 238.0,-283.5 241.6,-314.6 245.2,-346.9 248.8,-380.2 252.4,-414.5 256.0,-450.0 259.6,-486.5 263.2,-524.2 266.8,-562.9 270.4,-602.6 274.0,-643.5 277.6,-685.4 281.2,-728.5 284.8,-772.6 288.4,-817.7 292.0,-864.0 295.6,-911.3 299.2,-959.8 302.8,-1009.3 306.4,-1059.8 310.0,-1111.5 313.6,-1164.2 317.2,-1218.1 320.8,-1273.0 324.4,-1328.9 328.0,-1386.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"136.0\" cy=\"150.0\" r=\"3.5\" fill=\"#222\"/><text x=\"142.0\" y=\"144.0\" fill=\"#222\" font-size=\"11\">(−2, −2)</text></svg>",
      "opties": [
        "y = 2x² + 8x + 8",
        "y = 2x² − 8x + 6",
        "y = −2x² − 8x − 6",
        "y = 2x² + 8x + 6"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −½x² + 3x + 6, y = ⅓x² − 5x + 8, y = 4x² − 4x − 1 en y = −¼x² − 7x + 6. Bij welke formule is de parabool het breedst?",
      "uitleg": "Vergelijk de getallen voor x²: −½, ⅓, 4, −¼. Het dichtst bij 0 ligt −¼, dus die parabool is het breedst.",
      "opties": [
        "y = −¼x² − 7x + 6",
        "y = 4x² − 4x − 1",
        "y = −½x² + 3x + 6",
        "y = ⅓x² − 5x + 8"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = (4 − x)(4 + x) − 3x². Schrijf de formule zonder haakjes. Welk getal staat dan voor x²?",
      "antwoord": "-4",
      "uitleg": "(4 − x)(4 + x) = −x² + 16. Samen met −3x²: y = −4x² + 16. Het getal voor x² is −4, dus de grafiek is een bergparabool."
    },
    {
      "type": "mc",
      "vraag": "Het snijpunt van de lijnen y = 3x + 50 en y = 5x − 8 valt buiten een schets. Ligt het snijpunt links of rechts van de lijn x = 22?",
      "uitleg": "Gelijkstellen: 3x + 50 = 5x − 8 → x = 29. Dat is meer dan 22, dus rechts.",
      "opties": [
        "rechts van de lijn x = 22",
        "precies op de lijn x = 22",
        "de lijnen snijden elkaar niet",
        "links van de lijn x = 22"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Uit de formule y = −x² + 9x − 1 volgt dat de grafiek een dalparabool is.",
      "antwoord": false,
      "uitleg": "Onwaar. a = −1 is negatief → bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Gegeven is de formule y = x² + bx + 4. De x-coördinaat van de top van de parabool is 1. Bereken b.",
      "antwoord": "-2",
      "uitleg": "De parabool snijdt de y-as in (0, 4). Het andere punt met y = 4 ligt even ver aan de andere kant van de top: x = 2 · 1 = 2. Invullen: 2² + b · 2 + 4 = 4 → 4 + 2b = 0 → b = −2."
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van het snijpunt van de lijnen y = −x + 1 en y = 7x − 71.",
      "antwoord": "-8",
      "uitleg": "−x + 1 = 7x − 71 geeft x = 9. Invullen: y = −1 · 9 + 1 = −8. Controle in de andere formule: −8."
    },
    {
      "type": "mc",
      "vraag": "De grafiek geeft de hoeveelheid medicijn in het bloed (N), met 400 op t = 2, en hoort bij een exponentieel verband. Welke formule hoort erbij?",
      "uitleg": "Op t = 0 is N = 100. Van t = 0 naar t = 1: 200 : 100 = 2. Dus N = 100 · 2ᵗ.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 346\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"206\" height=\"346\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"40.0\" y=\"30.0\" width=\"136.0\" height=\"272.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"302.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"74.0\" y1=\"302.0\" x2=\"74.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"108.0\" y1=\"302.0\" x2=\"108.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"142.0\" y1=\"302.0\" x2=\"142.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"176.0\" y1=\"302.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"176.0\" y2=\"302.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"268.0\" x2=\"176.0\" y2=\"268.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"234.0\" x2=\"176.0\" y2=\"234.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"200.0\" x2=\"176.0\" y2=\"200.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"166.0\" x2=\"176.0\" y2=\"166.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"132.0\" x2=\"176.0\" y2=\"132.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"98.0\" x2=\"176.0\" y2=\"98.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"64.0\" x2=\"176.0\" y2=\"64.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"176.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"176.0\" y2=\"302.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"302.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"74.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"108.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"142.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"176.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"35.0\" y=\"272.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"238.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"204.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"170.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"136.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"102.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"68.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"317.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"182.0\" y=\"306.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"108.0\" y=\"338.0\" fill=\"#222\" text-anchor=\"middle\">t →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ N</text><polyline clip-path=\"url(#w1c2)\" points=\"40.0,268.0 41.7,266.8 43.4,265.6 45.1,264.3 46.8,262.9 48.5,261.6 50.2,260.1 51.9,258.7 53.6,257.1 55.3,255.6 57.0,253.9 58.7,252.2 60.4,250.5 62.1,248.6 63.8,246.8 65.5,244.8 67.2,242.8 68.9,240.7 70.6,238.6 72.3,236.3 74.0,234.0 75.7,231.6 77.4,229.1 79.1,226.5 80.8,223.9 82.5,221.1 84.2,218.3 85.9,215.3 87.6,212.3 89.3,209.1 91.0,205.8 92.7,202.4 94.4,198.9 96.1,195.3 97.8,191.5 99.5,187.6 101.2,183.6 102.9,179.4 104.6,175.1 106.3,170.6 108.0,166.0 109.7,161.2 111.4,156.2 113.1,151.1 114.8,145.8 116.5,140.3 118.2,134.6 119.9,128.7 121.6,122.5 123.3,116.2 125.0,109.7 126.7,102.9 128.4,95.9 130.1,88.6 131.8,81.1 133.5,73.3 135.2,65.2 136.9,56.9 138.6,48.2 140.3,39.3 142.0,30.0 143.7,20.4 145.4,10.5 147.1,0.2 148.8,-10.4 150.5,-21.5 152.2,-32.9 153.9,-44.7 155.6,-56.9 157.3,-69.6 159.0,-82.7 160.7,-96.2 162.4,-110.3 164.1,-124.8 165.8,-139.9 167.5,-155.4 169.2,-171.6 170.9,-188.3 172.6,-205.6 174.3,-223.5 176.0,-242.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"268.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"262.0\" fill=\"#222\" font-size=\"11\">(0, 100)</text><circle cx=\"74.0\" cy=\"234.0\" r=\"3.5\" fill=\"#222\"/><text x=\"80.0\" y=\"228.0\" fill=\"#222\" font-size=\"11\">(1, 200)</text><circle cx=\"108.0\" cy=\"166.0\" r=\"3.5\" fill=\"#222\"/><text x=\"114.0\" y=\"160.0\" fill=\"#222\" font-size=\"11\">(2, 400)</text><circle cx=\"142.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"148.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(3, 800)</text></svg>",
      "opties": [
        "N = 100 · 2ᵗ",
        "N = 100 + 100t",
        "N = 100 · 0,5ᵗ",
        "N = 200 · 2ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Een basketbalspeler gooit een bal vanaf 1,8 m hoogte richting het basket. Na 10 m horizontale afstand is de bal weer op 1,8 m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
      "uitleg": "Werk de haakjes weg. h = −0,1a(a − 10) + 1,8: h = −0,1a² + a + 1,8 — het getal voor a² is negatief, dus een bergparabool. Bij h = 0,1a(a − 10) + 1,8 en h = −0,1a(10 − a) + 1,8 is het getal voor a² positief (dalparabool); h = 0,1a² + 1,8 is ook een dalparabool.",
      "opties": [
        "h = −0,1a(10 − a) + 1,8",
        "h = 0,1a(a − 10) + 1,8",
        "h = 0,1a² + 1,8",
        "h = −0,1a(a − 10) + 1,8"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De vorm van een hangmat tussen twee bomen past bij de formule h = 0,25(a − 2)² + 0,4. Hierin is h de hoogte boven de grond in meters en a de afstand vanaf de linkerboom in meters. Hoeveel cm boven de grond is het laagste punt?",
      "antwoord": "40",
      "uitleg": "Het laagste punt is de top (a = 2): h = 0,4 m = 40 cm. Bij de boom (a = 0): h = 0,25 · 2² + 0,4 = 1,4 m. De andere boom staat even ver aan de andere kant: a = 4 m."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² − 24x + 40 heeft als top (4, −8). Bij x = 1 hoort y = 19. Bij welke andere x-waarde hoort ook y = 19?",
      "antwoord": "7",
      "uitleg": "De parabool is symmetrisch in de lijn x = 4. x = 1 ligt 3 links van de symmetrieas, dus ook 3 rechts: x = 7."
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,2ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,73",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 1,2³ ≈ 1,7280 ≈ 1,73.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (−10, −8) en loopt evenwijdig aan lijn l: y = −0,5x + 4. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = −0,5. Invullen van (−10, −8): −8 = −0,5 · (−10) + b = 5 + b, dus b = −13. Lijn m: y = −0,5x − 13.",
      "opties": [
        "y = −0,5x − 8",
        "y = −0,5x − 13",
        "y = 0,5x − 3",
        "y = −0,5x − 3"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Welke formule hoort bij de lijn door de punten (−6, −34) en (2, 6)?",
      "uitleg": "a = (6 − (−34)) / (2 − (−6)) = 5. Invullen van (−6, −34) geeft −34 = −30 + b, dus b = −4. De formule is y = 5x − 4.",
      "opties": [
        "y = 5x + 4",
        "y = 5x − 34",
        "y = 5x − 4",
        "y = −5x − 4"
      ],
      "antwoord": 2
    }
  ]
});
