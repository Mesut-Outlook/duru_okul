/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 1.3: Budgetteren
   ========================================================= */
DURU.register({
  "id": "h1-3",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Budgetteren",
  "korteUitleg": "Een begroting opstellen, omrekenen per maand/jaar, budgetoverzicht en NIBUD.",
  "icoon": "📊",
  "kleur": "oranje",
  "theorie": "<h3>1.3 Budgetteren</h3>\n<p><b>Budgetteren</b> is het nauwkeurig op elkaar afstemmen van je verwachte inkomsten en uitgaven over een komende periode (bijvoorbeeld een maand of een jaar). Dit doe je door een <b>begroting (budgetplan)</b> op te stellen.</p>\n<h4>De drie uitkomsten van een begroting</h4>\n<p>Wanneer je alle verwachte inkomsten en uitgaven op een rij zet, zijn er drie mogelijke uitkomsten:</p>\n<ul>\n  <li><b>Begrotingsevenwicht:</b> De totale verwachte inkomsten zijn precies gelijk aan de totale verwachte uitgaven. Er is geen overschot en geen tekort (saldo = € 0).</li>\n  <li><b>Begrotingsoverschot:</b> De verwachte inkomsten zijn groter dan de verwachte uitgaven. Je houdt geld over dat je kunt sparen of gebruiken voor extra aflossingen.</li>\n  <li><b>Begrotingstekort:</b> De verwachte uitgaven zijn hoger dan de inkomsten. Je komt geld tekort en moet direct maatregelen nemen: bezuinigen op variabele uitgaven of extra inkomsten zoeken.</li>\n</ul>\n<h4>Omrekenen van financiële periodes</h4>\n<p>Om inkomsten en uitgaven goed met elkaar te kunnen vergelijken, moet je alle bedragen altijd omrekenen naar dezelfde standaardperiode (meestal <b>per maand</b>). Let goed op de wiskundige regels:</p>\n<div class=\"formule-box\">\n  <b>Standaard omrekenformules:</b><br>\n  • <b>Van week naar maand:</b> <code>(bedrag per week × 52) / 12</code> (want 1 jaar telt 52 weken en 12 maanden; 52 / 12 = 4,33 weken per maand!)<br>\n  • <b>Van kwartaal naar maand:</b> <code>bedrag per kwartaal / 3</code> (want 1 kwartaal = 3 maanden)<br>\n  • <b>Van jaar naar maand:</b> <code>bedrag per jaar / 12</code><br>\n  • <b>Van maand naar jaar:</b> <code>bedrag per maand × 12</code><br>\n  • <b>Van maand naar week:</b> <code>(bedrag per maand × 12) / 52</code>\n</div>\n<p>Het <b>NIBUD (Nationaal Instituut voor Budgetvoorlichting)</b> is een onafhankelijke stichting die consumenten informeert en adviseert over verstandig budgetteren en geldbeheer.</p>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Duru krijgt € 15 zakgeld per week. Hoeveel zakgeld ontvangt zij gemiddeld per maand?",
      "opties": [
        "€ 60",
        "€ 70",
        "€ 65",
        "€ 75"
      ],
      "antwoord": 2,
      "uitleg": "(15 × 52) / 12 = 780 / 12 = € 65 per maand."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een jaar telt precies 48 weken, waardoor 1 maand altijd gelijk is aan exact 4 weken.",
      "antwoord": false,
      "uitleg": "Een jaar heeft 52 weken (365 dagen). 52 / 12 is gemiddeld 4,33 weken per maand."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet de situatie waarin de verwachte inkomsten groter zijn dan de verwachte uitgaven?",
      "antwoord": "begrotingsoverschot|overschot",
      "uitleg": "Bij een begrotingsoverschot houd je geld over in je begroting."
    },
    {
      "type": "mc",
      "vraag": "Wat is het voornaamste doel van budgetteren?",
      "opties": [
        "Inkomsten en uitgaven op elkaar afstemmen om tekorten te voorkomen.",
        "Zoveel mogelijk leningen afsluiten bij de bank.",
        "Al je geld uitgeven aan secundaire behoeften.",
        "Alle belastingen ontwijken."
      ],
      "antwoord": 0,
      "uitleg": "Budgetteren zorgt voor inzicht en evenwicht tussen wat er binnenkomt en wat eruit gaat."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het NIBUD is een overheidsinstantie die zelf leningen verstrekt aan jongeren.",
      "antwoord": false,
      "uitleg": "Het NIBUD is een voorlichtingsinstituut dat budgetadvies geeft, maar leent zelf geen geld uit."
    },
    {
      "type": "mc",
      "vraag": "Een huishouden betaalt elk kwartaal € 180 aan water en heffingen. Hoeveel is dit per maand?",
      "opties": [
        "€ 45",
        "€ 90",
        "€ 120",
        "€ 60"
      ],
      "antwoord": 3,
      "uitleg": "Een kwartaal heeft 3 maanden. € 180 / 3 = € 60 per maand."
    },
    {
      "type": "invoer",
      "vraag": "Welk financieel overzicht toont alle verwachte inkomsten en uitgaven voor een toekomstige periode?",
      "antwoord": "begroting|budgetplan",
      "uitleg": "Een begroting geeft een overzicht van toekomstige verwachte geldstromen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je uitgaven hoger zijn dan je inkomsten, heb je een begrotingstekort.",
      "antwoord": true,
      "uitleg": "Een tekort betekent dat de uitgaven de inkomsten overstijgen."
    }
  ]
});
