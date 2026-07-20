/* Extra Proeftoets 6 — De Rijksoverheid: Den Haag regeert */
DURU.registerExamen({
  id: "ex-extra-rijksoverheid-denhaag",
  titel: "Extra Proeftoets 6 — De Rijksoverheid: Den Haag regeert",
  vak: "Economie · De Overheid",
  icoon: "🏛️",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Waar zit de rijksoverheid, die zaken regelt voor heel Nederland?",
      opties: [
        "In de hoofdstad van elke provincie",
        "In Den Haag",
        "In het gemeentehuis van de grootste stad",
        "Bij de Verenigde Naties"
      ],
      antwoord: 1,
      uitleg: "De **rijksoverheid** zit in **Den Haag** en regelt zaken die voor het hele land gelden, zoals onderwijs en veiligheid."
    },
    {
      type: "mc",
      vraag: "Uit wie bestaat de regering van Nederland?",
      opties: [
        "De koning en de ministers",
        "De burgemeester en de wethouders",
        "De Provinciale Staten",
        "De gemeenteraad en de koning"
      ],
      antwoord: 0,
      uitleg: "De **regering** bestaat uit de **koning en de ministers** samen."
    },
    {
      type: "mc",
      vraag: "Hoe wordt de minister-president ook wel genoemd?",
      opties: [
        "Burgemeester",
        "Premier",
        "Commissaris",
        "Voorzitter van de Tweede Kamer"
      ],
      antwoord: 1,
      uitleg: "De **minister-president** wordt ook **premier** genoemd en leidt de regering."
    },
    {
      type: "mc",
      vraag: "Welke twee Kamers controleren samen de regering?",
      opties: [
        "De Eerste Kamer en de Tweede Kamer",
        "De gemeenteraad en de provincie",
        "Het college van B en W en de Tweede Kamer",
        "De Eerste Kamer en de gemeenteraad"
      ],
      antwoord: 0,
      uitleg: "De **Eerste Kamer** en de **Tweede Kamer** controleren samen of de regering goed werk doet."
    },
    {
      type: "mc",
      vraag: "Welke taak regelt de rijksoverheid, en niet de gemeente of de provincie?",
      opties: [
        "Het ophalen van huisvuil",
        "De aanleg van spoorwegen en autosnelwegen voor heel het land",
        "Het uitgeven van paspoorten aan inwoners",
        "Het aanleggen van een lokaal speelpark"
      ],
      antwoord: 1,
      uitleg: "**Spoorwegen en autosnelwegen** zijn er voor heel het land, dus dit regelt de **rijksoverheid**."
    },
    {
      type: "mc",
      vraag: "Welke minister gaat over de rijksbegroting (alle inkomsten en uitgaven van het Rijk)?",
      opties: [
        "De minister van Onderwijs",
        "De minister-president",
        "De minister van Financiën",
        "De minister van Defensie"
      ],
      antwoord: 2,
      uitleg: "De **minister van Financiën** is verantwoordelijk voor de **rijksbegroting**."
    },
    {
      type: "waaronwaar",
      vraag: "De rijksoverheid zorgt ervoor dat het onderwijs in heel Nederland op een gelijk niveau is.",
      antwoord: true,
      uitleg: "Waar. De **rijksoverheid** bewaakt dat scholen in heel het land aan dezelfde kwaliteitseisen voldoen."
    },
    {
      type: "waaronwaar",
      vraag: "Het leger en de dijken zijn voorbeelden van veiligheid die de gemeente regelt.",
      antwoord: false,
      uitleg: "Onwaar. **Leger en dijken** vallen onder veiligheid die de **rijksoverheid** regelt, niet de gemeente."
    },
    {
      type: "waaronwaar",
      vraag: "De gemeenteraad lijkt qua functie op de Tweede Kamer, omdat beide het bestuur controleren.",
      antwoord: true,
      uitleg: "Waar. Net zoals de **Tweede Kamer** de regering controleert, controleert de **gemeenteraad** het college van B en W."
    },
    {
      type: "waaronwaar",
      vraag: "De ministers worden door de inwoners van Nederland rechtstreeks gekozen tijdens de gemeenteraadsverkiezingen.",
      antwoord: false,
      uitleg: "Onwaar. Ministers maken deel uit van de **regering** en worden niet via gemeenteraadsverkiezingen gekozen."
    },
    {
      type: "invul",
      vraag: "De regering bestaat uit de koning en de _______.",
      antwoord: "ministers",
      uitleg: "De regering = de koning + de **ministers**."
    },
    {
      type: "invul",
      vraag: "De minister-president wordt ook wel de _______ genoemd.",
      antwoord: "premier",
      uitleg: "**Premier** is een andere naam voor de minister-president."
    },
    {
      type: "invul",
      vraag: "Heel Nederland wordt bestuurd door de regering en gecontroleerd door de Eerste en Tweede _______.",
      antwoord: "Kamer",
      uitleg: "De Eerste en Tweede **Kamer** controleren samen de regering."
    },
    {
      type: "open",
      vraag: "Leg uit wie de regering van Nederland vormt en wie deze regering controleert.",
      sleutelwoorden: ["koning/ministers", "regering", "Eerste Kamer/Tweede Kamer/controleren"],
      minTreffers: 2,
      modelantwoord: "De regering bestaat uit de koning en de ministers. De Eerste Kamer en de Tweede Kamer controleren samen of de regering haar werk goed doet.",
      uitleg: "Regering = koning + ministers; gecontroleerd door Eerste en Tweede Kamer."
    },
    {
      type: "open",
      vraag: "Noem twee taken die de rijksoverheid (Den Haag) regelt voor heel Nederland en leg uit waarom dit op landelijk niveau gebeurt.",
      sleutelwoorden: ["onderwijs/gelijk niveau", "veiligheid/politie/leger/dijken", "spoorwegen/autosnelwegen", "heel het land/landelijk"],
      minTreffers: 2,
      modelantwoord: "De rijksoverheid regelt bijvoorbeeld dat het onderwijs in heel het land op een gelijk niveau is en zorgt voor veiligheid via politie, leger en dijken. Dit gebeurt op landelijk niveau omdat deze zaken voor alle inwoners van Nederland gelijk moeten zijn, niet alleen voor één gemeente of provincie.",
      uitleg: "De rijksoverheid regelt zaken die voor heel het land gelden, zoals onderwijs, veiligheid en spoorwegen/autosnelwegen."
    }
  ]
});
