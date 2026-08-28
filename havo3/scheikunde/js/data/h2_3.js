/* Onderwerp 2.3 — Formuletaal en naamgeving */
DURU.register({
  id: "sch-h2-3-formuletaal",
  hoofdstuk: 2,
  paragraaf: "2.3",
  titel: "Chemische Formuletaal & Naamgeving",
  korteUitleg: "Indices, coëfficiënten, Griekse voorvoegsels (mono, di, tri, tetra) en triviale namen.",
  icoon: "📝",
  kleur: "h2-thema",
  theorie: "<h3>2.3 Formuletaal en naamgeving</h3><div class='formule-box'><strong>Index vs. Coëfficiënt:</strong><br>In 3 H₂O:<br>• <b>Coëfficiënt (3):</b> Er zijn 3 losse watermoleculen.<br>• <b>Index (2):</b> Elk watermolecuul bevat 2 H-atomen en 1 O-atoom (totaal 3 × 2 = 6 H en 3 × 1 = 3 O).<br><br><strong>Griekse voorvoegsels:</strong><br>1 = mono, 2 = di, 3 = tri, 4 = tetra, 5 = penta, 6 = hexa.</div><h4>Triviale namen</h4><ul><li>H₂O = water &nbsp;|&nbsp; CH₄ = methaan (aardgas) &nbsp;|&nbsp; NH₃ = ammoniak &nbsp;|&nbsp; C₆H₁₂O₆ = glucose</li></ul>",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat geeft de index 2 aan in CO₂?",
      opties: ["Dat er 2 zuurstofatomen in 1 molecuul zitten", "Dat er 2 moleculen zijn", "Dat het molecuul 2 gram weegt", "Het atoomnummer"],
      antwoord: 0,
      uitleg: "Index = aantal atomen van die soort in het molecuul."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Hoeveel waterstofatomen (H) zitten er in totaal in 3 CH₄ (3 moleculen methaan)?",
      antwoord: "12|twaalf",
      uitleg: "3 moleculen × 4 H-atomen = 12 H-atomen."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Wat is de systematische naam van CO (1 koolstofatoom en 1 zuurstofatoom)?",
      antwoord: "koolstofmonoxide|koolstofmono-oxide|koolstof monoxide",
      uitleg: "CO = koolstofmonoxide."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welk voorvoegsel hoort bij het getal 4?",
      opties: ["tri", "tetra", "penta", "di"],
      antwoord: 1,
      uitleg: "4 = tetra (bijv. CCl₄ = koolstoftetrachloride)."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Wat is de molecuulformule van ammoniak?",
      antwoord: "NH3|NH₃",
      uitleg: "Ammoniak = NH₃."
    },
    {
      type: "waaronwaar",
      niveau: 3,
      vraag: "In 2 C₆H₁₂O₆ zitten in totaal 24 waterstofatomen (H).",
      antwoord: true,
      uitleg: "Waar: 2 × 12 = 24 H-atomen."
    }
  ]
});
