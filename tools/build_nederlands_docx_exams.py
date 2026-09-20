# -*- coding: utf-8 -*-
"""
Generator voor 4 HAVO 3 Nederlands leestoetsen conform het Word-proeftoetsformaat:
- Toets 1: Officiële Proeftoets Lezen (Tekst 1 'De ziekte van Vrek' & Tekst 2 'Tour de fiets' uit het Word-bestand)
- Toets 2: §2 Inleiding en Slot (Leesteksten met vragen over aandachtstrekkers, onderwerpintroductie, slot en mooi rond)
- Toets 3: §5 Vaste Tekststructuren (Leesteksten met vragen over de 7 vaste structuren, tekstdoelen en signaalwoorden)
- Toets 4: Proeftoets Lezen HAVO 3 (Integrale Oefentoets B volgens het Word-formaat)
"""
import json
import os
import re

out_dir = "/home/mesuto/Documents/PROJELER/duru_okul/havo3/nederlands/js/data"
os.makedirs(out_dir, exist_ok=True)

# Helper om een scrollbare leestekst HTML-kaart te maken
def maak_leestekst_card(titel, bron, alineas, extra_info=""):
    h = ['<div class="leestekst-card" style="background:#f8fafc; border:1px solid #cbd5e1; border-left:4px solid #15803d; border-radius:12px; padding:16px 20px; margin-bottom:14px; max-height:350px; overflow-y:auto; font-size:14.5px; line-height:1.65; color:#1e293b; box-shadow:0 2px 8px rgba(0,0,0,0.04);">']
    h.append(f'  <div style="font-weight:800; color:#15803d; font-size:15px; margin-bottom:10px; display:flex; align-items:center; justify-content:space-between; border-bottom:1px solid #e2e8f0; padding-bottom:6px;">')
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

# ==============================================================================
# TEKSTEN UIT HET WORD-BESTAND (PROEFTOETS LEZEN 3H)
# ==============================================================================
vrek_alineas = [
    "Het is weer zover. Je zit op een terrasje met wat vrienden en iedereen heeft al een rondje gegeven. Iedereen, op één persoon na. En jawel hoor, die is toevallig net zijn portemonnee vergeten. Zuchtend kijken jij en de anderen elkaar aan: altijd hetzelfde met die gast. Zal jij dan nog maar eens wat gaan halen? ‘Graag’, zegt de ‘vergeetachtige’ vriend blij.",
    "De neiging om spullen of geld op te potten is op zich niet gek, zegt sociaalpsycholoog Terri Seuntjens van Tilburg University. Zij onderzoekt een fenomeen dat veel op gierigheid lijkt: hebzucht. ‘Terwijl gierigaards willen houden wat ze al hebben, willen hebzuchtige mensen steeds meer. Deze eigenschappen gaan vaak samen.’",
    "Volgens Seuntjens zijn gierigheid en hebzucht normale, nuttige eigenschappen. ‘Ze kunnen belangrijk zijn om te overleven. Als je in de oertijd goed was in het hamsteren van voedsel, wist je zeker dat je een barre winter overleefde. Nu hebben we die eigenschap niet echt meer nodig, want hier in het westen is altijd genoeg te krijgen.’",
    "De meeste mensen storen zich aan vrekkig gedrag, omdat we hebben geleerd dat delen nodig is. Niet dat we zulke lieve wezens zijn. We geven graag, maar we verwachten daarvoor wel iets terug. Het tit for tat-principe (‘voor wat hoort wat’) heet dat. Geef je iets, dan staat iemand bij je in het krijt. Je verwacht dat je er wel weer een keer iets voor terugkrijgt (hulp, een drankje of ander lekkers), wat een band schept. Alleen houdt de gierigaard zich niet aan die voor-wat-hoort-wat-regel. Wat je hem ook geeft, hij geeft niets terug.",
    "Gierigaards lappen de voor-wat-hoort-wat-gedragscode aan hun laars doordat ze speciaal zijn. ‘Ze hebben een, zoals dat heet, dwangmatige persoonlijkheid’, vertelt hoogleraar klinische psychologie Willem van der Does, verbonden aan de Universiteit Leiden. ‘Als je altijd maar kortingsbonnen uitknipt of altijd in de kou zit omdat de thermostaat laag moet, terwijl je wel genoeg geld hebt, dan is je zuinigheid weinig functioneel meer.’ Dwangmatige types houden er een strenge en perfectionistische levensstijl op na. ‘Ze willen alles goed doen en onder controle houden. Orde en perfectie, daar draait het om.’ Zulke mensen zijn vaak bang om de controle te verliezen in hun werk of om zich in emoties te verliezen. Ook willen ze hun uitgaven onder controle houden. ‘Dat komt voort uit angst,’ zegt Van der Does. ‘Want je weet maar nooit. Straks is je geld op en dan heb je niets meer.’",
    "‘Gierigheid is niet aangeboren’, zegt Van der Does. ‘Extreem gierige mensen zijn erg bang om zonder geld te zitten. Vermoedelijk raakt het angstcircuit in hun hersenen sneller geprikkeld dan gemiddeld.’ De angst begint in het midden van het brein. Vandaar wordt de angstreactie (‘O nee, ik moet betalen!’) doorgegeven aan een ander gebied. Normaal gesproken worden dan de bange reacties gedempt (‘Rustig maar, geld uitgeven is niet levensbedreigend’). Werkt die ‘demping’ niet goed, dan kun je het gevoel krijgen dat geld uitgeven geen goed idee is.",
    "Of zo’n ’bang’ brein je daadwerkelijk gierig maakt, is sterk afhankelijk van je omgeving, zegt Van der Does. ‘Ben je altijd heel voorzichtig opgevoed, dan is de kans groter dat je een angstig en gierig mens wordt. En als je grote schaarste hebt meegemaakt, kun je doorslaan in zuinigheid.’ Daarom ziet Van der Does vaak erg gierig gedrag bij oude mensen die de Tweede Wereldoorlog nog hebben meegemaakt.’ Zij kampten met honger en armoede, en leven nog steeds met de angst dat hun geld of eten opraakt.’",
    "Sommige sociale kringen kunnen je ook stimuleren in gierigheid en inhaligheid, weet sociaalpsycholoog Seuntjens. ‘Onder beurshandelaren is het verzamelen van zoveel mogelijk geld juist een positieve eigenschap. ‘Denk maar aan de film Wall Street uit de jaren tachtig, met de bekende quote: ‘Greed is good!’ (Hebzucht is goed!). In religieuze kringen worden gierigheid en hebzucht echter helemaal niet gewaardeerd. ‘In het christendom is hebzucht een van de zeven hoofdzonden. Ook in de islam, het boeddhisme en het jodendom wordt hebzucht of gierigheid ten koste van anderen als iets slechts gezien.’ Het ligt er dus maar net aan in wat voor omgeving je verkeert, of waar je geboren bent.",
    "De krenterige vriend die nooit rondjes geeft, kun je gewoon vertellen wat je van zijn gierige trekken en gedrag vindt. Als hij daar niet naar luistert, heb je kans dat zijn dwangmatigheid zich ontwikkelt tot een stoornis, een ‘obsessieve compulsieve persoonlijkheidsstoornis’ (OCP), zoals het heet in het handboek voor de psychiatrie. Waar ligt de grens? ‘Die is moeilijk te bepalen’, zegt Van der Does. ‘Iemand die aan zo’n stoornis lijdt, ziet vaak zelf het probleem niet. Het kwartje valt pas als de omgeving gaat klagen. Maar dan nog voelt iemand zich vooral onbegrepen. Wordt hij uiteindelijk ongelukkig van zijn gierigheid, dan spreek je van OCP.’",
    "Daarvoor kun je in therapie gaan. Dwangmatig gierig gedrag kan verbeteren door iemand te laten begrijpen dat zijn gedrag onredelijk is. Om dat te bereiken laat een therapeut zo iemand bijvoorbeeld iedere week een opdracht doen om zijn gierige gewoontes te doorbreken. ‘Dat gaat in stapjes’, zegt Van der Does. ‘Stel dat iemand geen rondjes wil geven. Dan is hij waarschijnlijk bang dat mensen van hem willen profiteren. En dan kan hij al zijn geld kwijtraken. Dus geef je als opdracht: geef deze week eens een rondje en kijk wat er gebeurt. Dan merkt hij dat anderen geen misbruik van hem maken, maar het gewoon waarderen als hij ook eens een keer betaalt.’",
    "Een echte gierigaard kent dus niet het tit for tat-principe, is snel bang om geld uit te geven en lijdt mogelijk aan een persoonlijkheidsstoornis. Gelukkig kan hij wel leren dat geven ook best leuk is, maar voordat hij dat echt doorheeft, gaan er wel een paar jaar overheen. Daarom moet je tot die tijd – als je met hem op een terrasje zit – nog even op je tanden bijten."
]
card_vrek = maak_leestekst_card("Tekst 1: De ziekte van Vrek", "Melanie Metz, Quest, januari 2014", vrek_alineas, "11 alinea's")

fiets_alineas = [
    "De Tour de France is weer begonnen. De komende drie weken fietsen 198 wielrenners zo’n 3500 kilometer, waarbij ze strijden om drie truien: de gele, de groene en die met bolletjes. Natuurlijk doen ze dat niet op huis-tuin-en-keukenfietsen, maar op peperdure, speciaal voor hen ontwikkelde hightechfietsen. Toch zouden de wielrenners die aan het eind van de negentiende eeuw leefden, er zo op kunnen wegrijden. Aan de basis is namelijk niets veranderd. Wel zijn er uiteraard details gewijzigd.",
    "In 1885 werden de ‘tweelingwielen’ geïntroduceerd, onder de naam Rover Safety Bicycle. Zoals de naam al zegt, was de Rover Safety Bicycle vooral veiliger dan de toen bestaande fietsen. Eerder trokken wielrenners veel publiek met spectaculaire races op de ‘hoge bi’: de fiets met het hoge voorwiel. Hoe hoger het wiel, hoe harder je kon. Maar er gebeurden veel ongelukken. Alleen al het opstappen vereiste behoorlijk wat acrobatiek.",
    "De Britse fietsontwerper John Kemp Starley introduceerde de Rover met ketting en twee wielen van gelijke grootte. Het werd en bleef de standaard voor wielrenners en gewone fietsers. De Rover ontketende eveneens een grote verandering buiten de sport. Het veilige ontwerp zorgde ervoor dat ook vrouwen gingen fietsen en dus verder konden reizen. Het betekende een belangrijke ontwikkeling in de vrouwenemancipatie.",
    "Drie jaar later kwamen er luchtbanden. Ook dat was een verbetering, want op de eerste Rover werd je behoorlijk door elkaar geschud. Je reed immers op ijzer of op hout. Zelfs massief rubberen banden brachten nog niet de gewenste combinatie van comfort en snelheid. Toen de Schotse dierenarts John Dunlop zijn zoontje op een driewieler zag rijden, kwam hij op het idee een opblaasbare band te maken. Eerst werd hij nog uitgelachen omdat de band te snel lek zou zijn. Maar hij legde sceptici het zwijgen op door een stevige rubber buitenband te introduceren. Vanaf de jaren 90 van de 19de eeuw rijdt iedere wielrenner zijn wedstrijden op luchtbanden.",
    "Op luchtbanden sneuvelde het ene record na het andere. Dat was de beste reclame voor Dunlop en al helemaal toen de Ierse wielrenner Richard James Mecredy in 1890 alle vier de onderdelen van het Engelse kampioenschap op deze banden won. De renner hielp zichzelf daarmee ook: hij was partner in Dunlops Pneumatic Tyre Company. Tegenwoordig rijdt het peloton van de Tour de France op dunnere en lichtere banden met een profiel dat minder weerstand geeft. De belangrijkste aanpassing is de druk die de band aankan. De meeste wegwielrenners rijden met ongeveer 9 bar in de banden. Bij hoge spanning heb je minder weerstand van de weg. Bij deze hoge druk waren de eerste Dunlopbanden al lang geknapt.",
    "In 1940 werd de Campagnolo-derailleur ontwikkeld. Sinds eind 19de eeuw was er gezocht naar een goed versnellingssysteem, maar jarenlang lukte het niet om zonder afstappen de ketting om een ander tandwiel te leggen. Met een derailleur kun je al fietsend schakelen met een hendeltje. De derailleur van de fietsenbouwer Tullio Campagnolo uit Italië was niet de eerste, wel de beste.",
    "Wel bleef schakelen in het begin van het tijdperk van de derailleur iets voor specialisten. Met de populaire Campagnolo Cambio Corsa moest je rijdend twee hendels aan de achtervork verstellen. De Italiaanse kampioen Gino Bartali won in 1948 de Tour de France onder meer omdat niemand zo goed kon schakelen als hij. Tegenwoordig is schakelen een eitje. De hendels verhuisden eerst naar het frame, maar ze zijn nu zelfs volledig weggewerkt in de handvatten. Wielrenners hoeven slechts een tikje met hun vinger te geven om lichter te klimmen.",
    "Sinds de jaren ’80 van de twintigste eeuw kennen we de vernieuwingen, waarmee geprobeerd wordt de luchtweerstand – de grootste vijand van de snelheidsduivel – te verkleinen. In de beginjaren van het wielrennen werd het gebogen stuur al geïntroduceerd voor een gestroomlijnde zit. Maar het duurde tot de jaren ‘80 van de vorige eeuw voordat wielrennen echt secondespel werd. Seconden die je kon winnen met aerodynamica. Greg Lemond, de eerste Amerikaanse winnaar van de Tour, verscheen in 1989 aan de start van de laatste tijdrit met een futuristische helm en een dicht wiel. Hij won dat jaar met het kleinste verschil ooit. Na 3 weken koersen over 3285 kilometer was Lemond in totaal 8 seconden sneller dan zijn rivaal Laurent Fignon. Wat zou er gebeurd zijn als Fignon niet met los wapperende paardenstaart van start gegaan was?",
    "In de loop der jaren is veel winst geboekt met de kleding: strakke, gladde kleding maakt snel. En natuurlijk wordt tegenwoordig elk onderdeel in de windtunnel getest.",
    "Nog een belangrijke ontwikkeling is het klikpedaal, uit 1984. Wielrenners reden lang met bandjes om hun voeten. Maar deze aangespen kostte tijd en bandjes waren gevaarlijk bij valpartijen: je voet schoot niet direct los. Het klikpedaal bracht uitkomst. Speciale schoenen klikken vast in het pedaal. Ze schieten los bij een val, en je kunt er harder aan ‘trekken’. Het klikpedaal is nu de standaard in het peloton. Bij de start van een race hoor je honderden klikjes.",
    "De laatste vernieuwing is het carbonframe. De eerste racefietsen waren van staal en wogen meer dan 20 kilo. Later werden uitgeholde frames en onderdelen van aluminium geïntroduceerd. Die waren allemaal bedoeld om de fiets lichter en dus sneller te maken. Maar de grootste revolutie kwam in 1992 toen de Brit Chris Boardman op de Olympische Spelen in de wielerbaan kwam met een hypermoderne aerodynamische fiets. Gemaakt van carbon, ofwel koolstofvezel. Dat is heel licht en toch erg stijf. Carbon wordt ook veel in de vliegtuigindustrie gebruikt. Met dat moderne materiaal haalde Boardman goud op de 4 kilometer achtervolging. Mede dankzij carbon onderdelen zijn fietsen steeds maar lichter geworden. Bouwers moeten hun fietsen inmiddels verzwaren om te voldoen aan de regels van de UCI – de Union Cycliste Internationale oftewel de Internationale Wielerunie. Die schrijven voor dat een racefiets minimaal 6,2 kilo moet wegen."
]
card_fiets = maak_leestekst_card("Tekst 2: Tour de fiets", "Leendert van der Valk, Quest, juli 2012", fiets_alineas, "11 alinea's")

# ==============================================================================
# EXAMEN 1: OFFICIËLE PROEFTOETS LEZEN (TEKST 1 & TEKST 2)
# ==============================================================================
vragen_ex1 = [
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een tekst waarin de chronologische ontwikkeling van een onderwerp door de tijd heen wordt geschetst?",
        "opties": [
            "Aspectenstructuur",
            "Verleden-heden(-toekomst)structuur",
            "Probleem-oplossingsstructuur",
            "Voor- en nadelenstructuur"
        ],
        "antwoord": 1,
        "uitleg": "Wanneer een tekst een historische en chronologische ontwikkeling beschrijft, spreken we van de verleden-heden(-toekomst)structuur."
    },
    {
        "type": "mc",
        "figuur": card_vrek,
        "vraag": "Wat is het centrale onderwerp van Tekst 1 (De ziekte van Vrek)?",
        "opties": [
            "Gierigheid",
            "Vergeetachtigheid",
            "Sparen",
            "Hebzucht"
        ],
        "antwoord": 0,
        "uitleg": "Het onderwerp is in één woord samen te vatten: gierigheid (vrekkig gedrag, de oorzaken en behandeling)."
    },
    {
        "type": "mc",
        "figuur": card_vrek,
        "vraag": "Op welke manier probeert de schrijver in alinea 1 van Tekst 1 de lezer nieuwsgierig te maken?",
        "opties": [
            "Door een situatie in het heden te vergelijken met het verleden",
            "Door in te spelen op de actualiteit",
            "Door een herkenbaar voorbeeld of anekdote te geven",
            "Door te laten zien dat het nuttig is voor de lezer"
        ],
        "antwoord": 2,
        "uitleg": "De auteur begint met een herkenbare anekdote / voorbeeld op een terrasje met vrienden waar iemand zijn portemonnee 'vergeten' is."
    },
    {
        "type": "mc",
        "figuur": card_vrek,
        "vraag": "Welke vaste structuur herken je primair in Tekst 1 (De ziekte van Vrek)?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verklaringsstructuur",
            "Vraag-antwoordstructuur",
            "Aspectenstructuur"
        ],
        "antwoord": 1,
        "uitleg": "Tekst 1 verklaart het verschijnsel gierigheid: kenmerken, psychologische en biologische oorzaken, en hoe het te behandelen is (een verklaringsstructuur)."
    },
    {
        "type": "open",
        "figuur": card_vrek,
        "vraag": "In alinea 3 stelt Seuntjens dat gierigheid en hebzucht normale, nuttige eigenschappen kunnen zijn. Waarom vindt ze dat volgens de tekst?",
        "sleutelwoorden": ["overleven/overleving", "oertijd/vroeger", "hamsteren/voedsel", "winter"],
        "minTreffers": 1,
        "modelantwoord": "Omdat het in de oertijd belangrijk was om te overleven: wie goed voedsel kon hamsteren, overleefde een barre winter.",
        "uitleg": "In alinea 3 legt Seuntjens uit dat voedsel hamsteren in de oertijd essentieel was om een strenge winter te overleven."
    },
    {
        "type": "open",
        "figuur": card_vrek,
        "vraag": "Leg uit wat volgens alinea 4 het zogeheten 'tit for tat-principe' inhoudt in menselijke relaties.",
        "sleutelwoorden": ["voor wat hoort wat", "terugkrijgen/terug", "verwachten", "delen"],
        "minTreffers": 1,
        "modelantwoord": "Het betekent 'voor wat hoort wat': als je iets aan iemand geeft, verwacht je daar op termijn ook weer iets voor terug.",
        "uitleg": "Alinea 4 omschrijft dit als de regel 'voor wat hoort wat': geven schept een verwachting dat je later iets terugkrijgt."
    },
    {
        "type": "mc",
        "figuur": card_vrek,
        "vraag": "Wat ligt er volgens hoogleraar Van der Does in alinea 5 ten diepste aan de basis van een dwangmatige persoonlijkheid?",
        "opties": [
            "Controledrift",
            "Perfectionisme",
            "Emoties",
            "Angst"
        ],
        "antwoord": 3,
        "uitleg": "In alinea 5 zegt Van der Does letterlijk: 'Dat komt voort uit angst... Straks is je geld op en dan heb je niets meer.'"
    },
    {
        "type": "open",
        "figuur": card_vrek,
        "vraag": "Welke twee omgevingsfactoren noemt Van der Does in alinea 7 als verklaring voor extreem zuinig gedrag?",
        "sleutelwoorden": ["voorzichtig/opvoeding/opgevoed", "schaarste/oorlog/armoede/honger"],
        "minTreffers": 1,
        "modelantwoord": "Een zeer voorzichtige opvoeding en het meegemaakt hebben van grote schaarste, honger of oorlog.",
        "uitleg": "Alinea 7 noemt (1) voorzichtig zijn opgevoed en (2) grote schaarste/armoede (zoals in de Tweede Wereldoorlog) hebben meegemaakt."
    },
    {
        "type": "open",
        "figuur": card_vrek,
        "vraag": "Welke tegenstelling herken je in alinea 8? Noteer ook het signaalwoord waaraan je de tegenstelling herkent.",
        "sleutelwoorden": ["echter", "positief/goed/succes/winst", "slecht/zonde/afkeuren/veroordelen"],
        "minTreffers": 1,
        "modelantwoord": "Onder beurshandelaren geldt hebzucht als positief, terwijl het in religies als zonde of iets slechts wordt gezien. Het signaalwoord is 'echter'.",
        "uitleg": "Alinea 8 toont aan dat Wall Street hebzucht toejuicht ('Greed is good'), maar religies het veroordelen als hoofdzonde. Het signaalwoord is 'echter'."
    },
    {
        "type": "waaronwaar",
        "figuur": card_vrek,
        "vraag": "Volgens klinisch psycholoog Van der Does in alinea 6 is extreme gierigheid een strikt aangeboren eigenschap waar je hersenen niets aan kunnen veranderen.",
        "antwoord": False,
        "uitleg": "Onwaar. In alinea 6 zegt Van der Does letterlijk: 'Gierigheid is niet aangeboren.'"
    },
    {
        "type": "invul",
        "figuur": card_vrek,
        "vraag": "De tekst heeft als titel 'De ziekte van Vrek'. In welke alinea van Tekst 1 wordt gierigheid voor het eerst expliciet als een officiële psychiatrische stoornis (OCP) benoemd? (Noteer alleen het alineanummer)",
        "antwoord": "9|alinea 9",
        "uitleg": "In alinea 9 wordt de grens besproken en wordt OCP (obsessieve compulsieve persoonlijkheidsstoornis) voor het eerst genoemd."
    },
    {
        "type": "mc",
        "figuur": card_vrek,
        "vraag": "Welke van de onderstaande zinnen verwoordt het meest treffend de hoofdgedachte van Tekst 1?",
        "opties": [
            "De meeste mensen storen zich aan gierige vrienden omdat ze zich niet houden aan de etiquette op het terras.",
            "Gierigheid komt voort uit angst en kan een psychische stoornis worden, maar is met gerichte therapie te behandelen.",
            "In de oertijd was voedsel hamsteren noodzakelijk, maar tegenwoordig is het een overbodige eigenschap.",
            "Beurshandelaren laten zien dat hebzucht een nuttige drijfveer is voor maatschappelijk succes."
        ],
        "antwoord": 1,
        "uitleg": "De tekst draait om de psychologie van gierigheid (angst en stoornis) en sluit af met de mogelijkheid van gedragstherapie."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een betoog waarin een mening of stellingname centraal staat en met argumenten wordt verdedigd?",
        "opties": [
            "Aspectenstructuur",
            "Probleem-oplossingsstructuur",
            "Argumentatiestructuur",
            "Verklaringsstructuur"
        ],
        "antwoord": 2,
        "uitleg": "Een tekst waarin een standpunt met argumenten wordt onderbouwd, volgt de argumentatiestructuur."
    },
    {
        "type": "mc",
        "figuur": card_fiets,
        "vraag": "Wat is het centrale onderwerp van Tekst 2 (Tour de fiets)?",
        "opties": [
            "De geschiedenis van de (race)fiets",
            "Speciaal ontwikkelde hightechfietsen",
            "Verschillende racefietsontwerpen",
            "Vernieuwingen aan de (race)fiets"
        ],
        "antwoord": 3,
        "uitleg": "De tekst behandelt stap voor stap de verschillende technische vernieuwingen die aan de racefiets zijn aangebracht."
    },
    {
        "type": "mc",
        "figuur": card_fiets,
        "vraag": "Op welke manier probeert de auteur in alinea 1 van Tekst 2 de aandacht van de lezer te vangen?",
        "opties": [
            "Door in te spelen op de actualiteit",
            "Door een historische anekdote te vertellen",
            "Door tot de verbeelding sprekende statistieken te noemen",
            "Door de lezer persoonlijk aan te spreken op zijn eigen fietsgedrag"
        ],
        "antwoord": 0,
        "uitleg": "De auteur speelt direct in op een actuele sportgebeurtenis: 'De Tour de France is weer begonnen.'"
    },
    {
        "type": "waaronwaar",
        "figuur": card_fiets,
        "vraag": "De auteur van Tekst 2 beweert dat wielrenners uit het eind van de 19e eeuw op moderne racefietsen totaal niet zouden kunnen wegrijden omdat het basisprincipe van de fiets compleet veranderd is.",
        "antwoord": False,
        "uitleg": "Onwaar. In alinea 1 staat juist: 'Toch zouden de wielrenners die aan het eind van de negentiende eeuw leefden, er zo op kunnen wegrijden. Aan de basis is namelijk niets veranderd.'"
    },
    {
        "type": "open",
        "figuur": card_fiets,
        "vraag": "In alinea 2 en 3 wordt een keten van oorzaak en gevolg beschreven rondom de Rover Safety Bicycle. Wat was het maatschappelijke gevolg van het veilige ontwerp buiten de sport?",
        "sleutelwoorden": ["vrouwen/vrouw", "fietsen/reizen/mobiliteit", "emancipatie/vrouwenemancipatie"],
        "minTreffers": 1,
        "modelantwoord": "Vrouwen konden hierdoor veilig gaan fietsen en verder reizen, wat een grote bijdrage leverde aan de vrouwenemancipatie.",
        "uitleg": "Alinea 3 vermeldt dat het veilige ontwerp ervoor zorgde dat ook vrouwen gingen fietsen, wat een belangrijke stap was in de vrouwenemancipatie."
    },
    {
        "type": "invul",
        "figuur": card_fiets,
        "vraag": "Welk signaalwoord van tegenstelling gebruikt de auteur in alinea 4 om te laten zien dat John Dunlop sceptici toch wist te overtuigen met zijn luchtband?",
        "antwoord": "maar",
        "uitleg": "In alinea 4 staat: 'Maar hij legde sceptici het zwijgen op...'"
    },
    {
        "type": "open",
        "figuur": card_fiets,
        "vraag": "Welke tegenstelling bevat alinea 7 met betrekking tot het schakelen op de racefiets?",
        "sleutelwoorden": ["specialisten/lastig/moeilijk/hendels", "tegenwoordig/nu/makkelijk/eitje/vingertikje"],
        "minTreffers": 1,
        "modelantwoord": "In het begin was schakelen heel lastig en iets voor specialisten met hendels aan de achtervork, terwijl het tegenwoordig 'een eitje' is met een vingertikje aan het handvat.",
        "uitleg": "Alinea 7 zet het moeilijke handmatige schakelen uit het begin af tegen het vederlichte schakelen van nu."
    },
    {
        "type": "mc",
        "figuur": card_fiets,
        "vraag": "Welke zin geeft het beste de hoofdgedachte van Tekst 2 (Tour de fiets) weer?",
        "opties": [
            "De belangrijkste verandering aan de fiets is de derailleur, omdat die bij vrijwel alle fietsen wordt ingebouwd.",
            "Dankzij alle vernieuwingen rijden wielrenners in de Tour de France veel sneller dan vroeger.",
            "In de laatste 130 jaar heeft de fiets allerlei vernieuwingen ondergaan, maar de basis is hetzelfde gebleven.",
            "Koolstofvezel en aerodynamica hebben de wielersport veranderd in een puur technologisch secondespel."
        ],
        "antwoord": 2,
        "uitleg": "De kernboodschap van de tekst is dat hoewel er talloze details zijn verbeterd (banden, derailleur, kleding, frame), de basis van de tweewieler ongewijzigd is."
    }
]

ex1_data = {
    "id": "ex-h3-nederlands-1",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "mix",
    "titel": "Toets 1 — Officiële Proeftoets Lezen (Tekst 1 & 2)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "📋",
    "duurMin": 30,
    "vragen": vragen_ex1
}

# ==============================================================================
# TEKSTEN VOOR TOETS 2: §2 INLEIDING EN SLOT
# ==============================================================================
slaap_alineas = [
    "In de zestiende eeuw, toen schilder Pieter Bruegel het winterse dorpsleven vastlegde, kropen gezinnen al vroeg bij het haardvuur onder dikke wollen dekens. Zonder elektrisch licht volgde de mens vanzelf het ritme van zonsopgang en zonsondergang. Tegenwoordig kijken we tot diep in de nacht naar oplichtende schermen en bepalen we met één druk op de knop ons eigen daglicht. Maar kan ons oeroude lichaam die moderne 24-uurseconomie wel bijbenen?",
    "Die vraag houdt neurowetenschappers al jaren bezig. Want hoewel we een derde van ons leven slapend doorbrengen, beschouwden veel mensen slaap lang als verloren tijd. 'Slaap is voor watjes', riepen zakenmensen in de jaren tachtig trots. Inmiddels weten we wel beter: slaap is geen passieve ruststand, maar een hyperactieve onderhoudsbeurt voor lichaam en geest.",
    "Tijdens een gezonde nachtrust doorloopt ons brein meerdere cycli van ongeveer anderhalf uur. Daarin wisselen lichte slaap, diepe herstelslaap en de zogeheten REM-slaap (waarin we levendig dromen) elkaar af. Tijdens de diepe slaap spoelt het hersenvocht giftige eiwitten weg die zich overdag hebben opgehoopt. De REM-slaap helpt juist bij het ordenen van emoties en het opslaan van leerstof in het langetermijngeheugen.",
    "Wie structureel te weinig slaapt, merkt dat onmiddellijk. Het reactievermogen daalt, het humeur verslechtert en het immuunsysteem verzwakt. Onderzoek van de Universiteit van Amsterdam toont aan dat middelbare scholieren die minder dan zeven uur per nacht slapen, gemiddeld een vol punt lager scoren op proefwerken.",
    "Toch is de verleiding om laat op te blijven groot, vooral door sociale media en streamingdiensten. Het blauwe licht van telefoons en tablets onderdrukt de aanmaak van melatonine, het slaaphormoon dat het brein het sein geeft dat de nacht is aangebroken.",
    "Gelukkig is een verstoord slaapritme te herstellen met eenvoudige aanpassingen: vaste bedtijden aanhouden, schermen minstens een uur voor het slapengaan uitschakelen en overdag voldoende natuurlijk daglicht opzoeken. Een koele, donkere slaapkamer doet de rest.",
    "Al met al is slaap geen overbodige luxe, maar een eerste levensbehoefte die onze gezondheid en schoolprestaties rechtstreeks bepaalt. Wie zijn brein overdag maximaal wil laten presteren, moet het 's nachts de rust gunnen die het verdient. Dus leg die telefoon vanavond eens wat eerder weg en kruip lekker onder de wol."
]
card_slaap = maak_leestekst_card("Tekst A: De geheimen van de biologische klok", "Natuurwetenschap & Gezondheid, 2025", slaap_alineas, "7 alinea's")

telefoon_alineas = [
    "Op een maandagochtend in september heerst er een ongewone stilte op het schoolplein van het Rembrandt College. Waar voorheen tientallen leerlingen gebogen zaten over hun oplichtende telefoons, klinkt nu gelach en het getik van een tafelvoetbalspelletje. De school voerde namelijk een strikt smartphoneverbod in: 'thuis of in de kluis'.",
    "Deze maatregel staat niet op zichzelf. Sinds de overheid landelijke richtlijnen opstelde tegen mobiele telefoons in de klas, worstelen veel scholen met de vraag: hoe creëren we een gezonde balans tussen digitale vaardigheden en ongestoorde lesaandacht?",
    "Tegenstanders van het verbod voeren aan dat de smartphone niet meer weg te denken is uit de maatschappij en dat scholen jongeren juist moeten leren omgaan met digitale prikkels. Bovendien wordt de telefoon soms handig ingezet voor educatieve quizzen of roosters.",
    "Onderwijskundigen en psychologen wijzen daarentegen op de harde cijfers: zelfs een telefoon die stil op de hoek van de tafel ligt, slurpt ongemerkt concentratie weg. Het brein staat voortdurend in de 'paraat-stand', wachtend op een trilling of pop-upmelding.",
    "De eerste resultaten van scholen met een kluisjesbeleid zijn veelbelovend. Docenten melden dat leerlingen aanzienlijk alerter zijn tijdens de instructie en dat er tijdens tussenuren spontaan meer met elkaar wordt gepraat en gesport.",
    "Natuurlijk lost een verbod op school niet alle digitale problemen op. Cyberpesten en verslavende algoritmes verdwijnen niet zodra de schoolbel om half vier gaat; dat vraagt ook om duidelijke afspraken thuis.",
    "Kortom: de smartphonevrije school blijkt een verademing voor de concentratie en sociale sfeer in de klas. Het verbod geeft leerlingen de broodnodige rust om weer echt te leren en contact te maken. Laten we die rust koesteren, zodat school weer een plek wordt voor ontmoeting en focus."
]
card_telefoon = maak_leestekst_card("Tekst B: De smartphone op school: zegen of ramp?", "Onderwijs & Samenleving, 2024", telefoon_alineas, "7 alinea's")

# ==============================================================================
# EXAMEN 2: §2 INLEIDING EN SLOT
# ==============================================================================
vragen_ex2 = [
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke beproefde aandachtstrekker herken je in alinea 1 van Tekst A?",
        "opties": [
            "Een verwijzing naar iets uit de geschiedenis",
            "Het noemen van actuele rampencijfers",
            "Een citaat van een bekende politicus",
            "Een persoonlijke aanleiding van de schrijver"
        ],
        "antwoord": 0,
        "uitleg": "De auteur grijpt terug op de zestiende eeuw en schilder Pieter Bruegel: dit is 'iets uit de geschiedenis'."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Op welke manier introduceert de auteur in alinea 1 en 2 van Tekst A het centrale onderwerp?",
        "opties": [
            "Door direct een scherp standpunt in te nemen",
            "Door een centrale hoofdvraag te stellen",
            "Door een definitie uit het woordenboek te citeren",
            "Door een juridische klacht in te dienen"
        ],
        "antwoord": 1,
        "uitleg": "Aan het einde van alinea 1 wordt een centrale vraag gesteld ('Maar kan ons oeroude lichaam die moderne 24-uurseconomie wel bijbenen?'), die in alinea 2 verder wordt uitgewerkt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_slaap,
        "vraag": "Volgens de theorie van paragraaf 2 heeft de inleiding van een zakelijke tekst altijd maar één vaste alinea; twee alinea's is volgens de regels niet toegestaan.",
        "antwoord": False,
        "uitleg": "Onwaar. Een inleiding kan uit één of twee alinea's bestaan, en bij langere artikelen zelfs uit meer."
    },
    {
        "type": "open",
        "figuur": card_slaap,
        "vraag": "Welke twee functies vervult de slotalinea (alinea 7) van Tekst A?",
        "sleutelwoorden": ["conclusie/samenvatting/hoofdgedachte", "aanbeveling/advies/oproep"],
        "minTreffers": 1,
        "modelantwoord": "Een conclusie/samenvatting van het belang van slaap én een concrete aanbeveling/advies om de telefoon eerder weg te leggen.",
        "uitleg": "Alinea 7 vat samen dat slaap een eerste levensbehoefte is (conclusie) en geeft de lezer het advies om de telefoon weg te leggen en op tijd te gaan slapen (aanbeveling)."
    },
    {
        "type": "invul",
        "figuur": card_slaap,
        "vraag": "Met welk typisch samenvattend signaalwoord begint de slotalinea van Tekst A?",
        "antwoord": "al met al",
        "uitleg": "Alinea 7 begint met de signaalwoordgroep 'Al met al'."
    },
    {
        "type": "mc",
        "figuur": card_telefoon,
        "vraag": "Welke aandachtstrekker gebruikt de auteur aan het begin van Tekst B in alinea 1?",
        "opties": [
            "Iets uit de geschiedenis van de oudheid",
            "Een sprekend voorbeeld of korte anekdote",
            "Tot de verbeelding sprekende statistieken",
            "Een verwijzing naar een buitenlands wetsartikel"
        ],
        "antwoord": 1,
        "uitleg": "De auteur begint met een herkenbare situatie op het schoolplein van het Rembrandt College (tafelvoetballende leerlingen): een concreet voorbeeld / anekdote."
    },
    {
        "type": "mc",
        "figuur": card_telefoon,
        "vraag": "Hoe wordt het onderwerp in alinea 2 van Tekst B gepresenteerd?",
        "opties": [
            "Via een historisch overzicht",
            "Via een opsomming van boetes",
            "Via het schetsen van een maatschappelijk probleem",
            "Via een sprookjesachtige verhaallijn"
        ],
        "antwoord": 2,
        "uitleg": "In alinea 2 wordt de probleemstelling neergezet: de worsteling van scholen om balans te vinden tussen digitale tools en lesaandacht."
    },
    {
        "type": "open",
        "figuur": card_telefoon,
        "vraag": "Wanneer noemen we een tekst volgens de theorie van paragraaf 2 'mooi rond'?",
        "sleutelwoorden": ["slot", "inleiding/aandachtstrekker", "aansluiten/terugkomen/teruggrijpen"],
        "minTreffers": 1,
        "modelantwoord": "Als de schrijver in het slot inhoudelijk of qua formulering teruggrijpt op de aandachtstrekker uit de inleiding.",
        "uitleg": "Een tekst is 'mooi rond' als het slot weer aansluit bij het beeld of de anekdote waarmee de inleiding begon."
    },
    {
        "type": "waaronwaar",
        "figuur": card_telefoon,
        "vraag": "In alinea 7 van Tekst B is er sprake van een tekst die 'mooi rond' is gemaakt, omdat de schrijver teruggrijpt op de rust en ontmoeting die in alinea 1 op het schoolplein werd beschreven.",
        "antwoord": True,
        "uitleg": "Waar. In het slot spreekt de auteur over 'ontmoeting en focus' en de rust om echt contact te maken, wat direct aansluit bij de ontmoetende leerlingen op het schoolplein uit alinea 1."
    },
    {
        "type": "mc",
        "figuur": card_telefoon,
        "vraag": "Welk tekstdoel past het beste bij Tekst B?",
        "opties": [
            "Puur amuseren met fictieve verhalen",
            "Beschouwen en overtuigen",
            "Uitsluitend instrueren met een stappenplan",
            "Activeren om een smartphone te kopen"
        ],
        "antwoord": 1,
        "uitleg": "De tekst weegt voor- en nadelen af (beschouwen) en overtuigt de lezer van het nut van een smartphonevrije school (overtuigen)."
    },
    {
        "type": "mc",
        "vraag": "Wat is volgens de theorie van paragraaf 2 een 'toekomstverwachting' in het slot van een tekst?",
        "opties": [
            "Een samenvatting van wat er vroeger allemaal is gebeurd",
            "Een lijst met moeilijke woorden uit de voorbije alinea's",
            "Een doorkijk of voorspelling van hoe de kwestie zich vermoedelijk zal ontwikkelen",
            "Een herhaling van de allereerste zin van de inleiding"
        ],
        "antwoord": 2,
        "uitleg": "Een toekomstverwachting blikt vooruit op de komende ontwikkelingen rondom het thema van de tekst."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een aanbeveling in de slotalinea is bedoeld om de lezer een concreet advies of nuttige suggestie te geven voor wat er moet gebeuren.",
        "antwoord": True,
        "uitleg": "Waar. De aanbeveling geeft een praktisch advies of handelingsperspectief naar aanleiding van de conclusie."
    },
    {
        "type": "open",
        "figuur": card_slaap,
        "vraag": "Waarom past de titel 'De geheimen van de biologische klok' goed bij alinea 3 van Tekst A?",
        "sleutelwoorden": ["slaapcyclus/slaapcycli/rem/diep", "brein/herstelslaap/hersenen/geheugen"],
        "minTreffers": 1,
        "modelantwoord": "Omdat alinea 3 precies uitlegt wat de biologische klok en de slaapcycli in ons brein doen (diepe slaap en REM-slaap).",
        "uitleg": "Alinea 3 onthult de werking van de slaapfasen en hoe het brein 's nachts functioneert."
    },
    {
        "type": "invul",
        "figuur": card_telefoon,
        "vraag": "Met welk klassiek signaalwoord opent alinea 7 van Tekst B om aan te geven dat de conclusie volgt?",
        "antwoord": "kortom",
        "uitleg": "Alinea 7 start met 'Kortom:'."
    },
    {
        "type": "mc",
        "vraag": "Welke van de onderstaande technieken is GEEN officiële aandachtstrekker volgens de theorie van paragraaf 2?",
        "opties": [
            "De lezer bedreigen met fysiek geweld",
            "Iets uit de actualiteit",
            "Een herkenbaar voorbeeld of anekdote",
            "Tot de verbeelding sprekende cijfers"
        ],
        "antwoord": 0,
        "uitleg": "Bedreigingen horen uiteraard niet thuis in een zakelijke tekst. De beproefde methoden zijn actualiteit, geschiedenis, anekdote, belang, aanleiding en cijfers."
    },
    {
        "type": "waaronwaar",
        "vraag": "De hoofdgedachte van een tekst is de belangrijkste mededeling over het onderwerp, samengevat in één duidelijke bewering of zin.",
        "antwoord": True,
        "uitleg": "Waar. De hoofdgedachte is altijd één volwaardige zin die de kern van de hele tekst weergeeft."
    },
    {
        "type": "mc",
        "figuur": card_slaap,
        "vraag": "Welke van de onderstaande zinnen verwoordt het meest adequaat de hoofdgedachte van Tekst A?",
        "opties": [
            "Middelbare scholieren halen door slaaptekort een punt lager op hun proefwerken.",
            "In de zestiende eeuw ging iedereen slapen zodra de zon onderging.",
            "Voldoende slaap is een onmisbare levensbehoefte voor herstel, gezondheid en prestaties.",
            "Sociale media zijn de voornaamste oorzaak van slaapstoornissen bij jongeren."
        ],
        "antwoord": 2,
        "uitleg": "De kern van Tekst A is dat slaap geen verloren tijd is, maar essentieel onderhoud voor het brein en lichaam."
    },
    {
        "type": "open",
        "figuur": card_telefoon,
        "vraag": "In alinea 4 van Tekst B wordt een argument genoemd tegen het toelaten van mobieltjes in de klas. Welk argument is dat?",
        "sleutelwoorden": ["concentratie/aandacht", "paraat/stand/melding/prikkels/trilling"],
        "minTreffers": 1,
        "modelantwoord": "Zelfs een stille telefoon op tafel slurpt concentratie weg doordat het brein voortdurend alert blijft op mogelijke meldingen.",
        "uitleg": "Alinea 4 legt uit dat de telefoon op de hoek van de tafel ongemerkt concentratie wegneemt omdat de hersenen in de 'paraat-stand' blijven."
    },
    {
        "type": "waaronwaar",
        "figuur": card_telefoon,
        "vraag": "Alinea 6 van Tekst B stelt dat een smartphoneverbod op school automatisch ook alle problemen rondom cyberpesten in de thuissituatie definitief oplost.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 6 zegt juist letterlijk dat een verbod op school cyberpesten niet oplost en dat daarvoor ook afspraken thuis nodig zijn."
    },
    {
        "type": "mc",
        "figuur": card_telefoon,
        "vraag": "Welke uitspraak geeft de hoofdgedachte van Tekst B het beste weer?",
        "opties": [
            "Leerlingen moeten op school leren programmeren en omgaan met algoritmes.",
            "Een smartphonevrije school bevordert de rust, concentratie en sociale omgang in het onderwijs.",
            "Het Rembrandt College is de enige school in Nederland waar leerlingen tafelvoetballen.",
            "Tegenstanders van het mobielverbod hebben gelijk dat educatieve apps onmisbaar zijn."
        ],
        "antwoord": 1,
        "uitleg": "De slotalinea en het betoog benadrukken dat het weren van smartphones rust, focus en echt sociaal contact oplevert."
    }
]

ex2_data = {
    "id": "ex-h3-nederlands-2",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "2",
    "titel": "Toets 2 — §2 Inleiding en Slot (Leesteksten & Functies)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🎯",
    "duurMin": 25,
    "vragen": vragen_ex2
}

# ==============================================================================
# TEKSTEN VOOR TOETS 3: §5 VASTE TEKSTSTRUCTUREN
# ==============================================================================
deelfiets_alineas = [
    "Wie dezer dagen door Utrecht, Antwerpen of Kopenhagen loopt, kan er niet omheen: overal staan rijen felgekleurde deelfietsen en e-bikes geparkeerd. Met één swipe op je telefoon ontgrendel je een tweewieler om naar college of het station te zoeven. De deelfiets belooft het ultieme groene alternatief voor de overvolle binnenstad te zijn. Maar is dit deelmobiliteitswonder werkelijk zo ideaal als de hippe apps ons willen doen geloven?",
    "Aan de positieve kant biedt het deelfietssysteem enorme voordelen voor stadsbewoners en toeristen. Ten eerste hoef je je geen zorgen te maken over diefstal of een lekke band; het onderhoud ligt immers volledig bij de aanbieder. Ten tweede verlichten de fietsen de druk op het openbaar vervoer tijdens de spits. Uit cijfers van de gemeente Utrecht blijkt dat ruim 30 procent van de deelfietstochten een autoritje vervangt, wat direct zorgt voor minder CO2-uitstoot en schonere stadslucht.",
    "Bovendien stimuleert het mensen om meer te bewegen. Voor forenzen die net te ver van het station wonen om te lopen, vormt de deelfiets de perfecte flexibele schakel in hun dagelijkse reis.",
    "Daar staat echter een reeks serieuze nadelen tegenover. Het grootste knelpunt is de zogeheten 'verrommeling' van de openbare ruimte. Omdat gebruikers hun gehuurde fiets overal mogen achterlaten ('free floating'), blokkeren omgevallen tweewielers regelmatig stoepen, blindegeleidestroken en winkelpuien. Voor rolstoelgebruikers en slechtzienden leidt dit tot levensgevaarlijke hindernissenparcoursen.",
    "Een tweede minpunt is het vandalisme en de korte levensduur van de voertuigen. Veel fietsen belanden in grachten of worden op straat gesloopt. Onderzoek toont aan dat een gemiddelde deelfiets soms al na zes maanden rijp is voor de schroot, wat de duurzaamheidswinst grotendeels tenietdoet.",
    "Ten slotte leidt de wildgroei aan concurrerende commerciële aanbieders tot frustratie: voor elk fietsmerk heb je weer een aparte app, account en betaalmethode nodig.",
    "Om de overlast te beteugelen, grijpen steeds meer gemeenten in met vaste parkeerzones ('dropzones') en strikte vergunningen. Wie zijn fiets buiten zo'n gemarkeerd vak achterlaat, betaalt een fikse boete via de app.",
    "Al met al brengt de deelfiets zowel grote gemakken voor flexibele reizigers als flinke uitdagingen voor de leefbaarheid in de straat. Pas wanneer steden strakke parkeerzones handhaven en gebruikers hun verantwoordelijkheid nemen, kan het systeem zijn duurzame belofte écht waarmaken."
]
card_deelfiets = maak_leestekst_card("Tekst A: De opkomst van de elektrische deelfiets", "Stadsgeografie & Mobiliteit, 2024", deelfiets_alineas, "8 alinea's")

diepzee_alineas = [
    "De diepzee, het gigantische watergebied onder de 200 meter diepte waar het zonlicht niet meer kan doordringen, beslaat meer dan 60 procent van onze planeet. Toch weten we momenteel meer van het oppervlak van de maan dan van de diepste oceanische troggen. Welke bijzondere geheimen herbergt deze ijskoude, aardedonkere wereld?",
    "In de eerste plaats worden diepzeeorganismen blootgesteld aan extreme omgevingsfactoren. De waterdruk op duizenden meters diepte is verpletterend hoog: vergelijkbaar met het gewicht van een olifant die op je duimnagel balanceert. Bovendien schommelt de watertemperatuur er rond het vriespunt en ontbreekt elk spoor van natuurlijk zonlicht.",
    "Om in deze vijandige omstandigheden te overleven, hebben zeedieren fascinerende lichamelijke aanpassingen ontwikkeld. Veel vissen hebben geen botten maar een flexibel kraakbeenskelet en speciale celmembranen die niet bezwijken onder de druk.",
    "Een tweede opvallend kenmerk is bioluminescentie: het vermogen van organismen om zelf licht te produceren via chemische reacties in hun lichaam. De diepzeehengelvis gebruikt bijvoorbeeld een oplichtend lantaarntje aan zijn kop om nieuwsgierige prooien rechtstreeks zijn bek in te lokken. Andere soorten gebruiken lichtsignalen om soortgenoten te herkennen of vijanden af te schrikken.",
    "Daarnaast is het voedselaanbod in de diepzee uiterst schaars. Omdat er geen zonlicht is voor fotosynthese, voeden veel bewoners zich met 'zeesneeuw': neerdwarrelende organische resten van dode algen en zeedieren uit de bovenste waterlagen. Sommige diepzeehaaien kunnen daardoor maandenlang zonder maaltijd.",
    "Een geheel uniek ecosysteem bevindt zich rond hydrothermale bronnen ('black smokers'). Deze vulkanische schoorstenen op de zeebodem spuwen mineraalrijk heet water uit, waar bacteriën energie halen uit zwavelverbindingen. Hier leeft een bizarre wereld van meterslange kokerwormen en witte reuzengarnalen die volledig onafhankelijk zijn van zonlicht.",
    "De afgelopen jaren staat de diepzee echter onder toenemende dreiging door plannen voor diepzeemijnbouw. Grote mijnbouwbedrijven willen mangaanknollen van de oceaanbodem oogsten voor batterijen in elektrische auto's, wat onherstelbare schade kan toebrengen aan deze kwetsbare riffen.",
    "Samenvattend blijkt de diepzee een rijk en wonderlijk ecosysteem vol unieke levensvormen en overlevingsstrategieën. Om deze mysterieuze wereld te behouden voor toekomstige generaties, is strikte internationale bescherming dringend noodzakelijk."
]
card_diepzee = maak_leestekst_card("Tekst B: Leven in de diepzee: wonderen in de duisternis", "Mariene Biologie & Aardwetenschappen, 2025", diepzee_alineas, "8 alinea's")

# ==============================================================================
# EXAMEN 3: §5 VASTE TEKSTSTRUCTUREN
# ==============================================================================
vragen_ex3 = [
    {
        "type": "mc",
        "figuur": card_deelfiets,
        "vraag": "Welke vaste tekststructuur herken je in Tekst A (De opkomst van de elektrische deelfiets)?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur",
            "Vraag-antwoordstructuur",
            "Aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "De tekst schetst de situatie, zet in het middenstuk de voordelen (al. 2-3) en nadelen (al. 4-6) tegen elkaar af en sluit af met een afweging: de voor- en nadelenstructuur."
    },
    {
        "type": "mc",
        "figuur": card_deelfiets,
        "vraag": "Wat is het voornaamste tekstdoel van de auteur in Tekst A?",
        "opties": [
            "Activeren (de lezer aanzetten tot het kopen van een e-bike)",
            "Beschouwen (de lezer laten nadenken door plussen en minnen te belichten)",
            "Amuseren (de lezer vermaken met komische fietsongelukken)",
            "Instrueren (een handleiding geven voor het repareren van fietsbanden)"
        ],
        "antwoord": 1,
        "uitleg": "Bij een voor- en nadelenstructuur wil de schrijver de lezer aan het denken zetten over beide kanten van de kwestie (tekstdoel: beschouwen)."
    },
    {
        "type": "waaronwaar",
        "figuur": card_deelfiets,
        "vraag": "Volgens alinea 2 van Tekst A blijkt uit gemeentecijfers dat de deelfiets nauwelijks invloed heeft op het autoverkeer en geen enkele CO2-reductie oplevert.",
        "antwoord": False,
        "uitleg": "Onwaar. In alinea 2 staat juist dat ruim 30 procent van de deelfietstochten een autorit vervangt en direct zorgt voor minder CO2-uitstoot."
    },
    {
        "type": "open",
        "figuur": card_deelfiets,
        "vraag": "In alinea 4 wordt het woord 'verrommeling' gebruikt. Leg uit wat daarmee in deze context wordt bedoeld.",
        "sleutelwoorden": ["openbare/ruimte/straat", "blokkeren/stoep/omgevallen/rommel/overal"],
        "minTreffers": 1,
        "modelantwoord": "Het slordig en overal achterlaten van omgevallen deelfietsen waardoor stoepen, winkelpuien en de openbare ruimte worden geblokkeerd.",
        "uitleg": "Alinea 4 legt uit dat fietsen overal worden achtergelaten en de openbare ruimte onveilig en rommelig maken."
    },
    {
        "type": "invul",
        "figuur": card_deelfiets,
        "vraag": "Met welk signaalwoord van tegenstelling opent alinea 4 van Tekst A de omslag naar de nadelen?",
        "antwoord": "daar staat echter|echter",
        "uitleg": "Alinea 4 opent met: 'Daar staat echter een reeks serieuze nadelen tegenover.'"
    },
    {
        "type": "mc",
        "figuur": card_diepzee,
        "vraag": "Welke vaste tekststructuur herken je primair in Tekst B (Leven in de diepzee)?",
        "opties": [
            "Probleem-oplossingsstructuur",
            "Voor- en nadelenstructuur",
            "Aspectenstructuur",
            "Argumentatiestructuur"
        ],
        "antwoord": 2,
        "uitleg": "De tekst belicht verschillende kanten en onderdelen van de diepzee (druk, bioluminescentie, voedsel/zeesneeuw, hydrothermale bronnen): een typische aspectenstructuur."
    },
    {
        "type": "mc",
        "figuur": card_diepzee,
        "vraag": "Wat is het tekstdoel van Tekst B?",
        "opties": [
            "Overtuigen van een politiek standpunt",
            "Informeren over een natuurwetenschappelijk onderwerp",
            "Waarschuwen voor naderend onweer",
            "Instrueren hoe je een duikboot bestuurt"
        ],
        "antwoord": 1,
        "uitleg": "De tekst geeft zakelijke en wetenschappelijke feiten over het leven in de diepzee: tekstdoel informeren."
    },
    {
        "type": "open",
        "figuur": card_diepzee,
        "vraag": "In alinea 4 wordt het begrip 'bioluminescentie' besproken. Wat betekent dit en noem één functie ervan uit de tekst.",
        "sleutelwoorden": ["licht/produceren/geven", "lokken/prooi/afschrikken/herkennen"],
        "minTreffers": 1,
        "modelantwoord": "Het zelf produceren van licht via chemische reacties, gebruikt om prooien te lokken, soortgenoten te herkennen of vijanden af te schrikken.",
        "uitleg": "Alinea 4 legt uit dat dieren zelf licht maken en dit inzetten voor de jacht of communicatie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_diepzee,
        "vraag": "Rond hydrothermale bronnen op de zeebodem (alinea 6) zijn organismen zoals kokerwormen volledig afhankelijk van zonlicht voor hun fotosynthese.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 6 stelt expliciet dat deze wezens leven van bacteriën die energie halen uit zwavel en 'volledig onafhankelijk zijn van zonlicht'."
    },
    {
        "type": "open",
        "figuur": card_diepzee,
        "vraag": "Bedenk een passend tussenkopje voor het tekstgedeelte dat bestaat uit alinea 3 en 4 van Tekst B.",
        "sleutelwoorden": ["aanpassingen/overleven/lichaam", "licht/bioluminescentie/kenmerken"],
        "minTreffers": 1,
        "modelantwoord": "Lichamelijke aanpassingen / Overleven in het donker / Licht in de diepte.",
        "uitleg": "Alinea 3 en 4 gaan over hoe diepzeedieren zich fysiek hebben aangepast aan druk en duisternis."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een artikel dat begint met een ernstig maatschappelijk knelpunt, in het middenstuk de oorzaken en gevolgen ontleedt, en afsluit met aanbevelingen voor de beste aanpak?",
        "opties": [
            "Aspectenstructuur",
            "Probleem-oplossingsstructuur",
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur"
        ],
        "antwoord": 1,
        "uitleg": "Dit is de klassieke opbouw van de probleem-oplossingsstructuur."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur past het beste bij een tekst waarin een biologisch verschijnsel (zoals het ontstaan van een tsunami) stap voor stap wordt verklaard aan de hand van kenmerken en oorzaken?",
        "opties": [
            "Argumentatiestructuur",
            "Vraag-antwoordstructuur",
            "Verklaringsstructuur",
            "Voor- en nadelenstructuur"
        ],
        "antwoord": 2,
        "uitleg": "Een tekst die het 'hoe en waarom' van een verschijnsel toelicht, volgt de verklaringsstructuur."
    },
    {
        "type": "waaronwaar",
        "vraag": "In een vraag-antwoordstructuur staat de centrale vraag altijd pas in de allerlaatste alinea van het slot geformuleerd.",
        "antwoord": False,
        "uitleg": "Onwaar. In een vraag-antwoordstructuur wordt de centrale vraag al in de inleiding gesteld, waarna het middenstuk de antwoorden uitwerkt."
    },
    {
        "type": "invul",
        "figuur": card_diepzee,
        "vraag": "Welk samenvattend signaalwoord gebruikt de auteur aan het begin van de slotalinea (alinea 8) van Tekst B?",
        "antwoord": "samenvattend",
        "uitleg": "Alinea 8 opent met het signaalwoord 'Samenvattend'."
    },
    {
        "type": "mc",
        "figuur": card_deelfiets,
        "vraag": "Welke alinea van Tekst A biedt een concrete oplossing voor het parkeerprobleem van deelfietsen?",
        "opties": [
            "Alinea 2",
            "Alinea 7",
            "Alinea 5",
            "Alinea 3"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 7 beschrijft de oplossing: vaste 'dropzones' en boetes via de app bij foutparkeren."
    },
    {
        "type": "open",
        "figuur": card_deelfiets,
        "vraag": "Vul het schema van oorzaak en gevolg aan op basis van alinea 4 van Tekst A: (1) Gebruikers mogen fietsen overal achterlaten -> (2) Fietsen blokkeren stoepen -> (3) ...",
        "sleutelwoorden": ["rolstoelgebruikers/slechtzienden", "gevaarlijk/hindernis/overlast/ontoegankelijk"],
        "minTreffers": 1,
        "modelantwoord": "Voor rolstoelgebruikers en slechtzienden ontstaan gevaarlijke hindernissen op het trottoir.",
        "uitleg": "Alinea 4 wijst specifiek op het gevaar voor mensen in een rolstoel of met een visuele beperking."
    },
    {
        "type": "waaronwaar",
        "vraag": "Signaalwoorden zoals 'ten eerste', 'bovendien', 'daarnaast' en 'ten slotte' duiden op een opsommend tekstverband binnen bijvoorbeeld een aspectenstructuur.",
        "antwoord": True,
        "uitleg": "Waar. Deze signaalwoorden kondigen gelijkwaardige deelaspecten of argumenten aan in een opsomming."
    },
    {
        "type": "mc",
        "figuur": card_deelfiets,
        "vraag": "Welke zin geeft het beste de hoofdgedachte van Tekst A (De opkomst van de elektrische deelfiets) weer?",
        "opties": [
            "De deelfiets vervangt autoritten, maar kan pas echt duurzaam zijn als gemeenten de overlast streng reguleren en gebruikers meewerken.",
            "Utrecht en Kopenhagen zijn de enige Europese steden waar deelfietsen succesvol zijn ingevoerd.",
            "De levensduur van een deelfiets is met zes maanden veel te kort voor commerciële bedrijven.",
            "Voor rolstoelgebruikers moeten alle deelfietsen in Nederland direct worden verboden."
        ],
        "antwoord": 0,
        "uitleg": "De hoofdgedachte weegt het succes (minder auto's) af tegen de randvoorwaarde van strenge regulering tegen overlast."
    },
    {
        "type": "mc",
        "figuur": card_diepzee,
        "vraag": "Welke zin verwoordt het meest treffend de hoofdgedachte van Tekst B (Leven in de diepzee)?",
        "opties": [
            "Mangaanknollen van de oceaanbodem zijn onmisbaar voor de fabricage van elektrische auto's.",
            "De diepzee is een wonderlijk en rijk ecosysteem met unieke aanpassingen dat beschermd moet worden tegen menselijke vernietiging.",
            "Diepzeehengelvissen zijn het gevaarlijkste roofdier op aarde door hun lichtgevende lantaarn.",
            "Op de bodem van de oceaan is de druk zo hoog dat onderzoek met duikboten onmogelijk is."
        ],
        "antwoord": 1,
        "uitleg": "De kern van Tekst B is de unieke biologische rijkdom van de diepzee en de noodzaak tot internationale bescherming."
    },
    {
        "type": "waaronwaar",
        "figuur": card_diepzee,
        "vraag": "In alinea 7 van Tekst B wordt diepzeemijnbouw gepresenteerd als een veilige activiteit die het mariene milieu juist beschermt.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 7 waarschuwt juist voor onherstelbare schade aan kwetsbare riffen door het oogsten van mangaanknollen."
    }
]

ex3_data = {
    "id": "ex-h3-nederlands-3",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "5",
    "titel": "Toets 3 — §5 Vaste Tekststructuren (De 7 Modellen & Signaalwoorden)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🏗️",
    "duurMin": 25,
    "vragen": vragen_ex3
}

# ==============================================================================
# TEKSTEN VOOR TOETS 4: INTEGRALE PROEFTOETS LEZEN (OEFENTOETS B)
# ==============================================================================
nepnieuws_alineas = [
    "‘Paus Franciscus steunt presidentschap Donald Trump!’ In de aanloop naar de Amerikaanse verkiezingen van 2016 werd dit sensationele bericht miljoenen keren gedeeld op Facebook. Pas veel later bleek het bericht compleet verzonnen door tieners in een klein Macedonisch dorpje, die met advertenties duizenden euro's opstreken. Het was het startsein van een wereldwijde crisis rondom nepnieuws.",
    "Nepnieuws – opzettelijk gefabriceerde desinformatie die als echt nieuws wordt gepresenteerd – is van alle tijden. Maar door sociale media verspreiden leugens zich tegenwoordig zes keer sneller dan de waarheid. Hoe komt het dat ons brein zo gevoelig is voor misleidende koppen?",
    "Psychologen wijzen ten eerste op de zogeheten 'confirmation bias' (bevestigingsvooroordeel). Mensen zijn van nature geneigd informatie te geloven die naadloos aansluit bij hun bestaande vooroordelen of wereldbeeld. Berichten die ons gelijk bevestigen, geven een prettig gevoel, waardoor we minder kritisch zijn op de bron.",
    "Ten tweede spelen emoties een doorslaggevende rol. Artikelen die verontwaardiging, angst of woede oproepen, worden veel sneller gedeeld. De algoritmes van sociale platforms zijn zo ontworpen dat berichten met veel interactie bovenaan in je tijdlijn verschijnen. Sensatie levert immers advertentie-inkomsten op.",
    "Bovendien ontbreekt het veel lezers aan 'digitale geletterdheid'. Jong en oud vinden het lastig om een betrouwbare journalistieke website te onderscheiden van een gesponsorde blog of een satirische parodie.",
    "De maatschappelijke gevolgen van deze desinformatiegolf zijn zorgwekkend. Het ondermijnt het vertrouwen in de wetenschap, wakkert maatschappelijke polarisatie aan en kan zelfs de democratische verkiezingen beïnvloeden.",
    "Gelukkig zijn er manieren om weerbaarder te worden. Factcheckers controleren verdachte beweringen, techbedrijven weren malafide advertentie-accounts en scholen besteden steeds meer aandacht aan mediawijsheid. Een gouden vuistregel voor iedere internetter luidt: check altijd de auteur, datum en primaire bron voordat je op 'delen' klikt.",
    "Kortom: nepnieuws teert op menselijke emoties en slimme algoritmes, maar is te bestrijden met een gezonde dosis wantrouwen en kritisch bronnenonderzoek. Wie zijn nieuwsgierigheid combineert met waakzaamheid, laat zich niet zomaar voor het karretje van desinformatie spannen."
]
card_nepnieuws = maak_leestekst_card("Tekst 1: De psychologie van nepnieuws", "Media & Maatschappij, 2025", nepnieuws_alineas, "8 alinea's")

plastic_alineas = [
    "Toen de Belgische uitvinder Leo Baekeland in 1907 het allereerste synthetische plastic (bakeliet) presenteerde, werd hij bejubeld als een genie. Plastic was licht, onbreekbaar, waterdicht enSpotgoedkoop. Niemand kon vermoeden dat ditzelfde wondermateriaal een eeuw later zou uitgroeien tot een van de grootste ecologische rampen in de geschiedenis van de mensheid.",
    "Vandaag de dag drijven er naar schatting honderden miljoenen kilo's plastic afval in onze wereldzeeën. In de Stille Oceaan heeft zich de beruchte 'Plastic Soep' gevormd: een reusachtige drijvende vuilnisbelt die driemaal zo groot is als Frankrijk. Jaarlijks belanden miljoenen zeevogels, vissen en schildpadden in deze plastic valstrik.",
    "Het grootste gevaar schuilt niet in grote stukken afval, maar in microplastics. Onder invloed van zout water en uv-straling verbrokkelen flessen en visnetten in microscopisch kleine deeltjes. Zeedieren zien deze deeltjes aan voor plankton en slikken ze in. Zo belanden giftige chemicaliën via de voedselketen uiteindelijk op ons eigen bord.",
    "Toch gloort er hoop aan de horizon dankzij technologische en beleidsmatige vernieuwingen. Ten eerste boekt het Nederlandse initiatief 'The Ocean Cleanup' van Boyan Slat indrukwekkende successen. Met gigantische drijvende vangarmen filtert de organisatie tonnen plastic uit rivieren en oceanen.",
    "Ten tweede zetten wetenschappers volop in op de ontwikkeling van bioplastics op basis van zeewier, suikerriet en maïszetmeel. Deze biologisch afbreekbare materialen composteren binnen enkele weken zonder schadelijke stoffen achter te laten.",
    "Ten slotte dwingen strengere overheidsmaatregelen verandering af. De Europese Unie verbood wegwerpplastic zoals rietjes, wattenstaafjes en plastic bestek, en breidde statiegeldregelingen met succes uit naar blikjes en kleine flesjes.",
    "Al met al toont de strijd tegen plasticvervuiling dat technologie, overheidsbeleid en consumentengedrag hand in hand moeten gaan om het tij te keren. Alleen als we de overstap maken naar een écht circulaire economie, waarin afval als grondstof dient, kunnen we onze oceanen redden voor toekomstige generaties."
]
card_plastic = maak_leestekst_card("Tekst 2: Van wondermateriaal tot plastic soep", "Milieu & Duurzaamheid, 2024", plastic_alineas, "7 alinea's")

# ==============================================================================
# EXAMEN 4: PROEFTOETS LEZEN HAVO 3 (INTEGRALE OEFENTOETS B)
# ==============================================================================
vragen_ex4 = [
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een tekst waarin twee tegengestelde gezichtspunten (de plussen en minnen) worden besproken alvorens een conclusie wordt getrokken?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur",
            "Vraag-antwoordstructuur",
            "Aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Het afwegen van positieve en negatieve kanten vooraleer te besluiten, is kenmerkend voor de voor- en nadelenstructuur."
    },
    {
        "type": "mc",
        "figuur": card_nepnieuws,
        "vraag": "Wat is het onderwerp van Tekst 1 (De psychologie van nepnieuws)?",
        "opties": [
            "Paus Franciscus",
            "Macedonische tieners",
            "Nepnieuws",
            "Facebook-advertenties"
        ],
        "antwoord": 2,
        "uitleg": "Het overkoepelende onderwerp is nepnieuws (desinformatie, oorzaken van de verspreiding en bestrijding)."
    },
    {
        "type": "mc",
        "figuur": card_nepnieuws,
        "vraag": "Op welke manier probeert de schrijver in alinea 1 van Tekst 1 de aandacht van de lezer te trekken?",
        "opties": [
            "Door een situatie in het heden te vergelijken met de middeleeuwen",
            "Door een sprekend voorbeeld / recente gebeurtenis aan te halen",
            "Door een filosofisch gedicht te citeren",
            "Door te dreigen met een internetverbod"
        ],
        "antwoord": 1,
        "uitleg": "De auteur opent met een geruchtmakend en waargebeurd voorbeeld uit de Amerikaanse verkiezingen van 2016."
    },
    {
        "type": "mc",
        "figuur": card_nepnieuws,
        "vraag": "Welke vaste tekststructuur herken je in Tekst 1?",
        "opties": [
            "Verklaringsstructuur",
            "Voor- en nadelenstructuur",
            "Vraag-antwoordstructuur",
            "Aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "De tekst verklaart waarom mensen zo vatbaar zijn voor nepnieuws (confirmation bias, emoties, algoritmes) en hoe het bestreden kan worden."
    },
    {
        "type": "open",
        "figuur": card_nepnieuws,
        "vraag": "In alinea 3 wordt het begrip 'confirmation bias' uitgelegd. Wat houdt dit psychologische mechanisme in?",
        "sleutelwoorden": ["bestaande/eigen/vooroordelen", "geloven/aansluit/bevestigt"],
        "minTreffers": 1,
        "modelantwoord": "De menselijke neiging om informatie die aansluit bij je eigen bestaande vooroordelen direct te geloven en minder kritisch te toetsen.",
        "uitleg": "Alinea 3 legt uit dat mensen informatie sneller aannemen als het overeenstemt met wat ze al dachten."
    },
    {
        "type": "open",
        "figuur": card_nepnieuws,
        "vraag": "Welke rol spelen de algoritmes van sociale media volgens alinea 4 bij de snelle verspreiding van nepnieuws?",
        "sleutelwoorden": ["emoties/woede/angst/verontwaardiging", "interactie/bovenaan/advertenties/geld"],
        "minTreffers": 1,
        "modelantwoord": "Algoritmes plaatsen berichten die sterke emoties en veel interactie oproepen bovenaan, omdat sensatie advertentie-inkomsten oplevert.",
        "uitleg": "Alinea 4 toont aan dat sensatie en emoties door de algoritmes beloond worden met een groter bereik."
    },
    {
        "type": "waaronwaar",
        "figuur": card_nepnieuws,
        "vraag": "Volgens alinea 2 van Tekst 1 is nepnieuws een verschijnsel dat pas in het jaar 2016 voor het allereerst in de menselijke geschiedenis ontstond.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 2 zegt letterlijk: 'Nepnieuws... is van alle tijden.'"
    },
    {
        "type": "invul",
        "figuur": card_nepnieuws,
        "vraag": "Met welk signaalwoord van tegenstelling opent alinea 2 de overgang van de Macedonische anekdote naar de algemene analyse?",
        "antwoord": "maar",
        "uitleg": "Alinea 2 stelt: 'Maar door sociale media verspreiden leugens zich tegenwoordig zes keer sneller...'"
    },
    {
        "type": "open",
        "figuur": card_nepnieuws,
        "vraag": "Noem twee concrete adviezen die in alinea 7 worden gegeven om betrouwbaarheid van internetnieuws zelf te controleren.",
        "sleutelwoorden": ["auteur", "datum", "bron/primaire"],
        "minTreffers": 1,
        "modelantwoord": "Controleer altijd de auteur, de publicatiedatum en de primaire bron voordat je iets deelt.",
        "uitleg": "Alinea 7 noemt specifiek het nagaan van de auteur, de datum en de achterliggende bron."
    },
    {
        "type": "mc",
        "figuur": card_nepnieuws,
        "vraag": "Welke zin verwoordt het beste de hoofdgedachte van Tekst 1?",
        "opties": [
            "Tieners in Macedonië verdienen veel geld met advertenties op sociale netwerken.",
            "Paus Franciscus heeft zich publiekelijk uitgesproken tegen politieke inmenging op Facebook.",
            "Nepnieuws verspreidt zich razendsnel door psychologische mechanismen en algoritmes, maar is te pareren met kritische broncontrole.",
            "Factcheckers zijn de enige mensen in de samenleving die nepnieuws nog kunnen ontmaskeren."
        ],
        "antwoord": 2,
        "uitleg": "De kernboodschap combineert de verklaring van de verspreiding met het belang van actieve broncontrole."
    },
    {
        "type": "mc",
        "vraag": "Welke structuur heeft een tekst waarin het verleden, het heden en een blik op de toekomst van een uitvinding chronologisch worden behandeld?",
        "opties": [
            "Probleem-oplossingsstructuur",
            "Verleden-heden(-toekomst)structuur",
            "Aspectenstructuur",
            "Vraag-antwoordstructuur"
        ],
        "antwoord": 1,
        "uitleg": "Een chronologische tijdlijn van vroeger naar nu en later is een verleden-heden(-toekomst)structuur."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Wat is het centrale onderwerp van Tekst 2?",
        "opties": [
            "De uitvinding van bakeliet in 1907",
            "Frankrijk en de Stille Oceaan",
            "Plasticvervuiling in de oceanen",
            "Statiegeld op frisdrankblikjes"
        ],
        "antwoord": 2,
        "uitleg": "De tekst draait om het probleem en de oplossingen rondom plasticvervuiling (de plastic soep) in de oceanen."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welke aandachtstrekker herken je in alinea 1 van Tekst 2?",
        "opties": [
            "Een verwijzing naar iets uit de geschiedenis",
            "Een angstaanjagend cijfer over de huidige verkiezingen",
            "Een klacht over te dure supermarktprijzen",
            "Een opsomming van biologische zeewiersoorten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 grijpt terug naar de historische uitvinding van bakeliet door Leo Baekeland in 1907."
    },
    {
        "type": "open",
        "figuur": card_plastic,
        "vraag": "In alinea 3 wordt uitgelegd waarom microplastics zo gevaarlijk zijn voor mens en dier. Verklaar hoe deze plastics uiteindelijk in ons voedsel terechtkomen.",
        "sleutelwoorden": ["zonlicht/uv/straling/zout/verbrokkelen", "zeedieren/vissen/slikken/eten/plankton", "voedselketen/eten/bord"],
        "minTreffers": 1,
        "modelantwoord": "Zwerfvuil verbrokkelt door zon en zout water in microscopische deeltjes; zeedieren eten dit aan voor plankton, waarna het via de voedselketen op ons bord belandt.",
        "uitleg": "Alinea 3 beschrijft het proces van verbrokkeling, inname door zeedieren en doorstroom via de voedselketen naar de mens."
    },
    {
        "type": "waaronwaar",
        "figuur": card_plastic,
        "vraag": "Volgens alinea 2 van Tekst 2 is de plastic soep in de Stille Oceaan inmiddels net zo klein geworden als een gemiddelde Nederlandse provincie.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 2 vermeldt juist dat het drijvende afvalveld 'driemaal zo groot is als Frankrijk'."
    },
    {
        "type": "open",
        "figuur": card_plastic,
        "vraag": "Bedenk een passend tussenkopje boven de alinea's 4, 5 en 6 van Tekst 2.",
        "sleutelwoorden": ["oplossingen/aanpak", "innovaties/vernieuwingen/maatregelen/hoop"],
        "minTreffers": 1,
        "modelantwoord": "Oplossingen en innovaties / Hoop voor de oceaan / Nieuwe maatregelen tegen plastic.",
        "uitleg": "Alinea 4 t/m 6 beschrijven drie hoopvolle oplossingen: The Ocean Cleanup, bioplastics en overheidsverboden."
    },
    {
        "type": "invul",
        "figuur": card_plastic,
        "vraag": "Welk signaalwoord van opsomming kondigt in alinea 6 de laatste categorie maatregelen aan?",
        "antwoord": "ten slotte|tenslotte",
        "uitleg": "Alinea 6 opent met 'Ten slotte dwingen strengere overheidsmaatregelen...'"
    },
    {
        "type": "waaronwaar",
        "figuur": card_plastic,
        "vraag": "Bioplastics op basis van suikerriet of zeewier (alinea 5) blijven volgens de tekst net zolang in het milieu rondzwerven als traditioneel plastic uit aardolie.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 meldt dat deze biologische plastics binnen enkele weken composteren zonder schade."
    },
    {
        "type": "open",
        "figuur": card_plastic,
        "vraag": "Welke twee functies herken je in de slotalinea (alinea 7) van Tekst 2?",
        "sleutelwoorden": ["samenvatting/conclusie", "aanbeveling/voorwaarde/toekomst/circulair"],
        "minTreffers": 1,
        "modelantwoord": "Een samenvatting van de gezamenlijke aanpak én een vooruitblik/aanbeveling naar een circulaire economie om de oceanen te redden.",
        "uitleg": "Alinea 7 vat samen dat technologie, beleid en gedrag moeten samengaan en sluit af met een dringende oproep tot een circulaire economie."
    },
    {
        "type": "mc",
        "figuur": card_plastic,
        "vraag": "Welke uitspraak verwoordt het meest treffend de hoofdgedachte van Tekst 2?",
        "opties": [
            "Leo Baekeland is de enige schuldige aan de huidige plasticcrisis in onze oceanen.",
            "De strijd tegen plasticvervuiling vraagt om een combinatie van opruimtechnologie, bioplastics en overheidsbeleid gericht op een circulaire economie.",
            "Wegwerprietjes en wattenstaafjes zijn het enige plastic afval dat in zeevogels wordt aangetroffen.",
            "The Ocean Cleanup heeft de hele Stille Oceaan inmiddels succesvol schoongeveegd."
        ],
        "antwoord": 1,
        "uitleg": "De tekst concludeert dat innovatie, wetgeving en een circulaire economie samen noodzakelijk zijn om het plasticprobleem op te lossen."
    }
]

ex4_data = {
    "id": "ex-h3-nederlands-4",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "mix",
    "titel": "Toets 4 — Proeftoets Lezen HAVO 3 (Integrale Oefentoets B)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "📝",
    "duurMin": 30,
    "vragen": vragen_ex4
}

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

# Schrijf alle bestanden weg
alle_examens = [
    ("examen_1.js", ex1_data),
    ("examen_2.js", ex2_data),
    ("examen_3.js", ex3_data),
    ("examen_4.js", ex4_data),
]

for bestandsnaam, data in alle_examens:
    balance_mc(data['vragen'])
    pad = os.path.join(out_dir, bestandsnaam)
    js_content = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 1) */\n"
    js_content += "DURU.registerExamen(" + json.dumps(data, indent=2, ensure_ascii=False) + ");\n"
    with open(pad, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Aangemaakt: {bestandsnaam} met {len(data['vragen'])} vragen.")

print("\nAlle 4 de examens succesvol aangemaakt!")
