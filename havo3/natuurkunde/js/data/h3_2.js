/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Atoombouw, Kernstraling & Halveringstijd
   ========================================================= */
DURU.register({
  "id": "h3-2-atoom-halveringstijd",
  "hoofdstuk": 3,
  "paragraaf": "3.2",
  "titel": "Atoombouw, Kernstraling & Halveringstijd",
  "korteUitleg": "Protonen, neutronen, isotopen, alfa/bèta/gammastraling en rekenen met halveringstijd.",
  "icoon": "⚛️",
  "kleur": "h3-thema",
  "theorie": "<h3>3.2 Straling uit atomen</h3><div class=\"formule-box\"><strong>Kernstraling soorten:</strong><br>• <b>Alfa ($\\alpha$):</b> Heliumkernen ($2\\text{p} + 2\\text{n}$), groot ioniserend vermogen, gestopt door papier/huid.<br>• <b>Bèta ($\\beta$):</b> Snelle elektronen, matig doordringend vermogen, gestopt door aluminium.<br>• <b>Gamma ($\\gamma$):</b> Energierijke EM-golven, zeer groot doordringend vermogen, afgeremd door dik lood/beton.<br><br><strong>Halveringstijd ($t_{1/2}$):</strong><br>De tijd waarin de helft van de radioactieve kernen vervalt. Activiteit $A$ in <b>Becquerel (Bq)</b>.</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat stelt de spiegelwet bij terugkaatsing van licht op een vlakke spiegel?",
      "opties": [
        "Hoek van inval is gelijk aan hoek van terugkaatsing (∠i = ∠t)",
        "De hoek van terugkaatsing is altijd 90°",
        "De hoek van inval is twee keer zo groot",
        "Het licht verdwijnt in de spiegel"
      ],
      "antwoord": 0,
      "uitleg": "Spiegelwet: ∠i = ∠t."
    },
    {
      "type": "mc",
      "vraag": "Een lichtstraal valt in onder een hoek van 35° met de normaal. Wat is de terugkaatsingshoek?",
      "opties": [
        "55°",
        "35°",
        "70°",
        "90°"
      ],
      "antwoord": 1,
      "uitleg": "Volgens de spiegelwet is de hoek van terugkaatsing gelijk aan de hoek van inval: ∠t = ∠i = 35°."
    },
    {
      "type": "mc",
      "vraag": "Wat voor soort spiegelbeeld zie je in een gewone vlakke passpiegel?",
      "opties": [
        "Een vergroot beeld",
        "Een reëel beeld op zijn kop",
        "Een virtueel spiegelbeeld dat even groot is als het voorwerp",
        "Een donkere vlek"
      ],
      "antwoord": 2,
      "uitleg": "Het spiegelbeeld in een vlakke spiegel is virtueel, rechtopstaand en even groot."
    },
    {
      "type": "mc",
      "vraag": "Wat is diffuse terugkaatsing?",
      "opties": [
        "Licht buigt af in een prisma",
        "Licht wordt gereflecteerd als in een spiegel",
        "Licht wordt omgezet in elektriciteit",
        "Licht wordt door een ruw oppervlak in alle richtingen verstrooid"
      ],
      "antwoord": 3,
      "uitleg": "Diffuus betekent verstrooid in alle richtingen (bijv. op een muur of papier)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De normaal is een denkbeeldige lijn die onder een hoek van 90° op het spiegeloppervlak staat.",
      "antwoord": true,
      "uitleg": "Waar: de normaal staat altijd loodrecht op het spiegelvlak."
    },
    {
      "type": "waaronwaar",
      "vraag": "De hoek van inval meet je tussen de lichtstraal en het spiegeloppervlak zelf.",
      "antwoord": false,
      "uitleg": "Onwaar: hoeken meet je ALTIJD ten opzichte van de NORMAAL, niet het oppervlak."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet de loodrechte hulplijn waarop hoeken worden gemeten?",
      "antwoord": "normaal",
      "uitleg": "De normaal staat loodrecht op het oppervlak."
    },
    {
      "type": "invoer",
      "vraag": "Als de hoek tussen de invallende straal en de spiegel 40° is, hoe groot is dan de hoek van inval ∠i?",
      "antwoord": "50|50 graden|50°",
      "uitleg": "∠i = 90° - 40° = 50°."
    }
  ]
});
