/* =========================================================
   Duru's Wiskunde (HAVO 3) — Steel-bladdiagrammen & Spreidingsmaten
   ========================================================= */
DURU.register({
  "id": "h2-5-steelbladdiagram",
  "hoofdstuk": 2,
  "paragraaf": "2.5",
  "titel": "Steel-bladdiagrammen & Spreidingsmaten",
  "korteUitleg": "Steel-bladdiagram aflezen, minimum, maximum, spreidingsbreedte en kwartielen.",
  "icoon": "🌳",
  "kleur": "blauw",
  "theorie": "<h3>2.5 Steel-bladdiagrammen & Spreidingsmaten</h3>\n<p>Een <b>steel-bladdiagram (stem-and-leaf plot)</b> is een compacte en overzichtelijke manier om getallen te ordenen zonder de oorspronkelijke exacte waarden te verliezen.</p>\n<h4>Hoe lees je een steel-bladdiagram?</h4>\n<ul>\n  <li><b>De steel (stam):</b> Bevat de tientallen (of honderdtallen/gehele getallen).</li>\n  <li><b>Het blad:</b> Bevat de eenheden (de laatste cijfers). De cijfers in het blad staan altijd <b>op volgorde van klein naar groot</b>.</li>\n  <li><b>Legenda (sleutel):</b> Geeft aan hoe je de getallen moet interpreteren. Bijvoorbeeld: <code>3 | 5 betekent 35</code> of <code>5 | 2 betekent 5,2</code>.</li>\n</ul>\n<h4>Spreidingsmaten: Hoe ver liggen de getallen uit elkaar?</h4>\n<p>Naast het centrum is het belangrijk om te weten hoe verspreid de data liggen:</p>\n<div class=\"formule-box\">\n  • <b>Minimum (Min):</b> De allerlaagste waarnemingswaarde.<br>\n  • <b>Maximum (Max):</b> De allerhoogste waarnemingswaarde.<br>\n  • <b>Spreidingsbreedte (Range):</b> <code>Spreidingsbreedte = Maximum - Minimum</code><br>\n  • <b>Kwartielen:</b> Verdelen de geordende data in 4 gelijke kwarten van 25%:<br>\n    - <b>Eerste kwartiel ($Q_1$):</b> De mediaan van de eerste (linker) helft van de data.<br>\n    - <b>Tweede kwartiel ($Q_2$):</b> De algehele mediaan (50%).<br>\n    - <b>Derde kwartiel ($Q_3$):</b> De mediaan van de tweede (rechter) helft van de data.<br>\n    - <b>Kwartielafstand:</b> <code>Kwartielafstand = Q₃ - Q₁</code>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram staat steel 4 met bladeren 2, 5, 8 (legenda 4 | 2 = 42). Welke getallen stelt dit voor?",
      "opties": [
        "42, 45, 48",
        "4, 2, 5, 8",
        "24, 54, 84",
        "4258"
      ],
      "antwoord": 0,
      "uitleg": "Steel 4 combineert met de bladeren 2, 5 en 8 tot de getallen 42, 45 en 48."
    },
    {
      "type": "mc",
      "vraag": "De hoogste toetsscore in een klas is 9,4 en de laagste is 3,8. Wat is de spreidingsbreedte?",
      "opties": [
        "5,4",
        "5,6",
        "6,2",
        "6,6"
      ],
      "antwoord": 1,
      "uitleg": "Spreidingsbreedte = Maximum (9,4) - Minimum (3,8) = 5,6."
    },
    {
      "type": "waaronwaar",
      "vraag": "De bladeren in een steel-bladdiagram moeten altijd van klein naar groot worden gerangschikt.",
      "antwoord": true,
      "uitleg": "Waar: een correct steel-bladdiagram ordent de bladeren oplopend."
    },
    {
      "type": "invoer",
      "vraag": "Als Q3 = 82 en Q1 = 54, wat is dan de kwartielafstand?",
      "antwoord": "28",
      "uitleg": "Kwartielafstand = Q3 - Q1 = 82 - 54 = 28."
    },
    {
      "type": "mc",
      "vraag": "Welk percentage van de waarnemingen ligt tussen het eerste kwartiel (Q1) en het derde kwartiel (Q3)?",
      "opties": [
        "25%",
        "75%",
        "50%",
        "100%"
      ],
      "antwoord": 2,
      "uitleg": "Tussen Q1 (25%) en Q3 (75%) bevindt zich precies de middelste 50% van de data."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een steel-bladdiagram gaan de oorspronkelijke exacte waarden van de getallen verloren.",
      "antwoord": false,
      "uitleg": "Niet waar: in tegenstelling tot een histogram kun je in een steel-bladdiagram elk individueel getal exact teruglezen."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet het verschil tussen de hoogste en de laagste score in een dataset?",
      "antwoord": "spreidingsbreedte|range",
      "uitleg": "Spreidingsbreedte = Max - Min."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het tweede kwartiel (Q2) is precies gelijk aan de mediaan van de hele dataset.",
      "antwoord": true,
      "uitleg": "Waar: Q2 en de mediaan delen de dataset beide precies in twee helften van 50%."
    }
  ]
});
