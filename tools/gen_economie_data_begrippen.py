# tools/gen_economie_data_begrippen.py
"""Theorie en 8 oefenvragen voor h4_1_begrippen.js en h4_2_begrippen.js.
Alleen begrippen uit het lesboek Pincode HAVO 3 (§4.1 en §4.2).
Geen BBP, geen MVO, geen kostprijs in 4.1/4.2, geen schaalvoordelen, geen BEP.
Alleen mc en waaronwaar (geen open/invul, gate regel 5b).
"""

H4_1_THEORIE = """<h3>Begrippen &sect;4.1 Productie</h3>
<p>In deze paragraaf leer je hoe goederen en diensten worden gemaakt, wat bedrijven daarvoor nodig hebben en hoe waarde ontstaat.</p>
<h4>Produceren, consumeren en zelfvoorziening</h4>
<ul>
<li><b>Produceren:</b> het maken van goederen door bedrijven voor anderen. Dit geldt ook voor diensten. Het bedrijf, de producent, maakt de producten geschikt voor consumptie.</li>
<li><b>Consumeren:</b> de producten gebruiken die bedrijven voor consumenten hebben gemaakt.</li>
<li><b>Zelfvoorziening:</b> wanneer consumenten voor zichzelf produceren. Je hoeft niet altijd iets te kopen, soms kun je het ook zelf maken. Het koken van een maaltijd thuis is daarom geen produceren, het koken in een restaurant wel.</li>
</ul>
<h4>De kringloop tussen consumenten en producenten</h4>
<p>Tussen gezinnen (consumenten) en bedrijven (producenten) bestaat een kringloop:</p>
<ul>
<li>Mensen werken voor bedrijven, dit noem je <b>arbeid</b>, en ontvangen hiervoor <b>loon</b>.</li>
<li>Consumenten ruilen geld voor de <b>goederen en diensten</b> die bedrijven leveren.</li>
</ul>
<h4>Bedrijfskolom en toegevoegde waarde</h4>
<ul>
<li><b>Bedrijfskolom:</b> een model dat de stappen van grondstof tot eindproduct weergeeft. Alle bedrijven die meewerken aan de productie behoren tot de bedrijfskolom, bijvoorbeeld katoenplantage, stoffenfabrikant, kledingfabriek, transportbedrijf en kledingwinkel.</li>
<li><b>Toegevoegde waarde:</b> de waarde die ieder bedrijf in de bedrijfskolom toevoegt aan het product. Ook arbeid die wordt toegevoegd of de winst die een bedrijf maakt valt hieronder, maar is niet tastbaar. Produceren wordt daarom ook wel waarde toevoegen genoemd.</li>
</ul>
<div class="formule-box"><b>Toegevoegde waarde</b> = verkoopprijs &minus; inkoopprijs</div>
<h4>De vier productiefactoren</h4>
<p>Om te produceren zijn productiefactoren nodig. Dit zijn de middelen die nodig zijn om waarde toe te voegen aan het product:</p>
<ul>
<li><b>Kapitaal:</b> machines, gebouwen, gereedschappen, hulpmiddelen en geld om producten te kunnen maken en verkopen. Deze middelen heten ook wel kapitaalgoederen.</li>
<li><b>Arbeid:</b> de werknemers die het werk verrichten.</li>
<li><b>Natuur:</b> alles wat zonder bewerking uit de natuur komt, zoals hout. Ook de vestigingsplaats en energie horen bij deze productiefactor.</li>
<li><b>Ondernemerschap:</b> de ondernemer combineert alle productiefactoren op de meest effici&euml;nte manier met elkaar.</li>
</ul>
<h4>Soorten bedrijven</h4>
<ul>
<li><b>Productieonderneming:</b> koopt grondstoffen in, maakt daar producten van en verkoopt die aan klanten. Dat kunnen andere bedrijven zijn, maar ook consumenten (bijvoorbeeld een fietsenfabriek of een wasmachinefabriek).</li>
<li><b>Handelsonderneming:</b> koopt producten in die ze weer verkoopt en verandert niets aan het product. Toch voegt ze waarde toe, bijvoorbeeld door in een winkel fietsen en accessoires samen te brengen (bijvoorbeeld een fietsenwinkel of telefoonwinkel).</li>
<li><b>Dienstverlenend bedrijf:</b> verleent een dienst, zoals een fietsenmaker die fietsen repareert. Ook een kapper en een transportbedrijf zijn dienstverleners.</li>
</ul>
<h4>Sneller werken en arbeidsproductiviteit</h4>
<ul>
<li><b>Arbeidsproductiviteit:</b> de hoeveelheid producten of diensten die een arbeidskracht in een bepaalde tijd kan maken.</li>
<li><b>Mechanisatie:</b> het vervangen van arbeidskrachten door machines en technische hulpmiddelen. Je ziet het vooral in de landbouw.</li>
<li><b>Automatisering:</b> computers zorgen ervoor dat het werk sneller gedaan wordt.</li>
<li><b>Robotisering:</b> het vervangen van werknemers door robots, bijvoorbeeld in de auto-industrie.</li>
<li>De arbeidsproductiviteit kan ook stijgen door meer ervaren of hoger opgeleide medewerkers aan te nemen. Een hogere arbeidsproductiviteit leidt tot lagere kosten per product, zodat een onderneming meer winst kan maken.</li>
</ul>
<div class="formule-box"><b>Arbeidsproductiviteit</b> = aantal geproduceerde producten of diensten in een bepaalde tijd &divide; aantal medewerkers</div>"""

H4_1_VRAGEN = [
    {
        "type": "mc",
        "vraag": "Wat verstaat men in de economie onder het begrip 'produceren'?",
        "opties": [
            "Het kopen en verbruiken van goederen door gezinnen",
            "Het maken van goederen en leveren van diensten door bedrijven voor anderen",
            "Het bewaren van spaargeld op een bankrekening",
            "Het verbouwen van groenten uitsluitend voor eigen consumptie"
        ],
        "antwoord": 1,
        "uitleg": "Produceren is het maken van goederen en leveren van diensten door bedrijven voor anderen."
    },
    {
        "type": "mc",
        "vraag": "Waarom staat de consument zelf niet in de bedrijfskolom?",
        "opties": [
            "Omdat de consument geen bedrijf is dat meewerkt aan de productie",
            "Omdat de consument het product alleen bij een winkel kan kopen",
            "Omdat een consument volgens het boek nooit loon ontvangt",
            "Omdat de consument een deel van de productie overneemt"
        ],
        "antwoord": 0,
        "uitleg": "Alle bedrijven die meewerken aan de productie behoren tot de bedrijfskolom, en de consument is geen bedrijf."
    },
    {
        "type": "mc",
        "vraag": "Een meubelmaker koopt hout in voor € 120 en verkoopt de gemaakte tafel voor € 350. Hoeveel bedraagt de toegevoegde waarde?",
        "opties": [
            "€ 470",
            "€ 120",
            "€ 230",
            "€ 350"
        ],
        "antwoord": 2,
        "uitleg": "Toegevoegde waarde = verkoopprijs minus inkoopprijs = € 350 - € 120 = € 230."
    },
    {
        "type": "mc",
        "vraag": "Onder welke productiefactor valt een bestelbus die een bakker gebruikt voor bezorging?",
        "opties": [
            "Arbeid",
            "Natuur",
            "Kapitaal",
            "Ondernemerschap"
        ],
        "antwoord": 2,
        "uitleg": "Een bestelbus is een kapitaalgoed: een hulpmiddel waarmee het bedrijf produceert of levert."
    },
    {
        "type": "mc",
        "vraag": "Wat is het verschil tussen mechanisatie en automatisering?",
        "opties": [
            "Bij mechanisatie zorgen computers voor sneller werk, bij automatisering nemen machines arbeidskrachten over",
            "Bij mechanisatie nemen robots het werk van werknemers over, bij automatisering gebeurt dat met machines",
            "Mechanisatie en automatisering betekenen hetzelfde en worden alleen in de landbouw gebruikt",
            "Bij mechanisatie nemen machines arbeidskrachten over, bij automatisering zorgen computers voor sneller werk"
        ],
        "antwoord": 3,
        "uitleg": "Mechanisatie vervangt arbeidskrachten door machines en technische hulpmiddelen, bij automatisering zorgen computers voor sneller werk."
    },
    {
        "type": "waaronwaar",
        "vraag": "Als je thuis zelf een pastamaaltijd kookt voor je gezin, is er sprake van zelfvoorziening.",
        "antwoord": True,
        "uitleg": "Waar. Wanneer consumenten voor zichzelf produceren, noem je dit zelfvoorziening."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een fietsenwinkel is een productieonderneming omdat zij dagelijks fietsen verkoopt.",
        "antwoord": False,
        "uitleg": "Niet waar. Een fietsenwinkel koopt fietsen in en verkoopt ze door zonder ze te veranderen, dus het is een handelsonderneming."
    },
    {
        "type": "waaronwaar",
        "vraag": "Als zes werknemers samen 180 stoelen per dag maken, is de arbeidsproductiviteit 180 stoelen per werknemer per dag.",
        "antwoord": False,
        "uitleg": "Niet waar. Arbeidsproductiviteit = 180 stoelen / 6 werknemers = 30 stoelen per werknemer per dag."
    }
]

H4_2_THEORIE = """<h3>Begrippen &sect;4.2 Kosten</h3>
<p>Produceren kost geld. Bij deze kosten gaat het om de productiefactoren die worden ingezet: een bedrijf betaalt bijvoorbeeld loon in ruil voor de productiefactor arbeid. In deze paragraaf leer je welke soorten kosten er zijn en hoe je ermee rekent.</p>
<h4>Inkoopwaarde van de omzet en bedrijfskosten</h4>
<ul>
<li><b>Inkoopwaarde van de omzet:</b> het bedrag waarvoor producten worden ingekocht. Handelsondernemingen maken onderscheid tussen de kosten voor het inkopen van producten en overige kosten.</li>
<li><b>Bedrijfskosten:</b> alle overige kosten samen, zoals de lonen van het personeel, de huur van het pand en de kosten voor elektriciteit en water.</li>
<li>Productieondernemingen maken dit onderscheid niet, zij hebben alleen productiekosten.</li>
</ul>
<h4>Constante en variabele kosten</h4>
<ul>
<li><b>Variabele kosten:</b> kosten die afhankelijk zijn van de verkoop (de afzet). De inkoopwaarde van de omzet stijgt als een bedrijf meer verkoopt en daalt als er minder wordt verkocht. Ook verpakkings- en verzendkosten horen hierbij.</li>
<li><b>Constante (vaste) kosten:</b> kosten die niet afhangen van de omvang van de productie of de verkoop, zoals de huur van het bedrijfspand. Dit betekent niet dat deze kosten nooit veranderen: bij een nieuwe machine voor uitbreiding van de productie veranderen ze wel.</li>
</ul>
<h4>Soorten bedrijfskosten</h4>
<ul>
<li><b>Loonkosten:</b> de kosten voor salarissen van personeel.</li>
<li><b>Huisvestingskosten:</b> de kosten voor de huur of hypotheek van het bedrijfspand, maar ook voor energie en water.</li>
<li><b>Verkoopkosten:</b> kosten die direct samenhangen met de verkoop van de producten of diensten, zoals reclame en verzendkosten.</li>
<li><b>Rentekosten:</b> de rente die betaald wordt over een lening, bijvoorbeeld voor het bedrijfspand of een dure machine.</li>
</ul>
<h4>Kapitaalgoederen en afschrijven</h4>
<ul>
<li><b>Afschrijven:</b> een machine wordt door slijtage in de loop van de tijd minder waard. Dit geldt voor kapitaalgoederen zoals machines, computers en bedrijfsauto's.</li>
<li><b>Afschrijvingskosten:</b> de kosten die een onderneming maakt doordat de kapitaalgoederen ieder jaar minder waard worden. Het zijn constante kosten en ze horen bij de bedrijfskosten.</li>
<li><b>Restwaarde:</b> het bedrag dat een oude machine bij verkoop na een aantal jaar nog oplevert.</li>
</ul>
<div class="formule-box"><b>Afschrijvingskosten per jaar</b> = (aanschafwaarde &minus; restwaarde) &divide; aantal gebruiksjaren</div>"""

H4_2_VRAGEN = [
    {
        "type": "mc",
        "vraag": "Wat verstaat een winkelier onder de 'inkoopwaarde van de omzet'?",
        "opties": [
            "Het bedrag waarvoor de winkelier zijn goederen heeft ingekocht",
            "Het totale bedrag dat de winkelier in een jaar aan zijn klanten heeft verkocht",
            "Het bedrag dat de winkelier per jaar uitgeeft aan salarissen van het personeel",
            "Het bedrag dat de winkelier per maand betaalt voor huur van het winkelpand"
        ],
        "antwoord": 0,
        "uitleg": "De inkoopwaarde van de omzet is het bedrag dat de ondernemer betaalde voor de verkochte goederen."
    },
    {
        "type": "mc",
        "vraag": "Welke kostenpost is voor een meubelfabriek een voorbeeld van variabele kosten?",
        "opties": [
            "De maandelijkse huur van de fabriekshal",
            "De brandverzekering van het kantoorpand",
            "Het hout en de schroeven die per meubelstuk worden gebruikt",
            "De jaarlijkse afschrijving op de zaagmachines"
        ],
        "antwoord": 2,
        "uitleg": "Grondstoffen zoals hout en schroeven stijgen naarmate er meer meubels geproduceerd worden; dit zijn variabele kosten."
    },
    {
        "type": "mc",
        "vraag": "Onder welke categorie bedrijfskosten vallen advertenties op sociale media en drukwerk van reclamefolders?",
        "opties": [
            "Huisvestingskosten",
            "Verkoopkosten",
            "Loonkosten",
            "Rentekosten"
        ],
        "antwoord": 1,
        "uitleg": "Kosten om producten aan te prijzen en klanten te trekken vallen onder de verkoopkosten."
    },
    {
        "type": "mc",
        "vraag": "Waarom worden kapitaalgoederen zoals bestelbussen en computers ieder jaar minder waard?",
        "opties": [
            "Doordat bedrijven ieder jaar een lagere prijs voor hun producten vragen",
            "Omdat de verkoopprijs van het eindproduct elk jaar daalt bij de klant",
            "Doordat de werknemers er steeds minder zorgvuldig mee omgaan",
            "Door slijtage in de loop van de tijd en doordat ze verouderen"
        ],
        "antwoord": 3,
        "uitleg": "Kapitaalgoederen verliezen waarde door slijtage bij gebruik en doordat nieuwere technieken ontstaan."
    },
    {
        "type": "mc",
        "vraag": "Een machine kost nieuw € 40.000, heeft na 5 jaar een restwaarde van € 5.000. Hoeveel bedraagt de jaarlijkse afschrijving?",
        "opties": [
            "€ 8.000",
            "€ 5.000",
            "€ 7.000",
            "€ 9.000"
        ],
        "antwoord": 2,
        "uitleg": "Afschrijving per jaar = (€ 40.000 - € 5.000) / 5 jaar = € 35.000 / 5 = € 7.000."
    },
    {
        "type": "waaronwaar",
        "vraag": "De inkoopwaarde van de omzet maakt onderdeel uit van de bedrijfskosten van een winkel.",
        "antwoord": False,
        "uitleg": "Niet waar. Bedrijfskosten zijn alle kosten behalve de inkoopwaarde van de omzet."
    },
    {
        "type": "waaronwaar",
        "vraag": "De afschrijvingskosten van een bestelauto behoren tot de constante kosten van een onderneming.",
        "antwoord": True,
        "uitleg": "Waar. Afschrijvingen liggen voor het hele jaar vast en veranderen op korte termijn niet met de productie."
    },
    {
        "type": "waaronwaar",
        "vraag": "De restwaarde is het bedrag dat een kapitaalgoed aan het einde van de gebruiksduur naar verwachting nog oplevert.",
        "antwoord": True,
        "uitleg": "Waar. De restwaarde is de geschatte verkoopopbrengst na afloop van de gebruiksperiode."
    }
]
