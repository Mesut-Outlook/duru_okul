/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 21 — Hefbomen & De Hefboomwerking
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-21",
  "titel": "Toets 21 — Hefbomen & De Hefboomwerking",
  "vak": "Natuurkunde · HAVO 3 (H8)",
  "icoon": "🪚",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de <b>arm van een kracht</b> ($) bij een hefboom?",
      "opties": [
        "De kortste (loodrechte) afstand van het draaipunt tot de werklijn van de kracht",
        "De totale lengte van de hefboom van begin tot eind",
        "De afstand tussen de spierkracht en de last",
        "De dikte van het materiaal van de hefboom"
      ],
      "antwoord": 0,
      "uitleg": "De arm (r) is per definitie de loodrechte afstand tussen het draaipunt en de werklijn van de kracht."
    },
    {
      "type": "mc",
      "vraag": "Waarom heeft een betonschaar of takkenschaar hele lange handvatten en korte bekken?",
      "opties": [
        "Om lichter in de hand te liggen",
        "Om de arm van de spierkracht veel groter te maken dan de arm van de werkkracht, zodat de werkkracht enorm wordt vergroot",
        "Zodat de schaar niet kan roesten",
        "Om sneller te kunnen knippen zonder kracht"
      ],
      "antwoord": 1,
      "uitleg": "Als r_spier veel groter is dan r_werk, wordt de resulterende knipkracht (F_werk) vele malen groter dan de spierkracht."
    },
    {
      "type": "mc",
      "vraag": "Welk gereedschap is een voorbeeld van een hefboom waarbij de kracht juist <b>verkleind</b> wordt om preciezer te kunnen werken?",
      "opties": [
        "Een koevoet (breekijzer)",
        "Een notenkraker",
        "Een pincet",
        "Een flesopener"
      ],
      "antwoord": 2,
      "uitleg": "Bij een pincet zit je vinger (spierkracht) dichter bij het draaipunt dan het uiteinde (werkkracht). Hierdoor is de werkkracht kleiner en werk je uiterst nauwkeurig."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een kruiwagen bevindt het draaipunt zich bij het voorwiel, waardoor het een voorbeeld is van een enkelzijdige hefboom.",
      "antwoord": true,
      "uitleg": "Waar. Bij een kruiwagen liggen de last en de spierkracht aan dezelfde kant van het draaipunt (enkelzijdige hefboom)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het verschil tussen een <b>enkelzijdige</b> en een <b>dubbelzijdige hefboom</b>?",
      "opties": [
        "Er is geen verschil",
        "Een dubbelzijdige hefboom heeft twee draaipunten",
        "Een enkelzijdige hefboom kan alleen trekken, niet duwen",
        "Bij een dubbelzijdige hefboom ligt het draaipunt tussen de twee krachten in; bij een enkelzijdige hefboom liggen beide krachten aan dezelfde kant van het draaipunt"
      ],
      "antwoord": 3,
      "uitleg": "Dubbelzijdig = draaipunt ertussen (bijv. schaar, wipwap, koevoet). Enkelzijdig = krachten aan 1 kant van draaipunt (bijv. kruiwagen, notenkraker, pincet)."
    },
    {
      "type": "invul",
      "vraag": "Hoe noem je het vaste punt waar een hefboom omheen kan draaien?",
      "antwoord": "draaipunt",
      "uitleg": "Het draaipunt (aangeduid met de letter D)."
    },
    {
      "type": "mc",
      "vraag": "Hoe noem je de oneindig lange denkbeeldige lijn die in de richting van de uitgeoefende kracht loopt?",
      "opties": [
        "De werklijn van de kracht",
        "De evenwichtslijn",
        "De hefboomlijn",
        "De richtingsas"
      ],
      "antwoord": 0,
      "uitleg": "De werklijn is de lijn waarin de krachtvector ligt."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je een moer wilt losdraaien met een steeksleutel, moet je de sleutel zo dicht mogelijk bij de moer vastpakken om de grootste kracht uit te oefenen.",
      "antwoord": false,
      "uitleg": "Niet waar. Je moet de sleutel juist zo ver mogelijk aan het uiteinde vastpakken om de arm (r) zo groot mogelijk te maken, waardoor het moment (draaieffect) maximaal is."
    },
    {
      "type": "invul",
      "vraag": "Welke eenheid hoort bij het moment van een kracht ($)? Geef het symbool van deze eenheid.",
      "antwoord": "Nm|N*m|N m|Newtonmeter",
      "uitleg": "Moment M = F × r -> Newton × meter = Nm (Newtonmeter)."
    },
    {
      "type": "mc",
      "vraag": "Een wipwap is in evenwicht. Aan de linkerkant zit iemand van 400 N op 1,5 m van het draaipunt. Hoe groot is het moment aan de linkerkant?",
      "opties": [
        "400 Nm",
        "600 Nm",
        "266,7 Nm",
        "800 Nm"
      ],
      "antwoord": 1,
      "uitleg": "M = F × r = 400 N × 1,5 m = 600 Nm."
    },
    {
      "type": "invul",
      "vraag": "Aan de rechterkant van deze wipwap (uit de vorige vraag, met {\text{links}} = 600\text{ Nm}$) gaat iemand zitten op 2,0 m van het draaipunt. Hoe zwaar moet deze persoon zijn in Newton om precies evenwicht te maken?",
      "antwoord": "300|300 N",
      "uitleg": "F = M / r = 600 Nm / 2,0 m = 300 N."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als de werklijn van een kracht precies door het draaipunt heen loopt, is de arm  = 0\text{ m}$ en is het moment van die kracht nul ( = 0\text{ Nm}$).",
      "antwoord": true,
      "uitleg": "Waar. Als je tegen het scharnier van een deur duwt, draait de deur niet (r = 0 -> M = 0)."
    },
    {
      "type": "mc",
      "vraag": "Welke formule beschrijft de <b>hefboomwet (momentenwet)</b> bij een hefboom in evenwicht?",
      "opties": [
        "p = F / A",
        "F = m × g",
        "F₁ × r₁ = F₂ × r₂ (of M_links = M_rechts)",
        "E = P × t"
      ],
      "antwoord": 2,
      "uitleg": "In evenwicht geldt: som van momenten linksom = som van momenten rechtsom (F₁ × r₁ = F₂ × r₂)."
    },
    {
      "type": "invul",
      "vraag": "Een flesopener heeft een spierkrachtarm van 12 cm en een werkkrachtarm van 1,5 cm. Hoeveel keer zo groot is de uitgeoefende werkkracht vergeleken met de spierkracht?",
      "antwoord": "8|8 keer|8x",
      "uitleg": "Krachtvergroting = r_spier / r_werk = 12 cm / 1,5 cm = 8 keer zo groot."
    },
    {
      "type": "mc",
      "vraag": "Waarom zit de klink van een deur aan de buitenkant van de deur en niet vlak naast de scharnieren?",
      "opties": [
        "Dat is alleen voor de sier",
        "Omdat de deur anders te zwaar wordt",
        "Om het slot te beschermen",
        "Om de arm van de spierkracht ten opzichte van het scharnier (draaipunt) zo groot mogelijk te maken, zodat je met minimale kracht de deur opent"
      ],
      "antwoord": 3,
      "uitleg": "Grote arm r betekent dat je met een kleine spierkracht F toch het benodigde draaimoment levert."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij het berekenen van een hefboom in evenwicht mogen de armen in centimeters (cm) staan, mits beide armen in dezelfde eenheid staan.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. F₁ × r₁ = F₂ × r₂ klopt ook als beide r in cm staan (de verhouding blijft gelijk). Als je het moment M zelf berekent, moet r wel in meters."
    },
    {
      "type": "invul",
      "vraag": "Een breekijzer heeft een totale lengte van 80 cm. Het draaipunt bevindt zich op 5 cm van het uiteinde waar de spijker vastzit. De spierkrachtarm is dus 75 cm. Als je met 200 N duwt, hoe groot is dan de uittrekkracht op de spijker in Newton?",
      "antwoord": "3000|3000 N|3.000|3.000 N",
      "uitleg": "F_werk = (F_spier × r_spier) / r_werk = (200 N × 75 cm) / 5 cm = 15.000 / 5 = 3000 N."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er met het moment van een kracht als je de spierkracht verdubbelt en tegelijk de afstand tot het draaipunt halveert?",
      "opties": [
        "Het moment blijft precies gelijk",
        "Het moment wordt twee keer zo groot",
        "Het moment wordt vier keer zo groot",
        "Het moment halveert"
      ],
      "antwoord": 0,
      "uitleg": "M_nieuw = (2 × F) × (0,5 × r) = F × r = M_oud."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe je met behulp van een geodriehoek de <b>arm van een kracht</b> correct opmeet in een natuurkundige tekening.",
      "sleutelwoorden": [
        "werklijn",
        "loodlijn/loodrecht",
        "afstand"
      ],
      "minTreffers": 2,
      "modelantwoord": "1. Teken of verleng de werklijn van de kracht met een stippellijn in beide richtingen. 2. Leg de nullijn van de geodriehoek langs de werklijn en schuif totdat de liniaal door het draaipunt (D) gaat. 3. Teken een loodrechte lijn (hoek van 90°) vanuit het draaipunt naar de werklijn. 4. Meet de lengte van deze loodlijn op; dat is de arm van de kracht (r).",
      "uitleg": "De arm is altijd de loodrechte afstand van draaipunt tot werklijn."
    },
    {
      "type": "open",
      "vraag": "Een kraan tilt een zware last. Beredeneer met de hefboomwet waarom het gevaarte dreigt om te slaan en hoe dit mechanisch voorkomen wordt.",
      "sleutelwoorden": [
        "moment/draaikracht",
        "tegengewicht/balans/contragewicht"
      ],
      "minTreffers": 2,
      "modelantwoord": "Dubbelzijdige hefbomen (draaipunt ligt tussen de twee krachten): 1. Schaar (of snoeischaar), 2. Wipwap (of koevoet/combinatietang). Enkelzijdige hefbomen (beide krachten liggen aan dezelfde kant van het draaipunt): 1. Kruiwagen, 2. Notenkraker (of flesopener/pincet).",
      "uitleg": "Classificatie van hefbomen in het dagelijks leven."
    }
  ]
});
