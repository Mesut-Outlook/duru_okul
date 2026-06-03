/* Proeftoets 5 — H6 Gemengde Eindtoets */
DURU.registerExamen({
  id: "ex-eindtoets",
  titel: "Gemengde Eindtoets — Hoofdstuk 6",
  vak: "Economie · H6 Complete Toets",
  icoon: "🎓",
  duurMin: 20,
  vragen: [
    /* ── PARAGRAAF 6.1: WIE IS DE OVERHEID? ── */
    {
      type: "mc",
      vraag: "Wie is de voorzitter van de provincie en leidt de vergaderingen van de Provinciale Staten?",
      opties: [
        "De Commissaris van de Koning",
        "De burgemeester",
        "De minister-president",
        "De gedeputeerde"
      ],
      antwoord: 0,
      uitleg: "De <b>Commissaris van de Koning</b> (CvdK) is de voorzitter van zowel Provinciale Staten als Gedeputeerde Staten in een provincie."
    },
    {
      type: "mc",
      vraag: "Hoe vaak worden de leden van de Tweede Kamer en de Provinciale Staten in principe gekozen door de Nederlandse burgers?",
      opties: ["Elke 4 jaar", "Elke 5 jaar", "Elke 6 jaar", "Elke 2 jaar"],
      antwoord: 0,
      uitleg: "In Nederland worden deze volksvertegenwoordigingen normaal gesproken <b>elke vier jaar</b> gekozen."
    },
    {
      type: "waaronwaar",
      vraag: "De Eerste Kamer mag zelf wetsvoorstellen indienen en wijzigen.",
      antwoord: false,
      uitleg: "Onwaar. De Eerste Kamer mag wetsvoorstellen alleen goedkeuren of afkeuren (het recht van amendement en initiatief ligt bij de Tweede Kamer)."
    },
    {
      type: "invul",
      vraag: "Het dagelijks bestuur van een gemeente heet het college van ______ en wethouders. (Vul één woord in)",
      antwoord: "burgemeester",
      uitleg: "Dit heet het college van <b>burgemeester</b> en wethouders (B&W)."
    },

    /* ── PARAGRAAF 6.2: WAAR ZORGT DE OVERHEID VOOR? ── */
    {
      type: "mc",
      vraag: "Welke van de volgende voorzieningen is een individueel goed en GEEN collectieve voorziening?",
      opties: [
        "Een abonnement op Netflix",
        "De straatverlichting in jouw wijk",
        "De dijken langs de grote rivieren",
        "Het onderwijs op een openbare school"
      ],
      antwoord: 0,
      uitleg: "Een <b>Netflix-abonnement</b> is een individueel goed: je kiest zelf of je betaalt en wie niet betaalt heeft geen toegang. Straatverlichting en dijken zijn voor iedereen tegelijk en kunnen niet per persoon worden uitgeschakeld."
    },
    {
      type: "waaronwaar",
      vraag: "De brandweer is een collectieve voorziening omdat het onveilig en te duur zou zijn als iedereen zelf zijn eigen brandweer moest inhuren.",
      antwoord: true,
      uitleg: "Waar. Veiligheid is een klassiek voorbeeld van een collectieve voorziening die we samen betalen via de overheid."
    },
    {
      type: "open",
      vraag: "Noem de vier belangrijkste terreinen waarvoor de overheid collectieve voorzieningen regelt.",
      sleutelwoorden: ["veiligheid", "infrastructuur", "onderwijs", "zorg"],
      minTreffers: 3,
      modelantwoord: "De vier terreinen zijn: (1) Veiligheid (zoals politie en brandweer), (2) Infrastructuur (zoals wegen, bruggen en dijken), (3) Onderwijs (zoals openbare scholen), (4) Zorg en sociale zekerheid (zoals ziekenhuizen en uitkeringen).",
      uitleg: "Onthoud de vier pijlers: <b>veiligheid</b>, <b>infrastructuur</b>, <b>onderwijs</b> en <b>zorg</b>."
    },
    {
      type: "invul",
      vraag: "Voorzieningen die door de markt (bedrijven) worden aangeboden voor winst noemen we ______ goederen.",
      antwoord: "individuele|individueel",
      uitleg: "Dit zijn <b>individuele goederen</b>. Je kunt mensen uitsluiten van het gebruik als ze niet betalen."
    },

    /* ── PARAGRAAF 6.3: BETALEN AAN DE OVERHEID ── */
    {
      type: "mc",
      vraag: "Welke van de volgende belastingen is een directe belasting?",
      opties: [
        "Loonheffing (loonbelasting)",
        "Btw op een nieuwe fiets",
        "Accijns op benzine",
        "Toeristenbelasting in Amsterdam"
      ],
      antwoord: 0,
      uitleg: "<b>Loonheffing</b> is een directe belasting omdat deze direct over jouw verdiende inkomen wordt geheven en ingehouden."
    },
    {
      type: "mc",
      vraag: "Op welk product zit naast btw ook nog accijns?",
      opties: ["Een liter benzine", "Een pak melk", "Een spijkerbroek", "Een bioscoopkaartje"],
      antwoord: 0,
      uitleg: "Op <b>benzine</b> (en ook alcohol en tabak) heft de overheid accijns om het gebruik ervan te ontmoedigen."
    },
    {
      type: "waaronwaar",
      vraag: "Als je in de winkel een fles cola koopt, betaal je 21% btw omdat het geen eerste levensbehoefte is.",
      antwoord: false,
      uitleg: "Onwaar. Eten en drinken (dus ook frisdrank) valt in Nederland onder het lage btw-tarief van <b>9%</b>."
    },
    {
      type: "invul",
      vraag: "De overheidsdienst die belastingen berekent en int heet de ______.",
      antwoord: "belastingdienst|Belastingdienst|fiscus",
      uitleg: "De <b>Belastingdienst</b> (ook wel fiscus genoemd) regelt het innen van de belastingen."
    },
    {
      type: "open",
      vraag: "Wat is loonheffing en wie houdt dit in?",
      sleutelwoorden: ["belasting", "premie/sociale premies", "werkgever", "loon/salaris"],
      minTreffers: 2,
      modelantwoord: "Loonheffing is een combinatie van loonbelasting en premies voor de volksverzekeringen. De werkgever houdt dit automatisch in op het brutoloon van de werknemer en draagt het af aan de Belastingdienst.",
      uitleg: "De <b>werkgever</b> houdt de <b>loonheffing</b> (loonbelasting + premies) in op je brutoloon, zodat je netto minder op je rekening krijgt."
    },

    /* ── PARAGRAAF 6.4: IS DE SCHATKIST GOED GEVULD? ── */
    {
      type: "mc",
      vraag: "Wat is de rijksbegroting?",
      opties: [
        "Een overzicht van de verwachte inkomsten en uitgaven van de rijksoverheid voor het komende jaar.",
        "De boekhouding van alle Nederlandse gemeenten samen.",
        "De totale schuld die Nederland heeft openstaan.",
        "Het geld dat de Koning jaarlijks krijgt voor zijn taken."
      ],
      antwoord: 0,
      uitleg: "De <b>rijksbegroting</b> is het jaarlijkse overzicht van de verwachte inkomsten (zoals belastingen) en uitgaven (zoals zorg en onderwijs) van de rijksoverheid."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de staatsschuld als de overheid meerdere jaren achter elkaar een begrotingstekort heeft?",
      opties: [
        "De staatsschuld stijgt.",
        "De staatsschuld daalt.",
        "De staatsschuld blijft gelijk.",
        "De staatsschuld verdwijnt."
      ],
      antwoord: 0,
      uitleg: "Bij een begrotingstekort moet de overheid geld lenen. Dit geleende geld telt op bij de <b>staatsschuld</b>, die daardoor stijgt."
    },
    {
      type: "waaronwaar",
      vraag: "Zorg en sociale zekerheid zijn de grootste uitgavenposten op de Nederlandse rijksbegroting.",
      antwoord: true,
      uitleg: "Waar. De overheid geeft verreweg het meeste geld uit aan zorg (ziekenhuizen, artsen) en sociale zekerheid (uitkeringen, AOW)."
    },
    {
      type: "invul",
      vraag: "De begroting van de overheid wordt gepresenteerd op de derde dinsdag van september. Deze feestelijke dag noemen we ______.",
      antwoord: "prinsjesdag|Prinsjesdag",
      uitleg: "Deze dag heet <b>Prinsjesdag</b>."
    },
    {
      type: "open",
      vraag: "Leg uit wat een begrotingstekort is en hoe de overheid dit tekort dekt.",
      sleutelwoorden: ["uitgaven groter/meer uitgeeft/meer uitgaven", "inkomsten/belasting", "lenen/lening/obligaties"],
      minTreffers: 2,
      modelantwoord: "Een begrotingstekort ontstaat wanneer de geplande uitgaven van de overheid groter zijn dan de verwachte inkomsten. De overheid dekt dit tekort door geld te lenen op de kapitaalmarkt.",
      uitleg: "Als <b>uitgaven > inkomsten</b> leent de overheid geld om het tekort op te vangen."
    },

    /* ── REKENVRAGEN EN DIVERSEN ── */
    {
      type: "mc",
      vraag: "Duru koopt een nieuwe laptop. De prijs exclusief btw is € 600. De btw is 21%. Wat betaalt Duru inclusief btw?",
      opties: ["€ 726,00", "€ 621,00", "€ 612,00", "€ 700,00"],
      antwoord: 0,
      uitleg: "Btw-bedrag: 21% van € 600 = 0,21 × 600 = € 126. <br>Totaalprijs: € 600 + € 126 = <b>€ 726,00</b>."
    },
    {
      type: "invul",
      vraag: "Een gezonde lunch in de schoolkantine kost € 6,00 exclusief btw. De btw op voeding is 9%. Hoeveel btw (in euro's) zit er op deze lunch? (Vul het getal in met een komma, bijv. 0,54)",
      antwoord: "0,54|0.54",
      uitleg: "Berekening: 9% van € 6,00 = 0,09 × 6 = <b>€ 0,54</b> (54 cent)."
    },
    {
      type: "mc",
      vraag: "Hoe noemen we de belasting die de gemeenten heffen voor het ophalen van huisvuil?",
      opties: [
        "Afvalstoffenheffing",
        "Rioolheffing",
        "Onroerendezaakbelasting",
        "Milieubelasting"
      ],
      antwoord: 0,
      uitleg: "De gemeente heft <b>afvalstoffenheffing</b> om de kosten voor het inzamelen en verwerken van afval te betalen."
    },
    {
      type: "waaronwaar",
      vraag: "De waterschappen zijn een aparte overheidsorganisatie die zorgt voor het waterbeheer en de dijken in een regio.",
      antwoord: true,
      uitleg: "Waar. De waterschappen zijn de oudste overheidsinstantie van Nederland en zorgen voor droge voeten en schoon water."
    },
    {
      type: "mc",
      vraag: "De inkomsten van de overheid zijn € 330 miljard en de uitgaven zijn € 325 miljard. Welke situatie is hier juist?",
      opties: [
        "Er is een begrotingsoverschot van € 5 miljard.",
        "Er is een begrotingstekort van € 5 miljard.",
        "De staatsschuld stijgt met € 5 miljard.",
        "De inkomsten en uitgaven zijn in evenwicht."
      ],
      antwoord: 0,
      uitleg: "Omdat de inkomsten (€ 330 miljard) groter zijn dan de uitgaven (€ 325 miljard), houdt de overheid geld over. Er is dus een <b>begrotingsoverschot van € 5 miljard</b>."
    },
    {
      type: "invul",
      vraag: "De totale schuld van de overheid die is opgebouwd door alle tekorten uit het verleden noemen we de ______.",
      antwoord: "staatsschuld|Staatsschuld",
      uitleg: "Dit noemen we de <b>staatsschuld</b>."
    }
  ]
});
