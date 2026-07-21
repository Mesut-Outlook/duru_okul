/* Extra Proeftoets 22 — Inkomstenbelasting & Loonbelasting */
DURU.registerExamen({
  id: "ex-extra-inkomsten-loonbelasting",
  titel: "Extra Proeftoets 22 — Inkomstenbelasting & Loonbelasting",
  vak: "Economie · Belastingen",
  icoon: "💶",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is loonbelasting?",
      opties: [
        "Een belasting die alleen gepensioneerden betalen.",
        "De inkomstenbelasting die meteen wordt ingehouden op je loon, als een voorheffing.",
        "Een belasting die je werkgever betaalt over zijn winst.",
        "Een belasting op producten die je in de winkel koopt."
      ],
      antwoord: 1,
      uitleg: "**Loonbelasting** is de inkomstenbelasting die meteen wordt ingehouden op je loon: een soort voorheffing die de werkgever inhoudt en afdraagt."
    },
    {
      type: "mc",
      vraag: "Wie houdt de loonbelasting in op het brutoloon van een werknemer?",
      opties: [
        "De werknemer zelf, aan het eind van het jaar.",
        "De gemeente.",
        "De werkgever, die het bedrag afdraagt aan de Belastingdienst.",
        "De bank waar de werknemer een rekening heeft."
      ],
      antwoord: 2,
      uitleg: "De **werkgever** houdt de loonbelasting in op het brutoloon van de werknemer en draagt dit bedrag af aan de Belastingdienst."
    },
    {
      type: "mc",
      vraag: "Wanneer moet je aan het eind van het jaar bijbetalen bij de inkomstenbelasting?",
      opties: [
        "Als er gedurende het jaar te véél loonbelasting is ingehouden.",
        "Als er gedurende het jaar te wéinig loonbelasting is ingehouden.",
        "Als je werkgever failliet gaat.",
        "Altijd, ieder jaar opnieuw, ongeacht wat er is ingehouden."
      ],
      antwoord: 1,
      uitleg: "Als er gedurende het jaar **te wéinig** loonbelasting is ingehouden ten opzichte van de uiteindelijke inkomstenbelasting, moet je **bijbetalen**."
    },
    {
      type: "waaronwaar",
      vraag: "Inkomstenbelasting bereken je per jaar, terwijl loonbelasting maandelijks (per loonperiode) wordt ingehouden.",
      antwoord: true,
      uitleg: "Waar. **Inkomstenbelasting** wordt over een heel jaar berekend, terwijl **loonbelasting** als voorheffing al per loonperiode wordt ingehouden."
    },
    {
      type: "mc",
      vraag: "Wat is vennootschapsbelasting?",
      opties: [
        "Belasting die werknemers betalen over hun salaris.",
        "Belasting over de winst van een bedrijf.",
        "Belasting die je betaalt bij de aankoop van een woning.",
        "Een andere naam voor btw."
      ],
      antwoord: 1,
      uitleg: "**Vennootschapsbelasting** is de belasting die bedrijven betalen over hun **winst**."
    },
    {
      type: "waaronwaar",
      vraag: "Als er gedurende het jaar te véél loonbelasting is ingehouden, krijg je geld terug van de Belastingdienst.",
      antwoord: true,
      uitleg: "Waar. Is er te véél loonbelasting ingehouden, dan krijg je het verschil terug van de **Belastingdienst**."
    },
    {
      type: "mc",
      vraag: "Senna heeft een brutoloon waarop € 480,- loonbelasting is ingehouden. Aan het eind van het jaar blijkt dat ze in totaal € 520,- inkomstenbelasting moet betalen. Wat moet Senna doen?",
      opties: [
        "€ 40,- terugkrijgen.",
        "€ 40,- bijbetalen.",
        "€ 480,- bijbetalen.",
        "Niets, het klopt precies."
      ],
      antwoord: 1,
      uitleg: "Er is € 480,- ingehouden, maar er moest € 520,- betaald worden. Senna moet **520 - 480 = € 40,- bijbetalen**."
    },
    {
      type: "waaronwaar",
      vraag: "Loonbelasting is een indirecte belasting, omdat de werkgever het bedrag afdraagt en niet de werknemer zelf.",
      antwoord: false,
      uitleg: "Onwaar. Loonbelasting is een **directe belasting**: het wordt rechtstreeks geheven over het inkomen van de werknemer. Dat de werkgever het inhoudt, verandert het type belasting niet."
    },
    {
      type: "invul",
      vraag: "Hoe noemen we het inkomen vóórdat er loonbelasting van af is gehaald?",
      antwoord: "brutoloon|bruto loon|bruto-inkomen|brutoinkomen",
      uitleg: "Het inkomen vóór inhoudingen heet het **brutoloon**. Na aftrek van loonbelasting houd je het nettoloon over."
    },
    {
      type: "mc",
      vraag: "Bram heeft een brutoloon waarop € 600,- loonbelasting is ingehouden. Aan het eind van het jaar berekent de Belastingdienst dat hij in totaal € 550,- inkomstenbelasting moet betalen. Wat gebeurt er?",
      opties: [
        "Bram moet € 50,- bijbetalen.",
        "Bram krijgt € 50,- terug.",
        "Bram krijgt € 600,- terug.",
        "Er verandert niets."
      ],
      antwoord: 1,
      uitleg: "Er is € 600,- ingehouden, maar slechts € 550,- was nodig. Bram krijgt het verschil **600 - 550 = € 50,- terug**."
    },
    {
      type: "invul",
      vraag: "Welke belasting wordt gezien als een 'voorheffing' op de inkomstenbelasting, omdat het al maandelijks wordt ingehouden?",
      antwoord: "loonbelasting",
      uitleg: "De **loonbelasting** is een voorheffing: een vooruitbetaling op de inkomstenbelasting die je uiteindelijk over het jaar verschuldigd bent."
    },
    {
      type: "invul",
      vraag: "Bedrijf De Bakker BV maakt winst en moet daarover belasting betalen aan de Belastingdienst. Hoe heet deze belasting?",
      antwoord: "vennootschapsbelasting",
      uitleg: "Bedrijven betalen over hun winst **vennootschapsbelasting**, een directe belasting."
    },
    {
      type: "waaronwaar",
      vraag: "Vennootschapsbelasting wordt betaald door werknemers over hun brutoloon.",
      antwoord: false,
      uitleg: "Onwaar. **Vennootschapsbelasting** wordt betaald door bedrijven over hun winst, niet door werknemers over hun loon (dat is loonbelasting)."
    },
    {
      type: "open",
      vraag: "Leg uit wat het verschil is tussen inkomstenbelasting en loonbelasting.",
      sleutelwoorden: ["per jaar/jaarlijks berekenen", "voorheffing/al ingehouden/maandelijks", "werkgever houdt in/brutoloon", "bijbetalen/terugkrijgen aan eind van jaar"],
      minTreffers: 2,
      modelantwoord: "Inkomstenbelasting is de belasting die je in totaal over een heel jaar over je inkomen moet betalen. Loonbelasting is een voorheffing hierop: de werkgever houdt deze al maandelijks in op het brutoloon en draagt dit af aan de Belastingdienst. Aan het eind van het jaar wordt vergeleken of er te veel of te weinig loonbelasting is ingehouden.",
      uitleg: "Loonbelasting is een vooruitbetaling per loonperiode, inkomstenbelasting is de jaarlijkse eindafrekening."
    },
    {
      type: "open",
      vraag: "Leg uit waarom je aan het eind van het jaar soms moet bijbetalen en soms geld terugkrijgt van de Belastingdienst.",
      sleutelwoorden: ["te veel ingehouden/terugkrijgen", "te weinig ingehouden/bijbetalen", "loonbelasting vergelijken met inkomstenbelasting", "verschil tussen ingehouden bedrag en werkelijke belasting"],
      minTreffers: 2,
      modelantwoord: "Gedurende het jaar houdt de werkgever loonbelasting in als voorheffing. Aan het eind van het jaar berekent de Belastingdienst hoeveel inkomstenbelasting je werkelijk moet betalen. Is er te véél ingehouden, dan krijg je het verschil terug. Is er te wéinig ingehouden, dan moet je het verschil bijbetalen.",
      uitleg: "Het verschil tussen de voorheffing (loonbelasting) en de definitieve inkomstenbelasting bepaalt of je geld terugkrijgt of moet bijbetalen."
    }
  ]
});
