/* Proeftoets 1 — Economie HAVO 3: introductie (schaarste, keuzes, geld).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-economie-1",
  titel: "Proeftoets 1 — Economie: de basis",
  vak: "Economie · HAVO 3",
  icoon: "🏛️",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Wat betekent het economische begrip <b>schaarste</b>?",
      opties: [
        "Er is bijna niets meer over van een product",
        "Behoeften zijn onbeperkt, maar de middelen om ze te vervullen zijn beperkt",
        "Iets is heel duur geworden",
        "Er is een tekort door een staking"
      ],
      antwoord: 1,
      uitleg: "Schaarste betekent dat onze behoeften vrijwel onbeperkt zijn, terwijl de middelen (geld, tijd, grondstoffen) beperkt zijn. Daarom moet je kiezen."
    },
    {
      type: "mc",
      vraag: "Je hebt € 20 en kiest voor een game in plaats van een boek van € 20. Wat zijn de <b>alternatieve kosten</b> van de game?",
      opties: [
        "€ 40, want samen kosten ze zoveel",
        "Niets, want je hebt genoeg geld",
        "Het boek dat je nu niet kunt kopen",
        "De btw die op de game zit"
      ],
      antwoord: 2,
      uitleg: "Alternatieve kosten (opportuniteitskosten) zijn wat je opgeeft door voor iets anders te kiezen. Kies je de game, dan geef je het boek op."
    },
    {
      type: "waaronwaar",
      vraag: "Ruilen met geld is handiger dan ruilhandel (goederen direct tegen goederen ruilen).",
      antwoord: true,
      uitleg: "Waar. Met geld hoef je niet iemand te vinden die precies wil wat jij hebt én biedt wat jij zoekt. Geld is een algemeen ruilmiddel."
    },
    {
      type: "invul",
      vraag: "Alles wat je nodig hebt of graag wilt hebben, noemen we in de economie een … .",
      antwoord: "behoefte|behoeften",
      uitleg: "Een behoefte is alles wat je nodig hebt of wilt. Onbeperkte behoeften + beperkte middelen = schaarste."
    },
    {
      type: "open",
      vraag: "Leg met een voorbeeld uit waarom je bij schaarste altijd een <b>keuze</b> moet maken.",
      sleutelwoorden: ["beperkt/beperkte middelen/beperkt geld", "kiezen/keuze", "behoefte/behoeften/wil"],
      minTreffers: 2,
      modelantwoord: "Omdat je middelen (bijv. geld of tijd) beperkt zijn en je behoeften onbeperkt, kun je niet alles hebben. Voorbeeld: met € 20 kun je een game óf een boek kopen, dus je moet kiezen.",
      uitleg: "Kernidee: beperkte middelen + onbeperkte behoeften dwingen je te kiezen. Een concreet voorbeeld maakt het compleet."
    }
  ]
});
