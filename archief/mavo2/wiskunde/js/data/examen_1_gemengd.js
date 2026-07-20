/* Proeftoets 1 — Gemengd H8 (Vergelijkingen) */
DURU.registerExamen({
  id: "ex-w-1",
  titel: "Proeftoets 1 — Gemengd H8",
  vak: "Wiskunde H8",
  icoon: "📝",
  duurMin: 20,
  vragen: [

    /* ── 8.1 Gelijksoortige termen ── */

    {
      type: "mc",
      vraag: "Welke twee termen zijn gelijksoortig?",
      opties: ["4x en 4", "4x en 7x", "4x en 7y", "4 en 7y"],
      antwoord: 1,
      uitleg: "<b>4x</b> en <b>7x</b> zijn gelijksoortig: ze hebben allebei de letter x. Bij de andere paren is er een verschil in letter of ontbreekt er een letter."
    },

    {
      type: "waaronwaar",
      vraag: "b + b + b = 3b²",
      antwoord: false,
      uitleg: "Onwaar! <b>b + b + b = 3b</b>. Je telt de coëfficiënten op: 1 + 1 + 1 = 3, de letter b blijft. Machten ontstaan bij vermenigvuldigen (b × b = b²), niet bij optellen."
    },

    {
      type: "invoer",
      vraag: "Vereenvoudig: 2a + 5a. Wat is de coëfficiënt van a?",
      antwoord: "7",
      tolerantie: 0,
      uitleg: "2a + 5a = <b>7a</b>. Coëfficiënt is 7.",
      hint: "Tel 2 en 5 op."
    },

    {
      type: "mc",
      vraag: "Vereenvoudig: 6x + 3 − 2x + 5",
      opties: ["4x + 8", "8x + 8", "4x − 8", "4x + 2"],
      antwoord: 0,
      uitleg: "x-termen: 6x − 2x = <b>4x</b>. Getallen: 3 + 5 = <b>8</b>. Samen: <b>4x + 8</b>.",
      hint: "Voeg de x-termen samen en de losse getallen samen."
    },

    {
      type: "invoer",
      vraag: "Schrijf korter: 9n − 4n + 2. Wat is de coëfficiënt van n?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "9n − 4n = <b>5n</b>. De +2 blijft staan: 5n + 2. Coëfficiënt van n is 5.",
      hint: "Trek de coëfficiënten van n van elkaar af: 9 − 4."
    },

    {
      type: "waaronwaar",
      vraag: "De formule 3x + 2y + 5x − y kan vereenvoudigd worden tot 8x + y.",
      antwoord: true,
      uitleg: "Waar! x-termen: 3x + 5x = <b>8x</b>. y-termen: 2y − y = <b>y</b> (= 1y). Samen: <b>8x + y</b>. ✓"
    },

    {
      type: "invoer",
      vraag: "Vereenvoudig: 3x + 2 + 5x − 1. Wat is de coëfficiënt van x?",
      antwoord: "8",
      tolerantie: 0,
      uitleg: "x-termen: 3x + 5x = <b>8x</b>. Getallen: 2 − 1 = 1. Samen: 8x + 1. Coëfficiënt van x is 8.",
      hint: "Voeg de x-termen samen: 3 + 5."
    },

    {
      type: "invoer",
      vraag: "Schrijf korter: 7k − 2k + 4k. Wat is de coëfficiënt van k?",
      antwoord: "9",
      tolerantie: 0,
      uitleg: "7k − 2k + 4k = (7 − 2 + 4)k = <b>9k</b>. Coëfficiënt is 9.",
      hint: "Bereken 7 − 2 + 4."
    },

    /* ── 8.2 De balans ── */

    {
      type: "invoer",
      vraag: "Los op met de balans: 2x + 1 = 9. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stap 1: haal 1 af van beide kanten → 2x = 8. Stap 2: deel door 2 → x = <b>4</b>. Controle: 2 × 4 + 1 = 8 + 1 = 9 ✓",
      hint: "Haal eerst 1 af van beide kanten, dan deel je door 2."
    },

    {
      type: "mc",
      vraag: "Los op: 4x + 3 = 15. Wat is x?",
      opties: ["x = 2", "x = 3", "x = 4", "x = 5"],
      antwoord: 1,
      uitleg: "4x + 3 − 3 = 15 − 3 → 4x = 12 → x = 12 : 4 = <b>3</b>. Controle: 4 × 3 + 3 = 12 + 3 = 15 ✓",
      hint: "Haal eerst 3 af van beide kanten, dan deel je door 4."
    },

    /* ── 8.3 Vergelijkingen oplossen ── */

    {
      type: "invoer",
      vraag: "Los op: 3x + 7 = 22. Wat is x?",
      antwoord: "5",
      tolerantie: 0,
      uitleg: "3x + 7 − 7 = 22 − 7 → 3x = 15 → x = 15 : 3 = <b>5</b>. Controle: 3 × 5 + 7 = 15 + 7 = 22 ✓",
      hint: "Haal 7 af van beide kanten, dan deel je door 3."
    },

    {
      type: "waaronwaar",
      vraag: "De oplossing van 6x − 2 = 16 is x = 3.",
      antwoord: true,
      uitleg: "Waar! 6x − 2 + 2 = 16 + 2 → 6x = 18 → x = 18 : 6 = <b>3</b>. Controle: 6 × 3 − 2 = 18 − 2 = 16 ✓"
    },

    {
      type: "invoer",
      vraag: "Los op: 5x = 3x + 8. Wat is x?",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Haal 3x van beide kanten af: 5x − 3x = 8 → 2x = 8 → x = 8 : 2 = <b>4</b>. Controle: links 5 × 4 = 20; rechts 3 × 4 + 8 = 12 + 8 = 20 ✓",
      hint: "Haal 3x van beide kanten af zodat alle x-termen links staan."
    },

    /* ── 8.4 Het snijpunt ── */

    {
      type: "mc",
      vraag: "Wat is het snijpunt van y = 2x + 3 en y = x + 7?",
      opties: ["(3, 9)", "(4, 11)", "(5, 13)", "(2, 9)"],
      antwoord: 1,
      uitleg: "Stel gelijk: 2x + 3 = x + 7 → x = 4. Vul in: y = 2 × 4 + 3 = 8 + 3 = <b>11</b>. Controle: y = 4 + 7 = 11 ✓. Snijpunt: <b>(4, 11)</b>.",
      hint: "Stel de twee formules gelijk, los op voor x, vul daarna x in voor y."
    },

    {
      type: "invoer",
      vraag: "Zoek de x-coördinaat van het snijpunt van y = 4x + 2 en y = 2x + 10.",
      antwoord: "4",
      tolerantie: 0,
      uitleg: "Stel gelijk: 4x + 2 = 2x + 10 → 4x − 2x = 10 − 2 → 2x = 8 → x = <b>4</b>. Vul in: y = 4 × 4 + 2 = 18. Controle: 2 × 4 + 10 = 8 + 10 = 18 ✓.",
      hint: "Haal 2x van beide kanten af, dan haal je 2 af van beide kanten."
    },

    {
      type: "waaronwaar",
      vraag: "Het snijpunt van y = 3x + 1 en y = x + 9 ligt op het punt (4, 13).",
      antwoord: true,
      uitleg: "Waar! Stel gelijk: 3x + 1 = x + 9 → 2x = 8 → x = <b>4</b>. y = 3 × 4 + 1 = 12 + 1 = <b>13</b>. Controle: y = 4 + 9 = 13 ✓. Snijpunt: (4, 13)."
    }

  ]
});
