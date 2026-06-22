/* Extra Proeftoets 34 — Inkomstenbelasting & Loonbelasting V */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting-5",
  titel: "Extra Proeftoets 34 — Inkomstenbelasting & Loonbelasting V",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het verschil tussen loonbelasting en premies volksverzekeringen?",
      opties: [
        "Loonbelasting is voor collectieve voorzieningen van de overheid; premies zijn specifiek voor sociale uitkeringen (zoals AOW).",
        "Loonbelasting betalen alleen rijke mensen; premies betaalt iedereen.",
        "Loonbelasting krijg je aan het eind van het jaar terug; premies nooit.",
        "Er is geen enkel verschil; het zijn gewoon twee namen voor btw."
      ],
      antwoord: 0,
      uitleg: "**Loonbelasting** gaat naar de algemene middelen van de overheid (wegen, scholen, politie). **Premies volksverzekeringen** zijn bedoeld voor sociale uitkeringen zoals de AOW en de Anw."
    },
    {
      type: "waaronwaar",
      vraag: "Loonheffing is de verzamelnaam voor loonbelasting en premies volksverzekeringen samen.",
      antwoord: true,
      uitleg: "Waar. Op je loonstrook staat vaak **loonheffing**. Dit is het totale bedrag van de ingehouden belasting én de sociale premies."
    },
    {
      type: "invul",
      vraag: "Hoe noemen we de optelsom van loonbelasting en premies volksverzekeringen die de werkgever inhoudt?",
      antwoord: "loonheffing|loonheffingen",
      uitleg: "De optelsom is de **loonheffing**."
    },
    {
      type: "mc",
      vraag: "Welk principe houdt in dat werkenden en gezonde mensen belasting en premies betalen zodat er gezorgd kan worden voor zieken, ouderen en werklozen?",
      opties: [
        "Het profijtprincipe.",
        "Het marktprincipe.",
        "Het solidariteitsbeginsel.",
        "Het concurrentiebeginsel."
      ],
      antwoord: 2,
      uitleg: "Dit is het **solidariteitsbeginsel**. We helpen elkaar door de kosten van risico's (zoals ouderdom of ziekte) samen te dragen via belastingen en premies."
    },
    {
      type: "waaronwaar",
      vraag: "In Nederland hoeft een werkloze geen premies volksverzekeringen te betalen over zijn uitkering.",
      antwoord: false,
      uitleg: "Onwaar. Iedereen met een inkomen in Nederland betaalt mee aan de volksverzekeringen, dus ook over een uitkering wordt loonheffing (inclusief premies) ingehouden."
    },
    {
      type: "mc",
      vraag: "Welke bekende volksverzekering zorgt voor een basisinkomen voor iedereen die de pensioengerechtigde leeftijd heeft bereikt?",
      opties: [
        "De WW (Werkloosheidswet).",
        "De AOW (Algemene Ouderdomswet).",
        "De Zorgverzekeringswet.",
        "De Bijstand."
      ],
      antwoord: 1,
      uitleg: "De **AOW** is een volksverzekering die een basispensioen geeft aan ouderen."
    },
    {
      type: "invul",
      vraag: "Hoe heet de uitkering die ouderen vanaf een bepaalde leeftijd ontvangen van de overheid?",
      antwoord: "AOW|AOW-uitkering|AOW uitkering",
      uitleg: "Dit heet de **AOW** (Algemene Ouderdomswet)."
    },
    {
      type: "mc",
      vraag: "Welk effect heeft de vergrijzing (meer ouderen ten opzichte van werkenden) op de premies voor de AOW?",
      opties: [
        "De premies kunnen omlaag omdat er minder werkenden zijn.",
        "De premies moeten waarschijnlijk omhoog, of de AOW-leeftijd moet stijgen om het betaalbaar te houden.",
        "Er is geen effect; de AOW wordt betaald uit de btw-opbrengsten.",
        "De overheid schaft de AOW direct af."
      ],
      antwoord: 1,
      uitleg: "Door de **vergrijzing** moeten steeds minder werkenden de AOW-premies opbrengen voor steeds meer ouderen. Hierdoor stijgen de kosten en moet de AOW-leeftijd omhoog."
    },
    {
      type: "waaronwaar",
      vraag: "Zelfs als je geen loonbelasting betaalt, profiteer je wel van de collectieve voorzieningen die ermee worden betaald.",
      antwoord: true,
      uitleg: "Waar. Iedereen maakt gebruik van wegen, straatverlichting en politiebeveiliging, ongeacht of je inkomstenbelasting betaalt."
    },
    {
      type: "mc",
      vraag: "Stel, Duru heeft een bijbaantje en verdient € 1.500,- per jaar. Er is € 150,- aan loonheffing ingehouden. Wat kan Duru doen om dit geld terug te krijgen?",
      opties: [
        "Niets, de overheid geeft scholieren nooit belasting terug.",
        "Aangifte doen aan het eind van het jaar om de te veel ingehouden belasting terug te vragen.",
        "Haar baas vragen om het contant terug te betalen.",
        "Een boze brief naar de koning sturen."
      ],
      antwoord: 1,
      uitleg: "Omdat Duru weinig verdient (onder de grens van de belastingvrije voet/loonheffingskorting), kan ze de ingehouden belasting via de **belastingaangifte** volledig terugvragen."
    },
    {
      type: "invul",
      vraag: "Wat moet Duru indienen bij de Belastingdienst om de ingehouden belasting van haar bijbaantje terug te krijgen?",
      antwoord: "belastingaangifte|aangifte|belastingaangifteapp|aangifteprogramma",
      uitleg: "Door het invullen van de **belastingaangifte** (online of via de app) kan ze het geld terugvragen."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen loonbelasting en loonheffing.",
      sleutelwoorden: ["loonheffing is breder/optelsom", "loonbelasting en premies", "volksverzekeringen", "onderdeel van"],
      minTreffers: 2,
      modelantwoord: "Loonbelasting is slechts één onderdeel van wat er op je loon wordt ingehouden. Loonheffing is de optelsom van loonbelasting én de premies volksverzekeringen die de werkgever gezamenlijk inhoudt en afdraagt aan de Belastingdienst.",
      uitleg: "Loonheffing = Loonbelasting + Premies Volksverzekeringen."
    },
    {
      type: "mc",
      vraag: "Waarom heft de overheid belasting over het loon van burgers?",
      opties: [
        "Om sparen minder aantrekkelijk te maken.",
        "Om geld in te zamelen voor de schatkist, zodat de overheid haar taken (zoals zorg, onderwijs en veiligheid) kan betalen.",
        "Om ervoor te zorgen dat bedrijven meer winst maken.",
        "Dat doet de overheid niet; loonbelasting gaat direct naar Europa."
      ],
      antwoord: 1,
      uitleg: "De overheid heeft belastinginkomsten nodig om de **collectieve voorzieningen** en overheidstaken te financieren."
    },
    {
      type: "waaronwaar",
      vraag: "De btw (belasting over de toegevoegde waarde) is een progressieve belasting, omdat rijke mensen duurdere spullen kopen.",
      antwoord: false,
      uitleg: "Onwaar. Btw is een constant percentage (bijv. 21%), ongeacht je inkomen. Dit noemen we een **vlaktaks** of proportionele belasting, en is geen progressieve belasting."
    },
    {
      type: "open",
      vraag: "Wat is het 'solidariteitsbeginsel' bij sociale verzekeringen? Leg kort uit.",
      sleutelwoorden: ["samen betalen/risico delen", "werkenden betalen voor uitkeringen", "helpen/zorgen voor zieken/ouderen/werklozen", "premies afdragen"],
      minTreffers: 2,
      modelantwoord: "Het solidariteitsbeginsel betekent dat we in de samenleving bereid zijn de kosten voor risico's samen te delen. Iedereen die verdient betaalt premies en belasting, zodat degenen die het nodig hebben (zoals ouderen, zieken of werklozen) een uitkering of zorg kunnen krijgen.",
      uitleg: "Iedereen draagt bij zodat de kwetsbaren in de samenleving beschermd zijn."
    }
  ]
});
