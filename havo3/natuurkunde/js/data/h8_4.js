/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Druk & Oppervlakte
   ========================================================= */
DURU.register({
  "id": "h8-4-druk",
  "hoofdstuk": 8,
  "paragraaf": "8.4",
  "titel": "Druk & Oppervlakte",
  "korteUitleg": "De formule p = F / A, eenheden Pascal (Pa) en N/cm², druk vergroten en verkleinen.",
  "icoon": "📐",
  "kleur": "h8-thema",
  "theorie": "<h3>8.4 Druk</h3><div class='formule-box'><strong>Drukformule:</strong><br>89565p = \frac{F}{A}89565<br>• $ = druk in Pascal ($\text{Pa} = \text{N/m}^2$) of $\text{N/cm}^2$<br>• $ = kracht loodrecht op het oppervlak in Newton ($\text{N}$)<br>• $ = oppervlakte in $\text{m}^2$ (of $\text{cm}^2$)<br><br><strong>Omrekenen:</strong> \text{ N/cm}^2 = 10.000\text{ N/m}^2 = 10.000\text{ Pa}$.</div><h4>Druk beïnvloeden</h4><ul><li><b>Druk verkleinen (groot oppervlak $):</b> Sneeuwschoenen, rupsbanden, brede trekkerbanden.</li><li><b>Druk vergroten (klein oppervlak $):</b> Naaldpunt, scherp mes, schaatsen, spijker.</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je voor de kinetische energie (bewegingsenergie) van een voorwerp?",
      "opties": [
        "Ekin = 0,5 × m × v²",
        "Ekin = m × g × h",
        "Ekin = F × s",
        "Ekin = P × t"
      ],
      "antwoord": 0,
      "uitleg": "Ekin = 0,5 × m × v²."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de kinetische energie van een auto als de snelheid verdrievoudigt (3× zo snel)?",
      "opties": [
        "De kinetische energie wordt 3 keer zo groot",
        "De kinetische energie wordt 9 keer zo groot (3²)",
        "De kinetische energie wordt 6 keer zo groot",
        "De energie blijft gelijk"
      ],
      "antwoord": 1,
      "uitleg": "Kwadratisch verband: 3² = 9× zoveel kinetische energie."
    },
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je voor de potentiële zwaarte-energie op hoogte?",
      "opties": [
        "Ez = F / s",
        "Ez = 0,5 × m × v²",
        "Ez = m × g × h",
        "Ez = U × I"
      ],
      "antwoord": 2,
      "uitleg": "Zwaarte-energie Ez = m × g × h."
    },
    {
      "type": "mc",
      "vraag": "Een massa van 2 kg bevindt zich op 5 meter hoogte (g = 9,8 N/kg). Hoe groot is de zwaarte-energie?",
      "opties": [
        "100 J",
        "10 J",
        "49 J",
        "98 J"
      ],
      "antwoord": 3,
      "uitleg": "Ez = 2 × 9,8 × 5 = 98 Joule."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een vallende bal zet tijdens zijn val potentiële zwaarte-energie om in kinetische bewegingsenergie.",
      "antwoord": true,
      "uitleg": "Waar: hoogte daalt en snelheid neemt toe."
    },
    {
      "type": "waaronwaar",
      "vraag": "De kinetische energie van een rijdende vrachtwagen is onafhankelijk van zijn massa.",
      "antwoord": false,
      "uitleg": "Onwaar: Ekin is recht evenredig met de massa m (dubbele massa = dubbele energie)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de kinetische energie in Joule van een massa van 4 kg met een snelheid van 3 m/s.",
      "antwoord": "18|18 J|18 Joule",
      "uitleg": "Ekin = 0,5 × 4 × 3² = 2 × 9 = 18 Joule."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de zwaarte-energie in Joule op de grond (hoogte h = 0 m)?",
      "antwoord": "0|0 J|0 Joule",
      "uitleg": "Op de grond is h = 0 dus Ez = 0 J."
    }
  ]
});
