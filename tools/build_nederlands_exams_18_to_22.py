# -*- coding: utf-8 -*-
"""
Generator voor 5 EXTRA HAVO 3 Nederlands leestoetsen (Toets 18 t/m 22):
- Toets 18: §2 Inleiding en Slot (Toets H — Natuurherstel & Biologische Ritmes)
- Toets 19: §5 Vaste Tekststructuren (Toets H — Probleem-Oplossing & Verschijnsel-Verklaring)
- Toets 20: §2 Inleiding en Slot (Toets I — Anekdotes, Cirkelstructuren & Reviewfraude)
- Toets 21: §5 Vaste Tekststructuren (Toets I — Voor- en Nadelen & Verleden-Heden-Toekomst)
- Toets 22: Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining B)
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
# TOETS 18: §2 INLEIDING EN SLOT (TOETS H)
# Tekst A: De otter in Nederland (Historisch feit, probleemstelling, slotoproep)
# Tekst B: Tienerbrein en vroege schooltijden (Herkenbare situatie, stelling, uitsmijter)
# ==============================================================================
otter_alineas = [
    "In de kille herfst van 1988 werd bij een provinciale weg in Friesland een aangereden dier gevonden. Het bleek de allerlaatste wilde otter van Nederland te zijn. Met die tragische autobotsing werd een icoon van onze waterrijke natuur officieel uitgestorven verklaard. Maar wie vandaag de dag door het Nationaal Park Weerribben-Wieden vaart, kan met een beetje geluk zomaar weer een glanzende snuit boven het riet zien uitsteken. De otter is terug, maar hoe bestendig is dit ecologische sprookje in een van de dichtstbevolkte landen ter wereld?",
    "De verdwijning van de otter in de twintigste eeuw was geen toeval. Zware industriële vervuiling met pcb's en zware metalen vergiftigde het oppervlaktewater, waardoor de visetende watermarter onvruchtbaar werd. Bovendien versnipperde de aanleg van snelwegen en kanalen het leefgebied van het dier volkomen.",
    "Rond het millennium keerden de kansen. Dankzij strengere Europese milieuregels werd het Nederlandse rivier- en polderwater schoner dan in honderd jaar het geval was geweest. In 2002 startte een ambitieus herintroductieprogramma met tientallen dieren uit Oost-Europa.",
    "Toch dreigt het succesverhaal vroegtijdig te stranden. Het grootste knelpunt blijft het drukke verkeer: jaarlijks sneuvelt ruim een derde van de totale otterpopulatie onder de wielen van auto's. Daarnaast raken otters nog altijd verstrikt in illegale fuiken van palingvissers.",
    "Natuurorganisaties en provincies investeren daarom miljoenen in zogeheten 'droge faunatunnels' onder gevaarlijke provinciale wegen en plaatsen speciale rasters langs waterwegen. Ook moeten visfuiken verplicht worden uitgerust met stopgazen waardoor otters niet kunnen binnenzwemmen.",
    "Samenvattend mogen we trots zijn op de spectaculaire wederopstanding van de otter in onze wateren. Maar een veilige toekomst is pas gewaarborgd als we de resterende knelpunten daadkrachtig aanpakken. Provincies en wegbeheerders moeten haast maken met de aanleg van faunatunnels bij risicovolle oversteekplaatsen. Alleen als we de otter letterlijk de ruimte geven om veilig te zwemmen en trekken, blijft dit prachtige roofdier behouden als de ware kroon op onze waternatuur."
]
card_otter = maak_leestekst_card("Tekst A: De triomfantelijke terugkeer van de otter", "Natuurbehoud & Landschap, 2025", otter_alineas, "6 alinea's")

tiener_alineas = [
    "Om kwart voor zeven 's ochtends schettert de wekker genadeloos door de slaapkamer. Met dichtgeknepen ogen, loodzware ledematen en een zucht strompelt de vijftienjarige Lucas naar de badkamer. Tegen de tijd dat hij om half negen in het scheikundelokaal zit, functioneert zijn brein nog altijd in een soort schemerstand. Vrijwel iedere middelbare scholier herkent deze dagelijkse martelgang. Maar is die ochtendvermoeidheid slechts het gevolg van luiheid en te lang gamen, of dwingt ons schoolsysteem jongeren in een biologisch onnatuurlijk keurslijf?",
    "Lange tijd werd laat opblijven door ouders en docenten afgedaan als gebrek aan discipline. 'Ga gewoon om tien uur naar bed en leg die smartphone weg', klinkt steevast het traditionele advies. Neurowetenschappelijk onderzoek veegt deze vooroordelen echter resoluut van tafel.",
    "Tijdens de puberteit ondergaat de biologische klok in de hersenen namelijk een dramatische verschuiving. De aanmaak van melatonine — het hormoon dat slaperig maakt — begint bij adolescenten gemiddeld pas twee uur later dan bij volwassenen of basisschoolkinderen. Een puber dwingen om om half elf te slapen, is biologisch vergelijkbaar met een volwassene vragen om om acht uur 's avonds in diepe slaap te vallen.",
    "Het resultaat van te vroege schooltijden is een chronisch slaaptekort bij jongeren, met desastreuze gevolgen voor schoolprestaties, concentratievermogen en mentale gezondheid. Experimenten in het buitenland tonen aan dat het verschuiven van het eerste lesuur naar negen uur direct leidt tot hogere cijfers en aanzienlijk minder spijbelgedrag.",
    "Critici werpen tegen dat een latere schooldag botst met het werkschema van ouders en de trainingstijden van sportverenigingen.",
    "Al met al is het krampachtig vasthouden aan half negen als starttijd achterhaald en wetenschappelijk onverantwoord. Een moderne school moet het welzijn en leerrendement van leerlingen centraal stellen in plaats van starre roosters. Laat tieners 's ochtends wat langer slapen en begin de lessen pas om negen uur; dat levert uitgeruste scholieren op die met een helder hoofd de toekomst tegemoet gaan."
]
card_tiener = maak_leestekst_card("Tekst B: Waarom tieners later moeten beginnen", "Brein, Onderwijs & Samenleving, 2025", tiener_alineas, "6 alinea's")

vragen_ex18 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Welke beproefde techniek gebruikt de auteur in de inleiding van Tekst A om de aandacht van de lezer vast te houden?",
        "opties": [
            "Een dramatisch historisch feit contrasteren met een hoopvolle actuele situatie",
            "Het integraal afdrukken van een ingewikkelde wetstekst over visserij",
            "Een reeks interviews met bezorgde Friese automobilisten weergeven",
            "Een sprookje van de gebroeders Grimm citeren"
        ],
        "antwoord": 0,
        "uitleg": "De auteur opent met het tragische uitsterven van de laatste otter in 1988 en stelt daar de recente terugkeer in de Weerribben tegenover."
    },
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Op welke wijze bakent de schrijver het centrale thema af aan het slot van alinea 1 van Tekst A?",
        "opties": [
            "Door een centrale vraag te stellen over de bestendigheid van de otterpopulatie",
            "Door direct een verbod op alle scheepvaart in Friesland te eisen",
            "Door een ranglijst van de snelste zwemdieren ter wereld te presenteren",
            "Door de lezer te verzoeken om financieel donateur te worden"
        ],
        "antwoord": 0,
        "uitleg": "De vraag aan het einde van alinea 1 formuleert de centrale probleemstelling van het artikel."
    },
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Welke twee historische oorzaken voor het eerdere uitsterven worden in alinea 2 van Tekst A aangewezen?",
        "opties": [
            "Ernstige industriële watervervuiling en versnippering van het leefgebied",
            "Extreem koude winters en een tekort aan zoetwatermosselen",
            "Overmatige jacht op otters voor de bontindustrie in de middeleeuwen",
            "Concurrentie met agressieve bevers uit Noord-Amerika"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 noemt industriële pcb-vervuiling en habitatversnippering door snelwegen en kanalen als hoofdoorzaken."
    },
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Wat is volgens alinea 4 momenteel de dodelijkste bedreiging voor de teruggekeerde otter?",
        "opties": [
            "Het drukke wegverkeer waarbij otters worden doodgereden",
            "Het ontbreken van voldoende prooivissen in de meren",
            "Een dodelijk virus dat uitsluitend waterroofdieren treft",
            "Aanvallen door loslopende jachthonden in het riet"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 benadrukt dat jaarlijks ruim een derde van de populatie sneuvelt onder autowielen."
    },
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Wat is het voornaamste doel van de slotalinea (alinea 6) in Tekst A?",
        "opties": [
            "Een samenvattende conclusie trekken en een duidelijke oproep aan overheden doen",
            "Het bekritiseren van het werk van Oost-Europese biologen",
            "Uitleggen hoe een otterhol onder de grond precies is gebouwd",
            "Aankondigen dat de auteur een eigen natuurfilm gaat regisseren"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 vat samen en doet een dringende oproep aan provincies en wegbeheerders om faunatunnels aan te leggen."
    },
    {
        "type": "mc",
        "figuur": card_otter,
        "vraag": "Welke beeldende metafoor gebruikt de auteur in de laatste zin van Tekst A?",
        "opties": [
            "De otter bestempelen als de 'ware kroon op onze waternatuur'",
            "De otter vergelijken met een onderzeeboot uit de Tweede Wereldoorlog",
            "Het Nederlandse polderlandschap omschrijven als een grote badkuip",
            "Automobilisten aanduiden als meedogenloze ridders"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin noemt de otter de 'ware kroon op onze waternatuur' als fraaie uitsmijter."
    },
    {
        "type": "waaronwaar",
        "figuur": card_otter,
        "vraag": "Volgens alinea 3 is het Nederlandse rivierwater tegenwoordig nog even zwaar vervuild met pcb's als in de twintigste eeuw.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt juist dat het water dankzij Europese regels schoner is dan in honderd jaar."
    },
    {
        "type": "waaronwaar",
        "figuur": card_otter,
        "vraag": "Volgens alinea 5 kunnen stopgazen in visfuiken voorkomen dat otters per ongeluk verdrinken.",
        "antwoord": True,
        "uitleg": "Waar. Stopgazen zorgen ervoor dat otters niet kunnen binnenzwemmen en verdrinken."
    },
    {
        "type": "open",
        "figuur": card_otter,
        "vraag": "Welke twee specifieke beschermingsmaatregelen worden in alinea 5 genoemd om de otter te behoeden voor verkeer en fuiken?",
        "sleutelwoorden": [
            "faunatunnels/droge faunatunnels/rasters",
            "stopgazen/fuiken aanpassen/visfuiken"
        ],
        "minTreffers": 1,
        "modelantwoord": "De aanleg van faunatunnels onder wegen en het verplicht plaatsen van stopgazen in visfuiken.",
        "uitleg": "In alinea 5 worden droge faunatunnels en verplichte stopgazen in fuiken genoemd."
    },
    {
        "type": "invul",
        "figuur": card_otter,
        "vraag": "Met welk signaalwoord van samenvatting luidt de auteur alinea 6 in Tekst A in?",
        "antwoord": "Samenvattend|samenvattend",
        "uitleg": "'Samenvattend' kondigt aan dat de hoofdlijnen van de tekst worden samengevat."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Welke herkenbare situatie kiest de auteur in de inleiding van Tekst B om de lezer aan te spreken?",
        "opties": [
            "De moeizame en slaperige ochtendroutine van een scholier met een vroege wekker",
            "Het vieren van een geslaagd eindexamenfeest tot diep in de nacht",
            "Het kopen van een nieuwe rugzak in een drukke winkelstraat",
            "Een chaotische gymles in de vrieskou op een sportveld"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 schetst het herkenbare beeld van scholier Lucas die om 06:45 moeizaam ontwaakt en naar school strompelt."
    },
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Welke traditionele misvatting over pubers wordt in alinea 2 bekritiseerd?",
        "opties": [
            "Dat ochtendmoeheid uitsluitend te wijten is aan luiheid en een gebrek aan discipline",
            "Dat pubers gemiddeld intelligenter zijn dan hun docenten",
            "Dat jongeren 's ochtends meer trek hebben in een stevig ontbijt",
            "Dat smartphones de concentratie van pubers juist enorm verbeteren"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 stelt dat ochtendmoeheid ten onrechte werd afgedaan als luiheid en gebrek aan discipline."
    },
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Welke biologische verklaring geeft alinea 3 voor het late slaapritme van pubers?",
        "opties": [
            "De melatonine-aanmaak begint bij adolescenten gemiddeld twee uur later",
            "Pubers hebben een veel lagere lichaamstemperatuur dan volwassenen",
            "De oogzenuwen van jongeren vangen minder zuurstof op in het donker",
            "De maag van een puber verteert voedsel uitsluitend tijdens de vroege ochtend"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat de biologische klok verschuift en het slaaphormoon melatonine pas twee uur later wordt geproduceerd."
    },
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Welk praktisch tegenargument van critici wordt kort aangestipt in alinea 5?",
        "opties": [
            "Latere schooltijden botsen met ouderlijke werkschema's en sporttrainingen",
            "Het elektriciteitsverbruik op scholen zou daardoor verdubbelen",
            "Docenten weigeren les te geven na twaalf uur 's middags",
            "Bussen en treinen rijden helemaal niet na half negen 's ochtends"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 noemt het praktische bezwaar dat latere tijden botsen met werktijden van ouders en sportclubs."
    },
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Welke concrete aanbeveling formuleert de auteur in de slotparagraaf van Tekst B?",
        "opties": [
            "Scholen moeten de lessen voortaan pas om negen uur laten beginnen",
            "Scholieren moeten verplicht om negen uur 's avonds hun kamerdeur op slot doen",
            "De overheid moet alle toetsen en proefwerken definitief afschaffen",
            "Alle lessen moeten worden omgezet in online onderwijs vanuit huis"
        ],
        "antwoord": 0,
        "uitleg": "De auteur adviseert schoolbesturen om de lessen pas om negen uur te laten beginnen."
    },
    {
        "type": "mc",
        "figuur": card_tiener,
        "vraag": "Wat typeert de toonzetting en strekking van de uitsmijter van Tekst B?",
        "opties": [
            "Een bemoedigende en optimistische aansporing gericht op leerwinst en welzijn",
            "Een cynische waarschuwing dat het onderwijs ten dode is opgeschreven",
            "Een formele dreiging met juridische stappen tegen schoolleiders",
            "Een vragende zin waarin de auteur bekent zelf altijd te verslapen"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin sluit optimistisch af met 'uitgeruste scholieren die met een helder hoofd de toekomst tegemoet gaan'."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tiener,
        "vraag": "Volgens alinea 4 toonden buitenlandse experimenten met latere schooltijden juist een flinke toename van het spijbelgedrag aan.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst meldt juist dat een start om negen uur leidde tot hogere cijfers en aanzienlijk minder spijbelen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tiener,
        "vraag": "Volgens alinea 3 is een puber om half elf laten slapen vergelijkbaar met een volwassene die om acht uur moet slapen.",
        "antwoord": True,
        "uitleg": "Waar. Deze expliciete biologische vergelijking wordt in alinea 3 gemaakt om het verschil duidelijk te maken."
    },
    {
        "type": "open",
        "figuur": card_tiener,
        "vraag": "Welke twee positieve effecten van een start om negen uur worden in alinea 4 genoemd op basis van buitenlandse experimenten?",
        "sleutelwoorden": [
            "hogere cijfers/betere cijfers/schoolprestaties",
            "minder spijbelgedrag/minder spijbelen/verzuim"
        ],
        "minTreffers": 1,
        "modelantwoord": "Hogere cijfers en aanzienlijk minder spijbelgedrag bij leerlingen.",
        "uitleg": "Alinea 4 vermeldt dat de verschuiving naar negen uur direct leidde tot hogere cijfers en minder spijbelgedrag."
    },
    {
        "type": "invul",
        "figuur": card_tiener,
        "vraag": "Met welke vaste woordgroep van conclusie opent alinea 6 in Tekst B?",
        "antwoord": "Al met al|al met al",
        "uitleg": "'Al met al' is de vaste signaalwoordgroep die de conclusie inluidt."
    }
]

# ==============================================================================
# TOETS 19: §5 VASTE TEKSTSTRUCTUREN (TOETS H)
# Tekst A: Stadsverhitting en hitte-eiland (Probleem-oplossingstructuur)
# Tekst B: Communicerende bomen en Wood Wide Web (Vraag-antwoord / Verschijnsel-verklaring)
# ==============================================================================
hitte_alineas = [
    "Op hete zomerdagen verandert de binnenstad van Utrecht of Amsterdam in een gigantische bakoven. Terwijl het in omliggende weilanden en bossen 's avonds heerlijk afkoelt naar een aangename twintig graden, blijft het kwik tussen de stenen grachtenpanden en winkelstraten vaak steken boven de dertig graden. Dit zogeheten 'hitte-eilandeffect' zorgt voor slapeloze nachten, benauwdheid en gezondheidsproblemen bij kwetsbare stedelingen. Hoe kunnen stadsbesturen onze oververhitte steden weer leefbaar en koel maken?",
    "De kernoorzaak van dit fenomeen is de massale verstening van de openbare ruimte. Donker asfalt, betonnen stoeptegels en bakstenen muren absorberen overdag grote hoeveelheden zonnestraling en geven die hitte pas diep in de nacht langzaam weer af. Bovendien ontbreekt het aan verkoelende bomen en waterpartijen, terwijl airconditioners warme lucht naar buiten blazen en de temperatuur extra opstuwen.",
    "Gelukkig bestaan er doeltreffende stedenbouwkundige oplossingen om dit hitteprobleem te lijf te gaan. Een eerste cruciale maatregel is 'ontstenen en vergroenen': het vervangen van overbodige parkeervakken en betegelde pleinen door gras, struiken en schaduwrijke bomen. Bomen werken immers als natuurlijke airco's doordat ze water verdampen via hun bladeren en zo de luchttemperatuur met meerdere graden verlagen.",
    "Daarnaast stimuleren gemeenten de aanleg van groene daken en verticale geveltuinen. Sedumplantjes op daken isoleren gebouwen tegen de hitte en houden regenwater vast, waardoor minder hittestress ontstaat.",
    "Tot slot kan het gebruik van lichte, zonreflecterende bouwmaterialen op daken en wegen voorkomen dat zonnewarmte überhaupt wordt opgeslagen.",
    "Kortom: stadsverhitting is een ernstig maar beheersbaar probleem. Door asfalt resoluut in te ruilen voor groen, daken te beplanten en water de ruimte te geven, transformeren we onze betonnen hitte-eilanden in gezonde, koele oases. De hittegolf van morgen vraagt om de vergroening van vandaag."
]
card_hitte = maak_leestekst_card("Tekst A: De stad als bakoven: strijd tegen het hitte-eiland", "Stad & Milieu, 2025", hitte_alineas, "6 alinea's")

bosnet_alineas = [
    "Wie door een eeuwenoud beukenbos wandelt, ziet ogenschijnlijk louter individuele bomen die strijden om het felbegeerde zonlicht. Maar schijn bedriegt. Onder onze voetzolen bevindt zich een geheimzinnig, kilometerslang netwerk van microscopisch dunne schimmeldraden dat alle bomen met elkaar verbindt. Wetenschappers noemen dit ondergrondse vlechtwerk gekscherend het 'Wood Wide Web'. Hoe slagen bomen erin om via dit netwerk met elkaar te communiceren en zelfs voedsel uit te wisselen?",
    "Decennialang zagen biologen het bos als een keihard slagveld waar bomen elkaar genadeloos beconcurreerden. Recent baanbrekend onderzoek heeft echter aangetoond dat een bos veel meer functioneert als één gigantisch, solidair superorganisme.",
    "De sleutel tot deze samenwerking ligt in de zogeheten mycorrhiza: een hechte symbiose tussen boomwortels en bodemschimmels. Bomen leveren via fotosynthese suikers aan de schimmels, terwijl de schimmels in ruil daarvoor water en schaarse mineralen zoals stikstof en fosfor aan de boomwortels overdragen.",
    "Nog fascinerender is dat bomen via deze schimmeldraden chemische waarschuwingssignalen naar elkaar versturen. Zodra een beuk wordt aangevallen door vraatzuchtige rupsen, stuurt de boom via het schimmelnetwerk een alarmsignaal naar zijn buren. Die buren beginnen direct bitterstoffen in hun bladeren aan te maken, nog vóór de rupsen hen hebben bereikt.",
    "Bovendien blijkt dat grote, oude 'moederbomen' via het netwerk extra suikers sturen naar jonge zaailingen die in de diepe schaduw staan en zelf onvoldoende zonlicht kunnen opvangen.",
    "Samenvattend toont het Wood Wide Web aan dat bomen geen eenzame strijders zijn, maar meesters in onderlinge samenwerking. Door voedsel te delen en elkaar tijdig te waarschuwen, houden zij het gehele bosecosysteem gezond en weerbaar. Voor de mensheid bevat dit verborgen wonder een waardevolle les: echte overlevingskracht schuilt niet in meedogenloze concurrentie, maar in verbondenheid."
]
card_bosnet = maak_leestekst_card("Tekst B: Het geheime internet van het woud", "Wetenschap & Bosbouw, 2025", bosnet_alineas, "6 alinea's")

vragen_ex19 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Welk model van de vaste tekststructuren vormt het fundament van Tekst A?",
        "opties": [
            "De probleem-oplossingstructuur",
            "De chronologische verleden-hedenstructuur",
            "De bewering-argumentatiestructuur",
            "De loutere aspectenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst A schetst eerst het probleem van stadsverhitting en presenteert vervolgens concrete oplossingen (vergroenen, groene daken, reflecterende materialen)."
    },
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Welk specifiek onderdeel van het probleem wordt geanalyseerd in alinea 2 van Tekst A?",
        "opties": [
            "De fysische oorzaken van de hitteophoping in de bebouwde omgeving",
            "De precieze verkoopprijzen van mobiele airconditioners",
            "De klachten van toeristen die musea bezoeken",
            "De werking van zonnepanelen op het platteland"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 verklaart de oorzaken: donkere materialen die warmte absorberen, gebrek aan groen en warme lucht van airco's."
    },
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Waarom fungeren bomen volgens alinea 3 als 'natuurlijke airco's' in een stad?",
        "opties": [
            "Doordat zij water verdampen via hun bladeren en schaduw werpen",
            "Omdat bomen koude wind aantrekken vanuit de Noordzee",
            "Doordat hun wortels ijs vasthouden in de diepe bodem",
            "Doordat zij alle koolstofdioxide in één seconde vernietigen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat bomen schaduw geven en water verdampen, wat de luchttemperatuur daadwerkelijk verlaagt."
    },
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Welke signaalwoorden in alinea 3, 4 en 5 structureren de opsomming van oplossingen?",
        "opties": [
            "Een eerste cruciale maatregel, daarnaast, tot slot",
            "Omdat, dientengevolge, dientengevolge",
            "Hoewel, daarentegen, desalniettemin",
            "Vroeger, tegenwoordig, in de toekomst"
        ],
        "antwoord": 0,
        "uitleg": "'Een eerste cruciale maatregel' (3), 'Daarnaast' (4) en 'Tot slot' (5) ordenen de aangedragen oplossingen."
    },
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Welke rol vervullen sedumplantjes op groene daken volgens alinea 4?",
        "opties": [
            "Zij isoleren gebouwen tegen hitte en houden regenwater vast",
            "Zij produceren eetbare vruchten voor stadsbewoners",
            "Zij vervangen de behoefte aan centrale verwarming in de winter",
            "Zij weren gevaarlijke roofvogels van de daken"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 stelt dat sedumplantjes gebouwen isoleren tegen zonnewarmte en water bufferen."
    },
    {
        "type": "mc",
        "figuur": card_hitte,
        "vraag": "Wat is de kernboodschap van de uitsmijter in alinea 6 van Tekst A?",
        "opties": [
            "Direct in actie komen met vergroening om toekomstige hittecrises te voorkomen",
            "Wachten tot de overheid alle airconditioners gratis vervangt",
            "Verhuizen naar het platteland is de enige remedie tegen warmte",
            "Steden moeten 's zomers volledig worden geëvacueerd"
        ],
        "antwoord": 0,
        "uitleg": "'De hittegolf van morgen vraagt om de vergroening van vandaag' spoort aan tot onmiddellijke actie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_hitte,
        "vraag": "Volgens alinea 1 koelt het 's zomers in stadscentra even snel af naar twintig graden als in weilanden.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst meldt juist dat het kwik in steden vaak boven de dertig graden blijft steken door het hitte-eilandeffect."
    },
    {
        "type": "waaronwaar",
        "figuur": card_hitte,
        "vraag": "Volgens alinea 5 kunnen lichte, reflecterende bouwmaterialen voorkomen dat zonnewarmte wordt opgeslagen.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt in alinea 5 letterlijk als innovatieve oplossing aangedragen."
    },
    {
        "type": "open",
        "figuur": card_hitte,
        "vraag": "Welke twee specifieke oplossingen worden in alinea 3 en 4 genoemd om stenen oppervlakken te vergroenen?",
        "sleutelwoorden": [
            "ontstenen/tegels wippen/gras en struiken/bomen",
            "groene daken/geveltuinen/sedumplantjes"
        ],
        "minTreffers": 1,
        "modelantwoord": "Het ontstenen van pleinen voor bomen en struiken en de aanleg van groene daken of geveltuinen.",
        "uitleg": "In alinea 3 en 4 worden het ontstenen voor groen/bomen en de aanleg van groene daken en geveltuinen genoemd."
    },
    {
        "type": "invul",
        "figuur": card_hitte,
        "vraag": "Met welk signaalwoord van samenvatting opent de slotalinea van Tekst A?",
        "antwoord": "Kortom|kortom",
        "uitleg": "'Kortom' luidt de samenvattende conclusie van alinea 6 in."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Welke vaste tekststructuur is leidend in Tekst B?",
        "opties": [
            "De vraag-antwoordstructuur (of verschijnsel-verklaring)",
            "De voor- en nadelenstructuur",
            "De historische verleden-hedenstructuur",
            "De probleem-oplossingstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B introduceert een verwonderlijk natuurverschijnsel (Wood Wide Web) met een centrale vraag en geeft in het middenstuk wetenschappelijke antwoorden."
    },
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Welke traditionele opvatting over het bos werd door recent onderzoek ontkracht (alinea 2)?",
        "opties": [
            "Dat bomen uitsluitend elkaars meedogenloze concurrenten zijn",
            "Dat bomen helemaal geen water nodig hebben om te groeien",
            "Dat schimmels altijd dodelijke ziektes veroorzaken bij bomen",
            "Dat beukenbomen veel ouder worden dan eikenbomen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 legt uit dat biologen het bos vroeger zagen als een slagveld van concurrentie, terwijl het juist een solidair netwerk blijkt."
    },
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Hoe werkt de wederzijdse ruilhandel bij de mycorrhiza-symbiose volgens alinea 3?",
        "opties": [
            "Bomen geven suikers en ontvangen water en mineralen van schimmels",
            "Schimmels eten de boombladeren op en geven zuurstof terug",
            "Bomen pompen gifstoffen in de bodem om schimmels te voeden",
            "Schimmels vangen zonlicht op en sturen dit door naar de wortels"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 beschrijft dat bomen suikers leveren via fotosynthese en schimmels water, stikstof en fosfor terugleveren."
    },
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Wat doen bomen volgens alinea 4 zodra ze via het schimmelnetwerk een rupsenalarm ontvangen?",
        "opties": [
            "Zij maken preventief bitterstoffen aan in hun eigen bladeren",
            "Zij laten onmiddellijk al hun takken op de grond vallen",
            "Zij trekken hun wortels dieper terug in de aarde",
            "Zij sluiten hun houtvaten voor de rest van het jaar af"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 beschrijft dat buurbomen preventief bitterstoffen aanmaken om rupsenvraat af te weren."
    },
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Welke bijzondere zorgtaak vervullen oude 'moederbomen' volgens alinea 5?",
        "opties": [
            "Zij sturen extra suikers naar jonge zaailingen in de schaduw",
            "Zij verjagen vogels die de zaden van jonge boompjes opeten",
            "Zij vallen expres om om plaats te maken voor paddenstoelen",
            "Zij filteren al het grondwater voor het hele bosgebied"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 vermeldt dat moederbomen suikers via het schimmelnetwerk transporteren naar zaailingen met te weinig zonlicht."
    },
    {
        "type": "mc",
        "figuur": card_bosnet,
        "vraag": "Welke levensles ontleent de auteur in alinea 6 aan het functioneren van het bosecosysteem?",
        "opties": [
            "Echte overlevingskracht schuilt in verbondenheid en samenwerking",
            "Mensen moeten ophouden met het stoken van houtkachels",
            "Paddenstoelen zijn gevaarlijke organismen die bestreden moeten worden",
            "Concurrentie is de enige wet die geldt in het dierenrijk"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 besluit met de les dat overleving niet draait om meedogenloze concurrentie, maar om onderlinge verbondenheid."
    },
    {
        "type": "waaronwaar",
        "figuur": card_bosnet,
        "vraag": "Volgens alinea 1 vechten bomen uitsluitend met elkaar en is er ondergronds geen enkel contact tussen boomwortels.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst onthult juist dat bomen via een enorm schimmelnetwerk (het Wood Wide Web) intensief verbonden zijn."
    },
    {
        "type": "waaronwaar",
        "figuur": card_bosnet,
        "vraag": "Volgens alinea 3 leveren bodemschimmels schaarse mineralen zoals stikstof en fosfor aan de boom.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt letterlijk genoemd als de tegenprestatie van de schimmels in de symbiose."
    },
    {
        "type": "open",
        "figuur": card_bosnet,
        "vraag": "Welke twee specifieke stoffen dragen bodemschimmels volgens alinea 3 over aan bomen via hun wortels?",
        "sleutelwoorden": [
            "water/vocht",
            "stikstof/fosfor/mineralen"
        ],
        "minTreffers": 1,
        "modelantwoord": "Water en mineralen zoals stikstof of fosfor.",
        "uitleg": "Alinea 3 vermeldt expliciet water en schaarse mineralen zoals stikstof en fosfor."
    },
    {
        "type": "invul",
        "figuur": card_bosnet,
        "vraag": "Met welk signaalwoord van samenvatting begint alinea 6 in Tekst B?",
        "antwoord": "Samenvattend|samenvattend",
        "uitleg": "'Samenvattend' kondigt aan dat de auteur de conclusies en lessen bijeenbrengt."
    }
]

# ==============================================================================
# TOETS 20: §2 INLEIDING EN SLOT (TOETS I)
# Tekst A: Het koraal van Bonaire (Zintuiglijke opening, contrast, cirkelstructuur)
# Tekst B: Fake reviews en online consumentenbedrog (Anekdote, vraagstelling, advies)
# ==============================================================================
koraal_alineas = [
    "Wie met een duikbril in het turquoise water rond het Caribische eiland Bonaire glijdt, waant zich in een betoverend onderwaterparadijs. Scholen felgekleurde papegaaivissen zwemmen sierlijk tussen wuivende gorgonen en reusachtige hersenkoralen. Maar wie beter kijkt, ziet ook een angstaanjagend schouwspel: spookachtige witte skeletten van afgestorven koraalriffen die roerloos op de zeebodem liggen. Kan dit kwetsbare kroonjuweel van het Nederlands mariene erfgoed nog gered worden, of zijn we getuige van de definitieve dood van onze tropische riffen?",
    "Koraalriffen worden niet voor niets de regenwouden van de oceaan genoemd. Hoewel ze minder dan één procent van de oceaanbodem beslaan, bieden ze onderdak aan ruim een kwart van al het zeeleven. Daarnaast vormen ze een onmisbare natuurlijke golfbreker die kusten beschermt tegen verwoestende orkanen.",
    "De sluipmoordenaar van het koraal is de opwarming van het zeewater. Wanneer de watertemperatuur wekenlang één graad boven het maximum stijgt, raken koraalpoliepen in paniek en stoten ze de microscopische algen uit die hen van voedsel en felle kleuren voorzien. Dit leidt tot het beruchte 'verbleken'; als het water niet snel afkoelt, sterft het koraal massaal af.",
    "Bovendien wordt het rif van Bonaire bedreigd door vervuiling vanaf het land. Ongezuiverd afvalwater en giftige chemicaliën in zonnebrandcrème — zoals oxybenzone — tasten het afweersysteem van jonge koraalstekjes aan.",
    "Marien biologen van de stichting Reef Renewal zetten zich echter onvermoeibaar in voor herstel. In speciale onderwaterkwekerijen telen zij resistente koraalsoorten die beter bestand zijn tegen warm water. Zodra de stekjes volgroeid zijn, worden ze met speciale onderwaterlijm handmatig op het beschadigde rif gezet.",
    "Al met al hangt het voortbestaan van de riffen van Bonaire aan een zijden draadje, maar is het tij nog te keren als we nu wereldwijd en lokaal ingrijpen. Toeristen moeten verplicht rifvriendelijke zonnebrand gebruiken en de eilandoverheid moet waterzuivering strenger handhaven. Laten we ervoor zorgen dat toekomstige duikers niet tussen bleke onderwatergraven moeten zwemmen, maar de adembenemende pracht van levend koraal kunnen blijven bewonderen."
]
card_koraal = maak_leestekst_card("Tekst A: De stille ramp onder de Caribische golven", "Oceanen & Natuurbehoud, 2025", koraal_alineas, "6 alinea's")

reviews_alineas = [
    "Je zoekt op internet naar een gezellig Italiaans restaurant in een onbekende stad. Het eerste zoekresultaat toont vijf glanzende sterren en honderden lyrische recensies: 'De lekkerste truffelpasta ooit!', juicht ene Sophie. Verlekkerd reserveer je een tafeltje, maar eenmaal ter plekke tref je een kille ruimte met lauwe magnetronpizza en een norse ober aan. Wat is hier gebeurd? Ben je zojuist in de geraffineerde fuik gezwommen van een zogeheten 'klikboerderij'? Hoe betrouwbaar zijn online sterren en beoordelingen anno 2025 eigenlijk nog?",
    "Online recensies bepalen tegenwoordig miljarden aan consumentenbestedingen. Uit cijfers van de Consumentenbond blijkt dat ruim tachtig procent van de Nederlanders reviews doorslaggevend vindt bij de aankoop van producten, het boeken van hotels of het kiezen van een specialist.",
    "Waar grote belangen spelen, ligt misbruik echter altijd op de loer. Er is een lucratieve wereldwijde schaduweconomie ontstaan waarin bedrijven tegen betaling massaal positieve nepbeoordelingen kopen. Zogeheten klikboerderijen in lagelonenlanden of geautomatiseerde AI-bots schrijven in opdracht duizenden vleiende teksten om de ranking van een restaurant of webwinkel kunstmatig omhoog te stuwen.",
    "Bovendien worden concurrerende bedrijven soms genadeloos zwartgemaakt met een hagelbui aan valse één-ster-recensies om hun reputatie te ruïneren.",
    "Grote techbedrijven proberen deze reviewfraude met algoritmes op te sporen, maar lopen voortdurend achter de feiten aan. Moderne AI-taalmodellen schrijven inmiddels zo overtuigend en gevarieerd dat software nepberichten nauwelijks nog kan onderscheiden van echte ervaringen.",
    "Concluderend moeten we vaststellen dat de tijd van blindelings vertrouwen op vijfsterrenscores definitief voorbij is. Consumenten doen er verstandig aan om recensies met een gezonde dosis wantrouwen te lezen: kijk naar de spreiding over langere tijd, negeer overdreven jubelverhalen en raadpleeg onafhankelijke tests. Pas wanneer we ons niet langer laten verblinden door gekochte sterren, prikken we door de digitale façade heen."
]
card_reviews = maak_leestekst_card("Tekst B: De illusie van vijf sterren: online reviewfraude", "Consument & Technologie, 2025", reviews_alineas, "6 alinea's")

vragen_ex20 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Welke stijlfiguur herken je in de openingsalinea van Tekst A om het onderwerp te introduceren?",
        "opties": [
            "Een scherp contrast tussen de kleurrijke onderwaterwereld en dode koraalskeletten",
            "Een lange lijst met wetenschappelijke Latijnse namen van vissen",
            "Een citaat uit een oud piratendagboek uit de zeventiende eeuw",
            "Het integraal afdrukken van de begroting van het eiland Bonaire"
        ],
        "antwoord": 0,
        "uitleg": "De auteur contrasteert de paradijselijke pracht van papegaaivissen met het spookachtige beeld van verbleekt koraal."
    },
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Wat is het doel van de centrale vraag aan het einde van alinea 1 in Tekst A?",
        "opties": [
            "De centrale probleemstelling over het lot van de riffen formuleren",
            "Vragen om de prijs van duiklessen op het eiland te verlagen",
            "Twijfel zaaien over het bestaan van tropische stormen",
            "Scholieren aansporen om mariene biologie te gaan studeren"
        ],
        "antwoord": 0,
        "uitleg": "De vraag formuleert de centrale probleemstelling van het artikel: kan het koraalrif van Bonaire nog gered worden?"
    },
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Waarom worden koraalriffen in alinea 2 'de regenwouden van de oceaan' genoemd?",
        "opties": [
            "Omdat ze een kwart van al het zeeleven herbergen op minder dan één procent van de bodem",
            "Omdat het onder water net zo hard regent als in het Amazonegebied",
            "Omdat koralen net als bomen van hout en bladeren zijn gemaakt",
            "Omdat er apen en papegaaien op de koraaltakken leven"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 verklaart deze metafoor door de enorme biodiversiteit (25% van al het zeeleven op <1% van de oceaanbodem)."
    },
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Wat is het biologische proces achter het 'verbleken' van koraal volgens alinea 3?",
        "opties": [
            "Gestrest koraal stoot de microscopische algen uit die voedsel en kleur leveren",
            "Koraal lost spontaan op in zout water wanneer er te veel golven zijn",
            "Vissen vreten de gekleurde buitenlaag van het koraal op bij honger",
            "De zon bleekt het koraal direct zoals chloor kleding ontkleurt"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 beschrijft dat koraalpoliepen bij te warm water hun symbiotische algen uitstoten, waardoor het koraal wit wordt en verhongert."
    },
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Op welke wijze vormt de slotzin van Tekst A een cirkelstructuur met de inleiding?",
        "opties": [
            "Door opnieuw te verwijzen naar duikers die koraal bewonderen",
            "Door dezelfde datum uit de geschiedenis te vermelden",
            "Door een vraag te stellen over de prijs van vliegtickets",
            "Door opnieuw het eiland Utrecht als voorbeeld te nemen"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin grijpt terug op duikers onder water uit alinea 1 (cirkelstructuur) en roept op tot bescherming."
    },
    {
        "type": "mc",
        "figuur": card_koraal,
        "vraag": "Welke twee handelingsadviezen worden in de slotalinea (alinea 6) gegeven?",
        "opties": [
            "Rifvriendelijke zonnebrand gebruiken en waterzuivering strenger handhaven",
            "Duiktoerisme verbieden en alle koraalriffen overdekken met zeilen",
            "De watertemperatuur verlagen met gigantische ijsblokken",
            "Alle papegaaivissen vangen en in aquaria in Europa onderbrengen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 adviseert het gebruik van rifvriendelijke zonnebrand en strenge handhaving van waterzuivering."
    },
    {
        "type": "waaronwaar",
        "figuur": card_koraal,
        "vraag": "Volgens alinea 4 is de chemische stof oxybenzone in gewone zonnebrandcrème volkomen onschadelijk voor jong koraal.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt dat oxybenzone het afweersysteem van jonge koraalstekjes ernstig aantast."
    },
    {
        "type": "waaronwaar",
        "figuur": card_koraal,
        "vraag": "Volgens alinea 5 lijmen biologen in kwekerijen geteelde koraalstekjes handmatig vast op beschadigde riffen.",
        "antwoord": True,
        "uitleg": "Waar. Dit handmatige herstelwerk met speciale lijm wordt in alinea 5 letterlijk beschreven."
    },
    {
        "type": "open",
        "figuur": card_koraal,
        "vraag": "Welke twee ernstige bedreigingen voor het koraalrif van Bonaire worden in alinea 3 en 4 behandeld?",
        "sleutelwoorden": [
            "opwarming/zeewater/temperatuur/warm water",
            "afvalwater/zonnebrandcrème/oxybenzone/vervuiling"
        ],
        "minTreffers": 1,
        "modelantwoord": "De opwarming van het zeewater en vervuiling door ongezuiverd afvalwater of zonnebrandcrème.",
        "uitleg": "Alinea 3 en 4 behandelen de stijgende watertemperatuur en vervuiling door afvalwater en zonnebrandchemicaliën."
    },
    {
        "type": "invul",
        "figuur": card_koraal,
        "vraag": "Met welk signaalwoord van conclusie begint de laatste alinea van Tekst A?",
        "antwoord": "Al met al|al met al",
        "uitleg": "'Al met al' kondigt de afrondende conclusie en adviezen aan."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Welke techniek past de auteur toe in alinea 1 van Tekst B om de lezer te boeien?",
        "opties": [
            "Een herkenbare, teleurstellende anekdote over een restaurantbezoek schetsen",
            "Een historisch overzicht van de Italiaanse keuken presenteren",
            "Een wiskundige berekening van de omzet van webwinkels geven",
            "Het interviewen van een chef-kok in Rome"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 beschrijft een herkenbare situatie: verlekkerd reserveren op basis van 5 sterren en lauwe magnetronpizza aantreffen."
    },
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Wat toont het statistische gegeven uit alinea 2 aan?",
        "opties": [
            "Dat het overgrote deel van de consumenten sterk leunt op online reviews",
            "Dat restaurants in Italië gemiddeld goedkoper zijn dan in Nederland",
            "Dat mensen steeds vaker contant betalen bij online aankopen",
            "Dat tachtig procent van de Nederlanders zelf recensies schrijft"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 toont aan dat ruim 80% van de Nederlanders reviews doorslaggevend vindt bij hun koopgedrag."
    },
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Welke twee malafide praktijken binnen de recensiewereld worden in alinea 3 en 4 genoemd?",
        "opties": [
            "Het inkopen van valse jubelrecensies en het zwartmaken van concurrenten",
            "Het hacken van bankrekeningen en het stelen van menukaarten",
            "Het eisen van gratis maaltijden door journalisten",
            "Het verkopen van kookboeken onder een valse naam"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 behandelt gekochte positieve reviews (klikboerderijen/AI) en alinea 4 valse één-ster-aanvallen op concurrenten."
    },
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Waarom hebben opsporingsalgoritmes van techbedrijven moeite met moderne neprecensies (alinea 5)?",
        "opties": [
            "Moderne AI-taalmodellen schrijven te overtuigend en gevarieerd",
            "Techbedrijven hebben geen internetverbinding in het weekend",
            "Consumenten weigeren om slechte ervaringen te melden",
            "De wet verbiedt het scannen van recensies op websites"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 legt uit dat AI-modellen zo levensecht formuleren dat detectiesoftware ze nauwelijks kan herkennen."
    },
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Welk advies geeft de auteur aan consumenten in de slotalinea (alinea 6)?",
        "opties": [
            "Niet blind varen op cijfers, maar spreiding bekijken en nuchter blijven",
            "Nooit meer online eten bestellen of hotels boeken",
            "Zelf uitsluitend nog één-ster-recensies achterlaten",
            "Alleen restaurants bezoeken die geen website hebben"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 adviseert om niet blind te vertrouwen op cijfers, jubelverhalen te wantrouwen en spreiding over tijd te checken."
    },
    {
        "type": "mc",
        "figuur": card_reviews,
        "vraag": "Wat is de stijl en functie van de uitsmijter in alinea 6 ('...prikken we door de digitale façade heen')?",
        "opties": [
            "Een pakkende beeldspraak die aanzet tot een kritische houding",
            "Een letterlijke waarschuwing voor beschadigde computerschermen",
            "Een citaat uit een Frans kooktijdschrift",
            "Een verontschuldiging van de auteur aan de horecabranche"
        ],
        "antwoord": 0,
        "uitleg": "De uitsmijter gebruikt de beeldspraak van 'door de façade heen prikken' om de consument tot scherpte aan te sporen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_reviews,
        "vraag": "Volgens alinea 3 worden klikboerderijen uitsluitend ingezet door non-profitorganisaties zonder winstoogmerk.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst spreekt van een lucratieve commerciële schaduweconomie waarin bedrijven betalen voor nepreviews."
    },
    {
        "type": "waaronwaar",
        "figuur": card_reviews,
        "vraag": "Volgens alinea 2 beïnvloeden online beoordelingen jaarlijks miljarden aan consumentenbestedingen.",
        "antwoord": True,
        "uitleg": "Waar. Dit enorme economische belang wordt in alinea 2 letterlijk genoemd."
    },
    {
        "type": "open",
        "figuur": card_reviews,
        "vraag": "Welke twee concrete tips geeft de auteur in alinea 6 aan consumenten om neprecensies te ontmaskeren?",
        "sleutelwoorden": [
            "spreiding bekijken/spreiding over tijd/langere tijd",
            "jubelverhalen negeren/overdreven verhalen/onafhankelijke tests"
        ],
        "minTreffers": 1,
        "modelantwoord": "Kijken naar de spreiding over langere tijd en overdreven jubelverhalen negeren.",
        "uitleg": "In alinea 6 noemt de auteur: spreiding over tijd bekijken, overdreven jubelverhalen negeren en onafhankelijke tests raadplegen."
    },
    {
        "type": "invul",
        "figuur": card_reviews,
        "vraag": "Met welk signaalwoord van conclusie luidt de auteur alinea 6 van Tekst B in?",
        "antwoord": "Concluderend|concluderend",
        "uitleg": "'Concluderend' signaleert dat de slotconclusie wordt geformuleerd."
    }
]

# ==============================================================================
# TOETS 21: §5 VASTE TEKSTSTRUCTUREN (TOETS I)
# Tekst A: Kweekvlees (Voor- en nadelenstructuur)
# Tekst B: De plastic tas door de eeuwen (Verleden-heden-toekomst / Chronologisch)
# ==============================================================================
kweekvlees_alineas = [
    "In 2013 presenteerde de Nederlandse hoogleraar Mark Post in Londen met veel ceremonieel 's werelds allereerste kweekvleesburger. De hamburger was niet afkomstig van een geslacht rund, maar opgekweekt uit een handjevol spierstamcellen in een steriele laboratoriumbioreactor. Het prijskaartje van die historische eerste hap: een slordige 250.000 euro. Ruim een decennium later staat kweekvlees op het punt van commerciële doorbraak. Is dit gekweekte eiwit de ultieme verlossing voor dieren en planeet, of een onbetaalbaar stukje Frankenstein-voedsel?",
    "Aan de positieve zijde biedt kweekvlees verbluffende ecologische en ethische voordelen. Om de groeiende wereldbevolking van dierlijke eiwitten te voorzien, hoeven in dit systeem geen miljarden dieren meer te worden gefokt en geslacht in de bio-industrie. Bovendien vereist kweekvlees tot wel negentig procent minder landbouwgrond en aanzienlijk minder water dan traditionele veehouderij, wat ontbossing kan stoppen.",
    "Een bijkomend voordeel is de voedselveiligheid: kweekvlees groeit in een steriele omgeving zonder antibiotica, waardoor het risico op gevaarlijke zoönosen (dierziekten die overspringen op mensen) en resistente bacteriën volledig verdwijnt.",
    "Daar staan echter aanzienlijke nadelen en economische barrières tegenover. Allereerst zijn de productiekosten van kweekvlees nog altijd torenhoog. Het op grote schaal laten groeien van cellen vereist dure voedingsvloeistoffen en bioreactoren die gigantische hoeveelheden elektriciteit verbruiken. Als die stroom niet honderd procent groen is, is de CO2-winst veel kleiner dan gehoopt.",
    "Daarnaast stuit kweekvlees op diepe psychologische weerstand bij consumenten. Veel mensen ervaren vlees uit een lab als 'onnatuurlijk' en vrezen onbekende gezondheidsrisico's op lange termijn. Ook blijkt het lastig om de complexe vezelstructuur van een malse biefstuk perfect na te bootsen.",
    "Afwegend kunnen we stellen dat kweekvlees een enorme technologische belofte inhoudt, maar nog een lange weg te gaan heeft. Pas wanneer de energiekosten drastisch dalen en consumenten hun koudwatervrees overwinnen, kan de bioreactor de bio-industrie écht naar het museum verwijzen."
]
card_kweekvlees = maak_leestekst_card("Tekst A: Kweekvlees: de bioreactor als redder van de planeet?", "Voeding & Toekomst, 2025", kweekvlees_alineas, "6 alinea's")

tas_alineas = [
    "Bijna iedereen heeft thuis wel zo'n 'la vol tassen' waarin opgevouwen plastic tasjes zich eindeloos ophopen. Toch is dit herkenbare plastic zakje een relatief recente uitvinding die in een halve eeuw tijd een ongekende gedaanteverwisseling heeft doorgemaakt. Hoe transformeerde een geniaal symbool van modern consumentengemak in een van de meest verfoeide milieuvervuilers ter wereld?",
    "Vroeger, in de eerste helft van de twintigste eeuw, deden onze grootouders hun boodschappen uitsluitend met rieten manden, linnen netjes of bruine papieren puntzakken. Die papieren zakken scheurden echter bij het minste spatje regen, en de productie kostte miljoenen bomen. In 1965 patenteerde de Zweedse ingenieur Sten Gustaf Thulin daarom de oersterke plastic tas van polyethyleen. De tas werd gevierd als een duurzame uitvinding die bomen redde en eindeloos hergebruikt kon worden.",
    "In de decennia daarna verwerd de plastic tas echter tot een wegwerpproduct. Winkels deelden jaarlijks miljarden gratis tasjes uit die na een eenmalig gebruik van twintig minuten in de vuilnisbak of in de natuur belandden, waar ze honderden jaren zwerfvuil en microplastics veroorzaakten.",
    "Tegenwoordig heeft het tij zich radicaal gekeerd. Sinds het Nederlandse verbod op gratis plastic tasjes in 2016 is het aantal zwerftasjes op straat met meer dan tachtig procent gedaald en brengt vrijwel iedereen een eigen shopper mee.",
    "In de toekomst zal het klassieke aardolieplastic definitief verdwijnen. Wetenschappers ontwikkelen bio-plastics op basis van algen en maïszetmeel die binnen enkele weken volledig afbreken in de tuinaarde als compost.",
    "Kortom: de geschiedenis van de plastic tas bewijst dat technisch gemak zonder milieubesef averechts uitpakt. Maar zij toont ook aan dat slim overheidsbeleid en gedragsverandering in staat zijn om een diepgewortelde wegwerpcultuur in recordtijd om te buigen naar een circulaire economie."
]
card_tas = maak_leestekst_card("Tekst B: De opkomst en val van de plastic tas", "Milieu & Consumptiegeschiedenis, 2025", tas_alineas, "6 alinea's")

vragen_ex21 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Welk model van de vaste tekststructuren herken je in het betoog van Tekst A over kweekvlees?",
        "opties": [
            "De voor- en nadelenstructuur",
            "De chronologische structuur",
            "De probleem-oplossingstructuur",
            "De bewering-argumentatiestructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst A behandelt in alinea 2 en 3 de voordelen en zet daar in alinea 4 en 5 de nadelen en bezwaren tegenover."
    },
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Wat wordt in alinea 2 en 3 genoemd als het belangrijkste ecologische pluspunt van kweekvlees?",
        "opties": [
            "Het bespaart tot 90% landbouwgrond en voorkomt ontbossing voor veevoer",
            "Het maakt het gebruik van traktoren in de landbouw volstrekt overbodig",
            "Het zorgt ervoor dat koeien sneller kunnen rennen in de wei",
            "Het laat regenwater sneller wegzakken in zandgronden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 stelt dat kweekvlees tot 90% minder landbouwgrond vereist en ontbossing kan tegengaan."
    },
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Welke signaalwoordgroep aan het begin van alinea 4 kondigt de overgang naar de bezwaren aan?",
        "opties": [
            "Daar staan echter",
            "Ten eerste",
            "Kortom",
            "Dientengevolge"
        ],
        "antwoord": 0,
        "uitleg": "'Daar staan echter aanzienlijke nadelen tegenover' markeert de klassieke overgang naar tegenargumenten."
    },
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Welk praktisch nadeel van kweekvlees wordt in alinea 4 beschreven?",
        "opties": [
            "Bioreactoren verbruiken enorme hoeveelheden energie en dure vloeistoffen",
            "Kweekvlees bederft al na tien seconden buiten de koelkast",
            "Het vlees kan uitsluitend rauw gegeten worden en niet gebakken",
            "Er mogen wettelijk geen kruiden aan kweekvlees worden toegevoegd"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 benadrukt dat grootschalige celgroei enorme hoeveelheden stroom en dure vloeistoffen vereist."
    },
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Wat is het uiteindelijke eindoordeel van de auteur over de toekomst van kweekvlees in alinea 6?",
        "opties": [
            "Het is een grote belofte, maar pas levensvatbaar bij lagere kosten en acceptatie",
            "De overheid moet alle slagers per direct sluiten en kweekvlees verplichten",
            "Kweekvlees is een hopeloze mislukking die nooit in supermarkten zal liggen",
            "Consumenten moeten uitsluitend nog plantaardige peulvruchten eten"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 concludeert genuanceerd dat energiekosten omlaag moeten en consumentenkoudwatervrees overwonnen moet worden."
    },
    {
        "type": "mc",
        "figuur": card_kweekvlees,
        "vraag": "Welk voordeel op het gebied van volksgezondheid wordt in alinea 3 uitdrukkelijk genoemd?",
        "opties": [
            "Er zijn geen antibiotica nodig, waardoor resistente bacteriën worden vermeden",
            "Het vlees geneest verkoudheid en griep binnen vierentwintig uur",
            "Het bevat tien keer zoveel vitamine C als verse sinaasappels",
            "Mensen hoeven nooit meer hun tanden te poetsen na het eten van kweekvlees"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat de steriele kweek zonder antibiotica het risico op resistente bacteriën en zoönosen elimineert."
    },
    {
        "type": "waaronwaar",
        "figuur": card_kweekvlees,
        "vraag": "Volgens alinea 1 werd de allereerste kweekvleesburger in 2013 gekweekt uit spierstamcellen van een levend rund.",
        "antwoord": True,
        "uitleg": "Waar. Dit historische feit van Mark Post in Londen wordt in alinea 1 beschreven."
    },
    {
        "type": "waaronwaar",
        "figuur": card_kweekvlees,
        "vraag": "Volgens alinea 5 vinden consumenten vlees uit een laboratorium meteen heerlijk natuurlijk en vertrouwd.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst meldt juist dat consumenten kweekvlees als 'onnatuurlijk' ervaren en psychologische weerstand voelen."
    },
    {
        "type": "open",
        "figuur": card_kweekvlees,
        "vraag": "Welke twee voorwaarden stelt de auteur in alinea 6 voordat de bioreactor de bio-industrie écht kan vervangen?",
        "sleutelwoorden": [
            "energiekosten/dalen/kosten dalen/goedkoper",
            "koudwatervrees overwinnen/koudwatervrees/weerstand overwinnen/acceptatie"
        ],
        "minTreffers": 1,
        "modelantwoord": "De energiekosten moeten drastisch dalen en consumenten moeten hun koudwatervrees overwinnen.",
        "uitleg": "Alinea 6 stelt: als de energiekosten drastisch dalen én consumenten hun koudwatervrees overwinnen."
    },
    {
        "type": "invul",
        "figuur": card_kweekvlees,
        "vraag": "Met welk signaalwoord van afweging begint de slotalinea van Tekst A?",
        "antwoord": "Afwegend|afwegend",
        "uitleg": "'Afwegend' markeert het begin van de afweging en conclusie in de slotalinea."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Welk model van de vaste tekststructuren herken je in de historische ontwikkeling van Tekst B?",
        "opties": [
            "De verleden-heden-toekomststructuur (chronologische structuur)",
            "De probleem-oplossingstructuur",
            "De bewering-argumentstructuur",
            "De voor- en nadelenstructuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B volgt de historische lijn: vroeger (alinea 2 en 3), heden (alinea 4) en toekomst (alinea 5)."
    },
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Waarom werd de plastic tas bij zijn uitvinding in 1965 juist als milieuvriendelijk beschouwd (alinea 2)?",
        "opties": [
            "Omdat hij stevig was en het kappen van bomen voor papieren zakken voorkwam",
            "Omdat de tas gemaakt werd van gerecycled vissenleer",
            "Omdat hij binnen drie minuten vanzelf oploste in zeewater",
            "Omdat hij direct diende als brandstof voor stoomtreinen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 vermeldt dat de uitvinder bomen wilde redden die gekapt werden voor scheurende papieren zakken."
    },
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Wat was volgens alinea 3 de hoofdoorzaak dat het plastic tasje een ecologische ramp werd?",
        "opties": [
            "Het verwerd tot een gratis wegwerpartikel met een levensduur van slechts twintig minuten",
            "De tassen werden gevuld met giftig chemisch afval door fabrieken",
            "Dieren leerden hoe ze de tassen moesten gebruiken als nestmateriaal",
            "Het plastic reageerde chemisch met de lucht en deed de ozonlaag verdwijnen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 legt uit dat de tas verwerd tot gratis wegwerpartikel dat na 20 minuten werd weggegooid en eeuwen bleef zwerven."
    },
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Wat was het meetbare effect van het Nederlandse verbod op gratis tasjes in 2016 (alinea 4)?",
        "opties": [
            "Het aantal zwerftasjes op straat daalde met meer dan tachtig procent",
            "Alle supermarkten in Nederland moesten tijdelijk sluiten",
            "De verkoop van rieten manden vertienvoudigde onmiddellijk",
            "De papierfabrieken gingen allemaal failliet"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 meldt dat het aantal zwerftassen met ruim 80% afnam na het verbod in 2016."
    },
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Welke innovatie voor de toekomst wordt in alinea 5 aangekondigd?",
        "opties": [
            "Bioplastics uit algen en maïszetmeel die composteren in tuinaarde",
            "Tassen geweven van gerecycled roestvrij staaldraad",
            "Elektronische tassen die zelf achter de klant aan rollen",
            "Een algeheel wereldwijd verbod op het meenemen van boodschappen"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 noemt bioplastics op basis van algen en maïszetmeel die in tuinaarde volledig afbreken."
    },
    {
        "type": "mc",
        "figuur": card_tas,
        "vraag": "Wat is de hoofdgedachte van de slotalinea van Tekst B?",
        "opties": [
            "Slim overheidsbeleid kan een wegwerpcultuur omvormen naar een circulaire economie",
            "De plastic tas had in 1965 nooit gepatenteerd mogen worden in Zweden",
            "Consumenten zijn niet in staat hun eigen gewoonten te veranderen",
            "Papieren zakken zijn onder alle omstandigheden superieur aan plastic"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 concludeert dat overheidsbeleid en gedragsverandering samen een wegwerpcultuur kunnen ombuigen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tas,
        "vraag": "Volgens alinea 2 waren papieren zakken in de vroege twintigste eeuw volkomen waterdicht bij zware regen.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst stelt dat papieren puntzakken juist scheurden bij het minste spatje regen."
    },
    {
        "type": "waaronwaar",
        "figuur": card_tas,
        "vraag": "Volgens alinea 4 brengen de meeste Nederlanders tegenwoordig zelf een herbruikbare tas mee naar de winkel.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt in alinea 4 genoemd als resultaat van de gedragsverandering sinds 2016."
    },
    {
        "type": "open",
        "figuur": card_tas,
        "vraag": "Welke twee natuurlijke grondstoffen worden in alinea 5 genoemd voor de fabricage van toekomstige bioplastics?",
        "sleutelwoorden": [
            "algen/zeewier",
            "maïszetmeel/maïs/zetmeel"
        ],
        "minTreffers": 1,
        "modelantwoord": "Algen en maïszetmeel.",
        "uitleg": "Alinea 5 vermeldt bioplastics op basis van algen en maïszetmeel."
    },
    {
        "type": "invul",
        "figuur": card_tas,
        "vraag": "Met welk signaalwoord van samenvatting vangt alinea 6 van Tekst B aan?",
        "antwoord": "Kortom|kortom",
        "uitleg": "'Kortom' luidt de afrondende samenvatting van de tekst in."
    }
]

# ==============================================================================
# TOETS 22: INTEGRALE EINDTOETS LEZEN (MIX §2 & §5 — EXAMENTRAINING B)
# Tekst A: Smartphone-algoritmes en privacy (Anekdote, vraagstelling, uitsmijter)
# Tekst B: Kernenergie in het klimaatdebat (Voor- en nadelenstructuur, afweging)
# ==============================================================================
algoritme_alineas = [
    "Je hebt het vast weleens meegemaakt: je praat met een vriend over een weekendje surfen in Portugal, en amper een uur later toont je Instagram-feed advertenties voor surflessen en wetsuits. Veel mensen geloven heilig dat hun smartphone hen stiekem afluistert via de microfoon. Maar de werkelijkheid is volgens datawetenschappers nog veel verontrustender: techbedrijven hoeven je helemaal niet af te luisteren. Hun algoritmes weten op basis van je digitale voetspoor al griezelig nauwkeurig wat je denkt en wilt. Hoe slagen deze computermodellen daarin en waar ligt de grens van onze privacy?",
    "Bij elke veegbeweging, like en zoekopdracht laten we een digitaal spoor achter. Grote techbedrijven combineren deze gegevens tot een uiterst gedetailleerd digitaal profiel. Ze weten niet alleen je leeftijd en woonplaats, maar ook je scrolsnelheid, je nachtelijke gewoontes en zelfs je wisselende gemoedstoestanden.",
    "Het geheim achter de griezelig treffende advertenties heet 'lookalike targeting'. Het algoritme ontdekt dat duizenden gebruikers met een vergelijkbaar zoek- en browsepatroon als jij interesse toonden in surfen. Zonder één gesproken woord op te vangen, concludeert het systeem met 99 procent zekerheid dat jij de volgende bent die die surfplank wil kopen.",
    "Critici waarschuwen dat deze datadrang leidt tot 'surveillance-kapitalisme': onze persoonlijke ervaringen worden gereduceerd tot gratis grondstof voor commerciële manipulatie en politieke beïnvloeding.",
    "Gelukkig bieden Europese privacywetten zoals de AVG houvast en kunnen gebruikers met slimme instellingen tracking beperken: cookies weigeren, locatievoorzieningen uitzetten en advertentie-identificatienummers resetten.",
    "Concluderend kunnen we stellen dat onze telefoons geen spionerende afluistervinken zijn, maar dat hyperintelligente algoritmes onze gedachten soms beter voorspellen dan we zelf kunnen. Het is tijd dat burgers hun digitale soevereiniteit terugeisen en niet klakkeloos op 'accepteer alle cookies' blijven klikken. Pas als we baas worden over onze eigen data, bepalen we zelf weer wat we zien, denken en kopen."
]
card_algoritme = maak_leestekst_card("Tekst A: Luistert je smartphone je af? De mythe ontmaskerd", "Technologie & Maatschappij, 2025", algoritme_alineas, "6 alinea's")

kernenergie_alineas = [
    "Terwijl de Europese Unie streeft naar een volledig klimaatneutrale economie in 2050, staat de energiewereld voor een kolossale puzzel. Zonne- en windenergie groeien exponentieel, maar wat doen we op windstille, grauwe winterdagen wanneer de stroomvraag piekt? In het verhitte klimaatdebat klinkt de roep om nieuwe kerncentrales luider dan ooit. Maar is kernenergie het onmisbare fundament van de energietransitie, of een peperdure, gevaarlijke dwaalweg?",
    "Voorstanders wijzen op de unieke betrouwbaarheid en milieuvriendelijkheid van atoomkracht. Een kerncentrale levert dag en nacht stabiele basisstroom, volkomen onafhankelijk van weersomstandigheden. Bovendien stoot kernenergie tijdens het opwekken geen gram CO2 uit. Ook het ruimtebeslag is minimaal: één centrale levert evenveel elektriciteit als duizenden windmolens op land.",
    "Bovendien blijkt uit statistieken dat kernenergie per opgewekte kilowattuur tot de veiligste energiebronnen ter wereld behoort, met veel minder slachtoffers dan steenkool of gas.",
    "Tegenstanders brengen daar zwaarwegende bezwaren tegenin. Het grootste struikelblok zijn de astronomische kosten en de tergend trage bouwtijd. Het bouwen van een moderne kerncentrale kost al snel tien tot vijftien miljard euro en duurt minstens tien tot vijftien jaar — tijd die we in de acute klimaatcrisis helemaal niet hebben.",
    "Daarnaast blijft het onopgeloste vraagstuk van het hoogradioactieve afval, dat honderdduizenden jaren veilig onder de grond moet worden opgeslagen. Tot slot vergt kernenergie enorme subsidies van belastingbetalers, geld dat volgens critici veel sneller en effectiever kan worden geïnvesteerd in energieopslag en slimme netten.",
    "Afwegend kunnen we concluderen dat kernenergie geen simpel wondermiddel is, maar evenmin zomaar kan worden afgeserveerd. Waar wind en zon op korte termijn de snelste winst boeken, kan kernenergie op de lange termijn dienen als stabiele achtervang. Een realistische energietransitie vereist geen ideologische stammenstrijd, maar een verstandige mix van hernieuwbare energie én CO2-vrije basislast."
]
card_kernenergie = maak_leestekst_card("Tekst B: Kernenergie: noodzakelijke reddingsboei of geldverslindende illusie?", "Energie, Politiek & Duurzaamheid, 2025", kernenergie_alineas, "6 alinea's")

vragen_ex22 = [
    # Tekst A (1-10)
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Welke herkenbare ervaring beschrijft de auteur in alinea 1 van Tekst A als aandachtstrekker?",
        "opties": [
            "Het verschijnen van Instagram-advertenties over een onderwerp waar je net over praatte",
            "Het per ongeluk bellen van een vreemde terwijl je telefoon in je broekzak zit",
            "Een computervirus dat al je vakantiefoto's plotseling wist",
            "Het kwijtraken van je oplader op een druk treinstation"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 opent met de herkenbare situatie dat je praat over surfen en direct daarna advertenties voor wetsuits ziet."
    },
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Wat is volgens datawetenschappers in alinea 1 de werkelijke reden voor de treffende advertenties?",
        "opties": [
            "Algoritmes voorspellen je gedrag nauwkeurig op basis van je digitale voetspoor",
            "Medewerkers van techbedrijven luisteren 's nachts de telefoons af",
            "Instagram heeft geheime satellietcamera's boven alle huizen hangen",
            "Je vrienden verkopen je surfgesprekken direct door aan bedrijven"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 1 ontzenuwt de afluistermythe: algoritmes voorspellen je interesses uiterst scherp aan de hand van je eerdere gedrag."
    },
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Hoe werkt het mechanisme van 'lookalike targeting' dat in alinea 3 wordt uitgelegd?",
        "opties": [
            "Het algoritme koppelt jouw gedrag aan duizenden gebruikers met een vergelijkbaar patroon",
            "De camera van de smartphone scant of jouw gezicht lijkt op dat van een bekend fotomodel",
            "Bedrijven sturen gratis proefmonsters naar iedereen met dezelfde achternaam",
            "De telefoon toont advertenties die uitsluitend populair zijn bij bejaarden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 3 beschrijft dat algoritmes voorspellen wat jij wilt doordat duizenden mensen met een vergelijkbaar patroon datzelfde zochten."
    },
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Waarom waarschuwen critici in alinea 4 voor 'surveillance-kapitalisme'?",
        "opties": [
            "Omdat persoonlijke ervaringen gratis grondstoffen worden voor manipulatie en winst",
            "Omdat de politie alle smartphones in beslag wil nemen",
            "Omdat internetbankieren binnenkort verboden wordt door de banken",
            "Omdat mobiele abonnementen elk jaar honderd euro duurder worden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 stelt dat surveillance-kapitalisme menselijke ervaring reduceert tot data voor manipulatie en beïnvloeding."
    },
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Welke oproep aan de lezer staat centraal in de slotalinea (alinea 6) van Tekst A?",
        "opties": [
            "Eis je digitale soevereiniteit terug en accepteer niet klakkeloos alle cookies",
            "Gooi je smartphone in de prullenbak en koop een oude typmachine",
            "Verwijder al je sociale media en praat nooit meer met vrienden over vakantie",
            "Stuur een boze brief naar het hoofdkantoor van Instagram in Amerika"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 spoort burgers aan om de regie te herwinnen en niet gedachteloos op cookie-knoppen te klikken."
    },
    {
        "type": "mc",
        "figuur": card_algoritme,
        "vraag": "Wat typeert de uitsmijter van Tekst A ('...bepalen we zelf weer wat we zien, denken en kopen')?",
        "opties": [
            "Een krachtige drieslag die de herwonnen vrijheid van de burger benadrukt",
            "Een waarschuwing dat alle winkels binnenkort failliet gaan",
            "Een vraag waarin de auteur toegeeft zelf verslaafd te zijn aan Instagram",
            "Een citaat van een negentiende-eeuwse filosoof over kleding"
        ],
        "antwoord": 0,
        "uitleg": "De slotzin sluit af met een krachtige stijlvorm (drieslag: zien, denken, kopen) over autonomie."
    },
    {
        "type": "waaronwaar",
        "figuur": card_algoritme,
        "vraag": "Volgens alinea 1 bevestigen datawetenschappers dat smartphones gesprekken via de microfoon afluisteren om advertenties te tonen.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst legt juist uit dat afluisteren een mythe is en dat algoritmes je gedrag voorspellen zonder audio-opnames."
    },
    {
        "type": "waaronwaar",
        "figuur": card_algoritme,
        "vraag": "Volgens alinea 5 biedt de Europese privacywetgeving (AVG) instrumenten om online tracking te beperken.",
        "antwoord": True,
        "uitleg": "Waar. Dit wordt letterlijk genoemd in alinea 5 als juridisch houvast."
    },
    {
        "type": "open",
        "figuur": card_algoritme,
        "vraag": "Welke twee specifieke instellingen kunnen gebruikers volgens alinea 5 aanpassen om tracking tegen te gaan?",
        "sleutelwoorden": [
            "cookies weigeren/geen cookies accepteren/cookies",
            "locatievoorzieningen uitzetten/locatie/advertentie-id resetten"
        ],
        "minTreffers": 1,
        "modelantwoord": "Het weigeren van cookies en het uitzetten van locatievoorzieningen (of resetten van advertentie-ID).",
        "uitleg": "In alinea 5 noemt de auteur: cookies weigeren, locatievoorzieningen uitzetten en advertentie-identificatienummers resetten."
    },
    {
        "type": "invul",
        "figuur": card_algoritme,
        "vraag": "Met welk signaalwoord van conclusie opent alinea 6 in Tekst A?",
        "antwoord": "Concluderend|concluderend",
        "uitleg": "'Concluderend' kondigt de samenvattende slotconclusie aan."
    },

    # Tekst B (11-20)
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Welke vaste tekststructuur herken je in het betoog van Tekst B?",
        "opties": [
            "De voor- en nadelenstructuur",
            "De verleden-heden-toekomststructuur",
            "De vraag-antwoordstructuur",
            "De chronologische structuur"
        ],
        "antwoord": 0,
        "uitleg": "Tekst B zet eerst de argumenten vóór kernenergie uiteen (alinea 2 en 3) en belicht daarna de nadelen (alinea 4 en 5)."
    },
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Wat is volgens alinea 2 het grootste voordeel van een kerncentrale ten opzichte van zonne- en windenergie?",
        "opties": [
            "Het levert dag en nacht stabiele basisstroom, ongeacht de weersomstandigheden",
            "Een kerncentrale kost helemaal niets om te bouwen voor de overheid",
            "Er is geen enkel onderhoud nodig gedurende de levensduur",
            "Het koelwater kan direct gedronken worden door de omwonenden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 2 benadrukt dat kernenergie weersonafhankelijke, stabiele basislast levert zonder directe CO2-uitstoot."
    },
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Welke twee zwaarwegende bezwaren tegen kerncentrales worden in alinea 4 aangevoerd?",
        "opties": [
            "De torenhoge bouwkosten en de tergend trage bouwtijd van tien tot vijftien jaar",
            "Het ontbreken van uranium op de aarde en het lawaai van de koeltorens",
            "De angst dat centrales spontaan wegvliegen bij een storm",
            "Dat kerncentrales uitsluitend stroom leveren aan buurlanden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 4 wijst op bouwkosten van 10-15 miljard euro en een bouwtijd van 10-15 jaar als enorme knelpunten."
    },
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Welk onopgelost milieuprobleem wordt in alinea 5 behandeld?",
        "opties": [
            "De veilige opslag van hoogradioactief afval voor honderdduizenden jaren",
            "De uitstoot van giftige roetdeeltjes die de ozonlaag aantasten",
            "De opwarming van de straten rondom de kerncentrale",
            "Het verdwijnen van zoetwater uit alle Nederlandse rivieren"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 5 noemt de veilige opslag van langlevend radioactief afval als groot onopgelost vraagstuk."
    },
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Wat is de afgewogen conclusie van de auteur in alinea 6?",
        "opties": [
            "Een verstandige energiemix combineren van hernieuwbare energie en stabiele basislast",
            "Alle investeringen in windmolens direct stopzetten ten gunste van kernkracht",
            "Het stroomverbruik in heel Europa met negentig procent verlagen",
            "Uitsluitend nog kolencentrales inzetten voor de wintermaanden"
        ],
        "antwoord": 0,
        "uitleg": "Alinea 6 pleit voor een nuchtere mix: snelle winst met wind/zon en kernenergie als stabiele achtervang."
    },
    {
        "type": "mc",
        "figuur": card_kernenergie,
        "vraag": "Welk signaalwoord van afweging leidt de slotbeschouwing in alinea 6 in?",
        "opties": [
            "Afwegend",
            "Omdat",
            "Vroeger",
            "Ten eerste"
        ],
        "antwoord": 0,
        "uitleg": "'Afwegend' is het signaalwoord waarmee de auteur de voor- en nadelen tegen elkaar afweegt."
    },
    {
        "type": "waaronwaar",
        "figuur": card_kernenergie,
        "vraag": "Volgens alinea 2 stoot een kerncentrale tijdens het opwekken van stroom meer CO2 uit dan een steenkoolcentrale.",
        "antwoord": False,
        "uitleg": "Onwaar. De tekst vermeldt expliciet dat kernenergie tijdens de stroomopwekking geen gram CO2 uitstoot."
    },
    {
        "type": "waaronwaar",
        "figuur": card_kernenergie,
        "vraag": "Volgens alinea 3 behoort kernenergie per kilowattuur statistisch tot de veiligste energiebronnen ter wereld.",
        "antwoord": True,
        "uitleg": "Waar. Dit statistische gegeven over lage slachtofferaantallen wordt in alinea 3 vermeld."
    },
    {
        "type": "open",
        "figuur": card_kernenergie,
        "vraag": "Welke twee nadelen of bezwaren tegen de bouw van kerncentrales worden in alinea 4 en 5 genoemd?",
        "sleutelwoorden": [
            "bouwkosten/duur/astronomische kosten/bouwtijd/traag",
            "radioactief afval/afval/subsidies"
        ],
        "minTreffers": 1,
        "modelantwoord": "De torenhoge bouwkosten (en trage bouwtijd) en het vraagstuk van radioactief afval.",
        "uitleg": "In alinea 4 en 5 worden de astronomische kosten/lange bouwtijd, het radioactieve afval en benodigde subsidies genoemd."
    },
    {
        "type": "invul",
        "figuur": card_kernenergie,
        "vraag": "Met welk signaalwoord van afweging vangt de slotconclusie in alinea 6 aan?",
        "antwoord": "Afwegend|afwegend",
        "uitleg": "'Afwegend' markeert het begin van de slotbeschouwing."
    }
]

examens = [
    {
        "file": "examen_18.js",
        "id": "ex-h3-nederlands-18",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 18 — §2 Inleiding en Slot (Toets H — Natuurherstel & Biologische Ritmes)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex18
    },
    {
        "file": "examen_19.js",
        "id": "ex-h3-nederlands-19",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 19 — §5 Vaste Tekststructuren (Toets H — Probleem-Oplossing & Verschijnsel-Verklaring)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex19
    },
    {
        "file": "examen_20.js",
        "id": "ex-h3-nederlands-20",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "2",
        "titel": "Toets 20 — §2 Inleiding en Slot (Toets I — Anekdotes, Cirkelstructuren & Reviewfraude)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex20
    },
    {
        "file": "examen_21.js",
        "id": "ex-h3-nederlands-21",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "5",
        "titel": "Toets 21 — §5 Vaste Tekststructuren (Toets I — Voor- en Nadelen & Verleden-Heden-Toekomst)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex21
    },
    {
        "file": "examen_22.js",
        "id": "ex-h3-nederlands-22",
        "hoofdstuk": 1,
        "hoofdstukTitel": "Cursus 1 — Meer dan lezen",
        "paragraaf": "mix",
        "titel": "Toets 22 — Cursus 1 Integrale Eindtoets Lezen (Mix §2 & §5 — Examentraining B)",
        "vak": "Nederlands · HAVO 3 (Cursus 1)",
        "icoon": "🎯",
        "duurMin": 25,
        "vragen": vragen_ex22
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

print("Alle 5 examens (18 t/m 22) succesvol gegenereerd!")
