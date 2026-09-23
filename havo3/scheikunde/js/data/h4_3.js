/* =========================================================
   Duru's Scheikunde (HAVO 3) — Energie en milieu
   Hoofdstuk 4 — Paragraaf 4.3 (Chemie Overal, Reacties en energie)
   ========================================================= */
DURU.register({
  id: "sch-h4-3-energie-milieu",
  hoofdstuk: 4,
  paragraaf: "4.3",
  titel: "Energie en milieu",
  korteUitleg: "Schadelijke uitstoot door fossiele brandstoffen, het versterkte broeikaseffect en alternatieven zoals waterstof en biomassa.",
  icoon: "🌍",
  kleur: "h4-thema",
  theorie: `<h3>4.3 Energie en milieu</h3>
<p>Onze energie voor verwarming, vervoer, elektriciteit en industrie komt nog steeds grotendeels uit <b>fossiele brandstoffen</b>: steenkool, aardolie en aardgas. Bij het verbranden hiervan komen stoffen vrij die schadelijk zijn voor milieu en gezondheid.</p>
<h4>Lucht- en bodemverontreiniging</h4>
<div class="begrippen-box">
  <ul>
    <li><b>Fijnstof</b> — kleine roetdeeltjes uit centrales en (vracht)auto's op diesel; slecht voor de longen.</li>
    <li><b>Smog</b> — een verstikkende mengeling van fijnstof en giftige gassen (o.a. koolstofmono-oxide, zwaveldioxide, stikstofoxiden) die op windstille dagen dagenlang kan blijven hangen.</li>
    <li><b>Zure regen</b> — zwaveldioxide (SO<sub>2</sub>) en stikstofoxiden (NO<sub>x</sub>) verzuren het regenwater. Dit tast gebouwen aan en verzuurt de bodem en natuur.</li>
  </ul>
</div>
<p>Deze uitstoot wordt beperkt door bijvoorbeeld een <b>roetfilter</b> in dieselauto's, het reinigen van rookgassen bij elektriciteitscentrales (waarbij zwaveldioxide wordt omgezet in het bruikbare gips CaSO<sub>4</sub>) en een <b>katalysator</b> die giftige uitlaatgassen omzet in ongevaarlijke stoffen. Vrachtauto's en bussen gebruiken vaak ook <b>AdBlue</b>, een vloeistof met ureum (CH<sub>4</sub>N<sub>2</sub>O) die giftig stikstofmono-oxide omzet in onschadelijke stoffen.</p>
<h4>Versterkt broeikaseffect</h4>
<p>Koolstofdioxide is een <b>broeikasgas</b>: het houdt warmte van de zon vast in de atmosfeer. Sinds het begin van de industriële revolutie is de concentratie CO<sub>2</sub> door grootschalige verbranding van fossiele brandstoffen met ongeveer <b>50% gestegen</b>. Hierdoor stijgt de temperatuur op aarde en verandert het klimaat wereldwijd — dit heet het <b>versterkte broeikaseffect</b>. Gevolgen zijn onder andere extremer weer (hittegolven, hevige regenval), het smelten van poolkappen en het stijgen van de zeespiegel.</p>
<h4>Alternatieven voor fossiele brandstoffen</h4>
<p>Om minder fossiele brandstoffen te verbranden kan worden overgestapt op <b>windenergie</b>, <b>zonne-energie</b> en <b>kernenergie</b>, of op <b>waterstof</b> als brandstof. Bij de verbranding van waterstof (H<sub>2</sub>) ontstaat namelijk alleen waterdamp — geen koolstofdioxide. Waterstof moet wel eerst gemaakt worden, bijvoorbeeld door <b>elektrolyse van water</b> met groene stroom.</p>
<p>Een ander alternatief is <b>biomassa</b> (materiaal van natuurlijke oorsprong, zoals houtsnippers en maisplanten) of een <b>biobrandstof</b> zoals bio-ethanol of biodiesel. Bij de verbranding van biomassa komt wel koolstofdioxide vrij, maar dat hoeft niet te zorgen voor een stijging van de concentratie in de atmosfeer: bomen en planten nemen tijdens hun groei via <b>fotosynthese</b> immers ongeveer evenveel CO<sub>2</sub> op als er later vrijkomt bij hun verbranding. Zo'n proces heet <b>CO<sub>2</sub>-neutraal</b>.</p>
<h4>Energie opslaan in stoffen</h4>
<p>Elektrische energie van windmolens en zonnepanelen kan tijdelijk worden opgeslagen in een chemische stof. Calciumhydroxide (Ca(OH)<sub>2</sub>) kan met overtollige elektrische energie verhit worden tot calciumoxide (CaO) en waterdamp. Is er weer energie nodig, dan wordt het calciumoxide met water gemengd: er komt dan veel warmte vrij (tot wel 450 °C).</p>`,
  vragen: [
    {
      type: "mc",
      vraag: "Welke drie brandstoffen worden fossiele brandstoffen genoemd?",
      opties: [
        "Steenkool, aardolie en aardgas",
        "Wind, zon en water",
        "Waterstof, biomassa en hout",
        "Uranium, zon en aardgas"
      ],
      antwoord: 0,
      uitleg: "Steenkool, aardolie en aardgas zijn de drie fossiele brandstoffen waar onze energievoorziening nog grotendeels van afhangt."
    },
    {
      type: "mc",
      vraag: "Wat is smog?",
      opties: [
        "Een broeikasgas dat de temperatuur verlaagt",
        "Een mengsel van fijnstof en giftige gassen dat op windstille dagen kan blijven hangen",
        "Een reagens om koolstofdioxide aan te tonen",
        "Een biobrandstof gemaakt van hout"
      ],
      antwoord: 1,
      uitleg: "Smog is een verstikkende mengeling van fijnstof en giftige gassen (o.a. CO, SO2, NOx) die vooral bij windstil weer in de lucht blijft hangen."
    },
    {
      type: "mc",
      vraag: "Door welke twee stoffen ontstaat er zure regen?",
      opties: [
        "Alleen koolstofdioxide",
        "Waterdamp uit elektriciteitscentrales",
        "Zwaveldioxide en stikstofoxiden die het regenwater verzuren",
        "Fotosynthese van planten"
      ],
      antwoord: 2,
      uitleg: "Zwaveldioxide en stikstofoxiden reageren met waterdamp in de lucht, waardoor zure regen ontstaat."
    },
    {
      type: "mc",
      vraag: "Welke functie heeft een katalysator in een auto?",
      opties: [
        "Hij verhoogt het brandstofverbruik van de motor",
        "Hij koelt alleen de motor af",
        "Hij versterkt de uitlaatgeur",
        "Hij zet giftige uitlaatgassen om in minder schadelijke stoffen"
      ],
      antwoord: 3,
      uitleg: "Een katalysator zet schadelijke uitlaatgassen om in minder schadelijke stoffen voordat ze de lucht in gaan."
    },
    {
      type: "waaronwaar",
      vraag: "Fijnstof en koolstofmono-oxide behoren tot de stoffen die vrijkomen bij de verbranding van fossiele brandstoffen.",
      antwoord: true,
      uitleg: "Waar: bij het verbranden van fossiele brandstoffen ontstaan onder andere fijnstof, koolstofmono-oxide, zwaveldioxide en stikstofoxiden."
    },
    {
      type: "waaronwaar",
      vraag: "Zure regen wordt vooral veroorzaakt door een teveel aan zuurstofgas in de lucht.",
      antwoord: false,
      uitleg: "Onwaar: zure regen ontstaat door zwaveldioxide en stikstofoxiden, niet door een teveel aan zuurstof."
    },
    {
      type: "waaronwaar",
      vraag: "Een voordeel van waterstof als brandstof is dat er bij verbranding uitsluitend waterdamp vrijkomt.",
      antwoord: true,
      uitleg: "Waar: bij de verbranding van waterstofgas ontstaat alleen waterdamp, geen koolstofdioxide."
    },
    {
      type: "invoer",
      vraag: "Vul het ontbrekende woord in: de opwarming van de aarde door een toename van koolstofdioxide in de atmosfeer heet het versterkte ______.",
      antwoord: "broeikaseffect",
      uitleg: "Het versterkte broeikaseffect ontstaat doordat de concentratie broeikasgassen (vooral koolstofdioxide) in de atmosfeer sterk is gestegen."
    },
    {
      type: "invoer",
      vraag: "Hout en maisplanten zijn materiaal van natuurlijke oorsprong. Vul in hoe we dit materiaal in het algemeen noemen: ______.",
      antwoord: "biomassa",
      uitleg: "Biomassa is materiaal van natuurlijke oorsprong dat gebruikt kan worden als (bio)brandstof."
    }
  ]
});
