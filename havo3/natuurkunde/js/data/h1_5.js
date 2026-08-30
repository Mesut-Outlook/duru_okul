/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Arbeid en Energieomzetting
   ========================================================= */
DURU.register({
  "id": "h1-5-arbeid",
  "hoofdstuk": 1,
  "paragraaf": "1.5",
  "titel": "Arbeid en Energieomzetting",
  "korteUitleg": "Bereken de verrichte arbeid met W = F·s en ontdek positieve en negatieve arbeid.",
  "icoon": "⚙️",
  "kleur": "h1-thema",
  "theorie": "<h3>1.5 Arbeid</h3><div class=\"formule-box\"><strong>Arbeid berekenen:</strong><br>W = F × s<br><br>• W = arbeid in Joule (J) of Newton-meter (N·m)<br>• F = kracht in Newton (N) in de bewegingsrichting<br>• s = verplaatsing in meter (m)</div><h4>Positieve, negatieve en geen arbeid</h4><ul><li><b>Positieve arbeid:</b> De kracht werkt in de bewegingsrichting mee (voegt bewegingsenergie toe).</li><li><b>Negatieve arbeid:</b> De kracht werkt tegen de beweging in, zoals wrijving of remmen (onttrekt bewegingsenergie en zet deze om in warmte).</li><li><b>Geen arbeid (W = 0 J):</b> Als er geen verplaatsing is (s = 0 m) of als de kracht loodrecht op de verplaatsing staat.</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om mechanische arbeid te berekenen?",
      "opties": [
        "W = F × s",
        "W = F / s",
        "W = P × I",
        "W = m × g"
      ],
      "antwoord": 0,
      "uitleg": "Arbeid (W) = Kracht (F) × Afstand (s)."
    },
    {
      "type": "mc",
      "vraag": "Wat is de eenheid van natuurkundige arbeid?",
      "opties": [
        "Watt (W)",
        "Joule (J) of Newtonmeter (Nm)",
        "Newton (N)",
        "Pascal (Pa)"
      ],
      "antwoord": 1,
      "uitleg": "Arbeid wordt uitgedrukt in Joule (1 J = 1 Nm)."
    },
    {
      "type": "mc",
      "vraag": "Een kracht van 50 N verplaatst een kist over 4 meter. Hoeveel arbeid wordt verricht?",
      "opties": [
        "54 J",
        "12,5 J",
        "200 J",
        "2000 J"
      ],
      "antwoord": 2,
      "uitleg": "W = F × s = 50 × 4 = 200 Joule."
    },
    {
      "type": "mc",
      "vraag": "In welke situatie is de verrichte arbeid exact nul?",
      "opties": [
        "Als een lift omhoog gaat",
        "Als je een winkelwagen voortduwt",
        "Als een raket opstijgt",
        "Als je een zware tas stil op één plek vasthoudt zonder verplaatsing"
      ],
      "antwoord": 3,
      "uitleg": "Zonder verplaatsing (s = 0) is W = F × 0 = 0 J."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 kiloJoule (kJ) is gelijk aan 1000 Joule (J).",
      "antwoord": true,
      "uitleg": "Waar: kilo = 1000."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de uitgeoefende kracht loodrecht op de bewegingsrichting staat, wordt er maximale arbeid verricht.",
      "antwoord": false,
      "uitleg": "Onwaar: bij een loodrechte kracht (90°) is de nuttige arbeid in de bewegingsrichting exact nul."
    },
    {
      "type": "invoer",
      "vraag": "Welke letter is het symbool voor arbeid in natuurkundige formules?",
      "antwoord": "W",
      "uitleg": "W staat voor Work (arbeid)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de arbeid in Joule als een hijskraan met een kracht van 3000 N een pallet 5 meter optilt.",
      "antwoord": "15000|15000 J|15 kJ",
      "uitleg": "W = F × s = 3000 × 5 = 15.000 J."
    }
  ]
});
