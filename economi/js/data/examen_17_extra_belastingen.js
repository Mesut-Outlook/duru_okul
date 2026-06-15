/* Extra Proeftoets 12 — Belastingen & Berekeningen */
DURU.registerExamen({
  id: "ex-extra-belastingen-berekeningen",
  titel: "Extra Proeftoets 12 — Belastingen & Berekeningen",
  vak: "Economie · Berekeningen",
  icoon: "🧮",
  duurMin: 15,
  vragen: [
    {
      type: "mc",
      vraag: "Een spelcomputer kost €242,- inclusief 21% btw. Wat is de prijs van deze spelcomputer exclusief btw?",
      opties: [
        "€ 191,18",
        "€ 200,00",
        "€ 221,00",
        "€ 292,82"
      ],
      antwoord: 1,
      uitleg: "De prijs inclusief btw is 121%. De prijs exclusief btw is: **242 / 1,21 = € 200,00**."
    },
    {
      type: "mc",
      vraag: "Een boek kost inclusief 9% btw € 32,70. Wat is het btw-bedrag dat in de prijs zit verwerkt?",
      opties: [
        "€ 2,70",
        "€ 2,94",
        "€ 3,00",
        "€ 29,73"
      ],
      antwoord: 0,
      uitleg: "De prijs inclusief btw is 109%. De btw bedraagt: **(32,70 / 109) * 9 = € 2,70**."
    },
    {
      type: "mc",
      vraag: "In een progressief belastingstelsel geldt: hoe hoger je inkomen,...",
      opties: [
        "... hoe lager het belastingtarief in procenten wordt.",
        "... hoe hoger het percentage belasting dat je gemiddeld betaalt.",
        "... hoe minder inkomstenbelasting je in euro's betaalt.",
        "... hoe lager de btw die je in winkels betaalt."
      ],
      antwoord: 1,
      uitleg: "Een **progressief stelsel** werkt met schijven. Naarmate je meer verdient, stijgt het percentage belasting (tarief) over je inkomen."
    },
    {
      type: "mc",
      vraag: "Daan verdient bruto € 2500,- per maand. Er wordt € 750,- aan loonheffing ingehouden. Wat is het netto-inkomen van Daan per maand?",
      opties: [
        "€ 3250,-",
        "€ 1750,-",
        "€ 2000,-",
        "€ 1250,-"
      ],
      antwoord: 1,
      uitleg: "Netto-inkomen = bruto-inkomen - loonheffing (belasting/premies). **2500 - 750 = € 1750,-**."
    },
    {
      type: "mc",
      vraag: "Een winkelier koopt een jas in voor € 50,- exclusief btw. Hij wil 21% btw berekenen aan de klant. Wat wordt de verkoopprijs inclusief btw?",
      opties: [
        "€ 71,00",
        "€ 60,50",
        "€ 50,21",
        "€ 52,10"
      ],
      antwoord: 1,
      uitleg: "Btw bedraagt: **50 * 0,21 = € 10,50**. Verkoopprijs = **50 + 10,50 = € 60,50** (of direct **50 * 1,21 = 60,50**)."
    },
    {
      type: "waaronwaar",
      vraag: "Loonheffing (loonbelasting) is een voorbeeld van een indirecte belasting omdat je werkgever het voor je betaalt.",
      antwoord: false,
      uitleg: "Onwaar. Loonheffing is een **directe belasting** (het drukt rechtstreeks op jouw inkomen). Dat de werkgever het inhoudt en afdraagt, verandert het type belasting niet."
    },
    {
      type: "waaronwaar",
      vraag: "Als de overheid de btw verhoogt, stijgen de prijzen in de winkel voor de consument.",
      antwoord: true,
      uitleg: "Waar. De btw is een belasting op consumptie. Een btw-verhoging wordt door winkeliers doorberekend aan de eindgebruiker."
    },
    {
      type: "invul",
      vraag: "Je verdient bruto € 400,- per maand. Je betaalt 25% loonheffing. Hoeveel euro houd je netto over?",
      antwoord: "300",
      uitleg: "Loonheffing is 25% van 400 = € 100,-. Netto-inkomen = **400 - 100 = 300 euro**."
    },
    {
      type: "open",
      vraag: "Leg uit hoe je de btw en de prijs exclusief btw berekent van een product dat inclusief 21% btw € 181,50 kost.",
      sleutelwoorden: ["inclusief/121%", "delen door 1,21/exclusief/€150", "btw-bedrag/btw is/€31,50/aftrekken"],
      minTreffers: 2,
      modelantwoord: "De prijs inclusief btw is 121%. Om de prijs exclusief btw te berekenen, deel je het bedrag door 1,21 (181,50 / 1,21 = € 150,-). De btw bereken je vervolgens door het verschil te nemen (181,50 - 150 = € 31,50) of door (181,50 / 121) * 21 te doen.",
      uitleg: "Formule: Excl = Incl / 1,21. Btw = Incl - Excl."
    },
    {
      type: "open",
      vraag: "Waarom houdt de overheid loonbelasting in als voorheffing op de inkomstenbelasting?",
      sleutelwoorden: ["maandelijks/voorheffing/vooraf", "gemak/belastingdienst/zekerheid", "achteraf/geen grote schuld/inkomstenbelasting verrekenen"],
      minTreffers: 2,
      modelantwoord: "De loonbelasting wordt maandelijks ingehouden zodat de overheid gedurende het jaar alvast inkomsten ontvangt (voorheffing). Dit voorkomt dat burgers achteraf bij de definitieve inkomstenbelasting in één keer een heel groot bedrag moeten betalen en zorgt voor stabiele inkomsten voor de schatkist.",
      uitleg: "Inhouding bij de bron = efficiënt en voorkomt betalingsproblemen achteraf."
    }
  ]
});
