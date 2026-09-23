/* =========================================================
   Duru's Scheikunde (HAVO 3) — Massaverhoudingen
   Hoofdstuk 3 — Paragraaf 3.3 (Chemie Overal)
   ========================================================= */
DURU.register({
  "id": "sch-h3-3-massaverhoudingen",
  "hoofdstuk": 3,
  "paragraaf": "3.3",
  "titel": "Massaverhoudingen",
  "korteUitleg": "Rekenen met de vaste massaverhouding waarin stoffen reageren, kruislings vermenigvuldigen en een massaverhouding afleiden uit metingen.",
  "icoon": "⚗️",
  "kleur": "h3-thema",
  "theorie": "<h3>3.3 Massaverhoudingen</h3><p>Stoffen reageren altijd in een <b>vaste massaverhouding</b> met elkaar. Neem bijvoorbeeld de reactie van ammoniak met waterstofchloride tot salmiak (ammoniumchloride): NH<sub>3</sub> (g) + HCl (g) → NH<sub>4</sub>Cl (s). Als je 17,0 gram ammoniak met 36,5 gram waterstofchloride bij elkaar brengt, reageren beide beginstoffen precies volledig — er blijft niets van over. De <b>massaverhouding</b> waarin ammoniak en waterstofchloride reageren, is dus 17,0 : 36,5. Deze verhouding staat vast voor élke hoeveelheid: breng je twee keer zoveel ammoniak (34,0 g) samen met twee keer zoveel waterstofchloride (73,0 g), dan reageert dat weer precies volledig, in dezelfde verhouding.</p><p>Met de wet van behoud van massa kun je ook meteen berekenen hoeveel reactieproduct er ontstaat: de massa van de reactieproducten is gelijk aan de totale massa van de beginstoffen. Bij 17,0 g ammoniak + 36,5 g waterstofchloride ontstaat er dus 17,0 + 36,5 = 53,5 g salmiak.</p><h4>Rekenen met kruislings vermenigvuldigen</h4><p>Ken je de massaverhouding, dan kun je bij een gegeven hoeveelheid van de ene stof berekenen hoeveel van de andere stof nodig is. Dat doe je met <b>kruislings vermenigvuldigen</b>: zet de bekende massaverhouding en de gegeven hoeveelheid onder elkaar in een tabelletje, en reken de onbekende (x) uit.</p><div class=\"voorbeeld\"><div class=\"vb-kop\">Rekenvoorbeeld — IJzer en zwavel</div><div class=\"stap\">IJzer en zwavel reageren tot ijzersulfide: Fe (s) + S (s) → FeS (s), in de massaverhouding Fe : S = 55,8 : 32,1.</div><div class=\"stap\">Vraag: hoeveel gram zwavel reageert volledig met 20,0 g ijzer?</div><table class=\"nask\"><tr><th></th><th>Fe</th><th>S</th></tr><tr><td>massaverhouding</td><td>55,8</td><td>32,1</td></tr><tr><td>hoeveelheid stof (g)</td><td>20,0</td><td>x</td></tr></table><div class=\"stap\">x = (20,0 × 32,1) / 55,8 = 642,0 / 55,8 = 11,5 g zwavel (1 decimaal).</div><div class=\"stap\">Met de wet van behoud van massa: er ontstaat 20,0 + 11,5 = 31,5 g ijzersulfide.</div></div><h4>Massaverhouding afleiden uit metingen</h4><p>Je kunt een massaverhouding ook <b>afleiden</b> uit gemeten hoeveelheden, zonder dat je de reactievergelijking met coëfficiënten hoeft te kennen. Laat je bijvoorbeeld koolstofmono-oxide (CO) ontleden tot koolstof (C) en zuurstof (O<sub>2</sub>): 2 CO (g) → 2 C (s) + O<sub>2</sub> (g). Reageert er 60,0 kg CO en ontstaat daarbij 34,0 kg O<sub>2</sub>, dan volgt uit de wet van behoud van massa dat er 60,0 − 34,0 = 26,0 kg C is ontstaan. De massaverhouding CO : C is dan 60,0 : 26,0 — en die verhouding kun je vervolgens gebruiken om andere hoeveelheden te berekenen, precies zoals bij voorbeeld 1.</p><div class=\"begrippen-box\"><b>Kernpunten massaverhouding:</b><ul><li>Elke reactie heeft zijn eigen, vaste massaverhouding tussen de beginstoffen (en de reactieproducten).</li><li>Verandert de hoeveelheid, dan verandert de <b>verhouding</b> niet — alleen de absolute hoeveelheden schalen mee.</li><li>Onbekende hoeveelheden bereken je door <b>kruislings vermenigvuldigen</b> met de bekende massaverhouding.</li><li>Een massaverhouding kun je ook afleiden uit twee gemeten massa's, met behulp van de wet van behoud van massa.</li></ul></div>",
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het als twee stoffen in een <b>vaste massaverhouding</b> reageren?",
      "opties": [
        "Ze reageren altijd in dezelfde onderlinge verhouding van massa's, ongeacht de totale hoeveelheid",
        "Ze hebben altijd precies dezelfde massa",
        "De massa van de stoffen verandert nooit tijdens de reactie",
        "Er is altijd een overmaat van één van de twee stoffen"
      ],
      "antwoord": 0,
      "uitleg": "De massaverhouding tussen twee stoffen die volledig met elkaar reageren, staat vast en geldt voor elke hoeveelheid van die reactie."
    },
    {
      "type": "invoer",
      "vraag": "IJzer en zwavel reageren in de massaverhouding Fe : S = 55,8 : 32,1. Bereken hoeveel gram zwavel volledig reageert met 10,0 g ijzer (1 decimaal).",
      "antwoord": "5,8|5.8",
      "uitleg": "x = (10,0 × 32,1) / 55,8 = 321,0 / 55,8 = 5,8 g zwavel."
    },
    {
      "type": "waaronwaar",
      "vraag": "De massaverhouding waarin twee stoffen reageren, verandert als je een grotere hoeveelheid van de beginstoffen gebruikt.",
      "antwoord": false,
      "uitleg": "Onwaar: de massaverhouding blijft precies gelijk, alleen de absolute hoeveelheden worden groter of kleiner."
    },
    {
      "type": "mc",
      "vraag": "Welke wet ligt aan de basis van het rekenen met massaverhoudingen?",
      "opties": [
        "De wet van Newton",
        "De wet van behoud van massa",
        "De wet van behoud van energie",
        "De wet op de reactiesnelheid"
      ],
      "antwoord": 1,
      "uitleg": "Massaverhoudingen zijn te berekenen dankzij de wet van behoud van massa: massa beginstoffen = massa reactieproducten."
    },
    {
      "type": "invoer",
      "vraag": "Bij de ontleding van koolstofmono-oxide (2 CO → 2 C + O2) is de massaverhouding CO : C gelijk aan 60,0 : 26,0. Bereken hoeveel kg CO nodig is om 13,0 kg C te maken (1 decimaal).",
      "antwoord": "30,0|30|30.0",
      "uitleg": "x = (60,0 × 13,0) / 26,0 = 780,0 / 26,0 = 30,0 kg CO."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je een onbekende massa als je de massaverhouding en één van de twee hoeveelheden kent?",
      "opties": [
        "Door de twee bekende getallen bij elkaar op te tellen",
        "Door de massa van de beginstof te delen door 2",
        "Door kruislings vermenigvuldigen met de bekende massaverhouding",
        "Door de reactietemperatuur op te zoeken"
      ],
      "antwoord": 2,
      "uitleg": "Je zet de massaverhouding en de bekende hoeveelheid in een tabelletje en berekent de onbekende (x) door kruislings te vermenigvuldigen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je van beide beginstoffen precies twee keer zoveel gebruikt (in dezelfde massaverhouding), ontstaat er ook twee keer zoveel reactieproduct.",
      "antwoord": true,
      "uitleg": "Waar: bij een verdubbeling van beide beginstoffen in de juiste verhouding verdubbelt ook de hoeveelheid reactieproduct."
    },
    {
      "type": "invoer",
      "vraag": "Ammoniak en waterstofchloride reageren in de massaverhouding 17,0 : 36,5. Bereken hoeveel gram waterstofchloride nodig is om volledig te reageren met 8,50 g ammoniak (2 decimalen).",
      "antwoord": "18,25|18.25",
      "uitleg": "x = (8,50 × 36,5) / 17,0 = 310,25 / 17,0 = 18,25 g waterstofchloride."
    },
    {
      "type": "waaronwaar",
      "vraag": "Je kunt een massaverhouding alleen berekenen als je van tevoren de kloppende reactievergelijking met coëfficiënten kent.",
      "antwoord": false,
      "uitleg": "Onwaar: een massaverhouding kun je ook rechtstreeks afleiden uit twee gemeten massa's, met behulp van de wet van behoud van massa."
    },
    {
      "type": "mc",
      "vraag": "Bij ijzer en zwavel (Fe + S → FeS) is de massaverhouding 55,8 : 32,1. Welke berekening geeft de massa van het ontstane ijzersulfide, als 20,0 g ijzer volledig reageert met 11,5 g zwavel?",
      "opties": [
        "20,0 g − 11,5 g = 8,5 g ijzersulfide",
        "20,0 g × 11,5 g = 230 g ijzersulfide",
        "Alleen 11,5 g, want ijzer verdwijnt volledig",
        "20,0 g + 11,5 g = 31,5 g ijzersulfide"
      ],
      "antwoord": 3,
      "uitleg": "Volgens de wet van behoud van massa is de massa van het reactieproduct gelijk aan de som van de massa's van de beginstoffen: 20,0 + 11,5 = 31,5 g."
    }
  ]
});
