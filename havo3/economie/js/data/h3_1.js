/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 3.1: Sparen
   ========================================================= */
DURU.register({
  "id": "h3-1",
  "hoofdstuk": 3,
  "paragraaf": "3.1",
  "titel": "Sparen",
  "korteUitleg": "Spaarredenen, spaarvormen, enkelvoudige en samengestelde rente (rente-op-rente).",
  "icoon": "🐖",
  "kleur": "groen",
  "theorie": "<h3>3.1 Sparen</h3>\n<p><b>Sparen</b> is het niet uitgeven van een deel van je beschikbare inkomen. In economische termen stel je huidige consumptie uit naar een later moment in de toekomst.</p>\n<h4>Drie klassieke spaarmotieven</h4>\n<ol>\n  <li><b>Sparen voor een doel:</b> Je spaart doelgericht voor een specifieke, geplande grote aankoop in de toekomst (bijvoorbeeld een rijbewijs, een scooter, een vakantiereis of een eigen laptop).</li>\n  <li><b>Sparen uit voorzorg:</b> Je spaart geld als financiële buffer om onverwachte tegenslagen en plotselinge reparaties op te vangen (bijvoorbeeld een kapotte wasmachine of een onvoorziene rekening van de tandarts).</li>\n  <li><b>Sparen voor het rendement:</b> Je spaart puur om extra inkomsten te verdienen dankzij de rentevergoeding die de bank over je spaargeld uitkeert.</li>\n</ol>\n<h4>Rente en samengestelde rente berekenen</h4>\n<p><b>Rente (spaarloon):</b> De vergoeding in geld die de bank jou betaalt omdat zij jouw spaartegoeden tijdelijk mag gebruiken om uit te lenen aan anderen.</p>\n<div class=\"formule-box\">\n  <b>Enkelvoudige renteformule:</b><br>\n  <code>Rente = (Spaargeld × Rentepercentage × Aantal maanden) / (100 × 12)</code><br><br>\n  <b>Samengestelde rente (rente-op-rente):</b><br>\n  Wanneer je de ontvangen rente aan het eind van het jaar op de spaarrekening laat staan, ontvang je het volgende jaar ook rente over die eerder bijgeschreven rente. Hierdoor groeit je spaarsaldo exponentieel sneller!\n</div>\n<h4>Verschillende spaarvormen en veiligheid</h4>\n<ul>\n  <li><b>Vrij opneembare spaarrekening:</b> Je kunt op elk gewenst moment zonder kosten geld storten of opnemen. De rente is meestal variabel.</li>\n  <li><b>Spaardeposito:</b> Je zet je geld voor een vooraf afgesproken termijn (bijvoorbeeld 2 of 5 jaar) vast tegen een vaste rente. Tussentijds opnemen kost vaak een boeterente.</li>\n  <li><b>Depositogarantiestelsel:</b> In Nederland en de EU beschermt De Nederlandsche Bank spaartegoeden tot maximaal € 100.000 per persoon per bankvergunning mocht een bank failliet gaan.</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Duru zet € 2.000 op een spaarrekening tegen 3% rente per jaar. Hoeveel rente ontvangt zij na 1 jaar?",
      "opties": [
        "€ 30",
        "€ 90",
        "€ 60",
        "€ 120"
      ],
      "antwoord": 2,
      "uitleg": "(2.000 × 3) / 100 = € 60 rente per jaar."
    },
    {
      "type": "waaronwaar",
      "vraag": "Geld opzij zetten voor het geval je laptop plotseling stukgaat, is sparen voor een doel.",
      "antwoord": false,
      "uitleg": "Dat is sparen uit voorzorg (voor onverwachte uitgaven). Sparen voor een doel is gericht op een geplande aankoop."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet het fenomeen waarbij je in het tweede jaar ook rente ontvangt over de eerder bijgeschreven rente?",
      "antwoord": "samengestelde rente|rente op rente",
      "uitleg": "Samengestelde rente betekent dat rente wordt toegevoegd aan het kapitaal en weer mee-rendeert."
    },
    {
      "type": "mc",
      "vraag": "Tot welk bedrag per persoon per bank garandeert de overheid spaartegoeden bij een bankfaillissement?",
      "opties": [
        "€ 20.000",
        "€ 100.000",
        "€ 50.000",
        "Onbeperkt"
      ],
      "antwoord": 1,
      "uitleg": "Het depositogarantiestelsel dekt in de EU spaargeld tot maximaal € 100.000 per persoon per bankvergunning."
    },
    {
      "type": "waaronwaar",
      "vraag": "Sparen is het uitstellen van consumptie naar een later moment.",
      "antwoord": true,
      "uitleg": "Door nu niet te consumeren houd je geld beschikbaar voor toekomstige behoeften."
    },
    {
      "type": "mc",
      "vraag": "Wat is een spaardeposito?",
      "opties": [
        "Een spaarrekening waarop je geld voor een vaste tijd vastzet tegen een vooraf afgesproken rente.",
        "Een rekening waarmee je direct kunt pinnen in winkels.",
        "Een lening bij de bank met variabele rente.",
        "Een creditcard met automatische incasso."
      ],
      "antwoord": 0,
      "uitleg": "Bij een deposito staat het geld voor een afgesproken periode vast tegen een vaste rente."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je de financiële vergoeding die de bank betaalt voor het stallen van je spaargeld?",
      "antwoord": "rente|spaarloon",
      "uitleg": "Rente is de prijs voor het uitlenen of beschikbaar stellen van geld."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een variabele rente blijft het rentepercentage gedurende 10 jaar gegarandeerd ongewijzigd.",
      "antwoord": false,
      "uitleg": "Variabele rente kan op ieder moment door de bank worden verhoogd of verlaagd."
    }
  ]
});
