/* Extra Proeftoets 22 — Inflatie, Deflatie & Koopkracht */
DURU.registerExamen({
  id: "ex-extra-inflatie-koopkracht",
  titel: "Extra Proeftoets 22 — Inflatie, Deflatie & Koopkracht",
  vak: "Economie · Prijzen & Inkomen",
  icoon: "🛒",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de juiste definitie van inflatie?",
      opties: [
        "Een daling van de prijzen van goederen en diensten.",
        "Een algemene stijging van het prijsniveau, waardoor je geld minder waard wordt.",
        "De groei van de totale hoeveelheid goud in een land.",
        "Het percentage mensen dat werkloos is."
      ],
      antwoord: 1,
      uitleg: "Bij **inflatie** stijgen de prijzen gemiddeld. Je kunt met één euro minder kopen dan voorheen; je geld verliest dus aan koopkracht."
    },
    {
      type: "waaronwaar",
      vraag: "Deflatie betekent dat de prijzen van goederen en diensten gemiddeld dalen.",
      antwoord: true,
      uitleg: "Waar. **Deflatie** is het tegenovergestelde van inflatie: het gemiddelde prijsniveau daalt."
    },
    {
      type: "invul",
      vraag: "Hoe noem je de hoeveelheid goederen en diensten die je daadwerkelijk met je inkomen kunt kopen?",
      antwoord: "koopkracht",
      uitleg: "Je **koopkracht** hangt af van de hoogte van je inkomen én van de prijzen (inflatie)."
    },
    {
      type: "mc",
      vraag: "Wat meet de Consumentenprijsindex (CPI)?",
      opties: [
        "De winst van de grootste supermarkten in Nederland.",
        "De prijsontwikkeling van een 'mandje' goederen en diensten dat een gemiddeld huishouden aanschaft.",
        "De totale waarde van alle exportproducten.",
        "Hoeveel belasting consumenten betalen."
      ],
      antwoord: 1,
      uitleg: "Het CBS gebruikt het **CPI** om de inflatie te meten door de prijs van een vast pakket aan producten en diensten te volgen."
    },
    {
      type: "waaronwaar",
      vraag: "Als je nominaal inkomen met 5% stijgt en de prijzen stijgen ook met 5%, dan stijgt je koopkracht met 5%.",
      antwoord: false,
      uitleg: "Onwaar. Als je inkomen en de prijzen met hetzelfde percentage stijgen, blijft je **koopkracht gelijk** (0% verandering)."
    },
    {
      type: "invul",
      vraag: "Welke Nederlandse overheidsinstantie berekent maandelijks het inflatiecijfer en de consumentenprijsindex? (Afkorting)",
      antwoord: "CBS|cbs",
      uitleg: "Het **CBS** (Centraal Bureau voor de Statistiek) verzamelt en publiceert deze gegevens."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen nominaal inkomen en reëel inkomen?",
      opties: [
        "Nominaal is je loon in euro's; reëel is je inkomen gecorrigeerd voor de inflatie (je koopkracht).",
        "Nominaal is bruto; reëel is netto.",
        "Nominaal is wat je spaart; reëel is wat je uitgeeft.",
        "Er is geen verschil; het zijn synoniemen."
      ],
      antwoord: 0,
      uitleg: "Je **nominale** inkomen is het bedrag op je loonstrook. Je **reële** inkomen laat zien wat je er echt voor kunt kopen."
    },
    {
      type: "waaronwaar",
      vraag: "Deflatie is altijd goed voor de economie omdat consumenten dan direct meer gaan uitgeven.",
      antwoord: false,
      uitleg: "Onwaar. Deflatie kan gevaarlijk zijn omdat consumenten aankopen gaan **uitstellen** (ze wachten tot het nog goedkoper wordt), wat de economie remt."
    },
    {
      type: "mc",
      vraag: "Wat is een loon-prijsspiraal?",
      opties: [
        "Een stijging van de rente die leidt tot hogere spaartegoeden.",
        "Een proces waarbij loonsverhogingen leiden tot hogere productiekosten en hogere prijzen, wat weer leidt tot nieuwe eisen voor loonsverhoging.",
        "Een grafiek die de inkomensverschillen in beeld brengt.",
        "Een belastingmaatregel om loonstrookjes te vereenvoudigen."
      ],
      antwoord: 1,
      uitleg: "De **loon-prijsspiraal** is een vicieuze cirkel die inflatie steeds verder kan aanjagen."
    },
    {
      type: "invul",
      vraag: "Als je geld op een spaarrekening hebt staan en de inflatie is hoger dan de spaarrente, dan wordt je spaargeld reëel _______ waard.",
      antwoord: "minder",
      uitleg: "Als de prijzen sneller stijgen dan je rente, daalt de koopkracht van je spaargeld. Je geld wordt reëel **minder** waard."
    },
    {
      type: "mc",
      vraag: "Wat is 'kosteninflatie'?",
      opties: [
        "Inflatie die ontstaat doordat consumenten te veel geld willen lenen.",
        "Inflatie die ontstaat doordat de productiekosten (zoals grondstoffen of lonen) voor bedrijven stijgen en worden doorberekend in de prijzen.",
        "Een daling van de kosten voor de overheid.",
        "Het stijgen van de kosten voor het maken van munten."
      ],
      antwoord: 1,
      uitleg: "Bij **kosteninflatie** stijgen de prijzen omdat de kosten van de ondernemer (energie, grondstoffen, loon) stijgen."
    },
    {
      type: "waaronwaar",
      vraag: "Wanneer de overheid de btw-tarieven verhoogt, leidt dit over het algemeen tot een stijging van het prijsniveau (inflatie).",
      antwoord: true,
      uitleg: "Waar. Een btw-verhoging maakt producten in de winkel duurder, wat direct zorgt voor inflatie."
    },
    {
      type: "mc",
      vraag: "Wie profiteert er relatief gezien van onverwacht hoge inflatie?",
      opties: [
        "Mensen met een grote spaarpot op de bank.",
        "Mensen met een hoge schuld (de reële waarde van hun schuld neemt af).",
        "Gepensioneerden met een vast pensioen.",
        "Mensen die leven van een vaste bijstandsuitkering."
      ],
      antwoord: 1,
      uitleg: "Schuldenaren profiteren omdat de **reële waarde** van de schuld daalt bij inflatie, terwijl spaarders juist koopkracht verliezen."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een stijging van de olieprijs kan leiden tot inflatie van veel producten in de supermarkt.",
      sleutelwoorden: ["transportkosten/vervoer", "energie/verwarming kassen", "verpakkingsmateriaal/plastic", "doorberekenen aan consument/prijzen stijgen"],
      minTreffers: 2,
      modelantwoord: "Olie is nodig voor het transport van producten naar de supermarkt en voor de productie (machines, plastic verpakkingen). Als olie duurder wordt, stijgen de productiekosten van fabrikanten en transporteurs. Zij berekenen deze hogere kosten door aan de consument, waardoor supermarktproducten duurder worden.",
      uitleg: "Grondstofstijgingen werken door in de hele keten."
    },
    {
      type: "open",
      vraag: "Leg uit waarom gepensioneerden vaak harder worden getroffen door inflatie dan werkenden.",
      sleutelwoorden: ["vast pensioen/geen loonsverhoging", "geen CAO-onderhandelingen/geen loonstijging", "koopkracht daalt/minder te besteden", "aanpassing uitkeringen blijft achter"],
      minTreffers: 2,
      modelantwoord: "Werkenden kunnen via hun vakbonden onderhandelen over loonsverhogingen om de inflatie te compenseren. Gepensioneerden hebben een vast pensioen dat vaak niet of pas veel later meestijgt met de inflatie. Hierdoor daalt hun koopkracht sneller.",
      uitleg: "Vaste inkomens zijn kwetsbaarder voor prijsstijgingen."
    }
  ]
});
