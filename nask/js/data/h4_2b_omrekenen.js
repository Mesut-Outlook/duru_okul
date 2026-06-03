DURU.register({
  id: "h4-2b",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Eenheden omrekenen: m/s ↔ km/h",
  korteUitleg: "Leer hoe je km/h omzet naar m/s en terug met de factor 3,6.",
  icoon: "🔁",

  theorie: `
<h3>Eenheden omrekenen: km/h en m/s</h3>

<p>Snelheid kun je uitdrukken in <b>kilometer per uur (km/h)</b> of in <b>meter per seconde (m/s)</b>.
Verkeersborden gebruiken km/h, maar in de natuurkunde rekenen we bijna altijd met m/s.
Gelukkig is omrekenen heel makkelijk — je deelt of vermenigvuldigt met <b>3,6</b>.</p>

<h4>Waarom 3,6?</h4>
<p>1 km = 1000 m en 1 uur = 3600 s. Dus:</p>

<div class="formule-box">
  <span class="formule">1 km/h = 1000 m ÷ 3600 s ≈ 0,278 m/s</span>
  <small>en omgekeerd: 1 m/s = 3,6 km/h</small>
</div>

<p>Dat geeft de twee omrekenregels:</p>

<div class="formule-box">
  <span class="formule">m/s = km/h ÷ 3,6</span>
  <small>Van km/h naar m/s: <b>deel</b> door 3,6</small>
</div>

<div class="formule-box">
  <span class="formule">km/h = m/s × 3,6</span>
  <small>Van m/s naar km/h: <b>vermenigvuldig</b> met 3,6</small>
</div>

<h4>Pijlenschema</h4>

<figure class="bron">
  <svg viewBox="0 0 420 130" width="100%" style="max-width:420px;display:block;margin:0 auto;">
    <!-- achtergrondkader -->
    <rect x="10" y="10" width="400" height="110" rx="14" ry="14"
          fill="#f0f4ff" stroke="#c7d2fe" stroke-width="2"/>

    <!-- km/h-blok -->
    <rect x="30" y="40" width="110" height="50" rx="10" ry="10"
          fill="#4f46e5" />
    <text x="85" y="61" text-anchor="middle" fill="white" font-size="13" font-weight="bold">km/h</text>
    <text x="85" y="79" text-anchor="middle" fill="#c7d2fe" font-size="11">bijv. 72</text>

    <!-- m/s-blok -->
    <rect x="280" y="40" width="110" height="50" rx="10" ry="10"
          fill="#059669" />
    <text x="335" y="61" text-anchor="middle" fill="white" font-size="13" font-weight="bold">m/s</text>
    <text x="335" y="79" text-anchor="middle" fill="#a7f3d0" font-size="11">bijv. 20</text>

    <!-- pijl rechts (÷ 3,6) -->
    <line x1="142" y1="56" x2="278" y2="56" stroke="#4f46e5" stroke-width="2.5"
          marker-end="url(#pijlR)"/>
    <text x="210" y="50" text-anchor="middle" fill="#4f46e5" font-size="12" font-weight="bold">÷ 3,6</text>

    <!-- pijl links (× 3,6) -->
    <line x1="278" y1="74" x2="142" y2="74" stroke="#059669" stroke-width="2.5"
          marker-end="url(#pijlL)"/>
    <text x="210" y="90" text-anchor="middle" fill="#059669" font-size="12" font-weight="bold">× 3,6</text>

    <!-- markeringen -->
    <defs>
      <marker id="pijlR" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
        <path d="M0,0 L0,6 L8,3 z" fill="#4f46e5"/>
      </marker>
      <marker id="pijlL" markerWidth="8" markerHeight="8" refX="1" refY="3" orient="auto">
        <path d="M8,0 L8,6 L0,3 z" fill="#059669"/>
      </marker>
    </defs>

    <!-- label boven -->
    <text x="210" y="30" text-anchor="middle" fill="#374151" font-size="12">Omrekenschema snelheid</text>
  </svg>
  <figcaption>Pijlenschema: van km/h naar m/s <b>deel</b> je door 3,6; van m/s naar km/h <b>vermenigvuldig</b> je met 3,6.</figcaption>
</figure>

<h4>Handige omrekentabel</h4>

<table class="nask">
  <tr><th>km/h</th><th>÷ 3,6 =</th><th>m/s</th></tr>
  <tr><td>18 km/h</td><td>18 ÷ 3,6</td><td>5 m/s</td></tr>
  <tr><td>36 km/h</td><td>36 ÷ 3,6</td><td>10 m/s</td></tr>
  <tr><td>54 km/h</td><td>54 ÷ 3,6</td><td>15 m/s</td></tr>
  <tr><td>72 km/h</td><td>72 ÷ 3,6</td><td>20 m/s</td></tr>
  <tr><td>90 km/h</td><td>90 ÷ 3,6</td><td>25 m/s</td></tr>
  <tr><td>108 km/h</td><td>108 ÷ 3,6</td><td>30 m/s</td></tr>
</table>

<div class="info-box">
  <span class="kop">💡 Onthoud</span>
  72 km/h = 20 m/s (stadssnelweg) en 36 km/h = 10 m/s (bebouwde kom fietser).
  Dit zijn de bekendste voorbeelden!
</div>

<div class="info-box tip">
  <span class="kop">✅ Handige tip</span>
  Twijfel je of je moet delen of vermenigvuldigen? Denk: km/h is groter dan m/s
  (72 > 20), dus van km/h naar m/s <b>deel</b> je (getal wordt kleiner).
</div>

<div class="info-box let-op">
  <span class="kop">⚠️ Let op</span>
  De factor is altijd 3,6 — niet 3,6 of iets anders. Leer hem gewoon uit je hoofd!
</div>

<h4>Uitgewerkte voorbeelden</h4>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — van km/h naar m/s</div>
  <div class="stap"><b>Gegeven:</b> v = 72 km/h</div>
  <div class="stap"><b>Formule:</b> m/s = km/h ÷ 3,6</div>
  <div class="stap"><b>Berekening:</b> 72 ÷ 3,6 = 20</div>
  <div class="stap"><b>Antwoord:</b> 72 km/h = <b>20 m/s</b></div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — van m/s naar km/h</div>
  <div class="stap"><b>Gegeven:</b> v = 12 m/s</div>
  <div class="stap"><b>Formule:</b> km/h = m/s × 3,6</div>
  <div class="stap"><b>Berekening:</b> 12 × 3,6 = 43,2</div>
  <div class="stap"><b>Antwoord:</b> 12 m/s = <b>43,2 km/h</b></div>
</div>
`,

  vragen: [

    // ── MEERKEUZE ────────────────────────────────────────────────

    {
      type: "mc", niveau: 1,
      vraag: "Hoe reken je een snelheid in km/h om naar m/s?",
      opties: [
        "Vermenigvuldig met 3,6",
        "Deel door 3,6",
        "Deel door 60",
        "Vermenigvuldig met 1000"
      ],
      antwoord: 1,
      uitleg: "Van km/h naar m/s <b>deel</b> je door 3,6. Voorbeeld: 72 km/h ÷ 3,6 = 20 m/s."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Hoe reken je een snelheid in m/s om naar km/h?",
      opties: [
        "Deel door 3,6",
        "Vermenigvuldig met 60",
        "Vermenigvuldig met 3,6",
        "Deel door 1000"
      ],
      antwoord: 2,
      uitleg: "Van m/s naar km/h <b>vermenigvuldig</b> je met 3,6. Voorbeeld: 10 m/s × 3,6 = 36 km/h."
    },

    {
      type: "mc", niveau: 1,
      vraag: "Een brommer rijdt 45 km/h. Welke berekening geeft de snelheid in m/s?",
      opties: [
        "45 × 3,6",
        "45 ÷ 60",
        "45 ÷ 3,6",
        "45 × 60"
      ],
      antwoord: 2,
      uitleg: "Van km/h naar m/s: <b>45 ÷ 3,6 = 12,5 m/s</b>.",
      hint: "Van km/h naar m/s → deel door 3,6."
    },

    {
      type: "mc", niveau: 2,
      vraag: "Een schaatser beweegt met 15 m/s. Wat is zijn snelheid in km/h?",
      opties: [
        "4,2 km/h",
        "54 km/h",
        "150 km/h",
        "41,7 km/h"
      ],
      antwoord: 1,
      uitleg: "15 m/s × 3,6 = <b>54 km/h</b>."
    },

    {
      type: "mc", niveau: 2,
      vraag: "De maximumsnelheid op de snelweg is 130 km/h. Welk getal is dit in m/s (afgerond op 1 decimaal)?",
      opties: [
        "468,0 m/s",
        "36,1 m/s",
        "46,8 m/s",
        "13,0 m/s"
      ],
      antwoord: 1,
      uitleg: "130 ÷ 3,6 ≈ <b>36,1 m/s</b>.",
      hint: "Deel 130 door 3,6."
    },

    {
      type: "mc", niveau: 3,
      vraag: "Twee auto's rijden even snel. Auto A: 90 km/h, Auto B: 26 m/s. Welke rijdt sneller?",
      opties: [
        "Auto A (90 km/h)",
        "Auto B (26 m/s)",
        "Ze rijden even snel",
        "Dat kun je niet vergelijken"
      ],
      antwoord: 1,
      uitleg: "Reken A om: 90 ÷ 3,6 = 25 m/s. Auto B rijdt 26 m/s. Dus <b>Auto B</b> is sneller.",
      hint: "Zet 90 km/h om naar m/s en vergelijk."
    },

    // ── WAAR / ONWAAR ─────────────────────────────────────────────

    {
      type: "waaronwaar", niveau: 1,
      vraag: "36 km/h is hetzelfde als 10 m/s.",
      antwoord: true,
      uitleg: "<b>Waar.</b> 36 ÷ 3,6 = 10 m/s. Dit is een van de bekendste omrekeningen!"
    },

    {
      type: "waaronwaar", niveau: 1,
      vraag: "Om van m/s naar km/h te gaan, deel je door 3,6.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> Van m/s naar km/h <b>vermenigvuldig</b> je met 3,6. Alleen van km/h naar m/s deel je."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "Een trein rijdt 50 m/s. Dat is meer dan 180 km/h.",
      antwoord: true,
      uitleg: "<b>Waar.</b> 50 × 3,6 = 180 km/h. Dus 50 m/s is <i>precies</i> 180 km/h — en dus inderdaad minstens 180 km/h."
    },

    {
      type: "waaronwaar", niveau: 2,
      vraag: "108 km/h is gelijk aan 3 m/s.",
      antwoord: false,
      uitleg: "<b>Onwaar.</b> 108 ÷ 3,6 = <b>30 m/s</b>, niet 3 m/s. Let op dat je door 3,6 deelt, niet door 36!"
    },

    // ── INVOER — km/h → m/s ───────────────────────────────────────

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 36 km/h = ? m/s",
      antwoord: "10",
      eenheid: "m/s",
      uitleg: "36 ÷ 3,6 = <b>10 m/s</b>."
    },

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 72 km/h = ? m/s",
      antwoord: "20",
      eenheid: "m/s",
      uitleg: "72 ÷ 3,6 = <b>20 m/s</b>. Dit is de standaard stadssnelweg!"
    },

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 18 km/h = ? m/s",
      antwoord: "5",
      eenheid: "m/s",
      uitleg: "18 ÷ 3,6 = <b>5 m/s</b>. Dat is een rustige fietser."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een auto rijdt 54 km/h. Bereken de snelheid in m/s.",
      antwoord: "15",
      eenheid: "m/s",
      uitleg: "54 ÷ 3,6 = <b>15 m/s</b>.",
      hint: "Deel de snelheid door 3,6."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Reken om: 90 km/h = ? m/s",
      antwoord: "25",
      eenheid: "m/s",
      uitleg: "90 ÷ 3,6 = <b>25 m/s</b>."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Reken om: 108 km/h = ? m/s",
      antwoord: "30",
      eenheid: "m/s",
      uitleg: "108 ÷ 3,6 = <b>30 m/s</b>. Dat is de snelheid van een snelle sprinter — nee, een sneltrein! 🚄"
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een fietser fietst 27 km/h. Bereken zijn snelheid in m/s.",
      antwoord: "7.5",
      eenheid: "m/s",
      tolerantie: 0.05,
      uitleg: "27 ÷ 3,6 = <b>7,5 m/s</b>.",
      hint: "Deel 27 door 3,6."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een auto rijdt 126 km/h op de snelweg. Bereken de snelheid in m/s.",
      antwoord: "35",
      eenheid: "m/s",
      uitleg: "126 ÷ 3,6 = <b>35 m/s</b>.",
      hint: "Deel 126 door 3,6. Tip: 126 = 108 + 18, dus 30 + 5 = 35."
    },

    // ── INVOER — m/s → km/h ───────────────────────────────────────

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 10 m/s = ? km/h",
      antwoord: "36",
      eenheid: "km/h",
      uitleg: "10 × 3,6 = <b>36 km/h</b>."
    },

    {
      type: "invoer", niveau: 1,
      vraag: "Reken om: 20 m/s = ? km/h",
      antwoord: "72",
      eenheid: "km/h",
      uitleg: "20 × 3,6 = <b>72 km/h</b>."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een hardloper sprint met 5 m/s. Bereken zijn snelheid in km/h.",
      antwoord: "18",
      eenheid: "km/h",
      uitleg: "5 × 3,6 = <b>18 km/h</b>. Reken maar uit, Duru! 🏃"
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Een schaatser rijdt 15 m/s. Bereken zijn snelheid in km/h.",
      antwoord: "54",
      eenheid: "km/h",
      uitleg: "15 × 3,6 = <b>54 km/h</b>."
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Reken om: 25 m/s = ? km/h",
      antwoord: "90",
      eenheid: "km/h",
      uitleg: "25 × 3,6 = <b>90 km/h</b>. Dat is de maximumsnelheid buiten de bebouwde kom!"
    },

    {
      type: "invoer", niveau: 2,
      vraag: "Reken om: 30 m/s = ? km/h",
      antwoord: "108",
      eenheid: "km/h",
      uitleg: "30 × 3,6 = <b>108 km/h</b>."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een zwemmer doet de 100 m in 50 seconden. Wat is zijn snelheid in km/h? (Reken eerst m/s, daarna naar km/h.)",
      antwoord: "7.2",
      eenheid: "km/h",
      tolerantie: 0.05,
      uitleg: "Stap 1: v = 100 ÷ 50 = 2 m/s. Stap 2: 2 × 3,6 = <b>7,2 km/h</b>.",
      hint: "Bereken eerst de snelheid in m/s met v = afstand ÷ tijd. Zet daarna om naar km/h."
    },

    {
      type: "invoer", niveau: 3,
      vraag: "Een cheetah haalt 28 m/s. Hoeveel km/h is dat? (Afronden op 1 decimaal.)",
      antwoord: "100.8",
      eenheid: "km/h",
      tolerantie: 0.1,
      uitleg: "28 × 3,6 = <b>100,8 km/h</b>. Waanzinnig snel! 🐆",
      hint: "Vermenigvuldig 28 met 3,6."
    }

  ]
});
