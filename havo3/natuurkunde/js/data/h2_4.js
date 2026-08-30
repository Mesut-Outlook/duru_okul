/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Elektrisch Vermogen & Energieverbruik
   ========================================================= */
DURU.register({
  "id": "h2-4-vermogen-energie",
  "hoofdstuk": 2,
  "paragraaf": "2.4",
  "titel": "Elektrisch Vermogen & Energieverbruik",
  "korteUitleg": "Vermogen berekenen (P = U·I), energieverbruik in Joule en kWh (E = P·t) en kosten.",
  "icoon": "⚡",
  "kleur": "h2-thema",
  "theorie": "<h3>2.4 Energie en vermogen</h3><div class=\"formule-box\"><strong>Formules:</strong><br>• <b>Vermogen ($P$):</b> $P = U \\cdot I$ (in Watt: $1\\text{ W} = 1\\text{ J/s}$)<br>• <b>Energie in Joule:</b> $E = P \\cdot t$ (met $P$ in Watt en $t$ in seconden)<br>• <b>Energie in kilowattuur:</b> $E = P \\cdot t$ (met $P$ in kW en $t$ in uren)<br>• <b>Omrekenen:</b> $1\\text{ kWh} = 3.600.000\\text{ J} = 3{,}6\\text{ MJ}$<br>• <b>Kosten:</b> $\\text{Kosten} = E\\text{ (in kWh)} \\times \\text{prijs per kWh}$</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om het elektrisch vermogen van een apparaat te berekenen?",
      "opties": [
        "P = U × I",
        "P = U / I",
        "P = I / U",
        "P = U + I"
      ],
      "antwoord": 0,
      "uitleg": "P = U × I (Vermogen in Watt = Spanning × Stroom)."
    },
    {
      "type": "mc",
      "vraag": "Een waterkoker van 2300 W is aangesloten op 230 V. Hoe groot is de stroomsterkte?",
      "opties": [
        "100 A",
        "10 A",
        "1 A",
        "529 A"
      ],
      "antwoord": 1,
      "uitleg": "I = P / U = 2300 / 230 = 10 A."
    },
    {
      "type": "mc",
      "vraag": "Welke formule geeft het energieverbruik van een apparaat in kiloWattuur (kWh)?",
      "opties": [
        "E = I / t",
        "E = P × U",
        "E = P (in kW) × t (in uren)",
        "E = U / R"
      ],
      "antwoord": 2,
      "uitleg": "Energie (kWh) = Vermogen (kW) × Tijd (h)."
    },
    {
      "type": "mc",
      "vraag": "Een kachel van 2 kW brandt gedurende 3 uur. Hoeveel kWh energie is verbruikt?",
      "opties": [
        "0,66 kWh",
        "5 kWh",
        "1,5 kWh",
        "6 kWh"
      ],
      "antwoord": 3,
      "uitleg": "E = P × t = 2 × 3 = 6 kWh."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 kiloWattuur (kWh) is exact gelijk aan 3.600.000 Joule (3,6 MJ).",
      "antwoord": true,
      "uitleg": "Waar: 1000 W × 3600 s = 3.600.000 J."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een apparaat met een hoog vermogen (bijv. 2000 W) verbruikt per seconde minder energie dan een apparaat van 50 W.",
      "antwoord": false,
      "uitleg": "Onwaar: vermogen is het energieverbruik PER SECONDE. 2000 W verbruikt 2000 J/s."
    },
    {
      "type": "invoer",
      "vraag": "Wat is de officiële eenheid van vermogen?",
      "antwoord": "Watt|W",
      "uitleg": "Vermogen wordt gemeten in Watt (W)."
    },
    {
      "type": "invoer",
      "vraag": "Hoeveel Watt is gelijk aan 1,5 kilowatt (kW)?",
      "antwoord": "1500|1500 W",
      "uitleg": "1,5 × 1000 = 1500 W."
    }
  ]
});
