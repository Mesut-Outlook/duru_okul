DURU.register({
  id: "h4-2",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Snelheid berekenen met de formule",
  korteUitleg: "Bereken snelheid, afstand of tijd met v = s / t.",
  icoon: "📐",

  theorie: `
<h3>Snelheid berekenen</h3>
<p>Als je weet hoe ver iemand rijdt én hoe lang dat duurt, kun je de snelheid uitrekenen. Daarvoor gebruik je de <b>hoofdformule</b>:</p>

<div class="formule-box">
  <span class="formule">snelheid = afstand : tijd</span>
  <small>v in m/s &nbsp;·&nbsp; s = afstand in m &nbsp;·&nbsp; t = tijd in s</small>
</div>

<h4>De formuledriehoek</h4>
<p>Met de formuledriehoek kun je snel zien welke formule je nodig hebt. Dek de gevraagde letter af — wat overblijft is jouw formule:</p>

<figure class="bron">
  <svg viewBox="0 0 260 180" width="100%" style="max-width:280px;display:block;margin:0 auto" aria-label="Formuledriehoek s, v en t">
    <!-- driehoek -->
    <polygon points="130,18 14,162 246,162" fill="#e8f4ff" stroke="#3a86ff" stroke-width="2.5"/>
    <!-- horizontale scheidingslijn -->
    <line x1="72" y1="90" x2="188" y2="90" stroke="#3a86ff" stroke-width="2"/>
    <!-- verticale scheidingslijn (midden onder) -->
    <line x1="130" y1="90" x2="130" y2="162" stroke="#3a86ff" stroke-width="2"/>
    <!-- letters -->
    <text x="130" y="72" text-anchor="middle" font-size="28" font-weight="bold" fill="#1d3557">s</text>
    <text x="82"  y="142" text-anchor="middle" font-size="28" font-weight="bold" fill="#e63946">v</text>
    <text x="178" y="142" text-anchor="middle" font-size="28" font-weight="bold" fill="#2a9d8f">t</text>
    <!-- labels -->
    <text x="130" y="175" text-anchor="middle" font-size="11" fill="#555">dek af wat je zoekt</text>
  </svg>
  <figcaption>Formuledriehoek: s (afstand) bovenin, v (snelheid) linksonder, t (tijd) rechtsonder.</figcaption>
</figure>

<h4>Drie formules uit één driehoek</h4>
<table class="nask">
  <tr><th>Wat zoek je?</th><th>Formule</th><th>Dek af</th></tr>
  <tr><td>snelheid (v)</td><td>v = s ÷ t</td><td>dek v af → s boven t</td></tr>
  <tr><td>afstand (s)</td><td>s = v × t</td><td>dek s af → v naast t</td></tr>
  <tr><td>tijd (t)</td><td>t = s ÷ v</td><td>dek t af → s boven v</td></tr>
</table>

<div class="info-box"><span class="kop">💡 Onthoud</span>
  <b>s</b> staat voor afstand (<i>afstand</i> = <i>s</i>pace in het Latijn), <b>v</b> voor snelheid (<i>velocity</i>) en <b>t</b> voor tijd (<i>time</i>).
</div>

<div class="info-box let-op"><span class="kop">⚠️ Let op</span>
  Zorg dat je <b>eenheden kloppen</b>: gebruik je meters en seconden, dan krijg je m/s. Gebruik je kilometers en uren, dan krijg je km/h. Nooit mixen!
</div>

<h3>Uitgewerkte voorbeelden</h3>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 1 — Snelheid berekenen (uit het boek)</div>
  <div class="stap"><b>Situatie:</b> Een schaatser legt 400 m af in 29,8 s.</div>
  <div class="stap"><b>Gegeven:</b> s = 400 m &nbsp;|&nbsp; t = 29,8 s</div>
  <div class="stap"><b>Gevraagd:</b> v = ?</div>
  <div class="stap"><b>Formule:</b> v = s ÷ t</div>
  <div class="stap"><b>Berekening:</b> v = 400 ÷ 29,8 ≈ 13,4 m/s</div>
  <div class="stap"><b>Antwoord:</b> De schaatser rijdt 13,4 m/s.</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 2 — Afstand berekenen</div>
  <div class="stap"><b>Situatie:</b> Een trein rijdt 45 m/s gedurende 120 s.</div>
  <div class="stap"><b>Gegeven:</b> v = 45 m/s &nbsp;|&nbsp; t = 120 s</div>
  <div class="stap"><b>Gevraagd:</b> s = ?</div>
  <div class="stap"><b>Formule:</b> s = v × t</div>
  <div class="stap"><b>Berekening:</b> s = 45 × 120 = 5 400 m</div>
  <div class="stap"><b>Antwoord:</b> De trein rijdt 5 400 m (= 5,4 km).</div>
</div>

<div class="voorbeeld">
  <div class="vb-kop">📐 Voorbeeld 3 — Tijd berekenen</div>
  <div class="stap"><b>Situatie:</b> Een fietser rijdt 8 m/s. Hij moet 1 200 m afleggen.</div>
  <div class="stap"><b>Gegeven:</b> v = 8 m/s &nbsp;|&nbsp; s = 1 200 m</div>
  <div class="stap"><b>Gevraagd:</b> t = ?</div>
  <div class="stap"><b>Formule:</b> t = s ÷ v</div>
  <div class="stap"><b>Berekening:</b> t = 1 200 ÷ 8 = 150 s</div>
  <div class="stap"><b>Antwoord:</b> De fietser doet er 150 s over.</div>
</div>

<div class="info-box tip"><span class="kop">✅ Handige tip</span>
  Werk <b>altijd</b> in stappen: Gegeven → Gevraagd → Formule → Berekening → Antwoord. Zo maak je nooit een vergissing over welke formule je nodig hebt.
</div>
`,

  vragen: [

    // ── NIVEAU 1 ──────────────────────────────────────────────────────────────

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de formule voor snelheid?",
      opties: [
        "v = s × t",
        "v = s ÷ t",
        "v = t ÷ s",
        "v = s + t"
      ],
      antwoord: 1,
      uitleg: "Snelheid = afstand gedeeld door tijd: <b>v = s ÷ t</b>."
    },

    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van snelheid als je afstand in meters en tijd in seconden invult?",
      opties: ["km/h", "m·s", "m/s", "s/m"],
      antwoord: 2,
      uitleg: "Meters gedeeld door seconden geeft <b>m/s</b>."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Als je de afstand en de snelheid weet, bereken je de tijd met: t = s × v.",
      antwoord: false,
      uitleg: "Onwaar. De juiste formule is <b>t = s ÷ v</b> (afstand gedeeld door snelheid)."
    },

    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Bij de formuledriehoek staat de afstand (s) bovenin.",
      antwoord: true,
      uitleg: "Waar. In de formuledriehoek staat <b>s</b> bovenin, met <b>v</b> en <b>t</b> eronder."
    },

    {
      type: "invoer",
      niveau: 1,
      vraag: "Een leerling loopt 60 m in 20 s. Bereken de snelheid.",
      antwoord: "3",
      eenheid: "m/s",
      uitleg: "v = s ÷ t = 60 ÷ 20 = <b>3 m/s</b>.",
      hint: "Gebruik v = s ÷ t."
    },

    // ── NIVEAU 2 ──────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een schaatser legt 400 m af in 29,8 s. Bereken de snelheid. Rond af op één decimaal.",
      antwoord: "13.4|13,4",
      eenheid: "m/s",
      tolerantie: 0.1,
      uitleg: "v = 400 ÷ 29,8 ≈ <b>13,4 m/s</b>. Dit is het voorbeeld uit het boek!",
      hint: "Gebruik v = s ÷ t en rond af op één decimaal."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een auto rijdt met een snelheid van 25 m/s gedurende 40 s. Bereken de afstand die de auto aflegt.",
      antwoord: "1000",
      eenheid: "m",
      uitleg: "s = v × t = 25 × 40 = <b>1 000 m</b>.",
      hint: "Gebruik s = v × t."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een fietser rijdt 8 m/s. Hij legt 1 200 m af. Hoe lang is hij onderweg?",
      antwoord: "150",
      eenheid: "s",
      uitleg: "t = s ÷ v = 1 200 ÷ 8 = <b>150 s</b>.",
      hint: "Gebruik t = s ÷ v."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een hardloper sprint 100 m in 10 s. Wat is zijn snelheid?",
      antwoord: "10",
      eenheid: "m/s",
      uitleg: "v = s ÷ t = 100 ÷ 10 = <b>10 m/s</b>. Een mooie sprint!"
    },

    {
      type: "mc",
      niveau: 2,
      vraag: "Je weet de snelheid (v) en de tijd (t). Welke formule gebruik je om de afstand te berekenen?",
      opties: ["s = v ÷ t", "s = t ÷ v", "s = v × t", "s = v − t"],
      antwoord: 2,
      uitleg: "Afstand = snelheid × tijd: <b>s = v × t</b>. Dek in de driehoek de s af en je ziet v naast t."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Reken maar uit, Duru! Een trein rijdt 54 m/s. Na 300 s stopt hij. Hoeveel meter heeft de trein afgelegd?",
      antwoord: "16200",
      eenheid: "m",
      uitleg: "s = v × t = 54 × 300 = <b>16 200 m</b> (= 16,2 km).",
      hint: "Gebruik s = v × t."
    },

    {
      type: "invoer",
      niveau: 2,
      vraag: "Een zwemmer legt 50 m af met een snelheid van 1,5 m/s. Hoe lang duurt dit?",
      antwoord: "33.3|33,3",
      eenheid: "s",
      tolerantie: 0.2,
      uitleg: "t = s ÷ v = 50 ÷ 1,5 ≈ <b>33,3 s</b>.",
      hint: "Gebruik t = s ÷ v."
    },

    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een auto rijdt 180 km in 2 uur. Zijn snelheid is 90 km/h.",
      antwoord: true,
      uitleg: "Waar. v = 180 ÷ 2 = <b>90 km/h</b>. Let op: hier km en h, dus de eenheid is km/h."
    },

    // ── NIVEAU 3 ──────────────────────────────────────────────────────────────

    {
      type: "invoer",
      niveau: 3,
      vraag: "Een vliegtuig legt in 2 uur 1 800 km af. Bereken de snelheid in km/h.",
      antwoord: "900",
      eenheid: "km/h",
      uitleg: "v = s ÷ t = 1 800 ÷ 2 = <b>900 km/h</b>. De eenheden zijn km en h, dus het antwoord is km/h.",
      hint: "Pas v = s ÷ t toe. Let op de eenheden: km en h geven km/h."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Een pijl verlaat de boog met 60 m/s. Hij vliegt 3 s. Hoe ver is het doelwit?",
      antwoord: "180",
      eenheid: "m",
      uitleg: "s = v × t = 60 × 3 = <b>180 m</b>.",
      hint: "Gebruik s = v × t."
    },

    {
      type: "mc",
      niveau: 3,
      vraag: "Een fietser rijdt 5 m/s en wil 2 km afleggen. Hoe lang doet hij erover? (Let op de eenheden!)",
      opties: ["4 s", "40 s", "400 s", "4 000 s"],
      antwoord: 2,
      uitleg: "Eerst 2 km omzetten: 2 km = 2 000 m. Dan t = s ÷ v = 2 000 ÷ 5 = <b>400 s</b>. Let altijd op de eenheden!",
      hint: "Zet 2 km eerst om naar meters, en gebruik daarna t = s ÷ v."
    },

    {
      type: "invoer",
      niveau: 3,
      vraag: "Duru sprint 80 m en doet er 12,5 s over. Bereken haar snelheid. Rond af op één decimaal.",
      antwoord: "6.4|6,4",
      eenheid: "m/s",
      tolerantie: 0.1,
      uitleg: "v = s ÷ t = 80 ÷ 12,5 = <b>6,4 m/s</b>. Goed gerend, Duru! 🏃‍♀️",
      hint: "Gebruik v = s ÷ t."
    }

  ]
});
