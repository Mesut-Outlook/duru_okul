import json

exam13 = {
  "id": "ex-h3-economie-13",
  "hoofdstuk": 1,
  "paragraaf": "1.1",
  "titel": "Proeftoets 13: Behoeften, keuzegedrag en schaarste (Extra)",
  "vak": "Economie · HAVO 3",
  "icoon": "🛍️",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Wat betekent het begrip 'alternatief aanwendbaar' in de economie?",
      "opties": [
        "Middelen zoals tijd en geld kunnen voor verschillende doeleinden worden ingezet, maar slechts voor één doel tegelijk.",
        "Producten die je na gebruik gratis kunt omruilen in een winkel.",
        "Goederen die alleen geproduceerd worden met behulp van wind- en zonne-energie.",
        "Inkomsten die uitsluitend worden overgemaakt naar een spaarrekening."
      ],
      "antwoord": 0,
      "uitleg": "Middelen zijn alternatief aanwendbaar: geef je een tientje uit aan de bioscoop, dan kun je datzelfde tientje niet sparen of aan boeken besteden."
    },
    {
      "type": "mc",
      "vraag": "Duru twijfelt tussen een middag werken in de supermarkt (€ 40 loon) of meegaan naar een pretpark (kaartje kost € 35). Wat zijn de opofferingskosten (opportunity costs) als ze naar het pretpark gaat?",
      "opties": [
        "Zij loopt de € 40 mis die ze anders had kunnen verdienen.",
        "Zij bespaart € 5 aan vervoerskosten.",
        "De opofferingskosten zijn altijd precies gelijk aan nul.",
        "Zij verliest haar baan bij de supermarkt definitief."
      ],
      "antwoord": 0,
      "uitleg": "De economische opoffering van een keuze bestaat uit het beste alternatief dat je opgeeft; in dit geval het misgelopen loon van € 40."
    },
    {
      "type": "mc",
      "vraag": "Waarom is leidingwater in Nederland geen 'vrij goed', hoewel het relatief goedkoop uit de kraan stroomt?",
      "opties": [
        "Omdat drinkwaterbedrijven veel arbeid, zuiveringsinstallaties en leidingnetwerken inzetten om het te produceren.",
        "Omdat de Europese Unie heeft bepaald dat water per definitie een luxegoed is.",
        "Omdat leidingwater uitsluitend via buitenlandse tankers wordt geïmporteerd.",
        "Omdat consumenten verplicht zijn minstens 10 liter per dag te drinken."
      ],
      "antwoord": 0,
      "uitleg": "Er zijn schaarse productiemiddelen (arbeid, machines, grondstoffen) opgeofferd om van grondwater veilig drinkwater te maken."
    },
    {
      "type": "mc",
      "vraag": "Welke van de volgende handelingen is een zuiver voorbeeld van een dienst?",
      "opties": [
        "Het laten repareren van je kapotte fiets door een fietsenmaker.",
        "Het aanschaffen van een nieuwe binnenband in de winkel.",
        "Het oogsten van aardbeien in de moestuin van je ouders.",
        "Het kopen van een koplamp op zonne-energie."
      ],
      "antwoord": 0,
      "uitleg": "Het repareren is een economische verrichting/arbeidsprestatie (dienst), terwijl de binnenband een stoffelijk goed is."
    },
    {
      "type": "mc",
      "vraag": "Wat is een direct economisch gevolg van de spanning tussen onbegrensde behoeften en schaarse middelen?",
      "opties": [
        "Mensen worden gedwongen om prioriteiten te stellen en keuzes te maken.",
        "Alle winkels worden wettelijk verplicht hun prijzen te verlagen naar € 0.",
        "De overheid schaft alle belastingen en subsidies af.",
        "Consumenten stoppen volledig met het kopen van goederen."
      ],
      "antwoord": 0,
      "uitleg": "Omdat je niet al je verlangens tegelijk kunt bevredigen met beperkte tijd en geld, moet je altijd kiezen."
    },
    {
      "type": "mc",
      "vraag": "Welke van de onderstaande goederen is voor een moderne Nederlandse scholier een secundaire behoefte?",
      "opties": [
        "Draadloze merkoortjes met ruisonderdrukking.",
        "Voedzame maaltijden gedurende de dag.",
        "Voldoende zuiver drinkwater.",
        "Een warme winterjas bij vorst."
      ],
      "antwoord": 0,
      "uitleg": "Draadloze oordopjes verhogen het comfort en plezier (secundair), terwijl eten, drinken en beschermende kleding primaire levensbehoeften zijn."
    },
    {
      "type": "mc",
      "vraag": "Wat verstaat de economische theorie onder het begrip 'zelfvoorziening'?",
      "opties": [
        "Het zelf voortbrengen van goederen en diensten voor eigen gebruik zonder geldtransacties.",
        "Het automatisch laten overboeken van je maandsalaris naar een beleggingsfonds.",
        "Uitsluitend producten kopen die in de aanbieding zijn bij een supermarkt.",
        "Het openen van een eigen bankrekening met pinpas."
      ],
      "antwoord": 0,
      "uitleg": "Bij zelfvoorziening (bijv. eigen groente kweken of zelf kleding herstellen) voorzie je in je behoeften zonder geld of handel."
    },
    {
      "type": "mc",
      "vraag": "Waarom beschouwen economen wind die windmolens aandrijft als een vrij goed?",
      "opties": [
        "Omdat de natuur wind onbeperkt levert zonder dat er productiemiddelen zijn opgeofferd om de wind te laten waaien.",
        "Omdat een windturbine geen geld kost om te bouwen.",
        "Omdat de geproduceerde groene stroom gratis aan huishoudens wordt geleverd.",
        "Omdat windenergie verboden is in stedelijke gebieden."
      ],
      "antwoord": 0,
      "uitleg": "De wind zelf is een vrij natuurelement; er is geen arbeid of kapitaal nodig geweest om de wind te scheppen."
    },
    {
      "type": "mc",
      "vraag": "Wanneer noemen economen een product 'schaars'?",
      "opties": [
        "Zodra er productiemiddelen (tijd, arbeid, grondstoffen, kapitaalgoederen) zijn ingezet om het te maken.",
        "Alleen als er een tekort is ontstaan en de winkelrekken leeg zijn.",
        "Uitsluitend als de prijs van het product hoger is dan € 1.000.",
        "Wanneer niemand het product meer wil kopen wegens ouderdom."
      ],
      "antwoord": 0,
      "uitleg": "In de economie betekent schaars niet 'zeldzaam', maar dat er offers aan productiemiddelen nodig waren."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste verschil tussen een goed en een dienst?",
      "opties": [
        "Een goed is een tastbaar, stoffelijk voorwerp en een dienst is een niet-tastbare activiteit of handeling.",
        "Een goed wordt uitsluitend in het buitenland gefabriceerd en een dienst altijd in eigen land.",
        "Op goederen betaal je nooit belasting en op diensten altijd 50% btw.",
        "Goederen zijn altijd secundaire behoeften en diensten altijd primaire behoeften."
      ],
      "antwoord": 0,
      "uitleg": "Goederen (zoals een laptop of brood) kun je beetpakken; diensten (zoals lesgeven of taxivervoer) zijn onstoffelijk."
    },
    {
      "type": "waaronwaar",
      "vraag": "Zuurstof die je inademt in het park is een vrij goed, maar zuurstof in een ziekenhuiscilinder is een schaars economisch goed.",
      "antwoord": True,
      "uitleg": "De buitenlucht is gratis in de natuur aanwezig, maar medische zuurstof moet gefilterd, gecomprimeerd en gebotteld worden met schaarse middelen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Als je besluit 2 uur te slapen in plaats van te leren voor een economietoets, heeft je tijd géén economische waarde.",
      "antwoord": False,
      "uitleg": "Tijd is een schaars middel dat alternatief aanwendbaar is; de keuze voor slaap kost je leertijd (opofferingskosten)."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een biologische appel uit de supermarkt is een vrij goed omdat hij aan een boom groeit.",
      "antwoord": False,
      "uitleg": "De teler, boomgaard, verzorging, plukarbeid en transport vergen allemaal schaarse productiemiddelen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Zelfvoorziening leidt er direct toe dat de consumptie in een land volledig stopt.",
      "antwoord": False,
      "uitleg": "Bij zelfvoorziening consumeer je nog steeds (je eet de groente op), maar zonder inschakeling van de markt of geld."
    },
    {
      "type": "invul",
      "vraag": "Middelen die je slechts voor één doel tegelijk kunt gebruiken noemen economen [alternatief aanwendbaar|alternatief aanwendbare].",
      "antwoord": "alternatief aanwendbaar|alternatief aanwendbare",
      "uitleg": "Alternatieve aanwendbaarheid betekent dat een middel (geld of tijd) op verschillende manieren kan worden benut, maar nooit tegelijk."
    },
    {
      "type": "invul",
      "vraag": "Het niet-tastbare werk dat een arts of leraar verricht noemen we een [dienst|diensten].",
      "antwoord": "dienst|diensten",
      "uitleg": "Diensten zijn economische handelingen die onstoffelijk van aard zijn."
    },
    {
      "type": "invul",
      "vraag": "Goederen waarvoor geen enkele inzet van productiemiddelen nodig is heten [vrije goederen|vrij goed].",
      "antwoord": "vrije goederen|vrij goed",
      "uitleg": "Vrije goederen (zoals zonlicht of zeewater) zijn door de natuur zonder kosten ter beschikking gesteld."
    },
    {
      "type": "invul",
      "vraag": "Het aanschaffen van producten door gezinnen om hun wensen en behoeften te vervullen heet [consumeren|consumptie].",
      "antwoord": "consumeren|consumptie",
      "uitleg": "Consumptie is het gebruiken of verbruiken van goederen en diensten door consumenten."
    },
    {
      "type": "open",
      "vraag": "Leg aan de hand van het begrip 'schaarste' uit waarom ook een miljardair toch economische keuzes moet maken.",
      "sleutelwoorden": [
        "tijd/uren/beperkt",
        "keuzes/prioriteiten/niet alles tegelijk"
      ],
      "minTreffers": 1,
      "modelantwoord": "Hoewel een miljardair enorm veel geld bezit, is zijn tijd beperkt (slechts 24 uur per dag). Omdat tijd schaars is en niet oneindig, moet ook een rijk persoon keuzes maken tussen verschillende activiteiten.",
      "uitleg": "Schaarste betreft niet alleen geld, maar ook tijd en energie: je kunt op hetzelfde moment maar op één plek tegelijk zijn."
    },
    {
      "type": "open",
      "vraag": "Geef één voorbeeld van een primair goed en één voorbeeld van een primaire dienst die onmisbaar zijn in het dagelijks leven.",
      "sleutelwoorden": [
        "water/brood/voedsel/kleding/woning",
        "arts/ziekenhuis/chirurg/huisarts/brandweer/drinkwatervoorziening"
      ],
      "minTreffers": 2,
      "modelantwoord": "Primair goed: drinkwater of basisvoedsel (zoals brood). Primaire dienst: acute medische zorg door een arts of de inzet van de brandweer bij nood.",
      "uitleg": "Zowel stoffelijke zaken (voeding) als diensten (levensreddende gezondheidszorg) kunnen eerste levensbehoeften zijn."
    }
  ]
}

exam14 = {
  "id": "ex-h3-economie-14",
  "hoofdstuk": 1,
  "paragraaf": "1.2",
  "titel": "Proeftoets 14: Inkomensstromen, gezinsuitgaven en reserves (Extra)",
  "vak": "Economie · HAVO 3",
  "icoon": "💳",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Duru's broer verhuurt een garagebox aan een buurtbewoner voor € 120 per maand. Tot welke inkomenscategorie behoort dit bedrag?",
      "opties": [
        "Inkomen uit bezit.",
        "Inkomen uit arbeid.",
        "Overdrachtsinkomen.",
        "Huishoudelijke toelage."
      ],
      "antwoord": 0,
      "uitleg": "Huuropbrengst vloeit voort uit het eigendom van onroerend goed (vermogen) en is dus inkomen uit bezit."
    },
    {
      "type": "mc",
      "vraag": "Een gezin betaalt maandelijks € 135 aan de premie voor de zorgverzekering. Welk type uitgave is dit volgens het NIBUD?",
      "opties": [
        "Vaste lasten.",
        "Huishoudelijke uitgaven.",
        "Incidentele uitgaven.",
        "Reserveringskosten."
      ],
      "antwoord": 0,
      "uitleg": "De zorgverzekering is een contractueel verplichte, maandelijks terugkerende betaling (vaste last)."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste kenmerk van een overdrachtsinkomen?",
      "opties": [
        "Je ontvangt het geld zonder dat je daar een directe economische tegenprestatie voor levert.",
        "Het wordt uitsluitend in contant papiergeld uitgekeerd door commerciële banken.",
        "Het is een directe beloning voor gewerkte overuren in de avond.",
        "Het mag uitsluitend worden uitgegeven aan primaire levensbehoeften."
      ],
      "antwoord": 0,
      "uitleg": "Bij overdrachtsinkomen (bijv. studiefinanciering, zakgeld, kinderbijslag) lever je geen directe arbeid of goederen in ruil."
    },
    {
      "type": "mc",
      "vraag": "De wasmachine van een familie begeeft het onverwacht en er moet direct een nieuw apparaat van € 650 worden aangeschaft. Tot welke uitgavencategorie behoort dit?",
      "opties": [
        "Incidentele uitgaven.",
        "Vaste lasten.",
        "Huishoudelijke uitgaven.",
        "Directe overdracht."
      ],
      "antwoord": 0,
      "uitleg": "Grote huishoudelijke apparaten koop je slechts af en toe; dit zijn incidentele (onregelmatige) uitgaven."
    },
    {
      "type": "mc",
      "vraag": "Welke van de volgende posten is een typisch voorbeeld van een huishoudelijke uitgave?",
      "opties": [
        "Het wekelijkse krat boodschappen bij de supermarkt met fruit, groente en melk.",
        "De aflossing op een 30-jarige hypothecaire lening bij de bank.",
        "De jaarlijkse contributie voor de hockeyvereniging.",
        "De aanschaf van een nieuwe elektrische bakfiets."
      ],
      "antwoord": 0,
      "uitleg": "Huishoudelijke uitgaven zijn de dagelijkse of wekelijkse uitgaven voor het lopende gezinshuishouden."
    },
    {
      "type": "mc",
      "vraag": "Waarom adviseert het NIBUD gezinnen om maandelijks een vast bedrag te reserveren?",
      "opties": [
        "Om onverwachte grote uitgaven of reparaties op te vangen zonder dure leningen af te sluiten.",
        "Omdat de wet gezinnen verbiedt meer dan € 50 per week uit te geven aan boodschappen.",
        "Om de inflatie in het hele land automatisch omlaag te brengen.",
        "Om het maandsalaris om te zetten in buitenlandse valuta."
      ],
      "antwoord": 0,
      "uitleg": "Door te reserveren bouw je een spaarbuffer op voor incidentele uitgaven zoals vervanging van witgoed of autoschade."
    },
    {
      "type": "mc",
      "vraag": "Een studente ontvangt maandelijks € 120 aan zorgtoeslag van de Belastingdienst. Onder welke inkomensvorm valt deze toeslag?",
      "opties": [
        "Overdrachtsinkomen.",
        "Inkomen uit arbeid.",
        "Inkomen uit bezit.",
        "Rendementsuitkering."
      ],
      "antwoord": 0,
      "uitleg": "Toeslagen van de overheid worden overgedragen zonder directe economische tegenprestatie."
    },
    {
      "type": "mc",
      "vraag": "Wat gebeurt er als de vaste lasten van een gezin een te groot percentage van het totale inkomen opeisen?",
      "opties": [
        "Het gezin houdt minder financiële speelruimte over voor huishoudelijke uitgaven en sparen.",
        "Het gezin ontvangt automatisch dubbel zoveel kinderbijslag van de staat.",
        "Alle incidentele uitgaven worden dan kwijtgescholden door leveranciers.",
        "Het inkomen uit arbeid stijgt direct mee met hetzelfde percentage."
      ],
      "antwoord": 0,
      "uitleg": "Als vaste lasten knellen, blijft er weinig vrije bestedingsruimte over, waardoor financiële kwetsbaarheid ontstaat."
    },
    {
      "type": "mc",
      "vraag": "Duru heeft aandelen gekocht in een duurzaam energiebedrijf en ontvangt na een winstgevend jaar € 85 dividend. Welke inkomensbron is dit?",
      "opties": [
        "Inkomen uit bezit.",
        "Inkomen uit arbeid.",
        "Overdrachtsinkomen.",
        "Vaste vergoeding."
      ],
      "antwoord": 0,
      "uitleg": "Aandelen vormen vermogen (bezit); de winstuitkering (dividend) is dus inkomen uit bezit."
    },
    {
      "type": "mc",
      "vraag": "Wat is het belangrijkste verschil tussen huishoudelijke uitgaven en incidentele uitgaven?",
      "opties": [
        "Huishoudelijke uitgaven keren bijna dagelijks of wekelijks terug (eten, drinken), terwijl incidentele uitgaven af en toe voorkomen en vaak grote bedragen betreffen.",
        "Huishoudelijke uitgaven worden verplicht door een notaris en incidentele uitgaven niet.",
        "Huishoudelijke uitgaven betaal je nooit met een pinpas.",
        "Incidentele uitgaven zijn altijd volledig aftrekbaar van de inkomstenbelasting."
      ],
      "antwoord": 0,
      "uitleg": "Het verschil zit in frequentie en omvang: dagelijkse boodschappen versus grote, onregelmatige aankopen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Vakantiegeld dat je werkgever in mei aan je uitkeert is een vorm van inkomen uit arbeid.",
      "antwoord": True,
      "uitleg": "Vakantiegeld is een wettelijk verplicht onderdeel van de beloning voor verrichte arbeid."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een Netflix-abonnement van € 14 per maand behoort tot de incidentele uitgaven.",
      "antwoord": False,
      "uitleg": "Een abonnement is een periodiek terugkerende verplichting en telt dus als vaste last."
    },
    {
      "type": "waaronwaar",
      "vraag": "Zakgeld dat ouders maandelijks aan hun kind geven is een overdrachtsinkomen voor dat kind.",
      "antwoord": True,
      "uitleg": "Het kind levert er geen economische arbeidsprestatie voor; het geld wordt overgedragen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Rente ontvangen op een spaarrekening bij de bank is een vorm van overdrachtsinkomen.",
      "antwoord": False,
      "uitleg": "Spaarrente is een beloning voor het beschikbaar stellen van vermogen (inkomen uit bezit)."
    },
    {
      "type": "invul",
      "vraag": "De periodieke vergoeding die een aandeelhouder ontvangt als aandeel in de bedrijfswinst heet [dividend].",
      "antwoord": "dividend",
      "uitleg": "Dividend is de winstuitkering op aandelen en behoort tot inkomen uit bezit."
    },
    {
      "type": "invul",
      "vraag": "Kosten die maandelijks volgens vaste contracten moeten worden voldaan noemen we [vaste lasten|vaste last].",
      "antwoord": "vaste lasten|vaste last",
      "uitleg": "Vaste lasten zijn terugkerende verplichtingen zoals internet, huur en verzekeringen."
    },
    {
      "type": "invul",
      "vraag": "Het opzijzetten van spaargeld om toekomstige grote vervangingen te betalen heet [reserveren|reserveringsuitgaven].",
      "antwoord": "reserveren|reserveringsuitgaven",
      "uitleg": "Reserveren voorkomt dat je plotseling geld tekortkomt bij een kapot apparaat."
    },
    {
      "type": "invul",
      "vraag": "Een uitkering zoals de bijstand of AOW zonder economische tegenprestatie heet een [overdrachtsinkomen|overdrachtsinkomens].",
      "antwoord": "overdrachtsinkomen|overdrachtsinkomens",
      "uitleg": "Overdrachtsinkomens worden door de overheid verstrekt om sociale zekerheid te bieden."
    },
    {
      "type": "open",
      "vraag": "Benoem de drie bronnen van inkomen en geef voor een gezin bij elke bron één passend praktijkvoorbeeld.",
      "sleutelwoorden": [
        "arbeid/salaris/loon",
        "bezit/rente/huur/dividend",
        "overdracht/kinderbijslag/zakgeld/zorgtoeslag"
      ],
      "minTreffers": 3,
      "modelantwoord": "1. Inkomen uit arbeid: het maandsalaris van een ouder. 2. Inkomen uit bezit: ontvangen rente op de spaarrekening of huur van een garagebox. 3. Overdrachtsinkomen: kinderbijslag of zorgtoeslag ontvangen van de overheid.",
      "uitleg": "Dit zijn de drie standaard economische inkomenscategorieën."
    },
    {
      "type": "open",
      "vraag": "Leg uit waarom bezuinigen op huishoudelijke uitgaven op korte termijn veel makkelijker is dan bezuinigen op vaste lasten.",
      "sleutelwoorden": [
        "contracten/termijn/opzegtermijn/vastzitten",
        "direct/boodschappen/goedkoper merk/flexibel"
      ],
      "minTreffers": 2,
      "modelantwoord": "Aan vaste lasten (zoals een huurcontract of jaarabonnement) zit je contractueel vast met opzegtermijnen. Huishoudelijke uitgaven (zoals boodschappen) doe je wekelijks en kun je direct verlagen door goedkopere huismerken te kopen of minder luxe snacks te halen.",
      "uitleg": "Vaste lasten vergen contractwijzigingen of verhuizing; dagelijkse boodschappen zijn direct aanpasbaar."
    }
  ]
}

exam15 = {
  "id": "ex-h3-economie-15",
  "hoofdstuk": 1,
  "paragraaf": "1.3",
  "titel": "Proeftoets 15: Begrotingen, financiële berekeningen en NIBUD (Extra)",
  "vak": "Economie · HAVO 3",
  "icoon": "🧮",
  "duurMin": 20,
  "vragen": [
    {
      "type": "mc",
      "vraag": "Duru verdient met haar bijbaan in een bakkerij € 45 per week. Wat zijn haar gemiddelde inkomsten per maand?",
      "opties": [
        "€ 195",
        "€ 180",
        "€ 210",
        "€ 225"
      ],
      "antwoord": 0,
      "uitleg": "Berekening: (45 × 52) / 12 = 2.340 / 12 = € 195 per maand."
    },
    {
      "type": "mc",
      "vraag": "Een huishouden betaalt elk kwartaal € 225 aan gemeentelijke belastingen en afvalstoffenheffing. Hoeveel moet er maandelijks in de begroting worden gereserveerd?",
      "opties": [
        "€ 75",
        "€ 56,25",
        "€ 90",
        "€ 112,50"
      ],
      "antwoord": 0,
      "uitleg": "1 kwartaal telt precies 3 maanden. € 225 / 3 = € 75 per maand."
    },
    {
      "type": "mc",
      "vraag": "Duru spaart maandelijks € 40. Een jaarlijks tijdschriftabonnement kost € 144 per jaar. Hoeveel bedragen de totale maandelijkse kosten van dit abonnement?",
      "opties": [
        "€ 12",
        "€ 14,40",
        "€ 10",
        "€ 16"
      ],
      "antwoord": 0,
      "uitleg": "1 jaar heeft 12 maanden. € 144 / 12 = € 12 per maand."
    },
    {
      "type": "mc",
      "vraag": "In de begroting van een student staan de verwachte inkomsten op € 980 en de verwachte uitgaven op € 1.050. Welke situatie is hier van toepassing?",
      "opties": [
        "Er is een begrotingstekort van € 70.",
        "Er is een begrotingsoverschot van € 70.",
        "Er is sprake van een begrotingsevenwicht.",
        "Het saldo op de spaarrekening verdubbelt automatisch."
      ],
      "antwoord": 0,
      "uitleg": "Inkomsten (€ 980) minus uitgaven (€ 1.050) = -€ 70; er is dus een tekort van € 70."
    },
    {
      "type": "mc",
      "vraag": "Waarom mag je bij het omrekenen van wekelijkse inkomsten naar maandinkomsten niet simpelweg 'bedrag × 4' doen?",
      "opties": [
        "Omdat een jaar 52 weken telt en 52 gedeeld door 12 gelijk is aan 4,33 weken per maand.",
        "Omdat banken vier maanden per jaar overslaan bij renteberekeningen.",
        "Omdat een kwartaal altijd uit 5 weken bestaat.",
        "Omdat de wet verbiedt om met weeklonen te rekenen."
      ],
      "antwoord": 0,
      "uitleg": "Een maand heeft gemiddeld 4,33 weken (52 / 12). Met '× 4' mis je 4 weken per jaar aan inkomsten!"
    },
    {
      "type": "mc",
      "vraag": "Een gezin heeft een maandelijks begrotingstekort van € 150. Welke actie lost dit probleem op structurele wijze op?",
      "opties": [
        "Niet-noodzakelijke abonnementen opzeggen en energieverbruik terugdringen.",
        "Elke maand een nieuwe persoonlijke lening afsluiten.",
        "De administratie en rekeningen weggooien zonder te betalen.",
        "Alleen nog betalen met contant geld uit de spaarpot."
      ],
      "antwoord": 0,
      "uitleg": "Een tekort moet je structureel oplossen door uitgaven te verlagen (bezuinigen) of inkomsten te verhogen."
    },
    {
      "type": "mc",
      "vraag": "Duru verdient € 520 per maand met haar stage. Hoeveel is dit gemiddeld per week?",
      "opties": [
        "€ 120",
        "€ 130",
        "€ 100",
        "€ 115"
      ],
      "antwoord": 0,
      "uitleg": "Berekening: (520 × 12) / 52 = 6.240 / 52 = € 120 per week."
    },
    {
      "type": "mc",
      "vraag": "Wat is een van de kerntaken van het NIBUD (Nationaal Instituut voor Budgetvoorlichting)?",
      "opties": [
        "Consumenten voorzien van onafhankelijke richtlijnen, budgetvoorbeelden en advies over geldbeheer.",
        "Geldleningen en hypotheken verstrekken aan gezinnen met schulden.",
        "De belastingtarieven in Nederland vaststellen en innen namens de overheid.",
        "Commerciële reclamespots keuren voor televisie en radio."
      ],
      "antwoord": 0,
      "uitleg": "Het NIBUD is een voorlichtingsinstituut dat consumenten leert budgetteren en richtbedragen berekent."
    },
    {
      "type": "mc",
      "vraag": "Wat betekent de term 'begrotingsevenwicht' voor een huishouden?",
      "opties": [
        "De totale verwachte inkomsten zijn precies gelijk aan de totale verwachte uitgaven.",
        "De helft van het inkomen wordt verplicht overgemaakt naar de spaarrekening.",
        "De huur van het huis is exact gelijk aan het zakgeld van de kinderen.",
        "Er zijn geen vaste lasten meer verschuldigd."
      ],
      "antwoord": 0,
      "uitleg": "Bij evenwicht zijn baten en lasten precies in balans (saldo = € 0)."
    },
    {
      "type": "mc",
      "vraag": "Een gezin betaalt € 480 per halfjaar aan autoverzekering en wegenbelasting. Hoeveel bedragen de maandelijkse kosten?",
      "opties": [
        "€ 80",
        "€ 60",
        "€ 120",
        "€ 40"
      ],
      "antwoord": 0,
      "uitleg": "Een halfjaar = 6 maanden. € 480 / 6 = € 80 per maand."
    },
    {
      "type": "waaronwaar",
      "vraag": "Bij een begrotingsoverschot zijn de verwachte inkomsten hoger dan de verwachte uitgaven.",
      "antwoord": True,
      "uitleg": "Bij een overschot houd je geld over in de begroting dat je kunt sparen of investeren."
    },
    {
      "type": "waaronwaar",
      "vraag": "Een kwartaal in het financieel beheer bestaat uit vier opeenvolgende maanden.",
      "antwoord": False,
      "uitleg": "Een kwartaal is een vierde deel van een jaar en telt precies 3 maanden."
    },
    {
      "type": "waaronwaar",
      "vraag": "Het opstellen van een begroting is uitsluitend nuttig voor mensen die torenhoge schulden hebben.",
      "antwoord": False,
      "uitleg": "Budgetteren geeft iedereen inzicht, controle en financiële rust, ongeacht het inkomen."
    },
    {
      "type": "waaronwaar",
      "vraag": "Om een bedrag van kwartaal naar jaar om te rekenen vermenigvuldig je met 4.",
      "antwoord": True,
      "uitleg": "Er gaan 4 kwartalen in 1 kalenderjaar (4 × 3 = 12 maanden)."
    },
    {
      "type": "invul",
      "vraag": "Het gestructureerde overzicht van verwachte inkomsten en uitgaven voor de komende periode noemen we een [begroting|budgetplan].",
      "antwoord": "begroting|budgetplan",
      "uitleg": "Een begroting laat vooraf zien of je zult uitkomen met je financiën."
    },
    {
      "type": "invul",
      "vraag": "Wanneer de uitgaven groter zijn dan de inkomsten is er sprake van een [begrotingstekort|tekort].",
      "antwoord": "begrotingstekort|tekort",
      "uitleg": "Bij een tekort kom je geld tekort en moet je bezuinigen."
    },
    {
      "type": "invul",
      "vraag": "Om van een weekbedrag een maandbedrag te maken vermenigvuldig je met 52 en deel je door [12].",
      "antwoord": "12",
      "uitleg": "Formule: (weekbedrag × 52) / 12."
    },
    {
      "type": "invul",
      "vraag": "Het onafhankelijke instituut voor budgetvoorlichting heet het [NIBUD|Nibud].",
      "antwoord": "NIBUD|Nibud",
      "uitleg": "Het Nationaal Instituut voor Budgetvoorlichting (NIBUD)."
    },
    {
      "type": "open",
      "vraag": "Duru krijgt € 18 zakgeld per week en verdient € 30 per week met oppassen. Bereken haar totale gemiddelde inkomsten per maand. Schrijf je tussenstappen op.",
      "sleutelwoorden": [
        "48/18 + 30",
        "208"
      ],
      "minTreffers": 1,
      "modelantwoord": "Totale weekinkomsten = € 18 + € 30 = € 48 per week. Per jaar = € 48 × 52 = € 2.496. Per maand = € 2.496 / 12 = € 208.",
      "uitleg": "(48 × 52) / 12 = € 208 per maand."
    },
    {
      "type": "open",
      "vraag": "Noem drie concrete tips die het NIBUD geeft om grip te houden op je maandelijkse geldzaken.",
      "sleutelwoorden": [
        "begroting/overzicht maken/budgetplan",
        "reserveren/buffer opbouwen/sparen voor onvoorzien",
        "vaste lasten checken/abonnementen opzeggen/pinnen"
      ],
      "minTreffers": 2,
      "modelantwoord": "1. Maak maandelijks een begroting (overzicht van inkomsten en uitgaven). 2. Reserveer maandelijks geld voor onverwachte uitgaven (noodbuffer). 3. Controleer regelmatig vaste lasten en zeg ongebruikte abonnementen op.",
      "uitleg": "Overzicht, buffers en scherpte op vaste lasten zijn de pijlers van gezond financieel beheer."
    }
  ]
}

new_exams = [exam13, exam14, exam15]

# Balance multiple choice options so answer is distributed evenly across A, B, C, D
for ex in new_exams:
    mc_c = 0
    for v in ex['vragen']:
        if v.get('type') == 'mc':
            target = mc_c % len(v['opties'])
            mc_c += 1
            curr = v['antwoord']
            if curr != target:
                v['opties'][curr], v['opties'][target] = v['opties'][target], v['opties'][curr]
                v['antwoord'] = target

# Output the JS files
for ex in new_exams:
    ex_num = ex['id'].split('-')[-1]
    fname = f"havo3/economie/js/data/examen_{ex_num}.js"
    content = f"/* =========================================================\n   Duru's Economie (HAVO 3) — {ex['titel']}\n   ========================================================= */\nDURU.registerExamen({json.dumps(ex, ensure_ascii=False, indent=2)});\n"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Written {fname}")

