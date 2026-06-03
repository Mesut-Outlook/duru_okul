DURU.register({
  id: "h8-2",
  hoofdstuk: 8,
  paragraaf: "8.2",
  titel: "De balans",
  korteUitleg: "Vergelijkingen oplossen met behulp van een balansmodel.",
  icoon: "⚖️",

  theorie: `
<h3>De balans als vergelijking</h3>
<p>Stel je een <b>weegschaal (balans)</b> voor. Als beide kanten even zwaar zijn, is de balans <b>in evenwicht</b>. Een vergelijking is precies zo: de linkerkant is altijd gelijk aan de rechterkant.</p>

<div class="formule-box">
  <span class="formule">linkerkant = rechterkant</span>
  <small>Wat je aan één kant doet, moet je ook aan de andere kant doen!</small>
</div>

<figure class="bron">
  <svg viewBox="0 0 380 180" width="100%" style="max-width:400px;display:block;margin:0 auto" aria-label="Balansschema met 5x + 3 = 18">
    <!-- balk -->
    <rect x="60" y="80" width="260" height="8" rx="4" fill="#3a86ff"/>
    <!-- middelste paal -->
    <rect x="186" y="85" width="8" height="60" fill="#555"/>
    <!-- voet -->
    <ellipse cx="190" cy="148" rx="30" ry="8" fill="#888"/>
    <!-- links schaaltje -->
    <line x1="100" y1="84" x2="100" y2="110" stroke="#555" stroke-width="2"/>
    <ellipse cx="100" cy="118" rx="40" ry="10" fill="#ffd166" stroke="#e9a100" stroke-width="1.5"/>
    <!-- rechts schaaltje -->
    <line x1="280" y1="84" x2="280" y2="110" stroke="#555" stroke-width="2"/>
    <ellipse cx="280" cy="118" rx="40" ry="10" fill="#ffd166" stroke="#e9a100" stroke-width="1.5"/>
    <!-- labels -->
    <text x="100" y="114" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d3557">5x + 3</text>
    <text x="280" y="114" text-anchor="middle" font-size="13" font-weight="bold" fill="#1d3557">18</text>
    <text x="190" y="172" text-anchor="middle" font-size="11" fill="#555">in evenwicht</text>
  </svg>
  <figcaption>De balans stelt de vergelijking 5x + 3 = 18 voor.</figcaption>
</figure>

<h3>Van beide kanten hetzelfde afhalen</h3>
<p>Om de onbekende <b>x</b> te vinden, haal je van <b>beide kanten</b> hetzelfde af (of tel je er hetzelfde bij op). Zo blijft de balans in evenwicht.</p>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Balans: 5x + 3 = 18</div>
  <div class="stap"><b>Vergelijking:</b> 5x + 3 = 18</div>
  <div class="stap"><b>Stap 1:</b> Haal van beide kanten 3 af:<br>5x + 3 − 3 = 18 − 3 → <b>5x = 15</b></div>
  <div class="stap"><b>Stap 2:</b> Er zijn 5 gelijke x-gewichten samen 15. Eén x is:<br>x = 15 : 5 = <b>3</b></div>
  <div class="stap"><b>Antwoord:</b> x = 3</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Balans: 3y + 6 = 24</div>
  <div class="stap"><b>Vergelijking:</b> 3y + 6 = 24</div>
  <div class="stap"><b>Stap 1:</b> Haal van beide kanten 6 af:<br>3y + 6 − 6 = 24 − 6 → <b>3y = 18</b></div>
  <div class="stap"><b>Stap 2:</b> Deel beide kanten door 3:<br>y = 18 : 3 = <b>6</b></div>
  <div class="stap"><b>Antwoord:</b> y = 6</div>
</div>

<div class="info-box teal"><span class="kop">💡 Onthoud</span>
  <b>De gouden regel:</b> Wat je aan één kant van de balans doet, moet je ook aan de andere kant doen. Alleen dan blijft de balans in evenwicht!
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Vergeet niet om na het oplossen te <b>controleren</b>: vul je antwoord in de oorspronkelijke vergelijking in. Als beide kanten gelijk zijn, klopt het!
</div>

<h4>Stap-voor-stap samenvatting</h4>
<table class="nask">
  <tr><th>Stap</th><th>Wat je doet</th><th>Voorbeeld (5x + 3 = 18)</th></tr>
  <tr><td>1</td><td>Haal het losse getal van beide kanten af</td><td>5x + 3 − 3 = 18 − 3 → 5x = 15</td></tr>
  <tr><td>2</td><td>Deel beide kanten door de coëfficiënt van x</td><td>x = 15 : 5 = 3</td></tr>
  <tr><td>3</td><td>Controleer door in te vullen</td><td>5 × 3 + 3 = 15 + 3 = 18 ✓</td></tr>
</table>
`,

  vragen: [

    // ── NIVEAU 1 ─────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "De balans staat voor de vergelijking 2x + 4 = 10. Wat haal je als eerste van beide kanten af om x te vinden?",
      opties: ["2", "4", "10", "x"],
      antwoord: 1,
      uitleg: "Je haalt eerst het losse getal <b>4</b> van beide kanten af: 2x + 4 − 4 = 10 − 4, dus 2x = 6. Daarna deel je door 2: x = 3.",
      hint: "Haal eerst het getal af dat bij x staat (de constante)."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Bij een vergelijking als balans geldt: als je van de linkerkant iets afhaalt, moet je dat ook van de rechterkant afhalen.",
      antwoord: true,
      uitleg: "Waar! Dit is de <b>balansprincipe</b>: wat je aan één kant doet, doe je ook aan de andere kant, zodat de balans in evenwicht blijft."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Los op met de balans: 3x = 12. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Deel beide kanten door 3: x = 12 : 3 = <b>4</b>.",
      hint: "Deel beide kanten door 3."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "De balans geeft: 4x + 2 = 10. Wat is 4x waard nadat je de balans stap 1 hebt toegepast?",
      opties: ["10", "12", "8", "6"],
      antwoord: 2,
      uitleg: "Haal van beide kanten 2 af: 4x + 2 − 2 = 10 − 2 → <b>4x = 8</b>.",
      hint: "Trek 2 af van beide kanten van de vergelijking."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Los op: 2x + 4 = 10. Wat is x?",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stap 1: 2x + 4 − 4 = 10 − 4 → 2x = 6. Stap 2: x = 6 : 2 = <b>3</b>.",
      hint: "Haal eerst 4 af van beide kanten, dan deel je door 2."
    },

    // ── NIVEAU 2 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 2,
      vraag: "Los op met de balans: 5x + 3 = 18. Wat is x?",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stap 1: 5x + 3 − 3 = 18 − 3 → 5x = 15. Stap 2: x = 15 : 5 = <b>3</b>. Controle: 5 × 3 + 3 = 15 + 3 = 18 ✓",
      hint: "Haal eerst 3 af van beide kanten, dan deel je door 5."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Los op: 4n + 5 = 21. Wat is n?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stap 1: 4n + 5 − 5 = 21 − 5 → 4n = 16. Stap 2: n = 16 : 4 = <b>4</b>. Controle: 4 × 4 + 5 = 16 + 5 = 21 ✓",
      hint: "Haal 5 af van beide kanten, dan deel je door 4."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Op de balans links liggen 6 gelijke potjes en 2 blokjes. Rechts liggen 20 blokjes. Één potje weegt evenveel als één blokje × p (de waarde van p is onbekend). Los op: 6p + 2 = 20. Wat is p?",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stap 1: 6p + 2 − 2 = 20 − 2 → 6p = 18. Stap 2: p = 18 : 6 = <b>3</b>. Controle: 6 × 3 + 2 = 18 + 2 = 20 ✓",
      hint: "Haal eerst 2 af van beide kanten."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Bij de vergelijking 3x + 9 = 24 geldt dat x = 5.",
      antwoord: true,
      uitleg: "Waar! 3x + 9 − 9 = 24 − 9 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: 3 × 5 + 9 = 15 + 9 = 24 ✓"
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Bij de vergelijking 7x + 4 = 39 is de oplossing:",
      opties: ["x = 3", "x = 4", "x = 5", "x = 6"],
      antwoord: 2,
      uitleg: "7x + 4 − 4 = 39 − 4 → 7x = 35 → x = 35 : 7 = <b>5</b>. Controle: 7 × 5 + 4 = 35 + 4 = 39 ✓"
    },

    // ── NIVEAU 3 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Reken maar uit, Duru! Op de markt kosten 8 gelijke appels samen €4 meer dan €20. Dus 8a + 4 = 24. Wat kost één appel? (Geef je antwoord als getal in euro's, zonder eenheidsteken.)",
      antwoord: "2.5|2,5",
      tolerantie: 0,
      uitleg: "8a + 4 − 4 = 24 − 4 → 8a = 20 → a = 20 : 8 = <b>2,50</b>. Eén appel kost €2,50. Controle: 8 × 2,5 + 4 = 20 + 4 = 24 ✓",
      hint: "Haal 4 af van beide kanten, dan deel je door 8. Let op: het antwoord is geen heel getal!"
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Los op: 9y + 7 = 52. Wat is y?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "9y + 7 − 7 = 52 − 7 → 9y = 45 → y = 45 : 9 = <b>5</b>. Controle: 9 × 5 + 7 = 45 + 7 = 52 ✓",
      hint: "Haal 7 af van beide kanten, dan deel je door 9."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "De balans: links 3x + 6 wisselmunten, rechts 21 wisselmunten (in evenwicht). Wat is de waarde van x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "3x + 6 = 21 → 3x + 6 − 6 = 21 − 6 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: 3 × 5 + 6 = 15 + 6 = 21 ✓",
      hint: "Stel de vergelijking op: 3x + 6 = 21."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Bij de vergelijking 5x + 3 = 23 geldt dat x = 4.",
      antwoord: true,
      uitleg: "Waar! 5x + 3 − 3 = 23 − 3 → 5x = 20 → x = 20 : 5 = <b>4</b>. Controle: 5 × 4 + 3 = 20 + 3 = 23 ✓"
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Twee keer een leeftijd plus 6 jaar is 30 jaar. Hoe oud is de persoon? (Vergelijking: 2x + 6 = 30)",
      opties: ["9 jaar", "12 jaar", "18 jaar", "15 jaar"],
      antwoord: 1,
      uitleg: "2x + 6 − 6 = 30 − 6 → 2x = 24 → x = 24 : 2 = <b>12</b>. De persoon is 12 jaar oud. Controle: 2 × 12 + 6 = 24 + 6 = 30 ✓",
      hint: "Los de vergelijking 2x + 6 = 30 op met de balansmethode."
    }

  ]
});
