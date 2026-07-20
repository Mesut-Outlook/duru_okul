/* Extra Proeftoets 16 — De Verzorgingsstaat & Sociale Zekerheid */
DURU.registerExamen({
  id: "ex-extra-verzorgingsstaat",
  titel: "Extra Proeftoets 16 — De Verzorgingsstaat & Sociale Zekerheid",
  vak: "Economie · Sociale Zekerheid",
  icoon: "🤝",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de belangrijkste omschrijving van een verzorgingsstaat?",
      opties: [
        "Een land waar de koning alle macht heeft en voor zijn burgers zorgt.",
        "Een land waar de overheid zorgt voor de burgers die zelf geen inkomen kunnen verdienen.",
        "Een land waar bedrijven alle zorgtaken overnemen van de overheid.",
        "Een land waar burgers geen belastingen betalen voor de zorg."
      ],
      antwoord: 1,
      uitleg: "In een **verzorgingsstaat** helpt de overheid burgers met uitkeringen en zorg als ze bijvoorbeeld werkloos, ziek of oud zijn."
    },
    {
      type: "waaronwaar",
      vraag: "Sociale zekerheid in Nederland wordt alleen gefinancierd door mensen die zelf een uitkering ontvangen.",
      antwoord: false,
      uitleg: "Onwaar. Sociale zekerheid wordt betaald door **werkenden** (via premies op hun loon) en door iedereen via de **belastingen**."
    },
    {
      type: "invul",
      vraag: "Welke wet regelt de basisuitkering voor mensen die de pensioengerechtigde leeftijd hebben bereikt? (Afkorting)",
      antwoord: "AOW|aow",
      uitleg: "De **AOW** (Algemene Ouderdomswet) geeft iedereen vanaf een bepaalde leeftijd recht op een basispensioen."
    },
    {
      type: "mc",
      vraag: "Als je buiten je eigen schuld om je baan verliest, op welke uitkering heb je dan recht?",
      opties: [
        "De ANW (Algemene nabestaandenwet)",
        "De WW (Werkloosheidswet)",
        "De WIA (Wet werk en inkomen naar arbeidsvermogen)",
        "De Bijstand"
      ],
      antwoord: 1,
      uitleg: "De **WW** is de Werkloosheidswet. Dit is een tijdelijke uitkering voor mensen die werkloos worden."
    },
    {
      type: "waaronwaar",
      vraag: "Het solidariteitsbeginsel betekent dat gezonde mensen meebetalen aan de zorg voor zieke mensen.",
      antwoord: true,
      uitleg: "Waar. Het **solidariteitsbeginsel** betekent dat we risico's en kosten met elkaar delen."
    },
    {
      type: "invul",
      vraag: "Welke overheidsinstantie beoordeelt of je recht hebt op een WW-uitkering en helpt je bij het zoeken naar werk?",
      antwoord: "UWV|uwv",
      uitleg: "Het **UWV** (Uitvoeringsinstituut Werknemersverzekeringen) regelt de WW-uitkeringen en werkzoekenden-begeleiding."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste verschil tussen een sociale verzekering en een sociale voorziening?",
      opties: [
        "Voor een verzekering betaal je premie, een voorziening wordt betaald uit belastinggeld.",
        "Voor een voorziening moet je werken, voor een verzekering niet.",
        "Een verzekering krijg je direct, op een voorziening moet je jaren wachten.",
        "Er is helemaal geen verschil, het zijn twee woorden voor hetzelfde."
      ],
      antwoord: 0,
      uitleg: "Sociale **verzekeringen** betaal je via premies (op je loon). Sociale **voorzieningen** (zoals de Bijstand) worden betaald uit de algemene belastingen."
    },
    {
      type: "waaronwaar",
      vraag: "Iedereen die in Nederland woont of werkt heeft automatisch recht op de AOW als de pensioengerechtigde leeftijd is bereikt.",
      antwoord: true,
      uitleg: "Waar. De AOW is een **volksverzekering** en geldt voor alle inwoners van Nederland."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende uitkeringen is een voorbeeld van een sociale voorziening?",
      opties: [
        "De WW (Werkloosheidswet)",
        "De Bijstand (Participatiewet)",
        "De AOW (Algemene Ouderdomswet)",
        "De ZW (Ziektewet)"
      ],
      antwoord: 1,
      uitleg: "De **Bijstand** is het laatste vangnet voor wie geen andere inkomsten of uitkeringen heeft en wordt betaald uit belastinggeld."
    },
    {
      type: "invul",
      vraag: "Als je door een langdurige ziekte of handicap niet meer (volledig) kunt werken, krijg je een uitkering via de wet genaamd: de _______.",
      antwoord: "WIA|wia",
      uitleg: "De **WIA** (Wet werk en inkomen naar arbeidsvermogen) regelt de uitkering bij arbeidsongeschiktheid."
    },
    {
      type: "mc",
      vraag: "Hoe noem je het minimale bedrag dat je volgens de overheid nodig hebt om van te kunnen leven?",
      opties: [
        "Het gemiddelde loon",
        "Het sociaal minimum",
        "Het zakgeldniveau",
        "De armoedegrens"
      ],
      antwoord: 1,
      uitleg: "Het **sociaal minimum** is het bedrag dat de overheid vaststelt als het absolute minimum dat je nodig hebt voor basisbehoeften."
    },
    {
      type: "waaronwaar",
      vraag: "Als je ziek wordt, is je werkgever verplicht om je loon minstens gedurende 2 jaar (voor een groot deel) door te betalen.",
      antwoord: true,
      uitleg: "Waar. Dit is wettelijk zo geregeld in Nederland om werknemers bei ziekte te beschermen."
    },
    {
      type: "mc",
      vraag: "Wie betaalt de kinderbijslag in Nederland?",
      opties: [
        "De ouders zelf via een spaarrekening",
        "De werkgevers van de ouders",
        "De Sociale Verzekeringsbank (SVB) namens de overheid",
        "De gemeente waar het kind woont"
      ],
      antwoord: 2,
      uitleg: "De **SVB** (Sociale Verzekeringsbank) keert de kinderbijslag uit, wat gefinancierd wordt door de overheid."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overheid het minimumloon wettelijk heeft vastgelegd en hoe dit werknemers beschermt.",
      sleutelwoorden: ["ondergrens/minimum", "uitbuiting voorkomen/te weinig betalen", "rondkomen/leefbaar loon/sociaal minimum", "werkgever verplichten/beschermen"],
      minTreffers: 2,
      modelantwoord: "De overheid stelt het minimumloon vast om werknemers te beschermen tegen onderbetaling en uitbuiting door werkgevers. Dit zorgt ervoor dat iedereen die fulltime werkt minimaal een loon ontvangt waarvan je fatsoenlijk kunt rondkomen.",
      uitleg: "Wettelijke bescherming tegen te lage lonen."
    },
    {
      type: "open",
      vraag: "Noem twee redenen waarom de kosten voor de sociale zekerheid in Nederland de laatste jaren stijgen (denk aan demografie).",
      sleutelwoorden: ["vergrijzing/meer ouderen", "langere levensverwachting/ouder worden", "stijgende zorgkosten/duurdere zorg", "meer uitkeringen/AOW-gerechtigden"],
      minTreffers: 2,
      modelantwoord: "Ten eerste is er sprake van vergrijzing: er zijn steeds meer ouderen die recht hebben op AOW en zorg. Ten tweede stijgen de kosten per patiënt in de zorg door geavanceerdere en duurdere behandelingen.",
      uitleg: "Vergrijzing en duurdere medische zorg zorgen voor hogere uitgaven."
    }
  ]
});
