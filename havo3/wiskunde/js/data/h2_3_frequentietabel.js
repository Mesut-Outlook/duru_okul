/* =========================================================
   Duru's Wiskunde (HAVO 3) — Frequentietabellen & Relatieve Frequentie
   ========================================================= */
DURU.register({
  "id": "h2-3-frequentietabel",
  "hoofdstuk": 2,
  "paragraaf": "2.3",
  "titel": "Frequentietabellen & Relatieve Frequentie",
  "korteUitleg": "Absolute frequentie, relatieve frequentie in procenten, turven en klassenindeling.",
  "icoon": "📋",
  "kleur": "blauw",
  "theorie": "<h3>2.3 Frequentietabellen & Relatieve Frequentie</h3>\n<p>Wanneer je een statistisch onderzoek uitvoert en veel data verzamelt, krijg je een lange lijst met losse getallen (de ruwe data). Om hier structuur en overzicht in aan te brengen, orden je de gegevens in een <b>frequentietabel</b>.</p>\n<h4>Verschillende soorten frequenties</h4>\n<ul>\n  <li><b>Absolute frequentie:</b> Het werkelijke aantal keren dat een bepaalde waarneming of score voorkomt (bijvoorbeeld: 7 leerlingen hadden een 8 voor de toets).</li>\n  <li><b>Relatieve frequentie (percentage):</b> Het aandeel van een waarneming ten opzichte van het totale aantal waarnemingen, meestal uitgedrukt in een percentage:\n  <div class=\"formule-box\">\n    <code>Relatieve frequentie = (Absolute frequentie / Totaal aantal waarnemingen) × 100%</code>\n  </div>\n  </li>\n  <li><b>Cumulatieve frequentie:</b> De opgetelde frequentie vanaf de laagste score tot en met de huidige score (de 'lopende som').</li>\n</ul>\n<h4>Klassenindeling bij grote datasets</h4>\n<p>Wanneer de data veel verschillende waarden bevat (zoals de lengtes van 200 scholieren tussen 140 cm en 195 cm), groepeer je de waarden in <b>klassen</b> (bijvoorbeeld <code>140 - < 150</code>, <code>150 - < 160</code>, etc.):</p>\n<ul>\n  <li><b>Klassenbreedte:</b> Het verschil tussen de bovengrens en de ondergrens van een klasse (bijvoorbeeld: 150 - 140 = 10 cm breed).</li>\n  <li><b>Klassenmidden:</b> Het exacte gemiddelde van de ondergrens en de bovengrens: <code>(140 + 150) / 2 = 145 cm</code>. Het klassenmidden gebruik je om het gemiddelde van de gegroepeerde data te schatten.</li>\n</ul>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "In een groep van 50 sporters spelen 15 sporters basketbal. Wat is de relatieve frequentie van basketballers?",
      "opties": [
        "30%",
        "25%",
        "15%",
        "35%"
      ],
      "antwoord": 0,
      "uitleg": "(15 / 50) × 100% = 30%."
    },
    {
      "type": "mc",
      "vraag": "Wat is het klassenmidden van de klasse 20 - < 30?",
      "opties": [
        "20",
        "25",
        "24",
        "30"
      ],
      "antwoord": 1,
      "uitleg": "(20 + 30) / 2 = 25."
    },
    {
      "type": "waaronwaar",
      "vraag": "De absolute frequentie is altijd een percentage tussen 0% en 100%.",
      "antwoord": false,
      "uitleg": "Niet waar: de absolute frequentie is het werkelijke aantal (een geheel getal), terwijl de relatieve frequentie een percentage is."
    },
    {
      "type": "invoer",
      "vraag": "Als in een klas van 25 leerlingen er 5 een onvoldoende hebben, wat is dan de relatieve frequentie in procenten?",
      "antwoord": "20|20%|20 procent",
      "uitleg": "(5 / 25) × 100% = 20%."
    },
    {
      "type": "mc",
      "vraag": "Wat is de klassenbreedte van de klasse 150 - < 175?",
      "opties": [
        "15",
        "20",
        "25",
        "162,5"
      ],
      "antwoord": 2,
      "uitleg": "Klassenbreedte = 175 - 150 = 25."
    },
    {
      "type": "waaronwaar",
      "vraag": "De som van alle relatieve frequenties in een complete frequentietabel is altijd gelijk aan 100%.",
      "antwoord": true,
      "uitleg": "Waar: alle delen samen vormen het volledige geheel (100%)."
    },
    {
      "type": "invoer",
      "vraag": "Hoe heet de frequentie waarbij de opeenvolgende aantallen bij elkaar worden opgeteld?",
      "antwoord": "cumulatieve frequentie|cumulatief",
      "uitleg": "De cumulatieve frequentie telt de waarnemingen door."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij de notatie 10 - < 20 telt de waarde 20 zelf ook mee in die klasse.",
      "antwoord": false,
      "uitleg": "Niet waar: het teken '<' betekent 'tot maar niet met'. De waarde 20 hoort in de volgende klasse (20 - < 30)."
    }
  ]
});
