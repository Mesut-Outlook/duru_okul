/* Proeftoets 1 — Natuurkunde HAVO 3: krachten/energie/snelheid.
   Smoke-test: 5 vragen (2 mc / 1 waaronwaar / 1 invul / 1 open). */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-1",
  titel: "Proeftoets 1 — Natuurkunde: krachten, energie & snelheid",
  vak: "Natuurkunde · HAVO 3",
  icoon: "⚛️",
  duurMin: 10,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de eenheid van <b>kracht</b>?",
      opties: [
        "Joule",
        "Newton",
        "Watt",
        "Pascal"
      ],
      antwoord: 1,
      uitleg: "Kracht wordt uitgedrukt in Newton (N). Joule is de eenheid van energie, Watt van vermogen en Pascal van druk."
    },
    {
      type: "mc",
      vraag: "Een auto rijdt 120 km in 2 uur. Wat is de <b>gemiddelde snelheid</b>?",
      opties: [
        "40 km/h",
        "60 km/h",
        "80 km/h",
        "100 km/h"
      ],
      antwoord: 1,
      uitleg: "Snelheid = afstand ÷ tijd = 120 km ÷ 2 uur = 60 km/h."
    },
    {
      type: "waaronwaar",
      vraag: "Energie kan worden omgezet van de ene vorm in de andere, maar niet worden vernietigd of uit het niets gemaakt (wet van behoud van energie).",
      antwoord: true,
      uitleg: "Waar. Dit is de wet van behoud van energie: de totale hoeveelheid energie in een gesloten systeem blijft gelijk, alleen de vorm kan veranderen (bijv. van bewegingsenergie naar warmte)."
    },
    {
      type: "invul",
      vraag: "De formule voor snelheid is v = s / … .",
      antwoord: "t|tijd",
      uitleg: "v = s / t, waarbij v = snelheid, s = afgelegde afstand en t = tijd."
    },
    {
      type: "open",
      vraag: "Leg uit wat er gebeurt met de energie van een vallend voorwerp, van het loslaten tot het de grond raakt. Gebruik de begrippen <b>zwaarte-energie</b> en <b>bewegingsenergie</b>.",
      sleutelwoorden: ["zwaarte-energie/potentiële energie", "bewegingsenergie/kinetische energie", "omzetten/neemt af/neemt toe"],
      minTreffers: 2,
      modelantwoord: "Bij het loslaten heeft het voorwerp veel zwaarte-energie (potentiële energie) door zijn hoogte. Terwijl het valt, neemt de zwaarte-energie af en wordt omgezet in bewegingsenergie (kinetische energie), die dus toeneemt. Vlak voor de grond is de zwaarte-energie bijna nul en de bewegingsenergie het grootst.",
      uitleg: "Kernidee: zwaarte-energie wordt tijdens het vallen omgezet in bewegingsenergie. De totale energie blijft (ongeveer) gelijk, alleen de vorm verandert."
    }
  ]
});
