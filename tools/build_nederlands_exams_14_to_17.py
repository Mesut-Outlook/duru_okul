# -*- coding: utf-8 -*-
"""
Generator voor 4 EXTRA HAVO 3 Nederlands leestoetsen (Toets 14 t/m 17):
- Toets 14: §2 Inleiding en Slot (Toets F — Actuele Kwesties, Probleemstellingen & Oproepen)
- Toets 15: §5 Vaste Tekststructuren (Toets F — Probleem-Oplossing & Vraag-Antwoord)
- Toets 16: §2 Inleiding en Slot (Toets G — Historische Vergelijkingen, Anekdotes & Cirkelstructuren)
- Toets 17: §5 Vaste Tekststructuren (Toets G — Voor- en Nadelen & Verleden-Heden-Toekomst)
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
# TOETS 14: §2 INLEIDING EN SLOT (TOETS F)
# Tekst A: Lichtvervuiling / Terugkeer van het donker
# Tekst B: E-sports / Tirannie van de prestatie
# ==============================================================================
donker_alineas = [
    "Wie op een heldere zomernacht op de Veluwe omhoogkijkt, ziet een adembenemende sterrenhemel met duizenden twinkelende lichtpuntjes en de vage witte band van de Melkweg. Maar wie datzelfde probeert in het centrum van Rotterdam of Utrecht, ziet vaak niet meer dan een fletse, oranje gloed waarin hooguit de maan en twee eenzame planeten te ontwaren zijn. Nederland behoort inmiddels tot de meest verlichte landen ter wereld. Is onze drang naar eeuwige verlichting slechts een teken van vooruitgang, of beroven we onszelf en de natuur van een onmisbare oerkracht: de duisternis?",
    "Al sinds de introductie van gaslantaarns in de negentiende eeuw associeert de westerse mens kunstlicht met veiligheid, welvaart en gezelligheid. Donkere steegjes stonden immers eeuwenlang synoniem voor gevaar en criminaliteit. Deze diepgewortelde angst heeft geleid tot een gigantische zee van licht: felverlichte snelwegen, brandende kantoortorens, reclamezuilen en kassencomplexen die dag en nacht gloeien alsof de zon nooit ondergaat.",
    "Biologen slaan echter alarm over de desastreuze ecologische gevolgen van deze continue lichtzee. Nachtdieren zoals vleermuizen, uilen en nachtvlinders raken volledig gedesoriënteerd door het felle schijnsel. Trekvogels botsen massaal tegen verlichte torens, en insecten sterven door uitputting omdat ze eindeloos rond straatlantaarns blijven cirkelen. Het natuurlijke ritme van jagen, paren en rusten raakt ernstig ontwricht.",
    "Ook voor de menselijke gezondheid blijkt het verdwijnen van de nacht schadelijk. De afwezigheid van natuurlijk donker verstoort de aanmaak van het slaaphormoon melatonine. Hierdoor slapen mensen minder diep, wat op termijn leidt tot concentratieproblemen, stemmingsstoornissen en een verhoogd risico op hart- en vaatziekten.",
    "Gelukkig groeit het besef dat donkerte een kostbaar natuurgoed is dat bescherming verdient. Natuurorganisaties pleiten voor 'Dark Sky Parks' en gemeenten experimenteren met slimme ledverlichting die automatisch dimt zodra er geen fietsers of auto's op de weg zijn. Bedrijven worden aangespoord om na sluitingstijd hun etalageverlichting en reclameborden resoluut te doven.",
    "Kortom: het licht hoeft heus niet overal definitief uit, maar een tikkeltje minder fel kan absoluut geen kwaad. Gemeenten en burgers moeten beseffen dat veiligheid prima hand in hand kan gaan met een gedimde nacht. Laten we de schakelaar vaker omzetten en de duisternis weer omarmen, want alleen wie het donker durft toe te laten, kan de sterren opnieuw zien stralen."
]
card_donker = maak_leestekst_card("Tekst A: De terugkeer van het donker", "Natuur & Milieu Magazine, 2025", donker_alineas, "6 alinea's")

esports_alineas = [
    "In een kolkende arena in Zuid-Korea juichen tienduizend uitzinnige fans een groep jongeren toe die op een gigantisch podium achter futuristische computerschermen zit. Op gigantische led-wanden flitsen digitale monsters, magische spreuken en bliksemsnelle manoeuvres voorbij. De winnaar van dit toernooi gaat naar huis met een prijzenpot van ruim twee miljoen dollar. Maar is dit urenlange gevecht met toetsenbord en muis wel échte topsport, of kijken we hier naar een zwaar gehypte vorm van computerverslaving?",
    "De discussie over de sportstatus van zogeheten e-sports laait al jaren fel op bij traditionele sportbonden. Tegenstanders wijzen er minachtend op dat gamen zittend gebeurt achter een bureau. 'Sport vereist fysieke uitputting, modder, zweet en rennen over een echt grasveld', zo luidt het veelgehoorde oordeel van traditionele atleten en sportjournalisten.",
    "Wetenschappelijk onderzoek van de Duitse Sportuniversiteit van Keulen toont echter een heel ander beeld. Professionele gamers leveren fysieke en mentale prestaties die vergelijkbaar zijn met die van Formule 1-coureurs en tafeltennissers. Ze halen hartslagen van 160 tot 180 slagen per minuut en produceren evenveel stresshormonen als marathonlopers. Daarnaast voeren ze tot wel vierhonderd precieze hand- en oogbewegingen per minuut uit op een split-second niveau.",
    "Bovendien trainen tope-sporters tegenwoordig minstens zo serieus als profvoetballers. Ze volgen strenge fitnessprogramma's om hun rug- en nekspieren te versterken, houden zich aan een strikt voedingsschema en worden intensief begeleid door sportpsychologen om mentale druk tijdens grote toernooien het hoofd te bieden.",
    "Zelfs het Internationaal Olympisch Comité (IOC) kan de enorme populariteit en professionalisering niet langer negeren en overweegt serieuze toevoeging van digitale disciplines aan toekomstige evenementen.",
    "Al met al kunnen we concluderen dat e-sports de kinderschoenen van zolderkamervermaak definitief is ontgroeid. Hoewel een gamer niet over een atletiekbaan sprint, vereist topgamen uitzonderlijke motoriek, tactisch inzicht en mentale weerbaarheid. Het is tijd dat critici hun vooroordelen laten varen en inzien dat de sportwereld van de 21e eeuw niet alleen van gras en gravel is gemaakt, maar ook van pixels en passie."
]
card_esports = maak_leestekst_card("Tekst B: E-sports: topsport of zolderkamervermaak?", "Sport & Maatschappij, 2025", esports_alineas, "6 alinea's")

vragen_ex14 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Welke techniek gebruikt de auteur in alinea 1 van Tekst A om de aandacht van de lezer te trekken?",
        "opties": [
            "Het schetsen van een opvallend contrast tussen stad en natuur",
            "Het citeren van een middeleeuws gedicht over de nacht",
            "Een reeks ingewikkelde statistische tabellen presenteren",
            "Een interview met een sterrenkundige weergeven"
        ],
        "antwoord": 0,
        "uitleg": "De auteur contrasteert de donkere sterrenhemel op de Veluwe met de fletse oranje gloed boven steden als Rotterdam en Utrecht."
    },
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Wat is de functie van de vraagzin aan het slot van alinea 1 in Tekst A?",
        "opties": [
            "De centrale probleemstelling van de tekst introduceren",
            "Aantonen dat sterrenkijken een nutteloze hobby is",
            "De lezer adviseren om direct een telescoop aan te schaffen",
            "Kritiek leveren op het beleid van de gemeente Rotterdam"
        ],
        "antwoord": 0,
        "uitleg": "De vraag formuleert de centrale probleemstelling van het artikel: verliezen we iets essentieels door overmatige verlichting?"
    },
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Welke historische verklaring geeft alinea 2 voor onze huidige overvloed aan kunstlicht?",
        "opties": [
            "Mensen associëren donker al eeuwenlang met gevaar en onveiligheid",
            "In de negentiende eeuw was elektriciteit gratis beschikbaar",
            "Vroegere vorsten eisten dat steden dag en nacht verlicht waren",
            "Gaslantaarns werkten destijds veel feller dan moderne lampen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 legt uit dat donkere stegen synoniem stonden voor criminaliteit en dat licht al eeuwen met veiligheid geassocieerd wordt."
    },
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Welk verband bestaat er tussen alinea 3 en alinea 4 van Tekst A?",
        "opties": [
            "Alinea 4 voegt de gevolgen voor mensen toe aan die voor dieren",
            "Alinea 4 ontkracht de onderzoeksresultaten uit alinea 3",
            "Alinea 4 beschrijft de historische oorzaak van alinea 3",
            "Alinea 4 geeft een samenvatting van alle diersoorten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 behandelt ecologische gevolgen voor dieren; alinea 4 breidt dit uit naar de gezondheid van de mens (opsommend/uitbreidend verband)."
    },
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Wat is de voornaamste functie van alinea 6 (de slotalinea) van Tekst A?",
        "opties": [
            "Een samenvattende conclusie met een concrete aanbeveling geven",
            "Een geheel nieuw wetenschappelijk tegenargument introduceren",
            "Uitsluitend cijfers over energieverspilling herhalen",
            "Een felle persoonlijke ruzie met een politicus beslechten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat samen ('Kortom...'), formuleert een conclusie en geeft een aanbeveling/oproep aan gemeenten en burgers."
    },
    {
        "type": "mc",
        "figuur": card_donker,
        "vraag": "Welke stijlfiguur herken je in de laatste zin van Tekst A ('...want alleen wie het donker durft toe te laten, kan de sterren opnieuw zien stralen')?",
        "opties": [
            "Een fraaie uitsmijter die teruggrijpt op de inleiding",
            "Een feitelijke opsomming van drie sterrenbeelden",
            "Een formele waarschuwing van de politie",
            "Een ironische grap over de weersverwachting"
        ],
        "antwoord": 0,
        "uitleg": "Dit is een typische uitsmijter (fraaie afsluiter) die mooi aansluit bij de opening over het zien van sterren in alinea 1 (cirkelstructuur)."
    },
    {
        "type": "waaronwaar",
        "figuur": card_donker,
        "vraag": "Volgens alinea 4 bevordert een gebrek aan duisternis juist de aanmaak van melatonine in ons lichaam.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt juist dat afwezigheid van natuurlijk donker de aanmaak van melatonine verstoort en onderdrukt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_donker,
        "vraag": "Volgens alinea 5 experimenteren gemeenten met ledverlichting die dimt wanneer er geen verkeer is.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt letterlijk in alinea 5 genoemd als een van de slimme maatregelen om donkerte te beschermen."
    },
    {
        "type": "open",
        "figuur": card_donker,
        "vraag": "Welke twee adviezen of maatregelen worden in alinea 5 en 6 genoemd om lichtvervuiling tegen te gaan?",
        "sleutelwoorden": [
            "dimmen/slimme ledverlichting/verlichting dimmen",
            "doven/etalages uitschakelen/reclame uitzetten"
        ],
        "minTreffers": 1,
        "modelantwoord": "Het toepassen van slimme ledverlichting die dimt en het doven van etalageverlichting en reclameborden na sluitingstijd.",
        "uitleg": "In alinea 5 en 6 worden het dimmen van slimme straatverlichting en het uitschakelen van etalage- en reclamelichten na sluitingstijd genoemd."
    },
    {
        "type": "invul",
        "figuur": card_donker,
        "vraag": "Met welk signaalwoord van samenvatting begint de slotalinea van Tekst A?",
        "antwoord": "Kortom|kortom",
        "uitleg": "'Kortom' kondigt aan dat de auteur in de laatste alinea de hoofdpunten samenvat."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Welke techniek gebruikt de schrijver in alinea 1 van Tekst B om de lezer bij het verhaal te betrekken?",
        "opties": [
            "Een levendige beschrijving van een spectaculaire actuele situatie",
            "Het citeren van een wetboek over kansspelen",
            "Een historische terugblik op schaken in de middeleeuwen",
            "Het afdrukken van een wiskundig algoritme"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 opent met een sfeertekening van een vol stadion met tienduizend fans en flitsende ledschermen."
    },
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Welke tegenstelling staat centraal in de inleiding (alinea 1 en 2) van Tekst B?",
        "opties": [
            "De vraag of e-sports topsport is of slechts computerverslaving",
            "Het verschil tussen de spelregels van voetbal en basketbal",
            "De concurrentie tussen computerfabrikanten in Azië",
            "De salarisverschillen tussen mannen en vrouwen in de sport"
        ],
        "antwoord": 0,
        "uitleg": "De inleiding stelt de vraag centraal of e-sports echte topsport is of een gehypte zolderkamerverslaving."
    },
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Wat is het belangrijkste argument van tegenstanders in alinea 2?",
        "opties": [
            "Echte sport vereist fysieke uitputting, zweet en rennen in de modder",
            "Computers zijn veel te duur voor de meeste jongeren",
            "Bij gamen is er nooit sprake van een echte scheidsrechter",
            "De wedstrijden duren meestal korter dan tien minuten"
        ],
        "antwoord": 0,
        "uitleg": "Tegenstanders menen dat gamen zittend gebeurt en dat sport gepaard moet gaan met fysieke uitputting, zweet en rennen."
    },
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Welke functie heeft alinea 3 in de opbouw van Tekst B ten opzichte van alinea 2?",
        "opties": [
            "Weerlegging van de kritiek met wetenschappelijke meetgegevens",
            "Herhaling van de stelling van traditionele sporters",
            "Een overzicht van de populairste computerspellen ter wereld",
            "Het aankondigen van een staking onder traditionele atleten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 ontkracht het idee dat gamen fysiek niets voorstelt met meetgegevens (hartslag 160-180, 400 bewegingen per minuut) van de Duitse Sportuniversiteit."
    },
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Welke conclusie trekt de auteur in alinea 6 van Tekst B?",
        "opties": [
            "E-sports is zolderkamervermaak ontgroeid en verdient erkenning als sport",
            "Gamen moet verboden worden voor jongeren onder de achttien jaar",
            "Traditioneel voetbal zal binnen vijf jaar volledig verdwijnen",
            "De Olympische Spelen moeten uitsluitend nog online plaatsvinden"
        ],
        "antwoord": 0,
        "uitleg": "De auteur concludeert dat topgamen volwaardige topsport is en dat critici hun vooroordelen moeten laten varen."
    },
    {
        "type": "mc",
        "figuur": card_esports,
        "vraag": "Wat typeert de uitsmijter aan het einde van Tekst B ('...niet alleen van gras en gravel is gemaakt, maar ook van pixels en passie')?",
        "opties": [
            "Een allitererende en beeldende samenvatting van de hoofdgedachte",
            "Een letterlijke waarschuwing voor beschadigde beeldschermen",
            "Een aankondiging van een nieuwe voetbalcompetitie",
            "Een vraag waarin de auteur toegeeft dat hij het ook niet weet"
        ],
        "antwoord": 0,
        "uitleg": "De uitsmijter gebruikt stijlfiguren (alliteratie van p/g en contrast) om het artikel krachtig en memorabel af te sluiten."
    },
    {
        "type": "waaronwaar",
        "figuur": card_esports,
        "vraag": "Volgens alinea 3 halen topgamers tijdens wedstrijden nauwelijks een hogere hartslag dan iemand die ontspannen tv-kijkt.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt dat zij piekhartslagen van 160 tot 180 slagen per minuut bereiken, vergelijkbaar met coureurs en lopers."
    },
    {
        "type": "waaronwaar",
        "figuur": card_esports,
        "vraag": "Volgens alinea 5 overweegt het Internationaal Olympisch Comité om digitale disciplines toe te voegen aan evenementen.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt letterlijk genoemd in alinea 5 als bewijs voor de groeiende erkenning van e-sports."
    },
    {
        "type": "open",
        "figuur": card_esports,
        "vraag": "Welke twee voorbeelden van professionele training worden in alinea 4 genoemd waaruit blijkt dat tope-sporters serieus trainen?",
        "sleutelwoorden": [
            "fitness/rugspieren versterken/fysieke training",
            "voedingsschema/sportpsycholoog/mentale begeleiding"
        ],
        "minTreffers": 1,
        "modelantwoord": "Ze volgen strenge fitnessprogramma's voor rug en nek en hanteren een strikt voedingsschema of mentale begeleiding.",
        "uitleg": "Alinea 4 noemt fitnessprogramma's ter versterking van rug- en nekspieren, een strikt voedingsschema en sportpsychologen."
    },
    {
        "type": "invul",
        "figuur": card_esports,
        "vraag": "Met welk signaalwoord van conclusie opent de slotalinea van Tekst B?",
        "antwoord": "Al met al|al met al",
        "uitleg": "'Al met al' is een vaste signaalwoordgroep om een slotconclusie in te luiden."
    }
]

# ==============================================================================
# TOETS 15: §5 VASTE TEKSTSTRUCTUREN (TOETS F)
# Tekst A: Snelladers en laadstress (Probleem-oplossing)
# Tekst B: Vogelmigratie / Trek (Vraag-antwoord / Verschijnsel-verklaring)
# ==============================================================================
laadpaal_alineas = [
    "Wie deze zomer met een elektrische auto richting Zuid-Frankrijk reed, zag het tafereel bij bijna elk tankstation langs de Route du Soleil: rijen toeterende automobilisten die nerveus op hun dashboard tuurden, verhitte discussies over wie het eerst mocht inpluggen en oververhitte laadpalen die weigerden dienst te doen. De zogeheten 'laadstress' dreigt een serieuze domper te zetten op de overstap naar duurzaam rijden. Hoe lossen we dit acute capaciteitsprobleem op voordat het Europese wegennet definitief vastloopt?",
    "De hoofdoorzaak van deze verkeerschaos is niet zozeer een tekort aan laadpalen, maar de enorme piekbelasting op het elektriciteitsnetwerk. Op piekdagen willen duizenden automobilisten tegelijkertijd in twintig minuten honderd kilowattuur stroom door een laadkabel jagen. Lokale transformatorhuisjes en stroomkabels zijn simpelweg niet berekend op zulke monsterlijke vermogens, waardoor netbeheerders gedwongen zijn om snelladers tijdelijk af te schakelen.",
    "Bovendien ontbreekt het aan slimme afstemming. Veel vakantiegangers laden hun batterij standaard vol tot 100 procent, terwijl het laden boven de 80 procent twee keer zoveel tijd kost en de wachtrijen onnodig verdubbelt.",
    "Om deze knelpunten op te lossen, werken energiebedrijven aan innovatieve maatregelen. Een eerste veelbelovende oplossing is de plaatsing van reusachtige 'bufferbatterijen' bij snelwegstations. Deze megabatterijen laden 's nachts geleidelijk op wanneer de stroom goedkoop is en het net rustig is, en leveren overdag razendsnel piekstroom aan passerende vakantiegangers zonder het openbare stroomnet te belasten.",
    "Daarnaast kan een dynamisch prijssysteem wonderen verrichten. Door snelladen tijdens piekdagen duurder te maken en laden tot maximaal 80 procent financieel te belonen, spreidt de verkeersstroom zich automatisch veel beter over rustigere locaties.",
    "Al met al is laadstress geen onoplosbare crisis, maar een typische groeistuip van de energietransitie. Door bufferbatterijen te combineren met slimme beprijzing en duidelijke voorlichting over efficiënt snelladen, kunnen we zonder files en stress koers zetten naar een emissieloze toekomst."
]
card_laadpaal = maak_leestekst_card("Tekst A: Laadstress op de Route du Soleil", "Mobiliteit & Toekomst, 2025", laadpaal_alineas, "6 alinea's")

migratie_alineas = [
    "Ieder najaar voltrekt zich boven onze hoofden een van de grootste wonderen der natuur. Miljoenen vogels verlaten hun broedgebieden in Europa en vliegen duizenden kilometers naar het zuiden om te overwinteren. De absolute recordhouder is de noordse stern: een sierlijke vogel die jaarlijks van de poolcirkel naar Antarctica en weer terug reist — een onvoorstelbare reis van ruim zeventigduizend kilometer. Hoe slagen deze gevederde navigators erin om zonder gps, kompas of wegenkaart feilloos hun tropische bestemming te vinden?",
    "Decennialang stonden biologen voor een raadsel, maar recent biologisch en natuurkundig onderzoek heeft de complexe navigatiekunst van trekvogels stap voor stap ontrafeld. Het antwoord blijkt te liggen in een ingenieus samenspel van meerdere zintuiglijke systemen.",
    "Allereerst beschikken trekvogels over een fenomenaal oriëntatievermogen op basis van hemellichamen. Overdag bepalen zij hun vliegrichting aan de hand van de stand van de zon, gecorrigeerd door hun interne biologische klok. Nachtvliegers, zoals de grasmus en de roodborst, oriënteren zich daarentegen op de patronen van de sterren rondom de Poolster.",
    "Nog spectaculairder is het ontdekte 'kwantumkompas' in de vogelogen. In het netvlies bevindt zich een speciaal lichtgevoelig eiwit (cryptochroom). Wanneer blauw licht op dit eiwit valt, ontstaan zogeheten verstrengelde radicalen die uiterst gevoelig zijn voor het magnetisch veld van de aarde. Hierdoor kan de vogel het magnetische veld letterlijk als lichte en donkere vlekken in zijn gezichtsveld 'zien'.",
    "Tot slot maken vogels op kortere afstand gebruik van een geurkaart en herkenbare landschapselementen, zoals bergketens, rivierlopen en kustlijnen, om hun exacte broedhol of tak van het voorgaande jaar terug te vinden.",
    "Samenvattend kunnen we stellen dat trekvogels niet op één enkel hulpmiddel vertrouwen, maar over een gelaagd navigatiesysteem beschikken. Door zon, sterren, aardmagnetisme en geuren naadloos te combineren, blijven zij de absolute meesters van het luchtruim. Voor ingenieurs die autonome drones ontwikkelen, vormt het vogelbrein dan ook nog altijd de ultieme inspiratiebron."
]
card_migratie = maak_leestekst_card("Tekst B: Het geheime kompas van de trekvogel", "Biologie & Natuurwonderen, 2025", migratie_alineas, "6 alinea's")

vragen_ex15 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Welke vaste tekststructuur herken je overduidelijk in Tekst A?",
        "opties": [
            "De probleem-oplossingstructuur",
            "De verleden-heden-toekomststructuur",
            "De bewering-argumentstructuur",
            "De aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst A schetst een probleem (laadstress, overbelasting netwerk) en draagt daarna concrete oplossingen aan (bufferbatterijen, slimme beprijzing)."
    },
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Welk onderdeel van de vaste tekststructuur wordt uitgewerkt in alinea 2 en 3 van Tekst A?",
        "opties": [
            "De diepere oorzaken van het geschetste probleem",
            "De historische achtergrond van fossiele brandstoffen",
            "De uiteindelijke eindoordelen van de rechters",
            "Een lijst met voordelen van elektrische auto's"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 en 3 behandelen de oorzaken: netcongestie/piekbelasting en het inefficiënt laden tot 100 procent."
    },
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Welke eerste concrete oplossing wordt in alinea 4 aangedragen?",
        "opties": [
            "Het installeren van reusachtige bufferbatterijen bij snellaadstations",
            "Het volledig verbieden van vakantieritten naar Zuid-Frankrijk",
            "Het verplicht stellen van een trekhaak met dieselaggregaat",
            "Het verhogen van de maximale snelheid naar 150 km per uur"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 introduceert bufferbatterijen die 's nachts stroom opslaan en overdag pieken opvangen."
    },
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Welk signaalwoord van tegenstelling markeert in alinea 3 een nieuw nadeel of knelpunt?",
        "opties": [
            "Bovendien",
            "Omdat",
            "Waardoor",
            "Kortom"
        ],
        "antwoord": 0,
        "uitleg": "'Bovendien' voegt hier een extra oorzaak/knelpunt toe aan het probleem."
    },
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Welke functie vervult de laatste alinea (alinea 6) in de gekozen tekststructuur?",
        "opties": [
            "Een samenvatting van de oplossingen en een hoopvolle conclusie",
            "Het introduceren van een compleet nieuw milieuprobleem",
            "Het bekritiseren van Franse benzinetankstations",
            "Een oproep om alle elektrische wagens direct te verkopen"
        ],
        "antwoord": 0,
        "uitleg": "In een probleem-oplossingstructuur bevat het slot een evaluatie/samenvatting van de oplossingen en een hoopvolle toekomstblik."
    },
    {
        "type": "mc",
        "figuur": card_laadpaal,
        "vraag": "Waarom is het laden van een batterij tot 100 procent volgens alinea 3 inefficiënt tijdens drukte?",
        "opties": [
            "Boven de 80 procent laadt de batterij twee keer zo traag",
            "Boven de 80 procent explodeert de kabel spontaan",
            "De stroomprijs verdrievoudigt automatisch per kilowattuur",
            "Het navigatiesysteem van de auto raakt dan ontregeld"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat laden boven de 80% twee keer zoveel tijd kost en wachttijden onnodig verdubbelt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_laadpaal,
        "vraag": "Volgens alinea 2 is het stroomnetwerk prima bestand tegen duizenden snelladers die tegelijk piekstroom vragen.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst meldt juist dat kabels en transformators niet berekend zijn op deze piekbelastingen en snelladers moeten uitschakelen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_laadpaal,
        "vraag": "Volgens alinea 5 kan een dynamisch prijssysteem helpen om de drukte bij laadstations beter te spreiden.",
        "antwoord": True,
        "uitleg": "Waar. Hogere prijzen tijdens pieken en belonen van laden tot 80% stimuleren automobilisten om slimmer te spreiden."
    },
    {
        "type": "open",
        "figuur": card_laadpaal,
        "vraag": "Welke twee specifieke oplossingen worden in alinea 4 en 5 uitgewerkt om de laaddrukte te beteugelen?",
        "sleutelwoorden": [
            "bufferbatterij/megabatterij/batterijen",
            "dynamisch prijssysteem/tarieven varieren/prijzen"
        ],
        "minTreffers": 1,
        "modelantwoord": "De plaatsing van megabatterijen als buffer en de invoering van een dynamisch prijssysteem.",
        "uitleg": "In alinea 4 worden bufferbatterijen genoemd en in alinea 5 een dynamisch prijssysteem om pieken te spreiden."
    },
    {
        "type": "invul",
        "figuur": card_laadpaal,
        "vraag": "Welk signaalwoord van doel-middel kondigt in alinea 4 de introductie van maatregelen aan?",
        "antwoord": "Om|om",
        "uitleg": "'Om deze knelpunten op te lossen' geeft een doel aan waarvoor maatregelen (middelen) worden ingezet."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Welke vaste tekststructuur domineert Tekst B?",
        "opties": [
            "De vraag-antwoordstructuur (of verschijnsel-verklaring)",
            "De voor- en nadelenstructuur",
            "De historische structuur van verleden tot heden",
            "De stelling-argumentstructuur"
        ],
        "antwoord": 0,
        "uitleg": "De tekst start met een centrale vraag over een opmerkelijk natuurverschijnsel en geeft in het middenstuk verklaringen/antwoorden."
    },
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Wat is het centrale verschijnsel dat in alinea 1 wordt geïntroduceerd?",
        "opties": [
            "De feilloze langeafstandsmigratie van trekvogels",
            "De opwarming van de poolzeeën rondom Antarctica",
            "Het uitsterven van zangvogels in West-Europa",
            "De economische schade van vogels bij windmolenparken"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 beschrijft hoe trekvogels zoals de noordse stern tienduizenden kilometers vliegen en feilloos navigeren."
    },
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Welk mechanisme gebruiken dagtrekkers volgens alinea 3 om koers te houden?",
        "opties": [
            "De stand van de zon gecorrigeerd door hun biologische klok",
            "Het geluid van brekende golven op de rotskusten",
            "De temperatuurverschillen tussen warme en koude luchtlagen",
            "De richting van passerende passagiersvliegtuigen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 vermeldt dat dagvliegers navigeren op de zonnestand in combinatie met hun interne biologische klok."
    },
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Wat ontdekten wetenschappers over het 'kwantumkompas' in het vogelnetvlies (alinea 4)?",
        "opties": [
            "Cryptochroom stelt de vogel in staat magnetische velden te zien",
            "De vogel heeft een piepklein magnetisch ijzerdraadje in zijn snavel",
            "De vogel voelt trillingen in de aardkorst via zijn klauwen",
            "Vogels communiceren via onhoorbaar ultrasoon geluid"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 beschrijft dat het eiwit cryptochroom reageert op licht en magnetisme, waardoor de vogel het aardmagnetisch veld kan 'zien'."
    },
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Welke signaalwoorden markeren de opeenvolgende deelaspecten van de navigatie in alinea 3, 4 en 5?",
        "opties": [
            "Allereerst, nog spectaculairder, tot slot",
            "Omdat, dientengevolge, daardoor",
            "Hoewel, desalniettemin, toch",
            "Kortom, samenvattend, ten slotte"
        ],
        "antwoord": 0,
        "uitleg": "De opsomming van zintuiglijke systemen wordt gestructureerd door 'Allereerst' (3), 'Nog spectaculairder' (4) en 'Tot slot' (5)."
    },
    {
        "type": "mc",
        "figuur": card_migratie,
        "vraag": "Wat is de hoofdconclusie van de auteur in alinea 6 van Tekst B?",
        "opties": [
            "Trekvogels benutten een ingenieus samenspel van meerdere systemen",
            "Binnenkort kunnen vogels niet meer vliegen door klimaatverandering",
            "GPS-navigatie van mensen is veel nauwkeuriger dan het vogelkompas",
            "De noordse stern is de enige vogel ter wereld die 's nachts kan vliegen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat samen dat vogels niet op één instrument vertrouwen, maar over een gelaagd en gecombineerd systeem beschikken."
    },
    {
        "type": "waaronwaar",
        "figuur": card_migratie,
        "vraag": "Volgens alinea 3 navigeren nachtvliegers zoals de grasmus uitsluitend op de maanstand en negeren zij de sterren.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt dat zij zich oriënteren op de patronen van de sterren rondom de Poolster."
    },
    {
        "type": "waaronwaar",
        "figuur": card_migratie,
        "vraag": "Volgens alinea 5 gebruiken vogels op kortere afstand ook geurkaarten en landschapselementen.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 5 noemt geurkaarten, kustlijnen, bergketens en rivierlopen voor navigatie op korte afstand."
    },
    {
        "type": "open",
        "figuur": card_migratie,
        "vraag": "Welke twee navigatiehulpmiddelen gebruiken trekvogels overdag en 's nachts volgens alinea 3?",
        "sleutelwoorden": [
            "stand van de zon/de zon/zonnestand",
            "sterren/sterrenpatronen/poolster"
        ],
        "minTreffers": 1,
        "modelantwoord": "Overdag gebruiken ze de stand van de zon en 's nachts de sterrenpatronen rondom de Poolster.",
        "uitleg": "Alinea 3 vermeldt de stand van de zon (overdag) en de sterrenpatronen rond de Poolster (voor nachtvliegers)."
    },
    {
        "type": "invul",
        "figuur": card_migratie,
        "vraag": "Met welk signaalwoord van samenvatting begint de slotbeschouwing in alinea 6 van Tekst B?",
        "antwoord": "Samenvattend|samenvattend",
        "uitleg": "'Samenvattend' geeft aan dat de auteur in de laatste alinea de hoofdpunten bijeenbrengt."
    }
]

# ==============================================================================
# TOETS 16: §2 INLEIDING EN SLOT (TOETS G)
# Tekst A: Microplastics in kleding (Anekdote, vraagstelling, slotadvies/uitsmijter)
# Tekst B: Angst voor technologie / Red Flag Act (Historisch citaat, cirkelstructuur)
# ==============================================================================
fleece_alineas = [
    "Het voelt heerlijk zacht en behaaglijk: die donzige fleechetrui die je aantrekt op een gure herfstdag. Maar terwijl die trui in de wasmachine vrolijk ronddraait met je favoriete wasmiddel, voltrekt zich een onzichtbare ecologische ramp. Bij elke wasbeurt spoelen tot wel een miljoen microscopisch kleine plastic vezels uit de stof via het riool rechtstreeks onze rivieren en oceanen in. Is onze hang naar goedkope, synthetische mode een sluipende bedreiging voor de wereldwijde voedselketen?",
    "Sinds de uitvinding van polyester en nylon in het midden van de twintigste eeuw is de textielindustrie radicaal getransformeerd. Waar kleding vroeger werd geweven van zuivere wol, linnen of katoen, bestaat tegenwoordig ruim zestig procent van alle kledingstukken uit aardolie. Synthetische stoffen zijn immers spotgoedkoop te produceren, kreukvrij en sneldrogend.",
    "Het probleem is echter dat deze synthetische polymeren in het milieu vrijwel niet biologisch afbreekbaar zijn. De minuscule draadjes zijn zo microscopisch klein dat rioolwaterzuiveringsinstallaties ze niet volledig kunnen tegenhouden. Ze drijven de zee op, waar vissen en garnalen ze aanzien voor voedsel en opeten.",
    "Via consumptie van vis en schelpdieren belanden de giftige microplastics uiteindelijk op ons eigen bord. Wetenschappers van de Vrije Universiteit Amsterdam troffen recentelijk zelfs microplastics aan in menselijk bloed. Welke gezondheidsschade deze deeltjes op lange termijn aanrichten, is nog volstrekt onduidelijk.",
    "Gelukkig ontstaan er innovatieve oplossingen. Speciale waszakken met ultrafijne maaswijdte vangen de loslatende vezels op vóórdat ze de afvoer bereiken. Ook experimenteren wasmachinefabrikanten met ingebouwde microplasticfilters en stimuleren ontwerpers de terugkeer naar natuurlijke textielvezels.",
    "Kortom: we kunnen onze ogen niet langer sluiten voor de keerzijde van synthetische mode. Zowel de kledingindustrie als de consument moet zijn verantwoordelijkheid nemen. Denk de volgende keer als je voor het kledingrek staat dus twee keer na over het label: kies voor natuurlijke materialen en was synthetische kleding minder vaak. Want alleen als we bewuster omgaan met onze garderobe, voorkomen we dat onze eigen truien ons uiteindelijk letterlijk de keel uithangen."
]
card_fleece = maak_leestekst_card("Tekst A: De onzichtbare gifstroom uit je wasmachine", "Milieu & Samenleving, 2025", fleece_alineas, "6 alinea's")

redflag_alineas = [
    "In 1865 voerde het Britse parlement een van de opmerkelijkste wetten uit de transportgeschiedenis in: de beruchte 'Locomotive Act', beter bekend als de 'Red Flag Act'. De wet schreef voor dat voor elk zelfrijdend stoomvoertuig een man met een rode vlag moest uitlopen om voetgangers en koetsiers te waarschuwen voor het naderende 'duivelse gevaarte'. Automobielen mochten in de stad niet sneller rijden dan drie kilometer per uur. Ruim anderhalve eeuw later klinkt dit bizar, maar reageren we tegenwoordig bij zelfrijdende auto's en kunstmatige intelligentie eigenlijk niet precies hetzelfde?",
    "Elke revolutionaire technologische doorbraak roept bij de mensheid aanvankelijk diepe angst en weerstand op. Toen de eerste stoomtreinen in de negentiende eeuw over rails raasden, waarschuwden gerespecteerde artsen bloedserieus dat de menselijke hersenen zouden bezwijken bij snelheden boven de dertig kilometer per uur.",
    "Vandaag de dag zien we een treffende herhaling van dit patroon bij de introductie van autonome voertuigen. Elk incident met een zelfrijdende Tesla of Google-robotaxi haalt met grote chocoladeletters de voorpagina's, vergezeld van verontruste oproepen om de technologie direct aan banden te leggen.",
    "Natuurlijk brengt automatisering reële dilemma's met zich mee: wie is er aansprakelijk bij een ongeval en hoe programmeer je morele keuzes in een computeralgoritme? Maar tegenstanders vergeten vaak dat menselijke bestuurders jaarlijks wereldwijd meer dan een miljoen dodelijke verkeersongevallen veroorzaken door vermoeidheid, alcohol en afleiding door smartphones. Een robotauto wordt nooit slaperig en appt nooit achter het stuur.",
    "Historische ervaring leert dat samenlevingen uiteindelijk altijd een balans vinden tussen bescherming en innovatie door verstandige wetgeving en strenge veiligheidstesten.",
    "Concluderend kunnen we stellen dat angst voor verandering van alle tijden is, maar technologie niet te stoppen valt. In plaats van krampachtig met een denkbeeldige rode vlag voor autonome auto's uit te blijven lopen, moeten we de techniek omarmen en kritisch perfectioneren. Alleen dan plukken we de vruchten van een toekomst waarin verkeersongelukken definitief tot het verleden behoren."
]
card_redflag = maak_leestekst_card("Tekst B: De denkbeeldige rode vlag", "Geschiedenis & Techniek, 2025", redflag_alineas, "6 alinea's")

vragen_ex16 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Welke techniek past de schrijver toe in de inleiding van Tekst A om de lezer direct aan te spreken?",
        "opties": [
            "Een herkenbare, zintuiglijke situatie beschrijven die omslaat in een probleem",
            "Het citeren van een Frans scheikundig handboek uit 1900",
            "Een formele lijst van alle wasmachinemerken in Europa geven",
            "Een juridische aanklacht tegen kledingfabrikanten citeren"
        ],
        "antwoord": 0,
        "uitleg": "De auteur begint met het zachte gevoel van een behaaglijke fleece trui en verbindt dit direct met het onzichtbare milieuprobleem."
    },
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Wat is de functie van de vraag aan het einde van alinea 1 van Tekst A?",
        "opties": [
            "Het formuleren van de centrale probleemstelling van de tekst",
            "Vragen om donaties voor een dierenopvangcentrum",
            "Controleren of de lezer wel goed kan rekenen",
            "Het bekritiseren van de werking van waspoeder"
        ],
        "antwoord": 0,
        "uitleg": "De vraag introduceert het kernthema: vormt synthetische kleding een bedreiging voor de wereldwijde voedselketen?"
    },
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Welke historische verschuiving wordt in alinea 2 van Tekst A beschreven?",
        "opties": [
            "De overgang van natuurlijke vezels naar synthetische aardoliestoffen",
            "De uitvinding van het allereerste houten spinnewiel",
            "De ontdekking van zijderupsen in het verre oosten",
            "Het verdwijnen van katoenplantages in Amerika"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 beschrijft hoe sinds de komst van polyester en nylon kleding voor 60% uit synthetische aardoliestoffen bestaat."
    },
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Welk schokkend onderzoeksfeit wordt in alinea 4 van Tekst A genoemd?",
        "opties": [
            "Er zijn zelfs microplastics aangetroffen in menselijk bloed",
            "Alle vissen in de Noordzee zijn inmiddels blind geworden",
            "Wasmachines gaan gemiddeld nog maar één jaar mee",
            "Synthetische truien lossen na drie wasbeurten volledig op"
        ],
        "antwoord": 0,
        "uitleg": "Onderzoekers van de Vrije Universiteit troffen recentelijk microplastics aan in menselijk bloed."
    },
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Wat is de functie van de laatste alinea (alinea 6) van Tekst A?",
        "opties": [
            "Een samenvatting met een dringende oproep en advies aan de consument",
            "Een overzicht geven van de prijzen van wasmachines",
            "Aantonen dat natuurlijke wol even schadelijk is als plastic",
            "Het aankondigen van een nieuw kledingmerk van de auteur"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat samen en geeft concrete adviezen (label checken, natuurlijke stoffen kiezen, minder wassen)."
    },
    {
        "type": "mc",
        "figuur": card_fleece,
        "vraag": "Welke dubbele betekenis of woordspeling herken je in de uitsmijter van Tekst A ('...letterlijk de keel uithangen')?",
        "opties": [
            "Een spreekwoord over kleding combineren met biologische verstikking",
            "Een citaat uit een bekend Nederlands toneelstuk",
            "Een grapje over stropdassen die te strak zitten",
            "Een verwijzing naar een traditionele waslijn"
        ],
        "antwoord": 0,
        "uitleg": "De uitsmijter speelt geestig in op de uitdrukking 'de keel uithangen' (iets beu zijn) en het letterlijke gevaar van microplastics."
    },
    {
        "type": "waaronwaar",
        "figuur": card_fleece,
        "vraag": "Volgens alinea 3 kunnen rioolwaterzuiveringsinstallaties alle microplastic vezels moeiteloos uit het afvalwater zeven.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst meldt juist dat de deeltjes zo minuscuul zijn dat zuiveringsinstallaties ze niet volledig tegenhouden."
    },
    {
        "type": "waaronwaar",
        "figuur": card_fleece,
        "vraag": "Volgens alinea 5 bestaan er speciale waszakken met ultrafijne maaswijdte die vezels tegenhouden.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt in alinea 5 genoemd als een innovatieve manier om vezels op te vangen."
    },
    {
        "type": "open",
        "figuur": card_fleece,
        "vraag": "Welke twee handelingsadviezen geeft de auteur in alinea 6 aan de koper van kleding?",
        "sleutelwoorden": [
            "natuurlijke materialen/stoffen/wol/katoen",
            "minder vaak wassen/minder wassen/label checken"
        ],
        "minTreffers": 1,
        "modelantwoord": "Kiezen voor natuurlijke materialen en kleding minder vaak wassen.",
        "uitleg": "In alinea 6 adviseert de schrijver: kies voor natuurlijke materialen en was synthetische kleding minder vaak."
    },
    {
        "type": "invul",
        "figuur": card_fleece,
        "vraag": "Met welk signaalwoord van samenvatting luidt de auteur alinea 6 van Tekst A in?",
        "antwoord": "Kortom|kortom",
        "uitleg": "'Kortom' vat de eerdere argumenten samen in de slotalinea."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Welke aandachtstrekker gebruikt de auteur in de inleiding (alinea 1) van Tekst B?",
        "opties": [
            "Een historische wet en bizarre anekdote uit de negentiende eeuw",
            "Een schokkende statistiek over hedendaags smartphonegebruik",
            "Een persoonlijk dagboekfragment van een buschauffeur",
            "Het beschrijven van een dodelijke aanrijding op een racecircuit"
        ],
        "antwoord": 0,
        "uitleg": "De schrijver opent met de historische 'Red Flag Act' uit 1865, waarbij een man met een rode vlag voor auto's uit moest lopen."
    },
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Wat is de functie van de vergelijking tussen de negentiende eeuw en het heden in alinea 1 en 2?",
        "opties": [
            "Laten zien dat angst voor nieuwe technologie een terugkerend fenomeen is",
            "Bewijzen dat stoomwagens veiliger waren dan moderne elektrische auto's",
            "Aantonen dat wetgeving in Engeland altijd vooroploopt",
            "De uitvinding van het paard en de wagen belachelijk maken"
        ],
        "antwoord": 0,
        "uitleg": "De auteur toont aan dat de mensheid bij elke grote vernieuwing (stoomtreinen, auto's, AI) aanvankelijk angstig reageert."
    },
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Welk sterk tegenargument ten gunste van de zelfrijdende auto wordt in alinea 4 aangevoerd?",
        "opties": [
            "Mensen veroorzaken miljoenen ongelukken door afleiding en vermoeidheid",
            "Robotauto's kunnen over water varen als er een file staat",
            "Een computergestuurde auto verbruikt helemaal geen elektriciteit",
            "Robotauto's hebben geen banden nodig en veroorzaken geen slijtage"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 benadrukt dat menselijke fouten (afleiding door telefoons, vermoeidheid, alcohol) jaarlijks miljoenen ongelukken veroorzaken, terwijl robots daar geen last van hebben."
    },
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Welk signaalwoord van tegenstelling kondigt in alinea 4 het verweer tegen critici aan?",
        "opties": [
            "Maar",
            "Immers",
            "Doordat",
            "Vandaar"
        ],
        "antwoord": 0,
        "uitleg": "'Maar tegenstanders vergeten vaak...' geeft een directe weerlegging van de tegenargumenten."
    },
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Op welke manier vormt het slot (alinea 6) een cirkelstructuur met de inleiding van Tekst B?",
        "opties": [
            "Door terug te grijpen op het beeld van de rode vlag uit alinea 1",
            "Door opnieuw de datum 1865 te noemen",
            "Door dezelfde Britse parlementsleden te interviewen",
            "Door de tekst te eindigen met een Engelse vertaling"
        ],
        "antwoord": 0,
        "uitleg": "De auteur verwijst in het slot naar 'krampachtig met een denkbeeldige rode vlag voor autonome auto's uit blijven lopen', wat teruggrijpt op de opening (cirkelstructuur)."
    },
    {
        "type": "mc",
        "figuur": card_redflag,
        "vraag": "Wat is de hoofdgedachte van Tekst B?",
        "opties": [
            "We moeten angst voor innovatie overwinnen en technologie perfectioneren",
            "De Red Flag Act had nooit ingetrokken mogen worden door Engeland",
            "Zelfrijdende auto's moeten voor altijd verboden blijven in binnensteden",
            "Mensen zijn betere chauffeurs dan computers ooit zullen worden"
        ],
        "antwoord": 0,
        "uitleg": "De hoofdgedachte is dat weerstand tegen vernieuwing van alle tijden is, maar dat we de techniek moeten omarmen en veilig perfectioneren."
    },
    {
        "type": "waaronwaar",
        "figuur": card_redflag,
        "vraag": "Volgens alinea 2 waren artsen in de negentiende eeuw meteen enthousiast over de enorme snelheden van de stoomtrein.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst vermeldt dat artsen serieus waarschuwden dat hersenen zouden bezwijken bij snelheden boven 30 km/u."
    },
    {
        "type": "waaronwaar",
        "figuur": card_redflag,
        "vraag": "Volgens alinea 4 brengt automatisering ook reële vraagstukken over aansprakelijkheid en ethische keuzes met zich mee.",
        "antwoord": True,
        "uitleg": "Waar. Alinea 4 erkent expliciet reële dilemma's zoals wettelijke aansprakelijkheid en morele beslissingen."
    },
    {
        "type": "open",
        "figuur": card_redflag,
        "vraag": "Welke twee menselijke tekortkomingen noemt de auteur in alinea 4 als hoofdoorzaak van dodelijke verkeersongevallen?",
        "sleutelwoorden": [
            "vermoeidheid/slaperigheid/slaap",
            "afleiding/smartphones/telefoons/alcohol"
        ],
        "minTreffers": 1,
        "modelantwoord": "Vermoeidheid en afleiding door smartphones (of alcoholgebruik).",
        "uitleg": "Alinea 4 vermeldt vermoeidheid, alcohol en afleiding door smartphones als menselijke oorzaken van ongevallen."
    },
    {
        "type": "invul",
        "figuur": card_redflag,
        "vraag": "Met welk signaalwoord van conclusie begint de laatste alinea van Tekst B?",
        "antwoord": "Concluderend|concluderend",
        "uitleg": "'Concluderend' geeft aan dat de schrijver zijn slotconclusie presenteert."
    }
]

# ==============================================================================
# TOETS 17: §5 VASTE TEKSTSTRUCTUREN (TOETS G)
# Tekst A: De 4-daagse werkweek (Voor- en nadelenstructuur)
# Tekst B: Geld door de eeuwen heen (Verleden-heden-toekomst / Chronologisch)
# ==============================================================================
werkweek_alineas = [
    "Steeds meer bedrijven in Europa experimenteren met een revolutionair arbeidsmodel: de vierdaagse werkweek met behoud van honderd procent salaris. Werknemers werken tweeëndertig uur in plaats van veertig, maar worden geacht dezelfde resultaten neer te zetten. Voorstanders spreken van een gouden formule voor het moderne gezinsleven, terwijl verontruste ondernemers vrezen voor torenhoge kosten en haperende dienstverlening. Is het schrappen van de vrijdag een zegen voor de samenleving, of een onbetaalbare illusie?",
    "Aan de voordelenkant wijzen talloze proefprojecten op verbluffende resultaten. Het belangrijkste pluspunt is een spectaculaire toename van het mentale welzijn: werknemers ervaren aanzienlijk minder werkstress, waardoor het ziekteverzuim met tientallen procenten daalt. Met een extra vrije dag hebben mensen meer tijd voor sport, mantelzorg en hun gezin, wat zorgt voor een betere balans tussen werk en privé.",
    "Bovendien blijkt de arbeidsproductiviteit verrassend genoeg nauwelijks te lijden onder de kortere week. Doordat personeel fitter en uitgeruster aan de start verschijnt, vervallen nutteloze vergaderingen en kletspraatjes bij het koffiezetapparaat, waardoor mensen in vier dagen evenveel werk verzetten als voorheen in vijf.",
    "Daar staan echter aanzienlijke nadelen en praktische knelpunten tegenover. Niet elke sector leent zich voor dit flexibele model. In cruciale beroepen zoals de zorg, het onderwijs en het openbaar vervoer kan een kortere werkweek niet simpelweg worden opgevangen door 'slimmer en sneller' te werken. Een verpleegkundige kan immers niet twintig procent sneller medicijnen uitdelen zonder de patiëntveiligheid in gevaar te brengen.",
    "Bovendien kampen veel van deze sectoren al met schrijnende personeelstekorten. Als zorgmedewerkers en leraren een dag minder gaan werken, moeten werkgevers extra personeel aannemen dat er simpelweg niet is, wat leidt tot torenhoge loonkosten en dichte ziekenhuisafdelingen.",
    "Afwegend kunnen we concluderen dat de vierdaagse werkweek geen universeel wondermiddel is dat klakkeloos op de hele economie kan worden toegepast. Op kantoor kan het model leiden tot fittere werknemers en hogere efficiëntie, maar in praktische diensten en zorgsectoren leidt het tot onoverkomelijke gaten in de roosters. Een maatwerkbenadering per sector is dan ook de enige realistische weg voorwaarts."
]
card_werkweek = maak_leestekst_card("Tekst A: De vierdaagse werkweek: paradijs of strop?", "Economie & Werk, 2025", werkweek_alineas, "6 alinea's")

geld_alineas = [
    "We betalen onze lunch tegenwoordig met een vingerafdruk op onze smartphone, scannen een QR-code op een festivalterrein en zien onze salarissen verschijnen als niets meer dan een reeks veranderende cijfers op een bankscherm. Fysieke munten en knisperende bankbiljetten verdwijnen in rap tempo uit het straatbeeld. Hoe is dit magische ruilmiddel dat we 'geld' noemen eigenlijk ontstaan, en hoe zal de toekomst van betalen eruitzien?",
    "Vroeger, ver voor het begin van onze jaartelling, kende de mensheid helemaal geen geld. Men deed aan directe ruilhandel: een zak graan werd geruild voor een wollen deken of twee kippen. Dit systeem had echter een groot praktisch mankement: als de pottenbakker geen kippen nodig had, kon de kippenboer geen soepkom kopen. Om dit probleem op te lossen, kozen vroege samenlevingen universele ruilmiddelen die schaars en houdbaar waren, zoals kauri-schelpen, zoutblokken en later zilveren en gouden munten.",
    "In de zeventiende eeuw, met de opkomst van de Amsterdamse Wisselbank, ontstond het heden van ons financiële systeem. Bankiers gaven papieren ontvangstbewijzen uit voor opgeslagen goud: het allereerste papiergeld. Gedurende de twintigste eeuw werd dit fiatgeld: geld dat geen intrinsieke waarde heeft, maar puur steunt op het vertrouwen in de overheid en centrale banken.",
    "Tegenwoordig is ruim negentig procent van al het geld in omloop al volledig digitaal, beheerd door commerciële banken en betalingsapps.",
    "In de nabije toekomst zal geld naar verwachting nóg radicaler transformeren. Centrale banken ontwikkelen de digitale euro (CBDC): een digitale munt die direct wordt uitgegeven door de Europese Centrale Bank. Tegelijkertijd winnen gedecentraliseerde cryptomunten terrein als alternatief zonder staatsbemoeienis. Contant geld zal vermoedelijk binnen enkele decennia een historisch museumstuk worden.",
    "Kortom: geld heeft een fascinerende reis afgelegd van tastbare schelpen en munten naar onzichtbare computercodes. De vorm verandert voortdurend mee met de stand van de techniek, maar de oeroude kernfunctie blijft altijd ongewijzigd: geld is en blijft het smeermiddel van menselijke samenwerking en onderling vertrouwen."
]
card_geld = maak_leestekst_card("Tekst B: De evolutie van geld: van schelp tot algoritme", "Geschiedenis & Maatschappij, 2025", geld_alineas, "6 alinea's")

vragen_ex17 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Welke specifieke vaste tekststructuur volgt de auteur bij het uiteenzetten van de vierdaagse werkweek in Tekst A?",
        "opties": [
            "De voor- en nadelenstructuur",
            "De verleden-heden-toekomststructuur",
            "De vraag-antwoordstructuur",
            "De chronologische structuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst A behandelt eerst de positieve punten (voordelen) van de kortere werkweek en weegt die af tegen de bezwaren en knelpunten (nadelen)."
    },
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Wat wordt in alinea 2 van Tekst A als voornaamste voordeel genoemd?",
        "opties": [
            "Een forse stijging van het mentale welzijn en minder ziekteverzuim",
            "Dat iedereen automatisch twintig procent opslag krijgt",
            "Dat alle scholen in Nederland op vrijdag dicht kunnen",
            "Dat bedrijven geen belasting meer hoeven te betalen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 noemt toename van mentaal welzijn, minder werkstress en lagere ziekteverzuimcijfers als hoofdvoordelen."
    },
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Welk signaalwoord aan het begin van alinea 4 geeft de overgang aan van voordelen naar nadelen?",
        "opties": [
            "Daar staan echter",
            "Bovendien",
            "Kortom",
            "Allereerst"
        ],
        "antwoord": 0,
        "uitleg": "'Daar staan echter aanzienlijke nadelen tegenover' markeert de klassieke tegenstelling tussen voor- en nadelen."
    },
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Waarom is een vierdaagse werkweek in de zorgsector volgens alinea 4 en 5 zo problematisch?",
        "opties": [
            "Zorgwerk kan niet versneld worden en er is al een ernstig personeelstekort",
            "Patiënten zijn alleen ziek op maandag tot en met donderdag",
            "Ziekenhuizen hebben geen toegang tot digitale computersystemen",
            "Verpleegkundigen weigeren in de weekenden te werken"
        ],
        "antwoord": 0,
        "uitleg": "In de zorg kan werk niet 20% sneller zonder kwaliteitsverlies, en het extra benodigde personeel is er simpelweg niet."
    },
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Wat is het eindoordeel van de schrijver in de slotalinea (alinea 6)?",
        "opties": [
            "Het model is geen universeel wondermiddel; maatwerk per sector is vereist",
            "De overheid moet de vierdaagse werkweek per wet overal verbieden",
            "Alle werknemers moeten verplicht overstappen op zes werkdagen per week",
            "Over tien jaar werkt niemand meer in West-Europa"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 weegt af en concludeert dat een maatwerkbenadering per sector noodzakelijk is."
    },
    {
        "type": "mc",
        "figuur": card_werkweek,
        "vraag": "Welk argument wordt in alinea 3 gebruikt om te verklaren dat de totale opbrengst gelijk blijft?",
        "opties": [
            "Fitte werknemers verspillen minder tijd aan nutteloze kletspraatjes en vergaderingen",
            "Werknemers drinken veel meer koffie tijdens de lunch",
            "Bedrijven schaffen alle pauzes af op de overgebleven vier dagen",
            "Er worden robots aangeschaft die op vrijdag al het werk doen"
        ],
        "antwoord": 0,
        "uitleg": "Doordat mensen uitgeruster zijn, vervallen overbodige vergaderingen en kletspraatjes, waardoor men geconcentreerder werkt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_werkweek,
        "vraag": "Volgens alinea 1 gaan werknemers in het nieuwe model ook twintig procent minder salaris ontvangen.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt uitdrukkelijk dat het experiment plaatsvindt 'met behoud van honderd procent salaris'."
    },
    {
        "type": "waaronwaar",
        "figuur": card_werkweek,
        "vraag": "Volgens alinea 2 zorgt een extra vrije dag voor meer tijd voor mantelzorg en gezin.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt in alinea 2 letterlijk genoemd als een van de positieve effecten op het welzijn."
    },
    {
        "type": "open",
        "figuur": card_werkweek,
        "vraag": "Welke twee specifieke sectoren worden in alinea 4 genoemd waar een kortere werkweek lastig te realiseren is?",
        "sleutelwoorden": [
            "zorg/verpleging/ziekenhuis",
            "onderwijs/leraren/scholen/openbaar vervoer"
        ],
        "minTreffers": 1,
        "modelantwoord": "De zorg en het onderwijs (of openbaar vervoer).",
        "uitleg": "In alinea 4 worden expliciet de zorg, het onderwijs en het openbaar vervoer genoemd als sectoren waar niet zomaar sneller gewerkt kan worden."
    },
    {
        "type": "invul",
        "figuur": card_werkweek,
        "vraag": "Welk signaalwoord van afweging gebruikt de auteur aan het begin van alinea 6 om de conclusie in te luiden?",
        "antwoord": "Afwegend|afwegend",
        "uitleg": "'Afwegend' is het signaalwoord waarmee de auteur de voordelen en nadelen tegen elkaar afweegt in de conclusie."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Welke specifieke tekststructuur ligt ten grondslag aan de historische tijdlijn van het betaalmiddel in Tekst B?",
        "opties": [
            "De verleden-heden-toekomststructuur (chronologische structuur)",
            "De probleem-oplossingstructuur",
            "De stelling-argumentstructuur",
            "De voor- en nadelenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B beschrijft de ontwikkeling van geld: vroeger (ruilhandel/munten), heden (papiergeld/digitaal) en toekomst (CBDC/crypto)."
    },
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Welk groot mankement van directe ruilhandel wordt in alinea 2 beschreven?",
        "opties": [
            "Als de partijen elkaars waren niet nodig hebben, ketst de ruil af",
            "Ruilhandel was wettelijk streng verboden door Romeinse keizers",
            "Graan en kippen waren in de oudheid veel te giftig om aan te raken",
            "Mensen konden vroeger niet rekenen en wisten de aantallen niet"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 illustreert dat directe ruil mislukt als de pottenbakker geen kippen nodig heeft van de boer."
    },
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Wat was de historische functie van de eerste papieren bankbiljetten in de zeventiende eeuw (alinea 3)?",
        "opties": [
            "Ontvangstbewijzen voor goud dat veilig was opgeslagen in bankkluizen",
            "Waardebonnen die je alleen kon inwisselen voor specerijen in Indië",
            "Boetes die werden uitgedeeld aan smokkelaars op de Zuiderzee",
            "Tekeningen van beroemde schilders zoals Rembrandt van Rijn"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat bankiers papieren ontvangstbewijzen uitgaven voor fysiek goud dat bij hen in bewaring lag."
    },
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Welke twee toekomstige vormen van geld worden in alinea 5 genoemd?",
        "opties": [
            "De digitale centrale-bankeuro (CBDC) en cryptomunten",
            "Gouden dukaten en zilveren guldens",
            "Kauri-schelpen en blokken steenzout",
            "Plastic speelgoedmunten en postzegels"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 noemt de digitale euro van centrale banken en gedecentraliseerde cryptomunten als toekomstscenario's."
    },
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Welke signaalwoorden geven in Tekst B de tijdsfasen van de tekststructuur aan?",
        "opties": [
            "Vroeger, tegenwoordig, in de nabije toekomst",
            "Ten eerste, voorts, tot slot",
            "Omdat, dientengevolge, hierdoor",
            "Echter, daarentegen, desalniettemin"
        ],
        "antwoord": 0,
        "uitleg": "De signaalwoorden 'Vroeger' (alinea 2), 'Tegenwoordig' (alinea 4) en 'In de nabije toekomst' (alinea 5) tonen de verleden-heden-toekomststructuur."
    },
    {
        "type": "mc",
        "figuur": card_geld,
        "vraag": "Wat blijft volgens alinea 6 ondanks alle technologische veranderingen de onveranderde kern van geld?",
        "opties": [
            "Het functioneren als smeermiddel van samenwerking en onderling vertrouwen",
            "Dat het altijd gemaakt moet worden van zeldzame edelmetalen",
            "Dat het uitsluitend door koningen en keizers geslagen mag worden",
            "Dat het altijd met een vingerafdruk moet worden bevestigd"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 stelt dat de essentie van geld ongewijzigd blijft: het is een instrument van menselijke samenwerking en vertrouwen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_geld,
        "vraag": "Volgens alinea 4 bestaat meer dan de helft van al het geld in onze huidige maatschappij nog uit tastbare munten en biljetten.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt dat ruim negentig procent van al het geld tegenwoordig al volledig digitaal is."
    },
    {
        "type": "waaronwaar",
        "figuur": card_geld,
        "vraag": "Volgens alinea 2 dienden kauri-schelpen en zoutblokken in vroege samenlevingen al als universele ruilmiddelen.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt in alinea 2 letterlijk genoemd als voorbeelden van vroege universele ruilmiddelen."
    },
    {
        "type": "open",
        "figuur": card_geld,
        "vraag": "Welke twee eigenschappen moesten universele ruilmiddelen hebben volgens alinea 2 om succesvol te zijn?",
        "sleutelwoorden": [
            "schaars/zeldzaam/beperkt",
            "houdbaar/niet bederven/duurzaam"
        ],
        "minTreffers": 1,
        "modelantwoord": "Ze moesten schaars en goed houdbaar zijn.",
        "uitleg": "Alinea 2 vermeldt dat men koos voor goederen die 'schaars en houdbaar waren'."
    },
    {
        "type": "invul",
        "figuur": card_geld,
        "vraag": "Met welk signaalwoord van samenvatting begint de slotconclusie in alinea 6 van Tekst B?",
        "antwoord": "Kortom|kortom",
        "uitleg": "'Kortom' vat de historische lijn en kernboodschap samen in de slotparagraaf."
    }
]

examens = [
    {
        "file": "examen_14.js",
        "id": "ex-h3-nederlands-14",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 14 — §2 Inleiding en Slot (Toets F — Actuele Kwesties, Probleemstellingen & Oproepen)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex14
    },
    {
        "file": "examen_15.js",
        "id": "ex-h3-nederlands-15",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 15 — §5 Vaste Tekststructuren (Toets F — Probleem-Oplossing & Vraag-Antwoord)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex15
    },
    {
        "file": "examen_16.js",
        "id": "ex-h3-nederlands-16",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 16 — §2 Inleiding en Slot (Toets G — Historische Vergelijkingen, Anekdotes & Cirkelstructuren)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex16
    },
    {
        "file": "examen_17.js",
        "id": "ex-h3-nederlands-17",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 17 — §5 Vaste Tekststructuren (Toets G — Voor- en Nadelen & Verleden-Heden-Toekomst)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex17
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

print("Alle 4 examens (14 t/m 17) succesvol gegenereerd!")
