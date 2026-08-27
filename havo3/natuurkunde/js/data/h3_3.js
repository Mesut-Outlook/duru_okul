/* Onderwerp 3.3 — Gevaren van straling */
DURU.register({
  id: "h3-3-gevaren-bescherming",
  hoofdstuk: 3,
  paragraaf: "3.3",
  titel: "Gevaren, Besmetting & Bescherming",
  korteUitleg: "Bestraling vs. besmetting, Sievert (Sv), achtergrondstraling en beschermingsregels.",
  icoon: "☢️",
  kleur: "h3-thema",
  theorie: "<h3>3.3 Gevaren van straling</h3><div class=\"formule-box\"><strong>Bestraling vs. Besmetting:</strong><br>• <b>Bestraling:</b> Blootstelling van buitenaf. Stopt zodra bron weg is; je wordt zelf NIET radioactief.<br>• <b>Besmetting:</b> Radioactief materiaal op de huid of in het lichaam (ingeademd/ingeslikt) blijft continu stralen.<br><br><strong>Dosis:</strong> Uitgedrukt in <b>Sievert (Sv)</b> of <b>milliSievert (mSv)</b>.<br><strong>Bescherming:</strong> 1) Afstand vergroten, 2) Tijd verkorten, 3) Afscherming (lood/beton).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is de eenheid voor de biologische stralingsdosis op het lichaam?",
      opties: ["Becquerel (Bq)", "Sievert (Sv)", "Newton (N)", "Volt (V)"],
      antwoord: 1,
      uitleg: "De effectieve dosis wordt uitgedrukt in Sievert (Sv) of millisievert (mSv)."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Na een röntgenfoto bij de tandarts ben je zelf nog urenlang radioactief.",
      antwoord: false,
      uitleg: "Niet waar: je bent alleen bestraald, niet besmet."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat zijn de 3 hoofdregels voor stralingsbescherming?",
      opties: ["Afstand vergroten, tijd verkorten, afscherming gebruiken", "Warm aankleden, rennen, water drinken", "Ramen openzetten, zout eten, slapen", "Koperen sieraden dragen"],
      antwoord: 0,
      uitleg: "Afstand, tijd en afscherming (lood/beton)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Welk radioactief edelgas komt van nature voor in de bodem en kan zich ophopen in slecht geventileerde woningen?",
      antwoord: "radon|radongas",
      uitleg: "Radongas ontstaat door natuurlijk radioactief verval in de aardkorst."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Voedsel dat met gammastraling gesteriliseerd is, is zelf niet radioactief.",
      antwoord: true,
      uitleg: "Waar: het voedsel is bestraald om bacteriën te doden, maar bevat geen radioactieve bron."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Als je de afstand tot een stralingsbron verdubbelt van 1 m naar 2 m, hoeveel keer zo klein wordt de stralingsintensiteit dan (omgekeerde kwadratenwet)?",
      antwoord: "4|4x|4 keer|vier",
      uitleg: "Intensiteit schaalt met 1/r²: bij 2× zo grote afstand wordt de straling 2² = 4 keer zo zwak."
    }
  ]
});
