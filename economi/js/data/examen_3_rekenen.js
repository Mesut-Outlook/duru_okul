/* Proeftoets 3 — Rekenen aan Btw & Begroting */
DURU.registerExamen({
  id: "ex-rekenen",
  titel: "Proeftoets — Rekenen aan Btw & Begroting",
  vak: "Economie · Rekenen met Btw & Begroting",
  icoon: "📊",
  duurMin: 20,
  vragen: [
    /* ── BTW REKENEN (EXCLUSIEF NAAR INCLUSIEF / BTW BEDRAG) ── */
    {
      type: "mc",
      vraag: "Duru koopt een nieuwe koptelefoon. De prijs exclusief btw is € 120. Hierover moet 21% btw betaald worden. Wat is het btw-bedrag?",
      opties: ["€ 25,20", "€ 21,00", "€ 12,00", "€ 145,20"],
      antwoord: 0,
      uitleg: "De btw is 21% van € 120. <br>Berekening: 0,21 × 120 = <b>€ 25,20</b>. De totale prijs inclusief btw wordt dan € 120 + € 25,20 = € 145,20."
    },
    {
      type: "invul",
      vraag: "Een set nieuwe boeken voor school kost € 80 exclusief btw. Het btw-tarief op boeken is 9%. Hoeveel euro btw betaal je over deze boeken? (Vul alleen het getal in)",
      antwoord: "7,2|7.2|7,20|7.20",
      uitleg: "Boeken vallen onder het lage btw-tarief van 9%. <br>Berekening: 9% van € 80 = 0,09 × 80 = <b>€ 7,20</b>."
    },
    {
      type: "mc",
      vraag: "Een nieuwe fiets kost € 500 exclusief btw. Welk btw-tarief (21%) moet hierover berekend worden en hoeveel is de totale consumentenprijs (inclusief btw)?",
      opties: ["€ 509", "€ 545", "€ 605", "€ 521"],
      antwoord: 2,
      uitleg: "Een fiets valt onder het hoge btw-tarief van 21%. <br>Btw-bedrag: 21% van € 500 = 0,21 × 500 = € 105. <br>Consumentenprijs = € 500 + € 105 = <b>€ 605</b>."
    },
    {
      type: "invul",
      vraag: "Duru bestelt pizza's voor haar verjaardag. De prijs van de pizza's is € 40 exclusief btw. Het btw-tarief voor eten en drinken is 9%. Wat is de totale prijs inclusief btw? (Vul alleen het getal in)",
      antwoord: "43,6|43.6|43,60|43.60",
      uitleg: "Eten en drinken valt onder het lage btw-tarief van 9%. <br>Btw: 9% van € 40 = 0,09 × 40 = € 3,60. <br>Totaalprijs: € 40 + € 3,60 = <b>€ 43,60</b>."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een product koopt van € 100 exclusief btw, en de btw is 21%, dan is de prijs inclusief btw altijd € 121.",
      antwoord: true,
      uitleg: "Waar. De prijs inclusief btw is 121% van de prijs exclusief btw. Dus € 100 × 1,21 = € 121."
    },

    /* ── BTW TERUGREKENEN (INCLUSIEF NAAR EXCLUSIEF / BTW INBEGREPEN) ── */
    {
      type: "mc",
      vraag: "Een computerspel kost in de winkel € 60,50 inclusief 21% btw. Wat is de prijs exclusief btw?",
      opties: ["€ 50,00", "€ 47,79", "€ 39,50", "€ 52,00"],
      antwoord: 0,
      uitleg: "De prijs inclusief btw is 121% (100% prijs + 21% btw). <br>Prijs exclusief btw = € 60,50 / 1,21 = <b>€ 50,00</b>. De btw is dan € 10,50."
    },
    {
      type: "invul",
      vraag: "Duru koopt een nieuwe roman. Het boek kost € 21,80 inclusief 9% btw. Wat is de prijs van het boek zonder btw (exclusief btw)? (Vul alleen het getal in)",
      antwoord: "20|20,00|20.00",
      uitleg: "De prijs inclusief btw is 109% (100% prijs + 9% btw). <br>Prijs exclusief btw = € 21,80 / 1,09 = <b>€ 20,00</b>."
    },
    {
      type: "mc",
      vraag: "Als een trui € 121 inclusief 21% btw kost, hoeveel euro btw zit er dan in deze prijs verwerkt?",
      opties: ["€ 21,00", "€ 25,41", "€ 100,00", "€ 17,36"],
      antwoord: 0,
      uitleg: "De prijs inclusief btw is 121%. <br>Prijs exclusief btw = € 121 / 1,21 = € 100. <br>Btw-bedrag = € 121 − € 100 = <b>€ 21,00</b>."
    },
    {
      type: "waaronwaar",
      vraag: "Om van een prijs inclusief 21% btw de btw te berekenen, neem je simpelweg 21% van het verkoopbedrag.",
      antwoord: false,
      uitleg: "Onwaar! Als de prijs inclusief btw € 121 is, dan is 21% daarvan € 25,41. Maar de echte btw is € 21. Je moet delen door 1,21 en dan vermenigvuldigen met 0,21 (of het verschil nemen met de prijs excl. btw)."
    },

    /* ── BEGROTING & TEKORTEN ── */
    {
      type: "mc",
      vraag: "De rijksoverheid raamt voor volgend jaar € 340 miljard aan inkomsten. De geplande uitgaven zijn € 355 miljard. Wat is het resultaat op de begroting?",
      opties: [
        "Een begrotingstekort van € 15 miljard",
        "Een begrotingsoverschot van € 15 miljard",
        "Een staatsschuld van € 15 miljard",
        "Een begrotingstekort van € 355 miljard"
      ],
      antwoord: 0,
      uitleg: "Omdat de uitgaven (€ 355 miljard) groter zijn dan de inkomsten (€ 340 miljard), heeft de overheid een <b>begrotingstekort van € 15 miljard</b>."
    },
    {
      type: "invul",
      vraag: "In een bepaald jaar heeft de rijksoverheid € 312 miljard uitgegeven. De inkomsten waren € 318 miljard. Hoe groot is het begrotingsoverschot in miljarden euro's? (Vul alleen het getal in)",
      antwoord: "6|6 miljard|6,00|6.00",
      uitleg: "Inkomsten (€ 318 miljard) − Uitgaven (€ 312 miljard) = <b>€ 6 miljard</b> overschot. De overheid houdt geld over!"
    },
    {
      type: "waaronwaar",
      vraag: "Als er in een jaar een begrotingstekort is van € 8 miljard, stijgt de staatsschuld met € 8 miljard (als er niet wordt afgelost).",
      antwoord: true,
      uitleg: "Waar. De overheid moet het tekort van € 8 miljard lenen op de kapitaalmarkt. Hierdoor stijgt de totale staatsschuld met dit bedrag."
    },
    {
      type: "mc",
      vraag: "De staatsschuld van Nederland is € 400 miljard. De gemiddelde rente die de overheid hierover moet betalen is 2%. Hoeveel rente betaalt de overheid dit jaar over de staatsschuld?",
      opties: ["€ 8 miljard", "€ 2 miljard", "€ 80 miljard", "€ 4 miljard"],
      antwoord: 0,
      uitleg: "Rente = 2% van € 400 miljard. <br>Berekening: 0,02 × 400 = <b>€ 8 miljard</b>. Dit is een grote uitgavenpost op de begroting!"
    },

    /* ── INKOMSTENBELASTING & SCHIJVENTARIEF (SIMPEL PROGRESSIEF) ── */
    {
      type: "mc",
      vraag: "Stel dat de belastingtarieven in een land als volgt zijn:<br>• Tot € 30.000 inkomen: 30% belasting<br>• Alles daarboven: 50% belasting<br>Hoeveel inkomstenbelasting betaalt iemand met een inkomen van € 40.000?",
      opties: ["€ 14.000", "€ 12.000", "€ 20.000", "€ 17.000"],
      antwoord: 0,
      uitleg: "Dit is een progressief schijvensysteem. <br>1) Over de eerste € 30.000 betaal je 30% = 0,30 × 30.000 = € 9.000.<br>2) Over het deel daarboven (€ 40.000 − € 30.000 = € 10.000) betaal je 50% = 0,50 × 10.000 = € 5.000.<br>Totaal = € 9.000 + € 5.000 = <b>€ 14.000</b>."
    },
    {
      type: "invul",
      vraag: "Gebruik dezelfde schijven als de vorige vraag (30% tot € 30.000, 50% daarboven). Iemand verdient € 20.000 per jaar. Hoeveel euro belasting betaalt deze persoon? (Vul alleen het getal in)",
      antwoord: "6000|6.000|6,000",
      uitleg: "Het inkomen van € 20.000 valt volledig in de eerste schijf. <br>Berekening: 30% van € 20.000 = 0,30 × 20.000 = <b>€ 6.000</b>."
    },
    {
      type: "mc",
      vraag: "Duru leest dat de overheid loonheffing inhoudt op het brutoloon van haar oudere zus. Haar zus verdient bruto € 2.000 per maand en krijgt netto € 1.600 op haar rekening. Hoeveel procent van haar brutoloon is ingehouden als loonheffing?",
      opties: ["20%", "40%", "25%", "15%"],
      antwoord: 0,
      uitleg: "Ingehouden bedrag = bruto − netto = € 2.000 − € 1.600 = € 400. <br>Percentage = (€ 400 / € 2.000) × 100% = <b>20%</b>."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een proportioneel belastingstelsel (vlaktaks) betaalt iemand met een inkomen van € 100.000 in verhouding (in procenten) meer belasting dan iemand die € 20.000 verdient.",
      antwoord: false,
      uitleg: "Onwaar. Bij een proportioneel stelsel betaalt <b>iedereen hetzelfde percentage</b> (bijvoorbeeld 35%), ongeacht het inkomen. Alleen bij een progressief stelsel betalen rijke mensen een hoger percentage."
    },

    /* ── GEMENGD REKENEN ── */
    {
      type: "mc",
      vraag: "Een winkelier koopt een jas in voor € 100. Hij wil 40% winstmarge (brutowinst) maken op de inkoopprijs. De verkoopprijs exclusief btw wordt dus € 140. Welke consumentenprijs moet er op het prijskaartje staan inclusief 21% btw?",
      opties: ["€ 169,40", "€ 140,00", "€ 170,00", "€ 159,40"],
      antwoord: 0,
      uitleg: "De prijs exclusief btw is € 140. <br>Btw-bedrag: 21% van € 140 = 0,21 × 140 = € 29,40. <br>Totaalprijs: € 140 + € 29,40 = <b>€ 169,40</b>."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de overheid bij een begrotingstekort geld moet lenen en wat de gevolgen daarvan zijn voor de toekomstige rijksbegroting.",
      sleutelwoorden: ["lenen", "staatsschuld", "rente", "toekomst/belasting"],
      minTreffers: 2,
      modelantwoord: "Bij een tekort geeft de overheid meer uit dan er binnenkomt. Ze moet dit lenen, waardoor de staatsschuld stijgt. Het gevolg is dat de overheid in de toekomst meer rente moet betalen over deze schuld, waardoor er minder geld overblijft voor collectieve voorzieningen.",
      uitleg: "Lenen leidt tot een hogere <b>staatsschuld</b>. Over deze schuld moet de overheid elk jaar <b>rente</b> betalen. Die rentelasten drukken op de toekomstige begrotingen."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen bruto en netto salaris?",
      sleutelwoorden: ["bruto/loonheffing/belasting/premie/voor", "netto/over/rekening/krijgt/na"],
      minTreffers: 2,
      modelantwoord: "Brutosalaris is het loon dat je afspreekt met je werkgever, waar de belastingen en premies nog vanaf moeten. Nettosalaris is het bedrag dat je daadwerkelijk op je bankrekening gestort krijgt nadat de loonheffing is ingehouden.",
      uitleg: "<b>Bruto</b> is vóór aftrek van belastingen en sociale premies. <b>Netto</b> is wat je echt overhoudt op je rekening (netto = bruto − loonheffing)."
    }
  ]
});
