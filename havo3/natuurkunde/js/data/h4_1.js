/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Stofeigenschappen & Dichtheid
   ========================================================= */
DURU.register({
  "id": "h4-1-stofeigenschappen-dichtheid",
  "hoofdstuk": 4,
  "paragraaf": "4.1",
  "titel": "Stofeigenschappen & Dichtheid",
  "korteUitleg": "Dichtheid berekenen (ρ = m / V), stofeigenschappen, onderdompelmethode en drijven/zinken.",
  "icoon": "🧱",
  "kleur": "h4-thema",
  "theorie": "<h3>4.1 Stofeigenschappen en dichtheid</h3><div class='formule-box'><strong>Dichtheid berekenen:</strong><br>ρ = m / V &nbsp;&nbsp;|&nbsp;&nbsp; m = ρ × V &nbsp;&nbsp;|&nbsp;&nbsp; V = m / ρ<br><br>• ρ (rho) = dichtheid in g/cm³ of kg/m³ (1 g/cm³ = 1000 kg/m³)<br>• m = massa in gram (g) of kilogram (kg)<br>• V = volume in cm³, dm³ (liter) of m³</div><h4>Drijven, zweven en zinken</h4><ul><li><b>Drijven:</b> ρ_voorwerp < ρ_vloeistof (bijv. hout of ijs op water).</li><li><b>Zweven:</b> ρ_voorwerp = ρ_vloeistof.</li><li><b>Zinken:</b> ρ_voorwerp > ρ_vloeistof (bijv. ijzer of steen in water).</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welke formule gebruik je om de massadichtheid van een stof te berekenen?",
      "opties": [
        "ρ = m / V",
        "ρ = m × V",
        "ρ = V / m",
        "ρ = m + V"
      ],
      "antwoord": 0,
      "uitleg": "Dichtheid (ρ) = Massa (m) / Volume (V)."
    },
    {
      "type": "mc",
      "vraag": "Een metalen blokje heeft een massa van 54 gram en een volume van 20 cm³. Wat is de dichtheid?",
      "opties": [
        "1080 g/cm³",
        "2,7 g/cm³ (aluminium)",
        "0,37 g/cm³",
        "7,8 g/cm³"
      ],
      "antwoord": 1,
      "uitleg": "ρ = 54 / 20 = 2,7 g/cm³."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel kg/m³ is een dichtheid van 1,0 g/cm³?",
      "opties": [
        "10 kg/m³",
        "100 kg/m³",
        "1000 kg/m³",
        "0,001 kg/m³"
      ],
      "antwoord": 2,
      "uitleg": "1 g/cm³ = 1000 kg/m³."
    },
    {
      "type": "mc",
      "vraag": "Met welke methode bepaal je het volume van een onregelmatig gevormd steentje?",
      "opties": [
        "Smelten in een oven",
        "Lengte × breedte × hoogte meten",
        "Wegen op een weegschaal",
        "De onderdompelmethode in een maatcilinder met water"
      ],
      "antwoord": 3,
      "uitleg": "Onderdompelen: V = V_eind - V_begin."
    },
    {
      "type": "waaronwaar",
      "vraag": "Dichtheid is een stofeigenschap die onafhankelijk is van de grootte van het voorwerp.",
      "antwoord": true,
      "uitleg": "Waar: een grote ijzeren balk heeft dezelfde dichtheid als een klein ijzeren spijkertje."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een voorwerp met een dichtheid van 1,5 g/cm³ blijft drijven op water.",
      "antwoord": false,
      "uitleg": "Onwaar: omdat 1,5 > 1,0 zinkt het voorwerp naar de bodem."
    },
    {
      "type": "invoer",
      "vraag": "Welke Griekse letter is het standaardsymbool voor dichtheid?",
      "antwoord": "rho|ρ",
      "uitleg": "De Griekse letter rho (ρ)."
    },
    {
      "type": "invoer",
      "vraag": "Bereken de massa in gram van 50 cm³ goud (dichtheid goud = 19,3 g/cm³).",
      "antwoord": "965|965 g|965 gram",
      "uitleg": "m = ρ × V = 19,3 × 50 = 965 gram."
    }
  ]
});
