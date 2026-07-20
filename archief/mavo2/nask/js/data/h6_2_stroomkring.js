DURU.register({
  id: "h6-2",
  hoofdstuk: 6,
  paragraaf: "6.2",
  titel: "Stroomkring & stroomsterkte",
  korteUitleg: "Gesloten kring, ampère en geleiders vs isolatoren.",
  icoon: "⚡",

  theorie: `
<h3>De stroomkring</h3>
<p>Een <b>stroomkring</b> is een gesloten kring die bestaat uit:</p>
<ul>
  <li>een <b>spanningsbron</b> (batterij of accu)</li>
  <li><b>snoeren / draden</b> die alles verbinden</li>
  <li>een <b>verbruiker</b> (bijv. een lampje of motor)</li>
  <li>(optioneel) een <b>schakelaar</b></li>
</ul>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  Elektrische stroom loopt <b>alleen</b> als de kring <b>gesloten</b> is. Is er ergens een opening (schakelaar open, draad los)? Dan loopt er géén stroom en brandt het lampje niet.
</div>

<h4>Elektrische stroom = bewegende elektronen</h4>
<p>In een metalen geleider zitten <b>vrije elektronen</b>. Een batterij drijft die elektronen rond door de kring — dat noemen we <b>elektrische stroom</b>.</p>

<h3>Schakelsymbolen</h3>
<p>In een <b>schakelschema</b> teken je een stroomkring met vaste symbolen (geen echte tekeningen van de onderdelen). Hieronder zie je de belangrijkste symbolen:</p>

<figure class="bron">
  <svg viewBox="0 0 420 260" width="100%" style="max-width:420px;display:block;margin:0 auto" aria-label="Overzicht schakelsymbolen">
    <!-- Achtergrond -->
    <rect width="420" height="260" rx="10" fill="#f0f7ff" stroke="#3a86ff" stroke-width="1.5"/>

    <!-- Kolomlabels -->
    <text x="70"  y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d3557">Symbool</text>
    <text x="210" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d3557">Naam</text>
    <text x="340" y="22" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d3557">Waarvoor?</text>
    <line x1="10" y1="28" x2="410" y2="28" stroke="#3a86ff" stroke-width="1"/>

    <!-- RIJ 1: Spanningsbron (batterij) -->
    <!-- lang streepje = plus, kort streepje = min -->
    <line x1="30"  y1="52" x2="30"  y2="68" stroke="#222" stroke-width="3"/>
    <line x1="42"  y1="56" x2="42"  y2="64" stroke="#222" stroke-width="1.5"/>
    <line x1="30"  y1="60" x2="10"  y2="60" stroke="#222" stroke-width="1.5"/>
    <line x1="42"  y1="60" x2="62"  y2="60" stroke="#222" stroke-width="1.5"/>
    <text x="36" y="80" text-anchor="middle" font-size="9" fill="#555">+ −</text>
    <text x="210" y="58" text-anchor="middle" font-size="11" fill="#333">Spanningsbron (batterij)</text>
    <text x="340" y="58" text-anchor="middle" font-size="11" fill="#555">Drijft de stroom aan</text>
    <line x1="10" y1="85" x2="410" y2="85" stroke="#ddd" stroke-width="1"/>

    <!-- RIJ 2: Schakelaar -->
    <line x1="10"  y1="110" x2="30"  y2="110" stroke="#222" stroke-width="1.5"/>
    <circle cx="33" cy="110" r="2" fill="#222"/>
    <line x1="33"  y1="110" x2="52"  y2="100" stroke="#222" stroke-width="1.5"/>
    <circle cx="55" cy="110" r="2" fill="#222"/>
    <line x1="55"  y1="110" x2="75"  y2="110" stroke="#222" stroke-width="1.5"/>
    <text x="42" y="127" text-anchor="middle" font-size="9" fill="#555">open</text>
    <text x="210" y="110" text-anchor="middle" font-size="11" fill="#333">Schakelaar</text>
    <text x="340" y="110" text-anchor="middle" font-size="11" fill="#555">Opent/sluit de kring</text>
    <line x1="10" y1="135" x2="410" y2="135" stroke="#ddd" stroke-width="1"/>

    <!-- RIJ 3: Lampje -->
    <circle cx="42" cy="162" r="12" fill="none" stroke="#222" stroke-width="1.5"/>
    <line x1="34" y1="154" x2="50" y2="170" stroke="#222" stroke-width="1.5"/>
    <line x1="50" y1="154" x2="34" y2="170" stroke="#222" stroke-width="1.5"/>
    <line x1="10"  y1="162" x2="30"  y2="162" stroke="#222" stroke-width="1.5"/>
    <line x1="54"  y1="162" x2="74"  y2="162" stroke="#222" stroke-width="1.5"/>
    <text x="210" y="162" text-anchor="middle" font-size="11" fill="#333">Lampje</text>
    <text x="340" y="162" text-anchor="middle" font-size="11" fill="#555">Verbruiker (licht)</text>
    <line x1="10" y1="180" x2="410" y2="180" stroke="#ddd" stroke-width="1"/>

    <!-- RIJ 4: Ampèremeter en Voltmeter naast elkaar -->
    <circle cx="28" cy="210" r="11" fill="none" stroke="#e63946" stroke-width="1.5"/>
    <text x="28" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#e63946">A</text>
    <line x1="10"  y1="210" x2="17"  y2="210" stroke="#222" stroke-width="1.5"/>
    <line x1="39"  y1="210" x2="48"  y2="210" stroke="#222" stroke-width="1.5"/>

    <circle cx="64" cy="210" r="11" fill="none" stroke="#2a9d8f" stroke-width="1.5"/>
    <text x="64" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="#2a9d8f">V</text>
    <line x1="46"  y1="210" x2="53"  y2="210" stroke="#222" stroke-width="1.5"/>
    <line x1="75"  y1="210" x2="84"  y2="210" stroke="#222" stroke-width="1.5"/>

    <text x="210" y="205" text-anchor="middle" font-size="11" fill="#333">Ampèremeter (A) &amp; Voltmeter (V)</text>
    <text x="210" y="220" text-anchor="middle" font-size="10" fill="#555">Meten stroom resp. spanning</text>
    <text x="340" y="210" text-anchor="middle" font-size="11" fill="#555">A in serie · V parallel</text>
  </svg>
  <figcaption>De vijf belangrijkste schakelsymbolen.</figcaption>
</figure>

<h3>Een complete stroomkring (schakelschema)</h3>
<p>Hieronder zie je een schakelschema met een batterij, een schakelaar (gesloten) en een lampje:</p>

<figure class="bron">
  <svg viewBox="0 0 340 220" width="100%" style="max-width:360px;display:block;margin:0 auto" aria-label="Schakelschema: batterij, schakelaar, lampje">
    <!-- Buitenste rechthoek van de kring -->
    <rect x="30" y="30" width="280" height="160" rx="8" fill="none" stroke="#3a86ff" stroke-width="2.5"/>

    <!-- BATTERIJ — linker zijkant, verticaal midden -->
    <!-- verbinding bovenkant naar batterij -->
    <line x1="30" y1="110" x2="50" y2="110" stroke="#3a86ff" stroke-width="2.5"/>
    <!-- lang streepje (+) -->
    <line x1="50" y1="96" x2="50" y2="124" stroke="#1d3557" stroke-width="3.5"/>
    <!-- kort streepje (−) -->
    <line x1="60" y1="102" x2="60" y2="118" stroke="#1d3557" stroke-width="2"/>
    <!-- verbinding batterij naar draad -->
    <line x1="60" y1="110" x2="80" y2="110" stroke="#3a86ff" stroke-width="2.5"/>
    <!-- labels + en − -->
    <text x="50" y="90" text-anchor="middle" font-size="13" fill="#e63946" font-weight="bold">+</text>
    <text x="60" y="90" text-anchor="middle" font-size="13" fill="#555">−</text>
    <text x="55" y="140" text-anchor="middle" font-size="10" fill="#555">batterij</text>

    <!-- SCHAKELAAR — bovenkant, horizontaal midden -->
    <!-- draad naar schakelaar -->
    <line x1="170" y1="30" x2="155" y2="30" stroke="#3a86ff" stroke-width="2.5"/>
    <circle cx="152" cy="30" r="3" fill="#1d3557"/>
    <!-- arm van schakelaar (gesloten = horizontaal) -->
    <line x1="152" y1="30" x2="188" y2="30" stroke="#1d3557" stroke-width="2"/>
    <circle cx="191" cy="30" r="3" fill="#1d3557"/>
    <line x1="191" y1="30" x2="210" y2="30" stroke="#3a86ff" stroke-width="2.5"/>
    <text x="171" y="20" text-anchor="middle" font-size="10" fill="#555">schakelaar (gesloten)</text>

    <!-- LAMPJE — rechterkant, verticaal midden -->
    <circle cx="310" cy="110" r="18" fill="#fffbe6" stroke="#f4a261" stroke-width="2"/>
    <!-- kruis in lampje -->
    <line x1="299" y1="99"  x2="321" y2="121" stroke="#f4a261" stroke-width="2"/>
    <line x1="321" y1="99"  x2="299" y2="121" stroke="#f4a261" stroke-width="2"/>
    <!-- aansluitdraden lampje -->
    <line x1="310" y1="30"  x2="310" y2="92"  stroke="#3a86ff" stroke-width="2.5"/>
    <line x1="310" y1="128" x2="310" y2="190" stroke="#3a86ff" stroke-width="2.5"/>
    <text x="310" y="148" text-anchor="middle" font-size="10" fill="#555">lampje</text>

    <!-- Draad onderkant (sluit de kring) -->
    <line x1="30"  y1="190" x2="310" y2="190" stroke="#3a86ff" stroke-width="2.5"/>

    <!-- Pijltje richting stroom (elektrisch) -->
    <text x="170" y="205" text-anchor="middle" font-size="10" fill="#e63946">→ stroom loopt rechtsom →</text>
  </svg>
  <figcaption>Schakelschema: batterij (links), schakelaar gesloten (boven), lampje (rechts). De kring is gesloten → het lampje brandt.</figcaption>
</figure>

<h3>Stroomsterkte</h3>
<p>De <b>stroomsterkte</b> geeft aan hoeveel elektrische lading er per seconde door een draad stroomt. Hoe groter de stroomsterkte, hoe meer elektronen er per seconde passeren.</p>

<div class="formule-box">
  <span class="formule">symbool: <b>I</b> &nbsp;·&nbsp; eenheid: <b>ampère (A)</b></span>
  <small>1 A = 1000 mA &nbsp;·&nbsp; mA = milliampère</small>
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  De <b>ampèremeter</b> meet de stroomsterkte. Je sluit hem altijd <b>in serie</b> aan — dat wil zeggen: de stroom moet écht door de meter heen lopen.
</div>

<h3>Omrekenen: A ↔ mA</h3>
<table class="nask">
  <tr><th>Van</th><th>Naar</th><th>Wat doe je?</th><th>Voorbeeld</th></tr>
  <tr><td>ampère (A)</td><td>milliampère (mA)</td><td>× 1000</td><td>2,5 A → 2500 mA</td></tr>
  <tr><td>milliampère (mA)</td><td>ampère (A)</td><td>÷ 1000</td><td>750 mA → 0,75 A</td></tr>
</table>

<div class="voorbeeld"><div class="vb-kop">📐 Voorbeeld — omrekenen</div>
  <div class="stap"><b>Gegeven:</b> 3,2 A</div>
  <div class="stap"><b>Gevraagd:</b> hoeveel mA?</div>
  <div class="stap"><b>Berekening:</b> 3,2 × 1000 = 3200 mA</div>
  <div class="stap"><b>Antwoord:</b> 3200 mA</div>
</div>

<h3>Geleiders en isolatoren</h3>
<p>Niet alle stoffen laten stroom door:</p>
<table class="nask">
  <tr><th>Type</th><th>Wat is het?</th><th>Voorbeelden</th></tr>
  <tr><td><b>Geleider</b></td><td>Laat stroom goed door</td><td>Koper, ijzer, aluminium, goud</td></tr>
  <tr><td><b>Isolator</b></td><td>Laat (bijna) geen stroom door</td><td>Plastic, rubber, hout, glas, lucht</td></tr>
</table>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Snoeren bestaan uit een koperen kern (geleider) met een plastic omhulsel (isolator). De isolator beschermt je tegen elektrische schokken.
</div>
`,

  vragen: [
    // ── MEERKEUZE ──────────────────────────────────────────────────────────────

    {
      type: "mc", niveau: 1,
      vraag: "Wat is de eenheid van stroomsterkte?",
      opties: ["volt (V)", "watt (W)", "ampère (A)", "ohm (Ω)"],
      antwoord: 2,
      uitleg: "Stroomsterkte meet je in <b>ampère (A)</b>. Het symbool is <em>I</em>."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Wanneer brandt een lampje in een stroomkring?",
      opties: [
        "Alleen als de schakelaar open is.",
        "Altijd, ongeacht de schakelaar.",
        "Alleen als de kring gesloten is.",
        "Alleen als er twee batterijen zijn."
      ],
      antwoord: 2,
      uitleg: "Elektrische stroom loopt <b>alleen in een gesloten kring</b>. Is de kring open, dan loopt er geen stroom en brandt het lampje niet."
    },

    {
      type: "mc", niveau: 1,
      figuur: `<svg viewBox="0 0 100 80" width="120" style="display:block;margin:8px auto" aria-label="Schakelsymbool lampje">
  <circle cx="50" cy="38" r="20" fill="none" stroke="#f4a261" stroke-width="2.5"/>
  <line x1="36" y1="24" x2="64" y2="52" stroke="#f4a261" stroke-width="2.5"/>
  <line x1="64" y1="24" x2="36" y2="52" stroke="#f4a261" stroke-width="2.5"/>
  <line x1="10"  y1="38" x2="30"  y2="38" stroke="#333" stroke-width="2"/>
  <line x1="70"  y1="38" x2="90"  y2="38" stroke="#333" stroke-width="2"/>
</svg>`,
      vraag: "Welk onderdeel stelt dit schakelsymbool voor?",
      opties: ["Schakelaar", "Voltmeter", "Lampje", "Spanningsbron"],
      antwoord: 2,
      uitleg: "Een cirkel met een kruis (✕) erin is het symbool voor een <b>lampje</b>."
    },

    {
      type: "mc", niveau: 2,
      figuur: `<svg viewBox="0 0 100 60" width="140" style="display:block;margin:8px auto" aria-label="Schakelsymbool batterij">
  <line x1="10" y1="30" x2="38" y2="30" stroke="#333" stroke-width="2"/>
  <line x1="38" y1="16" x2="38" y2="44" stroke="#1d3557" stroke-width="4"/>
  <line x1="50" y1="22" x2="50" y2="38" stroke="#1d3557" stroke-width="2"/>
  <line x1="50" y1="30" x2="90" y2="30" stroke="#333" stroke-width="2"/>
  <text x="38" y="54" text-anchor="middle" font-size="11" fill="#e63946">+</text>
  <text x="50" y="54" text-anchor="middle" font-size="11" fill="#555">−</text>
</svg>`,
      vraag: "Wat stelt dit schakelsymbool voor?",
      opties: ["Lampje", "Schakelaar", "Ampèremeter", "Spanningsbron (batterij)"],
      antwoord: 3,
      uitleg: "Twee streepjes (lang = + en kort = −) naast elkaar is het symbool voor een <b>spanningsbron (batterij)</b>."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Hoe sluit je een ampèremeter aan in een stroomkring?",
      opties: [
        "Parallel — naast het lampje.",
        "In serie — de stroom loopt erdoorheen.",
        "Direct op de plus-pool van de batterij.",
        "Het maakt niet uit, beide manieren werken."
      ],
      antwoord: 1,
      uitleg: "Een ampèremeter sluit je altijd <b>in serie</b> aan. De stroom moet écht door de meter stromen om gemeten te kunnen worden.",
      hint: "Serie = in de kring; parallel = ernaast."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Welk materiaal is een goede geleider van elektrische stroom?",
      opties: ["Hout", "Rubber", "Koper", "Plastic"],
      antwoord: 2,
      uitleg: "<b>Koper</b> is een metaal en geleidt stroom uitstekend. Hout, rubber en plastic zijn isolatoren."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Duru gooit een schakelaar open in een werkende stroomkring. Wat gebeurt er?",
      opties: [
        "De stroom wordt groter.",
        "Er loopt geen stroom meer en het lampje gaat uit.",
        "De batterij laadt op.",
        "Het lampje brandt feller."
      ],
      antwoord: 1,
      uitleg: "Als de schakelaar open gaat, is de kring <b>verbroken</b>. Er loopt geen stroom meer en het lampje gaat uit."
    },

    {
      type: "mc", niveau: 3,
      vraag: "Een stroomkring heeft een stroomsterkte van 450 mA. Hoe groot is dat in ampère?",
      opties: ["4,5 A", "45 A", "0,045 A", "0,45 A"],
      antwoord: 3,
      uitleg: "450 mA ÷ 1000 = <b>0,45 A</b>.",
      hint: "mA → A: deel door 1000."
    },

    // ── WAAR / ONWAAR ──────────────────────────────────────────────────────────

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Een ampèremeter sluit je parallel aan (naast het lampje).",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Een ampèremeter sluit je <b>in serie</b> aan. De stroom moet erdoorheen stromen."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "In een open kring loopt er stroom en brandt het lampje.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> In een open kring is de kring verbroken — er loopt géén stroom en het lampje brandt niet."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Lucht is een isolator.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Lucht geleidt (bijna) geen stroom en is dus een isolator."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "1 ampère is gelijk aan 1000 milliampère.",
      antwoord: true,
      uitleg: "<b>Waar.</b> 1 A = 1000 mA. Het voorvoegsel <em>milli-</em> betekent een duizendste."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Elektrische stroom bestaat uit bewegende elektronen in een geleider.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Vrije elektronen bewegen door de geleider — dat is elektrische stroom."
    },

    // ── INVOER (omrekenen) ─────────────────────────────────────────────────────

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 2,5 A = … mA",
      antwoord: "2500",
      eenheid: "mA",
      uitleg: "2,5 × 1000 = <b>2500 mA</b>.",
      hint: "A → mA: vermenigvuldig met 1000."
    },

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 750 mA = … A",
      antwoord: "0.75|0,75",
      eenheid: "A",
      uitleg: "750 ÷ 1000 = <b>0,75 A</b>.",
      hint: "mA → A: deel door 1000."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een zaklamp verbruikt 0,3 A. Hoeveel milliampère is dat? Reken maar uit, Duru!",
      antwoord: "300",
      eenheid: "mA",
      uitleg: "0,3 × 1000 = <b>300 mA</b>."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een telefoonlader geeft een stroom van 2000 mA. Hoeveel ampère is dat?",
      antwoord: "2",
      eenheid: "A",
      uitleg: "2000 ÷ 1000 = <b>2 A</b>."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een kerstlampje heeft een stroomsterkte van 0,08 A. Reken dit om naar milliampère.",
      antwoord: "80",
      eenheid: "mA",
      uitleg: "0,08 × 1000 = <b>80 mA</b>."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een ampèremeter meet 1250 mA. Schrijf dit op in ampère.",
      antwoord: "1.25|1,25",
      eenheid: "A",
      uitleg: "1250 ÷ 1000 = <b>1,25 A</b>.",
      hint: "mA → A: deel door 1000."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een elektrische fiets heeft een motor die 4,5 A trekt. Hoeveel milliampère is dat?",
      antwoord: "4500",
      eenheid: "mA",
      uitleg: "4,5 × 1000 = <b>4500 mA</b>."
    }
  ]
});
