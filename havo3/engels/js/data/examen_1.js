/* Proeftoets 1 — Engels HAVO 3: grammatica/vocabulaire (vraagstelling in het Nederlands).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-engels-1",
  titel: "Proeftoets 1 — Engels: grammatica & vocabulaire",
  vak: "Engels · HAVO 3",
  icoon: "🇬🇧",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Welke Engelse zin is grammaticaal <b>correct</b>?",
      opties: [
        "She don't like apples.",
        "She doesn't likes apples.",
        "She doesn't like apples.",
        "She not like apples."
      ],
      antwoord: 2,
      uitleg: "Bij 'she' (derde persoon enkelvoud) gebruik je 'doesn't' + het werkwoord zonder -s: 'She doesn't like apples.'"
    },
    {
      type: "mc",
      vraag: "Wat betekent het Engelse woord <b>'therefore'</b>?",
      opties: [
        "daarom",
        "daarnaast",
        "daarvoor",
        "daarna"
      ],
      antwoord: 0,
      uitleg: "'Therefore' betekent 'daarom' — het geeft een gevolg of conclusie aan, bijvoorbeeld: 'It was raining, therefore we stayed home.'"
    },
    {
      type: "waaronwaar",
      vraag: "'Went' is de 'simple past' (verleden tijd) vorm van het werkwoord 'to go'.",
      antwoord: true,
      uitleg: "Waar. 'Go' is een onregelmatig werkwoord: go — went — gone. 'Went' gebruik je voor de simple past."
    },
    {
      type: "invul",
      vraag: "Vul het juiste Engelse werkwoord in: 'I ___ (to be) very tired yesterday.'",
      antwoord: "was",
      uitleg: "'Yesterday' geeft de verleden tijd aan. Bij 'I' (eerste persoon enkelvoud) is de simple past van 'to be' → 'was'."
    },
    {
      type: "open",
      vraag: "Leg in het Nederlands uit wanneer je de <b>present perfect</b> (have/has + voltooid deelwoord) gebruikt in het Engels, en geef een Engelse voorbeeldzin.",
      sleutelwoorden: ["verleden/gebeurtenis/is gebeurd", "nu/heden/gevolg voor nu/resultaat", "voorbeeldzin/have/has"],
      minTreffers: 2,
      modelantwoord: "Je gebruikt de present perfect voor iets dat in het verleden is gebeurd maar nog gevolgen heeft voor nu, of waarvan het precieze tijdstip niet belangrijk is. Voorbeeld: 'I have finished my homework.'",
      uitleg: "Present perfect (have/has + past participle) verbindt het verleden met het heden: de actie is voltooid, maar het resultaat telt nu nog mee. Een correcte Engelse voorbeeldzin met 'have'/'has' + voltooid deelwoord maakt het antwoord compleet."
    }
  ]
});
