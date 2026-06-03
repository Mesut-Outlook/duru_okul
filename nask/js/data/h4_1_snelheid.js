DURU.register({
  id: "h4-1",
  hoofdstuk: 4,
  paragraaf: "4.1",
  titel: "Wat is snelheid?",
  korteUitleg: "Snelheid berekenen met v = s/t, in m/s en km/h.",
  icoon: "🏎️",

  theorie: `
<h3>Wat is snelheid?</h3>
<p>Snelheid vertelt je <b>hoe snel iets beweegt</b>: hoeveel afstand je in een bepaalde tijd aflegt.
Een hogere snelheid betekent: grotere afstand in dezelfde tijd, <em>of</em> dezelfde afstand in kortere tijd.</p>

<div class="formule-box">
  <span class="formule">snelheid = afstand ÷ tijd</span>
  <small>v = s ÷ t &nbsp;|&nbsp; v in m/s &nbsp;·&nbsp; s = afstand in m &nbsp;·&nbsp; t = tijd in s</small>
</div>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  <b>m/s</b> = meter per seconde (voor kleine afstanden/tijden).
  <b>km/h</b> = kilometer per uur (voor auto's, treinen). Beide zijn eenheden van snelheid.
</div>

<h4>Bekende snelheden</h4>
<table class="nask">
  <tr><th>Beweging</th><th>Snelheid (km/h)</th><th>Snelheid (m/s)</th></tr>
  <tr><td>Wandelen</td><td>~5 km/h</td><td>~1,4 m/s</td></tr>
  <tr><td>Hardlopen</td><td>~10 km/h</td><td>~2,8 m/s</td></tr>
  <tr><td>Fietsen</td><td>~18 km/h</td><td>~5 m/s</td></tr>
  <tr><td>Auto in bebouwde kom</td><td>50 km/h</td><td>~13,9 m/s</td></tr>
  <tr><td>Auto buiten de kom</td><td>80 km/h</td><td>~22,2 m/s</td></tr>
  <tr><td>Snelweg</td><td>100–130 km/h</td><td>~28–36 m/s</td></tr>
  <tr><td>Usain Bolt (100 m sprint)</td><td>~37,6 km/h</td><td>~10,4 m/s</td></tr>
</table>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Usain Bolt rende 100 m in <b>9,58 seconden</b> — dat is het wereldrecord!
  v = 100 ÷ 9,58 ≈ <b>10,4 m/s</b>.
</div>

<h4>De verhoudingstabel</h4>
<p>Met een verhoudingstabel kun je snel snelheid bepalen zonder formule.
Je zet <b>afstand boven</b> en <b>tijd onder</b>, en rekent terug naar 1 uur of 1 seconde.</p>

<figure class="bron">
  <svg viewBox="0 0 420 160" width="100%" style="max-width:420px;font-family:sans-serif;">
    <!-- achtergrond -->
    <rect x="10" y="10" width="400" height="140" rx="12" fill="#f0f7ff" stroke="#4a90d9" stroke-width="2"/>
    <!-- titel -->
    <text x="210" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="#2c3e50">Verhoudingstabel — snelheid</text>
    <!-- rijen header -->
    <rect x="30" y="50" width="110" height="30" rx="6" fill="#4a90d9"/>
    <text x="85" y="70" text-anchor="middle" font-size="13" fill="white" font-weight="bold">Afstand (km)</text>
    <rect x="30" y="90" width="110" height="30" rx="6" fill="#27ae60"/>
    <text x="85" y="110" text-anchor="middle" font-size="13" fill="white" font-weight="bold">Tijd (uur)</text>
    <!-- cellen data -->
    <!-- kolom 1: 60 km / 2 uur -->
    <rect x="155" y="50" width="80" height="30" rx="4" fill="#dbeafe"/>
    <text x="195" y="70" text-anchor="middle" font-size="13" fill="#1e3a5f">60</text>
    <rect x="155" y="90" width="80" height="30" rx="4" fill="#d1fae5"/>
    <text x="195" y="110" text-anchor="middle" font-size="13" fill="#14532d">2</text>
    <!-- pijl -->
    <text x="250" y="80" text-anchor="middle" font-size="20" fill="#e67e22">÷2</text>
    <!-- kolom 2: 30 km / 1 uur -->
    <rect x="280" y="50" width="110" height="30" rx="4" fill="#fef9c3" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="335" y="70" text-anchor="middle" font-size="13" font-weight="bold" fill="#78350f">30 km/h ✓</text>
    <rect x="280" y="90" width="110" height="30" rx="4" fill="#d1fae5" stroke="#10b981" stroke-width="1.5"/>
    <text x="335" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#14532d">1 uur</text>
    <!-- onderschrift -->
    <text x="210" y="145" text-anchor="middle" font-size="11" fill="#6b7280">60 km in 2 uur → deel beide door 2 → 30 km in 1 uur = 30 km/h</text>
  </svg>
  <figcaption>Verhoudingstabel: deel afstand én tijd door hetzelfde getal totdat de tijd = 1 uur (of 1 s).</figcaption>
</figure>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — m/s</div>
  <div class="stap"><b>Gegeven:</b> afstand = 200 m, tijd = 25 s</div>
  <div class="stap"><b>Formule:</b> v = s ÷ t</div>
  <div class="stap"><b>Berekening:</b> v = 200 ÷ 25 = 8 m/s</div>
  <div class="stap"><b>Antwoord:</b> de snelheid is <b>8 m/s</b></div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — km/h</div>
  <div class="stap"><b>Gegeven:</b> afstand = 120 km, tijd = 2 uur</div>
  <div class="stap"><b>Formule:</b> v = s ÷ t</div>
  <div class="stap"><b>Berekening:</b> v = 120 ÷ 2 = 60 km/h</div>
  <div class="stap"><b>Antwoord:</b> de snelheid is <b>60 km/h</b></div>
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Controleer altijd of je afstand in <b>km</b> (→ antwoord in km/h) of <b>m</b> (→ antwoord in m/s) hebt!
  Niet mixen: 1 km = 1000 m, 1 uur = 3600 s.
</div>

<h4>Snelheidsmeter — visualisatie</h4>
<figure class="bron">
  <svg viewBox="0 0 420 180" width="100%" style="max-width:420px;font-family:sans-serif;">
    <rect x="5" y="5" width="410" height="170" rx="14" fill="#1a1a2e" stroke="#4a90d9" stroke-width="2"/>
    <!-- boog snelheidsmeter -->
    <path d="M 80 140 A 80 80 0 0 1 260 140" fill="none" stroke="#2d3561" stroke-width="22" stroke-linecap="round"/>
    <path d="M 80 140 A 80 80 0 0 1 170 65" fill="none" stroke="#e74c3c" stroke-width="22" stroke-linecap="round"/>
    <path d="M 170 65 A 80 80 0 0 1 200 62" fill="none" stroke="#e67e22" stroke-width="22" stroke-linecap="round"/>
    <!-- naald bij ~50 km/h -->
    <line x1="170" y1="140" x2="130" y2="80" stroke="white" stroke-width="3" stroke-linecap="round"/>
    <circle cx="170" cy="140" r="7" fill="#4a90d9"/>
    <!-- labels -->
    <text x="72" y="158" font-size="11" fill="#aaa">0</text>
    <text x="145" y="57" font-size="11" fill="#aaa">50</text>
    <text x="250" y="158" font-size="11" fill="#aaa">100</text>
    <text x="170" y="175" text-anchor="middle" font-size="13" fill="white" font-weight="bold">50 km/h</text>
    <!-- rechter tekst -->
    <text x="300" y="60" font-size="12" fill="#4a90d9" font-weight="bold">Snelheden:</text>
    <text x="300" y="80" font-size="11" fill="#aab">Wandelen  ≈ 5</text>
    <text x="300" y="96" font-size="11" fill="#aab">Fietsen    ≈ 18</text>
    <text x="300" y="112" font-size="11" fill="#f39c12">Auto bebouwde kom 50</text>
    <text x="300" y="128" font-size="11" fill="#aab">Buitenweg ≈ 80</text>
    <text x="300" y="144" font-size="11" fill="#aab">Snelweg  100–130</text>
    <text x="300" y="163" font-size="10" fill="#666">km/h</text>
  </svg>
  <figcaption>Snelheidsmeter met bekende snelheden in km/h.</figcaption>
</figure>
`,

  vragen: [
    // ── NIVEAU 1 — Begrip ────────────────────────────────────────────────
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van snelheid?",
      opties: [
        "meter (m)",
        "seconde (s)",
        "meter per seconde (m/s)",
        "kilogram (kg)"
      ],
      antwoord: 2,
      uitleg: "Snelheid druk je uit in <b>m/s</b> (of km/h). Het gaat om afstand <em>per</em> tijd."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Een hogere snelheid betekent dat je in dezelfde tijd een grotere afstand aflegt.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Meer snelheid = meer afstand in dezelfde tijd. Dat is precies wat snelheid betekent."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke formule klopt voor snelheid?",
      opties: [
        "v = s × t",
        "v = t ÷ s",
        "v = s ÷ t",
        "v = s + t"
      ],
      antwoord: 2,
      uitleg: "<b>v = s ÷ t</b>: snelheid = afstand gedeeld door tijd.",
      hint: "Denk aan 'meter per seconde': dat is meter <em>gedeeld door</em> seconde."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "km/h en m/s zijn allebei eenheden van snelheid.",
      antwoord: true,
      uitleg: "<b>Waar.</b> Kilometer per uur (km/h) gebruik je voor auto's en treinen; meter per seconde (m/s) voor kortere afstanden."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Usain Bolt rende 100 m in 9,58 s. Welke snelheid is dit bij benadering?",
      opties: [
        "Ongeveer 5 m/s",
        "Ongeveer 10 m/s",
        "Ongeveer 20 m/s",
        "Ongeveer 1 m/s"
      ],
      antwoord: 1,
      uitleg: "v = 100 ÷ 9,58 ≈ <b>10,4 m/s</b>. Antwoord B (≈ 10 m/s) is het dichtst bij.",
      hint: "Gebruik v = s ÷ t met s = 100 m en t = 9,58 s."
    },

    // ── NIVEAU 2 — Rekenen ───────────────────────────────────────────────
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een fiets rijdt 200 m in 40 s. Bereken de snelheid.",
      antwoord: "5",
      eenheid: "m/s",
      uitleg: "v = s ÷ t = 200 ÷ 40 = <b>5 m/s</b>.",
      hint: "Gebruik v = afstand ÷ tijd."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto rijdt 90 km in 1 uur. Wat is de snelheid?",
      antwoord: "90",
      eenheid: "km/h",
      uitleg: "v = 90 km ÷ 1 uur = <b>90 km/h</b>.",
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een loper legt 300 m af in 60 s. Bereken de snelheid.",
      antwoord: "5",
      eenheid: "m/s",
      uitleg: "v = s ÷ t = 300 ÷ 60 = <b>5 m/s</b>.",
      hint: "Deel afstand door tijd."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een trein rijdt 240 km in 3 uur. Wat is de snelheid in km/h?",
      antwoord: "80",
      eenheid: "km/h",
      uitleg: "v = 240 ÷ 3 = <b>80 km/h</b>.",
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een steen valt 80 m in 4 s. Bereken de snelheid.",
      antwoord: "20",
      eenheid: "m/s",
      uitleg: "v = s ÷ t = 80 ÷ 4 = <b>20 m/s</b>.",
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Een auto rijdt 30 m in 3 s. Welke snelheid is dit?",
      opties: [
        "3 m/s",
        "10 m/s",
        "90 m/s",
        "0,1 m/s"
      ],
      antwoord: 1,
      uitleg: "v = 30 ÷ 3 = <b>10 m/s</b>.",
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Reken maar uit, Duru! Een schaatser rijdt 500 m in 50 s. Wat is zijn snelheid?",
      antwoord: "10",
      eenheid: "m/s",
      uitleg: "v = 500 ÷ 50 = <b>10 m/s</b>.",
      hint: "Gebruik v = s ÷ t."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een snelheid van 10 m/s is groter dan een snelheid van 30 km/h.",
      antwoord: true,
      uitleg: "<b>Waar.</b> 10 m/s × 3600 s/uur ÷ 1000 m/km = 36 km/h. Dus 10 m/s = 36 km/h > 30 km/h.",
      hint: "Zet 10 m/s om: × 3,6 → km/h."
    },

    // ── NIVEAU 3 — Uitdagend ─────────────────────────────────────────────
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een bus rijdt 180 km in 2 uur. Bereken de snelheid in km/h. Gebruik daarna de verhoudingstabel: hoeveel km legt de bus in 1 uur af?",
      antwoord: "90",
      eenheid: "km/h",
      uitleg: "v = 180 ÷ 2 = <b>90 km/h</b>. In de verhoudingstabel: 180 km / 2 uur → deel door 2 → 90 km / 1 uur = 90 km/h.",
      hint: "Deel afstand én tijd door 2."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een vliegtuig legt 2 500 km af in 5 uur. Bereken de snelheid in km/h.",
      antwoord: "500",
      eenheid: "km/h",
      uitleg: "v = 2500 ÷ 5 = <b>500 km/h</b>.",
      hint: "Gebruik de formule v = s ÷ t."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "Duru fietst 36 km in 2 uur. Haar vriendin loopt 5 km in 30 minuten (= 0,5 uur). Wie is sneller?",
      opties: [
        "Duru, want zij legt meer afstand af",
        "De vriendin, want 10 km/h > 18 km/h klopt niet",
        "Duru, want 18 km/h > 10 km/h",
        "Ze rijden even snel"
      ],
      antwoord: 2,
      uitleg: "Duru: 36 ÷ 2 = <b>18 km/h</b>. Vriendin: 5 ÷ 0,5 = <b>10 km/h</b>. Duru is sneller: 18 > 10.",
      hint: "Bereken voor allebei v = s ÷ t."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Usain Bolt rende 100 m in 9,58 s. Bereken zijn snelheid in m/s. Rond af op 1 decimaal.",
      antwoord: "10.4|10,4",
      eenheid: "m/s",
      tolerantie: 0.1,
      uitleg: "v = 100 ÷ 9,58 ≈ <b>10,4 m/s</b>. Indrukwekkend, toch?",
      hint: "Deel 100 door 9,58 op je rekenmachine."
    }
  ]
});
