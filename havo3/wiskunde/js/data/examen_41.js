/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 41 — §1.5 Groeifactor en tijd (2/5, oefenen)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-31",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 41 — §1.5 Groeifactor en tijd (2/5, oefenen)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,1 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "1,21",
      "uitleg": "Per twee weken zijn er twee stappen: 1,1 · 1,1 = 1,1² = 1,21.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,8ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,26",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 0,8⁶ ≈ 0,2621 ≈ 0,26.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "De waarde van een postzegelverzameling groeit met groeifactor 1,019 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,019¹² ≈ 1,253. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "1,078",
        "1,228",
        "12,228",
        "1,253"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 1000 · 1,04ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 1,04⁴ ≈ 1,17. De beginwaarde (1000) blijft hetzelfde.",
      "opties": [
        "A = 1000 · 1,17ᵗ",
        "A = 4000 · 1,04ᵗ",
        "A = 1000 · 4,16ᵗ",
        "A = 1170 · 1,17ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit met 2% per jaar. Dat is hetzelfde als een groei van 40% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,02²⁰ ≈ 1,486, dus ongeveer 48,6% groei, niet 40%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,025 per uur. Nu is de hoeveelheid 320.000. Hoe groot was de hoeveelheid 5 uur eerder? Rond af op een geheel getal.",
      "antwoord": "282833",
      "uitleg": "Groeifactor per 5 uur: 1,025⁵. Terugrekenen = delen: 320.000 : 1,025⁵ ≈ 282833.",
      "tolerantie": 141
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 1,019ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 1,019 = 101,9%, dus toename van 1,9% per maand.",
      "opties": [
        "+19% per maand",
        "+1,9% per maand",
        "+0,19% per maand",
        "−1,9% per maand"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 2400. Bereken de groeifactor per uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,0625",
      "uitleg": "Per kwartier: 1200 : 2400 = 0,5. Een uur is 4 kwartier: 0,5⁴ = 0,0625.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 254\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"254\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c45\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"180.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"210.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"210.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"210.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"210.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"210.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"210.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">1000</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">1500</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">2000</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">2500</text><text x=\"35.0\" y=\"225.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"214.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"246.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c45)\" points=\"40.0,37.2 42.2,44.5 44.5,51.5 46.8,58.3 49.0,64.7 51.2,70.9 53.5,76.8 55.8,82.4 58.0,87.8 60.2,93.0 62.5,98.0 64.8,102.7 67.0,107.3 69.2,111.6 71.5,115.8 73.8,119.8 76.0,123.6 78.2,127.3 80.5,130.8 82.8,134.1 85.0,137.3 87.2,140.4 89.5,143.4 91.8,146.2 94.0,148.9 96.2,151.5 98.5,154.0 100.8,156.4 103.0,158.6 105.2,160.8 107.5,162.9 109.8,164.9 112.0,166.8 114.2,168.6 116.5,170.4 118.8,172.1 121.0,173.7 123.2,175.2 125.5,176.7 127.8,178.1 130.0,179.5 132.2,180.7 134.5,182.0 136.8,183.2 139.0,184.3 141.2,185.4 143.5,186.4 145.8,187.4 148.0,188.4 150.2,189.3 152.5,190.2 154.8,191.0 157.0,191.8 159.2,192.6 161.5,193.3 163.8,194.1 166.0,194.7 168.2,195.4 170.5,196.0 172.8,196.6 175.0,197.2 177.2,197.7 179.5,198.2 181.8,198.7 184.0,199.2 186.2,199.7 188.5,200.1 190.8,200.5 193.0,200.9 195.2,201.3 197.5,201.7 199.8,202.0 202.0,202.4 204.2,202.7 206.5,203.0 208.8,203.3 211.0,203.6 213.2,203.9 215.5,204.1 217.8,204.4 220.0,204.6\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"37.2\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"31.2\" fill=\"#222\" font-size=\"11\">(0, 2400)</text><circle cx=\"76.0\" cy=\"123.6\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"117.6\" fill=\"#222\" font-size=\"11\">(1, 1200)</text><circle cx=\"112.0\" cy=\"166.8\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"160.8\" fill=\"#222\" font-size=\"11\">(2, 600)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp verandert exponentieel: 6400 in 2020 en 3200 in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?",
      "uitleg": "Groeifactor per jaar: 3200 : 6400 = 0,5. Per drie jaar: 0,5³ = 0,125.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 284 62\" width=\"284\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"282\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"83\" y1=\"1\" x2=\"83\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"133\" y1=\"1\" x2=\"133\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"183\" y1=\"1\" x2=\"183\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"208.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"233\" y1=\"1\" x2=\"233\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">inwoners</text><line x1=\"83\" y1=\"31\" x2=\"83\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"108.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">6400</text><line x1=\"133\" y1=\"31\" x2=\"133\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"158.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">3200</text><line x1=\"183\" y1=\"31\" x2=\"183\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"208.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">1600</text><line x1=\"233\" y1=\"31\" x2=\"233\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"258.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">800</text><line x1=\"1\" y1=\"31\" x2=\"283\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "0,125",
        "1,5",
        "0,5",
        "−0,5"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de groeifactor per jaar 1,07 is, dan is de groeifactor per 3 jaar gelijk aan 1,07³.",
      "antwoord": true,
      "uitleg": "Waar. Elk jaar vermenigvuldig je met 1,07; na 3 jaar dus 3 keer: 1,07³."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 300 · 1,019ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "590,73",
      "uitleg": "Na 3 jaar is t = 36: W = 300 · 1,019³⁶ ≈ 590,73 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,6 per 10 minuten, soort B met groeifactor 30 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,6⁶ ≈ 16,8. Vergelijk met 30: soort B groeit het snelst.",
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
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,9 per halfjaar. Bereken de groeifactor per jaar.",
      "antwoord": "0,81",
      "uitleg": "Per jaar zijn er twee stappen: 0,9 · 0,9 = 0,9² = 0,81.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,1ᵗ is t de tijd in kwartieren. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,46",
      "uitleg": "In een uur passen 4 keer kwartier. Groeifactor per uur: 1,1⁴ ≈ 1,4641 ≈ 1,46.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal leden van een club groeit met 5% per jaar. Dat is hetzelfde als een groei van 100% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,05²⁰ ≈ 2,653, dus ongeveer 165,3% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,025 per maand. Nu is de hoeveelheid 2000. Hoe groot was de hoeveelheid 4 maanden eerder? Rond af op een geheel getal.",
      "antwoord": "1812",
      "uitleg": "Groeifactor per 4 maanden: 1,025⁴. Terugrekenen = delen: 2000 : 1,025⁴ ≈ 1812.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 80 · 1,04ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 1,04⁴ ≈ 1,17. De beginwaarde (80) blijft hetzelfde.",
      "opties": [
        "A = 80 · 4,16ᵗ",
        "A = 80 · 1,17ᵗ",
        "A = 94 · 1,17ᵗ",
        "A = 320 · 1,04ᵗ"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de groei van een aantal bacteriën zien; op t = 0 zijn het er 40. Bereken de groeifactor per half uur.",
      "antwoord": "4",
      "uitleg": "Per kwartier: 80 : 40 = 2. Een half uur is 2 kwartier: 2² = 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 326\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"326\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c46\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"252.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"282.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"282.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"282.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"282.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"282.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"286.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"318.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c46)\" points=\"40.0,267.6 42.2,267.0 44.5,266.3 46.8,265.6 49.0,264.9 51.2,264.1 53.5,263.3 55.8,262.5 58.0,261.6 60.2,260.7 62.5,259.8 64.8,258.8 67.0,257.8 69.2,256.7 71.5,255.6 73.8,254.4 76.0,253.2 78.2,251.9 80.5,250.6 82.8,249.2 85.0,247.8 87.2,246.2 89.5,244.7 91.8,243.0 94.0,241.3 96.2,239.5 98.5,237.6 100.8,235.6 103.0,233.6 105.2,231.4 107.5,229.2 109.8,226.8 112.0,224.4 114.2,221.8 116.5,219.2 118.8,216.4 121.0,213.5 123.2,210.5 125.5,207.3 127.8,204.0 130.0,200.5 132.2,196.9 134.5,193.2 136.8,189.2 139.0,185.1 141.2,180.8 143.5,176.4 145.8,171.7 148.0,166.8 150.2,161.7 152.5,156.4 154.8,150.8 157.0,145.0 159.2,138.9 161.5,132.6 163.8,126.0 166.0,119.1 168.2,111.9 170.5,104.3 172.8,96.5 175.0,88.3 177.2,79.7 179.5,70.7 181.8,61.4 184.0,51.6 186.2,41.4 188.5,30.7 190.8,19.6 193.0,8.0 195.2,-4.1 197.5,-16.8 199.8,-30.0 202.0,-43.8 204.2,-58.3 206.5,-73.3 208.8,-89.1 211.0,-105.5 213.2,-122.6 215.5,-140.6 217.8,-159.3 220.0,-178.8\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"267.6\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"261.6\" fill=\"#222\" font-size=\"11\">(0, 40)</text><circle cx=\"76.0\" cy=\"253.2\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"247.2\" fill=\"#222\" font-size=\"11\">(1, 80)</text><circle cx=\"112.0\" cy=\"224.4\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"218.4\" fill=\"#222\" font-size=\"11\">(2, 160)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een stripboek groeit met groeifactor 1,025 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,025¹² ≈ 1,345. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "12,300",
        "1,300",
        "1,104",
        "1,345"
      ],
      "antwoord": 3
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 500 · 1,04ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 500 · 1,12ᵗ",
      "sleutelwoorden": [
        "1,12/1.12"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,04³ ≈ 1,12. De beginwaarde blijft 500: A = 500 · 1,12ᵗ."
    }
  ]
});
