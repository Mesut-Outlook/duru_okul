/* Proeftoets 15 — Natuurkunde HAVO 3: Hoofdstuk 3 (Straling - Integrale Eindtoets)
   Focus: Volledig Hoofdstuk 3 (§3.1 t/m §3.5) — Kernenergie, kernsplijting, kettingreacties en integrale opgaven.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-15",
  titel: "Toets 15 — Kernenergie & Integrale Eindtoets Hoofdstuk 3",
  vak: "Natuurkunde · HAVO 3 (H3)",
  icoon: "🏆",
  duurMin: 35,
  vragen: [
    {
      type: "mc",
      vraag: "Welk proces vindt plaats in de kern van een kerncentrale om energie op te wekken?",
      opties: [
        "Kernsplijting van zware Uranium-235 kernen",
        "Kernfusie van waterstofatomen",
        "Chemische verbranding van uraniumpoeder",
        "Elektrolyse van zwaar water"
      ],
      antwoord: 0,
      uitleg: "In een kernreactor worden zware Uranium-235 kernen gespleten door invangst van langzame neutronen."
    },
    {
      type: "mc",
      vraag: "Wat ontstaat er wanneer een Uranium-235 kern een langzaam neutron invangt en splitst?",
      opties: [
        "Eén grotere plutoniumkern en zuurstof",
        "Twee middelzware dochterkernen, 2 à 3 nieuwe snelle neutronen en een enorme hoeveelheid energie (warmte)",
        "Alleen alfadeeltjes zonder energie",
        "Waterdamp en koolstofdioxide"
      ],
      antwoord: 1,
      uitleg: "Bij kernsplijting splitst de kern in 2 splijtingsproducten, komen er 2 tot 3 neutronen vrij en komt er gigantisch veel warmte-energie vrij."
    },
    {
      type: "waaronwaar",
      vraag: "Een kettingreactie in een kernreactor ontstaat doordat de vrijgekomen neutronen uit eerdere splijtingen weer nieuwe uraniumkernen kunnen raken en splijten.",
      antwoord: true,
      uitleg: "Waar. Dit heet een kettingreactie: 1 splijting veroorzaakt meerdere volgende splijtingen."
    },
    {
      type: "mc",
      vraag: "Wat is de functie van de <b>regelstaven</b> (van bijv. boor of cadmium) in een kernreactor?",
      opties: [
        "De reactor extra heet stoken",
        "Straling omzetten in elektriciteit",
        "Overtollige neutronen absorberen om de kettingreactie te beheersen of de reactor stil te leggen",
        "Het koelwater zuiveren"
      ],
      antwoord: 2,
      uitleg: "Regelstaven vangen neutronen weg. Door ze dieper in de reactor te laten zakken, stopt de kettingreactie."
    },
    {
      type: "invul",
      vraag: "Hoe heet het onderdeel in een kerncentrale dat door de stoom wordt aangedreven en op zijn beurt de generator laat draaien?",
      antwoord: "turbine|stoomturbine|de turbine",
      uitleg: "Hogedrukstoom blaast tegen de schoepen van de turbine, die de generator aandrijft."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste <b>milieuvoordeel</b> van kernenergie vergeleken met een kolen- of gascentrale?",
      opties: [
        "Het koelwater kan direct als mineraalwater verkocht worden",
        "Er ontstaat helemaal geen afval",
        "De bouw van een kerncentrale kost bijna niets",
        "Bij de stroomopwekking in een kernreactor komt vrijwel geen CO₂ (broeikasgas) vrij"
      ],
      antwoord: 3,
      uitleg: "Kerncentrales stoten tijdens bedrijf geen broeikasgassen (zoals CO₂) of roet uit."
    },
    {
      type: "mc",
      vraag: "Wat is het belangrijkste <b>nadeel</b> en risico van kernenergie?",
      opties: [
        "Het ontstaan van hoogradioactief kernafval dat tienduizenden jaren veilig moet worden opgeslagen",
        "Dat de stroom te koud is voor stopcontacten",
        "Dat kernenergie alleen 's nachts werkt",
        "Dat uranium binnen 2 jaar volledig op is"
      ],
      antwoord: 0,
      uitleg: "Kernafval blijft duizenden jaren gevaarlijk radioactief en vereist diepe, veilige geologische eindberging."
    },
    {
      type: "waaronwaar",
      vraag: "De dikke betonnen koepel (containment) om het reactorvat dient om te voorkomen dat er bij een calamiteit radioactiviteit in het milieu ontsnapt.",
      antwoord: true,
      uitleg: "Waar. De containment is een metersdikke bunker van gewapend beton en staal."
    },
    {
      type: "invul",
      vraag: "Een hoeveelheid Jodium-131 ($t_{1/2} = 8\text{ dagen}$) heeft een beginactiviteit van 160 kBq. Na hoeveel dagen is de activiteit gedaald tot 10 kBq?",
      antwoord: "32|32 dagen|32 d",
      uitleg: "160 -> 80 -> 40 -> 20 -> 10 kBq = 4 halveringstijden. Tijd = 4 × 8 dagen = 32 dagen."
    },
    {
      type: "mc",
      vraag: "Welke soort straling ontstaat bij het verval van Radon-222 in de woning?",
      opties: [
        "Röntgenstraling",
        "Alfastraling",
        "Microgolven",
        "Infraroodstraling"
      ],
      antwoord: 1,
      uitleg: "Radon-222 is een alfastraler; inademing van radongas levert risico op longkanker."
    },
    {
      type: "waaronwaar",
      vraag: "In het elektromagnetisch spectrum hebben microgolven een hogere frequentie en meer energie dan radiogolven.",
      antwoord: true,
      uitleg: "Waar. Microgolven zitten tussen radiogolven en infrarood in."
    },
    {
      type: "invul",
      vraag: "Een atoomkern van Uranium-238 ($^{238}_{92}\text{U}$) zendt een alfadeeltje ($^{4}_{2}\text{He}$) uit. Wat is het massagetal van de ontstane dochterkern (Thorium)?",
      antwoord: "234",
      uitleg: "Massagetal = 238 - 4 = 234 ($^{234}_{90}\text{Th}$)."
    },
    {
      type: "mc",
      vraag: "Wat is de functie van de <b>moderator</b> (bijv. water of grafiet) in een kernreactor?",
      opties: [
        "Het uranium laten smelten",
        "De elektriciteit opslaan in batterijen",
        "De snelle neutronen afremmen tot langzame neutronen, zodat ze makkelijker uraniumkernen kunnen splijten",
        "De turbine sneller laten draaien"
      ],
      antwoord: 2,
      uitleg: "Snelle neutronen ketsen te snel af; een moderator vertraagt ze zodat kernsplijting optimaal verloopt."
    },
    {
      type: "waaronwaar",
      vraag: "Bij een kernongeval is het koelhouden van de reactor cruciaal, omdat de splijtingsproducten na uitschakeling nog langere tijd nawarmte produceren.",
      antwoord: true,
      uitleg: "Waar. Zonder noodkoeling kan de reactorkern oververhitten en smelten (meltdown)."
    },
    {
      type: "invul",
      vraag: "Reken om: een stralingsdosis van 2500 μSv (microsievert) is gelijk aan hoeveel millisievert (mSv)?",
      antwoord: "2,5|2,5 mSv|2.5",
      uitleg: "1 mSv = 1000 μSv. Dus 2500 / 1000 = 2,5 mSv."
    },
    {
      type: "mc",
      vraag: "Waarom is goede ventilatie in een nieuwbouwwoning belangrijk met betrekking tot radioactiviteit?",
      opties: [
        "Om te voorkomen dat de wifi-straling blijft hangen",
        "Om de zwaartekracht laag te houden",
        "Omdat elektronen anders niet kunnen bewegen",
        "Om te voorkomen dat radioactief radongas uit betonnen muren en de kruipruimte zich ophoopt in de leefruimte"
      ],
      antwoord: 3,
      uitleg: "Ventilatie voert radongas en thorongas uit bouwmaterialen continu af naar buiten."
    },
    {
      type: "waaronwaar",
      vraag: "Alfastraling heeft een lading van +2, bètastraling een lading van -1 en gammastraling heeft geen elektrische lading (0).",
      antwoord: true,
      uitleg: "Waar. Alfa = He²⁺ (+2), Bèta = elektron (-1), Gamma = foton (0)."
    },
    {
      type: "invul",
      vraag: "In een ziekenhuis wordt een radioactieve bron afgeschermd met loden platen. Eén loden plaat van 1,5 cm dikte halveert de stralingsintensiteit (halveringsdikte $d_{1/2} = 1{,}5\text{ cm}$). Hoeveel cm lood is er nodig om de straling terug te brengen tot 12,5% (drie halveringen)?",
      antwoord: "4,5|4,5 cm|4.5",
      uitleg: "3 halveringsdiktes: 3 × 1,5 cm = 4,5 cm lood."
    },
    {
      type: "open",
      vraag: "Leg stap voor stap uit hoe in een kerncentrale elektrische stroom wordt opgewekt, vanaf de kernsplijting tot de elektriciteit op het hoogspanningsnet.",
      sleutelwoorden: ["kernsplijting levert warmte", "water verdampt tot stoom", "stoom drijft turbine aan", "generator wekt elektriciteit op"],
      minTreffers: 3,
      modelantwoord: "1. In het reactorvat vindt gecontroleerde kernsplijting van uranium plaats, waarbij een enorme hoeveelheid warmte-energie vrijkomt.\n2. Deze warmte verhit het koelwater, dat via een stoomgenerator water in een tweede circuit omzet in stoom onder hoge druk.\n3. De krachtige stoom blaast tegen de schoepen van een stoomturbine en laat deze met hoge snelheid ronddraaien.\n4. De as van de turbine drijft een generator (dynamo) aan, die de mechanische draaienergie via elektromagnetische inductie omzet in elektrische wisselspanning voor het stroomnet.",
      uitleg: "Kernenergie -> warmte -> stoom -> turbine (beweging) -> generator (elektriciteit)."
    },
    {
      type: "open",
      vraag: "Bespreek de voor- en nadelen van kernenergie in het kader van het klimaat en de energievoorziening. Noem minimaal twee duidelijke voordelen en twee duidelijke nadelen/risico's.",
      sleutelwoorden: ["geen CO2/geen CO₂/CO2-vrij/geen uitstoot", "betrouwbaar/continu/leveringszekerheid/weersonafhankelijk/hoge opbrengst", "kernafval/radioactief afval/opslag van afval", "ongeluk/ongeval/meltdown/ramp/veiligheidsrisico/hoge bouwkosten/dure bouw"],
      minTreffers: 3,
      modelantwoord: "Voordelen:\n1. Geen directe CO₂-uitstoot tijdens energieproductie (draagt niet bij aan het broeikaseffect).\n2. Hoge leveringszekerheid: levert continu en weersonafhankelijk grote hoeveelheden basislast-stroom.\n\nNadelen:\n1. Hoogradioactief kernafval dat duizenden jaren extreem veilig opgeslagen moet worden.\n2. Kans op catastrofale kernongevallen (meltdown, vrijkomen van straling) en zeer hoge kosten/lange bouwtijd voor nieuwe reactoren.",
      uitleg: "Evenwichtige bespreking van CO2-vrije betrouwbare stroom vs. kernafval, veiligheidsrisico's en bouwkosten."
    }
  ]
});
