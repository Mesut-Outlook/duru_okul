DURU.register({
  id: "h8-1",
  hoofdstuk: 8,
  paragraaf: "8.1",
  titel: "Gelijksoortige termen",
  korteUitleg: "Termen herkennen en samenvoegen om formules korter te schrijven.",
  icoon: "🔢",

  theorie: `
<h3>Wat zijn termen?</h3>
<p>Een <b>formule</b> bestaat uit stukken die bij elkaar worden opgeteld of afgetrokken. Zo'n stuk heet een <b>term</b>. In de formule <b>3a + 5b + 4</b> zijn er drie termen: <b>3a</b>, <b>5b</b> en <b>4</b>.</p>
<ul>
  <li>Een term met een letter heet een <b>variabele term</b> (bijv. 3a, 7x, 2b).</li>
  <li>Een term zonder letter heet een <b>constante</b> (bijv. 4, 10, −3).</li>
</ul>

<h3>Gelijksoortige termen</h3>
<p><b>Gelijksoortige termen</b> hebben <b>dezelfde letter(s)</b> — en ook dezelfde macht. Je kunt ze samenvoegen (optellen of aftrekken).</p>

<div class="formule-box">
  <span class="formule">3a + 2a = 5a</span>
  <small>Beide termen hebben de letter a → gelijksoortig → samenvoegen</small>
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  <b>5a</b> en <b>5</b> zijn <u>niet</u> gelijksoortig! De ene heeft een letter, de andere niet.<br>
  <b>a²</b> en <b>a</b> zijn ook <u>niet</u> gelijksoortig: de letter heeft een andere macht.
</div>

<h4>Termen samenvoegen ("korter schrijven")</h4>
<p>Als je gelijksoortige termen samenvoegt, schrijf je de formule <b>korter</b>. Alleen de <b>getallen voor de letters</b> (coëfficiënten) tel je op of trek je af — de letter zelf blijft hetzelfde.</p>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Variabele termen samenvoegen</div>
  <div class="stap"><b>Gegeven:</b> 3a + 4 + 2a</div>
  <div class="stap"><b>Stap 1:</b> Zoek gelijksoortige termen: <b>3a</b> en <b>2a</b> zijn gelijksoortig (beide letter a). <b>4</b> staat alleen.</div>
  <div class="stap"><b>Stap 2:</b> Voeg samen: 3a + 2a = 5a</div>
  <div class="stap"><b>Resultaat:</b> 3a + 4 + 2a = <b>5a + 4</b></div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Aftrekken van gelijksoortige termen</div>
  <div class="stap"><b>Gegeven:</b> 7p − 3p + 2</div>
  <div class="stap"><b>Stap 1:</b> <b>7p</b> en <b>3p</b> zijn gelijksoortig.</div>
  <div class="stap"><b>Stap 2:</b> 7p − 3p = 4p</div>
  <div class="stap"><b>Resultaat:</b> 7p − 3p + 2 = <b>4p + 2</b></div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 3 — Meerdere letters</div>
  <div class="stap"><b>Gegeven:</b> 4x + 3y + 2x + y</div>
  <div class="stap"><b>Stap 1:</b> Groepeer: de x-termen (<b>4x</b> en <b>2x</b>) en de y-termen (<b>3y</b> en <b>y</b>, want y = 1y).</div>
  <div class="stap"><b>Stap 2:</b> 4x + 2x = 6x &nbsp;|&nbsp; 3y + 1y = 4y</div>
  <div class="stap"><b>Resultaat:</b> 4x + 3y + 2x + y = <b>6x + 4y</b></div>
</div>

<div class="info-box teal"><span class="kop">💡 Onthoud</span>
  <b>a + a = 2a</b> (niet a²!). Je telt de aantallen op, de letter blijft.<br>
  De coëfficiënt van <b>a</b> alleen is 1: schrijf gewoon <b>a</b>, niet 1a.
</div>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Onderstreep of kleur alle gelijksoortige termen dezelfde kleur. Dan zie je snel wat je kunt samenvoegen!
</div>
`,

  vragen: [

    // ── NIVEAU 1 ─────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Welke twee termen zijn gelijksoortig?",
      opties: ["3x en 5", "3x en 5x", "3x en 5y", "3 en 5y"],
      antwoord: 1,
      uitleg: "<b>3x</b> en <b>5x</b> zijn gelijksoortig: ze hebben allebei de letter x. De andere paren hebben verschillende letters of een letter versus een getal.",
      hint: "Gelijksoortige termen hebben dezelfde letter."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "a + a = a²",
      antwoord: false,
      uitleg: "Onwaar! <b>a + a = 2a</b>. Je telt de coëfficiënten op: 1 + 1 = 2, en de letter a blijft. Machten ontstaan alleen bij vermenigvuldigen (a × a = a²), niet bij optellen."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de korte schrijfwijze van 5b + 3b?",
      opties: ["8b²", "15b", "8b", "5b + 3b kan niet korter"],
      antwoord: 2,
      uitleg: "5b en 3b zijn gelijksoortig. <b>5b + 3b = 8b</b>. Je telt de coëfficiënten op: 5 + 3 = 8.",
      hint: "Tel de getallen voor de b bij elkaar op."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Vereenvoudig: 4a + 3a. Wat is de coëfficiënt van a in het antwoord?",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "4a + 3a = <b>7a</b>. Coëfficiënt is 7.",
      hint: "Tel 4 en 3 op."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "In de formule 3x + 5 zijn 3x en 5 gelijksoortige termen.",
      antwoord: false,
      uitleg: "Onwaar. <b>3x</b> heeft een letter, <b>5</b> niet. Termen zijn alleen gelijksoortig als ze dezelfde letter(s) hebben."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Hoeveel termen heeft de formule 2a + 4b + 7?",
      opties: ["1", "2", "3", "4"],
      antwoord: 2,
      uitleg: "De formule heeft <b>3 termen</b>: <b>2a</b>, <b>4b</b> en <b>7</b>. Elke term wordt gescheiden door een + of −.",
      hint: "Tel de stukken die worden gescheiden door + of −."
    },

    // ── NIVEAU 2 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 2,
      vraag: "Schrijf korter: 6p − 2p + 1. Wat is de coëfficiënt van p?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "6p − 2p = <b>4p</b>. De +1 blijft staan: 4p + 1. De coëfficiënt van p is 4.",
      hint: "Trek de coëfficiënten van p van elkaar af."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Vereenvoudig: 3x + 5 + 2x + 3",
      opties: ["5x + 8", "5x + 8x", "10x", "13x"],
      antwoord: 0,
      uitleg: "De x-termen: 3x + 2x = <b>5x</b>. De getallen: 5 + 3 = <b>8</b>. Samen: <b>5x + 8</b>.",
      hint: "Voeg de x-termen samen en de getallen samen."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Vereenvoudig: 8n − 3n + 2n. Geef de coëfficiënt van n.",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "8n − 3n + 2n = (8 − 3 + 2)n = <b>7n</b>. Coëfficiënt is 7.",
      hint: "Bereken 8 − 3 + 2."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "4x + 2y kan korter geschreven worden als 6xy.",
      antwoord: false,
      uitleg: "Onwaar. <b>4x</b> en <b>2y</b> zijn <u>niet</u> gelijksoortig: ze hebben verschillende letters. Je kunt ze niet samenvoegen. De formule blijft 4x + 2y."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een rechthoek heeft een omtrek van a + 3 + a + 3 + a + 3 + a + 3. Vereenvoudig dit. Wat is de coëfficiënt van a?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Er zijn vier a-termen: a + a + a + a = <b>4a</b>. De constanten: 3 + 3 + 3 + 3 = 12. Samen: <b>4a + 12</b>. Coëfficiënt van a is 4.",
      hint: "Tel alle a-termen op en alle losse getallen op."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Vereenvoudig: 10m − 4m + 3 − 1",
      opties: ["6m + 2", "14m + 2", "6m − 2", "14m − 2"],
      antwoord: 0,
      uitleg: "m-termen: 10m − 4m = <b>6m</b>. Getallen: 3 − 1 = <b>2</b>. Samen: <b>6m + 2</b>.",
      hint: "Behandel de letter-termen apart van de getallen."
    },

    // ── NIVEAU 3 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Vereenvoudig: 5x + 3y + 2x + 4y − x. Geef de coëfficiënt van x in het antwoord.",
      antwoord: "6",
      tolerantie: 0,
      uitleg: "x-termen: 5x + 2x − x = (5 + 2 − 1)x = <b>6x</b>. y-termen: 3y + 4y = 7y. Samen: <b>6x + 7y</b>. Coëfficiënt van x is 6.",
      hint: "Pas op: − x betekent −1x. Bereken 5 + 2 − 1 voor de coëfficiënt van x."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Jantien verkoopt appels. Ze heeft p zakjes met elk 5 appels en q losse appels, plus nog 3p zakjes. Schrijf de totale formule zo kort mogelijk als formule in p en q. Geef de coëfficiënt van p.",
      antwoord: "8",
      tolerantie: 0,
      uitleg: "p-termen: 5p + 3p = <b>8p</b>. q staat alleen: q (= 1q). Totaal: <b>8p + q</b>. Coëfficiënt van p is 8.",
      hint: "Voeg de p-termen samen. Let op: q staat er maar één keer."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Welke formule is correct vereenvoudigd?",
      opties: [
        "3a + 4b + 2a = 9ab",
        "3a + 4b + 2a = 5a + 4b",
        "3a + 4b + 2a = 5a + 4b + 1",
        "3a + 4b + 2a = 9a + b"
      ],
      antwoord: 1,
      uitleg: "a-termen: 3a + 2a = <b>5a</b>. b-term: 4b blijft staan (er is maar één b-term). Correct antwoord: <b>5a + 4b</b>.",
      hint: "Groepeer de a-termen apart van de b-term."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Vereenvoudig: 12k − 5k + 3 + 2k − 8. Geef de coëfficiënt van k.",
      antwoord: "9",
      tolerantie: 0,
      uitleg: "k-termen: 12k − 5k + 2k = (12 − 5 + 2)k = <b>9k</b>. Getallen: 3 − 8 = −5. Samen: <b>9k − 5</b>. Coëfficiënt van k is 9.",
      hint: "Bereken 12 − 5 + 2 voor de k-termen, en 3 − 8 voor de getallen."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "De formule 6a − 2a + a kan vereenvoudigd worden tot 5a.",
      antwoord: true,
      uitleg: "Waar! <b>6a − 2a + a</b> = (6 − 2 + 1)a = <b>5a</b>. Let op: de losse a heeft coëfficiënt 1."
    }

  ]
});
