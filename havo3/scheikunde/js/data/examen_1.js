/* Proeftoets 1 — Scheikunde HAVO 3: stoffen, atomen & reacties.
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-scheikunde-1",
  titel: "Proeftoets 1 — Scheikunde: stoffen, atomen & reacties",
  vak: "Scheikunde · HAVO 3",
  icoon: "🧪",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Welke formule hoort bij <b>water</b>?",
      opties: [
        "CO<sub>2</sub>",
        "H<sub>2</sub>O",
        "O<sub>2</sub>",
        "NaCl"
      ],
      antwoord: 1,
      uitleg: "Water is H<sub>2</sub>O: één watermolecuul bestaat uit 2 waterstofatomen en 1 zuurstofatoom."
    },
    {
      type: "mc",
      vraag: "Uit welke deeltjes bestaat de <b>kern</b> van een atoom?",
      opties: [
        "alleen elektronen",
        "protonen en elektronen",
        "protonen en neutronen",
        "alleen neutronen"
      ],
      antwoord: 2,
      uitleg: "In de kern zitten protonen (positief) en neutronen (neutraal). De elektronen (negatief) draaien daaromheen in schillen."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een chemische reactie ontstaan er nieuwe stoffen.",
      antwoord: true,
      uitleg: "Waar. Bij een chemische reactie verdwijnen de beginstoffen en ontstaan er nieuwe stoffen (reactieproducten) met andere eigenschappen. Bij een faseovergang, zoals smelten, blijft het dezelfde stof."
    },
    {
      type: "invul",
      vraag: "Een stof die uit maar één soort atomen bestaat, noem je een … .",
      antwoord: "element|elementen|enkelvoudige stof",
      uitleg: "Een element (enkelvoudige stof) bestaat uit één soort atomen, bijvoorbeeld ijzer (Fe) of zuurstof (O<sub>2</sub>). Bestaat een stof uit meerdere soorten atomen, dan is het een verbinding."
    },
    {
      type: "open",
      vraag: "Leg uit wat de <b>wet van behoud van massa</b> betekent bij een chemische reactie, en waarom je een reactievergelijking daarom moet <b>kloppend maken</b>.",
      sleutelwoorden: [
        "massa blijft gelijk/even zwaar/niets verdwijnt",
        "atomen/aantal atomen/zelfde atomen",
        "links en rechts/voor en na/beide kanten"
      ],
      minTreffers: 2,
      modelantwoord: "De totale massa van de beginstoffen is precies even groot als de totale massa van de reactieproducten: er verdwijnen geen atomen en er komen er ook geen bij, ze worden alleen anders gerangschikt. Daarom moet in een reactievergelijking links en rechts van de pijl van elke atoomsoort hetzelfde aantal staan — dat noem je kloppend maken.",
      uitleg: "De kern is: atomen gaan niet verloren, dus links en rechts van de pijl moeten evenveel atomen van elke soort staan. Daarom zet je coëfficiënten vóór de formules."
    }
  ]
});
