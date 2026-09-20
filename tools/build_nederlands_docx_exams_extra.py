# -*- coding: utf-8 -*-
"""
Generator voor 4 EXTRA HAVO 3 Nederlands leestoetsen:
- Toets 5: §2 Inleiding en Slot (Toets B — Tekstanalyse & Aandachtstrekkers)
- Toets 6: §2 Inleiding en Slot (Toets C — Probleemstelling & Hoofdgedachte)
- Toets 7: §5 Vaste Tekststructuren (Toets B — Modellen & Alineaverbanden)
- Toets 8: §5 Vaste Tekststructuren (Toets C — Signaalwoorden & Oorzaak-Gevolg)
"""
import json
import os
import re

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
# TEKSTEN VOOR TOETS 5 (§2 INLEIDING EN SLOT - TOETS B)
# ==============================================================================
vinyl_alineas = [
    "In 2024 werden er in Nederland voor het eerst in meer dan dertig jaar weer meer fysieke vinylplaten verkocht dan cd’s: een duizelingwekkend aantal van ruim 2,3 miljoen exemplaren. Terwijl muziek op streamingplatforms als Spotify met één muisklik oneindig beschikbaar is, staan jongeren van vijftien jaar in het weekend in lange rijen voor platenzaken. Hoe is het mogelijk dat een kwetsbare, zware zwarte schijf uit het midden van de vorige eeuw een ongekende comeback beleeft?",
    "Die verrassende herwaardering heeft alles te maken met onze behoefte aan tastbaarheid. In een wereld waarin alles digitaal, virtueel en vluchtig is geworden, verlangen muziekliefhebbers weer naar een product dat je kunt vasthouden, ruiken en bewonderen. Een elpeehoes is een tastbaar kunstwerk met songteksten, foto's en liners.",
    "Bovendien dwingt vinyl tot aandachtig luisteren. Wie een elpee opzet, moet de naald voorzichtig in de groef laten zakken en na twintig minuten opstaan om de plaat om te draaien. Er is geen shuffle-knop en je skipt niet na tien seconden door naar het volgende hitje. Het album wordt weer beluisterd zoals de artiest het ooit bedoeld heeft.",
    "Natuurlijk kent het draaien van grammofoonplaten ook flinke nadelen. Vinyl is duur: voor een nieuw studioalbum betaal je al snel dertig tot veertig euro. Daarnaast slijten platen door stof en krassen, en vereist een platenspeler goed afgestelde apparatuur met versterkers en speakers.",
    "Fabrikanten kunnen de explosieve vraag nauwelijks bijbenen. Platenperserijen in Europa draaien dag en nacht op volle toeren op gereviseerde machines uit de jaren zeventig. Zelfs popiconen als Taylor Swift en Harry Styles danken een aanzienlijk deel van hun monsterverkopen aan exclusieve, gekleurde vinylversies.",
    "Al met al blijkt de vinylplaat veel meer dan een voorbijgaande hipsterhype. Het is een bewust statement tegen de hap-snapcultuur van streamingdiensten en een ode aan ambachtelijke muziekbeleving. Wie de warmte van krakend vinyl eenmaal heeft ervaren, begrijpt waarom die 2,3 miljoen zwarte schijven over de toonbank vlogen."
]
card_vinyl = maak_leestekst_card("Tekst A: De wedergeboorte van het zwarte goud", "Muziek & Cultuur, 2025", vinyl_alineas, "6 alinea's")

noordzee_alineas = [
    "In de ijskoude stormnacht van 1 februari 1953 braken in Zeeland en Zuid-Holland tientallen dijken door. De woeste Noordzee overstroomde honderden dorpen en eiste 1836 mensenlevens. Deze historische ramp dwong ons land tot het ontwerpen van de wereldberoemde Deltawerken: een ingenieus netwerk van dammen en stormvloedkeringen dat Nederland voorgoed veilig moest maken tegen het water.",
    "Zeventig jaar later staat onze kustverdediging echter voor een volstrekt nieuwe beproeving. Door de wereldwijde opwarming van de aarde smelt het poolijs sneller dan ooit voorspeld. Wetenschappers van het KNMI waarschuwen dat de zeespiegel voor de Nederlandse kust deze eeuw met wel één tot twee meter kan stijgen.",
    "Die stijgende zeespiegel brengt gigantische vraagstukken met zich mee. Onze stormvloedkeringen, zoals de Oosterscheldekering en de Maeslantkering, zijn berekend op het klimaat van vroeger. Bij een structureel hogere waterstand moeten ze vaker dicht, wat schadelijk is voor de scheepvaart en de kwetsbare getijdennatuur.",
    "Daarnaast zorgt het zoute zeewater voor 'verzilting' van onze landbouwgronden: zoet drinkwater en vruchtbare polderakkers raken langzaam vergiftigd met zout kwelwater dat onder de duinen door sijpelt.",
    "Klimaatdeskundigen pleiten daarom voor een radicale koerswijziging: niet alleen maar starre betonnen muren bouwen, maar 'bouwen met de natuur'. Door zandsuppleties voor de kust en het aanleggen van brede duingebieden kan de kustlijn op een natuurlijke manier meegroeien met de zee.",
    "Kortom: de Noordzee die ons in 1953 zo wreed verraste, dwingt ons opnieuw tot ongekende waakzaamheid en innovatie. Willen we voorkomen dat toekomstige generaties met natte voeten komen te staan, dan moeten we niet wachten op de volgende stormvloed, maar vandaag al fors investeren in toekomstbestendige kustbescherming."
]
card_noordzee = maak_leestekst_card("Tekst B: De onstuitbare opmars van de Noordzee", "Geografie & Klimaat, 2024", noordzee_alineas, "6 alinea's")

# Sınav 5 soruları
vragen_ex5 = [
    {
        "type": "mc",
        "figuur": card_vinyl,
        "vraag": "Op welke manier probeert de auteur de aandacht te trekken in de openingsalinea van Tekst A?",
        "opties": [
            "Tot de verbeelding sprekende cijfers",
            "Een citaat uit de middeleeuwse literatuur",
            "Een fictief sprookje over robots",
            "Een waarschuwing voor gevaarlijke virussen"
        ],
        "antwoord": 0,
        "uitleg": "De auteur opent met opvallende verkoopcijfers (ruim 2,3 miljoen platen, meer dan cd's): 'tot de verbeelding sprekende cijfers rondom een verschijnsel'."
    },
    {
        "type": "mc",
        "figuur": card_vinyl,
        "vraag": "Op welke wijze introduceert de auteur het centrale onderwerp aan het einde van alinea 1 in Tekst A?",
        "opties": [
            "Door een juridisch wetsartikel te citeren",
            "Door een centrale onderzoeksvraag te formuleren",
            "Door direct een boze klacht in te dienen",
            "Door een stappenplan voor platenspelers te geven"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 1 sluit af met een prikkelende hoofdvraag: 'Hoe is het mogelijk dat een kwetsbare, zware zwarte schijf... een ongekende comeback beleeft?'"
    },
    {
        "type": "open",
        "figuur": card_vinyl,
        "vraag": "Waarom is Tekst A een schoolvoorbeeld van een tekst die 'mooi rond' is gemaakt?",
        "sleutelwoorden": ["slot/einde", "opening/inleiding/aandachtstrekker", "cijfers/miljoen/aansluiten/teruggrijpen"],
        "minTreffers": 1,
        "modelantwoord": "Omdat de schrijver in de slotalinea letterlijk teruggrijpt op de 2,3 miljoen verkochte exemplaren waarmee de inleiding begon.",
        "uitleg": "Alinea 6 verwijst aan het eind direct terug naar de verkoopcijfers uit alinea 1, wat de tekst inhoudelijk 'mooi rond' maakt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_vinyl,
        "vraag": "Volgens alinea 3 van Tekst A dwingt vinyl de luisteraar tot passief luisteren omdat je met een handige afstandsbediening snel liedjes kunt overslaan.",
        "antwoord": False,
        "uitleg": "Onwaar. In alinea 3 staat juist dat vinyl tot aandachtig luisteren dwingt omdat er géén shuffle-knop is en je niet zomaar skipt."
    },
    {
        "type": "invul",
        "figuur": card_vinyl,
        "vraag": "Met welke signaalwoordgroep opent de slotalinea (alinea 6) van Tekst A?",
        "antwoord": "al met al",
        "uitleg": "Alinea 6 opent met de signaalgroep 'Al met al'."
    },
    {
        "type": "mc",
        "figuur": card_noordzee,
        "vraag": "Welke aandachtstrekker gebruikt de schrijver in alinea 1 van Tekst B?",
        "opties": [
            "Een recente roddel over een filmster",
            "Iets van persoonlijk belang voor automobilisten",
            "Iets uit de geschiedenis",
            "Cijfers over de verkoop van strandhuisjes"
        ],
        "antwoord": 2,
        "uitleg": "De tekst opent met een terugblik naar een historisch ijkpunt: de Watersnoodramp van 1 februari 1953."
    },
    {
        "type": "mc",
        "figuur": card_noordzee,
        "vraag": "Hoe wordt het centrale probleem in alinea 2 van Tekst B geïntroduceerd?",
        "opties": [
            "Door een vrolijke anekdote over vakantiegangers",
            "Door een scherpe probleemstelling over zeespiegelstijging",
            "Door een handleiding over dijken bouwen",
            "Door een overzicht van scheepsongelukken"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 2 introduceert het knelpunt: de zeespiegelstijging als nieuwe bedreiging voor onze veiligheid."
    },
    {
        "type": "open",
        "figuur": card_noordzee,
        "vraag": "Welke twee functies vervult de slotalinea (alinea 6) van Tekst B?",
        "sleutelwoorden": ["conclusie/samenvatting", "aanbeveling/oproep/advies/investeren"],
        "minTreffers": 1,
        "modelantwoord": "Een samenvatting van de nieuwe dreiging én een dringende aanbeveling om nu fors te investeren in kustbescherming.",
        "uitleg": "Alinea 6 vat het probleem samen en formuleert een krachtige aanbeveling voor actie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_noordzee,
        "vraag": "Volgens de theorie van paragraaf 2 mag een slotalinea alleen maar bestaan uit een herhaling van het eerste woord van de tekst.",
        "antwoord": False,
        "uitleg": "Onwaar. Een slotalinea bevat een conclusie, samenvatting, aanbeveling en/of toekomstverwachting."
    },
    {
        "type": "mc",
        "vraag": "Wat verstaat de theorie van paragraaf 2 onder een 'probleemstelling' in de inleiding?",
        "opties": [
            "Een lijst met taalfouten in een proefwerk",
            "Een ruzie tussen de redactie en de uitgever",
            "Een duidelijke formulering van het knelpunt of vraagstuk dat centraal staat",
            "Een opsomming van moeilijke woorden met hun betekenis"
        ],
        "antwoord": 2,
        "uitleg": "De probleemstelling bakent helder af welk maatschappelijk of praktisch probleem in de tekst aan de orde komt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_noordzee,
        "vraag": "Ook Tekst B is 'mooi rond' gemaakt doordat de slotalinea teruggrijpt op de ramp van 1953 uit de inleiding.",
        "antwoord": True,
        "uitleg": "Waar. In alinea 6 noemt de auteur expliciet 'de Noordzee die ons in 1953 zo wreed verraste', wat direct aansluit bij alinea 1."
    },
    {
        "type": "invul",
        "figuur": card_noordzee,
        "vraag": "Welk signaalwoord aan het begin van alinea 6 kondigt aan dat de samenvattende afronding begint?",
        "antwoord": "kortom",
        "uitleg": "Alinea 6 opent met 'Kortom:'."
    },
    {
        "type": "mc",
        "figuur": card_vinyl,
        "vraag": "Welke titel zou het beste passen boven alinea 2 en 3 van Tekst A?",
        "opties": [
            "Fabrieken in geldnood",
            "De charme van tastbaarheid en focus",
            "Waarom vinyl binnenkort verdwijnt",
            "De geschiedenis van de compact disc"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 2 en 3 verklaren de aantrekkingskracht: tastbare kunst en onverdeelde luisteraandacht."
    },
    {
        "type": "open",
        "figuur": card_noordzee,
        "vraag": "In alinea 4 wordt het begrip 'verzilting' genoemd. Leg in je eigen woorden uit wat daarmee wordt bedoeld.",
        "sleutelwoorden": ["zout/zeewater", "grondwater/polder/zoet/landbouw/drinkwater"],
        "minTreffers": 1,
        "modelantwoord": "Het binnendringen van zout zeewater in zoet grondwater en landbouwgrond, waardoor drinkwater en gewassen worden aangetast.",
        "uitleg": "Alinea 4 beschrijft hoe zout kwelwater onder de duinen door sijpelt en zoet water vergiftigt."
    },
    {
        "type": "mc",
        "figuur": card_vinyl,
        "vraag": "Welke zin geeft het beste de hoofdgedachte van Tekst A (De wedergeboorte van het zwarte goud) weer?",
        "opties": [
            "Vinyl is een blijvende tegenbeweging tegen digitale vluchtigheid die voorziet in tastbaarheid en aandachtige muziekbeleving.",
            "Cd's zijn veel te goedkoop geworden waardoor platenzaken alleen nog elpees willen verkopen.",
            "Alleen popiconen als Taylor Swift kunnen nog profiteren van de verkoop van grammofoonplaten.",
            "Platenspelers zijn onhandig en veroorzaken veel te veel stof in de woonkamer."
        ],
        "antwoord": 0,
        "uitleg": "De tekst concludeert dat vinyl een bewuste keuze is voor tastbaarheid, rust en artistieke waarde boven digitale vluchtigheid."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een tekst waarin de auteur in de inleiding een standpunt inneemt en dit in het middenstuk onderbouwt, hoort bij een overtuigende tekst.",
        "antwoord": True,
        "uitleg": "Waar. Een standpunt verdedigen met argumenten heeft als doel de lezer te overtuigen van een mening."
    },
    {
        "type": "mc",
        "figuur": card_noordzee,
        "vraag": "Welke uitspraak verwoordt het meest adequaat de hoofdgedachte van Tekst B?",
        "opties": [
            "De zeespiegelstijging vereist dat we niet wachten op een nieuwe ramp, maar nu investeren in innovatieve kustbescherming.",
            "De Deltawerken uit 1953 zijn nog honderden jaren voldoende om Nederland te beschermen.",
            "De Maeslantkering moet het hele jaar door gesloten blijven voor de scheepvaart.",
            "Zeeland is de enige provincie in Nederland die gevaar loopt bij stormvloeden."
        ],
        "antwoord": 0,
        "uitleg": "De centrale boodschap is dat klimaatverandering ons dwingt om tijdig en proactief te investeren in nieuwe kustbescherming."
    },
    {
        "type": "open",
        "figuur": card_vinyl,
        "vraag": "Noem twee nadelen van vinyl die in alinea 4 van Tekst A worden besproken.",
        "sleutelwoorden": ["duur/prijs/kosten", "slijten/stof/krassen/apparatuur/kwetsbaar"],
        "minTreffers": 1,
        "modelantwoord": "Het is duur in aanschaf en het is kwetsbaar voor stof, krassen en slijtage (of vereist dure apparatuur).",
        "uitleg": "Alinea 4 somt de hoge aanschafprijs en de gevoeligheid voor slijtage en stof op."
    },
    {
        "type": "waaronwaar",
        "figuur": card_noordzee,
        "vraag": "In alinea 5 van Tekst B pleiten klimaatdeskundigen voor het uitsluitend storten van nog meer beton in zee in plaats van natuurlijk meegroeiende duinen.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 pleit juist voor 'bouwen met de natuur' (zandsuppleties en meegroeiende duinen) in plaats van starre betonnen muren."
    },
    {
        "type": "mc",
        "vraag": "Wat is volgens paragraaf 2 het voornaamste doel van de inleiding van een zakelijke tekst?",
        "opties": [
            "Alle moeilijke vaktermen alfabetisch rangschikken",
            "De lezer nieuwsgierig maken en het onderwerp introduceren",
            "Meteen de volledige bronnenlijst publiceren",
            "Direct beginnen met het slotakkoord van de auteur"
        ],
        "antwoord": 1,
        "uitleg": "De twee hoofdfuncties zijn: de aandacht trekken (nieuwsgierig maken) en het onderwerp helder introduceren."
    }
]

ex5_data = {
    "id": "ex-h3-nederlands-5",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "2",
    "titel": "Toets 5 — §2 Inleiding en Slot (Toets B — Tekstanalyse & Aandachtstrekkers)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🎯",
    "duurMin": 25,
    "vragen": vragen_ex5
}

# ==============================================================================
# TEKSTEN VOOR TOETS 6 (§2 INLEIDING EN SLOT - TOETS C)
# ==============================================================================
ai_zorg_alineas = [
    "Toen radioloog Peter de Vries op een drukke dinsdagmiddag honderden longscans beoordeelde, zag hij op foto 142 niets verontrustends. Maar het nieuwe zelflerende algoritme van het ziekenhuis sloeg alarm: een microscopisch stipje van amper twee millimeter werd rood omcirkeld. Een biopsie bevestigde het vermoeden: een beginnende tumor in een stadium dat voor het menselijk oog nog onzichtbaar was. De patiënt kon dankzij die tijdige vondst volledig genezen.",
    "Dit hoopgevende voorbeeld staat niet op zichzelf. Overal in de medische wereld rukt kunstmatige intelligentie (AI) op. Algoritmes analyseren weefsels, ontwerpen nieuwe medicijnen en voorspellen complicaties op de intensive care. Toch roept deze ontwikkeling ook felle weerstand en onrust op: gaan slimme computers binnenkort de rol van de empathische arts overnemen?",
    "Naar mijn overtuiging is die angst ongegrond. AI is geen bedreiging voor de dokter, maar juist het krachtigste hulpmiddel dat de moderne geneeskunde ooit heeft gekend. Slimme software kan bergen data verwerken, maar mist wezenlijke menselijke eigenschappen.",
    "Ten eerste bezit een algoritme geen empathie. Een computer kan een diagnose berekenen, maar kan geen troostende hand op de schouder leggen van een bange patiënt of aanvoelen wanneer iemand aarzelt bij een zware behandeling.",
    "Ten tweede vereist medische besluitvorming ethische afwegingen die niet in programmeercode te vangen zijn. Wanneer stop je met behandelen bij een terminaal zieke? Dat vraagt om menselijke wijsheid en compassie.",
    "Bovendien kan AI fouten maken door vertekende trainingsdata. Als een algoritme vooral getraind is op scans van westerse mannen, kan het symptomen bij vrouwen of andere bevolkingsgroepen over het hoofd zien. Een arts moet daarom altijd de eindcontrole behouden.",
    "Kortom: we moeten AI omarmen om diagnoses sneller en nauwkeuriger te stellen, zodat artsen meer tijd overhouden voor waar het werkelijk om draait: warme aandacht voor de mens achter de patiënt. Laat de computer rekenen, en de dokter zorgen."
]
card_ai_zorg = maak_leestekst_card("Tekst A: De dokter en het algoritme", "Wetenschap & Zorg, 2025", ai_zorg_alineas, "7 alinea's")

geluk_alineas = [
    "Je herkent het vast: na een slopende schooldag vol toetsen plof je futloos op de bank. Je hebt nergens zin in en je hoofd voelt als een wolk watten. Het laatste waar je op dat moment aan denkt, is je hardloopschoenen aantrekken of op de fiets stappen. Maar wie zichzelf toch over die drempel heensleept, ervaart binnen een halfuur een wonderlijke metamorfose: de vermoeidheid verdwijnt en maakt plaats voor een heldere, vrolijke energie.",
    "Waarom heeft een stevige wandeling of een partijtje basketbal zo'n directe invloed op ons gemoed? Wetenschappers van de Vrije Universiteit ontdekten dat lichaamsbeweging in onze hersenen een ware cocktail aan gelukshormonen activeert.",
    "Zodra je hartslag omhooggaat, produceren de hersenen endorfine en dopamine. Deze neurotransmitters verminderen stress, dempen pijn en creëren een gevoel van tevredenheid en euforie. Duursporters kennen dit als de befaamde 'runners high'.",
    "Bovendien stimuleert regelmatige beweging de aanmaak van BDNF, een speciaal eiwit dat zorgt voor de groei van nieuwe hersencellen in de hippocampus. Dat is precies het hersengebied dat verantwoordelijk is voor leren, geheugen en emotionele stabiliteit.",
    "Daar staat tegenover dat een zittende leefstijl funest is voor de mentale gezondheid. Wie urenlang stilzit achter een scherm, produceert meer van het stresshormoon cortisol, wat somberheid en angstgevoelens in de hand werkt.",
    "Al met al is bewegen het goedkoopste en meest effectieve medicijn tegen een somber humeur. Wie dagelijks dertig minuten matig intensief beweegt, versterkt niet alleen zijn spieren, maar poetst vooral zijn hersenen op. Dus kom van die bank af, trek je schoenen aan en ren die somberheid van je af!"
]
card_geluk = maak_leestekst_card("Tekst B: Waarom bewegen je brein oplaadt", "Psychologie & Gezondheid, 2024", geluk_alineas, "6 alinea's")

# Sınav 6 soruları
vragen_ex6 = [
    {
        "type": "mc",
        "figuur": card_ai_zorg,
        "vraag": "Welke aandachtstrekker gebruikt de auteur in alinea 1 van Tekst A?",
        "opties": [
            "Een fictieve toekomstvisie in het jaar 3000",
            "Een sprekend voorbeeld of korte anekdote",
            "Cijfers over werkloosheid onder artsen",
            "Een historisch overzicht van de middeleeuwen"
        ],
        "antwoord": 1,
        "uitleg": "De auteur opent met een waargebeurd en spannend voorbeeld: radioloog Peter de Vries die dankzij een algoritme een piepkleine tumor ontdekt."
    },
    {
        "type": "mc",
        "figuur": card_ai_zorg,
        "vraag": "Hoe introduceert de auteur het centrale onderwerp in alinea 2 en 3 van Tekst A?",
        "opties": [
            "Door een serie wettelijke regels voor te lezen",
            "Door een persoonlijk standpunt over AI in te nemen",
            "Door een woordenboekdefinitie van 'software' te geven",
            "Door de lezer op te roepen om programmeur te worden"
        ],
        "antwoord": 1,
        "uitleg": "In alinea 3 verwoordt de auteur helder zijn stellingname: 'Naar mijn overtuiging is die angst ongegrond. AI is geen bedreiging voor de dokter...'"
    },
    {
        "type": "open",
        "figuur": card_ai_zorg,
        "vraag": "Noem twee essentiële menselijke eigenschappen die een algoritme volgens alinea 4 en 5 mist.",
        "sleutelwoorden": ["empathie/inleving/troost/gevoel", "ethiek/ethische/compassie/wijsheid/besluitvorming"],
        "minTreffers": 1,
        "modelantwoord": "Empathie (echt medeleven en troost bieden) en ethische afwegingen (morele keuzes maken).",
        "uitleg": "Alinea 4 benadrukt het ontbreken van empathie en alinea 5 noemt ethische afwegingen en compassie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_ai_zorg,
        "vraag": "In alinea 6 van Tekst A stelt de auteur dat kunstmatige intelligentie volstrekt onfeilbaar is en nooit fouten kan maken door vooringenomen data.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 6 waarschuwt juist dat AI fouten kan maken door vertekende trainingsdata."
    },
    {
        "type": "invul",
        "figuur": card_ai_zorg,
        "vraag": "Met welk signaalwoord van conclusie opent alinea 7 van Tekst A?",
        "antwoord": "kortom",
        "uitleg": "Alinea 7 opent met 'Kortom:'."
    },
    {
        "type": "mc",
        "figuur": card_geluk,
        "vraag": "Welke aandachtstrekker herken je in alinea 1 van Tekst B?",
        "opties": [
            "Een overzicht van Olympische medailles",
            "Iets van direct persoonlijk belang voor de lezer",
            "Een juridische aanklacht tegen banken",
            "Cijfers over de wereldbevolking"
        ],
        "antwoord": 1,
        "uitleg": "De tekst spreekt de lezer direct aan op een herkenbare eigen ervaring na een schooldag: 'iets van persoonlijk belang'."
    },
    {
        "type": "mc",
        "figuur": card_geluk,
        "vraag": "Hoe wordt het onderwerp in alinea 2 van Tekst B geïntroduceerd?",
        "opties": [
            "Via een centrale onderzoeksvraag",
            "Via een recept voor sportdrank",
            "Via een interview met een topatleet",
            "Via een historisch jaartallenoverzicht"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 opent met de centrale vraag: 'Waarom heeft een stevige wandeling of een partijtje basketbal zo'n directe invloed op ons gemoed?'"
    },
    {
        "type": "open",
        "figuur": card_geluk,
        "vraag": "Welke twee functies herken je in de slotalinea (alinea 6) van Tekst B?",
        "sleutelwoorden": ["conclusie/samenvatting/medicijn", "aanbeveling/advies/oproep/bewegen/bank"],
        "minTreffers": 1,
        "modelantwoord": "Een conclusie/samenvatting over bewegen als effectief medicijn én een krachtige aanbeveling om van de bank af te komen en te gaan bewegen.",
        "uitleg": "Alinea 6 vat de voordelen samen en roept de lezer met een concreet advies op tot actie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_geluk,
        "vraag": "In Tekst B is er sprake van een tekst die 'mooi rond' is gemaakt, doordat de slotalinea teruggrijpt op de futloze bankhanger uit de inleiding.",
        "antwoord": True,
        "uitleg": "Waar. In alinea 6 sluit de auteur af met 'Dus kom van die bank af', wat direct teruggrijpt op het openingsbeeld van de bank in alinea 1."
    },
    {
        "type": "mc",
        "vraag": "Wat is volgens paragraaf 2 het verschil tussen een 'conclusie' en een 'aanbeveling' in een slotalinea?",
        "opties": [
            "Een conclusie bevat altijd cijfers en een aanbeveling bevat alleen werkwoorden",
            "Een conclusie is een logische slotsom; een aanbeveling geeft een praktisch advies voor actie",
            "Een conclusie staat altijd vooraan en een aanbeveling staat in het middenstuk",
            "Er is volgens de theorie geen enkel verschil tussen beide begrippen"
        ],
        "antwoord": 1,
        "uitleg": "Een conclusie trekt de inhoudelijke slotsom; de aanbeveling geeft raad of advies over wat men moet doen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_ai_zorg,
        "vraag": "Het tekstdoel van Tekst A is primair overtuigen, omdat de auteur de lezer wil winnen voor zijn stelling dat AI de arts versterkt in plaats van vervangt.",
        "antwoord": True,
        "uitleg": "Waar. De auteur verdedigt een duidelijk standpunt met argumenten om de lezer te overtuigen."
    },
    {
        "type": "invul",
        "figuur": card_geluk,
        "vraag": "Met welk signaalwoord opent alinea 6 van Tekst B om de samenvatting in te luiden?",
        "antwoord": "al met al",
        "uitleg": "Alinea 6 start met 'Al met al'."
    },
    {
        "type": "mc",
        "figuur": card_geluk,
        "vraag": "Welke titel zou het beste passen boven alinea 3 en 4 van Tekst B?",
        "opties": [
            "De gevaren van overtraining",
            "De chemische fabriek in je hoofd",
            "Waarom hardlopen geld kost",
            "De geschiedenis van de wandelsport"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 3 en 4 behandelen de hormonen en eiwitten (endorfine, dopamine, BDNF) die vrijkomen in het brein."
    },
    {
        "type": "open",
        "figuur": card_geluk,
        "vraag": "In alinea 5 van Tekst B wordt gewaarschuwd voor langdurig stilzitten. Welk negatief biochemisch effect wordt daar genoemd?",
        "sleutelwoorden": ["cortisol/stresshormoon", "somberheid/angst/stress"],
        "minTreffers": 1,
        "modelantwoord": "Wie urenlang stilzit produceert meer van het stresshormoon cortisol, wat somberheid en angst in de hand werkt.",
        "uitleg": "Alinea 5 toont aan dat stilzitten leidt tot een toename van het stresshormoon cortisol."
    },
    {
        "type": "mc",
        "figuur": card_ai_zorg,
        "vraag": "Welke uitspraak geeft de hoofdgedachte van Tekst A het meest accuraat weer?",
        "opties": [
            "Radiologen kunnen al hun werkzaamheden gerust delegeren aan zelflerende algoritmes.",
            "AI is een krachtig diagnostisch hulpmiddel dat de arts ondersteunt, zodat er meer tijd overblijft voor menselijke zorg en empathie.",
            "Kunstmatige intelligentie is te gevaarlijk om te gebruiken in de gezondheidszorg vanwege programmeerfouten.",
            "Peter de Vries is de enige radioloog in Nederland die met software tumoren opspoort."
        ],
        "antwoord": 1,
        "uitleg": "De kern van Tekst A is dat AI diagnoses versnelt en verbetert, waardoor de dokter meer tijd krijgt voor menselijke empathie."
    },
    {
        "type": "waaronwaar",
        "vraag": "De hoofdgedachte van een tekst kan volgens de regels van het Nederlands nooit een conclusie of samenvatting zijn.",
        "antwoord": False,
        "uitleg": "Onwaar. De hoofdgedachte is in het slot juist heel vaak geformuleerd als een conclusie of samenvatting."
    },
    {
        "type": "mc",
        "figuur": card_geluk,
        "vraag": "Welke zin verwoordt het beste de hoofdgedachte van Tekst B?",
        "opties": [
            "Regelmatig bewegen stimuleert gelukshormonen en hersengroei, en is daarmee een doeltreffend middel voor mentale veerkracht.",
            "De Vrije Universiteit heeft als enige universiteit onderzoek gedaan naar de runners high.",
            "Middelbare scholieren moeten stoppen met huiswerk maken en alleen nog sporten.",
            "Sporten is alleen gezond als je minstens drie uur per dag hardloopt."
        ],
        "antwoord": 0,
        "uitleg": "De hoofdgedachte vat samen dat bewegen gelukshormonen activeert en een bewezen effectief medicijn is voor het brein."
    },
    {
        "type": "open",
        "figuur": card_ai_zorg,
        "vraag": "Leg uit wat de auteur in alinea 7 bedoelt met de beeldende slotzin over de ideale taakverdeling in het ziekenhuis.",
        "sleutelwoorden": ["software/data/analyse/diagnose/berekening", "empathie/menselijke/compassie/persoonlijk"],
        "minTreffers": 1,
        "modelantwoord": "Technologie moet het snelle rekenwerk en de data-analyse doen, zodat medici zich kunnen concentreren op empathie en persoonlijke menselijke zorg.",
        "uitleg": "Alinea 7 vat de taakverdeling samen: technologie voor de berekeningen, de arts voor de persoonlijke en empathische zorg."
    },
    {
        "type": "waaronwaar",
        "figuur": card_ai_zorg,
        "vraag": "Alinea 7 van Tekst A kan niet beschouwd worden als een echte slotalinea omdat de auteur daarin een compleet nieuw onderwerp introduceert.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 7 is juist een volwaardige slotalinea: het vat het voorgaande betoog samen en trekt een heldere conclusie."
    },
    {
        "type": "mc",
        "vraag": "Welke signaalwoorden horen typisch thuis in een slotalinea?",
        "opties": [
            "Kortom, al met al, dus, daarom",
            "Ten eerste, ten tweede, om te beginnen",
            "Vroeger, eeuwen geleden, destijds",
            "Hoewel, ofschoon, daarentegen"
        ],
        "antwoord": 0,
        "uitleg": "Signaalwoorden als 'kortom', 'al met al', 'dus' en 'daarom' kondigen een samenvatting of slotsom aan."
    }
]

ex6_data = {
    "id": "ex-h3-nederlands-6",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "2",
    "titel": "Toets 6 — §2 Inleiding en Slot (Toets C — Probleemstelling & Hoofdgedachte)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🎯",
    "duurMin": 25,
    "vragen": vragen_ex6
}

# ==============================================================================
# TEKSTEN VOOR TOETS 7 (§5 VASTE TEKSTSTRUCTUREN - TOETS B)
# ==============================================================================
wolf_alineas = [
    "Na een afwezigheid van meer dan honderdvijftig jaar heeft de wolf zijn comeback gemaakt op de Nederlandse heide en in onze bossen. Sinds de eerste roedel zich op de Veluwe vestigde, laait het maatschappelijke debat hoog op. Is de terugkeer van dit iconische toproofdier een zegen voor onze verarmde natuur, of een onaanvaardbaar gevaar voor veehouders en wandelaars?",
    "Voorstanders en natuurbeschermers wijzen enthousiast op de ecologische voordelen. Als toproofdier vervult de wolf een sleutelrol in het natuurlijk evenwicht. Door te jagen op reeën, herten en wilde zwijnen houdt hij populaties gezond en voorkomt hij dat bossen worden kaalgevreten door wild. Kadavers die de wolf achterlaat, vormen bovendien een onmisbare voedselbron voor zeldzame kevers, raven en roofvogels.",
    "Daarnaast zorgt de aanwezigheid van de wolf voor het zogeheten 'landschap van angst': hoefdieren blijven alerter en vermijden open plekken, waardoor jonge boompjes spontaan kunnen opgroeien.",
    "Daar staat echter een schaduwzijde tegenover waar vooral schapenhouders de dupe van zijn. Wolven zijn opportunistische jagers; een wei vol tamme schapen is een veel makkelijkere prooi dan een alert wild zwijn. Jaarlijks worden honderden landbouwdieren doodgebeten, wat leidt tot grote emotionele en financiële schade bij boeren.",
    "Bovendien groeit de onrust onder dorpsbewoners en recreanten. Incidenten waarbij nieuwsgierige wolven wandelaars met honden dicht naderen, voeden de roep om het dier af te schieten of strenger te bejagen.",
    "Om het conflict te bezweren, experimenteren provincies met preventieve maatregelen: het subsidiëren van wolfwerende elektrische rasters en de inzet van getrainde kuddewaakhonden.",
    "Al met al brengt de wolf zowel waardevolle natuurlijke dynamiek als bittere conflicten met onze cultuurlandschappen. Alleen wanneer overheden veehouders ruimhartig compenseren en dwingen tot effectieve rasters, kan de wolf een duurzame plek behouden in ons dichtbevolkte land."
]
card_wolf = maak_leestekst_card("Tekst A: De wolf terug in Nederland: zegen of plaag?", "Natuurbeheer & Samenleving, 2024", wolf_alineas, "7 alinea's")

tornado_alineas = [
    "Van alle weersverschijnselen op aarde is de tornado ongetwijfeld het meest verwoestende en angstaanjagende. Binnen enkele seconden kan zo'n kolkende slurf van wind en puin een complete woonwijk van de kaart vegen. Hoe ontstaat deze atmosferische wervelwind en waarom komt hij vooral in Noord-Amerika zo veelvuldig voor?",
    "De geboorte van een tornado begint met een zogeheten 'supercell': een reusachtige, roterende onweersbui. Zo'n bui kan alleen ontstaan wanneer twee volstrekt verschillende luchtmassa's met elkaar in botsing komen. In de Amerikaanse 'Tornado Alley' botst warme, vochtige lucht uit de Golf van Mexico frontaal op ijskoude, droge lucht uit Canada en de Rocky Mountains.",
    "Wanneer deze luchtsoorten botsen, ontstaat sterke windschering: de wind waait op grote hoogte veel sneller en uit een andere richting dan aan de grond. Dit verschil zorgt ervoor dat de lucht tussen de lagen horizontaal begint te tollen, als een onzichtbare wentelende boomstam.",
    "Vervolgens zuigt een krachtige stijgstroom van warme lucht deze tollende buis omhoog, waardoor de rotatie verticaal komt te staan. De hele wolk begint nu rond te draaien; dit heet een mesocycloon.",
    "Als de rotatie krachtig genoeg is, vernauwt de draaikolk zich en zakt er een trechtervormige slurf uit de wolkenbasis omlaag naar het aardoppervlak. Pas op het moment dat de slurf de grond daadwerkelijk raakt, spreken meteorologen officieel van een tornado.",
    "De kracht van tornado's wordt uitgedrukt op de Enhanced Fujita-schaal (EF-schaal), variërend van EF0 (matige schade) tot EF5 (windsnelheden boven de 320 kilometer per uur, waarbij zelfs funderingen van huizen worden weggerukt).",
    "Samenvattend ontstaat een tornado uit een unieke en gewelddadige combinatie van botsende luchtmassa's, windschering en extreme opwaartse luchtstromen. Dankzij geavanceerde Doppler-radars slagen weermodellen er gelukkig steeds beter in om bewoners tijdig te waarschuwen."
]
card_tornado = maak_leestekst_card("Tekst B: De anatomie van de tornado", "Aardwetenschappen & Meteorologie, 2025", tornado_alineas, "7 alinea's")

# Sınav 7 soruları
vragen_ex7 = [
    {
        "type": "mc",
        "figuur": card_wolf,
        "vraag": "Welke vaste tekststructuur herken je in Tekst A (De wolf terug in Nederland)?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur",
            "Vraag-antwoordstructuur",
            "Verklaringsstructuur"
        ],
        "antwoord": 0,
        "uitleg": "De tekst weegt de voordelen voor het ecosysteem (al. 2-3) af tegen de nadelen voor veehouders (al. 4-5) en sluit af met een oordeel: een voor- en nadelenstructuur."
    },
    {
        "type": "mc",
        "figuur": card_wolf,
        "vraag": "Wat is het voornaamste tekstdoel van Tekst A?",
        "opties": [
            "Puur amuseren met spannende verhalen",
            "Beschouwen (de lezer laten nadenken over verschillende kanten van de wolf)",
            "Instrueren (een stappenplan geven voor schapen scheren)",
            "Activeren (oproepen om direct geld te doneren)"
        ],
        "antwoord": 1,
        "uitleg": "De auteur belicht beide zijden van het conflict om de lezer een afgewogen oordeel te laten vormen (beschouwen)."
    },
    {
        "type": "waaronwaar",
        "figuur": card_wolf,
        "vraag": "Volgens alinea 2 van Tekst A zijn kadavers van prooidieren volstrekt nutteloos en schadelijk voor de bosbodem.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 2 legt uit dat kadavers juist een onmisbare voedselbron vormen voor zeldzame kevers, raven en roofvogels."
    },
    {
        "type": "open",
        "figuur": card_wolf,
        "vraag": "In alinea 3 wordt het begrip 'landschap van angst' genoemd. Wat is het positieve gevolg hiervan voor het bos?",
        "sleutelwoorden": ["hoefdieren/wild/herten", "jonge/boompjes/opgroeien/bos/herstel"],
        "minTreffers": 1,
        "modelantwoord": "Hoefdieren blijven alerter en vermijden open plekken, waardoor jonge boompjes de kans krijgen om ongestoord op te groeien.",
        "uitleg": "Alinea 3 legt uit dat prooidieren door waakzaamheid open plekken mijden, zodat nieuw bos spontaan kan regenereren."
    },
    {
        "type": "invul",
        "figuur": card_wolf,
        "vraag": "Met welk signaalwoord van tegenstelling opent alinea 4 de bespreking van de problemen rondom de wolf?",
        "antwoord": "daar staat echter|echter",
        "uitleg": "Alinea 4 opent met: 'Daar staat echter een schaduwzijde tegenover...'"
    },
    {
        "type": "mc",
        "figuur": card_tornado,
        "vraag": "Welke vaste tekststructuur herken je in Tekst B (De anatomie van de tornado)?",
        "opties": [
            "Aspectenstructuur",
            "Probleem-oplossingsstructuur",
            "Verklaringsstructuur",
            "Argumentatiestructuur"
        ],
        "antwoord": 2,
        "uitleg": "De tekst legt stap voor stap uit hoe en waarom een tornado ontstaat (oorzaken, botsende luchtmassa's, stijgstromen): een verklaringsstructuur."
    },
    {
        "type": "mc",
        "figuur": card_tornado,
        "vraag": "Met welk hoofddoel heeft de auteur Tekst B (De anatomie van de tornado) geschreven?",
        "opties": [
            "De lezer overtuigen om te verhuizen",
            "De lezer informeren over het ontstaan van een natuurverschijnsel",
            "De lezer amuseren met stormavonturen",
            "De lezer instrueren hoe je een kelder graaft"
        ],
        "antwoord": 1,
        "uitleg": "De tekst biedt wetenschappelijke en feitelijke informatie over het weerfenomeen (informeren)."
    },
    {
        "type": "open",
        "figuur": card_tornado,
        "vraag": "Welke twee luchtsoorten botsen er volgens alinea 2 in Tornado Alley frontaal op elkaar?",
        "sleutelwoorden": ["warme/vochtige/golf/mexico", "koude/droge/canada/rocky"],
        "minTreffers": 1,
        "modelantwoord": "Warme, vochtige lucht uit de Golf van Mexico botst op koude, droge lucht uit Canada en de Rocky Mountains.",
        "uitleg": "Alinea 2 benoemt de botsing tussen warme subtropische zeelucht en ijskoude poollucht."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tornado,
        "vraag": "Volgens alinea 5 spreken meteorologen al van een tornado zodra er ergens hoog in de wolk een roterende beweging zichtbaar is, zelfs als die de grond niet raakt.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 benadrukt: 'Pas op het moment dat de slurf de grond daadwerkelijk raakt, spreken meteorologen officieel van een tornado.'"
    },
    {
        "type": "open",
        "figuur": card_tornado,
        "vraag": "Bedenk een passend tussenkopje boven de alinea's 3, 4 en 5 van Tekst B.",
        "sleutelwoorden": ["ontstaan/vorming/stappen", "windschering/slurf/trechter/rotatie"],
        "minTreffers": 1,
        "modelantwoord": "Het ontstaan van de slurf / Van windschering naar trechter / De geboorte van de wervelwind.",
        "uitleg": "Alinea 3 t/m 5 beschrijven het stapsgewijze proces van horizontale rotatie tot de grondaanraking van de slurf."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een artikel waarin de auteur een probleem schetst, de oorzaken daarvan analyseert en vervolgens verschillende oplossingen evalueert?",
        "opties": [
            "Probleem-oplossingsstructuur",
            "Aspectenstructuur",
            "Voor- en nadelenstructuur",
            "Vraag-antwoordstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Dit is de klassieke probleem-oplossingsstructuur."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een brochure waarin achtereenvolgens de geschiedenis, het onderwijs, de sportfaciliteiten en het schoolgebouw van een gymnasium worden gepresenteerd?",
        "opties": [
            "Verklaringsstructuur",
            "Argumentatiestructuur",
            "Aspectenstructuur",
            "Voor- en nadelenstructuur"
        ],
        "antwoord": 2,
        "uitleg": "Verschillende kanten of facetten van een onderwerp behandelen is typerend voor de aspectenstructuur."
    },
    {
        "type": "waaronwaar",
        "vraag": "In een verklaringsstructuur draait de inhoud om het 'hoe en waarom' van een bepaald verschijnsel.",
        "antwoord": True,
        "uitleg": "Waar. Een verklaringsstructuur legt oorzaken, redenen en werkingen van een verschijnsel uit."
    },
    {
        "type": "invul",
        "figuur": card_tornado,
        "vraag": "Met welk signaalwoord opent alinea 7 van Tekst B om de afronding in te luiden?",
        "antwoord": "samenvattend",
        "uitleg": "Alinea 7 opent met het woord 'Samenvattend'."
    },
    {
        "type": "mc",
        "figuur": card_wolf,
        "vraag": "Welke alinea van Tekst A draagt concrete oplossingen aan om schapenaanvallen door wolven tegen te gaan?",
        "opties": [
            "Alinea 1",
            "Alinea 4",
            "Alinea 6",
            "Alinea 2"
        ],
        "antwoord": 2,
        "uitleg": "Alinea 6 noemt elektrische rasters en kuddewaakhonden als preventieve maatregelen."
    },
    {
        "type": "open",
        "figuur": card_wolf,
        "vraag": "Vul het schema van oorzaak en gevolg aan op basis van alinea 4 van Tekst A: (1) Wolven zijn opportunistische jagers -> (2) Schapen zijn makkelijker te vangen dan wilde zwijnen -> (3) ...",
        "sleutelwoorden": ["doodgebeten/doden/aanval", "boeren/schade/emotioneel/financieel/landbouwdieren"],
        "minTreffers": 1,
        "modelantwoord": "Honderden landbouwdieren worden doodgebeten, wat leidt tot grote emotionele en financiële schade bij schapenhouders.",
        "uitleg": "Alinea 4 toont aan dat dit leidt tot massale doodgebeten schapen en grote schade voor boeren."
    },
    {
        "type": "waaronwaar",
        "vraag": "Signaalwoorden zoals 'doordat', 'daardoor', 'waardoor' en 'het gevolg hiervan is' wijzen op een oorzaak-gevolgverband.",
        "antwoord": True,
        "uitleg": "Waar. Deze voegwoorden en bijwoorden geven aan dat het ene feit het onvermijdelijke resultaat is van het andere."
    },
    {
        "type": "mc",
        "figuur": card_wolf,
        "vraag": "Welke zin geeft het beste de hoofdgedachte van Tekst A (De wolf terug in Nederland) weer?",
        "opties": [
            "De terugkeer van de wolf verrijkt onze natuur, maar kan alleen slagen als veehouders goed beschermd en gecompenseerd worden.",
            "De wolf hoort thuis op de Veluwe en alle veehouders moeten hun schapen maar binnenhouden.",
            "De wolf is een gevaarlijk roofdier dat direct moet worden afgeschoten om de recreatie te redden.",
            "In Nederland leven te veel reeën en zwijnen waardoor het bos compleet verdwijnt."
        ],
        "antwoord": 0,
        "uitleg": "De tekst brengt beide kanten bijeen: ecologische winst kan alleen samengaan met strenge bescherming en compensatie voor boeren."
    },
    {
        "type": "mc",
        "figuur": card_tornado,
        "vraag": "Welke zin verwoordt het meest adequaat de hoofdgedachte van Tekst B?",
        "opties": [
            "Tornado's zijn het resultaat van een botsing tussen polaire en subtropische lucht, die dankzij moderne radar steeds beter voorspeld kan worden.",
            "Tornado Alley is de enige plek ter wereld waar onweersbuien voorkomen.",
            "Een EF5-tornado kan alleen ontstaan als er geen Canadian air aanwezig is.",
            "Doppler-radars kunnen tornado's met laserstralen onschadelijk maken."
        ],
        "antwoord": 0,
        "uitleg": "De hoofdgedachte vat het meteorologische ontstaansproces en de verbeterde waarschuwingsmodellen samen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tornado,
        "vraag": "Op de Enhanced Fujita-schaal (alinea 6) staat EF0 voor de zwaarste categorie met windsnelheden boven 320 km/u.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 6 stelt dat EF0 staat voor matige schade en EF5 voor de zwaarste categorie boven 320 km/u."
    }
]

ex7_data = {
    "id": "ex-h3-nederlands-7",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "5",
    "titel": "Toets 7 — §5 Vaste Tekststructuren (Toets B — Modellen & Alineaverbanden)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🏗️",
    "duurMin": 25,
    "vragen": vragen_ex7
}

# ==============================================================================
# TEKSTEN VOOR TOETS 8 (§5 VASTE TEKSTSTRUCTUREN - TOETS C)
# ==============================================================================
trein_alineas = [
    "In 1829 vergaapte het Britse publiek zich aan de Rainhill Trials, waar de legendarische stoomlocomotief 'The Rocket' van George Stephenson een ongekende topsnelheid van 46 kilometer per uur haalde. Dokters waarschuwden destijds ernstig dat reizen met zulke duizelingwekkende snelheden zou leiden tot hersenschade en ademnood bij passagiers. Twee eeuwen later zoeven reizigers in magneetzweeftreinen met 400 kilometer per uur geruisloos door het landschap.",
    "De stormachtige geschiedenis van het spoor weerspiegelt de menselijke drang om afstanden te verkleinen. In de negentiende eeuw verbond het stoomspoor steden en industrieën met elkaar, wat leidde tot de industriële revolutie. Landen kregen voor het eerst een gestandaardiseerde landelijke tijdzone, omdat treinen volgens een strakke dienstregeling moesten rijden.",
    "In het midden van de twintigste eeuw werd de stoomtrein ingehaald door diesel- en elektrische treinen. Elektriciteit bleek sneller, schoner en betrouwbaarder. In 1964 zette Japan met de Shinkansen ('kogeltrein') de nieuwe standaard voor internationaal hogesnelheidsvervoer.",
    "Tegenwoordig vormen hogesnelheidslijnen zoals de Franse TGV en de Duitse ICE het ruggengraat van het Europese transportnetwerk. Ze bieden een comfortabel en milieuvriendelijk alternatief voor vervuilende korteafstandsvluchten.",
    "Maar de innovatie staat niet stil; de blik is inmiddels gericht op de toekomst. In China rijden commerciële magneetzweeftreinen (Maglev) die dankzij elektromagnetische velden boven de baan zweven. Zonder wrijvingsweerstand van rails kunnen deze treinen snelheden tot wel 600 kilometer per uur bereiken.",
    "De ultieme toekomstvisie is de zogeheten 'hyperloop': een capsule die door een vacuüm gezogen buis raast met de snelheid van een straalvliegtuig (meer dan 1000 km/u), met een fractie van het energieverbruik.",
    "Samenvattend heeft de trein zich in tweehonderd jaar getransformeerd van een krakend stoommonster tot een futuristische zweeftrein. In het tijdperk van klimaatcrisis en verstedelijking lijkt de trein meer dan ooit hét vervoermiddel van de toekomst te worden."
]
card_trein = maak_leestekst_card("Tekst A: Twee eeuwen spoor: van stoom tot zweeftrein", "Geschiedenis & Techniek, 2025", trein_alineas, "7 alinea's")

bijen_alineas = [
    "Wie in de lente door een boomgaard loopt, hoort het vertrouwde gezoem van duizenden ijverige insecten. Maar dat gezoem klinkt de laatste decennia steeds stiller. Wereldwijd luiden imkers en biologen de noodklok over alarmerende bijensterfte. Dat is geen klein ecologisch detail: ruim 70 procent van alle voedselgewassen die wij dagelijks consumeren – van sappige appels en aardbeien tot koffie en chocola – is voor bestuiving direct afhankelijk van bijen.",
    "Hoe komt het dat bijenpopulaties in zo'n alarmerend tempo instorten? Wetenschappelijk onderzoek toont aan dat er sprake is van een fatale cocktail aan oorzaken. De belangrijkste boosdoener is het grootschalige gebruik van chemische bestrijdingsmiddelen in de landbouw, met name zogeheten neonicotinoïden. Dit gif tast het zenuwstelsel en het navigatievermogen van bijen aan, waardoor ze de weg naar de korf niet meer terugvinden.",
    "Een tweede grote oorzaak is habitatverlies en voedselgebrek. Door monotone landbouwgronden ('groene woestijnen') en strak betegelde tuinen vinden bijen tussen mei en augustus nauwelijks nog bloeiende bloemen met nectar en stuifmeel.",
    "Tot slot worden honingbijen geteisterd door de varroamijt, een agressieve parasiet die virussen overbrengt en hele bijenvolken binnen één winter kan uitroeien.",
    "Gelukkig zijn er krachtige maatregelen voorhanden om het tij te keren. De Europese Unie heeft inmiddels de meest schadelijke neonicotinoïden verboden, wat de eerste voorzichtige hersteltekens oplevert.",
    "Daarnaast stimuleren overheden agrariërs om bloemrijke akkerranden in te zaaien en biologische landbouw te omarmen. Ook stadsbewoners kunnen een grote rol spelen door tegels uit de tuin te wippen en inheemse bloemen en bijenhotels te plaatsen.",
    "Kortom: de bijencrisis is een ernstige bedreiging voor onze voedselzekerheid, maar met een streng gifverbod en meer bloeiende biodiversiteit kunnen we het gezoem in onze boomgaarden behouden. Het redden van de bij begint op ons eigen bord en in onze eigen achtertuin."
]
card_bijen = maak_leestekst_card("Tekst B: Het verdwijnende gezoem: reddingsplan voor de bij", "Milieu & Voedselketen, 2024", bijen_alineas, "7 alinea's")

# Sınav 8 soruları
vragen_ex8 = [
    {
        "type": "mc",
        "figuur": card_trein,
        "vraag": "Welke vaste tekststructuur herken je in Tekst A (Twee eeuwen spoor: van stoom tot zweeftrein)?",
        "opties": [
            "Verleden-heden(-toekomst)structuur",
            "Voor- en nadelenstructuur",
            "Vraag-antwoordstructuur",
            "Probleem-oplossingsstructuur"
        ],
        "antwoord": 0,
        "uitleg": "De tekst volgt een strikt chronologische lijn van 1829 (verleden), via de 20e eeuw en nu (heden), naar Maglev en hyperloop (toekomst): verleden-heden-toekomststructuur."
    },
    {
        "type": "mc",
        "figuur": card_trein,
        "vraag": "Wat is het tekstdoel van Tekst A?",
        "opties": [
            "Overtuigen om een stoomtrein te kopen",
            "Informeren over de historische en technologische evolutie van de trein",
            "Amuseren met griezelige spoorwegongelukken",
            "Instrueren hoe je een wissel bedient"
        ],
        "antwoord": 1,
        "uitleg": "De auteur verschaft objectieve historische en technische feiten (tekstdoel informeren)."
    },
    {
        "type": "waaronwaar",
        "figuur": card_trein,
        "vraag": "Volgens alinea 1 van Tekst A waren dokters in 1829 razend enthousiast over de snelheid van 46 km/u en noemden ze het gezond voor de longen.",
        "antwoord": False,
        "uitleg": "Onwaar. In alinea 1 staat dat dokters juist ernstig waarschuwden dat zulke snelheden zouden leiden tot hersenschade en ademnood."
    },
    {
        "type": "open",
        "figuur": card_trein,
        "vraag": "In alinea 2 wordt een belangrijk maatschappelijk gevolg genoemd van de opkomst van het stoomspoor in de negentiende eeuw. Welk gevolg is dat?",
        "sleutelwoorden": ["tijdzone/tijd/dienstregeling", "industrie/industriële/revolutie/afstanden/verbinden"],
        "minTreffers": 1,
        "modelantwoord": "De industriële revolutie werd aangejaagd en landen kregen voor het eerst een gestandaardiseerde landelijke tijdzone voor de dienstregeling.",
        "uitleg": "Alinea 2 noemt de verbinding van industrieën en het ontstaan van een gestandaardiseerde landelijke tijdzone."
    },
    {
        "type": "invul",
        "figuur": card_trein,
        "vraag": "Met welk signaalwoord van tijd en tegenstelling opent alinea 4 de overgang naar de huidige situatie op het spoor?",
        "antwoord": "tegenwoordig",
        "uitleg": "Alinea 4 opent met het tijdsaanduidende woord 'Tegenwoordig'."
    },
    {
        "type": "mc",
        "figuur": card_bijen,
        "vraag": "Welke vaste tekststructuur herken je primair in Tekst B (Het verdwijnende gezoem)?",
        "opties": [
            "Aspectenstructuur",
            "Probleem-oplossingsstructuur",
            "Voor- en nadelenstructuur",
            "Verleden-heden-toekomststructuur"
        ],
        "antwoord": 1,
        "uitleg": "De tekst beschrijft een ernstig probleem (bijensterfte, al. 1), ontleedt de oorzaken (al. 2-4), draagt oplossingen aan (al. 5-6) en sluit af met een oproep: de probleem-oplossingsstructuur."
    },
    {
        "type": "mc",
        "figuur": card_bijen,
        "vraag": "Waarom is bijensterfte volgens alinea 1 van Tekst B een directe bedreiging voor de mens?",
        "opties": [
            "Omdat bijen giftige honing produceren als ze ziek zijn",
            "Omdat 70% van onze dagelijkse voedselgewassen voor bestuiving van bijen afhankelijk is",
            "Omdat bloemen zonder bijen geen zuurstof meer maken",
            "Omdat imkers de belangrijkste beroepsgroep van Europa vormen"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 1 vermeldt dat 70 procent van onze voedselgewassen (fruit, koffie, chocola) afhankelijk is van bestuiving door bijen."
    },
    {
        "type": "open",
        "figuur": card_bijen,
        "vraag": "In alinea 2 worden neonicotinoïden genoemd. Wat doen deze chemische stoffen met het lichaam van de bij?",
        "sleutelwoorden": ["zenuwstelsel", "navigatie/navigatievermogen/weg/terugvinden"],
        "minTreffers": 1,
        "modelantwoord": "Ze tasten het zenuwstelsel en het navigatievermogen aan, waardoor de bij de weg naar de korf niet meer terugvindt.",
        "uitleg": "Alinea 2 legt uit dat het gif het zenuwstelsel beschadigt waardoor bijen verdwalen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_bijen,
        "vraag": "Volgens alinea 3 van Tekst B zorgen strak betegelde tuinen en monotone akkerranden voor een overvloed aan voedsel voor bijen.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 3 noemt monotone akkers en betegelde tuinen 'groene woestijnen' waar nauwelijks voedsel te vinden is."
    },
    {
        "type": "open",
        "figuur": card_bijen,
        "vraag": "Bedenk een passend tussenkopje boven de alinea's 2, 3 en 4 van Tekst B.",
        "sleutelwoorden": ["oorzaken/cocktail/boosdoeners", "bedreigingen/gevaren/sterfte"],
        "minTreffers": 1,
        "modelantwoord": "De oorzaken van de bijensterfte / Een fatale cocktail / Waarom bijen sterven.",
        "uitleg": "Alinea 2 t/m 4 behandelen de drie hoofdoorzaken: pesticiden, voedselgebrek en de varroamijt."
    },
    {
        "type": "mc",
        "vraag": "Welke vaste tekststructuur herken je in een consumentenartikel waarin de positieve en negatieve kanten van het kopen van een elektrische auto worden afgewogen?",
        "opties": [
            "Voor- en nadelenstructuur",
            "Verklaringsstructuur",
            "Vraag-antwoordstructuur",
            "Aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Het tegen elkaar afzetten van plussen en minnen ter overweging is een voor- en nadelenstructuur."
    },
    {
        "type": "mc",
        "vraag": "Welk tekstverband wordt aangeduid door signaalwoorden als 'omdat', 'want', 'immers' en 'aangezien'?",
        "opties": [
            "Tijdvolgorde",
            "Tegenstelling",
            "Reden / argument",
            "Voorwaarde"
        ],
        "antwoord": 2,
        "uitleg": "Deze signaalwoorden luiden een reden, verklaring of argument in."
    },
    {
        "type": "waaronwaar",
        "vraag": "In een tekst met een aspectenstructuur behandelt de schrijver in het middenstuk verschillende deelaspecten of invalshoeken van een onderwerp.",
        "antwoord": True,
        "uitleg": "Waar. De kern van een aspectenstructuur is het belichten van verschillende facetten."
    },
    {
        "type": "invul",
        "figuur": card_trein,
        "vraag": "Met welk signaalwoord opent alinea 7 van Tekst A de afrondende beschouwing?",
        "antwoord": "samenvattend",
        "uitleg": "Alinea 7 begint met 'Samenvattend'."
    },
    {
        "type": "mc",
        "figuur": card_bijen,
        "vraag": "Welke alinea van Tekst B bespreekt de maatregelen die overheden en burgers nemen om de bij te redden?",
        "opties": [
            "Alinea 2",
            "Alinea 5 en 6",
            "Alinea 3",
            "Alinea 1"
        ],
        "antwoord": 1,
        "uitleg": "Alinea 5 (gifverbod) en alinea 6 (bloemrijke akkerranden en tuinen) behandelen de oplossingen."
    },
    {
        "type": "open",
        "figuur": card_bijen,
        "vraag": "Vul het schema van oorzaak en gevolg aan op basis van alinea 2 en 5 van Tekst B: (1) Neonicotinoïden tasten navigatievermogen aan -> (2) Europese Unie verbiedt schadelijke middelen -> (3) ...",
        "sleutelwoorden": ["herstel/eerste/tekens/beter", "bijen/populatie/overleven"],
        "minTreffers": 1,
        "modelantwoord": "De eerste voorzichtige tekenen van herstel worden zichtbaar bij bijenpopulaties.",
        "uitleg": "Alinea 5 toont aan dat het verbod leidt tot de eerste hoopvolle hersteltekens."
    },
    {
        "type": "waaronwaar",
        "vraag": "Een tekst waarin een vraag in de inleiding wordt gesteld en in het middenstuk verschillende mogelijke antwoorden worden onderzocht, noemen we een vraag-antwoordstructuur.",
        "antwoord": True,
        "uitleg": "Waar. Dit is de exacte definitie van een vraag-antwoordstructuur."
    },
    {
        "type": "mc",
        "figuur": card_trein,
        "vraag": "Welke uitspraak verwoordt het beste de hoofdgedachte van Tekst A (Twee eeuwen spoor)?",
        "opties": [
            "George Stephenson was de enige uitvinder die stoomlocomotieven kon bouwen.",
            "De trein heeft zich in twee eeuwen ontwikkeld van stoommachine tot zweeftrein en is hét duurzame vervoermiddel van de toekomst.",
            "Vliegtuigen zijn sneller en zuiniger dan de hyperloop.",
            "Magneetzweeftreinen kunnen alleen in Japan en China functioneren."
        ],
        "antwoord": 1,
        "uitleg": "De tekst toont de evolutie van de trein en concludeert dat deze meer dan ooit het vervoermiddel van de toekomst is."
    },
    {
        "type": "mc",
        "figuur": card_bijen,
        "vraag": "Welke zin geeft het meest accuraat de hoofdgedachte van Tekst B (Het verdwijnende gezoem) weer?",
        "opties": [
            "Bijensterfte bedreigt onze voedselvoorziening, maar kan gekeerd worden door een gifverbod en herstel van bloemrijke biodiversiteit.",
            "De varroamijt is niet schadelijk voor bijen als er genoeg appelbomen bloeien.",
            "Het eten van biologische aardbeien is de enige manier om insecten te beschermen.",
            "Neonicotinoïden zijn onmisbaar om landbouwgewassen te laten groeien."
        ],
        "antwoord": 0,
        "uitleg": "De hoofdgedachte brengt het gevaar voor de voedselketen samen met de noodzaak tot gifverbod en bloemrijke akkerranden."
    },
    {
        "type": "waaronwaar",
        "figuur": card_trein,
        "vraag": "In alinea 5 van Tekst A wordt de Maglev beschreven als een trein die juist extreem veel wrijving met de rails nodig heeft om te kunnen remmen.",
        "antwoord": False,
        "uitleg": "Onwaar. Alinea 5 legt uit dat de Maglev zweeft boven de baan en 'zonder wrijvingsweerstand van rails' snelheden tot 600 km/u haalt."
    }
]

ex8_data = {
    "id": "ex-h3-nederlands-8",
    "hoofdstuk": 1,
    "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
    "paragraaf": "5",
    "titel": "Toets 8 — §5 Vaste Tekststructuren (Toets C — Signaalwoorden & Oorzaak-Gevolg)",
    "vak": "Nederlands · HAVO 3 (Cursus 1)",
    "icoon": "🏗️",
    "duurMin": 25,
    "vragen": vragen_ex8
}

alle_extra = [
    ("examen_5.js", ex5_data),
    ("examen_6.js", ex6_data),
    ("examen_7.js", ex7_data),
    ("examen_8.js", ex8_data),
]

for bestandsnaam, data in alle_extra:
    balance_mc(data['vragen'])
    pad = os.path.join(out_dir, bestandsnaam)
    js_content = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 1) */\n"
    js_content += "DURU.registerExamen(" + json.dumps(data, indent=2, ensure_ascii=False) + ");\n"
    with open(pad, "w", encoding="utf-8") as f:
        f.write(js_content)
    print(f"Aangemaakt: {bestandsnaam} met {len(data['vragen'])} vragen.")

print("\nAlle 4 de extra examens (Toets 5 t/m 8) succesvol aangemaakt!")
