DURU.register({
  id: "h8-3",
  hoofdstuk: 8,
  paragraaf: "8.3",
  titel: "Vergelijkingen oplossen",
  korteUitleg: "Systematisch vergelijkingen oplossen met dezelfde bewerking aan beide kanten.",
  icoon: "✏️",

  theorie: `
<h3>Vergelijkingen oplossen — de systematische methode</h3>
<p>In 8.2 gebruikten we de balans als plaatje. Nu leren we dezelfde stappen <b>op papier</b> te zetten, zonder tekening. De kern is steeds: doe <b>dezelfde bewerking aan beide kanten</b>.</p>

<div class="formule-box">
  <span class="formule">ax + b = c</span>
  <small>Stap 1: haal b van beide kanten af &nbsp;→&nbsp; ax = c − b &nbsp;·&nbsp; Stap 2: deel door a &nbsp;→&nbsp; x = (c − b) : a</small>
</div>

<h4>De vier stappen</h4>
<table class="nask">
  <tr><th>Stap</th><th>Bewerking</th></tr>
  <tr><td>1</td><td>Haal de <b>constante</b> (het losse getal) van beide kanten af (of tel op als het negatief is)</td></tr>
  <tr><td>2</td><td>Deel beide kanten door de <b>coëfficiënt</b> van x</td></tr>
  <tr><td>3</td><td><b>Controle</b>: vul x in en check of links = rechts</td></tr>
</table>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Standaard vergelijking</div>
  <div class="stap"><b>Vergelijking:</b> 3x + 5 = 20</div>
  <div class="stap"><b>Stap 1:</b> 3x + 5 − 5 = 20 − 5 → <b>3x = 15</b></div>
  <div class="stap"><b>Stap 2:</b> x = 15 : 3 → <b>x = 5</b></div>
  <div class="stap"><b>Controle:</b> links: 3 × 5 + 5 = 15 + 5 = 20 &nbsp;|&nbsp; rechts: 20 ✓</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Met aftrekken links</div>
  <div class="stap"><b>Vergelijking:</b> 4x − 6 = 18</div>
  <div class="stap"><b>Stap 1:</b> 4x − 6 + 6 = 18 + 6 → <b>4x = 24</b></div>
  <div class="stap"><b>Stap 2:</b> x = 24 : 4 → <b>x = 6</b></div>
  <div class="stap"><b>Controle:</b> links: 4 × 6 − 6 = 24 − 6 = 18 &nbsp;|&nbsp; rechts: 18 ✓</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 3 — Variabele aan beide kanten</div>
  <div class="stap"><b>Vergelijking:</b> 5x = 2x + 9</div>
  <div class="stap"><b>Stap 1:</b> Haal 2x van beide kanten af: 5x − 2x = 2x − 2x + 9 → <b>3x = 9</b></div>
  <div class="stap"><b>Stap 2:</b> x = 9 : 3 → <b>x = 3</b></div>
  <div class="stap"><b>Controle:</b> links: 5 × 3 = 15 &nbsp;|&nbsp; rechts: 2 × 3 + 9 = 6 + 9 = 15 ✓</div>
</div>

<div class="info-box teal"><span class="kop">💡 Onthoud</span>
  Schrijf <b>altijd de controle</b> op. Zo zie je meteen of je een foutje hebt gemaakt. Op een toets krijg je hiervoor punten!
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Als er een minteken staat (<b>4x − 6 = 18</b>), <u>tel</u> je 6 op aan beide kanten (je doet het tegenovergestelde). Hetzelfde geldt als je deelt: bij vermenigvuldigen doe je er het omgekeerde van (delen).
</div>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Schrijf alle stappen netjes onder elkaar. Laat zien wat je bij beide kanten doet. Zo maak je geen rekenfouten.
</div>
`,

  vragen: [

    // ── NIVEAU 1 ─────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eerste stap bij het oplossen van 3x + 5 = 20?",
      opties: [
        "Deel beide kanten door 3",
        "Haal 5 af van beide kanten",
        "Haal 20 af van beide kanten",
        "Vermenigvuldig beide kanten met 3"
      ],
      antwoord: 1,
      uitleg: "De eerste stap is het isoleren van de term met x. Je haalt eerst het losse getal <b>5 af van beide kanten</b>: 3x + 5 − 5 = 20 − 5 → 3x = 15.",
      hint: "Haal eerst de constante (het losse getal) weg."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Los op: 5x = 25. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "Deel beide kanten door 5: x = 25 : 5 = <b>5</b>. Controle: 5 × 5 = 25 ✓",
      hint: "Deel beide kanten door 5."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Bij het oplossen van een vergelijking mag je links iets anders doen dan rechts.",
      antwoord: false,
      uitleg: "Onwaar! De gouden regel is: wat je aan de ene kant doet, <b>moet je ook aan de andere kant doen</b>. Anders klopt de vergelijking niet meer."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Los op: 2x + 6 = 14. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stap 1: 2x + 6 − 6 = 14 − 6 → 2x = 8. Stap 2: x = 8 : 2 = <b>4</b>. Controle: 2 × 4 + 6 = 8 + 6 = 14 ✓",
      hint: "Haal eerst 6 af van beide kanten."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Los op: 6x + 4 = 22. Wat is x?",
      opties: ["x = 2", "x = 3", "x = 4", "x = 6"],
      antwoord: 1,
      uitleg: "6x + 4 − 4 = 22 − 4 → 6x = 18 → x = 18 : 6 = <b>3</b>. Controle: 6 × 3 + 4 = 18 + 4 = 22 ✓"
    },

    // ── NIVEAU 2 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 2,
      vraag: "Los op: 3x + 5 = 20. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "3x + 5 − 5 = 20 − 5 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: 3 × 5 + 5 = 15 + 5 = 20 ✓",
      hint: "Haal eerst 5 af van beide kanten, dan deel je door 3."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Los op: 4x − 6 = 18. Wat is x?",
      antwoord: "6",
      tolerantie: 0,
      uitleg: "4x − 6 + 6 = 18 + 6 → 4x = 24 → x = 24 : 4 = <b>6</b>. Controle: 4 × 6 − 6 = 24 − 6 = 18 ✓",
      hint: "Er staat een minteken: tel 6 op aan beide kanten."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Duru spaart geld. Ze heeft al €8 en spaart elke week €5. Na hoeveel weken heeft ze €33? Vergelijking: 5w + 8 = 33. Los op voor w.",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "5w + 8 − 8 = 33 − 8 → 5w = 25 → w = 25 : 5 = <b>5</b>. Na 5 weken heeft Duru €33. Controle: 5 × 5 + 8 = 25 + 8 = 33 ✓",
      hint: "Haal 8 af van beide kanten, dan deel je door 5."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "De oplossing van 7x − 3 = 25 is x = 4.",
      antwoord: true,
      uitleg: "Waar! 7x − 3 + 3 = 25 + 3 → 7x = 28 → x = 28 : 7 = <b>4</b>. Controle: 7 × 4 − 3 = 28 − 3 = 25 ✓"
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "De lengte van een rechthoek is 3 cm meer dan de breedte. De omtrek is 26 cm. De vergelijking voor de breedte b is: 2b + 2(b + 3) = 26, wat vereenvoudigt naar 4b + 6 = 26. Wat is b?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "4b + 6 − 6 = 26 − 6 → 4b = 20 → b = 20 : 4 = <b>5</b>. De breedte is 5 cm. Controle: 4 × 5 + 6 = 20 + 6 = 26 ✓",
      hint: "Haal 6 af van beide kanten, dan deel je door 4."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Los op: 8x − 4 = 28. Wat is x?",
      opties: ["x = 3", "x = 4", "x = 5", "x = 8"],
      antwoord: 1,
      uitleg: "8x − 4 + 4 = 28 + 4 → 8x = 32 → x = 32 : 8 = <b>4</b>. Controle: 8 × 4 − 4 = 32 − 4 = 28 ✓"
    },

    // ── NIVEAU 3 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Los op: 5x = 2x + 9. Wat is x?",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Haal 2x van beide kanten af: 5x − 2x = 2x − 2x + 9 → 3x = 9 → x = 9 : 3 = <b>3</b>. Controle: links 5 × 3 = 15; rechts 2 × 3 + 9 = 6 + 9 = 15 ✓",
      hint: "Trek 2x af van beide kanten zodat alle x-termen aan één kant staan."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Twee vrienden lopen punten. Morris heeft 10x + 3 punten, Bo heeft 2x + 19 punten. Ze hebben even veel punten als 10x + 3 = 2x + 19. Hoeveel is x?",
      antwoord: "2",
      tolerantie: 0,
      uitleg: "10x + 3 = 2x + 19 → 10x − 2x + 3 = 19 → 8x + 3 = 19 → 8x = 16 → x = 16 : 8 = <b>2</b>. Controle: links 10 × 2 + 3 = 23; rechts 2 × 2 + 19 = 4 + 19 = 23 ✓",
      hint: "Haal 2x van beide kanten af, daarna haal je 3 af van beide kanten."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Los op: 6x + 10 = 3x + 25. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "6x + 10 = 3x + 25 → 6x − 3x + 10 = 25 → 3x + 10 = 25 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: links 6 × 5 + 10 = 40; rechts 3 × 5 + 25 = 15 + 25 = 40 ✓",
      hint: "Haal eerst 3x van beide kanten af, dan haal je 10 af van beide kanten."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Los op: −2x + 14 = 4. Wat is x?",
      opties: ["x = 5", "x = 6", "x = 7", "x = 9"],
      antwoord: 0,
      uitleg: "−2x + 14 − 14 = 4 − 14 → −2x = −10 → x = −10 : −2 = <b>5</b>. Controle: −2 × 5 + 14 = −10 + 14 = 4 ✓",
      hint: "Haal 14 af van beide kanten: dan houd je −2x = −10. Deel door −2."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "De oplossing van 9x − 15 = 3x + 9 is x = 4.",
      antwoord: true,
      uitleg: "Waar! 9x − 15 = 3x + 9 → 9x − 3x − 15 = 9 → 6x − 15 = 9 → 6x = 24 → x = 24 : 6 = <b>4</b>. Controle: links 9 × 4 − 15 = 36 − 15 = 21; rechts 3 × 4 + 9 = 12 + 9 = 21 ✓"
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Op een feest zijn er x tafels. Elke tafel heeft 4 stoelen. Er staan ook 7 extra stoelen langs de muur. In totaal zijn er 35 stoelen. Vergelijking: 4x + 7 = 35. Hoeveel tafels zijn er?",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "4x + 7 − 7 = 35 − 7 → 4x = 28 → x = 28 : 4 = <b>7</b>. Er zijn 7 tafels. Controle: 4 × 7 + 7 = 28 + 7 = 35 ✓",
      hint: "Haal 7 af van beide kanten, dan deel je door 4."
    }

  ]
});
