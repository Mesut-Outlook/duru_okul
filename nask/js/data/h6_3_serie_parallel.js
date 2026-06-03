DURU.register({
  id: "h6-3",
  hoofdstuk: 6,
  paragraaf: "6.3",
  titel: "Serie- en parallelschakeling",
  korteUitleg: "Lampjes achter elkaar (serie) of naast elkaar (parallel) — leer het verschil!",
  icoon: "💡",

  theorie: `
<h3>Serie- en parallelschakeling</h3>

<p>Er zijn twee manieren om meerdere lampjes (of andere onderdelen) op een batterij aan te sluiten:
<b>in serie</b> of <b>parallel</b>. Ze gedragen zich heel anders!</p>

<h4>Serieschakeling</h4>
<p>Bij een <b>serieschakeling</b> staan de onderdelen <b>achter elkaar</b> in één enkele stroomkring.
Er is maar één pad waarover de stroom kan lopen.</p>

<figure class="bron">
<svg viewBox="0 0 420 180" width="100%" style="max-width:420px;display:block;margin:0 auto;font-family:sans-serif">
  <!-- draad (rechthoek) -->
  <rect x="20" y="30" width="380" height="120" rx="8" fill="none" stroke="#333" stroke-width="2.5"/>

  <!-- Batterij links midden -->
  <line x1="20" y1="90" x2="50" y2="90" stroke="#333" stroke-width="2.5"/>
  <line x1="50" y1="70" x2="50" y2="110" stroke="#e74c3c" stroke-width="4"/>
  <line x1="62" y1="78" x2="62" y2="102" stroke="#333" stroke-width="2.5"/>
  <line x1="62" y1="90" x2="80" y2="90" stroke="#333" stroke-width="2.5"/>
  <text x="48" y="65" font-size="11" fill="#e74c3c" text-anchor="middle">+</text>
  <text x="64" y="115" font-size="11" fill="#333" text-anchor="middle">−</text>
  <text x="56" y="140" font-size="12" fill="#555" text-anchor="middle">batterij</text>

  <!-- Lampje 1 (boven, midden-links) -->
  <circle cx="180" cy="30" r="18" fill="none" stroke="#f39c12" stroke-width="2.5"/>
  <line x1="167" y1="17" x2="193" y2="43" stroke="#f39c12" stroke-width="2"/>
  <line x1="193" y1="17" x2="167" y2="43" stroke="#f39c12" stroke-width="2"/>
  <line x1="155" y1="30" x2="162" y2="30" stroke="#333" stroke-width="2.5"/>
  <line x1="198" y1="30" x2="205" y2="30" stroke="#333" stroke-width="2.5"/>
  <text x="180" y="12" font-size="12" fill="#555" text-anchor="middle">L1</text>

  <!-- Lampje 2 (boven, midden-rechts) -->
  <circle cx="290" cy="30" r="18" fill="none" stroke="#f39c12" stroke-width="2.5"/>
  <line x1="277" y1="17" x2="303" y2="43" stroke="#f39c12" stroke-width="2"/>
  <line x1="303" y1="17" x2="277" y2="43" stroke="#f39c12" stroke-width="2"/>
  <line x1="265" y1="30" x2="272" y2="30" stroke="#333" stroke-width="2.5"/>
  <line x1="308" y1="30" x2="315" y2="30" stroke="#333" stroke-width="2.5"/>
  <text x="290" y="12" font-size="12" fill="#555" text-anchor="middle">L2</text>

  <!-- pijl stroom -->
  <text x="210" y="168" font-size="12" fill="#2980b9" text-anchor="middle">→ stroom loopt in één kring →</text>
</svg>
<figcaption>Serieschakeling: batterij + lampje L1 + lampje L2 achter elkaar in één kring.</figcaption>
</figure>

<ul>
  <li>De <b>stroom is overal even groot</b>: door L1 en L2 loopt precies evenveel stroom.</li>
  <li>De <b>spanning wordt verdeeld</b>: elke lamp krijgt maar een deel van de spanning van de batterij. Met meer lampjes brandt elk lampje <em>minder fel</em>.</li>
  <li><b>Als één lampje stukgaat</b> (of de draad breekt), is de kring verbroken → <em>alle lampjes gaan uit</em>.</li>
</ul>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Oude kerstverlichting was in serie geschakeld. Ging er één peertje kapot?
  Dan ging de <em>hele slinger</em> uit!
</div>

<h4>Parallelschakeling</h4>
<p>Bij een <b>parallelschakeling</b> staan de onderdelen <b>naast elkaar</b>, elk in een eigen tak.
De stroom kan via meerdere paden stromen.</p>

<figure class="bron">
<svg viewBox="0 0 420 220" width="100%" style="max-width:420px;display:block;margin:0 auto;font-family:sans-serif">
  <!-- Buitenste kring -->
  <rect x="20" y="20" width="380" height="180" rx="8" fill="none" stroke="#333" stroke-width="2.5"/>

  <!-- Batterij links midden -->
  <line x1="20" y1="110" x2="50" y2="110" stroke="#333" stroke-width="2.5"/>
  <line x1="50" y1="86" x2="50" y2="134" stroke="#e74c3c" stroke-width="4"/>
  <line x1="63" y1="96" x2="63" y2="124" stroke="#333" stroke-width="2.5"/>
  <line x1="63" y1="110" x2="90" y2="110" stroke="#333" stroke-width="2.5"/>
  <text x="48" y="82" font-size="11" fill="#e74c3c" text-anchor="middle">+</text>
  <text x="65" y="140" font-size="11" fill="#333" text-anchor="middle">−</text>
  <text x="56" y="165" font-size="12" fill="#555" text-anchor="middle">batterij</text>

  <!-- Verticale verbindingsdraden (splits) -->
  <line x1="220" y1="20" x2="220" y2="200" stroke="#333" stroke-width="2"/>
  <line x1="360" y1="20" x2="360" y2="200" stroke="#333" stroke-width="2"/>

  <!-- Lampje 1 (bovenste tak) -->
  <circle cx="290" cy="60" r="18" fill="none" stroke="#f39c12" stroke-width="2.5"/>
  <line x1="277" y1="47" x2="303" y2="73" stroke="#f39c12" stroke-width="2"/>
  <line x1="303" y1="47" x2="277" y2="73" stroke="#f39c12" stroke-width="2"/>
  <line x1="220" y1="60" x2="272" y2="60" stroke="#333" stroke-width="2.5"/>
  <line x1="308" y1="60" x2="360" y2="60" stroke="#333" stroke-width="2.5"/>
  <text x="290" y="42" font-size="12" fill="#555" text-anchor="middle">L1</text>

  <!-- Lampje 2 (onderste tak) -->
  <circle cx="290" cy="155" r="18" fill="none" stroke="#f39c12" stroke-width="2.5"/>
  <line x1="277" y1="142" x2="303" y2="168" stroke="#f39c12" stroke-width="2"/>
  <line x1="303" y1="142" x2="277" y2="168" stroke="#f39c12" stroke-width="2"/>
  <line x1="220" y1="155" x2="272" y2="155" stroke="#333" stroke-width="2.5"/>
  <line x1="308" y1="155" x2="360" y2="155" stroke="#333" stroke-width="2.5"/>
  <text x="290" y="137" font-size="12" fill="#555" text-anchor="middle">L2</text>

  <!-- pijl stroom -->
  <text x="210" y="213" font-size="12" fill="#2980b9" text-anchor="middle">stroom splits in twee takken</text>
</svg>
<figcaption>Parallelschakeling: lampje L1 en L2 staan naast elkaar in eigen takken, beide op de volle spanning.</figcaption>
</figure>

<ul>
  <li>Elk onderdeel krijgt de <b>volle spanning</b> van de batterij. Lampjes branden even fel als ze elk apart aan de batterij hingen.</li>
  <li><b>Als één lampje stukgaat</b>, blijven de andere gewoon branden — de andere takken zijn nog intact.</li>
  <li>Je kunt onderdelen <b>apart aan- en uitzetten</b> (schakelaar in één tak).</li>
</ul>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  De lampen en apparaten in je huis staan <b>parallel</b> geschakeld. Ze krijgen allemaal 230 V en je kunt ze los in- en uitschakelen. Gaat een lamp kapot? De rest blijft gewoon branden.
</div>

<h4>Vergelijking op een rij</h4>
<table class="nask">
  <tr><th>Eigenschap</th><th>Serieschakeling</th><th>Parallelschakeling</th></tr>
  <tr><td>Opstelling</td><td>Achter elkaar, één pad</td><td>Naast elkaar, meerdere takken</td></tr>
  <tr><td>Spanning per lampje</td><td>Gedeeld (minder)</td><td>Volledig (evenveel als bron)</td></tr>
  <tr><td>Stroom</td><td>Overal gelijk</td><td>Verdeeld over de takken</td></tr>
  <tr><td>Als één lampje kapot</td><td>Alles gaat uit</td><td>Rest blijft branden</td></tr>
  <tr><td>Zelfstandig schakelen</td><td>Nee</td><td>Ja</td></tr>
  <tr><td>Voorbeeld</td><td>Oude kerstverlichting</td><td>Lampen in huis (230 V)</td></tr>
</table>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Herken een serieschakeling: er is <em>maar één draad</em> waarlangs de stroom loopt — alle onderdelen zitten er in één rij op. Bij parallel zie je <em>vertakkingen</em> (zijpaden).
</div>
`,

  vragen: [

    // ── Niveau 1 — meerkeuze / waar-onwaar ──────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Welke uitspraak beschrijft een serieschakeling?",
      opties: [
        "De lampjes staan naast elkaar in aparte takken.",
        "De lampjes staan achter elkaar in één enkele stroomkring.",
        "Elk lampje krijgt de volle spanning van de batterij.",
        "Je kunt elk lampje apart uitschakelen."
      ],
      antwoord: 1,
      uitleg: "Bij een <b>serieschakeling</b> staan de onderdelen <b>achter elkaar</b> in één enkele kring."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "De lampen in een gewoon huis staan ...",
      opties: [
        "in serie, want ze krijgen alle 230 V.",
        "parallel, want ze kunnen los van elkaar aan en uit.",
        "in serie, want als één lamp kapot is, gaan ze allemaal uit.",
        "parallel, want de stroom is overal even groot."
      ],
      antwoord: 1,
      uitleg: "Thuislampen staan <b>parallel</b>: ze krijgen elk de volle 230 V en zijn los te schakelen."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Bij een serieschakeling brandt elk lampje even fel als wanneer je het in zijn eentje op de batterij zou aansluiten.",
      antwoord: false,
      uitleg: "Onwaar. Bij serie wordt de spanning <b>verdeeld</b> over de lampjes; elk lampje krijgt minder spanning en brandt dus <em>minder fel</em>."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Als één lampje kapotgaat in een serieschakeling, gaan alle andere lampjes ook uit.",
      antwoord: true,
      uitleg: "Waar! Bij serie is er maar één pad voor de stroom. Breekt dat pad, dan stopt de stroom <b>overal</b>."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "In een parallelschakeling kunnen lampjes elk apart worden uitgeschakeld.",
      antwoord: true,
      uitleg: "Waar. Elke tak heeft zijn eigen pad, zodat je één tak kunt onderbreken zonder de rest te beïnvloeden."
    },

    // ── Niveau 2 ─────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 2,
      vraag: "Kijk naar het schema hieronder. Is dit een serie- of parallelschakeling?",
      figuur: `<svg viewBox="0 0 300 140" width="100%" style="max-width:300px;display:block;margin:8px auto;font-family:sans-serif">
  <rect x="15" y="20" width="270" height="100" rx="6" fill="none" stroke="#333" stroke-width="2.2"/>
  <line x1="15" y1="70" x2="40" y2="70" stroke="#333" stroke-width="2.2"/>
  <line x1="40" y1="50" x2="40" y2="90" stroke="#e74c3c" stroke-width="3.5"/>
  <line x1="52" y1="58" x2="52" y2="82" stroke="#333" stroke-width="2.2"/>
  <line x1="52" y1="70" x2="70" y2="70" stroke="#333" stroke-width="2.2"/>
  <circle cx="115" cy="20" r="15" fill="none" stroke="#f39c12" stroke-width="2.2"/>
  <line x1="104" y1="9" x2="126" y2="31" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="126" y1="9" x2="104" y2="31" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="85" y1="20" x2="100" y2="20" stroke="#333" stroke-width="2.2"/>
  <line x1="130" y1="20" x2="145" y2="20" stroke="#333" stroke-width="2.2"/>
  <circle cx="210" cy="20" r="15" fill="none" stroke="#f39c12" stroke-width="2.2"/>
  <line x1="199" y1="9" x2="221" y2="31" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="221" y1="9" x2="199" y2="31" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="160" y1="20" x2="195" y2="20" stroke="#333" stroke-width="2.2"/>
  <line x1="225" y1="20" x2="285" y2="20" stroke="#333" stroke-width="2.2"/>
</svg>`,
      opties: [
        "Serieschakeling, want de lampjes staan achter elkaar in één kring.",
        "Parallelschakeling, want er zijn twee takken.",
        "Serieschakeling, want elk lampje krijgt de volle spanning.",
        "Parallelschakeling, want de stroom is overal gelijk."
      ],
      antwoord: 0,
      uitleg: "In het schema lopen de twee lampjes <b>achter elkaar</b> langs de bovenkant van de kring — dat is een <b>serieschakeling</b>."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Kijk naar het schema hieronder. Is dit een serie- of parallelschakeling?",
      figuur: `<svg viewBox="0 0 300 200" width="100%" style="max-width:300px;display:block;margin:8px auto;font-family:sans-serif">
  <rect x="15" y="15" width="270" height="170" rx="6" fill="none" stroke="#333" stroke-width="2.2"/>
  <line x1="15" y1="100" x2="42" y2="100" stroke="#333" stroke-width="2.2"/>
  <line x1="42" y1="78" x2="42" y2="122" stroke="#e74c3c" stroke-width="3.5"/>
  <line x1="55" y1="88" x2="55" y2="112" stroke="#333" stroke-width="2.2"/>
  <line x1="55" y1="100" x2="80" y2="100" stroke="#333" stroke-width="2.2"/>
  <line x1="160" y1="15" x2="160" y2="185" stroke="#333" stroke-width="2"/>
  <line x1="285" y1="15" x2="285" y2="185" stroke="#333" stroke-width="2"/>
  <circle cx="222" cy="55" r="15" fill="none" stroke="#f39c12" stroke-width="2.2"/>
  <line x1="211" y1="44" x2="233" y2="66" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="233" y1="44" x2="211" y2="66" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="160" y1="55" x2="207" y2="55" stroke="#333" stroke-width="2.2"/>
  <line x1="237" y1="55" x2="285" y2="55" stroke="#333" stroke-width="2.2"/>
  <circle cx="222" cy="145" r="15" fill="none" stroke="#f39c12" stroke-width="2.2"/>
  <line x1="211" y1="134" x2="233" y2="156" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="233" y1="134" x2="211" y2="156" stroke="#f39c12" stroke-width="1.8"/>
  <line x1="160" y1="145" x2="207" y2="145" stroke="#333" stroke-width="2.2"/>
  <line x1="237" y1="145" x2="285" y2="145" stroke="#333" stroke-width="2.2"/>
</svg>`,
      opties: [
        "Serieschakeling, want er is maar één pad.",
        "Parallelschakeling, want de lampjes staan in aparte takken naast elkaar.",
        "Serieschakeling, want de lampjes branden minder fel.",
        "Parallelschakeling, want de stroom is overal gelijk."
      ],
      antwoord: 1,
      uitleg: "In het schema heeft elk lampje een <b>eigen tak</b> — dat zijn twee paden naast elkaar. Dit is een <b>parallelschakeling</b>."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Bij een serieschakeling met twee identieke lampjes op een batterij van 6 V, hoeveel volt krijgt elk lampje?",
      opties: [
        "6 V, want elk lampje krijgt de volle spanning.",
        "3 V, want de spanning wordt gelijk verdeeld over de twee lampjes.",
        "12 V, want de lampjes verdubbelen de spanning.",
        "0 V, want de spanning is op."
      ],
      antwoord: 1,
      uitleg: "Bij serie wordt de spanning <b>verdeeld</b>. Met twee gelijke lampjes op 6 V krijgt elk lampje 6 ÷ 2 = <b>3 V</b>."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Oude kerstverlichting bestaat uit 20 lampjes in serie op 230 V. Eén lampje gaat kapot. Wat gebeurt er?",
      opties: [
        "Alleen dat ene kapotte lampje gaat uit.",
        "De helft van de lampjes gaat uit.",
        "Alle 20 lampjes gaan uit.",
        "De lampjes branden juist feller."
      ],
      antwoord: 2,
      uitleg: "Bij een <b>serieschakeling</b> is er maar één kring. Kapot lampje = kring verbroken = <b>alle lampjes uit</b>."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Bij een parallelschakeling met twee lampjes krijgen beide lampjes de volle spanning van de batterij.",
      antwoord: true,
      uitleg: "Waar. Elk lampje in een parallelschakeling is rechtstreeks op de batterijpolen aangesloten en krijgt de <b>volle spanning</b>."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een serieschakeling met drie lampjes gaat de rest gewoon branden als er één kapotgaat.",
      antwoord: false,
      uitleg: "Onwaar. Bij serie is er maar één stroompad. Een kapot lampje verbreekt dit pad en <em>alle</em> lampjes gaan uit."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Reken maar uit, Duru! Een serieschakeling heeft drie gelijke lampjes op een batterij van 9 V. Welke spanning staat er over elk lampje?",
      opties: [
        "9 V",
        "27 V",
        "3 V",
        "1 V"
      ],
      antwoord: 2,
      uitleg: "Bij serie wordt de spanning gelijk verdeeld: 9 V ÷ 3 = <b>3 V</b> per lampje."
    },

    // ── Niveau 3 — redeneren / toepassingen ──────────────────────────────────

    {
      type: "mc",
      niveau: 3,
      vraag: "Een leerling sluit vier lampjes op een batterij aan in serie. De lampjes branden erg zwak. Ze sluit daarna dezelfde lampjes parallel aan op dezelfde batterij. Wat merkt ze nu?",
      opties: [
        "De lampjes branden even zwak als voorheen.",
        "De lampjes branden feller, want ze krijgen elk de volle spanning.",
        "De lampjes branden feller, want de stroom is nu groter in de kring.",
        "De lampjes gaan allemaal uit, want de stroom wordt verdeeld."
      ],
      antwoord: 1,
      uitleg: "Parallel: elk lampje krijgt de <b>volle spanning</b> van de batterij in plaats van een kwart. Ze branden dus veel feller.",
      hint: "Denk aan wat elke lampje krijgt: gedeelde spanning (serie) of volle spanning (parallel)?"
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "In een huis zijn vijf kamers elk uitgerust met één lamp. Ze zijn allemaal op het lichtnet (230 V) aangesloten. De lamp in de keuken brandt door. Welke andere lampen gaan uit?",
      opties: [
        "Alle lampen in huis gaan uit.",
        "De twee kamers naast de keuken gaan uit.",
        "Geen enkele andere lamp gaat uit.",
        "Alle lampen gaan feller branden."
      ],
      antwoord: 2,
      uitleg: "Thuislampen staan <b>parallel</b>. Elke lamp heeft zijn eigen tak. Gaat er één kapot, dan blijven de andere takken intact — <em>geen andere lamp gaat uit</em>."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Je kunt bij een parallelschakeling één lamp uitschakelen zonder de andere lampen te beïnvloeden.",
      antwoord: true,
      uitleg: "Waar. Elke tak is onafhankelijk. Een schakelaar in één tak verbreekt alleen die tak — de rest blijft branden.",
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Twee lampjes branden even fel in een schakeling. Eén lampje gaat kapot — de andere gaat meteen ook uit. Welke schakeling is dit hoogstwaarschijnlijk?",
      opties: [
        "Een parallelschakeling, want de takken zijn afhankelijk van elkaar.",
        "Een serieschakeling, want het verbreken van de kring stopt alle stroom.",
        "Een parallelschakeling, want de spanning wordt verdeeld.",
        "Een serieschakeling, want de spanning blijft gelijk."
      ],
      antwoord: 1,
      uitleg: "Als het uitvallen van één lampje de andere ook uitzet, is er maar één stroompad — dat is kenmerkend voor een <b>serieschakeling</b>.",
      hint: "Bij welke schakeling is er slechts één pad voor de stroom?"
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Welke schakeling heeft de voorkeur voor de verlichting van een fiets, zodat voor- en achterlicht onafhankelijk kunnen werken?",
      opties: [
        "Serieschakeling, want de stroom is overal gelijk.",
        "Parallelschakeling, want elk licht kan apart branden.",
        "Serieschakeling, want de lampjes branden feller.",
        "Het maakt niet uit — beide schakelingstypen geven hetzelfde resultaat."
      ],
      antwoord: 1,
      uitleg: "Een <b>parallelschakeling</b> is beter: elk licht heeft zijn eigen tak en kan onafhankelijk werken. Gaat het voorlicht kapot, dan brandt het achterlicht gewoon door.",
      hint: "Wat is het voordeel van parallel als één onderdeel kapotgaat?"
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "In een parallelschakeling is de stroom overal in de kring even groot.",
      antwoord: false,
      uitleg: "Onwaar. Bij parallel <em>splitst</em> de stroom zich over de takken. De totale stroom van de batterij is groter dan de stroom door één tak. Overal gelijke stroom is een kenmerk van de <b>serie</b>schakeling."
    }

  ]
});
