/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Kracht en Versnelling (F = m · a)
   ========================================================= */
DURU.register({
  "id": "h1-3-kracht-versnelling",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Kracht en Versnelling (F = m · a)",
  "korteUitleg": "De tweede wet van Newton, versnelling berekenen en de traagheid van massa.",
  "icoon": "⚡",
  "kleur": "h1-thema",
  "theorie": "<h3>1.3 Kracht en versnelling</h3><div class=\"formule-box\"><strong>Tweede wet van Newton:</strong><br>Fres = m × a<br><br>• Fres = resulterende kracht in Newton (N)<br>• m = massa in kilogram (kg)<br>• a = versnelling in meter per seconde kwadraat (m/s²)<br><br><strong>Versnelling:</strong> a = Δv / Δt = (veind - vbegin) / t</div><h4>Traagheid (inertie)</h4><p>Massa heeft de eigenschap dat het zich verzet tegen verandering van beweging. Dit heet <b>traagheid</b>. Een zwaar voorwerp heeft een grote kracht nodig om te versnellen of af te remmen.</p>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de snelheid van een auto als de voortstuwende motorkracht groter is dan de tegenwerkende wrijvingskrachten?",
      "opties": [
        "De auto versnelt (de snelheid neemt toe)",
        "De snelheid blijft exact constant",
        "De auto remt af",
        "De auto slaat direct om"
      ],
      "antwoord": 0,
      "uitleg": "Een resulterende kracht voorwaarts veroorzaakt een versnelling (F = m × a)."
    },
    {
      "type": "mc",
      "vraag": "Een massa van 800 kg versnelt met 2 m/s². Wat is de benodigde nettokracht?",
      "opties": [
        "400 N",
        "1600 N",
        "800 N",
        "3200 N"
      ],
      "antwoord": 1,
      "uitleg": "F = m × a = 800 × 2 = 1600 N."
    },
    {
      "type": "mc",
      "vraag": "Wat is de eenheid van versnelling?",
      "opties": [
        "km/h",
        "m/s",
        "m/s²",
        "N/kg"
      ],
      "antwoord": 2,
      "uitleg": "Versnelling is de snelheidsverandering per seconde (m/s²)."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt de eerste wet van Newton?",
      "opties": [
        "Energie gaat nooit verloren",
        "Elke actie heeft een reactie",
        "Kracht is massa maal versnelling",
        "Zonder nettokracht blijft een voorwerp in rust of beweegt het met constante snelheid"
      ],
      "antwoord": 3,
      "uitleg": "Traagheidswet: als Fres = 0 N verandert de bewegingstoestand niet."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een zware vrachtwagen heeft een grotere traagheid dan een lichte personenauto.",
      "antwoord": true,
      "uitleg": "Waar: grotere massa betekent grotere traagheid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een auto met constante snelheid rijdt op de snelweg, is de motorkracht groter dan de wrijvingskracht.",
      "antwoord": false,
      "uitleg": "Onwaar: bij constante snelheid zijn de voorwaartse en tegenwerkende krachten exact in evenwicht (Fres = 0 N)."
    },
    {
      "type": "invoer",
      "vraag": "Welke formule beschrijft de tweede wet van Newton?",
      "antwoord": "F = m * a|F = m x a|F=m*a|F=m.a",
      "uitleg": "De tweede wet van Newton luidt: F = m × a."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de versnelling als een kracht van 30 N werkt op een massa van 6 kg.",
      "antwoord": "5|5 m/s2|5 m/s²",
      "uitleg": "a = F / m = 30 / 6 = 5 m/s²."
    }
  ]
});
