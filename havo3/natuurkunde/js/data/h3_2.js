/* Onderwerp 3.2 — Straling uit atomen */
DURU.register({
  id: "h3-2-atoom-halveringstijd",
  hoofdstuk: 3,
  paragraaf: "3.2",
  titel: "Atoombouw, Kernstraling & Halveringstijd",
  korteUitleg: "Protonen, neutronen, isotopen, alfa/bèta/gammastraling en rekenen met halveringstijd.",
  icoon: "⚛️",
  kleur: "h3-thema",
  theorie: "<h3>3.2 Straling uit atomen</h3><div class=\"formule-box\"><strong>Kernstraling soorten:</strong><br>• <b>Alfa ($\\alpha$):</b> Heliumkernen ($2\\text{p} + 2\\text{n}$), groot ioniserend vermogen, gestopt door papier/huid.<br>• <b>Bèta ($\\beta$):</b> Snelle elektronen, matig doordringend vermogen, gestopt door aluminium.<br>• <b>Gamma ($\\gamma$):</b> Energierijke EM-golven, zeer groot doordringend vermogen, afgeremd door dik lood/beton.<br><br><strong>Halveringstijd ($t_{1/2}$):</strong><br>De tijd waarin de helft van de radioactieve kernen vervalt. Activiteit $A$ in <b>Becquerel (Bq)</b>.</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Waaruit bestaat de atoomkern?",
      opties: ["Alleen elektronen", "Protonen en neutronen", "Elektronen en protonen", "Neutronen en fotonen"],
      antwoord: 1,
      uitleg: "De kern bestaat uit positieve protonen en ongeladen neutronen."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Wat is de eenheid van radioactieve activiteit (aantal kernvervallen per seconde)?",
      antwoord: "Becquerel|Bq|becquerel",
      uitleg: "Activiteit wordt gemeten in Becquerel (Bq)."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke stralingssoort wordt al gestopt door een velletje papier?",
      opties: ["Alfastraling", "Bètastraling", "Gammastraling", "Röntgenstraling"],
      antwoord: 0,
      uitleg: "Alfastraling heeft een heel klein doordringend vermogen en wordt door papier tegengehouden."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Een bron heeft een activiteit van 400 Bq en een halveringstijd van 5 uur. Wat is de activiteit na 10 uur in Bq?",
      antwoord: "100|100 Bq|100Bq",
      uitleg: "10 uur = 2 halveringstijden: 400 -> 200 -> 100 Bq."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Je kunt de halveringstijd van een stof verkorten door deze heel heet te maken.",
      antwoord: false,
      uitleg: "Niet waar: kernverval is een spontaan proces en onafhankelijk van temperatuur of druk."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een radioactief monster heeft na 3 halveringstijden nog welk percentage van zijn oorspronkelijke instabiele kernen over?",
      antwoord: "12,5|12,5%|12.5|12.5%",
      uitleg: "100% -> 50% -> 25% -> 12,5%."
    }
  ]
});
