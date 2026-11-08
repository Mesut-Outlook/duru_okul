/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 65 — §2.3 Parabolen tekenen (1/2)
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-parabolen-5",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Proeftoets 65 — §2.3 Parabolen tekenen (1/2)",
  "vak": "Wiskunde · H2 Parabolen",
  "icoon": "⛰️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een cirkelsproeier in het park verspreidt water volgens de formule h = −0,25a² + 2a + 0,5, waarin h de hoogte in meters is en a de horizontale afstand in meters. Bereken de hoogte van het hoogste punt van de waterstraal (in meters).",
      "antwoord": "4,5",
      "uitleg": "Stap 1: Bereken de a-waarde van de top:\na_top = −b / (2 · a-coëfficiënt) = −2 / (2 · −0,25) = 4 meter.\nStap 2: Vul a = 4 in de formule in om de maximale hoogte te berekenen:\nh = −0,25 · 4² + 2 · 4 + 0,5 = −4 + 8 + 0,5 = 4,5 meter."
    },
    {
      "type": "invul",
      "vraag": "Bij een sierfontein in de tuin spuit een waterstraal volgens de baan h = −0,5x² + 2,5x + 0,65, waarbij h de hoogte in meters is en x de afstand in meters. Hoeveel cm hoog bevindt zich het vertrekpunt van de straal bij x = 0?",
      "antwoord": "65",
      "uitleg": "Stap 1: Vul x = 0 in de formule in:\nh = −0,5 · 0² + 2,5 · 0 + 0,65 = 0,65 meter.\nStap 2: Reken meters om naar centimeters:\n0,65 · 100 = 65 cm."
    },
    {
      "type": "invul",
      "vraag": "In een assenstelsel zie je een dalparabool met top (3, −2) die de verticale as snijdt in (0, 7). Welke formule heeft de gedaante y = ax² + bx + c? Bereken het getal dat hoort bij b.",
      "antwoord": "-6",
      "uitleg": "Stap 1: Gebruik de topvorm y = a(x − p)² + q met top (3, −2):\ny = a(x − 3)² − 2.\nStap 2: Vul het punt (0, 7) in om a te berekenen:\n7 = a(0 − 3)² − 2 → 7 = 9a − 2 → 9a = 9 → a = 1.\nStap 3: Werk de haakjes uit:\ny = 1(x² − 6x + 9) − 2 = x² − 6x + 7.\nVoor x staat het getal b = −6."
    },
    {
      "type": "mc",
      "vraag": "Twee verschillende punten op dezelfde parabool bereiken dezelfde hoogte: de grafiek y = −x² + 14x + 9 heeft als y-afsnede 9. Wat is de x-waarde van het andere punt op de parabool met deze functiewaarde?",
      "opties": [
        "−14",
        "14",
        "7",
        "−7"
      ],
      "antwoord": 1,
      "uitleg": "Stap 1: Stel de vergelijking y = 9 op:\n−x² + 14x + 9 = 9.\nStap 2: Trek 9 af aan beide kanten:\n−x² + 14x = 0.\nStap 3: Ontbind in factoren:\nx(−x + 14) = 0.\nDit geeft x = 0 of −x + 14 = 0, dus x = 14."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij de formule y = 2x² + 4x − 4 hoort het punt (1, 2).",
      "antwoord": true,
      "uitleg": "Waar. x = 1 invullen: y = 2·1² + 4 · 1 − 4 = 2."
    },
    {
      "type": "invul",
      "vraag": "Voor de parabool bij y = 3x² − 24x + 39 is de tabel gemaakt rondom de top (4, −9). Welk getal hoort in de tabel bij x = 6?",
      "antwoord": "3",
      "uitleg": "y = 3·6² − 24 · 6 + 39 = 3.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 218 62\" width=\"218\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"216\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"53\" y1=\"1\" x2=\"53\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"66.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"79\" y1=\"1\" x2=\"79\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"105\" y1=\"1\" x2=\"105\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"122.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"139\" y1=\"1\" x2=\"139\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"165\" y1=\"1\" x2=\"165\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"191\" y1=\"1\" x2=\"191\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">7</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"40.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"53\" y1=\"31\" x2=\"53\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"66.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"79\" y1=\"31\" x2=\"79\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"92.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"105\" y1=\"31\" x2=\"105\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"122.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">−9</text><line x1=\"139\" y1=\"31\" x2=\"139\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"152.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"165\" y1=\"31\" x2=\"165\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"178.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"191\" y1=\"31\" x2=\"191\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"204.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"217\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij de formule y = 2x² + 20x + 56 hoort het punt (−6, 10).",
      "antwoord": false,
      "uitleg": "Onwaar. x = −6 invullen: y = 2·(−6)² + 20 · (−6) + 56 = 8."
    },
    {
      "type": "mc",
      "vraag": "In de figuur zie je een parabool met top (3, −2). Welke formule hoort bij deze parabool?",
      "uitleg": "1 Uit x = 0 volgt y = −20. 2 −2x² + 12x − 20 = −20 → −2x² + 12x = 0 → x(−2x + 12) = 0 → x = 0 of x = 6. 3 De x-coördinaat van de top ligt midden tussen 0 en 6: x = 3. 4 y = −2·3² + 12 · 3 − 20 = −2. 5 De top is (3, −2). Bij de andere formules ligt de top ergens anders of is het een dalparabool.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 378 252\" width=\"378\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"378\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c13\"><rect x=\"40.0\" y=\"30.0\" width=\"288.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"304.0\" y1=\"222.0\" x2=\"304.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"328.0\" y1=\"222.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"328.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"328.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"328.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"328.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"328.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"328.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"328.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"328.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"328.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−6</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"160.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"304.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"328.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">6</text><text x=\"179.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"179.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"179.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"179.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"179.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"179.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"179.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"179.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"179.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"334.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"180.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c13)\" points=\"40.0,2094.0 43.6,2029.7 47.2,1966.6 50.8,1904.5 54.4,1843.4 58.0,1783.5 61.6,1724.6 65.2,1666.9 68.8,1610.2 72.4,1554.5 76.0,1500.0 79.6,1446.5 83.2,1394.2 86.8,1342.9 90.4,1292.6 94.0,1243.5 97.6,1195.4 101.2,1148.5 104.8,1102.6 108.4,1057.7 112.0,1014.0 115.6,971.3 119.2,929.8 122.8,889.3 126.4,849.8 130.0,811.5 133.6,774.2 137.2,738.1 140.8,703.0 144.4,668.9 148.0,636.0 151.6,604.1 155.2,573.4 158.8,543.7 162.4,515.0 166.0,487.5 169.6,461.0 173.2,435.7 176.8,411.4 180.4,388.1 184.0,366.0 187.6,344.9 191.2,325.0 194.8,306.1 198.4,288.2 202.0,271.5 205.6,255.8 209.2,241.3 212.8,227.8 216.4,215.3 220.0,204.0 223.6,193.7 227.2,184.6 230.8,176.5 234.4,169.4 238.0,163.5 241.6,158.6 245.2,154.9 248.8,152.2 252.4,150.5 256.0,150.0 259.6,150.5 263.2,152.2 266.8,154.9 270.4,158.6 274.0,163.5 277.6,169.4 281.2,176.5 284.8,184.6 288.4,193.7 292.0,204.0 295.6,215.3 299.2,227.8 302.8,241.3 306.4,255.8 310.0,271.5 313.6,288.2 317.2,306.1 320.8,325.0 324.4,344.9 328.0,366.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"256.0\" cy=\"150.0\" r=\"3.5\" fill=\"#222\"/><text x=\"262.0\" y=\"144.0\" fill=\"#222\" font-size=\"11\">(3, −2)</text></svg>",
      "opties": [
        "y = −2x² + 12x − 20",
        "y = −2x² + 12x − 18",
        "y = 2x² − 12x + 20",
        "y = −2x² − 12x − 20"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = −3x² − 12x − 14. Vul in: x = …",
      "antwoord": "-2",
      "uitleg": "1 Uit x = 0 volgt y = −14. 2 −3x² − 12x − 14 = −14 → −3x² − 12x = 0 → x(−3x − 12) = 0 → x = 0 of x = −4. 3 De x-coördinaat van de top ligt midden tussen 0 en −4: x = −2. 4 y = −3·(−2)² − 12 · (−2) − 14 = −2. 5 De top is (−2, −2). De symmetrieas is de lijn x = −2."
    },
    {
      "type": "invul",
      "vraag": "De parabool bij y = 3x² + 24x + 57 heeft als top (−4, 9). Bij x = −6 hoort y = 21. Bij welke andere x-waarde hoort ook y = 21?",
      "antwoord": "-2",
      "uitleg": "De parabool is symmetrisch in de lijn x = −4. x = −6 ligt 2 links van de symmetrieas, dus ook 2 rechts: x = −2."
    },
    {
      "type": "invul",
      "vraag": "Bij de waterstraal van een tuinsproeier hoort de formule h = −0,3a² + 0,6a + 0,4. Hierin is h de hoogte in meters en a de horizontale afstand tot de sproeier in meters. Hoeveel cm hoog is de sproeier zelf (a = 0)?",
      "antwoord": "40",
      "uitleg": "a = 0 geeft h = 0,4 m = 40 cm. Top: −0,3a² + 0,6a = 0 → a = 0 of a = 2, midden a = 1; h = 0,7 m."
    },
    {
      "type": "invul",
      "vraag": "Voor de parabool bij y = −3x² − 24x − 57 is de tabel gemaakt rondom de top (−4, −9). Welk getal hoort in de tabel bij x = −2?",
      "antwoord": "-21",
      "uitleg": "y = −3·(−2)² − 24 · (−2) − 57 = −21.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 266 62\" width=\"266\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"264\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−7</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−6</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−5</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−4</text><line x1=\"163\" y1=\"1\" x2=\"163\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−3</text><line x1=\"197\" y1=\"1\" x2=\"197\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−2</text><line x1=\"231\" y1=\"1\" x2=\"231\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−1</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"146.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">−9</text><line x1=\"163\" y1=\"31\" x2=\"163\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"180.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"197\" y1=\"31\" x2=\"197\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"214.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"231\" y1=\"31\" x2=\"231\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"265\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    },
    {
      "type": "mc",
      "vraag": "Tijdens een training gooit Daan een basketbal omhoog. Na 14 meter horizontale verplaatsing heeft de bal weer dezelfde hoogte als bij aanvang. Welke x-waarde hoort bij de symmetrieas?",
      "opties": [
        "14 meter",
        "3,5 meter",
        "7 meter",
        "9 meter"
      ],
      "antwoord": 2,
      "uitleg": "Stap 1: De bal is op dezelfde hoogte bij x = 0 en x = 14 meter.\nStap 2: De symmetrieas van de parabool ligt precies halverwege:\nx = (0 + 14) / 2 = 7 meter."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij de formule y = −x² + 10x − 31 hoort het punt (4, −5).",
      "antwoord": false,
      "uitleg": "Onwaar. x = 4 invullen: y = −4² + 10 · 4 − 31 = −7."
    },
    {
      "type": "invul",
      "vraag": "Bij de waterstraal van een tuinsproeier hoort de formule h = −0,3a² + 1,8a + 0,2 (h en a in meters). Op welke afstand a bereikt de waterstraal zijn hoogste punt?",
      "antwoord": "3",
      "uitleg": "a = 0 geeft h = 0,2 m = 20 cm. Top: −0,3a² + 1,8a = 0 → a = 0 of a = 6, midden a = 3; h = 2,9 m."
    },
    {
      "type": "invul",
      "vraag": "Een hard weggeschoten bal beschrijft een vluchtbaan h = −0,2x² + 2,4x, waarbij h de hoogte in meters is en x de afstand in meters. Bereken de hoogte van het hoogste punt van de bal (in meters).",
      "antwoord": "7,2",
      "uitleg": "Stap 1: Bereken de x-coördinaat van de top:\nx = −2,4 / (2 · −0,2) = 6 meter.\nStap 2: Vul x = 6 in de formule in:\nh = −0,2 · 6² + 2,4 · 6 = −7,2 + 14,4 = 7,2 meter."
    },
    {
      "type": "invul",
      "vraag": "Geef de formule van de symmetrieas van de parabool bij y = 2x² − 8x + 14. Vul in: x = …",
      "antwoord": "2",
      "uitleg": "1 Uit x = 0 volgt y = 14. 2 2x² − 8x + 14 = 14 → 2x² − 8x = 0 → x(2x − 8) = 0 → x = 0 of x = 4. 3 De x-coördinaat van de top ligt midden tussen 0 en 4: x = 2. 4 y = 2·2² − 8 · 2 + 14 = 6. 5 De top is (2, 6). De symmetrieas is de lijn x = 2."
    },
    {
      "type": "invul",
      "vraag": "Bij de waterstraal van een tuinsproeier hoort de formule h = −0,2a² + 0,8a + 0,4 (h en a in meters). Hoeveel meter hoog komt de waterstraal maximaal?",
      "antwoord": "1,2",
      "uitleg": "a = 0 geeft h = 0,4 m = 40 cm. Top: −0,2a² + 0,8a = 0 → a = 0 of a = 4, midden a = 2; h = 1,2 m."
    },
    {
      "type": "invul",
      "vraag": "De hoogte h in cm van een speer is h = -6t² + 48t + 180, met t de tijd in seconden. Hoe hoog komt de speer maximaal (in cm)?",
      "antwoord": "276",
      "uitleg": "t = 0 geeft h = 180. -6t² + 48t = 0 → t = 0 of t = 8; midden t = 4. h = -6 · 4² + 48 · 4 + 180 = 276 cm."
    },
    {
      "type": "invul",
      "vraag": "Voor de parabool bij y = −2x² + 4x − 6 is de tabel gemaakt rondom de top (1, −4). Welk getal hoort in de tabel bij x = 3?",
      "antwoord": "-12",
      "uitleg": "y = −2·3² + 4 · 3 − 6 = −12.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 234 62\" width=\"234\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"232\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">x</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−2</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">−1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"121\" y1=\"1\" x2=\"121\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"155\" y1=\"1\" x2=\"155\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"168.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"181\" y1=\"1\" x2=\"181\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"194.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"207\" y1=\"1\" x2=\"207\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">y</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"121\" y1=\"31\" x2=\"121\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"138.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">−4</text><line x1=\"155\" y1=\"31\" x2=\"155\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"168.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"181\" y1=\"31\" x2=\"181\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"194.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"207\" y1=\"31\" x2=\"207\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"220.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">…</text><line x1=\"1\" y1=\"31\" x2=\"233\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>"
    }
  ]
});
