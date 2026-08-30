/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 4.3: Omzet, winst en btw
   ========================================================= */
DURU.register({
  "id": "h4-3",
  "hoofdstuk": 4,
  "paragraaf": "4.3",
  "titel": "Omzet, winst en btw",
  "korteUitleg": "Omzet (TO), inkoopwaarde, brutowinst, nettowinst, break-even en btw-berekeningen.",
  "icoon": "💶",
  "kleur": "roze",
  "theorie": "<h3>4.3 Omzet, winst en btw</h3>\n<p>Voor elke commerciële onderneming is inzicht in de omzet, kosten, belastingen en uiteindelijke winst van levensbelang.</p>\n<h4>Omzet, brutowinst en nettowinst</h4>\n<ul>\n  <li><b>Afzet (q):</b> Het aantal fysiek verkochte stuks producten (bijvoorbeeld 500 paar schoenen).</li>\n  <li><b>Omzet (Totale Opbrengst / TO):</b> De totale geldopbrengst van alle verkopen exclusief btw.<br>\n  <code>Omzet (TO) = Verkoopprijs per stuk (p) × Afzet (q)</code></li>\n  <li><b>Brutowinst:</b> De omzet verminderd met wat de ondernemer zelf heeft betaald om de goederen in te kopen.<br>\n  <code>Brutowinst = Omzet - Inkoopwaarde van de omzet</code></li>\n  <li><b>Nettowinst:</b> De werkelijke winst die overblijft nadat alle overige bedrijfskosten (personeelssalarissen, huur, energie, reclame) van de brutowinst zijn afgetrokken.<br>\n  <code>Nettowinst = Brutowinst - Bedrijfskosten</code> of <code>Totale winst = Totale Opbrengst (TO) - Totale Kosten (TK)</code></li>\n  <li><b>Break-evenpunt (BEP):</b> De omzet of afzet waarbij de totale opbrengst precies gelijk is aan de totale kosten (TO = TK). Het bedrijf speelt quitte en de winst is exact € 0.</li>\n</ul>\n<h4>Btw (Belasting over de Toegevoegde Waarde)</h4>\n<p>Ondernemers zijn wettelijk verplicht btw (omzetbelasting) in rekening te brengen aan consumenten en af te dragen aan de Belastingdienst:</p>\n<ul>\n  <li><b>Laag tarief (9%):</b> Primaire eerste levensbehoeften zoals voedingsmiddelen, drinkwater, boeken, kappersdiensten en openbaar vervoer.</li>\n  <li><b>Hoog tarief (21%):</b> Het algemene tarief voor alle overige goederen en luxe diensten (elektronica, meubels, kleding, auto's).</li>\n</ul>\n<div class=\"formule-box\">\n  <b>Omrekenregels voor btw:</b><br>\n  • Consumentenprijs (inclusief 21% btw) = <code>Verkoopprijs excl. btw × 1,21</code><br>\n  • Verkoopprijs (exclusief 21% btw) = <code>Consumentenprijs incl. btw / 1,21</code><br>\n  • Btw-bedrag = <code>Consumentenprijs incl. btw - Verkoopprijs excl. btw</code>\n</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een winkelier verkoopt 500 paar schoenen voor € 80 per stuk (excl. btw). Wat is de omzet?",
      "opties": [
        "€ 4.000",
        "€ 48.400",
        "€ 40.000",
        "€ 50.000"
      ],
      "antwoord": 2,
      "uitleg": "Omzet = Prijs × Afzet = 80 × 500 = € 40.000."
    },
    {
      "type": "waaronwaar",
      "vraag": "Op het break-evenpunt (BEP) maakt een onderneming maximale winst.",
      "antwoord": false,
      "uitleg": "Op het break-evenpunt zijn de opbrengsten gelijk aan de kosten en is de winst precies € 0."
    },
    {
      "type": "invoer",
      "vraag": "Wat is het hoge btw-tarief in Nederland (in procenten)?",
      "antwoord": "21|21%",
      "uitleg": "Het algemene hoge btw-tarief in Nederland is 21%."
    },
    {
      "type": "mc",
      "vraag": "Een jas kost € 100 exclusief 21% btw. Wat betaalt de consument in de winkel (inclusief btw)?",
      "opties": [
        "€ 100",
        "€ 109",
        "€ 125",
        "€ 121"
      ],
      "antwoord": 3,
      "uitleg": "100 × 1,21 = € 121 consumentenprijs incl. btw."
    },
    {
      "type": "waaronwaar",
      "vraag": "Nettowinst is gelijk aan de brutowinst verminderd met de overige bedrijfskosten.",
      "antwoord": true,
      "uitleg": "Nettowinst = Brutowinst - Bedrijfskosten (personeel, huur, energie)."
    },
    {
      "type": "mc",
      "vraag": "Welk product valt in Nederland onder het lage btw-tarief van 9%?",
      "opties": [
        "Een smartphone",
        "Een paar sportschoenen",
        "Vers volkorenbrood",
        "Een bioscoopticket voor een 3D-film"
      ],
      "antwoord": 2,
      "uitleg": "Levensmiddelen en eerste levensbehoeften zoals brood vallen onder het lage 9% btw-tarief."
    },
    {
      "type": "invoer",
      "vraag": "Hoe noem je het aantal stuks producten dat een onderneming daadwerkelijk verkoopt?",
      "antwoord": "afzet",
      "uitleg": "Afzet is de fysieke hoeveelheid verkochte eenheden (terwijl omzet het geldbedrag is)."
    },
    {
      "type": "waaronwaar",
      "vraag": "De btw die een winkelier ontvangt van klanten mag de winkelier als eigen winst houden.",
      "antwoord": false,
      "uitleg": "De winkelier moet de ontvangen btw direct afdragen aan de Belastingdienst."
    }
  ]
});
