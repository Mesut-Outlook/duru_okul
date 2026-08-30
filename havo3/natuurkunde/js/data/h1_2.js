/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Soorten beweging & Diagrammen
   ========================================================= */
DURU.register({
  "id": "h1-2-soorten-beweging",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Soorten beweging & Diagrammen",
  "korteUitleg": "Herken bewegingssoorten in (s,t)- en (v,t)-diagrammen en reken met snelheid en afstand.",
  "icoon": "📈",
  "kleur": "h1-thema",
  "theorie": "<h3>1.2 Soorten beweging</h3><div class=\"formule-box\"><strong>Snelheid berekenen:</strong><br>v_gem = s / t &nbsp;&nbsp;|&nbsp;&nbsp; s = v × t &nbsp;&nbsp;|&nbsp;&nbsp; t = s / v<br><br><strong>Omrekenen eenheden:</strong><br>• m/s → vermenigvuldig met 3,6 → km/h<br>• km/h → deel door 3,6 → m/s</div><h4>Diagrammen herkennen</h4><ul><li><b>(s,t)-diagram:</b> De helling stelt de <b>snelheid</b> voor. Een rechte schuine lijn = constante snelheid; horizontale lijn = stilstand.</li><li><b>(v,t)-diagram:</b> De helling stelt de <b>versnelling</b> voor. Horizontale lijn = constante snelheid; schuin omhoog = eenparig versneld; schuin omlaag = eenparig vertraagd.</li><li><b>Afstand uit (v,t)-diagram:</b> De <b>oppervlakte</b> onder de grafiek is gelijk aan de afgelegde afstand s.</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het kenmerk van een eenparige beweging?",
      "opties": [
        "De snelheid blijft constant",
        "De snelheid neemt gelijkmatig toe",
        "Het voorwerp staat stil",
        "De richting verandert steeds"
      ],
      "antwoord": 0,
      "uitleg": "Eenparig betekent constante snelheid in grootte en richting."
    },
    {
      "type": "mc",
      "vraag": "Een fietser legt 150 meter af in 10 seconden. Wat is zijn gemiddelde snelheid?",
      "opties": [
        "1500 m/s",
        "15 m/s",
        "1,5 m/s",
        "54 m/s"
      ],
      "antwoord": 1,
      "uitleg": "v = s / t = 150 / 10 = 15 m/s."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel km/h is een snelheid van 20 m/s?",
      "opties": [
        "200 km/h",
        "5,55 km/h",
        "72 km/h",
        "36 km/h"
      ],
      "antwoord": 2,
      "uitleg": "20 × 3,6 = 72 km/h."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt de oppervlakte onder een (v,t)-grafiek voor?",
      "opties": [
        "De massa (m)",
        "De versnelling (a)",
        "De nettokracht (F)",
        "De afgelegde afstand (s)"
      ],
      "antwoord": 3,
      "uitleg": "De oppervlakte onder een snelheid-tijdgrafiek is gelijk aan de afstand."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een (s,t)-diagram is een eenparige beweging een rechte lijn vanuit de oorsprong.",
      "antwoord": true,
      "uitleg": "Waar: afstand groeit evenredig met de tijd bij constante snelheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om van km/h naar m/s om te rekenen moet je vermenigvuldigen met 3,6.",
      "antwoord": false,
      "uitleg": "Onwaar: je moet DELEN door 3,6 om van km/h naar m/s te gaan."
    },
    {
      "type": "invoer",
      "vraag": "Welke letter is het symbool voor de afgelegde weg (afstand)?",
      "antwoord": "s",
      "uitleg": "s staat voor afstand (spatium)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de afstand in meters bij een snelheid van 4 m/s gedurende 12 seconden.",
      "antwoord": "48|48 m|48 meter",
      "uitleg": "s = v × t = 4 × 12 = 48 meter."
    }
  ]
});
