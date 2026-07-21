DURU.register({
  id: "h8-4",
  hoofdstuk: 8,
  paragraaf: "8.4",
  titel: "Het snijpunt",
  korteUitleg: "Het snijpunt van twee grafieken berekenen door formules gelijk te stellen.",
  icoon: "📈",

  theorie: `
<h3>Wat is een snijpunt?</h3>
<p>Twee rechte lijnen in een grafiek kunnen elkaar op precies één punt kruisen. Dat punt heet het <b>snijpunt</b>. Op het snijpunt hebben de twee lijnen <b>dezelfde x én dezelfde y</b>.</p>

<div class="formule-box">
  <span class="formule">Snijpunt: stel de twee formules gelijk aan elkaar</span>
  <small>Als y₁ = ax + b en y₂ = cx + d, dan los je op: ax + b = cx + d</small>
</div>

<h4>Stappen om een snijpunt te berekenen</h4>
<table class="nask">
  <tr><th>Stap</th><th>Wat je doet</th></tr>
  <tr><td>1</td><td>Stel de twee formules gelijk: <b>y₁ = y₂</b></td></tr>
  <tr><td>2</td><td>Los de vergelijking op voor <b>x</b></td></tr>
  <tr><td>3</td><td>Bereken <b>y</b> door x in een van de formules in te vullen</td></tr>
  <tr><td>4</td><td>Schrijf het snijpunt als coördinaat <b>(x, y)</b></td></tr>
  <tr><td>5</td><td><b>Controle</b>: vul x ook in de andere formule in — je moet dezelfde y krijgen</td></tr>
</table>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Snijpunt berekenen</div>
  <div class="stap"><b>Formule 1:</b> y = 3x + 2</div>
  <div class="stap"><b>Formule 2:</b> y = x + 8</div>
  <div class="stap"><b>Stap 1:</b> Stel gelijk: 3x + 2 = x + 8</div>
  <div class="stap"><b>Stap 2:</b> 3x − x + 2 = 8 → 2x + 2 = 8 → 2x = 6 → x = 3</div>
  <div class="stap"><b>Stap 3:</b> Vul in formule 1: y = 3 × 3 + 2 = 9 + 2 = 11</div>
  <div class="stap"><b>Controle:</b> formule 2: y = 3 + 8 = 11 ✓</div>
  <div class="stap"><b>Snijpunt:</b> (3, 11)</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Snijpunt met negatieve richtingscoëfficiënt</div>
  <div class="stap"><b>Formule 1:</b> y = 2x + 10</div>
  <div class="stap"><b>Formule 2:</b> y = 4x + 2</div>
  <div class="stap"><b>Stap 1:</b> Stel gelijk: 2x + 10 = 4x + 2</div>
  <div class="stap"><b>Stap 2:</b> 10 − 2 = 4x − 2x → 8 = 2x → x = 4</div>
  <div class="stap"><b>Stap 3:</b> y = 2 × 4 + 10 = 8 + 10 = 18</div>
  <div class="stap"><b>Controle:</b> formule 2: y = 4 × 4 + 2 = 16 + 2 = 18 ✓</div>
  <div class="stap"><b>Snijpunt:</b> (4, 18)</div>
</div>

<h4>Snijpunt aflezen uit een grafiek</h4>
<p>Je kunt een snijpunt ook <b>aflezen uit een grafiek</b>: zoek het punt waar de twee lijnen elkaar kruisen, en lees de x- en y-coördinaat af.</p>

<figure class="bron">
  <svg viewBox="0 0 360 280" width="100%" style="max-width:400px;display:block;margin:0 auto" aria-label="Grafiek met twee lijnen en snijpunt">
    <!-- assen -->
    <line x1="40" y1="250" x2="340" y2="250" stroke="#888" stroke-width="1.5"/>
    <line x1="40" y1="10"  x2="40"  y2="250" stroke="#888" stroke-width="1.5"/>
    <!-- pijlen -->
    <polygon points="340,250 334,247 334,253" fill="#888"/>
    <polygon points="40,10 37,16 43,16"       fill="#888"/>
    <!-- raster (x=0..6, y=0..12 met stapgrootte 20px) -->
    <!-- y=3x+2: door (0,2) en (3,11) → pixels: x0=40+0*40=40, y0=250-2*20=210; x3=40+3*40=160, y3=250-11*20=30 -->
    <line x1="40" y1="210" x2="220" y2="30" stroke="#3a86ff" stroke-width="2.5"/>
    <!-- y=x+8: door (0,8) en (3,11) → x0=40, y0=250-8*20=90; x3=160, y3=30 -->
    <line x1="40" y1="90" x2="260" y2="30" stroke="#e63946" stroke-width="2.5"/>
    <!-- snijpunt (3,11) → x=40+3*40=160, y=250-11*20=30 -->
    <circle cx="160" cy="30" r="6" fill="#f4a261" stroke="#fff" stroke-width="1.5"/>
    <text x="168" y="26" font-size="12" fill="#333">(3, 11)</text>
    <!-- as-labels -->
    <text x="345" y="254" font-size="12" fill="#555">x</text>
    <text x="44"  y="8"   font-size="12" fill="#555">y</text>
    <!-- x-getallen -->
    <text x="78"  y="263" text-anchor="middle" font-size="11" fill="#555">1</text>
    <text x="118" y="263" text-anchor="middle" font-size="11" fill="#555">2</text>
    <text x="158" y="263" text-anchor="middle" font-size="11" fill="#555">3</text>
    <text x="198" y="263" text-anchor="middle" font-size="11" fill="#555">4</text>
    <!-- lijn-labels -->
    <text x="224" y="26" font-size="12" fill="#3a86ff">y = 3x + 2</text>
    <text x="265" y="26" font-size="12" fill="#e63946">y = x + 8</text>
  </svg>
  <figcaption>Snijpunt van y = 3x + 2 (blauw) en y = x + 8 (rood) ligt op (3, 11).</figcaption>
</figure>

<div class="info-box teal"><span class="kop">💡 Onthoud</span>
  Op het snijpunt zijn BEIDE formules waar: vul je x in in formule 1 én formule 2, dan krijg je altijd <b>dezelfde y</b>. Gebruik dit voor de controle!
</div>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Schrijf het snijpunt altijd als <b>(x, y)</b> — eerst x dan y, tussen haakjes, gescheiden door een komma.
</div>
`,

  vragen: [

    // ── NIVEAU 1 ─────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is een snijpunt van twee grafieken?",
      opties: [
        "Het punt waar de grafiek de y-as kruist",
        "Het punt waar twee lijnen elkaar kruisen",
        "Het hoogste punt van de grafiek",
        "Het punt waar x = 0"
      ],
      antwoord: 1,
      uitleg: "Het <b>snijpunt</b> is het punt waar twee lijnen elkaar kruisen. Op dat punt hebben beide lijnen exact dezelfde coördinaten (x, y).",
      hint: "Twee lijnen kunnen elkaar op één punt kruisen."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Je hebt y = 2x + 1 en y = 5. Op welke stap begin je om het snijpunt te berekenen?",
      opties: [
        "Bereken y = 2 × 5 + 1",
        "Stel 2x + 1 = 5",
        "Stel x = 5",
        "Bereken 2 + 1 = 3"
      ],
      antwoord: 1,
      uitleg: "Je begint met de twee formules <b>gelijk stellen</b>: 2x + 1 = 5. Dan los je op voor x.",
      hint: "Op het snijpunt geldt y₁ = y₂."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Op het snijpunt van twee lijnen zijn zowel de x- als de y-waarde gelijk voor beide lijnen.",
      antwoord: true,
      uitleg: "Waar! Op het snijpunt hebben beide lijnen <b>dezelfde x én dezelfde y</b>. Dat is juist waarom je de formules gelijk stelt."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Los op: 2x + 1 = 5 (dit geeft de x-coördinaat van een snijpunt). Wat is x?",
      antwoord: "2",
      tolerantie: 0,
      uitleg: "2x + 1 − 1 = 5 − 1 → 2x = 4 → x = 4 : 2 = <b>2</b>.",
      hint: "Haal 1 af van beide kanten, dan deel je door 2."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Twee lijnen: y = x + 3 en y = 2x + 1. Je stelt ze gelijk: x + 3 = 2x + 1. Wat is de volgende stap?",
      opties: [
        "Haal x af van beide kanten: 3 = x + 1",
        "Haal 3 af van beide kanten: x = 2x − 2",
        "Vermenigvuldig beide kanten met x",
        "Tel x + 1 op: 2x + 4 = 2x + 1"
      ],
      antwoord: 0,
      uitleg: "Haal <b>x af van beide kanten</b>: x + 3 − x = 2x + 1 − x → 3 = x + 1 → x = 2. Dit is de meest logische volgende stap.",
      hint: "Probeer alle x-termen naar één kant te brengen."
    },

    // ── NIVEAU 2 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 2,
      vraag: "Zoek het snijpunt van y = 3x + 2 en y = x + 8. Wat is de x-coördinaat van het snijpunt?",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stel gelijk: 3x + 2 = x + 8 → 3x − x + 2 = 8 → 2x = 6 → x = 3. De x-coördinaat is <b>3</b>.",
      hint: "Stel de twee formules gelijk en los op voor x."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Zoek het snijpunt van y = 3x + 2 en y = x + 8. Wat is de y-coördinaat? (Gebruik x = 3 in formule 1.)",
      antwoord: "11",
      tolerantie: 0,
      uitleg: "Vul x = 3 in: y = 3 × 3 + 2 = 9 + 2 = <b>11</b>. Controle in formule 2: y = 3 + 8 = 11 ✓. Het snijpunt is (3, 11).",
      hint: "Vul x = 3 in in y = 3x + 2."
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Wat is het snijpunt van y = 2x + 4 en y = x + 7?",
      opties: ["(2, 8)", "(3, 10)", "(4, 11)", "(1, 8)"],
      antwoord: 1,
      uitleg: "Stel gelijk: 2x + 4 = x + 7 → x = 3. Vul in: y = 2 × 3 + 4 = 6 + 4 = <b>10</b>. Controle: y = 3 + 7 = 10 ✓. Snijpunt: <b>(3, 10)</b>.",
      hint: "Stel de formules gelijk en los op voor x, vul dan in voor y."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Zoek de x-coördinaat van het snijpunt van y = 4x + 1 en y = 2x + 9.",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stel gelijk: 4x + 1 = 2x + 9 → 4x − 2x = 9 − 1 → 2x = 8 → x = <b>4</b>. Controle y: 4 × 4 + 1 = 17; 2 × 4 + 9 = 8 + 9 = 17 ✓.",
      hint: "Haal 2x van beide kanten af, dan haal je 1 af van beide kanten."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Het snijpunt van y = 5x en y = 2x + 6 ligt op (2, 10).",
      antwoord: true,
      uitleg: "Waar! Stel gelijk: 5x = 2x + 6 → 3x = 6 → x = 2. Vul in: y = 5 × 2 = <b>10</b>. Controle: 2 × 2 + 6 = 4 + 6 = 10 ✓. Snijpunt: (2, 10)."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Jasmijn verdient €3 per uur zakgeld en heeft al €5 gespaard. Tim verdient €1 per uur en heeft al €9. Formules: y = 3x + 5 en y = x + 9. Na hoeveel uur (x) hebben ze even veel? Geef de x-coördinaat van het snijpunt.",
      antwoord: "2",
      tolerantie: 0,
      uitleg: "Stel gelijk: 3x + 5 = x + 9 → 2x = 4 → x = <b>2</b>. Na 2 uur hebben ze allebei y = 3 × 2 + 5 = 11 euro. Controle: x + 9 = 2 + 9 = 11 ✓.",
      hint: "Stel 3x + 5 = x + 9 en los op voor x."
    },

    // ── NIVEAU 3 ─────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Zoek het snijpunt van y = 5x − 3 en y = 2x + 6. Geef eerst de x-coördinaat.",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stel gelijk: 5x − 3 = 2x + 6 → 3x = 9 → x = <b>3</b>. y = 5 × 3 − 3 = 15 − 3 = 12. Controle: 2 × 3 + 6 = 6 + 6 = 12 ✓. Snijpunt: (3, 12).",
      hint: "Haal 2x van beide kanten af, tel dan 3 op bij beide kanten."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Wat is het snijpunt van y = 6x − 2 en y = 2x + 10?",
      opties: ["(2, 10)", "(3, 16)", "(4, 22)", "(1, 12)"],
      antwoord: 1,
      uitleg: "Stel gelijk: 6x − 2 = 2x + 10 → 4x = 12 → x = 3. Vul in: y = 6 × 3 − 2 = 18 − 2 = <b>16</b>. Controle: 2 × 3 + 10 = 6 + 10 = 16 ✓. Snijpunt: <b>(3, 16)</b>.",
      hint: "Stel de vergelijking op, los op voor x, vul dan in voor y."
    },

    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Het snijpunt van y = 3x + 4 en y = 7x − 8 heeft x-coördinaat 3.",
      antwoord: true,
      uitleg: "Waar! Stel gelijk: 3x + 4 = 7x − 8 → 4 + 8 = 7x − 3x → 12 = 4x → x = <b>3</b>. y = 3 × 3 + 4 = 9 + 4 = 13. Controle: 7 × 3 − 8 = 21 − 8 = 13 ✓."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Twee sportzalen rekenen als volgt: zaal A: y = 4x + 20 (maandkosten) en zaal B: y = 2x + 40. Na hoeveel maanden (x) zijn de kosten gelijk? Geef de x-coördinaat van het snijpunt.",
      antwoord: "10",
      tolerantie: 0,
      uitleg: "Stel gelijk: 4x + 20 = 2x + 40 → 2x = 20 → x = <b>10</b>. Na 10 maanden: y = 4 × 10 + 20 = 60. Controle zaal B: 2 × 10 + 40 = 20 + 40 = 60 ✓. Snijpunt: (10, 60).",
      hint: "Haal 2x van beide kanten af, trek dan 20 af van beide kanten."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Zoek de y-coördinaat van het snijpunt van y = 2x + 3 en y = x + 7. (Bereken eerst x, daarna y.)",
      antwoord: "11",
      tolerantie: 0,
      uitleg: "Stel gelijk: 2x + 3 = x + 7 → x = 4. Vul in: y = 2 × 4 + 3 = 8 + 3 = <b>11</b>. Controle: y = 4 + 7 = 11 ✓. Snijpunt: (4, 11).",
      hint: "Los eerst 2x + 3 = x + 7 op voor x, vul dan x in."
    }

  ]
});
