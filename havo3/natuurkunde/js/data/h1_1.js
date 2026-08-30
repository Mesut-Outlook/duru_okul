/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Kracht bij beweging
   ========================================================= */
DURU.register({
  "id": "h1-1-kracht-beweging",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Kracht bij beweging",
  "korteUitleg": "Wat doet een kracht met een beweging en hoe bereken je de resulterende kracht?",
  "icoon": "🎯",
  "kleur": "h1-thema",
  "theorie": "<h3>1.1 Kracht bij beweging</h3><div class=\"formule-box\"><strong>Resulterende kracht (F_res):</strong><br>De som van alle krachten die op een voorwerp werken.<br>• Krachten in dezelfde richting: optellen (F_res = F1 + F2)<br>• Krachten in tegengestelde richting: aftrekken (F_res = F_vooruit - F_tegen)</div><h4>Wat doet een kracht met de snelheid?</h4><ul><li><b>F_res > 0 in de bewegingsrichting:</b> De snelheid neemt toe (de beweging is <b>versneld</b>).</li><li><b>F_res > 0 tegen de bewegingsrichting in:</b> De snelheid neemt af (de beweging is <b>vertraagd</b>).</li><li><b>F_res = 0 N (krachten heffen elkaar op):</b> De snelheid blijft constant (de beweging is <b>eenparig</b>) of het voorwerp blijft stilstaan.</li></ul><h4>Tegenwerkende krachten</h4><p>Bij bewegende voorwerpen werken meestal twee belangrijke wrijvingskrachten tegen: de <b>luchtweerstand (F_l)</b> en de <b>rolweerstand (F_r)</b>.</p>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat meet je met een dynamometer (veerkrachtmeter)?",
      "opties": [
        "Een kracht in Newton (N)",
        "De snelheid in m/s",
        "De energie in Joule",
        "Het vermogen in Watt"
      ],
      "antwoord": 0,
      "uitleg": "Een dynamometer meet krachten in Newton."
    },
    {
      "type": "mc",
      "vraag": "Wat is de zwaartekracht op een massa van 5 kg op aarde (neem g = 9,8 N/kg)?",
      "opties": [
        "50 N",
        "49 N",
        "5 N",
        "9,8 N"
      ],
      "antwoord": 1,
      "uitleg": "Fz = m × g = 5 × 9,8 = 49 N."
    },
    {
      "type": "mc",
      "vraag": "Welke eigenschap van een veerkrachtig voorwerp beschrijft de veerconstante (C)?",
      "opties": [
        "Het gewicht van de veer",
        "De maximale lengte van de veer",
        "De stugheid van de veer in N/cm",
        "De kleur van de veer"
      ],
      "antwoord": 2,
      "uitleg": "De veerconstante geeft aan hoeveel kracht nodig is per centimeter uitrekking."
    },
    {
      "type": "mc",
      "vraag": "Twee krachten van 4 N en 3 N werken in dezelfde richting op een doos. Wat is de nettokracht?",
      "opties": [
        "5 N",
        "1 N",
        "12 N",
        "7 N"
      ],
      "antwoord": 3,
      "uitleg": "In dezelfde richting tel je krachten op: 4 + 3 = 7 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "De massa van een voorwerp verandert als je het meeneemt naar de maan.",
      "antwoord": false,
      "uitleg": "Onwaar: de hoeveelheid materie (massa in kg) blijft overal gelijk; alleen het gewicht verandert."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kracht heeft altijd een grootte, een richting en een aangrijpingspunt.",
      "antwoord": true,
      "uitleg": "Waar: een kracht is een vectorgrootheid."
    },
    {
      "type": "invoer",
      "vraag": "Welke letter is het standaardsymbool voor kracht in formules?",
      "antwoord": "F",
      "uitleg": "F staat voor Force (kracht)."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de SI-eenheid van kracht?",
      "antwoord": "Newton|N",
      "uitleg": "Kracht wordt gemeten in Newton (N)."
    }
  ]
});
