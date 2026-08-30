/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Sensoren (NTC, PTC, LDR)
   ========================================================= */
DURU.register({
  "id": "h4-5-sensoren-ntc-ptc-ldr",
  "hoofdstuk": 4,
  "paragraaf": "4.5",
  "titel": "Sensoren (NTC, PTC, LDR)",
  "korteUitleg": "Hoe NTC-, PTC- en LDR-sensoren fysische grootheden omzetten in elektrische signalen.",
  "icoon": "🎛️",
  "kleur": "h4-thema",
  "theorie": "<h3>4.5 Temperatuur, weerstand en sensoren</h3><div class='formule-box'><strong>Soorten sensoren:</strong><br>• <b>NTC (Negative Temperature Coefficient):</b> Temperatuur ↑ -> Weerstand ↓ (thermometers/thermostaat).<br>• <b>PTC (Positive Temperature Coefficient):</b> Temperatuur ↑ -> Weerstand ↑ (beveiliging/gloeidraad).<br>• <b>LDR (Light Dependent Resistor):</b> Lichtsterkte ↑ -> Weerstand ↓ (schemerschakelaar).</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het absolute nulpunt in graden Celsius (0 Kelvin)?",
      "opties": [
        "-273,15 °C",
        "0 °C",
        "-100 °C",
        "-500 °C"
      ],
      "antwoord": 0,
      "uitleg": "0 Kelvin = -273,15 °C (alle moleculaire trilling stopt)."
    },
    {
      "type": "mc",
      "vraag": "Hoe reken je een temperatuur in graden Celsius om naar Kelvin?",
      "opties": [
        "T (in K) = T (in °C) - 273",
        "T (in K) = T (in °C) + 273",
        "T (in K) = T (in °C) × 3,6",
        "T (in K) = T (in °C) / 100"
      ],
      "antwoord": 1,
      "uitleg": "De absolute temperatuur in Kelvin bereken je met de formule: T in Kelvin = T in Celsius + 273."
    },
    {
      "type": "mc",
      "vraag": "Wat is de functie van een bimetaal in een traditionele thermostaat?",
      "opties": [
        "Het meet de luchtdruk",
        "Het wekt elektriciteit op",
        "Twee verschillende metalen zetten bij verhitting ongelijk uit waardoor de strip kromtrekt en een contact verbreekt",
        "Het smelt bij kamertemperatuur"
      ],
      "antwoord": 2,
      "uitleg": "Verschil in uitzettingscoëfficiënt doet het bimetaal buigen."
    },
    {
      "type": "mc",
      "vraag": "Hoe verandert de weerstand van een NTC-sensor wanneer de temperatuur stijgt?",
      "opties": [
        "De weerstand wordt oneindig",
        "De weerstand stijgt",
        "De weerstand blijft gelijk",
        "De weerstand daalt (Negative Temperature Coefficient)"
      ],
      "antwoord": 3,
      "uitleg": "NTC = Negatieve Temperatuur Coëfficiënt: warmer betekent lagere weerstand."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuur van 0 Kelvin kan in de praktijk nooit volledig worden onderschreden.",
      "antwoord": true,
      "uitleg": "Waar: 0 K is de laagst denkbare temperatuur in het universum."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een temperatuurverschil van 10 graden Celsius is gelijk aan een verschil van 283 Kelvin.",
      "antwoord": false,
      "uitleg": "Onwaar: de schaalstappen van Celsius en Kelvin zijn identiek: een VERSCHIL (ΔT) van 10 °C is exact 10 K."
    },
    {
      "type": "invoer",
      "vraag": "Hoeveel Kelvin is het vriespunt van zuiver water (0 °C)?",
      "antwoord": "273|273 K|273,15 K",
      "uitleg": "0 + 273 = 273 K."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet een lichtgevoelige weerstandssensor waarvan de weerstand daalt als er licht op valt?",
      "antwoord": "LDR|lichtsensor",
      "uitleg": "LDR staat voor Light Dependent Resistor."
    }
  ]
});
