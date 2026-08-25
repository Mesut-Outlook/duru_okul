DURU.registerExamen({
  id: "ex-wiskunde-h2-5",
  titel: "Proeftoets 5 — Eindexamen Proeftoets Statistiek",
  vak: "Wiskunde · H2 Statistiek",
  icoon: "🏆",
  duurMin: 20,
  vragen: [
    {
      type: "mc",
      vraag: "Een artikel kost € 239,- inclusief 21% btw. Hoeveel euro kost het artikel exclusief btw? (Rond af op 2 decimalen).",
      opties: ["€ 197,52", "€ 200,00", "€ 205,10", "€ 218,00"],
      antwoord: 0,
      uitleg: "Inclusief 21% btw = 121%. Exclusief btw (100%) = 239 ÷ 121 × 100 = € 197,5206... → € 197,52."
    },
    {
      type: "waaronwaar",
      vraag: "Als alle getallen in een gegevensverzameling even vaak voorkomen, heeft de verzameling geen modus.",
      antwoord: true,
      uitleg: "Waar. Er is geen waarde die het vaakst voorkomt."
    },
    {
      type: "invul",
      vraag: "Van 120 reizigers gaan er 15 met de bus. Hoeveel graden is de sector 'bus' in een cirkeldiagram?",
      antwoord: "45|45°",
      uitleg: "(15 ÷ 120) × 360° = 45°."
    },
    {
      type: "mc",
      vraag: "In een klas van 20 leerlingen is de gemiddelde lengte 165 cm. Er komt een nieuwe leerling bij van 186 cm. Wat wordt de nieuwe gemiddelde lengte?",
      opties: ["165,5 cm", "166,0 cm", "166,5 cm", "167,0 cm"],
      antwoord: 1,
      uitleg: "Totale som = 20 × 165 = 3300. Nieuwe som = 3300 + 186 = 3486. Nieuw aantal = 21. Nieuw gemiddelde = 3486 ÷ 21 = 166,0 cm."
    },
    {
      type: "open",
      vraag: "Leg uit waarom een cirkeldiagram niet geschikt is om de temperatuurverandering per uur gedurende 24 uur weer te geven.",
      sleutelwoorden: ["tijdverloop", "verandering", "lijndiagram", "tijd"],
      minTreffers: 1,
      modelantwoord: "Temperatuur over tijd is een continu proces (tijdverloop). Een lijndiagram is daarvoor geschikt; een cirkeldiagram is bedoeld voor verdelingen van een totaal in percentages/sectoren.",
      uitleg: "Tijdverloop vraagt om een lijndiagram."
    },
    {
      type: "mc",
      vraag: "Gegeven de getallen in een steelbladdiagram: 145, 148, 148, 148, 152, 156, 159, 163, 164, 167, 171. Wat is de mediaan?",
      opties: ["152", "156", "159", "163"],
      antwoord: 1,
      uitleg: "11 getallen. Het 6e getal is 156."
    },
    {
      type: "waaronwaar",
      vraag: "De relatieve frequentie van een categorie bereken je door de frequentie van die categorie te delen door de totale frequentie.",
      antwoord: true,
      uitleg: "Waar. Relatieve frequentie = (frequentie ÷ totaal)."
    },
    {
      type: "invul",
      vraag: "Een band van een BMX-fiets is met 6,4 liter lucht voor 73% gevuld. Hoeveel liter lucht zit er in de band als hij tot 100% is opgepompt? (Rond af op 1 decimaal).",
      antwoord: "8,8|8,8 liter|8.8",
      uitleg: "6,4 ÷ 73 × 100 = 8,767... → 8,8 liter."
    },
    {
      type: "mc",
      vraag: "Van de rij getallen 9, 2, 6, 4, 9, x, 9, 7, 6, 8 is de mediaan gelijk aan 7. Gegeven dat er 10 getallen zijn, tussen welke waarden moet x minimaal liggen?",
      opties: ["x ≤ 6", "x ≥ 8", "x = 7", "x maakt niet uit"],
      antwoord: 1,
      uitleg: "De geordende rij zonder x has 6 en 8 rond het midden. Om de mediaan (som 5e+6e)/2 = 7 te laten zijn, moeten 6 ve 8 de 5e en 6e getallen zijn, dus x moet minimaal 8 (of groter) zijn."
    },
    {
      type: "open",
      vraag: "Bereken de korting in procenten als een artikel van € 125,- wordt afgeprijsd naar € 100,-.",
      sleutelwoorden: ["20", "20%"],
      minTreffers: 1,
      modelantwoord: "Korting = € 25,-. (25 ÷ 125) × 100% = 20% korting.",
      uitleg: "(25 ÷ 125) × 100% = 20%."
    },
    {
      type: "mc",
      vraag: "Hoeveel procent van een cirkeldiagram beslaat een sector met een middelpuntshoek van 126°?",
      opties: ["30%", "35%", "40%", "45%"],
      antwoord: 1,
      uitleg: "(126° ÷ 360°) × 100% = 35%."
    },
    {
      type: "waaronwaar",
      vraag: "Het toevoegen van één extreem hoog getal aan een gegevensverzameling heeft een grotere invloed op de mediaan dan op het gemiddelde.",
      antwoord: false,
      uitleg: "Onwaar. Het gemiddelde is juist erg gevoelig voor uitschieters, terwijl de mediaan robuust/ongevoelig is."
    },
    {
      type: "invul",
      vraag: "In een bedrijf werken 108 mannen met OV (43%) ve 106 vrouwen met OV (54%). Hoeveel personen komen in totaal met het OV?",
      antwoord: "162|162 personen",
      uitleg: "Mannen met OV = 108. Vrouwen met OV = 54. Totaal = 108 + 54 = 162 personen."
    },
    {
      type: "mc",
      vraag: "Bij een beelddiagram stelt 1 icoon van een fiets 15 fietsen voor. Als er 11 ikonens getekend staan, hoeveel fietsen zijn dat?",
      opties: ["150", "165", "180", "195"],
      antwoord: 1,
      uitleg: "11 × 15 = 165 fietsen."
    },
    {
      type: "open",
      vraag: "Geef een verkorte samenvatting van hoe je het gemiddelde uit een steelbladdiagram berekent.",
      sleutelwoorden: ["telt", "som", "bladeren", "delen"],
      minTreffers: 1,
      modelantwoord: "Lees alle afzonderlijke getallen af uit de stelen en bladeren, tel alle getallen bij elkaar op en deel deze som door het totale aantal bladeren.",
      uitleg: "Som van alle waarden ÷ aantal bladeren."
    }
  ]
});
