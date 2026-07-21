/* Proeftoets 1 — Frans HAVO 3: basiswoorden/grammatica (vraagstelling in het Nederlands).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-frans-1",
  titel: "Proeftoets 1 — Frans: basiswoorden & grammatica",
  vak: "Frans · HAVO 3",
  icoon: "🇫🇷",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Wat betekent het Franse woord <b>'la maison'</b>?",
      opties: [
        "de auto",
        "het huis",
        "de school",
        "de tuin"
      ],
      antwoord: 1,
      uitleg: "'La maison' betekent 'het huis'. Let op: het is een vrouwelijk woord, dus 'la' en niet 'le'."
    },
    {
      type: "mc",
      vraag: "Welke vorm van <b>'être'</b> (zijn) hoort bij 'nous' (wij)?",
      opties: [
        "es",
        "est",
        "sommes",
        "êtes"
      ],
      antwoord: 2,
      uitleg: "'Nous sommes' betekent 'wij zijn'. Volledig: je suis, tu es, il/elle est, nous sommes, vous êtes, ils/elles sont."
    },
    {
      type: "waaronwaar",
      vraag: "'Bonjour' betekent 'goedenavond' in het Frans.",
      antwoord: false,
      uitleg: "Onwaar. 'Bonjour' betekent 'goedendag/hallo'. 'Goedenavond' is 'bonsoir'."
    },
    {
      type: "invul",
      vraag: "Het Franse woord voor 'kat' is … .",
      antwoord: "chat|le chat|un chat",
      uitleg: "'Chat' (mannelijk woord: le chat) betekent 'kat'. Een vrouwelijke kat is 'la chatte'."
    },
    {
      type: "open",
      vraag: "Leg uit hoe je in het Frans een zin <b>ontkennend</b> maakt (bijvoorbeeld 'ik eet niet'), en geef een voorbeeldzin met 'ne...pas'.",
      sleutelwoorden: ["ne...pas/ne/pas", "voor en na het werkwoord/rond het werkwoord/om het werkwoord heen", "voorbeeldzin/voorbeeld"],
      minTreffers: 2,
      modelantwoord: "In het Frans zet je 'ne' vóór het werkwoord en 'pas' erna, zodat het werkwoord tussen 'ne' en 'pas' in staat. Voorbeeld: 'Je ne mange pas.' (Ik eet niet.)",
      uitleg: "De basisstructuur voor ontkenning in het Frans is 'ne + werkwoord + pas'. Een correcte voorbeeldzin (zoals 'Je ne mange pas' of 'Il ne parle pas') laat zien dat je het snapt."
    }
  ]
});
