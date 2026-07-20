/* Extra Proeftoets 36 — De Overheid als Bestuurder */
DURU.registerExamen({
  id: "ex-extra-consument-overheid-2",
  titel: "Extra Proeftoets 36 — De Overheid als Bestuurder",
  vak: "Economie · Rijksoverheid",
  icoon: "🏛️",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wie vormen samen de regering van Nederland?",
      opties: [
        "De Koning en de Tweede Kamer.",
        "De Koning en de ministers.",
        "De Tweede Kamer en de Eerste Kamer.",
        "De ministers en de wethouders."
      ],
      antwoord: 1,
      uitleg: "De **regering** bestaat uit de Koning en de ministers samen. De Koning is het staatshoofd, maar de ministers zijn politiek verantwoordelijk."
    },
    {
      type: "waaronwaar",
      vraag: "De minister-president (premier) is de voorzitter van de ministerraad en de leider van de ministers.",
      antwoord: true,
      uitleg: "Waar. De **minister-president** is het hoofd van de regering en leidt de wekelijkse vergaderingen van de ministers."
    },
    {
      type: "invul",
      vraag: "In welke Nederlandse stad bevindt zich het centrum van de rijksoverheid (het parlement en de ministeries)?",
      antwoord: "Den Haag|den haag|'s-Gravenhage",
      uitleg: "**Den Haag** is de regeringsstad van Nederland."
    },
    {
      type: "mc",
      vraag: "Hoeveel volksvertegenwoordigers zitten er in de Tweede Kamer?",
      opties: [
        "75 gekozen leden.",
        "150 gekozen leden.",
        "220 gekozen leden.",
        "340 gekozen leden."
      ],
      antwoord: 1,
      uitleg: "De **Tweede Kamer** bestaat uit **150 leden** die rechtstreeks door de Nederlandse bevolking worden gekozen."
    },
    {
      type: "waaronwaar",
      vraag: "De Eerste Kamer (75 leden) heeft als belangrijkste taak het beoordelen en goedkeuren of afkeuren van wetten die al door de Tweede Kamer zijn aangenomen.",
      antwoord: true,
      uitleg: "Waar. De **Eerste Kamer** controleert of wetsvoorstellen van de Tweede Kamer deugen, maar mag ze niet meer zelf aanpassen."
    },
    {
      type: "invul",
      vraag: "Hoe heet het document waarin de regering de plannen en de begroting voor het komende jaar presenteert op Prinsjesdag?",
      antwoord: "Miljoenennota|de Miljoenennota",
      uitleg: "Op Prinsjesdag wordt de **Miljoenennota** samen met de Rijksbegroting gepresenteerd door de minister van Financiën."
    },
    {
      type: "mc",
      vraag: "Welk ministerie is verantwoordelijk voor het beheren van de schatkist en het innen van de belastingen?",
      opties: [
        "Het Ministerie van Binnenlandse Zaken.",
        "Het Ministerie van Financiën.",
        "Het Ministerie van Economische Zaken.",
        "Het Ministerie van Justitie en Veiligheid."
      ],
      antwoord: 1,
      uitleg: "Het **Ministerie van Financiën** gaat over het geld van de rijksoverheid en stelt de begroting op."
    },
    {
      type: "waaronwaar",
      vraag: "Ministers mogen zelfstandig nieuwe wetten invoeren zonder dat de Tweede en Eerste Kamer hierover stemmen.",
      antwoord: false,
      uitleg: "Onwaar. In een democratie moet het **parlement** (de Eerste en Tweede Kamer) altijd akkoord gaan met een nieuwe wet voordat deze geldig is."
    },
    {
      type: "open",
      vraag: "Leg uit wat de verschillende rollen zijn van de Tweede Kamer en de Eerste Kamer bij het maken van wetten in Nederland.",
      sleutelwoorden: ["Tweede Kamer/wetsvoorstellen/wijzigen/ontwerpen", "Eerste Kamer/beoordelen/controleren/keuren", "parlement/stemmen", "volksvertegenwoordiging"],
      minTreffers: 2,
      modelantwoord: "De Tweede Kamer ontwerpt wetten, bespreekt ze en mag er wijzigingen in aanbrengen. Als de Tweede Kamer voorstemt, gaat het voorstel naar de Eerste Kamer. De Eerste Kamer mag de wet alleen nog goedkeuren of afwijzen, niet meer veranderen.",
      uitleg: "De Tweede Kamer past aan en ontwerpt; de Eerste Kamer toetst en keurt definitief goed of af."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen het kabinet en de regering?",
      sleutelwoorden: ["kabinet/ministers en staatssecretarissen", "regering/koning en ministers", "koning geen deel", "staatshoofd"],
      minTreffers: 2,
      modelantwoord: "De regering bestaat uit de Koning en de ministers. Het kabinet bestaat uit de ministers en de staatssecretarissen samen (de Koning maakt dus geen deel uit van het kabinet).",
      uitleg: "Koning + ministers = regering. Ministers + staatssecretarissen = kabinet."
    }
  ]
});
