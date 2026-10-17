/* =========================================================
   Duru's Economie (HAVO 3) — Onderwerp 4.3: Begrippen §4.3 Omzet en winst
   ========================================================= */
DURU.register({
  "id": "h4-3-begrippen",
  "hoofdstuk": 4,
  "paragraaf": "4.3",
  "titel": "Begrippen §4.3 Omzet en winst",
  "korteUitleg": "Alle begrippen van §4.3: omzet, afzet, kostprijs, winstmarge, btw, accijns, brutowinst en nettowinst.",
  "icoon": "🔑",
  "kleur": "roze",
  "theorie": "<h3>Begrippen &sect;4.3 Omzet en winst</h3>\n<p>Wanneer de opbrengsten van een onderneming hoger zijn dan de kosten, maakt het bedrijf winst. Dit zijn alle begrippen en formules van deze paragraaf.</p>\n<h4>Omzet</h4>\n<ul>\n<li><b>Omzet (TO, totale opbrengst):</b> hoeveel geld er in totaal is verdiend met de verkopen, exclusief btw.</li>\n<li><b>Afzet (Q, quantity):</b> de hoeveelheid producten die is verkocht.</li>\n<li><b>Verkoopprijs (P):</b> de prijs waarvoor een product wordt verkocht.</li>\n</ul>\n<div class=\"formule-box\"><b>Omzet</b> = verkoopprijs &times; afzet, dus TO = P &times; Q</div>\n<h4>Van kostprijs naar verkoopprijs</h4>\n<ul>\n<li><b>Kostprijs:</b> de prijs die het kost om &eacute;&eacute;n product te maken, met constante en variabele kosten.</li>\n<li><b>Winstmarge:</b> de winst die je bovenop de kostprijs zet, vaak als percentage van de kostprijs. De winst is meestal het inkomen van de eigenaar: een beloning voor de productiefactor ondernemerschap.</li>\n</ul>\n<div class=\"formule-box\">Kostprijs = vaste kosten &divide; aantal producten + variabele kosten per product<br>Verkoopprijs = kostprijs + winstmarge</div>\n<h4>Btw en accijns</h4>\n<ul>\n<li><b>Btw (belasting over de toegevoegde waarde):</b> wordt bij de verkoopprijs opgeteld; de winkel draagt de btw af aan de Belastingdienst. Daarom hoort btw niet bij de omzet.</li>\n<li><b>Tarieven:</b> hoog tarief 21%, laag tarief 9% (levensmiddelen, geneesmiddelen, kapper, schilder) en nultarief 0% (bijvoorbeeld zonnepanelen en onderwijs).</li>\n<li><b>Accijns:</b> belasting op producten waarvan de overheid het gebruik wil ontmoedigen, zoals tabak en alcohol; een vast bedrag of percentage per product.</li>\n</ul>\n<div class=\"formule-box\">Prijs inclusief btw = prijs exclusief btw &times; (1 + btw-tarief)<br>Prijs exclusief btw = prijs inclusief btw &divide; (1 + btw-tarief)</div>\n<h4>Winst</h4>\n<ul>\n<li><b>Inkoopwaarde van de omzet:</b> het bedrag waarvoor de ondernemer de verkochte producten zelf heeft ingekocht (inkoopprijs &times; aantal).</li>\n<li><b>Brutowinst:</b> omzet &minus; inkoopwaarde van de omzet.</li>\n<li><b>Bedrijfskosten:</b> bijvoorbeeld loonkosten, verkoopkosten, huisvestingskosten en afschrijvingskosten.</li>\n<li><b>Nettowinst:</b> brutowinst &minus; bedrijfskosten.</li>\n</ul>\n<div class=\"voorbeeld\"><div class=\"vb-kop\">Voorbeeld</div>Een bedrijf verkoopt 4.000 producten voor &euro; 12: omzet = &euro; 12 &times; 4.000 = &euro; 48.000.</div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Welk begrip past bij: ‘hoeveel geld er in totaal is verdiend met de verkopen’?",
      "opties": [
        "Afzet",
        "Omzet",
        "Kostprijs",
        "Winstmarge"
      ],
      "antwoord": 1,
      "uitleg": "De omzet (TO) = verkoopprijs × afzet."
    },
    {
      "type": "mc",
      "vraag": "Wat staat de Q voor in TO = P × Q?",
      "opties": [
        "De kostprijs",
        "De omzet",
        "De verkoopprijs",
        "De afzet (quantity)"
      ],
      "antwoord": 3,
      "uitleg": "Q is quantity: de afzet."
    },
    {
      "type": "mc",
      "vraag": "Welk begrip past bij: ‘omzet min inkoopwaarde van de omzet’?",
      "opties": [
        "Brutowinst",
        "Nettowinst",
        "Winstmarge",
        "Bedrijfskosten"
      ],
      "antwoord": 0,
      "uitleg": "Brutowinst = omzet − inkoopwaarde van de omzet."
    },
    {
      "type": "mc",
      "vraag": "Welk btw-tarief is het lage tarief?",
      "opties": [
        "0%",
        "12%",
        "9%",
        "21%"
      ],
      "antwoord": 2,
      "uitleg": "Hoog 21%, laag 9%, nul 0%."
    },
    {
      "type": "waaronwaar",
      "vraag": "De btw die een winkel van klanten ontvangt, hoort bij de omzet van de winkel.",
      "antwoord": false,
      "uitleg": "Onwaar. De winkel draagt de btw af aan de Belastingdienst, dus de omzet is exclusief btw."
    },
    {
      "type": "waaronwaar",
      "vraag": "Verkoopprijs = kostprijs + winstmarge.",
      "antwoord": true,
      "uitleg": "Waar. Zo bereken je de verkoopprijs."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet de belasting op tabak en alcohol die het gebruik moet ontmoedigen?",
      "antwoord": "accijns",
      "uitleg": "Accijns verhoogt de prijs van producten waarvan de overheid het gebruik wil ontmoedigen."
    },
    {
      "type": "invoer",
      "vraag": "Nettowinst = brutowinst min de ...?",
      "antwoord": "bedrijfskosten",
      "uitleg": "Nettowinst = brutowinst − bedrijfskosten."
    }
  ]
});
