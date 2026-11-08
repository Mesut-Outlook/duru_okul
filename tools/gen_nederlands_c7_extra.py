#!/usr/bin/env python3
"""Nederlands HAVO 3 · Cursus 7 Spelling — 5 extra proeftoetsen (examen_63…67.js, ex-h3-nederlands-63…67).

Bron: Noordhoff Nederlands 3 HAVO Cursus 7 (§2 Trema, apostrof, accenten en cedille; §3 Met of zonder n?;
§9 Werkwoordspelling; §10 Engelse werkwoorden; §11 Homofone werkwoordsvormen) + lesnotities docent
(inbox/2026-2027/nederlands/Nederlands Notlar/).

Schrijft havo3/nederlands/js/data/examen_63…67.js:
  63 · §7.2 Trema, apostrof, accenten en cedille: verdieping
  64 · §7.3 Met of zonder -n en bijvoeglijk naamwoord (-e / -en)
  65 · §7.9 Werkwoordspelling: tegenwoordige tijd, verleden tijd en voltooid deelwoord
  66 · §7.10 & §7.11 Engelse werkwoorden en homofone werkwoordsvormen
  67 · Foutentraining & Eindtoets Cursus 7 Spelling (§2, §3, §9–§11)

Draai: python3 tools/gen_nederlands_c7_extra.py
Daarna: node tools/gate.js nederlands && node tools/open_check.js && node tools/teslim_check.js nederlands 63
"""
import json, os, random, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "havo3", "nederlands", "js", "data")
rng = random.Random("c7_extra_2026_11_08")


def mc(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": list(fout), "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    """Spellings-invul: altijd exact: True."""
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "exact": True, "uitleg": uitleg}


def W(stelling, waar, uitleg):
    return {"type": "waaronwaar", "vraag": stelling, "antwoord": waar,
            "uitleg": ("Waar. " if waar else "Niet waar. ") + uitleg}


def O(vraag, sleutels, model, uitleg, minT=1):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": minT,
            "modelantwoord": model, "uitleg": uitleg}


TOETSEN = []

# =====================================================================================================
# 63 · §7.2 Trema, apostrof, accenten en cedille: verdieping
# =====================================================================================================
TOETSEN.append(dict(
    par="7.2", hf=7,
    titel="§7.2 Trema, apostrof, accenten en cedille: verdieping",
    icoon="✏️",
    vragen=[
        mc("Welke meervoudsvorm van het woord <i>bacterie</i> is juist gespeld?",
           "bacteriën", ["bacterieën", "bacterien", "bacteri-en"],
           "Bij woorden op -ie met de klemtoon vóór -ie schrijf je -ën: bac-te-ri-ën. Het trema staat op de e."),
        mc("Welke samenstelling met het woord <i>diploma</i> is helemaal goed geschreven?",
           "diploma-uitreiking", ["diplomauitreiking", "diplomaüitreiking", "diploma-üitreiking"],
           "In een samenstelling botsen de klinkers a en u; dan gebruik je een koppelteken en nooit een trema."),
        mc("Hoe spel je het meervoud van het woord <i>paraplu</i> in een Nederlandse zin?",
           "paraplu's", ["paraplus", "parapluus", "paraplu-s"],
           "Paraplu eindigt op de enkele klinker u; voor de meervouds-s komt een apostrof zodat de u lang blijft."),
        mc("Hoe schrijf je de jas die van Max is met een bezitsvorm?",
           "Max' winterjas", ["Max's winterjas", "Maxes winterjas", "Max-s winterjas"],
           "Max eindigt op een sisklank (x); de bezits-s valt weg en je schrijft alleen een apostrof als weglatingsteken."),
        mc("Wat is het juiste verkleinwoord van het Engelse leenwoord <i>hobby</i>?",
           "hobby'tje", ["hobbytje", "hobbietje", "hobby-tje"],
           "Hobby eindigt op -y met een medeklinker (b) ervoor; daarom krijgt het verkleinwoord een apostrof."),
        mc("Wat is het juiste verkleinwoord van het woord <i>jockey</i> (ruiter bij paardenraces)?",
           "jockeytje", ["jockey'tje", "jockey-tje", "jockietje"],
           "Vóór de -y staat een klinker (e); er is geen uitspraakprobleem, dus je schrijft jockeytje zonder apostrof."),
        mc("In welke woordgroep is de apostrof als weglatingsteken helemaal juist gebruikt?",
           "'s middags om drie uur", ["s' middags om drie uur", "'s-middags om drie uur", "smiddags om drie uur"],
           "'s middags staat voor des middags; de apostrof vervangt de weggelaten letters en er komt geen koppelteken."),
        mc("Kies het juist gespelde woord in: <i>Op de menukaart stond een Frans voorgerecht met ____.</i>",
           "crème fraîche", ["creme fraiche", "crème fraiche", "créme fraîche"],
           "Crème heeft een accent grave (è) en fraîche heeft een accent circonflexe (î)."),
        mc("Kies de juiste spelling: <i>De voorzitter wilde een nieuw ____ voorkomen door op tijd in te grijpen.</i>",
           "conflict", ["cónflict", "conflíct", "cônflict"],
           "Een klemtoonteken zet je alleen als er verwarring mogelijk is; bij conflict is geen accent nodig."),
        mc("In welke zin zijn de klemtoontekens op het woord met drie klinkers goed geplaatst?",
           "Dat was echt een móói doelpunt in de laatste minuut!",
           ["Dat was echt een móóí doelpunt in de laatste minuut!",
            "Dat was echt een moói doelpunt in de laatste minuut!",
            "Dat was echt een môôi doelpunt in de laatste minuut!"],
           "Bij drie opeenvolgende klinkers krijgen alleen de eerste twee klinkers een accent aigu: móói."),
        mc("Waarom staat er in het woord <i>reçu</i> (betalingsbewijs) een cedille onder de c?",
           "Omdat de c vóór de klinker u als een s moet klinken.",
           ["Omdat de c vóór de klinker u als een k moet klinken.",
            "Omdat de laatste lettergreep van het woord de klemtoon krijgt.",
            "Omdat er na de c een nieuwe lettergreep begint."],
           "Vóór a, o en u klinkt de c normaal als k; de cedille (ç) zorgt ervoor dat de c als s klinkt."),
        mc("In welk rijtje zijn het meervoud van <i>piano</i>, <i>cadeau</i> en <i>ski</i> allemaal goed gespeld?",
           "piano's – cadeaus – ski's",
           ["pianos – cadeaus – ski's",
            "piano's – cadeau's – ski's",
            "piano's – cadeaus – skis"],
           "Piano (o) en ski (i) eindigen op een enkele klinker → apostrof. Cadeau eindigt op -eau → geen apostrof."),
        W("In de samenstelling <i>collega-auteur</i> gebruik je een koppelteken omdat de a en de a botsen.", True,
          "In samenstellingen zet je bij klinkerbotsing (a + a) een koppelteken en geen trema."),
        W("Het meervoud van de afkorting <i>ufo</i> schrijf je zonder apostrof als <i>ufos</i>, omdat het geen Nederlandse afkorting is.", False,
          "Zowel bij woorden op een enkele klinker (-o) als bij afkortingen schrijf je een apostrof: ufo's."),
        W("In het woord <i>geïllustreerd</i> staat een trema op de i om te voorkomen dat je 'ei' als één klank leest.", True,
          "Ge- is een voorvoegsel; het trema op de i laat zien dat bij -illustreerd een nieuwe lettergreep begint."),
        W("In het woord <i>clubrecord</i> moet een cedille onder de eerste c staan, omdat er een u na komt.", False,
          "In clubrecord staat een l na de eerste c en een o na de tweede c, en beide klinken gewoon als k."),
        I("Schrijf het woord met het ontbrekende trema correct over: <i>financieel</i>", "financieel",
          "Let op: in financieel staat géén trema (fi-nan-ci-eel heeft geen uitspraakprobleem), maar in financiën wel."),
        I("Schrijf het voltooid deelwoord van <i>isoleren</i> correct op (denk aan het trema).", "geïsoleerd",
          "Ge-ï-so-leerd: zonder trema op de i zou je 'ei' als één klank lezen."),
        I("Schrijf de samenstelling van <i>massa</i> en <i>immigratie</i> correct aan elkaar.", "massa-immigratie",
          "Samenstelling waarin de klinkers a en i botsen → koppelteken: massa-immigratie."),
        O("Leg uit waarom je in <i>camera's</i> wél een apostrof schrijft, maar in <i>etages</i> niet.",
          ["enkele klinker/op een a/kort", "op een e/geen uitspraakprobleem"],
          "Camera eindigt op de enkele klinker a; zonder apostrof zou je die kort uitspreken. Etage eindigt op een e en daar is geen uitspraakprobleem.",
          "Bij -s na de enkele klinkers a, i, o, u en y schrijf je een apostrof; na een e niet.", minT=2),
    ]
))
# Fix question 17 in test 63 so it actually asks to add a missing trema (e.g. "officieel" -> "officiële" or "industrieel" -> "industriële")
TOETSEN[0]["vragen"][16] = I(
    "Schrijf het woord met het ontbrekende trema correct over: <i>officiele</i> (zoals in: de ____ opening).",
    "officiële",
    "Of-fi-ci-ë-le: het trema op de eerste e na de i laat zien dat daar een nieuwe lettergreep begint."
)

# =====================================================================================================
# 64 · §7.3 Met of zonder -n en bijvoeglijk naamwoord (-e / -en)
# =====================================================================================================
TOETSEN.append(dict(
    par="7.3", hf=7,
    titel="§7.3 Met of zonder -n en bijvoeglijk naamwoord (-e / -en)",
    icoon="✒️",
    vragen=[
        mc("Kies de juiste combinatie: <i>Op de vergadering namen ____ het woord, maar ____ leden zwegen.</i>",
           "enkelen – de meeste", ["enkele – de meeste", "enkelen – de meesten", "enkele – de meesten"],
           "Enkelen is zelfstandig gebruikt en verwijst naar personen → met n. De meeste leden staat vóór een zelfstandig naamwoord → zonder n."),
        mc("Kies de juiste combinatie: <i>In de boomgaard hingen ____ peren, maar ____ waren al door wespen aangevreten.</i>",
           "honderden – sommige", ["honderde – sommige", "honderden – sommigen", "honderde – sommigen"],
           "Honderden krijgt altijd een n. Sommige verwijst naar peren (zaken/dingen) → zonder n."),
        mc("Kies de juiste combinatie: <i>De ____ kregen voorrang bij de arts, terwijl de ____ in de wachtkamer bleven.</i>",
           "gewonden – anderen", ["gewonde – andere", "gewonden – andere", "gewonde – anderen"],
           "De gewonden en de anderen zijn zelfstandig gebruikte woorden voor meerdere personen → allebei met n."),
        mc("Kies de juiste combinatie: <i>Mijn zus kocht een ____ bureau en een ____ bureaustoel voor haar kamer.</i>",
           "nieuw – zwarte", ["nieuwe – zwarte", "nieuw – zwart", "nieuwe – zwart"],
           "Het bureau is een het-woord na 'een' → geen -e (nieuw). De bureaustoel is een de-woord → altijd -e (zwarte)."),
        mc("Kies de juiste combinatie: <i>Elk ____ lid ontvangt bij inschrijving dit ____ welkomstpakket.</i>",
           "nieuw – leuke", ["nieuwe – leuke", "nieuw – leuk", "nieuwe – leuk"],
           "Het lid na 'elk' → geen -e (nieuw). Het welkomstpakket na 'dit' → wel -e (leuke)."),
        mc("Kies de juiste vorm: <i>De archeologen vonden twee ____ munten en drie ____ kruiken in de grond.</i>",
           "bronzen – aardewerken", ["bronzen – aardewerkene", "bronzene – aardewerken", "bronzene – aardewerkene"],
           "Bronzen en aardewerken zijn stoffelijke bijvoeglijke naamwoorden (materiaal) en eindigen altijd op -en."),
        mc("Kies de juiste vorm: <i>Als ____ van het team mag jij vandaag de toss verrichten bij de scheidsrechter.</i>",
           "oudste", ["oudsten", "oud", "ouden"],
           "'Als oudste' slaat op één persoon (jij, enkelvoud) → eindigt op -e zonder n."),
        mc("Kies de juiste vorm: <i>Mijn neef en mijn nicht zijn ____ geslaagd voor hun rijexamen.</i>",
           "beiden", ["beide", "beidde", "beidden"],
           "Beiden is zelfstandig gebruikt en verwijst naar twee personen (neef en nicht) → met n."),
        mc("Welke zin over de boekenkast in de woonkamer is helemaal foutloos gespeld?",
           "Ik heb veel romans gelezen, maar enkele vond ik echt saai.",
           ["Ik heb veel romans gelezen, maar enkelen vond ik echt saai.",
            "Ik heb vele romans gelezen, maar enkelen vond ik echt saai.",
            "Ik heb velen romans gelezen, maar enkele vond ik echt saai."],
           "Enkele verwijst terug naar romans (zaken); je kunt 'romans' erachter invullen, dus zonder n."),
        mc("Wat betekent het verschil tussen <i>De voorzitter bedankte de aanwezige.</i> en <i>De voorzitter bedankte de aanwezigen.</i>?",
           "In de eerste zin bedankt hij één persoon, in de tweede meerdere personen.",
           ["In de eerste zin gaat het om dingen, in de tweede om personen.",
            "In de eerste zin is aanwezige bijvoeglijk, in de tweede zelfstandig.",
            "Er is geen betekenisverschil; beide vormen zijn meervoud."],
           "Een zelfstandig gebruikt bijvoeglijk naamwoord voor personen eindigt in het enkelvoud op -e en in het meervoud op -en."),
        mc("Kies de juiste vorm: <i>De ____ monteurs repareerden de kapotte motor binnen een uur.</i>",
           "ervaren", ["ervarene", "ervarenen", "ervarig"],
           "Bijvoeglijke naamwoorden die al op -en eindigen (zoals ervaren, open, eigen), krijgen geen extra -e."),
        mc("In welke zin is het bijvoeglijk naamwoord bij het het-woord <b>fout</b> geschreven?",
           "Wij hebben gisteren een gezellige restaurant in het centrum ontdekt.",
           ["Het gezellige restaurant zat op zaterdagavond helemaal vol.",
            "Dat gezellige restaurant serveert heerlijke Italiaanse gerechten.",
            "Ons gezellige restaurant bestaat volgende maand precies tien jaar."],
           "Het restaurant is een het-woord; na 'een' krijgt het bijvoeglijk naamwoord géén -e (een gezellig restaurant)."),
        W("Na woorden als <i>geen, elk</i> en <i>ieder</i> krijgt een bijvoeglijk naamwoord vóór een het-woord geen -e: <i>ieder goed idee</i>.", True,
          "Bij een het-woord schrijf je na een, geen, elk en ieder geen -e achter het bijvoeglijk naamwoord."),
        W("In de zin <i>Op het festival stonden tienduizende bezoekers voor het hoofdpodium</i> is het telwoord goed gespeld.", False,
          "Woorden als tientallen, honderden, (tien)duizenden en miljoenen schrijf je altijd met een n: tienduizenden."),
        W("Als een zelfstandig gebruikt bijvoeglijk naamwoord naar dieren of dingen verwijst, schrijf je geen n: <i>Van de appels neem ik de rode</i>.", True,
          "Bij zaken en dieren eindigt het zelfstandig gebruikte bijvoeglijk naamwoord op -e zonder n."),
        W("Een stoffelijk bijvoeglijk naamwoord krijgt bij een de-woord altijd een -e en bij een het-woord altijd -en.", False,
          "Een stoffelijk bijvoeglijk naamwoord (houten, glazen, wollen) eindigt altijd op -en, ongeacht het lidwoord."),
        I("Vul het stoffelijk bijvoeglijk naamwoord van <i>leer</i> in: <i>Mijn vader draagt een ____ jas.</i>", "leren",
          "Materiaal (leer) → stoffelijk bijvoeglijk naamwoord op -en: een leren jas."),
        I("Vul het stoffelijk bijvoeglijk naamwoord van <i>ijzer</i> in: <i>De tuin heeft een zwaar ____ hek.</i>", "ijzeren",
          "Materiaal (ijzer) → stoffelijk bijvoeglijk naamwoord op -en: een ijzeren hek."),
        I("Vul de juiste vorm van <i>groot</i> in: <i>Zij kochten een ____ appartement vlak bij het station.</i>", "groot",
          "Het appartement is een het-woord; na 'een' komt er geen -e achter het bijvoeglijk naamwoord: een groot appartement."),
        O("Leg uit waarom je in <i>Sommigen bleven na de les zitten</i> een n schrijft, maar in <i>Sommige stoelen waren bezet</i> niet.",
          ["personen/mensen", "zelfstandig/bijvoeglijk/naamwoord"],
          "In de eerste zin is sommigen zelfstandig gebruikt en verwijst het naar personen. In de tweede zin staat het bijvoeglijk vóór het zelfstandig naamwoord stoelen.",
          "Zelfstandig gebruikt + personen = met n; bijvoeglijk gebruikt (vóór een zelfstandig naamwoord) = zonder n.", minT=2),
    ]
))

# =====================================================================================================
# 65 · §7.9 Werkwoordspelling: alle tijden gemengd
# =====================================================================================================
TOETSEN.append(dict(
    par="7.9", hf=7,
    titel="§7.9 Werkwoordspelling: alle tijden gemengd",
    icoon="✍️",
    vragen=[
        I("De conducteur ____ (controleren) in de trein alle vervoersbewijzen.", "controleert",
          "De conducteur = hij (tegenwoordige tijd) → stam (controleer) + t = controleert."),
        I("____ (antwoorden) jij straks nog even op het bericht van de trainer?", "Antwoord",
          "Jij staat achter de persoonsvorm (inversie) → alleen de stam, zonder t: Antwoord jij?"),
        I("Mijn tante ____ (snijden) de versgebakken appeltaart in acht gelijke punten.", "snijdt",
          "Mijn tante = zij → stam (snijd) + t = snijdt."),
        I("Tijdens het kamperen ____ (branden) het kampvuur nog urenlang door.", "brandde",
          "Verleden tijd enkelvoud: stam brand → de d zit niet in 't kofschip X → brand + de = brandde."),
        I("De vrijwilligers ____ (verhuizen) vorige maand alle boeken naar het nieuwe gebouw.", "verhuisden",
          "Hele werkwoord verhuizen: de z zit niet in 't kofschip X → stam verhuis + den = verhuisden."),
        I("De passagiers ____ (wachten) gisteren bijna een uur op het perron.", "wachtten",
          "Verleden tijd meervoud: stam wacht → t zit in 't kofschip X → wacht + ten = wachtten."),
        I("De leerlingen hebben de hele middag voor het proefwerk ____ (oefenen).", "geoefend",
          "Voltooid deelwoord: stam oefen → n zit niet in 't kofschip X → ge + oefen + d = geoefend."),
        I("De burgemeester heeft het nieuwe sportpark gisteren feestelijk ____ (openen).", "geopend",
          "Voltooid deelwoord: stam open → n zit niet in 't kofschip X → ge + open + d = geopend."),
        mc("Kies de juiste persoonsvorm: <i>____ (houden) u ook zo van klassieke muziek?</i>",
           "Houdt", ["Houd", "Houden", "Hout"],
           "Bij 'u' blijft de t altijd staan, ook als u achter de persoonsvorm staat: stam houd + t = Houdt u."),
        mc("Kies de juiste persoonsvorm: <i>____ (rijden) jouw neef morgen ook mee naar het toernooi?</i>",
           "Rijdt", ["Rijd", "Rijden", "Rijt"],
           "Het onderwerp is 'jouw neef' (= hij, niet jij!). Daarom stam + t: Rijdt jouw neef mee?"),
        mc("Kies de juiste verleden tijd: <i>De fietser ____ (remmen) plotseling voor het rode stoplicht.</i>",
           "remde", ["remdde", "remte", "remden"],
           "De stam van remmen is rem (één m). De m zit niet in 't kofschip X → rem + de = remde."),
        mc("Kies de juiste verleden tijd: <i>De toeristen ____ (reizen) met de nachttrein naar Wenen.</i>",
           "reisden", ["reisten", "reisde", "reizen"],
           "Kijk naar het hele werkwoord reizen: de z zit niet in 't kofschip X → stam reis + den = reisden."),
        mc("Kies het juiste voltooid deelwoord: <i>De scheidsrechter heeft de wedstrijd kort ____ (onderbreken).</i>",
           "onderbroken", ["geonderbroken", "onderbreekt", "onderbreken"],
           "Onderbreken is een sterk en onscheidbaar werkwoord (klemtoon op -breken): het voltooid deelwoord is onderbroken, zonder ge-."),
        mc("Kies het juiste voltooid deelwoord: <i>Heb jij de kerstverlichting al in de boom ____ (ophangen)?</i>",
           "opgehangen", ["geopgehangen", "ophangen", "opgehangd"],
           "Ophangen is een scheidbaar sterk werkwoord (ik hang op): ge- komt in het midden → opgehangen."),
        mc("Kies het juiste voltooid deelwoord: <i>De verdachte werd door twee agenten ____ (vasthouden).</i>",
           "vastgehouden", ["vastgehoudt", "gevastgehouden", "vastgehoud"],
           "Vasthouden is scheidbaar en sterk: vast + ge + houden = vastgehouden."),
        mc("In welke zin zijn alle werkwoordsvormen foutloos gespeld?",
           "Hij antwoordde direct nadat hij het bericht had gelezen.",
           ["Hij antwoorde direct nadat hij het bericht had gelezen.",
            "Hij antwoordde direct nadat hij het bericht had geleest.",
            "Hij antwoordt gisteren direct nadat hij het bericht las."],
           "Stam antwoord + de = antwoordde (dubbele d); lezen is een sterk werkwoord → had gelezen."),
        W("In de zin <i>Zet jij de vuilniszak even buiten?</i> schrijf je maar één t omdat de stam al op t eindigt én jij achter de persoonsvorm staat.", True,
          "De stam van zetten is zet; bij inversie met jij gebruik je alleen de stam: Zet jij."),
        W("Het voltooid deelwoord van <i>herkennen</i> schrijf je als <i>geherkend</i>, met een d aan het eind.", False,
          "Werkwoorden die beginnen met be-, ge-, her-, ont-, ver- of er- krijgen géén extra ge-: het is herkend."),
        W("De verleden tijd van het werkwoord <i>straffen</i> bij <i>hij</i> schrijf je met dubbel f: <i>straffte</i>.", False,
          "De stam van straffen is straf (één f); f zit in 't kofschip X → straf + te = strafte."),
        O("Leg uit waarom je in <i>Wij geloofden zijn verhaal</i> de uitgang <i>-den</i> schrijft, terwijl er in de stam <i>geloof</i> een f staat.",
          ["hele werkwoord/geloven", "v/kofschip"],
          "Je kijkt naar het hele werkwoord geloven met een v. De letter v zit niet in 't kofschip X, dus krijgt de verleden tijd -de/-den: geloofden.",
          "Kijk bij werkwoorden met v/f of z/s naar het hele werkwoord (geloven → v niet in 't kofschip → -den).", minT=2),
    ]
))

# =====================================================================================================
# 66 · §7.10 & §7.11 Engelse werkwoorden en homofone werkwoordsvormen
# =====================================================================================================
TOETSEN.append(dict(
    par="7.10", hf=7,
    titel="§7.10 & §7.11 Engelse werkwoorden en homofonen",
    icoon="🇬🇧",
    vragen=[
        I("Mijn broertje ____ (gamen) in het weekend graag met zijn klasgenoten.", "gamet",
          "Hij → stam (game, Engelse spelling blijft) + t = gamet."),
        I("Vorige maand ____ (leasen) het bedrijf vijf elektrische bestelbusjes.", "leasete",
          "De stam lease eindigt in de uitspraak op een s-klank (zit in 't kofschip X) → lease + te = leasete."),
        I("Heb jij je oude winterjas al op die tweedehandssite ____ (plaatsen)?", "geplaatst",
          "Stam plaats → s zit in 't kofschip X → ge + plaats + t = geplaatst."),
        I("De ict-afdeling heeft gisteren alle computers op school ____ (resetten).", "gereset",
          "De stam van resetten is reset; omdat de stam al op een t eindigt, komt er bij het voltooid deelwoord geen extra t achter: gereset."),
        I("Wij hebben tijdens de vakantie elke dag met opa en oma ____ (facetimen).", "gefacetimed",
          "De stam facetime eindigt op een m-klank (niet in 't kofschip X) → ge + facetime + d = gefacetimed."),
        I("Het klimaat op aarde ____ (veranderen) de laatste tientallen jaren merkbaar.", "verandert",
          "Persoonsvorm in de tegenwoordige tijd bij het onderwerp 'het klimaat' (het) → stam verander + t = verandert."),
        I("De scholieren hebben het klaslokaal voor het afscheid prachtig ____ (versieren).", "versierd",
          "Hebben + voltooid deelwoord. Ver- krijgt geen ge-; verleng: het versierde lokaal → d: versierd."),
        I("De directeur ____ (beantwoorden) tijdens de ouderavond alle vragen van de ouders.", "beantwoordt",
          "Persoonsvorm in de tegenwoordige tijd bij 'de directeur' (hij) → stam beantwoord + t = beantwoordt."),
        mc("Welke vorm van het Engelse werkwoord <i>deleten</i> (verwijderen) is goed in: <i>Ik heb het bestand per ongeluk ____.</i>?",
           "gedeletet", ["gedelete", "gedeleted", "gedeleet"],
           "Stam delete (Engelse spelling blijft) eindigt op een t-klank ('diliet') → ge + delete + t = gedeletet."),
        mc("Kies de juiste verleden tijd: <i>Tijdens het concert ____ (streamen) zij het optreden live via haar telefoon.</i>",
           "streamde", ["streamte", "streamed", "striemde"],
           "De stam stream eindigt op een m-klank; de m zit niet in 't kofschip X → stream + de = streamde."),
        mc("Kies het juiste voltooid deelwoord: <i>Heb jij je foto's al op de externe harde schijf ____ (back-uppen)?</i>",
           "geback-upt", ["geback-upd", "back-geüpt", "gebackupt"],
           "Het streepje in back-up blijft staan; de stam eindigt op een p-klank (in 't kofschip X) → geback-upt."),
        mc("Kies de juiste vorm: <i>Niemand weet precies wat er die avond op het plein is ____ (gebeuren).</i>",
           "gebeurd", ["gebeurt", "gebeurdt", "gebeurde"],
           "Er staat het hulpwerkwoord 'is' bij → voltooid deelwoord. Verleng: het gebeurde voorval → met een d."),
        mc("Kies de juiste vorm: <i>Elke keer als ik dit programma opstart, ____ (gebeuren) er precies hetzelfde.</i>",
           "gebeurt", ["gebeurd", "gebeurdt", "gebeuren"],
           "Persoonsvorm van de hoofdzin in de tegenwoordige tijd → stam gebeur + t = gebeurt (lopen-test: loopt er)."),
        mc("Kies de juiste combinatie: <i>Hij ____ (beloven) beterschap, nadat hij eerder ook al veel had ____ (beloven).</i>",
           "belooft – beloofd", ["beloofd – belooft", "belooft – belooft", "beloofd – beloofd"],
           "Eerste plek: persoonsvorm bij hij → stam + t (belooft). Tweede plek: voltooid deelwoord bij had → beloven (v niet in 't kofschip) → beloofd."),
        mc("Kies de juiste combinatie: <i>De docent ____ (herhalen) de uitleg die hij gisteren ook al heeft ____ (herhalen).</i>",
           "herhaalt – herhaald", ["herhaald – herhaalt", "herhaalt – geherhaald", "herhaald – herhaald"],
           "Eerste plek: persoonsvorm bij de docent → herhaalt. Tweede plek: voltooid deelwoord bij heeft (her- krijgt geen ge-) → herhaald."),
        mc("In welke zin zijn zowel de persoonsvorm als het voltooid deelwoord foutloos geschreven?",
           "Word jij daar niet moe van als het rooster steeds wordt aangepast?",
           ["Wordt jij daar niet moe van als het rooster steeds wordt aangepast?",
            "Word jij daar niet moe van als het rooster steeds word aangepast?",
            "Word jij daar niet moe van als het rooster steeds wordt aangepasd?"],
           "Inversie met jij → Word jij (geen t). Bij 'het rooster' → wordt (stam + t) + aangepast (s in 't kofschip → t)."),
        W("Bij het Engelse werkwoord <i>racen</i> is de verleden tijd <i>racete</i>, omdat je aan het eind van de stam een s-klank hoort.", True,
          "Stam race spreek je uit als 'rees' (s-klank zit in 't kofschip X) → race + te = racete."),
        W("Het voltooid deelwoord van <i>updaten</i> is <i>geupdate</i>, want de stam eindigt al op een t-klank.", False,
          "De stam update eindigt in het schrift op -e (niet op de letter t), dus komt er een t achter én een trema op de u: geüpdatet."),
        W("In de zin <i>De reizigers worden bij de uitgang gecontroleerd</i> is <i>gecontroleerd</i> een persoonsvorm.", False,
          "Worden is hier de persoonsvorm; gecontroleerd is het voltooid deelwoord en eindigt daarom op een d."),
        O("Leg uit hoe je met de <b>lopen-test</b> en met <b>verlengen</b> het verschil bepaalt tussen <i>bepaalt</i> en <i>bepaald</i>.",
          ["persoonsvorm/loopt", "voltooid deelwoord/bepaalde/bijvoeglijk"],
          "Bij de persoonsvorm gebruik je de lopen-test: hij loopt → hij bepaalt (met t). Bij het voltooid deelwoord verleng je het woord tot een bijvoeglijk naamwoord: het bepaalde bedrag → je hoort een d.",
          "Persoonsvorm = lopen-test (t); voltooid deelwoord = verlengen tot bijvoeglijk naamwoord (d).", minT=2),
    ]
))

# =====================================================================================================
# 67 · Foutentraining & Eindtoets Cursus 7 Spelling (§2, §3, §9–§11)
# =====================================================================================================
TOETSEN.append(dict(
    par="eind", hf=7,
    titel="Foutentraining & Eindtoets Cursus 7 Spelling",
    icoon="🕵️",
    vragen=[
        I("Verbeter het fout gespelde woord in de zin: <i>Mijn oom heeft gisteren de nieuwe software gedownloadt.</i>", "gedownload",
          "De stam download eindigt al op een d; bij het voltooid deelwoord komt er geen t achter: gedownload."),
        I("Verbeter het fout gespelde woord in de zin: <i>Tijdens de reünie hebben wij urenlang over vroeger gediscussieerd.</i>", "gediscussieerd",
          "Let op: gediscussieerd heeft géén trema (ie + ee geeft geen uitspraakprobleem). Kies een zin met een echte fout."),
        I("Verbeter het fout gespelde woord in de zin: <i>De voorzitter heeft alle binnengekomen klachten gisteren beantwoordt.</i>", "beantwoord",
          "Heeft + voltooid deelwoord; de stam beantwoord eindigt al op een d, dus er komt geen t bij: beantwoord."),
        I("Verbeter het fout gespelde woord in de zin: <i>Vorige zomer verhuiste mijn buren naar een dorp in Drenthe.</i>", "verhuisden",
          "Het onderwerp 'mijn buren' is meervoud, en de z van verhuizen zit niet in 't kofschip X → verhuisden."),
        I("Verbeter het fout gespelde woord in de zin: <i>De scholiere heeft haar boekverslag gisteravond naar het portaal geupload.</i>", "geüpload",
          "Bij ge + upload spreek je de e en de u los van elkaar uit; daarom moet er een trema op de u staan: geüpload."),
        I("Verbeter het fout gespelde woord in de zin: <i>Op zolder vonden we drie kartonne dozen vol oude tijdschriften.</i>", "kartonnen",
          "Kartonnen is een stoffelijk bijvoeglijk naamwoord (van karton) en eindigt altijd op -en: kartonnen."),
        mc("Welk woord in deze zin is <b>fout</b> gespeld? <i>'s Morgens controleert de conciërge of alle lichten op de gang zijn uitgedaan en of er niets vreemds is gebeurt.</i>",
           "gebeurt", ["'s Morgens", "conciërge", "controleert"],
           "Na 'is' volgt een voltooid deelwoord: is gebeurd (met een d). De andere woorden zijn goed gespeld."),
        mc("Welk woord in deze zin is <b>fout</b> gespeld? <i>Tijdens het filmfestival in Italië bekeken duizende bezoekers de première van de documentaire.</i>",
           "duizende", ["Italië", "bekeken", "première"],
           "Tientallen, honderden, duizenden en miljoenen schrijf je altijd met een n: duizenden bezoekers."),
        mc("Welk woord in deze zin is <b>fout</b> gespeld? <i>Na het auto-ongeluk belde de geschrokken autoeigenaar direct het alarmnummer op zijn telefoon.</i>",
           "autoeigenaar", ["auto-ongeluk", "belde", "geschrokken"],
           "In de samenstelling auto + eigenaar botsen de o en de e → met een koppelteken: auto-eigenaar."),
        mc("Welk woord in deze zin is <b>fout</b> gespeld? <i>Mijn beide zussen hebben het filmpje op sociale media geliked en doorgestuurd naar hun vrienden.</i>",
           "geliked", ["beide", "zussen", "doorgestuurd"],
           "Het voltooid deelwoord van liken volgt de Nederlandse regels: stam like (k-klank) → ge + like + t = geliket."),
        mc("Kies het enige foutloos gespelde rijtje van drie woorden.",
           "patiënten – baby'tje – gereisd",
           ["patienten – baby'tje – gereisd",
            "patiënten – babytje – gereisd",
            "patiënten – baby'tje – gereist"],
           "Patiënten (trema op e), baby'tje (-y na medeklinker → apostrof) en gereisd (voltooid deelwoord van reizen: z niet in 't kofschip X → d)."),
        mc("Kies de zin waarin alle woorden <b>helemaal goed</b> zijn gespeld.",
           "Velen dachten dat het een makkelijk examen zou worden, maar sommigen vonden het best lastig.",
           ["Vele dachten dat het een makkelijk examen zou worden, maar sommigen vonden het best lastig.",
            "Velen dachten dat het een makkelijke examen zou worden, maar sommigen vonden het best lastig.",
            "Velen dachten dat het een makkelijk examen zou worden, maar sommige vonden het best lastig."],
           "Velen en sommigen zijn zelfstandig gebruikt voor personen → met n. Het examen is een het-woord na 'een' → makkelijk (zonder -e)."),
        mc("Welke vraagzin over de toetsvragen bevat géén enkele fout in de werkwoordspelling?",
           "Vind jij ook dat de docent de toetsvragen goed heeft voorbereid?",
           ["Vindt jij ook dat de docent de toetsvragen goed heeft voorbereid?",
            "Vind jij ook dat de docent de toetsvragen goed heeft voorbereidt?",
            "Vindt jij ook dat de docent de toetsvragen goed heeft voorbereidt?"],
           "Vind jij (inversie met jij → geen t) en heeft voorbereid (voltooid deelwoord; stam eindigt al op d → geen t erachter)."),
        mc("Kies de zin waarin het trema, het koppelteken en de apostrof allemaal goed zijn toegepast.",
           "Tijdens de radio-uitzending vertelde Chloë enthousiast over haar twee pony's.",
           ["Tijdens de radiouitzending vertelde Chloë enthousiast over haar twee pony's.",
            "Tijdens de radio-uitzending vertelde Chloë enthousiast over haar twee ponys.",
            "Tijdens de radio-üitzending vertelde Chloë enthousiast over haar twee pony's."],
           "Radio-uitzending (samenstelling met klinkerbotsing → koppelteken), Chloë (trema) en pony's (-s na enkele klinker y → apostrof)."),
        W("In de zin <i>De ouderen in de wijk hielpen de jongere met zijn kapotte fiets</i> gaat het om één jonge persoon.", True,
          "De jongere (zonder n, plus 'zijn fiets') is enkelvoud: één jong persoon. De ouderen (met n, hielpen) is meervoud."),
        W("In de zin <i>Gisteren skatete mijn neefje voor het eerst op de nieuwe baan</i> is de verleden tijd goed gespeld.", True,
          "Stam skate eindigt in de uitspraak op een t-klank (in 't kofschip X) → skate + te = skatete."),
        W("In de zin <i>De caissière gaf de klant een mooi katoene tasje mee</i> zijn alle woorden goed gespeld.", False,
          "Katoenen is een stoffelijk bijvoeglijk naamwoord (van katoen) en eindigt altijd op -en: een katoenen tasje."),
        W("In de zin <i>Wordt je morgen door je vader naar het station gebracht?</i> is de persoonsvorm goed gespeld.", False,
          "Je staat achter de persoonsvorm (inversie met jij/je), dus de t valt weg: Word je morgen gebracht?"),
        O("In de zin <i>De journaliste heeft het interview gisteren uitgewerkt en naar de redactie gemailt</i> staat één spelfout. Schrijf het foute woord verbeterd op en leg de regel uit.",
          ["gemaild", "klank/l/kofschip"],
          "Het foute woord is gemailt; dat moet gemaild zijn. De stam mail eindigt op een l-klank en die zit niet in 't kofschip X, dus ge + mail + d.",
          "Mailen → stam mail → l-klank zit niet in 't kofschip X → voltooid deelwoord gemaild.", minT=2),
        O("In de zin <i>Op tafel lagen zes glazen borden: vier witte en twee blauwen</i> staat één spelfout. Schrijf het foute woord verbeterd op en leg de regel uit.",
          ["zonder n/geen n", "zaken/dingen/voorwerpen"],
          "Het foute woord is blauwen; dat moet blauwe zijn (zonder n). Het zelfstandig gebruikte bijvoeglijk naamwoord verwijst naar borden (zaken, geen personen) en krijgt dus geen n.",
          "Zelfstandig gebruikt bijvoeglijk naamwoord voor zaken eindigt op -e zonder n: blauwe.", minT=2),
    ]
))
# Replace question 2 in test 67 with a real error to fix!
TOETSEN[4]["vragen"][1] = I(
    "Verbeter het fout gespelde woord in de zin: <i>De regisseur was erg geinteresseerd in het nieuwe filmscript.</i>",
    "geïnteresseerd",
    "Ge-ïn-te-res-seerd: zonder trema op de i zou je 'ei' als één klank lezen."
)


# =====================================================================================================
# Bouwen en valideren
# =====================================================================================================
def kaal(s):
    return re.sub(r"<[^>]+>", "", s)


def schud(v):
    opts = [v["_goed"]] + v["_fout"]
    rng.shuffle(opts)
    out = {k: x for k, x in v.items() if not k.startswith("_")}
    out["opties"] = opts
    out["antwoord"] = opts.index(v["_goed"])
    keys = ["type", "niveau", "vraag", "opties", "antwoord", "uitleg", "hint"]
    return {k: out[k] for k in keys if k in out}


def langste(v):
    L = [len(kaal(o)) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] < L[v["antwoord"]] for i in range(len(L)))


def kortste(v):
    L = [len(o) for o in v["opties"]]
    return all(i == v["antwoord"] or L[i] > L[v["antwoord"]] for i in range(len(L)))


def ok(vragen):
    m = [v for v in vragen if v["type"] == "mc"]
    if len(m) < 2:
        return True
    s = [v["antwoord"] for v in m]
    if max(s.count(i) for i in set(s)) / len(s) > 0.4:
        return False
    if len(s) < 6:
        return True
    if any(all(a == s[i - p] for i, a in enumerate(s) if i >= p) for p in (2, 3, 4)):
        return False
    n = max(len(v["opties"]) for v in m)
    if sum(1 for i in range(1, len(s)) if s[i] == (s[i - 1] + 1) % n) / (len(s) - 1) >= 0.5:
        return False
    return True


def bouw(ruw):
    for _ in range(20000):
        vragen = [schud(v) if v["type"] == "mc" else dict(v) for v in ruw]
        if ok(vragen):
            return vragen
    raise SystemExit("geen geldige optievolgorde gevonden")


def controleer_regel_19(nr, vragen):
    """Regel 19: het antwoord van een invul-vraag mag niet letterlijk in een andere vraag of optie van dezelfde toets staan."""
    invuls = [(idx, v) for idx, v in enumerate(vragen) if v["type"] == "invul"]
    for idx, inv in invuls:
        for ant in inv["antwoord"].split("|"):
            a_norm = ant.strip().lower()
            if len(a_norm) < 3:
                continue
            pat = re.compile(r"(?<![a-zà-ÿ])" + re.escape(a_norm) + r"(?![a-zà-ÿ])", re.I)
            for j, andere in enumerate(vragen):
                if j == idx:
                    continue
                teksten = [kaal(andere["vraag"])] + [kaal(o) for o in andere.get("opties", [])]
                for t in teksten:
                    if pat.search(t):
                        raise AssertionError(f"Regel 19 in examen_{nr}: invul #{idx+1} antwoord '{ant}' komt voor in vraag #{j+1}: {t}")


def schrijf(pad, kop, obj, fn):
    with open(pad, "w", encoding="utf-8") as f:
        f.write(kop + "\n" + fn + "(" + json.dumps(obj, ensure_ascii=False, indent=2) + ");\n")


KOP = "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 7 Spelling extra) — gegenereerd door tools/gen_nederlands_c7_extra.py */"

alle_vragen = set()
for i, t in enumerate(TOETSEN):
    nr = 63 + i
    assert len(t["vragen"]) == 20, (nr, len(t["vragen"]))
    vragen = bouw(t["vragen"])
    controleer_regel_19(nr, vragen)
    for v in vragen:
        assert v["vraag"] not in alle_vragen, v["vraag"]
        alle_vragen.add(v["vraag"])
        assert v.get("uitleg") and len(kaal(v["uitleg"])) >= 15, v["vraag"]
        if v["type"] == "open":
            q = kaal(v["vraag"]).lower()
            for s in v["sleutelwoorden"]:
                for w in s.split("/"):
                    assert not (len(w) > 2 and w.lower() in q), (nr, w, q)
    m = [v for v in vragen if v["type"] == "mc"]
    lang = sum(langste(v) for v in m)
    kort = sum(kortste(v) for v in m)
    wo = [v for v in vragen if v["type"] == "waaronwaar"]
    onw = sum(not v["antwoord"] for v in wo)
    print(f"examen_{nr}: mc {len(m)} (langste {lang}/{len(m)}, kortste {kort}/{len(m)}), "
          f"wow {len(wo)} (onwaar {onw}), invul {sum(v['type'] == 'invul' for v in vragen)}, "
          f"open {sum(v['type'] == 'open' for v in vragen)}, volgorde {''.join(str(v['antwoord']) for v in m)}")
    assert lang / len(m) <= 0.4, (nr, "langste", lang, len(m))
    assert kort / len(m) <= 0.4, (nr, "kortste", kort, len(m))
    assert onw / len(wo) >= 0.35, (nr, "onwaar", onw, len(wo))
    titel = f"Toets {nr} — {t['titel']}"
    schrijf(os.path.join(ROOT, f"examen_{nr}.js"), KOP,
            {"id": f"ex-h3-nederlands-{nr}", "hoofdstuk": t["hf"], "hoofdstukTitel": "Cursus 7 — Spelling",
             "paragraaf": t["par"], "titel": titel, "vak": "Nederlands · HAVO 3 (Cursus 7)",
             "icoon": t["icoon"], "duurMin": 20, "vragen": vragen}, "DURU.registerExamen")
