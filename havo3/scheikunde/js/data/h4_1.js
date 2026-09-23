/* =========================================================
   Duru's Scheikunde (HAVO 3) — Verbranding
   Hoofdstuk 4 — Paragraaf 4.1 (Chemie Overal, Reacties en energie)
   ========================================================= */
DURU.register({
  id: "sch-h4-1-verbranding",
  hoofdstuk: 4,
  paragraaf: "4.1",
  titel: "Verbranding",
  korteUitleg: "De branddriehoek, volledige versus onvolledige verbranding, reagentia en het opstellen van verbrandingsvergelijkingen.",
  icoon: "🔥",
  kleur: "h4-thema",
  theorie: `<h3>4.1 Verbranding</h3>
<p>Een <b>verbrandingsreactie</b> is een <b>exotherme</b> chemische reactie tussen een brandbare stof en zuurstof (O<sub>2</sub>), waarbij warmte en licht vrijkomen. Bij kamertemperatuur vindt geen verbranding plaats — er is warmte nodig om de reactie op gang te brengen.</p>
<h4>De branddriehoek — drie voorwaarden voor verbranding</h4>
<div class="begrippen-box">
  <ul>
    <li><b>Brandbare stof</b> (brandstof)</li>
    <li><b>Zuurstof</b> (O<sub>2</sub>)</li>
    <li><b>Ontbrandingstemperatuur</b> — de temperatuur moet hoog genoeg zijn</li>
  </ul>
</div>
<p>Neem je één van deze drie voorwaarden weg, dan stopt de verbranding of ontstaat er geen brand. Zo blus je een brandende prullenbak met een deksel (zuurstof weg) of met water (temperatuur onder de ontbrandingstemperatuur brengen). Let op: een brandende pan met hete olie (&gt;100 °C) mag je <b>NOOIT</b> met water blussen — het water verdampt onmiddellijk tot een wolk van stoom en brandende oliedruppels (een steekvlam)! Doe in dat geval een deksel op de pan.</p>
<h4>Volledige en onvolledige verbranding</h4>
<p>Is er <b>voldoende</b> zuurstof aanwezig, dan brandt de brandstof met een kleurloze of blauwe vlam: dit heet <b>volledige verbranding</b>. Sluit je de luchttoevoer van een brander (bijna) af, dan is er <b>onvoldoende</b> zuurstof: de vlam wordt geel en er ontstaat zwart <b>roet</b> (C) en/of het zeer giftige gas <b>koolstofmono-oxide</b> (CO). Dit heet <b>onvolledige verbranding</b>. Koolstofmono-oxide is extra gevaarlijk omdat je het niet ruikt of ziet — installeer daarom een CO-melder in huis.</p>
<div class="formule-box">
  <div class="formule">atoomsoort in de brandstof → reactieproduct(en)</div>
  <small>
    C (koolstof) → CO<sub>2</sub> bij volledige verbranding, of C (roet) en/of CO bij onvolledige verbranding<br>
    H (waterstof) → H<sub>2</sub>O (altijd, ongeacht volledig of onvolledig)<br>
    S (zwavel) → SO<sub>2</sub> (altijd)<br>
    O (zuurstof al aanwezig in de brandstof zelf) → geen extra reactieproduct
  </small>
</div>
<h4>Reactieproducten aantonen met een reagens</h4>
<p>Een <b>reagens</b> is een stof waarmee je een andere stof kunt aantonen. Helder <b>kalkwater</b> wordt troebel als je er koolstofdioxide doorheen blaast — dit is de aantoningsreactie voor CO<sub>2</sub>. Wit <b>kopersulfaat</b> kleurt blauw zodra het met water in aanraking komt — dit toont water (H<sub>2</sub>O) aan.</p>
<h4>Vergelijkingen van verbrandingsreacties opstellen</h4>
<p>Bij een verbranding reageert een brandbare stof met zuurstof (O<sub>2</sub>). Zet eerst de formules van deze twee stoffen voor de pijl. Bepaal met de tabel hierboven welke reactieproducten ontstaan op basis van de atoomsoorten in de brandstof en zet deze na de pijl. Maak de vergelijking tot slot kloppend; pas de coëfficiënt van O<sub>2</sub> als laatste aan.</p>
<div class="voorbeeld">
  <div class="vb-kop">Voorbeeld — Volledige verbranding van koolstofdisulfide (CS<sub>2</sub>)</div>
  <div class="stap">Formules opschrijven: CS<sub>2</sub> + O<sub>2</sub> → CO<sub>2</sub> + SO<sub>2</sub></div>
  <div class="stap">C en S kloppend maken: CS<sub>2</sub> + O<sub>2</sub> → CO<sub>2</sub> + 2 SO<sub>2</sub></div>
  <div class="stap">O als laatste kloppend maken: CS<sub>2</sub> + 3 O<sub>2</sub> → CO<sub>2</sub> + 2 SO<sub>2</sub></div>
</div>
<p>Bij de volledige verbranding van butaan (C<sub>4</sub>H<sub>10</sub>) ontstaan CO<sub>2</sub> en H<sub>2</sub>O: 2 C<sub>4</sub>H<sub>10</sub> + 13 O<sub>2</sub> → 8 CO<sub>2</sub> + 10 H<sub>2</sub>O.</p>`,
  vragen: [
    {
      type: "mc",
      vraag: "Wat zijn volgens de branddriehoek de drie voorwaarden voor verbranding?",
      opties: [
        "Brandbare stof, zuurstof en de ontbrandingstemperatuur",
        "Water, zuurstof en koolstofdioxide",
        "Brandbare stof, warmte en een reagens",
        "Zuurstof, roet en een vonk"
      ],
      antwoord: 0,
      uitleg: "De branddriehoek bestaat uit een brandbare stof, zuurstof en het bereiken van de ontbrandingstemperatuur. Ontbreekt één van deze drie, dan is er geen verbranding."
    },
    {
      type: "mc",
      vraag: "Op welke manier zorgt water ervoor dat een brandende prullenbak dooft?",
      opties: [
        "Omdat het water zuurstof aan het vuur toevoegt",
        "Omdat het water de brandstof afkoelt tot onder de ontbrandingstemperatuur",
        "Omdat het water de brandstof in roet verandert",
        "Omdat het water als reagens werkt"
      ],
      antwoord: 1,
      uitleg: "Water koelt de brandbare stof af tot onder de ontbrandingstemperatuur, waardoor de verbranding stopt. Bij hete olie werkt dit niet: dan ontstaat juist een gevaarlijke steekvlam."
    },
    {
      type: "mc",
      vraag: "Wat verandert er aan de vlam als je de luchttoevoer van een brander (bijna) afsluit?",
      opties: [
        "Er ontstaat een blauwe vlam door volledige verbranding",
        "Het vuur dooft direct volledig uit",
        "Er ontstaat een gele vlam met roet en/of koolstofmono-oxide door onvoldoende zuurstof",
        "De ontbrandingstemperatuur daalt automatisch naar 0 °C"
      ],
      antwoord: 2,
      uitleg: "Bij onvoldoende zuurstof (luchttoevoer bijna dicht) verloopt de verbranding onvolledig: gele vlam, roet en/of koolstofmono-oxide."
    },
    {
      type: "mc",
      vraag: "Welke eigenschap maakt koolstofmono-oxide (CO) zo gevaarlijk voor mensen?",
      opties: [
        "Het ruikt sterk naar rotte eieren, waardoor je het meteen opmerkt",
        "Het is alleen gevaarlijk bij temperaturen boven 500 °C",
        "Het reageert nooit met stoffen in je lichaam",
        "Het is een reukloos en kleurloos gas, waardoor je vergiftiging niet merkt"
      ],
      antwoord: 3,
      uitleg: "Koolstofmono-oxide is reukloos en kleurloos. Slachtoffers raken bewusteloos zonder gewaarschuwd te zijn; daarom is een CO-melder belangrijk."
    },
    {
      type: "waaronwaar",
      vraag: "Volledige verbranding vindt plaats als er onvoldoende zuurstof aanwezig is.",
      antwoord: false,
      uitleg: "Onwaar: bij volledige verbranding is juist voldoende zuurstof aanwezig. Bij onvoldoende zuurstof spreek je van onvolledige verbranding."
    },
    {
      type: "waaronwaar",
      vraag: "Helder kalkwater wordt troebel als er koolstofdioxide doorheen geblazen wordt.",
      antwoord: true,
      uitleg: "Waar: kalkwater is het standaardreagens om koolstofdioxide aan te tonen; het wordt troebel."
    },
    {
      type: "invoer",
      vraag: "Vul de ontbrekende coëfficiënt in: CH<sub>4</sub> + ... O<sub>2</sub> → CO<sub>2</sub> + 2 H<sub>2</sub>O (volledige verbranding van methaan).",
      antwoord: "2|twee",
      uitleg: "CH4 + 2 O2 → CO2 + 2 H2O. Er zijn 2 zuurstofmoleculen nodig: één voor de CO2 en één voor de twee watermoleculen."
    },
    {
      type: "invoer",
      vraag: "Zwavel (S) verbrandt volledig met zuurstof. Welk gas ontstaat er dan? Geef de naam van de stof.",
      antwoord: "zwaveldioxide|so2",
      uitleg: "S + O2 → SO2. Zwavel levert bij verbranding altijd zwaveldioxide (SO2) als reactieproduct."
    },
    {
      type: "invoer",
      vraag: "Wit kopersulfaat kleurt blauw zodra het met een bepaalde stof in aanraking komt. Welke stof toon je hiermee aan?",
      antwoord: "water|h2o",
      uitleg: "Blauw kleurend kopersulfaat is het reagens waarmee je water aantoont."
    }
  ]
});
