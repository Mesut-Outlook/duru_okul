/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 43 — §1.5 Groeifactor en tijd (4/5, toetsniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-33",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 43 — §1.5 Groeifactor en tijd (4/5, toetsniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 2,4 per halfjaar. Bereken de groeifactor per jaar.",
      "antwoord": "5,76",
      "uitleg": "Per jaar zijn er twee stappen: 2,4 · 2,4 = 2,4² = 5,76.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,05ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,16",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 1,05³ ≈ 1,1576 ≈ 1,16.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "De waarde van een oude auto groeit met groeifactor 0,985 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,985¹² ≈ 0,834. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,834",
        "0,820",
        "11,820",
        "0,941"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 80 · 1,10ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 1,10³ ≈ 1,33. De beginwaarde (80) blijft hetzelfde.",
      "opties": [
        "A = 80 · 1,33ᵗ",
        "A = 240 · 1,10ᵗ",
        "A = 106 · 1,33ᵗ",
        "A = 80 · 3,30ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Een spaarbedrag groeit met 5% per jaar. Dat is hetzelfde als een groei van 50% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,05¹⁰ ≈ 1,629, dus ongeveer 62,9% groei, niet 50%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per jaar. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 4 jaar eerder? Rond af op een geheel getal.",
      "antwoord": "203366",
      "uitleg": "Groeifactor per 4 jaar: 1,12⁴. Terugrekenen = delen: 320.000 : 1,12⁴ ≈ 203366.",
      "tolerantie": 101
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 0,88ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 0,88 = 88%, dus afname van 12% per maand.",
      "opties": [
        "−1,2% per maand",
        "−120% per maand",
        "−12% per maand",
        "+12% per maand"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 1200. Bereken de groeifactor per uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,0625",
      "uitleg": "Per kwartier: 600 : 1200 = 0,5. Een uur is 4 kwartier: 0,5⁴ = 0,0625.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c50\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">150</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">450</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">750</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">900</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">1050</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">1200</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c50)\" points=\"40.0,30.0 42.2,42.2 44.5,53.9 46.8,65.1 49.0,75.8 51.2,86.1 53.5,95.9 55.8,105.3 58.0,114.4 60.2,123.0 62.5,131.3 64.8,139.2 67.0,146.8 69.2,154.0 71.5,161.0 73.8,167.6 76.0,174.0 78.2,180.1 80.5,186.0 82.8,191.5 85.0,196.9 87.2,202.0 89.5,207.0 91.8,211.7 94.0,216.2 96.2,220.5 98.5,224.6 100.8,228.6 103.0,232.4 105.2,236.0 107.5,239.5 109.8,242.8 112.0,246.0 114.2,249.1 116.5,252.0 118.8,254.8 121.0,257.5 123.2,260.0 125.5,262.5 127.8,264.8 130.0,267.1 132.2,269.2 134.5,271.3 136.8,273.3 139.0,275.2 141.2,277.0 143.5,278.7 145.8,280.4 148.0,282.0 150.2,283.5 152.5,285.0 154.8,286.4 157.0,287.7 159.2,289.0 161.5,290.2 163.8,291.4 166.0,292.5 168.2,293.6 170.5,294.7 172.8,295.6 175.0,296.6 177.2,297.5 179.5,298.4 181.8,299.2 184.0,300.0 186.2,300.8 188.5,301.5 190.8,302.2 193.0,302.9 195.2,303.5 197.5,304.1 199.8,304.7 202.0,305.3 204.2,305.8 206.5,306.3 208.8,306.8 211.0,307.3 213.2,307.8 215.5,308.2 217.8,308.6 220.0,309.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(0, 1200)</text><circle cx=\"76.0\" cy=\"174.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"168.0\" fill=\"#222\" font-size=\"11\">(1, 600)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 300)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp verandert exponentieel: 25.600 in 2020 en 12.800 in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?",
      "uitleg": "Groeifactor per jaar: 12.800 : 25.600 = 0,5. Per drie jaar: 0,5³ = 0,125.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 316 62\" width=\"316\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"314\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"83\" y1=\"1\" x2=\"83\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"149\" y1=\"1\" x2=\"149\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"265\" y1=\"1\" x2=\"265\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"290.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">inwoners</text><line x1=\"83\" y1=\"31\" x2=\"83\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">25.600</text><line x1=\"149\" y1=\"31\" x2=\"149\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">12.800</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"240.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6400</text><line x1=\"265\" y1=\"31\" x2=\"265\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"290.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3200</text><line x1=\"1\" y1=\"31\" x2=\"315\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "1,5",
        "−0,5",
        "0,5",
        "0,125"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de groeifactor per jaar 0,95 is, dan is de groeifactor per 5 jaar gelijk aan 0,95⁵.",
      "antwoord": true,
      "uitleg": "Waar. Elk jaar vermenigvuldig je met 0,95; na 5 jaar dus 5 keer: 0,95⁵."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 50 · 1,012ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "76,82",
      "uitleg": "Na 3 jaar is t = 36: W = 50 · 1,012³⁶ ≈ 76,82 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,9 per 10 minuten, soort B met groeifactor 30 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,9⁶ ≈ 47,0. Vergelijk met 30: soort A groeit het snelst.",
      "opties": [
        "ze groeien even snel",
        "dat kun je niet vergelijken",
        "soort B",
        "soort A"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,2 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "1,44",
      "uitleg": "Per twee weken zijn er twee stappen: 1,2 · 1,2 = 1,2² = 1,44.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,9ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,73",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 0,9³ ≈ 0,7290 ≈ 0,73.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit met 2% per jaar. Dat is hetzelfde als een groei van 20% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,02¹⁰ ≈ 1,219, dus ongeveer 21,9% groei, niet 20%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per maand. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 3 maanden eerder? Rond af op een geheel getal.",
      "antwoord": "227770",
      "uitleg": "Groeifactor per 3 maanden: 1,12³. Terugrekenen = delen: 320.000 : 1,12³ ≈ 227770.",
      "tolerantie": 113
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 80 · 1,06ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 1,06⁴ ≈ 1,26. De beginwaarde (80) blijft hetzelfde.",
      "opties": [
        "A = 101 · 1,26ᵗ",
        "A = 80 · 1,26ᵗ",
        "A = 80 · 4,24ᵗ",
        "A = 320 · 1,06ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 800. Bereken de groeifactor per uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,0625",
      "uitleg": "Per kwartier: 400 : 800 = 0,5. Een uur is 4 kwartier: 0,5⁴ = 0,0625.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c55\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c55)\" points=\"40.0,30.0 42.2,42.2 44.5,53.9 46.8,65.1 49.0,75.8 51.2,86.1 53.5,95.9 55.8,105.3 58.0,114.4 60.2,123.0 62.5,131.3 64.8,139.2 67.0,146.8 69.2,154.0 71.5,161.0 73.8,167.6 76.0,174.0 78.2,180.1 80.5,186.0 82.8,191.5 85.0,196.9 87.2,202.0 89.5,207.0 91.8,211.7 94.0,216.2 96.2,220.5 98.5,224.6 100.8,228.6 103.0,232.4 105.2,236.0 107.5,239.5 109.8,242.8 112.0,246.0 114.2,249.1 116.5,252.0 118.8,254.8 121.0,257.5 123.2,260.0 125.5,262.5 127.8,264.8 130.0,267.1 132.2,269.2 134.5,271.3 136.8,273.3 139.0,275.2 141.2,277.0 143.5,278.7 145.8,280.4 148.0,282.0 150.2,283.5 152.5,285.0 154.8,286.4 157.0,287.7 159.2,289.0 161.5,290.2 163.8,291.4 166.0,292.5 168.2,293.6 170.5,294.7 172.8,295.6 175.0,296.6 177.2,297.5 179.5,298.4 181.8,299.2 184.0,300.0 186.2,300.8 188.5,301.5 190.8,302.2 193.0,302.9 195.2,303.5 197.5,304.1 199.8,304.7 202.0,305.3 204.2,305.8 206.5,306.3 208.8,306.8 211.0,307.3 213.2,307.8 215.5,308.2 217.8,308.6 220.0,309.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(0, 800)</text><circle cx=\"76.0\" cy=\"174.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"168.0\" fill=\"#222\" font-size=\"11\">(1, 400)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 200)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een postzegelverzameling groeit met groeifactor 1,025 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,025¹² ≈ 1,345. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "1,104",
        "1,300",
        "1,345",
        "12,300"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 200 · 0,90ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 200 · 0,73ᵗ",
      "sleutelwoorden": [
        "0,73/0.73"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 0,90³ ≈ 0,73. De beginwaarde blijft 200: A = 200 · 0,73ᵗ."
    }
  ]
});
