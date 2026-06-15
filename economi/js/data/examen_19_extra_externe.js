/* Extra Proeftoets 14 — Externe Effecten & Maatschappelijke Kosten */
DURU.registerExamen({
  id: "ex-extra-externe-effecten",
  titel: "Extra Proeftoets 14 — Externe Effecten & Maatschappelijke Kosten",
  vak: "Economie · Milieu",
  icoon: "💨",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is een extern effect in de economie?",
      opties: [
        "De invloed van het weer op de oogst van boeren.",
        "Gevolgen van productie of consumptie voor derden die niet in de marktprijs van het product zijn opgenomen.",
        "De import van goederen uit het buitenland.",
        "Het effect van de rentevoet op de staatsschuld."
      ],
      antwoord: 1,
      uitleg: "Een **extern effect** is een onbedoeld gevolg. Het kan negatief (schadelijk) of positief (voordelig) zijn voor anderen."
    },
    {
      type: "mc",
      vraag: "Hoe kan de overheid een negatief extern effect, zoals CO2-uitstoot door fabrieken, direct aanpakken via heffingen?",
      opties: [
        "Door de fabriek gratis stroom te geven.",
        "Hogere belastingen (heffingen) opleggen per ton uitstoot, zodat schoon produceren aantrekkelijker wordt.",
        "De btw op de producten van de fabriek verlagen naar 0%.",
        "Het verbieden van alle export."
      ],
      antwoord: 1,
      uitleg: "Een **milieuheffing** verhoogt de kosten van vervuiling, waardoor bedrijven gestimuleerd worden schonere technieken te gebruiken."
    },
    {
      type: "mc",
      vraag: "Wat verstaan we onder maatschappelijke kosten?",
      opties: [
        "De kosten die de overheid maakt voor sociale uitkeringen.",
        "De private kosten van het bedrijf (grondstoffen, loon) plus de externe kosten (zoals schade aan milieu en gezondheid) samen.",
        "De kosten voor het organiseren van buurtbijeenkomsten.",
        "De btw die consumenten betalen."
      ],
      antwoord: 1,
      uitleg: "Maatschappelijke kosten geven het complete plaatje van de **totale kosten** van een product voor de hele samenleving."
    },
    {
      type: "mc",
      vraag: "Welk van de volgende is een voorbeeld van een positief extern effect?",
      opties: [
        "Een fabriek die warmte loost in een rivier waardoor vissen sterven.",
        "Een imker die bijen houdt voor honing, waarbij de bijen ook de fruitbomen van de buurman bestuiven.",
        "Een automobilist die in de file staat.",
        "Het kopen van een nieuwe spijkerbroek."
      ],
      antwoord: 1,
      uitleg: "De fruitboer profiteert gratis van de bestuiving door de bijen van de imker. Dit is een onbedoeld **positief extern effect**."
    },
    {
      type: "mc",
      vraag: "Waarom faalt de markt bij het oplossen van negatieve externe effecten?",
      opties: [
        "Omdat consumenten altijd te veel willen betalen.",
        "Omdat bedrijven en consumenten uit zichzelf geen rekening houden met kosten die zij op anderen afwentelen (zoals vervuiling).",
        "Omdat de overheid geen btw heft op vervuiling.",
        "Omdat de koning alle fabrieken bezit."
      ],
      antwoord: 1,
      uitleg: "Aangezien milieuschade gratis is voor het bedrijf, rekent het bedrijf dit niet door in zijn verkoopprijs. De overheid moet ingrijpen via regels of heffingen."
    },
    {
      type: "waaronwaar",
      vraag: "Als je een lening afsluit voor zonnepanelen en de overheid betaalt een deel via subsidie, is dat bedoeld om positieve externe effecten te stimuleren.",
      antwoord: true,
      uitleg: "Waar. Zonnepanelen wekken schone stroom op en verminderen CO2-uitstoot, wat goed is voor de hele samenleving (positief effect)."
    },
    {
      type: "waaronwaar",
      vraag: "Lawaaioverlast door een nabijgelegen snelweg is een voorbeeld van een positief extern effect voor omwonenden.",
      antwoord: false,
      uitleg: "Onwaar. Het is een **negatief extern effect**: het brengt overlast en vermindering van woongenot (schade) met zich mee zonder compensatie."
    },
    {
      type: "invul",
      vraag: "Het opnemen van externe kosten in de prijs van een product (zodat de vervuiler de echte prijs betaalt) noemen we _________.",
      antwoord: "internaliseren|internalisering",
      uitleg: "Door te **internaliseren** (bijv. via een belasting) wordt milieuschade onderdeel van de verkoopprijs."
    },
    {
      type: "open",
      vraag: "Leg uit waarom heffingen op plastic verpakkingen bijdragen aan een beter milieu.",
      sleutelwoorden: ["heffing/belasting/duurder", "ontmoedigen/minder kopen/minder gebruiken", "afval verminderen/plastic afval/milieu", "alternatief/bewustwording"],
      minTreffers: 2,
      modelantwoord: "Een heffing op plastic verpakkingen maakt deze producten duurder. Dit ontmoedigt het gebruik ervan door consumenten en producenten, die overstappen op milieuvriendelijkere alternatieven (zoals papier of herbruikbare tassen), waardoor er minder plastic afval in de natuur belandt.",
      uitleg: "Hogere prijs -> lagere vraag -> minder vervuiling (prijsmechanisme)."
    },
    {
      type: "open",
      vraag: "Wat is het verschil tussen private kosten en externe kosten? Geef een voorbeeld.",
      sleutelwoorden: ["private kosten/bedrijf zelf/grondstoffen/lonen", "externe kosten/maatschappij/derden/natuur", "voorbeeld/luchtvervuiling/schade"],
      minTreffers: 2,
      modelantwoord: "Private kosten zijn de kosten die de maker of koper zelf betaalt (zoals benzinekosten voor een auto of loonkosten voor een fabriek). Externe kosten zijn kosten die niet door de koper of verkoper worden gedragen, maar door de samenleving (zoals de kosten voor het opruimen van luchtvervuiling of gezondheidsschade door fijnstof).",
      uitleg: "Private kosten = markttransactie. Externe kosten = afgewentelde schade."
    }
  ]
});
