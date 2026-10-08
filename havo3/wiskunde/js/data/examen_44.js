/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 44 — §1.5 Groeifactor en tijd (5/5, eindniveau)
   Bron: Noordhoff H1 Lineaire en exponentiële formules, §1.5 (opgaven uit het boek met andere getallen;
   antwoorden berekend door tools-script, figuren als inline SVG)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-34",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Proeftoets 44 — §1.5 Groeifactor en tijd (5/5, eindniveau)",
  "vak": "Wiskunde · H1 Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 0,8 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "0,64",
      "uitleg": "Per twee weken zijn er twee stappen: 0,8 · 0,8 = 0,8² = 0,64.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 1,05ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "1,34",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 1,05⁶ ≈ 1,3401 ≈ 1,34.",
      "tolerantie": 0.006
    },
    {
      "type": "mc",
      "vraag": "De waarde van een aandeel groeit met groeifactor 1,015 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,015¹² ≈ 1,196. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "12,180",
        "1,196",
        "1,061",
        "1,180"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 1000 · 1,10ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 1,10³ ≈ 1,33. De beginwaarde (1000) blijft hetzelfde.",
      "opties": [
        "A = 1331 · 1,33ᵗ",
        "A = 3000 · 1,10ᵗ",
        "A = 1000 · 3,30ᵗ",
        "A = 1000 · 1,33ᵗ"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Een hoeveelheid groeit met 5% per jaar. Dat is hetzelfde als een groei van 100% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,05²⁰ ≈ 2,653, dus ongeveer 165,3% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,12 per jaar. Nu is de hoeveelheid 254.200. Hoe groot was de hoeveelheid 4 jaar eerder? Rond af op een geheel getal.",
      "antwoord": "161549",
      "uitleg": "Groeifactor per 4 jaar: 1,12⁴. Terugrekenen = delen: 254.200 : 1,12⁴ ≈ 161549.",
      "tolerantie": 80
    },
    {
      "type": "mc",
      "vraag": "De waarde W van een vaas wordt berekend met W = 20 · 0,96ᵗ, met t in maanden. Wat gebeurt er per maand met de waarde?",
      "uitleg": "Groeifactor 0,96 = 96%, dus afname van 4% per maand.",
      "opties": [
        "−4% per maand",
        "−40% per maand",
        "+4% per maand",
        "−0,4% per maand"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de groei van een aantal bacteriën zien; op t = 0 zijn het er 50. Bereken de groeifactor per half uur.",
      "antwoord": "4",
      "uitleg": "Per kwartier: 100 : 50 = 2. Een half uur is 2 kwartier: 2² = 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c56\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c56)\" points=\"40.0,300.0 42.2,299.2 44.5,298.4 46.8,297.5 49.0,296.6 51.2,295.6 53.5,294.7 55.8,293.6 58.0,292.5 60.2,291.4 62.5,290.2 64.8,289.0 67.0,287.7 69.2,286.4 71.5,285.0 73.8,283.5 76.0,282.0 78.2,280.4 80.5,278.7 82.8,277.0 85.0,275.2 87.2,273.3 89.5,271.3 91.8,269.2 94.0,267.1 96.2,264.8 98.5,262.5 100.8,260.0 103.0,257.5 105.2,254.8 107.5,252.0 109.8,249.1 112.0,246.0 114.2,242.8 116.5,239.5 118.8,236.0 121.0,232.4 123.2,228.6 125.5,224.6 127.8,220.5 130.0,216.2 132.2,211.7 134.5,207.0 136.8,202.0 139.0,196.9 141.2,191.5 143.5,186.0 145.8,180.1 148.0,174.0 150.2,167.6 152.5,161.0 154.8,154.0 157.0,146.8 159.2,139.2 161.5,131.3 163.8,123.0 166.0,114.4 168.2,105.3 170.5,95.9 172.8,86.1 175.0,75.8 177.2,65.1 179.5,53.9 181.8,42.2 184.0,30.0 186.2,17.2 188.5,3.9 190.8,-10.0 193.0,-24.5 195.2,-39.7 197.5,-55.5 199.8,-72.0 202.0,-89.3 204.2,-107.3 206.5,-126.2 208.8,-145.8 211.0,-166.4 213.2,-187.8 215.5,-210.2 217.8,-233.6 220.0,-258.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"300.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"294.0\" fill=\"#222\" font-size=\"11\">(0, 50)</text><circle cx=\"76.0\" cy=\"282.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"276.0\" fill=\"#222\" font-size=\"11\">(1, 100)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 200)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "Het aantal inwoners van een dorp verandert exponentieel: 25.600 in 2020 en 19.200 in 2021 (zie tabel). Hoe groot is de groeifactor per drie jaar?",
      "uitleg": "Groeifactor per jaar: 19.200 : 25.600 = 0,75. Per drie jaar: 0,75³ = 0,421875.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 348 62\" width=\"348\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"346\" height=\"60\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">jaar</text><line x1=\"83\" y1=\"1\" x2=\"83\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2020</text><line x1=\"149\" y1=\"1\" x2=\"149\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2021</text><line x1=\"215\" y1=\"1\" x2=\"215\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2022</text><line x1=\"281\" y1=\"1\" x2=\"281\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2023</text><rect x=\"1\" y=\"31\" width=\"82\" height=\"30\" fill=\"#fde7ef\"/><text x=\"42.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">inwoners</text><line x1=\"83\" y1=\"31\" x2=\"83\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"116.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">25.600</text><line x1=\"149\" y1=\"31\" x2=\"149\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"182.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">19.200</text><line x1=\"215\" y1=\"31\" x2=\"215\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"248.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">14.400</text><line x1=\"281\" y1=\"31\" x2=\"281\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"314.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">10.800</text><line x1=\"1\" y1=\"31\" x2=\"347\" y2=\"31\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "0,25",
        "0,75",
        "2,25",
        "0,421875"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de groeifactor per jaar 1,3 is, dan is de groeifactor per 3 jaar gelijk aan 1,3³.",
      "antwoord": true,
      "uitleg": "Waar. Elk jaar vermenigvuldig je met 1,3; na 3 jaar dus 3 keer: 1,3³."
    },
    {
      "type": "invul",
      "vraag": "De waarde W in dollars van een vaas is W = 50 · 1,025ᵗ, met t in maanden. Hoeveel dollar is de vaas na 3 jaar waard? Rond af op twee decimalen.",
      "antwoord": "121,63",
      "uitleg": "Na 3 jaar is t = 36: W = 50 · 1,025³⁶ ≈ 121,63 dollar.",
      "tolerantie": 0.02
    },
    {
      "type": "mc",
      "vraag": "Soort A groeit met groeifactor 1,9 per 10 minuten, soort B met groeifactor 8 per uur. Welke soort groeit het snelst?",
      "uitleg": "Zet A om naar een uur (6 × 10 minuten): 1,9⁶ ≈ 47,0. Vergelijk met 8: soort A groeit het snelst.",
      "opties": [
        "dat kun je niet vergelijken",
        "soort A",
        "ze groeien even snel",
        "soort B"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,3 per week. Bereken de groeifactor per twee weken.",
      "antwoord": "1,69",
      "uitleg": "Per twee weken zijn er twee stappen: 1,3 · 1,3 = 1,3² = 1,69.",
      "tolerantie": 0.0005
    },
    {
      "type": "invul",
      "vraag": "In de formule A = 10 · 0,9ᵗ is t de tijd in eenheden van tien minuten. Bereken de groeifactor per uur. Rond af op twee decimalen.",
      "antwoord": "0,53",
      "uitleg": "In een uur passen 6 keer tien minuten. Groeifactor per uur: 0,9⁶ ≈ 0,5314 ≈ 0,53.",
      "tolerantie": 0.006
    },
    {
      "type": "waaronwaar",
      "vraag": "Een spaarbedrag groeit met 5% per jaar. Dat is hetzelfde als een groei van 100% in 20 jaar.",
      "antwoord": false,
      "uitleg": "Onwaar. De groeifactor per 20 jaar is 1,05²⁰ ≈ 2,653, dus ongeveer 165,3% groei, niet 100%."
    },
    {
      "type": "invul",
      "vraag": "Een hoeveelheid groeit exponentieel met groeifactor 1,1 per uur. Nu is de hoeveelheid 8000. Hoe groot was de hoeveelheid 3 uur eerder? Rond af op een geheel getal.",
      "antwoord": "6011",
      "uitleg": "Groeifactor per 3 uur: 1,1³. Terugrekenen = delen: 8000 : 1,1³ ≈ 6011.",
      "tolerantie": 3
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 200 · 1,06ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 1,06³ ≈ 1,19. De beginwaarde (200) blijft hetzelfde.",
      "opties": [
        "A = 200 · 1,19ᵗ",
        "A = 200 · 3,18ᵗ",
        "A = 600 · 1,06ᵗ",
        "A = 238 · 1,19ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 1000. Bereken de groeifactor per half uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,25",
      "uitleg": "Per kwartier: 500 : 1000 = 0,5. Een half uur is 2 kwartier: 0,5² = 0,25.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 326\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"326\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c58\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"252.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"282.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"282.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"282.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"282.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"282.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">150</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">450</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">750</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">900</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">1050</text><text x=\"35.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"286.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"318.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c58)\" points=\"40.0,42.0 42.2,52.2 44.5,61.9 46.8,71.2 49.0,80.2 51.2,88.7 53.5,96.9 55.8,104.8 58.0,112.3 60.2,119.5 62.5,126.4 64.8,133.0 67.0,139.3 69.2,145.3 71.5,151.1 73.8,156.7 76.0,162.0 78.2,167.1 80.5,172.0 82.8,176.6 85.0,181.1 87.2,185.4 89.5,189.5 91.8,193.4 94.0,197.1 96.2,200.7 98.5,204.2 100.8,207.5 103.0,210.6 105.2,213.7 107.5,216.6 109.8,219.3 112.0,222.0 114.2,224.5 116.5,227.0 118.8,229.3 121.0,231.5 123.2,233.7 125.5,235.7 127.8,237.7 130.0,239.6 132.2,241.4 134.5,243.1 136.8,244.7 139.0,246.3 141.2,247.8 143.5,249.3 145.8,250.7 148.0,252.0 150.2,253.3 152.5,254.5 154.8,255.7 157.0,256.8 159.2,257.8 161.5,258.9 163.8,259.8 166.0,260.8 168.2,261.7 170.5,262.5 172.8,263.4 175.0,264.2 177.2,264.9 179.5,265.6 181.8,266.3 184.0,267.0 186.2,267.6 188.5,268.2 190.8,268.8 193.0,269.4 195.2,269.9 197.5,270.4 199.8,270.9 202.0,271.4 204.2,271.8 206.5,272.3 208.8,272.7 211.0,273.1 213.2,273.5 215.5,273.8 217.8,274.2 220.0,274.5\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"42.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"36.0\" fill=\"#222\" font-size=\"11\">(0, 1000)</text><circle cx=\"76.0\" cy=\"162.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"156.0\" fill=\"#222\" font-size=\"11\">(1, 500)</text><circle cx=\"112.0\" cy=\"222.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"216.0\" fill=\"#222\" font-size=\"11\">(2, 250)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een stripboek groeit met groeifactor 0,970 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,970¹² ≈ 0,694. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "0,885",
        "0,640",
        "0,694",
        "11,640"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 200 · 1,10ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 200 · 1,33ᵗ",
      "sleutelwoorden": [
        "1,33/1.33"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 1,10³ ≈ 1,33. De beginwaarde blijft 200: A = 200 · 1,33ᵗ."
    }
  ]
});
