/* Onderwerp 2.5 — Elektromagnetisme */
DURU.register({
  id: "h2-5-elektromagnetisme",
  hoofdstuk: 2,
  paragraaf: "2.5",
  titel: "Elektromagnetisme & Inductie",
  korteUitleg: "Elektromagneten, dynamo's, generatoren, transformatoren en inductiespanning.",
  icoon: "🧲",
  kleur: "h2-thema",
  theorie: "<h3>2.5 Elektromagnetisme</h3><div class=\"formule-box\"><strong>Kernconcepten:</strong><br>• <b>Elektromagneet:</b> Stroom door een spoel wekt een magnetisch veld op. Versterken via: 1) meer windingen, 2) grotere stroom $I$, 3) weekijzeren kern.<br>• <b>Inductie:</b> Beweging van een magneet t.o.v. een spoel wekt spanning op (dynamo / generator).<br>• <b>Transformator:</b> Verhoogt of verlaagt wisselspanning (hoogspanningstransport voorkomt energieverlies).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat ontstaat er rondom een stroomvoerende draad?",
      opties: ["Een magnetisch veld", "Zwaartekracht", "Licht", "Geen veld"],
      antwoord: 0,
      uitleg: "Stroom wekt altijd een magnetisch veld op."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Hoe kun je een elektromagneet sterker maken?",
      opties: ["Minder windingen maken", "Een weekijzeren kern toevoegen en meer stroom laten lopen", "De spoel van rubber maken", "De magneet uitschakelen"],
      antwoord: 1,
      uitleg: "IJzeren kern, meer windingen en hogere stroom versterken het magnetisch veld."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een dynamo wekt spanning op door een magneet en een spoel ten opzichte van elkaar te laten bewegen.",
      antwoord: true,
      uitleg: "Waar: dit verschijnsel heet elektromagnetische inductie."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Waarom werkt een transformator alleen op wisselspanning?",
      opties: ["Omdat gelijkspanning te heet is", "Omdat batterijen te zwaar zijn", "Omdat er een veranderend magnetisch veld nodig is voor inductie", "Omdat wisselspanning geen weerstand heeft"],
      antwoord: 2,
      uitleg: "Alleen wisselstroom zorgt voor een voortdurend veranderend magnetisch veld dat inductiespanning wekt in de secundaire spoel."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Elektriciteitstransport via hoogspanningslijnen vermindert energieverlies omdat de stroomsterkte I dan veel kleiner is.",
      antwoord: true,
      uitleg: "Waar: bij hoge spanning is I lager, waardoor kabelweerstandsverlies (I²·R) sterk afneemt."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Een dynamo wekt 6 V op en voedt een fietslamp van 3 W. Hoeveel Ampère stroom levert de dynamo?",
      antwoord: "0,5|0,5 A|0,50",
      uitleg: "I = P / U = 3 W / 6 V = 0,5 A."
    }
  ]
});
