/* Extra Proeftoets 5B — Sociale Zekerheid & Zorg */
DURU.registerExamen({
  id: "ex-extra-sociale-zekerheid-3",
  titel: "Extra Proeftoets 5B — Sociale Zekerheid & Zorg",
  vak: "Economie · Sociale Zekerheid",
  icoon: "🏥",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Welke Nederlandse overheidsinstantie is verantwoordelijk voor het beoordelen van arbeidsongeschiktheid en het uitvoeren van de WW- en WIA-uitkeringen?",
      opties: [
        "Het UWV (Uitvoeringsinstituut Werknemersverzekeringen).",
        "De Belastingdienst (dienst Toeslagen).",
        "De Sociale Verzekeringsbank (SVB).",
        "De gemeentelijke sociale dienst."
      ],
      antwoord: 0,
      uitleg: "Het <b>UWV</b> beoordeelt of je recht hebt op een werknemersverzekering bij werkloosheid of ziekte en helpt mensen bij het vinden van werk."
    },
    {
      type: "waaronwaar",
      vraag: "Het 'eigen risico' in de zorgverzekering betekent dat je de eerste zorgkosten (zoals ziekenhuisbezoek of medicijnen) tot een bepaald bedrag zelf betaalt, maar dit geldt niet voor een bezoek aan de huisarts.",
      antwoord: true,
      uitleg: "Waar. Het bezoek aan de **huisarts** is volledig uitgesloten van het eigen risico om te voorkomen dat mensen bij gezondheidsklachten de drempel naar de eerste zorg mijden."
    },
    {
      type: "invul",
      vraag: "De uitkering voor werknemers die na twee jaar ziekte nog steeds niet (volledig) kunnen werken door arbeidsongeschiktheid heet de WIA. Dit is een voorbeeld van een ___________verzekering.",
      antwoord: "werknemers",
      uitleg: "De WIA (Wet werk en inkomen naar arbeidsvermogen) is specifiek voor mensen die in loondienst hebben gewerkt en premies hebben betaald via hun loon, dus een <b>werknemersverzekering</b>."
    },
    {
      type: "mc",
      vraag: "Welk effect heeft de 'vergrijzing' op de financiering van de AOW-uitkeringen in Nederland?",
      opties: [
        "Er zijn relatief meer ouderen die een uitkering ontvangen en minder werkenden die premie betalen, waardoor de druk op het stelsel toeneemt.",
        "De AOW wordt hierdoor een stuk goedkoper en de premies voor werkenden dalen snel.",
        "De overheid hoeft door vergrijzing geen AOW meer uit te keren aan nieuwe gepensioneerden.",
        "Vergrijzing zorgt ervoor dat de AOW automatisch gefinancierd wordt door buitenlandse subsidies."
      ],
      antwoord: 0,
      uitleg: "Door de **vergrijzing** (een stijgend aandeel ouderen in de bevolking) stijgen de totale kosten voor de AOW, waardoor de pensioenleeftijd stapsgewijs omhoog moet."
    },
    {
      type: "waaronwaar",
      vraag: "De Anw (Algemene nabestaandenwet) is een werknemersverzekering die alleen een uitkering verstrekt als de overledene in loondienst werkte.",
      antwoord: false,
      uitleg: "Onwaar. De Anw is een **volksverzekering**. Iedereen die in Nederland woont of werkt is hiervoor verzekerd. Het biedt een financiële bijdrage na het overlijden van een partner of ouders."
    },
    {
      type: "invul",
      vraag: "Het vaste bedrag dat je maandelijks aan een zorgverzekeraar betaalt voor je zorgverzekering heet de zorg________.",
      antwoord: "premie",
      uitleg: "De **zorgpremie** (of nominale premie) betaal je rechtstreeks aan je gekozen zorgverzekeraar om verzekerd te zijn voor basiszorg."
    },
    {
      type: "mc",
      vraag: "Wat houdt de wettelijke 'acceptatieplicht' in voor zorgverzekeraars bij de basisverzekering?",
      opties: [
        "Zorgverzekeraars moeten iedereen accepteren die een basisverzekering aanvraagt, ongeacht hun leeftijd, geslacht of gezondheid.",
        "Consumenten moeten verplicht de eerste zorgverzekeraar accepteren die hen een aanbod doet.",
        "Ziekenhuizen moeten elke patiënt accepteren die door een huisarts is doorverwezen voor een operatie.",
        "De overheid moet alle buitenlandse zorgverzekeraars zonder controle toelaten op de Nederlandse markt."
      ],
      antwoord: 0,
      uitleg: "De **acceptatieplicht** voorkomt dat verzekeraars alleen gezonde mensen kiezen en chronisch zieken of ouderen weigeren. Dit waarborgt de solidariteit."
    },
    {
      type: "waaronwaar",
      vraag: "Kinderen tot 18 jaar betalen in Nederland geen zorgpremie en hebben ook geen verplicht eigen risico voor de zorgverzekering.",
      antwoord: true,
      uitleg: "Waar. Kinderen zijn gratis meeverzekerd op de polis van hun ouders om de zorg voor gezinnen betaalbaar te houden."
    },
    {
      type: "open",
      vraag: "Leg uit hoe het 'omslagstelsel' werkt waarmee de AOW-uitkeringen in Nederland worden gefinancierd.",
      sleutelwoorden: ["werkenden/nu/werkende", "premie/premies/belasting/belastingen/betalen", "ouderen/gepensioneerden/direct/ontvangen/uitkeren", "omslag/omgeslagen"],
      minTreffers: 2,
      modelantwoord: "Bij het omslagstelsel worden de premies die de werkenden nu betalen, direct hetzelfde jaar weer uitgegeven aan de AOW-uitkeringen van de ouderen van nu. Het geld wordt dus direct doorgegeven (omgeslagen) en niet opgespaard voor later.",
      uitleg: "De premie-inkomsten van vandaag betalen direct de uitkeringen van vandaag."
    },
    {
      type: "open",
      vraag: "Leg uit wat de reden is dat de overheid een verplicht 'eigen risico' in de zorgverzekering heeft ingevoerd. Noem een voordeel en een nadeel voor de consument.",
      sleutelwoorden: ["kosten/bewust/minder snel/dokter/ziekenhuis/remmen", "nadeel/mijden/zorg/geld/duur/betalen", "voordeel/premie/lager/goedkoper"],
      minTreffers: 2,
      modelantwoord: "De overheid heeft het eigen risico ingevoerd om consumenten bewuster te maken van zorgkosten, zodat ze niet onnodig snel naar een medisch specialist of ziekenhuis gaan. Een voordeel is dat hierdoor de maandelijkse zorgpremie voor iedereen lager blijft. Een nadeel is dat mensen met een laag inkomen noodzakelijke zorg soms gaan mijden om kosten te besparen.",
      uitleg: "Het eigen risico remt onnodig zorggebruik en houdt de premie lager, maar kan zorgmijding veroorzaken."
    }
  ]
});
