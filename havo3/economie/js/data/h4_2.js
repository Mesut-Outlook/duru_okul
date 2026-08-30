/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 4.2: Kosten van een onderneming
   ========================================================= */
DURU.register({
  "id": "h4-2",
  "hoofdstuk": 4,
  "paragraaf": "4.2",
  "titel": "Kosten van een onderneming",
  "korteUitleg": "Constante kosten, variabele kosten, totale kosten en kostprijs per product.",
  "icoon": "📉",
  "kleur": "roze",
  "theorie": "<h3>4.2 Kosten van een onderneming</h3>\n<p>Om goederen te produceren en diensten te leveren, maakt elke onderneming kosten. Binnen de bedrijfseconomie verdelen we deze kosten in constante en variabele kosten.</p>\n<h4>Vaste (constante) versus variabele kosten</h4>\n<ul>\n  <li><b>Constante kosten (TCK / Vaste kosten):</b> Kosten die op de korte termijn <b>niet veranderen</b> wanneer er meer of minder producten worden gefabriceerd (bijvoorbeeld de maandelijkse huur van de fabriekshal, de vaste afschrijving van machines, accountantskosten en vaste internetabonnementen). Zelfs als de fabriek tijdelijk stilstaat (productie = 0), lopen deze kosten volledig door.</li>\n  <li><b>Variabele kosten (TVK):</b> Kosten die <b>rechtstreeks meegroeien of dalen</b> met de omvang van de productie (bijvoorbeeld grondstoffen, halffabricaten, verpakkingsdozen, elektriciteit voor productiemachines en transportkosten).</li>\n</ul>\n<div class=\"formule-box\">\n  <b>Kostenformules van een bedrijf:</b><br>\n  • <code>Totale kosten (TK) = Totale constante kosten (TCK) + Totale variabele kosten (TVK)</code><br>\n  • <code>Totale variabele kosten (TVK) = Variabele kosten per stuk (GVK) × Aantal stuks (q)</code><br>\n  • <code>Kostprijs per stuk (GTK) = Totale kosten (TK) / Aantal stuks (q)</code>\n</div>\n<h4>Schaalvoordelen en massaproductie</h4>\n<p>Wanneer een onderneming haar productie sterk uitbreidt, worden de totale constante kosten verdeeld over een veel groter aantal producten. Hierdoor daalt het aandeel vaste kosten per eenheid en wordt de <b>kostprijs per stuk lager</b>. Dit noemen we <b>schaalvoordelen</b> (of economies of scale). Dit verklaart waarom grote fabrieken vaak veel goedkoper kunnen produceren dan kleine ambachtelijke werkplaatsen.</p>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een bakkerij heeft € 4.000 constante kosten per maand. De variabele kosten zijn € 1 per brood. Bij een productie van 2.000 broden bedragen de totale kosten:",
      "opties": [
        "€ 2.000",
        "€ 4.000",
        "€ 6.000",
        "€ 8.000"
      ],
      "antwoord": 2,
      "uitleg": "TK = TCK (€ 4.000) + TVK (2.000 × € 1 = € 2.000) = € 6.000."
    },
    {
      "type": "waaronwaar",
      "vraag": "De huur van een fabrieksgebouw stijgt automatisch als de fabriek deze maand twee keer zoveel produceert.",
      "antwoord": false,
      "uitleg": "De huur is een constante (vaste) last en blijft gelijk, ongeacht hoeveel er geproduceerd wordt."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je de kosten die rechtstreeks meegroeien als de productieomvang toeneemt?",
      "antwoord": "variabele kosten|variabel",
      "uitleg": "Variabele kosten zijn afhankelijk van de geproduceerde hoeveelheid (output)."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met de kostprijs per product als de vaste kosten over veel meer producten worden verdeeld?",
      "opties": [
        "De kostprijs per product stijgt.",
        "De kostprijs per product daalt.",
        "De kostprijs per product blijft exact gelijk.",
        "De omzet wordt nul."
      ],
      "antwoord": 1,
      "uitleg": "Door schaalvoordelen daalt het aandeel vaste kosten per stuk, waardoor de kostprijs daalt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Verpakkingsmateriaal en grondstoffen zijn typische voorbeelden van variabele kosten.",
      "antwoord": true,
      "uitleg": "Hoe meer producten je maakt, hoe meer verpakkingen en grondstoffen je verbruikt."
    },
    {
      "type": "mc",
      "vraag": "Een timmerman heeft € 10.000 totale kosten voor het maken van 50 eettafels. Wat is de kostprijs per tafel?",
      "opties": [
        "€ 100",
        "€ 200",
        "€ 500",
        "€ 1.000"
      ],
      "antwoord": 1,
      "uitleg": "Kostprijs per product = € 10.000 / 50 = € 200 per tafel."
    },
    {
      "type": "invoer",
      "vraag": "Welke term gebruikt de economie voor kosten die gelijk blijven bij verandering van de productie?",
      "antwoord": "constante kosten|vaste kosten",
      "uitleg": "Constante kosten (vaste kosten) veranderen niet met het productievolume."
    },
    {
      "type": "waaronwaar",
      "vraag": "Totale kosten zijn gelijk aan de constante kosten minus de variabele kosten.",
      "antwoord": false,
      "uitleg": "Totale kosten zijn de SOM van constante en variabele kosten (TK = TCK + TVK)."
    }
  ]
});
