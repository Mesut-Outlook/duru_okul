/* Extra Proeftoets 7 — Milieu & Overheidsbeleid */
DURU.registerExamen({
  id: "ex-extra-milieu-beleid",
  titel: "Extra Proeftoets 7 — Milieu & Overheidsbeleid",
  vak: "Economie · Milieubeleid",
  icoon: "🌱",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is in de economie een negatief extern effect?",
      opties: [
        "Een stijging van de btw die de prijzen verhoogt.",
        "Onbedoelde schade van productie of consumptie die buiten de markt om de samenleving treft.",
        "Een boete die je krijgt als je te snel rijdt.",
        "De afname van het aantal banen in de chemische industrie."
      ],
      antwoord: 1,
      uitleg: "Een <b>negatief extern effect</b> is schade voor derden die niet is meegerekend in de prijs van het product (bijv. luchtvervuiling door een fabriek of geluidsoverlast door vliegverkeer)."
    },
    {
      type: "mc",
      vraag: "Welke heffing gebruikt de overheid om autobezitters te stimuleren een schonere auto te kopen?",
      opties: [
        "De toeristenbelasting.",
        "Milieudifferentiatie in de motorrijtuigenbelasting en bpm (vervuilende auto's betalen meer).",
        "Een vast btw-tarief van 50% op benzine.",
        "Hogere boetes voor foutparkeren."
      ],
      antwoord: 1,
      uitleg: "Door vervuilende auto's zwaarder te belasten (hogere bpm en wegenbelasting) maakt de overheid **schone auto's** relatief goedkoper en aantrekkelijker."
    },
    {
      type: "mc",
      vraag: "Waarom geeft de overheid subsidies voor zonnepanelen, isolatie en warmtepompen?",
      opties: [
        "Om de inkomsten van de overheid te verhogen.",
        "Om duurzaam gedrag te stimuleren en de CO2-uitstoot te verlagen.",
        "Omdat de installateurs van zonnepanelen vrienden zijn van de ministers.",
        "Om te zorgen dat mensen minder stroom gaan gebruiken."
      ],
      antwoord: 1,
      uitleg: "Met **subsidies** stimuleert de overheid de consumptie van milieuvriendelijke alternatieven (meritorische goederen)."
    },
    {
      type: "mc",
      vraag: "Wat houdt het economische principe 'de vervuiler betaalt' in?",
      opties: [
        "De overheid betaalt alle schade die door fabrieken wordt veroorzaakt.",
        "De kosten van milieuvervuiling worden via heffingen doorberekend aan de producent of consument die het veroorzaakt.",
        "Als je zwerfafval opruimt, krijg je geld van de gemeente.",
        "Bedrijven die vervuilen hoeven geen belasting meer te betalen."
      ],
      antwoord: 1,
      uitleg: "Dit principe zorgt ervoor dat de maatschappelijke kosten (schade) van vervuiling in de prijs van het product terechtkomen (**internaliseren**), waardoor het product duurder en minder populair wordt."
    },
    {
      type: "mc",
      vraag: "Welk van de volgende goederen probeert de overheid juist te stimuleren omdat ze positieve effecten hebben op de maatschappij?",
      opties: [
        "Vliegreizen naar zonnige bestemmingen.",
        "Het gebruik van plastic verpakkingen.",
        "Het openbaar vervoer (trein en bus) en onderwijs.",
        "De productie van steenkool."
      ],
      antwoord: 2,
      uitleg: "Het openbaar vervoer en onderwijs hebben **positieve externe effecten** (minder files, beter opgeleide bevolking). De overheid subsidieert deze meritorische goederen."
    },
    {
      type: "waaronwaar",
      vraag: "Een milieuheffing (zoals op plastic tasjes of verpakkingen) is bedoeld om de consumptie van die producten te ontmoedigen.",
      antwoord: true,
      uitleg: "Waar. Door een heffing stijgt de prijs, waardoor consumenten het product minder snel kopen en bewuster omgaan met het milieu."
    },
    {
      type: "waaronwaar",
      vraag: "Positieve externe effecten zijn nadelen van consumptie waar de samenleving voor moet betalen.",
      antwoord: false,
      uitleg: "Onwaar. Positieve externe effecten zijn **voordelen** voor de samenleving waar de veroorzaker niet voor wordt betaald (bijvoorbeeld een mooi onderhouden voortuin of een gevaccineerd persoon die anderen niet besmet)."
    },
    {
      type: "invul",
      vraag: "Een extra belasting op milieuvervuilende producten noemen we een milieu_______.",
      antwoord: "heffing|heffingen",
      uitleg: "Een <b>milieuheffing</b> maakt vervuilende producten duurder, zodat de vervuiler meebetaalt aan de schade."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de overheid negatieve externe effecten van productie (bijvoorbeeld fijnstof uit een fabriek) kan aanpakken met wetgeving.",
      sleutelwoorden: ["verbod/verbieden/eisen", "normen/grenswaarden/limiet/filter", "boete/boetes/stilleggen/straffen"],
      minTreffers: 2,
      modelantwoord: "De overheid kan strenge milieueisen of normen stellen (bijvoorbeeld een verplicht roetfilter of een maximum aan de uitstoot). Als een fabriek zich hier niet aan houdt, kan de overheid boetes opleggen of de fabriek tijdelijk stilleggen.",
      uitleg: "Gebruik van gebod- en verbodswetgeving (directe regulering) dwingt bedrijven schoner te produceren."
    },
    {
      type: "open",
      vraag: "Geef een voorbeeld van een negatief extern effect van vliegverkeer en leg uit waarom dit een extern effect is.",
      sleutelwoorden: ["geluidsoverlast/fijnstof/co2/klimaatverandering", "schade/overlast/omwonenden/samenleving", "niet in prijs/prijs van ticket/niet betaald"],
      minTreffers: 2,
      modelantwoord: "Een voorbeeld is geluidsoverlast voor omwonenden van een vliegveld of de CO2-uitstoot die bijdraagt aan klimaatverandering. Dit is een extern effect omdat de omwonenden en de maatschappij de lasten dragen, terwijl deze schade niet volledig is doorberekend in de prijs van het vliegticket.",
      uitleg: "Externe kosten = maatschappelijke kosten die buiten de markttransactie vallen."
    }
  ]
});
