/* Onderwerp 3.1 — Elektromagnetische straling */
DURU.register({
  id: "h3-1-spectrum",
  hoofdstuk: 3,
  paragraaf: "3.1",
  titel: "Elektromagnetische Straling & Spectrum",
  korteUitleg: "Het elektromagnetisch spectrum: radiogolven, IR, zichtbaar licht, UV en röntgenstraling.",
  icoon: "🌈",
  kleur: "h3-thema",
  theorie: "<h3>3.1 Elektromagnetische straling</h3><div class=\"formule-box\"><strong>Het Elektromagnetisch Spectrum:</strong><br>Van lange golflengte (lage energie) naar korte golflengte (hoge energie):<br><b>Radiogolven → Microgolven → Infrarood (IR) → Zichtbaar licht (ROGGBIV) → Ultraviolet (UV) → Röntgenstraling → Gammastraling</b></div><h4>Eigenschappen van EM-straling</h4><ul><li>Alle EM-straling reist in vacuüm met de <b>lichtsnelheid</b> ($c = 300.000\\text{ km/s}$).</li><li><b>Infrarood (IR):</b> Warmtestraling uitgezonden door warme lichamen en voorwerpen.</li><li><b>UV-straling:</b> Zorgt voor vitamine D en zonnebrand; gefilterd door de ozonlaag.</li><li><b>Röntgenstraling:</b> Dringt door weke weefsels; geabsorbeerd door botten en lood (ioniserend).</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke stralingssoort heeft de langste golflengte in het spectrum?",
      opties: ["Röntgenstraling", "Radiogolven", "Gammastraling", "UV-straling"],
      antwoord: 1,
      uitleg: "Radiogolven hebben de langste golflengte en laagste frequentie."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke straling zendt het menselijk lichaam vooral uit?",
      opties: ["Ultraviolet (UV)", "Infrarood (IR)", "Röntgenstraling", "Gammastraling"],
      antwoord: 1,
      uitleg: "Lichaamswarmte wordt uitgezonden als infraroodstraling."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Alle elektromagnetische golven bewegen in vacuüm met circa 300.000 km/s.",
      antwoord: true,
      uitleg: "Waar: dit is de universele lichtsnelheid c."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Welk gas in de atmosfeer beschermt ons tegen gevaarlijke UV-C en UV-B straling van de zon?",
      antwoord: "ozon|ozonlaag|de ozonlaag",
      uitleg: "De ozonlaag absorbeert het grootste deel van de schadelijke UV-straling."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Waarom zijn botten wit op een röntgenfoto?",
      opties: ["Omdat botten zelf licht geven", "Omdat botten meer röntgenstraling absorberen/tegenhouden", "Omdat botten warmer zijn", "Omdat spieren de straling reflecteren"],
      antwoord: 1,
      uitleg: "Calcium in botten absorbeert de röntgenstralen, waardoor er een witte schaduw ontstaat."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "Röntgenstraling en gammastraling zijn vormen van ioniserende straling.",
      antwoord: true,
      uitleg: "Waar: ze bezitten genoeg energie om elektronen uit atomen te slaan en DNA te beschadigen."
    }
  ]
});
