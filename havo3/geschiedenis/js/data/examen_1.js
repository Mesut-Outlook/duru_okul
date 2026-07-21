/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Proeftoets 1: Tijdvakken & Bronnen
   ========================================================= */
(function () {
  "use strict";

  DURU.registerExamen({
    id: "ex-h3-geschiedenis-1",
    titel: "Proeftoets 1 — Tijdvakken, Bronnen & Gebeurtenissen",
    vak: "Geschiedenis · HAVO 3",
    icoon: "🕰️",
    duurMin: 10,
    vragen: [
      {
        id: "ges1_v1",
        type: "mc",
        vraag: "Wat voor soort bron is een dagboek geschreven door een soldaat tijdens de Eerste Wereldoorlog?",
        opties: [
          "Een primaire bron",
          "Een secundaire bron",
          "Een tertiaire bron",
          "Een niet-historische bron"
        ],
        antwoord: 0,
        uitleg: "Een primaire bron is afkomstig uit de tijd zelf en gemaakt door iemand die er rechtstreeks bij betrokken was."
      },
      {
        id: "ges1_v2",
        type: "mc",
        vraag: "In welk tijdvak vond de Industriële Revolutie in Europa voornamelijk plaats?",
        opties: [
          "Tijd van ontdekkers en hervormers (16e eeuw)",
          "Tijd van pruiken en revoluties (18e eeuw)",
          "Tijd van burgers en stoommachines (19e eeuw)",
          "Tijd van de wereldoorlogen (20e eeuw)"
        ],
        antwoord: 2,
        uitleg: "De Industriële Revolutie vond plaats in het tijdvak van burgers en stoommachines (19e eeuw, 1800-1900)."
      },
      {
        id: "ges1_v3",
        type: "waaronwaar",
        vraag: "Een geschiedenisboek dat dit jaar is geschreven over de Romeinen is een voorbeeld van een primaire bron.",
        antwoord: false,
        uitleg: "Onwaar! Een modern geschiedenisboek over de Romeinen is een secundaire bron, omdat het later is geschreven op basis van oudere bronnen."
      },
      {
        id: "ges1_v4",
        type: "invul",
        vraag: "Hoe noemen we een historische bron die niet uit geschreven tekst bestaat, zoals een munt of een zwaard?",
        antwoord: "ongeschreven bron|ongeschreven|archeologische vondst",
        uitleg: "Historische bronnen zonder tekst noemen we ongeschreven bronnen (zoals voorwerpen, gebouwen of fossielen)."
      },
      {
        id: "ges1_v5",
        type: "open",
        vraag: "Leg in je eigen woorden uit wat het verschil is tussen een oorzaak en een aanleiding van een oorlog.",
        sleutelwoorden: [
          "oorzaak/dieper/langere tijd/achtergrond",
          "aanleiding/vonk/gebeurtenis/druppel"
        ],
        minTreffers: 1,
        modelantwoord: "Een oorzaak is een dieper liggende reden die al langer speelt, terwijl een aanleiding de directe gebeurtenis (de 'vonk') is waardoor de oorlog opeens uitbreekt.",
        uitleg: "Oorzaken bouwen spanning op over een langere periode; de aanleiding is het specifieke voorval dat het conflict direct doet ontbranden."
      }
    ]
  });
})();
