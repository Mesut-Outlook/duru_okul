DURU.register({
  id: "h6-1",
  hoofdstuk: 6,
  paragraaf: "6.1",
  titel: "Spanning & spanningsbronnen",
  korteUitleg: "Spanning (U) in volt, spanningsbronnen en hoe je een voltmeter aansluit.",
  icoon: "🔋",

  theorie: `
<h3>Wat is spanning?</h3>
<p>Een <b>spanningsbron</b> zorgt ervoor dat er stroom door een schakeling kan lopen. De spanningsbron levert <b>elektrische spanning</b>. Zonder spanning geen stroom, en zonder stroom geen licht, warmte of beweging.</p>

<h4>Voorbeelden van spanningsbronnen</h4>
<ul>
  <li>🔋 Gewone <b>batterij</b> (wegwerpbatterij) — bijv. in een zaklamp of afstandsbediening</li>
  <li>🔋 <b>Accu</b> (oplaadbare batterij) — bijv. in een smartphone of laptop</li>
  <li>🚗 <b>Auto-accu</b> — de accu onder de motorkap van een auto</li>
  <li>🔌 <b>Stopcontact (lichtnet)</b> — de stroom uit de muur thuis</li>
  <li>🚲 <b>Dynamo</b> — zit op een fiets; draait de wiel, dan maakt hij spanning</li>
  <li>☀️ <b>Zonnecel</b> (zonnepaneel) — zet zonlicht om in elektrische spanning</li>
</ul>

<h4>Het symbool: U en volt</h4>
<div class="formule-box">
  <span class="formule">Symbool: U &nbsp;|&nbsp; Eenheid: volt (V)</span>
  <small>U staat voor spanning · volt (V) is de meeteenheid</small>
</div>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  Het symbool voor spanning is <b>U</b>. De eenheid is <b>volt</b>, afgekort <b>V</b>. Dus: U = 1,5 V betekent "de spanning is 1,5 volt".
</div>

<h4>Bekende spanningswaarden</h4>
<table class="nask">
  <tr><th>Spanningsbron</th><th>Spanning</th></tr>
  <tr><td>Gewone batterij (AA, AAA)</td><td>1,5 V</td></tr>
  <tr><td>Knoopcel (horloge)</td><td>1,5 V of 3 V</td></tr>
  <tr><td>Oplaadbare batterij (accu)</td><td>verschilt (bijv. 1,2 V of 3,7 V)</td></tr>
  <tr><td>Auto-accu</td><td>12 V</td></tr>
  <tr><td>Stopcontact / lichtnet (thuis)</td><td>230 V</td></tr>
  <tr><td>Adapter (lader) voor apparaten</td><td>bijv. 5 V, 9 V of 12 V</td></tr>
</table>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  De spanning uit het stopcontact is <b>230 V</b>. Dat is gevaarlijk hoog! Kom nooit aan losse draden in een stopcontact.
</div>

<h3>De voltmeter</h3>
<p>Spanning meet je met een <b>voltmeter</b> (ook wel: spanningsmeter). De voltmeter meet in <b>volt (V)</b>.</p>

<h4>Symbool van de voltmeter</h4>
<figure class="bron">
  <svg viewBox="0 0 120 120" width="120" style="display:block;margin:0 auto" aria-label="Symbool voltmeter: cirkel met V erin">
    <circle cx="60" cy="60" r="48" fill="#fffbe6" stroke="#f4a11d" stroke-width="3"/>
    <text x="60" y="75" text-anchor="middle" font-size="44" font-weight="bold" fill="#e06000" font-family="serif">V</text>
  </svg>
  <figcaption>Symbool van de voltmeter: een cirkel met de letter V erin.</figcaption>
</figure>

<h4>Hoe sluit je een voltmeter aan?</h4>
<p>Een voltmeter sluit je altijd <b>parallel</b> aan — dat wil zeggen: <em>naast</em> (over) het onderdeel waarvan je de spanning wilt meten. Je sluit hem <b>niet</b> in serie aan!</p>

<figure class="bron">
  <svg viewBox="0 0 420 240" width="100%" style="max-width:420px;display:block;margin:0 auto" aria-label="Schakeling met batterij, lampje en voltmeter parallel">
    <!-- Achtergrond -->
    <rect width="420" height="240" fill="#f8faff" rx="10"/>

    <!-- Hoofdcircuit: rechthoek -->
    <!-- Bovenste draad -->
    <line x1="40" y1="50" x2="380" y2="50" stroke="#333" stroke-width="2.5"/>
    <!-- Linkse draad -->
    <line x1="40" y1="50" x2="40" y2="190" stroke="#333" stroke-width="2.5"/>
    <!-- Rechtse draad -->
    <line x1="380" y1="50" x2="380" y2="190" stroke="#333" stroke-width="2.5"/>
    <!-- Onderste draad (links van lampje) -->
    <line x1="40" y1="190" x2="160" y2="190" stroke="#333" stroke-width="2.5"/>
    <!-- Onderste draad (rechts van lampje) -->
    <line x1="260" y1="190" x2="380" y2="190" stroke="#333" stroke-width="2.5"/>

    <!-- Batterij (links, verticaal, op de linkse draad) -->
    <line x1="40" y1="95" x2="40" y2="105" stroke="#333" stroke-width="1"/>
    <!-- lange streep = plus -->
    <line x1="22" y1="95" x2="58" y2="95" stroke="#e63946" stroke-width="4"/>
    <!-- korte streep = min -->
    <line x1="29" y1="110" x2="51" y2="110" stroke="#1d3557" stroke-width="3"/>
    <text x="64" y="100" font-size="11" fill="#e63946" font-weight="bold">+</text>
    <text x="64" y="115" font-size="11" fill="#1d3557" font-weight="bold">−</text>
    <text x="14" y="135" font-size="11" fill="#555" text-anchor="middle">batterij</text>

    <!-- Lampje (midden onderin, cirkel met kruis) -->
    <circle cx="210" cy="190" r="28" fill="#fffbe6" stroke="#f4a11d" stroke-width="2.5"/>
    <line x1="190" y1="170" x2="230" y2="210" stroke="#f4a11d" stroke-width="2"/>
    <line x1="230" y1="170" x2="190" y2="210" stroke="#f4a11d" stroke-width="2"/>
    <text x="210" y="232" text-anchor="middle" font-size="11" fill="#555">lampje</text>

    <!-- Voltmeter parallel over lampje: draad omhoog van knooppunten -->
    <!-- Linker aansluiting voltmeter (van x=160,y=190 omhoog naar y=135, dan naar 260,y=135) -->
    <line x1="160" y1="190" x2="160" y2="135" stroke="#3a86ff" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="160" y1="135" x2="260" y2="135" stroke="#3a86ff" stroke-width="2" stroke-dasharray="5,3"/>
    <line x1="260" y1="135" x2="260" y2="190" stroke="#3a86ff" stroke-width="2" stroke-dasharray="5,3"/>

    <!-- Voltmeter symbool (cirkel met V) op de paralleltak -->
    <circle cx="210" cy="120" r="22" fill="#e8f4ff" stroke="#3a86ff" stroke-width="2.5"/>
    <text x="210" y="128" text-anchor="middle" font-size="20" font-weight="bold" fill="#0056b3" font-family="serif">V</text>

    <!-- Label voltmeter -->
    <text x="210" y="94" text-anchor="middle" font-size="11" fill="#0056b3" font-weight="bold">voltmeter</text>
    <text x="210" y="107" text-anchor="middle" font-size="10" fill="#0056b3">(parallel)</text>
  </svg>
  <figcaption>De voltmeter (V, blauw gestippeld) staat <b>parallel</b> over het lampje — niet in serie in de hoofddraad.</figcaption>
</figure>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Onthoud: voltmeter = <b>parallel</b>. Je sluit hem over (naast) het onderdeel aan, nooit erdoorheen (in serie). Een ampèremeter (strooммeter) sluit je wél in serie aan — maar dat is een andere paragraaf!
</div>

<h4>Meetbereik instellen en aflezen</h4>
<p>Een analoge voltmeter heeft verschillende <b>meetbereiken</b>, bijv. 3 V, 15 V en 30 V. Kies altijd het bereik dat net boven de te verwachten spanning ligt. Lees daarna de juiste schaal af.</p>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld — Meetbereik aflezen</div>
  <div class="stap"><b>Situatie:</b> Je meet de spanning van een gewone batterij (± 1,5 V). Je stelt de voltmeter in op het 3 V-bereik.</div>
  <div class="stap"><b>Schaal:</b> Als de wijzer tot halverwege staat op de 3 V-schaal, lees je af: 1,5 V.</div>
  <div class="stap"><b>Antwoord:</b> U = 1,5 V.</div>
</div>
`,

  vragen: [

    // ── NIVEAU 1 ──────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van elektrische spanning?",
      opties: ["ampère (A)", "watt (W)", "volt (V)", "ohm (Ω)"],
      antwoord: 2,
      uitleg: "Spanning meet je in <b>volt (V)</b>. Het symbool voor spanning is U."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Welk symbool gebruik je voor elektrische spanning?",
      opties: ["I", "R", "P", "U"],
      antwoord: 3,
      uitleg: "Het symbool voor spanning is <b>U</b>. De eenheid is volt (V)."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Welke van deze vier is een spanningsbron?",
      opties: ["Een weerstand", "Een lampje", "Een batterij", "Een schakelaar"],
      antwoord: 2,
      uitleg: "Een <b>batterij</b> levert elektrische spanning. Een weerstand, lampje en schakelaar zijn verbruikers of schakelaars, geen bronnen."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Hoeveel volt levert een gewone AA-batterij?",
      opties: ["12 V", "230 V", "9 V", "1,5 V"],
      antwoord: 3,
      uitleg: "Een gewone AA- of AAA-batterij levert <b>1,5 V</b>."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Een dynamo op een fiets is een spanningsbron.",
      antwoord: true,
      uitleg: "Waar. Een dynamo zet bewegingsenergie om in elektrische spanning — het is dus een spanningsbron."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Een voltmeter sluit je in serie aan in de schakeling.",
      antwoord: false,
      uitleg: "Onwaar! Een voltmeter sluit je altijd <b>parallel</b> aan — naast (over) het onderdeel waarvan je de spanning meet."
    },

    // ── NIVEAU 2 ──────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 2,
      vraag: "Hoeveel volt heeft het stopcontact (lichtnet) in huis?",
      opties: ["12 V", "24 V", "110 V", "230 V"],
      antwoord: 3,
      uitleg: "Het Nederlandse lichtnet (stopcontact) levert <b>230 V</b>. Dit is gevaarlijk hoog!"
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Hoeveel volt levert een auto-accu?",
      opties: ["1,5 V", "12 V", "230 V", "9 V"],
      antwoord: 1,
      uitleg: "Een auto-accu levert <b>12 V</b>. Dit is veel meer dan een gewone batterij, maar veel minder dan het lichtnet."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een voltmeter meet de spanning in ampère (A).",
      antwoord: false,
      uitleg: "Onwaar. Een voltmeter meet spanning in <b>volt (V)</b>, niet in ampère. Ampère is de eenheid van elektrische stroom."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een zonnecel kan als spanningsbron dienen.",
      antwoord: true,
      uitleg: "Waar. Een zonnecel (zonnepaneel) zet zonlicht om in elektrische spanning — het is een spanningsbron."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Duru heeft 4 gewone batterijen (elk 1,5 V) in serie (achter elkaar) geschakeld. Bereken de totale spanning.",
      antwoord: "6",
      eenheid: "V",
      uitleg: "Batterijen in serie tel je op: 4 × 1,5 V = <b>6 V</b>.",
      hint: "Tel de spanningen van alle batterijen bij elkaar op."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een adapter voor een tablet heeft een spanning van 9 V. Hoeveel volt is de spanning van het stopcontact (230 V) <em>meer</em> dan die van de adapter?",
      antwoord: "221",
      eenheid: "V",
      uitleg: "230 V − 9 V = <b>221 V</b>. Het stopcontact levert veel meer spanning dan de adapter."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Hoe sluit je een voltmeter aan om de spanning over een lampje te meten?",
      opties: [
        "In serie: achter het lampje in de draad",
        "Parallel: naast het lampje (over de aansluitpunten van het lampje)",
        "Parallel: naast de batterij",
        "Het maakt niet uit hoe je hem aansluit"
      ],
      antwoord: 1,
      uitleg: "De voltmeter sluit je <b>parallel over het lampje</b> aan — dat wil zeggen: tussen de twee aansluitpunten van het lampje. Zo meet je precies de spanning over dat lampje."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een voltmeter staat ingesteld op het 3 V-bereik. De wijzer staat op precies ¾ van de schaal. Wat is de afgelezen spanning?",
      antwoord: "2.25|2,25",
      eenheid: "V",
      tolerantie: 0.05,
      uitleg: "¾ van 3 V = 0,75 × 3 = <b>2,25 V</b>.",
      hint: "Bereken ¾ van het maximale meetbereik (3 V)."
    },

    // ── NIVEAU 3 ──────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Reken maar uit, Duru! Je hebt 8 batterijen van elk 1,5 V in serie. Hoeveel volt is de totale spanning?",
      antwoord: "12",
      eenheid: "V",
      uitleg: "8 × 1,5 V = <b>12 V</b>. Dat is precies de spanning van een auto-accu!",
      hint: "Tel alle spanningen op: aantal × spanning per batterij."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Een voltmeter staat op het 15 V-bereik. De wijzer staat op 2/5 van de schaal. Wat is de afgelezen spanning?",
      antwoord: "6",
      eenheid: "V",
      uitleg: "2/5 van 15 V = 0,4 × 15 = <b>6 V</b>.",
      hint: "Bereken 2/5 van het maximale meetbereik (15 V)."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Je wilt de spanning over een lampje meten met een voltmeter. Het meetbereik van je voltmeter is instelbaar op 3 V, 15 V of 30 V. Je verwacht een spanning van ongeveer 4,5 V. Welk bereik kies je?",
      opties: ["3 V — want dat is het dichtst bij 4,5 V", "15 V — want dit bereik is net groter dan 4,5 V", "30 V — want dan kun je altijd meten", "Het maakt niet uit welk bereik je kiest"],
      antwoord: 1,
      uitleg: "Je kiest altijd het bereik dat <b>net boven</b> de te verwachten spanning ligt. 3 V is te klein (4,5 V past niet), 30 V is onnodig groot (je leest minder nauwkeurig af). <b>15 V</b> is correct.",
      hint: "Kies het kleinst mogelijke bereik waarbij de te meten spanning nog past."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Als je twee batterijen van 1,5 V parallel aansluit (naast elkaar), is de totale spanning 3 V.",
      antwoord: false,
      uitleg: "Onwaar. Bij <b>parallelle</b> schakeling van batterijen blijft de spanning <b>1,5 V</b>. De spanning telt alleen op bij <em>serie</em>schakeling. Parallel verdubbelt de capaciteit (hoe lang ze meegaan), niet de spanning."
    }

  ]
});
