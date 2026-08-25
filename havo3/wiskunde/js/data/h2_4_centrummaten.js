DURU.register({
  id: "h2-4-centrummaten",
  hoofdstuk: 2,
  paragraaf: "2.4",
  titel: "2.4 Gemiddelde, Modus & Mediaan",
  korteUitleg: "De drie centrummaten berekenen bij een rij getallen en bij een frequentietabel.",
  icoon: "📐",
  theorie: `
    <h3>Paragraaf 2.4 — Centrummaten (Gemiddelde, Modus & Mediaan)</h3>
    <p>Centrummaten geven in één getal een indruk van het midden van een verzameling waarnemingen.</p>

    <div class="formule-box">
      <strong>De 3 Centrummaten:</strong><br>
      1. <strong>Gemiddelde:</strong> <code>Totale som van alle waarden ÷ Totaal aantal waarnemingen</code>.<br>
         • Bij een frequentietabel: <code>(∑ waarde × frequentie) ÷ (∑ frequentie)</code>.<br>
      2. <strong>Modus:</strong> De waarde die het <em>meest voorkomt</em> (hoogste frequentie).<br>
         • Als twee of meer waarden even vaak het meest voorkomen (of alle waarden even vaak), is er <strong>geen modus</strong>!<br>
      3. <strong>Mediaan:</strong> Het <em>middelste getal</em> nadat alle getallen van klein naar groot op volgorde zijn gezet.<br>
         • Bij een <em>oneven</em> aantal getallen (bijv. 15): het 8e getal.<br>
         • Bij een <em>even</em> aantal getallen (bijv. 16): het gemiddelde van het 8e en 9e getal.
    </div>

    <div class="voorbeeld">
      <div class="vb-kop">Voorbeeld: Centrummaten bepalen</div>
      <p>Cijfers van Sandra: 5, 5, 6, 6, 6, 7, 7, 7, 7, 8 (al op volgorde, n = 10).</p>
      <div class="stap">
        • <strong>Modus:</strong> Cijfer 7 komt het vaakst voor (4 keer) → Modus = <strong>7</strong>.<br>
        • <strong>Mediaan:</strong> n = 10 (even). Middelste twee zijn het 5e en 6e getal (6 en 7) → Mediaan = <code>(6 + 7) ÷ 2 = 6,5</code>.<br>
        • <strong>Gemiddelde:</strong> <code>(5+5+6+6+6+7+7+7+7+8) ÷ 10 = 64 ÷ 10 = 6,4</code>.
      </div>
    </div>
  `,
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de definitie van de modus?",
      opties: [
        "Het gemiddelde van de hoogste en laagste waarde",
        "Het middelste getal van een geordende rij",
        "De waarde die het vaakst voorkomt",
        "Het totaal van alle getallen gedeeld door het aantal"
      ],
      antwoord: 2,
      uitleg: "De modus is de waarde met de hoogste frequentie (komt het vaakst voor)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Gegeven de cijfers: 4, 6, 6, 7, 8, 9. Wat is de mediaan van deze 6 cijfers?",
      antwoord: "6,5|6.5",
      tolerantie: 0.1,
      uitleg: "Bij 6 getallen pak je de middelste twee (3e en 4e getal: 6 en 7). Mediaan = (6 + 7) ÷ 2 = 6,5."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "In een klas scoren leerlingen op een toets: drie 5'en, vijf 6'en, vier 7'ens ve twee 8'en. Wat is de modus?",
      opties: ["5", "6", "7", "8"],
      antwoord: 1,
      uitleg: "Het cijfer 6 komt het vaakst voor (5 keer), dus de modus is 6."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Bereken het gemiddelde van de cijfers: 6, 7, 8, 5, 9, 7. (Rond desnoods af op 1 decimaal).",
      antwoord: "7",
      tolerantie: 0.1,
      uitleg: "Som = 6 + 7 + 8 + 5 + 9 + 7 = 42. Totaal = 6 cijfers. Gemiddelde = 42 ÷ 6 = 7,0."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Als in een gegevensverzameling de waarden 6 en 8 beide 4 keer voorkomen en alle andere waarden minder vaak, dan heeft de verzameling twee modussen (modus = 6 en modus = 8).",
      antwoord: false,
      uitleg: "Onwaar. Als twee waarden gelijkelijk het vaakst voorkomen, zeggen we bij Schoolwiskunde dat er GEEN modus is (of men noemt het bimodaal, maar op de HAVO geldt: geen unieke modus)."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "In een frequentietabel: cijfer 6 (freq 4), cijfer 7 (freq 10), cijfer 8 (freq 6). Bereken het gemiddelde afgerond op 2 decimalen.",
      antwoord: "7,10|7,1|7.1",
      tolerantie: 0.05,
      uitleg: "Totale som = (6×4) + (7×10) + (8×6) = 24 + 70 + 48 = 142. Totaal aantal = 4 + 10 + 6 = 20. Gemiddelde = 142 ÷ 20 = 7,1."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "Van 15 spechten-tellingen is de geordende rij eieren/spechten gemaakt. Omdat n = 15 oneven is, welke rangnummer heeft de mediaan?",
      opties: ["7e getal", "8e getal", "9e getal", "Gemiddelde van 7e en 8e getal"],
      antwoord: 1,
      uitleg: "(15 + 1) ÷ 2 = 8e getal. Er staan 7 getallen voor en 7 getallen na het 8e getal."
    }
  ]
});
