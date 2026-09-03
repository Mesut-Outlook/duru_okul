/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 19 — Soortelijke Weerstand & Weerstandsdraden
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-19",
  "hoofdstuk": 4,
  "titel": "Toets 19 — Soortelijke Weerstand & Weerstandsdraden",
  "vak": "Natuurkunde · HAVO 3 (H4)",
  "icoon": "📏",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is de formule om de weerstand van een stroomdraad te berekenen uit lengte (l), doorsnede (A) en soortelijke weerstand (ρ)?",
      "opties": [
        "R = (ρ × l) / A",
        "R = (ρ × A) / l",
        "R = ρ × l × A",
        "R = U / I"
      ],
      "antwoord": 0,
      "uitleg": "R = (ρ · l) / A, waarbij R de weerstand in Ω is, ρ de soortelijke weerstand, l de lengte in meters en A de doorsnede in mm²."
    },
    {
      "type": "mc",
      "vraag": "Wat geeft de <b>soortelijke weerstand (ρ)</b> van een materiaal aan?",
      "opties": [
        "Hoeveel stroom er maximaal doorheen kan",
        "De weerstand van een draad van dat materiaal met een lengte van 1 meter en een doorsnede van 1 mm²",
        "Het gewicht van 1 meter draad",
        "De smelttemperatuur van de draad"
      ],
      "antwoord": 1,
      "uitleg": "Soortelijke weerstand ρ (in Ω·mm²/m) is een stofeigenschap die het elektrisch weerstandsvermogen van het materiaal aangeeft."
    },
    {
      "type": "invul",
      "vraag": "Koper heeft een soortelijke weerstand van 0,017 Ω·mm²/m. Bereken de weerstand van een koperdraad van 50 meter lengte met een doorsnede van 2,5 mm² in Ohm.",
      "antwoord": "0,34|0,34 Ω|0,34 ohm",
      "uitleg": "R = (ρ × l) / A = (0,017 × 50) / 2,5 = 0,85 / 2,5 = 0,34 Ω."
    },
    {
      "type": "mc",
      "vraag": "Welk metaal heeft van alle veelgebruikte metalen de <b>laagste</b> soortelijke weerstand (is de allerbeste geleider)?",
      "opties": [
        "Lood",
        "IJzer",
        "Zilver (en direct daarna koper)",
        "Constantaan"
      ],
      "antwoord": 2,
      "uitleg": "Zilver (ρ ≈ 0,016) en koper (ρ ≈ 0,017) zijn de beste elektrische geleiders."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je een koperdraad twee keer zo lang maakt én de doorsnede twee keer zo groot maakt, blijft de elektrische weerstand exact hetzelfde.",
      "antwoord": true,
      "uitleg": "Waar. R = ρ · (2·l) / (2·A) = ρ · l / A (de factoren 2 vallen tegen elkaar weg)."
    },
    {
      "type": "invul",
      "vraag": "Constantaan heeft een soortelijke weerstand van 0,45 Ω·mm²/m. Een constantaandraad van 10 meter heeft een doorsnede van 0,50 mm². Bereken de weerstand in Ohm.",
      "antwoord": "9|9 Ω|9 ohm|9,0",
      "uitleg": "R = (ρ × l) / A = (0,45 × 10) / 0,50 = 4,5 / 0,50 = 9 Ω."
    },
    {
      "type": "mc",
      "vraag": "Waarom gebruikt men in huizen dikkere installatiedraad (bijv. 2,5 mm²) voor zware groepen i.p.v. dunne draadjes van 0,5 mm²?",
      "opties": [
        "Omdat de spanning anders daalt naar nul",
        "Omdat dunne draadjes te duur zijn",
        "Omdat dikke draad buigzamer is",
        "Omdat dikkere draad een lagere weerstand heeft, waardoor er minder warmteontwikkeling (I²·R verlies) en minder risico op brand is bij hoge stroomsterktes"
      ],
      "antwoord": 3,
      "uitleg": "Grotere doorsnede A verlaagt R, waardoor draden niet gevaarlijk oververhit raken bij stromen tot 16 A."
    },
    {
      "type": "waaronwaar",
      "vraag": "Constantaan heeft een veel hogere soortelijke weerstand dan koper en wordt daarom gebruikt om verwarmingselementen en weerstanden te maken.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Koper geleidt bijna 26× beter dan constantaan."
    },
    {
      "type": "invul",
      "vraag": "Een ijzerdraad (ρ = 0,10 Ω·mm²/m) heeft een weerstand van 4,0 Ω en een doorsnede van 0,50 mm². Bereken de lengte van de draad in meters.",
      "antwoord": "20|20 m|20,0",
      "uitleg": "l = (R × A) / ρ = (4,0 × 0,50) / 0,10 = 2,0 / 0,10 = 20 meter."
    },
    {
      "type": "mc",
      "vraag": "Wat is een <b>schuifweerstand (potentiometer / dimmer)</b>?",
      "opties": [
        "Een regelbare weerstand waarbij je met een schuifje de effectieve lengte van de weerstandsdraad (en dus de weerstandswaarde) kunt variëren",
        "Een batterij die je kunt verschuiven",
        "Een schakelaar die alleen aan of uit kan",
        "Een transformator voor wisselstroom"
      ],
      "antwoord": 0,
      "uitleg": "Door het schuifcontact te verplaatsen maak je het actieve stuk draad langer of korter, waardoor R verandert."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je de diameter van een ronde draad verdubbelt, wordt de oppervlakte van de doorsnede (A = π·r²) <b>vier keer zo groot</b>.",
      "antwoord": true,
      "uitleg": "Waar. Omdat A = π · (0,5d)², groeit de doorsnede kwadratisch met de diameter (2² = 4)."
    },
    {
      "type": "invul",
      "vraag": "Een ronde koperdraad heeft een straal r = 1,0 mm. Bereken de doorsnede A in mm² (neem A = π × r² met π ≈ 3,14, rond af op 2 decimalen).",
      "antwoord": "3,14|3,14 mm²",
      "uitleg": "A = π × 1,0² = 3,14 mm²."
    },
    {
      "type": "mc",
      "vraag": "Welke van de volgende vier draden van hetzelfde materiaal heeft de <b>ALLERGROOTSTE weerstand</b>?",
      "opties": [
        "Een lange, dikke draad",
        "Een lange, dunne draad",
        "Een korte, dunne draad",
        "Een korte, dikke draad"
      ],
      "antwoord": 1,
      "uitleg": "Grote lengte l (boven de breuk) en kleine doorsnede A (onder de breuk) maximaliseert R = ρ · l / A."
    },
    {
      "type": "waaronwaar",
      "vraag": "Supergeleiding is een verschijnsel waarbij bepaalde materialen bij extreem lage temperaturen (nabij 0 Kelvin) hun elektrische weerstand volledig verliezen (R = 0 Ω).",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Bij supergeleiding kan stroom zonder enig energieverlies blijven rondstromen."
    },
    {
      "type": "invul",
      "vraag": "Door een verlengsnoer van 20 m koperdraad (weerstand R = 0,40 Ω) loopt een stroom van 10 A. Hoeveel Volt spanningsverlies treedt er op over het snoer ( = I \times R$)?",
      "antwoord": "4|4 V|4,0|4,0 V",
      "uitleg": "U = I × R = 10 A × 0,40 Ω = 4,0 V."
    },
    {
      "type": "mc",
      "vraag": "Hoeveel Watt warmteverlies ontstaat er in het verlengsnoer uit de vorige vraag ( = U \times I$ of  = I^2 \times R$)?",
      "opties": [
        "4 W",
        "400 W",
        "40 W",
        "4000 W"
      ],
      "antwoord": 2,
      "uitleg": "P = U × I = 4 V × 10 A = 40 W (of P = 10² × 0,40 = 40 W)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je een kabelhaspel gebruikt voor een zwaar apparaat (zoals een hogedrukreiniger van 2000 W), moet je de haspel altijd <b>volledig afrollen</b> om oververhitting en smelten te voorkomen.",
      "antwoord": true,
      "uitleg": "Waar. Opgewikkeld kan de ontwikkelde warmte (I²·R) niet ontsnappen, waardoor de haspel kan smelten of vlam vatten."
    },
    {
      "type": "invul",
      "vraag": "Een draad van 2,0 meter heeft een weerstand van 6,0 Ω. Welke weerstand heeft een stuk van 5,0 meter van exact dezelfde draad?",
      "antwoord": "15|15 Ω|15 ohm",
      "uitleg": "De weerstand is recht evenredig met de lengte: 6,0 Ω / 2,0 m = 3,0 Ω/m. Voor 5,0 m: 3,0 × 5,0 = 15 Ω."
    },
    {
      "type": "open",
      "vraag": "Beredeneer met behulp van de formule R = (ρ · l) / A wat er gebeurt met de weerstand van een draad als je: 1) de lengte verdrievoudigt, 2) de doorsnede verdubbelt, 3) beide tegelijk doet.",
      "sleutelwoorden": [
        "3x zo groot/3x groter",
        "2) doorsnede 2x zo groot -> weerstand gehalveerd / 0,5x",
        "3) beide -> factor 3/2 = 1,5x zo groot"
      ],
      "minTreffers": 3,
      "modelantwoord": "1. Lengte verdrievoudigen: Omdat R ~ l, wordt de weerstand 3 keer zo groot (3×). 2. Doorsnede verdubbelen: Omdat R ~ 1/A, wordt de weerstand gehalveerd (0,5×). 3. Beide tegelijk: De nieuwe weerstand wordt 3 / 2 = 1,5 keer zo groot als de oorspronkelijke weerstand.",
      "uitleg": "Evenredigheden in de draadweerstandsformule."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom hoogspanningskabels vaak van aluminium met een stalen kern gemaakt worden in plaats van massief koper, ondanks dat koper een iets betere geleider is.",
      "sleutelwoorden": [
        "lichter/lage dichtheid",
        "stalen kern geeft treksterkte",
        "koper te zwaar/duur"
      ],
      "minTreffers": 2,
      "modelantwoord": "Koper heeft een hoge dichtheid (8,9 g/cm³) en is erg zwaar en duur. Aluminium heeft een veel lagere dichtheid (2,7 g/cm³) en is ruim drie keer zo licht. Hierdoor kunnen hoogspanningsmasten veel verder uit elkaar staan zonder dat de kabels door hun eigen gewicht breken. De stalen binnenkern zorgt voor de nodige mechanische treksterkte, terwijl het aluminium de stroom geleidt.",
      "uitleg": "Afweging tussen elektrische geleidbaarheid, gewicht (dichtheid), mechanische sterkte en kosten."
    }
  ]
});
