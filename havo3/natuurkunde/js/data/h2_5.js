/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Elektromagnetisme & Inductie
   ========================================================= */
DURU.register({
  "id": "h2-5-elektromagnetisme",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Elektromagnetisme & Inductie",
  "korteUitleg": "Elektromagneten, dynamo's, generatoren, transformatoren en inductiespanning.",
  "icoon": "🧲",
  "kleur": "h2-thema",
  "theorie": "<h3>2.5 Elektromagnetisme</h3><div class=\"formule-box\"><strong>Kernconcepten:</strong><br>• <b>Elektromagneet:</b> Stroom door een spoel wekt een magnetisch veld op. Versterken via: 1) meer windingen, 2) grotere stroom $I$, 3) weekijzeren kern.<br>• <b>Inductie:</b> Beweging van een magneet t.o.v. een spoel wekt spanning op (dynamo / generator).<br>• <b>Transformator:</b> Verhoogt of verlaagt wisselspanning (hoogspanningstransport voorkomt energieverlies).</div>\n<h4>Belangrijke natuurkundige principes en rekenvaardigheden</h4>\n<p>Bij het oplossen van natuurkundige vraagstukken in deze paragraaf is een systematische aanpak essentieel:</p>\n<ol>\n  <li><b>Gegevens en gevraagd:</b> Schrijf altijd eerst op welke grootheden bekend zijn met hun juiste eenheid en wat er precies berekend moet worden.</li>\n  <li><b>Eenheden omrekenen naar standaard SI-eenheden:</b>\n    <ul>\n      <li>Afstand en lengte: altijd omrekenen naar meter ($m$) (bijv. $1\\text{ km} = 1000\\text{ m}$, $1\\text{ cm} = 0,01\\text{ m}$).</li>\n      <li>Tijd: altijd omrekenen naar seconden ($s$) (bijv. $1\\text{ uur} = 3600\\text{ s}$, $1\\text{ min} = 60\\text{ s}$).</li>\n      <li>Snelheid: van $\\text{km/h}$ naar $\\text{m/s}$ deel je door $3,6$. Van $\\text{m/s}$ naar $\\text{km/h}$ vermenigvuldig je met $3,6$.</li>\n      <li>Massa: in kilogram ($kg$) of gram ($g$) afhankelijk van de gebruikte formule en dichtheid.</li>\n    </ul>\n  </li>\n  <li><b>Formule noteren en omschrijven:</b> Noteer eerst de basisformule in letters voordat je getallen invult.</li>\n  <li><b>Conclusie en eenheid:</b> Vergeet nooit de eenheid achter je eindantwoord te vermelden en rond af op een realistisch aantal decimalen.</li>\n</ol>\n<div class=\"begrippen-box\">\n  <b>Onthoud voor de toets:</b>\n  <p>Natuurkunde gaat over het begrijpen van de werkelijkheid om ons heen. Door theorie te koppelen aan praktische experimenten en alledaagse voorbeelden (zoals verkeersveiligheid, elektrische apparaten thuis en sportbewegingen) krijg je diepgaand inzicht in de natuurwetten.</p>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welk materiaal is het meest geschikt als kern in een elektromagneet om het magnetisch veld tijdelijk te versterken?",
      "opties": [
        "Weekijzer",
        "Koper",
        "Aluminium",
        "Plastic"
      ],
      "antwoord": 0,
      "uitleg": "Weekijzer wordt direct sterk magnetisch en ontmagnetiseert direct wanneer de stroom stopt."
    },
    {
      "type": "mc",
      "vraag": "Hoe kun je de magnetische veldsterkte van een elektromagneet effectief vergroten?",
      "opties": [
        "De stroomsterkte verlagen",
        "Meer windingen toevoegen en de stroomsterkte verhogen",
        "De weekijzeren kern verwijderen",
        "De spoel afkoelen tot -50 °C"
      ],
      "antwoord": 1,
      "uitleg": "Meer windingen en grotere stroom verhogen het magneetveld."
    },
    {
      "type": "mc",
      "vraag": "Waarom zijn twee permanente magneten met hun noordpolen naar elkaar toe gericht afstotend?",
      "opties": [
        "Omdat ze van plastic zijn",
        "Ze trekken elkaar juist aan",
        "Gelijknamige magnetische polen stoten elkaar altijd af",
        "Omdat er stroom doorheen loopt"
      ],
      "antwoord": 2,
      "uitleg": "N-N en Z-Z stoten elkaar af; N-Z trekt aan."
    },
    {
      "type": "mc",
      "vraag": "Waarvoor wordt een relais in de elektrotechniek gebruikt?",
      "opties": [
        "Om warmte te meten",
        "Om wisselstroom om te zetten in zonne-energie",
        "Om batterijen op te laden",
        "Om met een kleine stroom een grote hoofdstroomkring veilig in of uit te schakelen"
      ],
      "antwoord": 3,
      "uitleg": "Een relais is een elektromagnetische schakelaar."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een elektromagneet blijft permanent magnetisch als je de batterij loskoppelt.",
      "antwoord": false,
      "uitleg": "Onwaar: zonder stroom verdwijnt het magnetisch veld van een elektromagneet direct."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het magnetisch veld van een aarde beschermt ons tegen gevaarlijke kosmische zonnedeeltjes.",
      "antwoord": true,
      "uitleg": "Waar: het aardmagnetisch veld buigt de zonnewind af."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet een spiraalvormig gewikkelde koperdraad die als magneet werkt bij stroomdoorgang?",
      "antwoord": "spoel|solenoïde",
      "uitleg": "Een spoel wekt een magnetisch veld op."
    },
    {
      "type": "invoer",
      "vraag": "Welke twee polen heeft elke magneet?",
      "antwoord": "noordpool en zuidpool|noord en zuid",
      "uitleg": "Elke magneet heeft een noordpool (N) en een zuidpool (Z)."
    }
  ]
});
