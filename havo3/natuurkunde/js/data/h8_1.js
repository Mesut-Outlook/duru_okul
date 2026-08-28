/* Onderwerp 8.1 — Hefbomen */
DURU.register({
  id: "h8-1-hefbomen",
  hoofdstuk: 8,
  paragraaf: "8.1",
  titel: "Hefbomen & Draaipunten",
  korteUitleg: "Draaipunt, spierkracht, werkkracht, de arm van een kracht en soorten hefbomen.",
  icoon: "🪚",
  kleur: "h8-thema",
  theorie: "<h3>8.1 Hefbomen</h3><div class='formule-box'><strong>Begrippen:</strong><br>• <b>Draaipunt ($):</b> Het vaste punt waar de hefboom omheen draait.<br>• <b>Arm van de kracht ($):</b> De kortste (loodrechte) afstand van het draaipunt tot de werklijn van de kracht.<br>• <b>Werklijn:</b> De oneindige lijn in de richting van de uitgeoefende kracht.</div><h4>Soorten hefbomen</h4><ul><li><b>Dubbelzijdige hefboom:</b> Het draaipunt ligt tussen de twee krachten in (bijv. schaar, koevoet, wipwap).</li><li><b>Enkelzijdige hefboom:</b> Beide krachten liggen aan dezelfde kant van het draaipunt (bijv. kruiwagen, notenkraker, flesopener, pincet).</li><li><b>Krachtvergroting:</b> Als {\text{spier}} > r_{\text{werk}}$, dan is {\text{werk}} > F_{\text{spier}}$ (bijv. betonschaar).</li><li><b>Krachtverkleining:</b> Als {\text{spier}} < r_{\text{werk}}$, dan is {\text{werk}} < F_{\text{spier}}$ voor precisie (bijv. pincet).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de arm van een kracht?",
      opties: ["De loodrechte afstand van het draaipunt tot de werklijn van de kracht", "De totale lengte van de hefboom", "De afstand tussen spier en last", "De breedte"],
      antwoord: 0,
      uitleg: "De arm is de loodrechte afstand van draaipunt tot werklijn."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Hoe noem je het vaste punt waar een hefboom omheen draait?",
      antwoord: "draaipunt",
      uitleg: "Het draaipunt (D)."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welk gereedschap is een voorbeeld van een enkelzijdige hefboom?",
      opties: ["Schaar", "Kruiwagen", "Wipwap", "Koevoet"],
      antwoord: 1,
      uitleg: "Bij een kruiwagen liggen wiel (draaipunt), bak (last) en handvatten (spierkracht) aan 1 kant."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een takkenschaar heeft lange handvatten om de arm van de spierkracht te vergroten.",
      antwoord: true,
      uitleg: "Waar: grotere spierkrachtarm = veel grotere knipkracht."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Waarom gebruik je een pincet als de werkkracht kleiner is dan je spierkracht?",
      opties: ["Om zware lasten te tillen", "Om spijkers te buigen", "Om heel nauwkeurig en precies kleine dingen vast te pakken", "Omdat het niet breekt"],
      antwoord: 2,
      uitleg: "Pincet verkleint de kracht voor uiterste precisie."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Als de werklijn van een kracht precies door het draaipunt gaat, is de arm r gelijk aan 0.",
      antwoord: true,
      uitleg: "Waar: er is dan geen draaiend effect (moment = 0)."
    }
  ]
});
