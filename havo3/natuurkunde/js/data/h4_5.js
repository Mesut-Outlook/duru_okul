/* Onderwerp 4.5 — Temperatuur, weerstand en sensoren */
DURU.register({
  id: "h4-5-sensoren-ntc-ptc-ldr",
  hoofdstuk: 4,
  paragraaf: "4.5",
  titel: "Sensoren (NTC, PTC, LDR)",
  korteUitleg: "Hoe NTC-, PTC- en LDR-sensoren fysische grootheden omzetten in elektrische signalen.",
  icoon: "🎛️",
  kleur: "h4-thema",
  theorie: "<h3>4.5 Temperatuur, weerstand en sensoren</h3><div class='formule-box'><strong>Soorten sensoren:</strong><br>• <b>NTC (Negative Temperature Coefficient):</b> Temperatuur ↑ -> Weerstand ↓ (thermometers/thermostaat).<br>• <b>PTC (Positive Temperature Coefficient):</b> Temperatuur ↑ -> Weerstand ↑ (beveiliging/gloeidraad).<br>• <b>LDR (Light Dependent Resistor):</b> Lichtsterkte ↑ -> Weerstand ↓ (schemerschakelaar).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat gebeurt er met de weerstand van een NTC als de temperatuur stijgt?",
      opties: ["De weerstand daalt", "De weerstand stijgt", "De weerstand blijft gelijk", "De weerstand wordt 0"],
      antwoord: 0,
      uitleg: "NTC = Negatieve coëfficiënt: warmer -> lagere weerstand."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat gebeurt er met de weerstand van een LDR bij fel licht?",
      opties: ["Weerstand wordt heel hoog", "Weerstand wordt heel laag", "Blijft gelijk", "Smelt"],
      antwoord: 1,
      uitleg: "LDR: veel licht = lage weerstand; donker = hoge weerstand."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een NTC-sensor wordt vaak gebruikt in een digitale koortsthermometer.",
      antwoord: true,
      uitleg: "Waar: de weerstandsverandering wordt direct vertaald naar temperatuur."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat gebeurt er met de weerstand van een PTC als hij warmer wordt?",
      opties: ["Spanning wordt nul", "Weerstand daalt", "Weerstand stijgt", "Stroom explodeert"],
      antwoord: 2,
      uitleg: "PTC = Positieve coëfficiënt: warmer -> hogere weerstand."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een sensor zet een natuurkundige grootheid (zoals temperatuur of licht) om in een elektrische spanning of weerstand.",
      antwoord: true,
      uitleg: "Waar: dat is precies de functie van een sensor. De NTC, PTC en LDR veranderen van weerstand door een verandering in temperatuur of lichtsterkte, waardoor een elektrisch circuit die grootheid kan 'meten' via een spanning."
    },
    {
      type: "mc",
      niveau: 3,
      vraag: "In een schemerschakelaar stijgt in het donker de weerstand van de LDR. Wat gebeurt er met de spanning over de LDR in een serieschakeling?",
      opties: ["De spanning over de LDR daalt", "De batterij raakt direct leeg", "De spanning blijft 0 V", "De spanning over de LDR stijgt"],
      antwoord: 3,
      uitleg: "In een serieschakeling krijgt de grootste weerstand het grootste deel van de spanning."
    }
  ]
});
