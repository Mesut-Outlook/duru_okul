/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 42 — §1.5 Groeifactor en tijd (3/5, gemengd)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-32",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 42 — §1.5 Groeifactor en tijd (3/5, gemengd)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,8 per half uur. Bereken de groeifactor per uur.",
      "antwoord": "0,64",
      "uitleg": "Per uur zijn er twee stappen: 0,8 · 0,8 = 0,8² = 0,64.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,3ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "2,20",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 1,3³ ≈ 2,1970 ≈ 2,20.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "De waarde van een stripboek groeit met groeifactor 1,019 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,019¹² ≈ 1,253. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "1,253",
        "1,078",
        "1,228",
        "12,228"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 80 · 1,06ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 1,06³ ≈ 1,19. De beginwaarde (80) blijft hetzelfde.",
      "opties": [
        "A = 95 · 1,19ᵗ",
        "A = 80 · 1,19ᵗ",
        "A = 80 · 3,18ᵗ",
        "A = 240 · 1,06ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal leden van een club groeit met 10% per jaar. Dat is hetzelfde als een groei van 200% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,1²⁰ ≈ 6,727, dus ongeveer 572,7% groei, niet 200%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,07 per uur. Nu is de hoeveelheid 254.200. Hoe groot was de hoeveelheid 4 uur eerder? Rond af op een geheel getal.",
      "antwoord": "193928",
      "uitleg": "Groeifactor per 4 uur: 1,07⁴. Terugrekenen = delen: 254.200 : 1,07⁴ ≈ 193928.",
      "tolerantie": 96
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 1,035ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 1,035 = 103,5%, dus toename van 3,5% per maand.",
      "opties": [
        "−3,5% per maand",
        "+35% per maand",
        "+0,35% per maand",
        "+3,5% per maand"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 1600. Bereken de groeifactor per uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,0625",
      "uitleg": "Per kwartier: 800 : 1600 = 0,5. Een uur is 4 kwartier: 0,5⁴ = 0,0625.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c47\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">1000</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">1200</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">1400</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">1600</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c47)\" points=\"40.0,30.0 42.2,42.2 44.5,53.9 46.8,65.1 49.0,75.8 51.2,86.1 53.5,95.9 55.8,105.3 58.0,114.4 60.2,123.0 62.5,131.3 64.8,139.2 67.0,146.8 69.2,154.0 71.5,161.0 73.8,167.6 76.0,174.0 78.2,180.1 80.5,186.0 82.8,191.5 85.0,196.9 87.2,202.0 89.5,207.0 91.8,211.7 94.0,216.2 96.2,220.5 98.5,224.6 100.8,228.6 103.0,232.4 105.2,236.0 107.5,239.5 109.8,242.8 112.0,246.0 114.2,249.1 116.5,252.0 118.8,254.8 121.0,257.5 123.2,260.0 125.5,262.5 127.8,264.8 130.0,267.1 132.2,269.2 134.5,271.3 136.8,273.3 139.0,275.2 141.2,277.0 143.5,278.7 145.8,280.4 148.0,282.0 150.2,283.5 152.5,285.0 154.8,286.4 157.0,287.7 159.2,289.0 161.5,290.2 163.8,291.4 166.0,292.5 168.2,293.6 170.5,294.7 172.8,295.6 175.0,296.6 177.2,297.5 179.5,298.4 181.8,299.2 184.0,300.0 186.2,300.8 188.5,301.5 190.8,302.2 193.0,302.9 195.2,303.5 197.5,304.1 199.8,304.7 202.0,305.3 204.2,305.8 206.5,306.3 208.8,306.8 211.0,307.3 213.2,307.8 215.5,308.2 217.8,308.6 220.0,309.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(0, 1600)</text><circle cx=\"76.0\" cy=\"174.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"168.0\" fill=\"#222\" font-size=\"11\">(1, 800)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 400)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp verandert exponentieel: 6400 in 2020 en 4800 in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?",
      "uitleg": "Groeifactor per jaar: 4800 : 6400 = 0,75. Per drie jaar: 0,75³ = 0,421875.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 62\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"282\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"83\" y1=\"1\" x2=\"83\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"133\" y1=\"1\" x2=\"133\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"183\" y1=\"1\" x2=\"183\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"208.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"233\" y1=\"1\" x2=\"233\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">inwoners</text><line x1=\"83\" y1=\"31\" x2=\"83\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6400</text><line x1=\"133\" y1=\"31\" x2=\"133\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">4800</text><line x1=\"183\" y1=\"31\" x2=\"183\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"208.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3600</text><line x1=\"233\" y1=\"31\" x2=\"233\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">2700</text><line x1=\"1\" y1=\"31\" x2=\"283\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "2,25",
        "0,25",
        "0,75",
        "0,421875"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de groeifactor per jaar 1,3 is, dan is de groeifactor per 2 jaar gelijk aan 1,3².",
      "antwoord": true,
      "uitleg": "Waar. Elk jaar vermenigvuldig je met 1,3; na 2 jaar dus 2 keer: 1,3²."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 300 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "729,76",
      "uitleg": "Na 3 jaar is t = 36: W = 300 · 1,025³⁶ ≈ 729,76 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,4 per 10 minuten, soort B met groeifactor 19 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,4⁶ ≈ 7,5. Vergelijk met 19: soort B groeit het snelst.",
      "opties": [
        "soort B",
        "ze groeien even snel",
        "soort A",
        "dat kun je niet vergelijken"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,5 per halfjaar. Bereken de groeifactor per jaar.",
      "antwoord": "2,25",
      "uitleg": "Per jaar zijn er twee stappen: 1,5 · 1,5 = 1,5² = 2,25.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,8ᵗ is t de tijd in eenheden van twintig minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,51",
      "uitleg": "In een uur passen 3 keer twintig minuten. Groeifactor per uur: 0,8³ ≈ 0,5120 ≈ 0,51.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "De bevolking groeit met 10% per jaar. Dat is hetzelfde als een groei van 200% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,1²⁰ ≈ 6,727, dus ongeveer 572,7% groei, niet 200%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per uur. Nu is de hoeveelheid 254.200. Hoe groot was de hoeveelheid 4 uur eerder? Rond af op een geheel getal.",
      "antwoord": "161549",
      "uitleg": "Groeifactor per 4 uur: 1,12⁴. Terugrekenen = delen: 254.200 : 1,12⁴ ≈ 161549.",
      "tolerantie": 80
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 200 · 1,04ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 1,04³ ≈ 1,12. De beginwaarde (200) blijft hetzelfde.",
      "opties": [
        "A = 225 · 1,12ᵗ",
        "A = 200 · 3,12ᵗ",
        "A = 200 · 1,12ᵗ",
        "A = 600 · 1,04ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 2400. Bereken de groeifactor per half uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,25",
      "uitleg": "Per kwartier: 1200 : 2400 = 0,5. Een half uur is 2 kwartier: 0,5² = 0,25.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 254\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"254\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c48\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"180.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"210.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"210.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"210.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"210.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"210.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"210.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">1000</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">1500</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">2000</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">2500</text><text x=\"35.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"214.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"246.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c48)\" points=\"40.0,37.2 42.2,44.5 44.5,51.5 46.8,58.3 49.0,64.7 51.2,70.9 53.5,76.8 55.8,82.4 58.0,87.8 60.2,93.0 62.5,98.0 64.8,102.7 67.0,107.3 69.2,111.6 71.5,115.8 73.8,119.8 76.0,123.6 78.2,127.3 80.5,130.8 82.8,134.1 85.0,137.3 87.2,140.4 89.5,143.4 91.8,146.2 94.0,148.9 96.2,151.5 98.5,154.0 100.8,156.4 103.0,158.6 105.2,160.8 107.5,162.9 109.8,164.9 112.0,166.8 114.2,168.6 116.5,170.4 118.8,172.1 121.0,173.7 123.2,175.2 125.5,176.7 127.8,178.1 130.0,179.5 132.2,180.7 134.5,182.0 136.8,183.2 139.0,184.3 141.2,185.4 143.5,186.4 145.8,187.4 148.0,188.4 150.2,189.3 152.5,190.2 154.8,191.0 157.0,191.8 159.2,192.6 161.5,193.3 163.8,194.1 166.0,194.7 168.2,195.4 170.5,196.0 172.8,196.6 175.0,197.2 177.2,197.7 179.5,198.2 181.8,198.7 184.0,199.2 186.2,199.7 188.5,200.1 190.8,200.5 193.0,200.9 195.2,201.3 197.5,201.7 199.8,202.0 202.0,202.4 204.2,202.7 206.5,203.0 208.8,203.3 211.0,203.6 213.2,203.9 215.5,204.1 217.8,204.4 220.0,204.6\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"37.2\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"31.2\" fill=\"#222\" font-size=\"11\">(0, 2400)</text><circle cx=\"76.0\" cy=\"123.6\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"117.6\" fill=\"#222\" font-size=\"11\">(1, 1200)</text><circle cx=\"112.0\" cy=\"166.8\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"160.8\" fill=\"#222\" font-size=\"11\">(2, 600)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een schilderij groeit met groeifactor 0,985 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,985¹² ≈ 0,834. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,820",
        "11,820",
        "0,834",
        "0,941"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 500 · 1,10ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 500 · 1,33ᵗ",
      "sleutelwoorden": [
        "1,33/1.33"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,10³ ≈ 1,33. De beginwaarde blijft 500: A = 500 · 1,33ᵗ."
    }
  ]
});
