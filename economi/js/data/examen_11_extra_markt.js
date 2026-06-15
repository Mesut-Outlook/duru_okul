/* Extra Proeftoets 6 — De Overheid op de Markt */
DURU.registerExamen({
  id: "ex-extra-overheid-markt",
  titel: "Extra Proeftoets 6 — De Overheid op de Markt",
  vak: "Economie · Marktwerking",
  icoon: "⚖️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is een monopolie op de economische markt?",
      opties: [
        "Er zijn heel veel aanbieders en heel weinig vragers.",
        "Er is slechts één aanbieder van een bepaald product of bepaalde dienst.",
        "Het verbod om reclame te maken op televisie.",
        "De markt waarop de overheid geen belasting mag heffen."
      ],
      antwoord: 1,
      uitleg: "Een <b>monopolie</b> betekent dat één bedrijf de markt beheerst (bijv. NS op het hoofdrailnet). Hierdoor kan dit bedrijf gemakkelijk zelf de prijs bepalen."
    },
    {
      type: "mc",
      vraag: "Waarom wil de overheid monopolies en kartels zoveel mogelijk tegengaan?",
      opties: [
        "Omdat monopolies te veel belasting betalen.",
        "Omdat concurrentie zorgt voor lagere prijzen, betere kwaliteit en meer keuze voor de consument.",
        "Omdat de koning alle bedrijven zelf wil bezitten.",
        "Omdat er dan te veel banen ontstaan in Nederland."
      ],
      antwoord: 1,
      uitleg: "Concurrentie (marktwerking) prikkelt bedrijven om efficiënt te werken, hun prijzen laag te houden en betere producten te leveren."
    },
    {
      type: "mc",
      vraag: "Wat houdt privatisering van een overheidsbedrijf in?",
      opties: [
        "Het bedrijf wordt eigendom van een buitenlandse staat.",
        "De overheid verkoopt het bedrijf aan particulieren, zodat het een commercieel bedrijf wordt en marktwerking ontstaat.",
        "Het bedrijf mag geen winst meer maken.",
        "De medewerkers worden allemaal ontslagen."
      ],
      antwoord: 1,
      uitleg: "Bij <b>privatisering</b> (zoals vroeger bij PostNL en KPN) trekt de overheid zich terug en laat de markt het werk doen."
    },
    {
      type: "mc",
      vraag: "Welk van de volgende goederen is een typisch voorbeeld van een collectief goed?",
      opties: [
        "Een treinkaartje naar Utrecht Centraal.",
        "De straatverlichting in je woonwijk.",
        "Een pak melk in de supermarkt.",
        "Een bioscoopkaartje."
      ],
      antwoord: 1,
      uitleg: "Collectieve goederen (zoals straatverlichting, defensie, dijken) worden door de overheid betaald omdat je er niemand van kunt uitsluiten en je er geen individuele prijs voor kunt vragen."
    },
    {
      type: "mc",
      vraag: "Wat is marktwerking?",
      opties: [
        "De prijs van een product wordt bepaald door vraag en aanbod zonder dat de overheid zich ermee bemoeit.",
        "De minister bepaalt elke ochtend wat brood kost.",
        "Winkels mogen alleen open op zaterdag op de markt.",
        "Bedrijven moeten verplicht samenwerken om de prijzen gelijk te houden."
      ],
      antwoord: 0,
      uitleg: "Bij **marktwerking** bepalen de vragers (consumenten) en aanbieders (producenten) samen de prijs via het prijsmechanisme."
    },
    {
      type: "waaronwaar",
      vraag: "Sinds de privatisering van de telecommarkt (KPN) zijn er meer aanbieders gekomen en zijn de tarieven voor mobiele telefonie flink gedaald.",
      antwoord: true,
      uitleg: "Waar. De toegenomen concurrentie tussen providers heeft gezorgd voor betere abonnementen en lagere prijzen."
    },
    {
      type: "waaronwaar",
      vraag: "Wanneer de overheid zich bemoeit met de markt door maximumprijzen in te stellen, is dat bedoeld om de producent te beschermen.",
      antwoord: false,
      uitleg: "Onwaar. Een **maximumprijs** is bedoeld om de **consument** te beschermen tegen te hoge prijzen (bijvoorbeeld bij sociale huurwoningen)."
    },
    {
      type: "invul",
      vraag: "De wet die kartels verbiedt en zorgt voor eerlijke concurrentie op de markt heet de ____________wet.",
      antwoord: "Mededingings|mededingings",
      uitleg: "De **Mededingingswet** verbiedt kartels en misbruik van machtsposities op de markt."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overheid collectieve goederen (zoals dijken of politie) levert en niet overlaat aan de vrije markt.",
      sleutelwoorden: ["uitsluiten/niet uitsluiten", "geen prijs/geen winst", "vrijbuitersgedrag/vrijbuiters/gratis", "markt faalt/markt levert niet"],
      minTreffers: 2,
      modelantwoord: "Collectieve goederen kunnen niet via de markt verkocht worden omdat je mensen er niet van kunt uitsluiten (iedereen profiteert van een dijk). Omdat mensen er niet individueel voor willen betalen (vrijbuitersgedrag), kan een commercieel bedrijf er geen winst op maken. De overheid moet ze dus leveren en betalen uit belastinggeld.",
      uitleg: "Geen uitsluiting mogelijk -> geen individuele verkoop -> overheid moet leveren via belastingen."
    },
    {
      type: "open",
      vraag: "Noem één voordeel en één nadeel van het privatiseren van een overheidsbedrijf (zoals het openbaar vervoer).",
      sleutelwoorden: ["efficiënter/goedkoper/concurrentie/prikkel (voordeel)", "kwaliteit/winstbejag/duurder/minder controle/lijnen opheffen (nadeel)"],
      minTreffers: 2,
      modelantwoord: "Een voordeel is dat concurrentie zorgt voor efficiënter werken, betere service en lagere prijzen voor de consument. Een nadeel is dat commerciële bedrijven winst willen maken, waardoor ze minder rendabele diensten (zoals buslijnen op het platteland) kunnen opheffen.",
      uitleg: "Voordeel = efficiëntie & innovatie. Nadeel = winstbejag ten koste van sociaal belang."
    }
  ]
});
