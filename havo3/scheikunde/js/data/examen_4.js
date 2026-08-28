/* Proeftoets 4 — Scheikunde HAVO 3: Hoofdstuk 2 (Bouwstenen van stoffen - Deel 4)
   Focus: Paragraaf 2.4 — Atoombouw, modellen (Dalton, Thomson, Rutherford, Bohr), protonen, neutronen, elektronen en isotopen.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-scheikunde-4",
  titel: "Toets 4 — Atoombouw, Deeltjes & Isotopen",
  vak: "Scheikunde · HAVO 3 (H2)",
  icoon: "⚛️",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Welke drie subatomaire deeltjes vormen samen een <b>atoom</b>?",
      opties: [
        "Protonen, neutronen en elektronen",
        "Moleculen, ionen en fotonen",
        "Alleen protonen en elektronen",
        "Cellen, weefsels en organen"
      ],
      antwoord: 0,
      uitleg: "Atoom = kern met protonen (p⁺) en neutronen (n⁰), omringd door elektronen (e⁻) in schillen."
    },
    {
      type: "mc",
      vraag: "Wat is de elektrische lading en massa van een <b>proton</b>?",
      opties: [
        "Lading: 0, massa: 1 u",
        "Lading: +1, massa: 1 u",
        "Lading: -1, massa: 0 u",
        "Lading: +2, massa: 4 u"
      ],
      antwoord: 1,
      uitleg: "Protonen zijn positief geladen (+1) en hebben een atomaire massa van 1 u."
    },
    {
      type: "mc",
      vraag: "Wat is de elektrische lading en massa van een <b>elektron</b>?",
      opties: [
        "Lading: 0, massa: 1 u",
        "Lading: +1, massa: 1 u",
        "Lading: -1, massa: verwaarloosbaar klein (ongeveer 0 u)",
        "Lading: -2, massa: 2 u"
      ],
      antwoord: 2,
      uitleg: "Elektronen zijn negatief geladen (-1) en wegen vrijwel niets vergeleken met kerndeeltjes (1/1836 u)."
    },
    {
      type: "mc",
      vraag: "Wat is de elektrische lading en massa van een <b>neutron</b>?",
      opties: [
        "Lading: +1, massa: 0 u",
        "Lading: +1, massa: 1 u",
        "Lading: -1, massa: 0 u",
        "Lading: 0 (neutraal/ongeladen), massa: 1 u"
      ],
      antwoord: 3,
      uitleg: "Neutronen zijn elektrisch neutraal (lading 0) en hebben een massa van 1 u."
    },
    {
      type: "mc",
      vraag: "Waarom is een compleet <b>neutraal atoom</b> als geheel elektrisch ongeladen?",
      opties: [
        "Omdat het aantal positieve protonen in de kern exact gelijk is aan het aantal negatieve elektronen in de schillen",
        "Omdat alle deeltjes neutraal zijn",
        "Omdat elektronen geen lading hebben",
        "Omdat de neutronen de lading opeten"
      ],
      antwoord: 0,
      uitleg: "Aantal p⁺ = aantal e⁻ -> netto lading = 0."
    },
    {
      type: "mc",
      vraag: "Wat geeft het <b>atoomnummer (Z)</b> van een element aan?",
      opties: [
        "Het totale gewicht van het atoom in gram",
        "Het aantal protonen in de kern van het atoom (bepaalt de atoomsoort)",
        "Het aantal neutronen",
        "De plaats in de rij van Mendelejev"
      ],
      antwoord: 1,
      uitleg: "Atoomnummer = aantal protonen. Elk element heeft een uniek atoomnummer (bijv. C = 6, O = 8, Au = 79)."
    },
    {
      type: "mc",
      vraag: "Wat geeft het <b>massagetal (A)</b> van een atoom aan?",
      opties: [
        "Het aantal elektronen maal twee",
        "Alleen het aantal protonen",
        "Het totale aantal kerndeeltjes: aantal protonen + aantal neutronen (A = p + n)",
        "De dichtheid van het element"
      ],
      antwoord: 2,
      uitleg: "Massagetal A = protonen + neutronen."
    },
    {
      type: "invul",
      vraag: "Een atoom van Fluor (F) heeft atoomnummer 9 en massagetal 19. Hoeveel <b>neutronen</b> zitten er in de kern van dit fluoratoom?",
      antwoord: "10|tien",
      uitleg: "Aantal neutronen = massagetal - atoomnummer = 19 - 9 = 10 neutronen."
    },
    {
      type: "invul",
      vraag: "Een neutraal atoom van IJzer (Fe) heeft atoomnummer 26 en massagetal 56. Hoeveel <b>elektronen</b> heeft dit atoom?",
      antwoord: "26|zesentwintig",
      uitleg: "In een neutraal atoom is het aantal elektronen gelijk aan het aantal protonen (atoomnummer) = 26."
    },
    {
      type: "mc",
      vraag: "Wat zijn <b>isotopen</b>?",
      opties: [
        "Atomen die elektronen hebben verloren",
        "Atomen met hetzelfde aantal neutronen maar ander aantal protonen",
        "Moleculen met dubbele bindingen",
        "Atomen van hetzelfde element (zelfde aantal protonen) met een verschillend aantal neutronen (dus een ander massagetal)"
      ],
      antwoord: 3,
      uitleg: "Isotopen horen bij hetzelfde element (zelfde p⁺), maar verschillen in kernmassa (aantal n⁰)."
    },
    {
      type: "waaronwaar",
      vraag: "Koolstof-12 (¹²C) heeft 6 neutronen en Koolstof-14 (¹⁴C) heeft 8 neutronen in de kern.",
      antwoord: true,
      uitleg: "Waar. Koolstof heeft altijd 6 protonen. ¹²C: 12 - 6 = 6 neutronen; ¹⁴C: 14 - 6 = 8 neutronen."
    },
    {
      type: "mc",
      vraag: "Welk atoommodel stelde dat het atoom een massief, ondeelbaar massabolletje is?",
      opties: [
        "Het atoommodel van Dalton (1803)",
        "Het krentenbolmodel van Thomson",
        "Het kernmodel van Rutherford",
        "Het schillenmodel van Bohr"
      ],
      antwoord: 0,
      uitleg: "John Dalton zag atomen als massieve ondeelbare biljartballetjes per element."
    },
    {
      type: "mc",
      vraag: "Wat ontdekte Ernest Rutherford met zijn beroemde <b>goudfolie-experiment</b>?",
      opties: [
        "Dat atomen massieve harde bollen zijn",
        "Dat het atoom voor het overgrote deel uit lege ruimte bestaat, met in het centrum een minuscule, zware, positief geladen atoomkern",
        "Dat elektronen in de kern zitten",
        "Dat goud radioactief is"
      ],
      antwoord: 1,
      uitleg: "Vrijwel alle alfadeeltjes vlogen rechtdoor de folie; slechts een enkel deeltje ketste terug op de compacte positieve atoomkern."
    },
    {
      type: "waaronwaar",
      vraag: "Volgens het atoommodel van Bohr bewegen elektronen zich in vaste <b>elektronenschillen</b> (K, L, M) op specifieke afstanden rond de kern.",
      antwoord: true,
      uitleg: "Waar. De K-schil kan max 2 elektronen bevatten, de L-schil max 8, de M-schil max 18 (of 8 bij de eerste perioden)."
    },
    {
      type: "invul",
      vraag: "Hoeveel elektronen passen er maximaal in de binnenste elektronenschil (de <b>K-schil</b>)?",
      antwoord: "2|twee",
      uitleg: "De K-schil kan maximaal 2 elektronen bevatten (zoals bij waterstof 1 en helium 2)."
    },
    {
      type: "invul",
      vraag: "Hoeveel elektronen passen er maximaal in de tweede elektronenschil (de <b>L-schil</b>)?",
      antwoord: "8|acht",
      uitleg: "De L-schil biedt plaats aan maximaal 8 elektronen (bijv. neon heeft verdeling 2, 8)."
    },
    {
      type: "mc",
      vraag: "Een chlooratoom (Cl, atoomnummer 17) heeft 17 elektronen. Wat is de <b>elektronenverdeling</b> over de schillen (K, L, M)?",
      opties: [
        "2, 10, 5",
        "2, 7, 8",
        "2, 8, 7",
        "8, 8, 1"
      ],
      antwoord: 2,
      uitleg: "K-schil: 2, L-schil: 8, M-schil: 17 - 10 = 7 elektronen -> verdeling (2, 8, 7)."
    },
    {
      type: "waaronwaar",
      vraag: "De atoommassa van een element in het periodiek systeem (zoals Cl = 35,45 u) is een gewogen gemiddelde van de massa's van de natuurlijk voorkomende isotopen.",
      antwoord: true,
      uitleg: "Waar. Chloor bestaat uit ca. 75% Chloor-35 en 25% Chloor-37, wat een gemiddelde van 35,45 u oplevert."
    },
    {
      type: "open",
      vraag: "Geef voor een atoom van Fosfor-31 (³¹₁₅P) het aantal: 1) protonen, 2) neutronen, 3) elektronen, 4) de elektronenverdeling over de schillen (K, L, M).",
      sleutelwoorden: ["15 protonen", "16 neutronen", "15 elektronen", "elektronenverdeling: 2, 8, 5"],
      minTreffers: 3,
      modelantwoord: "Voor Fosfor-31 (³¹₁₅P): 1. Aantal protonen = atoomnummer = 15, 2. Aantal neutronen = massagetal - atoomnummer = 31 - 15 = 16, 3. Aantal elektronen = aantal protonen = 15, 4. Elektronenverdeling: K-schil: 2, L-schil: 8, M-schil: 5 (notatie: 2, 8, 5).",
      uitleg: "Bepaling van kernsamenstelling en schillenverdeling."
    },
    {
      type: "open",
      vraag: "Beschrijf in grote lijnen de historische ontwikkeling van het atoommodel van <b>Dalton</b> via <b>Thomson</b> en <b>Rutherford</b> naar <b>Bohr</b>.",
      sleutelwoorden: ["Dalton: massieve ondeelbare bol", "Thomson: krentenbol met elektronen", "Rutherford: kleine positieve kern + lege ruimte", "Bohr: elektronen in schillen"],
      minTreffers: 3,
      modelantwoord: "1. Dalton (1803): Het atoom is een massief en ondeelbaar bolletje per element. 2. Thomson (1897): Ontdekte het elektron; het atoom is een positieve bol waarin negatieve elektronen zitten als krenten in een krentenbol. 3. Rutherford (1911): Ontdekte via goudfolie dat het atoom grotendeels leeg is, met een extreem kleine, zware positieve atoomkern en elektronen eromheen. 4. Bohr (1913): Verfijnde dit door aan te tonen dat elektronen in vaste schillen (K, L, M) om de kern draaien.",
      uitleg: "De 4 klassieke atoommodellen in chronologische volgorde."
    }
  ]
});
