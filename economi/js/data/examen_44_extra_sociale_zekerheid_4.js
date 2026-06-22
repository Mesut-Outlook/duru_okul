/* Extra Proeftoets 5C — Sociale Zekerheid & Zorg */
DURU.registerExamen({
  id: "ex-extra-sociale-zekerheid-4",
  titel: "Extra Proeftoets 5C — Sociale Zekerheid & Zorg",
  vak: "Economie · Sociale Zekerheid",
  icoon: "🏥",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het belangrijkste doel van de 'Participatiewet'?",
      opties: [
        "Zorgen dat zoveel mogelijk mensen met een afstand tot de arbeidsmarkt werk vinden, en het bieden van de Bijstandsuitkering als vangnet.",
        "Het verplicht stellen dat alle burgers deelnemen aan lokale politieke verkiezingen.",
        "Het subsidiëren van zonnepanelen en warmtepompen voor particulieren.",
        "Het controleren en goedkeuren van de begrotingen van de verschillende provincies."
      ],
      antwoord: 0,
      uitleg: "De <b>Participatiewet</b> vervangt de oude bijstandswetgeving en is erop gericht iedereen te laten participeren (meedoen) in de maatschappij via werk."
    },
    {
      type: "waaronwaar",
      vraag: "Als je zelf vrijwillig ontslag neemt bij je werkgever omdat je een lange reis wilt gaan maken, heb je direct recht op een WW-uitkering van de overheid.",
      antwoord: false,
      uitleg: "Onwaar. Om recht te hebben op een WW-uitkering moet je **onverwijtbaar** (buiten je eigen schuld om) werkloos zijn geworden en actief solliciteren."
    },
    {
      type: "invul",
      vraag: "Een uitkering die niet wordt betaald uit premies van werkenden, maar rechtstreeks uit de algemene belastinginkomsten van de overheid, heet een sociale __________.",
      antwoord: "voorziening",
      uitleg: "In tegenstelling tot sociale verzekeringen worden **sociale voorzieningen** (zoals de bijstand of de Wajong) betaald met belastinggeld."
    },
    {
      type: "mc",
      vraag: "Welk risico wordt primair afgedekt door de Ziektewet (ZW)?",
      opties: [
        "Het doorbetalen van loon of een uitkering bij ziekte aan werknemers die geen vaste werkgever hebben die hun loon doorbetaalt (zoals uitzendkrachten).",
        "Het vergoeden van medicijnen, behandelingen en verblijf in het ziekenhuis bij ziekte.",
        "Het betalen van de kosten voor fysiotherapie en tandartscontroles bij chronische ziekten.",
        "Het uitkeren van een basispensioen aan ouderen die door ziekte eerder moeten stoppen met werken."
      ],
      antwoord: 0,
      uitleg: "De **Ziektewet** fungeert als vangnet voor zieke werknemers die geen recht hebben op loondoorbetaling bij ziekte door een werkgever."
    },
    {
      type: "waaronwaar",
      vraag: "Het solidariteitsbeginsel in de zorg houdt in dat gezonde mensen via hun premie meebetalen aan de zorg van zieke mensen, en rijken meer betalen via de inkomensafhankelijke bijdrage.",
      antwoord: true,
      uitleg: "Waar. Solidariteit betekent dat de **sterkste schouders de zwaarste lasten dragen** en dat we gezamenlijk zorgen voor wie hulp nodig heeft."
    },
    {
      type: "invul",
      vraag: "Het UWV controleert streng of mensen met een WW-uitkering voldoende hun best doen om een nieuwe baan te vinden. Dit noemen we de sollicitatie_________.",
      antwoord: "plicht",
      uitleg: "Wie een WW-uitkering krijgt, moet aan de **sollicitatieplicht** voldoen om te laten zien dat hij er alles aan doet om weer aan het werk te gaan."
    },
    {
      type: "mc",
      vraag: "Welke toeslag kun je aanvragen bij de Belastingdienst als de basispremie van je zorgverzekering te zwaar drukt op je lage huishoudinkomen?",
      opties: [
        "De zorgtoeslag.",
        "De huurtoeslag.",
        "De kinderbijslag.",
        "De AOW-toeslag."
      ],
      antwoord: 0,
      uitleg: "De <b>zorgtoeslag</b> is een inkomensafhankelijke tegemoetkoming van de overheid om de verplichte zorgverzekering betaalbaar te houden voor lagere inkomens."
    },
    {
      type: "waaronwaar",
      vraag: "Voor het recht op een Bijstandsuitkering geldt een vermogenstoets; als je te veel spaargeld hebt, moet je dat eerst opmaken voordat je een uitkering krijgt.",
      antwoord: true,
      uitleg: "Waar. De bijstand is het allerlaatste vangnet. Je krijgt het pas als je echt geen andere inkomstenbronnen of noemenswaardige **eigen vermogensmiddelen** meer hebt."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen het kapitaaldekkingstelsel (zoals bij aanvullende pensioenen via een pensioenfonds) en het omslagstelsel (zoals bij de AOW).",
      sleutelwoorden: ["kapitaaldekking/sparen/spaar/beleggen/belegd/opsparen/fondsen", "omslag/direct/nu/werkenden/ouderen/gepensioneerden", "eigen/toekomst"],
      minTreffers: 2,
      modelantwoord: "Bij het omslagstelsel (AOW) betalen de werkenden van nu de uitkeringen van de ouderen van nu direct; het geld wordt meteen doorgegeven. Bij het kapitaaldekkingstelsel (aanvullend pensioen) spaar en beleg je tijdens je werkende leven geld in een pensioenfonds voor je eigen toekomstige pensioen.",
      uitleg: "Omslagstelsel = direct doorgeven aan ouderen van nu. Kapitaaldekkingstelsel = opsparen voor je eigen pensioen later."
    },
    {
      type: "open",
      vraag: "Als iemand in Nederland langer dan twee jaar (104 weken) ernstig ziek is en niet kan werken, welke wet treedt dan in werking en welke instantie beoordeelt dit?",
      sleutelwoorden: ["WIA", "UWV", "keuring/beoordeling/beoordeelt/keuren", "arbeidsongeschikt/arbeidsongeschiktheid"],
      minTreffers: 2,
      modelantwoord: "Na twee jaar loondoorbetaling bij ziekte treedt de wet WIA in werking. Het UWV voert deze wet uit en voert een medische en arbeidsdeskundige keuring uit om te beoordelen in hoeverre de persoon nog kan werken en op welke uitkering hij recht heeft.",
      uitleg: "De WIA volgt na de Ziektewet, en het UWV beoordeelt de mate van arbeidsongeschiktheid."
    }
  ]
});
