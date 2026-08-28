/* Proeftoets 7 — Natuurkunde HAVO 3: Hoofdstuk 2 (Elektriciteit - Deel 2)
   Focus: Paragraaf 2.2 — Weerstand, wet van Ohm (R = U / I), weerstandsdraden en (I,U)-diagrammen.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-7",
  titel: "Toets 7 — Weerstand, Wet van Ohm & Weerstandsdraden",
  vak: "Natuurkunde · HAVO 3 (H2)",
  icoon: "💡",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is de eenheid van <b>elektrische weerstand (R)</b>?",
      opties: ["Watt (W)", "Ampère (A)", "Volt (V)", "Ohm (Ω)"],
      antwoord: 3,
      uitleg: "Elektrische weerstand wordt gemeten in Ohm (symbool: Ω, de Griekse letter omega)."
    },
    {
      type: "mc",
      vraag: "Welke formule geeft de <b>Wet van Ohm</b> correct weer?",
      opties: [
        "R = U / I",
        "R = U × I",
        "R = I / U",
        "R = P × t"
      ],
      antwoord: 0,
      uitleg: "R = U / I (Weerstand = Spanning / Stroomsterkte). Hieruit volgt ook U = I × R en I = U / R."
    },
    {
      type: "invul",
      vraag: "Over een weerstand staat een spanning van 12 V. De stroomsterkte is 0,40 A. Bereken de weerstand R in Ohm.",
      antwoord: "30|30 Ω|30 ohm|30,0",
      uitleg: "R = U / I = 12 V / 0,40 A = 30 Ω."
    },
    {
      type: "invul",
      vraag: "Een kacheltje met een weerstand van 46 Ω wordt aangesloten op de netspanning van 230 V. Bereken de stroomsterkte in Ampère.",
      antwoord: "5|5 A|5,0|5,0 A",
      uitleg: "I = U / R = 230 V / 46 Ω = 5,0 A."
    },
    {
      type: "invul",
      vraag: "Door een weerstand van 150 Ω loopt een stroom van 0,08 A. Bereken de spanning over de weerstand in Volt.",
      antwoord: "12|12 V|12,0|12,0 V",
      uitleg: "U = I × R = 0,08 A × 150 Ω = 12 V."
    },
    {
      type: "mc",
      vraag: "Wat voor soort lijn zie je in een <b>(I,U)-diagram</b> bij een <b>ohmse weerstand</b> (constante weerstand)?",
      opties: [
        "Een parabool die steeds vlakker wordt",
        "Een rechte lijn door de oorsprong (0,0)",
        "Een cirkelvormige boog",
        "Een getrapte lijn"
      ],
      antwoord: 1,
      uitleg: "Bij een ohmse weerstand is de verhouding U/I constant. De grafiek is een rechte lijn door de oorsprong."
    },
    {
      type: "waaronwaar",
      vraag: "Een gewone gloeilamp is een voorbeeld van een ohmse weerstand met een constante weerstandswaarde bij elke temperatuur.",
      antwoord: false,
      uitleg: "Niet waar. Als de gloeidraad heet wordt, gaan de metaalatomen harder trillen en stijgt de weerstand sterk (PTC-gedrag). Een gloeilamp is niet-ohms."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de weerstand van een koperdraad als je de draad <b>twee keer zo lang</b> maakt?",
      opties: [
        "De weerstand wordt twee keer zo klein",
        "De weerstand wordt vier keer zo groot",
        "De weerstand wordt twee keer zo groot",
        "De weerstand verandert niet"
      ],
      antwoord: 2,
      uitleg: "De weerstand is recht evenredig met de lengte van de draad (R ~ l). Twee keer zo lang = twee keer zoveel weerstand."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met de weerstand van een draad als je de <b>doorsnede (dikte)</b> van de draad twee keer zo groot maakt?",
      opties: [
        "De weerstand blijft gelijk",
        "De weerstand verdubbelt",
        "De weerstand verviervoudigt",
        "De weerstand wordt twee keer zo klein (gehalveerd)"
      ],
      antwoord: 3,
      uitleg: "Een dikkere draad biedt meer ruimte voor passerende elektronen: de weerstand is omgekeerd evenredig met de doorsnede (R ~ 1/A)."
    },
    {
      type: "waaronwaar",
      vraag: "Als je bij een constante weerstand de spanning over de weerstand verdubbelt, wordt de stroomsterkte ook twee keer zo groot.",
      antwoord: true,
      uitleg: "Waar. Volgens I = U / R zijn stroomsterkte en spanning recht evenredig bij constante R."
    },
    {
      type: "invul",
      vraag: "Reken om: hoeveel Ohm is <b>4,7 kΩ</b>?",
      antwoord: "4700|4700 Ω|4.700|4700 ohm",
      uitleg: "1 kΩ (kilo-ohm) = 1000 Ω. Dus 4,7 × 1000 = 4700 Ω."
    },
    {
      type: "invul",
      vraag: "Reken om: hoeveel Ohm is <b>2,2 MΩ</b> (mega-ohm)?",
      antwoord: "2200000|2.200.000|2200000 Ω|2200000 ohm",
      uitleg: "1 MΩ = 1.000.000 Ω. Dus 2,2 × 1.000.000 = 2.200.000 Ω."
    },
    {
      type: "mc",
      vraag: "Een LDR (Light Dependent Resistor) is een speciale weerstand waarvan de weerstandswaarde:",
      opties: [
        "Afneemt als er meer licht op valt",
        "Toeneemt als er meer licht op valt",
        "Altijd precies 100 Ω blijft",
        "Alleen afhangt van de spanning"
      ],
      antwoord: 0,
      uitleg: "Bij een LDR geldt: veel licht = lage weerstand; in het donker = zeer hoge weerstand."
    },
    {
      type: "mc",
      vraag: "Een NTC-weerstand is een temperatuursensor. Wat gebeurt er met de weerstand van een NTC als de temperatuur <b>stijgt</b>?",
      opties: [
        "De weerstand stijgt",
        "De weerstand daalt (Negative Temperature Coefficient)",
        "De weerstand blijft gelijk",
        "De stroom valt direct weg naar nul"
      ],
      antwoord: 1,
      uitleg: "NTC = Negatieve Temperatuur Coëfficiënt: bij hogere temperatuur DAALT de weerstand."
    },
    {
      type: "waaronwaar",
      vraag: "Van vier verschillende draden van hetzelfde materiaal heeft een korte, dikke draad de kleinste elektrische weerstand.",
      antwoord: true,
      uitleg: "Waar. Kort (kleine l) en dik (grote A) geeft de laagste weerstand."
    },
    {
      type: "invul",
      vraag: "Door een weerstand loopt 25 mA bij een spanning van 5,0 V. Bereken de weerstand in Ohm.",
      antwoord: "200|200 Ω|200 ohm",
      uitleg: "25 mA = 0,025 A. R = U / I = 5,0 V / 0,025 A = 200 Ω."
    },
    {
      type: "mc",
      vraag: "In een schakeling vervang je een weerstand van 50 Ω door een weerstand van 100 Ω. De spanning blijft 10 V. Wat gebeurt er met de stroomsterkte?",
      opties: [
        "De stroomsterkte verdubbelt",
        "De stroomsterkte blijft 0,2 A",
        "De stroomsterkte wordt gehalveerd (van 0,2 A naar 0,1 A)",
        "De stroomsterkte wordt vier keer zo klein"
      ],
      antwoord: 2,
      uitleg: "I = U / R. Bij 50 Ω: I = 10 / 50 = 0,2 A. Bij 100 Ω: I = 10 / 100 = 0,1 A (gehalveerd)."
    },
    {
      type: "waaronwaar",
      vraag: "Constantaan is een legering waarvan de weerstand nauwelijks verandert als de temperatuur stijgt. Het is dus zeer geschikt voor precisieweerstanden.",
      antwoord: true,
      uitleg: "Waar. Daarom heet het 'constantaan': de weerstand blijft nagenoeg constant."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de gloeidraad van een lampje bij het inschakelen (als hij nog koud is) een lagere weerstand heeft dan wanneer de lamp fel brandt.",
      sleutelwoorden: ["temperatuur/koud lage weerstand", "heet/warmte atomen trillen harder", "elektronen botsen vaker/meer weerstand"],
      minTreffers: 2,
      modelantwoord: "In koude toestand trillen de metaalatomen in de gloeidraad relatief rustig, waardoor elektronen er makkelijk langs bewegen (lage weerstand). Zodra de lamp brandt en de draad gloeiend heet wordt (ca. 2500 °C), trillen de metaalatomen zeer hevig. De elektronen botsen daardoor veel vaker tegen de atomen, waardoor de weerstand sterk toeneemt.",
      uitleg: "Hogere temperatuur leidt tot hevigere atoomtrillingen en meer botsingen voor elektronen, dus hogere weerstand (PTC-effect)."
    },
    {
      type: "open",
      vraag: "Twee weerstandsdraden A en B zijn gemaakt van hetzelfde materiaal. Draad A is 1,0 m lang en heeft een doorsnede van 0,2 mm². Draad B is 2,0 m lang en heeft een doorsnede van 0,8 mm². Beredeneer welke draad de grootste weerstand heeft.",
      sleutelwoorden: ["Draad A grotere weerstand", "lengte factor 2", "doorsnede factor 4", "R = rho * l / A"],
      minTreffers: 2,
      modelantwoord: "Draad B is 2× zo lang (weerstand 2× groter), maar heeft een 4× zo grote doorsnede (weerstand 4× kleiner). De totale weerstand van B is dus 2/4 = 0,5× (de helft) van die van A. Draad A heeft dus de grootste weerstand (twee keer zo groot als die van draad B).",
      uitleg: "Verhouding R ~ l / A: Draad A heeft 1,0 / 0,2 = 5; Draad B heeft 2,0 / 0,8 = 2,5. Draad A heeft de grootste weerstand."
    }
  ]
});
