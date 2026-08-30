/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Hefbomen & Draaipunten
   ========================================================= */
DURU.register({
  "id": "h8-1-hefbomen",
  "hoofdstuk": 8,
  "paragraaf": "8.1",
  "titel": "Hefbomen & Draaipunten",
  "korteUitleg": "Draaipunt, spierkracht, werkkracht, de arm van een kracht en soorten hefbomen.",
  "icoon": "🪚",
  "kleur": "h8-thema",
  "theorie": "<h3>8.1 Hefbomen</h3><div class='formule-box'><strong>Begrippen:</strong><br>• <b>Draaipunt ($):</b> Het vaste punt waar de hefboom omheen draait.<br>• <b>Arm van de kracht ($):</b> De kortste (loodrechte) afstand van het draaipunt tot de werklijn van de kracht.<br>• <b>Werklijn:</b> De oneindige lijn in de richting van de uitgeoefende kracht.</div><h4>Soorten hefbomen</h4><ul><li><b>Dubbelzijdige hefboom:</b> Het draaipunt ligt tussen de twee krachten in (bijv. schaar, koevoet, wipwap).</li><li><b>Enkelzijdige hefboom:</b> Beide krachten liggen aan dezelfde kant van het draaipunt (bijv. kruiwagen, notenkraker, flesopener, pincet).</li><li><b>Krachtvergroting:</b> Als {\text{spier}} > r_{\text{werk}}$, dan is {\text{werk}} > F_{\text{spier}}$ (bijv. betonschaar).</li><li><b>Krachtverkleining:</b> Als {\text{spier}} < r_{\text{werk}}$, dan is {\text{werk}} < F_{\text{spier}}$ voor precisie (bijv. pincet).</li></ul>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Hoe luidt de hefboomwet in evenwicht?",
      "opties": [
        "F1 × d1 = F2 × d2 (kracht × arm links = kracht × arm rechts)",
        "F1 / d1 = F2 / d2",
        "F1 + d1 = F2 + d2",
        "F1 × F2 = d1 × d2"
      ],
      "antwoord": 0,
      "uitleg": "Evenwicht: som van momenten linksom = som van momenten rechtsom."
    },
    {
      "type": "mc",
      "vraag": "Wat is het moment (M) van een kracht van 40 N met een arm van 0,5 meter?",
      "opties": [
        "80 Nm",
        "20 Nm",
        "40,5 Nm",
        "200 Nm"
      ],
      "antwoord": 1,
      "uitleg": "M = F × d = 40 × 0,5 = 20 Nm."
    },
    {
      "type": "mc",
      "vraag": "Waarom heeft een betonschaar of notenkraker hele lange handvatten en korte bekken?",
      "opties": [
        "Voor het comfort",
        "Om de schaar lichter te maken",
        "Om met een kleine spierkracht op de lange arm een gigantische knipkracht op de korte arm te genereren",
        "Om minder ver te hoeven knijpen"
      ],
      "antwoord": 2,
      "uitleg": "Grote arm = grote krachtvermenigvuldiging."
    },
    {
      "type": "mc",
      "vraag": "Wat is de arm van een kracht?",
      "opties": [
        "De afstand tot de grond",
        "De totale lengte van de hefboom",
        "Het gewicht van het draaipunt",
        "De kortste loodrechte afstand van het draaipunt tot de werklijn van de kracht"
      ],
      "antwoord": 3,
      "uitleg": "Arm d is altijd loodrecht op de werklijn van F."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als een kracht precies door het draaipunt heen gaat, is het moment van die kracht gelijk aan nul.",
      "antwoord": true,
      "uitleg": "Waar: omdat d = 0 m is M = F × 0 = 0 Nm (geen draaieffect)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De eenheid van moment (draaikracht) is Newton per meter (N/m).",
      "antwoord": false,
      "uitleg": "Onwaar: de eenheid is Newtonmeter (Nm = N × m)."
    },
    {
      "type": "invoer",
      "vraag": "Welke eenheid hoort bij het moment van een kracht?",
      "antwoord": "Nm|Newtonmeter",
      "uitleg": "Moment wordt gemeten in Newtonmeter (Nm)."
    },
    {
      "type": "invoer",
      "vraag": "Als een kracht van 10 N een arm van 3 meter heeft, wat is dan het moment in Nm?",
      "antwoord": "30|30 Nm",
      "uitleg": "M = F × d = 10 × 3 = 30 Nm."
    }
  ]
});
