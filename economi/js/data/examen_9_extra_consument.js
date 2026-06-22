/* Extra Proeftoets 4 — Collectieve Voorzieningen & Overheidstaken */
DURU.registerExamen({
  id: "ex-extra-consument-overheid",
  titel: "Extra Proeftoets 4 — Collectieve Voorzieningen & Overheidstaken",
  vak: "Economie · Overheidstaken",
  icoon: "🏛️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat zijn collectieve voorzieningen?",
      opties: [
        "Producten die je alleen in de supermarkt kunt kopen.",
        "Voorzieningen die door de overheid worden betaald en geregeld, omdat iedereen er belang bij heeft.",
        "Diensten die alleen voor ambtenaren bedoeld zijn.",
        "Leningen die particuliere banken verstrekken."
      ],
      antwoord: 1,
      uitleg: "**Collectieve voorzieningen** zijn diensten en goederen die de overheid regelt en betaalt met belastinggeld, zoals politie, brandweer en wegen."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende voorzieningen is een voorbeeld van een collectieve voorziening?",
      opties: [
        "Een pretparkbezoek.",
        "De straatverlichting en het onderhoud van wegen.",
        "Een abonnement op een streamingdienst.",
        "De aankoop van een nieuwe fiets."
      ],
      antwoord: 1,
      uitleg: "**Straatverlichting** en wegen zijn openbaar en voor iedereen toegankelijk. De overheid regelt dit collectief."
    },
    {
      type: "waaronwaar",
      vraag: "De overheid levert collectieve voorzieningen vooral omdat commerciële bedrijven hier vaak geen winst op kunnen maken.",
      antwoord: true,
      uitleg: "Waar. Omdat je mensen niet gemakkelijk kunt uitsluiten van het gebruik (zoals bij dijken), willen bedrijven deze goederen niet produceren. De overheid doet dit dus."
    },
    {
      type: "mc",
      vraag: "Waarom heft de overheid accijns op tabak, benzine en alcohol?",
      opties: [
        "Omdat deze goederen heel goedkoop te maken zijn.",
        "Om het gebruik van schadelijke of milieuvervuilende producten af te remmen.",
        "Omdat de koning deze producten zelf veel gebruikt.",
        "Om te zorgen dat er minder winkels in Nederland komen."
      ],
      antwoord: 1,
      uitleg: "**Accijns** is een extra belasting bedoeld om het gedrag te beïnvloeden en de consumptie van ongezonde of schadelijke goederen te ontmoedigen."
    },
    {
      type: "mc",
      vraag: "Wat is meeliftgedrag (free-ridergedrag) in de economie?",
      opties: [
        "Gratis meereizen met het openbaar vervoer zonder kaartje.",
        "Profiteren van een collectieve voorziening zonder er zelf aan mee te betalen via belastingen.",
        "Samen met je vrienden op één fiets rijden om kosten te sparen.",
        "Het importeren van goedkope goederen uit het buitenland."
      ],
      antwoord: 1,
      uitleg: "**Meeliftgedrag** betekent dat iemand geniet van voorzieningen (zoals straatverlichting of veiligheid) zonder hieraan bij te dragen (bijvoorbeeld door belasting te ontwijken)."
    },
    {
      type: "waaronwaar",
      vraag: "De particuliere sector bestaat uit alle organisaties en bedrijven die eigendom zijn van de overheid.",
      antwoord: false,
      uitleg: "Onwaar. De **particuliere sector** bestaat uit private bedrijven die gericht zijn op het maken van winst. De overheid behoort tot de collectieve sector."
    },
    {
      type: "mc",
      vraag: "Waarom kan een voorziening zoals een dijk die ons beschermt tegen overstromingen niet via de vrije markt verkocht worden?",
      opties: [
        "Omdat een dijk te duur is om te bouwen voor de overheid.",
        "Omdat je mensen die niet betalen niet kunt uitsluiten van de bescherming die de dijk biedt.",
        "Omdat dijken alleen in de provincie Utrecht nodig zijn.",
        "Omdat burgers dijken liever zelf bouwen."
      ],
      antwoord: 1,
      uitleg: "Een dijk biedt bescherming aan het hele gebied. Omdat je niet-betalers niet kunt uitsluiten, gaat niemand er vrijwillig voor betalen op de markt. Dit is een **zuiver collectief goed**."
    },
    {
      type: "invul",
      vraag: "Hoe noemen we iemand die profiteert van een collectieve voorziening (zoals een veilige straat) zonder daarvoor belasting te betalen? Een meelif____.",
      antwoord: "ter|ters|tergedrag|ter gedrag",
      uitleg: "Deze persoon noemen we een **meelifter** (free-rider)."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overheid straatverlichting zelf moet regelen en betalen, in plaats van dit over te laten aan private bedrijven op de markt.",
      sleutelwoorden: ["niet uitsluiten/iedereen profiteert/profiteren", "geen prijs bepalen/onmogelijk individueel betalen", "meeliftgedrag/meelifters/gratis", "geen winst te maken/bedrijven willen dit niet"],
      minTreffers: 2,
      modelantwoord: "Straatverlichting is een collectief goed. Je kunt mensen die niet betalen niet uitsluiten van het licht op straat. Hierdoor ontstaat meeliftgedrag: mensen gaan niet vrijwillig betalen. Omdat een private onderneming hierdoor geen winst kan maken, moet de overheid dit met belastinggeld financieren.",
      uitleg: "Niet-uitsluitbaarheid maakt marktwerking onmogelijk en dwingt collectieve financiering af."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen btw en accijns?",
      sleutelwoorden: ["accijns/specifiek/bepaald", "btw/algemeen/percentage", "remmen/gezondheid/schadelijk"],
      minTreffers: 2,
      modelantwoord: "Btw is een algemene omzetbelasting die op bijna elk product en elke dienst zit als percentage van de prijs (9% of 21%). Accijns is een extra, specifieke belasting die per volume (bijvoorbeeld per liter of per pakje) wordt geheven op geselecteerde schadelijke goederen zoals tabak en alcohol om het gebruik te remmen.",
      uitleg: "Btw is een algemeen percentage op consumptie. Accijns is een vast bedrag per volume op schadelijke goederen."
    }
  ]
});
