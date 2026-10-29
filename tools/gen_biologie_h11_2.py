#!/usr/bin/env python3
"""Biologie HAVO 3 · Hoofdstuk 11 Voortplanting · §11.2 Bevruchting (boek p. 134–138).
Schrijft havo3/biologie/js/data/h11_2.js (onderwerp) + examen_9…11.js (ex-h3-biologie-9…11).
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
<h3>11.2 Bevruchting</h3>
<h4>Hoe ontstaat een zwangerschap?</h4>
<p>Als een man tijdens de geslachtsgemeenschap klaarkomt, komt er ongeveer 3 mL <b>sperma</b> in de <b>vagina</b>, vlak bij de <b>baarmoedermond</b>. In het sperma zitten 20 tot 300 miljoen <b>zaadcellen</b>. Die zwemmen via de baarmoeder de <b>eileiders</b> binnen en kunnen daar enkele dagen overleven.</p>
<p>Als de vrouw net een <b>eisprong</b> heeft gehad, kunnen de zaadcellen in de eileider een rijpe <b>eicel</b> tegenkomen. De kop van een zaadcel dringt de eicel binnen. De kern van de zaadcel versmelt met de kern van de eicel en er ontstaat één nieuwe kern.</p>
<div class="formule-box"><b>Bevruchting</b> = het versmelten van de kern van een zaadcel met de kern van een eicel.</div>
<p>Nadat een zaadcel de eicel is binnengedrongen, wordt de buitenste laag van de eicel <b>ondoordringbaar</b> voor andere zaadcellen. Zo kan maar één zaadcel de eicel bevruchten.</p>

<h4>Wat gebeurt er na de bevruchting?</h4>
<ul>
  <li>De <b>bevruchte eicel</b> begint direct te delen: twee cellen, dan vier cellen, enzovoort.</li>
  <li>Zo ontstaat een <b>bolletje van cellen</b> dat naar de baarmoeder gaat.</li>
  <li>Na ongeveer zes dagen zet het bolletje zich vast in het baarmoederslijmvlies. Dat heet <b>innesteling</b>. Het bolletje cellen noem je nu een <b>embryo</b>.</li>
</ul>
<div class="info-box tip"><span class="kop">Vanaf wanneer ben je zwanger?</span>
<p>Vanaf de innesteling is de vrouw <b>zwanger</b>. Ze wordt dan niet meer ongesteld. Met een <b>zwangerschapstest</b> kan ze zeker weten of ze zwanger is.</p></div>

<h3>Hoe voorkom je een zwangerschap?</h3>
<p>Met een <b>voorbehoedmiddel</b> (anticonceptiemiddel) kunnen mensen voorkomen dat een vrouw zwanger wordt. Een goed voorbehoedmiddel voldoet aan drie eisen:</p>
<ol>
  <li>het voorkomt zwangerschap;</li>
  <li>het is makkelijk in gebruik;</li>
  <li>het is niet schadelijk voor je gezondheid.</li>
</ol>
<table class="nask"><tr><th>middel</th><th>werking</th></tr>
<tr><td><b>Condoom</b></td><td>Zaadcellen kunnen niet bij de eicel komen. Het <b>enige</b> voorbehoedmiddel dat ook beschermt tegen <b>soa's</b>.</td></tr>
<tr><td><b>Pil</b></td><td>Bevat de hormonen <b>oestrogeen</b> en <b>progesteron</b>: geen eicellen rijpen, geen eisprong; het slijm bij de baarmoedermond wordt dikker.</td></tr>
<tr><td><b>Anticonceptiepleister</b> en <b>hormoonstaafje</b></td><td>Geven hormonen af die de eisprong tegenhouden. De pleister plak je op de huid, het staafje zit onder de huid.</td></tr>
<tr><td><b>Spiraaltje</b></td><td>Wordt door een arts in de baarmoeder geplaatst. Maakt zaadcellen minder vruchtbaar en voorkomt dat een bevruchte eicel zich innestelt.</td></tr>
<tr><td><b>Sterilisatie</b></td><td>Doorsnijden van de zaadleiders (man) of eileiders (vrouw). Definitief.</td></tr></table>
<div class="info-box let-op"><span class="kop">Onbetrouwbare methoden</span>
<ul>
  <li><b>Coïtus interruptus</b>: de man trekt zijn penis terug voordat hij klaarkomt. Onbetrouwbaar, want in het <b>voorvocht</b> kunnen al zaadcellen zitten.</li>
  <li><b>Periodieke onthouding</b>: geen geslachtsgemeenschap in de vruchtbare periode. Onbetrouwbaar, want de eisprong is moeilijk te bepalen en hoeft niet op de 14e dag te zijn.</li>
</ul></div>

<h3>Wat kun je doen bij een noodgeval?</h3>
<ul>
  <li>Een vrouw die de pil vergeet, is niet beschermd. In de <b>bijsluiter</b> staat wat ze dan moet doen.</li>
  <li>Na seks zonder voorbehoedmiddel kan ze een <b>morning-afterpil</b> halen bij de drogist of apotheek. Die onderdrukt de ovulatie en voorkomt innesteling. Binnen <b>72 uur</b> innemen; hoe eerder, hoe kleiner de kans op zwangerschap. Mogelijke bijwerkingen: overgeven en buikpijn.</li>
  <li>Is de vrouw toch zwanger, dan kan een arts in een abortuskliniek het embryo laten verwijderen: een <b>abortus</b>. Dat mag alleen als de vrouw niet langer dan <b>24 weken</b> zwanger is.</li>
</ul>

<h3>Hoe ontstaat een embryo precies?</h3>
<ul>
  <li>Ongeveer vijf dagen na de bevruchting ontstaat in het bolletje cellen een <b>holte</b>. Binnenin zit een groepje cellen: de <b>kiemschijf</b>. Daaruit ontstaat het embryo.</li>
  <li>De buitenste cellen vormen uitstulpingen: <b>vlokken</b>. Die groeien in het baarmoederslijmvlies, nemen voedingsstoffen en zuurstof op uit het bloed van de moeder en geven afvalstoffen terug. Later worden ze de <b>placenta</b>.</li>
  <li>Tussen de vlokken en de kiemschijf ontstaat een <b>steel</b>, die later de <b>navelstreng</b> wordt.</li>
</ul>
<div class="formule-box">De vlokken maken het zwangerschapshormoon <b>HCG</b>: (1) het voorkomt dat er een nieuwe eicel gaat rijpen en (2) het zorgt dat het baarmoederslijmvlies niet wordt afgestoten.</div>
<p>Een zwangerschapstest toont HCG aan in de <b>urine</b>.</p>

<h3>Toepassen: ivf</h3>
<p>Sommige vrouwen kunnen niet zwanger worden, bijvoorbeeld omdat hun eileiders verstopt zijn. Bij <b>ivf</b> (<b>in-vitrofertilisatie</b>, letterlijk: bevruchting in glas) worden de eicellen buiten het lichaam bevrucht. Een baby die zo ontstaat heet ook wel <b>reageerbuisbaby</b>.</p>
<ol>
  <li>Door hormonen rijpen meerdere eicellen tegelijk.</li>
  <li>De arts haalt rijpe eicellen uit de eierstokken.</li>
  <li>De eicellen worden met zaadcellen in een schaaltje met voedingsstoffen gedaan.</li>
  <li>Enkele eicellen worden bevrucht en groeien uit tot een bolletje cellen.</li>
  <li>De arts brengt maximaal twee bolletjes cellen in de baarmoeder. Ongeveer 1 op de 3 groeit uit tot een baby.</li>
</ol>
"""

BEGRIPPEN = [
    ("bevruchting", "Het versmelten van de kern van een zaadcel met de kern van een eicel."),
    ("zaadcel", "Mannelijke geslachtscel die via de baarmoeder naar de eileider zwemt en daar de eicel kan bevruchten."),
    ("eicel", "Vrouwelijke geslachtscel die na de eisprong in de eileider door een zaadcel bevrucht kan worden."),
    ("sperma", "Vocht met 20 tot 300 miljoen zaadcellen dat bij een zaadlozing in de vagina komt."),
    ("innesteling", "Het vastzetten van het bolletje cellen in het baarmoederslijmvlies, ongeveer zes dagen na de bevruchting."),
    ("embryo", "Het bolletje cellen vanaf de innesteling in het baarmoederslijmvlies."),
    ("voorbehoedmiddel", "Middel waarmee je voorkomt dat een vrouw zwanger wordt."),
    ("condoom", "Voorbehoedmiddel dat zaadcellen bij de eicel weghoudt en als enige ook beschermt tegen soa's."),
    ("pil", "Voorbehoedmiddel met oestrogeen en progesteron dat de rijping van eicellen en de eisprong voorkomt."),
    ("spiraaltje", "Door een arts in de baarmoeder geplaatst middel dat zaadcellen minder vruchtbaar maakt en innesteling voorkomt."),
    ("sterilisatie", "Het definitief doorsnijden van de zaadleiders of eileiders tijdens een operatie."),
    ("morning-afterpil", "Pil die de ovulatie onderdrukt en innesteling voorkomt als je hem binnen 72 uur na seks zonder voorbehoedmiddel inneemt."),
    ("abortus", "Het door een arts laten verwijderen van het embryo uit de baarmoeder (alleen tot 24 weken zwangerschap)."),
    ("kiemschijf", "Groepje cellen in de holte van het bolletje cellen waaruit het embryo ontstaat."),
    ("vlokken", "Uitstulpingen van de buitenste cellen die in het baarmoederslijmvlies groeien en later de placenta worden."),
    ("HCG", "Zwangerschapshormoon van de vlokken dat een nieuwe eirijping en het afstoten van het baarmoederslijmvlies voorkomt."),
    ("ivf", "In-vitrofertilisatie: bevruchting van eicellen buiten het lichaam, in een schaaltje."),
]

ONDERWERP_VRAGEN = [
    {"type": "mc", "niveau": 1, "vraag": "Wat is bevruchting?",
     "_goed": "Het versmelten van de kern van een zaadcel met de kern van een eicel",
     "_fout": ["Het vastzetten van een bolletje cellen in het baarmoederslijmvlies", "Het naar buiten komen van een rijpe eicel uit de eierstok", "Het binnendringen van zaadcellen in de baarmoedermond"],
     "uitleg": "Bevruchting is het versmelten van de kernen van zaadcel en eicel; zo ontstaat één nieuwe kern.",
     "hint": "Wat versmelt er precies?"},
    {"type": "mc", "niveau": 1, "vraag": "Waar komt een zaadcel normaal gesproken de rijpe eicel tegen?",
     "_goed": "In de eileider", "_fout": ["In de vagina", "In de baarmoedermond", "In de eierstok"],
     "uitleg": "De zaadcellen zwemmen via de baarmoeder de eileiders in; daar vindt de bevruchting plaats.",
     "hint": "Waar zwemmen de zaadcellen naartoe?"},
    {"type": "mc", "niveau": 2, "vraag": "Waarom kan maar één zaadcel een eicel bevruchten?",
     "_goed": "De buitenste laag van de eicel wordt ondoordringbaar",
     "_fout": ["De eicel sluit zich af met slijm uit de baarmoeder", "De andere zaadcellen overleven in de eileider niet", "De eicel is te klein voor meer zaadcellen"],
     "uitleg": "Na het binnendringen van één zaadcel wordt de buitenste laag van de eicel ondoordringbaar voor andere zaadcellen.",
     "hint": "Wat verandert er aan de eicel nadat de eerste zaadcel binnen is?"},
    {"type": "mc", "niveau": 2, "vraag": "Wat is het enige voorbehoedmiddel dat ook beschermt tegen soa's?",
     "_goed": "Het condoom", "_fout": ["De pil", "Het spiraaltje", "Het hormoonstaafje"],
     "uitleg": "Alleen een condoom beschermt ook tegen soa's; de andere middelen voorkomen alleen zwangerschap.",
     "hint": "Het middel houdt de zaadcellen buiten het lichaam."},
    {"type": "mc", "niveau": 3, "vraag": "Een vrouw plakt een anticonceptiepleister op haar huid. Hoe voorkomt dat een zwangerschap?",
     "_goed": "De pleister geeft hormonen af die de eisprong tegenhouden",
     "_fout": ["De pleister sluit de eileiders van binnenuit af", "De pleister doodt de zaadcellen in de vagina", "De pleister voorkomt dat het embryo groeit"],
     "uitleg": "De pleister geeft hormonen af die de eisprong tegenhouden; zonder eisprong is er geen eicel om te bevruchten.",
     "hint": "Denk aan hoe de pil werkt."},
    {"type": "waaronwaar", "niveau": 1, "vraag": "Een vrouw is zwanger vanaf het moment van de innesteling.",
     "antwoord": True, "uitleg": "Waar. Vanaf de innesteling is de vrouw zwanger en wordt ze niet meer ongesteld.",
     "hint": "Wanneer zet het bolletje cellen zich vast?"},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Coïtus interruptus is een betrouwbaar voorbehoedmiddel.",
     "antwoord": False, "uitleg": "Niet waar. Coïtus interruptus is erg onbetrouwbaar: in het voorvocht kunnen al zaadcellen zitten.",
     "hint": "Wat komt er vóór de zaadlozing al uit de penis?"},
    {"type": "waaronwaar", "niveau": 2, "vraag": "Het zwangerschapshormoon HCG zorgt ervoor dat het baarmoederslijmvlies wordt afgestoten.",
     "antwoord": False, "uitleg": "Niet waar. HCG zorgt er juist voor dat het baarmoederslijmvlies niet wordt afgestoten.",
     "hint": "Er komt geen menstruatie meer."},
    {"type": "invoer", "niveau": 1, "vraag": "Hoe heet het vastzetten van het bolletje cellen in het baarmoederslijmvlies?",
     "antwoord": "innesteling|de innesteling", "uitleg": "Dat heet innesteling; het bolletje cellen heet vanaf dan een embryo.",
     "hint": "Het begint met 'inn'."},
    {"type": "invoer", "niveau": 2, "vraag": "Hoe heet de behandeling waarbij eicellen buiten het lichaam worden bevrucht? Geef de afkorting.",
     "antwoord": "ivf|IVF", "uitleg": "Ivf staat voor in-vitrofertilisatie: bevruchting in glas.",
     "hint": "Drie letters."},
]

EXAMENS = {
9: ("Bevruchting en innesteling", "🧬", [
    M("Hoeveel zaadcellen zitten er ongeveer in het sperma bij één zaadlozing?", "20 tot 300 miljoen", ["2 tot 30 miljoen", "20 tot 300 duizend", "200 tot 3000 miljoen"],
      "In het sperma zitten 20 tot 300 miljoen zaadcellen."),
    M("Hoeveel sperma komt er ongeveer in de vagina als een man klaarkomt?", "Ongeveer 3 mL", ["Ongeveer 30 mL", "Ongeveer 0,3 mL", "Ongeveer 300 mL"],
      "Er komt ongeveer 3 mL sperma in de vagina, vlak bij de baarmoedermond."),
    M("Hoe lang kunnen zaadcellen in de eileider overleven?", "Enkele dagen", ["Enkele uren", "Enkele weken", "Precies één dag"],
      "Zaadcellen kunnen in de eileider enkele dagen overleven."),
    M("Wat ontstaat er door het versmelten van de kernen van zaadcel en eicel?", "Eén nieuwe kern", ["Twee gelijke kernen", "Een kern met een dubbele wand", "Een kern zonder erfelijke eigenschappen"],
      "De kern van de zaadcel versmelt met de kern van de eicel en er ontstaat één nieuwe kern."),
    M("Hoe heet het bolletje cellen vanaf de innesteling?", "Embryo", ["Kiemschijf", "Placenta", "Bevruchte eicel"],
      "Na de innesteling noem je het bolletje cellen een embryo."),
    M("Hoeveel dagen na de bevruchting vindt de innesteling ongeveer plaats?", "Ongeveer zes dagen", ["Ongeveer één dag", "Ongeveer twee weken", "Ongeveer zes weken"],
      "Na ongeveer zes dagen zet het bolletje cellen zich vast in het baarmoederslijmvlies."),
    M("Hoeveel cellen heeft de bevruchte eicel na de eerste deling?", "Twee cellen", ["Eén cel", "Vier cellen", "Acht cellen"],
      "Eerst ontstaan er twee cellen, die delen weer en worden vier cellen, enzovoort."),
    M("Welk deel van de zaadcel dringt de eicel binnen?", "De kop van de zaadcel", ["De staart van de zaadcel", "De hele zaadcel inclusief staart", "Alleen het celmembraan van de zaadcel"],
      "De kop van de zaadcel dringt de eicel binnen; daar zit de kern in."),
    M("Wanneer kunnen zaadcellen in de eileider een eicel bevruchten?", "Kort na een eisprong, als er een rijpe eicel is", ["Tijdens de menstruatie, als het slijmvlies loskomt", "Direct na de innesteling van een embryo", "Als de eierstokken geen eicellen meer rijpen"],
      "Alleen als de vrouw net een eisprong heeft gehad, kunnen de zaadcellen een rijpe eicel tegenkomen."),
    W("Het sperma komt tijdens de geslachtsgemeenschap vlak bij de baarmoedermond terecht.", True,
      "Waar. Bij het klaarkomen komt het sperma in de vagina, vlak bij de baarmoedermond."),
    W("Bij de bevruchting versmelten twee hele cellen tot één cel met twee kernen.", False,
      "Niet waar. Alleen de kernen versmelten; daardoor ontstaat één nieuwe kern."),
    W("De innesteling vindt plaats in de eileider.", False,
      "Niet waar. Het bolletje cellen zet zich vast in het baarmoederslijmvlies, dus in de baarmoeder."),
    W("Doordat de cellen blijven delen, ontstaat een bolletje cellen dat naar de baarmoeder gaat.", True,
      "Waar. De bevruchte eicel deelt steeds opnieuw; het bolletje cellen beweegt naar de baarmoeder."),
    W("Vanaf de innesteling wordt de vrouw niet meer ongesteld.", True,
      "Waar. Vanaf de innesteling is de vrouw zwanger en ze wordt niet meer ongesteld."),
    I("Het versmelten van de kernen van een zaadcel en een eicel heet ____.", "bevruchting|de bevruchting",
      "Het versmelten van de kernen is de bevruchting."),
    I("De zaadcellen zwemmen via de baarmoeder naar de ____, waar ze een rijpe eicel kunnen tegenkomen.", "eileider|eileiders|de eileiders|de eileider",
      "In de eileider vindt de bevruchting plaats."),
    I("Na de innesteling heet het bolletje cellen een ____.", "embryo|een embryo|het embryo",
      "Vanaf de innesteling noem je het bolletje cellen een embryo."),
    I("Een zwangere vrouw wordt niet meer ____.", "ongesteld",
      "Na de innesteling is er geen menstruatie meer."),
    O("Een zaadlozing bevat 20 tot 300 miljoen zaadcellen, maar slechts één zaadcel bevrucht de eicel. Beschrijf de weg die de zaadcellen afleggen en wat er gebeurt als er een zaadcel bij de eicel is.",
      ["vagina", "baarmoeder", "eileider", "kern"], 3,
      "De zaadcellen komen in de vagina en zwemmen via de baarmoeder de eileiders in. Daar dringt de kop van een zaadcel een rijpe eicel binnen en versmelt de kern van de zaadcel met de kern van de eicel.",
      "Route: vagina, baarmoeder, eileider. Bij de bevruchting versmelten de kernen."),
    O("Beschrijf wat er met de bevruchte eicel gebeurt vanaf de bevruchting tot en met de innesteling.",
      ["delen", "bolletje", "baarmoeder", "zes dagen", "slijmvlies"], 3,
      "De bevruchte eicel begint te delen: twee cellen, vier cellen, enzovoort. Er ontstaat een bolletje cellen dat naar de baarmoeder gaat. Na ongeveer zes dagen zet het zich vast in het baarmoederslijmvlies.",
      "Deling, bolletje cellen, naar de baarmoeder, na ongeveer zes dagen innesteling in het slijmvlies."),
]),
10: ("Voorbehoedmiddelen en noodgevallen", "💊", [
    M("Welke eigenschap is GEEN eis voor een goed voorbehoedmiddel?", "Het wordt door een arts geplaatst", ["Het voorkomt zwangerschap", "Het is makkelijk in gebruik", "Het is niet schadelijk voor je gezondheid"],
      "De drie eisen zijn: het voorkomt zwangerschap, het is makkelijk in gebruik en het is niet schadelijk voor je gezondheid."),
    M("Welke hormonen bevat de pil?", "Oestrogeen en progesteron", ["Testosteron en oestrogeen", "HCG en progesteron", "HCG en testosteron"],
      "De pil bevat de hormonen oestrogeen en progesteron."),
    M("Wat gebeurt er door de pil met het slijm bij de baarmoedermond?", "Het wordt dikker", ["Het wordt dunner", "Het wordt zuurder", "Het verdwijnt helemaal"],
      "Het slijm wordt dikker, zodat zaadcellen moeilijker de baarmoeder in komen."),
    M("Wie plaatst een spiraaltje in de baarmoeder?", "Een arts", ["De vrouw zelf", "Een apotheker", "Een drogist"],
      "Een spiraaltje wordt door een arts in de baarmoeder geplaatst."),
    M("Wat is het gevolg van sterilisatie bij een man?", "Er komen geen zaadcellen meer voor in het sperma", ["Er worden geen zaadcellen meer gemaakt", "Het sperma komt niet meer naar buiten", "Er komt geen voorvocht meer"],
      "De zaadleiders zijn doorgesneden, dus er komen geen zaadcellen meer in het sperma."),
    M("Waarom is periodieke onthouding onbetrouwbaar?", "De eisprong is moeilijk precies te bepalen", ["De eisprong is altijd op de 14e dag", "Zaadcellen sterven direct na de zaadlozing", "Het voorvocht bevat altijd zaadcellen"],
      "De eisprong hoeft niet op de 14e dag te zijn en kan vroeger of later komen."),
    M("Binnen hoeveel tijd na seks moet je de morning-afterpil innemen om waarschijnlijk niet zwanger te worden?", "Binnen 72 uur", ["Binnen 24 uur", "Binnen 7 dagen", "Binnen 2 weken"],
      "Binnen 72 uur; hoe eerder, hoe kleiner de kans op zwangerschap."),
    M("Welke bijwerkingen kan de morning-afterpil soms geven?", "Overgeven en buikpijn", ["Haaruitval en een droge huid", "Koorts en keelpijn", "Spierpijn en jeuk"],
      "Soms geeft de morning-afterpil bijwerkingen zoals overgeven en buikpijn."),
    M("Tot hoeveel weken zwangerschap mag een abortus?", "Niet langer dan 24 weken", ["Niet langer dan 12 weken", "Niet langer dan 36 weken", "Niet langer dan 8 weken"],
      "Abortus mag alleen als de vrouw niet langer dan 24 weken zwanger is."),
    W("Een spiraaltje voorkomt dat een bevruchte eicel zich vastzet in het baarmoederslijmvlies.", True,
      "Waar. Daardoor kan de bevruchte eicel niet uitgroeien tot een kind."),
    W("Bij sterilisatie bij de vrouw worden de eierstokken verwijderd.", False,
      "Niet waar. Bij sterilisatie worden de eileiders doorgesneden, zodat zaadcellen niet meer bij de eicel kunnen komen."),
    W("Een vrouw die één keer de pil vergeet, is nog steeds volledig beschermd tegen zwangerschap.", False,
      "Niet waar. Als je de pil vergeet, ben je niet beschermd tegen zwangerschap."),
    W("Het hormoonstaafje wordt onder de huid geplaatst en geeft hormonen af die een eisprong voorkomen.", True,
      "Waar. Het staafje zit onder de huid en geeft hormonen af."),
    W("Sterilisatie is definitief, daarom kiezen mensen er meestal pas voor als ze geen kinderen (meer) willen.", True,
      "Waar. Sterilisatie kun je niet zomaar terugdraaien."),
    I("Het enige voorbehoedmiddel dat ook beschermt tegen soa's is het ____.", "condoom|het condoom",
      "Alleen het condoom beschermt ook tegen soa's."),
    I("Het doorsnijden van de zaadleiders of de eileiders heet ____.", "sterilisatie|de sterilisatie",
      "Dat is sterilisatie."),
    I("Het door een arts laten weghalen van het embryo uit de baarmoeder heet een ____.", "abortus|een abortus",
      "Dat heet een abortus; dat mag tot 24 weken zwangerschap."),
    I("Vóór de zaadlozing komt er al een beetje vocht uit de penis: het ____.", "voorvocht|het voorvocht",
      "In het voorvocht kunnen al zaadcellen zitten."),
    O("Leg uit hoe de pil een zwangerschap voorkomt.",
      ["rijp", "eisprong", "slijm"], 2,
      "De pil bevat hormonen waardoor er in de eierstokken geen eicellen rijpen en er geen eisprong plaatsvindt. Ook wordt het slijm bij de baarmoedermond dikker, zodat zaadcellen moeilijker de baarmoeder in komen.",
      "Geen rijpe eicellen en geen eisprong, plus dikker slijm bij de baarmoedermond."),
    O("Een vrouw heeft gisteren seks gehad zonder voorbehoedmiddel. Wat kan zij doen en hoe werkt dat?",
      ["morning", "72", "ovulatie/eisprong", "innesteling"], 3,
      "Ze kan een morning-afterpil nemen bij de drogist of apotheek, het liefst zo snel mogelijk en binnen 72 uur. Die onderdrukt de ovulatie en voorkomt de innesteling van de bevruchte eicel.",
      "Morning-afterpil binnen 72 uur; onderdrukt de ovulatie en voorkomt innesteling."),
]),
11: ("Embryo, HCG en ivf", "🔬", [
    M("Wat ontstaat er ongeveer vijf dagen na de bevruchting in het bolletje cellen?", "Een holte met daarin een kiemschijf", ["Een steel met daarin een navelstreng", "Een placenta met daarin bloedvaten", "Een kopje met daarin vlokken"],
      "In het bolletje cellen ontstaat een holte; binnenin zit een groepje cellen, de kiemschijf."),
    M("Uit welk deel van het bolletje cellen ontstaat het embryo?", "Uit de kiemschijf", ["Uit de vlokken", "Uit de steel", "Uit de holte"],
      "Uit de kiemschijf ontstaat het embryo."),
    M("Wat worden de vlokken later?", "De placenta", ["De navelstreng", "De kiemschijf", "Het vruchtwater"],
      "De vlokken worden later de placenta; daar worden stoffen uitgewisseld tussen moeder en kind."),
    M("Wat wordt de steel tussen de vlokken en de kiemschijf later?", "De navelstreng", ["De placenta", "De baarmoedermond", "Het baarmoederslijmvlies"],
      "De steel wordt later de navelstreng."),
    M("Welk zwangerschapshormoon maken de vlokken?", "HCG", ["Oestrogeen", "Progesteron", "Testosteron"],
      "De vlokken maken het zwangerschapshormoon HCG."),
    M("Wat toont een zwangerschapstest aan?", "HCG in de urine", ["Oestrogeen in het bloed", "Progesteron in de urine", "Zaadcellen in de urine"],
      "De test toont aan of het zwangerschapshormoon HCG in de urine aanwezig is."),
    M("Wat is een effect van HCG op de eierstokken?", "Er rijpt geen nieuwe eicel", ["Er rijpen meerdere eicellen tegelijk", "De eisprong vindt eerder plaats", "De eierstokken maken extra zaadcellen"],
      "HCG voorkomt dat er een nieuwe eicel gaat rijpen."),
    M("Wat betekent ivf letterlijk?", "Bevruchting in glas", ["Bevruchting in de baarmoeder", "Voorkomen van een bevruchting", "Hormoonbehandeling van de eicel"],
      "Ivf is in-vitrofertilisatie: bevruchting (fertilisatie) in glas (vitro)."),
    M("Hoeveel bolletjes cellen brengt de arts bij ivf maximaal in de baarmoeder?", "Maximaal twee", ["Maximaal één", "Maximaal vier", "Alle bevruchte eicellen"],
      "Enkele dagen na de bevruchting brengt de arts maximaal twee bolletjes cellen in de baarmoeder."),
    W("De vlokken geven afvalstoffen terug aan het bloed van de moeder.", True,
      "Waar. De vlokken nemen voedingsstoffen en zuurstof op en geven afvalstoffen terug."),
    W("Bij ivf worden de eicellen in de baarmoeder van de vrouw bevrucht.", False,
      "Niet waar. De eicellen worden buiten het lichaam bevrucht, in een schaaltje."),
    W("Bij ivf groeit elk teruggeplaatst bolletje cellen uit tot een baby.", False,
      "Niet waar. Ongeveer 1 op de 3 bolletjes cellen groeit uit tot een baby."),
    W("In de placenta worden stoffen uitgewisseld tussen moeder en kind.", True,
      "Waar. In de placenta zitten bloedvaten van het kind en van de moeder."),
    W("Voor ivf krijgt de vrouw eerst een hormoonbehandeling waardoor meerdere eicellen tegelijk rijpen.", True,
      "Waar. Daardoor kan de arts meerdere rijpe eicellen uit de eierstokken halen."),
    I("In het bolletje cellen zit een groepje cellen waaruit het embryo ontstaat: de ____.", "kiemschijf|de kiemschijf",
      "Uit de kiemschijf ontstaat het embryo."),
    I("De uitstulpingen van de buitenste cellen van het bolletje cellen heten ____.", "vlokken|de vlokken",
      "De vlokken groeien in het baarmoederslijmvlies."),
    I("Het zwangerschapshormoon dat de vlokken maken heet ____.", "HCG|hcg",
      "De vlokken maken HCG."),
    I("Een baby die door ivf ontstaat heet ook wel een ____.", "reageerbuisbaby|een reageerbuisbaby",
      "Bij ivf gebeurt de bevruchting buiten het lichaam, vandaar de naam reageerbuisbaby."),
    O("Leg uit waarom een vrouw met verstopte eileiders met ivf toch zwanger kan worden.",
      ["buiten", "schaal", "baarmoeder"], 2,
      "Bij ivf worden de eicellen buiten het lichaam in een schaaltje bevrucht, dus de zaadcellen hoeven niet door de eileiders. Daarna brengt de arts bolletjes cellen in de baarmoeder, waar ze zich kunnen innestelen.",
      "Bevruchting buiten het lichaam in een schaaltje; daarna terugplaatsen in de baarmoeder."),
    O("Leg uit welke rol de vlokken spelen tijdens de eerste weken van de ontwikkeling van het embryo.",
      ["voedingsstoffen", "zuurstof", "afvalstoffen", "HCG", "placenta"], 3,
      "De vlokken groeien in het baarmoederslijmvlies. Ze nemen voedingsstoffen en zuurstof op uit het bloed van de moeder en geven afvalstoffen terug. Ze maken HCG en worden later de placenta.",
      "Stofuitwisseling met de moeder, HCG maken en later de placenta worden."),
]),
}


def schrijf(pad, kop, obj):
    with open(pad, 'w', encoding='utf-8') as f:
        f.write(kop)
        f.write(obj)


def main():
    rng = random.Random('bio_h11_2')
    vragen = plaats([dict(v) for v in ONDERWERP_VRAGEN], rng)
    onderwerp = {
        "id": "bio-h11-2-bevruchting", "hoofdstuk": 11, "paragraaf": "11.2",
        "titel": "Bevruchting",
        "korteUitleg": "Van zaadcel en eicel tot embryo: bevruchting, innesteling, voorbehoedmiddelen, HCG en ivf.",
        "kleur": "h11-thema", "icoon": "🧬", "theorie": THEORIE, "vragen": vragen,
    }
    schrijf(os.path.join(ROOT, 'h11_2.js'),
            "/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 Voortplanting §11.2) — gegenereerd door tools/gen_biologie_h11_2.py */\n",
            "DURU.register(" + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ");\n")
    for nr, (sub, icoon, vr) in EXAMENS.items():
        assert len(vr) == 20, (nr, len(vr))
        vr = plaats([dict(v) for v in vr], rng)
        n, tot = langste_aandeel(vr)
        assert n / tot <= 0.4, f"examen_{nr}: juiste optie {n}/{tot} keer langste"
        ex = {"id": f"ex-h3-biologie-{nr}", "hoofdstuk": 11, "hoofdstukTitel": "Hoofdstuk 11 — Voortplanting",
              "paragraaf": "11.2", "titel": f"Toets {nr} — §11.2 {sub}", "vak": "Biologie · HAVO 3 (H11.2)",
              "icoon": icoon, "duurMin": 20, "vragen": vr}
        schrijf(os.path.join(ROOT, f'examen_{nr}.js'),
                "/* Examen conform DURU ENGINE_SPEC (HAVO 3 Biologie · H11 §11.2) — gegenereerd door tools/gen_biologie_h11_2.py */\n",
                "DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(f"examen_{nr}: 20 vragen, juiste optie langste {n}/{tot}")


if __name__ == '__main__':
    main()
