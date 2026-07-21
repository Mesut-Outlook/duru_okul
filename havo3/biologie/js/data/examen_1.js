/* =========================================================
   Duru's Biologie (HAVO 3) — Proeftoets 1: Cellen, Organen & Planten
   ========================================================= */
(function () {
  "use strict";

  DURU.registerExamen({
    id: "ex-h3-biologie-1",
    titel: "Proeftoets 1 — Cellen, Organen & Planten",
    vak: "Biologie · HAVO 3",
    icoon: "🧬",
    duurMin: 10,
    vragen: [
      {
        id: "bio1_v1",
        type: "mc",
        vraag: "Welk onderdeel van een plantaardige cel geeft stevigheid aan de cel?",
        opties: [
          "Celmembraan",
          "Celwand",
          "Celkern",
          "Cytoplasma"
        ],
        antwoord: 1,
        uitleg: "De celwand is een stevig laagje om de plantaardige cel heen dat voor stevigheid en vorm zorgt. Dierlijke cellen hebben géén celwand."
      },
      {
        id: "bio1_v2",
        type: "mc",
        vraag: "In welk celorgaan vindt de fotosynthese plaats bij planten?",
        opties: [
          "Vacuole",
          "Mitochondriën",
          "Bladgroenkorrels (chloroplasten)",
          "Celkern"
        ],
        antwoord: 2,
        uitleg: "In de bladgroenkorrels (chloroplasten) gebruikt de plant zonlicht, water en koolstofdioxide om glucose en zuurstof te maken."
      },
      {
        id: "bio1_v3",
        type: "waaronwaar",
        vraag: "Dierlijke cellen hebben wel een vacuole en celwand, maar geen celkern.",
        antwoord: false,
        uitleg: "Onwaar! Dierlijke cellen hebben juist wel een celkern, maar géén celwand en meestal geen grote vacuole."
      },
      {
        id: "bio1_v4",
        type: "invul",
        vraag: "Welk gas nemen planten op uit de lucht voor het proces van fotosynthese?",
        antwoord: "koolstofdioxide|CO2|koolzuurgas",
        uitleg: "Planten nemen koolstofdioxide (CO2) op uit de lucht en geven zuurstof af als bijproduct van de fotosynthese."
      },
      {
        id: "bio1_v5",
        type: "open",
        vraag: "Leg kort uit wat de functie is van het celmembraan in een cel.",
        sleutelwoorden: [
          "bescherming/grens/scheiding",
          "stoffen/doorlaten/in en uit"
        ],
        minTreffers: 1,
        modelantwoord: "Het celmembraan vormt de buitenste grens van de cel en regelt welke stoffen de cel in en uit mogen gaan.",
        uitleg: "Het celmembraan is een dun vliesje dat de inhoud van de cel bijeenhoudt en selectief stoffen doorlaat."
      }
    ]
  });
})();
