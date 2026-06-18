/* Extra Proeftoets 13 — Ambtenaren & de Drie Overheidslagen */
DURU.registerExamen({
  id: "ex-extra-overheidslagen",
  titel: "Extra Proeftoets 13 — Ambtenaren & de Drie Overheidslagen",
  vak: "Economie · De Overheid",
  icoon: "🗂️",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is een ambtenaar?",
      opties: [
        "Iemand die een eigen bedrijf runt",
        "Iemand die in dienst is van de overheid",
        "Iemand die werkt bij een privé-pretpark",
        "Iemand die games maakt bij een ICT-bedrijf"
      ],
      antwoord: 1,
      uitleg: "Een **ambtenaar** is een werknemer die in dienst is van de **overheid**, zoals het Rijk, de provincie of de gemeente."
    },
    {
      type: "mc",
      vraag: "Welke van deze personen is GEEN ambtenaar?",
      opties: [
        "Een politieagent",
        "Een leraar op een openbare school",
        "Een medewerker van het gemeentehuis",
        "Een medewerker van een ICT-bedrijf dat games maakt"
      ],
      antwoord: 3,
      uitleg: "Een medewerker van een **ICT-bedrijf** werkt niet voor de overheid en is dus geen **ambtenaar**."
    },
    {
      type: "mc",
      vraag: "Welke drie lagen heeft de Nederlandse overheid?",
      opties: [
        "Rijk, provincie en gemeente",
        "Koning, premier en burgemeester",
        "Politie, leger en brandweer",
        "Rijk, stad en dorp"
      ],
      antwoord: 0,
      uitleg: "De overheid bestaat uit drie lagen: het **Rijk**, de **provincie** en de **gemeente**."
    },
    {
      type: "mc",
      vraag: "Hoeveel provincies heeft Nederland?",
      opties: [
        "10",
        "12",
        "14",
        "16"
      ],
      antwoord: 1,
      uitleg: "Nederland heeft **12 provincies**."
    },
    {
      type: "mc",
      vraag: "Wie vormen het college van B en W van een gemeente?",
      opties: [
        "De burgemeester en de wethouders",
        "De gemeenteraad en de premier",
        "De ministers en de koning",
        "De raadsleden en de Commissaris van de Koning"
      ],
      antwoord: 0,
      uitleg: "Het **college van B en W** bestaat uit de **burgemeester en de wethouders**."
    },
    {
      type: "mc",
      vraag: "Welke taak regelt de provincie?",
      opties: [
        "Het ophalen van huisvuil",
        "Paspoorten en rijbewijzen uitgeven",
        "Het openbaar vervoer en de infrastructuur (zoals wegen en vliegvelden)",
        "Het bouwen van scholen"
      ],
      antwoord: 2,
      uitleg: "De **provincie** regelt onder andere het **openbaar vervoer** en de infrastructuur, zoals wegen, vliegvelden en havens."
    },
    {
      type: "waaronwaar",
      vraag: "De gemeenteraad wordt gekozen door de inwoners van de gemeente.",
      antwoord: true,
      uitleg: "Waar. De **gemeenteraad** wordt rechtstreeks gekozen door de inwoners."
    },
    {
      type: "waaronwaar",
      vraag: "Een wethouder is een raadslid dat in de gemeenteraad zit.",
      antwoord: false,
      uitleg: "Onwaar. Een **wethouder** is een bestuurder in het college van B en W; een raadslid zit in de **gemeenteraad**."
    },
    {
      type: "waaronwaar",
      vraag: "De gemeente is de overheidslaag die het dichtst bij de burger staat.",
      antwoord: true,
      uitleg: "Waar. De **gemeente** regelt zaken zoals paspoorten, vuilnis en riolering en staat het dichtst bij de inwoners."
    },
    {
      type: "waaronwaar",
      vraag: "Jeugdzorg is een taak die door de provincie wordt geregeld.",
      antwoord: false,
      uitleg: "Onwaar. **Jeugdzorg** is een taak van de **gemeente**, niet van de provincie."
    },
    {
      type: "invul",
      vraag: "Een werknemer die in dienst is van de overheid heet een _______.",
      antwoord: "ambtenaar",
      uitleg: "Zo'n werknemer heet een **ambtenaar**."
    },
    {
      type: "invul",
      vraag: "Na de gemeenteraadsverkiezingen wordt een nieuw college van B en _______ gevormd.",
      antwoord: "W",
      uitleg: "Na de verkiezingen wordt een nieuw **college van B en W** gevormd."
    },
    {
      type: "invul",
      vraag: "Defensie (het leger) is een taak van het _______ (de overheidslaag in Den Haag).",
      antwoord: "Rijk|rijk|de rijksoverheid|rijksoverheid",
      uitleg: "**Defensie** is een taak van het **Rijk**."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen de gemeenteraad en het college van B en W.",
      sleutelwoorden: ["gemeenteraad/gekozen door inwoners", "B en W/wethouders/burgemeester", "controleert/controleren", "bestuurders/uitvoeren"],
      minTreffers: 2,
      modelantwoord: "De gemeenteraad wordt gekozen door de inwoners en controleert de plannen van het college van B en W. Het college van B en W, met de burgemeester en de wethouders als bestuurders, bestuurt de gemeente.",
      uitleg: "De gemeenteraad controleert; het college van B en W (burgemeester + wethouders) bestuurt."
    },
    {
      type: "open",
      vraag: "Geef voor drie van deze taken aan welke overheidslaag (Rijk, provincie of gemeente) hiervoor verantwoordelijk is: defensie, drinkwatervoorziening, jeugdzorg, openbaar vervoer, ophalen huisvuil, politie.",
      sleutelwoorden: ["Rijk/defensie/politie", "provincie/drinkwater/openbaar vervoer", "gemeente/jeugdzorg/huisvuil"],
      minTreffers: 2,
      modelantwoord: "Defensie en politie zijn taken van het Rijk. Drinkwatervoorziening en openbaar vervoer zijn taken van de provincie. Jeugdzorg en het ophalen van huisvuil zijn taken van de gemeente.",
      uitleg: "Rijk: defensie, politie. Provincie: drinkwater, openbaar vervoer. Gemeente: jeugdzorg, huisvuil."
    }
  ]
});
