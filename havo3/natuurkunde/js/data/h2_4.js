/* Onderwerp 2.4 — Energie en vermogen */
DURU.register({
  id: "h2-4-vermogen-energie",
  hoofdstuk: 2,
  paragraaf: "2.4",
  titel: "Elektrisch Vermogen & Energieverbruik",
  korteUitleg: "Vermogen berekenen (P = U·I), energieverbruik in Joule en kWh (E = P·t) en kosten.",
  icoon: "⚡",
  kleur: "h2-thema",
  theorie: "<h3>2.4 Energie en vermogen</h3><div class=\"formule-box\"><strong>Formules:</strong><br>• <b>Vermogen ($P$):</b> $P = U \\cdot I$ (in Watt: $1\\text{ W} = 1\\text{ J/s}$)<br>• <b>Energie in Joule:</b> $E = P \\cdot t$ (met $P$ in Watt en $t$ in seconden)<br>• <b>Energie in kilowattuur:</b> $E = P \\cdot t$ (met $P$ in kW en $t$ in uren)<br>• <b>Omrekenen:</b> $1\\text{ kWh} = 3.600.000\\text{ J} = 3{,}6\\text{ MJ}$<br>• <b>Kosten:</b> $\\text{Kosten} = E\\text{ (in kWh)} \\times \\text{prijs per kWh}$</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid van elektrisch vermogen?",
      opties: ["Watt (W)", "Joule (J)", "Volt (V)", "Ampère (A)"],
      antwoord: 0,
      uitleg: "Vermogen P wordt gemeten in Watt (W)."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Een lamp op 230 V trekt een stroom van 0,5 A. Wat is het vermogen in Watt?",
      antwoord: "115|115 W|115 watt",
      uitleg: "P = U × I = 230 V × 0,5 A = 115 W."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een straalkachel van 2000 W (2 kW) staat 3 uur aan. Hoeveel kWh energie is er verbruikt?",
      antwoord: "6|6 kWh|6,0",
      uitleg: "E = P × t = 2 kW × 3 h = 6 kWh."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Bij een stroomprijs van € 0,35 per kWh, wat kost het verbruik van 6 kWh (in euro's)?",
      antwoord: "2,10|2,1|€ 2,10|€2,10",
      uitleg: "6 kWh × € 0,35 = € 2,10."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "1 kilowattuur (kWh) is gelijk aan 3.600.000 Joule.",
      antwoord: true,
      uitleg: "Waar: 1000 W × 3600 s = 3.600.000 J."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een waterkoker van 1500 W brengt in 120 seconden water aan de kook. Hoeveel kJ elektrische energie is gebruikt?",
      antwoord: "180|180 kJ|180000",
      uitleg: "E = P × t = 1500 W × 120 s = 180.000 J = 180 kJ."
    }
  ]
});
