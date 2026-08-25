DURU.registerExamen({
  id: "ex-wiskunde-h2-4",
  titel: "Proeftoets 4 — Gemengde Proeftoets Statistiek",
  vak: "Wiskunde · H2 Statistiek",
  icoon: "📊",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Een T-shirt kost met 35% korting € 8,95. Hoeveel procent hoort bij de prijs die Josien betaalt?",
      opties: ["35%", "65%", "100%", "135%"],
      antwoord: 1,
      uitleg: "100% - 35% korting = 65%."
    },
    {
      type: "waaronwaar",
      vraag: "De middelpuntshoek van een sector bereken je met de formule: (percentage ÷ 100) × 360°.",
      antwoord: true,
      uitleg: "Waar. (percentage ÷ 100) × 360° geeft de hoek van de sector."
    },
    {
      type: "invul",
      vraag: "Op een sportschool doen 40 leerlingen aan voetbal, 28 aan volleybal en 22 aan basketbal. Hoeveel graden is de sector 'voetbal' in een cirkeldiagram?",
      antwoord: "160|160°",
      uitleg: "Totaal = 40 + 28 + 22 = 90 leerlingen. Voetbal = (40 ÷ 90) × 360° = 160°."
    },
    {
      type: "mc",
      vraag: "Hoe noem je een tabel waarin vermeld staat hoe vaak elke waarde voorkomt?",
      opties: ["Verhoudingstabel", "Frequentietabel", "Kruistabel", "Steelbladdiagram"],
      antwoord: 1,
      uitleg: "Een frequentietabel vermeldt de frequenties van waarden."
    },
    {
      type: "open",
      vraag: "Josien krijgt € 11,02 korting op een trui. Dit is 24% van de normale prijs. Bereken de normale prijs van de trui in euro's.",
      sleutelwoorden: ["45,92", "45,92 euro", "45.92"],
      minTreffers: 1,
      modelantwoord: "11,02 ÷ 24 × 100 = € 45,916... → afgerond € 45,92.",
      uitleg: "11,02 ÷ 24 × 100 = € 45,92."
    },
    {
      type: "mc",
      vraag: "Gegeven cijfers: 5, 6, 7, 7, 8. Wat is het gemiddelde?",
      opties: ["6,4", "6,6", "6,8", "7,0"],
      antwoord: 1,
      uitleg: "(5 + 6 + 7 + 7 + 8) ÷ 5 = 33 ÷ 5 = 6,6."
    },
    {
      type: "waaronwaar",
      vraag: "De mediaan van een oneven aantal geordende getallen is het exacte middelste getal.",
      antwoord: true,
      uitleg: "Waar. Bij oneven n is de mediaan de middelste waarde."
    },
    {
      type: "invul",
      vraag: "In een steelbladdiagram staan bij steel 17 de bladeren: 0, 0, 1, 4, 8. Uit hoeveel metingen bestaat deze steel?",
      antwoord: "5",
      uitleg: "5 bladeren = 5 metingen."
    },
    {
      type: "mc",
      vraag: "In januari stonden er in een gemeente 17.613 koopwoningen, wat 73,8% van alle woningen was. Hoeveel woningen stonden er in totaal? (Rond af op een geheel getal).",
      opties: ["22.500", "23.866", "24.110", "25.000"],
      antwoord: 1,
      uitleg: "17.613 ÷ 73,8 × 100 = 23.865,85... → afgerond 23.866 woningen."
    },
    {
      type: "open",
      vraag: "Leg uit hoe je bij een frequentietabel de gemiddelde waarde berekenen kunt.",
      sleutelwoorden: ["vermenigvuldig", "keer", "som", "delen"],
      minTreffers: 1,
      modelantwoord: "Vermenigvuldig elke waarde met zijn frequentie, tel alle uitkomsten bij elkaar op en deel deze totale som door de som van alle frequenties.",
      uitleg: "(∑ waarde × freq) ÷ (∑ freq)."
    },
    {
      type: "mc",
      vraag: "Wat stelt de steel in een steelbladdiagram meestal voor als het om gewichten van 45 g tot 68 g gaat?",
      opties: ["Honderdtallen", "Tientallen", "Eenheden", "Decimalen"],
      antwoord: 1,
      uitleg: "De steel bevat de tientallen (4, 5, 6) en de bladeren de eenheden."
    },
    {
      type: "waaronwaar",
      vraag: "Een lijndiagram is minder geschikt dan een staafdiagram om losse categorieën fruit te vergelijken.",
      antwoord: true,
      uitleg: "Waar. Categorieën fruit hebben geen continu tijdsverloop, dus een staafdiagram is daar beter voor."
    },
    {
      type: "invul",
      vraag: "In een klas zijn 4 BMX-rijders, wat 14,8% van de klas is. Hoeveel leerlingen zitten er in de klas? (Rond af op een geheel getal).",
      antwoord: "27|27 leerlingen",
      uitleg: "4 ÷ 14,8 × 100 = 27,02... → 27 leerlingen."
    },
    {
      type: "mc",
      vraag: "Gegeven de cijfers: 4, 6, 7, 8, 9, 10. Wat is de mediaan?",
      opties: ["7", "7,5", "8", "8,5"],
      antwoord: 1,
      uitleg: "(7 + 8) ÷ 2 = 7,5."
    },
    {
      type: "open",
      vraag: "Bereken de hoek in graden voor een sector die 40% van een cirkeldiagram beslaat.",
      sleutelwoorden: ["144", "144°", "144 graden"],
      minTreffers: 1,
      modelantwoord: "0,40 × 360° = 144°.",
      uitleg: "0,40 × 360° = 144°."
    }
  ]
});
