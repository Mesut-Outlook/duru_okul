/* Extra Proeftoets 9 — De Gemeente & Lokale Overheid */
DURU.registerExamen({
  id: "ex-extra-gemeente-lokaal",
  titel: "Extra Proeftoets 9 — De Gemeente & Lokale Overheid",
  vak: "Economie · Gemeente",
  icoon: "🏡",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wie bestuurt de gemeente op dagelijkse basis (het dagelijks bestuur)?",
      opties: [
        "De gemeenteraad",
        "Het college van Burgemeester en Wethouders (B&W)",
        "De Commissaris van de Koning",
        "De Minister van Binnenlandse Zaken"
      ],
      antwoord: 1,
      uitleg: "Het **college van B&W** vormt het dagelijks bestuur van de gemeente. Zij voeren de plannen en wetten uit."
    },
    {
      type: "mc",
      vraag: "Welk orgaan controleert het college van B&W en neemt de belangrijkste besluiten (de volksvertegenwoordiging)?",
      opties: [
        "De Provinciale Staten",
        "De Tweede Kamer",
        "De gemeenteraad",
        "De Consumentenbond"
      ],
      antwoord: 2,
      uitleg: "De **gemeenteraad** wordt rechtstreeks gekozen door de inwoners en heeft de wetgevende en controlerende macht binnen de gemeente."
    },
    {
      type: "mc",
      vraag: "Hoe heten de lokale regels en wetten die alleen binnen een bepaalde gemeente gelden?",
      opties: [
        "De Rijksbegroting",
        "De Algemene Plaatselijke Verordening (APV)",
        "Het bestemmingsplan",
        "De Miljoenennota"
      ],
      antwoord: 1,
      uitleg: "In de **APV** staan de gemeentelijke regels over bijvoorbeeld hondenpoep, geluidsoverlast, parkeren en evenementen."
    },
    {
      type: "mc",
      vraag: "Welke belasting betaalt een huiseigenaar jaarlijks aan de gemeente over de waarde van zijn woning?",
      opties: [
        "Inkomstenbelasting",
        "Onroerendezaakbelasting (OZB)",
        "Motorrijtuigenbelasting",
        "Loonbelasting"
      ],
      antwoord: 1,
      uitleg: "De **OZB** wordt geheven over de WOZ-waarde van onroerende zaken zoals huizen en bedrijfspanden."
    },
    {
      type: "mc",
      vraag: "Welke gemeentelijke heffing betaal je om de kosten van het inzamelen en verwerken van huisvuil te dekken?",
      opties: [
        "Rioolheffing",
        "Afvalstoffenheffing",
        "Kansenspelbelasting",
        "Toeristenbelasting"
      ],
      antwoord: 1,
      uitleg: "De **afvalstoffenheffing** is een doelbelasting: de opbrengst mag alleen gebruikt worden voor het ophalen en verwerken van afval."
    },
    {
      type: "waaronwaar",
      vraag: "De burgemeester wordt in Nederland rechtstreeks door de inwoners van de gemeente gekozen via verkiezingen.",
      antwoord: false,
      uitleg: "Onwaar. De burgemeester wordt in Nederland benoemd door de regering (de Kroon), op advies van de gemeenteraad."
    },
    {
      type: "waaronwaar",
      vraag: "Een bestemmingsplan (waarin staat of een stuk grond gebruikt mag worden voor woningen, winkels of natuur) wordt vastgesteld door de gemeenteraad.",
      antwoord: true,
      uitleg: "Waar. Het **bestemmingsplan** is een belangrijk ruimtelijk besluit dat door de gemeenteraad moet worden goedgekeurd."
    },
    {
      type: "invul",
      vraag: "De lokale regels en wetten van een gemeente staan in de afkorting de _______.",
      antwoord: "APV",
      uitleg: "APV staat voor **Algemene Plaatselijke Verordening**."
    },
    {
      type: "open",
      vraag: "Wat is de belangrijkste taak van de gemeenteraad en hoe verschilt dit van het college van B&W?",
      sleutelwoorden: ["volksvertegenwoordiging/gekozen", "controleren/controleert B&W", "besluiten nemen/wetten maken", "B&W voert uit/dagelijks bestuur"],
      minTreffers: 2,
      modelantwoord: "De gemeenteraad is de volksvertegenwoordiging (gekozen door de burgers) die de grote besluiten neemt en het college van B&W controleert. Het college van B&W (Burgemeester en Wethouders) is het dagelijks bestuur dat de plannen en wetten daadwerkelijk uitvoert.",
      uitleg: "Gemeenteraad = besluiten & controle (wetgevend). B&W = uitvoerend (dagelijks bestuur)."
    },
    {
      type: "open",
      vraag: "Noem twee voorzieningen die door de gemeente worden geregeld en leg uit hoe ze dit betalen.",
      sleutelwoorden: ["parken/sportvelden/zwembad/bibliotheek/afval/riool/onderhoud", "belastingen/ozb/afvalstoffenheffing/gemeentefonds/Rijk"],
      minTreffers: 2,
      modelantwoord: "Voorbeelden zijn het onderhoud van lokale parken/wegen en het ophalen van huisvuil. De gemeente betaalt dit met geld dat ze krijgen van het Rijk (via het Gemeentefonds) en uit eigen belastingen zoals de OZB en de afvalstoffenheffing.",
      uitleg: "Lokale voorzieningen worden gefinancierd uit het gemeentefonds en lokale belastingen."
    }
  ]
});
