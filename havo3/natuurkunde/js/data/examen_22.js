/* Proeftoets 22 — Natuurkunde HAVO 3: Hoofdstuk 8 (Krachten gebruiken - Deel 2)
   Focus: Paragraaf 8.2 — Rekenen aan hefbomen, de momentenwet met meerdere krachten, zwaartepunt en evenwicht.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-22",
  titel: "Toets 22 — Rekenen aan Hefbomen & Momenten",
  vak: "Natuurkunde · HAVO 3 (H8)",
  icoon: "⚖️",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Een kracht van 85 N werkt op een arm van 0,40 m van het draaipunt. Hoe groot is het moment van deze kracht?",
      opties: [
        "34 Nm",
        "212,5 Nm",
        "85,4 Nm",
        "21,25 Nm"
      ],
      antwoord: 0,
      uitleg: "M = F × r = 85 N × 0,40 m = 34 Nm."
    },
    {
      type: "invul",
      vraag: "Een moer moet worden vastgedraaid met een moment van 120 Nm. De monteur gebruikt een momentsleutel met een arm van 0,50 m. Welke spierkracht in Newton moet de monteur uitoefenen?",
      antwoord: "240|240 N",
      uitleg: "F = M / r = 120 Nm / 0,50 m = 240 N."
    },
    {
      type: "mc",
      vraag: "Op een hefboom werken aan de linkerkant twee krachten: F₁ = 10 N op r₁ = 0,20 m en F₂ = 20 N op r₂ = 0,50 m. Hoe groot is het totale moment linksom?",
      opties: [
        "15 Nm",
        "12 Nm",
        "6 Nm",
        "30 Nm"
      ],
      antwoord: 1,
      uitleg: "M_totaal = (10 × 0,20) + (20 × 0,50) = 2 + 10 = 12 Nm."
    },
    {
      type: "invul",
      vraag: "Om de hefboom uit de vorige vraag ({\text{links}} = 12\text{ Nm}$) in evenwicht te brengen, wordt rechts één gewichtje geplaatst op een afstand van 0,30 m van het draaipunt. Hoe groot moet de zwaartekracht op dit gewichtje zijn in Newton?",
      antwoord: "40|40 N",
      uitleg: "F_rechts = M_links / r_rechts = 12 Nm / 0,30 m = 40 N."
    },
    {
      type: "waaronwaar",
      vraag: "Als een voorwerp in rust is en niet draait, is de som van alle linksdraaiende momenten exact gelijk aan de som van alle rechtsdraaiende momenten.",
      antwoord: true,
      uitleg: "Waar. Dit is de momentenwet voor statisch evenwicht."
    },
    {
      type: "mc",
      vraag: "Een hijskraan heeft een contragewicht van 50.000 N op een afstand van 8,0 m van de draaias. Hoeveel last in Newton kan de kraan maximaal dragen op een giek van 25 m afstand?",
      opties: [
        "25.000 N",
        "400.000 N",
        "16.000 N",
        "156.250 N"
      ],
      antwoord: 2,
      uitleg: "M_contra = 50.000 N × 8,0 m = 400.000 Nm. F_last = 400.000 Nm / 25 m = 16.000 N."
    },
    {
      type: "invul",
      vraag: "Wat is de massa in kg van de maximale last van 16.000 N uit de vorige vraag (neem  = 9{,}8\text{ N/kg}$ of 0\text{ N/kg}$, reken met  = 10\text{ N/kg}$)?",
      antwoord: "1600|1600 kg|1.600|1.600 kg",
      uitleg: "m = F_z / g = 16.000 N / 10 N/kg = 1.600 kg (of 1633 kg bij g=9,8)."
    },
    {
      type: "mc",
      vraag: "Wat is het <b>zwaartepunt (Z)</b> van een voorwerp?",
      opties: [
        "Het geometrische middelpunt van een cirkel",
        "Het zwaarste deel van het voorwerp",
        "Het punt dat altijd op de grond rust",
        "Het aangrijpingspunt waar je de totale zwaartekracht op het voorwerp geconcentreerd kunt denken"
      ],
      antwoord: 3,
      uitleg: "In het zwaartepunt Z grijpt de zwaartekracht F_z aan."
    },
    {
      type: "waaronwaar",
      vraag: "Een hefboom is stabiel in evenwicht als het zwaartepunt zich recht BOVEN het draaipunt bevindt.",
      antwoord: false,
      uitleg: "Niet waar. Als het zwaartepunt boven het draaipunt ligt is het evenwicht labiel (wankel); het zwaartepunt moet juist recht ONDER het draaipunt liggen voor stabiel evenwicht.",
      uitleg: "Waar. Als het zwaartepunt onder het ophangpunt ligt, keert het bij verstoring vanzelf terug naar evenwicht (stabiel evenwicht)."
    },
    {
      type: "invul",
      vraag: "Een vlaggenmast van 6,0 m lengte heeft een gewicht van 600 N. Het zwaartepunt ligt in het midden van de mast (op 3,0 m van het scharnierpunt aan de voet). Welk moment oefent de zwaartekracht uit om de mast omlaag te laten draaien als hij horizontaal ligt?",
      antwoord: "1800|1800 Nm|1.800|1.800 Nm",
      uitleg: "M = F_z × r = 600 N × 3,0 m = 1.800 Nm."
    },
    {
      type: "mc",
      vraag: "Twee kinderen zitten op een wip. Daan weegt 30 kg en zit op 2,0 m van het draaipunt. Sophie weegt 40 kg. Op welke afstand van het draaipunt moet Sophie gaan zitten voor evenwicht? (neem g = 10 N/kg)",
      opties: [
        "1,5 m",
        "1,2 m",
        "2,67 m",
        "1,8 m"
      ],
      antwoord: 0,
      uitleg: "M_Daan = (30 × 10) × 2,0 = 600 Nm. r_Sophie = 600 Nm / (40 × 10) = 600 / 400 = 1,5 m."
    },
    {
      type: "waaronwaar",
      vraag: "Als een kracht schuin werkt op een hefboom (hoek kleiner dan 90°), is de arm $ korter dan de afstand langs de hefboom van draaipunt tot aangrijpingspunt.",
      antwoord: true,
      uitleg: "Waar. Omdat de loodrechte afstand altijd korter is dan de schuine zijde van de driehoek (r = l × sin(alpha))."
    },
    {
      type: "invul",
      vraag: "Een kruiwagen bevat 90 kg zand ( = 900\text{ N}$). De last bevindt zich op een arm van 40 cm van het voorwiel (draaipunt). De handvatten zitten op 120 cm van het voorwiel. Welke opwaartse tilkracht in Newton moet je uitoefenen op de handvatten om de kruiwagen op te tillen?",
      antwoord: "300|300 N",
      uitleg: "F_spier × 120 cm = 900 N × 40 cm = 36.000 -> F_spier = 36.000 / 120 = 300 N."
    },
    {
      type: "mc",
      vraag: "Wat is het voordeel van de kruiwagen uit de vorige vraag?",
      opties: [
        "Je hoeft helemaal geen kracht te zetten",
        "Je tilt met slechts 300 N spierkracht een last van 900 N op (krachtvergroting van factor 3)",
        "De kruiwagen rijdt vanzelf",
        "De afstand die je armen afleggen wordt kleiner"
      ],
      antwoord: 1,
      uitleg: "Factor = 900 N / 300 N = 3. De spierkracht is 3× kleiner dan de last."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een kracht van 50 N loodrecht op een arm van 20 cm uitoefent, is het moment 0\text{ Nm}$.",
      antwoord: true,
      uitleg: "Waar. 20 cm = 0,20 m. M = 50 N × 0,20 m = 10 Nm."
    },
    {
      type: "invul",
      vraag: "Een pedaal van een fiets heeft een arm van 17 cm (0,17 m). Een fietser trapt met een neerwaartse kracht van 400 N op het pedaal op het moment dat de crank horizontaal staat. Hoe groot is het uitgeoefende moment in Nm?",
      antwoord: "68|68 Nm",
      uitleg: "M = 400 N × 0,17 m = 68 Nm."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met het moment op het fietspedaal als de crank in de hoogste verticale stand staat (bovenste dode punt) en de fietser recht naar beneden trapt?",
      opties: [
        "Het moment is negatief",
        "Het moment is maximaal",
        "Het moment is 0 Nm, omdat de werklijn van de kracht recht door de as (draaipunt) gaat",
        "Het pedaal breekt af"
      ],
      antwoord: 2,
      uitleg: "In de bovenste stand loopt de werklijn door de as -> arm r = 0 m -> M = 0 Nm."
    },
    {
      type: "waaronwaar",
      vraag: "Een balans of weegschaal met twee gelijke armen werkt op basis van de hefboomwet ( \times r = F_2 \times r \implies F_1 = F_2$).",
      antwoord: true,
      uitleg: "Waar. Omdat de armen gelijk zijn, moeten de gewichten aan beide zijden precies gelijk zijn voor evenwicht."
    },
    {
      type: "open",
      vraag: "Een liniaal van 100 cm ligt uitgebalanceerd op een draaipunt in het midden bij 50 cm. Links hangt bij 20 cm (arm 30 cm) een massa van 200 gram. Rechts hangt bij 70 cm (arm 20 cm) een massa van 150 gram. Toon met een berekening aan of de liniaal in evenwicht is, of naar welke kant hij zal kantelen. (neem g = 10 N/kg)",
      sleutelwoorden: ["0,6/0,60/60", "0,3/0,30/30", "links/kantelt links"],
      minTreffers: 2,
      modelantwoord: "Berekening links: - Massa links: m₁ = 0,20 kg -> F₁ = 2,0 N; arm r₁ = 50 - 20 = 30 cm = 0,30 m. - Moment linksom: M_links = 2,0 N × 0,30 m = 0,60 Nm. Berekening rechts: - Massa rechts: m₂ = 0,15 kg -> F₂ = 1,5 N; arm r₂ = 70 - 50 = 20 cm = 0,20 m. - Moment rechtsom: M_rechts = 1,5 N × 0,20 m = 0,30 Nm. Conclusie: M_links (0,60 Nm) > M_rechts (0,30 Nm), dus de liniaal is niet in evenwicht en zal naar links kantelen.",
      uitleg: "Vergelijking van links- en rechtsdraaiende momenten."
    },
    {
      type: "open",
      vraag: "Leg uit waarom een torenkraan op een bouwplaats zware betonnen contragewichten aan de achterkant heeft en waarom deze gewichten soms verder naar achteren of voren worden geschoven.",
      sleutelwoorden: ["tegenmoment/tegengesteld moment", "evenwicht/omvallen", "contragewicht"],
      minTreffers: 2,
      modelantwoord: "De contragewichten leveren een tegenmoment aan de achterkant van de kraan om het moment van de gehesen last (aan de voorkant) te compenseren. Hierdoor blijft de totale som van de momenten in balans en kantelt of bezwijkt de kraan niet. Wanneer een zwaardere last of een last op grotere afstand van de mast wordt gehesen, kan het contragewicht naar achteren worden verplaatst om de arm te vergroten, zodat het tegenmoment precies overeenkomt met de belasting.",
      uitleg: "Stabiliteit en momentenbalans bij torenkranen."
    }
  ]
});
