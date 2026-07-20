// De data voor de Begrijpend Lezen quiz op niveau 2 mavo (Gegroepeerd in 10 examens)
const quizData = [
  {
    examId: 1,
    examTitle: "Sınav 1: Digitale Wereld",
    texts: [
      {
        title: "Tekst 1: De illusie van deepfakes",
        goal: "Informeren",
        text: `Stel je voor dat je een video ziet waarin de president beweert dat schoolvakanties worden afgeschaft. Grote kans dat dit een 'deepfake' is. Dit zijn video's en afbeeldingen waarin gezichten en stemmen met hulp van kunstmatige intelligentie (AI) heel echt worden nagemaakt. <strong>Ten eerste</strong> hebben deepfakes grote voordelen voor de filmindustrie, omdat regisseurs hiermee acteurs digitaal jonger kunnen maken. <strong>Echter</strong>, kwaadwillenden gebruiken het ook om nepnews te verspreiden en mensen te misleiden, <strong>omdat</strong> de technologie tegenwoordig voor iedereen gratis beschikbaar is. Pas in 2017 doken de eerste echte deepfakes online op. Het is dus belangrijk om kritisch te blijven kijken naar wat je online ziet.`,
        questions: [
          {
            id: 1,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de regel uit het spiekbriefje!)",
            options: [
              { key: "A", text: "Hoe computerexperts in 2017 begonnen met het manipuleren van presidenten in filmpjes." },
              { key: "B", text: "De opkomst van deepfakes." },
              { key: "C", text: "Waarom nepnieuws zo ontzettend gevaarlijk is voor onze samenleving." },
              { key: "D", text: "De voordelen van AI in de bioscoop." }
            ],
            correct: "B",
            explanation: "Kijk eens naar het <strong>Spiekbriefje</strong> bij het begrip <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('De opkomst van deepfakes') bestaat uit 4 woorden en vat de hele tekst perfect samen! Optie A is veel te lang (meer dan 4 woorden) en optie D is slechts een klein detail uit het middenstuk en niet waar de héle tekst over gaat."
          },
          {
            id: 2,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft objectieve uitleg en feiten over wat deepfakes zijn." },
              { key: "B", text: "Overtuigen, want de schrijver wil dat je dezelfde politieke mening krijgt." },
              { key: "C", text: "Activeren, want de schrijver spoort je aan om direct een deepfake-app te downloaden." },
              { key: "D", text: "Amuseren, want het is een spannend, fictief sprookje over robots." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Informeren</em>: 'uitleg / feiten'. De schrijver deelt feiten over hoe deepfakes worden gemaakt, de geschiedenis (2017) en hoe ze worden gebruikt. Er wordt geen zware mening opgedrongen of actie geëist, dus is het doel informeren."
          },
          {
            id: 3,
            question: "In welke van de onderstaande zinnen is er sprake van een juiste citering van de voordelen voor de filmwereld?",
            options: [
              { key: "A", text: "De regisseur kan acteurs hiermee digitaal een stuk jonger maken." },
              { key: "B", text: "De schrijver vertelt dat deepfakes handig zijn voor films." },
              { key: "C", text: "“Ten eerste hebben deepfakes grote voordelen voor de filmindustrie”" },
              { key: "D", text: "“Het is dus belangrijk om kritisch te blijven kijken naar wat je online ziet.”" }
            ],
            correct: "C",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie C is letterlijk gekopieerd uit de tekst en staat netjes tussen de juiste aanhalingstekens. Optie A en B hebben geen aanhalingstekens, en optie D citeert wel, maar dat gaat over kritisch kijken, niet over de filmindustrie!"
          },
          {
            id: 4,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit signaalwoord aan?",
            options: [
              { key: "A", text: "Opsomming, want de schrijver voegt een extra voordeel toe." },
              { key: "B", text: "Reden/oorzaak, want het legt uit hoe de video's worden verspreid." },
              { key: "C", text: "Tegenstelling, omdat het een contrast aangeeft tussen de voordelen en de nadelen." },
              { key: "D", text: "Gevolg, want het is het resultaat van de AI-ontwikkelingen." }
            ],
            correct: "C",
            explanation: "Als je op het <strong>Spiekbriefje</strong> kijkt bij <em>Tekstverbanden + signaalwoorden</em>, zie je 'echter' staan onder het kopje <strong>Tegenstelling</strong> (samen met maar, toch, hoewel). De schrijver noemt eerst een positieve kant van deepfakes (filmindustrie), en stelt daar een negatieve kant tegenover ('Echter, kwaadwillenden gebruiken het ook...')."
          }
        ]
      },
      {
        title: "Tekst 2: Iedereen moet leren coderen!",
        goal: "Overtuigen",
        text: `Het is eigenlijk belachelijk dat programmeren nog steeds geen verplicht vak is op alle middelbare scholen. We leven in een wereld die volledig draait op software en technologie. <strong>Ten eerste</strong> stimuleert leren coderen je logisch denkvermogen, wat je helpt bij andere vakken zoals wiskunde en economie. <strong>Bovendien</strong> zorgt het voor uitstekende baankansen in de toekomst, omdat de vraag naar tech-specialisten gigantisch groot is. <strong>Hoewel</strong> sommige critici beweren dat programmeren te saai of te ingewikkeld is voor jongeren, bewijzen moderne apps dat het juist heel creatief en toegankelijk kan zijn. Scholen moeten daarom nu hun lesroosters aanpassen om leerlingen klaar te stomen voor de digitale toekomst!`,
        questions: [
          {
            id: 5,
            question: "Wat is de hoofdgedachte van deze tekst? (Truc: Wat wil de schrijver dat ik onthoud?)",
            options: [
              { key: "A", text: "Programmeren is heel erg goed voor je logisch denkvermogen en helpt bij wiskunde." },
              { key: "B", text: "Sommige critici vinden dat programmeren te saai of te moeilijk is voor scholieren." },
              { key: "C", text: "Middelbare scholen moeten programmeren verplicht stellen om leerlingen voor te bereiden op de toekomst." },
              { key: "D", text: "Er is momenteel een enorm tekort aan goede tech-specialisten op de arbeidsmarkt." }
            ],
            correct: "C",
            explanation: "De <em>Hoofdgedachte</em> is volgens ons <strong>Spiekbriefje</strong> de belangrijkste boodschap van de héle tekst. De truc is: 'Wat wil de schrijver dat ik onthoud?'. De schrijver wil niet alleen vertellen dat coderen goed is voor je logica (A) of dat critici het moeilijk vinden (B), maar hij betoogt dat scholen het NU verplicht moeten maken (C). Dat is de kernboodschap!"
          },
          {
            id: 6,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen neutrale, historische feiten over computers." },
              { key: "B", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link in om direct een programmeer-app te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een kapotte robot." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt het ontbreken van programmeerles 'belachelijk' (mening) en geeft argumenten waarom het wel moet ('logisch denken', 'baankansen'). Hij wil dat jij het met hem eens bent."
          },
          {
            id: 7,
            question: "In de tekst staat het signaalwoord 'Hoewel'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan tussen de mening van critici en de werkelijkheid." },
              { key: "B", text: "Opsomming, want het voegt een extra voordeel toe aan het leren coderen." },
              { key: "C", text: "Vergelijking, want het vergelijkt coderen met wiskunde." },
              { key: "D", text: "Tijd, want het geeft aan wanneer scholieren moeten beginnen." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'hoewel' onder het kopje <strong>Tegenstelling</strong> staan. De schrijver stelt de bezwaren van critici (saai/ingewikkeld) tegenover de werkelijkheid (creatief/toegankelijk)."
          },
          {
            id: 8,
            question: "Wat is de kernzin van het eerste deel van de tekst (de eerste twee zinnen)?",
            options: [
              { key: "A", text: "Het is eigenlijk belachelijk dat programmeren nog steeds geen verplicht vak is op alle middelbare scholen." },
              { key: "B", text: "We leven in een wereld die volledig draait op software en technologie." },
              { key: "C", text: "Scholen moeten daarom nu hun lesroosters aanpassen." },
              { key: "D", text: "Er is geen kernzin te vinden in dit gedeelte." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Kernzin</em>: 'Belangrijkste zin van 1 alinea, Vaak 1e of laatste zin'. De allereerste zin stelt direct het standpunt en onderwerp van de alinea vast, namelijk dat programmeren verplicht moet zijn. De zinnen daarna onderbouwen dit."
          }
        ]
      },
      {
        title: "Tekst 3: Start vandaag met je scherm-dieet!",
        goal: "Activeren",
        text: `Lig jij ook urenlang lusteloos op de bank door je telefoon te scrollen vlak voor je examens? Heel begrijpelijk, maar het is funest voor je concentratie en je cijfers. <strong>Hoewel</strong> even ontspannen op je telefoon heel verleidelijk is, raken je hersenen er juist overprikkeld door. In dit artikel leggen we uit hoe je met een simpel scherm-dieet weer controle krijgt over je eigen tijd en betere resultaten boekt.<br><br>
        Ten eerste zorgt de constante stroom aan meldingen ervoor dat je focus steeds onderbroken wordt. Je hersenen hebben na elke afleiding wel tien minuten nodig om weer diep in de leerstof te komen. <strong>Bovendien</strong> zorgt het blauwe licht van je scherm voor een slechtere nachtrust, waardoor je de volgende ochtend moe aan je toetsen begins.<br><br>
        Start daarom vandaag nog! Download een app die je social media tijdelijk blokkeert en leg je telefoon in een andere kamer als je gaat studeren. Spreek met jezelf af dat je pas na een uur leren vijf minuten op je scherm mag kijken. Als je dit nu uitprobeert, zul je merken dat je veel sneller klaar bent met leren en fris aan je proefwerken begint. Kom op, leg die telefoon nu meteen weg en begin eraan!`,
        questions: [
          {
            id: 9,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom social media apps heel erg slecht zijn voor de hersenen van studenten." },
              { key: "B", text: "Minder schermtijd voor examens." },
              { key: "C", text: "Het downloaden van blokkeer-apps op je smartphone." },
              { key: "D", text: "Blauw licht en nachtrust." }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <em>Onderwerp</em> op je <strong>Spiekbriefje</strong>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('Minder schermtijd voor examens') bestaat uit 4 woorden en dekt de lading van the hele tekst! Optie A is veel te lang, en optie C en D zijn slechts details uit het middenstuk."
          },
          {
            id: 10,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen neutrale feiten over het brein." },
              { key: "B", text: "Amuseren, want het is een grappig verhaal over een kapotte telefoon." },
              { key: "C", text: "Activeren, want de schrijver spoort je direct aan om actie te ondernemen en je telefoon weg te leggen." },
              { key: "D", text: "Overtuigen, want de schrijver wil dat je vegetariër wordt." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Activeren</em>: 'Je iets laten doen'. De schrijver geeft niet alleen feiten, maar roept je actief op om nú actie te ondernemen: 'leg je telefoon in een andere kamer...', 'Kom op, leg die telefoon nu meteen weg...' Het doel is dus activeren!"
          },
          {
            id: 11,
            question: "In de tweede alinea staat het signaalwoord 'Bovendien'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan met de focus." },
              { key: "B", text: "Reden/oorzaak, want het legt uit waarom melatonine wordt aangemaakt." },
              { key: "C", text: "Opsomming, want de schrijver voegt een extra nadeel toe aan schermtijd." },
              { key: "D", text: "Tijd, want het geeft aan hoe laat je moet gaan slapen." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'bovendien' onder het kopje <strong>Opsomming</strong>. De schrijver noemt eerst één nadeel van meldingen (focus onderbroken), en somt daarna een tweede nadeel op ('Bovendien zorgt het blauwe licht...')."
          },
          {
            id: 12,
            question: "Stel: je bekijkt vóór het lezen alleen snel de titel van de tekst, de eerste alinea en de dikgedrukte woorden om een eerste indruk te krijgen. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "A",
            explanation: "Volgens het <strong>Spiekbriefje</strong> is <strong>Oriënterend lezen</strong> de strategie waarbij je kijkt naar de 'titel, plaatjes, bron, inleiding'. Je leest de tekst nog niet helemaal, maar bekijkt alleen de buitenkant om snel te voorspellen waar het over gaat."
          }
        ]
      },
      {
        title: "Tekst 4: Verdwaald in de vertaling",
        goal: "Amuseren",
        text: `Het was een bloedhete zomermiddag in Rome toen Emma hongerig op zoek ging naar een restaurantje. Om indruk te maken op de ober, besloot ze een handige vertaal-app te gebruiken om in het Italiaans eten te bestellen. <strong>Toen</strong> ze luidkeels riep: "Ik wil graag een pizza met verse champignons!", vertaalde de app haar woorden per ongeluk heel anders. De app riep door de luidspreker: "Ik wil graag een pizza met levende spinnen!". <strong>Daarna</strong> keek de ober haar doodsbang aan, sloeg een kruisje en rende snel de keuken in om de kok te waarschuwen. Gelukkig konden Emma en de ober er achteraf hartelijk om lachen, en kreeg ze uiteindelijk gewoon haar pizza met champignons.`,
        questions: [
          {
            id: 13,
            question: "Welk tekstdoel heeft deze tekst?",
            options: [
              { key: "A", text: "Activeren, want Emma wil dat iedereen spinnen gaat eten." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat vertaal-apps verboden moeten worden." },
              { key: "C", text: "Informeren, want de schrijver legt uit hoe je een Italiaanse pizza bakt." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal dat bedoeld is om de lezer te vermaken." }
            ],
            correct: "D",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Amuseren</em>: 'verhaal / vermaken'. Deze tekst is een leuk, humoristisch verhaal over Emma die een grappige fout maakt met een vertaal-app in Italië. Het is geschreven om de lezer te vermaken!"
          },
          {
            id: 14,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Reden/oorzaak, want de ober is geschrokken." },
              { key: "B", text: "Opsomming, want er worden meerdere gerechten genoemd." },
              { key: "C", text: "Tijd, want het geeft de chronologische volgorde van de gebeurtenissen aan." },
              { key: "D", text: "Gevolg, want de pizza was uiteindelijk heel erg lekker." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'daarna' onder het kopje <strong>Tijd</strong>. Het geeft aan in welke volgorde de gebeurtenissen plaatsvinden: eerst maakt de app de fout, DAARNA rent de ober geschrokken weg."
          },
          {
            id: 15,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Een grappige vertaalfout." },
              { key: "B", text: "Waarom reizen naar Italië in de hete zomer heel erg vermoeiend is." },
              { key: "C", text: "Emma en de spinnen." },
              { key: "D", text: "Pizza bakken in Rome." }
            ],
            correct: "A",
            explanation: "Het <em>Onderwerp</em> moet volgens de regels van het <strong>Spiekbriefje</strong> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Een grappige vertaalfout' is 3 woorden en dekt precies de lading van het verhaal! Optie B heeft te veel woorden, en opties C en D missen de kern van het misverstand."
          },
          {
            id: 16,
            question: "Stel dat je voor het lezen alleen snel naar de titel en het eerste plaatje kijkt om te voorspellen waar het verhaal over gaat. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "A",
            explanation: "Volgens het <strong>Spiekbriefje</strong> is <strong>Oriënterend lezen</strong> de leesstrategie waarbij je kijkt naar de 'titel, plaatjes, bron, inleiding'. Dit doe je om snel een eerste indruk te krijgen."
          }
        ]
      }
    ]
  },
  {
    examId: 2,
    examTitle: "Sınav 2: School & Samenleving",
    texts: [
      {
        title: "Tekst 5: Telefoons uit in de klas!",
        goal: "Overtuigen",
        text: `Het is echt onbegrijpelijk dat er nog steeds scholen zijn waar leerlingen hun smartphone mogen gebruiken tijdens de les. Deze flitsende apparaatjes zijn de grootste vijand van een productieve les. <strong>Ten eerste</strong> leidt elke binnenkomende melding je direct af, <strong>want</strong> je hersenen willen meteen weten wie er een berichtje stuurt. Dit zorgt ervoor dat je de uitleg van de docent mist. Onze school moet daarom een streng telefoonverbod invoeren, <strong>evenals</strong> de scholen in onze buurgemeente die hiermee al geweldige resultaten en hogere cijfers hebben behaald. Laten we er samen voor zorgen dat onze klaslokalen weer plekken van echte concentratie worden!`,
        questions: [
          {
            id: 17,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Smartphones sturen constant meldingen die de hersenen van scholieren overprikkelen." },
              { key: "B", text: "Scholen moeten smartphones in de klas verbieden om de concentratie en cijfers te verbeteren." },
              { key: "C", text: "Scholen in de buurgemeente hebben al heel veel succes met hun strenge telefoonbeleid." },
              { key: "D", text: "Leerlingen missen vaak de belangrijke uitleg van de docent door afleiding." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de belangrijkste boodschap van de hele tekst. De schrijver wil dat we het eens zijn met zijn standpunt: telefoons moeten verboden worden in de klas voor een betere concentratie (B). De andere opties zijn slechts ondersteunende argumenten of voorbeelden."
          },
          {
            id: 18,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is echt onbegrijpelijk dat er nog steeds scholen zijn waar leerlingen hun smartphone mogen gebruiken tijdens de les." },
              { key: "B", text: "Deze flitsende apparaatjes zijn de grootste vijand van een productieve les." },
              { key: "C", text: "Dit zorgt ervoor dat je de uitleg van de docent mist." },
              { key: "D", text: "Er is geen duidelijke kernzin te vinden in deze alinea." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Kernzin</em>: 'Belangrijkste zin van 1 alinea, Vaak 1e of laatste zin'. De allereerste zin stelt direct het centrale standpunt en onderwerp van de alinea vast, namelijk dat telefoons in de klas onbegrijpelijk zijn. De rest legt uit waarom."
          },
          {
            id: 19,
            question: "In de tekst staat het signaalwoord 'evenals'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, omdat onze school verschilt van de buurscholen." },
              { key: "B", text: "Vergelijking, omdat onze school vergeleken wordt met scholen in de buurgemeente." },
              { key: "C", text: "Reden/oorzaak, omdat de buurscholen de reden zijn dat we moeten stoppen." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de andere scholen het verbod invoerden." }
            ],
            correct: "B",
            explanation: "Kijk op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em>. Daar staat 'evenals' onder het kopje <strong>Vergelijking</strong>. De schrijver vergelijkt de situatie op onze school met de succesvolle scholen in de buurt."
          },
          {
            id: 20,
            question: "What is het belangrijkste tekstdoel van deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver wil ons uitleggen hoe een smartphone technisch werkt." },
              { key: "B", text: "Amuseren, want het is een grappig verhaal over een rinkelende telefoon." },
              { key: "C", text: "Overtuigen, want de schrijver geeft een duidelijke mening met argumenten om je te overtuigen." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een nieuwe telefoon gaat kopen." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt het 'onbegrijpelijk' (mening) dat telefoons mogen, en gebruikt argumenten ('leidt af', 'uitleg missen') om jou van zijn standpunt te overtuigen."
          }
        ]
      },
      {
        title: "Tekst 6: De onverwoestbare beerdiertjes",
        goal: "Informeren",
        text: `Diep in de oceanen, op de hoogste bergen en zelfs in de ijskoude ruimte leeft een van de meest bizarre wezens op aarde: het beerdiertje. Dit microscopisch kleine diertje is bijna onmogelijk te doden. <strong>Ten eerste</strong> kunnen beerdiertjes extreme temperaturen overleven, van bijna het absolute nulpunt (-272 °C) tot kokend heet water. <strong>Daardoor</strong> kunnen ze onder extreme omstandigheden in een soort schijndood gaan, waarbij ze al hun lichaamsvocht verliezen en jarenlang overleven. <strong>Omdat</strong> ze zo ongelooflijk sterk zijn, stuurden wetenschappers ze in 2007 zelfs mee met een ruimtemissie, waar ze de dodelijke straling van de kosmos overleefden. Het is dus duidelijk dat deze mini-monstertjes de ultieme overlevers van de natuur zijn.`,
        questions: [
          {
            id: 21,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Wetenschappers stuurden in 2007 beerdiertjes de ruimte in om kosmische straling te meten." },
              { key: "B", text: "Beerdiertjes zijn microscopisch kleine wezens die extreme temperaturen en omstandigheden kunnen overleven." },
              { key: "C", text: "Schijndood is een biologisch proces waarbij een dier al zijn vocht verliest om te overleven." },
              { key: "D", text: "Extreme temperaturen zoals kokend water of de ruimte zijn dodelijk voor de meeste insecten." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de belangrijkste boodschap van de hele tekst. De schrijver wil dat je onthoudt dat beerdiertjes extreme en bizarre omstandigheden overleven (B). De andere opties zijn slechts losse details (2007, schijndood) uit de tekst."
          },
          {
            id: 22,
            question: "In de tekst staat het signaalwoord 'Daardoor'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Opsomming, want er wordt een tweede temperatuur genoemd." },
              { key: "B", text: "Tegenstelling, want schijndood is het tegenovergestelde van leven." },
              { key: "C", text: "Gevolg, omdat de schijndood en het overleven het directe resultaat zijn van hun extreme weerstand." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de beerdiertjes doodgaan." }
            ],
            correct: "C",
            explanation: "Op ons <strong>Spiekbriefje</strong> staat 'daardoor' onder het kopje <strong>Gevolg</strong>. Hun extreme weerstand heeft als direct <em>gevolg</em> dat ze in schijndood kunnen gaan en jarenlang kunnen overleven zonder water."
          },
          {
            id: 23,
            question: "Welke leesstrategie gebruik je als je snel alleen de eerste en de laatste alinea van deze tekst leest om te weten te komen wat de grote lijn van het artikel is?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> is hier heel duidelijk over! Bij <strong>Globaal lezen</strong> staat: '1e + laatste alinea'. Dit doe je als je snel de hoofdlijnen van de tekst wilt begrijpen zonder alle details te lezen."
          },
          {
            id: 24,
            question: "In welke optie is de zin waarin staat dat beerdiertjes microscopisch klein zijn juist geciteerd?",
            options: [
              { key: "A", text: "Beerdiertjes zijn microscopisch klein en overleven de ruimte." },
              { key: "B", text: "“Diep in de oceanen, op de hoogste bergen en zelfs in de ijskoude ruimte leeft een van de meest bizarre wezens op aarde: het beerdiertje.”" },
              { key: "C", text: "“Dit microscopisch kleine diertje is bijna onmogelijk te doden.”" },
              { key: "D", text: "In de tekst staat geschreven dat ze microscopisch klein zijn." }
            ],
            correct: "C",
            explanation: "Voor <strong>Citeren</strong> kijken we naar the regel op het <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie C is de enige optie die de zin letterlijk overneemt én tussen de juiste aanhalingstekens zet."
          }
        ]
      },
      {
        title: "Tekst 7: De brutale papegaai in de klas",
        goal: "Amuseren",
        text: `Het was een rustige vrijdagochtend toen meneer Gijsberts begon met zijn saaie aardrijkskundeles. <strong>Eerst</strong> leek iedereen braaf op te letten en aantekeningen te maken. <strong>Maar</strong> toen de klok kwart voor twaalf sloeg, klonk er ineens een schelle, luide schoolbel door de klas. Iedereen pakte enthousiast zijn tas in en rende naar de deur. Meneer Gijsberts keek verbaasd op zijn horloge: de echte bel zou pas over een kwartier gaan! Uit de hoek van de klas klonk ineens een luid, krassend gelach. Daar zat Coco, de ontsnapte papegaai van de buurman, die de schoolbel perfect had leren imiteren. Zelfs meneer Gijsberts kon zijn lachen niet inhouden; de les was officieel afgelopen.`,
        questions: [
          {
            id: 25,
            question: "Welk tekstdoel heeft deze tekst?",
            options: [
              { key: "A", text: "Activeren, want Coco wil dat we allemaal papegaaien gaan kopen." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat aardrijkskunde saai is." },
              { key: "C", text: "Informeren, want de schrijver legt uit hoe papegaaien geluiden produceren." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal dat bedoeld is om de lezer te vermaken." }
            ],
            correct: "D",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Amuseren</em>: 'verhaal / vermaken'. Deze tekst is een grappig, verhalend stukje over Coco de papegaai die de klas fopt met een nagemaakte schoolbel. Het is puur bedoeld om de lezer te vermaken en te laten lachen!"
          },
          {
            id: 26,
            question: "Welke leesstrategie gebruik je als je deze tekst heel nauwkeurig gaat lezen om alle details goed te begrijpen voor een proefwerk?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <strong>Intensief lezen</strong>: 'hele tekst goed lezen'. Als je een toets of proefwerk krijgt, moet je elk detail en elke zin heel nauwkeurig begrijpen. Dit doe je dus door intensief te lezen."
          },
          {
            id: 27,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Een brutale, slimme papegaai." },
              { key: "B", text: "Waarom aardrijkskundelessen op de vrijdag soms heel erg saai kunnen zijn." },
              { key: "C", text: "Coco en de schoolbel." },
              { key: "D", text: "Tassen inpakken." }
            ],
            correct: "A",
            explanation: "Het <em>Onderwerp</em> moet volgens de regels van het <strong>Spiekbriefje</strong> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Een brutale, slimme papegaai' is 4 woorden en dekt precies de kern van het verhaal! Optie B heeft veel te veel woorden, en opties C en D missen de kern."
          },
          {
            id: 28,
            question: "In welk deel van de opbouw bevindt zich de zin: 'Het was een rustige vrijdagochtend toen meneer Gijsberts begon met zijn saaie aardrijkskundeles.'?",
            options: [
              { key: "A", text: "Het Middenstuk" },
              { key: "B", text: "De Inleiding" },
              { key: "C", text: "Het Slot" },
              { key: "D", text: "De Kernzin" }
            ],
            correct: "B",
            explanation: "Volgens het <strong>Spiekbriefje</strong> bestaat de <em>Opbouw van een tekst</em> uit: Inleiding, Middenstuk, Slot. De allereerste alinea (en zeker de allereerste zin) vormt de <strong>Inleiding</strong>, waarin de hoofdpersoon, de situatie en het onderwerp worden geïntroduceerd."
          }
        ]
      },
      {
        title: "Tekst 8: Lichtgevende golven in de zee",
        goal: "Informeren",
        text: `Wie 's nachts over een donker strand wandelt, kan soms getuige zijn van een sprookjesachtig blauw licht in de golven. Dit natuurverschijnsel heet 'bioluminescentie'. <strong>Ten eerste</strong> wordt dit licht geproduceerd door minuscule organismen in de zee, genaamd zeevonk. <strong>Echter</strong>, ze geven dit licht niet zomaar af: het is een afweermechanisme dat alleen geactiveerd wordt bij beweging, bijvoorbeeld als er golven omslaan of als je door het water loopt. <strong>Daardoor</strong> schrikken roofdieren af die de zeevonk willen opeten. Dit magische, blauwe schijnsel is een van de mooiste biologische lichtshows ter wereld.`,
        questions: [
          {
            id: 29,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel!)",
            options: [
              { key: "A", text: "Hoe minuscule zeevonk-organismen 's nachts heel mooi blauw licht kunnen geven in zee." },
              { key: "B", text: "Lichtgevende golven in zee." },
              { key: "C", text: "Waarom roofdieren bang zijn voor blauw licht in de donkere oceanen." },
              { key: "D", text: "Wandelen op het strand." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('Lichtgevende golven in zee') is 4 woorden en dekt precies de lading van het hele artikel! Optie A is veel te lang."
          },
          {
            id: 30,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft biologische feiten en uitleg over bioluminescentie." },
              { key: "B", text: "Overtuigen, want de schrijver wil dat we allemaal zeevonk in een potje gaan houden." },
              { key: "C", text: "Activeren, want de schrijver roept op om direct naar het strand te rennen." },
              { key: "D", text: "Amuseren, want het is een spannend sprookje over tovenaars in zee." }
            ],
            correct: "A",
            explanation: "Kijk op het <strong>Spiekbriefje</strong> bij <em>Tekstdoelen</em>. Bij <strong>Informeren</strong> staat: 'uitleg / feiten'. De schrijver deelt interessante, biologische feiten over zeevonk en bioluminescentie. Er wordt geen mening gegeven en we hoeven niets te doen."
          },
          {
            id: 31,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Opsomming, want er wordt een tweede organisme genoemd." },
              { key: "B", text: "Tegenstelling, want het geeft aan dat het licht niet continu brandt maar een reactie is." },
              { key: "C", text: "Reden/oorzaak, want het legt uit waarom roofdieren schrikken." },
              { key: "D", text: "Gevolg, want het is het resultaat van de golven." }
            ],
            correct: "B",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'echter' onder het kopje <strong>Tegenstelling</strong>. Het geeft een contrast/tegenstelling aan: zeevonk kan licht maken, ECHTER/MAAR dat doen ze niet constant zomaar."
          },
          {
            id: 32,
            question: "In welke optie is de wetenschappelijke term voor het lichtgevende natuurverschijnsel juist geciteerd?",
            options: [
              { key: "A", text: "Dit natuurverschijnsel heet bioluminescentie." },
              { key: "B", text: "“bioluminescentie”" },
              { key: "C", text: "“zeevonk”" },
              { key: "D", text: "“magische, blauwe schijnsel”" }
            ],
            correct: "B",
            explanation: "Volgens het <strong>Spiekbriefje</strong> moet je bij <strong>Citeren</strong> de woorden 'Letterlijk overschrijven met aanhalingstekens: “...”'. De term voor het verschijnsel zelf is bioluminescentie, en optie B citeert dit letterlijk met aanhalingstekens."
          }
        ]
      }
    ]
  },
  {
    examId: 3,
    examTitle: "Sınav 3: Natuur & Extreme Werelden",
    texts: [
      {
        title: "Tekst 9: De geheimzinnige diepzee",
        goal: "Informeren",
        text: `Op de bodem van de diepste oceanen, waar geen straaltje zonlicht doordringt, heerst een mysterieuze wereld vol vreemde schepsels. <strong>Ten eerste</strong> leven hier vissen die hun eigen licht kunnen maken met hulp van bacteriën, wat bioluminescentie heet. Dit licht gebruiken ze om prooien te lokken of partners te vinden in de inktzwarte duisternis. <strong>Echter</strong>, het leven is daar heel zwaar, <strong>omdat</strong> de waterdruk gigantisch hoog is en de temperatuur vlak boven het vriespunt ligt. Toch hebben deze diepzeebewoners zich perfect aangepast aan deze extreme leefomgeving.`,
        questions: [
          {
            id: 33,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel uit het spiekbriefje!)",
            options: [
              { key: "A", text: "De geheimzinnige diepzee." },
              { key: "B", text: "Waarom vissen op de bodem van de diepste oceanen leven en licht maken." },
              { key: "C", text: "Bioluminescentie in diepzeevissen." },
              { key: "D", text: "Extreme temperaturen en waterdruk." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie A ('De geheimzinnige diepzee') is 3 woorden en dekt perfect de hele tekst! Optie B is veel te lang, en optie C en D zijn slechts details."
          },
          {
            id: 34,
            question: "Welk tekstdoel heeft deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver wil dat je diepzeeduiker wordt." },
              { key: "B", text: "Informeren, want de schrijver geeft objectieve feiten en uitleg over de diepzee." },
              { key: "C", text: "Activeren, want de schrijver roept op om de oceanen te beschermen." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over pratende diepzeevissen." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt bij <em>Informeren</em>: 'uitleg / feiten'. De schrijver legt uit hoe het leven in de diepzee werkt en geeft feiten over bioluminescentie en de omstandigheden daar."
          },
          {
            id: 35,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan met het handige gebruik van bioluminescentie." },
              { key: "B", text: "Opsomming, want er wordt een extra feit toegevoegd." },
              { key: "C", text: "Reden/oorzaak, want het legt uit hoe de diepzeevissen zich hebben aangepast." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de vissen licht maken." }
            ],
            correct: "A",
            explanation: "Op ons <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'echter' onder het kopje <strong>Tegenstelling</strong> staan. De schrijver noemt eerst hoe handig het eigen licht is, maar stelt daar de zware leefomstandigheden tegenover."
          },
          {
            id: 36,
            question: "In welke van de onderstaande zinnen is de term voor het maken van eigen licht juist geciteerd?",
            options: [
              { key: "A", text: "Dit verschijnsel noemen we bioluminescentie." },
              { key: "B", text: "“wat bioluminescentie heet”" },
              { key: "C", text: "“bioluminescentie”" },
              { key: "D", text: "Ze maken hun eigen licht, wat bioluminescentie wordt genoemd." }
            ],
            correct: "C",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie C is de exacte term tussen de juiste aanhalingstekens!"
          }
        ]
      },
      {
        title: "Tekst 10: Ban energiedrankjes voor jongeren!",
        goal: "Overtuigen",
        text: `Het is onbegrijpelijk dat jongeren onder de achttien jaar nog steeds supergoedkoop energiedrankjes kunnen kopen in de supermarkt. Deze zoete blikjes zijn een gevaar voor de gezondheid van tieners. <strong>Ten eerste</strong> bevatten ze een enorme hoeveelheid cafeïne en suiker, wat kan leiden tot hartkloppingen en slapeloosheid. <strong>Bovendien</strong> presteren leerlingen op school juist slechter na de bekende 'suikercrash'. <strong>Hoewel</strong> fabrikanten beweren dat hun drankjes zorgen for betere focus tijdens het gamen of leren, waarschuwen artsen dat de gezondheidsrisico's veel groter zijn. De overheid moet <strong>daarom</strong> snel een wettelijke leeftijdsgrens van achttien jaar invoeren voor deze ongezonde drankjes!`,
        questions: [
          {
            id: 37,
            question: "Wat is de hoofdgedachte van deze tekst? (Truc: Wat wil de schrijver dat ik onthoud?)",
            options: [
              { key: "A", text: "Energiedrankjes bevatten heel veel cafeïne en suiker wat slecht is voor de gezondheid." },
              { key: "B", text: "Er moet een leeftijdsgrens van 18 jaar komen voor energiedrankjes om jongeren te beschermen." },
              { key: "C", text: "Fabrikanten maken reclame voor betere focus tijdens het gamen en leren." },
              { key: "D", text: "Supermarkten verdienen veel geld met de verkoop van goedkope energiedrankjes." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de belangrijkste boodschap van de hele tekst. De truc is: 'Wat wil de schrijver dat ik onthoud?'. De schrijver wil dat we het eens zijn met zijn standpunt: er moet een leeftijdsgrens van 18 jaar komen (B). De andere opties zijn slechts argumenten of details."
          },
          {
            id: 38,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want er staan alleen maar neutrale feiten in over suiker." },
              { key: "B", text: "Overtuigen, want de schrijver geeft een sterke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een knop om direct een petitie te tekenen." },
              { key: "D", text: "Amuseren, want het is een grappig stripverhaal over een vliegend blikje." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt de verkoop 'onbegrijpelijk' (mening) en geeft argumenten ('cafeïne', 'suikercrash') om je te overtuigen van een verbod."
          },
          {
            id: 39,
            question: "In de tekst staat het signaalwoord 'daarom'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Reden/oorzaak of Gevolg, want het geeft de conclusie/het gevolg aan van alle gezondheidsrisico's." },
              { key: "B", text: "Tegenstelling, want het laat een verschil zien." },
              { key: "C", text: "Opsomming, want het voegt nog een risico toe." },
              { key: "D", text: "Vergelijking, want het vergelijkt energiedrank met koffie." }
            ],
            correct: "A",
            explanation: "Op ons <strong>Spiekbriefje</strong> staat 'daarom' onder zowel <strong>Reden/oorzaak</strong> als <strong>Gevolg</strong>. Omdat de drankjes zo gevaarlijk zijn (oorzaak), moet de overheid DAAROM (gevolg) een verbod invoeren."
          },
          {
            id: 40,
            question: "Wat is de kernzin van de eerste twee zinnen van deze alinea?",
            options: [
              { key: "A", text: "Het is onbegrijpelijk dat jongeren onder de achttien jaar nog steeds supergoedkoop energiedrankjes kunnen kopen in de supermarkt." },
              { key: "B", text: "Deze zoete blikjes zijn een gevaar voor de gezondheid van tieners." },
              { key: "C", text: "Er is geen kernzin te vinden in deze zinnen." },
              { key: "D", text: "De overheid moet daarom snel een wettelijke leeftijdsgrens invoeren." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> leert ons over de <em>Kernzin</em>: 'Belangrijkste zin alinea (1e of laatste)'. De allereerste zin stelt direct het centrale standpunt en het onderwerp van de alinea vast."
          }
        ]
      },
      {
        title: "Tekst 11: Zeg ja tegen de natuur: Plant een bijenhotel!",
        goal: "Activeren",
        text: `Wist je dat wilde bijen onmisbaar zijn voor onze natuur, maar dat ze steeds moeilijker een nestje kunnen vinden? Gelukkig kun jij heel makkelijk helpen om onze bijen te redden! <strong>Hoewel</strong> bijen soms een griezelig imago hebben, doen ze geen vlieg kwaad als je ze met rust laat. <strong>Bovendien</strong> is het superleuk en leerzaam om te zien hoe ze hun eitjes leggen in een zelfgemaakt hotel. <strong>Dus</strong> kom direct in actie! Koop vandaag nog een bijenhotel in het tuincentrum, of bouw er zelf een van hout en holle bamboestokken. Hang het hotel op een zonnige plek op <strong>wanneer</strong> de lente begint, en geniet van al het leven in je eigen tuin!`,
        questions: [
          {
            id: 41,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver legt alleen de anatomie van de wilde bij uit." },
              { key: "B", text: "Activeren, want de schrijver spoort de lezer actief aan om direct een bijenhotel te plaatsen." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat de lezer op een politieke bijenpartij stemt." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over bijenkoningin Maya." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Activeren</em>: 'je iets laten doen'. De schrijver roept je direct op om in actie te komen: 'kom direct in actie!', 'Koop vandaag nog...', 'Hang het hotel op...'. Het doel is dus activeren!"
          },
          {
            id: 42,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Wilde bijen in onze natuur." },
              { key: "B", text: "Een bijenhotel plaatsen." },
              { key: "C", text: "Waarom bijen erg nuttig zijn voor het bestuiven van planten en bloemen." },
              { key: "D", text: "Bamboe en hout kopen." }
            ],
            correct: "B",
            explanation: "Volgens het <strong>Spiekbriefje</strong> mag het <em>Onderwerp</em> maximaal 4 woorden lang zijn en moet het vertellen waar de tekst over gaat. 'Een bijenhotel plaatsen' (3 woorden) dekt de lading perfect! Optie C is veel te lang."
          },
          {
            id: 43,
            question: "In de tekst staat het signaalwoord 'wanneer'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want de lente is anders dan de winter." },
              { key: "B", text: "Reden, want de lente is de reden dat de bijen vliegen." },
              { key: "C", text: "Tijd, want het geeft aan op welk moment je het hotel moet ophangen." },
              { key: "D", text: "Opsomming, want het voegt een seizoen toe." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'wanneer' onder het kopje <strong>Tijd</strong> (samen met eerst, daarna, voordat). Het geeft het tijdstip of moment aan waarop je actie moet ondernemen: in de lente!"
          },
          {
            id: 44,
            question: "In welke van de onderstaande opties is het nut van de bijen op een juiste manier geciteerd?",
            options: [
              { key: "A", text: "De schrijver zegt dat bijen erg belangrijk zijn." },
              { key: "B", text: "“Wist je dat wilde bijen onmisbaar zijn voor onze natuur”" },
              { key: "C", text: "“wilde bijen onmisbaar zijn”" },
              { key: "D", text: "Bijen zijn nuttig voor de bloemetjes." }
            ],
            correct: "B",
            explanation: "Bij <strong>Citeren</strong> zegt het <strong>Spiekbriefje</strong>: 'Letterlijk woorden overschrijven met aanhalingstekens'. Optie B citeert een volledige zin over het nut van bijen op de juiste manier met aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 12: Het mysterie van de verdwenen linkerloopschoen",
        goal: "Amuseren",
        text: `Hardloper Dennis werd de afgelopen weken helemaal gek van zijn verdwenen spullen. <strong>Eerst</strong> dacht hij nog dat hij gewoon slordig was en zijn loopschoenen steeds kwijtraakte. <strong>Maar</strong> toen hij al voor de vierde keer een gloednieuwe rechterloopschoen in de gang vond zonder de linkerschoen, wist hij dat er iets geks aan de hand was. Hij besloot op onderzoek uit te gaan en legde een reservelinkschoen in de tuin als lokaas. <strong>Daarna</strong> zag hij vanuit het keukenraam hoe Max, de golden retriever van de buurman, geruisloos over de schutting sprong, de linkerschoen met zijn tanden oppakte en vrolijk kwispelend wegglipte. Gelukkig kon Dennis erom lachen en heeft Max nu een prachtige verzameling linkerschoenen in zijn hondenhok liggen.`,
        questions: [
          {
            id: 45,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Activeren, want de schrijver wil dat je loopschoenen gaat kopen." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat honden verboden moeten worden." },
              { key: "C", text: "Informeren, want de schrijver geeft wetenschappelijke feiten over honden." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal om de lezer te vermaken." }
            ],
            correct: "D",
            explanation: "Volgens het <strong>Spiekbriefje</strong> hoort bij <em>Amuseren</em>: 'verhaal / vermaken'. Dit is een grappig en vermakelijk verhaal over een hond die de linkerschoenen van de buurman steelt. Geen meningen of zware feiten, puur vermaak!"
          },
          {
            id: 46,
            question: "In de tekst staat het signaalwoord 'Eerst'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tijd, want het geeft de chronologische volgorde van Dennis zijn gedachten aan." },
              { key: "B", text: "Tegenstelling, want Dennis vindt de loopschoenen heel erg duur." },
              { key: "C", text: "Reden/oorzaak, want Dennis is slordig." },
              { key: "D", text: "Vergelijking, want Dennis vergelijkt honden met katten." }
            ],
            correct: "A",
            explanation: "Kijk op het <strong>Spiekbriefje</strong>. Het woord 'eerst' staat onder het kopje <strong>Tijd</strong> (samen met daarna, voordat, wanneer). Het geeft aan wat er als eerste gebeurde in de tijdlijn."
          },
          {
            id: 47,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel!)",
            options: [
              { key: "A", text: "Dennis die zijn loopschoenen kwijtraakt in de hete zomerdagen." },
              { key: "B", text: "Honden die heel erg lief zijn." },
              { key: "C", text: "De diefstal van linkerschoenen." },
              { key: "D", text: "Een schoenenstelende hond." }
            ],
            correct: "D",
            explanation: "Het <em>Onderwerp</em> mag volgens de regels van het <strong>Spiekbriefje</strong> maximaal 4 woorden zijn. 'Een schoenenstelende hond' (3 woorden) omschrijft de kern van de tekst perfect! Optie A is veel te lang."
          },
          {
            id: 48,
            question: "Stel dat je voor het lezen alleen snel naar de titel en het grappige plaatje kijkt om te voorspellen waar de tekst over gaat. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <strong>Oriënterend lezen</strong>: 'titel, plaatjes, bron, inleiding bekijken'. Dit doe je om snel een eerste voorspelling te maken van de inhoud voordat je echt gaat lezen."
          }
        ]
      }
    ]
  },
  {
    examId: 4,
    examTitle: "Sınav 4: Slimme Dieren & Huiswerk",
    texts: [
      {
        title: "Tekst 13: De verbazingwekkende slimheid van kraaien",
        goal: "Informeren",
        text: `Kraaien worden door biologen gezien als een van de meest intelligente diersoorten op onze planeet. <strong>Ten eerste</strong> kunnen ze ingewikkelde gereedschappen maken, zoals het buigen van een ijzerdraadje om hiermee voedsel uit een smalle buis te peuteren. <strong>Daardoor</strong> zijn ze in staat om complexe puzzels op te lossen die voor de meeste andere dieren veel te moeilijk zijn. <strong>Echter</strong>, ze zijn niet alleen goed met objecten; kraaien kunnen ook de gezichten van mensen herkennen. Als een mens ooit gemeen tegen hen is geweest, onthouden ze dat jarenlang en waarschuwen ze zelfs hun soortgenoten met luide kreten.`,
        questions: [
          {
            id: 49,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "De intelligentie van kraaien." },
              { key: "B", text: "Hoe kraaien met ijzerdraadjes en gereedschappen heel slim voedsel uit buisjes kunnen peuteren." },
              { key: "C", text: "Gezichten herkennen door vogels." },
              { key: "D", text: "Biologen en vogels." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie A ('De intelligentie van kraaien') is 4 woorden en dekt perfect de lading van het hele artikel! Optie B is veel te lang."
          },
          {
            id: 50,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Activeren, want de schrijver wil dat je direct een kraai als huisdier gaat kopen." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat kraaien the baas van de wereld moeten worden." },
              { key: "C", text: "Informeren, want de schrijver geeft wetenschappelijke uitleg en feiten over kraaien." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een sprekende kraai." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt bij <em>Informeren</em>: 'uitleg / feiten'. De schrijver deelt interessante feiten en biologische uitleg over het gedrag van kraaien, zonder een mening op te dringen."
          },
          {
            id: 51,
            question: "In de tekst staat het signaalwoord 'Daardoor'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Opsomming, want er wordt een vergelijking gemaakt." },
              { key: "B", text: "Tegenstelling, want kraaien zijn soms ook heel erg stout." },
              { key: "C", text: "Gevolg of Reden/oorzaak, omdat het vermogen om gereedschap te maken als gevolg heeft dat ze puzzels oplossen." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de vogels eten." }
            ],
            correct: "C",
            explanation: "Op ons <strong>Spiekbriefje</strong> staat 'daardoor' onder <strong>Gevolg</strong> en <strong>Reden/oorzaak</strong>. Omdat ze gereedschappen maken, is het <em>gevolg</em> dat ze complexe puzzels kunnen oplossen."
          },
          {
            id: 52,
            question: "In welke van de onderstaande zinnen is het vermogen om mensen te herkennen juist geciteerd?",
            options: [
              { key: "A", text: "Ze kunnen ook de gezichten van mensen herkennen." },
              { key: "B", text: "Kraaien onthouden je gezicht heel erg lang." },
              { key: "C", text: "“kraaien kunnen ook de gezichten van mensen herkennen”" },
              { key: "D", text: "“gezichten van mensen herkennen”" }
            ],
            correct: "C",
            explanation: "Volgens het <strong>Spiekbriefje</strong> moet je bij <strong>Citeren</strong> de woorden 'Letterlijk overschrijven met aanhalingstekens: “...”'. Optie C doet dit perfect."
          }
        ]
      },
      {
        title: "Tekst 14: Huiswerk moet direct afgeschaft worden!",
        goal: "Overtuigen",
        text: `Het is werkelijk bizar dat scholieren na een lange, vermoeiende schooldag thuis nog urenlang aan hun huiswerk moeten zitten. Dit ouderwetse systeem moet direct worden afgeschaft. <strong>Ten eerste</strong> zorgt huiswerk voor een enorme hoop onnodige stress en faalangst bij jongeren, die al genoeg druk ervaren. <strong>Bovendien</strong> vergroot het de kansenongelijkheid, omdat niet alle ouders thuis de tijd of de kennis hebben om hun kinderen te helpen. <strong>Hoewel</strong> voorstanders beweren dat huiswerk goed is voor de discipline, bewijzen moderne onderzoeken dat leerlingen juist veel effectiever leren als ze alle stof gewoon op school onder begeleiding van hun eigen docent afronden. Scholen moeten <strong>daarom</strong> nu stoppen met dit nutteloze huiswerk!`,
        questions: [
          {
            id: 53,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Huiswerk bezorgt scholieren heel veel stress en zorgt voor grote kansenongelijkheid." },
              { key: "B", text: "Scholen moeten huiswerk afschaffen omdat het ineffectief is en stress veroorzaakt." },
              { key: "C", text: "Sommige ouders hebben geen tijd of kennis om hun kinderen te helpen bij schooltaken." },
              { key: "D", text: "Docenten moeten leerlingen op school beter begeleiden tijdens de gewone lessen." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de kernboodschap. De truc is: 'Wat wil de schrijver dat ik onthoud?'. De schrijver wil dat we het eens zijn met zijn standpunt: scholen moeten huiswerk afschaffen (B). De andere opties zijn slechts ondersteunende argumenten."
          },
          {
            id: 54,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen neutrale, wetenschappelijke definities van huiswerk." },
              { key: "B", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want de schrijver wil dat je direct een huiswerkhulp-app gaat downloaden." },
              { key: "D", text: "Amuseren, want het is een spannend verhaal over een ontsnapte docent." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt huiswerk 'bizar' (mening) en somt argumenten op ('stress', 'ongelijkheid') om je te overtuigen van de afschaffing."
          },
          {
            id: 55,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een argument tegen huiswerk." },
              { key: "B", text: "Reden/oorzaak, want het legt uit waarom scholieren moe zijn." },
              { key: "C", text: "Opsomming, want de schrijver voegt een tweede nadeel toe aan de lijst." },
              { key: "D", text: "Tijd, want het geeft aan wanneer scholieren moeten leren." }
            ],
            correct: "C",
            explanation: "Op ons <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'bovendien' onder het kopje <strong>Opsomming</strong> staan. Na het eerste nadeel (stress), somt de schrijver direct een tweede nadeel op (kansenongelijkheid)."
          },
          {
            id: 56,
            question: "Wat is de kernzin van de allereerste alinea (de eerste twee zinnen) van de tekst?",
            options: [
              { key: "A", text: "Het is werkelijk bizar dat scholieren na een lange, vermoeiende schooldag thuis nog urenlang aan hun huiswerk moeten zitten." },
              { key: "B", text: "Dit ouderwetse systeem moet direct worden afgeschaft." },
              { key: "C", text: "Er is geen kernzin te vinden in deze inleiding." },
              { key: "D", text: "Scholen moeten daarom nu stoppen met dit nutteloze huiswerk!" }
            ],
            correct: "B",
            explanation: "Volgens het <strong>Spiekbriefje</strong> staat de <em>Kernzin</em> vaak op de eerste of laatste plek van de alinea. Zin B stelt het centrale standpunt en de hoofdzaak van de inleiding heel krachtig vast, terwijl de eerste zin de aanleiding beschrijft."
          }
        ]
      },
      {
        title: "Tekst 15: Doe mee met de Opschoondag!",
        goal: "Activeren",
        text: `Ligt er bij jou in de buurt ook zoveel zwerfafval op straat en in de bosjes? Dat is niet alleen een lelijk gezicht, maar het is ook nog eens hartstikke gevaarlijk voor vogels en egeltjes die erin verstrikt raken. <strong>Hoewel</strong> het opruimen van andermans troep misschien saai klinkt, maken we er samen een supergezellige dag van! <strong>Bovendien</strong> beloont de gemeente elke deelnemer met een gratis ijsje en een leuke verrassing. Kom <strong>daarom</strong> aanstaande zaterdag om tien uur naar het marktplein en help ons dorp weer stralend schoon te maken! Neem je vrienden en klasgenoten mee <strong>wanneer</strong> je komt, en zorg samen voor een schone buurt!`,
        questions: [
          {
            id: 57,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen biologische feiten over egeltjes." },
              { key: "B", text: "Overtuigen, want de schrijver wil dat je vegetariër wordt." },
              { key: "C", text: "Activeren, want de schrijver spoort je actief aan om mee te doen en afval op te ruimen." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een vuilnisman." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Activeren</em>: 'je iets laten doen'. De schrijver spoort je heel actief aan om in actie te komen: 'Kom daarom aanstaande zaterdag...', 'help ons dorp...', 'Neem je vrienden mee...'. Het doel is dus activeren!"
          },
          {
            id: 58,
            question: "In de tekst staat het signaalwoord 'Hoewel'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan tussen het saaie imago en de gezellige werkelijkheid." },
              { key: "B", text: "Opsomming, want de schrijver voegt een extra activiteit toe." },
              { key: "C", text: "Gevolg, want door het afval gaan we nu opruimen." },
              { key: "D", text: "Vergelijking, want het vergelijkt zwerfafval met egeltjes." }
            ],
            correct: "A",
            explanation: "Op ons <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'hoewel' onder het kopje <strong>Tegenstelling</strong> staan. De schrijver stelt het vooroordeel (saai opruimen) tegenover de gezellige werkelijkheid."
          },
          {
            id: 59,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel!)",
            options: [
              { key: "A", text: "Zwerfafval opruimen in ons eigen gezellige dorp." },
              { key: "B", text: "De gevaren van plastic voor egeltjes en vogels." },
              { key: "C", text: "Meedoen met de Opschoondag." },
              { key: "D", text: "Een gratis ijsje verdienen." }
            ],
            correct: "C",
            explanation: "Het <em>Onderwerp</em> mag volgens het <strong>Spiekbriefje</strong> maximaal 4 woorden zijn. 'Meedoen met de Opschoondag' (4 woorden) dekt de lading van de hele tekst perfect! Optie A is te lang."
          },
          {
            id: 60,
            question: "In welke van de onderstaande zinnen is de beloning van de gemeente op een juiste manier geciteerd?",
            options: [
              { key: "A", text: "De gemeente geeft iedereen die helpt een lekker ijsje." },
              { key: "B", text: "“beloont de gemeente elke deelnemer met een gratis ijsje en een leuke verrassing”" },
              { key: "C", text: "“gratis ijsje en een leuke verrassing”" },
              { key: "D", text: "De gemeente belooft een gratis ijsje en een verrassing aan alle deelnemers." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Citeren</em>: 'Letterlijk woorden overschrijven met aanhalingstekens: “...”'. Optie B citeert de zin over de beloning exact en plaatst deze tussen aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 16: De mislukte pannenkoekenshow",
        goal: "Amuseren",
        text: `Tante Sjaak besloot gisteravond haar beroemde pannenkoeken te bakken voor de hele familie. Om indruk te maken op de kinderen, beloofde ze een spectaculaire pannenkoekenshow te geven. <strong>Eerst</strong> ging alles perfect: het beslag was heerlijk en de eerste pannenkoek gleed soepel door de pan. <strong>Maar</strong> toen ze met een grote zwaai de pan omhoog gooide om de pannenkoek in de lucht om te draaien, ging het hopeloos mis. De pannenkoek vloog met een rotvaart omhoog, miste de pan bij de landing en bleef met een natte klap aan het plafond plakken. <strong>Daarna</strong> keek iedereen met open mond omhoog, waarna de pannenkoek langzaam losliet en precies op tante Sjaaks hoofd landde. Het was <strong>dus</strong> een onvergetelijke show, al moest tante Sjaak wel eerst haar haren wassen.`,
        questions: [
          {
            id: 61,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat tante Sjaak niet kan koken." },
              { key: "B", text: "Informeren, want de schrijver geeft een biologisch recept voor pannenkoeken." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal dat bedoeld is om de lezer te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct pannenkoeken gaan bakken." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> leert ons dat bij <em>Amuseren</em> hoort: 'verhaal / vermaken'. Dit is een grappige anekdote over een mislukte pannenkoeken-flip die op iemands hoofd belandt. Puur geschreven voor de lach!"
          },
          {
            id: 62,
            question: "In de tekst staat het signaalwoord 'dus'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Gevolg of conclusie, want het is de logische conclusie na de mislukte show." },
              { key: "B", text: "Tegenstelling, want de show was eigenlijk heel erg mislukt." },
              { key: "C", text: "Reden/oorzaak, want tante Sjaak moest haar haren wassen." },
              { key: "D", text: "Tijd, want het geeft aan dat de show afgelopen is." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'dus' onder het kopje <strong>Gevolg</strong>. Het geeft de conclusie of het gevolg aan van de hele grappige gebeurtenis: het was dus een onvergetelijke show!"
          },
          {
            id: 63,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Pannenkoeken bakken met tante Sjaak op een gezellige gisteravond." },
              { key: "B", text: "Een mislukte pannenkoekenshow." },
              { key: "C", text: "Haren wassen na het bakken." },
              { key: "D", text: "Tante Sjaak haar haren." }
            ],
            correct: "B",
            explanation: "Het <em>Onderwerp</em> moet volgens de regels van het <strong>Spiekbriefje</strong> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Een mislukte pannenkoekenshow' (3 woorden) dekt de hele tekst perfect!"
          },
          {
            id: 64,
            question: "Stel dat je voor het lezen alleen snel naar de titel en de eerste en laatste alinea kijkt om te weten waar de grote lijn van het artikel over gaat. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "B",
            explanation: "Op ons <strong>Spiekbriefje</strong> onder <em>Leesstrategieën</em> staat bij <strong>Globaal lezen</strong>: '1e + laatste alinea'. Dit doe je om snel de hoofdlijnen van de tekst te begrijpen."
          }
        ]
      }
    ]
  },
  {
    examId: 5,
    examTitle: "Sınav 5: Aarde, Plastic & Ruimte",
    texts: [
      {
        title: "Tekst 17: Hoe ontstaan vulkanen?",
        goal: "Informeren",
        text: `Diep onder de aardkorst is het zo ontzettend heet dat gesteente vloeibaar wordt, wat we magma noemen. Dit magma kan soms via scheuren in de aarde naar buiten stromen, waardoor een vulkaan ontstaat. <strong>Ten eerste</strong> bewegen de grote platen waaruit de aardkorst bestaat constant heel langzaam langs elkaar. <strong>Omdat</strong> deze platen soms botsen of uit elkaar schuiven, ontstaan er zwakke plekken in de aardkorst waar het magma makkelijk omhoog kan drukken. <strong>Daardoor</strong> bouwt de druk ondergronds enorm op, tot de vulkaan uiteindelijk met veel geweld uitbarst, <strong>evenals</strong> een geschudde fles frisdrank waarvan je de dop eraf draait. Het bestuderen van vulkanen helpt wetenschappers om de krachten van onze planeet beter te begrijpen.`,
        questions: [
          {
            id: 65,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel!)",
            options: [
              { key: "A", text: "Het ontstaan van vulkanen." },
              { key: "B", text: "Hoe vloeibaar magma diep onder de aardkorst voor heftige vulkaanuitbarstingen zorgt." },
              { key: "C", text: "Platen in de aardkorst." },
              { key: "D", text: "Wetenschappers en aardbevingen." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie A ('Het ontstaan van vulkanen') is 4 woorden en dekt precies de hele tekst! Optie B is veel te lang."
          },
          {
            id: 66,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Activeren, want de schrijver wil dat je direct op reis gaat naar een actieve vulkaan." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat vulkanen verboden moeten worden." },
              { key: "C", text: "Informeren, want de schrijver geeft wetenschappelijke feiten en uitleg over de aarde." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een spugende berg." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Informeren</em>: 'uitleg / feiten'. De schrijver legt uit hoe vulkanen ontstaan en deelt geografische feiten, zonder een mening op te dringen."
          },
          {
            id: 67,
            question: "In de tekst staat het signaalwoord 'evenals'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want een vulkaan is warmer dan frisdrank." },
              { key: "B", text: "Opsomming, want frisdrank is ook vloeibaar." },
              { key: "C", text: "Vergelijking, omdat de uitbarsting vergeleken wordt met het openen van een geschudde fles frisdrank." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de dop van de fles gaat." }
            ],
            correct: "C",
            explanation: "Op ons <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'evenals' onder het kopje <strong>Vergelijking</strong> (samen met zoals) staan. De schrijver vergelijkt de druk in een vulkaan met de druk in een geschudde fles frisdrank."
          },
          {
            id: 68,
            question: "In welke van de onderstaande opties is de definitie van vloeibaar gesteente op een juiste manier geciteerd?",
            options: [
              { key: "A", text: "Gesteente dat vloeibaar is heet magma." },
              { key: "B", text: "“gesteente vloeibaar wordt, wat we magma noemen”" },
              { key: "C", text: "“magma”" },
              { key: "D", text: "Vloeibaar gesteente is heel erg heet." }
            ],
            correct: "B",
            explanation: "Bij <strong>Citeren</strong> zegt het <strong>Spiekbriefje</strong>: 'Letterlijk woorden overschrijven met aanhalingstekens: “...”'. Optie B citeert de volledige uitleg van de term magma letterlijk en op de juiste wijze."
          }
        ]
      },
      {
        title: "Tekst 18: Stop met plastictassen in de supermarkt!",
        goal: "Overtuigen",
        text: `Het is werkelijk schandalig dat supermarkten nog steeds plastic wegwerptasjes aanbieden bij de kassa. Deze tassen zijn een enorme ramp voor onze oceanen en ons milieu. <strong>Ten eerste</strong> duurt het honderden jaren voordat plastic in de natuur is afgebroken, waardoor het dierlijk leven langzaam wordt vergiftigd. <strong>Bovendien</strong> kost de productie van plastic enorm veel fossiele brandstoffen, wat slecht is voor het klimaat. <strong>Hoewel</strong> supermarkten beweren dat ze al veel recyclen, is de enige echte oplossing om helemaal te stoppen met plastic zakken. Scholen en gezinnen moeten <strong>daarom</strong> vandaag nog overstappen op herbruikbare stoffen tassen en plastic definitief verbannen!`,
        questions: [
          {
            id: 69,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Supermarkten verkopen heel veel plastic tasjes die slecht zijn voor vogels en vissen." },
              { key: "B", text: "Supermarkten moeten direct stoppen met plastic tasjes en we moeten overstappen op stoffen tassen." },
              { key: "C", text: "Het duurt honderden jaren voordat plastic tasjes in de natuur volledig zijn afgebroken." },
              { key: "D", text: "Stoffen tassen zijn veel mooier en steviger dan goedkope plastic tasjes." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de belangrijkste boodschap van de hele tekst. De truc is: 'Wat wil de schrijver dat ik onthoud?'. De schrijver wil dat we het eens zijn met zijn standpunt: we moeten stoppen met plastic tassen en overstappen op stoffen tassen (B)."
          },
          {
            id: 70,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen neutrale, chemische feiten over plastic." },
              { key: "B", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om direct een stoffen tas te bestellen." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een pratende plastic zak." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt het gebruik 'schandalig' (mening) en geeft argumenten ('honderden jaren afbreken', 'fossiele brandstoffen') om je te overtuigen."
          },
          {
            id: 71,
            question: "In de tekst staat het signaalwoord 'Hoewel'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan tussen de bewering van supermarkten en de echte oplossing." },
              { key: "B", text: "Opsomming, want de schrijver noemt een extra voordeel." },
              { key: "C", text: "Reden/oorzaak, want het legt uit waarom we plastic recyclen." },
              { key: "D", text: "Vergelijking, want het vergelijkt plastic met katoen." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'hoewel' onder het kopje <strong>Tegenstelling</strong> staan. De schrijver stelt de claim van supermarkten (wij recyclen al veel) tegenover de werkelijke oplossing (helemaal stoppen)."
          },
          {
            id: 72,
            question: "Wat is de kernzin van het eerste deel van de tekst (de eerste twee zinnen)?",
            options: [
              { key: "A", text: "Het is werkelijk schandalig dat supermarkten nog steeds plastic wegwerptasjes aanbieden bij de kassa." },
              { key: "B", text: "Deze tassen zijn een enorme ramp voor onze oceanen en ons milieu." },
              { key: "C", text: "Er is geen kernzin te vinden in dit gedeelte van de tekst." },
              { key: "D", text: "Scholen en gezinnen moeten daarom vandaag nog overstappen." }
            ],
            correct: "A",
            explanation: "Volgens ons <strong>Spiekbriefje</strong> staat de <em>Kernzin</em> vaak op de eerste plek van de alinea. De allereerste zin stelt direct de hoofdzaak en de mening van de schrijver vast."
          }
        ]
      },
      {
        title: "Tekst 19: Reizen naar Mars",
        goal: "Informeren",
        text: `Binnen nu en twintig jaar willen ruimtevaartorganisaties de eerste mensen naar de planeet Mars sturen. Dit is een gigantische stap voor de mensheid. <strong>Ten eerste</strong> duurt de reis naar de rode planeet al snel zo'n negen maanden, waarin astronauten in een heel kleine capsule moeten samenleven. <strong>Echter</strong>, eenmaal aangekomen is het gevaar nog niet geweken, <strong>omdat</strong> Mars geen ademhalingslucht heeft en de dodelijke straling van de zon er vrij spel heeft. Astronauten zullen dus in speciale ondergrondse koepels moeten wonen om te overleven.`,
        questions: [
          {
            id: 73,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Astronauten in de ruimte." },
              { key: "B", text: "De reis naar Mars." },
              { key: "C", text: "Waarom Mars een heel erg gevaarlijke en ijskoude planeet is." },
              { key: "D", text: "Ondergrondse koepels bouwen." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('De reis naar Mars') is 4 woorden en dekt de hele tekst perfect!"
          },
          {
            id: 74,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Activeren, want de schrijver wil dat je direct een ticket naar Mars boekt." },
              { key: "B", text: "Overtuigen, want de schrijver geeft zijn politieke mening over NASA." },
              { key: "C", text: "Informeren, want the schrijver geeft wetenschappelijke feiten over reizen naar Mars." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over aliens." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt bij <em>Informeren</em>: 'uitleg / feiten'. De schrijver deelt feiten over de reisduur en omstandigheden op Mars."
          },
          {
            id: 75,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan met de eerste stap voor de mensheid." },
              { key: "B", text: "Opsomming, want er wordt een extra planeet genoemd." },
              { key: "C", text: "Reden, want Mars heeft geen atmosfeer." },
              { key: "D", text: "Tijd, want het geeft aan wanneer ze vertrekken." }
            ],
            correct: "A",
            explanation: "Op ons <strong>Spiekbriefje</strong> staat 'echter' onder <strong>Tegenstelling</strong>. De schrijver stelt de opwinding van de reis tegenover de grote gevaren op de planeet zelf."
          },
          {
            id: 76,
            question: "In welke optie is de zin over de reisduur naar Mars juist geciteerd?",
            options: [
              { key: "A", text: "De reis naar de rode planeet duurt ongeveer negen maanden." },
              { key: "B", text: "“Ten eerste duurt de reis naar de rode planeet al snel zo'n negen maanden”" },
              { key: "C", text: "“negen maanden”" },
              { key: "D", text: "In de tekst staat geschreven dat de reis heel lang duurt." }
            ],
            correct: "B",
            explanation: "Bij <strong>Citeren</strong> zegt het <strong>Spiekbriefje</strong>: 'Letterlijk woorden overschrijven met aanhalingstekens: “...”'. Optie B citeert de zin exact."
          }
        ]
      },
      {
        title: "Tekst 20: Stop met vuurwerk tijdens oud en nieuw!",
        goal: "Overtuigen",
        text: `Het afsteken van consumentenvuurwerk tijdens de jaarwisseling moet per direct landelijk verboden worden. Deze gevaarlijke traditie brengt elk jaar te veel schade met zich mee. <strong>Ten eerste</strong> zorgt vuurwerk voor honderden ernstige oogwonden en afgeblazen vingers bij jongeren. <strong>Bovendien</strong> levert de enorme hoeveelheid giftige rook extreme angst op bij huisdieren en wilde vogels, die doodsbang vluchten voor de harde knallen. <strong>Hoewel</strong> liefhebbers beweren dat vuurwerk zorgt voor gezelligheid en sfeer, waarschuwen artsen en politie dat de feestvreugde niet opweegt tegen het leed. De overheid moet <strong>daarom</strong> nu haar verantwoordelijkheid nemen en kiezen voor veilige, centrale vuurwerkshows!`,
        questions: [
          {
            id: 77,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Vuurwerk afsteken zorgt elk jaar voor ernstige ongelukken en gewonden in het ziekenhuis." },
              { key: "B", text: "De overheid moet consumentenvuurwerk verbieden en kiezen voor centrale shows om overlast te voorkomen." },
              { key: "C", text: "Huisdieren en wilde vogels ervaren extreem veel angst door de harde knallen en rook." },
              { key: "D", text: "Vuurwerkliefhebbers vinden dat vuurwerk hoort bij de gezelligheid van oud en nieuw." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de kernboodschap: 'Wat wil de schrijver dat ik onthoud?'. De schrijver betoogt dat er een landelijk verbod moet komen ten gunste van centrale shows (B)."
          },
          {
            id: 78,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt alleen chemische formules van vuurwerkkruit." },
              { key: "B", text: "Overtuigen, want de schrijver geeft een duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om direct een vuurwerkbril te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een rotje." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt de traditie gevaarlijk (mening) en bepleit een verbod met argumenten."
          },
          {
            id: 79,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Opsomming, want het voegt een extra argument toe over dierenleed en milieu." },
              { key: "B", text: "Tegenstelling, want dieren houden niet van vuurwerk." },
              { key: "C", text: "Reden, want de knallen zijn erg hard." },
              { key: "D", text: "Tijd, want oud en nieuw is om middernacht." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'bovendien' onder <strong>Opsomming</strong>. De schrijver noemt eerst oogletsel, en somt daarna het dierenleed op."
          },
          {
            id: 80,
            question: "Wat is de kernzin van de allereerste alinea (de eerste twee zinnen)?",
            options: [
              { key: "A", text: "Het afsteken van consumentenvuurwerk tijdens de jaarwisseling moet per direct landelijk verboden worden." },
              { key: "B", text: "Deze gevaarlijke traditie brengt elk jaar te veel schade met zich mee." },
              { key: "C", text: "Er is geen kernzin te vinden in deze zinnen." },
              { key: "D", text: "De overheid moet daarom nu haar verantwoordelijkheid nemen." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over de <em>Kernzin</em>: 'Belangrijkste zin alinea (1e of laatste)'. De eerste zin stelt direct het krachtige standpunt en onderwerp vast."
          }
        ]
      }
    ]
  },
  {
    examId: 6,
    examTitle: "Sınav 6: Gezondheid & Voedsel",
    texts: [
      {
        title: "Tekst 21: De geschiedenis van chocolade",
        goal: "Informeren",
        text: `Tegenwoordig is chocolade een van de meest populaire lekkernijen ter wereld, maar dat was vroeger wel anders. <strong>Eerst</strong> werd chocolade duizenden jaren geleden door de Maya's gedronken als een bittere, hete drank met chilipeper. Ze geloofden dat cacaobonen een geschenk van de goden waren. <strong>Daarna</strong> brachten Spaanse ontdekkingsreizigers de cacaoboon in de zestiende eeuw naar Europa, <strong>maar</strong> pas toen er suiker aan werd toegevoegd, ontstond de zoete chocolade zoals we die nu kennen.`,
        questions: [
          {
            id: 81,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de 4-woordenregel!)",
            options: [
              { key: "A", text: "De geschiedenis van chocolade." },
              { key: "B", text: "Hoe de Maya's cacaobonen gebruikten in hete drankjes." },
              { key: "C", text: "Cacaobonen in Europa." },
              { key: "D", text: "Chocolade met suiker." }
            ],
            correct: "A",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie A is 4 woorden en dekt de hele historische tekst."
          },
          {
            id: 82,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat iedereen chocolade moet eten." },
              { key: "B", text: "Informeren, want de schrijver deelt historische feiten over chocolade." },
              { key: "C", text: "Activeren, want de schrijver spoort je aan cacaobonen te oogsten." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een cacaomonster." }
            ],
            correct: "B",
            explanation: "De schrijver geeft uitleg en feiten over de geschiedenis van chocolade. Het doel is dus informeren."
          },
          {
            id: 83,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want surfers zijn anders dan skateboarders." },
              { key: "B", text: "Opsomming, want er worden meerdere trucs genoemd." },
              { key: "C", text: "Tijd, want het geeft de chronologische volgorde van het ontstaan aan." },
              { key: "D", text: "Gevolg, want skateboarden werd er populairder door." }
            ],
            correct: "C",
            explanation: "'Daarna' staat op het spiekbriefje onder <strong>Tijd</strong> en geeft de volgorde aan."
          },
          {
            id: 84,
            question: "In welke optie is de bittere drank van de Maya's juist geciteerd?",
            options: [
              { key: "A", text: "De Maya's dronken chocolade als een bittere drank." },
              { key: "B", text: "“drinken als een bittere, hete drank met chilipeper”" },
              { key: "C", text: "“gedronken als een bittere, hete drank met chilipeper”" },
              { key: "D", text: "Chocolade werd met chilipeper gedronken." }
            ],
            correct: "C",
            explanation: "Voor <strong>Citeren</strong> schrijven we de woorden letterlijk over met aanhalingstekens. Optie C doet dit exact zoals in de tekst."
          }
        ]
      },
      {
        title: "Tekst 22: Gezonde lunch op school verplichten!",
        goal: "Overtuigen",
        text: `Het is schrikbarend dat zoveel leerlingen tijdens de pauze grote blikken energiedrank en vette frikandelbroodjes kopen in de supermarkt. Scholen moeten een gezonde, verplichte lunch invoeren voor iedereen. <strong>Ten eerste</strong> zorgt gezonde voeding voor een veel betere concentratie en hogere cijfers tijdens de middaglessen. <strong>Bovendien</strong> vermindert het vermoeidheid en futloosheid bij jongeren. <strong>Hoewel</strong> critici beweren dat scholieren zelf moeten kunnen kiezen wat ze eten, bewijst de praktijk dat jongeren te makkelijk kiezen voor ongezonde rommel. Scholen moeten <strong>daarom</strong> nu gezonde kantines verplichten om leerlingen een gezonde start te geven!`,
        questions: [
          {
            id: 85,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Leerlingen kopen te veel ongezonde frikandelbroodjes en energiedrank in de supermarkt." },
              { key: "B", text: "Scholen moeten een gezonde, verplichte lunch invoeren om de gezondheid en prestaties te verbeteren." },
              { key: "C", text: "Gezonde voeding zorgt for betere concentratie en voorkomt middagdippen." },
              { key: "D", text: "Critici vinden dat scholieren zelf mogen kiezen wat ze in de pauze eten." }
            ],
            correct: "B",
            explanation: "De <em>Hoofdgedachte</em> is de kernboodschap: 'Wat wil de schrijver dat ik onthoud?'. De schrijver wil dat scholen een gezonde, verplichte lunch invoeren (B)."
          },
          {
            id: 86,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen biologische feiten over vitaminen." },
              { key: "B", text: "Overtuigen, want de schrijver geeft een duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om groenten te bestellen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een pratende appel." }
            ],
            correct: "B",
            explanation: "De schrijver geeft zijn mening over de schoollunch en gebruikt argumenten om de lezer te overtuigen."
          },
          {
            id: 87,
            question: "In de tekst staat het signaalwoord 'daarom'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want ongezond is het tegenovergestelde van gezond." },
              { key: "B", text: "Opsomming, want er wordt fruit toegevoegd." },
              { key: "C", text: "Gevolg/conclusie, want de verplichte gezonde kantine is het gevolg van de slechte eetgewoonten." },
              { key: "D", text: "Vergelijking, want frikandelbroodjes worden vergeleken met fruit." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'daarom' onder <strong>Gevolg</strong> en <strong>Reden/oorzaak</strong>. Het trekt de conclusie."
          },
          {
            id: 88,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is schrikbarend dat zoveel leerlingen tijdens de pauze grote blikken energiedrank kopen." },
              { key: "B", text: "Scholen moeten een gezonde, verplichte lunch invoeren voor iedereen." },
              { key: "C", text: "Er is geen kernzin te vinden in deze zinnen." },
              { key: "D", text: "Scholen moeten daarom nu gezonde kantines verplichten." }
            ],
            correct: "B",
            explanation: "De <em>Kernzin</em> is de belangrijkste zin van de alinea (vaak 1e of laatste). De tweede zin stelt heel duidelijk de hoofdzaak en stelling van de alinea vast."
          }
        ]
      },
      {
        title: "Tekst 23: Start met water drinken!",
        goal: "Activeren",
        text: `Voel jij je ook vaak moe, slap of heb je regelmatig last van hoofdpijn tijdens de lessen? Grote kans dat je simpelweg te weinig water drinkt! <strong>Hoewel</strong> frisdranken en sapjes heel lekker lijken, zitten ze vol suikers die je juist uitdrogen. <strong>Bovendien</strong> heeft je lichaam zuiver water nodig om gifstoffen af te voeren en je hersenen scherp te houden. <strong>Dus</strong> kom direct in actie! Leg die zoete blikjes weg en drink vanaf vandaag minstens anderhalve liter kraanwater per dag. Koop een mooie, herbruikbare drinkfles en vul deze <strong>wanneer</strong> je opstaat, zodat je de hele dag fit blijft!`,
        questions: [
          {
            id: 89,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver legt de scheikundige formule van water uit." },
              { key: "B", text: "Activeren, want de schrijver spoort je actief aan om water te drinken en actie te ondernemen." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat kraanwater duurder wordt." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een waterdruppel." }
            ],
            correct: "B",
            explanation: "Het doel is activeren, want de schrijver spoort de lezer actief aan: 'kom direct in actie!', 'drink vanaf vandaag...', 'Koop een mooie fles...'"
          },
          {
            id: 90,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom frisdranken slecht zijn." },
              { key: "B", text: "Meer water drinken." },
              { key: "C", text: "Hoofdpijn tijdens de lessen." },
              { key: "D", text: "Kraanwater en hersenen." }
            ],
            correct: "B",
            explanation: "Het onderwerp omschrijft in maximaal 4 woorden waar de tekst over gaat: 'Meer water drinken' (3 woorden)."
          },
          {
            id: 91,
            question: "In de tekst staat het signaalwoord 'wanneer'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want opstaan is anders dan slapen." },
              { key: "B", text: "Tijd, want het geeft aan op welk moment je de fles moet vullen." },
              { key: "C", text: "Reden, want opstaan is de reden van het vullen." },
              { key: "D", text: "Vergelijking, want opstaan wordt vergeleken met slapen." }
            ],
            correct: "B",
            explanation: "Het woord 'wanneer' staat op het spiekbriefje onder <strong>Tijd</strong>. Het duidt het specifieke moment aan."
          },
          {
            id: 92,
            question: "In welke van de onderstaande opties is de reactie op suikerhoudende frisdranken juist geciteerd?",
            options: [
              { key: "A", text: "Sapjes zitten vol suikers die je uitdrogen." },
              { key: "B", text: "“zitten ze vol suikers die je juist uitdrogen”" },
              { key: "C", text: "“vol suikers”" },
              { key: "D", text: "Sapjes en frisdranken drogen je hersenen uit." }
            ],
            correct: "B",
            explanation: "Optie B citeert de zin uit de tekst letterlijk en plaatst deze tussen aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 24: De soepramp in de keuken",
        goal: "Amuseren",
        text: `Bas wilde indruk maken op zijn vrienden door een chique Franse uiensoep te koken. <strong>Eerst</strong> ging hij vol enthousiasme aan de slag met het snijden van een enorme berg uien. De tranen stroomden over zijn wangen, <strong>maar</strong> hij hield dapper vol. Toen hij de soep op het vuur zette, ging het echter gruwelijk mis. Bas vergat de deksel op de pan te doen, waardoor de soep begon te borrelen en met een harde sisser over de gloeiend hete kookplaat stroomde. De hele keuken vulde zich binnen een minuut met dichte, stinkende rook. <strong>Daarna</strong> ging het brandalarm luidkeels af, waarna zijn vrienden hoestend en lachend de tuin in moesten vluchten. Het was een culinaire ramp, maar ze hebben uiteindelijk wel gezellig pizza besteld.`,
        questions: [
          {
            id: 93,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat Bas niet mag koken." },
              { key: "B", text: "Informeren, want het is een wetenschappelijk recept voor Franse soep." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal dat bedoeld is om de lezer te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een brandblusser koopt." }
            ],
            correct: "C",
            explanation: "Het is een humoristisch en vermakelijk verhaal over een mislukt kookavontuur. Het doel is amuseren."
          },
          {
            id: 94,
            question: "In de tekst staat het signaalwoord 'Eerst'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tijd, want het geeft het begin van de chronologische volgorde van Bas' acties aan." },
              { key: "B", text: "Tegenstelling, want de uien waren erg scherp." },
              { key: "C", text: "Gevolg, want Bas begon te huilen." },
              { key: "D", text: "Vergelijking, want Bas vergelijkt uien met pizza." }
            ],
            correct: "A",
            explanation: "Het woord 'eerst' duidt op het verloop van de gebeurtenissen in de tijd (chronologie)."
          },
          {
            id: 95,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Uien snijden en brandalarmen." },
              { key: "B", text: "Een mislukt soepavontuur." },
              { key: "C", text: "Franse uiensoep koken met je beste vrienden op een gezellige avond." },
              { key: "D", text: "Pizza bestellen in de tuin." }
            ],
            correct: "B",
            explanation: "Het onderwerp omschrijft in maximaal 4 woorden de kern van de tekst: 'Een mislukt soepavontuur' (3 woorden)."
          },
          {
            id: 96,
            question: "Stel dat je voor het lezen alleen snel naar de titel en de inleiding kijkt om te voorspellen waar de tekst over gaat. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "A",
            explanation: "Oriënterend lezen houdt in dat je kijkt naar de buitenkant (titel, inleiding, plaatjes) om te voorspellen waar de tekst over gaat."
          }
        ]
      }
    ]
  },
  {
    examId: 7,
    examTitle: "Sınav 7: Uitvindingen & Boeken",
    texts: [
      {
        title: "Tekst 25: Hoe werkt het internet?",
        goal: "Informeren",
        text: `Het internet is tegenwoordig niet meer weg te denken uit ons dagelijks leven, maar hoe werkt het eigenlijk? <strong>Ten eerste</strong> worden alle websites, filmpjes en games die je bekijkt opgeslagen op gigantische computers die we servers noemen. Wanneer je een website opent, stuurt jouw telefoon een digitaal verzoek via kabels onder de grond of door de lucht naar zo'n server. <strong>Daardoor</strong> reizen de gegevens met bijna de snelheid van het licht terug naar jouw scherm, <strong>omdat</strong> glasvezelkabels data razendsnel kunnen transporteren. Het internet is dus eigenlijk een gigantisch, wereldwijd netwerk van met elkaar verbonden computers.`,
        questions: [
          {
            id: 97,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "De werking van servers." },
              { key: "B", text: "De werking van internet." },
              { key: "C", text: "Waarom glasvezelkabels zo ontzettend snel data kunnen transporteren." },
              { key: "D", text: "Wereldwijd netwerk van computers." }
            ],
            correct: "B",
            explanation: "Het onderwerp moet in maximaal 4 woorden de hele tekst samenvatten. 'De werking van internet' (4 woorden) is perfect."
          },
          {
            id: 98,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat internet goedkoper moet worden." },
              { key: "B", text: "Informeren, want de schrijver legt uit en deelt feiten over hoe het internet werkt." },
              { key: "C", text: "Activeren, want de schrijver roept op om internetkabels te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een wifi-router." }
            ],
            correct: "B",
            explanation: "De schrijver geeft een duidelijke uitleg en feiten over servers en glasvezelkabels. Het doel is dus informeren."
          },
          {
            id: 99,
            question: "In de tekst staat het signaalwoord 'Daardoor'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want servers zijn erg groot." },
              { key: "B", text: "Opsomming, want er worden meerdere kabels genoemd." },
              { key: "C", text: "Gevolg, want de snelle datareis is het gevolg van de verbinding met de server." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de server opstart." }
            ],
            correct: "C",
            explanation: "'Daardoor' geeft het gevolg aan (spiekbriefje: 'Dus, daardoor, daarom')."
          },
          {
            id: 100,
            question: "In welke optie is de definitie van servers juist geciteerd?",
            options: [
              { key: "A", text: "De websites worden opgeslagen op grote computers die servers heten." },
              { key: "B", text: "“gigantische computers die we servers noemen”" },
              { key: "C", text: "“servers”" },
              { key: "D", text: "Servers slaan al onze websites en video's op." }
            ],
            correct: "B",
            explanation: "Optie B citeert de definitie letterlijk met de juiste aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 26: Boeken zijn beter dan films!",
        goal: "Overtuigen",
        text: `Het is werkelijk zonde dat steeds minder jongeren boeken lezen en in plaats daarvan urenlang naar films en series kijken. Lezen is namelijk vele malen beter voor je dan tv-kijken. <strong>Ten eerste</strong> prikkelt een boek je eigen fantasie veel meer, omdat je zelf de personages en de omgeving moet inbeelden. Bij een film wordt alles al voor je ingevuld door de regisseur. <strong>Bovendien</strong> vergroot lezen je woordenschat en taalvaardigheid, wat je helpt bij al je andere schoolvakken. <strong>Hoewel</strong> films kijken heel ontspannend kan zijn, is een goed boek lezen een veel rijkere ervaring voor je brein. We moeten <strong>daarom</strong> vaker die afstandsbediening wegleggen en een goed boek openslaan!`,
        questions: [
          {
            id: 101,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Boeken lezen vergroot je woordenschat en helpt bij andere schoolvakken." },
              { key: "B", text: "Boeken zijn beter dan films omdat ze je fantasie en taalvaardigheid stimuleren." },
              { key: "C", text: "Regisseurs vullen bij films al alle personages en omgevingen voor je in." },
              { key: "D", text: "Jongeren moeten stoppen met series kijken en vaker naar de bibliotheek gaan." }
            ],
            correct: "B",
            explanation: "De hoofdgedachte is dat boeken beter zijn dan films vanwege de voordelen voor fantasie en taalvaardigheid (B)."
          },
          {
            id: 102,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft biologische definities van het brein." },
              { key: "B", text: "Overtuigen, want de schrijver deelt een sterke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om direct een specifiek boek te bestellen." },
              { key: "D", text: "Amuseren, want het is een grappig stripverhaal over een pratend boek." }
            ],
            correct: "B",
            explanation: "De schrijver verdedigt zijn mening ('zonde dat...', 'beter voor je') met argumenten. Het doel is overtuigen."
          },
          {
            id: 103,
            question: "In de tekst staat het signaalwoord 'Hoewel'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het stelt de ontspanning van films tegenover de rijkdom van boeken." },
              { key: "B", text: "Opsomming, want films kijken is ook heel erg leuk." },
              { key: "C", text: "Reden, want het brein wordt er actief van." },
              { key: "D", text: "Vergelijking, want films worden vergeleken met boeken." }
            ],
            correct: "A",
            explanation: "'Hoewel' staat op het spiekbriefje onder <strong>Tegenstelling</strong>."
          },
          {
            id: 104,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is werkelijk zonde dat steeds minder jongeren boeken lezen." },
              { key: "B", text: "Lezen is namelijk vele malen beter voor je dan tv-kijken." },
              { key: "C", text: "Er is geen kernzin te vinden in deze zinnen." },
              { key: "D", text: "We moeten daarom vaker die afstandsbediening wegleggen." }
            ],
            correct: "B",
            explanation: "De tweede zin stelt heel duidelijk de stelling en hoofdzaak van de alinea vast, die daarna met argumenten wordt onderbouwd."
          }
        ]
      },
      {
        title: "Tekst 27: Word lid van de bibliotheek!",
        goal: "Activeren",
        text: `Wist je dat lezen niet alleen goed is voor je brein, maar dat je er ook nog eens gratis duizenden verhalen mee kunt ontdekken? De bibliotheek heeft speciaal voor jongeren een geweldig aanbod! <strong>Hoewel</strong> veel mensen denken dat de bieb saai of ouderwets is, vind je er tegenwoordig de nieuwste strips, games en e-books. <strong>Bovendien</strong> is het lidmaatschap for jongeren onder de achttien jaar helemaal gratis! <strong>Dus</strong> kom vandaag nog in actie! Ga naar de website van de bibliotheek of loop even binnen om je gratis pasje op te halen. Begin <strong>wanneer</strong> je pas binnen is direct met het ontdekken van je favoriete boeken en game-avonturen!`,
        questions: [
          {
            id: 105,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft de openingstijden van de bieb." },
              { key: "B", text: "Activeren, want de schrijver spoort je aans om direct lid te worden van de bibliotheek." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat de bibliotheek groter wordt." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een boekenwurm." }
            ],
            correct: "B",
            explanation: "De schrijver spoort de lezer actief aan: 'kom vandaag nog in actie!', 'Ga naar de website...', 'loop even binnen...'"
          },
          {
            id: 106,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Strips en gratis e-books." },
              { key: "B", text: "Lid worden van bieb." },
              { key: "C", text: "Waarom de bibliotheek voor jongeren onder de achttien gratis is." },
              { key: "D", text: "Games en pasjes ophalen." }
            ],
            correct: "B",
            explanation: "Het onderwerp omschrijft in maximaal 4 woorden de hele tekst: 'Lid worden van bieb.' (4 woorden)."
          },
          {
            id: 107,
            question: "In de tekst staat het signaalwoord 'Dus'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want de bieb is niet ouderwets." },
              { key: "B", text: "Opsomming, want er worden strips opgesomd." },
              { key: "C", text: "Gevolg of conclusie, want de oproep om actie te voeren volgt logisch uit de voordelen." },
              { key: "D", text: "Vergelijking, want strips worden vergeleken met games." }
            ],
            correct: "C",
            explanation: "Het woord 'dus' staat onder <strong>Gevolg</strong> op het spiekbriefje en trekt de conclusie."
          },
          {
            id: 108,
            question: "In welke van de onderstaande opties is de gratis toegang voor jongeren juist geciteerd?",
            options: [
              { key: "A", text: "Jongeren onder de 18 hoeven niets te betalen." },
              { key: "B", text: "“lidmaatschap voor jongeren onder de achttien jaar helemaal gratis!”" },
              { key: "C", text: "“helemaal gratis!”" },
              { key: "D", text: "Lidmaatschap is onder de achttien jaar gratis." }
            ],
            correct: "B",
            explanation: "Optie B citeert de volledige zin letterlijk met aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 28: De robot die te veel wilde helpen",
        goal: "Amuseren",
        text: `Sander kocht gisteren een hypermoderne hulp-robot genaamd Robby om zijn kamer op te ruimen. <strong>Eerst</strong> ging alles perfect: Robby vouwde zijn kleren netjes op en zette zijn boeken keurig in de kast. <strong>Maar</strong> toen Sander vroeg om zijn bed op te maken, sloegen Robbys stoppen door. De robot tilde met zijn metalen armen het hele bed op, liep ermee naar het raam en gooide het bed zo de tuin in! <strong>Daarna</strong> keek Robby hem met knipperende rode ogen aan en riep: "Kamer is nu volledig opgeruimd!". Sander kon zijn ogen niet geloven; hij moest die nacht noodgedwongen in een slaapzak op het gras slapen.`,
        questions: [
          {
            id: 109,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat robots verboden moeten worden." },
              { key: "B", text: "Informeren, want de schrijver geeft instructies om een robot te programmeren." },
              { key: "C", text: "Amuseren, want het is een grappig en fictief verhaal om de lezer te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een Robby koopt." }
            ],
            correct: "C",
            explanation: "Het is een humoristisch en fictief verhaal over een robot die op hol slaat. Het doel is amuseren."
          },
          {
            id: 110,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want Robby is kapot." },
              { key: "B", text: "Opsomming, want Robby heeft ook kleren opgevouwen." },
              { key: "C", text: "Tijd, want het geeft aan wat er gebeurde nadat het bed in de tuin was gegooid." },
              { key: "D", text: "Gevolg, want het bed ligt in de tuin." }
            ],
            correct: "C",
            explanation: "'Daarna' geeft de volgorde van de gebeurtenissen in de tijd aan."
          },
          {
            id: 111,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Sander en zijn bed." },
              { key: "B", text: "Op hol geslagen robot." },
              { key: "C", text: "Waarom robots kopen voor je kamer opruimen heel erg gevaarlijk is." },
              { key: "D", text: "Slapen in de tuin." }
            ],
            correct: "B",
            explanation: "Het onderwerp omschrijft in maximaal 4 woorden de hele tekst: 'Op hol geslagen robot.' (4 woorden)."
          },
          {
            id: 112,
            question: "Welke leesstrategie gebruik je als je snel alleen de eerste en de laatste alinea/zinnen leest om de hoofdlijn te snappen?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "B",
            explanation: "Globaal lezen houdt in dat je de eerste en laatste gedeelten leest om snel de grote lijn te begrijpen."
          }
        ]
      }
    ]
  },
  {
    examId: 8,
    examTitle: "Sınav 8: Milieu & Klimaat",
    texts: [
      {
        title: "Tekst 29: Waarom smelten de gletsjers?",
        goal: "Informeren",
        text: `Gletsjers zijn enorme ijsmassa's die gedurende duizenden jaren zijn gevormd op de koudste plekken op aarde. <strong>Ten eerste</strong> spelen gletsjers een cruciale rol in ons klimaat, omdat ze zonlicht terugkaatsen in de ruimte en de aarde zo koel houden. <strong>Daardoor</strong> stijgt de zeespiegel momenteel wereldwijd in een alarmerend tempo, <strong>omdat</strong> de gletsjers door de opwarming van de aarde steeds sneller wegsmelten. Wetenschappers waarschuwen dat we nu actie moeten ondernemen om deze prachtige ijsreuzen te beschermen voor de toekomst.`,
        questions: [
          {
            id: 113,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Het smelten van gletsjers." },
              { key: "B", text: "Waarom gletsjers zo belangrijk zijn voor het koel houden van onze planeet." },
              { key: "C", text: "Opwarming van de aarde." },
              { key: "D", text: "Stijging van de zeespiegel." }
            ],
            correct: "A",
            explanation: "Het onderwerp is in 4 woorden: 'Het smelten van gletsjers' (4 woorden)."
          },
          {
            id: 114,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver wil dat je vegetariër wordt." },
              { key: "B", text: "Informeren, want de schrijver geeft wetenschappelijke uitleg en feiten over gletsjers." },
              { key: "C", text: "Activeren, want de schrijver wil dat je direct zonnepanelen koopt." },
              { key: "D", text: "Amuseren, want het is een spannend sprookje over ijskoningen." }
            ],
            correct: "B",
            explanation: "De schrijver geeft wetenschappelijke feiten over de werking en het smelten van gletsjers. Het doel is dus informeren."
          },
          {
            id: 115,
            question: "In de tekst staat het signaalwoord 'omdat'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want ijs is koud en de aarde warmt op." },
              { key: "B", text: "Opsomming, want er smelten meerdere gletsjers." },
              { key: "C", text: "Reden/oorzaak, want het legt de reden uit waarom de gletsjers smelten (de opwarming)." },
              { key: "D", text: "Vergelijking, want smelten wordt vergeleken met ijs." }
            ],
            correct: "C",
            explanation: "'Omdat' geeft de reden of oorzaak aan."
          },
          {
            id: 116,
            question: "In welke optie is de rol van gletsjers in ons klimaat juist geciteerd?",
            options: [
              { key: "A", text: "Gletsjers houden de aarde lekker koel." },
              { key: "B", text: "“spelen gletsjers een cruciale rol in ons klimaat”" },
              { key: "C", text: "“cruciale rol”" },
              { key: "D", text: "Gletsjers spelen een heel erg grote rol in ons klimaat." }
            ],
            correct: "B",
            explanation: "Optie B citeert de zin letterlijk en correct."
          }
        ]
      },
      {
        title: "Tekst 30: Vlees eten moet duurder worden!",
        goal: "Overtuigen",
        text: `Het is eigenlijk onbegrijpelijk dat de prijzen van vlees in de supermarkt nog steeds zo belachelijk laag zijn. De massale productie van vlees heeft namelijk een rampzalige invloed op onze planeet. <strong>Ten eerste</strong> stoot de veehouderij gigantische hoeveelheden broeikasgassen uit, wat de opwarming van de aarde enorm versnelt. <strong>Bovendien</strong> kost het produceren van één kilo rundvlees duizenden liters schaars drinkwater. <strong>Hoewel</strong> vleeseters beweren dat goedkoop vlees een recht is voor iedereen, moeten we inzien dat de werkelijke prijs voor het milieu veel hoger ligt. De overheid moet <strong>daarom</strong> snel een vleestaks invoeren om de consumptie te verminderen!`,
        questions: [
          {
            id: 117,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Het produceren van rundvlees kost heel veel liters schaars drinkwater." },
              { key: "B", text: "De overheid moet vlees duurder maken via een vleestaks om het milieu te beschermen." },
              { key: "C", text: "Vleeseters vinden dat goedkoop vlees een recht is voor alle consumenten." },
              { key: "D", text: "De veehouderij stoot veel broeikasgassen uit die de aarde opwarmen." }
            ],
            correct: "B",
            explanation: "De schrijver pleit voor het duurder maken van vlees via een vleestaks om het milieu te sparen (B)."
          },
          {
            id: 118,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen biologische definities van koelen." },
              { key: "B", text: "Overtuigen, want de schrijver deelt zijn duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een knop om direct een vegetarisch kookboek te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een ontsnapte koe." }
            ],
            correct: "B",
            explanation: "De schrijver geeft zijn mening ('onbegrijpelijk', 'belachelijk') en gebruikt argumenten om de lezer te overtuigen."
          },
          {
            id: 119,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Opsomming, want het voegt een extra milieunadeel (waterverbruik) toe." },
              { key: "B", text: "Tegenstelling, want water stopt de opwarming." },
              { key: "C", text: "Reden, want vlees is erg lekker." },
              { key: "D", text: "Vergelijking, want water wordt vergeleken met broeikasgas." }
            ],
            correct: "A",
            explanation: "Het woord 'bovendien' staat op het spiekbriefje onder <strong>Opsomming</strong>."
          },
          {
            id: 120,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is eigenlijk onbegrijpelijk dat de prijzen van vlees nog steeds zo laag zijn." },
              { key: "B", text: "De massale productie van vlees heeft namelijk een rampzalige invloed op onze planeet." },
              { key: "C", text: "Er is geen kernzin te vinden in deze inleiding." },
              { key: "D", text: "De overheid moet daarom snel een vleestaks invoeren." }
            ],
            correct: "B",
            explanation: "De tweede zin stelt de centrale stelling en hoofdzaak vast, die daarna in de alinea wordt onderbouwd."
          }
        ]
      },
      {
        title: "Tekst 31: Doe het licht uit!",
        goal: "Activeren",
        text: `Wist je dat we in Nederland jaarlijks miljoenen kilowatturen aan elektriciteit verspillen door simpelweg lampen te laten branden in lege kamers? Deze onnodige verspilling is heel makkelijk te stoppen door jou! <strong>Hoewel</strong> het misschien een kleine moeite lijkt, bespaar je hiermee enorm veel CO2-uitstoot. <strong>Bovendien</strong> scheelt het je ouders honderden euro's op de energierekening. <strong>Dus</strong> kom direct in actie! Maak er vanaf vandaag een gewoonte van om altijd het licht uit te doen <strong>wanneer</strong> je een kamer verlaat. Plak kleine herinneringsstickers bij de lichtknoppen en draag direct bij aan een groenere toekomst!`,
        questions: [
          {
            id: 121,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt alleen natuurkundige definities van elektriciteit." },
              { key: "B", text: "Activeren, want de schrijver spoort je actief aan om energie te besparen en het licht uit te doen." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat de stroomprijzen gaan stijgen." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een gloeilamp." }
            ],
            correct: "B",
            explanation: "De schrijver spoort de lezer actief aan: 'kom direct in actie!', 'Maak er een gewoonte van...', 'Plak herinneringsstickers...'"
          },
          {
            id: 122,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Elektriciteit verspillen in lege kamers." },
              { key: "B", text: "Licht uitdoen." },
              { key: "C", text: "Energierekening en CO2-uitstoot." },
              { key: "D", text: "Herinneringsstickers plakken." }
            ],
            correct: "B",
            explanation: "Het onderwerp in maximaal 4 woorden omschrijft waar de tekst over gaat: 'Licht uitdoen' (2 woorden)."
          },
          {
            id: 123,
            question: "In de tekst staat het signaalwoord 'wanneer'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want verlaten is het tegenovergestelde van binnenkomen." },
              { key: "B", text: "Tijd, want het geeft aan op welk moment je de knop moet omdraaien." },
              { key: "C", text: "Reden, want het verlaten is de reden dat de kamer leeg is." },
              { key: "D", text: "Vergelijking, want verlaten wordt vergeleken met licht." }
            ],
            correct: "B",
            explanation: "Het woord 'wanneer' staat op het spiekbriefje onder <strong>Tijd</strong> en geeft het moment aan."
          },
          {
            id: 124,
            question: "In welke optie is de verspilling van stroom juist geciteerd?",
            options: [
              { key: "A", text: "We verspillen miljoenen kilowatturen stroom in lege kamers." },
              { key: "B", text: "“verspillen door simpelweg lampen te laten branden in lege kamers”" },
              { key: "C", text: "“verspillen”" },
              { key: "D", text: "In Nederland wordt er jaarlijks heel veel elektriciteit verspild." }
            ],
            correct: "B",
            explanation: "Optie B citeert de tekst letterlijk en correct."
          }
        ]
      },
      {
        title: "Tekst 32: De windvlaag en de pruik",
        goal: "Amuseren",
        text: `Meneer Van Driel liep vanochtend uiterst deftig over de drukke winkelstraat om een belangrijk zakengesprek te voeren. Hij droeg een prachtige, glanzende pruik om zijn kale hoofd te verbergen. <strong>Eerst</strong> was er geen vuiltje aan de lucht en groette hij vriendelijk de voorbijgangers. <strong>Maar</strong> toen hij de hoek van de straat omsloeg, werd hij verrast door een gigantische, plotselinge windvlaag. De wind greep zijn pruik, trok deze met een harde ruk los en blies de pruik zo over de daken van de huizen! <strong>Daarna</strong> keek iedereen met open mond naar zijn glanzende, spiegelgladde kale hoofd, waarna meneer Van Driel doodsbenauwd zijn aktetas op zijn hoofd hield en snel een winkel in rende. Zelfs de deftigste heren kunnen weleens pech hebben!`,
        questions: [
          {
            id: 125,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat pruiken verboden moeten worden." },
              { key: "B", text: "Informeren, want de schrijver geeft wetenschappelijke feiten over windkracht." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal dat bedoeld is om de lezer te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een pruik gaat kopen." }
            ],
            correct: "C",
            explanation: "Het is een humoristische en grappige anekdote om de lezer te vermaken. Het doel is amuseren."
          },
          {
            id: 126,
            question: "In de tekst staat het signaalwoord 'Maar'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft het contrast aan tussen de rustige start en de plotselinge windvlaag." },
              { key: "B", text: "Opsomming, want er wordt een aktetas toegevoegd." },
              { key: "C", text: "Reden, want meneer Van Driel was erg deftig." },
              { key: "D", text: "Tijd, want het geeft aan hoe laat meneer Van Driel liep." }
            ],
            correct: "A",
            explanation: "'Maar' geeft een contrast of tegenstelling aan (spiekbriefje: 'Maar, toch, echter, hoewel')."
          },
          {
            id: 127,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Meneer Van Driel en zijn zakengesprek." },
              { key: "B", text: "Een weggewaaide pruik." },
              { key: "C", text: "Waarom kale heren deftige pruiken moeten dragen in de winkelstraat." },
              { key: "D", text: "Een glanzende kale kop." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 3 woorden omschrijft de kern van de tekst perfect: 'Een weggewaaide pruik' (3 woorden)."
          },
          {
            id: 128,
            question: "Stel dat je voor het lezen alleen snel naar de titel en het grappige plaatje kijkt om te voorspellen waar de tekst over gaat. Welke leesstrategie gebruik je dan?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "A",
            explanation: "Oriënterend lezen (titel, plaatjes bekijken) gebruik je om snel te voorspellen waar de tekst over gaat."
          }
        ]
      }
    ]
  },
  {
    examId: 9,
    examTitle: "Sınav 9: Sport & Hobby's",
    texts: [
      {
        title: "Tekst 33: De geschiedenis van het skateboarden",
        goal: "Informeren",
        text: `Skateboarden is tegenwoordig een razend populaire sport en zelfs een officieel onderdeel van de Olympische Spelen, maar het begon heel simpel. <strong>Eerst</strong> werd het skateboard in de jaren vijftig uitgevonden door Californische surfers die ook wilden 'surfen' als er geen golven in zee waren. Ze schroefden simpelweg rolschaatswieltjes onder een houten plank. <strong>Daarna</strong> verspreidde de trend zich snel over de hele wereld, <strong>maar</strong> pas in de jaren tachtig ontstond de moderne straatstijl met spectaculaire sprongen en trucs.`,
        questions: [
          {
            id: 129,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "De geschiedenis van skateboarden." },
              { key: "B", text: "Californische surfers en wieltjes." },
              { key: "C", text: "De Olympische Spelen en skateboarden." },
              { key: "D", text: "Moderne straatstijl trucs." }
            ],
            correct: "A",
            explanation: "Het onderwerp in 4 woorden: 'De geschiedenis van skateboarden' (4 woorden)."
          },
          {
            id: 130,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver wil dat je een skateboard koopt." },
              { key: "B", text: "Informeren, want de schrijver geeft historische feiten en uitleg over skateboarden." },
              { key: "C", text: "Activeren, want de schrijver spoort je aan om direct een truc uit te proberen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een skateboardende hond." }
            ],
            correct: "B",
            explanation: "De schrijver geeft historische uitleg en feiten over het ontstaan van skateboarden. Het doel is informeren."
          },
          {
            id: 131,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want surfers zijn anders dan skateboarders." },
              { key: "B", text: "Opsomming, want er worden meerdere trucs genoemd." },
              { key: "C", text: "Tijd, want het geeft de chronologische volgorde van het ontstaan aan." },
              { key: "D", text: "Gevolg, want skateboarden werd er populairder door." }
            ],
            correct: "C",
            explanation: "'Daarna' staat op het spiekbriefje onder <strong>Tijd</strong> en geeft de volgorde aan."
          },
          {
            id: 132,
            question: "In welke optie is de uitvinding van het skateboard juist geciteerd?",
            options: [
              { key: "A", text: "Skateboards werden uitgevonden door rolschaatswieltjes te schroeven." },
              { key: "B", text: "“schroefden simpelweg rolschaatswieltjes onder een houten plank”" },
              { key: "C", text: "“houten plank”" },
              { key: "D", text: "Californische surfers schroefden wieltjes onder een plank." }
            ],
            correct: "B",
            explanation: "Optie B citeert de tekst letterlijk en correct met de juiste aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 34: Sporten moet verplicht worden voor iedereen!",
        goal: "Overtuigen",
        text: `Het is werkelijk zorgwekkend dat steeds meer jongeren een groot deel van hun dag zittend doorbrengen achter schermen. Sporten en bewegen moet verplicht worden gesteld op alle scholen, elke dag opnieuw. <strong>Ten eerste</strong> voorkomt dagelijks sporten ernstige gezondheidsproblemen zoals overgewicht en hartziekten op latere leeftijd. <strong>Bovendien</strong> stimuleert beweging de aanmaak van geluksstoffen in je brein, wat zorgt voor minder stress en betere schoolprestaties. <strong>Hoewel</strong> sommigen beweren dat niet iedereen sporten leuk vindt, zijn er tegenwoordig zoveel verschillende sporten dat er voor iedereen wel iets passends is. De overheid moet <strong>daarom</strong> nu ingrijpen en dagelijkse sporturen invoeren!`,
        questions: [
          {
            id: 133,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Jongeren brengen te veel uren zittend door achter tablets en telefoons." },
              { key: "B", text: "Sporten moet verplicht worden gesteld op alle scholen om de gezondheid te bevorderen." },
              { key: "C", text: "Beweging zorgt for minder stress en betere cijfers op school." },
              { key: "D", text: "Er zijn zoveel verschillende sporten dat iedereen wel een leuke activiteit kan vinden." }
            ],
            correct: "B",
            explanation: "De schrijver verdedigt de stelling dat sporten op scholen verplicht gesteld moet worden (B)."
          },
          {
            id: 134,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt alleen biologische feiten over spieren." },
              { key: "B", text: "Overtuigen, want de schrijver geeft een duidelijke mening met argumenten om je te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om direct sportschoenen te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een gymleraar." }
            ],
            correct: "B",
            explanation: "De schrijver geeft zijn mening ('zorgwekkend', 'verplicht stelt') met argumenten om de lezer te overtuigen."
          },
          {
            id: 135,
            question: "In de tekst staat het signaalwoord 'daarom'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want stress is anders dan geluk." },
              { key: "B", text: "Opsomming, want er worden meerdere scholen genoemd." },
              { key: "C", text: "Gevolg, want het verplichten van sporturen is de conclusie na alle gezondheidsvoordelen." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de sporturen moeten beginnen." }
            ],
            correct: "C",
            explanation: "'Daarom' staat op het spiekbriefje onder <strong>Gevolg</strong> en trekt de conclusie."
          },
          {
            id: 136,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is werkelijk zorgwekkend dat steeds meer jongeren een groot deel van hun dag zittend doorbrengen." },
              { key: "B", text: "Sporten en bewegen moet verplicht worden gesteld op alle scholen, elke dag opnieuw." },
              { key: "C", text: "Er is geen kernzin te vinden in dit deel." },
              { key: "D", text: "De overheid moet daarom nu ingrijpen." }
            ],
            correct: "B",
            explanation: "De tweede zin verwoordt heel krachtig de centrale stelling van de alinea, die daarna met argumenten wordt onderbouwd."
          }
        ]
      },
      {
        title: "Tekst 35: Kom in beweging: Doe mee met de sportclub!",
        goal: "Activeren",
        text: `Verveel jij je ook vaak na schooltijd en wil je graag nieuwe vrienden maken én fitter worden? Onze lokale sportclub biedt jou de ultieme kans om te schitteren! <strong>Hoewel</strong> je misschien denkt dat je niet sportief genoeg bent, zijn onze gezellige trainingen geschikt voor elk niveau. <strong>Bovendien</strong> mag je de eerste drie keer helemaal gratis uitproberen en meedoen. <strong>Dus</strong> kom direct in actie! Meld je vandaag nog aan via onze website en neem je klasgenoten mee <strong>wanneer</strong> de eerste training aanstaande woensdag begint!`,
        questions: [
          {
            id: 137,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt alleen de adressen van alle sportvelden." },
              { key: "B", text: "Activeren, want de schrijver spoort je actief aan om lid te worden van de sportclub." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat de contributie stijgt." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een acrobatische scheidsrechter." }
            ],
            correct: "B",
            explanation: "De schrijver spoort de lezer actief aan: 'kom direct in actie!', 'Meld je vandaag nog aan...', 'neem je klasgenoten mee...'"
          },
          {
            id: 138,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Nieuwe vrienden maken." },
              { key: "B", text: "Lid worden sportclub." },
              { key: "C", text: "Gratis trainingen en woensdagen." },
              { key: "D", text: "Sporten en fit worden." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 3 woorden omschrijft de kern van de tekst perfect: 'Lid worden sportclub' (3 woorden)."
          },
          {
            id: 139,
            question: "In de tekst staat het signaalwoord 'Dus'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want sporten is zwaar." },
              { key: "B", text: "Opsomming, want er worden trainingen genoemd." },
              { key: "C", text: "Gevolg, want de oproep om je aan te melden volgt direct uit de gratis proeflessen." },
              { key: "D", text: "Vergelijking, want contributie wordt vergeleken met gratis." }
            ],
            correct: "C",
            explanation: "'Dus' trekt het logische gevolg of de conclusie (spiekbriefje: 'Dus, daardoor, daarom')."
          },
          {
            id: 140,
            question: "In welke optie is de gratis kennismaking juist geciteerd?",
            options: [
              { key: "A", text: "Je mag de trainingen een paar keer gratis uitproberen." },
              { key: "B", text: "“mag je de eerste drie keer helemaal gratis uitproberen en meedoen”" },
              { key: "C", text: "“helemaal gratis”" },
              { key: "D", text: "De eerste drie keer meedoen is gratis." }
            ],
            correct: "B",
            explanation: "Optie B citeert de zin uit de tekst letterlijk met aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 36: De acrobatische kat",
        goal: "Amuseren",
        text: `Mila besloot vanochtend een video te maken van haar luie kat Minoes om op TikTok te plaatsen. <strong>Eerst</strong> lag Minoes urenlang doodstil te slapen in de zonnigste vensterbank, wat een uiterst saaie video opleverde. <strong>Maar</strong> toen Mila een klein rood laserstipje op de muur scheen, veranderde Minoes in een ware acrobaat. De kat sprong met een driedubbele salto tegen de boekenkast, gleed soepel over de gladde eettafel en belandde met een zachte plof precies in de volle fruitschaal. <strong>Daarna</strong> keek Minoes haar met een slaperige blik aan met een schil van een mandarijn op haar linkeroor. De video ging binnen een dag viraal en Minoes is nu een internetberoemdheid!`,
        questions: [
          {
            id: 141,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt dat alle katten op TikTok moeten." },
              { key: "B", text: "Informeren, want de schrijver deelt wetenschappelijke feiten over lasers." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal over een wilde kat dat bedoeld is om te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een kat gaat kopen." }
            ],
            correct: "C",
            explanation: "Het is een humoristisch en amusant verhaal over een kat die rare sprongen maakt. Het doel is amuseren."
          },
          {
            id: 142,
            question: "In de tekst staat het signaalwoord 'Eerst'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tijd, want het geeft het begin van de chronologische volgorde van Minoes' gedrag aan." },
              { key: "B", text: "Tegenstelling, want slapen is anders dan springen." },
              { key: "C", text: "Gevolg, want Mila begon te filmen." },
              { key: "D", text: "Opsomming, want Minoes deed veel trucs." }
            ],
            correct: "A",
            explanation: "'Eerst' staat op het spiekbriefje onder <strong>Tijd</strong> en duidt het verloop in de tijd aan."
          },
          {
            id: 143,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Minoes en de fruitschaal." },
              { key: "B", text: "Een acrobatische kat." },
              { key: "C", text: "Waarom kattenfilmpjes op TikTok zo ontzettend populair en grappig zijn." },
              { key: "D", text: "Laserstipjes en katten." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 3 woorden omschrijft de kern van de tekst perfect: 'Een acrobatische kat' (3 woorden)."
          },
          {
            id: 144,
            question: "Welke leesstrategie gebruik je als je deze tekst heel nauwkeurig gaat lezen om alle grappige details goed te begrijpen voor een boekbespreking?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "C",
            explanation: "Intensief lezen houdt in dat je de hele tekst heel goed en nauwkeurig leest om alle details te snappen."
          }
        ]
      }
    ]
  },
  {
    examId: 10,
    examTitle: "Sınav 10: Kunst & Cultuur",
    texts: [
      {
        title: "Tekst 37: De geheimen van de Mona Lisa",
        goal: "Informeren",
        text: `Het wereldberoemde schilderij de Mona Lisa, gemaakt door Leonardo da Vinci, trekt jaarlijks miljoenen bezoekers naar het Louvre-museum in Parijs. <strong>Ten eerste</strong> staat het schilderij bekend om haar mysterieuze glimlach, die vanuit elke hoek lijkt te veranderen. <strong>Echter</strong>, het schilderij herbergt nog meer geheimen, <strong>omdat</strong> microscopisch onderzoek heeft aangetoond dat Da Vinci minuscule letters en cijfers in haar ogen heeft geschilderd. Kunsthistorici proberen deze verborgen codes tot op de dag van vandaag te ontcijferen.`,
        questions: [
          {
            id: 145,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Leonardo da Vinci en zijn schilderij in het Louvre-museum te Parijs." },
              { key: "B", text: "Geheimen van Mona Lisa." },
              { key: "C", text: "Mysterieuze verborgen codes." },
              { key: "D", text: "Bezoekers in Parijs." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 4 woorden: 'Geheimen van Mona Lisa' (4 woorden)."
          },
          {
            id: 146,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver wil dat je kunstenaar wordt." },
              { key: "B", text: "Informeren, want de schrijver geeft kunsthistorische feiten en uitleg over het schilderij." },
              { key: "C", text: "Activeren, want de schrijver spoort je aan direct een ticket naar Parijs te kopen." },
              { key: "D", text: "Amuseren, want het is een spannend sprookje over pratende schilderijen." }
            ],
            correct: "B",
            explanation: "De schrijver geeft kunsthistorische feiten en uitleg over de geschilderde letters en de glimlach. Het doel is informeren."
          },
          {
            id: 147,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het stelt de bekende glimlach tegenover de nog onbekende verborgen codes." },
              { key: "B", text: "Opsomming, want er worden meerdere musea genoemd." },
              { key: "C", text: "Reden, want het schilderij is erg oud." },
              { key: "D", text: "Tijd, want het schilderij hangt er al heel erg lang." }
            ],
            correct: "A",
            explanation: "'Echter' geeft een contrast of tegenstelling aan (spiekbriefje: 'Maar, toch, echter, hoewel')."
          },
          {
            id: 148,
            question: "In welke optie is de schilder van de Mona Lisa juist geciteerd?",
            options: [
              { key: "A", text: "De Mona Lisa is geschilderd door Leonardo da Vinci." },
              { key: "B", text: "“de Mona Lisa, gemaakt door Leonardo da Vinci”" },
              { key: "C", text: "“Leonardo da Vinci”" },
              { key: "D", text: "Mona Lisa is gemaakt door een bekende kunstenaar." }
            ],
            correct: "B",
            explanation: "Optie B citeert de tekst letterlijk en correct met aanhalingstekens."
          }
        ]
      },
      {
        title: "Tekst 38: Kunstles op school is essentieel!",
        goal: "Overtuigen",
        text: `Het is werkelijk onbegrijpelijk dat sommige scholen bezuinigen op creatieve vakken zoals tekenen en handvaardigheid om meer tijd te besteden aan rekenen en talen. Creatieve vorming is namelijk onmisbaar voor de ontwikkeling van jongeren. <strong>Ten eerste</strong> stimuleert kunstles je probleemoplossend vermogen en creativiteit, vaardigheden die je bij alle andere vakken en in je latere werk hard nodig hebt. <strong>Bovendien</strong> biedt het een welkome en ontspannende afwisseling na urenlang stilzitten en theorie stampen. <strong>Hoewel</strong> critici beweren dat je van kunstles later geen geld kunt verdienen, bewijst de bloeiende creatieve industrie het tegendeel. Scholen moeten <strong>daarom</strong> direct investeren in creatieve vakken!`,
        questions: [
          {
            id: 149,
            question: "Wat is de hoofdgedachte van deze tekst?",
            options: [
              { key: "A", text: "Scholen bezuinigen tegenwoordig te veel op creatieve vakken zoals tekenen." },
              { key: "B", text: "Creatieve vakken zijn essentieel voor jongeren en moeten behouden en versterkt worden op scholen." },
              { key: "C", text: "Kunstles stimuleert het probleemoplossend vermogen en biedt ontspanning." },
              { key: "D", text: "Critici vinden dat creatieve vakken minder belangrijk zijn dan rekenen en talen." }
            ],
            correct: "B",
            explanation: "De hoofdgedachte is dat creatieve vakken essentieel zijn en scholen hierin moeten investeren (B)."
          },
          {
            id: 150,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft scheikundige definities van verf." },
              { key: "B", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou te overtuigen." },
              { key: "C", text: "Activeren, want er staat een link om direct verfspullen te kopen." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een sprekend schilderij." }
            ],
            correct: "B",
            explanation: "De schrijver verdedigt zijn mening over het belang van kunstles met argumenten om de lezer te overtuigen."
          },
          {
            id: 151,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Opsomming, want het voegt een extra voordeel (ontspanning) toe aan de voordelen van kunstles." },
              { key: "B", text: "Tegenstelling, want ontspanning is anders dan theorie stampen." },
              { key: "C", text: "Reden, want stilzitten is erg vermoeiend." },
              { key: "D", text: "Vergelijking, want tekenen wordt vergeleken met handvaardigheid." }
            ],
            correct: "A",
            explanation: "Het woord 'bovendien' staat op het spiekbriefje onder <strong>Opsomming</strong>."
          },
          {
            id: 152,
            question: "Wat is de kernzin van het eerste deel van de tekst?",
            options: [
              { key: "A", text: "Het is werkelijk onbegrijpelijk dat sommige scholen bezuinigen op creatieve vakken." },
              { key: "B", text: "Creatieve vorming is namelijk onmisbaar voor de ontwikkeling van jongeren." },
              { key: "C", text: "Er is geen kernzin te vinden in deze inleiding." },
              { key: "D", text: "Scholen moeten daarom direct investeren in creatieve vakken!" }
            ],
            correct: "B",
            explanation: "De tweede zin stelt de centrale stelling van de alinea vast, die de basis vormt voor alle argumenten."
          }
        ]
      },
      {
        title: "Tekst 39: Bezoek het museum in de buurt!",
        goal: "Activeren",
        text: `Wist je dat cultuur snuiven in je eigen regio niet alleen ontzettend inspirerend is, maar dat het je ook helpt om de geschiedenis van je eigen omgeving beter te begrijpen? Ons lokale museum heeft een spectaculaire tijdelijke tentoonstelling! <strong>Hoewel</strong> je misschien denkt dat een museum saai is, bewijst de interactieve VR-bril-beleving het tegendeel. <strong>Bovendien</strong> is de toegang voor scholieren onder de achttien jaar dit weekend helemaal gratis! <strong>Dus</strong> kom direct in actie! Bezoek aanstaande zaterdag ons museum en ontdek de geschiedenis op een hypermoderne manier. Neem je vrienden mee <strong>wanneer</strong> je gaat, en beleef een onvergetelijke middag!`,
        questions: [
          {
            id: 153,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt de geschiedenis van alle musea ter wereld." },
              { key: "B", text: "Activeren, want de schrijver spoort je actief aan om het lokale museum te bezoeken." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat de VR-brillen verplicht worden." },
              { key: "D", text: "Amuseren, want het is een grappig verhaal over een pratende ridderuitrusting." }
            ],
            correct: "B",
            explanation: "De schrijver spoort de lezer actief aan tot actie: 'kom direct in actie!', 'Bezoek ons museum...', 'Neem je vrienden mee...'"
          },
          {
            id: 154,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "VR-brillen en geschiedenis." },
              { key: "B", text: "Museumbezoek in buurt." },
              { key: "C", text: "Waarom cultuur snuiven voor scholieren onder de achttien gratis is dit weekend." },
              { key: "D", text: "Samen geschiedenis ontdekken." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 4 woorden omschrijft de kern perfect: 'Museumbezoek in buurt' (4 woorden)."
          },
          {
            id: 155,
            question: "In de tekst staat het signaalwoord 'wanneer'. Welk tekstverband geeft dit aan?",
            options: [
              { key: "A", text: "Tegenstelling, want zaterdag is anders dan woensdag." },
              { key: "B", text: "Tijd, want het geeft aan op welk moment je de knop moet omdraaien." },
              { key: "C", text: "Reden, want het weekend is de reden dat het gratis is." },
              { key: "D", text: "Vergelijking, want geschiedenis wordt vergeleken met VR." }
            ],
            correct: "B",
            explanation: "'Wanneer' staat op het spiekbriefje onder <strong>Tijd</strong> en duidt het moment aan."
          },
          {
            id: 156,
            question: "In welke optie is de gratis toegang voor scholieren juist geciteerd?",
            options: [
              { key: "A", text: "Scholieren onder de 18 jaar hoeven dit weekend niets te betalen." },
              { key: "B", text: "“toegang voor scholieren onder de achttien jaar dit weekend helemaal gratis!”" },
              { key: "C", text: "“helemaal gratis!”" },
              { key: "D", text: "Dit weekend is het museum gratis voor alle jongeren." }
            ],
            correct: "B",
            explanation: "Optie B citeert de zin letterlijk en correct."
          }
        ]
      },
      {
        title: "Tekst 40: Het schilderij dat ondersteboven hing",
        goal: "Amuseren",
        text: `De beroemde kunstenaar Jean-Luc hield gisteravond een chique opening van zijn nieuwe tentoonstelling in de stad. <strong>Eerst</strong> was hij dolblij met alle lovende reacties van de kunstkenners, die urenlang diepzinnig stonden te praten bij zijn nieuwste abstracte meesterwerk. <strong>Maar</strong> toen de schoonmaker aan het eind van de avond langskwam om de glazen op te ruimen, ging het gruwelijk mis. De schoonmaker keek verbaasd naar de handtekening en zei droog: "Mooi schilderij hoor, maar waarom hangt het eigenlijk ondersteboven?". <strong>Daarna</strong> werd het doodstil in de zaal, waarna Jean-Luc vuurrood aanliep en de kenners beschaamd naar hun voeten keken. Het was een enorme blunder, al konden ze er achteraf bij de borrel wel hartelijk om lachen.`,
        questions: [
          {
            id: 157,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver vindt abstracte kunst stom." },
              { key: "B", text: "Informeren, want de schrijver legt uit hoe je verf mengt." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal over een kunstblunder om te vermaken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct een schilderij koopt." }
            ],
            correct: "C",
            explanation: "Het is een grappig verhaal over een abstract schilderij dat per ongeluk ondersteboven hing. Het doel is amuseren."
          },
          {
            id: 158,
            question: "In de tekst staat het signaalwoord 'Maar'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft het contrast aan tussen de complimenten vooraf en de blunder daarna." },
              { key: "B", text: "Opsomming, want er worden borrels opgesomd." },
              { key: "C", text: "Reden, want de schoonmaker wilde opruimen." },
              { key: "D", text: "Tijd, want de borrel was achteraf." }
            ],
            correct: "A",
            explanation: "'Maar' duidt op een contrast of tegenstelling (spiekbriefje: 'Maar, toch, echter, hoewel')."
          },
          {
            id: 159,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Jean-Luc en de schoonmaker." },
              { key: "B", text: "Een ondersteboven hangend schilderij." },
              { key: "C", text: "Waarom chique kunstkenners soms heel erg dom uit hun ogen kunnen kijken." },
              { key: "D", text: "Abstracte kunst en blunders." }
            ],
            correct: "B",
            explanation: "Het onderwerp in 4 woorden: 'Een ondersteboven hangend schilderij' (4 woorden)."
          },
          {
            id: 160,
            question: "Welke leesstrategie gebruik je als je alleen de eerste zin en de laatste alinea/zin leest om snel de kern te snappen?",
            options: [
              { key: "A", text: "Oriënterend lezen" },
              { key: "B", text: "Globaal lezen" },
              { key: "C", text: "Intensief lezen" },
              { key: "D", text: "Zoekend lezen" }
            ],
            correct: "B",
            explanation: "Globaal lezen houdt in dat je de inleiding en het slot (eerste en laatste zinnen/alinea's) bekijkt voor de hoofdlijnen."
          }
        ]
      }
    ]
  },
  {
    examId: 11,
    examTitle: "Sınav 11: Klimaatverandering",
    texts: [
      {
        title: "Tekst 41: De opwarming van de aarde",
        goal: "Informeren",
        text: `De gemiddelde temperatuur op aarde stijgt de laatste decennia in een alarmerend tempo. <strong>Ten eerste</strong> komt dit door de enorme hoeveelheid broeikasgassen, zoals CO2, die we door het verbranden van fossiele brandstoffen uitstoten. Deze gassen vormen een deken om de aarde, <strong>waardoor</strong> de warmte van de zon niet meer weg kan. <strong>Echter</strong>, ook ontbossing speelt een grote rol, <strong>omdat</strong> bomen juist CO2 uit de lucht opnemen. Wetenschappers hebben gemeten dat de aarde sinds 1880 al met ongeveer 1,2 graden Celsius is opgewarmd. Het is dus van groot belang dat we wereldwijd actie ondernemen om de uitstoot te verminderen, zodat we ergere gevolgen kunnen voorkomen.`,
        questions: [
          {
            id: 161,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de regel uit het spiekbriefje!)",
            options: [
              { key: "A", text: "De geschiedenis van wetenschappelijke metingen sinds het jaar 1880." },
              { key: "B", text: "Opwarming van de aarde." },
              { key: "C", text: "Hoe CO2 een deken om de planeet vormt door fossiele brandstoffen." },
              { key: "D", text: "Bomen kappen." }
            ],
            correct: "B",
            explanation: "Kijk eens naar het <strong>Spiekbriefje</strong> bij het begrip <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('Opwarming van de aarde') bestaat uit 4 woorden en vat de hele tekst perfect samen! Optie A en C zijn veel te lang (meer dan 4 woorden) en optie D is slechts een klein detail en niet waar de héle tekst over gaat."
          },
          {
            id: 162,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Overtuigen, want de schrijver wil dat we allemaal direct lid worden van een milieugroepering." },
              { key: "B", text: "Activeren, want er staat een link om direct geld te doneren aan een goed doel." },
              { key: "C", text: "Informeren, want de schrijver geeft objectieve uitleg en feiten over waarom de temperatuur stijgt." },
              { key: "D", text: "Amuseren, want het is een grappig kerstverhaal over smeltende sneeuwpoppen." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Informeren</em>: 'uitleg / feiten'. De schrijver deelt feiten over broeikasgassen, de stijging van 1,2 graden sinds 1880 en ontbossing. Er wordt geen zware mening opgedrongen of actie geëist, dus is het tekstdoel informeren!"
          },
          {
            id: 163,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit signaalwoord aan?",
            options: [
              { key: "A", text: "Opsomming, want de schrijver voegt nog meer gassen toe aan de lijst." },
              { key: "B", text: "Tegenstelling, omdat het een contrast aangeeft tussen de verschillende oorzaken van de opwarming." },
              { key: "C", text: "Reden/oorzaak, want het legt uit waarom bomen worden gekapt." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de ontbossing precies is begonnen." }
            ],
            correct: "B",
            explanation: "Als je op het <strong>Spiekbriefje</strong> kijkt bij <em>Tekstverbanden + signaalwoorden</em>, zie je 'echter' staan onder het kopje <strong>Tegenstelling</strong> (net als 'maar' en 'hoewel'). De schrijver noemt eerst het verbranden van fossiele brandstoffen als oorzaak, en stelt daar de rol van ontbossing tegenover."
          },
          {
            id: 164,
            question: "In welke van de onderstaande zinnen is er sprake van een juiste, letterlijke citering van de temperatuurstijging sinds 1880?",
            options: [
              { key: "A", text: "De aarde is sinds 1880 al met 1,2 graden Celsius opgewarmd." },
              { key: "B", text: "“Wetenschappers hebben gemeten dat de aarde sinds 1880 al met ongeveer 1,2 graden Celsius is opgewarmd.”" },
              { key: "C", text: "De schrijver vertelt dat de temperatuur sinds het jaartal 1880 is gestegen." },
              { key: "D", text: "“Het is dus van groot belang dat we wereldwijd actie ondernemen”" }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B is letterlijk gekopieerd uit de tekst en staat netjes tussen de juiste aanhalingstekens. Optie A en C hebben geen aanhalingstekens, en optie D citeert wel, maar dat gaat over actie ondernemen en niet over de temperatuurstijging sinds 1880!"
          }
        ]
      },
      {
        title: "Tekst 42: De overstap naar zonne-energie",
        goal: "Overtuigen",
        text: `Het is werkelijk onbegrijpelijk dat nog niet alle daken in Nederland vol liggen met zonnepanelen. We moeten nu massaal overstappen op duurzame energie om onze planeet te redden van de klimaatcrisis. <strong>Ten eerste</strong> zijn zonnepanelen ontzettend goed voor het milieu, <strong>omdat</strong> ze schone stroom opwekken zonder CO2-uitstoot. <strong>Bovendien</strong> verdien je de investering snel terug, <strong>daarom</strong> is het ook nog eens fantastisch voor je eigen portemonnee. <strong>Hoewel</strong> sommigen klagen dat zonnepanelen het uitzicht van huizen verpesten, weegt dit esthetische bezwaar absoluut niet op tegen de gigantische voordelen voor de toekomst van onze kinderen. Iedere huizenbezitter moet nu zijn verantwoordelijkheid nemen en zonnepanelen aanschaffen!`,
        questions: [
          {
            id: 165,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom zonnepanelen goed zijn voor het milieu en je portemonnee." },
              { key: "B", text: "Huizen met zonnepanelen in heel Nederland." },
              { key: "C", text: "Overstap naar zonne-energie." },
              { key: "D", text: "Klimaatcrisis in Nederland." }
            ],
            correct: "C",
            explanation: "Kijk naar het <strong>Spiekbriefje</strong> bij het begrip <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie C ('Overstap naar zonne-energie') bestaat uit exact 4 woorden en dekt de volledige tekst perfect! Optie A is veel te lang, and optie D is veel te algemeen."
          },
          {
            id: 166,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen neutrale, technische specificaties van panelen." },
              { key: "B", text: "Activeren, want er staat een link om direct panelen te bestellen." },
              { key: "C", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou te overtuigen van zonnepanelen." },
              { key: "D", text: "Amuseren, want het is een spannend stripverhaal over een zonnepaneel-superheld." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Overtuigen</em>: 'mening + argumenten'. De schrijver vindt het 'onbegrijpelijk' dat niet iedereen panelen heeft (mening) en noemt argumenten zoals milieuvoordelen en geldbesparing om je over te halen."
          },
          {
            id: 167,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan met het milieu." },
              { key: "B", text: "Opsomming, want de schrijver voegt een extra voordeel (financieel voordeel) toe aan de voordelen van zonnepanelen." },
              { key: "C", text: "Reden/oorzaak, want het legt uit hoe zonne-energie wordt opgeslagen." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de panelen stroom opwekken." }
            ],
            correct: "B",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'bovendien' onder het kopje <strong>Opsomming</strong> staan. De schrijver noemt eerst het milieuvoordeel (schone stroom), en somt daarna een second voordeel op over de portemonnee."
          },
          {
            id: 168,
            question: "In welke optie is de klacht over zonnepanelen juist geciteerd?",
            options: [
              { key: "A", text: "Veel mensen klagen dat zonnepanelen erg lelijk zijn op het dak." },
              { key: "B", text: "“Hoewel sommigen klagen dat zonnepanelen het uitzicht van huizen verpesten”" },
              { key: "C", text: "“esthetische bezwaar absoluut niet opweegt tegen de gigantische voordelen”" },
              { key: "D", text: "Zonnepanelen verpesten het uitzicht van huizen." }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B citeert de zin met de klacht letterlijk uit de tekst met aanhalingstekens. Optie A en D hebben geen aanhalingstekens, en optie C citeert wel, maar dat gaat over de afweging van de bezwaren."
          }
        ]
      },
      {
        title: "Tekst 43: Eet minder vlees!",
        goal: "Activeren",
        text: `Wist je dat de veeteelt verantwoordelijk is voor een enorme hoeveelheid broeikasgassen? Het eten van vlees heeft <strong>daarom</strong> een gigantische impact op het klimaat. <strong>Hoewel</strong> vegetarisch eten soms als een uitdaging wordt gezien, zijn er tegenwoordig heerlijke alternatieven beschikbaar. <strong>Bovendien</strong> is een plantaardig dieet ook nog eens hartstikke gezond voor je lichaam! <strong>Dus</strong> kom vandaag nog in actie voor ons klimaat! Probeer deze week minstens drie days vegetarisch te eten. Schrap die hamburger van je menu en kies voor een lekkere linzenburger of vegetarische pasta. Doe nu mee met de 'Veggie Challenge' en verklein direct jouw ecologische voetafdruk. Samen kunnen we het verschil maken, begin vanavond al bij het avondeten!`,
        questions: [
          {
            id: 169,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom minder vlees eten goed is voor de opwarming van de aarde." },
              { key: "B", text: "Minder vlees eten." },
              { key: "C", text: "De Veggie Challenge en linzenburgers." },
              { key: "D", text: "Plantaardige diëten in Nederland." }
            ],
            correct: "B",
            explanation: "Volgens het <strong>Spiekbriefje</strong> moet het <em>Onderwerp</em> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Minder vlees eten' (3 woorden) vat de kern van de hele tekst perfect samen! De andere opties zijn te lang of missen het hoofdonderwerp."
          },
          {
            id: 170,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver deelt alleen biologische feiten over de veeteelt." },
              { key: "B", text: "Amuseren, want het is een grappig verhaal over een sprekende koe." },
              { key: "C", text: "Activeren, want de schrijver spoort je actief aan om direct minder vlees te eten en mee te doen aan een challenge." },
              { key: "D", text: "Overtuigen, want de schrijver wil dat je een eigen moestuin begint." }
            ],
            correct: "C",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Activeren</em>: 'Je iets laten doen'. De schrijver spoort de lezer heel direct aan tot actie: 'kom vandaag nog in actie!', 'Probeer deze week...', 'Doe nu mee...' Het doel is dus activeren!"
          },
          {
            id: 171,
            question: "In de tekst staat het signaalwoord 'Dus'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want het geeft een contrast aan met vlees." },
              { key: "B", text: "Reden/oorzaak, want het legt uit hoe broeikasgassen ontstaan." },
              { key: "C", text: "Gevolg, omdat het de logische conclusie trekt dat we in actie moeten komen op basis van de eerdere feiten." },
              { key: "D", text: "Opsomming, want het voegt nog een voordeel toe aan vegetarisch eten." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je 'dus' staan onder het kopje <strong>Gevolg/conclusie</strong>. De schrijver noemt de impact van vlees, en trekt daaruit de conclusie: DUS kom in actie!"
          },
          {
            id: 172,
            question: "In welke optie is de impact van vlees op het klimaat juist geciteerd?",
            options: [
              { key: "A", text: "Het eten van vlees heeft daarom een gigantische impact op het klimaat." },
              { key: "B", text: "“Het eten van vlees heeft daarom een gigantische impact op het klimaat.”" },
              { key: "C", text: "De schrijver zegt dat vlees eten heel erg slecht is voor de opwarming van de aarde." },
              { key: "D", text: "“Wist je dat de veeteelt verantwoordelijk is voor een enorme hoeveelheid broeikasgassen?”" }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B citeert de zin over de impact van vlees eten letterlijk uit de tekst met aanhalingstekens. Optie A en C hebben geen aanhalingstekens, en optie D citeert wel, maar dat gaat over broeikasgassen uit veeteelt en niet direct over vleesconsumptie."
          }
        ]
      },
      {
        title: "Tekst 44: De ijsbeer en de smeltende gletsjer",
        goal: "Amuseren",
        text: `Het was een ijskoude ochtend op de Noordpool toen de jonge ijsbeer Lars geeuwend wakker werd. <strong>Eerst</strong> rekte hij zich eens flink uit, klaar voor een heerlijke dag spelen in de sneeuw. <strong>Maar</strong> toen hij zijn eerste stap buiten zijn hol zette, gleed hij met een luide plons het ijskoude zeewater in. De gletsjer waarop zijn hol stond, was door de stijgende temperatuur vannacht geruisloos in tweeën gespleten! <strong>Daarna</strong> krabbelde hij geschrokken op een klein drijvend ijsschotsje, terwijl een groep voorbijzwemmende zeehonden hem luidruchtig uitlachte. Lars keek sip naar zijn natte vacht en besloot dat hij voortaan toch maar beter eerst kon kijken waar hij liep. Uiteindelijk kon hij er met zijn moeder wel om lachen toen hij weer veilig thuis was.`,
        questions: [
          {
            id: 173,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "De avonturen van de jonge ijsbeer Lars op de smeltende Noordpool." },
              { key: "B", text: "Lars en de gletsjer." },
              { key: "C", text: "Waarom gletsjers smelten op de Noordpool door de opwarming van de aarde." },
              { key: "D", text: "Spelende ijsberen in de sneeuw." }
            ],
            correct: "B",
            explanation: "Het <em>Onderwerp</em> moet volgens het <strong>Spiekbriefje</strong> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Lars en de gletsjer' (4 woorden) is perfect! De andere opties zijn te lang of missen het hoofdonderwerp."
          },
          {
            id: 174,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want het is een wetenschappelijke tekst over gletsjerverschuivingen." },
              { key: "B", text: "Overtuigen, want de schrijver wil dat we ijsberen gaan adopteren." },
              { key: "C", text: "Activeren, want de schrijver wil dat je direct naar de Noordpool reist." },
              { key: "D", text: "Amuseren, want het is een grappig, verzonnen verhaal over de avonturen van Lars de ijsbeer." }
            ],
            correct: "D",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Amuseren</em>: 'verhaal / vermaken'. Deze tekst is een leuk en een beetje grappig verhaal over Lars de ijsbeer die in het water valt. Het is geschreven om de lezer te vermaken!"
          },
          {
            id: 175,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want Lars is nat geworden." },
              { key: "B", text: "Tijd, want het geeft de chronologische volgorde van Lars' avontuur aan." },
              { key: "C", text: "Reden, want de zeehonden lachten hem uit." },
              { key: "D", text: "Vergelijking, want Lars wordt vergeleken met een zeehond." }
            ],
            correct: "B",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'daarna' onder het kopje <strong>Tijd</strong>. Het geeft aan in welke volgorde de gebeurtenissen plaatsvinden: eerst valt Lars in het water, en DAARNA krabbelt hij op een ijsschots."
          },
          {
            id: 176,
            question: "In welke optie is de schrik van Lars juist geciteerd?",
            options: [
              { key: "A", text: "Lars schrok heel erg toen hij in het koude water viel." },
              { key: "B", text: "“Daarna krabbelde hij geschrokken op een klein drijvend ijsschotsje”" },
              { key: "C", text: "“Uiteindelijk kon hij er met zijn moeder wel om lachen”" },
              { key: "D", text: "Lars krabbelde snel op een klein ijsschotsje." }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B citeert de zin waarin hij geschrokken op de ijsschots klimt letterlijk uit de tekst met aanhalingstekens. Optie A en D hebben geen aanhalingstekens, en optie C citeert een andere zin."
          }
        ]
      }
    ]
  },
  {
    examId: 12,
    examTitle: "Sınav 12: Eten & Wereldkeuken",
    texts: [
      {
        title: "Tekst 45: De geheimen van sushi",
        goal: "Informeren",
        text: `Wanneer je aan sushi denkt, denk je waarschijnlijk aan verse rauwe vis en rijst uit Japan. <strong>Ten eerste</strong> was sushi vroeger echter helemaal geen luxe snack, maar een manier om vis langer te kunnen bewaren door het in gefermenteerde rijst te wikkelen. De zure rijst zorgde ervoor dat de vis niet bedierf, <strong>waardoor</strong> men de rijst daarna gewoon weggooide. <strong>Echter</strong>, in de negentiende eeuw veranderde dit in de stad Edo, het huidige Tokio. Chef Hanaya Yohei bedacht dat het veel sneller en lekkerder was om verse vis op een klein blokje rijst met azijn te serveren. Dit was de geboorte van de moderne 'nigiri'. Tegenwoordig eten mensen over de hele wereld sushi als een gezonde en heerlijke delicatesse.`,
        questions: [
          {
            id: 177,
            question: "Wat is het onderwerp van deze tekst? (Denk aan de regel uit het spiekbriefje!)",
            options: [
              { key: "A", text: "De geschiedenis van Hanaya Yohei en de nigiri-sushi in de stad Edo." },
              { key: "B", text: "Hoe Japanners in de negentiende eeuw vis leerden bewaren in zure rijst." },
              { key: "C", text: "De geschiedenis van sushi." },
              { key: "D", text: "Rauwe vis in Japan." }
            ],
            correct: "C",
            explanation: "Kijk eens naar het <strong>Spiekbriefje</strong> bij het begrip <em>Onderwerp</em>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie C ('De geschiedenis van sushi') bestaat uit exact 4 woorden en dekt de hele tekst perfect! Optie A en B zijn veel te lang (meer dan 4 woorden), en optie D noemt alleen een klein detail en is niet het hoofdonderwerp."
          },
          {
            id: 178,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft objectieve uitleg en feiten over het ontstaan en de geschiedenis van sushi." },
              { key: "B", text: "Overtuigen, want de schrijver probeert jou over te halen om vanavond sushi te gaan bestellen." },
              { key: "C", text: "Activeren, want de schrijver roept je op om direct zelf sushi te gaan rollen in de keuken." },
              { key: "D", text: "Amuseren, want het is een grappig, fictief sprookje over pratende vissen in de zee." }
            ],
            correct: "A",
            explanation: "Op ons <strong>Spiekbriefje</strong> staat bij <em>Informeren</em>: 'uitleg / feiten'. De schrijver legt je uit hoe sushi vroeger werd gemaakt om vis te bewaren, wie de moderne sushi heeft uitgevonden (Hanaya Yohei) en hoe het zich heeft ontwikkeld. Er is geen mening of oproep tot actie, dus is het doel informeren!"
          },
          {
            id: 179,
            question: "In de tekst staat het signaalwoord 'Echter'. Welk tekstverband geeft dit signaalwoord aan?",
            options: [
              { key: "A", text: "Opsomming, want de schrijver voegt een extra ingrediënt toe aan de rijst." },
              { key: "B", text: "Tegenstelling, omdat het een contrast aangeeft tussen de oude bewaarmethode en de nieuwe manier van sushi eten in de negentiende eeuw." },
              { key: "C", text: "Reden/oorzaak, want het verklaart waarom men de gefermenteerde rijst vroeger weggooide." },
              { key: "D", text: "Tijd, want het geeft aan hoe laat de moderne sushi werd gegeten." }
            ],
            correct: "B",
            explanation: "Kijk op je <strong>Spiekbriefje</strong> bij <em>Tekstverbanden</em>: 'echter' hoort bij een <strong>Tegenstelling</strong> (samen met maar, toch en hoewel). De tekst stelt de oude methode van sushi maken (rijst weggooien) tegenover de nieuwe, negentiende-eeuwse methode (rijst juist opeten). Een duidelijke tegenstelling dus!"
          },
          {
            id: 180,
            question: "In welke van de onderstaande opties is er sprake van een juiste, letterlijke citering over de uitvinder van de nigiri-sushi?",
            options: [
              { key: "A", text: "Chef Hanaya Yohei bedacht de moderne nigiri in Edo." },
              { key: "B", text: "“Chef Hanaya Yohei bedacht dat het veel sneller en lekkerder was om verse vis op een klein blokje rijst met azijn te serveren.”" },
              { key: "C", text: "De schrijver vertelt dat een chef genaamd Hanaya Yohei de uitvinder is." },
              { key: "D", text: "“Tegenwoordig eten mensen over de hele wereld sushi als een gezonde en heerlijke delicatesse.”" }
            ],
            correct: "B",
            explanation: "Herinner je de regel voor <strong>Citeren</strong> van je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B is letterlijk gekopieerd uit de tekst en staat keurig tussen aanhalingstekens. Optie A en C hebben geen aanhalingstekens, en optie D citeert wel, maar dat gaat over sushi over de hele wereld, niet over de uitvinder van nigiri!"
          }
        ]
      },
      {
        title: "Tekst 46: Red de lokale eetcultuur!",
        goal: "Overtuigen",
        text: `Het is buitengewoon zonde dat authentieke, lokale restaurants steeds vaker moeten sluiten door de opkomst van gigantische, wereldwijde fastfoodketens. We verliezen hierdoor onze unieke eetcultuur en dat is een verschrikkelijke ontwikkeling. <strong>Ten eerste</strong> gebruiken lokale eethuisjes vaak verse, gezonde ingrediënten uit de eigen regio, <strong>waardoor</strong> ze de lokale boeren steunen en het milieu sparen. <strong>Bovendien</strong> vertellen hun gerechten een verhaal over traditie en liefde voor het vak, iets wat een smaakloze hamburgerfabriek nooit kan bieden. <strong>Hoewel</strong> fastfoodketens goedkoper en sneller zijn, weegt dit gemak absoluut niet op tegen het verlies van onze culturele identiteit en gezonde voeding. We moeten onze lokale ondernemers steunen om deze culinaire rijkdom te behouden!`,
        questions: [
          {
            id: 181,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom grote fastfoodketens heel erg slecht zijn voor de gezondheid en cultuur." },
              { key: "B", text: "Behoud van lokale restaurants." },
              { key: "C", text: "Het verlies van onze culturele identiteit door smaakloze hamburgers." },
              { key: "D", text: "Gezonde ingrediënten van lokale boeren." }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <em>Onderwerp</em> op je <strong>Spiekbriefje</strong>: 'Waar de tekst over gaat, Max. 4 woorden'. Optie B ('Behoud van lokale restaurants') is exact 4 woorden en omschrijft de kern van de hele tekst perfect! De andere opties zijn te lang (meer dan 4 woorden) of belichten slechts een klein detail."
          },
          {
            id: 182,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen wetenschappelijke statistieken over faillissementen van horecabedrijven." },
              { key: "B", text: "Amuseren, want het is een komisch verhaal over een mislukt diner in een chic restaurant." },
              { key: "C", text: "Activeren, want de schrijver geeft een link naar een petitie om fastfoodketens te verbieden." },
              { key: "D", text: "Overtuigen, want de schrijver geeft zijn duidelijke mening met argumenten om jou ervan te overtuigen lokale restaurants te steunen." }
            ],
            correct: "D",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Overtuigen</em> staat: 'mening + argumenten'. De schrijver vindt het sluiten van lokale eethuisjes 'buitengewoon zonde' (mening) en geeft argumenten ('verse ingrediënten', 'steunen van boeren', 'behoud van traditie') om jou te overtuigen van zijn standpunt."
          },
          {
            id: 183,
            question: "In de tekst staat het signaalwoord 'Bovendien'. Welk tekstverband hoort hierbij?",
            options: [
              { key: "A", text: "Tegenstelling, want het laat het verschil zien tussen hamburgers en gezonde voeding." },
              { key: "B", text: "Opsomming, omdat de schrijver na het argument over verse ingrediënten nog een extra argument (traditie en liefde) toevoegt." },
              { key: "C", text: "Reden/oorzaak, want het legt uit waarom fastfoodketens zo goedkoop kunnen zijn." },
              { key: "D", text: "Tijd, want het geeft aan wanneer de restaurants moeten sluiten." }
            ],
            correct: "B",
            explanation: "Als je op het <strong>Spiekbriefje</strong> kijkt bij <em>Tekstverbanden</em>, zie je 'bovendien' onder het kopje <strong>Opsomming</strong> staan. De schrijver somt argumenten op waarom we lokale restaurants moeten steunen: eerst noemt hij de verse ingrediënten, en daarna voegt hij daar nog een argument aan toe."
          },
          {
            id: 184,
            question: "In welke optie is de vergelijking met fastfoodketens juist geciteerd?",
            options: [
              { key: "A", text: "“Hoewel fastfoodketens goedkoper en sneller zijn, weegt dit gemak absoluut niet op tegen het verlies van onze culturele identiteit en gezonde voeding.”" },
              { key: "B", text: "De schrijver beweert dat fastfood goedkoper en sneller is, maar niet opweegt tegen cultuur." },
              { key: "C", text: "Fastfoodketens zijn weliswaar goedkoper en sneller, maar we verliezen onze identiteit." },
              { key: "D", text: "“We moeten onze lokale ondernemers steunen om deze culinaire rijkdom te behouden!”" }
            ],
            correct: "A",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie A is the enige optie die de vergelijking letterlijk citeert met de juiste aanhalingstekens. Optie B en C missen aanhalingstekens, en optie D citeert wel, maar dat is een oproep en geen vergelijking met fastfoodketens!"
          }
        ]
      },
      {
        title: "Tekst 47: Ontdek de Italiaanse keuken!",
        goal: "Activeren",
        text: `Ben jij die kant-en-klare magnetronmaaltijden en die diepvriespizza's ook zo zat? Dat snappen we heel goed, want er gaat niets boven de geur van verse basilicum en zelfgemaakte tomatensaus. <strong>Hoewel</strong> het maken van echte Italiaanse pasta soms ingewikkeld lijkt, kan iedereen het leren met de juiste tips. <strong>Daarom</strong> organiseren we deze zaterdag een gezellige, gratis kookworkshop in het buurthuis. <strong>Dus</strong> trek die keukenschort maar alvast aan! Meld je vandaag nog aan via onze website en leer hoe je met slechts bloem, eieren en passie de allerlekkerste tagliatelle op tafel toovert. Wacht niet langer, schrijf je nu direct in en word de ster van je eigen Italiaanse keuken!`,
        questions: [
          {
            id: 185,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Waarom kant-en-klare magnetronmaaltijden heel erg ongezond zijn." },
              { key: "B", text: "Zaterdag gratis kookworkshop in het buurthuis." },
              { key: "C", text: "Workshop Italiaans koken." },
              { key: "D", text: "Verse basilicum en tomatensaus." }
            ],
            correct: "C",
            explanation: "Het <em>Onderwerp</em> moet volgens het <strong>Spiekbriefje</strong> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Workshop Italiaans koken' (3 woorden) vat de hele tekst uitstekend samen! Optie A en B zijn te lang, en optie D is slechts een klein detail uit de inleiding."
          },
          {
            id: 186,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver geeft alleen de geschiedenis van de Italiaanse pastamachine." },
              { key: "B", text: "Activeren, want de schrijver spoort je heel direct aan om je in te schrijven voor de kookworkshop." },
              { key: "C", text: "Overtuigen, want de schrijver wil dat je vegetariër wordt." },
              { key: "D", text: "Amuseren, want het is een grappig sprookje over een pratende pastamachine." }
            ],
            correct: "B",
            explanation: "Het <strong>Spiekbriefje</strong> zegt over <em>Activeren</em>: 'Je iets laten doen'. De schrijver spoort je actief aan om in actie te komen met uitroepen zoals: 'Meld je vandaag nog aan...', 'trek die keukenschort maar alvast aan!' en 'schrijf je nu direct in!'. Het doel is dus overduidelijk activeren!"
          },
          {
            id: 187,
            question: "In de tekst staat het signaalwoord 'Dus'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Gevolg of conclusie, omdat de schrijver na de uitleg over de workshop de logische conclusie trekt dat je je schort moet aantrekken." },
              { key: "B", text: "Tegenstelling, want het geeft een contrast aan met de magnetronmaaltijden." },
              { key: "C", text: "Opsomming, want de schrijver noemt de ingrediënten van de pasta op." },
              { key: "D", text: "Tijd, want het geeft aan hoe laat de workshop precies begint." }
            ],
            correct: "A",
            explanation: "Op het <strong>Spiekbriefje</strong> onder <em>Tekstverbanden</em> zie je dat het signaalwoord 'dus' hoort bij een <strong>Gevolg/conclusie</strong>. De schrijver vertelt over de workshop, en trekt daaruit de conclusie: DUS trek die keukenschort maar aan!"
          },
          {
            id: 188,
            question: "In welke optie is de belofte over wat je leert maken juist geciteerd?",
            options: [
              { key: "A", text: "Je leert hoe je met bloem, eieren en passie tagliatelle op tafel tovert." },
              { key: "B", text: "“Meld je vandaag nog aan via onze website”" },
              { key: "C", text: "“leer hoe je met slechts bloem, eieren en passie de allerlekkerste tagliatelle op tafel toovert”" },
              { key: "D", text: "De schrijver belooft dat je lekkere tagliatelle leert maken met simpele ingrediënten." }
            ],
            correct: "C",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie C is de enige optie die de belofte letterlijk uit de tekst citeert met de juiste aanhalingstekens. Optie A en D missen de aanhalingstekens, en optie B citeert wel, maar dat is de oproep tot aanmelden, niet wat je leert maken!"
          }
        ]
      },
      {
        title: "Tekst 48: De brandende burrito",
        goal: "Amuseren",
        text: `Het was een gezellige vrijdagavond toen Daan met zijn vrienden in een hip Mexicaans restaurant zat. Om indruk te maken op zijn vrienden, besloot hij de 'El Infierno Burrito' te bestellen met de allerspicietste chilipepers. <strong>Toen</strong> de ober de burrito bezorgde, lachte Daan nog stoer en nam hij een gigantische hap. <strong>Maar</strong> al snel kleurde zijn gezicht vuurrood en begonnen de tranen uit zijn ogen te spuiten. <strong>Daarna</strong> hapte hij wild naar adem en greep hij in paniek het glas melk van zijn buurman om de brand in zijn mond te blussen. Zijn vrienden lagen gierend van het lachen onder de tafel. Daan nam zich plechtig voor om de volgende keer gewoon weer voor een milde taco te kiezen.`,
        questions: [
          {
            id: 189,
            question: "Wat is het onderwerp van deze tekst? (Max. 4 woorden!)",
            options: [
              { key: "A", text: "Daan eet spicy burrito." },
              { key: "B", text: "Waarom je nooit te veel chilipepers moet eten in een Mexicaans restaurant." },
              { key: "C", text: "Daan en zijn vrienden in een hip Mexicaans restaurant." },
              { key: "D", text: "De gevaren van spicy burrito's." }
            ],
            correct: "A",
            explanation: "Volgens het <strong>Spiekbriefje</strong> moet het <em>Onderwerp</em> in maximaal 4 woorden omschrijven waar de tekst over gaat. 'Daan eet spicy burrito' (4 woorden) vat het grappige verhaal perfect en superkort samen! De andere opties zijn te lang of missen de kern."
          },
          {
            id: 190,
            question: "Welk tekstdoel past het beste bij deze tekst?",
            options: [
              { key: "A", text: "Informeren, want de schrijver legt uit hoe heet chilipepers biologisch gezien zijn." },
              { key: "B", text: "Overtuigen, want de schrijver vindt dat Mexicaans eten verboden moet worden." },
              { key: "C", text: "Amuseren, want het is een grappig verhaal over Daan die een veel te hete burrito eet om indruk te maken." },
              { key: "D", text: "Activeren, want de schrijver wil dat je direct melk gaat kopen." }
            ],
            correct: "C",
            explanation: "Op het <strong>Spiekbriefje</strong> staat bij <em>Amuseren</em>: 'verhaal / vermaken'. Deze tekst is een grappig, humoristisch verhaal over Daan die stoer wil doen maar door de hete burrito rode wangen en tranen krijgt. Het is puur geschreven om de lezer te vermaken!"
          },
          {
            id: 191,
            question: "In de tekst staat het signaalwoord 'Daarna'. Welk tekstverband geeft dit woord aan?",
            options: [
              { key: "A", text: "Tegenstelling, want Daan drinkt melk in plaats van water." },
              { key: "B", text: "Tijd, want het geeft de chronologische volgorde van de grappige gebeurtenissen aan." },
              { key: "C", text: "Reden/oorzaak, want het legt uit hoe Daan zich voelde." },
              { key: "D", text: "Opsomming, want er worden verschillende Mexicaanse gerechten opgesomd." }
            ],
            correct: "B",
            explanation: "Op het <strong>Spiekbriefje</strong> staat 'daarna' onder het kopje <strong>Tijd</strong>. Het geeft aan in welke chronologische volgorde de acties gebeuren: eerst krijgt Daan tranen in zijn ogen, en DAARNA pakt hij in paniek het glas melk van zijn buurman."
          },
          {
            id: 192,
            question: "In welke optie is de reactie van de vrienden van Daan juist geciteerd?",
            options: [
              { key: "A", text: "Zijn vrienden moesten ontzettend hard lachen om zijn blunder." },
              { key: "B", text: "“Zijn vrienden lagen gierend van het lachen onder de tafel.”" },
              { key: "C", text: "“Daan nam zich plechtig voor om de volgende keer gewoon weer voor een milde taco te kiezen.”" },
              { key: "D", text: "De vrienden lagen gierend van het lachen onder de tafel." }
            ],
            correct: "B",
            explanation: "Kijk naar de regel voor <strong>Citeren</strong> op je <strong>Spiekbriefje</strong>: 'Letterlijk iemands woorden opschrijven met aanhalingstekens: “...”'. Optie B is letterlijk overgenomen uit de tekst en staat correct tussen aanhalingstekens. Optie A en D hebben geen aanhalingstekens, en optie C citeert Daan's voornemen, niet de reactie van de vrienden!"
          }
        ]
      }
    ]
  }
];

// Motivatie-uitspraken van "Meester Max"
const teacherQuotes = [
  "Fouten maken is de enige manier om slimmer te worden! Je doet het fantastisch. 🌟",
  "Begrijpend lezen is net als gamen: hoe meer je oefent, hoe beter je skills worden! 🎮",
  "Blijf goed naar het Spiekbriefje kijken, dat is jouw superkracht vandaag! ⚡",
  "Supertrots op hoe geconcentreerd je bezig bent. Zet 'm op! 🚀",
  "Elke stap die je nu zet, helpt je straks bij je proefwerken. Je bent een topper! 💎",
  "Zelfs de beste lezers hebben moeten oefenen. Je bent geweldig op weg! 🌈",
  "Rustig lezen, goed nadenken, en altijd het Spiekbriefje checken. Jij kunt dit! 🎓"
];

// Complimenten voor goede antwoorden
const positiveCompliments = [
  "Wauw, fantastisch gedaan! 🎉",
  "Helemaal juist! Je hebt dit echt goed begrepen. ⭐",
  "Super! Je bent scherp vandaag. 🚀",
  "Geweldig! Dat Spiekbriefje helpt je echt hè? 💎",
  "Spot on! Dit is 100% correct. 🎯",
  "Klasse! Je leest als een echte mavo-expert. 🏆",
  "Ja! Helemaal goed. Lekker bezig! ✨"
];
