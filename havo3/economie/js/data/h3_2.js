/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 3.2: Lenen
   ========================================================= */
DURU.register({
  "id": "h3-2",
  "hoofdstuk": 3,
  "paragraaf": "3.2",
  "titel": "Lenen",
  "korteUitleg": "Leenvormen, kredietkosten, hypotheeklening, BKR en de gevaren van schulden.",
  "icoon": "🏦",
  "kleur": "groen",
  "theorie": "<h3>3.2 Lenen</h3>\n<p><b>Lenen (krediet opnemen)</b> is het tijdelijk gebruikmaken van geld van iemand anders (meestal een bank of financieringsmaatschappij). Bij lenen haal je toekomstige consumptie naar het heden: je koopt het product nu, maar betaalt het in de toekomst terug met rente.</p>\n<h4>Verschillende kredietvormen</h4>\n<ul>\n  <li><b>Persoonlijke lening:</b> Je leent in één keer een vast geldbedrag voor een specifiek doel (zoals een auto of verbouwing). Je lost dit maandelijks in vaste termijnen (aflossing + rente) af binnen een afgesproken looptijd.</li>\n  <li><b>Doorlopend krediet:</b> Je spreekt met de bank een maximale kredietlimiet af. Binnen die limiet mag je flexibel geld opnemen en aflossen. Je betaalt alleen rente over het daadwerkelijk opgenomen bedrag.</li>\n  <li><b>Hypothecaire lening (hypotheek):</b> Een zeer grote, langlopende lening (meestal 30 jaar) voor de aankoop van een woning of bedrijfspand. Het onroerend goed dient hierbij als <b>onderpand</b> voor de bank: betaal je niet, dan mag de bank de woning verkopen.</li>\n  <li><b>Kopen op afbetaling & huurkoop:</b> Je betaalt een aankoop in termijnen. Bij koop op afbetaling ben je direct eigenaar; bij <b>huurkoop</b> word je pas juridisch eigenaar zodra de allerlaatste termijn volledig is betaald.</li>\n  <li><b>Rood staan:</b> Een negatief saldo op je betaalrekening. Dit is een van de allerduurste leenvormen met rentetarieven tot wel 14%.</li>\n</ul>\n<div class=\"formule-box\">\n  <b>Kredietkosten berekenen:</b><br>\n  <code>Totale kredietkosten = (Aantal termijnen × Termijnbedrag) - Oorspronkelijk geleend bedrag</code><br>\n  De kredietkosten bestaan volledig uit de <b>rente</b> en de administratiekosten die de bank extra in rekening brengt.\n</div>\n<p>Het <b>BKR (Bureau Krediet Registratie)</b> in Tiel registreert alle leningen vanaf € 250 die langer dan een maand lopen. Banken zijn verplicht het BKR te raadplegen om te voorkomen dat consumenten onverantwoorde schulden aangaan (overkreditering).</p>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Duru koopt een scooter van € 1.500 op afbetaling. Ze betaalt 12 maanden lang € 140 per maand. Hoeveel bedragen de totale kredietkosten?",
      "opties": [
        "€ 140",
        "€ 1.680",
        "€ 180",
        "€ 1.500"
      ],
      "antwoord": 2,
      "uitleg": "Totaal betaald = 12 × 140 = € 1.680. Kredietkosten = 1.680 - 1.500 = € 180."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een hypothecaire lening dient de gekochte woning als onderpand voor de bank.",
      "antwoord": true,
      "uitleg": "Als de lener niet meer betaalt, mag de bank de woning verkopen om de schuld te innen (onderpand)."
    },
    {
      "type": "invoer",
      "vraag": "Welke instantie in Tiel registreert in Nederland leningen om problematische schulden te voorkomen?",
      "antwoord": "BKR|Bureau Krediet Registratie",
      "uitleg": "Het BKR registreert kredieten om te voorkomen dat consumenten te veel lenen."
    },
    {
      "type": "mc",
      "vraag": "Wat is het verschil tussen koop op afbetaling en huurkoop?",
      "opties": [
        "Bij koop op afbetaling ben je direct eigenaar; bij huurkoop pas na de laatste termijn.",
        "Bij koop op afbetaling betaal je geen rente.",
        "Huurkoop geldt alleen voor huizen.",
        "Koop op afbetaling is wettelijk verboden."
      ],
      "antwoord": 0,
      "uitleg": "Bij huurkoop gaat het eigendom pas over op de koper zodra de allerlaatste termijn volledig is voldaan."
    },
    {
      "type": "waaronwaar",
      "vraag": "Rood staan op je betaalrekening is doorgaans de goedkoopste manier om geld te lenen.",
      "antwoord": false,
      "uitleg": "Rood staan kent juist een van de allerhoogste rentepercentages (vaak 10-14%)."
    },
    {
      "type": "mc",
      "vraag": "Wat omvat het maandelijkse termijnbedrag van een persoonlijke lening?",
      "opties": [
        "Alleen de winst van de bank",
        "Alleen de wettelijke btw",
        "Aflossing (terugbetaling van de schuld) plus rente",
        "Uitsluitend de premie van de opstalverzekering"
      ],
      "antwoord": 2,
      "uitleg": "Een termijn bestaat uit aflossing (verlaging van de schuld) en kredietvergoeding (rente)."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je het terugbetalen van het daadwerkelijk geleende bedrag (zonder de rente)?",
      "antwoord": "aflossen|aflossing",
      "uitleg": "Aflossen is het verminderen van de openstaande hoofdsom van een schuld."
    },
    {
      "type": "waaronwaar",
      "vraag": "Geld lenen kost altijd geld door de verschuldigde rente.",
      "antwoord": true,
      "uitleg": "De bekende waarschuwing luidt: 'Let op! Geld lenen kost geld' vanwege de kredietkosten."
    }
  ]
});
