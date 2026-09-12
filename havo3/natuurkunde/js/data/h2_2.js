/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Weerstand & Wet van Ohm (R = U / I)
   ========================================================= */
DURU.register({
  "id": "h2-2-weerstand-ohm",
  "hoofdstuk": 2,
  "paragraaf": "2.2",
  "titel": "Weerstand & Wet van Ohm (R = U / I)",
  "korteUitleg": "Weerstand berekenen in Ohm, ohmse weerstanden en factoren van draadweerstand.",
  "icoon": "💡",
  "kleur": "h2-thema",
  "theorie": "<h3>2.2 Weerstand en de Wet van Ohm</h3><div class=\"formule-box\"><strong>Wet van Ohm:</strong><br>R = U/I &nbsp;&nbsp;|&nbsp;&nbsp; U = I · R &nbsp;&nbsp;|&nbsp;&nbsp; I = U/R<br><br>• R = weerstand in <b>Ohm (Ω)</b><br>• U = spanning in <b>Volt (V)</b><br>• I = stroomsterkte in <b>Ampère (A)</b></div><h4>Factoren voor draadweerstand</h4><ul><li><b>Lengte (l):</b> Hoe langer de draad, hoe <b>groter</b> de weerstand (R ~ l).</li><li><b>Doorsnede (A):</b> Hoe dikker de draad, hoe <b>kleiner</b> de weerstand (R ~ 1/A).</li><li><b>Materiaal:</b> Bepaald door de soortelijke weerstand (ρ). Koper heeft lage weerstand, constantaan een matige.</li><li><b>Temperatuur:</b> Bij de meeste metalen stijgt de weerstand als de draad warmer wordt (PTC).</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter (m) (bijv. 1 km = 1000 m, 1 cm = 0,01 m).</li>\n      <li>Tijd: altijd omrekenen naar seconden (s) (bijv. 1 uur = 3600 s, 1 min = 60 s).</li>\n      <li>Snelheid: van km/h naar m/s deel je door 3,6. Van m/s naar km/h vermenigvuldig je met 3,6.</li>\n      <li>Massa: in kilogram (kg) of gram (g) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule staat bekend als de wet van Ohm?",
      "opties": [
        "U = I × R",
        "U = I / R",
        "R = U × I",
        "I = U × R"
      ],
      "antwoord": 0,
      "uitleg": "Wet van Ohm: U = I × R."
    },
    {
      "type": "mc",
      "vraag": "Een weerstand van 50 Ω is aangesloten op een spanning van 10 V. Wat is de stroomsterkte?",
      "opties": [
        "500 A",
        "0,2 A",
        "5 A",
        "2 A"
      ],
      "antwoord": 1,
      "uitleg": "I = U / R = 10 / 50 = 0,2 A."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de stroomsterkte als de weerstand in de schakeling groter wordt bij constante spanning?",
      "opties": [
        "De stroomsterkte blijft gelijk",
        "De stroomsterkte neemt toe",
        "De stroomsterkte neemt af",
        "De spanning wordt nul"
      ],
      "antwoord": 2,
      "uitleg": "Grotere weerstand belemmert de stroom meer (I = U / R)."
    },
    {
      "type": "mc",
      "vraag": "Welk materiaal is een uitstekende elektrische geleider?",
      "opties": [
        "Porselein",
        "Glas",
        "Rubber",
        "Koper"
      ],
      "antwoord": 3,
      "uitleg": "Koper bevat veel vrije elektronen en geleidt stroom zeer goed."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een lange dunne draad heeft een lagere weerstand dan een korte dikke draad van hetzelfde materiaal.",
      "antwoord": false,
      "uitleg": "Onwaar: langer en dunner betekent juist een HOGERE weerstand."
    },
    {
      "type": "waaronwaar",
      "vraag": "Isolatoren zoals plastic en rubber laten vrijwel geen elektrische stroom door.",
      "antwoord": true,
      "uitleg": "Waar: isolatoren hebben geen vrije ladingdragers."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de eenheid van elektrische weerstand?",
      "antwoord": "Ohm|Ω",
      "uitleg": "Weerstand wordt gemeten in Ohm (Ω)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de spanning in Volt als I = 3 A en R = 15 Ω.",
      "antwoord": "45|45 V|45 Volt",
      "uitleg": "U = I × R = 3 × 15 = 45 Volt."
    }
  ]
});
