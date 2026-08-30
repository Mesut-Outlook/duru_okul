/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Rekenen aan Hefbomen & Momenten
   ========================================================= */
DURU.register({
  "id": "h8-2-rekenen-hefbomen",
  "hoofdstuk": 8,
  "paragraaf": "8.2",
  "titel": "Rekenen aan Hefbomen & Momenten",
  "korteUitleg": "Het moment van een kracht (M = F × r), de momentenwet en het zwaartepunt.",
  "icoon": "⚖️",
  "kleur": "h8-thema",
  "theorie": "<h3>8.2 Rekenen aan hefbomen</h3><div class='formule-box'><strong>Formules:</strong><br>• <b>Moment van een kracht ($):</b> 89565M = F \times r89565 ($ in $\text{Nm}$, $ in $\text{N}$, $ in $\text{m}$)<br>• <b>Hefboomwet / Momentenwet in evenwicht:</b> 89565M_{\text{links}} = M_{\text{rechts}} iff F_1 \times r_1 = F_2 \times r_289565<br>• <b>Zwaartekracht:</b>  = m \times g$ ( approx 10\text{ N/kg}$ of {,}8\text{ N/kg}$)</div><h4>Het Zwaartepunt ($)</h4><p>Het zwaartepunt is het punt waar je de totale zwaartekracht op het voorwerp geconcentreerd kunt denken. Een hefboom is stabiel als het zwaartepunt zich recht onder het ophangpunt bevindt.</p>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is het kenmerk van een vaste katrol bij het hijsen van een last?",
      "opties": [
        "De benodigde trekkracht blijft gelijk aan het gewicht van de last, maar de richting verandert",
        "De benodigde trekkracht halveert",
        "De touwlengte verdubbelt",
        "De zwaartekracht verdwijnt"
      ],
      "antwoord": 0,
      "uitleg": "Een vaste katrol geeft geen krachtwinst, alleen richtingsgemak."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel spierkracht is nodig om een last van 600 N op te tillen met één losse katrol (2 dragende touwdelen)?",
      "opties": [
        "600 N",
        "300 N",
        "1200 N",
        "150 N"
      ],
      "antwoord": 1,
      "uitleg": "Kracht halveert: 600 / 2 = 300 N."
    },
    {
      "type": "mc",
      "vraag": "Wat is de gulden regel van de mechanica bij eenvoudige werktuigen zoals katrollen en hefbomen?",
      "opties": [
        "Kracht en afstand nemen beide af",
        "Werktuigen leveren gratis extra energie",
        "Wat je wint aan kracht, verlies je aan afstand (de benodigde arbeid blijft gelijk)",
        "Arbeid wordt verdubbeld"
      ],
      "antwoord": 2,
      "uitleg": "De totale arbeid blijft gelijk: F halveert betekent s verdubbelt."
    },
    {
      "type": "mc",
      "vraag": "In een takel met 4 dragende touwen hijs je een last 2 meter omhoog. Hoeveel meter touw moet je binnenhalen?",
      "opties": [
        "0,5 meter",
        "2 meter",
        "4 meter",
        "8 meter"
      ],
      "antwoord": 3,
      "uitleg": "Touwlengte = 4 × 2 m = 8 meter."
    },
    {
      "type": "waaronwaar",
      "vraag": "Met een takel kun je energie uit het niets creëren.",
      "antwoord": false,
      "uitleg": "Onwaar: energiebehoud geldt altijd; je spaart kracht ten koste van meer touwlengte."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een losse katrol beweegt de katrol zelf mee met de opgetilde last.",
      "antwoord": true,
      "uitleg": "Waar: vandaar de naam losse katrol."
    },
    {
      "type": "invoer",
      "vraag": "Hoeveel keer zo klein wordt de benodigde spierkracht bij gebruik van een takel met 4 dragende touwen?",
      "antwoord": "4|4x|4 keer",
      "uitleg": "Factor 4 krachtvoordeel."
    },
    {
      "type": "invoer",
      "vraag": "Een last van 500 N wordt gehesen met een vaste katrol. Hoeveel Newton spankracht moet je leveren?",
      "antwoord": "500|500 N|500 Newton",
      "uitleg": "Bij een vaste katrol is Ftrek = Flast = 500 N."
    }
  ]
});
