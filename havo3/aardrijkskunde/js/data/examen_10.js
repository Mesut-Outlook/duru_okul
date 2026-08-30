/* Proeftoets 10 — Aardrijkskunde HAVO 3: Hoofdstuk 2 (Schatkist aarde?)
   Focus: Paragraaf 2.5 & Eindtoets H2 — Delfstoffen in Nederland, Zuid-Limburg (kalksteen/Mergel, steenkool), Groningen (aardgas Slochteren, bevingen), zoutwinning, zand & grind.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-ak-10",
  hoofdstuk: 2,
  hoofdstukTitel: "Hoofdstuk 2 — Schatkist aarde?",
  titel: "Toets 10 — Delfstoffen in Nederland: Mergel, Steenkool, Gas & Zout",
  vak: "Aardrijkskunde · HAVO 3 (H2)",
  icoon: "🏆",
  duurMin: 35,
  vragen: [
    {
      type: "mc",
      vraag: "In welke Nederlandse provincie ligt het oudste gesteente van ons land (kalksteen uit het Krijt en steenkool uit het Carboon) dicht aan of aan de oppervlakte?",
      opties: [
        "Limburg (Zuid-Limburg)",
        "Friesland",
        "Noord-Holland",
        "Flevoland"
      ],
      antwoord: 0,
      uitleg: "In Zuid-Limburg zijn door geologische opheffing (Ardennen-uitlopers) oude lagen uit het Krijt en Carboon nabij het maaiveld komen te liggen."
    },
    {
      type: "mc",
      vraag: "Hoe is de <b>Limburgse kalksteen (Mergel)</b> circa 70 miljoen jaar geleden ontstaan?",
      opties: [
        "Door vulkaanuitbarstingen van de Vaalserberg",
        "In een warme, ondiepe subtropische Krijtzee door de opeenhoping van ontelbare schelpjes en kalkskeletjes van zeedieren",
        "Door rivierklei die tijdens de laatste ijstijd door de Rijn is afgezet",
        "Door het droogvallen van de Zuiderzee in 1932"
      ],
      antwoord: 1,
      uitleg: "Zuid-Limburg lag in het Krijt onder een warme zee waarin zich dikke pakketten kalkslib vormden, bekend als mergel (o.a. Sint-Pietersberg)."
    },
    {
      type: "waaronwaar",
      vraag: "Mergel/kalksteen uit Zuid-Limburg werd en wordt gebruikt als bouwsteen voor historische gebouwen en als grondstof voor cement (bijvoorbeeld door de ENCI).",
      antwoord: true,
      uitleg: "Waar. Mergelblokken dienden als traditionele bouwsteen en de kalksteen was de basis voor de cementindustrie in Maastricht."
    },
    {
      type: "invul",
      vraag: "In welke periode van het Paleozoïcum zijn de steenkoollagen in Zuid-Limburg ontstaan uit tropische moeraswouden?",
      antwoord: "Carboon|het Carboon",
      uitleg: "Tijdens het Carboon (300 miljoen jaar geleden) zorgde een tropisch moerasklimaat voor dikke veenlagen die later door inkoling steenkool werden."
    },
    {
      type: "mc",
      vraag: "Waarom besloot de Nederlandse regering (onder leiding van minister Joop den Uyl) tussen 1965 en 1974 om alle Limburgse <b>steenkoolmijnen te sluiten</b>?",
      opties: [
        "Omdat alle steenkool in Limburg tot op de laatste gram was opgemaakt",
        "Omdat steenkool plotseling verboden werd in heel Europa",
        "De winning werd te duur en te diep, buitenlandse steenkool was goedkoper en er was in Groningen een gigantische voorraad goedkoop aardgas ontdekt",
        "Omdat de mijnwerkers weigerden nog langer onder de grond te werken"
      ],
      antwoord: 2,
      uitleg: "Door de vondst van de gasbel in Slochteren (1959) en goedkope steenkoolimport uit het buitenland was de diepe, gevaarlijke Limburgse mijnbouw niet langer rendabel."
    },
    {
      type: "waaronwaar",
      vraag: "In 1959 werd bij het Groningse Slochteren een van de grootste aardgasvelden ter wereld ontdekt in een poreuze zandsteenlaag.",
      antwoord: true,
      uitleg: "Waar. Het Groningenveld bevatte bijna 3000 miljard kuub aardgas en voorzag Nederland decennialang van goedkope energie en staatsbaten."
    },
    {
      type: "invul",
      vraag: "Hoe noem je de aardbevingen in Groningen die niet ontstaan door natuurlijke platentektoniek, maar door menselijke gaswinning en bodemdrukdaling?",
      antwoord: "geïnduceerde aardbevingen|geinduceerde aardbevingen|geïnduceerde bevingen|geinduceerde bevingen",
      uitleg: "Geïnduceerde bevingen ontstaan door het inklinken en verschuiven van het zandsteenreservoir door de afgenomen gasdruk."
    },
    {
      type: "mc",
      vraag: "Waarom heeft het aardgas in Groningen miljoenen jaren lang onder de grond kunnen blijven zitten zonder naar de oppervlakte te ontsnappen?",
      opties: [
        "Omdat mensen er in de prehistorie een betonnen plaat overheen hebben gestort",
        "Omdat aardgas zwaarder is dan steen en vanzelf naar beneden zakt",
        "Omdat het gas bevroren was tot massief ijs",
        "Boven het poreuze zandsteenreservoir ligt een dikke, volkomen ondoordringbare laag steenzout en klei (afsluitend gesteente)"
      ],
      antwoord: 3,
      uitleg: "Het Perm-zout (Zechstein) vormde een perfecte geologische 'deksel' (seal) die het gas in het poreuze Rotliegend-zandsteen gevangen hield."
    },
    {
      type: "waaronwaar",
      vraag: "De winning van het Groningen-gasveld is in 2023/2024 definitief stopgezet vanwege de aanhoudende aardbevingsschade aan huizen en de veiligheid van bewoners.",
      antwoord: true,
      uitleg: "Waar. Na decennia van protesten en een parlementaire enquête besloot de regering de gaskraan in Groningen definitief te sluiten."
    },
    {
      type: "mc",
      vraag: "Waar worden <b>zand en grind</b>, die op grote schaal in Midden- en Oost-Nederland en langs de Maas worden gewonnen, voornamelijk voor gebruikt?",
      opties: [
        "Als onmisbaar bouwmateriaal voor beton, asfalt, ophoogzand en woningbouw",
        "Als brandstof in elektriciteitscentrales",
        "Voor de fabricage van geavanceerde microchips",
        "Als voedingssupplement voor vee"
      ],
      antwoord: 0,
      uitleg: "Zand en grind (afgezet door rivieren en gletsjers in het Kwartair) zijn de belangrijkste bulkgrondstoffen voor de Nederlandse bouw en infrastructuur."
    },
    {
      type: "invul",
      vraag: "Welke delfstof wordt in Twente (Hengelo) en Friesland (Barradeel) gewonnen door diepe zoutlagen met water op te lossen (oplosmijnbouw)?",
      antwoord: "zout|steenzout|keukenzout",
      uitleg: "Via oplosmijnbouw wordt water in zoutlagen uit het Perm gepompt; de pekel wordt omhoog gepompt en ingedampt tot zuiver zout voor de chemie en voeding."
    },
    {
      type: "waaronwaar",
      vraag: "Rivierklei die langs de uiterwaarden van de Waal en Maas wordt afgegraven, wordt in steenfabrieken gebakken tot bakstenen en dakpannen.",
      antwoord: true,
      uitleg: "Waar. De fijnkorrelige rivierklei uit het Holoceen is de traditionele grondstof voor de Nederlandse keramische en baksteenindustrie."
    },
    {
      type: "mc",
      vraag: "Wat ontstaat er vaak na afloop van grootschalige grind- en zandwinning langs de Maas (ontgrinding)?",
      opties: [
        "Een actieve vulkaankrater",
        "Grote recreatieplassen en nieuwe waterrijke natuurgebieden (zoals de Maasplassen)",
        "Een kilometers hoge berg van basalt",
        "Een woestijn vol cactussen"
      ],
      antwoord: 1,
      uitleg: "De diepe plassen die achterblijven na ontgrinding worden ingericht voor waterberging, natuurontwikkeling en watersport (bijv. Maasplassen bij Roermond)."
    },
    {
      type: "invul",
      vraag: "Hoe noem je het geologische proces waarbij plantenresten onder toenemende druk en temperatuur over miljoenen jaren transformeren van veen naar bruinkool, steenkool en antraciet?",
      antwoord: "inkolingsproces|inkoling|het inkolingsproces",
      uitleg: "Door inkoling stijgt het koolstofpercentage en de energiedichtheid naarmate de druk en temperatuur dieper in de aardkorst toenemen."
    },
    {
      type: "waaronwaar",
      vraag: "In Nederland wordt vandaag de dag nog steeds op grote schaal steenkool gedolven in actieve ondergrondse mijnschachten in Limburg.",
      antwoord: false,
      uitleg: "Niet waar. Alle Nederlandse steenkoolmijnen zijn al in de jaren 1960 en 1970 gesloten en de schachten zijn volgestort met beton of water."
    },
    {
      type: "mc",
      vraag: "Wat is een mogelijk risico van de zoutwinning via cavernes in Twente en Friesland voor de omgeving?",
      opties: [
        "Het spontaan bevriezen van alle sloten in de zomer",
        "Het ontstaan van giftige gaswolken die de zon verduisteren",
        "Bodemdaling en het eventueel instorten van ondergrondse zoutholtes (cavernes)",
        "Het wegvallen van het internetverkeer in de regio"
      ],
      antwoord: 2,
      uitleg: "Als een uitgeloogde zoutcaverne instort, kan er een zinkgat ontstaan en daalt het maaiveld in de omgeving."
    },
    {
      type: "waaronwaar",
      vraag: "De zand- en grindafzettingen in Midden-Nederland (Utrechtse Heuvelrug en Veluwe) zijn mede gevormd doordat gletsjers uit Scandinavië tijdens het Saalien de bodem opstuwden tot stuwwallen.",
      antwoord: true,
      uitleg: "Waar. Landijs uit het Pleistoceen duwde bevroren rivierzand en grind op tot de markante heuvelruggen in ons landschap."
    },
    {
      type: "mc",
      vraag: "Wat is de zogeheten 'aardgasbaten' of 'aardgasbel' geweest voor de Nederlandse staat?",
      opties: [
        "Een belasting op het drinken van bruisend mineraalwater",
        "Een reusachtige zeepbel die boven het dorp Slochteren zweefde",
        "Een speciale subsidie voor mensen die op steenkool kookten",
        "De honderden miljarden euro's aan overheidsinkomsten uit de verkoop van Gronings aardgas sinds de jaren 1960"
      ],
      antwoord: 3,
      uitleg: "De gasbaten leverden de Nederlandse overheid meer dan 400 miljard euro op, waarmee de verzorgingsstaat en infrastructuur werden gefinancierd."
    },
    {
      type: "open",
      vraag: "Leg uit hoe de geologische opbouw van Groningen (poreus reservoir, ondoordringbare afsluitlaag) zorgde voor het ontstaan en vasthouden van het aardgasveld.",
      sleutelwoorden: ["steenkool onderin vormt gas/moedergesteente", "poreus zandsteen als reservoirgesteente", "ondoordringbare zoutlaag/Zechstein als afsluiting"],
      minTreffers: 2,
      modelantwoord: "Diep in de ondergrond vormden de Carboon-steenkoollagen onder hoge temperatuur en druk het aardgas (moedergesteente). Dit gas steeg op en verzamelde zich in de poriën van de bovenliggende zandsteenlaag uit het Perm (reservoirgesteente). Bovenop dit zandsteen lag een dikke, volkomen dichte zoutlaag (Zechstein), die als afsluitend gesteente fungeerde en voorkwam dat het gas naar de oppervlakte kon ontsnappen.",
      uitleg: "Combinatie van Carboon-steenkool (bron), Perm-zandsteen (reservoir) en Zechstein-zout (afsluiting) maakte het gasveld mogelijk."
    },
    {
      type: "open",
      vraag: "Beredeneer waarom de sluiting van de Limburgse steenkoolmijnen in de jaren 1960/1970 leidde tot grote sociaaleconomische problemen in de regio en hoe de overheid dit probeerde op te vangen.",
      sleutelwoorden: ["massale werkloosheid/tienduizenden banen verloren", "mijnstreek economisch ontwricht", "overheidsdiensten verhuizen/CBS/DAF"],
      minTreffers: 2,
      modelantwoord: "Tienduizenden mijnwerkers en toeleveranciers verloren in korte tijd hun baan, waardoor Zuid-Limburg kampte met torenhoge werkloosheid en economische neergang. Om dit verlies te compenseren, verhuisde de overheid rijksdiensten naar Limburg (zoals het CBS naar Heerlen en het ABP) en stimuleerde zij nieuwe bedrijven zoals de DAF-autofabriek (later NedCar) in Born.",
      uitleg: "Mijnsluiting veroorzaakte massale werkloosheid; spreiding van rijksdiensten en industriële subsidies moesten de regio herstellen."
    }
  ]
});
