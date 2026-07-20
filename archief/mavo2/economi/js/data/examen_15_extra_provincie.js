/* Extra Proeftoets 10 — De Provincie & Ruimtelijke Ordening */
DURU.registerExamen({
  id: "ex-extra-provincie-ruimte",
  titel: "Extra Proeftoets 10 — De Provincie & Ruimtelijke Ordening",
  vak: "Economie · Provincie",
  icoon: "🗺️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de belangrijkste taak van het provinciebestuur?",
      opties: [
        "Het uitgeven van paspoorten en rijbewijzen.",
        "De ruimtelijke ordening (zoals de indeling van natuur, landbouw, industrie en wegen buiten de bebouwde kom).",
        "Het bepalen van het minimumloon.",
        "Het controleren van de Rijksbegroting."
      ],
      antwoord: 1,
      uitleg: "De **provincie** richt zich vooral op ruimtelijke inrichting, natuurbeheer, milieu en het onderhoud van provinciale wegen en fietspaden."
    },
    {
      type: "mc",
      vraag: "Hoe heten de leden van de volksvertegenwoordiging in de provincie die om de 4 jaar door de burgers worden gekozen?",
      opties: [
        "Gedeputeerde Staten",
        "Provinciale Staten",
        "De gemeenteraad",
        "Het Waterschapsbestuur"
      ],
      antwoord: 1,
      uitleg: "De **Provinciale Staten** vormen de volksvertegenwoordiging (het 'parlement') van de provincie."
    },
    {
      type: "mc",
      vraag: "Wie is de voorzitter van de Provinciale Staten en het dagelijks bestuur van de provincie?",
      opties: [
        "De Burgemeester",
        "De Commissaris van de Koning",
        "De Minister-President",
        "De Dijkgraaf"
      ],
      antwoord: 1,
      uitleg: "De **Commissaris van de Koning** leidt de vergaderingen van de provincie en vertegenwoordigt het Rijk in de provincie."
    },
    {
      type: "mc",
      vraag: "Welke belasting heft de provincie rechtstreeks via de motorrijtuigenbelasting?",
      opties: [
        "Onroerendezaakbelasting (OZB)",
        "Opcenten (provinciale toeslag op de wegenbelasting)",
        "Btw",
        "Accijns"
      ],
      antwoord: 1,
      uitleg: "De **opcenten** zijn een toeslag bovenop de landelijke wegenbelasting. Dit is de belangrijkste eigen belastinginkomst van de provincie."
    },
    {
      type: "mc",
      vraag: "Hoe heet het dagelijks bestuur van de provincie?",
      opties: [
        "Het college van B&W",
        "De Gedeputeerde Staten",
        "De Provinciale Staten",
        "De ministerraad"
      ],
      antwoord: 1,
      uitleg: "De **Gedeputeerde Staten** voeren het dagelijks beleid van de provincie uit (vergelijkbaar met wethouders in een gemeente)."
    },
    {
      type: "waaronwaar",
      vraag: "Leden van de Eerste Kamer worden rechtstreeks door de Nederlandse bevolking gekozen tijdens de parlementsverkiezingen.",
      antwoord: false,
      uitleg: "Onwaar. De **Eerste Kamer** wordt indirect gekozen door de leden van de **Provinciale Staten** (getrapte verkiezingen)."
    },
    {
      type: "waaronwaar",
      vraag: "Provincies hebben elk hun eigen structuurvisie waarin de grote lijnen voor het gebruik van de ruimte staan vastgelegd.",
      antwoord: true,
      uitleg: "Waar. In deze **structuurvisie** staat bijvoorbeeld waar grote windmolenparken of nieuwe snelwegen gepland worden."
    },
    {
      type: "invul",
      vraag: "De voorzitter van de Provinciale Staten heet de Commissaris van de _______.",
      antwoord: "Koning",
      uitleg: "De **Commissaris van de Koning** wordt benoemd door de regering voor een periode van zes jaar."
    },
    {
      type: "open",
      vraag: "Leg uit waarom ruimtelijke ordening (zoals de aanleg van een nieuwe provinciale weg) een typische taak is voor de provincie en niet voor een gemeente.",
      sleutelwoorden: ["gemeentegrenzen/gemeentegrenzen overschrijden", "groter gebied/regionaal/regio", "afstemming/coördinatie/samenwerking"],
      minTreffers: 2,
      modelantwoord: "Ruimtelijke plannen zoals grote wegen of natuurgebieden overschrijden vaak de grenzen van één gemeente. Omdat gemeenten dit niet alleen kunnen beslissen, coördineert de provincie dit voor de hele regio zodat plannen goed op elkaar aansluiten.",
      uitleg: "Provincie overstijgt het lokale niveau van individuele gemeenten en stemt regionaal af."
    },
    {
      type: "open",
      vraag: "Hoe komt de provincie aan het geld om haar taken (zoals openbaar vervoer en natuurbeheer) te betalen?",
      sleutelwoorden: ["opcenten/motorrijtuigenbelasting/wegenbelasting", "provinciefonds/Rijk/belastinggeld", "subsidies/eigen leges"],
      minTreffers: 2,
      modelantwoord: "De provincie krijgt het meeste geld van de rijksoverheid via het Provinciefonds. Daarnaast heffen ze een eigen belasting: de provinciale opcenten op de motorrijtuigenbelasting (wegenbelasting) die autobezitters betalen.",
      uitleg: "Gefinancierd uit het provinciefonds en provinciale opcenten op de wegenbelasting."
    }
  ]
});
