/* =========================================================
   Duru's Wiskunde (HAVO 3) — Onderwerp §2.4 De vorm en de ligging van de parabool
   Bron: Noordhoff H2 Parabolen (opdrachten 1–37, O4–O34, U1–U7, E1–E15, P1–P8; andere getallen)
   Gegenereerd met tools/gen_wiskunde_h2_parabolen.py
   ========================================================= */
DURU.register({
  "id": "h2-parabolen-4",
  "hoofdstuk": 2,
  "paragraaf": "2.4",
  "titel": "De vorm en de ligging van de parabool",
  "korteUitleg": "Uit a, b en c in y = ax² + bx + c lees je af: berg of dal, smal of breed, top op de y-as, door de oorsprong.",
  "icoon": "⛰️",
  "kleur": "blauw",
  "theorie": "<h3>§2.4 De vorm en de ligging van de parabool</h3>\n<p>De formule <b>y = ax² + bx + c</b> heet de <b>algemene vorm</b> van een kwadratische formule. Zonder te tekenen kun je uit de getallen a, b en c al veel over de parabool zeggen.</p>\n<h4>De vorm: kijk naar a</h4>\n<div class=\"formule-box\">a &gt; 0 → dalparabool, a &lt; 0 → bergparabool<br>Hoe <b>verder a van 0</b> af ligt, hoe <b>smaller</b> de parabool. Hoe <b>dichter a bij 0</b>, hoe <b>breder</b>.</div>\n<p>Voorbeeld: y = −2x² + 3 is smaller dan y = x² − 4x, want −2 ligt verder van 0 dan 1. En y = ½x² + 2x + 2 is breder dan y = 4x² + x, want ½ ligt dichter bij 0 dan 4. Het teken telt hierbij niet mee: −3 en 3 geven even brede parabolen.</p>\n<h4>De ligging: kijk naar b en c</h4>\n<ul><li>Het snijpunt met de y-as is altijd <b>(0, c)</b> (vul x = 0 in).</li><li>Is <b>b = 0</b>, dan is de formule y = ax² + c. De top ligt dan <b>op de y-as</b>: de top is (0, c). Voorbeeld: y = 2x² − 5 heeft top (0, −5).</li><li>Is <b>c = 0</b>, dan is de formule y = ax² + bx. De parabool gaat dan <b>door de oorsprong</b> (0, 0). Voorbeeld: y = 4x² − 8x.</li></ul>\n<h4>Parabolen herkennen</h4><p>Moet je bij een figuur met meerdere parabolen de juiste formule zoeken, werk dan stap voor stap: berg of dal (teken van a)? Top op de y-as (b = 0)? Door de oorsprong (c = 0)? Waar snijdt hij de y-as (c)? Smal of breed (grootte van a)? Meestal blijft er dan maar één parabool over.</p>\n<p>Ook in context werkt dit: twee ballen met h = −0,75a² + … en h = −0,9a² + … — de tweede baan is smaller, want −0,9 ligt verder van 0.</p>",
  "vragen": [
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = 2x² + 7x + 6 is smaller dan de parabool bij y = ½x² − 6x + 5.",
      "antwoord": true,
      "uitleg": "Waar. Kijk naar het getal voor x²: 2 en ½. Hoe verder van 0, hoe smaller. 2 ligt verder van 0 dan ½, dus de eerste parabool is smaller."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −4x² + 6x − 4, y = −2x² − 8x − 4, y = 3x² + 7x + 6 en y = −5x² − x + 8. Bij welke formule is de parabool het smalst?",
      "uitleg": "Vergelijk de getallen voor x²: −4, −2, 3, −5. Het verst van 0 ligt −5, dus die parabool is het smalst.",
      "opties": [
        "y = −5x² − x + 8",
        "y = −4x² + 6x − 4",
        "y = −2x² − 8x − 4",
        "y = 3x² + 7x + 6"
      ],
      "antwoord": 0
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = 4x² + 2x + 8, y = −¼x² − x − 5, y = −¼x² − 4 en y = 2x² + 6x + 7. Bij welke formule ligt de top van de parabool op de y-as?",
      "uitleg": "Ligt de top op de y-as, dan is b = 0: de formule heeft de vorm y = ax² + c. Dat is y = −¼x² − 4.",
      "opties": [
        "y = 4x² + 2x + 8",
        "y = −¼x² − 4",
        "y = 2x² + 6x + 7",
        "y = −¼x² − x − 5"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = 2x² − 8x − 9, y = 4x² + x, y = −¼x² + 7x + 2 en y = x² + 9x + 5. Bij welke formule gaat de parabool door de oorsprong?",
      "uitleg": "Gaat de parabool door de oorsprong, dan is c = 0: bij x = 0 hoort y = 0. Dat is y = 4x² + x.",
      "opties": [
        "y = 4x² + x",
        "y = −¼x² + 7x + 2",
        "y = 2x² − 8x − 9",
        "y = x² + 9x + 5"
      ],
      "antwoord": 0
    },
    {
      "type": "invoer",
      "vraag": "Geef de y-coördinaat van het snijpunt van de parabool bij y = (x − 1)(x + 1) met de y-as.",
      "antwoord": "-1|−1",
      "uitleg": "Vul x = 0 in: y = (0 − 1)(0 − (−1)) = −1. Het snijpunt is (0, −1)."
    },
    {
      "type": "mc",
      "vraag": "Wat zijn de coördinaten van de top van de parabool bij y = 2 − x²?",
      "uitleg": "Er is geen term met x (b = 0), dus de top ligt op de y-as: (0, 2).",
      "opties": [
        "(2, 0)",
        "(0, −2)",
        "(−1, 2)",
        "(0, 2)"
      ],
      "antwoord": 3
    },
    {
      "type": "mc",
      "vraag": "In de figuur staan vier parabolen. Welke parabool hoort bij de formule y = −x² + 4?",
      "uitleg": "y = −x² + 4: bergparabool, top op de y-as in (0, 4). Dat past alleen bij parabool 2.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 330 252\" width=\"330\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"330\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c5\"><rect x=\"40.0\" y=\"30.0\" width=\"240.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"280.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"280.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"280.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"280.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"280.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"280.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"280.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"184.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"155.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"155.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"155.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"155.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"155.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"155.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"155.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"155.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"155.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"286.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"156.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c5)\" points=\"40.0,738.0 43.0,708.4 46.0,679.5 49.0,651.4 52.0,624.0 55.0,597.4 58.0,571.5 61.0,546.4 64.0,522.0 67.0,498.4 70.0,475.5 73.0,453.4 76.0,432.0 79.0,411.4 82.0,391.5 85.0,372.4 88.0,354.0 91.0,336.4 94.0,319.5 97.0,303.4 100.0,288.0 103.0,273.4 106.0,259.5 109.0,246.4 112.0,234.0 115.0,222.4 118.0,211.5 121.0,201.4 124.0,192.0 127.0,183.4 130.0,175.5 133.0,168.4 136.0,162.0 139.0,156.4 142.0,151.5 145.0,147.4 148.0,144.0 151.0,141.4 154.0,139.5 157.0,138.4 160.0,138.0 163.0,138.4 166.0,139.5 169.0,141.4 172.0,144.0 175.0,147.4 178.0,151.5 181.0,156.4 184.0,162.0 187.0,168.4 190.0,175.5 193.0,183.4 196.0,192.0 199.0,201.4 202.0,211.5 205.0,222.4 208.0,234.0 211.0,246.4 214.0,259.5 217.0,273.4 220.0,288.0 223.0,303.4 226.0,319.5 229.0,336.4 232.0,354.0 235.0,372.4 238.0,391.5 241.0,411.4 244.0,432.0 247.0,453.4 250.0,475.5 253.0,498.4 256.0,522.0 259.0,546.4 262.0,571.5 265.0,597.4 268.0,624.0 271.0,651.4 274.0,679.5 277.0,708.4 280.0,738.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"128.6\" y=\"203.4\" fill=\"#c2185b\" font-weight=\"bold\" font-size=\"14\">1</text><polyline clip-path=\"url(#w1c5)\" points=\"40.0,378.0 43.0,363.2 46.0,348.8 49.0,334.7 52.0,321.0 55.0,307.7 58.0,294.8 61.0,282.2 64.0,270.0 67.0,258.2 70.0,246.8 73.0,235.7 76.0,225.0 79.0,214.7 82.0,204.8 85.0,195.2 88.0,186.0 91.0,177.2 94.0,168.8 97.0,160.7 100.0,153.0 103.0,145.7 106.0,138.8 109.0,132.2 112.0,126.0 115.0,120.2 118.0,114.8 121.0,109.7 124.0,105.0 127.0,100.7 130.0,96.8 133.0,93.2 136.0,90.0 139.0,87.2 142.0,84.8 145.0,82.7 148.0,81.0 151.0,79.7 154.0,78.8 157.0,78.2 160.0,78.0 163.0,78.2 166.0,78.8 169.0,79.7 172.0,81.0 175.0,82.7 178.0,84.8 181.0,87.2 184.0,90.0 187.0,93.2 190.0,96.8 193.0,100.7 196.0,105.0 199.0,109.7 202.0,114.8 205.0,120.2 208.0,126.0 211.0,132.2 214.0,138.8 217.0,145.7 220.0,153.0 223.0,160.7 226.0,168.8 229.0,177.2 232.0,186.0 235.0,195.2 238.0,204.8 241.0,214.7 244.0,225.0 247.0,235.7 250.0,246.8 253.0,258.2 256.0,270.0 259.0,282.2 262.0,294.8 265.0,307.7 268.0,321.0 271.0,334.7 274.0,348.8 277.0,363.2 280.0,378.0\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.6\"/><text x=\"229.4\" y=\"163.1\" fill=\"#2563eb\" font-weight=\"bold\" font-size=\"14\">2</text><polyline clip-path=\"url(#w1c5)\" points=\"40.0,-210.0 43.0,-195.2 46.0,-180.8 49.0,-166.7 52.0,-153.0 55.0,-139.7 58.0,-126.8 61.0,-114.2 64.0,-102.0 67.0,-90.2 70.0,-78.8 73.0,-67.7 76.0,-57.0 79.0,-46.7 82.0,-36.8 85.0,-27.2 88.0,-18.0 91.0,-9.2 94.0,-0.8 97.0,7.3 100.0,15.0 103.0,22.3 106.0,29.2 109.0,35.8 112.0,42.0 115.0,47.8 118.0,53.2 121.0,58.3 124.0,63.0 127.0,67.3 130.0,71.2 133.0,74.8 136.0,78.0 139.0,80.8 142.0,83.2 145.0,85.3 148.0,87.0 151.0,88.3 154.0,89.2 157.0,89.8 160.0,90.0 163.0,89.8 166.0,89.2 169.0,88.3 172.0,87.0 175.0,85.3 178.0,83.2 181.0,80.8 184.0,78.0 187.0,74.8 190.0,71.2 193.0,67.3 196.0,63.0 199.0,58.3 202.0,53.2 205.0,47.8 208.0,42.0 211.0,35.8 214.0,29.2 217.0,22.3 220.0,15.0 223.0,7.3 226.0,-0.8 229.0,-9.2 232.0,-18.0 235.0,-27.2 238.0,-36.8 241.0,-46.7 244.0,-57.0 247.0,-67.7 250.0,-78.8 253.0,-90.2 256.0,-102.0 259.0,-114.2 262.0,-126.8 265.0,-139.7 268.0,-153.0 271.0,-166.7 274.0,-180.8 277.0,-195.2 280.0,-210.0\" fill=\"none\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"195.8\" y=\"76.7\" fill=\"#0d9488\" font-weight=\"bold\" font-size=\"14\">3</text><polyline clip-path=\"url(#w1c5)\" points=\"40.0,-750.0 43.0,-705.6 46.0,-662.2 49.0,-620.1 52.0,-579.0 55.0,-539.1 58.0,-500.2 61.0,-462.6 64.0,-426.0 67.0,-390.6 70.0,-356.2 73.0,-323.1 76.0,-291.0 79.0,-260.1 82.0,-230.2 85.0,-201.6 88.0,-174.0 91.0,-147.6 94.0,-122.2 97.0,-98.1 100.0,-75.0 103.0,-53.1 106.0,-32.2 109.0,-12.6 112.0,6.0 115.0,23.4 118.0,39.8 121.0,54.9 124.0,69.0 127.0,81.9 130.0,93.8 133.0,104.4 136.0,114.0 139.0,122.4 142.0,129.8 145.0,135.9 148.0,141.0 151.0,144.9 154.0,147.8 157.0,149.4 160.0,150.0 163.0,149.4 166.0,147.8 169.0,144.9 172.0,141.0 175.0,135.9 178.0,129.8 181.0,122.4 184.0,114.0 187.0,104.4 190.0,93.8 193.0,81.9 196.0,69.0 199.0,54.9 202.0,39.8 205.0,23.4 208.0,6.0 211.0,-12.6 214.0,-32.2 217.0,-53.1 220.0,-75.0 223.0,-98.1 226.0,-122.2 229.0,-147.6 232.0,-174.0 235.0,-201.6 238.0,-230.2 241.0,-260.1 244.0,-291.0 247.0,-323.1 250.0,-356.2 253.0,-390.6 256.0,-426.0 259.0,-462.6 262.0,-500.2 265.0,-539.1 268.0,-579.0 271.0,-620.1 274.0,-662.2 277.0,-705.6 280.0,-750.0\" fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.6\"/><text x=\"145.4\" y=\"124.8\" fill=\"#b45309\" font-weight=\"bold\" font-size=\"14\">4</text></svg>",
      "opties": [
        "parabool 1",
        "parabool 3",
        "parabool 4",
        "parabool 2"
      ],
      "antwoord": 3
    },
    {
      "type": "waaronwaar",
      "vraag": "De top van de parabool bij y = 4x² − 5x − 2 ligt op de y-as.",
      "antwoord": false,
      "uitleg": "Onwaar. Top op de y-as ⇔ b = 0 (geen term met x). Hier is b = −5."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de formules y = −4x² − 4x + 5, y = 2x² + 3x + 1, y = ⅓x² + 2x − 3 en y = −3x² − 6x + 7. Bij welke formule is de parabool het breedst?",
      "uitleg": "Vergelijk de getallen voor x²: −4, 2, ⅓, −3. Het dichtst bij 0 ligt ⅓, dus die parabool is het breedst.",
      "opties": [
        "y = −4x² − 4x + 5",
        "y = ⅓x² + 2x − 3",
        "y = 2x² + 3x + 1",
        "y = −3x² − 6x + 7"
      ],
      "antwoord": 1
    },
    {
      "type": "mc",
      "vraag": "In de figuur staan vier parabolen. Welke parabool hoort bij de formule y = 3x² − 3?",
      "uitleg": "y = 3x² − 3: dalparabool, top op de y-as in (0, −3), smaller dan y = x². Dat past alleen bij parabool 4.",
      "figuur": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 330 252\" width=\"330\" style=\"max-width:100%;height:auto\" font-family=\"sans-serif\" font-size=\"12\"><rect x=\"0\" y=\"0\" width=\"330\" height=\"252\" rx=\"12\" fill=\"#ffffff\"/><defs><clipPath id=\"w1c6\"><rect x=\"40.0\" y=\"30.0\" width=\"240.0\" height=\"192.0\"/></clipPath></defs><line x1=\"40.0\" y1=\"222.0\" x2=\"40.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"64.0\" y1=\"222.0\" x2=\"64.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"88.0\" y1=\"222.0\" x2=\"88.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"112.0\" y1=\"222.0\" x2=\"112.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"136.0\" y1=\"222.0\" x2=\"136.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"184.0\" y1=\"222.0\" x2=\"184.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"208.0\" y1=\"222.0\" x2=\"208.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"232.0\" y1=\"222.0\" x2=\"232.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"256.0\" y1=\"222.0\" x2=\"256.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"280.0\" y1=\"222.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"222.0\" x2=\"280.0\" y2=\"222.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"198.0\" x2=\"280.0\" y2=\"198.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"174.0\" x2=\"280.0\" y2=\"174.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"150.0\" x2=\"280.0\" y2=\"150.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"102.0\" x2=\"280.0\" y2=\"102.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"78.0\" x2=\"280.0\" y2=\"78.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"54.0\" x2=\"280.0\" y2=\"54.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"30.0\" x2=\"280.0\" y2=\"30.0\" stroke=\"#d6dbe4\" stroke-width=\"1\"/><line x1=\"40.0\" y1=\"126.0\" x2=\"280.0\" y2=\"126.0\" stroke=\"#222\" stroke-width=\"1.6\"/><line x1=\"160.0\" y1=\"222.0\" x2=\"160.0\" y2=\"30.0\" stroke=\"#222\" stroke-width=\"1.6\"/><text x=\"40.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−5</text><text x=\"64.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−4</text><text x=\"88.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−3</text><text x=\"112.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−2</text><text x=\"136.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">−1</text><text x=\"184.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">1</text><text x=\"208.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">2</text><text x=\"232.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">3</text><text x=\"256.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">4</text><text x=\"280.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"middle\">5</text><text x=\"155.0\" y=\"226.0\" fill=\"#333\" text-anchor=\"end\">−8</text><text x=\"155.0\" y=\"202.0\" fill=\"#333\" text-anchor=\"end\">−6</text><text x=\"155.0\" y=\"178.0\" fill=\"#333\" text-anchor=\"end\">−4</text><text x=\"155.0\" y=\"154.0\" fill=\"#333\" text-anchor=\"end\">−2</text><text x=\"155.0\" y=\"106.0\" fill=\"#333\" text-anchor=\"end\">2</text><text x=\"155.0\" y=\"82.0\" fill=\"#333\" text-anchor=\"end\">4</text><text x=\"155.0\" y=\"58.0\" fill=\"#333\" text-anchor=\"end\">6</text><text x=\"155.0\" y=\"34.0\" fill=\"#333\" text-anchor=\"end\">8</text><text x=\"155.0\" y=\"141.0\" fill=\"#333\" text-anchor=\"end\" font-style=\"italic\">O</text><text x=\"286.0\" y=\"130.0\" fill=\"#222\" font-style=\"italic\">x</text><text x=\"156.0\" y=\"20.0\" fill=\"#222\" font-style=\"italic\">y</text><polyline clip-path=\"url(#w1c6)\" points=\"40.0,738.0 43.0,708.4 46.0,679.5 49.0,651.4 52.0,624.0 55.0,597.4 58.0,571.5 61.0,546.4 64.0,522.0 67.0,498.4 70.0,475.5 73.0,453.4 76.0,432.0 79.0,411.4 82.0,391.5 85.0,372.4 88.0,354.0 91.0,336.4 94.0,319.5 97.0,303.4 100.0,288.0 103.0,273.4 106.0,259.5 109.0,246.4 112.0,234.0 115.0,222.4 118.0,211.5 121.0,201.4 124.0,192.0 127.0,183.4 130.0,175.5 133.0,168.4 136.0,162.0 139.0,156.4 142.0,151.5 145.0,147.4 148.0,144.0 151.0,141.4 154.0,139.5 157.0,138.4 160.0,138.0 163.0,138.4 166.0,139.5 169.0,141.4 172.0,144.0 175.0,147.4 178.0,151.5 181.0,156.4 184.0,162.0 187.0,168.4 190.0,175.5 193.0,183.4 196.0,192.0 199.0,201.4 202.0,211.5 205.0,222.4 208.0,234.0 211.0,246.4 214.0,259.5 217.0,273.4 220.0,288.0 223.0,303.4 226.0,319.5 229.0,336.4 232.0,354.0 235.0,372.4 238.0,391.5 241.0,411.4 244.0,432.0 247.0,453.4 250.0,475.5 253.0,498.4 256.0,522.0 259.0,546.4 262.0,571.5 265.0,597.4 268.0,624.0 271.0,651.4 274.0,679.5 277.0,708.4 280.0,738.0\" fill=\"none\" stroke=\"#c2185b\" stroke-width=\"2.6\"/><text x=\"128.6\" y=\"203.4\" fill=\"#c2185b\" font-weight=\"bold\" font-size=\"14\">1</text><polyline clip-path=\"url(#w1c6)\" points=\"40.0,390.0 43.0,375.2 46.0,360.8 49.0,346.7 52.0,333.0 55.0,319.7 58.0,306.8 61.0,294.2 64.0,282.0 67.0,270.2 70.0,258.8 73.0,247.7 76.0,237.0 79.0,226.7 82.0,216.8 85.0,207.2 88.0,198.0 91.0,189.2 94.0,180.8 97.0,172.7 100.0,165.0 103.0,157.7 106.0,150.8 109.0,144.2 112.0,138.0 115.0,132.2 118.0,126.8 121.0,121.7 124.0,117.0 127.0,112.7 130.0,108.8 133.0,105.2 136.0,102.0 139.0,99.2 142.0,96.8 145.0,94.7 148.0,93.0 151.0,91.7 154.0,90.8 157.0,90.2 160.0,90.0 163.0,90.2 166.0,90.8 169.0,91.7 172.0,93.0 175.0,94.7 178.0,96.8 181.0,99.2 184.0,102.0 187.0,105.2 190.0,108.8 193.0,112.7 196.0,117.0 199.0,121.7 202.0,126.8 205.0,132.2 208.0,138.0 211.0,144.2 214.0,150.8 217.0,157.7 220.0,165.0 223.0,172.7 226.0,180.8 229.0,189.2 232.0,198.0 235.0,207.2 238.0,216.8 241.0,226.7 244.0,237.0 247.0,247.7 250.0,258.8 253.0,270.2 256.0,282.0 259.0,294.2 262.0,306.8 265.0,319.7 268.0,333.0 271.0,346.7 274.0,360.8 277.0,375.2 280.0,390.0\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.6\"/><text x=\"224.6\" y=\"163.1\" fill=\"#2563eb\" font-weight=\"bold\" font-size=\"14\">2</text><polyline clip-path=\"url(#w1c6)\" points=\"40.0,-222.0 43.0,-207.2 46.0,-192.8 49.0,-178.7 52.0,-165.0 55.0,-151.7 58.0,-138.8 61.0,-126.2 64.0,-114.0 67.0,-102.2 70.0,-90.8 73.0,-79.7 76.0,-69.0 79.0,-58.7 82.0,-48.8 85.0,-39.2 88.0,-30.0 91.0,-21.2 94.0,-12.8 97.0,-4.7 100.0,3.0 103.0,10.3 106.0,17.2 109.0,23.8 112.0,30.0 115.0,35.8 118.0,41.2 121.0,46.3 124.0,51.0 127.0,55.3 130.0,59.2 133.0,62.8 136.0,66.0 139.0,68.8 142.0,71.2 145.0,73.3 148.0,75.0 151.0,76.3 154.0,77.2 157.0,77.8 160.0,78.0 163.0,77.8 166.0,77.2 169.0,76.3 172.0,75.0 175.0,73.3 178.0,71.2 181.0,68.8 184.0,66.0 187.0,62.8 190.0,59.2 193.0,55.3 196.0,51.0 199.0,46.3 202.0,41.2 205.0,35.8 208.0,30.0 211.0,23.8 214.0,17.2 217.0,10.3 220.0,3.0 223.0,-4.7 226.0,-12.8 229.0,-21.2 232.0,-30.0 235.0,-39.2 238.0,-48.8 241.0,-58.7 244.0,-69.0 247.0,-79.7 250.0,-90.8 253.0,-102.2 256.0,-114.0 259.0,-126.2 262.0,-138.8 265.0,-151.7 268.0,-165.0 271.0,-178.7 274.0,-192.8 277.0,-207.2 280.0,-222.0\" fill=\"none\" stroke=\"#0d9488\" stroke-width=\"2.6\"/><text x=\"133.4\" y=\"58.5\" fill=\"#0d9488\" font-weight=\"bold\" font-size=\"14\">3</text><polyline clip-path=\"url(#w1c6)\" points=\"40.0,-738.0 43.0,-693.6 46.0,-650.2 49.0,-608.1 52.0,-567.0 55.0,-527.1 58.0,-488.2 61.0,-450.6 64.0,-414.0 67.0,-378.6 70.0,-344.2 73.0,-311.1 76.0,-279.0 79.0,-248.1 82.0,-218.2 85.0,-189.6 88.0,-162.0 91.0,-135.6 94.0,-110.2 97.0,-86.1 100.0,-63.0 103.0,-41.1 106.0,-20.2 109.0,-0.6 112.0,18.0 115.0,35.4 118.0,51.8 121.0,66.9 124.0,81.0 127.0,93.9 130.0,105.8 133.0,116.4 136.0,126.0 139.0,134.4 142.0,141.8 145.0,147.9 148.0,153.0 151.0,156.9 154.0,159.8 157.0,161.4 160.0,162.0 163.0,161.4 166.0,159.8 169.0,156.9 172.0,153.0 175.0,147.9 178.0,141.8 181.0,134.4 184.0,126.0 187.0,116.4 190.0,105.8 193.0,93.9 196.0,81.0 199.0,66.9 202.0,51.8 205.0,35.4 208.0,18.0 211.0,-0.6 214.0,-20.2 217.0,-41.1 220.0,-63.0 223.0,-86.1 226.0,-110.2 229.0,-135.6 232.0,-162.0 235.0,-189.6 238.0,-218.2 241.0,-248.1 244.0,-279.0 247.0,-311.1 250.0,-344.2 253.0,-378.6 256.0,-414.0 259.0,-450.6 262.0,-488.2 265.0,-527.1 268.0,-567.0 271.0,-608.1 274.0,-650.2 277.0,-693.6 280.0,-738.0\" fill=\"none\" stroke=\"#b45309\" stroke-width=\"2.6\"/><text x=\"203.0\" y=\"85.0\" fill=\"#b45309\" font-weight=\"bold\" font-size=\"14\">4</text></svg>",
      "opties": [
        "parabool 2",
        "parabool 3",
        "parabool 4",
        "parabool 1"
      ],
      "antwoord": 2
    },
    {
      "type": "waaronwaar",
      "vraag": "De parabool bij y = ½x² + 7x gaat door de oorsprong.",
      "antwoord": true,
      "uitleg": "Waar. Door de oorsprong ⇔ c = 0: bij x = 0 moet y = 0 zijn. Hier is c = 0."
    },
    {
      "type": "invoer",
      "vraag": "Geef de y-coördinaat van het snijpunt van de parabool bij y = −(x + 3)(x + 5) met de y-as.",
      "antwoord": "-15|−15",
      "uitleg": "Vul x = 0 in: y = −(0 − (−3))(0 − (−5)) = −15. Het snijpunt is (0, −15)."
    }
  ]
});
