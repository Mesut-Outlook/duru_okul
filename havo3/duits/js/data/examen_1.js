/* Proeftoets 1 — Duits HAVO 3: basiswoorden/grammatica (vraagstelling in het Nederlands).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-duits-1",
  titel: "Proeftoets 1 — Duits: basiswoorden & grammatica",
  vak: "Duits · HAVO 3",
  icoon: "🇩🇪",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Wat betekent het Duitse woord <b>'das Haus'</b>?",
      opties: [
        "de auto",
        "het huis",
        "de school",
        "de tuin"
      ],
      antwoord: 1,
      uitleg: "'Das Haus' betekent 'het huis'. Het is een onzijdig woord, dus 'das' en niet 'der' of 'die'."
    },
    {
      type: "mc",
      vraag: "Welke vorm van <b>'sein'</b> (zijn) hoort bij 'wir' (wij)?",
      opties: [
        "bist",
        "ist",
        "sind",
        "seid"
      ],
      antwoord: 2,
      uitleg: "'Wir sind' betekent 'wij zijn'. Volledig: ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind."
    },
    {
      type: "waaronwaar",
      vraag: "In het Duits schrijf je alle zelfstandige naamwoorden met een hoofdletter.",
      antwoord: true,
      uitleg: "Waar. Anders dan in het Nederlands krijgen álle zelfstandige naamwoorden in het Duits een hoofdletter: der Hund, die Schule, das Buch."
    },
    {
      type: "invul",
      vraag: "Het Duitse woord voor 'kat' is … .",
      antwoord: "katze|die katze|eine katze",
      uitleg: "'Katze' (vrouwelijk woord: die Katze) betekent 'kat'. Let op de hoofdletter: Katze."
    },
    {
      type: "open",
      vraag: "Leg uit wat de <b>vier naamvallen</b> in het Duits zijn en waar je de <b>Akkusativ</b> voor gebruikt. Geef een voorbeeldzin.",
      sleutelwoorden: [
        "Nominativ/nominatief/1e naamval",
        "Akkusativ/accusatief/4e naamval/lijdend voorwerp",
        "voorbeeldzin/voorbeeld/den"
      ],
      minTreffers: 2,
      modelantwoord: "Duits heeft vier naamvallen: Nominativ (onderwerp), Akkusativ (lijdend voorwerp), Dativ (meewerkend voorwerp) en Genitiv (bezit). De Akkusativ gebruik je voor het lijdend voorwerp. Voorbeeld: 'Ich sehe den Hund.' (Ik zie de hond.) — 'der Hund' wordt 'den Hund'.",
      uitleg: "Het belangrijkste is dat je weet dat de Akkusativ bij het lijdend voorwerp hoort en dat 'der' dan 'den' wordt. Een goede voorbeeldzin laat zien dat je het snapt."
    }
  ]
});
