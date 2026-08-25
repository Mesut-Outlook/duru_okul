DURU.registerExamen({
  id: "ex-wiskunde-h2-3",
  titel: "Proeftoets 3 — Centrummaten & Steelbladdiagram",
  vak: "Wiskunde · H2 Statistiek",
  icoon: "📐",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Welke centrummaat bereken je door de totale som van alle waarden te delen door het aantal waarden?",
      opties: ["Modus", "Mediaan", "Gemiddelde", "Spreidingsbreedte"],
      antwoord: 2,
      uitleg: "Het gemiddelde = totale som ÷ aantal waarden."
    },
    {
      type: "waaronwaar",
      vraag: "In een steelbladdiagram vormen de getallen aan de linkerkant van de verticale streep de steel en aan de rechterkant de bladeren.",
      antwoord: true,
      uitleg: "Waar. Links is de steel, rechts zijn de bladeren."
    },
    {
      type: "invul",
      vraag: "Bij steel 15 staan de bladeren: 2, 5, 8. Welke drie lengten in cm stelt dit voor als de steel de tientallen zijn?",
      antwoord: "152, 155, 158|152 155 158|152,155,158",
      uitleg: "Steel 15 met bladeren 2, 5, 8 geeft 152 cm, 155 cm ve 158 cm."
    },
    {
      type: "mc",
      vraag: "Wat is de mediaan van de rij getallen: 4, 7, 9, 11, 15, 18, 20?",
      opties: ["9", "11", "13", "15"],
      antwoord: 1,
      uitleg: "7 getallen (oneven). Het 4e getal is 11."
    },
    {
      type: "open",
      vraag: "In een steelbladdiagram staan bij steel 16 de bladeren: 3, 3, 4, 7. Geef de modus van deze lengten.",
      sleutelwoorden: ["163", "163 cm"],
      minTreffers: 1,
      modelantwoord: "Het blad 3 komt bij steel 16 het vaakst voor (2 keer), dus de modus is 163 cm.",
      uitleg: "163 komt het vaakst voor."
    },
    {
      type: "mc",
      vraag: "Een rij bestaat uit de getallen: 6, 8, 10, 12. Wat is de mediaan van deze 4 getallen?",
      opties: ["8", "9", "10", "11"],
      antwoord: 1,
      uitleg: "Even aantal getallen (4). Mediaan = (8 + 10) ÷ 2 = 9."
    },
    {
      type: "waaronwaar",
      vraag: "De bladeren achter een steel in een steelbladdiagram hoeven niet op volgorde te staan.",
      antwoord: false,
      uitleg: "Onwaar. De bladeren worden per steel altijd netjes van klein naar groot gesorteerd!"
    },
    {
      type: "invul",
      vraag: "Joost telt eieren in koolmeesnesten: 6, 8, 8, 10, 12, 12, 7, 8, 9, 10. Wat is de modus van het aantal eieren?",
      antwoord: "8",
      uitleg: "Het getal 8 komt 3 keer voor (het vaakst)."
    },
    {
      type: "mc",
      vraag: "In een klas scoren 3 leerlingen een 5, 8 leerlingen een 6, 7 leerlingen een 7 en 2 leerlingen een 8. Uit hoeveel leerlingen bestaat deze klas?",
      opties: ["18", "20", "22", "25"],
      antwoord: 1,
      uitleg: "Totale frequentie = 3 + 8 + 7 + 2 = 20 leerlingen."
    },
    {
      type: "open",
      vraag: "In een steelbladdiagram staan 15 gewichten van appels in grammen. De steel zijn de tientallen. Bij steel 4 staan bladeren: 5, 7, 8. Bij steel 5 staan: 2, 2, 3, 6, 8. Bij steel 6 staan: 1, 4. Wat is de massa van de zwaarste appel?",
      sleutelwoorden: ["64", "64 gram", "64g"],
      minTreffers: 1,
      modelantwoord: "Grootste steel is 6 met grootste blad 4 → 64 gram.",
      uitleg: "Steel 6 + blad 4 = 64 gram."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de mediaan als je aan een rij van 10 getallen één heel hoog getal toevoegt?",
      opties: [
        "De mediaan stijgt heel erg sterk",
        "De mediaan schuift hooguit één positie opschuiven naar de volgende waarde",
        "De mediaan verandert gegarandeerd niet",
        "De mediaan wordt gelijk aan het gemiddelde"
      ],
      antwoord: 1,
      uitleg: "De mediaan is anders dan het gemiddelde niet erg gevoelig voor uitschieters en schuift hooguit één plek op."
    },
    {
      type: "waaronwaar",
      vraag: "Als in een frequentietabel de hoogste frequentie 14 is bij de waarde 7, dan is de modus gelijk aan 7.",
      antwoord: true,
      uitleg: "Waar. De modus is de waarde met de hoogste frequentie (waarde 7)."
    },
    {
      type: "invul",
      vraag: "Bereken de gemiddelde lengte in cm van de meisjes met lengten: 150 cm, 155 cm, 160 cm, 165 cm, 170 cm.",
      antwoord: "160|160 cm",
      uitleg: "Som = 800. 800 ÷ 5 = 160 cm."
    },
    {
      type: "mc",
      vraag: "Hoeveel bladeren staan er in totaal in een steelbladdiagram van een klas met 28 leerlingen?",
      opties: ["14", "28", "56", "Afhankelijk van de stelen"],
      antwoord: 1,
      uitleg: "Elke leerling heeft precies 1 blad, dus in totaal 28 bladeren."
    },
    {
      type: "open",
      vraag: "Gegeven de getallen: 4, 5, 7, y, 5, 7, 6, 4, 5, 6, 3, 6. Geef een waarde voor y zodat er geen modus is.",
      sleutelwoorden: ["4", "7"],
      minTreffers: 1,
      modelantwoord: "Als y = 4 of y = 7, komen 4, 5, 6 en 7 allemaal even vaak (3 keer) voor, waardoor er geen unieke modus is.",
      uitleg: "Bij y = 4 of y = 7 hebben alle waarden frequentie 3, dus geen unieke modus."
    }
  ]
});
