/* Onderwerp 2.3 — Serie en parallel */
DURU.register({
  id: "h2-3-serie-parallel",
  hoofdstuk: 2,
  paragraaf: "2.3",
  titel: "Serie- en Parallelschakelingen",
  korteUitleg: "Stroom- en spanningsverdeling, vervangingsweerstand en huisinstallaties.",
  icoon: "🔌",
  kleur: "h2-thema",
  theorie: "<h3>2.3 Serie en parallel</h3><div class=\"formule-box\"><strong>Serieschakeling:</strong><br>• $I_{tot} = I_1 = I_2 = \\dots$ (stroom overal gelijk)<br>• $U_{tot} = U_1 + U_2 + \\dots$ (spanning verdeelt zich)<br>• $R_{tot} = R_1 + R_2 + \\dots$ (weerstanden tellen op)<br><br><strong>Parallelschakeling:</strong><br>• $U_{tot} = U_1 = U_2 = \\dots$ (spanning overal gelijk)<br>• $I_{tot} = I_1 + I_2 + \\dots$ (hoofdstroom is som van takstromen)<br>• Totale weerstand daalt: $\\frac{1}{R_{tot}} = \\frac{1}{R_1} + \\frac{1}{R_2}$ of $R_{tot} = \\frac{U}{I_{tot}}$</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat geldt voor de spanning in een parallelschakeling?",
      opties: ["De spanning is over elke tak gelijk", "De spanning verdeelt zich", "De spanning is overal nul", "De grootste weerstand krijgt de meeste spanning"],
      antwoord: 0,
      uitleg: "In parallel staat over elke tak direct de volledige bronspanning."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Twee weerstanden van 40 Ω en 60 Ω staan in serie. Wat is de totale vervangingsweerstand in Ohm?",
      antwoord: "100|100 Ω|100 ohm",
      uitleg: "R_tot = 40 + 60 = 100 Ω."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Twee gelijke lampjes van elk 50 Ω staan parallel. Wat is de vervangingsweerstand in Ohm?",
      antwoord: "25|25 Ω|25 ohm",
      uitleg: "R_tot = 50 / 2 = 25 Ω."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat gebeurt er als één lampje in een serieschakeling kapotgaat?",
      opties: ["De rest brandt feller", "Alle lampjes gaan uit", "De rest blijft gewoon branden", "Er ontstaat kortsluiting"],
      antwoord: 1,
      uitleg: "De stroomkring is onderbroken, dus alle lampjes gaan uit."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In huis zijn alle stopcontacten parallel aangesloten zodat elk apparaat 230 V krijgt.",
      antwoord: true,
      uitleg: "Waar: parallel garandeert 230 V voor elk apparaat en onafhankelijke bediening."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "In een parallelschakeling op 12 V loopt door tak 1 een stroom van 1,5 A en door tak 2 een stroom van 2,5 A. Bereken de totale vervangingsweerstand R_tot in Ohm.",
      antwoord: "3|3 Ω|3 ohm|3,0",
      uitleg: "I_tot = 1,5 + 2,5 = 4,0 A. R_tot = U / I_tot = 12 V / 4,0 A = 3,0 Ω."
    }
  ]
});
