/* =========================================================
   Duru's Scheikunde (HAVO 3) — Atoombouw & Atoommodellen
   ========================================================= */
DURU.register({
  "id": "sch-h2-4-atoombouw",
  "hoofdstuk": 2,
  "paragraaf": "2.4",
  "titel": "Atoombouw & Atoommodellen",
  "korteUitleg": "Protonen, neutronen, elektronen, atoomnummer, massagetal, isotopen en atoommodellen van Dalton tot Bohr.",
  "icoon": "⚛️",
  "kleur": "h2-thema",
  "theorie": "<h3>2.4 Atoombouw & Historische Atoommodellen</h3>\n<p>Atomen zijn de microscopische bouwstenen van alle materie. Een atoom is zelf weer opgebouwd uit drie fundamentele subatomaire deeltjes:</p>\n<ol>\n  <li><b>Protonen (p⁺):</b> Positief geladen deeltjes in de atoomkern met een massa van 1 u. Het aantal protonen bepaalt welk chemisch element het is en vormt het <b>atoomnummer</b>.</li>\n  <li><b>Neutronen (n⁰):</b> Neutrale deeltjes (lading 0) in de atoomkern met een massa van 1 u. Ze zorgen voor kernkracht en stabiliteit tussen de positieve protonen.</li>\n  <li><b>Elektronen (e⁻):</b> Negatief geladen deeltjes met een verwaarloosbare massa (0,00055 u) die met hoge snelheid in banen (elektronenschalen) rondom de kern bewegen.</li>\n</ol>\n<p>In een neutraal atoom is het aantal protonen in de kern altijd exact gelijk aan het aantal elektronen in de elektronenwolk (totale lading = 0).</p>\n<h4>Atoomnummer, Massagetal en Isotopen</h4>\n<div class=\"formule-box\">\n  • <b>Atoomnummer (Z):</b> Aantal protonen = Aantal elektronen in een neutraal atoom.<br>\n  • <b>Massagetal (A):</b> Aantal protonen + Aantal neutronen in de kern.<br>\n  • <b>Aantal neutronen:</b> <code>Massagetal (A) - Atoomnummer (Z)</code><br>\n  • <b>Isotopen:</b> Atomen van <i>hetzelfde element</i> (dus hetzelfde aantal protonen/atoomnummer), maar met een <i>verschillend aantal neutronen</i> (en dus een ander massagetal, zoals Koolstof-12 en Koolstof-14).\n</div>\n<h4>Ontwikkeling van historische atoommodellen</h4>\n<ul>\n  <li><b>John Dalton (1803):</b> Stelde het atoom voor als een massief, ondeelbaar hard massief kogeltje.</li>\n  <li><b>J.J. Thomson (1897):</b> Ontdekte het negatieve elektron en bedacht het 'krentenbolmodel': een positieve bol waarin losse elektronen als krenten zitten ingebed.</li>\n  <li><b>Ernest Rutherford (1911):</b> Schoot alfadeeltjes op goudfolie en ontdekte dat het atoom grotendeels leeg is, met een extreem kleine, zware positieve kern in het centrum.</li>\n  <li><b>Niels Bohr (1913):</b> Verfijnde het model: elektronen bewegen in vaste schillen (K, L, M, N...) op specifieke afstanden rondom de kern.</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een atoom heeft atoomnummer 6 en massagetal 14. Hoeveel neutronen bevat de kern?",
      "opties": [
        "8 neutronen",
        "14 neutronen",
        "6 neutronen",
        "20 neutronen"
      ],
      "antwoord": 0,
      "uitleg": "Aantal neutronen = Massagetal (14) - Atoomnummer (6) = 8 neutronen."
    },
    {
      "type": "mc",
      "vraag": "Wie toonde met het beroemde goudfolie-experiment aan dat een atoom grotendeels leeg is met een zware positieve kern?",
      "opties": [
        "John Dalton",
        "Ernest Rutherford",
        "J.J. Thomson",
        "Niels Bohr"
      ],
      "antwoord": 1,
      "uitleg": "Rutherford ontdekte de atoomkern door alfadeeltjes op goudfolie te schieten."
    },
    {
      "type": "waaronwaar",
      "vraag": "Isotopen van een element hebben hetzelfde aantal neutronen, maar een verschillend aantal protonen.",
      "antwoord": false,
      "uitleg": "Onwaar: isotopen hebben altijd hetzelfde aantal protonen (hetzelfde atoomnummer), maar een verschillend aantal neutronen."
    },
    {
      "type": "invoer",
      "vraag": "Welke elektrische lading heeft een neutron in de atoomkern?",
      "antwoord": "0|neutraal|geen lading|geen",
      "uitleg": "Een neutron is elektrisch neutraal (lading 0)."
    },
    {
      "type": "mc",
      "vraag": "Wat bevindt zich in de schillen van het atoommodel van Bohr?",
      "opties": [
        "Protonen",
        "Neutronen",
        "Elektronen",
        "Alfadeeltjes"
      ],
      "antwoord": 2,
      "uitleg": "Elektronen draaien in schillen rond de positieve kern."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een elektrisch neutraal atoom is het aantal protonen gelijk aan het aantal elektronen.",
      "antwoord": true,
      "uitleg": "Waar: de positieve lading van de protonen heft de negatieve lading van de elektronen precies op."
    },
    {
      "type": "invoer",
      "vraag": "Welk deeltje in de atoomkern bepaalt het atoomnummer en daarmee de identiteit van het element?",
      "antwoord": "proton|protonen",
      "uitleg": "Het aantal protonen bepaalt welk element het is."
    },
    {
      "type": "waaronwaar",
      "vraag": "De massa van een elektron is vrijwel gelijk aan de massa van een proton.",
      "antwoord": false,
      "uitleg": "Onwaar: een elektron is bijna 2000 keer lichter dan een proton en heeft een verwaarloosbare massa."
    }
  ]
});
