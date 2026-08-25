DURU.registerExamen({
  id: "ex-wiskunde-h2-2",
  titel: "Proeftoets 2 — Frequentietabellen & Grafieken",
  vak: "Wiskunde · H2 Statistiek",
  icoon: "📈",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat geeft het woord 'frequentie' in een frequentietabel aan?",
      opties: [
        "De middelste waarde",
        "Het aantal keren dat een bepaalde waarde voorkomt",
        "De stijging in procenten",
        "Het gemiddelde van de verzameling"
      ],
      antwoord: 1,
      uitleg: "Frequentie = het aantal keren dat een waarde voorkomt."
    },
    {
      type: "waaronwaar",
      vraag: "Een lijndiagram is vooral geschikt om te laten zien hoe aantallen in de loop van de tijd veranderen.",
      antwoord: true,
      uitleg: "Waar. Een lijndiagram toont de ontwikkeling over de tijd (tijdverloop)."
    },
    {
      type: "invul",
      vraag: "Sandra haalde voor wiskunde de cijfers: 7, 5, 8, 6, 6, 7, 5, 7, 7, 6. Wat is de frequentie van het cijfer 7?",
      antwoord: "4",
      uitleg: "Het cijfer 7 komt precies 4 keer voor."
    },
    {
      type: "mc",
      vraag: "Arjan verkocht 85 racefietsen van Cannondale, 57 van Felt, 115 van Giant, 97 van Specialized en 72 van Trek. Wat is het totale aantal verkochte racefietsen uit deze top 5?",
      opties: ["386", "412", "426", "450"],
      antwoord: 2,
      uitleg: "85 + 57 + 115 + 97 + 72 = 426 racefietsen."
    },
    {
      type: "open",
      vraag: "Leg het verschil uit tussen de manier waarop de staven in een staafdiagram worden getekend ten opzichte van een histogram.",
      sleutelwoorden: ["los", "ruimte", "tussen", "afstand"],
      minTreffers: 1,
      modelantwoord: "In een staafdiagram staan de staven los van elkaar met ruimte ertussen, omdat de categorieën losstaande gegevens representeren.",
      uitleg: "Bij een staafdiagram staan staven los van elkaar."
    },
    {
      type: "mc",
      vraag: "In het eerste kwartaal werden per maand de volgende pakken sap verkocht: Jan (120), Feb (150), Maart (180). Hoeveel pakken zijn in het 1e kwartaal totaal verkocht?",
      opties: ["350", "420", "450", "480"],
      antwoord: 2,
      uitleg: "120 + 150 + 180 = 450 pakken sap."
    },
    {
      type: "waaronwaar",
      vraag: "In een staafdiagram kun je op de verticale as altijd de frequenties (aantallen) aflezen.",
      antwoord: true,
      uitleg: "Waar. De verticale as geeft de frequenties of aantallen aan."
    },
    {
      type: "invul",
      vraag: "Teun heeft 15 blauwe, 22 rode en 17 gele knikkers. Wat is de frequentie van de rode knikkers?",
      antwoord: "22",
      uitleg: "Rode knikkers = 22."
    },
    {
      type: "mc",
      vraag: "Bij de WK-wedstrijden maakte de Nederlandse handbalploeg de volgende doelpunten: 26, 35, 51, 36, 30, 23, 24, 40, 33, 30. Bereken het gemiddeld aantal doelpunten per wedstrijd.",
      opties: ["30,8", "32,8", "34,2", "35,0"],
      antwoord: 1,
      uitleg: "Som = 328. Totaal 10 wedstrijden. Gemiddelde = 328 ÷ 10 = 32,8."
    },
    {
      type: "open",
      vraag: "Een leerling heeft cijfers: 5, 6, 6, 7, 7, 7, 8, 9. Bereken het gemiddelde en rond af op 2 decimalen.",
      sleutelwoorden: ["6,88", "6.88"],
      minTreffers: 1,
      modelantwoord: "Som = 5+6+6+7+7+7+8+9 = 55. Aantal = 8. Gemiddelde = 55 ÷ 8 = 6,875 → afgerond 6,88.",
      uitleg: "55 ÷ 8 = 6,875 → 6,88."
    },
    {
      type: "mc",
      vraag: "Wat is de modus van de cijfers: 5, 6, 6, 7, 7, 7, 8, 9?",
      opties: ["6", "7", "7,5", "8"],
      antwoord: 1,
      uitleg: "Het cijfer 7 komt het vaakst voor (3 keer), dus de modus is 7."
    },
    {
      type: "waaronwaar",
      vraag: "Als je de mediaan van 10 getallen berekent, neem je het 5e getal nadat je ze op volgorde van klein naar groot hebt gezet.",
      antwoord: false,
      uitleg: "Onwaar. Bij 10 (even) getallen neem je het gemiddelde van het 5e en 6e getal!"
    },
    {
      type: "invul",
      vraag: "Gegeven de gewichten van 5 kalfjes: 35 kg, 37 kg, 38 kg, 40 kg, 40 kg. Wat is het gemiddelde gewicht in kg?",
      antwoord: "38|38 kg",
      uitleg: "(35 + 37 + 38 + 40 + 40) ÷ 5 = 190 ÷ 5 = 38 kg."
    },
    {
      type: "mc",
      vraag: "Op hoeveel dagen is de temperatuur gemeten als de frequentietabel 5 dagen 14°C, 8 dagen 15°C en 3 dagen 16°C vermeldt?",
      opties: ["14 dagen", "15 dagen", "16 dagen", "18 dagen"],
      antwoord: 2,
      uitleg: "Totale frequentie = 5 + 8 + 3 = 16 dagen."
    },
    {
      type: "open",
      vraag: "Gegeven de getallenrij: 3, 5, 7, 8, 12. Wat is de mediaan van deze rij?",
      sleutelwoorden: ["7"],
      minTreffers: 1,
      modelantwoord: "De rij bestaat uit 5 getallen (oneven). Het 3e getal is de mediaan, dus 7.",
      uitleg: "Het middelste (3e) getal is 7."
    }
  ]
});
