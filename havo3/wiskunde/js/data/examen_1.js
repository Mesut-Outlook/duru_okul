DURU.registerExamen({
  id: "ex-wiskunde-h2-1",
  titel: "Proeftoets 1 — Verhoudingstabel & Cirkeldiagram",
  vak: "Wiskunde · H2 Statistiek",
  icoon: "➗",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Op een jas die normaal € 40,- kost, krijgt Samira € 12,- korting. Hoeveel procent korting is dat?",
      opties: ["25%", "30%", "33,3%", "40%"],
      antwoord: 1,
      uitleg: "(12 ÷ 40) × 100% = 30% korting."
    },
    {
      type: "waaronwaar",
      vraag: "De som van alle sectoren in een cirkeldiagram is bij elkaar altijd 360°.",
      antwoord: true,
      uitleg: "Waar. Een cirkel heeft rondom het middelpunt altijd 360°."
    },
    {
      type: "invul",
      vraag: "Op een oude e-reader van € 109,10 krijgt José € 20,- korting. Hoeveel procent korting is dit? (Rond af op 1 decimaal).",
      antwoord: "18,3%|18,3|18.3%|18.3",
      uitleg: "(20 ÷ 109,10) × 100% = 18,331...% → afgerond 18,3%."
    },
    {
      type: "mc",
      vraag: "Een klas heeft 30 leerlingen. 12 van hen hebben een hond. Hoe groot is de middelpuntshoek van de sector 'hond' in het cirkeldiagram?",
      opties: ["108°", "120°", "144°", "160°"],
      antwoord: 2,
      uitleg: "(12 ÷ 30) × 360° = 144°."
    },
    {
      type: "open",
      vraag: "Een flatscreen televisie kost inclusief 21% btw € 242,-. Leg uit wat de originele prijs van de tv is exclusief btw en bereken dit bedrag.",
      sleutelwoorden: ["200", "121%", "121"],
      minTreffers: 1,
      modelantwoord: "De prijs inclusief 21% btw komt overeen met 121%. De prijs exclusief btw (100%) is 242 ÷ 121 × 100 = € 200,-.",
      uitleg: "Inclusief 21% btw is 121%. 242 ÷ 121 × 100 = € 200,-."
    },
    {
      type: "mc",
      vraag: "Een aquarium van 50 liter is voor 67% gevuld met water. Hoeveel liter water zit er in het aquarium? (Rond af op 1 decimaal).",
      opties: ["30,5 liter", "33,5 liter", "35,0 liter", "37,2 liter"],
      antwoord: 1,
      uitleg: "0,67 × 50 = 33,5 liter water."
    },
    {
      type: "waaronwaar",
      vraag: "Als een sector in een cirkeldiagram een hoek van 90° heeft, stelt dit 25% van de hele cirkel voor.",
      antwoord: true,
      uitleg: "Waar. 90° ÷ 360° = 0,25 = 25%."
    },
    {
      type: "invul",
      vraag: "Een BMX-club heeft 103 leden jonger dan 16 jaar. Dit is 77% van alle clubleden. Hoeveel leden heeft de club in totaal? (Rond af op een geheel getal).",
      antwoord: "134|134 leden",
      uitleg: "103 ÷ 77 × 100 = 133,76... → afgerond 134 leden."
    },
    {
      type: "mc",
      vraag: "Hoeveel graden hoort bij een sector die 15% van het totaal beslaat?",
      opties: ["45°", "54°", "60°", "72°"],
      antwoord: 1,
      uitleg: "0,15 × 360° = 54°."
    },
    {
      type: "open",
      vraag: "Van 120 reizigers gaan er 30 met het vliegtuig, 15 met de bus en 75 met de auto. Bereken de hoek in graden voor de sector 'auto'.",
      sleutelwoorden: ["225", "225°", "225 graden"],
      minTreffers: 1,
      modelantwoord: "(75 ÷ 120) × 360° = 225°.",
      uitleg: "Auto = 75 ÷ 120 × 360° = 225°."
    },
    {
      type: "mc",
      vraag: "Bij een korting van 40% betaalt Margriet € 16,50 voor een trein kaartje. Hoeveel euro was de korting zelf?",
      opties: ["€ 6,60", "€ 9,90", "€ 11,00", "€ 13,20"],
      antwoord: 0,
      uitleg: "Korting = 40% van € 16,50 = 0,40 × 16,50 = € 6,60."
    },
    {
      type: "waaronwaar",
      vraag: "Bij het rekenen met een verhoudingstabel op een rekenmachine mag je tussenuitkomsten tussendoor afronden op 2 decimalen.",
      antwoord: false,
      uitleg: "Onwaar. Tussenantwoorden niet afronden om nauwkeurig te blijven!"
    },
    {
      type: "invul",
      vraag: "In een klas van 25 leerlingen kiezen 10 leerlingen voor gym. Hoeveel graden is de sector 'gym' in het cirkeldiagram?",
      antwoord: "144|144°",
      uitleg: "(10 ÷ 25) × 360° = 144°."
    },
    {
      type: "mc",
      vraag: "Een aantal verandert van 169 naar 242. Met hoeveel procent is het aantal gestegen? (Rond af op 1 decimaal).",
      opties: ["36,2%", "40,5%", "43,2%", "45,0%"],
      antwoord: 2,
      uitleg: "Stijging = 242 - 169 = 73. Procentuele stijging = (73 ÷ 169) × 100% = 43,195...% → 43,2%."
    },
    {
      type: "open",
      vraag: "Aan 800 inwoners is gevraagd naar welke supermarkt ze gaan. 24% kiest voor Albert Heijn. Bereken hoeveel van deze 800 inwoners naar Albert Heijn gaan.",
      sleutelwoorden: ["192", "192 inwoners"],
      minTreffers: 1,
      modelantwoord: "0,24 × 800 = 192 inwoners.",
      uitleg: "24% van 800 = 192 inwoners."
    }
  ]
});
