import json
import os

ECONOMIE_DIR = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/economie/js/data"
os.makedirs(ECONOMIE_DIR, exist_ok=True)

# 12 Full Exams (20 questions each, balanced options, rich explanation)
EXAMS = [
  # Examen 1: 1.1 Behoeften en middelen
  {
    "id": "ex-h3-economie-1",
    "hoofdstuk": 1,
    "paragraaf": "1.1",
    "titel": "Proeftoets 1: Behoeften, schaarste en middelen",
    "vak": "Economie · HAVO 3",
    "icoon": "🛒",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Wat is het belangrijkste kenmerk van een primaire behoefte?", "opties": ["Het is strikt noodzakelijk om in leven te blijven.", "Het maakt het leven vooral luxueuzer en comfortabeler.", "Het is gratis verkrijgbaar in de vrije natuur.", "Het kan uitsluitend via een lening gefinancierd worden."], "antwoord": 0, "uitleg": "Primaire behoeften zoals water, voedsel en onderdak zijn essentieel om te overleven."},
      {"type": "mc", "vraag": "Welk van de onderstaande voorbeelden is een vrij goed?", "opties": ["Leidingwater uit de kraan", "Zonlicht op een open veld", "Een gratis proefmonster in de supermarkt", "Een openbare speelplaats"], "antwoord": 1, "uitleg": "Zonlicht kost geen productiemiddelen en is onbeperkt voorhanden in de natuur."},
      {"type": "mc", "vraag": "Wat betekent de term schaarste in de economische wetenschap?", "opties": ["Dat producten tijdelijk uitverkocht zijn in de schappen.", "Dat er productiemiddelen zijn ingezet om een goed te produceren.", "Dat consumenten het product weigeren te kopen.", "Dat een goed alleen in het buitenland gefabriceerd wordt."], "antwoord": 1, "uitleg": "Schaarste betekent dat middelen beperkt zijn ten opzichte van de oneindige menselijke behoeften."},
      {"type": "mc", "vraag": "Wat is een typisch voorbeeld van een dienst?", "opties": ["Een tube zonnebrandcrème", "Een wollen wintertrui", "Een knipbeurt bij de kapper", "Een paar leren schoenen"], "antwoord": 2, "uitleg": "Een knipbeurt is een niet-tastbare economische handeling (dienst)."},
      {"type": "mc", "vraag": "Waarom dwingt schaarste een consument tot het stellen van prioriteiten?", "opties": ["Omdat de overheid aankooplimieten oplegt aan burgers.", "Omdat tijd en financiële middelen beperkt zijn ten opzichte van onze wensen.", "Omdat producenten wettelijk geen reclame mogen maken.", "Omdat er geen vrije goederen meer beschikbaar zijn."], "antwoord": 1, "uitleg": "Beperkte middelen dwingen ieder individu tot keuzes tussen verschillende behoeften."},
      {"type": "mc", "vraag": "Wat is het belangrijkste verschil tussen goederen en diensten?", "opties": ["Goederen zijn altijd gratis en diensten zijn altijd betaald.", "Goederen zijn tastbare producten en diensten zijn niet-tastbare activiteiten.", "Goederen worden uitsluitend door de staat geleverd.", "Er bestaat in de economie geen enkel onderscheid tussen beide."], "antwoord": 1, "uitleg": "Goederen zijn fysiek tastbaar; diensten zijn onstoffelijke handelingen."},
      {"type": "mc", "vraag": "Welke van de volgende behoeften is een secundaire behoefte?", "opties": ["Een abonnement op een gaming-platform", "Zuiver drinkwater", "Eenvoudige basisvoeding", "Beschermende kleding tegen strenge vorst"], "antwoord": 0, "uitleg": "Gamen is ontspanning en luxe, en dus een secundaire behoefte."},
      {"type": "mc", "vraag": "Wat houdt het begrip zelfvoorziening in?", "opties": ["Al je inkomen automatisch laten sparen bij een bank.", "Zelf goederen telen of maken voor eigen consumptie zonder geld.", "Werken in loondienst bij een multinational.", "Geld lenen van vrienden of familieleden."], "antwoord": 1, "uitleg": "Bij zelfvoorziening produceer je zelf rechtstreeks voor eigen consumptie."},
      {"type": "mc", "vraag": "Wat verstaan economen onder de term consumeren?", "opties": ["Het produceren van halffabricaten in een fabriek.", "Het aanschaffen van goederen en diensten door eindgebruikers.", "Het exporteren van landbouwproducten naar buurlanden.", "Het heffen van accijnzen op tabak en alcohol."], "antwoord": 1, "uitleg": "Consumeren is het kopen van producten door consumenten ter bevrediging van behoeften."},
      {"type": "mc", "vraag": "Welke omstandigheid maakt dat elk mens economische keuzes moet maken?", "opties": ["De wetgeving van de Europese Unie", "De spanning tussen onbegrensde behoeften en beperkte middelen", "Het vaste aanbod in warenhuizen", "De vaste rentestand van commerciële banken"], "antwoord": 1, "uitleg": "De oneindigheid van wensen tegenover begrensde middelen is de kern van het keuzeprobleem."},
      {"type": "waaronwaar", "vraag": "Een luxe spelcomputer is een primaire behoefte voor tieners.", "antwoord": False, "uitleg": "Een spelcomputer is een secundair goed; je kunt zonder overleven."},
      {"type": "waaronwaar", "vraag": "Vrije goederen vereisen geen inzet van schaarse productiemiddelen.", "antwoord": True, "uitleg": "Zonlicht en wind zijn door de natuur gegeven en kosten geen arbeid of kapitaal."},
      {"type": "waaronwaar", "vraag": "Bij zelfvoorziening maak je gebruik van bankoverschrijvingen om te betalen.", "antwoord": False, "uitleg": "Zelfvoorziening vindt plaats zonder enige vorm van geld of betaling."},
      {"type": "waaronwaar", "vraag": "Als een product schaars is, betekent dit dat er middelen zijn opgeofferd om het voort te brengen.", "antwoord": True, "uitleg": "Economische schaarste betekent dat er tijd, arbeid en grondstoffen voor nodig waren."},
      {"type": "invul", "vraag": "Goederen die de natuur ons gratis en onbeperkt schenkt noemen we [vrije goederen|vrij goed].", "antwoord": "vrije goederen|vrij goed", "uitleg": "Vrije goederen zijn niet schaars en kosten geen productiemiddelen."},
      {"type": "invul", "vraag": "Het kopen van producten door particulieren om in behoeften te voorzien heet [consumeren|consumptie].", "antwoord": "consumeren|consumptie", "uitleg": "Consumeren is het eindgebruik van goederen en diensten door consumenten."},
      {"type": "invul", "vraag": "Behoeften die noodzakelijk zijn om fysiek te kunnen overleven heten [primaire behoeften|basisbehoeften].", "antwoord": "primaire behoeften|basisbehoeften", "uitleg": "Primaire behoeften zijn de basisvoorwaarden voor het menselijk bestaan."},
      {"type": "invul", "vraag": "Niet-tastbare werkzaamheden die voor een ander worden verricht noemen we [diensten|dienst].", "antwoord": "diensten|dienst", "uitleg": "Diensten zijn onlichamelijke prestaties zoals openbaar vervoer of medische zorg."},
      {"type": "open", "vraag": "Leg uit waarom een economisch goed schaars wordt genoemd, ook al liggen de winkelrekken er vol mee.", "sleutelwoorden": ["productiemiddelen/arbeid/tijd", "opgeofferd/inzet/kost"], "minTreffers": 1, "modelantwoord": "Een goed is economisch schaars omdat er productiemiddelen (tijd, arbeid, grondstoffen) voor zijn opgeofferd om het te maken.", "uitleg": "Schaarste in de economie betekent dat iets niet vanzelf ontstaat maar middelen kost."},
      {"type": "open", "vraag": "Noem twee concrete voorbeelden van secundaire behoeften van een middelbare scholier.", "sleutelwoorden": ["smartphone/telefoon", "merkkleding/scooter/gaming/bioscoop"], "minTreffers": 1, "modelantwoord": "Bijvoorbeeld een smartphone, merkkleding, spelcomputer, bioscoopbezoek of een scooter.", "uitleg": "Dit zijn luxe behoeften die het leven aangenamer maken maar niet van levensbelang zijn."}
    ]
  },

  # Examen 2: 1.2 Inkomsten en uitgaven
  {
    "id": "ex-h3-economie-2",
    "hoofdstuk": 1,
    "paragraaf": "1.2",
    "titel": "Proeftoets 2: Inkomensvormen en soorten uitgaven",
    "vak": "Economie · HAVO 3",
    "icoon": "💶",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Tot welke uitgavencategorie behoort de maandelijkse huur van een appartement?", "opties": ["Incidentele uitgaven", "Vaste lasten", "Huishoudelijke uitgaven", "Variabele consumptie"], "antwoord": 1, "uitleg": "Huur is een contractueel vastgelegde, maandelijks terugkerende verplichting (vaste last)."},
      {"type": "mc", "vraag": "Welke van de volgende inkomens is een voorbeeld van een overdrachtsinkomen?", "opties": ["Salaris uit een bijbaan in de supermarkt", "Rente op een spaarrekening", "Studiefinanciering van de overheid", "Winst uit een eenmanszaak"], "antwoord": 2, "uitleg": "Bij een overdrachtsinkomen (zoals studiefinanciering) lever je geen directe economische tegenprestatie."},
      {"type": "mc", "vraag": "Wat is een kenmerkend voorbeeld van een incidentele uitgave?", "opties": ["De aankoop van een nieuwe wasmachine", "De wekelijkse boodschappen voor het ontbijt", "De maandelijkse zorgverzekeringspremie", "Het abonnement voor de sportschool"], "antwoord": 0, "uitleg": "Een wasmachine koop je slechts af en toe (grote incidentele uitgave)."},
      {"type": "mc", "vraag": "Onder welke inkomenscategorie valt het salaris dat een leraar maandelijks ontvangt?", "opties": ["Inkomen uit bezit", "Inkomen uit arbeid", "Overdrachtsinkomen", "Incidentele bate"], "antwoord": 1, "uitleg": "Salaris is de directe beloning voor geleverde arbeid."},
      {"type": "mc", "vraag": "Wat verstaan we onder huishoudelijke uitgaven van een gezin?", "opties": ["Jaarlijkse premies voor de opstalverzekering", "Wekelijkse en dagelijkse uitgaven voor levensmiddelen en schoonmaakartikelen", "De aflossing op een dertigjarige hypotheek", "De aanschaf van een nieuwe personenauto"], "antwoord": 1, "uitleg": "Huishoudelijke uitgaven betreffen de dagelijkse levensmiddelen en verzorging."},
      {"type": "mc", "vraag": "Welke inkomensvorm ontvangt een huiseigenaar die een tweede woning verhuurt?", "opties": ["Inkomen uit arbeid", "Overdrachtsinkomen", "Inkomen uit bezit", "Subsidie-inkomen"], "antwoord": 2, "uitleg": "Huuropbrengst en rente zijn beloningen voor het bezit van vermogen/onroerend goed."},
      {"type": "mc", "vraag": "Waarom zetten verstandige gezinnen maandelijks geld opzij voor reserveringsuitgaven?", "opties": ["Om te voorkomen dat ze belasting moeten betalen over hun spaargeld.", "Om onverwachte grote uitgaven en vervanging van apparaten probleemloos te betalen.", "Omdat banken dit wettelijk verplichten bij een betaalrekening.", "Om uitsluitend te kunnen beleggen in buitenlandse valuta."], "antwoord": 1, "uitleg": "Reserveren zorgt voor een financiële buffer voor toekomstige grote vervangingsuitgaven."},
      {"type": "mc", "vraag": "Wat is het kenmerk van vaste lasten van een huishouden?", "opties": ["Ze variëren sterk per week afhankelijk van het weer.", "Het zijn terugkerende uitgaven waaraan je vastzit door langlopende contracten.", "Het zijn uitsluitend uitgaven aan luxe merkartikelen.", "Ze worden altijd volledig betaald met contant muntgeld."], "antwoord": 1, "uitleg": "Vaste lasten (zoals huur en energie) keren op vaste momenten terug."},
      {"type": "mc", "vraag": "Welke van de volgende posten valt onder inkomen uit bezit?", "opties": ["Loon van een vakantiebaan", "Dividend uitgekeerd op aandelen", "Kinderbijslag van de Sociale Verzekeringsbank", "Fooien ontvangen in de horeca"], "antwoord": 1, "uitleg": "Dividend is de winstuitkering op aandelenbezit (vermogen)."},
      {"type": "mc", "vraag": "Wat voor soort uitgave is de jaarlijkse aanslag gemeentelijke afvalstoffenheffing?", "opties": ["Huishoudelijke uitgave", "Vaste last", "Incidentele uitgave", "Vrijwillige gift"], "antwoord": 1, "uitleg": "Gemeentelijke heffingen zijn verplichte, periodieke vaste lasten."},
      {"type": "waaronwaar", "vraag": "Kinderbijslag en AOW zijn vormen van inkomen uit arbeid.", "antwoord": False, "uitleg": "Dit zijn overdrachtsinkomens die worden uitgekeerd door de overheid zonder directe tegenprestatie."},
      {"type": "waaronwaar", "vraag": "Een abonnement van € 30 per maand voor mobiele telefonie behoort tot de vaste lasten.", "antwoord": True, "uitleg": "Omdat je aan een contract vastzit en maandelijks betaalt, is het een vaste last."},
      {"type": "waaronwaar", "vraag": "Dagelijkse uitgaven voor groente en fruit in de supermarkt zijn incidentele uitgaven.", "antwoord": False, "uitleg": "Dit zijn huishoudelijke (dagelijkse) uitgaven."},
      {"type": "waaronwaar", "vraag": "Door regelmatig te reserveren voorkom je geldproblemen als de cv-ketel kapot gaat.", "antwoord": True, "uitleg": "Reserveringsuitgaven zijn bedoeld om incidentele kosten en reparaties op te vangen."},
      {"type": "invul", "vraag": "De periodieke beloning die een werknemer ontvangt voor zijn werk heet [loon|salaris].", "antwoord": "loon|salaris", "uitleg": "Loon of salaris is de vergoeding voor verrichte arbeid."},
      {"type": "invul", "vraag": "Uitgaven die maandelijks volgens een contract terugkeren noemen we [vaste lasten|vaste last].", "antwoord": "vaste lasten|vaste last", "uitleg": "Vaste lasten zijn contractuele terugkerende kosten zoals huur of verzekering."},
      {"type": "invul", "vraag": "Inkomen waarvoor je geen directe economische prestatie levert heet [overdrachtsinkomen|overdrachtsinkomens].", "antwoord": "overdrachtsinkomen|overdrachtsinkomens", "uitleg": "Overdrachtsinkomens worden door de overheid of familie overgedragen (bijv. zakgeld, bijstand)."},
      {"type": "invul", "vraag": "Het sparen van geld voor toekomstige grote reparaties of vervangingen noemen we [reserveren|reserveringsuitgaven].", "antwoord": "reserveren|reserveringsuitgaven", "uitleg": "Reserveren is het apart zetten van geld voor incidentele kosten."},
      {"type": "open", "vraag": "Leg het verschil uit tussen een actieve inkomensbron en een inkomensbron uit vermogen aan de hand van twee duidelijke voorbeelden.", "sleutelwoorden": ["arbeid/loon/salaris", "bezit/rente/huur/dividend"], "minTreffers": 2, "modelantwoord": "Inkomen uit arbeid is beloning voor werk (bijv. loon of salaris), terwijl inkomen uit bezit beloning is voor vermogen (bijv. spaarrente, dividend of huuropbrengst).", "uitleg": "Arbeid vraagt een actieve inspanning; bezit levert rendement op over vermogen."},
      {"type": "open", "vraag": "Noem de drie hoofdgroepen van gezinsuitgaven en geef bij elk één concreet voorbeeld.", "sleutelwoorden": ["vaste lasten", "huishoudelijke", "incidentele"], "minTreffers": 2, "modelantwoord": "1. Vaste lasten (huur), 2. Huishoudelijke uitgaven (boodschappen), 3. Incidentele uitgaven (wasmachine/vakantie).", "uitleg": "Dit zijn de drie standaardcategorieën van het NIBUD."}
    ]
  },

  # Examen 3: 1.3 Budgetteren
  {
    "id": "ex-h3-economie-3",
    "hoofdstuk": 1,
    "paragraaf": "1.3",
    "titel": "Proeftoets 3: Budgetteren, begroting en NIBUD",
    "vak": "Economie · HAVO 3",
    "icoon": "📊",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Duru verdient met haar krantenwijk € 24 per week. Hoeveel bedragen haar inkomsten gemiddeld per maand?", "opties": ["€ 96", "€ 104", "€ 110", "€ 120"], "antwoord": 1, "uitleg": "(24 × 52) / 12 = 1.248 / 12 = € 104 per maand."},
      {"type": "mc", "vraag": "Wat is een begrotingsevenwicht?", "opties": ["De uitgaven zijn exact twee keer zo hoog als de inkomsten.", "De totale verwachte inkomsten zijn precies gelijk aan de totale verwachte uitgaven.", "Er is geen spaargeld op de bankrekening aanwezig.", "Alle schulden zijn in één maand afgelost."], "antwoord": 1, "uitleg": "Bij evenwicht zijn de begrote baten en lasten gelijk aan elkaar."},
      {"type": "mc", "vraag": "Een gezin betaalt € 600 per kwartaal aan energie. Hoeveel is dit per maand?", "opties": ["€ 150", "€ 200", "€ 250", "€ 300"], "antwoord": 1, "uitleg": "Een kwartaal = 3 maanden. € 600 / 3 = € 200 per maand."},
      {"type": "mc", "vraag": "Wat is het voornaamste doel van het opstellen van een budgetplan?", "opties": ["Om direct een lening aan te vragen bij een bank.", "Om inzicht te krijgen in toekomstige geldstromen en geldproblemen te voorkomen.", "Om zoveel mogelijk contant geld in huis te bewaren.", "Om geen administratiekosten meer te betalen."], "antwoord": 1, "uitleg": "Budgetteren geeft grip op inkomsten en uitgaven en voorkomt tekorten."},
      {"type": "mc", "vraag": "Wat betekent een begrotingsoverschot?", "opties": ["De uitgaven overstijgen de inkomsten.", "De inkomsten zijn groter dan de uitgaven.", "Er is sprake van torenhoge inflatie.", "Het banksaldo is geblokkeerd."], "antwoord": 1, "uitleg": "Bij een overschot houd je geld over dat je kunt sparen of investeren."},
      {"type": "mc", "vraag": "Hoe reken je een maandelijks bedrag van € 75 om naar een jaarbedrag?", "opties": ["75 × 4", "75 × 10", "75 × 12", "75 × 52"], "antwoord": 2, "uitleg": "1 jaar heeft 12 maanden, dus € 75 × 12 = € 900 per jaar."},
      {"type": "mc", "vraag": "Welke instantie geeft in Nederland onafhankelijk advies over verantwoord budgetteren?", "opties": ["De Nederlandsche Bank (DNB)", "Het NIBUD (Nationaal Instituut voor Budgetvoorlichting)", "De Autoriteit Financiële Markten (AFM)", "Het Centraal Planbureau (CPB)"], "antwoord": 1, "uitleg": "Het NIBUD berekent richtbedragen en geeft budgetvoorlichting aan consumenten."},
      {"type": "mc", "vraag": "Wat moet een huishouden doen bij een structureel begrotingstekort?", "opties": ["Nog meer abonnementen afsluiten", "De uitgaven verlagen (bezuinigen) of de inkomsten proberen te verhogen", "Stoppen met het bijhouden van de administratie", "Al het spaargeld direct contant opnemen"], "antwoord": 1, "uitleg": "Bij een tekort moet je bezuinigen op uitgaven of extra inkomsten werven."},
      {"type": "mc", "vraag": "Een fitnessabonnement kost € 360 per jaar. Wat zijn de maandelijkse kosten?", "opties": ["€ 25", "€ 30", "€ 35", "€ 40"], "antwoord": 1, "uitleg": "€ 360 / 12 = € 30 per maand."},
      {"type": "mc", "vraag": "Waarom mag je bij omrekening van week naar maand NIET simpelweg vermenigvuldigen met 4?", "opties": ["Omdat banken 5 weken per maand rekenen.", "Omdat een jaar 52 weken telt en 52/12 gelijk is aan 4,33 weken per maand.", "Omdat schrikkeljaren geen maanden hebben.", "Omdat zakgeld wekelijks wordt belast."], "antwoord": 1, "uitleg": "Een jaar heeft 52 weken, dus 52/12 = 4,33 weken per maand."},
      {"type": "waaronwaar", "vraag": "Als een begroting een tekort vertoont, zijn de inkomsten hoger dan de uitgaven.", "antwoord": False, "uitleg": "Bij een tekort zijn juist de uitgaven hoger dan de inkomsten."},
      {"type": "waaronwaar", "vraag": "Een kwartaal bestaat in het economisch rekenen uit precies 3 maanden.", "antwoord": True, "uitleg": "1 jaar = 4 kwartalen van elk 3 maanden."},
      {"type": "waaronwaar", "vraag": "Het NIBUD stelt wetten op waarmee burgers verplicht worden hun uitgaven te halveren.", "antwoord": False, "uitleg": "Het NIBUD adviseert en informeert; zij hebben geen wetgevende macht."},
      {"type": "waaronwaar", "vraag": "Door vaste lasten en inkomsten per maand gelijk te trekken, ontstaat overzicht in je bestedingsruimte.", "antwoord": True, "uitleg": "Maandelijkse standaarden maken vergelijking en planning mogelijk."},
      {"type": "invul", "vraag": "Het financiële plan waarin verwachte inkomsten en uitgaven op elkaar worden afgestemd heet een [begroting|budgetplan].", "antwoord": "begroting|budgetplan", "uitleg": "Een begroting is een overzicht van verwachte toekomstige baten en lasten."},
      {"type": "invul", "vraag": "Als de inkomsten groter zijn dan de uitgaven ontstaat een [begrotingsoverschot|overschot].", "antwoord": "begrotingsoverschot|overschot", "uitleg": "Een begrotingsoverschot betekent een positief saldo op de begroting."},
      {"type": "invul", "vraag": "De afkorting van het Nationaal Instituut voor Budgetvoorlichting is [NIBUD|Nibud].", "antwoord": "NIBUD|Nibud", "uitleg": "NIBUD staat voor Nationaal Instituut voor Budgetvoorlichting."},
      {"type": "invul", "vraag": "Om weekbedragen om te rekenen naar maandbedragen vermenigvuldig je met 52 en deel je door [12].", "antwoord": "12", "uitleg": "Formule: (weekbedrag × 52) / 12."},
      {"type": "open", "vraag": "Bereken de maandelijkse kosten van een zorgverzekering die € 390 per kwartaal bedraagt. Geef de berekening.", "sleutelwoorden": ["390 / 3", "130"], "minTreffers": 1, "modelantwoord": "390 / 3 = € 130 per maand.", "uitleg": "Een kwartaal telt 3 maanden; dus 390 delen door 3 is 130 euro per maand."},
      {"type": "open", "vraag": "Noem twee maatregelen die een gezin kan nemen om een begrotingstekort op te lossen.", "sleutelwoorden": ["bezuinigen/uitgaven verlagen/besparen", "meer werken/inkomsten verhogen/extra baan"], "minTreffers": 1, "modelantwoord": "1. Bezuinigen op variabele of incidentele uitgaven (abonnementen opzeggen), 2. Extra inkomsten genereren (overwerken, bijbaan).", "uitleg": "Een tekort los je op door kosten te drukken of inkomsten te verhogen."}
    ]
  },

  # Examen 4: 2.1 Ontstaan van geld
  {
    "id": "ex-h3-economie-4",
    "hoofdstuk": 2,
    "paragraaf": "2.1",
    "titel": "Proeftoets 4: Ontstaan van geld en directe/indirecte ruil",
    "vak": "Economie · HAVO 3",
    "icoon": "🪙",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Wat is een groot nadeel van directe ruil (ruil in natura)?", "opties": ["Er is altijd wisselgeld nodig in gouden munten.", "Het kost veel tijd om iemand te vinden met wie je wensen exact overeenkomen.", "De belastingdienst heft 21% btw op elke ruil.", "Directe ruil is wettelijk verboden in Europa."], "antwoord": 1, "uitleg": "Directe ruil vereist een dubbele samenval van wensen, wat zeer inefficiënt is."},
      {"type": "mc", "vraag": "Wat verstaan we onder indirecte ruil?", "opties": ["Goederen ruilen tegen goederen zonder tussenkomst van geld.", "Goederen ruilen met behulp van een algemeen aanvaard ruilmiddel (zoals geld).", "Online goederen bestellen via buitenlandse webwinkels.", "Geld lenen van een commerciële bank."], "antwoord": 1, "uitleg": "Bij indirecte ruil verkoop je een goed voor geld en koop je met dat geld een ander goed."},
      {"type": "mc", "vraag": "Welke van de onderstaande goederen diende in het verleden vaak als goederengeld?", "opties": ["Zout en schelpen", "Plastic jetons", "Digitale tegoedbonnen", "Gedrukte kranten"], "antwoord": 0, "uitleg": "Zout, schelpen en vee waren duurzame, zeldzame goederen die als vroeg geld fungeerden."},
      {"type": "mc", "vraag": "Waarom werd goud en zilver eeuwenlang als metaalgeld gebruikt?", "opties": ["Omdat het snel oxideert en vergaat in water.", "Omdat het schaars, duurzaam en makkelijk deelbaar was.", "Omdat iedereen het gratis kon opgraven in zijn achtertuin.", "Omdat het verplicht was door de Verenigde Naties."], "antwoord": 1, "uitleg": "Edelmetalen behouden hun waarde, rotten niet en kunnen in munten geslagen worden."},
      {"type": "mc", "vraag": "Waarop is de waarde van modern fiduciair geld gebaseerd?", "opties": ["Op de goudvoorraad in de kluis van de centrale bank.", "Op het onderlinge vertrouwen dat iedereen het geld accepteert.", "Op de hoge intrinsieke materiaalwaarde van papier en inkt.", "Op de hoeveelheid aardgas in de bodem."], "antwoord": 1, "uitleg": "Fiduciair geld ontleent zijn waarde aan vertrouwen (fiducia)."},
      {"type": "mc", "vraag": "Hoe zijn de eerste bankbiljetten in Europa ontstaan?", "opties": ["Als speelgeld voor adellijke families.", "Uit ontvangstbewijzen van goudsmeden waar mensen goud in bewaring gaven.", "Als belastingaanslagen van de koning.", "Door uitvinding van de pinautomaat."], "antwoord": 1, "uitleg": "Papieren bewaarbewijzen van goudsmeden gingen als betaalmiddel circuleren."},
      {"type": "mc", "vraag": "Waarom is een levende koe als betaalmiddel economisch onhandig?", "opties": ["Omdat een koe geen waarde heeft.", "Omdat een koe moeilijk deelbaar is zonder waardeverlies en onderhoud kost.", "Omdat koeien niet in Nederland voorkomen.", "Omdat banken geen vee accepteren op de spaarrekening."], "antwoord": 1, "uitleg": "Levend vee is ondeelbaar, bederfelijk en lastig te transporteren."},
      {"type": "mc", "vraag": "Wat betekent het Latijnse woord fiducia?", "opties": ["Macht", "Rijkdom", "Vertrouwen", "Betaling"], "antwoord": 2, "uitleg": "Fiducia betekent vertrouwen."},
      {"type": "mc", "vraag": "Wat was de functie van een muntstempel door een vorst op metaalgeld?", "opties": ["Het garanderen van het gewicht en het gehalte aan edelmetaal van de munt.", "Het heffen van invoerrechten.", "Het verbieden van buitenlandse handel.", "Het aangeven van de houdbaarheidsdatum."], "antwoord": 0, "uitleg": "Het koninklijke stempel gaf garantie over het gewicht en de zuiverheid van het metaal."},
      {"type": "mc", "vraag": "Welke overgang markeert het ontstaan van geld in de geschiedenis?", "opties": ["Van vrije handel naar planeconomie", "Van directe ruil naar indirecte ruil", "Van chartaal geld naar goederengeld", "Van giraal geld naar schelpenhandel"], "antwoord": 1, "uitleg": "De komst van een algemeen ruilmiddel maakte indirecte ruil mogelijk."},
      {"type": "waaronwaar", "vraag": "Bij directe ruil ruil je goederen direct tegen elkaar zonder geld te gebruiken.", "antwoord": True, "uitleg": "Directe ruil is ruil in natura."},
      {"type": "waaronwaar", "vraag": "Het papier van een 100-eurobiljet heeft een intrinsieke materiaalwaarde van exact 100 euro.", "antwoord": False, "uitleg": "De materiaalwaarde is slechts enkele centen; de nominale waarde is 100 euro."},
      {"type": "waaronwaar", "vraag": "Goederengeld had naast ruilmiddel vaak ook een eigen gebruiks- of consumptiewaarde.", "antwoord": True, "uitleg": "Zout kon je eten en vee gaf melk en vlees."},
      {"type": "waaronwaar", "vraag": "Tegenwoordig kun je met een bankbiljet bij de bank altijd de tegenwaarde in puur goud opeisen.", "antwoord": False, "uitleg": "De goudstandaard is al decennia geleden volledig afgeschaft."},
      {"type": "invul", "vraag": "Het ruilen van goederen tegen goederen zonder geld noemen we [directe ruil|ruil in natura].", "antwoord": "directe ruil|ruil in natura", "uitleg": "Directe ruil is handel in natura."},
      {"type": "invul", "vraag": "Geld waarvan de waarde berust op onderling vertrouwen heet [fiduciair geld|fiduciair].", "antwoord": "fiduciair geld|fiduciair", "uitleg": "Fiduciair geld heeft geen intrinsieke gouddekking meer."},
      {"type": "invul", "vraag": "Vroegere ruilmiddelen zoals schelpen, zout en vee noemen we [goederengeld].", "antwoord": "goederengeld", "uitleg": "Goederengeld bestaat uit goederen die tevens als ruilmiddel dienstdeden."},
      {"type": "invul", "vraag": "Het ruilen van goederen met behulp van een algemeen ruilmiddel noemen we [indirecte ruil].", "antwoord": "indirecte ruil", "uitleg": "Indirecte ruil verloopt via geld."},
      {"type": "open", "vraag": "Noem twee nadelen van directe ruil vergeleken met betalen met geld.", "sleutelwoorden": ["dubbele samenval/wensen vinden", "bederfelijk/niet houdbaar/ondeelbaar"], "minTreffers": 1, "modelantwoord": "1. Moeilijk iemand te vinden die elkaars goederen wil hebben (dubbele samenval van wensen), 2. Goederen zijn bederfelijk of lastig te verdelen.", "uitleg": "Directe ruil kost veel transactietijd en goederen bederven."},
      {"type": "open", "vraag": "Leg uit waarom vertrouwen essentieel is voor het functioneren van ons huidige geldsysteem.", "sleutelwoorden": ["intrinsieke/materiaalwaarde laag", "iedereen accepteert/aanvaardt"], "minTreffers": 1, "modelantwoord": "Omdat bankbiljetten en digitaal geld nauwelijks intrinsieke materiaalwaarde hebben; het werkt alleen als iedereen erop vertrouwt dat een ander het ook als betaalmiddel accepteert.", "uitleg": "Fiduciair geld staat of valt bij maatschappelijk acceptatievertrouwen."}
    ]
  },

  # Examen 5: 2.2 Waarde van geld & Functies
  {
    "id": "ex-h3-economie-5",
    "hoofdstuk": 2,
    "paragraaf": "2.2",
    "titel": "Proeftoets 5: De functies en verschijningsvormen van geld",
    "vak": "Economie · HAVO 3",
    "icoon": "💳",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Welke functie van geld gebruik je wanneer je een pizza afrekent met je pinpas?", "opties": ["Oppotmiddel", "Ruilmiddel (betaalmiddel)", "Rekenmiddel", "Beleggingsmiddel"], "antwoord": 1, "uitleg": "Direct betalen voor een product is de functie ruilmiddel."},
      {"type": "mc", "vraag": "Wat is het verschil tussen chartaal en giraal geld?", "opties": ["Chartaal geld is tastbaar (munten/biljetten); giraal geld is digitaal banktegoed.", "Chartaal geld is van de overheid; giraal geld is uitsluitend van particulieren.", "Chartaal geld is buitenlands geld; giraal geld is de euro.", "Er is geen enkel juridisch of economisch verschil."], "antwoord": 0, "uitleg": "Chartaal geld kun je vastpakken; giraal geld staat op een betaalrekening."},
      {"type": "mc", "vraag": "Wat betekent de nominale waarde van een bankbiljet van 50 euro?", "opties": ["De waarde van het katoenen papier.", "Het getal van 50 euro dat op het biljet gedrukt staat.", "De wisselkoers van het biljet in Japanse Yen.", "De productiekosten bij de drukkerij."], "antwoord": 1, "uitleg": "Nominale waarde is de officiële opdrukwaarde."},
      {"type": "mc", "vraag": "Duru spaart 500 euro op haar spaarrekening voor een studiereis. Welke geldfunctie staat hier centraal?", "opties": ["Rekenmiddel", "Oppotmiddel (spaarmiddel)", "Ruilmiddel", "Chartaal middel"], "antwoord": 1, "uitleg": "Geld bewaren voor toekomstig gebruik is de oppotfunctie."},
      {"type": "mc", "vraag": "Hoe noemen we de economische waarde die gebaseerd is op het zuivere metaal van een munt?", "opties": ["De koopkracht in de supermarkt", "De zuivere materiaalwaarde van het metaal", "De rentevergoeding op de bank", "Het serienummer van de munt"], "antwoord": 1, "uitleg": "Intrinsieke waarde is de waarde van het fysieke materiaal van het geldstuk."},
      {"type": "mc", "vraag": "In een kledingwinkel vergelijkt Duru een jurk van € 60 met een trui van € 30. Welke geldfunctie benut zij?", "opties": ["Rekenmiddel (waardemeter)", "Oppotmiddel", "Ruilmiddel", "Giraal middel"], "antwoord": 0, "uitleg": "Prijzen met elkaar vergelijken is de functie rekenmiddel."},
      {"type": "mc", "vraag": "Welke van de onderstaande vormen behoort tot het girale geld?", "opties": ["Een herdenkingsmunt van 5 euro in een kluis", "Een positief saldo op een direct opvraagbare betaalrekening", "Een briefje van 20 euro in een jaszak", "Goudstaven bewaard bij een handelaar"], "antwoord": 1, "uitleg": "Direct opeisbaar banktegoed is giraal geld."},
      {"type": "mc", "vraag": "Waarom is de intrinsieke waarde van moderne euromunten lager dan de nominale waarde?", "opties": ["Om te voorkomen dat mensen munten gaan omsmelten voor de metaalwaarde.", "Omdat de Europese Centrale Bank geen koper meer mag inkopen.", "Om munten zwaarder te maken voor verkoopautomaten.", "Omdat munten anders te snel slijten."], "antwoord": 0, "uitleg": "Als de metaalwaarde hoger zou zijn dan de muntwaarde, zouden mensen munten omsmelten."},
      {"type": "mc", "vraag": "Wat is een kenmerk van giraal geld?", "opties": ["Je kunt het fysiek in een spaarpot stoppen.", "Je verplaatst het elektronisch via pinnen, mobiel bankieren of overschrijving.", "Het is niet beschermd door bankgaranties.", "Het kan uitsluitend in vreemde valuta worden aangehouden."], "antwoord": 1, "uitleg": "Giraal geld circuleert via girale overboekingen en elektronische betaalmethoden."},
      {"type": "mc", "vraag": "Welke drie functies vervult geld in de economie?", "opties": ["Lenen, investeren en speculeren", "Ruilmiddel, rekenmiddel en oppotmiddel", "Chartaal, giraal en vreemde valuta", "Nominaal, reëel en inflatoir"], "antwoord": 1, "uitleg": "De drie klassieke geldfuncties zijn ruilen, rekenen en oppotten/sparen."},
      {"type": "waaronwaar", "vraag": "Munten en bankbiljetten in de kassa van een supermarkt zijn chartaal geld.", "antwoord": True, "uitleg": "Fysieke munten en biljetten vallen onder chartaal geld."},
      {"type": "waaronwaar", "vraag": "Giraal geld kun je niet omzetten in chartaal geld.", "antwoord": False, "uitleg": "Bij een geldautomaat pin je giraal saldo om naar chartale bankbiljetten."},
      {"type": "waaronwaar", "vraag": "Als rekenmiddel stelt geld ons in staat de waarde van verschillende goederen objectief te vergelijken.", "antwoord": True, "uitleg": "Prijzen in euro's maken waardevergelijking tussen producten mogelijk."},
      {"type": "waaronwaar", "vraag": "De intrinsieke waarde van een bankbiljet van 100 euro is gelijk aan 100 euro.", "antwoord": False, "uitleg": "De intrinsieke materiaalwaarde van het papier is slechts een fractie van een cent."},
      {"type": "invul", "vraag": "Fysieke munten en bankbiljetten noemen we [chartaal geld|chartaal].", "antwoord": "chartaal geld|chartaal", "uitleg": "Chartaal geld is tastbaar contant geld."},
      {"type": "invul", "vraag": "Direct opvraagbaar geld op een bankrekening noemen we [giraal geld|giraal].", "antwoord": "giraal geld|giraal", "uitleg": "Giraal geld is elektronisch banktegoed."},
      {"type": "invul", "vraag": "Het bedrag dat officieel op een munt of biljet staat gedrukt heet de [nominale waarde|nominaal].", "antwoord": "nominale waarde|nominaal", "uitleg": "De nominale waarde is de aangegeven waarde op het geldstuk."},
      {"type": "invul", "vraag": "De materiële waarde van het metaal of papier van geld heet de [intrinsieke waarde|intrinsiek].", "antwoord": "intrinsieke waarde|intrinsiek", "uitleg": "Intrinsieke waarde is de zuivere grondstofwaarde."},
      {"type": "open", "vraag": "Noem de drie functies van geld en geef bij elke functie een kort voorbeeld.", "sleutelwoorden": ["ruilmiddel", "rekenmiddel", "oppotmiddel/spaarmiddel"], "minTreffers": 3, "modelantwoord": "1. Ruilmiddel (brood betalen), 2. Rekenmiddel (prijzen vergelijken), 3. Oppotmiddel (sparen voor later).", "uitleg": "Dit zijn de drie kernfuncties van geld."},
      {"type": "open", "vraag": "Leg uit wat er zou gebeuren als de intrinsieke waarde van een 1-euromunt zou stijgen naar 1,50 euro.", "sleutelwoorden": ["omsmelten/verkopen als metaal", "uit circulatie verdwijnen/winst"], "minTreffers": 1, "modelantwoord": "Mensen zouden de munten massaal verzamelen en omsmelten om het metaal voor 1,50 euro te verkopen, waardoor de munten uit de roulatie verdwijnen.", "uitleg": "Dit fenomeen heet de wet van Gresham."}
    ]
  },

  # Examen 6: 2.3 Koopkracht & Inflatie
  {
    "id": "ex-h3-economie-6",
    "hoofdstuk": 2,
    "paragraaf": "2.3",
    "titel": "Proeftoets 6: Koopkracht, inflatie en het CBS",
    "vak": "Economie · HAVO 3",
    "icoon": "📈",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Wat betekent inflatie voor de waarde van ons geld?", "opties": ["Het geld wordt meer waard; prijzen dalen.", "Het geld wordt minder waard; prijzen stijgen gemiddeld.", "De rentestand op leningen daalt automatisch naar nul.", "Er mag geen buitenlandse valuta meer gewisseld worden."], "antwoord": 1, "uitleg": "Inflatie is een stijging van het algemene prijspeil, waardoor geld ontwaardt."},
      {"type": "mc", "vraag": "Duru krijgt 3% salarisverhoging. In hetzelfde jaar stijgen de prijzen in de winkels met 5%. Wat gebeurt er met haar koopkracht?", "opties": ["Haar koopkracht stijgt met 2%.", "Haar koopkracht daalt met ongeveer 2%.", "Haar koopkracht blijft gelijk.", "Haar nominale inkomen daalt met 5%."], "antwoord": 1, "uitleg": "Omdat de prijzen harder stijgen (+5%) dan het loon (+3%), kan zij reëel minder kopen (-2%)."},
      {"type": "mc", "vraag": "Wat is het verschil tussen het nominale en het reële inkomen?", "opties": ["Nominaal is in euro's uitgedrukt; reëel meet de hoeveelheid goederen die je ermee kunt kopen (koopkracht).", "Nominaal is het nettosalaris; reëel is het brutosalaris.", "Nominaal is voor ambtenaren; reëel voor ondernemers.", "Er is geen verschil."], "antwoord": 0, "uitleg": "Nominaal = bedrag in geld; reëel = koopkracht."},
      {"type": "mc", "vraag": "Hoe meet het Centraal Bureau voor de Statistiek (CBS) de inflatie in Nederland?", "opties": ["Door te kijken naar de goudkoers op de beurs.", "Met de Consumentenprijsindex (CPI) aan de hand van een gemiddeld boodschappenmandje.", "Door alle bankrekeningen van burgers op te tellen.", "Door het aantal failliete bedrijven te tellen."], "antwoord": 1, "uitleg": "Het CBS monitort maandelijkse prijzen van een representatief mandje goederen en diensten (CPI)."},
      {"type": "mc", "vraag": "Wat is deflatie?", "opties": ["Een extreme stijging van de rentetarieven", "Een aanhoudende daling van het gemiddelde prijspeil", "Het plotseling verdwijnen van bankbiljetten", "Een verhoging van de btw op basisbehoeften"], "antwoord": 1, "uitleg": "Deflatie is het tegenovergestelde van inflatie: prijzen dalen."},
      {"type": "mc", "vraag": "Wat is prijscompensatie in een cao-onderhandeling?", "opties": ["Een loonsverhoging die gelijk is aan het inflatiepercentage om koopkracht te behouden.", "Een korting die supermarkten geven aan vaste klanten.", "Een subsidie van de overheid op luxe merkartikelen.", "Het afschaffen van de inkomstenbelasting."], "antwoord": 0, "uitleg": "Prijscompensatie zorgt dat lonen meestijgen met de inflatie."},
      {"type": "mc", "vraag": "Wie ondervindt het meeste nadeel van een aanhoudend hoge inflatie?", "opties": ["Mensen met hoge schulden", "Mensen met veel spaargeld en een vast inkomen dat niet meestijgt", "Bedrijven die hun verkoopprijzen direct kunnen verhogen", "De overheid die belasting int over hogere omzetten"], "antwoord": 1, "uitleg": "Spaarders zien de reële koopkracht van hun spaargeld snel verdampen."},
      {"type": "mc", "vraag": "Waarom kan aanhoudende deflatie gevaarlijk zijn voor de economie?", "opties": ["Omdat consumenten aankopen gaan uitstellen in afwachting van verdere prijsdalingen.", "Omdat er te veel bankbiljetten gedrukt moeten worden.", "Omdat de lonen explosief stijgen.", "Omdat het buitenland weigert goederen te leveren."], "antwoord": 0, "uitleg": "Uitgestelde bestedingen leiden tot minder productie en stijgende werkloosheid."},
      {"type": "mc", "vraag": "Als het nominale inkomen stijgt met 4% en de inflatie bedraagt 4%, wat gebeurt er met de reële koopkracht?", "opties": ["De koopkracht stijgt met 4%.", "De koopkracht blijft nagenoeg gelijk (0% verandering).", "De koopkracht daalt met 8%.", "Het reële inkomen verdubbelt."], "antwoord": 1, "uitleg": "Loonstijging compenseert exact de inflatie, dus de koopkracht verandert niet."},
      {"type": "mc", "vraag": "Wat meet de Consumentenprijsindex (CPI)?", "opties": ["De totale winst van alle Nederlandse beursgenoteerde bedrijven.", "De procentuele prijsverandering van goederen en diensten die huishoudens consumeren.", "De totale waarde van alle Nederlandse exportgoederen.", "Het aantal openstaande vacatures in de zorg."], "antwoord": 1, "uitleg": "CPI meet de prijsontwikkeling van het levensonderhoud van consumenten."},
      {"type": "waaronwaar", "vraag": "Door inflatie kun je met hetzelfde geldbedrag meer producten kopen dan voorheen.", "antwoord": False, "uitleg": "Bij inflatie stijgen prijzen en kun je juist minder kopen met hetzelfde geld."},
      {"type": "waaronwaar", "vraag": "Het CBS berekent de inflatie aan de hand van het consumentenprijsindexcijfer (CPI).", "antwoord": True, "uitleg": "Het CPI is de officiële maatstaf voor de inflatie in Nederland."},
      {"type": "waaronwaar", "vraag": "Prijscompensatie zorgt ervoor dat de koopkracht van werknemers op peil blijft.", "antwoord": True, "uitleg": "Lonen stijgen dan mee met de stijging van de consumentenprijzen."},
      {"type": "waaronwaar", "vraag": "Deflatie betekent dat alle prijzen gemiddeld met meer dan 10% stijgen.", "antwoord": False, "uitleg": "Deflatie betekent dalende prijzen."},
      {"type": "invul", "vraag": "Een algemene stijging van het gemiddelde prijspeil heet [inflatie].", "antwoord": "inflatie", "uitleg": "Inflatie is het duurder worden van het dagelijks leven."},
      {"type": "invul", "vraag": "De hoeveelheid goederen en diensten die je met je inkomen kunt kopen heet je [koopkracht|reëel inkomen].", "antwoord": "koopkracht|reëel inkomen", "uitleg": "Koopkracht is het reële inkomen."},
      {"type": "invul", "vraag": "De instantie die in Nederland de inflatie berekent is het [CBS|Centraal Bureau voor de Statistiek].", "antwoord": "CBS|Centraal Bureau voor de Statistiek", "uitleg": "CBS berekent de CPI en andere nationale statistieken."},
      {"type": "invul", "vraag": "Een algemene daling van het gemiddelde prijspeil noemen we [deflatie].", "antwoord": "deflatie", "uitleg": "Deflatie is een daling van het prijspeil."},
      {"type": "open", "vraag": "Leg uit waarom een loonsverhoging van 4% niet automatisch leidt tot meer koopkracht.", "sleutelwoorden": ["inflatie/prijzen stijgen", "harder stijgen/meer dan 4 procent"], "minTreffers": 1, "modelantwoord": "Als de prijzen in de winkels (inflatie) in hetzelfde jaar harder stijgen dan 4% (bijvoorbeeld met 6%), daalt de koopkracht ondanks de loonsverhoging.", "uitleg": "Koopkracht hangt af van het verschil tussen loongroei en prijsstijging."},
      {"type": "open", "vraag": "Wat is het verschil tussen nominaal inkomen en reëel inkomen?", "sleutelwoorden": ["nominaal is bedrag/in euros", "reëel is koopkracht/wat je kunt kopen"], "minTreffers": 2, "modelantwoord": "Nominaal inkomen is het bedrag in euro's op je loonstrook; reëel inkomen is de koopkracht (de hoeveelheid goederen en diensten die je met dat geld kunt kopen).", "uitleg": "Nominaal = geldgetal; reëel = koopkracht."}
    ]
  },

  # Examen 7: 3.1 Sparen
  {
    "id": "ex-h3-economie-7",
    "hoofdstuk": 3,
    "paragraaf": "3.1",
    "titel": "Proeftoets 7: Sparen, rente en spaarmotieven",
    "vak": "Economie · HAVO 3",
    "icoon": "🐖",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Duru zet € 4.000 op een spaarrekening tegen 2,5% rente per jaar. Hoeveel rente ontvangt zij na 1 jaar?", "opties": ["€ 50", "€ 100", "€ 150", "€ 200"], "antwoord": 1, "uitleg": "(4.000 × 2,5) / 100 = € 100 rente."},
      {"type": "mc", "vraag": "Wat is een voorbeeld van sparen uit voorzorg?", "opties": ["Sparen voor een vakantie naar Spanje", "Geld opzij zetten voor onverwachte medische kosten of autoreparaties", "Geld beleggen in risicovolle aandelen", "Een lening afsluiten voor een nieuwe keuken"], "antwoord": 1, "uitleg": "Sparen uit voorzorg is bedoeld als buffer voor onvoorziene tegenslagen."},
      {"type": "mc", "vraag": "Wat verstaan we onder samengestelde rente (rente-op-rente)?", "opties": ["Rente die je maandelijks contant moet ophalen.", "Rente die wordt bijgeschreven op je rekening en in het volgende jaar zélf ook rente oplevert.", "Een boeterente bij te late betaling.", "Rente die je betaalt aan de Belastingdienst."], "antwoord": 1, "uitleg": "Bij samengestelde rente groeit het kapitaal steeds sneller doordat rente over rente wordt berekend."},
      {"type": "mc", "vraag": "Wat is het belangrijkste kenmerk van een spaardeposito?", "opties": ["Je kunt er dagelijks onbeperkt mee pinnen in winkels.", "Het spaargeld staat voor een vooraf afgesproken periode vast tegen een vaste rente.", "Je betaalt maandelijks een boete over je spaartegoed.", "Het deposito is uitsluitend bestemd voor bedrijven."], "antwoord": 1, "uitleg": "Bij een deposito staat het geld voor een vaste looptijd vast."},
      {"type": "mc", "vraag": "Tot welk bedrag beschermt het depositogarantiestelsel spaargeld per persoon per bankvergunning in Nederland?", "opties": ["€ 25.000", "€ 50.000", "€ 100.000", "€ 250.000"], "antwoord": 2, "uitleg": "Het wettelijke garantiestelsel dekt spaartegoeden tot maximaal € 100.000."},
      {"type": "mc", "vraag": "Wat is een belangrijk motief om te sparen voor het rendement?", "opties": ["Zoveel mogelijk schulden opbouwen", "Extra inkomen genereren uit de rentevergoeding van de bank", "Voorkomen dat je contant geld gebruikt", "Uitsluitend sparen voor een geplande aankoop"], "antwoord": 1, "uitleg": "Bij het rendementsmotief spaar je om je vermogen te laten aangroeien door rente."},
      {"type": "mc", "vraag": "Hoe bereken je de rente over 6 maanden op een spaarbedrag van € 3.000 tegen 4% per jaar?", "opties": ["(3.000 × 4) / 100", "(3.000 × 4 × 6) / (100 × 12)", "(3.000 × 6) / 100", "(3.000 × 4 × 12) / 100"], "antwoord": 1, "uitleg": "Rente voor een deel van het jaar: (Bedrag × Percentage × Maanden) / (100 × 12) = € 60."},
      {"type": "mc", "vraag": "Wat gebeurt er met het rentepercentage bij een variabele spaarrente?", "opties": ["Het rentepercentage staat voor altijd muurvast.", "De bank kan het rentepercentage op ieder moment verhogen of verlagen.", "Het rentepercentage daalt elk jaar met exact 1%.", "Het rentepercentage is gekoppeld aan de goudkoers."], "antwoord": 1, "uitleg": "Een variabele rente beweegt mee met de marktrente en kan wijzigen."},
      {"type": "mc", "vraag": "Waarom spaart iemand 'voor een doel'?", "opties": ["Omdat men bang is voor onverwachte pech", "Om over een bepaalde tijd een specifieke aankoop (zoals een rijbewijs) te kunnen betalen", "Omdat de overheid sparen verplicht stelt", "Om uitsluitend rente op rente te ontvangen"], "antwoord": 1, "uitleg": "Doelsparen richt zich op een concrete toekomstige aanschaf."},
      {"type": "mc", "vraag": "Wat is het effect van inflatie op je spaargeld als de spaarrente 1% is en de inflatie 4%?", "opties": ["De reële waarde van je spaargeld groeit met 3%.", "De reële koopkracht van je spaargeld daalt met ongeveer 3%.", "Je spaargeld verdubbelt in 5 jaar.", "Er verandert niets aan de koopkracht van het spaargeld."], "antwoord": 1, "uitleg": "Omdat inflatie hoger is dan de spaarrente, verliest het spaargeld reële koopkracht."},
      {"type": "waaronwaar", "vraag": "Sparen is het uitstellen van consumptie naar de toekomst.", "antwoord": True, "uitleg": "Door nu niet uit te geven houd je middelen over voor later."},
      {"type": "waaronwaar", "vraag": "Bij een spaardeposito kun je op ieder willekeurig moment zonder boete al je geld opnemen.", "antwoord": False, "uitleg": "Het geld staat vast; tussentijds opnemen kost vaak een boeterente."},
      {"type": "waaronwaar", "vraag": "Samengestelde rente leidt ertoe dat je spaarbedrag elk jaar sneller groeit.", "antwoord": True, "uitleg": "Omdat je ook rente over rente ontvangt, versnelt de vermogensgroei."},
      {"type": "waaronwaar", "vraag": "Het depositogarantiestelsel keert bij faillissement maximaal 1 miljoen euro per burger uit.", "antwoord": False, "uitleg": "De wettelijke limiet bedraagt € 100.000 per persoon per bank."},
      {"type": "invul", "vraag": "De vergoeding die je van de bank ontvangt over je spaargeld heet [rente|spaarloon].", "antwoord": "rente|spaarloon", "uitleg": "Rente is de prijs voor het uitlenen van spaargeld."},
      {"type": "invul", "vraag": "Het fenomeen waarbij rente bij het kapitaal wordt opgeteld en zelf weer rente oplevert heet [samengestelde rente|rente op rente].", "antwoord": "samengestelde rente|rente op rente", "uitleg": "Samengestelde rente is rente-op-rente."},
      {"type": "invul", "vraag": "Het wettelijke stelsel dat spaargeld tot € 100.000 garandeert heet het [depositogarantiestelsel].", "antwoord": "depositogarantiestelsel", "uitleg": "Het depositogarantiestelsel waarborgt spaartegoeden."},
      {"type": "invul", "vraag": "Een spaarrekening waarop geld voor een afgesproken vaste periode vaststaat heet een [spaardeposito|deposito].", "antwoord": "spaardeposito|deposito", "uitleg": "Bij een deposito staat het spaargeld tijdelijk vast."},
      {"type": "open", "vraag": "Noem de drie motieven om te sparen en geef bij elk motief een voorbeeld.", "sleutelwoorden": ["voor een doel", "uit voorzorg", "voor het rendement/rente"], "minTreffers": 3, "modelantwoord": "1. Sparen voor een doel (vakantie/scooter), 2. Sparen uit voorzorg (onverwachte reparatie wasmachine), 3. Sparen voor het rendement (extra inkomsten via rente).", "uitleg": "Dit zijn de drie klassieke spaarmotieven."},
      {"type": "open", "vraag": "Bereken de enkelvoudige rente na 9 maanden over een spaarbedrag van € 6.000 bij een rente van 2% per jaar. Toon de berekening.", "sleutelwoorden": ["(6000 * 2 * 9) / 1200", "90"], "minTreffers": 1, "modelantwoord": "(6.000 × 2 × 9) / (100 × 12) = 108.000 / 1.200 = € 90 rente.", "uitleg": "Formule: (Kapitaal × Percentage × Maanden) / (100 × 12)."}
    ]
  },

  # Examen 8: 3.2 Lenen
  {
    "id": "ex-h3-economie-8",
    "hoofdstuk": 3,
    "paragraaf": "3.2",
    "titel": "Proeftoets 8: Lenen, kredietvormen en BKR",
    "vak": "Economie · HAVO 3",
    "icoon": "🏦",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Duru leent € 1.200 voor een laptop en betaalt 10 maanden lang € 135 per maand terug. Hoeveel bedragen de kredietkosten?", "opties": ["€ 135", "€ 150", "€ 1.350", "€ 1.200"], "antwoord": 1, "uitleg": "Totaal betaald = 10 × 135 = € 1.350. Kredietkosten = 1.350 - 1.200 = € 150."},
      {"type": "mc", "vraag": "Wat is een hypothecaire lening (hypotheek)?", "opties": ["Een kortlopende lening voor de aankoop van een smartphone.", "Een langlopende lening voor een woning waarbij het huis als onderpand dient.", "Een lening zonder rentevergoeding verstrekt door familie.", "Een doorlopend krediet met variabele limiet."], "antwoord": 1, "uitleg": "Een hypotheek is een lening voor onroerend goed met het pand als zekerheid."},
      {"type": "mc", "vraag": "Wat is het belangrijkste verschil tussen koop op afbetaling en huurkoop?", "opties": ["Bij huurkoop word je pas eigenaar na betaling van de allerlaatste termijn.", "Bij koop op afbetaling betaal je geen kredietkosten.", "Huurkoop geldt uitsluitend voor zakelijke vrachtwagens.", "Koop op afbetaling is wettelijk verboden in Nederland."], "antwoord": 0, "uitleg": "Bij huurkoop blijft de verkoper eigenaar totdat de laatste cent is betaald."},
      {"type": "mc", "vraag": "Wat is de functie van het Bureau Krediet Registratie (BKR) in Tiel?", "opties": ["Het direct verstrekken van leningen aan particulieren.", "Het registreren van afgesloten leningen om overkreditering te voorkomen.", "Het innen van gemeentelijke belastingen.", "Het vaststellen van de wisselkoers van de euro."], "antwoord": 1, "uitleg": "Het BKR registreert leningen om te voorkomen dat mensen problematische schulden maken."},
      {"type": "mc", "vraag": "Waaruit bestaat een maandelijkse termijnbetaling van een persoonlijke lening?", "opties": ["Alleen rente", "Aflossing (terugbetaling van de leensom) plus rente", "Alleen administratiekosten", "Uitsluitend vermogensbelasting"], "antwoord": 1, "uitleg": "Elke termijn lost een stukje schuld af en betaalt rentevergoeding."},
      {"type": "mc", "vraag": "Wat is een doorlopend krediet?", "opties": ["Een lening waarbij je binnen een afgesproken kredietlimiet flexibel geld kunt opnemen en aflossen.", "Een lening die je binnen 24 uur volledig moet terugbetalen.", "Een lening die automatisch wordt kwijtgescholden na één jaar.", "Een lening zonder rentekosten."], "antwoord": 0, "uitleg": "Bij een doorlopend krediet kun je afgeloste bedragen opnieuw opnemen."},
      {"type": "mc", "vraag": "Wat is een groot financieel risico van rood staan op je betaalrekening?", "opties": ["Je spaarrente stijgt automatisch.", "De rente op rood staan is extreem hoog (vaak 10% tot 14%).", "De bank blokkeert je paspoort.", "Je mag geen contant geld meer storten."], "antwoord": 1, "uitleg": "Rood staan is een van de duurste vormen van consumptief krediet."},
      {"type": "mc", "vraag": "Wat betekent aflossen op een schuld?", "opties": ["Het betalen van de wettelijke btw over een aankoop.", "Het daadwerkelijk terugbetalen van het geleende bedrag aan de schuldeiser.", "Het uitstellen van de betalingstermijn.", "Het opzeggen van je bankrekening."], "antwoord": 1, "uitleg": "Aflossen vermindert de openstaande schuld (de hoofdsom)."},
      {"type": "mc", "vraag": "Waarom waarschuwt de overheid met de slogan: 'Let op! Geld lenen kost geld'?", "opties": ["Omdat geld lenen strafbaar is gesteld in het wetboek.", "Omdat je bovenop het geleende bedrag altijd rente en kosten moet betalen.", "Omdat bankbiljetten na een lening ongeldig worden.", "Omdat leningen uitsluitend in vreemde valuta worden uitgekeerd."], "antwoord": 1, "uitleg": "Lenen kost geld vanwege de verschuldigde rente en kredietkosten."},
      {"type": "mc", "vraag": "Wat gebeurt er als een huiseigenaar zijn hypotheekrente en aflossing niet meer kan betalen?", "opties": ["De bank mag de woning executoriaal verkopen om de schuld te innen.", "De schuld wordt automatisch kwijtgescholden door het BKR.", "De overheid betaalt de woning volledig af.", "De huiseigenaar krijgt een gratis nieuw huis toegewezen."], "antwoord": 0, "uitleg": "Het huis dient als onderpand; bij wanbetaling mag de bank het pand verkopen."},
      {"type": "waaronwaar", "vraag": "Bij een persoonlijke lening betaal je een vast maandbedrag gedurende een vooraf vastgestelde looptijd.", "antwoord": True, "uitleg": "Persoonlijke leningen hebben vaste termijnen, vaste looptijd en vaste rente."},
      {"type": "waaronwaar", "vraag": "Bij huurkoop ben je vanaf de eerste dag juridisch eigenaar van het product.", "antwoord": False, "uitleg": "Bij huurkoop word je pas eigenaar na de allerlaatste betalingstermijn."},
      {"type": "waaronwaar", "vraag": "Het BKR registreert leningen vanaf € 250 die langer dan één maand lopen.", "antwoord": True, "uitleg": "Dit voorkomt dat consumenten ongemerkt te veel schulden stapelen."},
      {"type": "waaronwaar", "vraag": "Kredietkosten zijn gelijk aan het totale terugbetaalde bedrag verminderd met het oorspronkelijk geleende bedrag.", "antwoord": True, "uitleg": "Kredietkosten = Totaal betaald - Geleend bedrag."},
      {"type": "invul", "vraag": "De instantie die in Nederland kredieten registreert heet het [BKR|Bureau Krediet Registratie].", "antwoord": "BKR|Bureau Krediet Registratie", "uitleg": "BKR staat voor Bureau Krediet Registratie."},
      {"type": "invul", "vraag": "Een langlopende lening voor een woning met het huis als onderpand heet een [hypotheek|hypothecaire lening].", "antwoord": "hypotheek|hypothecaire lening", "uitleg": "Een hypotheek is een lening voor onroerend goed."},
      {"type": "invul", "vraag": "Het daadwerkelijk terugbetalen van de geleende hoofdsom heet [aflossen|aflossing].", "antwoord": "aflossen|aflossing", "uitleg": "Aflossen verlaagt de openstaande leenschuld."},
      {"type": "invul", "vraag": "De totale extra kosten (rente + administratie) van een lening noemen we de [kredietkosten].", "antwoord": "kredietkosten", "uitleg": "Kredietkosten zijn alle kosten bovenop de geleende som."},
      {"type": "open", "vraag": "Duru koopt een scooter van € 2.000. Ze betaalt 24 maanden lang € 95 per maand. Bereken de totale kredietkosten.", "sleutelwoorden": ["24 * 95 = 2280", "280"], "minTreffers": 1, "modelantwoord": "Totaal betaald = 24 × € 95 = € 2.280. Kredietkosten = € 2.280 - € 2.000 = € 280.", "uitleg": "Kredietkosten = Totale termijnen minus de aanschafwaarde."},
      {"type": "open", "vraag": "Leg uit waarom de bank bij een hypotheeklening een lager rentepercentage vraagt dan bij een persoonlijke lening.", "sleutelwoorden": ["onderpand/woning als zekerheid", "lager risico voor de bank"], "minTreffers": 1, "modelantwoord": "Omdat de bank het huis als onderpand heeft. Als de klant niet betaalt, kan de bank het huis verkopen. Het risico voor de bank is daardoor veel lager.", "uitleg": "Onderpand verlaagt het wanbetalingsrisico voor de kredietverstrekker."}
    ]
  },

  # Examen 9: 3.3 Verzekeren
  {
    "id": "ex-h3-economie-9",
    "hoofdstuk": 3,
    "paragraaf": "3.3",
    "titel": "Proeftoets 9: Verzekeringen, risico en solidariteit",
    "vak": "Economie · HAVO 3",
    "icoon": "🛡️",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Op welk principe berust het verzekeringswezen?", "opties": ["Op speculatie op de effectenbeurs", "Op solidariteit tussen veel verzekerden die samen de schadelast van enkelen dragen", "Op subsidies van de Europese Unie", "Op verplichte leningen bij de centrale bank"], "antwoord": 1, "uitleg": "Veel mensen betalen premie zodat de pechvogels schadeloos gesteld kunnen worden."},
      {"type": "mc", "vraag": "Wat is een inboedelverzekering?", "opties": ["Een verzekering voor schade aan het gemetselde woonhuis zelf.", "Een verzekering voor schade aan alle losse, verhuisbare spullen in je woning.", "Een verplichte verzekering voor bromfietsen.", "Een verzekering die medische ziekenhuiskosten vergoedt."], "antwoord": 1, "uitleg": "Inboedel omvat alle losse bezittingen in huis (meubels, tv, kleding)."},
      {"type": "mc", "vraag": "Welke schade dekt de Wettelijke Aansprakelijkheidsverzekering voor Motorrijtuigen (WA)?", "opties": ["Alleen de schade aan je eigen voertuig", "Schade die jij met je voertuig toebrengt aan anderen en andermans bezittingen", "Diefstal van je eigen autoradio", "Schade veroorzaakt door noodweer aan je eigen motorkap"], "antwoord": 1, "uitleg": "WA vergoedt de schade die jij toebrengt aan de tegenpartij."},
      {"type": "mc", "vraag": "Wat is het eigen risico bij een schadeverzekering?", "opties": ["De maximale uitkering die een verzekeraar ooit uitkeert.", "Het deel van het schadebedrag dat de verzekerde volgens de polisvoorwaarden zelf moet betalen.", "De rentevergoeding over de betaalde premie.", "De belasting op verzekeringscontracten."], "antwoord": 1, "uitleg": "Eigen risico is het vaste schadebedrag voor eigen rekening."},
      {"type": "mc", "vraag": "Wat verstaan economen onder 'moreel wangedrag' (moral hazard)?", "opties": ["Het niet betalen van de maandelijkse premie.", "Het verschijnsel dat mensen minder voorzichtig worden met hun spullen omdat ze toch verzekerd zijn.", "Fraude plegen bij de Belastingdienst.", "Het weigeren van een verplichte zorgverzekering."], "antwoord": 1, "uitleg": "Verzekerd zijn kan ertoe leiden dat men minder voorzorgsmaatregelen neemt."},
      {"type": "mc", "vraag": "Wat is een verzekeringspolis?", "opties": ["Het officiële contract en schriftelijke bewijs van de verzekeringsovereenkomst.", "De betaalpas waarmee je zorgkosten pint.", "De rekening van het schadeherstelbedrijf.", "Het registratienummer bij de Kamer van Koophandel."], "antwoord": 0, "uitleg": "De polis is het contractdocument met alle dekkingsvoorwaarden."},
      {"type": "mc", "vraag": "Wat dekt een opstalverzekering (woonhuisverzekering)?", "opties": ["Schade aan losse meubels en kleding in de woonkamer.", "Schade aan het gebouw zelf en alles wat daaraan nagelvast vastzit (muren, dak, leidingen).", "Schade die je hond toebrengt aan de buurman.", "Schade door verlies van je smartphone op straat."], "antwoord": 1, "uitleg": "Opstal betreft het onroerende huis zelf en nagelvaste installaties."},
      {"type": "mc", "vraag": "Waarom kiezen sommige mensen voor een vrijwillig hoger eigen risico bij hun zorgverzekering?", "opties": ["Omdat ze dan gratis medische behandelingen in het buitenland krijgen.", "Omdat een hoger eigen risico leidt tot een lagere maandelijkse premie.", "Omdat het wettelijk verplicht is vanaf 18 jaar.", "Om geen assurantiebelasting meer te betalen."], "antwoord": 1, "uitleg": "Een hoger eigen risico verlaagt de maandelijkse premiekosten."},
      {"type": "mc", "vraag": "Wat is de periodieke vergoeding die je betaalt voor een verzekering?", "opties": ["De franchise", "De premie", "Het dividend", "De provisie"], "antwoord": 1, "uitleg": "De premie is de prijs voor de verzekeringsdekking."},
      {"type": "mc", "vraag": "Duru fietst per ongeluk tegen de geparkeerde auto van de buren en veroorzaakt een kras. Welke verzekering dekt dit?", "opties": ["Haar inboedelverzekering", "Haar Aansprakelijkheidsverzekering voor Particulieren (AVP)", "De opstalverzekering van haar ouders", "Haar reisverzekering"], "antwoord": 1, "uitleg": "De AVP dekt schade die particulieren per ongeluk aan derden toebrengen."},
      {"type": "waaronwaar", "vraag": "Een WA-verzekering voor een bromfiets is in Nederland wettelijk verplicht.", "antwoord": True, "uitleg": "Ieder motorvoertuig moet minimaal WA-verzekerd zijn op de openbare weg."},
      {"type": "waaronwaar", "vraag": "Een inboedelverzekering dekt de schade als het dak van je huis wegwaait door een zware storm.", "antwoord": False, "uitleg": "Het dak hoort bij het huis zelf en valt onder de opstalverzekering."},
      {"type": "waaronwaar", "vraag": "Het solidariteitsbeginsel houdt in dat alle verzekerden gezamenlijk de schadelast dragen.", "antwoord": True, "uitleg": "Door risicospreiding betalen velen voor de pech van enkelen."},
      {"type": "waaronwaar", "vraag": "Moreel wangedrag betekent dat verzekeraars weigeren schade uit te keren aan polishouders.", "antwoord": False, "uitleg": "Moral hazard slaat op onvoorzichtig gedrag van de verzekerde zélf."},
      {"type": "invul", "vraag": "Het officiële schriftelijke contract van een verzekering heet de [polis|verzekeringspolis].", "antwoord": "polis|verzekeringspolis", "uitleg": "De polis is het contractuele document."},
      {"type": "invul", "vraag": "Het vaste bedrag dat je bij schade eerst zelf moet betalen heet het [eigen risico].", "antwoord": "eigen risico", "uitleg": "Het eigen risico blijft voor eigen rekening."},
      {"type": "invul", "vraag": "Het periodieke bedrag dat je betaalt aan de verzekeringsmaatschappij heet de [premie].", "antwoord": "premie", "uitleg": "Premie is de periodieke vergoeding voor dekking."},
      {"type": "invul", "vraag": "De verzekering die schade dekt aan losse spullen in huis heet de [inboedelverzekering].", "antwoord": "inboedelverzekering", "uitleg": "Inboedelverzekering dekt roerende goederen in huis."},
      {"type": "open", "vraag": "Leg het verschil uit tussen een inboedelverzekering en een opstalverzekering.", "sleutelwoorden": ["inboedel: losse spullen/meubels", "opstal: huis zelf/nagelvast/muren"], "minTreffers": 2, "modelantwoord": "Een inboedelverzekering dekt schade aan losse verhuisbare spullen in huis (meubels, tv); een opstalverzekering dekt schade aan het huis zelf en alles wat nagelvast aan de woning zit (dak, muren, leidingen).", "uitleg": "Inboedel = roerend; opstal = onroerend goed."},
      {"type": "open", "vraag": "Waarom hanteren verzekeraars een eigen risico bij schadeverzekeringen? Noem twee redenen.", "sleutelwoorden": ["premie verlagen/laag houden", "minder kleine claims/voorzichtiger zijn"], "minTreffers": 1, "modelantwoord": "1. Het verlaagt de maandelijkse premie voor de klant, 2. Het voorkomt dat mensen voor elk klein wissewasje declareren en stimuleert voorzichtiger gedrag.", "uitleg": "Eigen risico vermindert administratielast en moreel wangedrag."}
    ]
  },

  # Examen 10: 4.1 Productie & Toegevoegde Waarde
  {
    "id": "ex-h3-economie-10",
    "hoofdstuk": 4,
    "paragraaf": "4.1",
    "titel": "Proeftoets 10: Productiefactoren, toegevoegde waarde en BBP",
    "vak": "Economie · HAVO 3",
    "icoon": "🏭",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Welke vier productiefactoren onderscheiden we in de economie (KANO)?", "opties": ["Krediet, Afzet, Netto en Omzet", "Kapitaal, Arbeid, Natuur en Ondernemerschap", "Koopkracht, Aflossing, Nominaal en Overheid", "Kosten, Accijns, Nationaal en Opbrengst"], "antwoord": 1, "uitleg": "KANO staat voor Kapitaal, Arbeid, Natuur en Ondernemerschap."},
      {"type": "mc", "vraag": "Welke beloning hoort bij de productiefactor Ondernemerschap?", "opties": ["Loon", "Pacht", "Winst", "Rente"], "antwoord": 2, "uitleg": "De ondernemer draagt ondernemersrisico en wordt beloond met de winst."},
      {"type": "mc", "vraag": "Een meubelmaker koopt hout en schroeven voor € 80 en verkoopt de tafel voor € 300. Wat is de toegevoegde waarde?", "opties": ["€ 80", "€ 220", "€ 300", "€ 380"], "antwoord": 1, "uitleg": "Toegevoegde waarde = Verkoopprijs (€ 300) - Inkoopwaarde grondstoffen (€ 80) = € 220."},
      {"type": "mc", "vraag": "Welke beloning ontvangt een grondeigenaar voor het verhuren van landbouwgrond aan een boer?", "opties": ["Salaris", "Pacht", "Dividend", "Courtage"], "antwoord": 1, "uitleg": "De vergoeding voor de productiefactor Natuur (grond) heet pacht."},
      {"type": "mc", "vraag": "Welke term beschrijft de opeenvolging van productiefasen van grondstof tot consumentenwinkel?", "opties": ["De keten van bedrijven die een product doorloopt van grondstof tot consument.", "Het financiële jaarverslag van een beursgenoteerde onderneming.", "De lijst van alle werknemers op de loonlijst van een fabriek.", "Het overzicht van alle winkels in een winkelcentrum."], "antwoord": 0, "uitleg": "De bedrijfskolom beschrijft het hele productietraject van oerproducent tot detaillist."},
      {"type": "mc", "vraag": "Wat vormt de som van alle toegevoegde waarden in een land gedurende één jaar?", "opties": ["De totale staatsschuld", "Het Bruto Binnenlands Product (BBP)", "De totale consumptie van gezinnen", "De handelsbalans"], "antwoord": 1, "uitleg": "Het BBP is de totale waardecreatie (productie) van een land in één jaar."},
      {"type": "mc", "vraag": "Welke van de onderstaande goederen behoort tot de productiefactor Kapitaal?", "opties": ["Landbouwgrond langs een rivier", "Een geautomatiseerde verpakkingsmachine", "De lichamelijke arbeid van een bouwvakker", "Het lef van een starter om een bedrijf te beginnen"], "antwoord": 1, "uitleg": "Machines, fabrieken en gereedschappen zijn kapitaalgoederen."},
      {"type": "mc", "vraag": "Waarom staat de consument NIET in de bedrijfskolom?", "opties": ["Omdat de consument geen btw betaalt.", "Omdat de consument niets meer toevoegt aan het product maar het verbruikt.", "Omdat de consument alleen chartaal mag betalen.", "Omdat de bedrijfskolom uitsluitend uit groothandels bestaat."], "antwoord": 1, "uitleg": "De bedrijfskolom eindigt bij de winkelier; de consument voegt geen waarde meer toe."},
      {"type": "mc", "vraag": "Wat is de beloning voor de productiefactor Arbeid?", "opties": ["Winst", "Loon (salaris)", "Pacht", "Rente"], "antwoord": 1, "uitleg": "Loon is de vergoeding voor geleverde arbeid."},
      {"type": "mc", "vraag": "Wat gebeurt er als een schakel uit de bedrijfskolom wordt overgeslagen (bijv. boer verkoopt direct aan consument)?", "opties": ["De bedrijfskolom wordt korter (integratie/rechtstreekse verkoop).", "Het product wordt automatisch twee keer zo duur.", "Er ontstaat een begrotingstekort bij de overheid.", "Het BBP daalt naar nul."], "antwoord": 0, "uitleg": "Schakels overslaan heet verkorting van de bedrijfskolom (of integratie/directe verkoop)."},
      {"type": "waaronwaar", "vraag": "Toegevoegde waarde is gelijk aan de verkoopprijs minus de inkoopwaarde van grond- en hulpstoffen.", "antwoord": True, "uitleg": "Toegevoegde waarde meet de waarde die door productie is gecreëerd."},
      {"type": "waaronwaar", "vraag": "Grondstoffen en aardgas in de bodem vallen onder de productiefactor Kapitaal.", "antwoord": False, "uitleg": "Natuurlijke hulpbronnen vallen onder de productiefactor Natuur."},
      {"type": "waaronwaar", "vraag": "De beloning voor de productiefactor Kapitaal is rente of huur.", "antwoord": True, "uitleg": "Kapitaal levert als vergoeding rente of huur op."},
      {"type": "waaronwaar", "vraag": "Het BBP meet de totale economische productie en welvaart van een land.", "antwoord": True, "uitleg": "Het BBP is de som van alle toegevoegde waarden in een land."},
      {"type": "invul", "vraag": "De vier productiefactoren korten we af met het woord [KANO].", "antwoord": "KANO", "uitleg": "KANO = Kapitaal, Arbeid, Natuur, Ondernemerschap."},
      {"type": "invul", "vraag": "De extra waarde die een bedrijf toevoegt door bewerking heet de [toegevoegde waarde].", "antwoord": "toegevoegde waarde", "uitleg": "Toegevoegde waarde = Verkoopprijs - Inkoopwaarde."},
      {"type": "invul", "vraag": "De beloning voor de productiefactor Natuur noemen we [pacht].", "antwoord": "pacht", "uitleg": "Pacht is de huurvergoeding voor grond en natuur."},
      {"type": "invul", "vraag": "De keten van bedrijven van oerproducent tot winkelier heet de [bedrijfskolom].", "antwoord": "bedrijfskolom", "uitleg": "De bedrijfskolom toont de opeenvolgende productieschakels."},
      {"type": "open", "vraag": "Noem de vier productiefactoren (KANO) en geef bij elke factor de bijbehorende beloning.", "sleutelwoorden": ["kapitaal - rente/huur", "arbeid - loon", "natuur - pacht", "ondernemerschap - winst"], "minTreffers": 3, "modelantwoord": "1. Kapitaal (rente/huur), 2. Arbeid (loon/salaris), 3. Natuur (pacht), 4. Ondernemerschap (winst).", "uitleg": "Dit zijn de vier productiefactoren en hun beloningen."},
      {"type": "open", "vraag": "Een bakker koopt bloem, gist en water in voor € 0,40 per brood. De energiekosten zijn € 0,10 per brood. Hij verkoopt het brood voor € 2,50. Bereken de toegevoegde waarde per brood.", "sleutelwoorden": ["2,50 - 0,50", "2,00/2 euro"], "minTreffers": 1, "modelantwoord": "Inkoopkosten = 0,40 + 0,10 = € 0,50. Toegevoegde waarde = € 2,50 - € 0,50 = € 2,00 per brood.", "uitleg": "Toegevoegde waarde = Verkoopprijs minus ingekochte grond- en hulpstoffen."}
    ]
  },

  # Examen 11: 4.2 Kosten van een onderneming
  {
    "id": "ex-h3-economie-11",
    "hoofdstuk": 4,
    "paragraaf": "4.2",
    "titel": "Proeftoets 11: Constante kosten, variabele kosten en schaalvoordelen",
    "vak": "Economie · HAVO 3",
    "icoon": "📉",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Wat zijn constante (vaste) kosten van een onderneming?", "opties": ["Kosten die stijgen zodra er één extra product gemaakt wordt.", "Kosten die op korte termijn niet veranderen als de productie toeneemt of afneemt.", "Kosten die uitsluitend bestaan uit grondstoffen.", "Kosten die de klant contant afrekent."], "antwoord": 1, "uitleg": "Constante kosten (zoals huur van het pand) blijven gelijk bij verandering van de productieomvang."},
      {"type": "mc", "vraag": "Een fietsenfabriek heeft € 10.000 constante kosten per maand. De variabele kosten zijn € 50 per fiets. Wat zijn de totale kosten bij 200 fietsen?", "opties": ["€ 10.000", "€ 20.000", "€ 25.000", "€ 30.000"], "antwoord": 1, "uitleg": "TK = TCK (€ 10.000) + TVK (200 × € 50 = € 10.000) = € 20.000."},
      {"type": "mc", "vraag": "Welke van de volgende kostenposten is een variabele kostenpost?", "opties": ["De huur van het kantoorpand", "De afschrijving op een grote drukpers", "Het verpakkingskarton voor verzonden bestellingen", "Het vaste salaris van de directeur"], "antwoord": 2, "uitleg": "Verpakkingsmateriaal groeit rechtstreeks mee met het aantal verzonden pakketjes."},
      {"type": "mc", "vraag": "Wat verstaan economen onder schaalvoordelen (economies of scale)?", "opties": ["De kostprijs per product daalt omdat de vaste kosten over meer stuks verdeeld worden.", "De belastingdienst geeft subsidie aan kleine bedrijven.", "De lonen van werknemers worden gehalveerd.", "De winst stijgt automatisch naar 100%."], "antwoord": 0, "uitleg": "Massaproductie spreidt de vaste kosten over grote aantallen, waardoor de eenheidsprijs daalt."},
      {"type": "mc", "vraag": "Hoe bereken je de kostprijs per product (gemiddelde totale kosten)?", "opties": ["Totale kosten vermenigvuldigd met de afzet", "Totale kosten gedeeld door het aantal geproduceerde producten (TK / q)", "Totale opbrengst minus de inkoopwaarde", "Totale variabele kosten plus de btw"], "antwoord": 1, "uitleg": "Kostprijs per stuk = Totale kosten / Productieaantal (TK / q)."},
      {"type": "mc", "vraag": "Een meubelmaker produceert 100 kasten. De totale kosten zijn € 15.000. Wat is de kostprijs per kast?", "opties": ["€ 100", "€ 150", "€ 200", "€ 250"], "antwoord": 1, "uitleg": "Kostprijs = € 15.000 / 100 = € 150 per kast."},
      {"type": "mc", "vraag": "Wat gebeurt er met de totale variabele kosten (TVK) als een fabriek besluit de productie stil te leggen (q = 0)?", "opties": ["De variabele kosten worden nul euro (€ 0).", "De variabele kosten verdubbelen.", "De variabele kosten blijven gelijk aan de huur.", "De variabele kosten worden negatief."], "antwoord": 0, "uitleg": "Bij nul productie verbruik je geen grondstoffen of verpakkingen, dus TVK = 0."},
      {"type": "mc", "vraag": "Wat gebeurt er met de totale constante kosten (TCK) als de productie nul is (q = 0)?", "opties": ["De constante kosten worden nul.", "De constante kosten moeten gewoon volledig doorbetaald worden (zoals de huur).", "De constante kosten worden omgezet in winst.", "De constante kosten worden door de bank vergoed."], "antwoord": 1, "uitleg": "Vaste lasten zoals huur lopen door, ongeacht of er geproduceerd wordt."},
      {"type": "mc", "vraag": "Wat is de formule voor Totale Kosten (TK)?", "opties": ["TK = TCK - TVK", "TK = TCK + TVK", "TK = TO - Winst", "TK = Prijs × Afzet"], "antwoord": 1, "uitleg": "Totale kosten = Totale Constante Kosten + Totale Variabele Kosten."},
      {"type": "mc", "vraag": "Waarom investeren grote bedrijven vaak in verregaande automatisering en robots?", "opties": ["Om de variabele arbeidskosten per product te verlagen en schaalvoordelen te behalen.", "Omdat robots geen elektriciteit verbruiken.", "Om meer inkomstenbelasting te kunnen afdragen.", "Omdat de overheid handmatig werk verbiedt."], "antwoord": 0, "uitleg": "Robots verhogen de productiviteit en verlagen de loonkosten per eenheid product."},
      {"type": "waaronwaar", "vraag": "Grondstoffen en verpakkingen zijn voorbeelden van constante kosten.", "antwoord": False, "uitleg": "Grondstoffen variëren met de productie en zijn dus variabele kosten."},
      {"type": "waaronwaar", "vraag": "Als de productie stijgt, daalt de constante kosten per stuk.", "antwoord": True, "uitleg": "De vaste kosten worden verdeeld over meer eenheden (schaalvoordeel)."},
      {"type": "waaronwaar", "vraag": "De huur van het bedrijfspand verandert automatisch elke maand afhankelijk van hoeveel producten er verkocht worden.", "antwoord": False, "uitleg": "Huur is een constante kostenpost en blijft gelijk."},
      {"type": "waaronwaar", "vraag": "De kostprijs per product is gelijk aan de totale kosten gedeeld door de productieomvang.", "antwoord": True, "uitleg": "Kostprijs = TK / q."},
      {"type": "invul", "vraag": "Kosten die niet veranderen bij een verandering van de productieomvang heten [constante kosten|vaste kosten].", "antwoord": "constante kosten|vaste kosten", "uitleg": "Constante kosten blijven vast op korte termijn."},
      {"type": "invul", "vraag": "Kosten die rechtstreeks meegroeien met het productievolume noemen we [variabele kosten].", "antwoord": "variabele kosten", "uitleg": "Variabele kosten hangen af van de productieomvang."},
      {"type": "invul", "vraag": "Het voordeel dat ontstaat doordat vaste kosten over grote aantallen worden verdeeld heet [schaalvoordeel|schaalvoordelen].", "antwoord": "schaalvoordeel|schaalvoordelen", "uitleg": "Schaalvoordelen verlagen de kostprijs per eenheid."},
      {"type": "invul", "vraag": "De formule voor totale kosten is TCK plus [TVK|totale variabele kosten].", "antwoord": "TVK|totale variabele kosten", "uitleg": "TK = TCK + TVK."},
      {"type": "open", "vraag": "Een pizzabakker heeft € 2.000 constante kosten per maand. De variabele kosten zijn € 2 per pizza. Bereken de totale kosten bij het bakken van 1.500 pizza's.", "sleutelwoorden": ["1500 * 2 = 3000", "5000/5.000 euro"], "minTreffers": 1, "modelantwoord": "TVK = 1.500 × € 2 = € 3.000. TK = TCK (€ 2.000) + TVK (€ 3.000) = € 5.000.", "uitleg": "Totale kosten = TCK + TVK."},
      {"type": "open", "vraag": "Leg uit waarom de kostprijs per product daalt als een fabriek haar productie verdubbelt van 1.000 naar 2.000 stuks.", "sleutelwoorden": ["constante/vaste kosten verdeeld", "over meer stuks/producten"], "minTreffers": 1, "modelantwoord": "Omdat de constante kosten (zoals huur en machines) nu verdeeld worden over 2.000 stuks in plaats van 1.000 stuks. Hierdoor daalt het aandeel vaste kosten per product (schaalvoordeel).", "uitleg": "Schaalvoordelen verlagen de gemiddelde vaste kosten per product."}
    ]
  },

  # Examen 12: 4.3 Omzet, Winst en Btw
  {
    "id": "ex-h3-economie-12",
    "hoofdstuk": 4,
    "paragraaf": "4.3",
    "titel": "Proeftoets 12: Omzet, nettowinst, break-even en btw",
    "vak": "Economie · HAVO 3",
    "icoon": "💶",
    "duurMin": 20,
    "vragen": [
      {"type": "mc", "vraag": "Een winkel verkoopt 400 jassen voor € 120 per stuk (excl. btw). Wat is de omzet (Totale Opbrengst)?", "opties": ["€ 4.800", "€ 48.000", "€ 58.080", "€ 60.000"], "antwoord": 1, "uitleg": "Omzet = Verkoopprijs × Afzet = 120 × 400 = € 48.000."},
      {"type": "mc", "vraag": "Wat betekent het break-evenpunt (BEP) voor een onderneming?", "opties": ["De productieomvang waarbij de winst maximaal is.", "Het punt waarop de totale opbrengst precies gelijk is aan de totale kosten (winst = € 0).", "Het moment waarop de winkel failliet wordt verklaard.", "De maximale kredietlimiet bij de bank."], "antwoord": 1, "uitleg": "Bij break-even speelt een bedrijf precies quitte: TO = TK en winst = 0."},
      {"type": "mc", "vraag": "Hoe bereken je de brutowinst van een handelsonderneming?", "opties": ["Omzet minus inkoopwaarde van de verkochte goederen", "Omzet plus btw", "Nettowinst minus bedrijfskosten", "Totale kosten gedeeld door de afzet"], "antwoord": 0, "uitleg": "Brutowinst = Omzet - Inkoopwaarde van de omzet."},
      {"type": "mc", "vraag": "Een smartphone kost in de winkel € 200 exclusief 21% btw. Wat is de consumentenprijs inclusief btw?", "opties": ["€ 221", "€ 242", "€ 250", "€ 260"], "antwoord": 1, "uitleg": "Consumentenprijs = € 200 × 1,21 = € 242."},
      {"type": "mc", "vraag": "Welk btw-tarief geldt in Nederland voor basisvoedsel, boeken en het openbaar vervoer?", "opties": ["0%", "9% (laag tarief)", "21% (hoog tarief)", "25%"], "antwoord": 1, "uitleg": "Primaire levensbehoeften vallen onder het verlaagde btw-tarief van 9%."},
      {"type": "mc", "vraag": "Wat is het verschil tussen afzet en omzet?", "opties": ["Afzet is het aantal verkochte stuks; omzet is de totale geldopbrengst van de verkoop.", "Afzet is inclusief btw; omzet is exclusief btw.", "Afzet geldt voor groothandels; omzet alleen voor consumenten.", "Er is geen verschil."], "antwoord": 0, "uitleg": "Afzet = aantal stuks (hoeveelheid); Omzet = aantal stuks × prijs (geldbedrag)."},
      {"type": "mc", "vraag": "Hoe bereken je de nettowinst van een onderneming?", "opties": ["Brutowinst verminderd met de bedrijfskosten (overige kosten)", "Omzet plus inkoopwaarde", "Totale kosten minus de btw", "Afzet vermenigvuldigd met de inkoopprijs"], "antwoord": 0, "uitleg": "Nettowinst = Brutowinst - Bedrijfskosten (personeel, huur, energie)."},
      {"type": "mc", "vraag": "Een consument koopt een fiets voor € 605 inclusief 21% btw. Wat is de verkoopprijs exclusief btw?", "opties": ["€ 484", "€ 500", "€ 550", "€ 600"], "antwoord": 1, "uitleg": "Prijs excl. btw = 605 / 1,21 = € 500."},
      {"type": "mc", "vraag": "Wat moet een winkelier doen met de btw die hij van consumenten ontvangt?", "opties": ["Hij mag de btw als extra nettowinst houden.", "Hij moet de ontvangen btw periodiek afdragen aan de Belastingdienst.", "Hij moet de btw terugstorten op de rekening van de klant.", "Hij moet de btw omzetten in goudstaven."], "antwoord": 1, "uitleg": "Btw is een indirecte belasting die winkels innen voor de Belastingdienst."},
      {"type": "mc", "vraag": "Wanneer maakt een onderneming verlies?", "opties": ["Als de totale kosten (TK) hoger zijn dan de totale opbrengst (TO).", "Als het break-evenpunt wordt overschreden.", "Als de afzet groter is dan de voorraad.", "Als de btw wordt verlaagd van 21% naar 9%."], "antwoord": 0, "uitleg": "Verlies ontstaat als TK > TO."},
      {"type": "waaronwaar", "vraag": "De omzet van een bedrijf is altijd gelijk aan de uiteindelijke nettowinst.", "antwoord": False, "uitleg": "Van de omzet moeten alle inkoop- en bedrijfskosten nog worden afgetrokken."},
      {"type": "waaronwaar", "vraag": "Op het break-evenpunt (BEP) is de winst van een bedrijf exact gelijk aan € 0.", "antwoord": True, "uitleg": "Break-even betekent quitte spelen: TO = TK."},
      {"type": "waaronwaar", "vraag": "Primaire levensmiddelen zoals groente en brood vallen onder het lage btw-tarief van 9%.", "antwoord": True, "uitleg": "Noodzakelijke levensbehoeften worden belast met het lage 9% tarief."},
      {"type": "waaronwaar", "vraag": "De afzet van een onderneming wordt altijd uitgedrukt in euro's.", "antwoord": False, "uitleg": "Afzet wordt uitgedrukt in fysieke eenheden (stuks, kilo's, liters)."},
      {"type": "invul", "vraag": "Het aantal verkochte stuks producten heet de [afzet].", "antwoord": "afzet", "uitleg": "Afzet meet de fysieke verkoophoeveelheid."},
      {"type": "invul", "vraag": "De totale geldopbrengst van de verkopen (prijs × afzet) heet de [omzet|totale opbrengst].", "antwoord": "omzet|totale opbrengst", "uitleg": "Omzet = Prijs × Afzet."},
      {"type": "invul", "vraag": "Het punt waarop de totale opbrengst precies gelijk is aan de totale kosten heet het [break-evenpunt|BEP].", "antwoord": "break-evenpunt|BEP", "uitleg": "Op het break-evenpunt is de winst nul."},
      {"type": "invul", "vraag": "De afkorting btw staat voor belasting over de [toegevoegde waarde].", "antwoord": "toegevoegde waarde", "uitleg": "Btw = Belasting over de Toegevoegde Waarde."},
      {"type": "open", "vraag": "Een winkelier behaalt een omzet van € 80.000. De inkoopwaarde van de verkochte goederen is € 45.000. De overige bedrijfskosten zijn € 20.000. Bereken de brutowinst en de nettowinst.", "sleutelwoorden": ["brutowinst: 35.000", "nettowinst: 15.000"], "minTreffers": 2, "modelantwoord": "Brutowinst = € 80.000 - € 45.000 = € 35.000. Nettowinst = € 35.000 - € 20.000 = € 15.000.", "uitleg": "Brutowinst = Omzet - Inkoopwaarde; Nettowinst = Brutowinst - Bedrijfskosten."},
      {"type": "open", "vraag": "Een tablet kost in de winkel € 363 inclusief 21% btw. Bereken het btw-bedrag in euro's. Toon de berekening.", "sleutelwoorden": ["363 / 1,21 = 300", "63/63 euro"], "minTreffers": 1, "modelantwoord": "Prijs excl. btw = € 363 / 1,21 = € 300. Btw-bedrag = € 363 - € 300 = € 63.", "uitleg": "Btw-bedrag = Prijs incl. btw verminderd met de prijs excl. btw."}
    ]
  }
]

# Write out all 12 exams
print("Generating all 12 Economie exams...")
for idx, ex in enumerate(EXAMS, 1):
    mc_c = 0
    for v in ex['vragen']:
        if v.get('type') == 'mc':
            target = mc_c % len(v['opties'])
            mc_c += 1
            curr = v['antwoord']
            if curr != target:
                v['opties'][curr], v['opties'][target] = v['opties'][target], v['opties'][curr]
                v['antwoord'] = target
    fname = f"{ECONOMIE_DIR}/examen_{idx}.js"
    content = f"/* =========================================================\n   Duru's Economie (HAVO 3) — {ex['titel']}\n   ========================================================= */\nDURU.registerExamen({json.dumps(ex, ensure_ascii=False, indent=2)});\n"
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Written {fname}")

print("\nSuccessfully built all 12 exams!")
