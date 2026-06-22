/* Extra Proeftoets 35 — Inkomstenbelasting & Loonbelasting VI */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting-6",
  titel: "Extra Proeftoets 35 — Inkomstenbelasting & Loonbelasting VI",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Duru heeft twee bijbaantjes: Job A (supermarkt, salaris € 400,- per maand) en Job B (oppassen, salaris € 150,- per maand). Wat is de beste keuze voor haar loonheffingskorting?",
      opties: [
        "Loonheffingskorting aanzetten bij Job A en uitzetten bij Job B.",
        "Loonheffingskorting aanzetten bij Job B en uitzetten bij Job A.",
        "Bij beide banen de loonheffingskorting aanzetten.",
        "Bij beide banen de loonheffingskorting uitzetten."
      ],
      antwoord: 0,
      uitleg: "Je moet de loonheffingskorting aanzetten bij de baan waar je het **meest** verdient (Job A) en uitzetten bij de baan waar je minder verdient (Job B). Zo voorkom je dat je achteraf moet bijbetalen."
    },
    {
      type: "waaronwaar",
      vraag: "Als je de loonheffingskorting ten onrechte niet hebt aangevraagd tijdens het jaar, ben je dit geld definitief kwijt.",
      antwoord: false,
      uitleg: "Onwaar. Als er gedurende het jaar te veel belasting is ingehouden (omdat je de korting niet aan had staan), kun je dit geld gewoon terugkrijgen door aan het eind van het jaar **belastingaangifte te doen**."
    },
    {
      type: "invul",
      vraag: "Hoe noemen we de verschillende percentages/trappen waarmee de Belastingdienst belasting over je inkomen berekent?",
      antwoord: "schijventarief|belastingschijven|schijven|schijf",
      uitleg: "In Nederland rekenen we met belastingschijven; dit heet het **schijventarief**."
    },
    {
      type: "mc",
      vraag: "Stel, Schijf 1 (tot € 75.000) heeft een belastingtarief van 37% en Schijf 2 (boven € 75.000) heeft een tarief van 49,5%. Iemand verdient € 80.000. Hoeveel procent belasting betaalt deze persoon over de eerste € 75.000?",
      opties: [
        "49,5%",
        "37%",
        "12,5%",
        "Niets, de eerste schijf is belastingvrij."
      ],
      antwoord: 1,
      uitleg: "Over de eerste € 75.000 betaal je het tarief van Schijf 1, dus **37%**. Alleen over het deel dat in Schijf 2 valt (de resterende € 5.000) betaal je 49,5%."
    },
    {
      type: "waaronwaar",
      vraag: "Als je door een loonsverhoging in een hogere belastingschijf terechtkomt, betaal je over je gehele inkomen het hogere belastingpercentage.",
      antwoord: false,
      uitleg: "Onwaar. Je betaalt het hogere percentage **alleen over het deel** van het inkomen dat in die hogere schijf valt. Je gaat er netto dus altijd op vooruit."
    },
    {
      type: "mc",
      vraag: "Welke instantie bepaalt uiteindelijk definitief of je geld terugkrijgt of moet bijbetalen?",
      opties: [
        "Je werkgever.",
        "De Belastingdienst, na controle van je belastingaangifte.",
        "Je eigen bank.",
        "De gemeenteraad."
      ],
      antwoord: 1,
      uitleg: "De **Belastingdienst** controleert de aangifte en stuurt je een definitieve aanslag."
    },
    {
      type: "invul",
      vraag: "Welke digitale identificatiecode gebruikt een burger in Nederland om veilig in te loggen bij de Belastingdienst?",
      antwoord: "DigiD|digid",
      uitleg: "Je logt in bij overheidsinstanties (zoals de Belastingdienst) met je **DigiD**."
    },
    {
      type: "mc",
      vraag: "Wat betekent het 'draagkrachtbeginsel'?",
      opties: [
        "Dat mensen met een zwaar beroep minder belasting hoeven te betalen.",
        "Dat wie financieel sterker is en meer verdient, verhoudingsgewijs meer belasting bijdraagt.",
        "Dat je belasting betaalt op basis van hoe zwaar de producten zijn die je koopt.",
        "Dat de sterkste bedrijven geen belasting hoeven te betalen."
      ],
      antwoord: 1,
      uitleg: "Het **draagkrachtbeginsel** betekent dat mensen met een hoger inkomen meer belasting kunnen missen en dus ook procentueel meer bijdragen aan de samenleving."
    },
    {
      type: "waaronwaar",
      vraag: "In een progressief belastingstelsel dragen de mensen met de hoogste inkomens procentueel de meeste belasting bij.",
      antwoord: true,
      uitleg: "Waar. Dit sluit aan bij het **draagkrachtbeginsel**: wie meer kan dragen, betaalt verhoudingsgewijs meer belasting."
    },
    {
      type: "mc",
      vraag: "Kijk goed mee, Duru! Bereken het nettoloon. Het brutoloon is € 2.000,-. De ingehouden loonbelasting is € 400,- en de premies zijn € 100,-. Er wordt € 50,- loonheffingskorting toegepast. Hoeveel nettoloon blijft er over?",
      opties: [
        "€ 1.450,-",
        "€ 1.500,-",
        "€ 1.550,-",
        "€ 2.000,-"
      ],
      antwoord: 2,
      uitleg: "Inhoudingen = Loonbelasting (€ 400) + Premies (€ 100) - Korting (€ 50) = € 450. Nettoloon = Brutoloon (€ 2000) - Inhoudingen (€ 450) = **€ 1.550,-**."
    },
    {
      type: "invul",
      vraag: "Hoe heet het strookje dat je elke maand van je werkgever krijgt waarop je bruto- en nettoloon en alle inhoudingen staan?",
      antwoord: "loonstrook|loonstrookje|salarisspecificatie|salarisstrook",
      uitleg: "Dit document noemen we de **loonstrook** of **salarisspecificatie**."
    },
    {
      type: "open",
      vraag: "Leg uit wat het 'draagkrachtbeginsel' inhoudt en hoe dit in de inkomstenbelasting is terug te zien.",
      sleutelwoorden: ["sterkste schouders/hoger inkomen", "meer belasting betalen/hoger percentage", "draagkracht/financieel sterker", "progressief/schijven"],
      minTreffers: 2,
      modelantwoord: "Het draagkrachtbeginsel houdt in dat mensen die financieel sterker zijn (meer verdienen) meer belasting betalen dan mensen met een laag inkomen. In de inkomstenbelasting zie je dit terug doordat we belastingschijven hebben waarbij het belastingpercentage stijgt naarmate je inkomen hoger is (progressief stelsel).",
      uitleg: "Hogere inkomens dragen procentueel meer bij aan de overheidsinkomsten."
    },
    {
      type: "mc",
      vraag: "Waarom vergelijkt de Belastingdienst aan het eind van het jaar de ingehouden loonbelasting met de verschuldigde inkomstenbelasting?",
      opties: [
        "Om te controleren of je wel genoeg geld op je spaarrekening hebt.",
        "Om te controleren of er gedurende het jaar via de voorheffing te veel of te weinig belasting is betaald.",
        "Omdat de werkgever aan het eind van het jaar failliet kan gaan.",
        "Om de btw op je aankopen te verrekenen."
      ],
      antwoord: 1,
      uitleg: "De loonbelasting is een geschatte maandelijks ingehouden voorheffing. Aan het eind van het jaar berekent de fiscus het echte jaarbedrag en **verrekent** dit."
    },
    {
      type: "waaronwaar",
      vraag: "Aftrekposten verhogen het bedrag waarover je belasting moet betalen, zodat de schatkist voller wordt.",
      antwoord: false,
      uitleg: "Onwaar. Aftrekposten verlagen het belastbare inkomen, waardoor je **minder** belasting hoeft te betalen."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een progressief belastingstelsel bijdraagt aan het verkleinen van inkomensverschillen (nivellering) in een land.",
      sleutelwoorden: ["hogere inkomens betalen meer percentage/belasting", "lage inkomens houden relatief meer over", "inkomensverschillen kleiner worden", "solidariteit/herverdelen"],
      minTreffers: 2,
      modelantwoord: "In een progressief belastingstelsel betalen mensen met een hoog inkomen een groter percentage aan belasting dan mensen met een laag inkomen. Hierdoor worden de verschillen in besteedbaar (netto) inkomen tussen rijke en arme mensen kleiner, wat leidt tot nivellering.",
      uitleg: "Door hogere inkomens procentueel zwaarder te belasten, krimpen de netto inkomensverschillen."
    }
  ]
});
