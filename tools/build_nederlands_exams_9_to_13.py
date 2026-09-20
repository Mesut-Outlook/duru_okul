# -*- coding: utf-8 -*-
"""
Generator voor 5 EXTRA HAVO 3 Nederlands leestoetsen (Toets 9 t/m 13):
- Toets 9: §2 Inleiding en Slot (Toets D — Aandachtstrekkers & Probleemstellingen)
- Toets 10: §5 Vaste Tekststructuren (Toets D — Probleem-Oplossing & Voor- en Nadelen)
- Toets 11: §2 Inleiding en Slot (Toets E — Vraagstellingen, Citaten & Uitsmijters)
- Toets 12: §5 Vaste Tekststructuren (Toets E — Oorzaak-Gevolg & Historische Structuur)
- Toets 13: Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining)
"""
import json
import os

out_dir = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/nederlands/js/data"
os.makedirs(out_dir, exist_ok=True)

def maak_leestekst_card(titel, bron, alineas, extra_info=""):
    h = ['<div class="leestekst-card" style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #15803d; border-radius:12px; padding:16px 20px; margin-bottom:14px; max-height:350px; overflow-y:auto; font-size:14.5px; line-height:1.65; color:#1e293b; box-shadow:0 2px 8px rgba(0,0,0,0.04);">']
    h.append('  <div style="font-weight:800; color:#15803d; font-size:15px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid #e2e8f0; padding-bottom:6px;">')
    h.append(f'    <span>📄 {titel}</span>')
    if extra_info:
        h.append(f'    <span style="font-size:12px; font-weight:600; color:#64748b; background:#e2e8f0; padding:2px 8px; border-radius:99px;">{extra_info}</span>')
    h.append('  </div>')
    for nr, txt in enumerate(alineas, 1):
        h.append(f'  <p style="margin-bottom:10px;"><strong>[{nr}]</strong> {txt}</p>')
    if bron:
        h.append(f'  <div style="font-size:12px; font-style:italic; color:#64748b; margin-top:8px; border-top:1px dashed #cbd5e1; padding-top:4px;">Bron: {bron}</div>')
    h.append('</div>')
    return '\n'.join(h)

def balance_mc(vragen):
    mc_idx = 0
    for v in vragen:
        if v.get('type') == 'mc':
            target = mc_idx % 4
            orig = v['antwoord']
            if orig != target:
                opties = v['opties']
                opties[orig], opties[target] = opties[target], opties[orig]
                v['antwoord'] = target
            mc_idx += 1

# ==============================================================================
# TEKSTEN EN VRAGEN VOOR TOETS 9 (§2 INLEIDING EN SLOT - TOETS D)
# ==============================================================================
slaap_alineas = [
    "Iedereen heeft het weleens meegemaakt: je hebt de hele nacht doorgewerkt voor een deadline of urenlang doorgelopen in een spannende game. De volgende ochtend voelen je oogleden als lood, dwalen je gedachten voortdurend af en lukt zelfs een simpele rekensom nauwelijks. Waarom kunnen we eigenlijk niet gewoon zonder slaap? Is slapen slechts een tijdrovende noodzaak, of gebeurt er iets cruciaals in ons hoofd zodra de lichten uitgaan?",
    "Lange tijd beschouwden biologen slaap als een passieve rusttoestand, vergelijkbaar met een computer die in de slaapstand staat. Inmiddels weten we dankzij moderne hersenscans dat onze hersenen 's nachts juist een intensieve nachtdienst draaien. Zodra het lichaam ontspant, schakelen neuronen over op een volstrekt ander werkprogramma.",
    "Tijdens de diepe slaap treedt het zogeheten glymfatische systeem in werking: een ingenieus biologisch rioolsysteem. Hersenvocht stroomt tussen de krimpende cellen door en spoelt giftige afvalstoffen en eiwitten weg die zich overdag hebben opgehoopt. Zonder deze grondige nachtelijke schoonmaak raken zenuwverbindingen verstopt.",
    "In de daaropvolgende REM-slaap (de fase met snelle oogbewegingen waarin we dromen) zijn de hersenen even actief als overdag. Hier vindt de 'archivering' plaats: nieuwe herinneringen en lesstof worden van het tijdelijke werkgeheugen overgebracht naar het langetermijngeheugen, terwijl overbodige informatie wordt gewist.",
    "Wie structureel te weinig slaapt, ondervindt dan ook al snel ernstige schade. Concentratiegebrek, stemmingswisselingen en een verminderde weerstand zijn nog maar het begin; op lange termijn stijgt het risico op hart- en vaatziekten en burn-out aanzienlijk.",
    "Kortom: die nacht doorhalen om nog even snel voor een proefwerk te stampen, keert zich als een boemerang tegen je. Wie echt topprestaties wil leveren op school of op het sportveld, moet slaap niet zien als verloren tijd, maar als de belangrijkste training van de dag. Geef je brein dus de rust die het verdient: leg die smartphone op tijd weg en slaap jezelf slim."
]
card_slaap = maak_leestekst_card("Tekst A: De nachtdienst van ons brein", "Brein & Gezondheid, 2025", slaap_alineas, "6 alinea's")

puin_alineas = [
    "Boven onze hoofden cirkelt op dit moment een angstaanjagend metaalkerkhof. Ruim 36.000 stukken ruimtepuin groter dan tien centimeter en meer dan honderd miljoen microscopisch kleine metaalsplinters razen met een duizelingwekkende vaart van 28.000 kilometer per uur om de aarde. Bij zulke extreme snelheden heeft zelfs een rondvliegend verfschilfertje de inslagkracht van een kogel.",
    "Sinds de lancering van de allereerste Spoetnik-satelliet in 1957 heeft de mensheid duizenden raketten de dampkring uitgeschoten. Afgedankte rakettrappen, ontplofte brandstoftanks en defecte spionagesatellieten zijn decennialang stomweg achtergelaten in een baan om onze planeet.",
    "Wetenschappers vrezen nu het beruchte Kessler-syndroom. Dat is een rampscenario waarin één botsing tussen twee grote satellieten duizenden nieuwe scherven veroorzaakt, die vervolgens weer andere satellieten raken. Er ontstaat dan een kettingreactie van explosies, waardoor de ruimte rond de aarde verandert in een ondoordringbare storm van rondvliegend schroot.",
    "De maatschappelijke gevolgen van zo'n kettingreactie zouden gigantisch zijn. Zonder satellieten vallen gps-navigatie, weersvoorspellingen, internationaal betalingsverkeer en rampenbestrijding in één klap uit. Onze moderne hightech economie kan simpelweg niet functioneren zonder veilige ruimtebanen.",
    "Ruimtevaartorganisaties zoals ESA en NASA ontwikkelen daarom haastig methoden om de ruimte schoon te vegen. Met gigantische grijparmen, magneten en zelfs speciale harpoenen willen ingenieurs dode satellieten vangen en naar de dampkring trekken, waar ze veilig verbranden.",
    "Als de internationale gemeenschap niet snel bindende verdragen opstelt om vervuiling in de ruimte keihard te beboeten, sluiten we onszelf op achter een muur van eigen afval. De tijd van vrijblijvend experimenteren is voorbij; er is dringend kosmische verkeershandhaving nodig voordat het doek valt voor onze satellieten."
]
card_puin = maak_leestekst_card("Tekst B: Ruimtepuin: tikkende tijdbom in de kosmos", "Wetenschap & Techniek, 2025", puin_alineas, "6 alinea's")

vragen_ex9 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke techniek gebruikt de auteur in de openingsalinea van Tekst A om de aandacht van de lezer te trekken?",
        "opties": [
            "Een herkenbare persoonlijke situatie beschrijven",
            "Een historisch overzicht van de middeleeuwen geven",
            "Direct beginnen met een ingewikkelde natuurkundige formule",
            "Het citeren van een onbekende buitenlandse dichter"
        ],
        "antwoord": 0,
        "uitleg": "De auteur opent met een herkenbare situatie die iedereen meemaakt: een nacht doorwerken of gamen en de vermoeidheid daarna."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Wat is de functie van de vragen aan het einde van alinea 1 in Tekst A?",
        "opties": [
            "De hoofdvraag en probleemstelling van de tekst introduceren",
            "Twijfel zaaien over de betrouwbaarheid van artsen",
            "Aantonen dat slapen volstrekt overbodig is geworden",
            "Het bekritiseren van het Nederlandse schoolsysteem"
        ],
        "antwoord": 0,
        "uitleg": "De retorische vragen aan het slot van de inleiding introduceren de centrale probleemstelling van het artikel."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke kernopvatting over slaap wordt in alinea 2 gecorrigeerd?",
        "opties": [
            "Dat slaap slechts een passieve toestand van uitschakeling is",
            "Dat mensen overdag meer rusten dan tijdens de nacht",
            "Dat computers intelligenter zijn dan menselijke hersenen",
            "Dat dromen alleen voorkomen bij volwassen personen"
        ],
        "antwoord": 0,
        "uitleg": "Vroeger zag men slapen als passieve ruststand, maar modern onderzoek bewijst dat hersenen juist een actieve nachtdienst draaien."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke beeldspraak gebruikt de auteur in alinea 3 om het glymfatische systeem te verduidelijken?",
        "opties": [
            "Een biologisch rioolsysteem",
            "Een razendsnelle raceauto",
            "Een bibliotheek vol oude boeken",
            "Een ondoordringbare vestingmuur"
        ],
        "antwoord": 0,
        "uitleg": "In alinea 3 wordt het glymfatische mechanisme letterlijk omschreven als een 'biologisch rioolsysteem' dat afvalstoffen afvoert."
    },
    {
        "type": "waaronwaar",
        "figuur": card_slaap,
        "vraag": "Tijdens de diepe slaap spoelt hersenvocht giftige eiwitten weg tussen de cellen.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 3 vermeldt expliciet dat hersenvocht giftige afvalstoffen en eiwitten wegspoelt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_slaap,
        "vraag": "In de REM-slaap zijn de hersenen volledig inactief en worden er geen herinneringen opgeslagen.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 4 stelt juist dat de hersenen in de REM-slaap even actief zijn als overdag en herinneringen archiveren."
    },
    {
        "type": "invul",
        "figuur": card_slaap,
        "vraag": "Het biologische reinigingsmechanisme van de hersenen tijdens diepe slaap heet het ____ systeem.",
        "antwoord": "glymfatische",
        "uitleg": "In alinea 3 staat: 'het zogeheten glymfatische systeem'."
    },
    {
        "type": "open",
        "figuur": card_slaap,
        "vraag": "Op welke manier grijpt de slotalinea van Tekst A inhoudelijk terug op de allereerste alinea?",
        "sleutelwoorden": ["nacht doorhalen/proefwerk/stampen/studeren", "teruggegrepen/teruggrijpen/begin/aansluiten"],
        "minTreffers": 1,
        "modelantwoord": "In het slot wordt teruggegrepen op het nachtje doorhalen om te stampen voor een proefwerk, wat in het begin werd genoemd.",
        "uitleg": "Alinea 6 noemt letterlijk het 'nacht doorhalen om nog even snel te stampen', wat exact aansluit bij de inleiding."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke twee elementen typeren de slotalinea (alinea 6) van Tekst A?",
        "opties": [
            "Een samenvatting en een dringend advies aan de lezer",
            "Een lange lijst met nieuwe medische definities",
            "Een historische vergelijking met de prehistorie",
            "Een financiële begroting voor slaaponderzoek"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat de hoofdgedachte samen ('Kortom...') en sluit af met een concreet advies/oproep om op tijd te gaan slapen."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Wat is de centrale hoofdgedachte van Tekst A over de functie van slaap?",
        "opties": [
            "Slaap is een onmisbare actieve fase waarin het brein herstelt en herinneringen ordent",
            "Studenten moeten 's nachts gamen om hun reflexen scherp te houden",
            "Biologen weten nog altijd niet waarom levende wezens moeten rusten",
            "Het innemen van slaapmedicatie is de enige manier om gezond te blijven"
        ],
        "antwoord": 0,
        "uitleg": "De kern van de hele tekst is dat slaap geen passieve tijdverspilling is, maar een essentiële actieve fase voor onderhoud en geheugen."
    },
    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Welke manier van aandacht trekken kiest de auteur in de inleiding van Tekst B?",
        "opties": [
            "Het noemen van indrukwekkende en alarmerende cijfers over puin en snelheden",
            "Het vertellen van een vermakelijke grap over ruimtewezens",
            "Het citeren van een sciencefictionroman uit de negentiende eeuw",
            "Een uiteenzetting over de bouw van het lanceerplatform in Houston"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 opent met sprekende cijfers: 36.000 stukken puin, honderd miljoen splinters en 28.000 km/u."
    },
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Wat verduidelijkt alinea 2 binnen de opbouw van Tekst B?",
        "opties": [
            "De historische ontstaansgeschiedenis en de oorzaak van het probleem",
            "De exacte kosten van een ticket naar het internationale ruimtestation",
            "Het bewijs dat de aarde langzaam uit haar baan raakt",
            "De namen van alle Russische kosmonauten sinds 1957"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 schetst het ontstaan van het afvalprobleem sinds de lancering van Spoetnik in 1957."
    },
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Wat houdt het zogeheten 'Kessler-syndroom' uit alinea 3 in?",
        "opties": [
            "Een onstuitbare kettingreactie van botsingen tussen rondvliegende brokstukken",
            "Een zeldzame spierziekte die optreedt bij langdurig verblijf in gewichtloosheid",
            "Het plotseling uitdoven van communicatiesatellieten door zonnevlammen",
            "Het smelten van hitteschilden tijdens de terugkeer in de dampkring"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 beschrijft het Kessler-syndroom als een escalerende kettingreactie van botsingen die de ruimte onbegaanbaar maakt."
    },
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Waarom zijn de gevolgen van het Kessler-syndroom volgens alinea 4 desastreus voor gewone burgers op aarde?",
        "opties": [
            "Omdat alledaagse diensten zoals gps, weerberichten en betalingsverkeer dan wegvallen",
            "Omdat brandend puin steden op aarde dagelijks zal bombarderen",
            "Omdat wetenschappers dan niet meer naar verre sterrenstelsels kunnen kijken",
            "Omdat astronauten nooit meer kunnen terugkeren naar hun familie"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 legt uit dat gps, weersvoorspellingen en internetbankieren direct afhankelijk zijn van intacte satellieten."
    },
    {
        "type": "waaronwaar",
        "figuur": card_puin,
        "vraag": "Ruimtepuin beweegt zich voort met snelheden tot wel 28.000 kilometer per uur.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 1 noemt expliciet de duizelingwekkende snelheid van 28.000 km/u."
    },
    {
        "type": "waaronwaar",
        "figuur": card_puin,
        "vraag": "Er bestaan momenteel al strenge internationale verdragen die vervuiling in de ruimte effectief beboeten.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 6 benadrukt juist dat bindende verdragen en handhaving nog ontbreken en dringend moeten worden opgesteld."
    },
    {
        "type": "invul",
        "figuur": card_puin,
        "vraag": "Het doemscenario van een kettingreactie van botsend puin in de ruimte heet het ____-syndroom.",
        "antwoord": "Kessler",
        "uitleg": "In alinea 3 wordt gesproken over het 'beruchte Kessler-syndroom'."
    },
    {
        "type": "open",
        "figuur": card_puin,
        "vraag": "Welke twee oplossingen van ingenieurs om dode satellieten op te ruimen worden in alinea 5 genoemd?",
        "sleutelwoorden": ["grijparmen/magneten/harpoenen", "dampkring/verbranden/opbranden/vangen"],
        "minTreffers": 1,
        "modelantwoord": "Ingenieurs ontwikkelen grijparmen, magneten of harpoenen om satellieten te vangen en in de dampkring te laten verbranden.",
        "uitleg": "Alinea 5 noemt grijparmen, magneten en harpoenen om satellieten gecontroleerd te laten opbranden."
    },
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Welke functie heeft de slotalinea (alinea 6) van Tekst B hoofdzakelijk?",
        "opties": [
            "Een dringende oproep en waarschuwing aan de internationale politiek",
            "Het bedanken van alle donateurs van het ruimtestation",
            "Een samenvatting van de geschiedenis van de Spoetnik",
            "Een technisch stappenplan om een raketmotor te bouwen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 formuleert een niet mis te verstane oproep tot bindende internationale verdragen en verkeershandhaving."
    },
    {
        "type": "mc",
        "figuur": card_puin,
        "vraag": "Welke toon typeert het slot van Tekst B?",
        "opties": [
            "Alarmerend en aansporend",
            "Laconiek en onverschillig",
            "Vreugdevol en feestelijk",
            "Nostalgisch en weemoedig"
        ],
        "antwoord": 0,
        "uitleg": "De zinnen 'De tijd van vrijblijvend experimenteren is voorbij' en 'voordat het doek valt' zetten een alarmerende en aansporende toon neer."
    }
]

# ==============================================================================
# TEKSTEN EN VRAGEN VOOR TOETS 10 (§5 VASTE TEKSTSTRUCTUREN - TOETS D)
# ==============================================================================
farming_alineas = [
    "De wereldbevolking groeit naar verwachting tot bijna tien miljard mensen in 2050. Tegelijkertijd slinkt het oppervlak aan vruchtbare landbouwgrond door verwoestijning, bodemerosie en verstedelijking. Bovendien zorgen aanhoudende droogtes en extreme hagelstormen steeds vaker voor mislukte oogsten. Hoe kunnen we in de nabije toekomst miljoenen monden voeden zonder onze aarde nog verder uit te putten?",
    "Een revolutionaire oplossing voor dit dreigende voedseltekort is vertical farming, oftewel verticale landbouw. In plaats van uitgestrekte akkers op het platteland, worden gewassen geteeld in torenhoge stellingen binnen leegstaande fabriekshallen en kantoorpanden in het hart van de stad.",
    "Binnen deze overdekte teeltfaciliteiten heerst een volmaakt gecontroleerd klimaat. Planten groeien niet in aarde, maar met hun wortels in een nevel van water en voedingsstoffen (hydrocultuur). Energiezuinige led-lampen schijnen dag en nacht in exact de lichtkleuren waar bladgroenten het snelst van groeien.",
    "Deze innovatieve kweekmethode levert gigantische voordelen op. Allereerst verbruiken verticale boerderijen tot wel 95 procent minder water dan traditionele akkers, doordat al het vocht circuleert. Omdat insecten en schimmels buiten de hermetisch gesloten deuren blijven, zijn chemische bestrijdingsmiddelen bovendien volstrekt overbodig.",
    "Toch kent vertical farming ook nog aanzienlijke knelpunten. De aanschaf van hypermoderne sensoren, klimaatcomputers en led-systemen vergt torenhoge investeringen. Daarnaast vreet de continue verlichting enorme hoeveelheden elektriciteit, wat de teelt pas echt duurzaam maakt als er volop groene stroom beschikbaar is.",
    "Kortom: vertical farming is weliswaar geen toverstokje dat het wereldvoedselprobleem in zijn eentje oplost, maar wel een onmisbare bouwsteen voor een klimaatbestendige toekomst. Door steden zelfvoorzienend te maken op het gebied van vers voedsel, ontlasten we de natuur en brengen we de akker letterlijk naar de consument."
]
card_farming = maak_leestekst_card("Tekst A: De opkomst van vertical farming", "Agrarisch Innovatie Magazine, 2024", farming_alineas, "6 alinea's")

cash_alineas = [
    "Wie op een zaterdagmiddag door een Nederlandse winkelstraat loopt, ziet bij bakkers, kledingwinkels en koffiebars steeds vaker hetzelfde bordje hangen: 'Hier alleen pinnen a.u.b.'. Geldautomaten verdwijnen in rap tempo uit het straatbeeld en banken sluiten hun filialen. Is het verdwijnen van contant geld een zegen voor onze efficiëntie, of moeten we vrezen voor een maatschappij zonder munten en biljetten?",
    "Voorstanders van een geheel girale economie wijzen op de overduidelijke voordelen van digitaal afrekenen. Betalen met je pinpas, smartwatch of smartphone verloopt razendsnel, wat lange rijen bij de kassa voorkomt. Voor winkeliers betekent het einde van contant geld bovendien veel minder administratief gedoe en aanzienlijk lagere kosten voor beveiligd waardetransport.",
    "Nog belangrijker is het veiligheidsaspect. Zonder kassa's vol flappen verdwijnt de buit voor overvallers. Overvallen op winkels en overvaltrauma's bij jonge kassamedewerkers zijn de afgelopen jaren dankzij pinbetalingen dan ook spectaculair gedaald.",
    "Aan de andere kant brengt het afschaffen van contant geld ernstige nadelen en risico's met zich mee. Ruim twee miljoen Nederlanders, waaronder veel ouderen en mensen met een verstandelijke beperking, hebben grote moeite met de steeds complexere digitale bankapps. Als contant geld verdwijnt, raken deze kwetsbare groepen buitengesloten van het economisch leven.",
    "Daar komt bij dat digitaal betalen onze privacy onder druk zet; elke transactie wordt geregistreerd en geanalyseerd door commerciële banken en overheden. Bovendien maakt een maatschappij zonder contant geld ons extreem kwetsbaar voor stroomstoringen en cyberaanvallen. Ligt het internet plat, dan kun je zelfs geen brood meer kopen.",
    "Al met al wegen de praktische voordelen van digitaal gemak niet op tegen het verlies van keuzevrijheid en privacy. Contant geld fungeert als een onmisbaar maatschappelijk vangnet. Voor een gezonde en inclusieve economie moet contant geld dan ook altijd als wettig en toegankelijk betaalmiddel blijven bestaan."
]
card_cash = maak_leestekst_card("Tekst B: Contant geld: zegen of verleden tijd?", "Economie & Samenleving, 2024", cash_alineas, "6 alinea's")

vragen_ex10 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Welke vaste tekststructuur herken je duidelijk in Tekst A?",
        "opties": [
            "Probleem-oplossingstructuur",
            "Onderzoeksstructuur van een laboratoriumexperiment",
            "Historische structuur van de middeleeuwen",
            "Beoordelingsstructuur van een filmrecensie"
        ],
        "antwoord": 0,
        "uitleg": "De tekst schetst eerst het probleem (voedseltekort en krimpende landbouwgrond) en presenteert vervolgens vertical farming als oplossing."
    },
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Welk concreet probleem staat centraal in de inleiding van Tekst A?",
        "opties": [
            "Krimpende landbouwgronden en mislukkende oogsten bij een groeiende wereldbevolking",
            "Het verdwijnen van boerenmarkten in historische dorpen",
            "Een overschot aan groenten in Europese supermarkten",
            "De stijgende benzineprijzen voor zware landbouwtractoren"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 schetst het probleem van bevolkingsgroei naar 10 miljard tegenover krimpende grond en mislukkende oogsten."
    },
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Wat is het belangrijkste kenmerk van vertical farming volgens alinea 2 en 3?",
        "opties": [
            "Gewassen worden binnen in verticale stellingen geteeld onder gecontroleerde condities",
            "Boeren ploegen hun akkers voortaan uitsluitend nog 's nachts met gps",
            "Alle groenten worden geïmporteerd uit tropische regenwouden",
            "Groenten worden genetisch gemanipuleerd om in zout water te groeien"
        ],
        "antwoord": 0,
        "uitleg": "Alinea's 2 en 3 beschrijven hoe planten in stellingen groeien zonder aarde en onder led-licht."
    },
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Welke twee grote voordelen worden in alinea 4 van Tekst A benadrukt?",
        "opties": [
            "Tot 95 procent waterbesparing en geen chemische bestrijdingsmiddelen nodig",
            "Lagere elektriciteitskosten en goedkopere vrachtwagens",
            "Planten die binnen twee uur volgroeid zijn en gratis zaden",
            "Minder personeelskosten doordat robots alles opeten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 noemt letterlijk de 95% waterbesparing en het ontbreken van chemische pesticiden."
    },
    {
        "type": "waaronwaar",
        "figuur": card_farming,
        "vraag": "Vertical farming verbruikt aanzienlijk minder water dan traditionele akkerbouw doordat water circuleert.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 4 vermeldt dat verticale boerderijen tot 95 procent minder water verbruiken doordat al het vocht circuleert."
    },
    {
        "type": "waaronwaar",
        "figuur": card_farming,
        "vraag": "Vertical farming vergt volgens alinea 5 nauwelijks elektriciteit en is direct spotgoedkoop.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 benadrukt dat de aanschaf torenhoge investeringen vergt en dat de verlichting juist enorme hoeveelheden stroom vreet."
    },
    {
        "type": "invul",
        "figuur": card_farming,
        "vraag": "De tekststructuur waarin na een maatschappelijke moeilijkheid maatregelen worden aangedragen heet de ____-structuur.",
        "antwoord": "probleem-oplossing",
        "uitleg": "De structuur heet de probleem-oplossingstructuur."
    },
    {
        "type": "open",
        "figuur": card_farming,
        "vraag": "Noem twee nadelen of knelpunten van vertical farming die in alinea 5 worden besproken.",
        "sleutelwoorden": ["hoge investeringen/duur/kosten", "veel stroom/elektriciteit/energieverbruik"],
        "minTreffers": 2,
        "modelantwoord": "De torenhoge investeringskosten voor sensoren en computers, en het enorme elektriciteitsverbruik door de continue verlichting.",
        "uitleg": "Alinea 5 noemt hoge investeringskosten en gigantisch elektriciteitsverbruik als voornaamste knelpunten."
    },
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Wat is de functie van alinea 6 binnen het geheel van Tekst A?",
        "opties": [
            "De oplossing evalueren en een toekomstgericht eindoordeel geven",
            "Nieuwe wetenschappelijke theorieën over meststoffen presenteren",
            "Het werk van traditionele boeren belachelijk maken",
            "Een subsidieaanvraag indienen bij de Europese Unie"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat de balans samen ('Kortom...') en formuleert een genuanceerde eindconclusie."
    },
    {
        "type": "mc",
        "figuur": card_farming,
        "vraag": "Welk signaalwoord in alinea 6 kondigt aan dat de hoofdgedachte wordt samengevat?",
        "opties": [
            "Kortom",
            "Omdat",
            "Daarentegen",
            "Ten eerste"
        ],
        "antwoord": 0,
        "uitleg": "'Kortom' is het klassieke signaalwoord voor een samenvatting aan het begin van de slotalinea."
    },
    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Welke vaste tekststructuur vormt het fundament van Tekst B?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur",
            "Verschijnsel-oorzaakstructuur",
            "Vraag-antwoordstructuur van een interview"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B behandelt in alinea 2 en 3 de voordelen van digitaal geld en in alinea 4 en 5 de nadelen, afgesloten met een afweging."
    },
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Welk voordeel voor winkeliers wordt genoemd in alinea 2 van Tekst B?",
        "opties": [
            "Snellere afhandeling en minder kosten voor beveiligd waardetransport",
            "Gratis levering van koffie en gebak door de banken",
            "Het verdwijnen van alle verplichtingen om belasting te betalen",
            "Winkels hoeven nooit meer schoongemaakt te worden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 stelt dat digitaal betalen minder administratief gedoe en lagere kosten voor waardetransport oplevert."
    },
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Waarom daalt het aantal winkelovervallen volgens alinea 3?",
        "opties": [
            "Omdat er zonder contant geld geen fysieke kastegoeden meer te stelen zijn",
            "Omdat alle overvallers tegenwoordig thuiswerken via internet",
            "Omdat winkels voortaan uitsluitend bewaakt worden door getrainde honden",
            "Omdat klanten verplicht een identiteitsbewijs moeten tonen bij de ingang"
        ],
        "antwoord": 0,
        "uitleg": "Zonder kassa's met contant geld is er voor overvallers geen directe contante buit meer te halen."
    },
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Welk maatschappelijk nadeel van een cashloze maatschappij wordt in alinea 4 aan de kaak gesteld?",
        "opties": [
            "Kwetsbare groepen zoals ouderen en laaggeletterden kunnen buitengesloten raken",
            "Bankmedewerkers raken allemaal tegelijk hun baan kwijt",
            "Muntgeld kan in musea niet meer tentoongesteld worden",
            "Kinderen leren op school niet meer hoe ze moeten rekenen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 benadrukt dat ruim twee miljoen mensen moeite hebben met digitale apps en buitengesloten dreigen te raken."
    },
    {
        "type": "waaronwaar",
        "figuur": card_cash,
        "vraag": "In alinea 2 en 3 van Tekst B worden de positieve kanten van giraal betalen uiteengezet.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 en 3 beschrijven de voordelen van snelheid, administratiegemak en veiligheid."
    },
    {
        "type": "waaronwaar",
        "figuur": card_cash,
        "vraag": "De auteur concludeert in het slot dat contant geld zo snel mogelijk volledig verboden moet worden.",
        "antwoord": False,
        "uitleg": "Onwaar. De auteur concludeert juist dat contant geld altijd als maatschappelijk vangnet en betaalmiddel behouden moet blijven."
    },
    {
        "type": "invul",
        "figuur": card_cash,
        "vraag": "Signaalwoorden zoals 'Aan de andere kant' en 'Anderzijds' wijzen meestal op een ____-structuur.",
        "antwoord": "voor- en nadelen",
        "uitleg": "Deze signaalwoorden introduceren de tegenzijde in een voor- en nadelenstructuur."
    },
    {
        "type": "open",
        "figuur": card_cash,
        "vraag": "Welke twee bezwaren tegen digitaal betalen worden in alinea 5 naar voren gebracht?",
        "sleutelwoorden": ["privacy/transacties geregistreerd", "stroomstoring/cyberaanval/internetstoring/kwetsbaar"],
        "minTreffers": 2,
        "modelantwoord": "De aantasting van privacy doordat alles geregistreerd wordt, en de extreme kwetsbaarheid bij stroomstoringen of cyberaanvallen.",
        "uitleg": "Alinea 5 noemt letterlijk privacy-aantasting en kwetsbaarheid voor stroomstoringen en cyberaanvallen."
    },
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Welk schrijfdoel heeft de auteur met Tekst B?",
        "opties": [
            "Beschouwen en overtuigen: argumenten afwegen om te pleiten voor behoud van contant geld",
            "Amuseren: grappige verhalen vertellen over winkelpersoneel",
            "Instrueren: stap voor stap uitleggen hoe je een bankapp downloadt",
            "Emoties opwekken: de lezer laten schrikken van inflatiecijfers"
        ],
        "antwoord": 0,
        "uitleg": "De auteur weegt eerst voors en tegens af (beschouwen) en trekt in het slot een duidelijke conclusie (overtuigen)."
    },
    {
        "type": "mc",
        "figuur": card_cash,
        "vraag": "Wat is het eindoordeel van de auteur in de slotalinea (alinea 6) van Tekst B?",
        "opties": [
            "Contant geld moet als wettig betaalmiddel en maatschappelijk vangnet behouden blijven",
            "Alle winkeliers moeten verplicht worden om alleen nog contant geld te accepteren",
            "Geldautomaten moeten worden omgebouwd tot oplaadpalen voor auto's",
            "Banken mogen geen kosten meer in rekening brengen voor pinpassen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 stelt onomwonden: 'Voor een gezonde en inclusieve economie moet contant geld dan ook altijd als wettig en toegankelijk betaalmiddel blijven bestaan.'"
    }
]

# ==============================================================================
# TEKSTEN EN VRAGEN VOOR TOETS 11 (§2 INLEIDING EN SLOT - TOETS E)
# ==============================================================================
horror_alineas = [
    "\"We verzinnen monsters om ons te helpen omgaan met de echte wereld,\" schreef de beroemde griezelauteur Stephen King ooit. Kijk op een zaterdagavond rond in een volle bioscoopzaal bij een griezelfilm: mensen slaan hun handen voor hun ogen, happen naar adem en gillen het uit van angst. En toch betalen we grif vijftien euro voor een kaartje om anderhalf uur lang doodsangsten uit te staan. Waarom zoeken mensen vrijwillig kippenvel en terreur op?",
    "Op het eerste gezicht lijkt deze fascinatie met griezelen tegenstrijdig. De mens is evolutionair geprogrammeerd om gevaar en pijn angstvallig te vermijden. Angst zorgt voor een acute stressreactie: je hartslag schiet omhoog, je spieren spannen zich en adrenaline giert door je lijf. Toch beleven miljoenen mensen enorm veel plezier aan dit angstzweet.",
    "Psychologen verklaren dit fenomeen met het concept van 'veilige dreiging'. Als je in een donkere bioscoopzaal of op de bank zit, registreren je zintuigen weliswaar gevaar, maar je verstand weet dondersgoed dat het monster op het witte doek je niet écht kan verscheuren. Je ervaart de fysieke kick van adrenaline en dopamine, zonder dat er reëel risico bestaat.",
    "Bovendien fungeert griezelen als een emotionele oefenruimte. Wetenschappers ontdekten dat fans van griezelfilms tijdens de coronapandemie mentaal veerkrachtiger waren. Door fictieve rampen te aanschouwen, trainen we ons brein onbewust in het omgaan met onvoorspelbare en stressvolle situaties.",
    "Niet iedereen geniet overigens evenveel van griezelen. Mensen met een hoge mate van 'sensatiezoeken' kunnen niet genoeg krijgen van bloedstollende plotwendingen, terwijl hoogsensitieve individuen na een griezelscène nachtenlang wakker liggen met nachtmerries.",
    "Zo blijkt de quote van Stephen King griezelig accuraat. We hebben fictieve spoken, zombies en psychopaten nodig om onze eigen diepgewortelde angsten te bezweren. Griezelen in het donker is geen ziekelijke afwijking, maar een oeroude overlevingsstrategie die ons leert dat het donker weliswaar eng is, maar dat het licht uiteindelijk altijd weer aangaat."
]
card_horror = maak_leestekst_card("Tekst A: De kick van kippenvel", "Psychologie Vandaag, 2024", horror_alineas, "6 alinea's")

bos_alineas = [
    "Wie door een oeroud beukenbos wandelt, ervaart een serene stilte. De majestueuze bomen lijken eenzame reuzen, roerloos verankerd in de aarde, elk vechtend voor hun eigen portie zonlicht en water. Maar schijn bedriegt volkomen. Onder de bosbodem bevindt zich een geheimzinnig, fijnvertakt netwerk dat biologen tegenwoordig het 'Wood Wide Web' noemen: een ondergronds internet waarin bomen met elkaar communiceren en grondstoffen uitwisselen.",
    "Dat ondergrondse netwerk bestaat uit kilometerslange schimmeldraden, zogeheten mycorrhiza. Deze schimmels gaan een innige symbiose aan met de boomwortels. Ze leveren mineralen en stikstof aan de bomen in ruil voor suikers die de bomen via fotosynthese aanmaken.",
    "Het netwerk doet echter veel meer dan alleen voedsel transporteren; het fungeert als een snelweg voor chemische alarmsignalen. Zodra een boom wordt aangevallen door vraatzuchtige rupsen of kevers, stuurt hij via de schimmeldraden noodsignalen naar zijn buren. Die buren beginnen direct met de aanmaak van bittere gifstoffen in hun bladeren, nog voordat de eerste rups hen heeft bereikt.",
    "Onderzoekers van de universiteit van British Columbia ontdekten bovendien dat zogeheten 'moederbomen' via dit netwerk stervende zaailingen herkennen en gericht suikers en water naar hun nakomelingen pompen om hen door droge zomers heen te loodsen.",
    "Helaas staat dit wonderbaarlijke ondergrondse communicatiesysteem zwaar onder druk. Intensieve houtkap, bodemverdichting door zware oogstmachines en overmatige stikstofuitstoot breken de kwetsbare schimmeldraden af, waardoor bomen geïsoleerd raken en vatbaar worden voor plagen.",
    "Kortom: een bos is geen verzameling individuele stammen, maar een hechte, solidaire gemeenschap. Als we bomen willen beschermen tegen de gevolgen van klimaatverandering, moeten we ophouden met het kappen van oude woudreuzen en beseffen dat het ware geheim van het bos onder onze schoenzolen verborgen ligt."
]
card_bos = maak_leestekst_card("Tekst B: Het geheime internet van het bos", "Natuur & Wetenschap, 2025", bos_alineas, "6 alinea's")

vragen_ex11 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Met welke twee stijlmiddelen probeert de auteur in alinea 1 van Tekst A de lezer te prikkelen?",
        "opties": [
            "Een literair citaat en een herkenbare situatiebeschrijving in de bioscoop",
            "Een sombere klaagzang over bioscooptarieven en popcornprijzen",
            "Een wiskundige berekening van de decibellen van een schreeuw",
            "Een pleidooi om alle bioscopen na tienen te sluiten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 opent met een citaat van Stephen King en schetst de herkenbare situatie van gillende bioscoopbezoekers."
    },
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Welke paradox (schijnbare tegenstelling) formuleert de auteur in alinea 1 en 2?",
        "opties": [
            "Mensen vermijden gevaar, maar betalen toch geld om doodsangst te ervaren",
            "Bioscoopkaartjes zijn duur, terwijl de films steeds korter worden",
            "Mensen willen graag gezond eten, maar eten te veel popcorn",
            "Regisseurs maken griezelfilms, hoewel ze zelf bang zijn in het donker"
        ],
        "antwoord": 0,
        "uitleg": "De paradox is dat mensen van nature gevaar mijden, maar toch vrijwillig geld betalen om doodsbang te zijn."
    },
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Wat wordt in alinea 3 bedoeld met de term 'veilige dreiging'?",
        "opties": [
            "Je lichaam ervaart de adrenalinekick van gevaar, terwijl je ratio weet dat je veilig bent",
            "Een alarmsysteem in huis dat waarschuwt bij inbraak",
            "Een actieheld in de film die het monster op tijd uitschakelt",
            "Het kijken naar een film met de lampen in de kamer aan"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat je zintuigen gevaar registreren, maar je hersenen weten dat het monster niet echt gevaar oplevert."
    },
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Welk voordeel van griezelen tijdens de coronacrisis ontdekten wetenschappers volgens alinea 4?",
        "opties": [
            "Griezelliefhebbers bleken mentaal veerkrachtiger bij stressvolle situaties",
            "Fans van griezelfilms hadden minder last van fysieke vermoeidheid",
            "Zij konden virussen sneller herkennen onder een microscoop",
            "Zij verveelden zich minder tijdens de lockdowns"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 meldt dat griezelfans mentaal veerkrachtiger waren omdat hun brein gewend was aan stress en rampscenario's."
    },
    {
        "type": "waaronwaar",
        "figuur": card_horror,
        "vraag": "Tijdens een angstreactie gieren adrenaline en dopamine door het lichaam.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 en 3 noemen de afgifte van adrenaline en dopamine bij een angstreactie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_horror,
        "vraag": "Volgens alinea 5 beleeft ieder mens exact evenveel plezier aan griezelscènes.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 legt uit dat sensatiezoekers ervan genieten, maar hoogsensitieve mensen nachtenlang wakker liggen."
    },
    {
        "type": "invul",
        "figuur": card_horror,
        "vraag": "Het psychologische mechanisme waarbij men spanning beleeft zonder echt risico heet een veilige ____.",
        "antwoord": "dreiging",
        "uitleg": "In alinea 3 staat: 'het concept van veilige dreiging'."
    },
    {
        "type": "open",
        "figuur": card_horror,
        "vraag": "Welk inhoudelijk verband legt de auteur in de slotalinea met de allereerste alinea van Tekst A?",
        "sleutelwoorden": ["quote/Stephen King/citaat/monsters", "terug/terugblik/teruggrijpen/verwijzen/aansluiten"],
        "minTreffers": 1,
        "modelantwoord": "De auteur verwijst letterlijk terug naar de openingsquote van Stephen King over monsters.",
        "uitleg": "Alinea 6 opent met: 'Zo blijkt de quote van Stephen King griezelig accuraat', waarmee direct wordt teruggegrepen op alinea 1."
    },
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Welke rol vervult de laatste zin van alinea 6 ('...maar dat het licht uiteindelijk altijd weer aangaat')?",
        "opties": [
            "Een krachtige uitsmijter en hoopvolle doordenker voor de lezer",
            "Een praktische mededeling over het aandoen van de zaalverlichting",
            "Een waarschuwing tegen te hoge energiekosten voor lampen",
            "Een samenvatting van de plot van de nieuwste film van King"
        ],
        "antwoord": 0,
        "uitleg": "Dit is een typische 'uitsmijter': een prikkelende, metaforische slotzin die de lezer aan het denken zet."
    },
    {
        "type": "mc",
        "figuur": card_horror,
        "vraag": "Wat is de belangrijkste hoofdgedachte van Tekst A over griezelen?",
        "opties": [
            "Griezelen is een nuttige overlevingsstrategie die ons veilig leert omgaan met angst en stress",
            "Stephen King is de meest getalenteerde schrijver van de moderne literatuur",
            "Mensen moeten stoppen met het bezoeken van bioscopen vanwege gehoorschade",
            "Adrenaline is een schadelijk hormoon dat koste wat het kost vermeden moet worden"
        ],
        "antwoord": 0,
        "uitleg": "De kernboodschap is dat griezelen een veilige manier is om onze angsten te bezweren en veerkracht te trainen."
    },
    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Welke beeldspraak introduceert de auteur in de inleiding van Tekst B?",
        "opties": [
            "Het vergelijken van de ondergrondse schimmeldraden met het internet (Wood Wide Web)",
            "Het vergelijken van bomen met wolkenkrabbers in New York",
            "Het vergelijken van het bos met een middeleeuws slagveld",
            "Het omschrijven van bladeren als zonnepanelen op een dak"
        ],
        "antwoord": 0,
        "uitleg": "In alinea 1 wordt het ondergrondse netwerk direct vergeleken met internet: 'Wood Wide Web'."
    },
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Wat is de symbiose tussen schimmels en boomwortels in alinea 2?",
        "opties": [
            "Schimmels leveren mineralen en stikstof, bomen leveren suikers uit fotosynthese",
            "Bomen beschermen de schimmels tegen regen, schimmels eten dood hout",
            "Schimmels verwarmen de grond in de winter, bomen geven schaduw in de zomer",
            "Bomen pompen water omhoog, schimmels vangen vogels en insecten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 vermeldt: schimmels leveren mineralen en stikstof in ruil voor suikers die bomen aanmaken via fotosynthese."
    },
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Hoe waarschuwen bomen elkaar volgens alinea 3 voor oprukkende rupsen?",
        "opties": [
            "Door chemische noodsignalen te verzenden via de ondergrondse schimmeldraden",
            "Door hun takken wild tegen elkaar aan te slaan in de wind",
            "Door ultrasone geluiden uit te stoten die vogels lokken",
            "Door al hun bladeren binnen een minuut massaal te laten vallen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 beschrijft hoe bomen via schimmeldraden chemische noodsignalen naar buren sturen."
    },
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Wat doen zogeheten 'moederbomen' volgens het onderzoek in alinea 4?",
        "opties": [
            "Ze pompen gericht water en suikers naar stervende zaailingen om hen te helpen",
            "Ze zorgen dat er geen enkele andere boom in hun buurt kan groeien",
            "Ze vangen al het zonlicht weg voor jongere boompjes",
            "Ze sterven direct af zodra hun eerste zaden ontkiemen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 beschrijft hoe moederbomen via het netwerk suikers en water naar nakomelingen sluizen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_bos,
        "vraag": "De schimmeldraden (mycorrhiza) vormen een functionele symbiose met boomwortels.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 legt deze symbiose gedetailleerd uit."
    },
    {
        "type": "waaronwaar",
        "figuur": card_bos,
        "vraag": "Zware oogstmachines en overmatige stikstofuitstoot hebben volgens alinea 5 geen enkele invloed op het bodemleven.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 stelt juist dat machines en stikstof de kwetsbare schimmeldraden kapotmaken."
    },
    {
        "type": "invul",
        "figuur": card_bos,
        "vraag": "Het ondergrondse communicatienetwerk van bomen wordt ook wel gekscherend het Wood Wide ____ genoemd.",
        "antwoord": "Web",
        "uitleg": "In alinea 1 staat letterlijk: 'het Wood Wide Web'."
    },
    {
        "type": "open",
        "figuur": card_bos,
        "vraag": "Noem twee bedreigingen voor het ondergrondse schimmelnetwerk die in alinea 5 worden opgesomd.",
        "sleutelwoorden": ["houtkap/bomen kappen", "zware machines/bodemverdichting", "stikstof/stikstofuitstoot"],
        "minTreffers": 2,
        "modelantwoord": "Intensieve houtkap, bodemverdichting door zware machines en overmatige stikstofuitstoot.",
        "uitleg": "Alinea 5 noemt intensieve houtkap, bodemverdichting door zware machines en stikstofuitstoot."
    },
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Wat is de functie van de slotalinea (alinea 6) van Tekst B?",
        "opties": [
            "Een samenvatting van de ontdekkingen en een oproep tot natuurbescherming",
            "Het aankondigen van een subsidie voor zaagfabrieken",
            "Het bekritiseren van wandelaars die van de paden afwijken",
            "Een opsomming van de prijzen van beukenhout op de wereldmarkt"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat de essentie samen ('Kortom...') en formuleert een krachtig pleidooi om oude wouden te sparen."
    },
    {
        "type": "mc",
        "figuur": card_bos,
        "vraag": "Welke conclusie trekt de auteur in de laatste alinea van Tekst B?",
        "opties": [
            "Een bos is een hechte gemeenschap waarvan het belangrijkste geheim onder de grond ligt",
            "Bomen kunnen beter gekapt worden om plaats te maken voor akkers",
            "Schimmels zijn parasieten die alle bomen uiteindelijk vernietigen",
            "Planten hebben geen water nodig als ze in een groepje staan"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin luidt dat een bos een solidaire gemeenschap is en dat het ware geheim onder onze voeten ligt."
    }
]

# ==============================================================================
# TEKSTEN EN VRAGEN VOOR TOETS 12 (§5 VASTE TEKSTSTRUCTUREN - TOETS E)
# ==============================================================================
plastic_alineas = [
    "Bijna iedereen heeft wel een heerlijk warme fleece trui, een ademend sportshirt of een paar nylon sokken in de kledingkast liggen. Synthetische kledingstoffen zoals polyester, acryl en polyamide zijn licht, kreukvrij en goedkoop te produceren. Weinig consumenten beseffen echter dat elke wasbeurt van deze kledingstukken leidt tot een onzichtbare milieuramp in onze waterwegen en oceanen.",
    "Het probleem ontstaat in de trommel van de wasmachine. Door de constante wrijving tussen kledingstukken breken microscopisch kleine plastic vezeltjes af van de stof. Bij een enkele wasbeurt van een fleece vest kunnen maar liefst een miljoen van deze microvezels vrijkomen en met het afvalwater weggespoeld worden.",
    "Omdat deze synthetische vezeltjes minuscuul zijn (vaak dunner dan een menselijke haar), glippen ze moeiteloos door de filters van onze rioolwaterzuiveringsinstallaties. Als gevolg hiervan stromen er dagelijks miljarden microplastics via beken en rivieren rechtstreeks de zee in.",
    "De ecologische gevolgen in zee zijn verwoestend. Kleine waterdiertjes, garnalen en vissen zien de minuscule plasticdeeltjes aan voor voedsel en eten ze op. Het plastic hoopt zich op in hun magen, waardoor ze verhongeren. Bovendien trekken microplastics giftige chemische stoffen uit het water aan als een magneet, waardoor het gif via visconsumptie uiteindelijk op onze eigen borden belandt.",
    "Gelukkig ontstaan er steeds meer maatregelen om dit probleem bij de bron aan te pakken. Wetenschappers ontwikkelen speciale waszakken en microplasticfilters voor wasmachines die vezels opvangen. Daarnaast experimenteren textielfabrikanten met biologisch afbreekbare garens op basis van algen en hennep.",
    "Kortom: zolang de kledingindustrie blijft leunen op goedkope synthetische vezels, blijven we de oceanen ongemerkt vervuilen. Een combinatie van strengere wetgeving voor wasmachinefilters en een bewuste keuze van consumenten voor natuurlijke stoffen is dringend noodzakelijk om dit plastic tij te keren."
]
card_plastic = maak_leestekst_card("Tekst A: De onzichtbare plaag in onze kleding", "Milieu & Samenleving, 2024", plastic_alineas, "6 alinea's")

communicatie_alineas = [
    "Stel je voor dat je een belangrijk bericht wilt sturen naar een vriend aan de andere kant van de wereld, en dat je drie maanden moet wachten tot je brief per zeilschip arriveert. Tegenwoordig sturen we binnen een fractie van een seconde een appje, foto of video naar iemand in Nieuw-Zeeland. Hoe heeft onze communicatietechnologie zich in twee eeuwen ontwikkeld van trage postkoets tot flitsend glasvezelnetwerk?",
    "Vroeger, tot diep in de negentiende eeuw, was communicatie gebonden aan fysieke verplaatsing. Berichten reisden zo snel als een rennend paard, een postduif of een schip kon varen. Belangrijk nieuws over oorlogen of verdragen deed er vaak weken of maanden over om de bevolking te bereiken.",
    "De eerste grote doorbraak kwam halverwege de negentiende eeuw met de uitvinding van de elektrische telegraaf en het morsealfabet. Voor het eerst in de geschiedenis kon informatie sneller reizen dan de mens zelf. Dankzij telegraafkabels op de oceaanbodem konden Europa en Amerika plotseling binnen enkele minuten met elkaar corresponderen. Snel daarna volgden de vaste telefoon en de draadloze radio.",
    "In de tweede helft van de twintigste eeuw voltrok zich een nog veel grotere digitale revolutie. De opkomst van computers, communicatiesatellieten en het wereldwijde internet maakte van onze aarde een 'global village'. Sinds de introductie van de smartphone rond 2007 dragen we een complete encyclopedie, filmcamera en zendmast in onze broekzak.",
    "En hoe ziet de toekomst van communicatie eruit? Wetenschappers werken al volop aan kwantuminternet: verbindingen die onkraakbaar veilig zijn en informatie met lichtsnelheid uitwisselen. Daarnaast experimenteren techbedrijven met holografische projecties en directe brein-computer-interfaces, waarbij gedachten zonder toetsenbord verzonden kunnen worden.",
    "Kortom: de manier waarop mensen contact onderhouden heeft in recordtijd een duizelingwekkende transformatie ondergaan. Van postduif tot smartphone is de afstand tussen mensen virtueel gekrompen tot nul; de grote uitdaging voor de toekomst is ervoor te zorgen dat we tussen al die razendsnelle schermen nog echt met elkaar blijven praten."
]
card_communicatie = maak_leestekst_card("Tekst B: Van postduif tot smartphone", "Geschiedenis & Techniek, 2025", communicatie_alineas, "6 alinea's")

vragen_ex12 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welke vaste tekststructuur herken je primair in Tekst A?",
        "opties": [
            "Oorzaak-gevolgstructuur",
            "Verleden-heden-toekomststructuur",
            "Beoordelingsstructuur",
            "Onderzoeksstructuur van een enquête"
        ],
        "antwoord": 0,
        "uitleg": "De tekst toont hoe het wassen van synthetische kleding (oorzaak) leidt tot microplastics in zee en giftige voedselketens (gevolgen)."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welke oorzaak voor het ontstaan van microvezels wordt in alinea 2 beschreven?",
        "opties": [
            "De mechanische wrijving tussen kledingstukken tijdens het wassen",
            "Het drogen van kleding in de felle zon",
            "Het strijken van overhemden met een te heet strijkijzer",
            "Het morsen van wasverzachter op synthetische stoffen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 wijst de constante wrijving tussen kledingstukken in de wastrommel aan als directe oorzaak van het afbreken van vezels."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Waarom komen de microvezels volgens alinea 3 gemakkelijk in rivieren en oceanen terecht?",
        "opties": [
            "Omdat ze te klein zijn om door waterzuiveringsinstallaties te worden tegengehouden",
            "Omdat riolen in Nederland direct uitmonden in zee zonder zuivering",
            "Omdat de filters van zuiveringsinstallaties in het weekend uitgeschakeld staan",
            "Omdat de vezels zwaarder zijn dan zand en direct naar de bodem zakken"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat de vezels vaak dunner zijn dan een haar en moeiteloos door de filters van waterzuiveringsinstallaties glippen."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welk ernstig gevolg voor de menselijke gezondheid wordt in alinea 4 genoemd?",
        "opties": [
            "Giftige deeltjes in vis kunnen via de voedselketen op ons eigen bord belanden",
            "Mensen krijgen huiduitslag van het dragen van katoenen shirts",
            "Drinkwater smaakt bitter door de aanwezigheid van zoutzuur",
            "Zwemmen in zee veroorzaakt acute ademnood"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 legt uit dat giftige stoffen via visconsumptie uiteindelijk in het menselijk lichaam belanden."
    },
    {
        "type": "waaronwaar",
        "figuur": card_plastic,
        "vraag": "Bij een enkele wasbeurt van een fleece vest kunnen wel een miljoen microvezels vrijkomen.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 vermeldt letterlijk dat er wel een miljoen microvezels per wasbeurt kunnen vrijkomen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_plastic,
        "vraag": "Microplastics stoten chemische gifstoffen in het zeewater direct af.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 4 stelt juist dat microplastics giftige chemische stoffen aantrekken als een magneet."
    },
    {
        "type": "invul",
        "figuur": card_plastic,
        "vraag": "De tekststructuur waarin het verband tussen aanleiding en uitkomst centraal staat heet de ____-structuur.",
        "antwoord": "oorzaak-gevolg",
        "uitleg": "Dit is de oorzaak-gevolgstructuur."
    },
    {
        "type": "open",
        "figuur": card_plastic,
        "vraag": "Welke twee oplossingen of maatregelen om het probleem te verkleinen worden in alinea 5 genoemd?",
        "sleutelwoorden": ["waszakken/filters/wasmachinefilters", "biologisch afbreekbare garens/algen/hennep/natuurlijke stoffen"],
        "minTreffers": 2,
        "modelantwoord": "Speciale waszakken en wasmachinefilters die vezels opvangen, en biologisch afbreekbare garens op basis van algen en hennep.",
        "uitleg": "Alinea 5 noemt waszakken/filters en biologisch afbreekbare garens van algen of hennep."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welk signaalwoord in alinea 3 geeft een direct gevolg aan?",
        "opties": [
            "Als gevolg hiervan",
            "Integendeel",
            "Desalniettemin",
            "Kortom"
        ],
        "antwoord": 0,
        "uitleg": "'Als gevolg hiervan' is een typisch signaalwoord van een oorzaak-gevolgrelatie."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Wat is het doel van de auteur in de slotalinea van Tekst A?",
        "opties": [
            "Oproepen tot strengere wetgeving en bewuste keuzes van consumenten",
            "Het faillissement eisen van alle kledingwinkels in Nederland",
            "Reclame maken voor een specifiek merk biologisch wasmiddel",
            "Aantonen dat fleece de warmste stof ter wereld is"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 formuleert een duidelijke oproep voor strengere regels en bewuste keuzes voor natuurlijke materialen."
    },
    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Welke vaste tekststructuur herken je in Tekst B?",
        "opties": [
            "Verleden-heden-toekomststructuur (historische structuur)",
            "Probleem-oplossingstructuur",
            "Voor- en nadelenstructuur",
            "Beoordelingsstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B behandelt chronologisch hoe communicatie verliep in het verleden (alinea 2 & 3), het heden (alinea 4) en de toekomst (alinea 5)."
    },
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Hoe verliep langeafstandscommunicatie tot diep in de negentiende eeuw volgens alinea 2?",
        "opties": [
            "Uitsluitend via fysieke verplaatsing per paard, postduif of schip",
            "Via ondergrondse glasvezelkabels van koper",
            "Via radiosignalen van vroege zendmasten",
            "Via rooksignalen die vanaf satellieten werden waargenomen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 vermeldt dat communicatie gebonden was aan fysieke verplaatsing (paard, postduif, schip)."
    },
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Waarom was de elektrische telegraaf in alinea 3 zo'n revolutionaire doorbraak?",
        "opties": [
            "Voor het eerst kon informatie sneller reizen dan de mens zelf kon bewegen",
            "Omdat iedereen plotseling gratis met elkaar kon bellen",
            "Omdat brieven voortaan per raketpost werden bezorgd",
            "Omdat morsecode de enige taal ter wereld werd"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 benadrukt dat informatie voor het eerst sneller reisde dan een mens fysiek kon bewegen."
    },
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Welke term gebruikt de auteur in alinea 4 om de wereld na de internetrevolutie te typeren?",
        "opties": [
            "Global village (mondiaal dorp)",
            "Digitale woestijn",
            "Elektrische jungle",
            "Stille oceaan"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 stelt dat internet en satellieten van onze aarde een 'global village' hebben gemaakt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_communicatie,
        "vraag": "Tot de negentiende eeuw deed belangrijk nieuws over oorlogen er vaak weken of maanden over om mensen te bereiken.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 vermeldt letterlijk dat belangrijk nieuws er vaak weken of maanden over deed."
    },
    {
        "type": "waaronwaar",
        "figuur": card_communicatie,
        "vraag": "Kwantuminternet is volgens alinea 5 een verouderde techniek die inmiddels niet meer gebruikt wordt.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 beschrijft kwantuminternet juist als een hypermoderne technologie voor de toekomst."
    },
    {
        "type": "invul",
        "figuur": card_communicatie,
        "vraag": "De tekststructuur die gebeurtenissen indeelt in vroeger, nu en later heet de ____ structuur.",
        "antwoord": "historische",
        "uitleg": "Dit heet de historische structuur (of verleden-heden-toekomststructuur)."
    },
    {
        "type": "open",
        "figuur": card_communicatie,
        "vraag": "Noem twee toekomstige communicatietechnologieën die in alinea 5 worden genoemd.",
        "sleutelwoorden": ["kwantuminternet", "holografische projecties/hologrammen", "brein-computer-interfaces/gedachten verzenden"],
        "minTreffers": 2,
        "modelantwoord": "Kwantuminternet, holografische projecties en directe brein-computer-interfaces.",
        "uitleg": "Alinea 5 noemt kwantuminternet, holografische projecties en brein-computer-interfaces."
    },
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Welke signaalwoorden markeren de chronologische overgangen tussen de alinea's 2, 4 en 5?",
        "opties": [
            "Vroeger - In de tweede helft van de twintigste eeuw - En hoe ziet de toekomst eruit",
            "Kortom - Samenvattend - Ten slotte",
            "Enerzijds - Anderzijds - Niettemin",
            "Doordat - Als gevolg van - Daardoor"
        ],
        "antwoord": 0,
        "uitleg": "Dit zijn de kenmerkende tijdsaanduidende signaalwoorden die de historische fasen markeren."
    },
    {
        "type": "mc",
        "figuur": card_communicatie,
        "vraag": "Welke relativerende gedachte geeft de auteur de lezer mee in de slotzin van Tekst B?",
        "opties": [
            "Dat we ondanks alle schermen nog wel echt met elkaar moeten blijven praten",
            "Dat smartphones binnenkort verboden moeten worden op straat",
            "Dat postduiven betrouwbaarder zijn dan glasvezelkabels",
            "Dat niemand meer brieven met de hand kan schrijven"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin stelt dat de grote uitdaging is om tussen al die schermen nog echt persoonlijk contact te behouden."
    }
]

# ==============================================================================
# TEKSTEN EN VRAGEN VOOR TOETS 13 (CURSUS 1 INTEGRALE EINDTOETS LEZEN - TOETS E)
# ==============================================================================
winkel_alineas = [
    "Je stapt op een regenachtige dinsdagmiddag een supermarkt binnen met één simpel doel: een pak melk en een halfje volkorenbrood halen. Drie kwartier later sta je bij de kassa met een overvol winkelwagentje vol koeken, speciale chips en luxe toetjes die je helemaal niet van plan was te kopen. Hoe slagen supermarkten er toch in om ons ongemerkt te verleiden tot impulsaankopen?",
    "Achter de inrichting van elke moderne supermarkt schuilt een uitgekiende psychologische strategie. Niets is er aan het toeval overgelaten. Zodra je binnenkomt, word je verwelkomd door de geur van versgebakken brood en felverlichte kraampjes met glanzend fruit. Deze aangename prikkels activeren onmiddellijk je hongergevoel en zetten je brein in een ontspannen, kooplustige stemming.",
    "Bovendien dwingt de plattegrond van de winkel je om zoveel mogelijk meters af te leggen. De basisproducten die iedereen dagelijks nodig heeft – zoals zuivel, eieren en brood – staan expres helemaal achterin de winkel opgesteld. Om die melk te pakken, móét je wel langs tientallen meters schappen vol verleidelijke aanbiedingen lopen.",
    "Ook op ooghoogte vindt een psychologische strijd plaats. Merken betalen grof geld voor de zogeheten 'grijphoogte' (tussen 1,20 en 1,60 meter), precies op de ooglijn van de gemiddelde consument. De goedkopere huismerken en kiloverpakkingen staan vrijwel altijd weggestopt op de onderste planken, waar je voor moet bukken.",
    "Tot slot is er de beruchte kassazone: de laatste horde. Terwijl je in de rij staat te wachten, word je omringd door chocoladerepen, kauwgom en batterijen. Na tientallen keuzes in de winkelpaden is je wilskracht uitgeput (een fenomeen dat psychologen 'keuzemoeheid' noemen), waardoor je voor het betalen alsnog zwicht voor een snelle zoete beloning.",
    "Kortom: de supermarkt is een doolhof vol psychologische trucs ontworpen om onze portemonnee lichter te maken. Wie zich wil wapenen tegen deze sluwe verleidingen, doet er verstandig aan om nooit met een rammelende maag boodschappen te doen en zich strikt aan een vooraf opgesteld boodschappenlijstje te houden."
]
card_winkel = maak_leestekst_card("Tekst A: De geheimen van het supermarktdoolhof", "Consumenten & Psychologie, 2024", winkel_alineas, "6 alinea's")

mars_alineas = [
    "\"Ik wil graag sterven op Mars, maar niet bij de landing,\" grapte tech-miljardair Elon Musk ooit. Zijn ambitieuze droom om binnen enkele decennia een permanente menselijke kolonie op de Rode Planeet te stichten, spreekt wereldwijd tot de verbeelding. Maar is het koloniseren van onze buurplaneet een realistisch toekomstperspectief, of een levensgevaarlijke en onbetaalbare illusie?",
    "Voorstanders van een bemande nederzetting op Mars wijzen op het overleven van de menselijke soort. Als de aarde onbewoonbaar dreigt te worden door een verwoestende asteroïdeninslag, een kernoorlog of onomkeerbare klimaatverandering, fungeert een tweede planeet als een ultieme reservekopie van de mensheid. Bovendien stimuleert een Mars-expeditie ongekende technologische doorbraken op het gebied van energie, waterrecycling en robotica.",
    "Tegenover deze dromen staat echter een ijskoude, dodelijke realiteit. Mars is een meedogenloze woestijn met een gemiddelde temperatuur van min 60 graden Celsius. De uiterst dunne atmosfeer bestaat voor 95 procent uit giftig koolstofdioxide en biedt geen enkele bescherming tegen dodelijke kosmische straling van de zon.",
    "Daar komt bij dat een reis naar Mars minstens zeven maanden duurt in een benauwde ruimtecapsule. Astronauten lopen een hoog risico op spierafbraak, botverlies en ernstige psychologische spanningen door langdurige opsluiting. Eenmaal geland zijn kolonisten levenslang opgesloten in ondergrondse bunkers.",
    "Tot slot zijn de financiële kosten astronomisch. Critici betogen dat de honderden miljarden euro's die een Marsmissie opslokt, oneindig veel nuttiger besteed kunnen worden aan het oplossen van armoede, honger en klimaatproblemen op onze eigen aarde.",
    "Al met al blijkt de droom van een Marskolonie vooralsnog een riskante sciencefictionfantasie. In plaats van miljarden te investeren in het bewoonbaar maken van een dode, bevroren planeet, moeten we onze energie en middelen eerst richten op het behoud van de enige planeet die ons daadwerkelijk in leven kan houden: onze eigen aarde."
]
card_mars = maak_leestekst_card("Tekst B: Wonen op Mars: utopie of waanzin?", "Ruimtevaart & Filosofie, 2025", mars_alineas, "6 alinea's")

vragen_ex13 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Welke techniek gebruikt de auteur in de inleiding van Tekst A om de lezer bij het onderwerp te betrekken?",
        "opties": [
            "Een herkenbare alledaagse anekdote over onverwachte impulsaankopen",
            "Het citeren van een middeleeuws gedicht over marktlui",
            "Een wiskundige formule over winstmarges van supermarktketens",
            "Een interview met een ontevreden vakkenvuller"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 beschrijft een herkenbare situatie: even melk halen en met een volle kar naar buiten lopen."
    },
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Wat is het doel van de vraag aan het einde van alinea 1 in Tekst A?",
        "opties": [
            "De centrale onderzoeksvraag van de tekst introduceren",
            "Twijfel zaaien over de kwaliteit van volkorenbrood",
            "De openingstijden van Nederlandse supermarkten bekritiseren",
            "Klanten aansporen om voortaan zelf brood te bakken"
        ],
        "antwoord": 0,
        "uitleg": "De vraag 'Hoe slagen supermarkten er toch in om ons ongemerkt te verleiden tot impulsaankopen?' vormt de probleemstelling."
    },
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Waarom staan basisproducten zoals melk en brood volgens alinea 3 helemaal achterin de winkel?",
        "opties": [
            "Zodat klanten verplicht langs alle andere verleidelijke schappen moeten lopen",
            "Omdat de koelcellen van vrachtwagens alleen aan de achterkant kunnen lossen",
            "Omdat brood in het donker minder snel beschimmelt",
            "Om te voorkomen dat kinderen bij de snoepafdeling kunnen komen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat de plattegrond klanten dwingt om langs zoveel mogelijk schappen met aanbiedingen te lopen."
    },
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Wat is het psychologische voordeel van 'grijphoogte' (1,20 tot 1,60 meter) in alinea 4?",
        "opties": [
            "Producten staan direct op de ooglijn van de consument en worden het snelst gepakt",
            "Kinderen kunnen er niet bij, waardoor snoepgoed heel blijft",
            "Vakkenvullers kunnen de schappen vullen zonder trapjes te gebruiken",
            "Het beschermt breekbare glazen potten tegen vallen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 stelt dat producten op ooghoogte direct in het zicht staan en daardoor het meest verkocht worden."
    },
    {
        "type": "waaronwaar",
        "figuur": card_winkel,
        "vraag": "De geur van vers brood en de aanblik van vers fruit bij de ingang zijn bedoeld om een kooplustig hongergevoel op te wekken.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 2 legt uit dat deze prikkels het hongergevoel activeren en consumenten ontspannen en kooplustig maken."
    },
    {
        "type": "waaronwaar",
        "figuur": card_winkel,
        "vraag": "Goedkopere huismerken worden in supermarkten altijd pontificaal op ooghoogte geplaatst.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 4 vermeldt dat goedkopere huismerken vrijwel altijd onderin worden weggestopt."
    },
    {
        "type": "invul",
        "figuur": card_winkel,
        "vraag": "Het psychologische fenomeen waarbij consumenten na veel keuzes minder wilskracht hebben heet ____.",
        "antwoord": "keuzemoeheid",
        "uitleg": "In alinea 5 staat letterlijk: 'een fenomeen dat psychologen keuzemoeheid noemen'."
    },
    {
        "type": "open",
        "figuur": card_winkel,
        "vraag": "Welke twee praktische adviezen geeft de auteur in de slotalinea om impulsaankopen te voorkomen?",
        "sleutelwoorden": ["rammelende maag/lege maag/niet met honger", "boodschappenlijstje/lijstje maken/aan lijstje houden"],
        "minTreffers": 2,
        "modelantwoord": "Nooit met een rammelende maag boodschappen doen en je strikt aan een boodschappenlijstje houden.",
        "uitleg": "Alinea 6 adviseert om niet met een lege maag te winkelen en je aan een lijstje te houden."
    },
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Welke vaste tekststructuur herken je in Tekst A?",
        "opties": [
            "Verschijnsel-verklaringstructuur (verschijnsel met achterliggende oorzaken en adviezen)",
            "Historische structuur van vroeger tot nu",
            "Beoordelingsstructuur van een consumentenbondtest",
            "Onderzoeksstructuur met statistische hypothesen"
        ],
        "antwoord": 0,
        "uitleg": "Tekst A beschrijft het verschijnsel van impulsaankopen en verklaart vervolgens stap voor stap de psychologische trucs."
    },
    {
        "type": "mc",
        "figuur": card_winkel,
        "vraag": "Wat is het voornaamste schrijfdoel van de auteur met Tekst A?",
        "opties": [
            "Informeren en adviseren: consumenten inzicht geven in marketingtrucs en tips geven",
            "Amuseren: grappen maken over overvolle winkelwagentjes",
            "Overtuigen: lezers overhalen om alleen nog online te bestellen",
            "Activeren: lezers oproepen tot een boycot van supermarkten"
        ],
        "antwoord": 0,
        "uitleg": "De auteur informeert over de psychologische trucs en adviseert hoe je je daartegen kunt wapenen."
    },
    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Welke aandachtstrekker gebruikt de auteur in de openingsalinea van Tekst B?",
        "opties": [
            "Een prikkelende uitspraak van een bekend tech-icoon (Elon Musk)",
            "Een lijst met natuurkundige berekeningen over raketbrandstof",
            "Een overzicht van alle asteroïdeninslagen op aarde",
            "Een beschrijving van een sciencefictionfilm uit de jaren tachtig"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 opent met een bekende quote van Elon Musk: 'Ik wil graag sterven op Mars, maar niet bij de landing.'"
    },
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Welk belangrijk argument van voorstanders voor een Marskolonie wordt in alinea 2 genoemd?",
        "opties": [
            "Het veiligstellen van het voortbestaan van de mensheid als 'reservekopie' bij aardse rampen",
            "Het exploiteren van rijke goudmijnen op de Rode Planeet",
            "Het verplaatsen van alle gevangenissen op aarde naar Mars",
            "Het bouwen van pretparken zonder zwaartekracht voor toeristen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 noemt het argument dat Mars fungeert als reservekopie van de mensheid mocht de aarde onbewoonbaar raken."
    },
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Welke dodelijke omstandigheden op Mars worden in alinea 3 opgesomd?",
        "opties": [
            "Extreme kou van min 60 graden, giftige CO2-atmosfeer en dodelijke kosmische straling",
            "Voortdurende vulkaanuitbarstingen en kokende oceanen van zoutzuur",
            "Reusachtige buitenaardse wezens die onder het zand leven",
            "Een zwaartekracht die zo sterk is dat botten direct breken"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 somt de gemiddelde temperatuur van -60 °C, 95% CO2 en dodelijke kosmische straling op."
    },
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Welke lichamelijke gevaren lopen astronauten tijdens de zeven maanden durende reis volgens alinea 4?",
        "opties": [
            "Ernstige spierafbraak en botverlies door gewichtloosheid",
            "Blindheid door het ontbreken van natuurlijk zonlicht",
            "Acute vergiftiging door bevroren ruimtestof",
            "Gewichtstoename door het calorierijke astronautenvoedsel"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 beschrijft de risico's op spierafbraak en botverlies tijdens de lange gewichtloze reis."
    },
    {
        "type": "waaronwaar",
        "figuur": card_mars,
        "vraag": "De atmosfeer op Mars biedt volgens alinea 3 volledige bescherming tegen schadelijke straling.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 3 stelt nadrukkelijk dat de dunne atmosfeer geen enkele bescherming biedt tegen kosmische straling."
    },
    {
        "type": "waaronwaar",
        "figuur": card_mars,
        "vraag": "Critici in alinea 5 stellen dat miljarden beter besteed kunnen worden aan acute problemen op aarde.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 5 bepleit dat geld beter naar armoede, honger en klimaat op aarde kan gaan."
    },
    {
        "type": "invul",
        "figuur": card_mars,
        "vraag": "De tekststructuur waarin voordelen en bezwaren tegenover elkaar worden gezet heet de ____-structuur.",
        "antwoord": "voor- en nadelen",
        "uitleg": "Dit is de voor- en nadelenstructuur."
    },
    {
        "type": "open",
        "figuur": card_mars,
        "vraag": "Welke twee bezwaren tegen de Marsreis worden in alinea 4 besproken?",
        "sleutelwoorden": ["spierafbraak/botverlies/lichamelijk", "psychologische spanningen/opsluiting/zeven maanden/bunkers"],
        "minTreffers": 2,
        "modelantwoord": "Spierafbraak en botverlies door gewichtloosheid, en ernstige psychologische spanningen door langdurige opsluiting.",
        "uitleg": "Alinea 4 noemt fysieke schade (spieren en botten) en mentale spanningen door opsluiting."
    },
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Wat is het standpunt van de auteur in de slotalinea (alinea 6) van Tekst B?",
        "opties": [
            "We moeten ons eerst concentreren op het behoud van onze eigen leefbare aarde",
            "Iedereen moet verplicht doneren aan het ruimtevaartprogramma van Elon Musk",
            "Binnen tien jaar moeten alle aardse industrieën naar Mars worden verplaatst",
            "Mars is de enige plek waar de mensheid vrede kan vinden"
        ],
        "antwoord": 0,
        "uitleg": "De auteur concludeert dat we onze energie moeten richten op het behoud van de enige planeet die ons kan onderhouden: de aarde."
    },
    {
        "type": "mc",
        "figuur": card_mars,
        "vraag": "Welke formulering in alinea 6 sluit de tekst af met een krachtige uitsmijter?",
        "opties": [
            "Het behoud van de enige planeet die ons daadwerkelijk in leven kan houden: onze eigen aarde",
            "En zo zal de mensheid overal in het heelal zegevieren",
            "Hopelijk zien we elkaar volgend jaar op de rode planeet",
            "Elon Musk had dus in alle opzichten gelijk"
        ],
        "antwoord": 0,
        "uitleg": "De laatste zin vormt een indringende uitsmijter waarin de aarde als onze enige echte thuishaven wordt benadrukt."
    }
]

# ==============================================================================
# BUNDELEN EN EXPORTEREN VAN EXAMEN 9 T/M 13
# ==============================================================================
examens = [
    {
        "file": "examen_9.js",
        "id": "ex-h3-nederlands-9",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 9 — §2 Inleiding en Slot (Toets D — Aandachtstrekkers & Probleemstellingen)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex9
    },
    {
        "file": "examen_10.js",
        "id": "ex-h3-nederlands-10",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 10 — §5 Vaste Tekststructuren (Toets D — Probleem-Oplossing & Voor- en Nadelen)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex10
    },
    {
        "file": "examen_11.js",
        "id": "ex-h3-nederlands-11",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 11 — §2 Inleiding en Slot (Toets E — Vraagstellingen, Citaten & Uitsmijters)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex11
    },
    {
        "file": "examen_12.js",
        "id": "ex-h3-nederlands-12",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 12 — §5 Vaste Tekststructuren (Toets E — Oorzaak-Gevolg & Historische Structuur)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex12
    },
    {
        "file": "examen_13.js",
        "id": "ex-h3-nederlands-13",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "mix",
        "titel": "Toets 13 — Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex13
    }
]

for ex in examens:
    balance_mc(ex["vragen"])
    filepath = os.path.join(out_dir, ex["file"])
    data_obj = {
        "id": ex["id"],
        "hoofdstuk": ex["hoofdstuk"],
        "hoofdstukTitel": ex["hoofdstukTitel"],
        "paragraaf": ex["paragraaf"],
        "titel": ex["titel"],
        "vak": ex["vak"],
        "icoon": ex["icoon"],
        "duurMin": ex["duurMin"],
        "vragen": ex["vragen"]
    }
    js_content = f"/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 1) */\nDURU.registerExamen({json.dumps(data_obj, indent=2, ensure_ascii=False)});\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Gereed: {filepath} ({len(ex['vragen'])} vragen)")

print("Alle 5 examens (9 t/m 13) succesvol gegenereerd!")
