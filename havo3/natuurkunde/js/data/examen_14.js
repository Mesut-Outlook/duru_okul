/* =========================================================
   Duru's Natuurkunde (HAVO 3) — Toets 14 — Toepassingen van Straling & Medische Beeldvorming
   ========================================================= */
DURU.registerExamen({
  "id": "ex-h3-natuurkunde-14",
  "hoofdstuk": 3,
  "titel": "Toets 14 — Toepassingen van Straling & Medische Beeldvorming",
  "vak": "Natuurkunde · HAVO 3 (H3)",
  "icoon": "🔬",
  "duurMin": 30,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat is een <b>tracer</b> (speurstof) in het ziekenhuis?",
      "opties": [
        "Een radioactieve stof met korte halveringstijd die bij een patiënt wordt ingebracht om organen of bloedstromen te onderzoeken",
        "Een chirurgisch mes met laser",
        "Een soort loden schort",
        "Een speciaal slaapmiddel"
      ],
      "antwoord": 0,
      "uitleg": "Een tracer (vaak een gammastraler zoals Technetium-99m) verspreidt zich in het lichaam; een gammacamera vangt de straling op en maakt een beeld van de orgaanfunctie."
    },
    {
      "type": "mc",
      "vraag": "Waarom moet een radioactieve tracer die bij een patiënt wordt ingespoten een <b>korte halveringstijd</b> (bijv. enkele uren) hebben?",
      "opties": [
        "Omdat lange halveringstijden de camera beschadigen",
        "Zodat het onderzoek snel genoeg klaar is en de patiënt daarna niet onnodig lang van binnenuit bestraald blijft",
        "Omdat de stof anders bevriest",
        "Zodat het bloed sneller gaat stromen"
      ],
      "antwoord": 1,
      "uitleg": "Korte halveringstijd zorgt voor voldoende activiteit tijdens de scan, terwijl de radioactiviteit binnen 1 à 2 dagen vrijwel volledig uit het lichaam verdwenen is."
    },
    {
      "type": "waaronwaar",
      "vraag": "Voor een tracer in het lichaam gebruikt een arts bij voorkeur een <b>gammastraler</b> en GEEN alfastraler.",
      "antwoord": true,
      "uitleg": "Waar. Gammastraling kan dwars door het lichaam naar buiten reizen om door de camera gedetecteerd te worden met minimale lokale schade. Alfastraling zou niet naar buiten komen en zware interne weefselschade veroorzaken."
    },
    {
      "type": "mc",
      "vraag": "Wat is <b>radiotherapie</b> (bestraling bij kanker)?",
      "opties": [
        "Het luisteren naar radioberichten ter ontspanning",
        "Het wassen van de huid met radioactieve zeep",
        "Het gericht bestralen van een kwaadaardige tumor met ioniserende straling om kankercellen te doden",
        "Een dieet met kaliumrijke bananen"
      ],
      "antwoord": 2,
      "uitleg": "Bij radiotherapie worden tumorcellen vanuit verschillende hoeken met sterke stralenbündels bestraald zodat de tumor sterft terwijl het gezonde weefsel gespaard blijft."
    },
    {
      "type": "invul",
      "vraag": "Welk medisch apparaat maakt met behulp van een ronddraaiende röntgenbuis en computers gedetailleerde 3D-dwarsdoorsneden van het menselijk lichaam?",
      "antwoord": "CT-scanner|CT-scan|CT scanner|CT scan|computertomograaf",
      "uitleg": "Een CT-scanner (Computer Tomografie) combineert honderden röntgenfoto's vanuit verschillende hoeken tot een 3D-doorsnede."
    },
    {
      "type": "mc",
      "vraag": "Hoe werkt een traditionele optische <b>rookmelder</b> of ionisatierookmelder in huis?",
      "opties": [
        "De melder luistert naar het knetteren van vuur",
        "De rookmelder meet de temperatuur van de kamer",
        "De melder ruikt chemische geuren met een koolstoffilter",
        "Rookdeeltjes blokkeren een lichtstraal of de ionisatiestroom van een kleine alfabron, waardoor het alarm afgaat"
      ],
      "antwoord": 3,
      "uitleg": "Rookdeeltjes verstoren het licht of de ionenstroom in de meetkamer, wat het alarm activeert."
    },
    {
      "type": "waaronwaar",
      "vraag": "Met behulp van een bètastralingsbron en een detector kan in een fabriek continu de dikte van geproduceerd papier of aluminiumfolie automatisch worden gemeten en bijgesteld.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. Als het papier dikker wordt, absorbeert het meer bètadeeltjes en meet de detector minder straling, waarna de walsen strakker worden gezet."
    },
    {
      "type": "mc",
      "vraag": "Waarom worden wegwerpspuiten, injectienaalden en operatiehandschoenen in de fabriek in hun plastic verpakking gesteriliseerd met <b>gammastraling</b>?",
      "opties": [
        "Omdat gammastraling door het plastic heen alle bacteriën en virussen doodt zonder dat de verpakking geopend hoeft te worden of warmte nodig is",
        "Omdat de naalden daardoor scherper worden",
        "Omdat het plastic daardoor flexibeler wordt",
        "Omdat chemicaliën te duur zijn"
      ],
      "antwoord": 0,
      "uitleg": "Gammastraling dringt door de verpakking heen en vernietigt DNA van micro-organismen (koude sterilisatie). Het materiaal blijft steriel in de dichte verpakking."
    },
    {
      "type": "invul",
      "vraag": "Welke elektromagnetische stralingssoort wordt gebruikt voor draadloze communicatie via Wi-Fi, 4G/5G en Bluetooth?",
      "antwoord": "radiogolven|microgolven|radio- en microgolven",
      "uitleg": "Draadloze netwerken zenden informatie uit via hoogfrequente radiogolven / microgolven (bijv. 2,4 GHz of 5 GHz)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het voordeel van een <b>PET-scan</b> (Positron Emissie Tomografie)?",
      "opties": [
        "Het kost helemaal geen elektriciteit",
        "Het kan actieve stofwisselingsprocessen en tumoren in een heel vroeg stadium opsporen via radioactief gelabeld glucose",
        "Het maakt alleen zwart-witfoto's van botten",
        "Het werkt met geluidsgolven"
      ],
      "antwoord": 1,
      "uitleg": "Kankercellen verbruiken veel suiker. Door radioactief suiker in te spuiten lichten tumoren fel op op de PET-scan."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een MRI-scan in het ziekenhuis maakt gebruik van gevaarlijke radioactieve ioniserende straling.",
      "antwoord": false,
      "uitleg": "Niet waar. Een MRI (Magnetic Resonance Imaging) werkt met een sterk magneetveld en onschadelijke radiogolven; er komt géén ioniserende straling aan te pas."
    },
    {
      "type": "mc",
      "vraag": "Wat is radiometrische <b>koolstofdatering (C-14 datering)</b> in de archeologie?",
      "opties": [
        "Het herstellen van oude schilderijen met UV-licht",
        "Het wegen van oude stenen",
        "Het bepalen van de ouderdom van oude organische voorwerpen (hout, botten) door het verval van Koolstof-14 te meten",
        "Het smelten van fossielen"
      ],
      "antwoord": 2,
      "uitleg": "Zolang een organisme leeft, neemt het C-14 op. Na het sterven vervalt het C-14 ($t_{1/2} approx 5730\text{ jaar}$); aan het restant meet men hoe lang geleden het organisme stierf."
    },
    {
      "type": "invul",
      "vraag": "Koolstof-14 heeft een halveringstijd van 5730 jaar. In een oud stuk hout uit een hunebed is nog maar 25% van de oorspronkelijke C-14 activiteit over. Hoe oud is dit hout in jaren?",
      "antwoord": "11460|11.460|11460 jaar",
      "uitleg": "25% over = 2 halveringstijden (100% -> 50% -> 25%). Ouderdom = 2 × 5730 jaar = 11.460 jaar."
    },
    {
      "type": "mc",
      "vraag": "Welke stralingssoort wordt gebruikt bij <b>bagagescanners</b> op luchthavens om door koffers heen te kijken?",
      "opties": [
        "Infraroodstraling",
        "Zichtbaar licht",
        "Alfastraling",
        "Röntgenstraling"
      ],
      "antwoord": 3,
      "uitleg": "Röntgenstralen dringen door kleding en kofferwanden heen en maken metalen voorwerpen en organische stoffen zichtbaar in verschillende kleuren."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij radiotherapie wordt de stralingsbron vanuit verschillende hoeken om de patiënt gedraaid, zodat de tumor maximaal bestraald wordt en omliggend gezond weefsel gespaard blijft.",
      "antwoord": false,
      "uitleg": "Onwaar: Waar. De stralenkruising zorgt dat alleen de tumor in het snijpunt de maximale dodelijke dosis ontvangt."
    },
    {
      "type": "mc",
      "vraag": "Waarom wordt voor lasnaadcontrole in stalen pijpleidingen (radiografie) een gammabron gebruikt?",
      "opties": [
        "Omdat gammastraling door dikke stalen wanden heen kan dringen om microscheurtjes op film zichtbaar te maken",
        "Omdat gammastraling het staal aan elkaar smelt",
        "Omdat gammastraling roest verwijdert",
        "Omdat het staal er mooier van gaat glanzen"
      ],
      "antwoord": 0,
      "uitleg": "Gammastraling dringt door centimeters staal; scheuren laten meer straling door en zijn direct zichtbaar op de film."
    },
    {
      "type": "invul",
      "vraag": "Welke straling wordt gebruikt om bankbiljetten te controleren op echtheidskenmerken en fluorescerende inkt?",
      "antwoord": "UV|UV-straling|ultraviolet|ultraviolette straling",
      "uitleg": "Onder ultraviolet licht lichten speciale fluorescerende vezels en inkt in echte bankbiljetten fel op."
    },
    {
      "type": "waaronwaar",
      "vraag": "Radiogolven hebben voldoende energie om moleculen in menselijke cellen rechtstreeks te ioniseren.",
      "antwoord": false,
      "uitleg": "Niet waar. Radiogolven zijn niet-ioniserend; de fotonenergie is veel te laag om elektronen uit atomen vrij te maken."
    },
    {
      "type": "open",
      "vraag": "Leg uit hoe een arts met een <b>radioactieve tracer</b> en een <b>gammacamera</b> een nieraandoening kan opsporen bij een patiënt.",
      "sleutelwoorden": [
        "tracer in bloedbaan spuiten",
        "gammastraling verlaat lichaam",
        "camera maakt beelden/functie zichtbaar"
      ],
      "minTreffers": 2,
      "modelantwoord": "De arts spuit een kleine hoeveelheid van een gammastralende tracer met korte halveringstijd in de bloedbaan. De nieren filteren deze stof uit het bloed. Omdat gammastraling makkelijk door het lichaam heen dringt, registreert de externe gammacamera waar en hoe snel de tracer zich ophoopt en wordt afgevoerd. Een verstopping of slecht functionerende nier is zo direct zichtbaar.",
      "uitleg": "Tracer -> orgaanopname -> gammastraling naar buiten -> camera maakt functie en doorstroming zichtbaar."
    },
    {
      "type": "open",
      "vraag": "Waarom is een <b>MRI-scan</b> voor het onderzoeken van zachte weefsels (zoals hersenen en spieren) vaak veiliger en geschikter dan een CT-scan?",
      "sleutelwoorden": [
        "geen ioniserende straling/magneetveld/onschadelijk",
        "zacht weefsel/contrast/hersenen",
        "geen stralingsbelasting"
      ],
      "minTreffers": 2,
      "modelantwoord": "Een MRI-scan maakt gebruik van een sterk magneetveld en radiogolven (geen ioniserende straling), waardoor er geen stralingsbelasting of risico op DNA-schade is. Bovendien geeft MRI een veel scherper contrast en meer detail bij zachte weefsels (zoals hersenen, pezen, kraakbeen en spieren) vergeleken met röntgen- of CT-scans.",
      "uitleg": "Geen stralingsrisico + superieur contrast bij weke delen."
    }
  ]
});
