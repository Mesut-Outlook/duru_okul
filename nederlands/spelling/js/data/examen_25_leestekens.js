DURU.registerExamen({
  id: "ex-sp-25",
  titel: "Proeftoets 25 — Leestekens & interpunctie",
  vak: "Nederlands Spelling",
  icoon: "✍️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Welke zin heeft een correcte komma?",
      opties: [
        "Omdat het regende, bleef Duru thuis.",
        "Omdat het regende bleef, Duru thuis.",
        "Omdat, het regende bleef Duru thuis."
      ],
      antwoord: 0,
      uitleg: "Als de bijzin <i>voor</i> de hoofdzin staat, zet je een komma tussen bijzin en hoofdzin: <b>Omdat het regende, bleef Duru thuis.</b>"
    },
    {
      type: "waaronwaar",
      vraag: "Bij een opsomming van drie of meer items zet je een komma na elk item, ook voor het laatste 'en'.",
      antwoord: false,
      uitleg: "Onwaar: in het Nederlands zet je gewoonlijk <i>geen</i> komma voor het laatste <b>en</b> in een opsomming: <b>appels, peren en bananen</b>."
    },
    {
      type: "mc",
      vraag: "Welk leesteken gebruik je om twee nauw verwante zinnen samen te voegen zonder voegwoord?",
      opties: ["een komma (,)", "een puntkomma (;)", "een dubbele punt (:)"],
      antwoord: 1,
      uitleg: "Een <b>puntkomma (;)</b> gebruik je om twee verwante zinnen samen te voegen die toch een zekere zelfstandigheid hebben: <i>Het was laat; toch ging hij nog even lopen.</i>"
    },
    {
      type: "invul",
      vraag: "Welk leesteken gebruik je vóór een opsomming of een uitleg? (schrijf het leesteken als woord: 'dubbele punt', 'puntkomma' of 'komma')",
      antwoord: "dubbele punt",
      uitleg: "De <b>dubbele punt (:)</b> gebruik je vóór een opsomming of een uitleg: <i>Ik heb drie vakken: wiskunde, Nederlands en geschiedenis.</i>"
    },
    {
      type: "mc",
      vraag: "Welke zin is correct gespeld?",
      opties: [
        "Heb jij al gegeten.",
        "Heb jij al gegeten?",
        "Heb jij al gegeten!"
      ],
      antwoord: 1,
      uitleg: "Een vraagzin eindigt altijd met een <b>vraagteken (?)</b>. Een punt of uitroepteken is hier fout."
    },
    {
      type: "waaronwaar",
      vraag: "In de zin 'Kijk uit!' is het uitroepteken correct gebruikt.",
      antwoord: true,
      uitleg: "Waar: een <b>uitroepteken (!)</b> gebruik je bij een bevel, uitroep of sterke emotie: <b>Kijk uit!</b>, Stop!, Wat geweldig!"
    },
    {
      type: "mc",
      vraag: "Welke zin heeft de juiste komma bij een bijvoeglijke bijzin?",
      opties: [
        "De fiets die ik gisteren kocht is al kapot.",
        "De fiets, die ik gisteren kocht, is al kapot.",
        "De, fiets die ik gisteren kocht is al kapot."
      ],
      antwoord: 1,
      uitleg: "Een bijvoeglijke bijzin die niet noodzakelijk is (toevoegend) wordt tussen komma's geplaatst: <b>De fiets, die ik gisteren kocht, is al kapot.</b>"
    },
    {
      type: "invul",
      vraag: "Maak de opsomming correct af met een leesteken: 'Ik kocht appels, peren en bananen___' (punt, komma of vraagteken?)",
      antwoord: ".",
      uitleg: "Een zin die geen vraag of uitroep is, eindigt met een <b>punt (.)</b>. Hier is het een gewone mededeling."
    },
    {
      type: "mc",
      vraag: "Welke zin is correct?",
      opties: [
        "Hij vroeg of ik mee wilde komen.",
        "Hij vroeg of ik mee wilde komen?",
        "Hij vroeg: of ik mee wilde komen."
      ],
      antwoord: 0,
      uitleg: "Bij een indirecte vraagzin (zonder aanhalingstekens) gebruik je een <b>punt</b>, geen vraagteken: <b>Hij vroeg of ik mee wilde komen.</b>"
    },
    {
      type: "waaronwaar",
      vraag: "De zin 'Duru, let op!' bevat een zogenaamde aanspreking. De komma achter 'Duru' is hier correct.",
      antwoord: true,
      uitleg: "Waar: een aanspreking (vocatief) wordt altijd door komma's omgeven: <b>Duru, let op!</b> of <i>Let op, Duru!</i>"
    },
    {
      type: "mc",
      vraag: "Welke zin gebruikt de dubbele punt correct?",
      opties: [
        "Ik weet het antwoord: 42.",
        "Ik weet: het antwoord 42.",
        "Ik weet het: antwoord is 42."
      ],
      antwoord: 0,
      uitleg: "De <b>dubbele punt</b> staat vóór het aangekondigde antwoord of de uitleg: <b>Ik weet het antwoord: 42.</b>"
    }
  ]
});
