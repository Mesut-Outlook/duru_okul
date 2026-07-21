/* Extra Proeftoets 26 — Begrotingstekort & Staatsschuld */
DURU.registerExamen({
  id: "ex-extra-tekort-staatsschuld",
  titel: "Extra Proeftoets 26 — Begrotingstekort & Staatsschuld",
  vak: "Economie · Staatsfinanciën",
  icoon: "📉",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is een begrotingstekort?",
      opties: [
        "De verwachte inkomsten zijn hoger dan de verwachte uitgaven",
        "De verwachte uitgaven zijn hoger dan de verwachte inkomsten",
        "De inkomsten en uitgaven zijn precies gelijk",
        "De staatsschuld is helemaal afbetaald"
      ],
      antwoord: 1,
      uitleg: "Bij een **begrotingstekort** zijn de verwachte uitgaven hoger dan de verwachte inkomsten."
    },
    {
      type: "mc",
      vraag: "Wat is een begrotingsoverschot?",
      opties: [
        "De inkomsten zijn hoger dan de uitgaven",
        "De uitgaven zijn hoger dan de inkomsten",
        "De staatsschuld stijgt",
        "Er moet extra geleend worden"
      ],
      antwoord: 0,
      uitleg: "Bij een **begrotingsoverschot** zijn de inkomsten hoger dan de uitgaven."
    },
    {
      type: "mc",
      vraag: "Wat kan de overheid doen om een begrotingstekort op te lossen?",
      opties: [
        "Alleen de koning vragen om geld te schenken",
        "Bezuinigen op de uitgaven, belastingen verhogen, of geld lenen",
        "Niets, een tekort lost zichzelf altijd op",
        "De staatsschuld direct schrappen"
      ],
      antwoord: 1,
      uitleg: "Een begrotingstekort kan worden opgelost door te **bezuinigen** op de uitgaven, de **belastingen te verhogen**, of **geld te lenen**."
    },
    {
      type: "mc",
      vraag: "Wat is de staatsschuld?",
      opties: [
        "Het bedrag dat een burger jaarlijks aan belasting betaalt",
        "Het tekort van precies één jaar",
        "Het totaal van alle schulden die de overheid in de loop der jaren heeft opgebouwd",
        "De rente die bedrijven aan de bank betalen"
      ],
      antwoord: 2,
      uitleg: "De **staatsschuld** is het totaal van alle schulden die de overheid door de jaren heen heeft opgebouwd."
    },
    {
      type: "mc",
      vraag: "Volgens de Rijksbegroting 2024 waren de inkomsten € 402,9 miljard en de uitgaven € 433,6 miljard. Wat is hier het geval?",
      opties: [
        "Een begrotingsoverschot van € 30,7 miljard",
        "Een begrotingstekort van € 30,7 miljard",
        "Precies evenwicht tussen inkomsten en uitgaven",
        "Een begrotingstekort van € 433,6 miljard"
      ],
      antwoord: 1,
      uitleg: "433,6 − 402,9 = 30,7. Omdat de uitgaven hoger zijn dan de inkomsten, is er een **begrotingstekort van € 30,7 miljard**."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de staatsschuld als de overheid een begrotingstekort heeft?",
      opties: [
        "De staatsschuld daalt",
        "De staatsschuld blijft precies gelijk",
        "De staatsschuld stijgt, omdat de overheid moet bijlenen",
        "De staatsschuld verdwijnt automatisch na een jaar"
      ],
      antwoord: 2,
      uitleg: "Bij een tekort heeft de overheid te weinig geld en moet ze **bijlenen**, waardoor de **staatsschuld stijgt**."
    },
    {
      type: "waaronwaar",
      vraag: "Over de staatsschuld moet de overheid rente (rentelasten) betalen.",
      antwoord: true,
      uitleg: "Waar. Hoe hoger de staatsschuld, hoe meer **rentelasten** de overheid jaarlijks moet betalen."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een begrotingsoverschot kan de overheid schulden aflossen die ze eerder had.",
      antwoord: true,
      uitleg: "Waar. Als de inkomsten hoger zijn dan de uitgaven, houdt de overheid geld over om eerdere **schulden af te lossen**."
    },
    {
      type: "waaronwaar",
      vraag: "Een begrotingstekort kan alleen worden opgelost door te lenen; bezuinigen of belastingen verhogen helpt niet.",
      antwoord: false,
      uitleg: "Onwaar. Een tekort kan ook worden opgelost door te **bezuinigen** op de uitgaven of de **belastingen te verhogen**, naast lenen."
    },
    {
      type: "waaronwaar",
      vraag: "De staatsschuld is hetzelfde als het begrotingstekort van één jaar.",
      antwoord: false,
      uitleg: "Onwaar. Het begrotingstekort is het tekort van één jaar; de **staatsschuld** is de optelsom van alle tekorten en leningen over meerdere jaren."
    },
    {
      type: "invul",
      vraag: "Als de verwachte uitgaven hoger zijn dan de verwachte inkomsten, spreken we van een begrotings____________.",
      antwoord: "tekort",
      uitleg: "Een **begrotingstekort** ontstaat wanneer de uitgaven hoger zijn dan de inkomsten."
    },
    {
      type: "invul",
      vraag: "De rente die de overheid betaalt over de staatsschuld heet ____________.",
      antwoord: "rentelasten|rente",
      uitleg: "De **rentelasten** zijn de rente die de overheid jaarlijks betaalt over haar staatsschuld."
    },
    {
      type: "invul",
      vraag: "Als de overheid bij een begrotingstekort geld tekort heeft, moet ze gaan ____________.",
      antwoord: "lenen|bijlenen",
      uitleg: "Bij een tekort moet de overheid **bijlenen**, wat de staatsschuld doet stijgen."
    },
    {
      type: "open",
      vraag: "Leg uit wat een begrotingstekort is en welke twee gevolgen dit kan hebben voor de overheid.",
      sleutelwoorden: ["uitgaven hoger/uitgaven groter dan inkomsten", "lenen/bijlenen", "staatsschuld stijgt/rentelasten"],
      minTreffers: 2,
      modelantwoord: "Een begrotingstekort betekent dat de verwachte uitgaven van de overheid hoger zijn dan de verwachte inkomsten. Hierdoor heeft de overheid te weinig geld en moet ze bijlenen. Dit zorgt ervoor dat de staatsschuld stijgt, waardoor de overheid in de toekomst ook meer rentelasten moet betalen.",
      uitleg: "Een tekort leidt tot lenen, wat de staatsschuld en de rentelasten verhoogt."
    },
    {
      type: "open",
      vraag: "Noem twee manieren waarop de overheid een begrotingstekort kan oplossen en leg er één van uit.",
      sleutelwoorden: ["bezuinigen/uitgaven verlagen", "belastingen verhogen", "lenen/geld lenen"],
      minTreffers: 2,
      modelantwoord: "De overheid kan een begrotingstekort oplossen door te bezuinigen op de uitgaven, bijvoorbeeld minder geld uitgeven aan bepaalde voorzieningen. Een andere manier is om de belastingen te verhogen, zodat de inkomsten stijgen. Ook kan de overheid geld lenen, maar dat vergroot de staatsschuld.",
      uitleg: "Bezuinigen, belastingen verhogen en lenen zijn de drie manieren om een tekort aan te pakken."
    }
  ]
});
