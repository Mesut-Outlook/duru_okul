/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 84 — Gemengd H1 — Lineaire en exponentiële formules (1/10)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-gemengd-1",
  "hoofdstuk": 1,
  "titel": "Proeftoets 84 — Gemengd H1 — Lineaire en exponentiële formules (1/10)",
  "vak": "Wiskunde · Hoofdstuk 1 · Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = −7x + 4. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = −7x + 4. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: −7. Het losse getal is het startgetal: 4.",
      "opties": [
        "richtingscoëfficiënt 7 en startgetal 4",
        "richtingscoëfficiënt −7 en startgetal 4",
        "richtingscoëfficiënt 4 en startgetal −7",
        "richtingscoëfficiënt −7 en startgetal −4"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(5, 7) en Q(9, 3). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "-1",
      "uitleg": "rc = toename y / toename x = (3 − 7) / (9 − 5) = −4 / 4 = −1."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (10, −40) ligt op de lijn y = −4x.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = 10: y = −4 · 10 + 0 = −40. Dat is gelijk aan −40, dus het punt ligt op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (3, 6) en loopt evenwijdig aan lijn l: y = 6x − 11. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = 6. Invullen van (3, 6): 6 = 6 · 3 + b = 18 + b, dus b = −12. Lijn m: y = 6x − 12.",
      "opties": [
        "y = 6x − 12",
        "y = 6x + 6",
        "y = 6x + 24",
        "y = −6x + 24"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van het snijpunt van de lijnen y = 3x + 41 en y = 5x + 49.",
      "antwoord": "29",
      "uitleg": "3x + 41 = 5x + 49 geeft x = −4. Invullen: y = 3 · (−4) + 41 = 29. Controle in de andere formule: 29."
    },
    {
      "type": "mc",
      "vraag": "De lijnen y = 6x + 53 en y = −5x − 2 snijden elkaar in S. Met welke vergelijking bereken je de x-coördinaat van S?",
      "uitleg": "Op het snijpunt hebben beide lijnen dezelfde y. Stel daarom de twee formules aan elkaar gelijk.",
      "opties": [
        "6x + 53 = −5x − 2",
        "6x + 53 = −(−5x − 2)",
        "6x − 2 = −5x + 53",
        "6x + 53 = 0"
      ],
      "antwoord": 0
    },
    {
      "type": "waaronwaar",
      "vraag": "Het snijpunt van de lijnen y = −x − 16 en y = 2x − 7 is (−3, −11).",
      "antwoord": false,
      "uitleg": "Onwaar. Gelijkstellen geeft x = −3 en y = −13; het snijpunt is (−3, −13)."
    },
    {
      "type": "invul",
      "vraag": "In een spel spaar je credits. Bram heeft op dag 0 nog geen credits en krijgt er elke dag 2 miljoen bij. Sara begint op hetzelfde moment en spaart ook elke dag hetzelfde aantal: na 2 dagen heeft Sara 3 miljoen credits en na 8 dagen 18 miljoen. Na hoeveel dagen hebben ze evenveel credits?",
      "antwoord": "4",
      "uitleg": "Bram: c = 2t. Sara: rc = (18 − 3) / (8 − 2) = 2,5, b = 3 − 5 = −2. Gelijkstellen geeft t = 4 dagen."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 16 − 0,008h. Na k kwartier wandelen is de hoogte h = 15k + 400. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 16 − 0,008(15k + 400) = 16 − 0,12k − 3,2 = 12,8 − 0,12k.",
      "opties": [
        "T = −384 − 0,12k",
        "T = 416 − 0,12k",
        "T = 12,8 − 0,008k",
        "T = 12,8 − 0,12k"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 18 − 0,0065h en h = 8k + 200, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 16 kwartier.",
      "antwoord": "15,868",
      "uitleg": "h = 8 · 16 + 200 = 328. T = 18 − 0,0065 · 328 = 15,868 °C."
    },
    {
      "type": "invul",
      "vraag": "Iris is twee keer zo oud als Jesse (a = 2b). Kiki is 2 jaar jonger dan Iris (c = a − 2). Samen zijn ze 28 jaar. Hoe oud is Jesse?",
      "antwoord": "6",
      "uitleg": "a + b + c = 28. Substitueer a = 2b en c = 2b − 2: 2b + b + 2b − 2 = 28 → 5b = 30 → b = 6."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 3 − 4p substitueert in h = 3t + 3, krijg je h = −4p + 12.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 3(3 − 4p) + 3 = 9 − 12p + 3, dus h = −12p + 12. Zonder haakjes vergeet je 4p met 3 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,75 per uur. Om 08.00 uur zijn er 2400 muggen. Hoeveel muggen waren er om 07.00 uur? Rond af op een geheel getal.",
      "antwoord": "3200",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 2400 : 0,75 ≈ 3200,0 → 3200 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal downloads van een spel op vier meetpunten. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×0,5). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 214 152\" width=\"214\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"212\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"61\" y1=\"1\" x2=\"61\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"95\" y1=\"1\" x2=\"95\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"129\" y1=\"1\" x2=\"129\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"171\" y1=\"1\" x2=\"171\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">80</text><line x1=\"61\" y1=\"31\" x2=\"61\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">40</text><line x1=\"95\" y1=\"31\" x2=\"95\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"129\" y1=\"31\" x2=\"129\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"171\" y1=\"31\" x2=\"171\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">5</text><line x1=\"1\" y1=\"31\" x2=\"213\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">60</text><line x1=\"61\" y1=\"61\" x2=\"61\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">75</text><line x1=\"95\" y1=\"61\" x2=\"95\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">90</text><line x1=\"129\" y1=\"61\" x2=\"129\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">105</text><line x1=\"171\" y1=\"61\" x2=\"171\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">120</text><line x1=\"1\" y1=\"61\" x2=\"213\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">20</text><line x1=\"61\" y1=\"91\" x2=\"61\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">29</text><line x1=\"95\" y1=\"91\" x2=\"95\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">58</text><line x1=\"129\" y1=\"91\" x2=\"129\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">88</text><line x1=\"171\" y1=\"91\" x2=\"171\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">17</text><line x1=\"1\" y1=\"91\" x2=\"213\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"44.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"61\" y1=\"121\" x2=\"61\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"78.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">7</text><line x1=\"95\" y1=\"121\" x2=\"95\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"112.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">10</text><line x1=\"129\" y1=\"121\" x2=\"129\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"150.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">19</text><line x1=\"171\" y1=\"121\" x2=\"171\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"192.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">26</text><line x1=\"1\" y1=\"121\" x2=\"213\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel B",
        "tabel D",
        "tabel C",
        "tabel A"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per week met 8% af. Om het aantal één week eerder te berekenen, deel je het huidige aantal door 0,92.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,92."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 20% af. Om 10.00 uur zijn er 4500 downloads. Bereken het aantal downloads om 12.00 uur. Rond af op een geheel getal.",
      "antwoord": "2880",
      "uitleg": "Groeifactor 0,8. Na 2 uur: 4500 · 0,8² ≈ 2880,0 → 2880.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 500 · 0,90ᵗ, met t in eenheden van twintig minuten. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 3 tijdseenheden: groeifactor per uur 0,90³ ≈ 0,73. De beginwaarde (500) blijft hetzelfde.",
      "opties": [
        "A = 500 · 2,70ᵗ",
        "A = 1500 · 0,90ᵗ",
        "A = 500 · 0,73ᵗ",
        "A = 365 · 0,73ᵗ"
      ],
      "antwoord": 2
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de groei van een aantal bacteriën zien; op t = 0 zijn het er 60. Bereken de groeifactor per half uur.",
      "antwoord": "4",
      "uitleg": "Per kwartier: 120 : 60 = 2. Een half uur is 2 kwartier: 2² = 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 326\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"326\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c2\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"252.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"282.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"282.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"282.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"282.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"282.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">150</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">450</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">750</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">900</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">1050</text><text x=\"35.0\" y=\"297.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"286.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"318.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c2)\" points=\"40.0,267.6 42.2,267.0 44.5,266.3 46.8,265.6 49.0,264.9 51.2,264.1 53.5,263.3 55.8,262.5 58.0,261.6 60.2,260.7 62.5,259.8 64.8,258.8 67.0,257.8 69.2,256.7 71.5,255.6 73.8,254.4 76.0,253.2 78.2,251.9 80.5,250.6 82.8,249.2 85.0,247.8 87.2,246.2 89.5,244.7 91.8,243.0 94.0,241.3 96.2,239.5 98.5,237.6 100.8,235.6 103.0,233.6 105.2,231.4 107.5,229.2 109.8,226.8 112.0,224.4 114.2,221.8 116.5,219.2 118.8,216.4 121.0,213.5 123.2,210.5 125.5,207.3 127.8,204.0 130.0,200.5 132.2,196.9 134.5,193.2 136.8,189.2 139.0,185.1 141.2,180.8 143.5,176.4 145.8,171.7 148.0,166.8 150.2,161.7 152.5,156.4 154.8,150.8 157.0,145.0 159.2,138.9 161.5,132.6 163.8,126.0 166.0,119.1 168.2,111.9 170.5,104.3 172.8,96.5 175.0,88.3 177.2,79.7 179.5,70.7 181.8,61.4 184.0,51.6 186.2,41.4 188.5,30.7 190.8,19.6 193.0,8.0 195.2,-4.1 197.5,-16.8 199.8,-30.0 202.0,-43.8 204.2,-58.3 206.5,-73.3 208.8,-89.1 211.0,-105.5 213.2,-122.6 215.5,-140.6 217.8,-159.3 220.0,-178.8\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"267.6\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"261.6\" fill=\"#222\" font-size=\"11\">(0, 60)</text><circle cx=\"76.0\" cy=\"253.2\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"247.2\" fill=\"#222\" font-size=\"11\">(1, 120)</text><circle cx=\"112.0\" cy=\"224.4\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"218.4\" fill=\"#222\" font-size=\"11\">(2, 240)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een schilderij groeit met groeifactor 0,980 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 0,980¹² ≈ 0,785. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "11,760",
        "0,922",
        "0,785",
        "0,760"
      ],
      "antwoord": 2
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 150 · 1,06ᵗ, met t in eenheden van half uur. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 150 · 1,12ᵗ",
      "sleutelwoorden": [
        "1,12/1.12"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 2 eenheden van half uur: 1,06² ≈ 1,12. De beginwaarde blijft 150: A = 150 · 1,12ᵗ."
    }
  ]
});
