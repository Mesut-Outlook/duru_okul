DURU.register({
  id: "h4-3",
  hoofdstuk: 4,
  paragraaf: "4.3",
  titel: "Reactieafstand, remafstand & stopafstand",
  korteUitleg: "Reactietijd, reactieafstand en stopafstand berekenen.",
  icoon: "🛑",

  theorie: `
<h3>🛑 Reactieafstand, remafstand en stopafstand</h3>

<h4>Reactietijd</h4>
<p>Als een bestuurder gevaar ziet (bijv. een rood stoplicht of een plotselinge remmer voor je), duurt het even voordat hij of zij reageert en op de rem trapt. Die tijd heet de <b>reactietijd</b>. Gemiddeld is dat ongeveer <b>1 seconde</b>.</p>

<div class="info-box"><span class="kop">💡 Onthoud</span> Tijdens de reactietijd rijdt de auto gewoon door met dezelfde snelheid — de remmen zijn dan nog <em>niet</em> ingetrapt!</div>

<h4>Reactieafstand</h4>
<p>De afstand die de auto aflegt <em>tijdens</em> de reactietijd heet de <b>reactieafstand</b>. Je berekent die met de gewone snelheidsformule:</p>

<div class="formule-box">
  <span class="formule">reactieafstand = snelheid × reactietijd</span>
  <small>s<sub>r</sub> in m &nbsp;·&nbsp; v in m/s &nbsp;·&nbsp; t in s</small>
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span> De snelheid moet in <b>m/s</b> zijn! Staat de snelheid in km/h? Deel dan door 3,6.<br>
Bijvoorbeeld: 72 km/h ÷ 3,6 = <b>20 m/s</b>.</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld — Reactieafstand berekenen</div>
  <div class="stap"><b>Gegeven:</b> snelheid = 54 km/h, reactietijd = 1 s</div>
  <div class="stap"><b>Stap 1 — omrekenen:</b> 54 km/h ÷ 3,6 = 15 m/s</div>
  <div class="stap"><b>Stap 2 — formule:</b> reactieafstand = snelheid × reactietijd</div>
  <div class="stap"><b>Stap 3 — berekening:</b> 15 × 1 = 15 m</div>
  <div class="stap"><b>Antwoord:</b> de reactieafstand is <b>15 m</b></div>
</div>

<h4>Remafstand</h4>
<p>Nadat de remmen ingetrapt zijn, rijdt de auto nog een stuk door voordat hij stilstaat. Die afstand heet de <b>remafstand</b>. De remafstand is afhankelijk van de snelheid en de staat van de remmen en de weg (droog, nat, glad).</p>

<h4>Stopafstand</h4>
<p>De totale afstand vanaf het zien van het gevaar tot volledig stilstaan is de <b>stopafstand</b>:</p>

<div class="formule-box">
  <span class="formule">stopafstand = reactieafstand + remafstand</span>
  <small>alle afstanden in meter (m)</small>
</div>

<figure class="bron">
  <svg viewBox="0 0 420 110" width="100%" style="max-width:420px;display:block;margin:0 auto">
    <!-- wegbalk -->
    <rect x="10" y="55" width="400" height="14" rx="4" fill="#ccc"/>
    <!-- auto -->
    <rect x="15" y="36" width="44" height="22" rx="5" fill="#3B82F6"/>
    <rect x="19" y="41" width="36" height="12" rx="3" fill="#bfdbfe"/>
    <circle cx="25" cy="59" r="6" fill="#1e3a5f"/>
    <circle cx="49" cy="59" r="6" fill="#1e3a5f"/>
    <!-- pijlen -->
    <!-- reactieafstand pijl: 59 → 200 -->
    <line x1="59" y1="80" x2="200" y2="80" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrow-red)"/>
    <text x="100" y="96" font-size="11" fill="#ef4444" text-anchor="middle">reactieafstand</text>
    <!-- remafstand pijl: 200 → 350 -->
    <line x1="200" y1="80" x2="350" y2="80" stroke="#f97316" stroke-width="2.5" marker-end="url(#arrow-orange)"/>
    <text x="275" y="96" font-size="11" fill="#f97316" text-anchor="middle">remafstand</text>
    <!-- stopafstand pijl: 59 → 350 boven -->
    <line x1="59" y1="28" x2="350" y2="28" stroke="#22c55e" stroke-width="2" marker-end="url(#arrow-green)"/>
    <text x="204" y="22" font-size="11" fill="#22c55e" text-anchor="middle">stopafstand</text>
    <!-- scheidingslijn midden -->
    <line x1="200" y1="50" x2="200" y2="90" stroke="#999" stroke-width="1" stroke-dasharray="3,3"/>
    <!-- stop-vlag -->
    <line x1="350" y1="36" x2="350" y2="70" stroke="#22c55e" stroke-width="2"/>
    <polygon points="350,36 364,42 350,48" fill="#22c55e"/>
    <!-- pijlhoofden -->
    <defs>
      <marker id="arrow-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 Z" fill="#ef4444"/>
      </marker>
      <marker id="arrow-orange" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 Z" fill="#f97316"/>
      </marker>
      <marker id="arrow-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L6,3 L0,6 Z" fill="#22c55e"/>
      </marker>
    </defs>
  </svg>
  <figcaption>Reactieafstand (rood) + remafstand (oranje) = stopafstand (groen)</figcaption>
</figure>

<h4>Factoren die de reactietijd vergroten</h4>
<ul>
  <li>Vermoeidheid (moe zijn)</li>
  <li>Alcohol en drugs</li>
  <li>Appen of bellen met de telefoon</li>
  <li>Afleiding (muziek, passagiers, etc.)</li>
</ul>

<div class="info-box tip"><span class="kop">✅ Handige tip</span> Hoe hoger de snelheid, hoe groter zowel de reactieafstand als de remafstand. Een hogere snelheid betekent dus een veel langere stopafstand!</div>

<table class="nask">
  <tr><th>Snelheid</th><th>In m/s</th><th>Reactieafstand (t = 1 s)</th></tr>
  <tr><td>36 km/h</td><td>10 m/s</td><td>10 m</td></tr>
  <tr><td>54 km/h</td><td>15 m/s</td><td>15 m</td></tr>
  <tr><td>72 km/h</td><td>20 m/s</td><td>20 m</td></tr>
  <tr><td>90 km/h</td><td>25 m/s</td><td>25 m</td></tr>
</table>
`,

  vragen: [
    // --- NIVEAU 1 (begrip / herkenning) ---
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de reactietijd?",
      opties: [
        "De tijd dat de auto stil staat",
        "De tijd tussen het zien van gevaar en het intrappen van de rem",
        "De tijd die nodig is om volledig te stoppen",
        "De tijd dat de remmen werken"
      ],
      antwoord: 1,
      uitleg: "De <b>reactietijd</b> is de tijd tussen het waarnemen van gevaar en het reageren (rem intrappen). Gemiddeld duurt dat ~1 seconde."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Tijdens de reactietijd rijdt de auto gewoon met dezelfde snelheid door.",
      antwoord: true,
      uitleg: "Waar! De bestuurder heeft de rem nog <b>niet ingetrapt</b> tijdens de reactietijd, dus de auto rijdt onverminderd door."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de formule voor de reactieafstand?",
      opties: [
        "reactieafstand = afstand ÷ tijd",
        "reactieafstand = snelheid × reactietijd",
        "reactieafstand = remafstand + stopafstand",
        "reactieafstand = snelheid ÷ reactietijd"
      ],
      antwoord: 1,
      uitleg: "De formule is: <b>reactieafstand = snelheid × reactietijd</b>. (Snelheid moet in m/s zijn!)"
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Alcohol verlengt de reactietijd van een bestuurder.",
      antwoord: true,
      uitleg: "Waar! Alcohol vertraagt de hersenen, waardoor de reactietijd langer wordt en de <b>reactieafstand groter</b>."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Hoe bereken je de stopafstand?",
      opties: [
        "stopafstand = reactieafstand × remafstand",
        "stopafstand = reactieafstand − remafstand",
        "stopafstand = reactieafstand + remafstand",
        "stopafstand = remafstand ÷ reactieafstand"
      ],
      antwoord: 2,
      uitleg: "<b>Stopafstand = reactieafstand + remafstand.</b> De totale weg die je aflegt van zien tot stilstaan."
    },

    // --- NIVEAU 2 (berekeningen) ---
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto rijdt met een snelheid van 10 m/s. De reactietijd is 1 s. Hoe groot is de reactieafstand?",
      antwoord: "10",
      eenheid: "m",
      uitleg: "reactieafstand = snelheid × reactietijd = 10 × 1 = <b>10 m</b>."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een scooter rijdt met 15 m/s. De reactietijd van de bestuurder is 1 s. Bereken de reactieafstand.",
      antwoord: "15",
      eenheid: "m",
      uitleg: "reactieafstand = 15 × 1 = <b>15 m</b>."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een fietser rijdt met 5 m/s. Zijn reactietijd is 2 s. Bereken de reactieafstand.",
      antwoord: "10",
      eenheid: "m",
      uitleg: "reactieafstand = 5 × 2 = <b>10 m</b>. Let op: de reactietijd is hier 2 seconden!"
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto rijdt met 20 m/s. De reactietijd is 1 s. Hoe groot is de reactieafstand?",
      antwoord: "20",
      eenheid: "m",
      uitleg: "reactieafstand = 20 × 1 = <b>20 m</b>."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een bestuurder rijdt met een snelheid van 25 m/s en heeft een reactietijd van 1 s. Bereken de reactieafstand.",
      antwoord: "25",
      eenheid: "m",
      uitleg: "reactieafstand = 25 × 1 = <b>25 m</b>. Op de snelweg is de reactieafstand dus al een kwart van een voetbalveld!"
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "De reactieafstand van een auto is 18 m en de remafstand is 27 m. Hoe groot is de stopafstand?",
      antwoord: "45",
      eenheid: "m",
      uitleg: "stopafstand = reactieafstand + remafstand = 18 + 27 = <b>45 m</b>."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto heeft een reactieafstand van 15 m en een remafstand van 20 m. Bereken de stopafstand.",
      antwoord: "35",
      eenheid: "m",
      uitleg: "stopafstand = 15 + 20 = <b>35 m</b>."
    },

    // --- NIVEAU 2 met km/h → m/s omrekenen ---
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto rijdt 36 km/h. Reken eerst om naar m/s en bereken dan de reactieafstand bij een reactietijd van 1 s.",
      antwoord: "10",
      eenheid: "m",
      hint: "Deel de snelheid in km/h door 3,6 om m/s te krijgen.",
      uitleg: "Stap 1: 36 ÷ 3,6 = 10 m/s. Stap 2: reactieafstand = 10 × 1 = <b>10 m</b>."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Reken maar uit, Duru! Een auto rijdt 72 km/h. De reactietijd is 1 s. Hoe groot is de reactieafstand?",
      antwoord: "20",
      eenheid: "m",
      hint: "Vergeet niet eerst km/h ÷ 3,6 te doen!",
      uitleg: "Stap 1: 72 ÷ 3,6 = 20 m/s. Stap 2: reactieafstand = 20 × 1 = <b>20 m</b>."
    },

    // --- NIVEAU 3 (gecombineerd / andersom) ---
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een auto rijdt 90 km/h. De reactietijd is 1 s en de remafstand is 56 m. Bereken de stopafstand.",
      antwoord: "81",
      eenheid: "m",
      hint: "Reken eerst km/h om naar m/s, daarna de reactieafstand, dan stopafstand = reactieafstand + remafstand.",
      uitleg: "Stap 1: 90 ÷ 3,6 = 25 m/s. Stap 2: reactieafstand = 25 × 1 = 25 m. Stap 3: stopafstand = 25 + 56 = <b>81 m</b>."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een automobilist rijdt 54 km/h. De reactietijd door vermoeidheid is 2 s (in plaats van de normale 1 s). De remafstand is 20 m. Bereken de stopafstand.",
      antwoord: "50",
      eenheid: "m",
      hint: "Let op: reactietijd = 2 s, niet 1 s! Stap 1: km/h naar m/s. Stap 2: reactieafstand. Stap 3: stopafstand.",
      uitleg: "Stap 1: 54 ÷ 3,6 = 15 m/s. Stap 2: reactieafstand = 15 × 2 = 30 m. Stap 3: stopafstand = 30 + 20 = <b>50 m</b>. Vermoeidheid maakt de stopafstand dus veel groter!"
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "Een auto rijdt bij 50 km/h. Welke van de volgende factoren vergroot de reactieafstand NIET?",
      opties: [
        "De bestuurder is erg moe",
        "De bestuurder appt op zijn telefoon",
        "Het wegdek is nat",
        "De bestuurder heeft alcohol gedronken"
      ],
      antwoord: 2,
      uitleg: "Een nat wegdek vergroot de <b>remafstand</b> (de banden grijpen minder goed), maar heeft geen invloed op de <b>reactietijd</b> van de bestuurder. Moeheid, appen en alcohol verlengen de reactietijd."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Als je snelheid verdubbelt, verdubbelt ook de reactieafstand (bij gelijke reactietijd).",
      antwoord: true,
      uitleg: "Waar! reactieafstand = snelheid × reactietijd. Als de snelheid 2× zo groot wordt, wordt de reactieafstand ook <b>2× zo groot</b>. Bijv.: 10 m/s → 10 m; 20 m/s → 20 m."
    }
  ]
});
