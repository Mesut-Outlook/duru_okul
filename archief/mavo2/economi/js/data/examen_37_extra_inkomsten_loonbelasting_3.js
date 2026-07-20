/* Extra Proeftoets 32 — Inkomstenbelasting & Loonbelasting III */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting-3",
  titel: "Extra Proeftoets 32 — Inkomstenbelasting & Loonbelasting III",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is loonheffingskorting?",
      opties: [
        "Een boete die je krijgt als je je belastingaangifte te laat opstuurt.",
        "Een korting op de belasting die wordt ingehouden op je loon, waardoor je meer nettoloon overhoudt.",
        "De korting die winkeliers krijgen op de btw van hun producten.",
        "Een belastingkorting die je alleen krijgt als je werkloos bent."
      ],
      antwoord: 1,
      uitleg: "De **loonheffingskorting** is een wettelijke korting op de belasting. Hierdoor hoef je minder loonheffing te betalen en is je nettoloon hoger."
    },
    {
      type: "waaronwaar",
      vraag: "Als je twee bijbaantjes hebt, mag je bij beide werkgevers tegelijk loonheffingskorting aanvragen.",
      antwoord: false,
      uitleg: "Onwaar. Je mag de loonheffingskorting maar bij **één werkgever tegelijk** laten toepassen. Doe je dit bij beide, dan krijg je te veel korting en moet je achteraf veel belasting bijbetalen."
    },
    {
      type: "invul",
      vraag: "Welke korting zorgt ervoor dat werkenden minder belasting betalen en zo netto meer overhouden?",
      antwoord: "loonheffingskorting|loonheffings korting",
      uitleg: "De **loonheffingskorting** zorgt ervoor dat er minder belasting op je loon wordt ingehouden."
    },
    {
      type: "mc",
      vraag: "Stel, Duru heeft twee bijbaantjes. Bij Job A verdient ze € 500,- per maand en bij Job B € 150,- per maand. Bij welke job kan ze het best de loonheffingskorting aanzetten?",
      opties: [
        "Bij Job B, want daar verdient ze het minst.",
        "Bij Job A, want daar verdient ze het meest en heeft de korting het grootste effect.",
        "Bij allebei de jobs tegelijk.",
        "Bij geen van beide; scholieren hebben geen recht op loonheffingskorting."
      ],
      antwoord: 1,
      uitleg: "Je kunt de loonheffingskorting het best aanzetten bij de baan waar je het **meeste verdient (Job A)**. Daar is je belastingdruk het hoogst en profiteer je optimaal van de korting."
    },
    {
      type: "waaronwaar",
      vraag: "Het toepassen van loonheffingskorting zorgt ervoor dat je nettosalaris omhooggaat.",
      antwoord: true,
      uitleg: "Waar. Omdat er door de loonheffingskorting **minder** belasting van je brutoloon afgaat, houd je netto meer geld over."
    },
    {
      type: "mc",
      vraag: "Wat kan er gebeuren als je bij twee werkgevers tegelijk de loonheffingskorting aan hebt staan?",
      opties: [
        "Je krijgt aan het eind van het jaar extra geld terug van de Belastingdienst.",
        "De Belastingdienst verdubbelt automatisch je salaris.",
        "Je moet aan het eind van het jaar waarschijnlijk belasting bijbetalen omdat er te weinig is ingehouden.",
        "Niets, de Belastingdienst vindt dit prima."
      ],
      antwoord: 2,
      uitleg: "Als je bij twee werkgevers korting krijgt, wordt er bij beide te weinig belasting ingehouden. Bij de jaarlijkse inkomstenbelasting moet je dit tekort **bijbetalen**."
    },
    {
      type: "invul",
      vraag: "Wie past de loonheffingskorting daadwerkelijk toe op het moment dat je salaris wordt berekend?",
      antwoord: "werkgever|de werkgever|werkgevers|de werkgevers",
      uitleg: "De **werkgever** past de loonheffingskorting toe op je loonstrook als je daar een handtekening voor hebt gezet."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste kenmerk van een progressief belastingstelsel?",
      opties: [
        "Iedereen betaalt precies hetzelfde bedrag aan belasting in euro's.",
        "Wie een hoger inkomen heeft, betaalt een hoger percentage aan belasting.",
        "Bedrijven betalen meer belasting dan gewone burgers.",
        "Hoe meer je verdient, hoe lager het percentage belasting dat je betaalt."
      ],
      antwoord: 1,
      uitleg: "In een **progressief stelsel** stijgt het belastingpercentage naarmate je inkomen stijgt. De sterkste schouders dragen de zwaarste lasten."
    },
    {
      type: "waaronwaar",
      vraag: "In een progressief belastingstelsel betaalt iemand met een heel hoog inkomen procentueel minder belasting dan iemand met een laag inkomen.",
      antwoord: false,
      uitleg: "Onwaar. In een progressief stelsel betaal je procentueel juist **meer** belasting als je inkomen stijgt."
    },
    {
      type: "mc",
      vraag: "Stel, Sophie verdient € 1000,- bruto. Ze heeft geen recht op loonheffingskorting. Het belastingtarief is 20%. Hoeveel euro loonbelasting wordt er ingehouden?",
      opties: [
        "€ 100,-",
        "€ 200,-",
        "€ 800,-",
        "€ 50,-"
      ],
      antwoord: 1,
      uitleg: "20% van € 1000 = 0,20 * 1000 = **€ 200,-** belasting."
    },
    {
      type: "invul",
      vraag: "Als de overheid de inkomensverschillen tussen arm en rijk kleiner maakt door middel van belastingen, hoe noemen we dit proces?",
      antwoord: "nivellering|nivelleren",
      uitleg: "Het verkleinen van inkomensverschillen heet **nivellering**. Progressieve belastingen dragen hieraan bij."
    },
    {
      type: "open",
      vraag: "Duru, stel dat je twee verschillende bijbaantjes hebt. Leg uit waarom het onverstandig is om bij beide banen de loonheffingskorting aan te vragen.",
      sleutelwoorden: ["twee keer korting", "te weinig belasting/loonheffing ingehouden", "bijbetalen/terugbetalen", "eind van het jaar/belastingdienst"],
      minTreffers: 2,
      modelantwoord: "Als je bij beide banen loonheffingskorting aanvraagt, krijg je twee keer korting op de belasting. Hierdoor houden beide werkgevers te weinig loonbelasting in. Aan het eind van het jaar berekent de Belastingdienst je totale inkomen en moet je de te veel ontvangen korting alsnog terugbetalen (bijbetalen).",
      uitleg: "Je mag maar één keer recht hebben op de heffingskorting over je totale jaarinkomen."
    },
    {
      type: "mc",
      vraag: "Welke directe belasting betalen nv's en bv's over de winst die zij maken?",
      opties: [
        "Loonbelasting",
        "Btw",
        "Vennootschapsbelasting",
        "Accijns"
      ],
      antwoord: 2,
      uitleg: "Bedrijven (zoals een bv of nv) betalen **vennootschapsbelasting** over hun winst."
    },
    {
      type: "waaronwaar",
      vraag: "De btw (belasting toegevoegde waarde) is een voorbeeld van een directe belasting.",
      antwoord: false,
      uitleg: "Onwaar. Btw is een **indirecte belasting** omdat de consument deze via de winkelier aan de Belastingdienst betaalt."
    },
    {
      type: "open",
      vraag: "Wat is het doel van de loonheffingskorting en wat is het gevolg hiervan voor je nettosalaris?",
      sleutelwoorden: ["korting op belasting/loonheffing", "minder belasting betalen", "nettoloon stijgt/hoger nettosalaris", "meer geld overhouden"],
      minTreffers: 2,
      modelantwoord: "Het doel van de loonheffingskorting is om burgers een korting te geven op de in te houden belasting. Het gevolg is dat er minder loonheffing wordt ingehouden op je brutoloon, waardoor je nettosalaris stijgt en je dus meer geld overhoudt.",
      uitleg: "Korting op belasting betekent direct een stijging van het nettoloon."
    }
  ]
});
