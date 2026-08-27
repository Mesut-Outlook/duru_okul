/* Onderwerp 4.1 — Stofeigenschappen en dichtheid */
DURU.register({
  id: "h4-1-stofeigenschappen-dichtheid",
  hoofdstuk: 4,
  paragraaf: "4.1",
  titel: "Stofeigenschappen & Dichtheid",
  korteUitleg: "Dichtheid berekenen (ρ = m / V), stofeigenschappen, onderdompelmethode en drijven/zinken.",
  icoon: "🧱",
  kleur: "h4-thema",
  theorie: "<h3>4.1 Stofeigenschappen en dichtheid</h3><div class='formule-box'><strong>Dichtheid berekenen:</strong><br>ρ = m / V &nbsp;&nbsp;|&nbsp;&nbsp; m = ρ × V &nbsp;&nbsp;|&nbsp;&nbsp; V = m / ρ<br><br>• ρ (rho) = dichtheid in g/cm³ of kg/m³ (1 g/cm³ = 1000 kg/m³)<br>• m = massa in gram (g) of kilogram (kg)<br>• V = volume in cm³, dm³ (liter) of m³</div><h4>Drijven, zweven en zinken</h4><ul><li><b>Drijven:</b> ρ_voorwerp < ρ_vloeistof (bijv. hout of ijs op water).</li><li><b>Zweven:</b> ρ_voorwerp = ρ_vloeistof.</li><li><b>Zinken:</b> ρ_voorwerp > ρ_vloeistof (bijv. ijzer of steen in water).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de dichtheid van zuiver water?",
      opties: ["0,5 g/cm³", "1,0 g/cm³", "2,7 g/cm³", "7,9 g/cm³"],
      antwoord: 1,
      uitleg: "Water heeft een dichtheid van 1,0 g/cm³ (= 1,0 kg/dm³ = 1000 kg/m³)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een blokje hout heeft een massa van 120 g en een volume van 150 cm³. Bereken de dichtheid in g/cm³.",
      antwoord: "0,8|0,8 g/cm³|0,80",
      uitleg: "ρ = m / V = 120 / 150 = 0,8 g/cm³."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Een voorwerp met dichtheid 1,2 g/cm³ wordt in water (1,0 g/cm³) gegooid. Wat gebeurt er?",
      opties: ["Het drijft", "Het zweeft", "Het zinkt naar de bodem", "Het verdampt"],
      antwoord: 2,
      uitleg: "Omdat de dichtheid groter is dan die van water (1,2 > 1,0), zinkt het voorwerp."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Goud heeft een dichtheid van 19,3 g/cm³. Wat is de massa van een goudstaafje van 10 cm³ in gram?",
      antwoord: "193|193 g|193,0",
      uitleg: "m = ρ × V = 19,3 × 10 = 193 gram."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Massa is een stofeigenschap, maar dichtheid is een voorwerpeigenschap.",
      antwoord: false,
      uitleg: "Niet waar: dichtheid is een stofeigenschap (onafhankelijk van grootte); massa is een voorwerpeigenschap."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "In een maatcilinder stijgt het water van 50 mL naar 75 mL door een steen van 65 gram. Bereken de dichtheid van de steen in g/cm³ (afgerond op 1 decimaal).",
      antwoord: "2,6|2,6 g/cm³",
      uitleg: "V = 75 - 50 = 25 cm³. ρ = 65 / 25 = 2,6 g/cm³."
    }
  ]
});
