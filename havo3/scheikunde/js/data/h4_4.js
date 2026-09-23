/* =========================================================
   Duru's Scheikunde (HAVO 3) — Overmaat en ondermaat
   Hoofdstuk 4 — Paragraaf 4.4 (Chemie Overal, Reacties en energie)
   ========================================================= */
DURU.register({
  id: "sch-h4-4-overmaat-ondermaat",
  hoofdstuk: 4,
  paragraaf: "4.4",
  titel: "Overmaat en ondermaat",
  korteUitleg: "Wat overmaat en ondermaat zijn bij reacties en hoe je rekent aan reacties waarbij een beginstof in overmaat aanwezig is.",
  icoon: "⚖️",
  kleur: "h4-thema",
  theorie: `<h3>4.4 Overmaat en ondermaat</h3>
<p>Meng je twee beginstoffen precies in de juiste <b>massaverhouding</b>, dan verloopt de reactie door totdat alle beginstoffen zijn omgezet. Meng je de beginstoffen in een <b>andere</b> verhouding, dan zal één beginstof volledig reageren: deze stof is in <b>ondermaat</b> aanwezig. Er blijft dan een deel van de andere beginstof over: die stof is in <b>overmaat</b> aanwezig.</p>
<p>Je gebruikt dit principe soms bewust: wil je zeker weten dat een bepaalde beginstof volledig reageert (bijvoorbeeld omdat de andere stof duur of giftig is), dan zorg je voor een overmaat van de andere beginstof. Zo leg je roestige schaatsijzers in een <b>overmaat</b> azijn: er is dan meer azijn aanwezig dan nodig is om alle roest te verwijderen, zodat de roest gegarandeerd volledig wegreageert.</p>
<div class="begrippen-box">
  <b>Kernregel:</b>
  <ul>
    <li><b>Ondermaat</b> = de beginstof die <b>volledig</b> reageert (raakt op).</li>
    <li><b>Overmaat</b> = de beginstof waarvan na afloop nog een deel <b>over</b> is.</li>
    <li>Voor het berekenen van de hoeveelheid <b>reactieproduct</b> ga je altijd uit van de stof in <b>ondermaat</b> — die bepaalt hoever de reactie komt.</li>
  </ul>
</div>
<h4>Rekenen met overmaat en ondermaat</h4>
<p>Om te bepalen welke stof in overmaat is, bereken je met de gegeven massaverhouding hoeveel je van de ene stof nodig hebt om de andere stof volledig te laten reageren (kruislings vermenigvuldigen), en vergelijk je dat met de werkelijk aanwezige hoeveelheid.</p>
<div class="voorbeeld">
  <div class="vb-kop">Voorbeeld 1 — Omzetting van koperoxide met methaan</div>
  <div class="stap">4 CuO (s) + CH<sub>4</sub> (g) → 4 Cu (s) + CO<sub>2</sub> (g) + 2 H<sub>2</sub>O (g)</div>
  <div class="stap">Je verhit 25 g koperoxide met 5,5 g methaan. Massaverhouding CuO : CH<sub>4</sub> = 19,9 : 1,00.</div>
  <div class="stap">Benodigde hoeveelheid methaan: x = (25 × 1,00) / 19,9 = 1,3 g CH<sub>4</sub>.</div>
  <div class="stap">Er is 5,5 g methaan aanwezig, maar er is maar 1,3 g nodig → methaan is in <b>overmaat</b> (koperoxide in ondermaat). De overmaat methaan is 5,5 − 1,3 = 4,2 gram.</div>
</div>
<div class="voorbeeld">
  <div class="vb-kop">Voorbeeld 2 — Synthese van hydrazine</div>
  <div class="stap">2 NH<sub>3</sub> + H<sub>2</sub>O<sub>2</sub> → N<sub>2</sub>H<sub>4</sub> + 2 H<sub>2</sub>O</div>
  <div class="stap">4,00 kg ammoniak gemengd met 3,50 kg waterstofperoxide. Massaverhouding NH<sub>3</sub> : H<sub>2</sub>O<sub>2</sub> = 34,1 : 34,0.</div>
  <div class="stap">Benodigd H<sub>2</sub>O<sub>2</sub>: x = (4,00 × 34,0) / 34,1 = 3,99 kg. Er is maar 3,50 kg aanwezig → waterstofperoxide is in <b>ondermaat</b>, ammoniak in overmaat.</div>
  <div class="stap">Reken door met de ondermaat (H<sub>2</sub>O<sub>2</sub> : N<sub>2</sub>H<sub>4</sub> = 1,00 : 0,942): x = (3,50 × 0,942) / 1,00 = 3,30 kg hydrazine.</div>
</div>`,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de definitie van 'ondermaat' bij een reactie?",
      opties: [
        "De beginstof die na de reactie nog overblijft",
        "Het reactieproduct dat als laatste ontstaat",
        "De beginstof die volledig reageert (raakt op)",
        "Een stof die nooit meedoet aan de reactie"
      ],
      antwoord: 2,
      uitleg: "De stof in ondermaat reageert volledig; deze raakt op tijdens de reactie."
    },
    {
      type: "mc",
      vraag: "Wat is de definitie van 'overmaat' bij een reactie?",
      opties: [
        "De beginstof waarvan na afloop van de reactie nog een deel over is",
        "De beginstof die als eerste volledig reageert",
        "Het totaal van beide beginstoffen samen",
        "Een reactieproduct dat verdampt"
      ],
      antwoord: 0,
      uitleg: "De stof in overmaat reageert niet volledig; er blijft na afloop nog een deel van over."
    },
    {
      type: "mc",
      vraag: "Bij het berekenen van de hoeveelheid gevormd reactieproduct ga je altijd uit van:",
      opties: [
        "De stof die in overmaat aanwezig is",
        "Het gemiddelde van beide beginstoffen",
        "De stof met de grootste massa",
        "De stof die in ondermaat aanwezig is"
      ],
      antwoord: 3,
      uitleg: "De stof in ondermaat bepaalt hoever de reactie komt, omdat deze stof volledig opraakt."
    },
    {
      type: "mc",
      vraag: "Waarom legt men roestige schaatsijzers in een overmaat azijn?",
      opties: [
        "Om het ijzer zwaarder te maken",
        "Om zeker te weten dat alle roest volledig wegreageert",
        "Om de schaats een blauwe kleur te geven",
        "Om de ontbrandingstemperatuur te verlagen"
      ],
      antwoord: 1,
      uitleg: "Door een overmaat azijn te gebruiken, weet je zeker dat de roest (de ondermaat) volledig wegreageert."
    },
    {
      type: "mc",
      vraag: "In voorbeeld 1 (25 g koperoxide met 5,5 g methaan, verhouding 19,9 : 1,00) blijkt maar 1,3 g methaan nodig. Welke stof is hier in ondermaat?",
      opties: [
        "Koperoxide (CuO)",
        "Methaan (CH4)",
        "Koper (Cu)",
        "Water (H2O)"
      ],
      antwoord: 0,
      uitleg: "Omdat er meer methaan aanwezig is dan nodig (5,5 g > 1,3 g), is methaan in overmaat en koperoxide dus in ondermaat."
    },
    {
      type: "waaronwaar",
      vraag: "Als de beginstoffen precies in de juiste massaverhouding gemengd zijn, is er geen sprake van overmaat of ondermaat.",
      antwoord: true,
      uitleg: "Waar: dan reageren beide beginstoffen precies volledig, zonder dat er iets van één van beide overblijft."
    },
    {
      type: "waaronwaar",
      vraag: "Voor het berekenen van de hoeveelheid gevormd reactieproduct ga je altijd uit van de stof die in overmaat aanwezig is.",
      antwoord: false,
      uitleg: "Onwaar: je gaat altijd uit van de stof in ondermaat, want die stof bepaalt hoever de reactie kan komen."
    },
    {
      type: "invoer",
      vraag: "In voorbeeld 1 is 5,5 g methaan aanwezig en 1,3 g nodig. Hoeveel gram methaan is er in overmaat (1 decimaal)?",
      antwoord: "4,2|4.2",
      uitleg: "5,5 − 1,3 = 4,2 gram methaan is in overmaat."
    },
    {
      type: "invoer",
      vraag: "In voorbeeld 2 is 3,99 kg waterstofperoxide nodig, maar er is maar 3,50 kg aanwezig. Welke stof is dan in ondermaat?",
      antwoord: "waterstofperoxide|h2o2",
      uitleg: "Omdat er minder waterstofperoxide aanwezig is dan nodig (3,50 kg < 3,99 kg), is waterstofperoxide de stof in ondermaat."
    }
  ]
});
