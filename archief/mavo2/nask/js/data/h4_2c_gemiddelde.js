DURU.register({
  id: "h4-2c",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Gemiddelde snelheid",
  korteUitleg: "Hoe bereken je de gemiddelde snelheid van een hele rit?",
  icoon: "⏱️",

  theorie: `
<h3>⏱️ Gemiddelde snelheid</h3>

<p>Tijdens een rit ga je zelden de hele tijd even snel. Je remt voor een stoplicht,
trekt op uit een bocht, of stopt even voor een pauze. De <b>gemiddelde snelheid</b>
vertelt hoe snel je <em>gemiddeld</em> reed over de hele rit — ook al was je soms
sneller en soms langzamer.</p>

<div class="formule-box">
  <span class="formule">gemiddelde snelheid = totale afstand ÷ totale tijd</span>
  <small>v<sub>gem</sub> in km/h of m/s &nbsp;·&nbsp; afstand in km of m &nbsp;·&nbsp; tijd in uur of s</small>
</div>

<div class="info-box let-op">
  <span class="kop">⚠️ Let op</span>
  Tel <b>alle</b> tijd mee — ook de tijd dat je stilstaat (pauze, wachten voor een stoplicht).
  Hetzelfde geldt voor de afstand: tel de <b>hele</b> route op.
</div>

<h4>Verschil: constante vs. gemiddelde snelheid</h4>
<p>Een <b>constante snelheid</b> betekent dat je élke seconde precies even snel rijdt
(de snelheidsmeter beweegt niet). Dat is zeldzaam in het echte leven. De
<b>gemiddelde snelheid</b> is de snelheid die je zou hebben <em>als</em> je de hele
rit in hetzelfde tempo had gereden.</p>

<table class="nask">
  <tr><th>Begrip</th><th>Wat het betekent</th><th>Voorbeeld</th></tr>
  <tr><td>Constante snelheid</td><td>Altijd even snel</td><td>Trein op de hogesnelheidslijn (±300 km/h)</td></tr>
  <tr><td>Gemiddelde snelheid</td><td>Totale afstand ÷ totale tijd</td><td>Trein Amsterdam–Rotterdam inclusief stops</td></tr>
</table>

<h4>📐 Voorbeeld 1 — Trein met tussenstops</h4>
<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Treinreis</div>
  <div class="stap"><b>Situatie:</b> Een trein legt 120 km af in 1 uur en 30 minuten (inclusief alle stops).</div>
  <div class="stap"><b>Gegeven:</b> totale afstand = 120 km &nbsp;|&nbsp; totale tijd = 1,5 uur</div>
  <div class="stap"><b>Formule:</b> gemiddelde snelheid = totale afstand ÷ totale tijd</div>
  <div class="stap"><b>Berekening:</b> 120 ÷ 1,5 = <b>80 km/h</b></div>
  <div class="stap"><b>Antwoord:</b> De gemiddelde snelheid van de trein is 80 km/h.</div>
</div>

<h4>📐 Voorbeeld 2 — Fietstocht met pauze</h4>
<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Fietstocht</div>
  <div class="stap"><b>Situatie:</b> Duru fietst 30 km. Ze rijdt 1 uur 45 minuten en rust dan 15 minuten. De totale tijd van deur tot deur is 2 uur.</div>
  <div class="stap"><b>Gegeven:</b> totale afstand = 30 km &nbsp;|&nbsp; totale tijd = 2 uur (pauze telt mee!)</div>
  <div class="stap"><b>Formule:</b> gemiddelde snelheid = totale afstand ÷ totale tijd</div>
  <div class="stap"><b>Berekening:</b> 30 ÷ 2 = <b>15 km/h</b></div>
  <div class="stap"><b>Antwoord:</b> De gemiddelde snelheid is 15 km/h. De pauze verlaagt het gemiddelde!</div>
</div>

<figure class="bron">
  <svg viewBox="0 0 420 160" width="100%" style="max-width:420px;display:block;margin:12px auto">
    <!-- Tijdlijn fietstocht -->
    <rect x="10" y="70" width="400" height="20" rx="4" fill="#e8f4fd" stroke="#5b9bd5" stroke-width="1.5"/>
    <!-- Rijden deel 1 -->
    <rect x="10" y="70" width="262" height="20" rx="4" fill="#5b9bd5" opacity="0.8"/>
    <text x="141" y="84" text-anchor="middle" fill="white" font-size="11" font-weight="bold">Rijden (1u 45min)</text>
    <!-- Pauze -->
    <rect x="272" y="70" width="38" height="20" fill="#f0ad4e" opacity="0.9"/>
    <text x="291" y="84" text-anchor="middle" fill="white" font-size="9" font-weight="bold">Pauze</text>
    <!-- Rijden deel 2 wordt al meegerekend in het totaal; lijn al afgedekt -->
    <!-- Pijlen -->
    <text x="10" y="62" font-size="10" fill="#555">Start</text>
    <text x="375" y="62" font-size="10" fill="#555">Einde</text>
    <!-- Afstandsbalk onder -->
    <text x="210" y="115" text-anchor="middle" font-size="12" fill="#333">Totale afstand: <tspan font-weight="bold">30 km</tspan></text>
    <text x="210" y="133" text-anchor="middle" font-size="12" fill="#333">Totale tijd: <tspan font-weight="bold">2 uur</tspan></text>
    <text x="210" y="151" text-anchor="middle" font-size="13" fill="#c0392b" font-weight="bold">v = 30 ÷ 2 = 15 km/h</text>
    <!-- Label pauze pijl -->
    <line x1="291" y1="96" x2="291" y2="108" stroke="#f0ad4e" stroke-width="1.5" marker-end="url(#arr)"/>
  </svg>
  <figcaption>Tijdlijn van de fietstocht — de pauze telt mee in de totale tijd.</figcaption>
</figure>

<h4>⏱️ Handige omrekeningen</h4>
<table class="nask">
  <tr><th>Tijd</th><th>In uren</th><th>In seconden</th></tr>
  <tr><td>30 minuten</td><td>0,5 uur</td><td>1 800 s</td></tr>
  <tr><td>1 uur 30 min</td><td>1,5 uur</td><td>5 400 s</td></tr>
  <tr><td>1 uur 40 min</td><td>1,67 uur</td><td>6 000 s</td></tr>
  <tr><td>2 uur</td><td>2 uur</td><td>7 200 s</td></tr>
</table>

<div class="info-box tip">
  <span class="kop">✅ Handige tip</span>
  Wil je km/h omrekenen naar m/s? Deel door 3,6.
  Wil je m/s naar km/h? Vermenigvuldig met 3,6.
  Voorbeeld: 72 km/h ÷ 3,6 = 20 m/s.
</div>

<div class="info-box">
  <span class="kop">💡 Onthoud</span>
  Bij gemiddelde snelheid telt <b>alles</b> mee: rijden én stoppen.
  De formule blijft altijd hetzelfde: <b>v<sub>gem</sub> = totale afstand ÷ totale tijd</b>.
</div>
`,

  vragen: [

    /* ── NIVEAU 1 — Begrip & eenvoudig rekenen ── */

    {
      type: "mc", niveau: 1,
      vraag: "Wat is de formule voor gemiddelde snelheid?",
      opties: [
        "gemiddelde snelheid = tijd ÷ afstand",
        "gemiddelde snelheid = afstand × tijd",
        "gemiddelde snelheid = totale afstand ÷ totale tijd",
        "gemiddelde snelheid = halve afstand ÷ halve tijd"
      ],
      antwoord: 2,
      uitleg: "De formule is altijd: <b>v<sub>gem</sub> = totale afstand ÷ totale tijd</b>. Let op: gebruik de <em>totale</em> waarden!"
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Als je 10 minuten pauze houdt tijdens een fietstocht, tel je die pauzetijd NIET mee bij de totale tijd voor de gemiddelde snelheid.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Pauzetijd telt WEL mee. De gemiddelde snelheid berekent de totale afstand over de totale verstreken tijd — inclusief stops."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Een loper rent 8 km in 1 uur. Wat is zijn gemiddelde snelheid?",
      opties: ["4 km/h", "8 km/h", "16 km/h", "1 km/h"],
      antwoord: 1,
      uitleg: "v<sub>gem</sub> = 8 ÷ 1 = <b>8 km/h</b>."
    },

    {
      type: "invoer", niveau: 1,
      vraag: "Een auto rijdt 200 km in 2 uur (zonder stops). Bereken de gemiddelde snelheid.",
      antwoord: "100",
      eenheid: "km/h",
      uitleg: "v<sub>gem</sub> = 200 ÷ 2 = <b>100 km/h</b>."
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Een constant rijdende auto met 90 km/h heeft dezelfde gemiddelde snelheid als een auto die afwisselend sneller en langzamer rijdt maar ook uitkomt op 90 km/h gemiddeld.",
      antwoord: true,
      uitleg: "<b>Waar.</b> De gemiddelde snelheid is een einduitkomst (afstand ÷ tijd). Of je constant reed of wisselend maakt voor de <em>waarde</em> van de gemiddelde snelheid niet uit."
    },

    /* ── NIVEAU 2 — Rekenen met eenheidsomrekeningen ── */

    {
      type: "invoer", niveau: 2,
      vraag: "Een trein legt 120 km af in 1 uur en 30 minuten. Bereken de gemiddelde snelheid. (Tip: 1 uur 30 min = 1,5 uur)",
      antwoord: "80",
      eenheid: "km/h",
      uitleg: "Totale tijd = 1,5 uur. v<sub>gem</sub> = 120 ÷ 1,5 = <b>80 km/h</b>.",
      hint: "Reken 1 uur 30 min om naar uren: dat is 1,5 uur."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een zwemmer legt 1 500 m af in 30 minuten. Bereken de gemiddelde snelheid in m/s. (30 min = 1 800 s)",
      antwoord: "0.83|0,83",
      eenheid: "m/s",
      tolerantie: 0.02,
      uitleg: "v<sub>gem</sub> = 1 500 ÷ 1 800 ≈ <b>0,83 m/s</b>.",
      hint: "Reken minuten om naar seconden: 30 × 60 = 1 800 s."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Duru fietst 30 km. Ze rijdt 1 uur 45 minuten en pauzeert 15 minuten. De totale tijd is 2 uur. Bereken de gemiddelde snelheid.",
      antwoord: "15",
      eenheid: "km/h",
      uitleg: "Pauze telt mee! Totale tijd = 2 uur. v<sub>gem</sub> = 30 ÷ 2 = <b>15 km/h</b>.",
      hint: "Vergeet de pauze niet bij de totale tijd."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een hardloper doet een halve marathon: 21 km in 1 uur en 40 minuten. Hoeveel minuten is dat? Bereken daarna de gemiddelde snelheid in km/h. (1 uur 40 min = 100 min = 5/3 uur ≈ 1,67 uur)",
      antwoord: "12.6|12,6",
      eenheid: "km/h",
      tolerantie: 0.1,
      uitleg: "Totale tijd = 1 uur 40 min = 100 min = 100/60 uur ≈ 1,67 uur. v<sub>gem</sub> = 21 ÷ 1,67 ≈ <b>12,6 km/h</b>.",
      hint: "Reken 1 uur 40 min om: 60 + 40 = 100 minuten = 100 ÷ 60 uur."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een bus rijdt in de ochtendspits 18 km in 45 minuten. Bereken de gemiddelde snelheid. (45 min = 0,75 uur)",
      antwoord: "24",
      eenheid: "km/h",
      uitleg: "v<sub>gem</sub> = 18 ÷ 0,75 = <b>24 km/h</b>.",
      hint: "45 minuten = 45 ÷ 60 = 0,75 uur."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een sporter sprint 400 m in 50 s. Bereken de gemiddelde snelheid in m/s.",
      antwoord: "8",
      eenheid: "m/s",
      uitleg: "v<sub>gem</sub> = 400 ÷ 50 = <b>8 m/s</b>."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Een auto rijdt 60 km in 30 minuten. Wat is de gemiddelde snelheid in km/h?",
      opties: ["30 km/h", "60 km/h", "90 km/h", "120 km/h"],
      antwoord: 3,
      uitleg: "30 min = 0,5 uur. v<sub>gem</sub> = 60 ÷ 0,5 = <b>120 km/h</b>.",
      hint: "Reken 30 minuten om naar uren vóór je deelt."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een schaatser rijdt 10 km in 15 minuten. Bereken de gemiddelde snelheid in km/h. (15 min = 0,25 uur)",
      antwoord: "40",
      eenheid: "km/h",
      uitleg: "v<sub>gem</sub> = 10 ÷ 0,25 = <b>40 km/h</b>."
    },

    /* ── NIVEAU 3 — Dieper rekenen & inzicht ── */

    {
      type: "invoer", niveau: 3,
      vraag: "Reken maar uit, Duru! Een vrachtwagen rijdt op de snelweg 72 km/h. Reken deze snelheid om naar m/s. (Deel door 3,6)",
      antwoord: "20",
      eenheid: "m/s",
      uitleg: "72 km/h ÷ 3,6 = <b>20 m/s</b>. Onthoud: km/h → m/s: deel door 3,6.",
      hint: "Gebruik de omrekenregel: km/h ÷ 3,6 = m/s."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een gezin maakt een autoritje van 180 km. De eerste 90 km duurt 1 uur. Dan staan ze 30 minuten in de file. De laatste 90 km duurt ook 1 uur. Hoe lang duurt de hele rit? Bereken daarna de gemiddelde snelheid in km/h.",
      antwoord: "72",
      eenheid: "km/h",
      tolerantie: 0.5,
      uitleg: "Totale tijd = 1 + 0,5 + 1 = 2,5 uur. v<sub>gem</sub> = 180 ÷ 2,5 = <b>72 km/h</b>. De file verlaagt de gemiddelde snelheid!",
      hint: "Tel alle tijd op: rijden én stilstaan in de file."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een duif vliegt in 2 uur een afstand van 144 km. Bereken de gemiddelde snelheid in m/s. (144 km = 144 000 m; 2 uur = 7 200 s)",
      antwoord: "20",
      eenheid: "m/s",
      uitleg: "v<sub>gem</sub> = 144 000 ÷ 7 200 = <b>20 m/s</b>. Of: 144 ÷ 2 = 72 km/h → 72 ÷ 3,6 = 20 m/s.",
      hint: "Reken eerst km naar m en uur naar seconden, of reken km/h uit en deel daarna door 3,6."
    },

    {
      type: "mc", niveau: 3,
      vraag: "Een fietser rijdt op de heenweg 20 km/h en op de terugweg (dezelfde afstand) 30 km/h. Wat is de gemiddelde snelheid over de hele rit?",
      opties: ["25 km/h", "24 km/h", "22 km/h", "26 km/h"],
      antwoord: 1,
      uitleg: "Stel de afstand één kant op = 60 km. Heenweg: 60 ÷ 20 = 3 uur. Terugweg: 60 ÷ 30 = 2 uur. Totaal: 120 km in 5 uur → 120 ÷ 5 = <b>24 km/h</b>. Het gemiddelde is <em>niet</em> simpelweg (20+30)÷2 = 25!",
      hint: "Kies een handige afstand (bijv. 60 km) en bereken de tijd voor elk deel apart."
    },

  ]
});
