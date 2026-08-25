DURU.register({
  id: "h2-2-cirkeldiagram",
  hoofdstuk: 2,
  paragraaf: "2.2",
  titel: "2.2 Cirkeldiagram",
  korteUitleg: "Sectoren, hoeken berekenen (100% = 360°), verhoudingen en cirkeldiagrammen aflezen.",
  icoon: "🍕",
  theorie: `
    <h3>Paragraaf 2.2 — Cirkeldiagram</h3>
    <p>In een <strong>cirkeldiagram</strong> worden gegevens weergegeven in taartpunten die we <strong>sectoren</strong> noemen.</p>

    <div class="formule-box">
      <strong>Belangrijke eigenschappen van een cirkeldiagram:</strong><br>
      • De hele cirkel is <strong>100%</strong>.<br>
      • De hoek rondom het middelpunt van een hele cirkel is <strong>360°</strong>.<br>
      • Formule hoek van een sector:<br>
      <code>Middelpuntshoek = (aantal ÷ totaal) × 360°</code><br>
      of<br>
      <code>Middelpuntshoek = (percentage ÷ 100) × 360°</code>
    </div>

    <div class="voorbeeld">
      <div class="vb-kop">Voorbeeld: Middelpuntshoek berekenen</div>
      <p>Van 120 toeristen gaan er 30 met het vliegtuig. Bereken de hoek van deze sector.</p>
      <div class="stap">
        <strong>Uitwerking:</strong><br>
        • Totaal aantal mensen = 120 → Hoort bij 360°.<br>
        • Hoek = <code>(30 ÷ 120) × 360° = 90°</code>.<br>
        • Een hoek van 90° is precies een kwart van de cirkel (25%).
      </div>
    </div>

    <div class="info-box tip">
      <strong>Controle:</strong> Als je de hoeken van alle sectoren in een cirkeldiagram bij elkaar optelt, moet de som altijd precies <strong>360°</strong> zijn!
    </div>
  `,
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Hoeveel graden is de totale hoek rondom het middelpunt van een cirkeldiagram?",
      opties: ["90°", "180°", "270°", "360°"],
      antwoord: 3,
      uitleg: "Een volle cirkel is altijd 360° rondom het middelpunt."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een sector in een cirkeldiagram stelt 25% van het totaal voor. Hoeveel graden is de middelpuntshoek van deze sector?",
      antwoord: "90",
      eenheid: "°",
      tolerantie: 0.1,
      uitleg: "25% van 360° = 0,25 × 360° = 90°."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Van 40 leerlingen kiezen er 15 voor voetbal. Hoe bereken je de middelpuntshoek van de sector 'voetbal'?",
      opties: [
        "(15 ÷ 40) × 100°",
        "(15 ÷ 40) × 360°",
        "(40 ÷ 15) × 360°",
        "(15 ÷ 360) × 40°"
      ],
      antwoord: 1,
      uitleg: "Hoek = (deel ÷ totaal) × 360° = (15 ÷ 40) × 360° = 135°."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "In een klas van 30 leerlingen hebben 12 leerlingen een hond als huisdier. Hoeveel graden is de sector voor honden in het cirkeldiagram?",
      antwoord: "144",
      eenheid: "°",
      tolerantie: 0.5,
      uitleg: "(12 ÷ 30) × 360° = 144°."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als een sector een hoek heeft van 72°, stelt deze sector 20% van het totaal voor.",
      antwoord: true,
      uitleg: "Waar. (72° ÷ 360°) × 100% = 20%."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "In een cirkeldiagram over vervoermiddelen (vliegtuig, bus, auto) heeft het vliegtuig 90° en de bus 45°. Hoeveel graden is de sector voor de auto?",
      opties: ["180°", "225°", "240°", "270°"],
      antwoord: 1,
      uitleg: "Totaal is 360°. Auto = 360° - 90° - 45° = 225°."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Aan 800 inwoners is gevraagd welke supermarkt ze bezoeken. De sector AH heeft een hoek van 86,4° (24%). Hoeveel van de 800 inwoners gaan naar AH?",
      antwoord: "192",
      tolerantie: 0.5,
      uitleg: "24% van 800 = 0,24 × 800 = 192 inwoners (of (86,4 ÷ 360) × 800 = 192)."
    }
  ]
});
