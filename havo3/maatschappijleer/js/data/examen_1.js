/* =========================================================
   Duru's Maatschappijleer (HAVO 3) — Proeftoets 1: Samenleven & Rechten
   ========================================================= */
(function () {
  "use strict";

  DURU.registerExamen({
    id: "ex-h3-maatschappijleer-1",
    titel: "Proeftoets 1 — Samenleven, Rechten & Overheid",
    vak: "Maatschappijleer · HAVO 3",
    icoon: "🏛️",
    duurMin: 10,
    vragen: [
      {
        id: "maats1_v1",
        type: "mc",
        vraag: "Welk kenmerk hoort bij een democratische rechtsstaat?",
        opties: [
          "De koning maakt alleen alle wetten",
          "Burgers hebben grondrechten en de overheid moet zich ook aan de wet houden",
          "Er is maar één politieke partij toegestaan",
          "De politie mag iedereen zonder rechtzaak opsluiten"
        ],
        antwoord: 1,
        uitleg: "In een rechtsstaat zijn grondrechten beschermd en is iedereen, inclusief de overheid, gebonden aan de wet."
      },
      {
        id: "maats1_v2",
        type: "mc",
        vraag: "Hoe noemen we de scheiding van de wetgevende, uitvoerende en rechterlijke macht?",
        opties: [
          "De Grondwet",
          "De Trias Politica",
          "Het parlementair stelsel",
          "De Rechtsbescherming"
        ],
        antwoord: 1,
        uitleg: "De Trias Politica is de verdeling van de staatsmacht in drie onafhankelijke machten om machtsmisbruik te voorkomen."
      },
      {
        id: "maats1_v3",
        type: "waaronwaar",
        vraag: "In Nederland geldt vrijheid van meningsuiting, maar je mag niet aanzetten tot haat of discriminatie.",
        antwoord: true,
        uitleg: "Waar! Vrijheid van meningsuiting is een belangrijk grondrecht, maar kent wettelijke grenzen zoals het verbod op discriminatie."
      },
      {
        id: "maats1_v4",
        type: "invul",
        vraag: "Welk belangrijk document bevat de belangrijkste rechten en plichten van alle Nederlandse burgers?",
        antwoord: "grondwet|de grondwet",
        uitleg: "De Grondwet is de basiswet van Nederland waarin de grondrechten en de inrichting van de staat staan."
      },
      {
        id: "maats1_v5",
        type: "open",
        vraag: "Leg in je eigen woorden uit waarom onafhankelijke rechters belangrijk zijn in een samenleving.",
        sleutelwoorden: [
          "eerlijk/onpartijdig/zonder beïnvloeding",
          "politiek/overheid/macht/bescherming"
        ],
        minTreffers: 1,
        modelantwoord: "Onafhankelijke rechters beoordelen zaken eerlijk en onpartijdig, zonder dat de overheid of politici invloed op de uitspraak kunnen uitoefenen.",
        uitleg: "Rechterlijke onafhankelijkheid garandeert dat burgers beschermd worden en dat iedereen een eerlijk proces krijgt."
      }
    ]
  });
})();
