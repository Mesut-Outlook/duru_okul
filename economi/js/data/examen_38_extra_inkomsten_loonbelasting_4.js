/* Extra Proeftoets 33 — Inkomstenbelasting & Loonbelasting IV */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting-4",
  titel: "Extra Proeftoets 33 — Inkomstenbelasting & Loonbelasting IV",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is 'belastingaangifte doen'?",
      opties: [
        "Het doorgeven van je inkomsten en persoonlijke gegevens aan de Belastingdienst na afloop van het jaar.",
        "Aangifte doen bij de politie als er geld van je rekening is gestolen.",
        "De rekening die je van de supermarkt krijgt voor je btw.",
        "Een formulier invullen om te bewijzen dat je geen belasting hoeft te betalen."
      ],
      antwoord: 0,
      uitleg: "Met de **belastingaangifte** geef je aan de Belastingdienst door wat je het afgelopen jaar hebt verdiend en welke aftrekposten je hebt. De Belastingdienst berekent dan de definitieve inkomstenbelasting."
    },
    {
      type: "waaronwaar",
      vraag: "Alleen mensen met een eigen bedrijf hoeven jaarlijks belastingaangifte te doen.",
      antwoord: false,
      uitleg: "Onwaar. Iedereen die in loondienst werkt of andere inkomsten heeft (en een uitnodiging krijgt of geld terug verwacht) kan of moet **belastingaangifte doen**."
    },
    {
      type: "invul",
      vraag: "Hoe heet het formulier of proces waarbij je na afloop van het jaar je inkomensgegevens invult voor de fiscus?",
      antwoord: "belastingaangifte|aangifte|aangifte doen",
      uitleg: "Dit noemen we de **belastingaangifte**."
    },
    {
      type: "mc",
      vraag: "Stel: Milan heeft in een jaar € 1.200,- aan loonbelasting vooraf betaald via zijn loonstrookjes. Aan het eind van het jaar berekent de Belastingdienst dat hij € 1.400,- aan inkomstenbelasting moet betalen. Wat moet Milan doen?",
      opties: [
        "Hij krijgt € 200,- terug van de Belastingdienst.",
        "Hij hoeft niets te doen; € 1.200,- is dichtbij genoeg.",
        "Hij moet € 200,- bijbetalen aan de Belastingdienst.",
        "Hij moet alsnog € 1.400,- volledig betalen."
      ],
      antwoord: 2,
      uitleg: "Milan heeft € 1.200 vooraf betaald, maar moet in totaal € 1.400 betalen. Hij moet het verschil **1400 - 1200 = € 200,- bijbetalen**."
    },
    {
      type: "waaronwaar",
      vraag: "Als je gedurende het jaar € 1.500,- aan loonbelasting hebt betaald, maar je definitieve inkomstenbelasting is € 1.300,-, dan krijg je € 200,- terug van de Belastingdienst.",
      antwoord: true,
      uitleg: "Waar. Omdat er vooraf meer belasting is ingehouden dan je daadwerkelijk verschuldigd bent, krijg je het verschil (**€ 200,-**) netjes teruggestort."
    },
    {
      type: "mc",
      vraag: "Waarom berekent de Belastingdienst de belasting pas definitief aan het eind van het jaar?",
      opties: [
        "Omdat ze gedurende het jaar vakantie vieren.",
        "Omdat pas aan het eind van het jaar je totale jaarinkomen en al je aftrekposten precies bekend zijn.",
        "Omdat werkgevers pas in december loonbelasting inhouden.",
        "Zodat de rente voor de overheid hoger is."
      ],
      antwoord: 1,
      uitleg: "Gedurende het jaar kan je inkomen veranderen of kun je extra kosten (zoals ziektekosten of hypotheekrente) hebben. Pas na 31 december is je **totale jaarinkomen** bekend."
    },
    {
      type: "invul",
      vraag: "Als de Belastingdienst berekent dat er te weinig loonbelasting is ingehouden op je loon, wat moet je dan doen met het verschil?",
      antwoord: "bijbetalen|terugbetalen|betalen",
      uitleg: "Als er te weinig is ingehouden, moet je het resterende bedrag **bijbetalen**."
    },
    {
      type: "mc",
      vraag: "Wat is een voorbeeld van een aftrekpost (kosten die je van je inkomen mag aftrekken voordat de belasting wordt berekend)?",
      opties: [
        "De kosten voor een vakantie naar Spanje.",
        "De rente op je hypotheek voor een eigen huis (hypotheekrenteaftrek).",
        "De aankoop van een nieuwe spelcomputer.",
        "Het geld dat je uitgeeft aan kleding."
      ],
      antwoord: 1,
      uitleg: "De **hypotheekrenteaftrek** is een bekende aftrekpost in Nederland. Hierdoor wordt je belastbare inkomen lager en betaal je minder belasting."
    },
    {
      type: "waaronwaar",
      vraag: "Een aftrekpost zorgt ervoor dat het bedrag waarover je belasting moet betalen groter wordt.",
      antwoord: false,
      uitleg: "Onwaar. Een aftrekpost zorgt er juist voor dat je belastbare inkomen **lager** wordt, waardoor je uiteindelijk minder belasting betaalt."
    },
    {
      type: "mc",
      vraag: "Waarom is inkomstenbelasting een directe belasting?",
      opties: [
        "Omdat je het geld rechtstreeks aan de Belastingdienst betaalt over je eigen inkomen.",
        "Omdat de winkelier het direct op je bon zet.",
        "Omdat je het direct in contanten aan de minister moet geven.",
        "Omdat het direct invloed heeft op de prijs van brood."
      ],
      antwoord: 0,
      uitleg: "Je betaalt het rechtstreeks aan de Belastingdienst over je eigen verdiende geld, dus is het een **directe belasting**."
    },
    {
      type: "invul",
      vraag: "Welke korting krijg je op de belasting omdat je actief aan het werk bent?",
      antwoord: "arbeidskorting|arbeids korting",
      uitleg: "De **arbeidskorting** is een heffingskorting die werkenden krijgen om werken te stimuleren."
    },
    {
      type: "open",
      vraag: "Leg uit hoe een aftrekpost, zoals de hypotheekrenteaftrek, ervoor zorgt dat je minder inkomstenbelasting betaalt.",
      sleutelwoorden: ["belastbaar inkomen/inkomen verlagen", "aftrekken van het inkomen", "minder belasting berekenen", "belastingaangifte"],
      minTreffers: 2,
      modelantwoord: "Een aftrekpost mag je aftrekken van je bruto jaarinkomen. Hierdoor wordt het belastbaar inkomen lager. Omdat het inkomen waarover de Belastingdienst belasting berekent kleiner is geworden, betaal je uiteindelijk minder belasting.",
      uitleg: "Minder belastbaar inkomen leidt direct tot een lagere belastingaanslag."
    },
    {
      type: "mc",
      vraag: "Wat is een 'jaaropgave'?",
      opties: [
        "Een formulier waarop staat hoeveel uur je dit jaar hebt geslapen.",
        "Een overzicht van je werkgever met je totale brutoloon en de ingehouden loonbelasting van het afgelopen jaar.",
        "Een brief van de overheid waarin staat hoeveel btw je hebt betaald.",
        "Het contract voor je nieuwe bijbaan."
      ],
      antwoord: 1,
      uitleg: "De **jaaropgave** ontvang je aan het begin van het nieuwe jaar van je werkgever. Dit formulier heb je nodig om je belastingaangifte in te vullen."
    },
    {
      type: "waaronwaar",
      vraag: "De jaaropgave van je werkgever bevat alle informatie die je nodig hebt om je belastingaangifte in te vullen.",
      antwoord: true,
      uitleg: "Waar. Op de **jaaropgave** staan je totale brutoloon, ingehouden loonheffing en arbeidskorting van dat jaar vermeld."
    },
    {
      type: "open",
      vraag: "Duru, stel dat je in januari een jaaropgave krijgt van je bijbaantje bij de supermarkt. Wat is het nut van dit document voor jou?",
      sleutelwoorden: ["belastingaangifte invullen", "loon/belasting gegevens", "geld terugvragen", "belastingdienst"],
      minTreffers: 2,
      modelantwoord: "Het nut van de jaaropgave is dat er precies op staat hoeveel je hebt verdiend en hoeveel belasting er is ingehouden. Deze gegevens heb je nodig om je belastingaangifte in te vullen. Omdat scholieren vaak weinig verdienen, kun je hiermee de ingehouden loonbelasting terugvragen bij de Belastingdienst.",
      uitleg: "De jaaropgave is het bewijs van je verdiende loon en de al afgedragen loonbelasting."
    }
  ]
});
