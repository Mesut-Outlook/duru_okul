/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — Proeftoets 1: Klimaat & Aarde
   ========================================================= */
(function () {
  "use strict";

  DURU.registerExamen({
    id: "ex-h3-aardrijkskunde-1",
    titel: "Proeftoets 1 — Klimaat, Aarde & Bevolking",
    vak: "Aardrijkskunde · HAVO 3",
    icoon: "🗺️",
    duurMin: 10,
    vragen: [
      {
        id: "ak1_v1",
        type: "mc",
        vraag: "Welk klimaat kenmerkt zich door warme droge zomers en zachte natte winters rond de Middellandse Zee?",
        opties: [
          "Tropisch regenwoudklimaat",
          "Middellandse Zeeklimaat (mediterraan)",
          "Toendraklimaat",
          "Woestijnklimaat"
        ],
        antwoord: 1,
        uitleg: "Het Middellandse Zeeklimaat (of mediterraan klimaat) heeft droge, warme zomers en milde, neerslagrijke winters."
      },
      {
        id: "ak1_v2",
        type: "mc",
        vraag: "Hoe noemen we het verschijnsel waarbij aardplaten langs of tegen elkaar bewegen?",
        opties: [
          "Erosie",
          "Verwering",
          "Platentektoniek",
          "Verwoestijning"
        ],
        antwoord: 2,
        uitleg: "Platentektoniek is het bewegen van de aardplaten, wat aardbevingen, vulkanisme en bergvorming veroorzaakt."
      },
      {
        id: "ak1_v3",
        type: "waaronwaar",
        vraag: "Erosie is het afbreken van gesteente door weersinvloeden zonder dat het gesteente wordt verplaatst.",
        antwoord: false,
        uitleg: "Onwaar! Het afbreken zonder verplaatsing heet verwering. Erosie is het afslijten én verplaatsen van materiaal door wind, water of ijs."
      },
      {
        id: "ak1_v4",
        type: "invul",
        vraag: "Welk begrip geeft het aantal inwoners aan dat gemiddeld per vierkante kilometer woont?",
        antwoord: "bevolkingsdichtheid|dichtheid",
        uitleg: "De bevolkingsdichtheid geeft aan hoeveel mensen er gemiddeld per km² in een gebied wonen."
      },
      {
        id: "ak1_v5",
        type: "open",
        vraag: "Leg uit wat het broeikaseffect is en waarom het essentieel is voor leven op aarde.",
        sleutelwoorden: [
          "warmte/gassen/vasthouden",
          "temperatuur/leefbaar/koud"
        ],
        minTreffers: 1,
        modelantwoord: "Het broeikaseffect is het vasthouden van warmte in de atmosfeer door broeikasgassen, waardoor de temperatuur op aarde leefbaar blijft.",
        uitleg: "Zonder natuurlijk broeikaseffect zou het op aarde gemiddeld zo'n -18 °C zijn, wat leven zoals we dat kennen onmogelijk maakt."
      }
    ]
  });
})();
