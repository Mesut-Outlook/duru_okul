/* Proeftoets 1 — Wiskunde HAVO 3: algebra/rekenen (lineaire vergelijkingen, procenten, machten).
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-wiskunde-1",
  titel: "Proeftoets 1 — Wiskunde: algebra & rekenen",
  vak: "Wiskunde · HAVO 3",
  icoon: "⚖️",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Los op: <b>3x + 5 = 20</b>. Wat is x?",
      opties: [
        "3",
        "5",
        "15",
        "25"
      ],
      antwoord: 1,
      uitleg: "3x + 5 = 20 → 3x = 15 (5 aftrekken van beide kanten) → x = 5 (delen door 3)."
    },
    {
      type: "mc",
      vraag: "Wat is <b>25% van 80</b>?",
      opties: [
        "15",
        "20",
        "25",
        "30"
      ],
      antwoord: 1,
      uitleg: "25% is een kwart. 80 : 4 = 20. Dus 25% van 80 is 20."
    },
    {
      type: "waaronwaar",
      vraag: "2³ (2 tot de macht 3) is gelijk aan 6.",
      antwoord: false,
      uitleg: "Onwaar. 2³ = 2 × 2 × 2 = 8, niet 6. Let op: machtsverheffen is geen vermenigvuldigen met de macht zelf."
    },
    {
      type: "invul",
      vraag: "Bereken: 4² = … .",
      antwoord: "16",
      uitleg: "4² betekent 4 × 4 = 16."
    },
    {
      type: "open",
      vraag: "Leg stap voor stap uit hoe je de vergelijking <b>2x − 4 = 10</b> oplost, en geef de uitkomst.",
      sleutelwoorden: ["2x=14/optellen/4 optellen bij beide kanten", "delen door 2/:2/gedeeld door 2", "x=7/x = 7"],
      minTreffers: 2,
      modelantwoord: "Eerst tel je 4 op bij beide kanten: 2x − 4 + 4 = 10 + 4, dus 2x = 14. Daarna deel je beide kanten door 2: x = 7.",
      uitleg: "Bij het oplossen van een lineaire vergelijking werk je in stappen: eerst getallen isoleren (hier: +4 aan beide kanten), dan delen door de coëfficiënt van x. Uitkomst: x = 7."
    }
  ]
});
