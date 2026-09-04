/* =========================================================
   Duru's Wiskunde (HAVO 3) — Proeftoets 10 — Steel-bladdiagram, Spreidingsbreedte & Kwartielen
   ========================================================= */
DURU.registerExamen(
{
  "id": "ex-wiskunde-h2-10",
  "hoofdstuk": 2,
  "titel": "Proeftoets 10 — Steel-bladdiagram, Spreidingsbreedte & Kwartielen",
  "vak": "Wiskunde · H2 Statistiek",
  "icoon": "🌳",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram staat in de steel het getal 5 en bij de bladeren 1, 4, 4, 9. De legenda vermeldt: 5 | 1 = 51. Welke getallen worden hier weergegeven?",
      "opties": [
        "51, 54, 54, 59",
        "15, 45, 45, 95",
        "5, 1, 4, 4, 9",
        "51449"
      ],
      "antwoord": 0,
      "uitleg": "De steel geeft de tientallen weer; gecombineerd met de bladeren levert dit 51, 54, 54 en 59 op."
    },
    {
      "type": "mc",
      "vraag": "Wat is de definitie van de 'spreidingsbreedte' van een statistische dataset?",
      "opties": [
        "Het gemiddelde van het eerste en derde kwartiel.",
        "Het verschil tussen de hoogste en de laagste waarneming (Maximum - Minimum).",
        "De breedte van de meest voorkomende klasse in een histogram.",
        "Het totale aantal waarnemingen in de steekproef."
      ],
      "antwoord": 1,
      "uitleg": "Spreidingsbreedte (range) = Maximum - Minimum."
    },
    {
      "type": "mc",
      "vraag": "In een groep scholieren is de langste leerling 194 cm en de kortste 158 cm. Wat is de spreidingsbreedte van de lengte?",
      "opties": [
        "34 cm",
        "46 cm",
        "36 cm",
        "176 cm"
      ],
      "antwoord": 2,
      "uitleg": "Spreidingsbreedte = 194 - 158 = 36 cm."
    },
    {
      "type": "mc",
      "vraag": "Wat stelt het eerste kwartiel (Q₁) van een geordende dataset voor?",
      "opties": [
        "De modus van de eerste helft van de getallen.",
        "Het minimum van de dataset.",
        "Een kwart van de totale som van alle getallen.",
        "De mediaan van de eerste (linker) helft van de waarnemingsgetallen (de grens van de eerste 25%)."
      ],
      "antwoord": 3,
      "uitleg": "Q₁ is de mediaan van de linkerhelft en markeert de eerste 25% van de waarnemingen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn de kwartielen: Q₁ = 18 en Q₃ = 31. Wat is de kwartielafstand van deze dataset?",
      "opties": [
        "13",
        "49",
        "24,5",
        "15"
      ],
      "antwoord": 0,
      "uitleg": "Kwartielafstand = Q₃ - Q₁ = 31 - 18 = 13."
    },
    {
      "type": "mc",
      "vraag": "Gegeven is de geordende reeks met 11 getallen: 12, 14, 15, 17, 19, 21, 24, 26, 28, 30, 35. Wat is het eerste kwartiel Q₁?",
      "opties": [
        "14",
        "15",
        "17",
        "21"
      ],
      "antwoord": 1,
      "uitleg": "De mediaan (Q₂) is 21 (het 6e getal). De linkerhelft bestaat uit 12, 14, 15, 17, 19. Het middelste getal daarvan is 15. Dus Q₁ = 15."
    },
    {
      "type": "mc",
      "vraag": "Wat is het derde kwartiel Q₃ van de getallenreeks uit de vorige vraag (rechterhelft: 24, 26, 28, 30, 35)?",
      "opties": [
        "30",
        "26",
        "28",
        "35"
      ],
      "antwoord": 2,
      "uitleg": "De rechterhelft is 24, 26, 28, 30, 35. Het middelste getal daarvan is 28. Dus Q₃ = 28."
    },
    {
      "type": "mc",
      "vraag": "Wat is een groot voordeel van een steel-bladdiagram boven een histogram?",
      "opties": [
        "Een steel-bladdiagram berekent automatisch de standaarddeviatie.",
        "Een steel-bladdiagram kan alleen met een passer worden getekend.",
        "Er kunnen nooit uitschieters in een steel-bladdiagram voorkomen.",
        "In een steel-bladdiagram blijven alle oorspronkelijke individuele meetwaarden zichtbaar en bewaard."
      ],
      "antwoord": 3,
      "uitleg": "In een histogram zie je alleen staafhoogtes en gaan individuele getallen verloren; in een steel-bladdiagram blijven alle exacte cijfers leesbaar."
    },
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram staat bij de legenda: 3 | 8 = 3,8 meter. Wat betekent een rij met steel 6 en bladeren 0, 2, 5?",
      "opties": [
        "6,0 meter; 6,2 meter en 6,5 meter",
        "60 meter; 62 meter en 65 meter",
        "0,6 meter; 2,6 meter en 5,6 meter",
        "6025 meter"
      ],
      "antwoord": 0,
      "uitleg": "Volgens de legenda stelt het blad decimalen voor: 6,0; 6,2 en 6,5 meter."
    },
    {
      "type": "mc",
      "vraag": "Welk percentage van alle waarnemingen ligt altijd tussen het eerste kwartiel Q₁ en het derde kwartiel Q₃?",
      "opties": [
        "25%",
        "50%",
        "75%",
        "100%"
      ],
      "antwoord": 1,
      "uitleg": "Tussen 25% (Q₁) en 75% (Q₃) ligt precies de middelste 50% van de waarnemingen."
    },
    {
      "type": "mc",
      "vraag": "In een steel-bladdiagram telt een onderzoeker in totaal 28 cijfers bij de bladeren. Hoeveel waarnemingen bevat deze dataset?",
      "opties": [
        "56 waarnemingen",
        "14 waarnemingen",
        "28 waarnemingen",
        "Dat hangt af van het aantal stelen"
      ],
      "antwoord": 2,
      "uitleg": "Elk blad vertegenwoordigt precies één afzonderlijke waarneming. 28 bladeren = 28 waarnemingen."
    },
    {
      "type": "mc",
      "vraag": "Gegeven zijn minimum = 12, Q₁ = 18, mediaan = 24, Q₃ = 32 en maximum = 45. Wat is de spreidingsbreedte van deze verdeling?",
      "opties": [
        "21",
        "14",
        "27",
        "33"
      ],
      "antwoord": 3,
      "uitleg": "Spreidingsbreedte = Maximum - Minimum = 45 - 12 = 33."
    },
    {
      "type": "waaronwaar",
      "vraag": "In een steel-bladdiagram moeten de cijfers in elk blad altijd op volgorde van klein naar groot worden genoteerd.",
      "antwoord": true,
      "uitleg": "Waar: bladeren horen netjes geordend van klein naar groot te staan zodat je direct de mediaan kunt aflezen."
    },
    {
      "type": "waaronwaar",
      "vraag": "De kwartielafstand is gelijk aan het maximum minus het minimum.",
      "antwoord": false,
      "uitleg": "Onwaar: dat is de spreidingsbreedte. De kwartielafstand is Q₃ - Q₁."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het tweede kwartiel Q₂ is exact hetzelfde als de mediaan van de totale dataset.",
      "antwoord": true,
      "uitleg": "Waar: Q₂ deelt de dataset in twee helften van 50% en is dus precies de mediaan."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een steel in een steel-bladdiagram mag worden overgeslagen als er geen waarnemingen in dat tiental zijn.",
      "antwoord": false,
      "uitleg": "Onwaar: alle opeenvolgende stelen tussen minimum en maximum moeten vermeld worden (met een leeg blad) om gaten in de spreiding te tonen."
    },
    {
      "type": "invul",
      "vraag": "De formule voor de kwartielafstand luidt: derde kwartiel ([Q3|Q₃]) minus eerste kwartiel ([Q1|Q₁]).",
      "antwoord": "Q3 - Q1|Q₃ - Q₁",
      "uitleg": "Kwartielafstand = Q₃ - Q₁."
    },
    {
      "type": "invul",
      "vraag": "De maat die het verschil tussen de hoogste en laagste waarneming aangeeft heet de [spreidingsbreedte].",
      "antwoord": "spreidingsbreedte",
      "uitleg": "Spreidingsbreedte = Maximum - Minimum."
    },
    {
      "type": "open",
      "vraag": "Gegeven zijn de meetwaarden: 5, 8, 12, 14, 17, 20, 25. Bepaal het minimum, het maximum, de spreidingsbreedte en de kwartielafstand van deze reeks.",
      "sleutelwoorden": [
        "spreidingsbreedte = 20|spreidingsbreedte 20",
        "kwartielafstand = 12|kwartielafstand 12"
      ],
      "minTreffers": 1,
      "modelantwoord": "Minimum = 5, Maximum = 25. Spreidingsbreedte = 25 - 5 = 20. Mediaan (Q₂) = 14. Q₁ = 8, Q₃ = 20. Kwartielafstand = Q₃ - Q₁ = 20 - 8 = 12.",
      "uitleg": "Spreidingsbreedte = 25 - 5 = 20; Kwartielafstand = 20 - 8 = 12."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom de legenda bij een steel-bladdiagram onmisbaar is.",
      "sleutelwoorden": [
        "betekenis van de getallen/eenheden",
        "tiental of decimaal/kommagetal"
      ],
      "minTreffers": 1,
      "modelantwoord": "Zonder legenda weet de lezer niet of bijvoorbeeld '4 | 7' staat voor het getal 47, voor 4,7 of voor 470. De legenda geeft aan wat de steel en het blad precies betekenen.",
      "uitleg": "De legenda bepaalt de schaal en decimale waarde van de cijfers."
    }
  ]
}
);
