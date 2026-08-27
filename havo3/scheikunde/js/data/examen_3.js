/* Proeftoets 3 — Scheikunde HAVO 3: Hoofdstuk 2 (Bouwstenen van stoffen - Deel 3)
   Focus: Paragraaf 2.3 — Formuletaal, indices, coëfficiënten, systematische naamgeving en triviale namen.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-scheikunde-3",
  titel: "Toets 3 — Chemische Formuletaal & Naamgeving",
  vak: "Scheikunde · HAVO 3 (H2)",
  icoon: "📝",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat geeft de <b>index</b> (het kleine verlaagde cijfer) in een molecuulformule aan (zoals de 2 in H₂O)?",
      opties: [
        "Het aantal atomen van die atoomsoort in één enkel molecuul",
        "Het aantal losse moleculen in het bekerglas",
        "De temperatuur van de stof",
        "Het atoomnummer in het periodiek systeem"
      ],
      antwoord: 0,
      uitleg: "De index staat rechtsonder het symbool en geeft aan hoeveel atomen van die soort in het molecuul zitten."
    },
    {
      type: "mc",
      vraag: "Wat geeft de <b>coëfficiënt</b> (het grote getal vóór de formule) aan (zoals de 3 in 3 H₂O)?",
      opties: [
        "Het aantal losse moleculen van die stof",
        "Het aantal protonen in de kern",
        "De massa van één atoom",
        "Het aantal schillen"
      ],
      antwoord: 0,
      uitleg: "Een coëfficiënt vóór de formule telt het aantal hele moleculen (3 H₂O betekent 3 losse watermoleculen)."
    },
    {
      type: "invul",
      vraag: "Hoeveel waterstofatomen (H) zitten er in totaal in <b>4 moleculen methaan (4 CH₄)</b>?",
      antwoord: "16|zestien",
      uitleg: "4 moleculen × 4 H-atomen per molecuul = 16 H-atomen."
    },
    {
      type: "invul",
      vraag: "Hoeveel zuurstofatomen (O) zitten er in totaal in <b>3 moleculen koolstofdioxide (3 CO₂)</b>?",
      antwoord: "6|zes",
      uitleg: "3 moleculen × 2 O-atomen = 6 zuurstofatomen."
    },
    {
      type: "mc",
      vraag: "Welk Grieks voorvoegsel hoort bij het getal <b>4</b> in de systematische naamgeving van niet-metaalverbindingen?",
      opties: [
        "tetra",
        "tri",
        "penta",
        "hexa"
      ],
      antwoord: 0,
      uitleg: "1 = mono, 2 = di, 3 = tri, 4 = tetra, 5 = penta, 6 = hexa."
    },
    {
      type: "invul",
      vraag: "Wat is de systematische naam voor de stof met formule <b>CO</b> (bestaande uit 1 koolstofatoom en 1 zuurstofatoom)?",
      antwoord: "koolstofmonoxide|koolstofmono-oxide|koolstof monoxide",
      uitleg: "CO = koolstofmonoxide (het gevaarlijke reukloze en giftige gas bij onvolledige verbranding)."
    },
    {
      type: "invul",
      vraag: "Wat is de systematische naam voor de stof met formule <b>SO₃</b>?",
      antwoord: "zwaveltrioxide|zwavel trioxide",
      uitleg: "S = zwavel, O₃ = trioxide -> zwaveltrioxide."
    },
    {
      type: "mc",
      vraag: "Wat is de molecuulformule van <b>distikstoftetraoxide</b>?",
      opties: [
        "N₂O₄",
        "NO₂",
        "N₄O₂",
        "2 NO"
      ],
      antwoord: 0,
      uitleg: "di-stikstof = N₂, tetra-oxide = O₄ -> N₂O₄."
    },
    {
      type: "invul",
      vraag: "Wat is de molecuulformule van <b>koolstoftetrachloride</b> (tetra = 4)?",
      antwoord: "CCl4|CCl₄",
      uitleg: "C = koolstof, Cl₄ = tetrachloride -> CCl₄."
    },
    {
      type: "mc",
      vraag: "Wat is de <b>triviale naam</b> (alledaagse naam) van de stof met formule <b>CH₄</b>?",
      opties: [
        "Methaan (aardgas)",
        "Ammoniak",
        "Glucose",
        "Koolstofdioxide"
      ],
      antwoord: 0,
      uitleg: "CH₄ heet triviaal methaan (het hoofdbestanddeel van aardgas)."
    },
    {
      type: "invul",
      vraag: "Wat is de formule van <b>ammoniak</b> (een scherp ruikend gas bestaande uit 1 stikstofatoom en 3 waterstofatomen)?",
      antwoord: "NH3|NH₃",
      uitleg: "Ammoniak = NH₃."
    },
    {
      type: "invul",
      vraag: "Wat is de molecuulformule van <b>glucose</b> (druivensuiker, bestaande uit 6 koolstof-, 12 waterstof- en 6 zuurstofatomen)?",
      antwoord: "C6H12O6|C₆H₁₂O₆",
      uitleg: "Glucose = C₆H₁₂O₆."
    },
    {
      type: "waaronwaar",
      vraag: "De formule <b>2 O₂</b> betekent 2 losse zuurstofmoleculen, die samen bestaan uit in totaal 4 zuurstofatomen.",
      antwoord: true,
      uitleg: "Waar. 2 × 2 = 4 atomen."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil in betekenis tussen <b>2 N</b> en <b>N₂</b>?",
      opties: [
        "2 N betekent twee losse stikstofatomen; N₂ betekent één stikstofmolecuul waarin twee stikstofatomen aan elkaar gebonden zijn",
        "2 N is een vloeistof, N₂ is een gas",
        "Er is geen verschil",
        "2 N betekent 2 moleculen stikstofgas"
      ],
      antwoord: 0,
      uitleg: "Coëfficiënt 2 = losse atomen; index 2 = chemisch aan elkaar gebonden in een molecuul."
    },
    {
      type: "invul",
      vraag: "Wat is de systematische naam voor <b>P₂O₅</b> (di = 2, penta = 5)?",
      antwoord: "difosforpentaoxide|difosforpentoxide|difosfor pentaoxide",
      uitleg: "P₂ = difosfor, O₅ = pentaoxide -> difosforpentaoxide."
    },
    {
      type: "waaronwaar",
      vraag: "Als er in een formule géén index bij een symbool staat (zoals bij C in CO₂), betekent dit dat er precies <b>1 atoom</b> van die soort in het molecuul zit.",
      antwoord: true,
      uitleg: "Waar. Index 1 wordt in de scheikunde nooit opgeschreven."
    },
    {
      type: "mc",
      vraag: "Wat is de formule van <b>waterstofchloride</b> (zoutzuurgas)?",
      opties: [
        "HCl",
        "H₂Cl",
        "HCl₂",
        "H₂O"
      ],
      antwoord: 0,
      uitleg: "Waterstofchloride = HCl."
    },
    {
      type: "invul",
      vraag: "Wat is de systematische naam voor de stof <b>NO₂</b>?",
      antwoord: "stikstofdioxide|stikstof dioxide",
      uitleg: "N = stikstof, O₂ = dioxide -> stikstofdioxide."
    },
    {
      type: "open",
      vraag: "Geef de systematische namen van de volgende drie stoffen: 1) SO₂, 2) N₂O, 3) SF₆.",
      sleutelwoorden: ["1) zwaveldioxide", "2) distikstofmonoxide / distikstofmono-oxide", "3) zwavelhexafluoride"],
      minTreffers: 3,
      modelantwoord: "1. SO₂ = zwaveldioxide, 2. N₂O = distikstofmonoxide (ook bekend als lachgas), 3. SF₆ = zwavelhexafluoride.",
      uitleg: "Systematische naamgeving met Griekse voorvoegsels."
    },
    {
      type: "open",
      vraag: "Bekijk de formule 3 C₂H₆O (drie moleculen ethanol/alcohol). Bepaal van elke atoomsoort hoeveel atomen er in totaal aanwezig zijn.",
      sleutelwoorden: ["koolstof / C: 6 atomen", "waterstof / H: 18 atomen", "zuurstof / O: 3 atomen"],
      minTreffers: 3,
      modelantwoord: "In 3 C₂H₆O: Koolstofatomen (C): 3 × 2 = 6 atomen; Waterstofatomen (H): 3 × 6 = 18 atomen; Zuurstofatomen (O): 3 × 1 = 3 atomen.",
      uitleg: "Coëfficiënt vermenigvuldigen met de index van elke atoomsoort."
    }
  ]
});
