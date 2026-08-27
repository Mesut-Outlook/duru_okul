/* Proeftoets 13 — Natuurkunde HAVO 3: Hoofdstuk 3 (Straling - Deel 3)
   Focus: Paragraaf 3.3 — Gevaren van straling, bestraling vs. besmetting, achtergrondstraling en bescherming.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-natuurkunde-13",
  titel: "Toets 13 — Gevaren van Straling, Besmetting & Bescherming",
  vak: "Natuurkunde · HAVO 3 (H3)",
  icoon: "☢️",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het belangrijkste verschil tussen <b>bestraling</b> en <b>besmetting</b>?",
      opties: [
        "Bij bestraling word je van buitenaf getroffen door straling zonder dat je zelf radioactief wordt; bij besmetting zit de radioactieve stof op of in je lichaam en blijft van binnenuit stralen",
        "Bestraling is altijd dodelijk, besmetting nooit",
        "Bij bestraling slik je radioactief poeder in",
        "Er is natuurkundig geen enkel verschil"
      ],
      antwoord: 0,
      uitleg: "Bestraling = blootstelling van buitenaf (stopt zodra bron weg is). Besmetting = radioactieve deeltjes op kleding/huid of ingeademd/ingeslikt."
    },
    {
      type: "mc",
      vraag: "Wat is <b>achtergrondstraling</b>?",
      opties: [
        "Straling die alleen ontstaat bij kernproeven",
        "De natuurlijke radioactieve straling die altijd en overal om ons heen aanwezig is (uit de bodem, bouwmaterialen en het heelal)",
        "Straling die uit je mobiele telefoon komt",
        "Straling die alleen 's nachts actief is"
      ],
      antwoord: 1,
      uitleg: "Achtergrondstraling is overal aanwezig en komt uit kosmische straling, gesteente, radongas in huis en voedsel (kalium-40)."
    },
    {
      type: "invul",
      vraag: "Wat is de officiële eenheid waarin de biologische schade van geabsorbeerde straling op het menselijk lichaam wordt uitgedrukt (de equivalente dosis)?",
      antwoord: "Sievert|Sv|milliSievert|mSv|sievert",
      uitleg: "Stralingsdosis wordt uitgedrukt in Sievert (Sv) of millisievert (mSv). 1 Sv = 1000 mSv."
    },
    {
      type: "mc",
      vraag: "Welke drie gouden regels gelden voor <b>stralingsbescherming</b>?",
      opties: [
        "Afstand vergroten, tijd zo kort mogelijk houden, en goede afscherming gebruiken (lood/beton)",
        "Snel rennen, warm aankleden en water drinken",
        "Ramen openzetten, zonlicht vermijden en batterijen verwijderen",
        "Straling absorberen met aluminiumfolie op je hoofd"
      ],
      antwoord: 0,
      uitleg: "De 3 beschermingsregels: 1) Afstand zo groot mogelijk, 2) Verblijftijd zo kort mogelijk, 3) Afscherming (lood, beton)."
    },
    {
      type: "waaronwaar",
      vraag: "Als je bij de tandarts een röntgenfoto hebt laten maken, ben je na afloop zelf radioactief en mag je 24 uur lang niemand aanraken.",
      antwoord: false,
      uitleg: "Niet waar. Je bent slechts bestraald. Er blijft geen straling of radioactieve stof in je lichaam achter; je zendt zelf geen straling uit."
    },
    {
      type: "mc",
      vraag: "Waarom is <b>besmetting met een alfastraler</b> (zoals inademen van radongas of plutoniumstof) in het lichaam levensgevaarlijk, terwijl alfastraling van buitenaf ongevaarlijk is?",
      opties: [
        "Omdat alfadeeltjes in het lichaam direct in contact komen met levende cellen en door hun grote massa en lading zware DNA-schade veroorzaken",
        "Omdat alfastraling in het lichaam verandert in gammastraling",
        "Omdat alfastraling het bloed laat koken",
        "Omdat alfadeeltjes giftig zijn voor de maagwand"
      ],
      antwoord: 0,
      uitleg: "Buiten het lichaam stopt de dode huidlaag alfa; binnenin het lichaam richten de zware deeltjes direct enorme cel- en DNA-schade aan in de longen/organen."
    },
    {
      type: "invul",
      vraag: "Hoeveel millisievert (mSv) is de gemiddelde natuurlijke achtergrondstraling die een inwoner van Nederland per jaar ontvangt?",
      antwoord: "2|2 à 2,5|2,5|2 mSv|2,5 mSv|2-3",
      uitleg: "In Nederland ontvangt men gemiddeld circa 2,0 tot 2,5 mSv per jaar aan achtergrond- en medische straling."
    },
    {
      type: "waaronwaar",
      vraag: "Piloten en cabinepersoneel ontvangen per jaar meer straling dan gemiddeld doordat er op grote vlieghoogte minder atmosfeer is om kosmische straling uit het heelal tegen te houden.",
      antwoord: true,
      uitleg: "Waar. Op 10 km hoogte is de kosmische stralingsintensiteit veel hoger dan op zeeniveau."
    },
    {
      type: "mc",
      vraag: "Wat draagt een radiologisch medewerker in het ziekenhuis op zijn kleding om te controleren hoeveel straling hij in de loop van de tijd heeft opgevangen?",
      opties: [
        "Een persoonlijke dosismeter (badge)",
        "Een koperen munt",
        "Een infraroodbril",
        "Een UV-sensor"
      ],
      antwoord: 0,
      uitleg: "Een dosismeter (film- of TLD-badge) registreert de cumulatieve stralingsdosis over weken of maanden."
    },
    {
      type: "mc",
      vraag: "Als je de afstand tot een kleine radioactieve puntbron <b>twee keer zo groot</b> maakt (van 1 m naar 2 m), wordt de stralingsintensiteit:",
      opties: [
        "Twee keer zo klein",
        "Vier keer zo klein (omgekeerde kwadratenwet: 1/2² = 1/4)",
        "Acht keer zo klein",
        "Blijft gelijk"
      ],
      antwoord: 1,
      uitleg: "Volgens de omgekeerde kwadratenwet ($I \sim 1/r^2$) daalt de intensiteit met een factor 4 bij verdubbeling van de afstand."
    },
    {
      type: "waaronwaar",
      vraag: "DNA-schade in een lichaamscel door ioniserende straling kan door de cel zelf gerepareerd worden, maar bij foute reparatie kan een tumor (kanker) ontstaan.",
      antwoord: true,
      uitleg: "Waar. Cellen hebben herstelmechanismen, maar bij ernstige of foutieve reparatie kan ongecontroleerde celdeling ontstaan."
    },
    {
      type: "invul",
      vraag: "Welk edelgas ontstaat door natuurlijk radioactief verval van uranium en radium in de bodem en kan zich ophopen in kruipruimtes en slecht geventileerde woningen?",
      antwoord: "radon|radongas|radon-222",
      uitleg: "Radongas (Rn-222) is een radioactief alfastralend gas dat uit de bodem en stenen bouwmaterialen vrijkomt."
    },
    {
      type: "mc",
      vraag: "Waarom worden na een ernstig kernongeval (zoals bij Tsjernobyl of Fukushima) <b>jodiumtabletten</b> uitgedeeld aan omwonenden?",
      opties: [
        "Om radioactieve straling direct te neutraliseren",
        "Om de schildklier te verzadigen met ongevaarlijk stabiel jodium, zodat schadelijk radioactief jodium-131 niet wordt opgenomen",
        "Om de huid ongevoelig te maken voor alfastraling",
        "Om besmet water drinkbaar te maken"
      ],
      antwoord: 1,
      uitleg: "De schildklier slaat jodium op. Door stabiel jodium in te nemen raakt de klier vol en wordt het gevaarlijke radioactieve jodium-131 meteen uitgescheiden."
    },
    {
      type: "waaronwaar",
      vraag: "Voedsel dat met gammastraling is behandeld om bacteriën en schimmels te doden (sterilisatie) wordt daardoor zelf radioactief en gevaarlijk om op te eten.",
      antwoord: false,
      uitleg: "Niet waar. Het voedsel wordt alleen bestraald. Er blijft geen radioactieve stof in het eten achter; het voedsel is volkomen veilig en langer houdbaar."
    },
    {
      type: "mc",
      vraag: "Wat is acute stralingsziekte?",
      opties: [
        "Een verkoudheid door koude stralen",
        "Een ernstige ziekte die ontstaat na blootstelling aan een zeer hoge stralingsdosis in korte tijd (schade aan beenmerg, darmen en bloed)",
        "Een allergie voor zonlicht",
        "Een ontsteking van de botten door calciumgebrek"
      ],
      antwoord: 1,
      uitleg: "Bij hoge doses (> 1 Sv ineens) sterven snel delende cellen massaal af, wat leidt tot misselijkheid, bloedingen en afweeruitval."
    },
    {
      type: "invul",
      vraag: "Een radioloog staat op 1 meter afstand van een bron en meet een dosistempo van 16 μSv/h. Hij doet twee stappen achteruit naar een afstand van 4 meter. Wat is het nieuwe dosistempo in μSv/h (4× grotere afstand)?",
      antwoord: "1|1 μSv/h|1 uSv/h",
      uitleg: "Afstand wordt 4× zo groot -> intensiteit wordt 4² = 16× zo klein: 16 / 16 = 1 μSv/h."
    },
    {
      type: "waaronwaar",
      vraag: "Mensen die werken met radioactiviteit dragen speciale beschermende pakken en maskers vooral om <b>inwendige besmetting</b> te voorkomen.",
      antwoord: true,
      uitleg: "Waar. De overalls en maskers voorkomen dat radioactief stof op de huid komt of wordt ingeademd."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er met kleding die besmet is geraakt met radioactief stof?",
      opties: [
        "Die kan gewoon in de wasmachine bij 40 graden gewassen worden",
        "Die moet worden uitgetrokken, in afgesloten zakken worden opgeborgen en als radioactief afval worden afgevoerd",
        "Die moet 5 minuten in de zon gelegd worden",
        "Die wordt direct met chloor geneutraliseerd"
      ],
      antwoord: 1,
      uitleg: "Besmette kleding wordt zorgvuldig verwijderd en als radioactief afval opgeslagen tot de stof is uitgestorven."
    },
    {
      type: "open",
      vraag: "Leg uit waarom het opruimen van radioactief stof na een kernongeval veel gevaarlijker is dan het passeren van een röntgenapparaat. Gebruik de begrippen <b>besmetting</b>, <b>bestraling</b> en <b>stralingsduur</b>.",
      sleutelwoorden: ["röntgen is alleen kortstondige bestraling", "radioactief stof veroorzaakt besmetting", "blijft continu van binnenuit stralen"],
      minTreffers: 2,
      modelantwoord: "Bij een röntgenapparaat is er slechts sprake van kortstondige bestraling van buitenaf; zodra het apparaat uit staat is er geen straling meer. Radioactief stof veroorzaakt echter besmetting: als de deeltjes op je kleding/huid komen of worden ingeademd/ingeslikt, blijven ze 24 uur per dag van binnenuit je organen bestralen (zeer lange stralingsduur), wat leidt tot ernstige DNA- en weefselschade.",
      uitleg: "Kortstondige externe bestraling vs. continue langdurige inwendige besmetting."
    },
    {
      type: "open",
      vraag: "Noem de drie belangrijkste maatregelen om de stralingsdosis voor werknemers in een ziekenhuis zo laag mogelijk te houden en licht bij elk kort toe hoe het werkt.",
      sleutelwoorden: ["afstand vergroten", "tijd verkorten", "afscherming/lood gebruiken"],
      minTreffers: 3,
      modelantwoord: "1. Afstand vergroten: Door afstand te houden van de bron daalt de stralingsintensiteit kwadratisch (omgekeerde kwadratenwet).\n2. Tijd verkorten: Door zo kort mogelijk in de buurt van de stralingsbron te verblijven, is de totale opgenomen dosis minimaal ($Dosis = tempo \times tijd$).\n3. Afscherming: Door loden schorten, loden schermen of dikke wanden te gebruiken, wordt de straling geabsorbeerd voordat deze het lichaam bereikt.",
      uitleg: "De 3 pijlers van stralingsbescherming: Afstand, Tijd en Afscherming."
    }
  ]
});
