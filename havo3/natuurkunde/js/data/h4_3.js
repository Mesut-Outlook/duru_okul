/* Onderwerp 4.3 — Warmtetransport en isolatie */
DURU.register({
  id: "h4-3-warmtetransport-isolatie",
  hoofdstuk: 4,
  paragraaf: "4.3",
  titel: "Warmtetransport & Isolatie",
  korteUitleg: "Geleiding, stroming, straling, warmtegeleidingscoëfficiënt (λ) en energiebesparing.",
  icoon: "🏡",
  kleur: "h4-thema",
  theorie: "<h3>4.3 Warmtetransport en isolatie</h3><div class='formule-box'><strong>Drie vormen van warmtetransport:</strong><br>1. <b>Geleiding (conductie):</b> Van atoom op atoom in vaste stoffen (metalen = goed; isolatoren = slecht).<br>2. <b>Stroming (convectie):</b> Warme vloeistof of gas stijgt op door lagere dichtheid.<br>3. <b>Straling (radiatie):</b> Infraroodstraling (werkt ook door vacuüm).<br><br><strong>Warmtegeleidingscoëfficiënt (λ):</strong><br>Lage λ = uitstekende warmte-isolator (bijv. stilstaande lucht, glaswol, EPS-schuim).</div>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Welke vorm van warmtetransport kan door het vacuüm van het heelal reizen?",
      opties: ["Geleiding", "Stroming", "Warmtestraling", "Geluid"],
      antwoord: 2,
      uitleg: "Straling heeft geen tussenstof nodig."
    },
    {
      type: "mc",
      niveau: 1,
      vraag: "Waarom stijgt warme lucht op boven een radiator?",
      opties: ["Omdat warme lucht uitzet en een lagere dichtheid krijgt", "Omdat warme lucht zwaarder is", "Omdat de zwaartekracht verdwijnt", "Door magnetisme"],
      antwoord: 0,
      uitleg: "Convectie: warme lucht zet uit -> dichtheid daalt -> stijgt op."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Stilstaande lucht is een uitstekende warmte-isolator.",
      antwoord: true,
      uitleg: "Waar: luchtmoleculen zitten ver uit elkaar en geleiden warmte heel slecht."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Wat voor waarde van de warmtegeleidingscoëfficiënt (λ) heeft een goed isolatiemateriaal?",
      opties: ["Een zo hoog mogelijke λ", "Een zo laag mogelijke λ", "Altijd exact 100", "Een negatieve λ"],
      antwoord: 1,
      uitleg: "Lage λ betekent dat er weinig warmte doorheen lekt."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "Een spiegelende laag in een thermosfles reflecteert warmtestraling terug.",
      antwoord: true,
      uitleg: "Waar: glimmende wanden houden stralingsverlies tegen."
    },
    {
      type: "invoer",
      niveau: 3,
      vraag: "Door een muur lekt 200 W warmte bij een dikte van 10 cm. Hoeveel Watt lekt er als de muur 20 cm dik wordt gemaakt (dubbele dikte)?",
      antwoord: "100|100 W|100 watt",
      uitleg: "2× zo dik -> warmtestroom gehalveerd: 200 / 2 = 100 W."
    }
  ]
});
