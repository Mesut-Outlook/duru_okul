/* Onderwerp 4.2 — Soortelijke warmte */
DURU.register({
  id: "h4-2-soortelijke-warmte",
  hoofdstuk: 4,
  paragraaf: "4.2",
  titel: "Temperatuur & Soortelijke Warmte",
  korteUitleg: "Temperatuur (Celsius/Kelvin), warmtehoeveelheid (Q = m·c·ΔT) en soortelijke warmte.",
  icoon: "🌡️",
  kleur: "h4-thema",
  theorie: "<h3>4.2 Soortelijke warmte</h3><div class='formule-box'><strong>Warmte berekenen:</strong><br>Q = m × c × ΔT<br><br>• Q = warmtehoeveelheid in <b>Joule (J)</b><br>• m = massa in kg (of gram)<br>• c = soortelijke warmte in J/(kg·K) (of J/(g·°C))<br>• ΔT = temperatuurverschil in K of °C<br><br><strong>Temperatuurschalen:</strong> T (in K) = T (in °C) + 273</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van warmte (energie)?",
      opties: ["Graden Celsius (°C)", "Kelvin (K)", "Joule (J)", "Watt (W)"],
      antwoord: 2,
      uitleg: "Warmte is thermische energie en wordt gemeten in Joule (J)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Reken om: 20 °C is gelijk aan hoeveel Kelvin?",
      antwoord: "293|293 K|293,15",
      uitleg: "T(K) = 20 + 273 = 293 K."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Hoeveel Joule warmte is nodig om 1,0 kg water (c = 4180 J/(kg·K)) 10 °C te verwarmen?",
      antwoord: "41800|41.800|41,8 kJ|41800 J",
      uitleg: "Q = m × c × ΔT = 1,0 × 4180 × 10 = 41.800 J."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Water heeft een veel hogere soortelijke warmte dan zand en de meeste metalen.",
      antwoord: true,
      uitleg: "Waar: water heeft een extreem hoge warmtecapaciteit (4180 J/kg·K)."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat is het absolute nulpunt (0 Kelvin) in graden Celsius?",
      opties: ["0 °C", "-100 °C", "-273 °C", "-373 °C"],
      antwoord: 2,
      uitleg: "0 K = -273,15 °C."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een aluminium blokje van 0,20 kg (c = 880 J/(kg·K)) koelt af met ΔT = 50 K. Hoeveel Joule warmte staat het blokje af?",
      antwoord: "8800|8.800|8,8 kJ|8800 J",
      uitleg: "Q = 0,20 × 880 × 50 = 8800 Joule."
    }
  ]
});
