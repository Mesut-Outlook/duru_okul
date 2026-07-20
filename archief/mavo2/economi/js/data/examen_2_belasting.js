DURU.registerExamen({
  id: "ex-belasting",
  titel: "Proeftoets — Belasting & begroting",
  vak: "Economie · H6 (6.3 & 6.4)",
  icoon: "💶",
  duurMin: 20,
  vragen: [

    /* ── MC ── */

    { type: "mc",
      vraag: "Welke belasting betaal je DIRECT aan de Belastingdienst?",
      opties: ["Loonbelasting", "Btw", "Accijns op benzine", "Toeristenbelasting"],
      antwoord: 0,
      uitleg: "<b>Loonbelasting</b> is een directe belasting: de werkgever houdt hem in op je salaris en draagt hem direct af aan de Belastingdienst. Btw en accijns zijn <i>indirecte</i> belastingen — je betaalt ze via de prijs van een product." },

    { type: "mc",
      vraag: "Het hoge btw-tarief in Nederland is:",
      opties: ["21%", "9%", "15%", "6%"],
      antwoord: 0,
      uitleg: "Het <b>hoge btw-tarief</b> is <b>21%</b>. Dit geldt voor de meeste producten zoals kleding, elektronica en auto's. Het lage tarief (9%) geldt o.a. voor voedsel en medicijnen." },

    { type: "mc",
      vraag: "Op welk tarief wordt btw berekend bij de aankoop van brood of groente?",
      opties: ["9%", "21%", "0%", "12%"],
      antwoord: 0,
      uitleg: "Voedingsmiddelen (brood, groente, fruit) vallen onder het <b>lage btw-tarief van 9%</b>. De overheid houdt eerste levensbehoeften bewust goedkoper." },

    { type: "mc",
      vraag: "Wat is accijns?",
      opties: [
        "Een belasting op bepaalde producten zoals benzine, tabak en alcohol",
        "Een belasting op je inkomen",
        "Een belasting die bedrijven betalen over hun winst",
        "Hetzelfde als btw"
      ],
      antwoord: 0,
      uitleg: "<b>Accijns</b> is een indirecte belasting op specifieke producten (benzine, tabak, alcohol). De overheid heft accijns deels om gebruik te ontmoedigen en deels voor inkomsten." },

    { type: "mc",
      vraag: "Hoe noemen we een belastingstelsel waarbij iemand met een hoger inkomen een hoger percentage belasting betaalt?",
      opties: ["Progressief", "Proportioneel", "Regressief", "Vlaktaks"],
      antwoord: 0,
      uitleg: "Bij een <b>progressief</b> belastingstelsel stijgt het belastingpercentage naarmate je meer verdient. Nederland heeft zo'n stelsel: hogere inkomens betalen in een hogere 'schijf'." },

    { type: "mc",
      vraag: "Wanneer presenteert de minister van Financiën de Miljoenennota aan de Tweede Kamer?",
      opties: ["Op Prinsjesdag (derde dinsdag van september)", "Op 1 januari", "Op Koningsdag (27 april)", "Op de eerste maandag van oktober"],
      antwoord: 0,
      uitleg: "<b>Prinsjesdag</b> valt op de <b>derde dinsdag van september</b>. De minister van Financiën biedt dan de Miljoenennota aan: de plannen en begroting voor het komende jaar." },

    { type: "mc",
      vraag: "Welke term gebruik je als de overheidsuitgaven GROTER zijn dan de overheidsinkomsten?",
      opties: ["Begrotingstekort", "Begrotingsoverschot", "Staatsschuld", "Belastingdruk"],
      antwoord: 0,
      uitleg: "Als <b>uitgaven > inkomsten</b> is er een <b>begrotingstekort</b>. De overheid moet dan geld lenen om het verschil te dekken. Zijn inkomsten juist groter, dan is er een overschot." },

    { type: "mc",
      vraag: "Duru koopt een nieuwe telefoon. De winkelprijs zonder btw is € 400. Ze betaalt het hoge btw-tarief van 21%. Wat betaalt ze in totaal?",
      opties: ["€ 484", "€ 421", "€ 436", "€ 480"],
      antwoord: 0,
      uitleg: "Btw = 21% van € 400 = 0,21 × 400 = <b>€ 84</b>. Totaal = € 400 + € 84 = <b>€ 484</b>." },

    { type: "mc",
      vraag: "Wat is de staatsschuld?",
      opties: [
        "Het totale bedrag dat de overheid in de loop der jaren heeft geleend en nog niet heeft terugbetaald",
        "Het bedrag dat de overheid dit jaar tekortkomt",
        "De rente die de overheid jaarlijks betaalt",
        "Het totaal aan belastingopbrengsten"
      ],
      antwoord: 0,
      uitleg: "De <b>staatsschuld</b> is de opgetelde schuld van alle voorgaande jaren. Bij elk nieuw begrotingstekort leent de overheid extra en groeit de schuld. Over die schuld betaalt de overheid ook rente." },

    { type: "mc",
      vraag: "Welk document geeft een overzicht van alle inkomsten en uitgaven van de rijksoverheid voor het komende jaar?",
      opties: ["De Miljoenennota", "Het Belastingplan", "De Staatsbegroting", "Het Regeerakkoord"],
      antwoord: 0,
      uitleg: "De <b>Miljoenennota</b> (ook wel rijksbegroting) bevat alle geraamde inkomsten en uitgaven van de rijksoverheid voor het volgende jaar. Hij wordt op Prinsjesdag gepresenteerd." },

    /* ── WAAR/ONWAAR ── */

    { type: "waaronwaar",
      vraag: "Inkomstenbelasting is een indirecte belasting.",
      antwoord: false,
      uitleg: "Onwaar. Inkomstenbelasting is een <b>directe</b> belasting: je betaalt hem rechtstreeks aan de Belastingdienst, niet via de prijs van een product." },

    { type: "waaronwaar",
      vraag: "Btw staat voor Belasting over de Toegevoegde Waarde.",
      antwoord: true,
      uitleg: "Waar. <b>Btw</b> = Belasting over de Toegevoegde Waarde. Bij elke stap in het productieproces wordt waarde toegevoegd, en daar berekent de overheid belasting over." },

    { type: "waaronwaar",
      vraag: "Als de overheid een begrotingstekort heeft, moet ze geld lenen. Hierdoor stijgt de staatsschuld.",
      antwoord: true,
      uitleg: "Waar. Bij een <b>begrotingstekort</b> geeft de overheid meer uit dan ze ontvangt. Het verschil wordt gefinancierd door te lenen, waardoor de <b>staatsschuld groeit</b>." },

    { type: "waaronwaar",
      vraag: "Accijns op sigaretten is een voorbeeld van een directe belasting.",
      antwoord: false,
      uitleg: "Onwaar. Accijns is een <b>indirecte</b> belasting — je betaalt hem via de aankoopprijs van het product, niet rechtstreeks aan de Belastingdienst." },

    { type: "waaronwaar",
      vraag: "De rijksoverheid gebruikt belastinginkomsten onder andere voor onderwijs, zorg en veiligheid.",
      antwoord: true,
      uitleg: "Waar. De grote uitgavenposten van de rijksbegroting zijn <b>zorg, sociale uitkeringen, onderwijs en veiligheid</b> — allemaal betaald uit belastingen en premies." },

    { type: "waaronwaar",
      vraag: "Bij een progressief belastingstelsel betaalt iedereen hetzelfde percentage belasting, ongeacht het inkomen.",
      antwoord: false,
      uitleg: "Onwaar. Bij een <b>progressief</b> stelsel betalen <b>hogere inkomens een hoger percentage</b>. Het tegenovergestelde (zelfde % voor iedereen) heet een vlaktaks of proportioneel stelsel." },

    { type: "waaronwaar",
      vraag: "Over de staatsschuld betaalt de overheid elk jaar rente.",
      antwoord: true,
      uitleg: "Waar. Net als jij rente betaalt als je geld leent bij de bank, betaalt de overheid <b>rente</b> over de staatsschuld. Hoe hoger de schuld, hoe meer rente er elk jaar af moet." },

    /* ── OPEN ── */

    { type: "open",
      vraag: "Leg uit wat het verschil is tussen een directe en een indirecte belasting. Geef van elk één voorbeeld.",
      sleutelwoorden: ["direct/rechtstreeks/zelf", "indirect/via prijs/aankoop", "loonbelasting/inkomstenbelasting", "btw/accijns"],
      minTreffers: 2,
      modelantwoord: "Directe belasting betaal je rechtstreeks aan de Belastingdienst, bijv. loonbelasting. Indirecte belasting betaal je via de prijs van een product, bijv. btw of accijns.",
      uitleg: "<b>Direct:</b> jij betaalt zelf aan de Belastingdienst (loonbelasting, inkomstenbelasting).<br><b>Indirect:</b> zit verborgen in de prijs van wat je koopt (btw, accijns)." },

    { type: "open",
      vraag: "Wat is Prinsjesdag en wat gebeurt er op die dag?",
      sleutelwoorden: ["derde dinsdag/september", "miljoenennota/begroting", "minister/financiën/tweede kamer", "inkomsten/uitgaven"],
      minTreffers: 2,
      modelantwoord: "Prinsjesdag is de derde dinsdag van september. Op die dag biedt de minister van Financiën de Miljoenennota (rijksbegroting) aan de Tweede Kamer aan. Daarin staan alle geplande inkomsten en uitgaven van de overheid voor het komende jaar.",
      uitleg: "<b>Prinsjesdag</b> = derde dinsdag september. De <b>Miljoenennota</b> toont wat de overheid wil ontvangen (belastingen) en uitgeven (zorg, onderwijs, veiligheid) in het komende jaar." },

    { type: "open",
      vraag: "Waarom int de overheid belasting? Noem twee redenen.",
      sleutelwoorden: ["collectieve voorzieningen/openbare voorzieningen/politie/wegen/school/zorg", "herverdeling/inkomen gelijker/minder ongelijkheid", "ontmoedigen/gedrag/accijns/roken"],
      minTreffers: 2,
      modelantwoord: "1) Om collectieve voorzieningen te betalen die voor iedereen zijn (wegen, politie, scholen, zorg). 2) Om inkomen te herverdelen: hogere inkomens betalen meer zodat de overheid ook mensen met een laag inkomen kan ondersteunen. Extra: om ongezond gedrag te ontmoedigen (accijns op tabak/alcohol).",
      uitleg: "Belasting is nodig voor: <b>collectieve voorzieningen</b> (waar iedereen gebruik van maakt) en <b>herverdeling van inkomen</b>. Accijns dient ook om gedrag te ontmoedigen." },

    /* ── INVUL ── */

    { type: "invul",
      vraag: "Een schooltas kost € 50 zonder btw. Het hoge btw-tarief is 21%. Bereken het btw-bedrag. (Geef alleen het getal in euro's)",
      antwoord: "10,5|10.5|10,50|10.50",
      uitleg: "21% van € 50 = 0,21 × 50 = <b>€ 10,50</b>." },

    { type: "invul",
      vraag: "Een pak melk kost € 1,00 zonder btw. Het lage btw-tarief is 9%. Hoeveel btw betaal je? (in centen, dus geef het antwoord in euro's)",
      antwoord: "0,09|0.09|0,09|9 cent",
      uitleg: "9% van € 1,00 = 0,09 × 1 = <b>€ 0,09</b> (9 cent)." },

    { type: "invul",
      vraag: "Een jas kost € 300 zonder btw. Het hoge btw-tarief is 21%. Hoeveel btw betaal je? (Geef alleen het getal in euro's)",
      antwoord: "63|63,00|63.00",
      uitleg: "21% van € 300 = 0,21 × 300 = <b>€ 63</b>." },

    { type: "invul",
      vraag: "De rijksoverheid heeft dit jaar inkomsten van € 290 miljard en uitgaven van € 310 miljard. Hoe groot is het begrotingstekort? (Geef het antwoord in miljard euro's)",
      antwoord: "20|20 miljard|20,00|20.00",
      uitleg: "Begrotingstekort = uitgaven − inkomsten = € 310 − € 290 = <b>€ 20 miljard</b>." },

    { type: "invul",
      vraag: "Vul in: Btw staat voor Belasting over de ______ Waarde.",
      antwoord: "toegevoegde|Toegevoegde",
      uitleg: "De volledige naam is <b>Belasting over de Toegevoegde Waarde</b>. Bij elke stap in het productieproces wordt waarde 'toegevoegd', en daar heft de overheid belasting over." },

    { type: "invul",
      vraag: "Vul in: De overheid biedt de rijksbegroting elk jaar aan op ______, de derde dinsdag van september.",
      antwoord: "prinsjesdag|Prinsjesdag",
      uitleg: "<b>Prinsjesdag</b> is de derde dinsdag van september. Op die dag wordt de Miljoenennota gepresenteerd aan de Tweede Kamer." },

    { type: "invul",
      vraag: "Als de overheid jaar na jaar een begrotingstekort heeft, moet ze steeds meer lenen. Het totale openstaande bedrag noemen we de ______.",
      antwoord: "staatsschuld|Staatsschuld|nationale schuld",
      uitleg: "De opgetelde schuld van alle jaren heet de <b>staatsschuld</b>. Hoe groter de tekorten, hoe hoger de staatsschuld — en hoe meer rente de overheid elk jaar kwijt is." }

  ]
});
