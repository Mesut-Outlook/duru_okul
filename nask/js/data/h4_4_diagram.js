DURU.register({
  id: "h4-4",
  hoofdstuk: 4,
  paragraaf: "4.4",
  titel: "Snelheid,tijd- en afstand,tijd-diagram",
  korteUitleg: "Grafieken aflezen: steilheid = snelheid, horizontaal = stilstaan.",
  icoon: "📈",

  theorie: `
<h3>Afstand,tijd-diagram</h3>
<p>In een <b>afstand,tijd-diagram</b> staat de <b>tijd</b> op de x-as (horizontaal) en de <b>afstand</b> op de y-as (verticaal). Aan de lijn kun je direct zien hoe snel iemand beweegt.</p>

<figure class="bron">
  <svg viewBox="0 0 420 240" width="100%" style="max-width:420px;display:block;margin:0 auto" aria-label="Afstand,tijd-diagram met vier situaties">
    <!-- raster -->
    <line x1="55" y1="10" x2="55" y2="200" stroke="#ccc" stroke-width="1"/>
    <line x1="55" y1="200" x2="405" y2="200" stroke="#ccc" stroke-width="1"/>
    <!-- rasterlijnen horizontaal -->
    <line x1="55" y1="50"  x2="405" y2="50"  stroke="#eee" stroke-width="1"/>
    <line x1="55" y1="100" x2="405" y2="100" stroke="#eee" stroke-width="1"/>
    <line x1="55" y1="150" x2="405" y2="150" stroke="#eee" stroke-width="1"/>
    <!-- rasterlijnen verticaal -->
    <line x1="130" y1="10" x2="130" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="205" y1="10" x2="205" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="280" y1="10" x2="280" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="355" y1="10" x2="355" y2="200" stroke="#eee" stroke-width="1"/>
    <!-- assen -->
    <line x1="55" y1="10" x2="55" y2="205" stroke="#333" stroke-width="2"/>
    <line x1="50" y1="200" x2="408" y2="200" stroke="#333" stroke-width="2"/>
    <!-- pijlpunten -->
    <polygon points="55,8 51,16 59,16" fill="#333"/>
    <polygon points="410,200 402,196 402,204" fill="#333"/>
    <!-- aslabels -->
    <text x="30" y="106" text-anchor="middle" font-size="11" fill="#555" transform="rotate(-90,30,106)">afstand (m)</text>
    <text x="230" y="220" text-anchor="middle" font-size="11" fill="#555">tijd (s)</text>
    <!-- y-waarden -->
    <text x="48" y="203" text-anchor="end" font-size="10" fill="#555">0</text>
    <text x="48" y="153" text-anchor="end" font-size="10" fill="#555">50</text>
    <text x="48" y="103" text-anchor="end" font-size="10" fill="#555">100</text>
    <text x="48" y="53"  text-anchor="end" font-size="10" fill="#555">150</text>
    <!-- x-waarden -->
    <text x="130" y="213" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="205" y="213" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="280" y="213" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="355" y="213" text-anchor="middle" font-size="10" fill="#555">8</text>
    <!-- lijn A: steile rechte lijn (snel) -->
    <line x1="55" y1="200" x2="205" y2="50" stroke="#e63946" stroke-width="2.5"/>
    <text x="175" y="65" font-size="10" fill="#e63946" font-weight="bold">A: snel</text>
    <!-- lijn B: vlakke rechte lijn (langzaam) -->
    <line x1="55" y1="200" x2="355" y2="100" stroke="#2a9d8f" stroke-width="2.5"/>
    <text x="360" y="97" font-size="10" fill="#2a9d8f" font-weight="bold">B: langzaam</text>
    <!-- lijn C: horizontale lijn (stilstaan) -->
    <line x1="55" y1="150" x2="355" y2="150" stroke="#f4a261" stroke-width="2.5" stroke-dasharray="6,3"/>
    <text x="360" y="147" font-size="10" fill="#f4a261" font-weight="bold">C: stil</text>
  </svg>
  <figcaption>Afstand,tijd-diagram: lijn A (rood) is steiler dan lijn B (groen) → A is sneller. Lijn C (oranje, gestippeld) is horizontaal → stilstaan.</figcaption>
</figure>

<ul>
  <li><b>Steile lijn</b> → beweegt <b>snel</b> (afstand neemt snel toe).</li>
  <li><b>Vlakke lijn</b> → beweegt <b>langzaam</b> (afstand neemt traag toe).</li>
  <li><b>Horizontale lijn</b> → <b>stilstaan</b> (afstand verandert niet).</li>
  <li><b>Rechte lijn</b> → <b>constante snelheid</b> (altijd even snel).</li>
  <li><b>Kromme lijn</b> → <b>veranderende snelheid</b> (versnellen of vertragen).</li>
</ul>

<div class="formule-box">
  <span class="formule">snelheid = afstand : tijd</span>
  <small>v in m/s &nbsp;·&nbsp; afstand in m &nbsp;·&nbsp; tijd in s &nbsp;|&nbsp; de steilheid (helling) van de lijn = de snelheid</small>
</div>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  Hoe <b>steiler</b> de lijn in een afstand,tijd-diagram, hoe <b>groter de snelheid</b>. De snelheid is gelijk aan de <b>helling</b> van de lijn: Δafstand ÷ Δtijd.
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld — Snelheid aflezen uit een afstand,tijd-diagram</div>
  <div class="stap"><b>Situatie:</b> Uit de grafiek lees je af: in 4 s legt een fietser 80 m af.</div>
  <div class="stap"><b>Gegeven:</b> afstand = 80 m &nbsp;|&nbsp; tijd = 4 s</div>
  <div class="stap"><b>Formule:</b> snelheid = afstand : tijd</div>
  <div class="stap"><b>Berekening:</b> 80 : 4 = 20 m/s</div>
  <div class="stap"><b>Antwoord:</b> De fietser rijdt 20 m/s.</div>
</div>

<h3>Snelheid,tijd-diagram</h3>
<p>In een <b>snelheid,tijd-diagram</b> staat de <b>tijd</b> op de x-as en de <b>snelheid</b> op de y-as. Dit diagram laat zien of iemand versnelt, vertraagt of gelijkmatig beweegt.</p>

<figure class="bron">
  <svg viewBox="0 0 420 240" width="100%" style="max-width:420px;display:block;margin:0 auto" aria-label="Snelheid,tijd-diagram met drie situaties">
    <!-- raster -->
    <line x1="55" y1="10" x2="55" y2="200" stroke="#ccc" stroke-width="1"/>
    <line x1="55" y1="200" x2="405" y2="200" stroke="#ccc" stroke-width="1"/>
    <line x1="55" y1="50"  x2="405" y2="50"  stroke="#eee" stroke-width="1"/>
    <line x1="55" y1="100" x2="405" y2="100" stroke="#eee" stroke-width="1"/>
    <line x1="55" y1="150" x2="405" y2="150" stroke="#eee" stroke-width="1"/>
    <line x1="130" y1="10" x2="130" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="205" y1="10" x2="205" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="280" y1="10" x2="280" y2="200" stroke="#eee" stroke-width="1"/>
    <line x1="355" y1="10" x2="355" y2="200" stroke="#eee" stroke-width="1"/>
    <!-- assen -->
    <line x1="55" y1="10" x2="55" y2="205" stroke="#333" stroke-width="2"/>
    <line x1="50" y1="200" x2="408" y2="200" stroke="#333" stroke-width="2"/>
    <polygon points="55,8 51,16 59,16" fill="#333"/>
    <polygon points="410,200 402,196 402,204" fill="#333"/>
    <!-- aslabels -->
    <text x="30" y="106" text-anchor="middle" font-size="11" fill="#555" transform="rotate(-90,30,106)">snelheid (m/s)</text>
    <text x="230" y="220" text-anchor="middle" font-size="11" fill="#555">tijd (s)</text>
    <!-- y-waarden -->
    <text x="48" y="203" text-anchor="end" font-size="10" fill="#555">0</text>
    <text x="48" y="153" text-anchor="end" font-size="10" fill="#555">5</text>
    <text x="48" y="103" text-anchor="end" font-size="10" fill="#555">10</text>
    <text x="48" y="53"  text-anchor="end" font-size="10" fill="#555">15</text>
    <!-- x-waarden -->
    <text x="130" y="213" text-anchor="middle" font-size="10" fill="#555">2</text>
    <text x="205" y="213" text-anchor="middle" font-size="10" fill="#555">4</text>
    <text x="280" y="213" text-anchor="middle" font-size="10" fill="#555">6</text>
    <text x="355" y="213" text-anchor="middle" font-size="10" fill="#555">8</text>
    <!-- lijn A: horizontale lijn (constante snelheid = 10 m/s) -->
    <line x1="55" y1="100" x2="355" y2="100" stroke="#3a86ff" stroke-width="2.5"/>
    <text x="360" y="97" font-size="10" fill="#3a86ff" font-weight="bold">A: constant</text>
    <!-- lijn B: stijgende lijn (versnellen) -->
    <line x1="55" y1="200" x2="355" y2="50" stroke="#e63946" stroke-width="2.5"/>
    <text x="240" y="90" font-size="10" fill="#e63946" font-weight="bold">B: versnellen</text>
    <!-- lijn C: dalende lijn (afremmen) -->
    <line x1="55" y1="50" x2="280" y2="200" stroke="#2a9d8f" stroke-width="2.5"/>
    <text x="75" y="65" font-size="10" fill="#2a9d8f" font-weight="bold">C: afremmen</text>
  </svg>
  <figcaption>Snelheid,tijd-diagram: lijn A (blauw) = constante snelheid; lijn B (rood) = versnellen; lijn C (groen) = afremmen.</figcaption>
</figure>

<ul>
  <li><b>Horizontale lijn</b> → <b>constante snelheid</b> (eenparige beweging).</li>
  <li><b>Stijgende lijn</b> → <b>versnellen</b> (versnelde beweging): snelheid neemt toe.</li>
  <li><b>Dalende lijn</b> → <b>afremmen</b> (vertraagde beweging): snelheid neemt af.</li>
</ul>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Een horizontale lijn in een <b>snelheid,tijd-diagram</b> betekent <b>constante snelheid</b> (NIET stilstaan!). Stilstaan is een horizontale lijn op snelheid = 0.
</div>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Let altijd eerst op de <b>aslabels</b>! Is de y-as "afstand" of "snelheid"? Dat bepaalt wat de lijn betekent.
</div>
`,

  vragen: [

    // ── NIVEAU 1 — afstand,tijd basisregels ────────────────────────────────────

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "In een afstand,tijd-diagram staat de tijd op de x-as (horizontaal).",
      antwoord: true,
      uitleg: "Waar. De <b>tijd</b> staat altijd op de x-as, de <b>afstand</b> op de y-as."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat betekent een horizontale lijn in een afstand,tijd-diagram?",
      opties: [
        "De persoon beweegt met constante snelheid.",
        "De persoon staat stil.",
        "De persoon versnelt.",
        "De persoon remt af."
      ],
      antwoord: 1,
      uitleg: "Een <b>horizontale lijn</b> in een afstand,tijd-diagram betekent dat de afstand niet verandert → de persoon staat <b>stil</b>."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Welke lijn hoort bij de snelste beweging in een afstand,tijd-diagram?",
      figuur: `<svg viewBox="0 0 300 200" width="100%" style="max-width:300px;display:block;margin:0 auto">
  <line x1="40" y1="10" x2="40" y2="175" stroke="#333" stroke-width="2"/>
  <line x1="35" y1="170" x2="285" y2="170" stroke="#333" stroke-width="2"/>
  <text x="162" y="190" text-anchor="middle" font-size="11" fill="#555">tijd (s)</text>
  <text x="18" y="90" text-anchor="middle" font-size="11" fill="#555" transform="rotate(-90,18,90)">afstand (m)</text>
  <line x1="40" y1="170" x2="200" y2="30"  stroke="#e63946" stroke-width="2.5"/>
  <text x="175" y="25" font-size="11" fill="#e63946" font-weight="bold">A</text>
  <line x1="40" y1="170" x2="270" y2="60"  stroke="#3a86ff" stroke-width="2.5"/>
  <text x="272" y="57" font-size="11" fill="#3a86ff" font-weight="bold">B</text>
  <line x1="40" y1="170" x2="270" y2="110" stroke="#2a9d8f" stroke-width="2.5"/>
  <text x="272" y="107" font-size="11" fill="#2a9d8f" font-weight="bold">C</text>
</svg>`,
      opties: ["Lijn A (rood)", "Lijn B (blauw)", "Lijn C (groen)", "Alle lijnen zijn even snel"],
      antwoord: 0,
      uitleg: "Lijn A is het <b>steilst</b>: bij dezelfde tijdsduur legt lijn A de meeste afstand af. Steiler = sneller in een afstand,tijd-diagram."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Een rechte lijn in een afstand,tijd-diagram betekent dat de snelheid steeds verandert.",
      antwoord: false,
      uitleg: "Onwaar. Een <b>rechte</b> lijn betekent <b>constante snelheid</b>. Een <b>kromme</b> lijn betekent veranderende snelheid."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat betekent een horizontale lijn in een snelheid,tijd-diagram?",
      opties: [
        "De persoon staat stil.",
        "De persoon versnelt.",
        "De persoon beweegt met constante snelheid.",
        "De persoon remt af."
      ],
      antwoord: 2,
      uitleg: "In een <b>snelheid,tijd-diagram</b> betekent een horizontale lijn dat de snelheid <b>niet verandert</b> → constante snelheid (eenparige beweging)."
    },

    // ── NIVEAU 1 — snelheid aflezen en berekenen ───────────────────────────────

    {
      type: "invoer",
      niveau: 1,
      vraag: "Uit een afstand,tijd-grafiek lees je af: in 5 s legt een fietser 50 m af. Bereken de snelheid.",
      antwoord: "10",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 50 : 5 = <b>10 m/s</b>.",
      hint: "Gebruik snelheid = afstand : tijd."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Uit een grafiek lees je af: in 4 s legt een loper 20 m af. Wat is zijn snelheid?",
      antwoord: "5",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 20 : 4 = <b>5 m/s</b>.",
      hint: "snelheid = afstand : tijd"
    },

    // ── NIVEAU 2 ────────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 2,
      vraag: "Wat voor beweging hoort bij deze snelheid,tijd-grafiek?",
      figuur: `<svg viewBox="0 0 300 200" width="100%" style="max-width:300px;display:block;margin:0 auto">
  <line x1="40" y1="10" x2="40" y2="175" stroke="#333" stroke-width="2"/>
  <line x1="35" y1="170" x2="285" y2="170" stroke="#333" stroke-width="2"/>
  <polygon points="40,8 36,16 44,16" fill="#333"/>
  <polygon points="287,170 279,166 279,174" fill="#333"/>
  <text x="162" y="190" text-anchor="middle" font-size="11" fill="#555">tijd (s)</text>
  <text x="18" y="90" text-anchor="middle" font-size="11" fill="#555" transform="rotate(-90,18,90)">snelheid (m/s)</text>
  <!-- stijgende lijn: versnellen -->
  <line x1="40" y1="170" x2="270" y2="40" stroke="#e63946" stroke-width="3"/>
</svg>`,
      opties: [
        "Constante snelheid (eenparige beweging)",
        "Versnelde beweging (versnellen)",
        "Vertraagde beweging (afremmen)",
        "Stilstaan"
      ],
      antwoord: 1,
      uitleg: "De lijn <b>stijgt</b> → de snelheid neemt toe → dit is een <b>versnelde beweging</b>.",
      hint: "Let op de richting van de lijn: stijgt hij of daalt hij?"
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Welke grafiek hoort bij 'iemand remt af tot stilstand'?",
      figuur: `<svg viewBox="0 0 320 220" width="100%" style="max-width:320px;display:block;margin:0 auto">
  <!-- grafiek A -->
  <text x="75" y="18" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">A</text>
  <line x1="15" y1="20" x2="15" y2="110" stroke="#333" stroke-width="1.5"/>
  <line x1="10" y1="105" x2="140" y2="105" stroke="#333" stroke-width="1.5"/>
  <text x="75" y="116" text-anchor="middle" font-size="9" fill="#888">tijd (s)</text>
  <text x="6" y="65" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,6,65)">v</text>
  <line x1="15" y1="40" x2="135" y2="105" stroke="#3a86ff" stroke-width="2.5"/>
  <!-- grafiek B -->
  <text x="235" y="18" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">B</text>
  <line x1="175" y1="20" x2="175" y2="110" stroke="#333" stroke-width="1.5"/>
  <line x1="170" y1="105" x2="300" y2="105" stroke="#333" stroke-width="1.5"/>
  <text x="235" y="116" text-anchor="middle" font-size="9" fill="#888">tijd (s)</text>
  <text x="166" y="65" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,166,65)">v</text>
  <line x1="175" y1="105" x2="295" y2="40" stroke="#e63946" stroke-width="2.5"/>
  <!-- grafiek C -->
  <text x="75" y="135" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">C</text>
  <line x1="15" y1="137" x2="15" y2="215" stroke="#333" stroke-width="1.5"/>
  <line x1="10" y1="210" x2="140" y2="210" stroke="#333" stroke-width="1.5"/>
  <text x="75" y="220" text-anchor="middle" font-size="9" fill="#888">tijd (s)</text>
  <text x="6" y="175" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,6,175)">v</text>
  <line x1="15" y1="165" x2="135" y2="165" stroke="#2a9d8f" stroke-width="2.5"/>
  <!-- grafiek D -->
  <text x="235" y="135" text-anchor="middle" font-size="11" fill="#333" font-weight="bold">D</text>
  <line x1="175" y1="137" x2="175" y2="215" stroke="#333" stroke-width="1.5"/>
  <line x1="170" y1="210" x2="300" y2="210" stroke="#333" stroke-width="1.5"/>
  <text x="235" y="220" text-anchor="middle" font-size="9" fill="#888">tijd (s)</text>
  <text x="166" y="175" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,166,175)">v</text>
  <line x1="175" y1="137" x2="175" y2="210" stroke="#f4a261" stroke-width="2.5"/>
  <line x1="175" y1="210" x2="295" y2="210" stroke="#f4a261" stroke-width="2.5"/>
</svg>`,
      opties: ["Grafiek A", "Grafiek B", "Grafiek C", "Grafiek D"],
      antwoord: 0,
      uitleg: "Bij afremmen tot stilstand <b>daalt</b> de snelheid van een waarde naar 0. Dat is grafiek A: een dalende lijn die de x-as raakt.",
      hint: "Afremmen = snelheid neemt af. Zoek de dalende lijn die op 0 eindigt."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Bekijk de grafiek. Na 6 s heeft een auto 90 m afgelegd (rechte lijn vanuit 0). Bereken de snelheid van de auto.",
      figuur: `<svg viewBox="0 0 300 200" width="100%" style="max-width:300px;display:block;margin:0 auto">
  <line x1="45" y1="10" x2="45" y2="170" stroke="#333" stroke-width="2"/>
  <line x1="40" y1="165" x2="280" y2="165" stroke="#333" stroke-width="2"/>
  <polygon points="45,8 41,16 49,16" fill="#333"/>
  <polygon points="282,165 274,161 274,169" fill="#333"/>
  <!-- raster -->
  <line x1="45" y1="57"  x2="280" y2="57"  stroke="#eee" stroke-width="1"/>
  <line x1="45" y1="111" x2="280" y2="111" stroke="#eee" stroke-width="1"/>
  <line x1="123" y1="10" x2="123" y2="165" stroke="#eee" stroke-width="1"/>
  <line x1="201" y1="10" x2="201" y2="165" stroke="#eee" stroke-width="1"/>
  <line x1="240" y1="10" x2="240" y2="165" stroke="#eee" stroke-width="1"/>
  <!-- aslabels -->
  <text x="162" y="183" text-anchor="middle" font-size="10" fill="#555">tijd (s)</text>
  <text x="20" y="90" text-anchor="middle" font-size="10" fill="#555" transform="rotate(-90,20,90)">afstand (m)</text>
  <!-- y-waarden -->
  <text x="38" y="168" text-anchor="end" font-size="9" fill="#555">0</text>
  <text x="38" y="114" text-anchor="end" font-size="9" fill="#555">30</text>
  <text x="38" y="60"  text-anchor="end" font-size="9" fill="#555">60</text>
  <text x="38" y="14"  text-anchor="end" font-size="9" fill="#555">90</text>
  <!-- x-waarden -->
  <text x="123" y="178" text-anchor="middle" font-size="9" fill="#555">2</text>
  <text x="201" y="178" text-anchor="middle" font-size="9" fill="#555">4</text>
  <text x="240" y="178" text-anchor="middle" font-size="9" fill="#555">6</text>
  <!-- de lijn -->
  <line x1="45" y1="165" x2="240" y2="11" stroke="#e63946" stroke-width="2.5"/>
  <!-- punt markering -->
  <circle cx="240" cy="11" r="4" fill="#e63946"/>
  <text x="248" y="16" font-size="9" fill="#e63946">(6 s, 90 m)</text>
</svg>`,
      antwoord: "15",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 90 : 6 = <b>15 m/s</b>. Je leest de punten af uit de grafiek en berekent dan de helling.",
      hint: "Lees af: na 6 s is de afstand 90 m. Gebruik snelheid = afstand : tijd."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Uit een afstand,tijd-grafiek lees je af: in 8 s legt een skater 120 m af (rechte lijn). Bereken de snelheid.",
      antwoord: "15",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 120 : 8 = <b>15 m/s</b>.",
      hint: "snelheid = afstand : tijd"
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een snelheid,tijd-diagram betekent een stijgende lijn dat het voorwerp versnelt.",
      antwoord: true,
      uitleg: "Waar. Als de lijn <b>stijgt</b> neemt de snelheid toe → het voorwerp <b>versnelt</b>."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Welke grafiek hoort bij 'een auto rijdt met constante snelheid, daarna remt hij af'?",
      figuur: `<svg viewBox="0 0 320 130" width="100%" style="max-width:320px;display:block;margin:0 auto">
  <!-- grafiek A -->
  <text x="75" y="14" text-anchor="middle" font-size="10" fill="#333" font-weight="bold">A</text>
  <line x1="15" y1="18" x2="15" y2="115" stroke="#333" stroke-width="1.5"/>
  <line x1="10" y1="110" x2="145" y2="110" stroke="#333" stroke-width="1.5"/>
  <text x="6" y="65" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,6,65)">v</text>
  <!-- horizontaal dan dalend -->
  <line x1="15" y1="45" x2="80"  y2="45"  stroke="#3a86ff" stroke-width="2.5"/>
  <line x1="80" y1="45" x2="135" y2="110" stroke="#3a86ff" stroke-width="2.5"/>
  <!-- grafiek B -->
  <text x="235" y="14" text-anchor="middle" font-size="10" fill="#333" font-weight="bold">B</text>
  <line x1="175" y1="18" x2="175" y2="115" stroke="#333" stroke-width="1.5"/>
  <line x1="170" y1="110" x2="305" y2="110" stroke="#333" stroke-width="1.5"/>
  <text x="166" y="65" text-anchor="middle" font-size="9" fill="#888" transform="rotate(-90,166,65)">v</text>
  <!-- stijgend dan horizontaal -->
  <line x1="175" y1="110" x2="230" y2="45"  stroke="#e63946" stroke-width="2.5"/>
  <line x1="230" y1="45"  x2="295" y2="45"  stroke="#e63946" stroke-width="2.5"/>
</svg>`,
      opties: [
        "Grafiek A (blauw)",
        "Grafiek B (rood)",
        "Geen van beide",
        "Beide grafieken"
      ],
      antwoord: 0,
      uitleg: "Grafiek A: eerst een <b>horizontale lijn</b> (constante snelheid) dan een <b>dalende lijn</b> (afremmen). Dat klopt precies met de beschrijving.",
      hint: "Constante snelheid = horizontale lijn; afremmen = dalende lijn in een snelheid,tijd-diagram."
    },

    // ── NIVEAU 3 ────────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "In een afstand,tijd-grafiek loopt een rechte lijn van (0 s, 0 m) naar (10 s, 250 m). Bereken de snelheid. Reken maar uit, Duru!",
      antwoord: "25",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 250 : 10 = <b>25 m/s</b>. De helling van de lijn geeft direct de snelheid.",
      hint: "Gebruik de eindpunten van de lijn: afstand = 250 m, tijd = 10 s."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Een grafiek toont een rechte lijn van (2 s, 10 m) naar (6 s, 50 m). Bereken de snelheid uit de helling van deze lijn.",
      antwoord: "10",
      eenheid: "m/s",
      tolerantie: 0.1,
      uitleg: "Helling = Δafstand ÷ Δtijd = (50 − 10) ÷ (6 − 2) = 40 ÷ 4 = <b>10 m/s</b>. Let op: je trekt de beginwaarden van de eindwaarden af.",
      hint: "Helling = (afstand₂ − afstand₁) ÷ (tijd₂ − tijd₁). Gebruik de twee gegeven punten."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Een leerling zegt: 'In mijn snelheid,tijd-diagram heb ik een horizontale lijn op v = 0. Dat betekent dat het object beweegt.' Klopt dit?",
      opties: [
        "Ja, want het object heeft snelheid.",
        "Nee, v = 0 betekent stilstaan.",
        "Ja, want de lijn is horizontaal.",
        "Nee, maar alleen als de lijn stijgt daarna."
      ],
      antwoord: 1,
      uitleg: "<b>Nee</b>. Een horizontale lijn op v = 0 betekent dat de snelheid <b>nul</b> is → het object staat <b>stil</b>. Pas als de lijn omhoog gaat, begint het object te bewegen.",
      hint: "Wat betekent v = 0 voor de snelheid?"
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Een trein heeft een afstand,tijd-grafiek met een rechte lijn. Na 0 s staat hij op 0 m, na 12 s staat hij op 360 m. Bereken zijn snelheid.",
      antwoord: "30",
      eenheid: "m/s",
      uitleg: "snelheid = afstand : tijd = 360 : 12 = <b>30 m/s</b>. Een rechte lijn door de oorsprong → constante snelheid gelijk aan de helling.",
      hint: "snelheid = afstand : tijd. Gebruik de eindwaarden uit de grafiek."
    }

  ]
});
