/* =========================================================
   Duru's Economie (HAVO 3) — Proeftoets 45: Omzet, kostprijs, btw en winst berekenen (Paragraaf 4.3)
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-economie-45",
  "hoofdstuk": 4,
  "paragraaf": "4.3",
  "titel": "Proeftoets 45: Omzet, kostprijs, btw en winst berekenen (Paragraaf 4.3)",
  "vak": "Economie · HAVO 3 (Pincode)",
  "icoon": "🧮",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Een bedrijf verkoopt 3.500 producten voor € 14 per stuk (exclusief btw). Wat is de omzet?",
      "opties": [
        "€ 49.000",
        "€ 3.514",
        "€ 4.900",
        "€ 59.290"
      ],
      "antwoord": 0,
      "uitleg": "Omzet = P × Q = € 14 × 3.500 = € 49.000."
    },
    {
      "type": "mc",
      "vraag": "De omzet van een bakkerij is € 27.000 bij een verkoopprijs van € 18 per taart. Hoeveel taarten zijn verkocht?",
      "opties": [
        "486.000",
        "150",
        "1.500",
        "27.018"
      ],
      "antwoord": 2,
      "uitleg": "Q = TO ÷ P = 27.000 ÷ 18 = 1.500."
    },
    {
      "type": "mc",
      "vraag": "Een bedrijf heeft een omzet van € 12.600 en een afzet van 600 producten. Wat is de verkoopprijs per product?",
      "opties": [
        "€ 21",
        "€ 7.560.000",
        "€ 12",
        "€ 210"
      ],
      "antwoord": 0,
      "uitleg": "P = TO ÷ Q = 12.600 ÷ 600 = € 21."
    },
    {
      "type": "mc",
      "vraag": "De vaste kosten van een bedrijf zijn € 3.000 en de variabele kosten per product zijn € 0,80. Er worden 5.000 producten gemaakt. Wat is de kostprijs?",
      "opties": [
        "€ 0,60",
        "€ 3.800",
        "€ 1,40",
        "€ 4,00"
      ],
      "antwoord": 2,
      "uitleg": "Kostprijs = vaste kosten ÷ aantal producten + variabele kosten per product = 3.000 ÷ 5.000 + 0,80 = 0,60 + 0,80 = € 1,40."
    },
    {
      "type": "mc",
      "vraag": "De kostprijs van een product is € 2,50 en de winstmarge is 30% van de kostprijs. Wat is de verkoopprijs?",
      "opties": [
        "€ 2,80",
        "€ 7,50",
        "€ 3,75",
        "€ 3,25"
      ],
      "antwoord": 3,
      "uitleg": "Verkoopprijs = 2,50 + (30% × 2,50) = 2,50 + 0,75 = € 3,25. Of kort: 2,50 × 1,3."
    },
    {
      "type": "mc",
      "vraag": "Een jas kost € 80 exclusief btw. Het btw-tarief is 21%. Wat is de prijs inclusief btw?",
      "opties": [
        "€ 96,80",
        "€ 80,21",
        "€ 100,80",
        "€ 63,20"
      ],
      "antwoord": 0,
      "uitleg": "Prijs incl. btw = 80 × (1 + 0,21) = 80 × 1,21 = € 96,80."
    },
    {
      "type": "mc",
      "vraag": "Een pak koffie kost € 6,54 inclusief 9% btw. Wat is de prijs exclusief btw?",
      "opties": [
        "€ 5,95",
        "€ 6,00",
        "€ 7,13",
        "€ 5,66"
      ],
      "antwoord": 1,
      "uitleg": "Prijs excl. btw = 6,54 ÷ 1,09 = € 6,00."
    },
    {
      "type": "mc",
      "vraag": "Een winkel heeft een omzet van € 85.000. Er zijn 1.200 producten verkocht met een gemiddelde inkoopprijs van € 25 per stuk. Wat is de brutowinst?",
      "opties": [
        "€ 30.000",
        "€ 85.000",
        "€ 84.975",
        "€ 55.000"
      ],
      "antwoord": 3,
      "uitleg": "Inkoopwaarde = 1.200 × 25 = 30.000. Brutowinst = 85.000 − 30.000 = € 55.000."
    },
    {
      "type": "mc",
      "vraag": "Een bedrijf heeft een brutowinst van € 40.000 en bedrijfskosten van € 28.500. Wat is de nettowinst?",
      "opties": [
        "€ 68.500",
        "€ 11.500",
        "€ 28.500",
        "€ 12.500"
      ],
      "antwoord": 1,
      "uitleg": "Nettowinst = brutowinst − bedrijfskosten = 40.000 − 28.500 = € 11.500."
    },
    {
      "type": "waaronwaar",
      "vraag": "Prijs inclusief btw = prijs exclusief btw × (1 + btw-tarief).",
      "antwoord": true,
      "uitleg": "Waar. Bij 21% reken je dus × 1,21 en bij 9% × 1,09."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het bedrag inclusief 21% btw bereken je door het bedrag exclusief btw met 0,21 te vermenigvuldigen.",
      "antwoord": false,
      "uitleg": "Onwaar. Met 0,21 bereken je alleen het btw-bedrag. Voor de prijs inclusief btw vermenigvuldig je met 1,21."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een kostprijs van € 4,00 en een winstmarge van 25% van de kostprijs is de verkoopprijs € 4,25.",
      "antwoord": false,
      "uitleg": "Onwaar. De winstmarge is 25% van € 4,00 = € 1,00, dus de verkoopprijs is € 5,00."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een omzet van € 20.000 en een inkoopwaarde van € 12.000 is de brutowinst € 8.000.",
      "antwoord": true,
      "uitleg": "Waar. 20.000 − 12.000 = 8.000."
    },
    {
      "type": "invul",
      "vraag": "Een product kost € 250 exclusief btw. Het btw-tarief is 21%. Hoeveel euro btw komt erbij? € ____",
      "antwoord": "52,50",
      "uitleg": "250 × 0,21 = € 52,50."
    },
    {
      "type": "invul",
      "vraag": "De verkoopprijs is € 9,50 en de afzet is 2.000. Hoeveel euro bedraagt de omzet? € ____",
      "antwoord": "19000|19.000",
      "uitleg": "Omzet = 9,50 × 2.000 = € 19.000."
    },
    {
      "type": "invul",
      "vraag": "Een boek kost € 30,25 inclusief 21% btw. De prijs exclusief btw is € 25. Hoeveel euro btw zit er in de prijs? € ____",
      "antwoord": "5,25",
      "uitleg": "Btw = 30,25 − 25 = € 5,25."
    },
    {
      "type": "invul",
      "vraag": "De brutowinst is € 62.000 en de nettowinst € 14.500. Hoeveel euro bedragen de bedrijfskosten? € ____",
      "antwoord": "47500|47.500",
      "uitleg": "Bedrijfskosten = brutowinst − nettowinst = 62.000 − 14.500 = € 47.500."
    },
    {
      "type": "invul",
      "vraag": "Een product heeft een kostprijs van € 4,00 en een winstmarge van 50% van de kostprijs. Wat is de verkoopprijs in euro’s? € ____",
      "antwoord": "6",
      "uitleg": "4,00 + (50% × 4,00) = 4,00 + 2,00 = € 6,00."
    },
    {
      "type": "open",
      "vraag": "Mila maakt kaarsen. Per jaar heeft ze constante kosten van € 600 (marktkraam en elektriciteit) en variabele kosten van € 300 (was en lont). Ze maakt 400 kaarsen per jaar. Haar winstmarge is 60% van de kostprijs. Bereken de kostprijs en de verkoopprijs van één kaars.",
      "sleutelwoorden": [
        "2,25",
        "3,60"
      ],
      "minTreffers": 2,
      "modelantwoord": "Kostprijs = 600 ÷ 400 + 300 ÷ 400 = 1,50 + 0,75 = € 2,25. Verkoopprijs = 2,25 + 60% × 2,25 = 2,25 + 1,35 = € 3,60.",
      "uitleg": "Eerst de kostprijs (vaste kosten ÷ aantal + variabele kosten per product), daarna de winstmarge erbij optellen."
    },
    {
      "type": "open",
      "vraag": "Een televisie kost € 363 inclusief 21% btw. Bereken de prijs exclusief btw en het btw-bedrag.",
      "sleutelwoorden": [
        "300",
        "63"
      ],
      "minTreffers": 2,
      "modelantwoord": "Prijs excl. btw = 363 ÷ 1,21 = € 300. Btw = 363 − 300 = € 63.",
      "uitleg": "Delen door 1,21 geeft de prijs exclusief btw; het verschil met de prijs inclusief btw is het btw-bedrag."
    }
  ]
});
