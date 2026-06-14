/* Extra Proeftoets 1 — Overheid & Voorzieningen (6.1 & 6.2) */
DURU.registerExamen({
  id: "ex-extra-overheid-voorzieningen",
  titel: "Extra Proeftoets 1 — Overheid & Voorzieningen",
  vak: "Economie · H6 (6.1 & 6.2)",
  icoon: "🏛️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wie kiest de leden van de Eerste Kamer in Nederland?",
      opties: [
        "De Nederlandse burgers rechtstreeks",
        "De leden van de Provinciale Staten",
        "De Tweede Kamer",
        "De Koning en de Minister-President"
      ],
      antwoord: 1,
      uitleg: "De burgers kiezen de leden van de Provinciale Staten. De leden van de Provinciale Staten kiezen vervolgens de 75 leden van de <b>Eerste Kamer</b>. Dit noemen we indirecte verkiezingen."
    },
    {
      type: "mc",
      vraag: "Wie vertegenwoordigt de regering en de Koning in een provincie en leidt de Gedeputeerde Staten?",
      opties: [
        "De burgemeester",
        "De Commissaris van de Koning",
        "De gedeputeerde",
        "De minister-president"
      ],
      antwoord: 1,
      uitleg: "De <b>Commissaris van de Koning</b> (CvdK) leidt het bestuur van de provincie en is de voorzitter van zowel Provinciale Staten als Gedeputeerde Staten."
    },
    {
      type: "mc",
      vraag: "Waarom is straatverlichting een zuiver collectieve voorziening?",
      opties: [
        "Omdat je het licht alleen kunt zien als je ervoor betaalt.",
        "Omdat het te duur is om door de gemeente te laten betalen.",
        "Omdat iedereen er tegelijk gebruik van maakt en je niemand kunt uitsluiten.",
        "Omdat het alleen overdag werkt."
      ],
      antwoord: 2,
      uitleg: "Je kunt mensen niet uitsluiten van <b>straatverlichting</b> als ze op straat lopen, ook al betalen ze geen belasting. Daarom kan de markt dit niet verkopen en regelt de overheid dit collectief."
    },
    {
      type: "mc",
      vraag: "Welke van de volgende voorzieningen is een voorbeeld van een SEMI-collectieve (of individuele) voorziening die door de overheid gesubsidieerd wordt?",
      opties: [
        "De rechtspraak",
        "Het openbaar vervoer (trein/bus)",
        "De politie",
        "De dijken"
      ],
      antwoord: 1,
      uitleg: "Bij het <b>openbaar vervoer</b> moet je een kaartje kopen. Wie niet betaalt, mag niet mee. Je kunt mensen dus uitsluiten. Omdat de overheid het wel belangrijk vindt en meebetaalt, is het een gesubsidieerde semi-collectieve voorziening."
    },
    {
      type: "mc",
      vraag: "Wie beslist in een gemeente over de belangrijkste plannen en controleert het college van B&W?",
      opties: [
        "De wethouder in zijn eentje",
        "De Provinciale Staten",
        "De gemeenteraad",
        "De burgemeester"
      ],
      antwoord: 2,
      uitleg: "De <b>gemeenteraad</b> is de volksvertegenwoordiging van de gemeente. Zij bepalen het beleid (de regels) en controleren of het college van B&W zijn werk goed doet."
    },
    {
      type: "waaronwaar",
      vraag: "De Eerste Kamer mag wetsvoorstellen die door de Tweede Kamer zijn goedgekeurd zelf nog aanpassen.",
      antwoord: false,
      uitleg: "Onwaar. De <b>Eerste Kamer</b> mag wetsvoorstellen alleen goedkeuren of afkeuren (recht van veto). Ze mogen de wetten niet zelf wijzigen; dat mag alleen de Tweede Kamer."
    },
    {
      type: "waaronwaar",
      vraag: "Collectieve voorzieningen worden betaald uit de algemene belastingmiddelen.",
      antwoord: true,
      uitleg: "Waar. Omdat collectieve voorzieningen voor iedereen zijn, betalen we ze samen via de belastingen die de overheid int."
    },
    {
      type: "invul",
      vraag: "Leden van de Tweede Kamer worden in principe eens in de ______ jaar rechtstreeks gekozen.",
      antwoord: "vier|4",
      uitleg: "De Tweede Kamerverkiezingen vinden normaal gesproken elke <b>vier jaar</b> plaats, tenzij het kabinet eerder valt."
    },
    {
      type: "open",
      vraag: "Waarom regelt de overheid de politie als collectieve voorziening, in plaats van dat burgers zelf beveiligers moeten inhuren?",
      sleutelwoorden: ["veiligheid/veilig", "uitsluiten/iedereen", "belasting/belastingen", "arm/armen/geld/betalen"],
      minTreffers: 2,
      modelantwoord: "Als iedereen zelf beveiligers moest betalen, zouden arme mensen niet beschermd worden. Veiligheid is belangrijk voor het hele land. Daarnaast kun je mensen niet uitsluiten van veiligheid op straat. Daarom betaalt iedereen belasting en regelt de overheid de politie voor iedereen.",
      uitleg: "Veiligheid is een basisrecht. De politie beschermt iedereen, ongeacht inkomen. Dit kan alleen collectief gefinancierd worden."
    },
    {
      type: "open",
      vraag: "Leg kort uit uit welke twee groepen personen het college van B&W in een gemeente bestaat en wat hun rol is.",
      sleutelwoorden: ["burgemeester", "wethouders/wethouder", "bestuur/besturen/dagelijks"],
      minTreffers: 2,
      modelantwoord: "Het college bestaat uit de burgemeester (de voorzitter) en de wethouders (elk met een eigen taak, zoals onderwijs of sport). Samen vormen zij het dagelijks bestuur van de gemeente.",
      uitleg: "De <b>burgemeester</b> leidt het college, en de <b>wethouders</b> voeren het beleid uit dat door de gemeenteraad is goedgekeurd."
    }
  ]
});
