#!/usr/bin/env python3
"""Biologie HAVO 3 · H11 Voortplanting · §11.3 Zwangerschap (boek p. 139–145).
Schrijft havo3/biologie/js/data/h11_3.js (onderwerp) + examen_12/13/14.js (ex-h3-biologie-12…14).
mc-volgorde willekeurig (geseed), opnieuw geschud tot gate-regels 3/16 kloppen.
⚠️ Zodra Duru een toets gemaakt heeft: id-inhoud niet meer wijzigen (nieuwe toets = nieuwe id)."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'havo3', 'biologie', 'js', 'data')

def M(vraag, goed, fout, uitleg):
    return {"type": "mc", "vraag": vraag, "_goed": goed, "_fout": fout, "uitleg": uitleg}


def W(vraag, antwoord, uitleg):
    return {"type": "waaronwaar", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def I(vraag, antwoord, uitleg):
    return {"type": "invul", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def O(vraag, sleutels, min_, model, uitleg):
    return {"type": "open", "vraag": vraag, "sleutelwoorden": sleutels, "minTreffers": min_,
            "modelantwoord": model, "uitleg": uitleg}


def plaats(vragen, rng):
    """Schud mc-opties tot: ≤40% op één index, geen periode 2–4, <60% '+1'-stappen."""
    mcs = [v for v in vragen if v["type"] == "mc"]
    for _ in range(5000):
        pos = [rng.randrange(len(v["_fout"]) + 1) for v in mcs]
        if max(pos.count(i) for i in set(pos)) / len(pos) > 0.4:
            continue
        if len(pos) < 6:  # gate 16 kijkt pas vanaf 6 mc
            break
        if any(all(a == pos[i - p] for i, a in enumerate(pos) if i >= p) for p in (2, 3, 4)):
            continue
        n = max(len(v["_fout"]) + 1 for v in mcs)
        if sum(pos[i + 1] == (pos[i] + 1) % n for i in range(len(pos) - 1)) / (len(pos) - 1) >= 0.6:
            continue
        break
    else:
        raise SystemExit("geen geldige volgorde gevonden")
    for v, p in zip(mcs, pos):
        opties = list(v.pop("_fout"))
        rng.shuffle(opties)
        opties.insert(p, v.pop("_goed"))
        v["opties"], v["antwoord"] = opties, p
    return vragen


def langste_aandeel(vragen):
    mcs = [v for v in vragen if v["type"] == "mc"]
    n = sum(all(len(o) < len(v["opties"][v["antwoord"]]) for i, o in enumerate(v["opties"]) if i != v["antwoord"]) for v in mcs)
    return n, len(mcs)


THEORIE = """
<h3>11.3 Zwangerschap</h3>
<p>Als een vrouw weet dat ze zwanger is, gaat ze naar een <b>verloskundige</b>. Die onderzoekt haar regelmatig om te zorgen dat moeder en kind gezond zijn.</p>

<h3>Hoe veranderen moeder en kind?</h3>
<p>Nadat het embryo zich heeft ingenesteld in de baarmoeder, gaat de ontwikkeling heel snel.</p>
<div class="formule-box"><b>Embryonale fase</b> = de eerste <b>twaalf weken</b> van de zwangerschap: alle organen van het kindje ontstaan.<br><b>Foetus</b> = het kindje na de embryonale fase: het ziet er al uit als een mensje en groeit vanaf nu alleen nog.</div>
<ul>
  <li>In de eerste twaalf weken is aan de buik van de vrouw niet veel te zien. Wel kan ze zich <b>moe en misselijk</b> voelen en trek hebben in ander eten dan normaal.</li>
  <li>Pas als de foetus ongeveer <b>twintig weken</b> oud is, wordt de buik dikker. Ze kan het kindje nu ook voelen bewegen.</li>
  <li>Doordat de foetus groter wordt, komen de <b>organen in de buik in de verdrukking</b>: de vrouw kan last krijgen van <b>oprispend maagzuur</b> en moet vaker naar de wc, omdat de <b>urineblaas</b> minder ruimte heeft voor urine.</li>
  <li>Het hormoon <b>progesteron</b> stimuleert de groei van de <b>melkklieren</b> in de borsten. De borsten worden ook groter door extra <b>vet</b>, dat de melkklieren beschermt.</li>
</ul>

<h3>Hoe leeft het kindje in de baarmoeder?</h3>
<p>Het kindje zit veilig in een 'zak' van <b>vruchtvliezen</b>, gevuld met <b>vruchtwater</b>. Die beschermen het embryo en de foetus tegen stoten.</p>
<p>Op de plaats waar de bevruchte eicel is ingenesteld, groeit de <b>placenta</b> (<b>moederkoek</b>). De foetus is via de <b>navelstreng</b> met de placenta verbonden. In de placenta lopen de bloedvaten van de foetus dicht langs de bloedvaten van de moeder. De wanden zijn zo dun dat hier <b>stoffen worden uitgewisseld</b>.</p>
<table class="nask"><tr><th>bloedvat in de navelstreng</th><th>wat vervoert het?</th></tr>
<tr><td>één <b>navelstrengader</b></td><td>van de moeder naar het kind: zuurstof en voedingsstoffen</td></tr>
<tr><td>twee <b>navelstrengslagaders</b></td><td>van het kind naar de moeder: afvalstoffen zoals koolstofdioxide</td></tr></table>
<div class="info-box tip"><span class="kop">De placenta als filter</span>
<p>De placenta houdt veel schadelijke stoffen en ziekteverwekkers tegen. Toch komen <b>alcohol, drugs, het rodehondvirus en nicotine</b> uit sigaretten wél via de placenta bij het embryo.</p></div>

<h3>Welk effect hebben schadelijke stoffen?</h3>
<p>Nicotine, alcohol, drugs en het rodehondvirus zijn schadelijk: het kindje groeit slechter, kan <b>afwijkingen</b> krijgen of doodgaan. Schadelijke stoffen hebben vooral veel effect in de <b>eerste weken</b> van de zwangerschap.</p>
<ul>
  <li><b>Rodehond</b> is niet gevaarlijk, behalve voor ongeboren kinderen: die kunnen oogafwijkingen en gehoorverlies krijgen.</li>
  <li>Alcohol kan leiden tot <b>Foetaal Alcohol Syndroom (FAS)</b>: de hersenen groeien niet goed, het kind heeft vaker een verstandelijke beperking en is kleiner dan leeftijdsgenoten.</li>
  <li>Bij <b>een op de tien</b> zwangerschappen gaat er in de eerste twaalf weken iets mis. Vaak sterft het embryo en wordt het afgestoten: een <b>miskraam</b>.</li>
</ul>

<h3>Hoe gaat de bevalling?</h3>
<p>Vanaf <b>zes weken</b> voor de bevalling trekken de spieren van de baarmoeder samen: een <b>wee</b>. Deze eerste weeën zijn <b>indalingsweeën</b>. Bij de <b>indaling</b> draait het kindje en komt het met het hoofdje naar beneden tegen de baarmoedermond aan te liggen. Na gemiddeld <b>veertig weken</b> wordt het kindje geboren.</p>
<ol>
  <li><b>Ontsluiting</b>: regelmatige weeën laten de baarmoedermond opengaan. Vlak voor of tijdens de ontsluiting breken de vruchtvliezen en loopt het vruchtwater naar buiten.</li>
  <li><b>Uitdrijving</b>: de baarmoedermond is ver genoeg open en sterke <b>persweeën</b> duwen de baby door de vagina naar buiten.</li>
  <li><b>Nageboorte</b>: weeën duwen de placenta met vruchtvliezen en resten van de navelstreng naar buiten.</li>
</ol>
<p>Zodra de baby geboren is, gaat hij zelf ademen. De verloskundige maakt het mondje schoon, knijpt de navelstreng dicht met twee klemmetjes en knipt hem tussen de klemmetjes door. Het stompje valt na een paar dagen af; het litteken is de <b>navel</b>.</p>
<div class="info-box let-op"><span class="kop">Als de baby niet goed ligt</span>
<p>Bij een <b>stuitligging</b> worden de billen eerst geboren en dan pas het hoofdje. Bij een <b>dwarsligging</b> kan de baby niet via de vagina geboren worden: de arts doet een <b>keizersnede</b>, een operatie waarbij een chirurg een snee onder in de buik maakt. Ook als de placenta voor de baarmoedermond ligt, volgt een keizersnede.</p></div>

<h3>Hoe ontstaat een tweeling?</h3>
<ul>
  <li><b>Eeneiige tweeling</b>: uit één bevruchte eicel (één eicel en één zaadcel). Het bolletje cellen splitst zich tijdens de eerste delingen in tweeën. Altijd hetzelfde geslacht; ze lijken sprekend op elkaar.</li>
  <li><b>Twee-eiige tweeling</b>: bij de eisprong komen twee eicellen tegelijk vrij en beide worden bevrucht. Ze kunnen op elkaar lijken, maar dat hoeft niet; het kunnen ook broer en zus zijn.</li>
</ul>
<p>Bij een twee-eiige tweeling zijn er altijd twee placenta's en heeft elk embryo eigen vruchtvliezen. Bij een eeneiige tweeling is dat zo als de splitsing vóór de innesteling plaatsvindt. Bij één procent van de eeneiige tweelingen splitst het pas na de innesteling: dan delen de embryo's placenta en vruchtvliezen.</p>
<p>Een <b>meerling</b> (drieling, vierling, ...) komt natuurlijk zelden voor: een drieling bij 1 op de 6400 zwangerschappen. Omdat er minder ruimte per baby is, is er meer risico op een te vroege geboorte.</p>

<h3>Toepassen: eieren</h3>
<p>Bij veel dieren begint het leven met een eicel die is verpakt als <b>ei</b>; alle eicellen bevatten <b>reservevoedsel</b> voor het embryo.</p>
<ul>
  <li><b>Vogels</b> leggen grote eieren met een kalkschaal die uitdroging voorkomt; de dooier is de eigenlijke eicel.</li>
  <li><b>Vissen</b> hebben een taai vlies in plaats van een schaal en geen laag gelei.</li>
  <li><b>Zoogdieren</b> hebben een kleine eicel zonder schaal met weinig reservevoedsel: in de baarmoeder krijgt het embryo voedingsstoffen via uitwisseling met het bloed van de moeder.</li>
</ul>
"""

BEGRIPPEN = [
    ("embryonale fase", "De eerste twaalf weken van de zwangerschap, waarin alle organen van het kindje ontstaan."),
    ("foetus", "Het ongeboren kind na de embryonale fase, dat er al uitziet als een mensje en alleen nog groeit."),
    ("progesteron", "Hormoon dat de groei van de melkklieren in de borsten stimuleert."),
    ("vruchtvliezen", "De zak rond het kindje in de baarmoeder, gevuld met vruchtwater."),
    ("vruchtwater", "De vloeistof in de vruchtvliezen die het kindje beschermt tegen stoten."),
    ("placenta", "De moederkoek: groeit waar de eicel is ingenesteld en is de plaats waar stoffen tussen moeder en kind worden uitgewisseld."),
    ("navelstreng", "Verbinding tussen de foetus en de placenta met drie bloedvaten."),
    ("navelstrengader", "Het ene bloedvat in de navelstreng dat zuurstof en voedingsstoffen van de moeder naar het kind vervoert."),
    ("navelstrengslagaders", "De twee bloedvaten in de navelstreng die afvalstoffen van het kind naar de moeder vervoeren."),
    ("Foetaal Alcohol Syndroom (FAS)", "Gevolg van alcohol tijdens de zwangerschap: de hersenen groeien niet goed en het kind is vaker verstandelijk beperkt en kleiner."),
    ("miskraam", "Het afsterven en afstoten van het embryo als er iets misgaat met de ontwikkeling."),
    ("wee", "Het samentrekken van de spieren van de baarmoeder."),
    ("indaling", "Het draaien van het kindje met het hoofdje naar beneden tegen de baarmoedermond, door indalingsweeën."),
    ("ontsluiting", "De eerste fase van de bevalling: door weeën gaat de baarmoedermond open."),
    ("uitdrijving", "De tweede fase van de bevalling: persweeën duwen de baby door de vagina naar buiten."),
    ("nageboorte", "De derde fase van de bevalling: de placenta met vruchtvliezen en resten van de navelstreng komen naar buiten."),
    ("keizersnede", "Operatie waarbij een chirurg een snee onder in de buik maakt om de baby te halen, bijvoorbeeld bij een dwarsligging."),
    ("eeneiige tweeling", "Tweeling uit één bevruchte eicel die zich splitst; altijd hetzelfde geslacht."),
    ("twee-eiige tweeling", "Tweeling uit twee eicellen die tegelijk zijn bevrucht; heeft altijd twee placenta's."),
]

ONDERWERP_VRAGEN = [
    {"type": "mc", "niveau": 1, "vraag": "Hoe lang duurt een zwangerschap gemiddeld tot de geboorte?",
     "_goed": "Veertig weken", "_fout": ["Twaalf weken", "Twintig weken", "Zes weken"],
     "uitleg": "Na gemiddeld veertig weken is de baby volgroeid en wordt hij geboren.", "hint": "Denk aan negen maanden."},
    {"type": "mc", "niveau": 1, "vraag": "Wanneer wordt de buik van de zwangere vrouw duidelijk dikker?",
     "_goed": "Na ongeveer twintig weken", "_fout": ["Na ongeveer vier weken", "Na ongeveer twaalf weken", "Pas vlak voor de bevalling"],
     "uitleg": "In de eerste twaalf weken is aan de buik weinig te zien; pas rond twintig weken wordt de buik dikker.",
     "hint": "Dit is ver na de embryonale fase."},
    {"type": "mc", "niveau": 2, "vraag": "Wanneer hebben schadelijke stoffen het grootste effect op het kindje?",
     "_goed": "In de eerste weken van de zwangerschap", "_fout": ["Vlak voor de bevalling", "Pas na de twintigste week", "In elke periode even veel"],
     "uitleg": "Schadelijke stoffen hebben vooral veel effect in de eerste weken, als de organen ontstaan.", "hint": "Denk aan de embryonale fase."},
    {"type": "mc", "niveau": 3, "vraag": "Bij hoeveel zwangerschappen gaat er in de eerste twaalf weken iets mis met de ontwikkeling van het embryo?",
     "_goed": "Bij één op de tien", "_fout": ["Bij één op de honderd", "Bij één op de twee", "Bij één op de duizend"],
     "uitleg": "Bij een op de tien zwangerschappen gaat er in de eerste twaalf weken iets mis; vaak volgt dan een miskraam.", "hint": "Het gaat om een tiende deel."},
    {"type": "mc", "niveau": 2, "vraag": "Wat gebeurt er bij de indaling?",
     "_goed": "Het kindje draait en komt met het hoofdje naar beneden",
     "_fout": ["De baarmoedermond gaat open door de weeën", "De placenta komt samen met de vruchtvliezen naar buiten", "De navelstreng wordt tussen twee klemmetjes doorgeknipt"],
     "uitleg": "Door indalingsweeën draait het kindje en ligt het met het hoofdje tegen de baarmoedermond.", "hint": "Dit gebeurt al zes weken voor de bevalling."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "Bij een stuitligging worden de billen van de baby eerst geboren.",
     "antwoord": True, "uitleg": "Waar. Bij een stuitligging komen eerst de billen en dan pas het hoofdje.", "hint": "Stuit betekent billen."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Een eeneiige tweeling heeft altijd twee placenta's.",
     "antwoord": False, "uitleg": "Niet waar. Alleen als de splitsing vóór de innesteling plaatsvindt; bij een deel van de eeneiige tweelingen delen de embryo's de placenta.",
     "hint": "Wanneer de splitsing plaatsvindt, bepaalt het aantal placenta's."},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Bij een vissenei zit rondom de eicel een harde kalkschaal.",
     "antwoord": False, "uitleg": "Niet waar. Visseneieren hebben een taai vlies en geen kalkschaal; een kalkschaal hoort bij een vogelei.",
     "hint": "Denk aan het ei van een kip, en dan aan een viseitje."},
    {"type": "invoer", "niveau": 2, "vraag": "Welke stof in de borsten beschermt de melkklieren, naast de melkklieren zelf? (één woord)",
     "antwoord": "vet", "uitleg": "De borsten worden groter door de groei van melkklieren en door extra vet, dat de melkklieren beschermt.", "hint": "Het zit naast de melkklieren."},
    {"type": "invoer", "niveau": 1, "vraag": "Hoe heet het orgaan waarin het ongeboren kind groeit?",
     "antwoord": "baarmoeder|de baarmoeder", "uitleg": "Het embryo nestelt zich in de baarmoeder en groeit daar tot het geboren wordt.", "hint": "Het zit in de onderbuik van de vrouw."},
]

EXAMENS = {
12: ("Begrippen en bouw", "🤰", [
    M("Hoe heet de periode van de eerste twaalf weken, waarin alle organen ontstaan?", "De embryonale fase",
      ["De foetale fase", "De indalingsfase", "De ontsluitingsfase"],
      "In de embryonale fase, de eerste twaalf weken, ontstaan alle organen van het kindje."),
    M("Waar groeit de placenta?", "Waar de eicel zich innestelt",
      ["Waar de eicel is bevrucht", "Aan de binnenkant van de vagina", "Rond de baarmoedermond"],
      "Op de plaats waar de bevruchte eicel is ingenesteld, groeit de placenta."),
    M("Hoeveel bloedvaten lopen er door de navelstreng?", "Drie: een ader en twee slagaders",
      ["Twee: een ader en een slagader", "Twee: twee aders", "Vier: twee aders en twee slagaders"],
      "Door de navelstreng lopen één navelstrengader en twee navelstrengslagaders."),
    M("Waaruit bestaat de zak waarin het kindje veilig zit?", "Vruchtvliezen met vruchtwater",
      ["Placenta met vruchtwater", "Navelstreng met bloed", "Baarmoederwand met vruchtwater"],
      "De zak bestaat uit vruchtvliezen, waarin het vruchtwater zit."),
    M("Hoe heet het kindje vanaf twaalf weken zwangerschap?", "Foetus", ["Embryo", "Bevruchte eicel", "Eicel"],
      "Aan het einde van de embryonale fase is het kindje een foetus: het groeit alleen nog."),
    M("Wat is een wee?", "Het samentrekken van de baarmoeder",
      ["Het breken van de vruchtvliezen", "Het dichtknijpen van de navelstreng", "Het indalen van het hoofdje"],
      "Het samentrekken van de spieren van de baarmoeder noem je een wee."),
    M("Hoe heet het als bij de geboorte de billen eerst geboren worden?", "Stuitligging",
      ["Dwarsligging", "Indaling", "Nageboorte"],
      "Bij een stuitligging komen de billen eerst; bij een dwarsligging ligt de baby dwars."),
    M("Wat is de navel?", "Het litteken van de afgevallen navelstreng",
      ["Het stompje van de placenta", "De opening van de baarmoedermond", "Het litteken van een keizersnede"],
      "Het stompje navelstreng valt na een paar dagen af; het litteken is de navel."),
    M("Waarom moet een zwangere vrouw vaker naar de wc?", "De urineblaas heeft minder ruimte",
      ["De foetus drukt op de maag", "De nieren maken door progesteron meer urine", "De placenta geeft urine af aan de blaas"],
      "Door de groeiende foetus komen de organen in de verdrukking; de urineblaas heeft geen ruimte meer voor veel urine."),
    W("Aan het einde van de embryonale fase zijn alle organen aangelegd.", True,
      "Waar. Daarna groeit het kindje alleen nog en heet het een foetus."),
    W("In de eerste twaalf weken van de zwangerschap heet het ongeboren kind een foetus.", False,
      "Niet waar. In de eerste twaalf weken is het een embryo; daarna heet het een foetus."),
    W("In de eerste twaalf weken van de zwangerschap is aan de buik van de vrouw al duidelijk iets te zien.", False,
      "Niet waar. Aan de buik is in de eerste twaalf weken niet veel te zien; pas rond twintig weken wordt de buik dikker."),
    W("In de placenta lopen de bloedvaten van de foetus dicht langs de bloedvaten van de moeder.", True,
      "Waar. De wanden zijn zo dun dat hier stoffen kunnen worden uitgewisseld."),
    W("Het vruchtwater beschermt het kindje tegen stoten.", True,
      "Waar. De vruchtvliezen met vruchtwater beschermen het embryo en de foetus tegen stoten."),
    I("Het kind is via de ____ verbonden met de placenta.", "navelstreng|de navelstreng",
      "De navelstreng verbindt de foetus met de placenta."),
    I("De zak met vruchtvliezen is gevuld met ____.", "vruchtwater|het vruchtwater",
      "In de vruchtvliezen zit het vruchtwater."),
    I("Het extra ____ in de borsten van een zwangere vrouw beschermt de melkklieren.", "vet",
      "De borsten worden groter door de groei van melkklieren en door extra vet."),
    I("Een andere naam voor de placenta is de ____.", "moederkoek|de moederkoek",
      "Placenta en moederkoek zijn twee namen voor hetzelfde orgaan."),
    O("Noem twee klachten die een zwangere vrouw kan krijgen doordat de foetus steeds groter wordt.",
      ["maagzuur/oprispen", "wc/plassen/urineblaas/urine"], 2,
      "Ze kan last krijgen van oprispend maagzuur en moet vaker naar de wc, omdat de urineblaas minder ruimte heeft voor urine.",
      "De organen in de buik komen in de verdrukking."),
    O("Hoe is het ongeboren kind in de baarmoeder beschermd tegen stoten?",
      ["vruchtvlies/vruchtvliezen", "vruchtwater"], 2,
      "Het kindje zit in een zak van vruchtvliezen die gevuld is met vruchtwater; die beschermen tegen stoten.",
      "Het gaat om de zak rond het kindje."),
]),
13: ("Functies en processen", "👶", [
    M("Wat gaat door de navelstrengader?", "Zuurstof en voedsel van moeder naar kind",
      ["Afvalstoffen van het kind naar de moeder", "Zuurstof van het kind naar de moeder", "Voedingsstoffen van het kind naar de placenta"],
      "Via de navelstrengader gaan alle stoffen die het kind nodig heeft van de moeder naar het kind."),
    M("Wat vervoeren de twee navelstrengslagaders?", "Afvalstoffen van het kind naar de moeder",
      ["Zuurstof van de moeder naar het kind", "Voedingsstoffen van de moeder naar het kind", "Hormonen van de moeder naar de melkklieren"],
      "De navelstrengslagaders voeren afvalstoffen van het kind af naar de moeder."),
    M("Waardoor kunnen stoffen in de placenta worden uitgewisseld?", "De wanden van de bloedvaten zijn zo dun",
      ["Het bloed van moeder en kind mengt zich", "De navelstreng is daar open", "De bloedvaten van het kind eindigen in de baarmoeder"],
      "In de placenta lopen de bloedvaten dicht langs elkaar en hun wanden zijn zo dun dat stoffen kunnen worden uitgewisseld."),
    M("Wat doet de placenta met schadelijke stoffen?", "Ze houdt veel schadelijke stoffen tegen",
      ["Ze laat alle schadelijke stoffen door", "Ze houdt alle schadelijke stoffen tegen, ook alcohol", "Ze breekt schadelijke stoffen af tot voedsel"],
      "De placenta werkt als filter, maar alcohol, drugs, het rodehondvirus en nicotine komen toch door."),
    M("Wat gebeurt er tijdens de ontsluiting?", "De baarmoedermond gaat open door weeën",
      ["De placenta wordt naar buiten geduwd", "De baby wordt door persweeën naar buiten geduwd", "Het hoofdje draait naar beneden"],
      "Bij de ontsluiting gaat de baarmoedermond open; het vruchtwater loopt vlak voor of tijdens de ontsluiting weg."),
    M("Wanneer begint de uitdrijving?", "Als de baarmoedermond open is",
      ["Zodra de vruchtvliezen breken", "Zodra de navelstreng is doorgeknipt", "Zes weken voor de geboorte"],
      "Als de baarmoedermond ver genoeg open is, duwen persweeën de baby naar buiten."),
    M("Wat komt er tijdens de nageboorte naar buiten?", "De placenta met vruchtvliezen en resten van de navelstreng",
      ["De baby met het vruchtwater", "Alleen het vruchtwater", "De baarmoeder met de eierstokken"],
      "Na de geboorte van de baby duwen weeën de placenta, vruchtvliezen en navelstrengresten naar buiten."),
    M("Wanneer doet een arts een keizersnede?", "Bij een dwarsligging van de baby",
      ["Bij een baby die met het hoofdje naar beneden ligt", "Bij indalingsweeën", "Bij elke eerste bevalling"],
      "Bij een dwarsligging kan de baby niet via de vagina geboren worden; een keizersnede is dan nodig."),
    M("Waarom maakt de verloskundige snel het mondje van de baby schoon?", "De baby gaat zelf ademen",
      ["De baby krijgt dan zijn eerste voeding", "Het vruchtwater moet uit de vagina lopen", "De navelstreng moet dichtgeknepen worden"],
      "Zo gauw de baby geboren is, gaat hij zelf ademen."),
    W("De indalingsweeën beginnen gemiddeld zes weken voor de bevalling.", True,
      "Waar. Vanaf ongeveer zes weken voor de bevalling trekken de baarmoederspieren samen."),
    W("Bij de indaling ligt het hoofdje van de baby met het gezicht naar boven in de buik.", False,
      "Niet waar. Bij de indaling komt het kindje met het hoofdje naar beneden tegen de baarmoedermond aan te liggen."),
    W("Tijdens de bevalling komt de nageboorte vóór de uitdrijving.", False,
      "Niet waar. De volgorde is ontsluiting, uitdrijving en daarna de nageboorte."),
    W("Vlak voor of tijdens de ontsluiting breken de vruchtvliezen.", True,
      "Waar. Het vruchtwater loopt dan via de vagina naar buiten."),
    W("Een keizersnede is een operatie waarbij een chirurg een snee onder in de buik maakt.", True,
      "Waar. Zo haalt de arts de baby uit de buik."),
    I("De eerste weeën voor de bevalling heten ____.", "indalingsweeën|indalingsweeen|indalingswee",
      "Indalingsweeën zorgen dat de baby goed komt te liggen."),
    I("Door sterke ____ wordt de baby tijdens de uitdrijving naar buiten geduwd.", "persweeën|persweeen|perswee",
      "Persweeën duwen de baby door de vagina naar buiten."),
    I("Het litteken dat overblijft na het afvallen van het stompje navelstreng is de ____.", "navel|de navel",
      "Het stompje valt na een paar dagen af; het litteken is de navel."),
    I("Het opengaan van de baarmoedermond noem je ____.", "ontsluiting|de ontsluiting",
      "Door weeën gaat de baarmoedermond open: dat is de ontsluiting."),
    O("Beschrijf hoe het kind aan zuurstof komt en hoe het koolstofdioxide kwijtraakt.",
      ["placenta", "navelstreng", "ader", "slagader"], 3,
      "Zuurstof gaat vanuit het bloed van de moeder in de placenta door de navelstrengader naar het kind; koolstofdioxide gaat via de twee navelstrengslagaders naar de placenta en de moeder.",
      "Denk aan de drie bloedvaten in de navelstreng."),
    O("Noem de drie fasen van de bevalling in de juiste volgorde.",
      ["ontsluiting", "uitdrijving", "nageboorte"], 3,
      "Eerst de ontsluiting, dan de uitdrijving en daarna de nageboorte.",
      "De baby komt in de tweede fase naar buiten."),
]),
14: ("Toepassen en redeneren", "🧬", [
    M("Een vrouw is acht weken zwanger. In welke fase zit het kindje?", "De embryonale fase, waarin de organen ontstaan",
      ["De foetale fase, waarin het kind alleen nog groeit", "De indalingsfase, vlak voor de bevalling", "De nageboortefase, vlak na de bevalling"],
      "De eerste twaalf weken vormen de embryonale fase."),
    M("Een zwangere vrouw drinkt regelmatig alcohol. Welk gevolg kan dit voor het kind hebben?", "De hersenen groeien niet goed (FAS)",
      ["Het kind groeit sneller en wordt groter", "Alleen de moeder wordt er ziek van", "Het kind krijgt rodehond"],
      "Alcohol komt via de placenta bij het kind en kan leiden tot Foetaal Alcohol Syndroom."),
    M("Waarom is rodehond vooral gevaarlijk voor ongeboren kinderen?", "Het virus komt via de placenta bij het embryo",
      ["Het virus wordt door de placenta tegengehouden", "Het virus komt pas bij de bevalling bij het kind", "Rodehond is altijd gevaarlijk, ook voor volwassenen"],
      "Voor volwassenen is rodehond niet gevaarlijk; het virus komt wel via de placenta bij het kind, met oogafwijkingen en gehoorverlies als gevolg."),
    M("Welke bewering over een eeneiige tweeling is juist?", "Ze zijn altijd van hetzelfde geslacht",
      ["Ze zijn altijd een broer en een zus", "Ze komen uit twee eicellen en twee zaadcellen", "Ze lijken nooit op elkaar"],
      "Een eeneiige tweeling ontstaat uit één eicel en één zaadcel en lijkt sprekend op elkaar."),
    M("Hoe ontstaat een twee-eiige tweeling?", "Er komen bij de eisprong twee eicellen vrij die beide bevrucht worden",
      ["Een bevruchte eicel splitst zich in tweeën", "Een eicel wordt door twee zaadcellen tegelijk bevrucht", "Het embryo splitst zich na de geboorte"],
      "Bij een twee-eiige tweeling worden twee eicellen bevrucht, vaak doordat in beide eierstokken een eicel rijpt."),
    M("Waarom is er bij een meerlingzwangerschap meer risico op een te vroege geboorte?", "Er is minder ruimte voor elke baby",
      ["De placenta houdt dan meer stoffen tegen", "De navelstreng is dan korter", "De weeën beginnen altijd eerder"],
      "Met meer baby's in de baarmoeder is er minder ruimte per baby."),
    M("Waarom heeft de eicel van een zoogdier weinig reservevoedsel?", "Het embryo krijgt voedingsstoffen via het bloed van de moeder",
      ["De eicel heeft een harde kalkschaal nodig", "Het embryo groeit in een ei buiten het lichaam", "Een zoogdier legt veel eieren tegelijk"],
      "In de baarmoeder wisselt het embryo stoffen uit met het bloed van de moeder."),
    M("De placenta ligt voor de baarmoedermond. Wat doet de arts?", "Een keizersnede uitvoeren",
      ["Wachten tot de weeën beginnen", "De vruchtvliezen laten breken", "De navelstreng doorknippen"],
      "Ook als de placenta voor de baarmoedermond ligt, wordt een keizersnede uitgevoerd."),
    M("Welke klachten kan een vrouw in de eerste twaalf weken van de zwangerschap hebben?", "Moe en misselijk zijn en trek in ander eten",
      ["Een duidelijk dikkere buik en voelbare bewegingen", "Last van de weeën", "Een gebroken vruchtwater"],
      "In de eerste twaalf weken is aan de buik weinig te zien, maar ze kan zich moe en misselijk voelen."),
    W("Rodehond is voor een zwangere vrouw zelf gevaarlijk en voor het ongeboren kind niet.", False,
      "Niet waar. Juist andersom: de ziekte is niet gevaarlijk, behalve voor ongeboren kinderen."),
    W("Een eeneiige tweeling lijkt sprekend op elkaar.", True,
      "Waar. Ze ontstaan uit dezelfde bevruchte eicel."),
    W("Bij een twee-eiige tweeling zijn er altijd twee placenta's.", True,
      "Waar. Elk embryo heeft ook zijn eigen vruchtvliezen."),
    W("De placenta houdt nicotine uit sigaretten tegen, zodat het embryo er geen last van heeft.", False,
      "Niet waar. Nicotine, alcohol, drugs en het rodehondvirus komen wel via de placenta bij het embryo."),
    W("Een twee-eiige tweeling kan bestaan uit een broer en een zus.", True,
      "Waar. Ze komen uit twee verschillende eicellen en zaadcellen."),
    I("Een tweeling uit één bevruchte eicel heet een ____ tweeling.", "eeneiige|eeneiig",
      "Een eeneiige tweeling ontstaat uit één eicel en één zaadcel."),
    I("Als het embryo sterft en wordt afgestoten, heet dat een ____.", "miskraam|een miskraam",
      "Dit gebeurt bij een op de tien zwangerschappen in de eerste twaalf weken."),
    I("Alcohol tijdens de zwangerschap kan leiden tot Foetaal Alcohol ____ (FAS).", "syndroom",
      "FAS staat voor Foetaal Alcohol Syndroom."),
    I("In een vogelei zit het reservevoedsel in de eicel: dit noem je de ____ (eigeel).", "dooier|de dooier",
      "De dooier is de eigenlijke eicel en bevat het voedsel voor het embryo."),
    O("Leg uit waarom een zwangere vrouw geen alcohol mag drinken.",
      ["placenta", "hersenen"], 2,
      "Alcohol komt via de placenta bij het kind. De hersenen groeien dan niet goed (FAS) en het kind kan een verstandelijke beperking krijgen.",
      "Denk aan het filter tussen moeder en kind."),
    O("Leg uit waarom de eicel van een zoogdier veel minder reservevoedsel heeft dan een kippenei.",
      ["baarmoeder", "bloed", "uitwisseling/voedingsstoffen"], 2,
      "Een zoogdierembryo groeit in de baarmoeder en krijgt voedingsstoffen via uitwisseling met het bloed van de moeder; een kippenei bevat al het voedsel zelf.",
      "Kijk waar het embryo groeit."),
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_3')
    vragen = plaats([dict(v) for v in ONDERWERP_VRAGEN], rng)
    onderwerp = {
        "id": "bio-h11-3-zwangerschap", "hoofdstuk": 11, "paragraaf": "11.3",
        "titel": "Zwangerschap",
        "korteUitleg": "Embryo en foetus, placenta en navelstreng, schadelijke stoffen, de drie fasen van de bevalling en tweelingen.",
        "icoon": "🤰", "kleur": "h11-thema", "theorie": THEORIE, "vragen": vragen,
    }
    schrijf(os.path.join(ROOT, 'h11_3.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 Voortplanting §11.3) — gegenereerd door tools/gen_biologie_h11_3.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-biologie-{nr}", "hoofdstuk": 11, "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
              "paragraaf": "11.3", "titel": f"Toets {nr} — §11.3 {sub}", "vak": "Biologie · HAVO 3 (H11.3)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 §11.3) — gegenereerd door tools/gen_biologie_h11_3.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
