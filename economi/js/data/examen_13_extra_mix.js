/* Extra Proeftoets 8 — Grote Eindtoets Economie Mix */
DURU.registerExamen({
  id: "ex-extra-eindtoets-mix",
  titel: "Extra Proeftoets 8 — Grote Eindtoets Economie Mix",
  vak: "Economie · Eindtoets",
  icoon: "🎓",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Welk deel van de overheid (de wetgevende macht) stemt in met wetsvoorstellen en controleert de regering?",
      opties: [
        "Het Kabinet (ministers en staatssecretarissen)",
        "De Koning en zijn adviseurs",
        "Het Parlement (de Eerste en Tweede Kamer)",
        "De Autoriteit Consument & Markt (ACM)"
      ],
      antwoord: 2,
      uitleg: "Het **Parlement** (de volksvertegenwoordiging) stemt over wetten en keurt de Rijksbegroting goed."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen directe en indirecte belastingen?",
      opties: [
        "Directe belastingen betaal je rechtstreeks aan de gemeente, indirecte belastingen aan het rijk.",
        "Directe belastingen betaal je over je inkomen, winst of vermogen. Indirecte belastingen zitten verwerkt in de prijs van goederen en diensten (zoals btw).",
        "Directe belastingen gelden alleen voor volwassenen, indirecte voor kinderen.",
        "Directe belastingen moeten binnen 24 uur betaald worden."
      ],
      antwoord: 1,
      uitleg: "Je betaalt **directe belastingen** rechtstreeks over je verdiende geld (bijv. loonbelasting). **Indirecte belastingen** (zoals btw en accijns) betaal je ongemerkt via je aankopen in de winkel."
    },
    {
      type: "mc",
      vraag: "Een skateboard kost €120,- inclusief 21% btw. Hoe bereken je de btw die in deze prijs zit?",
      opties: [
        "120 * 0,21",
        "120 / 121 * 21",
        "120 / 21 * 100",
        "120 * 1,21"
      ],
      antwoord: 1,
      uitleg: "De prijs inclusief btw is gelijk aan 121%. De formule om het btw-bedrag te berekenen is: **(bedrag inclusief btw / 121) * 21**."
    },
    {
      type: "mc",
      vraag: "Wanneer heeft de overheid een begrotingstekort?",
      opties: [
        "Als de staatsschuld volledig is afgelost.",
        "Als de verwachte uitgaven in de Rijksbegroting groter zijn dan de verwachte inkomsten.",
        "Als de inflatie stijgt naar 10%.",
        "Als de btw wordt verlaagd."
      ],
      antwoord: 1,
      uitleg: "Er is sprake van een **tekort** als de overheid in een begrotingsjaar meer geld wil uitgeven dan er binnenkomt. De overheid moet dan geld lenen, waardoor de staatsschuld stijgt."
    },
    {
      type: "mc",
      vraag: "Wat is nivellering?",
      opties: [
        "Het verhogen van de staatsschuld om wegen aan te leggen.",
        "Het verkleinen van de relatieve inkomensverschillen tussen hoge en lage inkomens.",
        "Het verkopen van overheidsbedrijven aan particulieren.",
        "Het verplichten van burgers om zonnepanelen te kopen."
      ],
      antwoord: 1,
      uitleg: "Bij **nivellering** zorgt de overheid via een progressief belastingstelsel en uitkeringen dat de inkomens dichter bij elkaar komen te liggen (de verschillen worden kleiner)."
    },
    {
      type: "waaronwaar",
      vraag: "De overheid heft accijns op luxe goederen zoals dure parfums, jachten en juwelen.",
      antwoord: false,
      uitleg: "Onwaar. Accijns wordt geheven op producten die schadelijk zijn voor de gezondheid of het milieu (alcohol, tabak, brandstof). Luxe goederen vallen onder het hoge btw-tarief van 21%."
    },
    {
      type: "waaronwaar",
      vraag: "De opcenten op de motorrijtuigenbelasting zijn een belangrijke inkomstenbron voor de provincies.",
      antwoord: true,
      uitleg: "Waar. Provincies mogen bovenop de landelijke wegenbelasting een eigen toeslag (opcenten) heffen om hun eigen uitgaven te financieren."
    },
    {
      type: "invul",
      vraag: "De dag waarop de Koning de Troonrede voorleest en de minister van Financiën de Miljoenennota presenteert noemen we ____________.",
      antwoord: "Prinsjesdag|prinsjesdag",
      uitleg: "Op **Prinsjesdag** (de derde dinsdag van september) opent de overheid officieel het nieuwe parlementaire jaar en presenteert ze de begroting."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de overheid via de loonbelasting zorgt voor herverdeling van inkomens op basis van het draagkrachtbeginsel.",
      sleutelwoorden: ["progressief/progressief stelsel/tarieven", "hoger percentage/meer betalen/rijken betalen meer", "draagkracht/sterkste schouders/draagkrachtbeginsel", "herverdelen/uitkeringen/nivellering"],
      minTreffers: 2,
      modelantwoord: "De overheid maakt gebruik van een progressief belastingstelsel, wat betekent dat mensen met een hoger inkomen een hoger percentage belasting betalen. Dit past bij het draagkrachtbeginsel (de sterkste schouders dragen de zwaarste lasten). Het belastinggeld wordt vervolgens via uitkeringen en subsidies herverdeeld naar mensen met lage inkomens.",
      uitleg: "Progressief stelsel -> rijk betaalt procentueel meer -> opbrengst financiert vangnetten voor armeren."
    },
    {
      type: "open",
      vraag: "Noem twee collectieve voorzieningen en leg uit waarom de vrije markt deze niet zelfstandig en efficiënt kan leveren.",
      sleutelwoorden: ["straatverlichting/dijken/politie/defensie/wegen", "niet uitsluiten/iedereen gebruikt", "vrijbuiters/vrijbuitersgedrag", "geen winst/geen individuele prijs"],
      minTreffers: 2,
      modelantwoord: "Voorbeelden zijn straatverlichting en dijken. Een privaat bedrijf kan deze goederen niet via de markt verkopen omdat je mensen er niet van kunt uitsluiten; iedereen maakt er gebruik van. Omdat niemand er vrijwillig individueel voor wil betalen (vrijbuitersgedrag), kan er geen winst op worden gemaakt en levert de vrije markt ze niet.",
      uitleg: "Collectieve goederen hebben geen uitsluitingsmogelijkheid, dus marktwerking faalt."
    }
  ]
});
