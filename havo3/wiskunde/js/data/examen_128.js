/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 128 — Gemengd H1 + H2 (5/5)
   Bron: Noordhoff H1 §1.1–§1.5 + H2 §2.1–§2.5 (2 vragen per paragraaf, andere getallen)
   Gegenereerd met tools/gen_wiskunde_h1_h2_gemengd.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1h2-gemengd-5",
  "hoofdstuk": 2,
  "paragraaf": "mix",
  "titel": "Proeftoets 128 — Gemengd H1 + H2 (5/5)",
  "vak": "Wiskunde · H1 Lineair & exponentieel + H2 Parabolen",
  "icoon": "🔀",
  "duurMin": 40,
  "vragen": [
    {
      "type": "waaronwaar",
      "vraag": "De lijn bij de formule y = 5 + 0,6x is dalend.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc is 0,6; die is positief, dus de lijn is stijgend."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij de formule y = 3x² + 12x + 3 hoort het punt (−3, −6).",
      "antwoord": true,
      "uitleg": "Waar. x = −3 invullen: y = 3·(−3)² + 12 · (−3) + 3 = −6."
    },
    {
      "type": "mc",
      "vraag": "Een hoeveelheid neemt elk jaar met 8% toe. Hoe groot is de groeifactor per jaar?",
      "uitleg": "Toename van 8%: je houdt 108% over, dus groeifactor 1,08.",
      "opties": [
        "0,8",
        "0,92",
        "0,08",
        "1,08"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij y = 3(x − 1)(x − 5) is een dalparabool.",
      "antwoord": true,
      "uitleg": "Waar. Zonder haakjes is het getal voor x² gelijk aan 3: een dalparabool."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,05 per uur. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 3 uur eerder? Rond af op een geheel getal.",
      "antwoord": "276428",
      "uitleg": "Groeifactor per 3 uur: 1,05³. Terugrekenen = delen: 320.000 : 1,05³ ≈ 276428.",
      "tolerantie": 138
    },
    {
      "type": "mc",
      "vraag": "Substitueer de formule 8a + 4q = 4 in de formule N = 5q − 12 en vereenvoudig. (Herleid eerst de eerste formule naar q = …)",
      "uitleg": "4q = 4 − 8a, dus q = −2a + 1. Invullen: N = 5(−2a + 1) − 12 = −10a − 7.",
      "opties": [
        "N = −10a − 11",
        "N = 10a − 7",
        "N = −2a − 7",
        "N = −10a − 7"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Een basketbalspeler gooit een bal vanaf 1,8 m hoogte richting het basket. Na 6 m horizontale afstand is de bal weer op 1,8 m hoogte. Neem h voor de hoogte van de bal in meters en a voor de horizontale afstand in meters. De baan is een bergparabool. Welke formule kan bij de hoogte van de bal horen?",
      "uitleg": "Werk de haakjes weg. h = −0,1a(a − 6) + 1,8: h = −0,1a² + 0,6a + 1,8 — het getal voor a² is negatief, dus een bergparabool. Bij h = 0,1a(a − 6) + 1,8 en h = −0,1a(6 − a) + 1,8 is het getal voor a² positief (dalparabool); h = 0,1a² + 1,8 is ook een dalparabool.",
      "opties": [
        "h = 0,1a² + 1,8",
        "h = −0,1a(6 − a) + 1,8",
        "h = −0,1a(a − 6) + 1,8",
        "h = 0,1a(a − 6) + 1,8"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Schrijf y = −½(x − 2)(x + 6) in de vorm y = ax² + bx + c. Hoe groot is b?",
      "antwoord": "-2",
      "uitleg": "(x − 2)(x + 6) = x² + 4x − 12; keer −0,5 geeft y = −½x² − 2x + 6, dus b = −2."
    },
    {
      "type": "mc",
      "vraag": "In de figuur staan vier parabolen. Welke parabool hoort bij de formule y = 3x² − 2?",
      "uitleg": "y = 3x² − 2: dalparabool, top op de y-as in (0, −2), smaller dan y = x². Dat past alleen bij parabool 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 330 252\" width=\"330\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"330\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c8\"><rect x=\"40.0\" y=\"30.0\" width=\"240.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"280.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"280.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"280.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"280.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"280.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"280.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"280.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"184.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"155.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"155.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"155.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"155.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"155.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"155.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"155.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"155.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"155.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"286.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"156.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c8)\" points=\"40.0,738.0 43.0,708.4 46.0,679.5 49.0,651.4 52.0,624.0 55.0,597.4 58.0,571.5 61.0,546.4 64.0,522.0 67.0,498.4 70.0,475.5 73.0,453.4 76.0,432.0 79.0,411.4 82.0,391.5 85.0,372.4 88.0,354.0 91.0,336.4 94.0,319.5 97.0,303.4 100.0,288.0 103.0,273.4 106.0,259.5 109.0,246.4 112.0,234.0 115.0,222.4 118.0,211.5 121.0,201.4 124.0,192.0 127.0,183.4 130.0,175.5 133.0,168.4 136.0,162.0 139.0,156.4 142.0,151.5 145.0,147.4 148.0,144.0 151.0,141.4 154.0,139.5 157.0,138.4 160.0,138.0 163.0,138.4 166.0,139.5 169.0,141.4 172.0,144.0 175.0,147.4 178.0,151.5 181.0,156.4 184.0,162.0 187.0,168.4 190.0,175.5 193.0,183.4 196.0,192.0 199.0,201.4 202.0,211.5 205.0,222.4 208.0,234.0 211.0,246.4 214.0,259.5 217.0,273.4 220.0,288.0 223.0,303.4 226.0,319.5 229.0,336.4 232.0,354.0 235.0,372.4 238.0,391.5 241.0,411.4 244.0,432.0 247.0,453.4 250.0,475.5 253.0,498.4 256.0,522.0 259.0,546.4 262.0,571.5 265.0,597.4 268.0,624.0 271.0,651.4 274.0,679.5 277.0,708.4 280.0,738.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"195.8\" y=\"176.6\" fill=\"#c2185b\" font-weight=\"bold\" font-size=\"14\">1</text><polyline clip-path=\"url(#w1c8)\" points=\"40.0,378.0 43.0,363.2 46.0,348.8 49.0,334.7 52.0,321.0 55.0,307.7 58.0,294.8 61.0,282.2 64.0,270.0 67.0,258.2 70.0,246.8 73.0,235.7 76.0,225.0 79.0,214.7 82.0,204.8 85.0,195.2 88.0,186.0 91.0,177.2 94.0,168.8 97.0,160.7 100.0,153.0 103.0,145.7 106.0,138.8 109.0,132.2 112.0,126.0 115.0,120.2 118.0,114.8 121.0,109.7 124.0,105.0 127.0,100.7 130.0,96.8 133.0,93.2 136.0,90.0 139.0,87.2 142.0,84.8 145.0,82.7 148.0,81.0 151.0,79.7 154.0,78.8 157.0,78.2 160.0,78.0 163.0,78.2 166.0,78.8 169.0,79.7 172.0,81.0 175.0,82.7 178.0,84.8 181.0,87.2 184.0,90.0 187.0,93.2 190.0,96.8 193.0,100.7 196.0,105.0 199.0,109.7 202.0,114.8 205.0,120.2 208.0,126.0 211.0,132.2 214.0,138.8 217.0,145.7 220.0,153.0 223.0,160.7 226.0,168.8 229.0,177.2 232.0,186.0 235.0,195.2 238.0,204.8 241.0,214.7 244.0,225.0 247.0,235.7 250.0,246.8 253.0,258.2 256.0,270.0 259.0,282.2 262.0,294.8 265.0,307.7 268.0,321.0 271.0,334.7 274.0,348.8 277.0,363.2 280.0,378.0\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.6\"/><text x=\"90.2\" y=\"204.9\" fill=\"#2563eb\" font-weight=\"bold\" font-size=\"14\">2</text><polyline clip-path=\"url(#w1c8)\" points=\"40.0,666.0 43.0,645.2 46.0,624.8 49.0,604.7 52.0,585.0 55.0,565.7 58.0,546.8 61.0,528.2 64.0,510.0 67.0,492.2 70.0,474.8 73.0,457.7 76.0,441.0 79.0,424.7 82.0,408.8 85.0,393.2 88.0,378.0 91.0,363.2 94.0,348.8 97.0,334.7 100.0,321.0 103.0,307.7 106.0,294.8 109.0,282.2 112.0,270.0 115.0,258.2 118.0,246.8 121.0,235.7 124.0,225.0 127.0,214.7 130.0,204.8 133.0,195.2 136.0,186.0 139.0,177.2 142.0,168.8 145.0,160.7 148.0,153.0 151.0,145.7 154.0,138.8 157.0,132.2 160.0,126.0 163.0,120.2 166.0,114.8 169.0,109.7 172.0,105.0 175.0,100.7 178.0,96.8 181.0,93.2 184.0,90.0 187.0,87.2 190.0,84.8 193.0,82.7 196.0,81.0 199.0,79.7 202.0,78.8 205.0,78.2 208.0,78.0 211.0,78.2 214.0,78.8 217.0,79.7 220.0,81.0 223.0,82.7 226.0,84.8 229.0,87.2 232.0,90.0 235.0,93.2 238.0,96.8 241.0,100.7 244.0,105.0 247.0,109.7 250.0,114.8 253.0,120.2 256.0,126.0 259.0,132.2 262.0,138.8 265.0,145.7 268.0,153.0 271.0,160.7 274.0,168.8 277.0,177.2 280.0,186.0\" fill=\"none\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"210.2\" y=\"82.5\" fill=\"#0d9488\" font-weight=\"bold\" font-size=\"14\">3</text><polyline clip-path=\"url(#w1c8)\" points=\"40.0,-750.0 43.0,-705.6 46.0,-662.2 49.0,-620.1 52.0,-579.0 55.0,-539.1 58.0,-500.2 61.0,-462.6 64.0,-426.0 67.0,-390.6 70.0,-356.2 73.0,-323.1 76.0,-291.0 79.0,-260.1 82.0,-230.2 85.0,-201.6 88.0,-174.0 91.0,-147.6 94.0,-122.2 97.0,-98.1 100.0,-75.0 103.0,-53.1 106.0,-32.2 109.0,-12.6 112.0,6.0 115.0,23.4 118.0,39.8 121.0,54.9 124.0,69.0 127.0,81.9 130.0,93.8 133.0,104.4 136.0,114.0 139.0,122.4 142.0,129.8 145.0,135.9 148.0,141.0 151.0,144.9 154.0,147.8 157.0,149.4 160.0,150.0 163.0,149.4 166.0,147.8 169.0,144.9 172.0,141.0 175.0,135.9 178.0,129.8 181.0,122.4 184.0,114.0 187.0,104.4 190.0,93.8 193.0,81.9 196.0,69.0 199.0,54.9 202.0,39.8 205.0,23.4 208.0,6.0 211.0,-12.6 214.0,-32.2 217.0,-53.1 220.0,-75.0 223.0,-98.1 226.0,-122.2 229.0,-147.6 232.0,-174.0 235.0,-201.6 238.0,-230.2 241.0,-260.1 244.0,-291.0 247.0,-323.1 250.0,-356.2 253.0,-390.6 256.0,-426.0 259.0,-462.6 262.0,-500.2 265.0,-539.1 268.0,-579.0 271.0,-620.1 274.0,-662.2 277.0,-705.6 280.0,-750.0\" fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.6\"/><text x=\"128.6\" y=\"61.8\" fill=\"#b45309\" font-weight=\"bold\" font-size=\"14\">4</text></svg>",
      "opties": [
        "parabool 4",
        "parabool 3",
        "parabool 2",
        "parabool 1"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "De lijnen y = 3x − 4 en y = −x − 8 snijden elkaar in S. Met welke vergelijking bereken je de x-coördinaat van S?",
      "uitleg": "Op het snijpunt hebben beide lijnen dezelfde y. Stel daarom de twee formules aan elkaar gelijk.",
      "opties": [
        "3x − 4 = −x − 8",
        "3x − 4 = −(−x − 8)",
        "3x − 4 = 0",
        "3x − 8 = −x − 4"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,8ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,41",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 0,8⁴ ≈ 0,4096 ≈ 0,41.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "De grafiek bij de formule y = x(3 − 5x) − 3x² is een bergparabool.",
      "antwoord": true,
      "uitleg": "Waar. x(3 − 5x) = −5x² + 3x. Samen met −3x²: y = −8x² + 3x. Het getal voor x² is −8: een bergparabool."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −3x² − 12x − 4. Vul in: x = …",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = −4. 2 −3x² − 12x − 4 = −4 → −3x² − 12x = 0 → x(−3x − 12) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −3·(−2)² − 12 · (−2) − 4 = 8. 5 De top is (−2, 8). De symmetrieas is de lijn x = −2."
    },
    {
      "type": "waaronwaar",
      "vraag": "De lijnen y = 5x + 3 en y = −5x + 3 hebben geen snijpunt.",
      "antwoord": false,
      "uitleg": "Onwaar. De rc's zijn verschillend (5 en −5), dus de lijnen snijden elkaar wel: in (0, 3), want ze hebben hetzelfde startgetal."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −2x² + 16x − 33. Vul in: x = …",
      "antwoord": "4",
      "uitleg": "1 Uit x = 0 volgt y = −33. 2 −2x² + 16x − 33 = −33 → −2x² + 16x = 0 → x(−2x + 16) = 0 → x = 0 of x = 8. 3 De x-coördinaat van de top ligt midden tussen 0 en 8: x = 4. 4 y = −2·4² + 16 · 4 − 33 = −1. 5 De top is (4, −1). De symmetrieas is de verticale lijn door de top: x = 4."
    },
    {
      "type": "invul",
      "vraag": "De tabel (het aantal planten in een kas) hoort bij een exponentieel verband met waarden 32 op t = 1 en 64 op t = 2. Bereken de waarde van a op t = 0.",
      "antwoord": "16",
      "uitleg": "Groeifactor: 64 : 32 = 2. Terug naar t = 0: 32 : 2 = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 206 62\" width=\"206\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"204\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"87\" y1=\"1\" x2=\"87\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">a</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"70.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">32</text><line x1=\"87\" y1=\"31\" x2=\"87\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"104.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">64</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"142.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">128</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"184.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">256</text><line x1=\"1\" y1=\"31\" x2=\"205\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(1, 3) en Q(9, −13). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-2",
      "uitleg": "rc = toename y / toename x = (−13 − 3) / (9 − 1) = −16 / 8 = −2."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = ¼x² − x + 6, y = ½x² + 8x − 6, y = 3x² − 5x + 2 en y = 5x² − 5x + 3. Bij welke formule is de parabool het breedst?",
      "uitleg": "Vergelijk de getallen voor x²: ¼, ½, 3, 5. Het dichtst bij 0 ligt ¼, dus die parabool is het breedst.",
      "opties": [
        "y = ½x² + 8x − 6",
        "y = ¼x² − x + 6",
        "y = 5x² − 5x + 3",
        "y = 3x² − 5x + 2"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De formule t = ax + b wordt gesubstitueerd in de formule y = 5t + 6. Het resultaat is y = −10x − 9. Bereken a.",
      "antwoord": "-2",
      "uitleg": "y = 5(ax + b) + 6 = 5a·x + 5b + 6. Dus 5a = −10 → a = −2 (en 5b + 6 = −9 → b = −3)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 3x² + 6x − 5?",
      "uitleg": "1 Uit x = 0 volgt y = −5. 2 3x² + 6x − 5 = −5 → 3x² + 6x = 0 → x(3x + 6) = 0 → x = 0 of x = −2. 3 De x-coördinaat van de top ligt midden tussen 0 en −2: x = −1. 4 y = 3·(−1)² + 6 · (−1) − 5 = −8. 5 De top is (−1, −8).",
      "opties": [
        "(−1, −5)",
        "(−1, 4)",
        "(−1, −8)",
        "(1, −8)"
      ],
      "antwoord": 2
    }
  ]
});
