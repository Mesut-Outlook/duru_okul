/* Proeftoets 2 — Vergelijkingen oplossen (focus 8.2 + 8.3, snijpunt 8.4) */
DURU.registerExamen({
  id: "ex-w-2",
  titel: "Proeftoets 2 — Vergelijkingen oplossen",
  vak: "Wiskunde H8",
  icoon: "⚖️",
  duurMin: 20,
  vragen: [

    /* ── 8.2 De balans ── */

    {
      type: "waaronwaar",
      vraag: "De oplossing van 4x + 4 = 24 is x = 5.",
      antwoord: true,
      uitleg: "Waar! 4x + 4 − 4 = 24 − 4 → 4x = 20 → x = 20 : 4 = <b>5</b>. Controle: 4 × 5 + 4 = 20 + 4 = 24 ✓"
    },

    {
      type: "invoer",
      vraag: "Los op met de balans: 3x = 21. Wat is x?",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "Deel beide kanten door 3: x = 21 : 3 = <b>7</b>. Controle: 3 × 7 = 21 ✓",
      hint: "Deel beide kanten door 3."
    },

    {
      type: "invoer",
      vraag: "Los op: 5x + 4 = 24. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stap 1: 5x + 4 − 4 = 24 − 4 → 5x = 20. Stap 2: x = 20 : 5 = <b>4</b>. Controle: 5 × 4 + 4 = 20 + 4 = 24 ✓",
      hint: "Haal 4 af van beide kanten, dan deel je door 5."
    },

    {
      type: "mc",
      vraag: "Los op: 2x + 8 = 20. Wat is x?",
      opties: ["x = 4", "x = 5", "x = 6", "x = 7"],
      antwoord: 2,
      uitleg: "2x + 8 − 8 = 20 − 8 → 2x = 12 → x = 12 : 2 = <b>6</b>. Controle: 2 × 6 + 8 = 12 + 8 = 20 ✓",
      hint: "Haal 8 af van beide kanten, dan deel je door 2."
    },

    {
      type: "mc",
      vraag: "Ali heeft €6 gespaard en krijgt elke week €8 zakgeld. Na hoeveel weken heeft hij €38? Vergelijking: 8w + 6 = 38. Wat is w?",
      opties: ["w = 3", "w = 4", "w = 5", "w = 6"],
      antwoord: 1,
      uitleg: "8w + 6 − 6 = 38 − 6 → 8w = 32 → w = 32 : 8 = <b>4</b>. Na 4 weken heeft Ali €38. Controle: 8 × 4 + 6 = 32 + 6 = 38 ✓",
      hint: "Haal 6 af van beide kanten, dan deel je door 8."
    },

    /* ── 8.3 Vergelijkingen oplossen — systematisch ── */

    {
      type: "invoer",
      vraag: "Los op: 7x − 5 = 30. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "7x − 5 + 5 = 30 + 5 → 7x = 35 → x = 35 : 7 = <b>5</b>. Controle: 7 × 5 − 5 = 35 − 5 = 30 ✓",
      hint: "Er staat een minteken: tel 5 op bij beide kanten."
    },

    {
      type: "invoer",
      vraag: "Duru oefent voor de toets. Los op: 4x + 9 = 33. Wat is x?",
      antwoord: "6",
      tolerantie: 0,
      uitleg: "4x + 9 − 9 = 33 − 9 → 4x = 24 → x = 24 : 4 = <b>6</b>. Controle: 4 × 6 + 9 = 24 + 9 = 33 ✓",
      hint: "Haal 9 af van beide kanten, dan deel je door 4."
    },

    {
      type: "waaronwaar",
      vraag: "De oplossing van −3x + 12 = 3 is x = 3.",
      antwoord: true,
      uitleg: "Waar! −3x + 12 − 12 = 3 − 12 → −3x = −9 → x = −9 : −3 = <b>3</b>. Controle: −3 × 3 + 12 = −9 + 12 = 3 ✓",
      hint: "Haal 12 af van beide kanten: dan houd je −3x = −9. Deel door −3."
    },

    {
      type: "mc",
      vraag: "Los op: 9x − 12 = 33. Wat is x?",
      opties: ["x = 4", "x = 5", "x = 6", "x = 7"],
      antwoord: 1,
      uitleg: "9x − 12 + 12 = 33 + 12 → 9x = 45 → x = 45 : 9 = <b>5</b>. Controle: 9 × 5 − 12 = 45 − 12 = 33 ✓",
      hint: "Tel 12 op bij beide kanten, dan deel je door 9."
    },

    {
      type: "invoer",
      vraag: "Los op: 6x = 4x + 14. Wat is x?",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "Haal 4x van beide kanten af: 6x − 4x = 14 → 2x = 14 → x = 14 : 2 = <b>7</b>. Controle: links 6 × 7 = 42; rechts 4 × 7 + 14 = 28 + 14 = 42 ✓",
      hint: "Haal 4x van beide kanten af zodat alle x-termen links staan."
    },

    {
      type: "invoer",
      vraag: "Los op: 5x + 3 = 2x + 18. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "5x + 3 = 2x + 18 → 5x − 2x + 3 = 18 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: links 5 × 5 + 3 = 28; rechts 2 × 5 + 18 = 10 + 18 = 28 ✓",
      hint: "Haal 2x van beide kanten af, trek dan 3 af van beide kanten."
    },

    {
      type: "invoer",
      vraag: "De lengte van een rechthoekige tuin is 8x + 2 meter. De breedte is 5x + 14 meter. De tuin is een vierkant (lengte = breedte). Vergelijking: 8x + 2 = 5x + 14. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "8x + 2 = 5x + 14 → 8x − 5x + 2 = 14 → 3x + 2 = 14 → 3x = 12 → x = 12 : 3 = <b>4</b>. Controle: links 8 × 4 + 2 = 34; rechts 5 × 4 + 14 = 20 + 14 = 34 ✓",
      hint: "Haal 5x van beide kanten af, trek dan 2 af van beide kanten."
    },

    {
      type: "mc",
      vraag: "Los op: 10x − 3 = 4x + 21. Wat is x?",
      opties: ["x = 3", "x = 4", "x = 5", "x = 6"],
      antwoord: 1,
      uitleg: "10x − 3 = 4x + 21 → 10x − 4x = 21 + 3 → 6x = 24 → x = 24 : 6 = <b>4</b>. Controle: links 10 × 4 − 3 = 37; rechts 4 × 4 + 21 = 16 + 21 = 37 ✓",
      hint: "Haal 4x van beide kanten af, tel dan 3 op bij beide kanten."
    },

    /* ── 8.4 Het snijpunt ── */

    {
      type: "invoer",
      vraag: "Zoek de x-coördinaat van het snijpunt van y = 3x + 5 en y = x + 13.",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stel gelijk: 3x + 5 = x + 13 → 3x − x = 13 − 5 → 2x = 8 → x = <b>4</b>. y = 3 × 4 + 5 = 17. Controle: y = 4 + 13 = 17 ✓. Snijpunt: (4, 17).",
      hint: "Stel de twee formules gelijk en los op voor x."
    },

    {
      type: "invoer",
      vraag: "Zoek de x-coördinaat van het snijpunt van y = 5x − 1 en y = 2x + 8.",
      antwoord: "3",
      tolerantie: 0,
      uitleg: "Stel gelijk: 5x − 1 = 2x + 8 → 5x − 2x = 8 + 1 → 3x = 9 → x = <b>3</b>. y = 5 × 3 − 1 = 15 − 1 = 14. Controle: 2 × 3 + 8 = 6 + 8 = 14 ✓. Snijpunt: (3, 14).",
      hint: "Haal 2x van beide kanten af, tel dan 1 op bij beide kanten."
    },

    {
      type: "mc",
      vraag: "Wat is het snijpunt van y = 4x + 6 en y = x + 15?",
      opties: ["(2, 14)", "(3, 18)", "(4, 19)", "(5, 20)"],
      antwoord: 1,
      uitleg: "Stel gelijk: 4x + 6 = x + 15 → 3x = 9 → x = 3. Vul in: y = 4 × 3 + 6 = 12 + 6 = <b>18</b>. Controle: y = 3 + 15 = 18 ✓. Snijpunt: <b>(3, 18)</b>.",
      hint: "Stel de formules gelijk, los op voor x, vul dan in voor y."
    }

  ]
});
