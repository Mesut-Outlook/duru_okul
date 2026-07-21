/* Extra Proeftoets 37 — Provincie & Lokale Besturen */
DURU.registerExamen({
  id: "ex-extra-consument-overheid-3",
  titel: "Extra Proeftoets 37 — Provincie & Lokale Besturen",
  vak: "Economie · Lokale overheid",
  icoon: "🌍",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Hoeveel provincies telt Nederland?",
      opties: [
        "10 provincies.",
        "12 provincies.",
        "15 provincies.",
        "340 provincies."
      ],
      antwoord: 1,
      uitleg: "Nederland is verdeeld in **12 provincies**, die elk hun eigen provinciebestuur hebben."
    },
    {
      type: "waaronwaar",
      vraag: "De provincie bestuurt het gebied dat tussen het Rijk en de gemeenten in ligt.",
      antwoord: true,
      uitleg: "Waar. De provincie regelt zaken die te groot zijn voor een enkele gemeente, maar te specifiek voor de landelijke rijksoverheid."
    },
    {
      type: "invul",
      vraag: "Hoe heet het dagelijks bestuur van de provincie, dat de besluiten van de Provinciale Staten uitvoert? Gedeputeerde ________.",
      antwoord: "Staten|staten",
      uitleg: "Het dagelijks bestuur van de provincie heet de **Gedeputeerde Staten**."
    },
    {
      type: "mc",
      vraag: "Wie is de voorzitter van het provinciebestuur en wordt benoemd door de regering?",
      opties: [
        "De burgemeester.",
        "De Commissaris van de Koning.",
        "De wethouder.",
        "De minister-president."
      ],
      antwoord: 1,
      uitleg: "De **Commissaris van de Koning** is de voorzitter van zowel de Provinciale Staten als de Gedeputeerde Staten."
    },
    {
      type: "waaronwaar",
      vraag: "De Provinciale Staten zijn de gekozen volksvertegenwoordigers op provinciaal niveau, vergelijkbaar met de gemeenteraad.",
      antwoord: true,
      uitleg: "Waar. Burgers stemmen eens in de vier jaar voor de **Provinciale Staten**, die de regels voor de provincie bepalen."
    },
    {
      type: "invul",
      vraag: "Wie vormen samen met de burgemeester het dagelijks bestuur van een gemeente? De burgemeester en ________.",
      antwoord: "wethouders|de wethouders",
      uitleg: "Het college van **Burgemeester en Wethouders** (B&W) vormt het dagelijks bestuur van de gemeente."
    },
    {
      type: "mc",
      vraag: "Welke taak behoort typisch tot de verantwoordelijkheid van de provincie en niet van de gemeente?",
      opties: [
        "Het ophalen van huisvuil.",
        "De ruimtelijke ordening (waar provinciale wegen en natuurgebieden komen).",
        "Het uitgeven van paspoorten en identiteitskaarten.",
        "Het onderhouden van lokale speeltuinen."
      ],
      antwoord: 1,
      uitleg: "**Ruimtelijke ordening** op grotere schaal en de aanleg van provinciale fielen en fietspaden zijn taken van de provincie."
    },
    {
      type: "waaronwaar",
      vraag: "De gemeente is de laag van de overheid die het dichtst bij de burger staat.",
      antwoord: true,
      uitleg: "Waar. De **gemeente** regelt dagelijkse, lokale zaken zoals afvalverwerking, paspoorten en onderhoud van de buurt."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de provincie gaat over streekbussen (openbaar vervoer) en niet de afzonderlijke gemeenten zelf.",
      sleutelwoorden: ["gemeentegrenzen/gemeente overschrijden", "streekbussen rijden tussen steden/dorpen", "te groot/schaal/gebied", "samenhang/provinciaal"],
      minTreffers: 2,
      modelantwoord: "Streekbussen rijden vaak door meerdere gemeenten heen om verschillende dorpen en steden met elkaar te verbinden. Omdat dit de grenzen van een enkele gemeente overschrijdt, is het logischer dat de provincie (die over een groter gebied gaat) dit openbaar vervoer regelt.",
      uitleg: "Bovenlokale infrastructuur wordt door een hogere bestuurslaag (de provincie) gecoördineerd."
    },
    {
      type: "open",
      vraag: "Duru, leg uit wat het college van B&W doet en hoe dit verschilt van de rol van de gemeenteraad.",
      sleutelwoorden: ["B&W dagelijks bestuur/uitvoeren", "gemeenteraad beslist/stemmen/volksvertegenwoordiging", "controleert/controleren", "burgemeester wethouders"],
      minTreffers: 2,
      modelantwoord: "Het college van B&W (burgemeester en wethouders) is het dagelijks bestuur en voert de plannen uit. De gemeenteraad is de gekozen volksvertegenwoordiging: zij stemmen over regels en plannen en controleren het college van B&W.",
      uitleg: "Gemeenteraad = wetgevende/controlerende macht lokaal. College van B&W = uitvoerende macht lokaal."
    }
  ]
});
