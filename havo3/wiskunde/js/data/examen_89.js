/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 89 — Gemengd H1 — Lineaire en exponentiële formules (6/10)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-wiskunde-h1-gemengd-6",
  "hoofdstuk": 1,
  "titel": "Proeftoets 89 — Gemengd H1 — Lineaire en exponentiële formules (6/10)",
  "vak": "Wiskunde · Hoofdstuk 1 · Lineaire en exponentiële formules",
  "icoon": "📈",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Gegeven is de formule y = −1 + 0,75x. Wat zijn de richtingscoëfficiënt en het startgetal?",
      "uitleg": "Schrijf de formule als y = ax + b: y = 0,75x − 1. Het getal vóór x (met het teken ervoor) is de richtingscoëfficiënt: 0,75. Het losse getal is het startgetal: −1.",
      "opties": [
        "richtingscoëfficiënt −0,75 en startgetal −1",
        "richtingscoëfficiënt 0,75 en startgetal 1",
        "richtingscoëfficiënt −1 en startgetal 0,75",
        "richtingscoëfficiënt 0,75 en startgetal −1"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Een lijn gaat door de punten P(−6, −26) en Q(−2, −14). Bereken de richtingscoëfficiënt van de lijn.",
      "antwoord": "3",
      "uitleg": "rc = toename y / toename x = (−14 − (−26)) / (−2 − (−6)) = 12 / 4 = 3."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het punt (12, −2) ligt op de lijn y = 0,5x − 8.",
      "antwoord": true,
      "uitleg": "Waar. Invullen van x = 12: y = 0,5 · 12 − 8 = −2. Dat is gelijk aan −2, dus het punt ligt op de lijn."
    },
    {
      "type": "mc",
      "vraag": "Lijn m gaat door het punt (10, 4) en loopt evenwijdig aan lijn l: y = 0,5x + 2. Welke formule hoort bij lijn m?",
      "uitleg": "Evenwijdig betekent dezelfde rc: a = 0,5. Invullen van (10, 4): 4 = 0,5 · 10 + b = 5 + b, dus b = −1. Lijn m: y = 0,5x − 1.",
      "opties": [
        "y = 0,5x + 9",
        "y = 0,5x − 1",
        "y = 0,5x + 4",
        "y = −0,5x + 9"
      ],
      "antwoord": 1
    },
    {
      "type": "invul",
      "vraag": "Bereken de y-coördinaat van het snijpunt van de lijnen y = 12x − 129 en y = −x + 14.",
      "antwoord": "3",
      "uitleg": "12x − 129 = −x + 14 geeft x = 11. Invullen: y = 12 · 11 − 129 = 3. Controle in de andere formule: 3."
    },
    {
      "type": "mc",
      "vraag": "De lijnen y = −x − 5 en y = −4x − 2 snijden elkaar in S. Met welke vergelijking bereken je de x-coördinaat van S?",
      "uitleg": "Op het snijpunt hebben beide lijnen dezelfde y. Stel daarom de twee formules aan elkaar gelijk.",
      "opties": [
        "−x − 5 = 0",
        "−x − 2 = −4x − 5",
        "−x − 5 = −4x − 2",
        "−x − 5 = −(−4x − 2)"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "Het snijpunt van de lijnen y = 4x − 2 en y = 9x + 13 is (−3, −12).",
      "antwoord": false,
      "uitleg": "Onwaar. Gelijkstellen geeft x = −3 en y = −14; het snijpunt is (−3, −14)."
    },
    {
      "type": "invul",
      "vraag": "In een spel spaar je credits. Sem heeft op dag 0 1 miljoen credits en krijgt er elke dag 2 miljoen bij. Lotte begint op hetzelfde moment en spaart ook elke dag hetzelfde aantal: na 2 dagen heeft Lotte 4,5 miljoen credits en na 10 dagen 24,5 miljoen. Na hoeveel dagen hebben ze evenveel credits?",
      "antwoord": "3",
      "uitleg": "Sem: c = 2t + 1. Lotte: rc = (24,5 − 4,5) / (10 − 2) = 2,5, b = 4,5 − 5 = −0,5. Gelijkstellen geeft t = 3 dagen."
    },
    {
      "type": "mc",
      "vraag": "De temperatuur T (°C) op een berg op hoogte h meter is T = 18 − 0,008h. Na k kwartier wandelen is de hoogte h = 8k + 400. Welke formule geeft T uitgedrukt in k?",
      "uitleg": "T = 18 − 0,008(8k + 400) = 18 − 0,064k − 3,2 = 14,8 − 0,064k.",
      "opties": [
        "T = 418 − 0,064k",
        "T = 14,8 − 0,008k",
        "T = −382 − 0,064k",
        "T = 14,8 − 0,064k"
      ],
      "antwoord": 3
    },
    {
      "type": "invul",
      "vraag": "Gegeven: T = 20 − 0,006h en h = 8k + 100, met k het aantal kwartieren wandelen. Bereken de temperatuur T na 12 kwartier.",
      "antwoord": "18,824",
      "uitleg": "h = 8 · 12 + 100 = 196. T = 20 − 0,006 · 196 = 18,824 °C."
    },
    {
      "type": "invul",
      "vraag": "Iris is twee keer zo oud als Jesse (a = 2b). Kiki is 1 jaar jonger dan Iris (c = a − 1). Samen zijn ze 44 jaar. Hoe oud is Jesse?",
      "antwoord": "9",
      "uitleg": "a + b + c = 44. Substitueer a = 2b en c = 2b − 1: 2b + b + 2b − 1 = 44 → 5b = 45 → b = 9."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je t = 5 − 3p substitueert in h = 4t + 10, krijg je h = −3p + 30.",
      "antwoord": false,
      "uitleg": "Onwaar. h = 4(5 − 3p) + 10 = 20 − 12p + 10, dus h = −12p + 30. Zonder haakjes vergeet je 3p met 4 te vermenigvuldigen."
    },
    {
      "type": "invul",
      "vraag": "Het aantal muggen verandert exponentieel met groeifactor 0,9 per uur. Om 04.00 uur zijn er 4800 muggen. Hoeveel muggen waren er om 03.00 uur? Rond af op een geheel getal.",
      "antwoord": "5333",
      "uitleg": "Terug in de tijd: delen door de groeifactor. 4800 : 0,9 ≈ 5333,3 → 5333 muggen.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "De tabellen A t/m D geven het aantal konijnen op een eiland op vier meetpunten. Welke tabel hoort bij exponentiële groei?",
      "uitleg": "Bij exponentiële groei vermenigvuldig je steeds met dezelfde factor (×1,5). Dat is tabel A.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 238 152\" width=\"238\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"13\"><rect x=\"1\" y=\"1\" width=\"236\" height=\"150\" rx=\"8\" fill=\"#ffffff\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"1\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">t</text><line x1=\"27\" y1=\"1\" x2=\"27\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">0</text><line x1=\"69\" y1=\"1\" x2=\"69\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">1</text><line x1=\"111\" y1=\"1\" x2=\"111\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">2</text><line x1=\"153\" y1=\"1\" x2=\"153\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">3</text><line x1=\"195\" y1=\"1\" x2=\"195\" y2=\"31\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"21\" text-anchor=\"middle\" fill=\"#222\">4</text><rect x=\"1\" y=\"31\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">A</text><line x1=\"27\" y1=\"31\" x2=\"27\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">160</text><line x1=\"69\" y1=\"31\" x2=\"69\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">240</text><line x1=\"111\" y1=\"31\" x2=\"111\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">360</text><line x1=\"153\" y1=\"31\" x2=\"153\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">540</text><line x1=\"195\" y1=\"31\" x2=\"195\" y2=\"61\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"51\" text-anchor=\"middle\" fill=\"#222\">810</text><line x1=\"1\" y1=\"31\" x2=\"237\" y2=\"31\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"61\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">B</text><line x1=\"27\" y1=\"61\" x2=\"27\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">15</text><line x1=\"69\" y1=\"61\" x2=\"69\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"111\" y1=\"61\" x2=\"111\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">39</text><line x1=\"153\" y1=\"61\" x2=\"153\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">51</text><line x1=\"195\" y1=\"61\" x2=\"195\" y2=\"91\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"81\" text-anchor=\"middle\" fill=\"#222\">63</text><line x1=\"1\" y1=\"61\" x2=\"237\" y2=\"61\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"91\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">C</text><line x1=\"27\" y1=\"91\" x2=\"27\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">62</text><line x1=\"69\" y1=\"91\" x2=\"69\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">61</text><line x1=\"111\" y1=\"91\" x2=\"111\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">75</text><line x1=\"153\" y1=\"91\" x2=\"153\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">91</text><line x1=\"195\" y1=\"91\" x2=\"195\" y2=\"121\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"111\" text-anchor=\"middle\" fill=\"#222\">41</text><line x1=\"1\" y1=\"91\" x2=\"237\" y2=\"91\" stroke=\"#9aa3b2\"/><rect x=\"1\" y=\"121\" width=\"26\" height=\"30\" fill=\"#fde7ef\"/><text x=\"14.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\" font-weight=\"bold\">D</text><line x1=\"27\" y1=\"121\" x2=\"27\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"48.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">4</text><line x1=\"69\" y1=\"121\" x2=\"69\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"90.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">6</text><line x1=\"111\" y1=\"121\" x2=\"111\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"132.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">12</text><line x1=\"153\" y1=\"121\" x2=\"153\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"174.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">18</text><line x1=\"195\" y1=\"121\" x2=\"195\" y2=\"151\" stroke=\"#9aa3b2\"/><text x=\"216.0\" y=\"141\" text-anchor=\"middle\" fill=\"#222\">27</text><line x1=\"1\" y1=\"121\" x2=\"237\" y2=\"121\" stroke=\"#9aa3b2\"/></svg>",
      "opties": [
        "tabel D",
        "tabel A",
        "tabel B",
        "tabel C"
      ],
      "antwoord": 1
    },
    {
      "type": "waaronwaar",
      "vraag": "Het aantal neemt per dag met 5% af. Om het aantal één dag eerder te berekenen, deel je het huidige aantal door 0,95.",
      "antwoord": true,
      "uitleg": "Waar. Terug in de tijd deel je door de groeifactor; die is 0,95."
    },
    {
      "type": "invul",
      "vraag": "Het aantal downloads van een app neemt per uur met 10% af. Om 10.00 uur zijn er 3600 downloads. Bereken het aantal downloads om 14.00 uur. Rond af op een geheel getal.",
      "antwoord": "2362",
      "uitleg": "Groeifactor 0,9. Na 4 uur: 3600 · 0,9⁴ ≈ 2362,0 → 2362.",
      "tolerantie": 1
    },
    {
      "type": "mc",
      "vraag": "Een algensoort groeit volgens A = 1000 · 0,95ᵗ, met t in kwartieren. Welke formule hoort bij t in uren?",
      "uitleg": "In een uur passen 4 tijdseenheden: groeifactor per uur 0,95⁴ ≈ 0,81. De beginwaarde (1000) blijft hetzelfde.",
      "opties": [
        "A = 1000 · 0,81ᵗ",
        "A = 4000 · 0,95ᵗ",
        "A = 1000 · 3,80ᵗ",
        "A = 815 · 0,81ᵗ"
      ],
      "antwoord": 0
    },
    {
      "type": "invul",
      "vraag": "De grafiek laat de afname van een aantal bacteriën zien; op t = 0 zijn het er 800. Bereken de groeifactor per half uur. Geef je antwoord als decimaal getal.",
      "antwoord": "0,25",
      "uitleg": "Per kwartier: 400 : 800 = 0,5. Een half uur is 2 kwartier: 0,5² = 0,25.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 250 362\" width=\"250\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"250\" height=\"362\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c15\"><rect x=\"40.0\" y=\"30.0\" width=\"180.0\" height=\"288.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"76.0\" y1=\"318.0\" x2=\"76.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"318.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"148.0\" y1=\"318.0\" x2=\"148.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"318.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"220.0\" y1=\"318.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"282.0\" x2=\"220.0\" y2=\"282.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"246.0\" x2=\"220.0\" y2=\"246.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"210.0\" x2=\"220.0\" y2=\"210.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"220.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"138.0\" x2=\"220.0\" y2=\"138.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"220.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"66.0\" x2=\"220.0\" y2=\"66.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"220.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"220.0\" y2=\"318.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"40.0\" y1=\"318.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"76.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"112.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"148.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"184.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"220.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"35.0\" y=\"286.0\" fill=\"#333\" text-anchor=\"end\">100</text><text x=\"35.0\" y=\"250.0\" fill=\"#333\" text-anchor=\"end\">200</text><text x=\"35.0\" y=\"214.0\" fill=\"#333\" text-anchor=\"end\">300</text><text x=\"35.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">400</text><text x=\"35.0\" y=\"142.0\" fill=\"#333\" text-anchor=\"end\">500</text><text x=\"35.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">600</text><text x=\"35.0\" y=\"70.0\" fill=\"#333\" text-anchor=\"end\">700</text><text x=\"35.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">800</text><text x=\"35.0\" y=\"333.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"226.0\" y=\"322.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"36.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\"></text><text x=\"130.0\" y=\"354.0\" fill=\"#222\" text-anchor=\"middle\">tijd in kwartieren →</text><text x=\"40.0\" y=\"18.0\" fill=\"#222\">↑ aantal bacteriën</text><polyline clip-path=\"url(#w1c15)\" points=\"40.0,30.0 42.2,42.2 44.5,53.9 46.8,65.1 49.0,75.8 51.2,86.1 53.5,95.9 55.8,105.3 58.0,114.4 60.2,123.0 62.5,131.3 64.8,139.2 67.0,146.8 69.2,154.0 71.5,161.0 73.8,167.6 76.0,174.0 78.2,180.1 80.5,186.0 82.8,191.5 85.0,196.9 87.2,202.0 89.5,207.0 91.8,211.7 94.0,216.2 96.2,220.5 98.5,224.6 100.8,228.6 103.0,232.4 105.2,236.0 107.5,239.5 109.8,242.8 112.0,246.0 114.2,249.1 116.5,252.0 118.8,254.8 121.0,257.5 123.2,260.0 125.5,262.5 127.8,264.8 130.0,267.1 132.2,269.2 134.5,271.3 136.8,273.3 139.0,275.2 141.2,277.0 143.5,278.7 145.8,280.4 148.0,282.0 150.2,283.5 152.5,285.0 154.8,286.4 157.0,287.7 159.2,289.0 161.5,290.2 163.8,291.4 166.0,292.5 168.2,293.6 170.5,294.7 172.8,295.6 175.0,296.6 177.2,297.5 179.5,298.4 181.8,299.2 184.0,300.0 186.2,300.8 188.5,301.5 190.8,302.2 193.0,302.9 195.2,303.5 197.5,304.1 199.8,304.7 202.0,305.3 204.2,305.8 206.5,306.3 208.8,306.8 211.0,307.3 213.2,307.8 215.5,308.2 217.8,308.6 220.0,309.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><circle cx=\"40.0\" cy=\"30.0\" r=\"3.5\" fill=\"#222\"/><text x=\"46.0\" y=\"24.0\" fill=\"#222\" font-size=\"11\">(0, 800)</text><circle cx=\"76.0\" cy=\"174.0\" r=\"3.5\" fill=\"#222\"/><text x=\"82.0\" y=\"168.0\" fill=\"#222\" font-size=\"11\">(1, 400)</text><circle cx=\"112.0\" cy=\"246.0\" r=\"3.5\" fill=\"#222\"/><text x=\"118.0\" y=\"240.0\" fill=\"#222\" font-size=\"11\">(2, 200)</text></svg>"
    },
    {
      "type": "mc",
      "vraag": "De waarde van een schilderij groeit met groeifactor 1,015 per maand. Hoe groot is de groeifactor per jaar (afgerond op drie decimalen)?",
      "uitleg": "Een jaar = 12 maanden: 1,015¹² ≈ 1,196. Je mag de procenten niet zomaar met 12 vermenigvuldigen.",
      "opties": [
        "1,196",
        "1,061",
        "1,180",
        "12,180"
      ],
      "antwoord": 0
    },
    {
      "type": "open",
      "vraag": "Een hoeveelheid groeit volgens A = 600 · 0,94ᵗ, met t in eenheden van twintig minuten. Stel een formule op met t in uren. Rond de groeifactor af op twee decimalen.",
      "modelantwoord": "A = 600 · 0,83ᵗ",
      "sleutelwoorden": [
        "0,83/0.83"
      ],
      "minTreffers": 1,
      "uitleg": "In een uur passen 3 eenheden van twintig minuten: 0,94³ ≈ 0,83. De beginwaarde blijft 600: A = 600 · 0,83ᵗ."
    }
  ]
});
