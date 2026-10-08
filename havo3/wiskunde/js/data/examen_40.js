/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 40 — §1.5 Groeifactor en tijd (1/5, basis)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-30",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 40 — §1.5 Groeifactor en tijd (1/5, basis)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 2,4 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "5,76",
      "uitleg": "Per twee weken zijn er twee stappen: 2,4 · 2,4 = 2,4² = 5,76.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,05ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,22",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 1,05⁴ ≈ 1,2155 ≈ 1,22.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "De waarde van een aandeel groeit met groeifactor 0,985 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,985¹² ≈ 0,834. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,941",
        "11,820",
        "0,834",
        "0,820"
      ],
      "antwoord": 2
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 200 · 1,06ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 1,06⁴ ≈ 1,26. De beginwaarde (200) blijft hetzelfde.",
      "opties": [
        "A = 800 · 1,06ᵗ",
        "A = 200 · 1,26ᵗ",
        "A = 252 · 1,26ᵗ",
        "A = 200 · 4,24ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal leden van een club groeit met 3% per jaar. Dat is hetzelfde als een groei van 30% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,03¹⁰ ≈ 1,344, dus ongeveer 34,4% groei, niet 30%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,1 per maand. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 5 maanden eerder? Rond af op een geheel getal.",
      "antwoord": "198695",
      "uitleg": "Groeifactor per 5 maanden: 1,1⁵. Terugrekenen = delen: 320.000 : 1,1⁵ ≈ 198695.",
      "tolerantie": 99
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 1,008ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 1,008 = 100,8%, dus toename van 0,8% per maand.",
      "opties": [
        "+0,08% per maand",
        "+8% per maand",
        "−0,8% per maand",
        "+0,8% per maand"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de groei van een aantal bacteriën zien; op t = 0 zijn het er 50. Bereken de groeifactor per uur.",
      "antwoord": "16",
      "uitleg": "Per kwartier: 100 : 50 = 2. Een uur is 4 kwartier: 2⁴ = 16.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c43\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c43)\" points=\"40.0,300.0 42.2,299.2 44.5,298.4 46.8,297.5 49.0,296.6 51.2,295.6 53.5,294.7 55.8,293.6 58.0,292.5 60.2,291.4 62.5,290.2 64.8,289.0 67.0,287.7 69.2,286.4 71.5,285.0 73.8,283.5 76.0,282.0 78.2,280.4 80.5,278.7 82.8,277.0 85.0,275.2 87.2,273.3 89.5,271.3 91.8,269.2 94.0,267.1 96.2,264.8 98.5,262.5 100.8,260.0 103.0,257.5 105.2,254.8 107.5,252.0 109.8,249.1 112.0,246.0 114.2,242.8 116.5,239.5 118.8,236.0 121.0,232.4 123.2,228.6 125.5,224.6 127.8,220.5 130.0,216.2 132.2,211.7 134.5,207.0 136.8,202.0 139.0,196.9 141.2,191.5 143.5,186.0 145.8,180.1 148.0,174.0 150.2,167.6 152.5,161.0 154.8,154.0 157.0,146.8 159.2,139.2 161.5,131.3 163.8,123.0 166.0,114.4 168.2,105.3 170.5,95.9 172.8,86.1 175.0,75.8 177.2,65.1 179.5,53.9 181.8,42.2 184.0,30.0 186.2,17.2 188.5,3.9 190.8,-10.0 193.0,-24.5 195.2,-39.7 197.5,-55.5 199.8,-72.0 202.0,-89.3 204.2,-107.3 206.5,-126.2 208.8,-145.8 211.0,-166.4 213.2,-187.8 215.5,-210.2 217.8,-233.6 220.0,-258.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"300.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"294.0\" fill=\"#222\" font-size=\"11\">(0, 50)</text><circle cx=\"76.0\" cy=\"282.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"276.0\" fill=\"#222\" font-size=\"11\">(1, 100)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 200)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp verandert exponentieel: 12.800 in 2020 en 16.000 in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?",
      "uitleg": "Groeifactor per jaar: 16.000 : 12.800 = 1,25. Per drie jaar: 1,25³ = 1,953125.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 348 62\" width=\"348\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"346\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"83\" y1=\"1\" x2=\"83\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"149\" y1=\"1\" x2=\"149\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"281\" y1=\"1\" x2=\"281\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">inwoners</text><line x1=\"83\" y1=\"31\" x2=\"83\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">12.800</text><line x1=\"149\" y1=\"31\" x2=\"149\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">16.000</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">20.000</text><line x1=\"281\" y1=\"31\" x2=\"281\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">25.000</text><line x1=\"1\" y1=\"31\" x2=\"347\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "1,953125",
        "3,75",
        "1,25",
        "1,75"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de groeifactor per jaar 0,95 is, dan is de groeifactor per 3 jaar gelijk aan 0,95³.",
      "antwoord": true,
      "uitleg": "Waar. Elk jaar vermenigvuldig je met 0,95; na 3 jaar dus 3 keer: 0,95³."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 120 · 1,019ᵗ, met t in maanden. Hoeveel dollar is de vaas na 2 jaar waard? Rond af op twee decimalen.",
      "antwoord": "188,52",
      "uitleg": "Na 2 jaar is t = 24: W = 120 · 1,019²⁴ ≈ 188,52 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,5 per 10 minuten, soort B met groeifactor 30 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,5⁶ ≈ 11,4. Vergelijk met 30: soort B groeit het snelst.",
      "opties": [
        "ze groeien even snel",
        "dat kun je niet vergelijken",
        "soort B",
        "soort A"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,9 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "0,81",
      "uitleg": "Per twee weken zijn er twee stappen: 0,9 · 0,9 = 0,9² = 0,81.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,2ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "2,99",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 1,2⁶ ≈ 2,9860 ≈ 2,99.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "De bevolking groeit met 10% per jaar. Dat is hetzelfde als een groei van 100% in 10 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 10 jaar is 1,1¹⁰ ≈ 2,594, dus ongeveer 159,4% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,1 per uur. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 5 uur eerder? Rond af op een geheel getal.",
      "antwoord": "198695",
      "uitleg": "Groeifactor per 5 uur: 1,1⁵. Terugrekenen = delen: 320.000 : 1,1⁵ ≈ 198695.",
      "tolerantie": 99
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 80 · 1,10ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 1,10⁴ ≈ 1,46. De beginwaarde (80) blijft hetzelfde.",
      "opties": [
        "A = 80 · 1,46ᵗ",
        "A = 320 · 1,10ᵗ",
        "A = 80 · 4,40ᵗ",
        "A = 117 · 1,46ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 1200. Bereken de groeifactor per half uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,25",
      "uitleg": "Per kwartier: 600 : 1200 = 0,5. Een half uur is 2 kwartier: 0,5² = 0,25.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c44\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">150</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">450</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">750</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">900</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">1050</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">1200</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c44)\" points=\"40.0,30.0 42.2,42.2 44.5,53.9 46.8,65.1 49.0,75.8 51.2,86.1 53.5,95.9 55.8,105.3 58.0,114.4 60.2,123.0 62.5,131.3 64.8,139.2 67.0,146.8 69.2,154.0 71.5,161.0 73.8,167.6 76.0,174.0 78.2,180.1 80.5,186.0 82.8,191.5 85.0,196.9 87.2,202.0 89.5,207.0 91.8,211.7 94.0,216.2 96.2,220.5 98.5,224.6 100.8,228.6 103.0,232.4 105.2,236.0 107.5,239.5 109.8,242.8 112.0,246.0 114.2,249.1 116.5,252.0 118.8,254.8 121.0,257.5 123.2,260.0 125.5,262.5 127.8,264.8 130.0,267.1 132.2,269.2 134.5,271.3 136.8,273.3 139.0,275.2 141.2,277.0 143.5,278.7 145.8,280.4 148.0,282.0 150.2,283.5 152.5,285.0 154.8,286.4 157.0,287.7 159.2,289.0 161.5,290.2 163.8,291.4 166.0,292.5 168.2,293.6 170.5,294.7 172.8,295.6 175.0,296.6 177.2,297.5 179.5,298.4 181.8,299.2 184.0,300.0 186.2,300.8 188.5,301.5 190.8,302.2 193.0,302.9 195.2,303.5 197.5,304.1 199.8,304.7 202.0,305.3 204.2,305.8 206.5,306.3 208.8,306.8 211.0,307.3 213.2,307.8 215.5,308.2 217.8,308.6 220.0,309.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(0, 1200)</text><circle cx=\"76.0\" cy=\"174.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"168.0\" fill=\"#222\" font-size=\"11\">(1, 600)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 300)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een stripboek groeit met groeifactor 0,985 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,985¹² ≈ 0,834. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,820",
        "0,834",
        "11,820",
        "0,941"
      ],
      "antwoord": 1
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 1000 · 1,06ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 1000 · 1,19ᵗ",
      "sleutelwoorden": [
        "1,19/1.19"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,06³ ≈ 1,19. De beginwaarde blijft 1000: A = 1000 · 1,19ᵗ."
    }
  ]
});
