/* Extra Proeftoets 15 — De Grote Finaletoets II (Mix) */
DURU.registerExamen({
  id: "ex-extra-eindtoets-mix-2",
  titel: "Extra Proeftoets 15 — De Grote Finaletoets II (Mix)",
  vak: "Economie · Eindtoets",
  icoon: "🏆",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Welke van de volgende belastingen betaal je rechtstreeks aan de provincie?",
      opties: [
        "Inkomstenbelasting",
        "Opcenten op de motorrijtuigenbelasting",
        "Btw op benzine",
        "Onroerendezaakbelasting (OZB)"
      ],
      antwoord: 1,
      uitleg: "De **opcenten** op de wegenbelasting zijn een extra toeslag die de provincie heft voor provinciale uitgaven."
    },
    {
      type: "mc",
      vraag: "Op welke dag leest de Koning de Troonrede voor en presenteert de regering de begroting?",
      opties: [
        "Op de eerste maandag van januari",
        "Op Prinsjesdag (de derde dinsdag van september)",
        "Op Koningsdag (27 april)",
        "Op de laatste vrijdag van december"
      ],
      antwoord: 1,
      uitleg: "Op **Prinsjesdag** presenteert de minister van Financiën de Miljoenennota en de Rijksbegroting."
    },
    {
      type: "mc",
      vraag: "Als de uitgaven van de overheid in een jaar groter zijn dan de inkomsten, is er sprake van een:",
      opties: [
        "Begrotingsoverschot",
        "Staatsschuldafname",
        "Begrotingstekort",
        "Btw-verlaging"
      ],
      antwoord: 2,
      uitleg: "Er is sprake van een **begrotingstekort** als er meer geld uitgaat dan er binnenkomt in de staatskas."
    },
    {
      type: "mc",
      vraag: "Welke sector bestaat uit private bedrijven die gericht zijn op het maken van winst?",
      opties: [
        "De collectieve sector",
        "De particuliere sector",
        "De publieke sector",
        "De semi-overheid"
      ],
      antwoord: 1,
      uitleg: "De **particuliere sector** (of private sector) bestaat uit bedrijven die winst willen maken. De collectieve sector bestaat uit de overheid en sociale verzekeringsinstellingen."
    },
    {
      type: "mc",
      vraag: "Een trui kost inclusief 21% btw € 121,-. Wat is de btw die in deze prijs zit?",
      opties: [
        "€ 25,41",
        "€ 21,00",
        "€ 100,00",
        "€ 17,35"
      ],
      antwoord: 1,
      uitleg: "De prijs exclusief btw is: **121 / 1,21 = € 100,-**. De btw bedraagt **121 - 100 = € 21,-**."
    },
    {
      type: "waaronwaar",
      vraag: "De overheid geeft subsidie op milieuvriendelijke producten om het gebruik ervan te stimuleren.",
      antwoord: true,
      uitleg: "Waar. Een **subsidie** maakt duurzame producten goedkoper, wat gedragsverandering stimuleert."
    },
    {
      type: "waaronwaar",
      vraag: "Het solidariteitsbeginsel houdt in dat iedereen in de samenleving alleen voor zijn eigen risico's en kosten betaalt.",
      antwoord: false,
      uitleg: "Onwaar. **Solidariteit** betekent dat we samen betalen: gezonden en werkenden dragen bij aan de zorg en uitkeringen van zieken, werklozen en ouderen."
    },
    {
      type: "invul",
      vraag: "De minister die de Rijksbegroting en de Miljoenennota presenteert is de minister van _______.",
      antwoord: "Financiën|financiën|financien",
      uitleg: "De minister van **Financiën** is verantwoordelijk voor de schatkist en het overheidsgeld."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de overheid via een progressief belastingtarief zorgt voor nivellering van de inkomens.",
      sleutelwoorden: ["progressief/schijventarief/tarieven", "hoger inkomen/hoger percentage", "draagkracht/rijk betaalt meer", "verschillen verkleinen/nivelleren/nivellering"],
      minTreffers: 2,
      modelantwoord: "In een progressief belastingstelsel betaal je een hoger percentage belasting naarmate je inkomen stijgt. Rijke mensen betalen dus relatief meer belasting. Dit geld wordt herverdeeld via uitkeringen en subsidies, waardoor de inkomensverschillen tussen rijk en arm kleiner worden (nivellering).",
      uitleg: "Progressieve schijven -> herverdeling belastinginkomsten -> kleinere inkomensverschillen."
    },
    {
      type: "open",
      vraag: "Duru, leg uit wat de staatsschuld is, hoe deze ontstaat, en waarom een te hoge staatsschuld een probleem kan zijn voor de overheid.",
      sleutelwoorden: ["begrotingstekort/tekort", "lenen/geld lenen/lening", "rente/rente betalen", "minder geld voor voorzieningen/toekomst"],
      minTreffers: 2,
      modelantwoord: "De staatsschuld is de totale schuld die de rijksoverheid heeft opgebouwd door geld te lenen om begrotingstekorten te financieren. Een te hoge staatsschuld is een probleem omdat de overheid veel rente moet betalen. Dit kost geld dat niet meer aan voorzieningen (zoals zorg of onderwijs) kan worden besteed.",
      uitleg: "Staatsschuld stijgt door begrotingstekorten en kost jaarlijks veel rente."
    }
  ]
});
