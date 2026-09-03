/* =========================================================
   Duru's Scheikunde (HAVO 3) — Toets 2 — Dichtheid & Eenheden Omrekenen
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-sch-h1-2",
  "hoofdstuk": 1,
  "titel": "Toets 2 — Dichtheid Berekenen & Eenheden Omrekenen",
  "vak": "Scheikunde · HAVO 3 (H1.1)",
  "icoon": "⚖️",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de wiskundige formule om de <b>dichtheid (ρ)</b> van een voorwerp te berekenen?",
      "opties": [
        "dichtheid = massa / volume (ρ = m / V)",
        "dichtheid = massa × volume (ρ = m × V)",
        "dichtheid = volume / massa (ρ = V / m)",
        "dichtheid = massa + volume (ρ = m + V)"
      ],
      "antwoord": 0,
      "uitleg": "Dichtheid is de massa per volume-eenheid: ρ = m / V."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je de <b>massa (m)</b> als je de dichtheid en het volume kent?",
      "opties": [
        "massa = dichtheid / volume (m = ρ / V)",
        "massa = dichtheid × volume (m = ρ × V)",
        "massa = volume / dichtheid (m = V / ρ)",
        "massa = dichtheid + volume"
      ],
      "antwoord": 1,
      "uitleg": "Uit ρ = m / V volgt door kruislings vermenigvuldigen: m = ρ × V."
    },
    {
      "type": "mc",
      "vraag": "Hoe bereken je het <b>volume (V)</b> als je de massa en de dichtheid kent?",
      "opties": [
        "volume = massa × dichtheid (V = m × ρ)",
        "volume = dichtheid / massa (V = ρ / m)",
        "volume = massa / dichtheid (V = m / ρ)",
        "volume = massa - dichtheid"
      ],
      "antwoord": 2,
      "uitleg": "Uit ρ = m / V volgt: V = m / ρ."
    },
    {
      "type": "mc",
      "vraag": "Welke twee eenheden van dichtheid hebben in getalwaarde <b>exact dezelfde waarde</b>?",
      "opties": [
        "g/cm³ en kg/m³",
        "kg/L en kg/m³",
        "mg/L en g/cm³",
        "g/cm³ en kg/dm³ (of kg/L)"
      ],
      "antwoord": 3,
      "uitleg": "Omdat 1 kg = 1000 g en 1 dm³ = 1000 cm³, is 1 kg/dm³ exact gelijk aan 1 g/cm³."
    },
    {
      "type": "invul",
      "vraag": "Een blok hout heeft een massa van 156 kg en een volume van 0,200 m³. Bereken de dichtheid in kg/m³.",
      "antwoord": "780|780 kg/m3|780 kg/m^3",
      "uitleg": "Dichtheid = massa / volume = 156 kg / 0,200 m³ = 780 kg/m³."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel gram (g) is gelijk aan 0,00571 kilogram (kg)?",
      "antwoord": "5,71|5.71|5,71 g|5.71 g",
      "uitleg": "0,00571 kg × 1000 = 5,71 gram."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel kubieke centimeter (cm³) is gelijk aan 0,094 liter (L)?",
      "antwoord": "94|94 cm3|94 cm^3",
      "uitleg": "1 liter = 1000 mL = 1000 cm³. Dus 0,094 L × 1000 = 94 cm³."
    },
    {
      "type": "mc",
      "vraag": "Het metaal osmium heeft een zeer grote dichtheid van 22,6 g/cm³. Wat weegt een klein blokje osmium met een volume van 15,0 cm³?",
      "opties": [
        "339 g",
        "1,51 g",
        "0,66 g",
        "226 g"
      ],
      "antwoord": 0,
      "uitleg": "Massa = dichtheid × volume = 22,6 g/cm³ × 15,0 cm³ = 339 gram."
    },
    {
      "type": "mc",
      "vraag": "Lithium is het lichtste metaal met een dichtheid van 0,53 g/cm³. Wat is het volume van 5,0 gram lithium?",
      "opties": [
        "2,65 cm³",
        "9,4 cm³",
        "0,11 cm³",
        "5,3 cm³"
      ],
      "antwoord": 1,
      "uitleg": "Volume = massa / dichtheid = 5,0 g / 0,53 g/cm³ ≈ 9,4 cm³."
    },
    {
      "type": "mc",
      "vraag": "Zuiver water heeft bij kamertemperatuur een dichtheid van 1,00 g/cm³ (1000 kg/m³). Een onbekende vloeistof heeft een dichtheid van 0,85 g/cm³ en mengt niet met water. Wat gebeurt er als je deze twee vloeistoffen bij elkaar giet?",
      "opties": [
        "De onbekende vloeistof zinkt direct naar de bodem",
        "De twee vloeistoffen lossen direct volledig in elkaar op",
        "De onbekende vloeistof gaat drijven als een bovenste laag op het water",
        "Het water verdwijnt onmiddellijk in damp"
      ],
      "antwoord": 2,
      "uitleg": "De vloeistof met de laagste dichtheid (0,85 g/cm³) blijft drijven op de vloeistof met de hogere dichtheid (water: 1,00 g/cm³)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kilogram veren is lichter dan een kilogram lood.",
      "antwoord": false,
      "uitleg": "Niet waar: een kilogram is een maat voor massa. Beide hebben exact dezelfde massa (1 kg). Wel heeft lood een veel grotere dichtheid dan veren."
    },
    {
      "type": "mc",
      "vraag": "In stripverhalen lopen de boeven vaak vrolijk weg met een grote plunjebaal vol massief gouden munten (volume ca. 30 liter). De dichtheid van goud is 19,3 kg/dm³. Waarom kan dit in werkelijkheid niet?",
      "opties": [
        "Omdat goud vloeibaar is bij kamertemperatuur",
        "Omdat gouden munten direct oplossen in een stoffen zak",
        "Omdat goud een kleinere dichtheid heeft dan lucht",
        "Omdat 30 liter massief goud een massa heeft van 30 × 19,3 = 579 kg, wat een mens onmogelijk kan dragen"
      ],
      "antwoord": 3,
      "uitleg": "Massa = ρ × V = 19,3 kg/dm³ × 30 dm³ = 579 kg. Dit is ruim een halve ton en onmogelijk op te tillen."
    },
    {
      "type": "invul",
      "vraag": "Hoeveel liter (L) is 2500 milliliter (mL)?",
      "antwoord": "2,5|2.5|2,5 L|2.5 L|2,5 liter|2.5 liter",
      "uitleg": "2500 mL / 1000 = 2,5 liter."
    },
    {
      "type": "mc",
      "vraag": "Wat was in 1983 de hoofdoorzaak van het beroemde 'Gimli Glider' incident van Air Canada (Boeing 767)?",
      "opties": [
        "Een ernstige omrekenfout tussen ponden (pounds/L) en kilogrammen (kg/L) bij de dichtheid van kerosine, waardoor er veel te weinig brandstof werd getankt",
        "De motor was ontploft door een chemische reactie",
        "De piloten hadden water getankt in plaats van kerosine",
        "De brandstoftanks waren lek gestoten door een vogel"
      ],
      "antwoord": 0,
      "uitleg": "Het grondpersoneel gebruikte een dichtheid in pounds/L (1,77) in plaats van kg/L (0,80), waardoor het vliegtuig met slechts 20.400 pounds i.p.v. 20.400 kg opsteeg."
    },
    {
      "type": "mc",
      "vraag": "Een diamant heeft een massa van 5,0 karaat (waarbij 1 karaat = 0,200 g). De dichtheid van diamant is 3,51 g/cm³. Wat is het volume van deze diamant?",
      "opties": [
        "3,51 cm³",
        "0,285 cm³",
        "1,755 cm³",
        "0,057 cm³"
      ],
      "antwoord": 1,
      "uitleg": "Massa = 5,0 × 0,200 g = 1,00 g. Volume = m / ρ = 1,00 g / 3,51 g/cm³ ≈ 0,285 cm³."
    },
    {
      "type": "waaronwaar",
      "vraag": "1 kubieke meter (1 m³) is gelijk aan 1000 liter.",
      "antwoord": true,
      "uitleg": "Waar: 1 m³ = 1000 dm³ = 1000 liter."
    },
    {
      "type": "mc",
      "vraag": "Een onbekend stuk metaal heeft een volume van 50 cm³ en weegt op de weegschaal 445 gram. Van welk metaal is dit stuk gemaakt? (Dichtheden: IJzer = 7,87 g/cm³, Koper = 8,90 g/cm³, Lood = 11,3 g/cm³, Zilver = 10,5 g/cm³)",
      "opties": [
        "IJzer (ρ = 7,87 g/cm³)",
        "Lood (ρ = 11,3 g/cm³)",
        "Koper (ρ = 8,90 g/cm³)",
        "Zilver (ρ = 10,5 g/cm³)"
      ],
      "antwoord": 2,
      "uitleg": "Dichtheid = m / V = 445 g / 50 cm³ = 8,90 g/cm³. Dit komt precies overeen met koper."
    },
    {
      "type": "invul",
      "vraag": "De dichtheid van zonnebloemolie is 0,92 g/cm³. Wat is de massa (in gram) van een fles met 0,75 liter (750 cm³) olie?",
      "antwoord": "690|690 g|690 gram",
      "uitleg": "m = ρ × V = 0,92 g/cm³ × 750 cm³ = 690 gram."
    },
    {
      "type": "mc",
      "vraag": "Waarom zinkt een massieve ijzeren bout in water, terwijl een gigantisch stalen containerschip wél kan blijven drijven?",
      "opties": [
        "Omdat het staal van schepen speciaal behandeld is om lichter te zijn dan water",
        "Omdat zout water magnetisch is",
        "Omdat schepen motoren hebben die water wegdrukken",
        "Omdat het containerschip hol is en heel veel lucht bevat, waardoor de gemiddelde dichtheid van het hele schip kleiner is dan die van water"
      ],
      "antwoord": 3,
      "uitleg": "De totale (gemiddelde) dichtheid van schip + opgesloten lucht is veel lager dan 1,0 g/cm³, waardoor het schip blijft drijven."
    },
    {
      "type": "mc",
      "vraag": "Als je de dichtheid in g/cm³ wilt omrekenen naar de SI-eenheid kg/m³, wat moet je dan doen?",
      "opties": [
        "Vermenigvuldigen met 1000",
        "Delen door 1000",
        "Vermenigvuldigen met 100",
        "Het getal blijft exact hetzelfde"
      ],
      "antwoord": 0,
      "uitleg": "1 g/cm³ = 1000 kg/m³ (bv. water: 1,0 g/cm³ = 1000 kg/m³). Je moet dus met 1000 vermenigvuldigen."
    }
  ]
});
