#!/usr/bin/env python3
"""Nederlands HAVO 3 · Cursus 5 §5 Verwijzen (boek p. 214-215).
Schrijft havo3/nederlands/js/data/c5_5.js (onderwerp) + examen_44..50.js (proeftoetsen).
Vragen staan hieronder met het juiste antwoord eerst; het script schudt de mc-opties (seed 'c5_5')
zo dat de juiste-antwoordpositie per bestand de gate-regels 3 en 16 haalt."""
import json, os, random

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
DATA = os.path.join(ROOT, 'havo3', 'nederlands', 'js', 'data')
rng = random.Random('c5_5')


def MC(vraag, goed, fout, uitleg, **kw):
    return dict(type='mc', vraag=vraag, _goed=goed, _fout=fout, uitleg=uitleg, **kw)


def WO(vraag, antwoord, uitleg, **kw):
    assert uitleg.startswith('Waar.' if antwoord else 'Niet waar.'), vraag
    return dict(type='waaronwaar', vraag=vraag, antwoord=antwoord, uitleg=uitleg, **kw)


def IV(vraag, antwoord, uitleg):
    return dict(type='invul', vraag=vraag, antwoord=antwoord, uitleg=uitleg)


def IN(vraag, antwoord, uitleg, **kw):
    return dict(type='invoer', vraag=vraag, antwoord=antwoord, uitleg=uitleg, **kw)


def OP(vraag, sleutels, model, uitleg, minT=1):
    return dict(type='open', vraag=vraag, sleutelwoorden=sleutels, minTreffers=minT,
                modelantwoord=model, uitleg=uitleg)


def cyclisch(seq):
    for p in (2, 3, 4):
        if len(seq) >= 2 * p and all(seq[i] == seq[i % p] for i in range(len(seq))):
            return True
    return False


def plaats_antwoorden(vragen):
    """Schud mc-opties tot de verdeling van het juiste antwoord gate-proof is."""
    mcs = [v for v in vragen if v['type'] == 'mc']
    for _ in range(5000):
        pos = [rng.randrange(len(v['_fout']) + 1) for v in mcs]
        if mcs and max(pos.count(i) for i in range(4)) / len(pos) > 0.4:
            continue
        plus1 = sum(1 for a, b in zip(pos, pos[1:]) if b == (a + 1) % 4)
        if len(pos) > 1 and plus1 / (len(pos) - 1) >= 0.6:
            continue
        if cyclisch(pos):
            continue
        break
    for v, p in zip(mcs, pos):
        fout = v.pop('_fout')[:]
        rng.shuffle(fout)
        v['opties'] = fout[:p] + [v.pop('_goed')] + fout[p:]
        v['antwoord'] = p
    # volgorde van sleutels zoals in de bestaande bestanden
    uit = []
    for v in vragen:
        orde = ['type', 'niveau', 'vraag', 'opties', 'antwoord', 'sleutelwoorden', 'minTreffers',
                'modelantwoord', 'uitleg', 'hint']
        uit.append({k: v[k] for k in orde if k in v})
    return uit


def langste_check(naam, vragen):
    mcs = [v for v in vragen if v['type'] == 'mc']
    n = sum(1 for v in mcs if sorted(len(o) for o in v['opties'])[-1] == len(v['opties'][v['antwoord']])
            and [len(o) for o in v['opties']].count(len(v['opties'][v['antwoord']])) == 1)
    print(f'  {naam}: {len(vragen)} vragen, mc {len(mcs)}, juiste optie uniek langst {n}')


# ---------------------------------------------------------------- theorie
THEORIE = """
<h3>1. Verwijswoorden en het antecedent</h3>
<p><b>Verwijswoorden</b> wijzen terug naar een of meer woorden die eerder genoemd zijn. Het woord (of de woordgroep, of de hele zin) waarnaar een verwijswoord terugwijst, heet het <b>antecedent</b>. Het antecedent kan in dezelfde zin staan, maar ook in een zin ervoor.</p>
<div class="voorbeeld"><div class="vb-kop">Voorbeeld</div>
<p><i><b>Mijn opa en oma</b> zijn bang dat <u>zij</u> de trein naar Schiphol niet halen.</i> → <i>zij</i> verwijst naar het antecedent <i>mijn opa en oma</i>.</p></div>

<h3>2. Welk verwijswoord hoort bij welk zelfstandig naamwoord?</h3>
<table class="nask">
<tr><th>Naar zelfstandige naamwoorden</th><th>verwijs je met</th><th>en</th></tr>
<tr><td>in het enkelvoud, mannelijk</td><td><i>hij, hem, zijn</i></td><td><i>deze, die</i></td></tr>
<tr><td>in het enkelvoud, vrouwelijk</td><td><i>zij, ze, haar</i></td><td><i>deze, die</i></td></tr>
<tr><td>in het enkelvoud, onzijdig</td><td><i>het, zijn</i></td><td><i>dit, dat</i></td></tr>
<tr><td>in het meervoud</td><td><i>zij, ze, hen, hun</i></td><td><i>deze, die</i></td></tr>
</table>

<div class="info-box tip"><h4>Het-woorden zijn onzijdig</h4>
<p>Namen van <b>landen, provincies, steden en clubs</b> en ook alle <b>verkleinwoorden</b> zijn het-woorden: <i><b>Amsterdam</b> en zijn parkeerproblemen</i>, <i>Ajax en zijn supporters</i>, <i>het fietsje en zijn bel</i>.</p></div>

<h4>Mannelijk of vrouwelijk?</h4>
<p>De-woorden zijn mannelijk of vrouwelijk. Als je dat niet aan een woord kunt zien, zoek je het geslacht op in het woordenboek. Van sommige woorden kun je wel vaststellen dat ze vrouwelijk zijn:</p>
<ul>
<li>vrouwelijke personen en dieren: <i>de actrice, de leeuwin</i>;</li>
<li>veel de-woorden op deze uitgangen:</li>
</ul>
<div class="formule-box">-de (liefde) · -heid (oudheid) · -ie (receptie) · -iek (muziek) · -ij (boerderij) · -ing (woning) · -nis (gevangenis) · -schap (weddenschap) · -st (opkomst: pv + st) · -te (belofte) · -teit (activiteit) · -theek (mediatheek) · -uur (natuur)</div>

<h3>3. Ze, zij, hen en hun (meervoud)</h3>
<ul>
<li>Gebruik in het meervoud <b>ze</b> of <b>zij</b> als <b>onderwerp</b>. Gaat het om personen, dan kun je <i>ze</i> of <i>zij</i> gebruiken; bij zaken gebruik je <i>ze</i>.</li>
<li>Gebruik <b>hen</b> als <b>lijdend voorwerp</b> en <b>na een voorzetsel</b>.</li>
<li>Gebruik <b>hun</b> als <b>meewerkend voorwerp zonder voorzetsel</b> en als <b>bezittelijk voornaamwoord</b>.</li>
</ul>
<div class="voorbeeld"><div class="vb-kop">Voorbeeld</div>
<p><i><b>Mijn opa en oma</b> zijn bang dat <u>zij</u> (ow) de trein niet halen, maar ik heb <u>hun</u> (mv) verzekerd dat ik <u>hen</u> (lv) op tijd kom ophalen.</i></p></div>
<div class="info-box let-op"><h4>Let op</h4><p><i>Hun</i> is nooit onderwerp: <i>Hun hebben gewonnen</i> is fout, het moet zijn <i>Zij hebben gewonnen</i>.</p></div>

<h3>4. Die, dat of wat?</h3>
<p>Naar een de-woord verwijs je met <i>die</i>, naar een het-woord met <i>dat</i>. Gebruik het verwijswoord <b>wat</b> als je verwijst naar:</p>
<ul>
<li><i>dat</i> en <i>datgene</i>;</li>
<li>een <b>onbepaald voornaamwoord</b>, zoals <i>alles</i>, <i>niets</i> of <i>iets</i>;</li>
<li>een <b>overtreffende trap</b>: <i>het mooiste wat ik ken</i>;</li>
<li>een <b>hele zin</b>: <i><b>Op mijn verjaardag gaan we indoor surfen</b>, <u>wat</u> ik erg leuk vind.</i></li>
</ul>

<h3>5. Waar + voorzetsel of voorzetsel + wie?</h3>
<ul>
<li>Gebruik <b>daar/waar + voorzetsel</b> als je naar <b>dieren en dingen</b> verwijst: <i>een <b>gravelbaan</b> <u>waarop</u> ze konden lopen</i>.</li>
<li>Gebruik <b>voorzetsel + wie</b> als je naar <b>personen</b> verwijst: <i>vijf <b>debutanten</b>, <u>van wie</u> twee van AZ</i>.</li>
</ul>
<div class="info-box tip"><h4>Ezelsbruggetje</h4><p>Kun je het antecedent een hand geven? Dan is het een persoon en kies je <i>met wie, voor wie, aan wie</i>. Anders kies je <i>waarmee, waarvoor, waaraan</i>.</p></div>
"""

OEFEN = [
    MC('Naar welk woord verwijst <b>zijn</b>? <i>Het station krijgt een nieuwe naam; zijn oude naam verdwijnt na de verbouwing.</i>',
       'station', ['naam', 'verbouwing', 'nieuwe'],
       '<i>Zijn</i> hoort bij een mannelijk of onzijdig woord in het enkelvoud. <i>Het station</i> is onzijdig en is het antecedent.',
       niveau=1, hint='Zoek een het-woord of mannelijk woord dat eerder in de zin staat.'),
    MC('Kies het juiste verwijswoord: <i>De koe likt ___ pasgeboren kalf schoon.</i>',
       'haar', ['zijn', 'hun', 'het'],
       'Een koe is een vrouwelijk dier, dus verwijs je met het vrouwelijke bezittelijk voornaamwoord <i>haar</i>.',
       niveau=1, hint='Is een koe mannelijk of vrouwelijk?'),
    WO('Namen van provincies, zoals Friesland en Zeeland, zijn het-woorden.', True,
       'Waar. Landen, provincies, steden en clubs zijn het-woorden: <i>Friesland en zijn meren</i>.', niveau=1),
    WO('Een woord op -ing, zoals <i>de woning</i>, is mannelijk.', False,
       'Niet waar. De uitgang -ing wijst op een vrouwelijk woord: <i>de woning en haar tuin</i>.', niveau=1),
    IN('Vul in (hen of hun): <i>Ik heb ___ een tekening gegeven.</i>', 'hun',
       '<i>Aan wie</i> heb ik een tekening gegeven? Dat is het meewerkend voorwerp zonder voorzetsel, dus <i>hun</i>.',
       niveau=2, hint='Meewerkend voorwerp zonder voorzetsel → hun.'),
    IN('Vul in (die, dat of wat): <i>Het liedje ___ ze op het schoolfeest zong, was nieuw.</i>', 'dat',
       '<i>Het liedje</i> is een het-woord (verkleinwoord), dus het betrekkelijk voornaamwoord is <i>dat</i>.',
       niveau=2, hint='Liedje is een verkleinwoord.'),
    MC('Kies het juiste verwijswoord: <i>De trainer ___ ik het meest heb geleerd, stopt na dit seizoen.</i>',
       'van wie', ['waarvan', 'van die', 'van wat'],
       'De trainer is een persoon. Naar personen verwijs je met voorzetsel + <i>wie</i>: <i>van wie</i>.',
       niveau=2, hint='Persoon of ding?'),
    IN('Vul in (waar + voorzetsel): <i>De doos ___ de cadeaus zitten, staat op zolder.</i>', 'waarin',
       'De doos is een ding. Je verwijst met waar + voorzetsel: de cadeaus zitten <i>in</i> de doos → <i>waarin</i>.',
       niveau=2, hint='Waar zitten de cadeaus? In ...'),
]

# ---------------------------------------------------------------- toetsen
T44 = ('Antecedent en geslacht', '🔎', [
    MC('Wat is het <b>antecedent</b> van een verwijswoord?',
       'Het woord waarnaar het verwijswoord terugwijst',
       ['Het woord dat direct na het verwijswoord in de zin staat', 'Het onderwerp van de zin met het verwijswoord',
        'Het werkwoord waarbij het verwijswoord hoort'],
       'Het antecedent is het woord (of de woordgroep of zin) dat eerder genoemd is en waarnaar het verwijswoord terugwijst.'),
    MC('Kies het juiste verwijswoord: <i>Het museum is drie maanden dicht, omdat ___ grondig wordt gerenoveerd.</i>',
       'het', ['hij', 'zij', 'die'],
       '<i>Het museum</i> is onzijdig. Als onderwerp verwijs je ernaar met <i>het</i>.'),
    MC('Waarom verwijs je naar <b>Utrecht</b> met <i>zijn</i>, zoals in <i>Utrecht en zijn grachten</i>?',
       'Namen van steden zijn het-woorden', ['Alle eigennamen zijn mannelijk', 'Utrecht eindigt op een medeklinker',
                                             'Plaatsnamen krijgen altijd de'],
       'Namen van landen, provincies, steden en clubs zijn het-woorden (onzijdig). Daarom: <i>Utrecht en zijn grachten</i>.'),
    MC('Welk woord is aan de uitgang te herkennen als <b>vrouwelijk</b>?',
       'de regering', ['de computer', 'de stoel', 'de wekker'],
       'De uitgang -ing wijst op een vrouwelijk woord: <i>de regering en haar plannen</i>.'),
    MC('Welke uitgang wijst <b>niet</b> op een vrouwelijk de-woord?',
       '-er (bakker)', ['-heid (vrijheid)', '-schap (vriendschap)', '-teit (kwaliteit)'],
       '-heid, -schap en -teit zijn vrouwelijke uitgangen. Een woord als <i>de bakker</i> (-er) is een mannelijk persoon.'),
    WO('Verkleinwoorden zijn altijd het-woorden, dus je verwijst ernaar met bijvoorbeeld <i>het</i> of <i>zijn</i>.', True,
       'Waar. Alle verkleinwoorden zijn het-woorden: <i>het bootje en zijn zeil</i>.'),
    WO('Naar <i>de universiteit</i> verwijs je met <i>hij</i>, <i>hem</i> of <i>zijn</i>.', False,
       'Niet waar. <i>Universiteit</i> eindigt op -teit en is vrouwelijk: <i>zij, ze, haar</i>.'),
    MC('Kies het juiste verwijswoord: <i>De bibliotheek verlengt in de examenweken ___ openingstijden.</i>',
       'haar', ['zijn', 'hun', 'het'],
       '<i>Bibliotheek</i> eindigt op -theek en is vrouwelijk: <i>haar openingstijden</i>.'),
    MC('Kies het juiste verwijswoord: <i>PSV heeft gisteren ___ nieuwe trainer gepresenteerd.</i>',
       'zijn', ['haar', 'hun', 'hem'],
       'Namen van clubs zijn het-woorden. Naar een het-woord verwijs je met <i>zijn</i>.'),
    MC('Kies het juiste verwijswoord: <i>Frankrijk heeft vanwege de top ___ grenzen tijdelijk strenger gecontroleerd.</i>',
       'zijn', ['haar', 'hun', 'ze'],
       'Namen van landen zijn het-woorden: <i>Frankrijk en zijn grenzen</i>.'),
    MC('Kies het juiste verwijswoord: <i>De leeuwin likt na de jacht ___ welpen schoon.</i>',
       'haar', ['zijn', 'hun', 'hem'],
       'Een leeuwin is een vrouwelijk dier, dus: <i>haar welpen</i>.'),
    MC('Kies het juiste verwijswoord: <i>Mijn opa heeft ___ oude racefiets aan mij gegeven.</i>',
       'zijn', ['haar', 'hun', 'hem'],
       'Opa is een mannelijk persoon: <i>zijn racefiets</i>.'),
    MC('Welke aanwijzende voornaamwoorden horen bij een <b>het-woord</b> in het enkelvoud?',
       'dit en dat', ['deze en die', 'die en wie', 'deze en dat'],
       'Bij een het-woord in het enkelvoud gebruik je <i>dit</i> en <i>dat</i>; bij de-woorden en het meervoud <i>deze</i> en <i>die</i>.'),
    MC('Kies het juiste woord: <i>Kijk eens naar ___ vakantiehuisje aan het water!</i>',
       'dat', ['die', 'deze', 'wie'],
       '<i>Vakantiehuisje</i> is een verkleinwoord en dus een het-woord: <i>dat vakantiehuisje</i>.'),
    MC('Kies het juiste verwijswoord: <i>De gemeente laat weten dat ___ het park volgend jaar opnieuw inricht.</i>',
       'zij', ['hij', 'het', 'hem'],
       '<i>Gemeente</i> eindigt op -te en is vrouwelijk. Als onderwerp: <i>zij</i> (of <i>ze</i>).'),
    WO('Als je aan een de-woord niet kunt zien of het mannelijk of vrouwelijk is, zoek je het geslacht op in het woordenboek.', True,
       'Waar. Dat is precies wat de regel zegt; alleen bij bepaalde uitgangen en vrouwelijke personen/dieren kun je het zelf vaststellen.'),
    WO('Het woord <i>fabriek</i> is onzijdig, omdat het niet op -ing of -heid eindigt.', False,
       'Niet waar. Het is <i>de fabriek</i>, en de uitgang -iek wijst op een vrouwelijk woord: <i>de fabriek en haar werknemers</i>.'),
    IV('Lees: <i>Het ziekenhuis heeft een nieuwe vleugel laten bouwen. Die is speciaal bedoeld voor kinderen.</i> Naar welk woord verwijst <b>Die</b>?',
       'vleugel', '<i>Die</i> verwijst naar een de-woord dat eerder genoemd is: <i>de vleugel</i>. Naar <i>het ziekenhuis</i> had je met <i>dat</i> verwezen.'),
    OP('Een leerling schrijft: <i>De stichting zoekt vrijwilligers voor zijn zomerkamp.</i> Welk verwijswoord is fout? Schrijf het juiste woord op en leg uit waarom.',
       ['haar', 'vrouwelijk/uitgang'],
       'Zijn moet haar zijn, want stichting eindigt op -ing en is dus een vrouwelijk woord.',
       '<i>Stichting</i> heeft de vrouwelijke uitgang -ing, dus: <i>haar zomerkamp</i>.'),
    OP('Waarom verwijs je naar <i>het nieuwe bedrijf van mijn tante</i> met <i>zijn</i> en niet met <i>haar</i>?',
       ['onzijdig/het-woord', 'antecedent/kern/hoofdwoord/niet naar'],
       'Het antecedent is bedrijf en niet tante; bedrijf is een het-woord (onzijdig), dus verwijs je met zijn.',
       'Het verwijswoord hoort bij het kernwoord <i>bedrijf</i>, een onzijdig het-woord. <i>Tante</i> is alleen een bijvoeglijke bepaling.'),
])

T45 = ('Ze, zij, hen en hun', '👥', [
    MC('Kies het juiste verwijswoord: <i>De leerlingen vroegen of de mentor ___ kon helpen met de planning.</i>',
       'hen', ['hun', 'zij', 'wie'],
       'Wie kon de mentor helpen? → <i>de leerlingen</i> zijn hier lijdend voorwerp, dus <i>hen</i>.'),
    MC('Kies het juiste verwijswoord: <i>Ik heb mijn neven een kaartje gestuurd en ___ daarna ook nog gebeld.</i>',
       'hen', ['hun', 'zij', 'wie'],
       '<i>Wie</i> heb ik gebeld? Mijn neven: lijdend voorwerp, dus <i>hen</i>.'),
    MC('Kies het juiste verwijswoord: <i>Mijn buren gaan verhuizen; ik heb ___ beloofd te helpen met inpakken.</i>',
       'hun', ['hen', 'zij', 'die'],
       'Aan wie heb ik iets beloofd? Aan de buren: meewerkend voorwerp zonder voorzetsel, dus <i>hun</i>.'),
    MC('Kies het juiste verwijswoord: <i>De spelers kregen een staande ovatie; de trainer was erg trots op ___.</i>',
       'hen', ['hun', 'zij', 'wie'],
       'Na het voorzetsel <i>op</i> gebruik je bij personen in het meervoud <i>hen</i>.'),
    MC('Kies het juiste verwijswoord: <i>De toeristen zochten ___ bagage op de verkeerde band.</i>',
       'hun', ['hen', 'zij', 'ze'],
       'Het gaat om de bagage ván de toeristen: bezittelijk voornaamwoord <i>hun</i>.'),
    MC('Kies het juiste verwijswoord: <i>Mijn zusjes zeggen dat ___ morgen zelf naar de sporthal fietsen.</i>',
       'zij', ['hun', 'hen', 'die'],
       'Het verwijswoord is hier onderwerp (wie fietsen?) in het meervoud: <i>zij</i> of <i>ze</i>.'),
    MC('Kies het juiste verwijswoord: <i>De kinderen hadden honger, dus de juf gaf ___ allemaal een appel.</i>',
       'hun', ['hen', 'zij', 'wie'],
       'Aan wie gaf de juf een appel? Aan de kinderen: meewerkend voorwerp zonder voorzetsel, dus <i>hun</i>.'),
    MC('Kies het juiste verwijswoord: <i>Waar zijn mijn voetbalschoenen? Ik heb ___ gisteren in de gang gezet.</i>',
       'ze', ['hen', 'hun', 'wie'],
       'Bij zaken in het meervoud gebruik je <i>ze</i>; <i>hen</i> en <i>hun</i> gebruik je alleen voor personen.'),
    MC('Welke functie heeft <b>hun</b> in: <i>De ouders van Sem? Ik heb hun de vakantiefoto\'s laten zien.</i>',
       'meewerkend voorwerp', ['lijdend voorwerp', 'onderwerp', 'bijwoordelijke bepaling'],
       'Aan wie heb ik de foto\'s laten zien? Aan de ouders: meewerkend voorwerp. Daarom staat er <i>hun</i>.'),
    MC('Welke functie heeft <b>hen</b> in: <i>De nieuwe buren zijn aardig; we hebben hen uitgenodigd voor de barbecue.</i>',
       'lijdend voorwerp', ['meewerkend voorwerp', 'onderwerp', 'naamwoordelijk deel'],
       'Wie hebben we uitgenodigd? De buren: lijdend voorwerp, dus <i>hen</i>.'),
    WO('Na een voorzetsel gebruik je <i>hun</i>, zoals in <i>Ik ga met hun naar de film.</i>', False,
       'Niet waar. Na een voorzetsel gebruik je <i>hen</i>: <i>Ik ga met hen naar de film.</i>'),
    WO('<i>Hun</i> kan ook een bezittelijk voornaamwoord zijn, zoals in <i>hun nieuwe huis</i>.', True,
       'Waar. <i>Hun</i> is meewerkend voorwerp zonder voorzetsel én bezittelijk voornaamwoord.'),
    WO('Als onderwerp in het meervoud kun je bij personen zowel <i>ze</i> als <i>zij</i> gebruiken.', True,
       'Waar. Gaat het om personen, dan kun je <i>ze</i> of <i>zij</i> als onderwerp gebruiken.'),
    WO('<i>Hun hebben gisteren de finale gewonnen</i> is correct Nederlands.', False,
       'Niet waar. Als onderwerp gebruik je <i>zij</i> of <i>ze</i>: <i>Zij hebben gisteren de finale gewonnen.</i>'),
    MC('In welke zin is het verwijswoord <b>goed</b> gebruikt?',
       'Ik heb hun een berichtje gestuurd.',
       ['Ik heb hen een berichtje gestuurd.', 'Ik heb hun gisteren gesproken.', 'Ik zei tegen hun dat het laat was.'],
       'Aan wie heb ik een berichtje gestuurd? Meewerkend voorwerp zonder voorzetsel → <i>hun</i>. In de andere zinnen hoort <i>hen</i>.'),
    MC('In welke zin is het verwijswoord <b>fout</b> gebruikt?',
       'De docent gaf hen een compliment.',
       ['De docent wachtte op hen.', 'De docent gaf hun een compliment.', 'De docent heeft hen gewaarschuwd.'],
       '<i>Aan wie</i> gaf de docent een compliment? Meewerkend voorwerp zonder voorzetsel, dus <i>hun</i> in plaats van <i>hen</i>.'),
    IV('Vul in: als bezittelijk voornaamwoord en als ___ zonder voorzetsel gebruik je <i>hun</i>.',
       'meewerkend voorwerp|meewerkend',
       'Volgens de regel gebruik je <i>hun</i> als meewerkend voorwerp zonder voorzetsel en als bezittelijk voornaamwoord.'),
    IV('Welk verwijswoord gebruik je bij personen in het meervoud als lijdend voorwerp en na een voorzetsel?',
       'hen', '<i>Hen</i> is lijdend voorwerp of staat na een voorzetsel: <i>Ik zie hen</i>, <i>Ik wacht op hen</i>.'),
    OP('Leg uit waarom het verwijswoord fout is in: <i>We hebben hen een uitnodiging gestuurd.</i>',
       ['meewerkend/mv', 'hun', 'voorzetsel'],
       'Hen is hier meewerkend voorwerp zonder voorzetsel (aan wie?), dan moet je hun gebruiken.',
       'Aan wie hebben we een uitnodiging gestuurd? Dat is het meewerkend voorwerp zonder voorzetsel → <i>hun</i>.', 2),
    OP('Verbeter de zin en leg uit: <i>Mijn vrienden waren laat, dus ik heb op hun gewacht.</i>',
       ['hen', 'voorzetsel'],
       'Ik heb op hen gewacht: na een voorzetsel (op) gebruik je hen.',
       'Na een voorzetsel gebruik je bij personen in het meervoud <i>hen</i>.'),
])

T46 = ('Die, dat of wat', '🔗', [
    MC('Kies het juiste verwijswoord: <i>Het boek ___ ik in de zomervakantie las, was erg spannend.</i>',
       'dat', ['die', 'wat', 'wie'], '<i>Het boek</i> is een het-woord, dus het betrekkelijk voornaamwoord is <i>dat</i>.'),
    MC('Kies het juiste verwijswoord: <i>De documentaire ___ we gisteren zagen, duurde bijna drie uur.</i>',
       'die', ['dat', 'wat', 'wie'], '<i>De documentaire</i> is een de-woord, dus <i>die</i>.'),
    MC('Kies het juiste verwijswoord: <i>Alles ___ je hier zegt, blijft tussen ons.</i>',
       'wat', ['dat', 'die', 'wie'], 'Na het onbepaald voornaamwoord <i>alles</i> gebruik je <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>Dat is het mooiste schilderij ___ ik ooit in een museum heb gezien.</i>',
       'dat', ['wat', 'die', 'wie'],
       'Het antecedent is hier het zelfstandig naamwoord <i>schilderij</i> (het-woord), dus <i>dat</i>. Staat er alleen <i>het mooiste</i> zonder zelfstandig naamwoord, dan gebruik je <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>Mijn broer haalde in één keer zijn rijbewijs, ___ niemand had verwacht.</i>',
       'wat', ['dat', 'die', 'wie'], 'Het verwijswoord verwijst naar de hele zin ervoor, dus gebruik je <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>Er is niets ___ haar kan tegenhouden.</i>',
       'wat', ['dat', 'die', 'wie'], 'Na <i>niets</i> (onbepaald voornaamwoord) gebruik je <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het meisje ___ naast me in de klas zit, heet Noor.</i>',
       'dat', ['die', 'wat', 'wie'], '<i>Het meisje</i> is grammaticaal een het-woord (verkleinwoord), dus <i>dat</i>.'),
    MC('Kies het juiste verwijswoord: <i>Datgene ___ je zoekt, ligt in de bovenste la.</i>',
       'wat', ['dat', 'die', 'wie'], 'Naar <i>datgene</i> verwijs je met <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>De mountainbike ___ ik vorige week kocht, is nu al gestolen.</i>',
       'die', ['dat', 'wat', 'wie'], '<i>De mountainbike</i> is een de-woord, dus <i>die</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het chalet ___ we in Oostenrijk gehuurd hebben, ligt vlak bij de piste.</i>',
       'dat', ['die', 'wat', 'wie'], '<i>Het chalet</i> is een het-woord, dus <i>dat</i>.'),
    MC('Waarom staat er <b>wat</b> in: <i>Ze won de schrijfwedstrijd, wat haar ouders erg trots maakte.</i>',
       'Wat verwijst naar de hele zin ervoor',
       ['Wat verwijst naar het woord ouders', 'Wat hoort bij een de-woord', 'Wat verwijst naar de schrijfwedstrijd'],
       'Niet de wedstrijd zelf maakte de ouders trots, maar het feit dát ze won: <i>wat</i> verwijst naar de hele zin.'),
    WO('Na <i>iets</i> en <i>niets</i> gebruik je als betrekkelijk voornaamwoord <i>dat</i>.', False,
       'Niet waar. <i>Iets</i> en <i>niets</i> zijn onbepaalde voornaamwoorden; daarna gebruik je <i>wat</i>.'),
    WO('Na een overtreffende trap zonder zelfstandig naamwoord, zoals <i>het leukste</i>, gebruik je <i>wat</i>.', True,
       'Waar. <i>Het leukste wat ik heb gedaan</i>: na een overtreffende trap gebruik je <i>wat</i>.'),
    WO('Als het antecedent een de-woord is, gebruik je het betrekkelijk voornaamwoord <i>die</i>.', True,
       'Waar. <i>De film die</i>, <i>de vriendin die</i>; bij het-woorden is het <i>dat</i>.'),
    WO('<i>Het concert die we bezochten, was uitverkocht</i> is correct.', False,
       'Niet waar. <i>Het concert</i> is een het-woord, dus: <i>Het concert dat we bezochten</i>.'),
    MC('In welke zin is het verwijswoord <b>fout</b>?',
       'Alles dat ik weet, heb ik zelf geleerd.',
       ['Het cadeau dat ik kreeg, was prachtig.', 'Het lied dat ze zong, was nieuw.', 'Iets wat je mist, kun je lenen.'],
       'Na <i>alles</i> gebruik je <i>wat</i>: <i>Alles wat ik weet</i>. De andere zinnen zijn correct.'),
    MC('Welke zin over het verhaal van de buurman is <b>correct</b>?',
       'Alles wat hij vertelde, klopte niet.',
       ['Alles dat hij vertelde, klopte niet.', 'Alles die hij vertelde, klopte niet.', 'Alles wie hij vertelde, klopte niet.'],
       'Na het onbepaald voornaamwoord <i>alles</i> gebruik je <i>wat</i>.'),
    IV('Lees: <i>Dit is het moeilijkste wat ik ooit heb moeten doen.</i> Welke vorm van het bijvoeglijk naamwoord staat vóór het verwijswoord, waardoor je <i>wat</i> gebruikt?',
       'overtreffende trap|overtreffend', '<i>Het moeilijkste</i> is een overtreffende trap; daarna gebruik je <i>wat</i>.'),
    OP('Leg uit waarom in <i>Het team dat gisteren won, viert vanavond feest</i> het woord <b>dat</b> correct is.',
       ['onzijdig/het-woord', 'antecedent/verwijst'],
       'Dat verwijst naar het antecedent team, en dat is een het-woord (onzijdig).',
       'Het antecedent <i>het team</i> is onzijdig; bij het-woorden gebruik je <i>dat</i>.'),
    OP('Leg uit waarom er <b>wat</b> staat in: <i>Alles wat je meeneemt, moet in één tas passen.</i>',
       ['onbepaald'],
       'Wat verwijst naar alles; dat is een onbepaald voornaamwoord, en daarna gebruik je wat.',
       'Naar een onbepaald voornaamwoord zoals <i>alles</i>, <i>niets</i> of <i>iets</i> verwijs je met <i>wat</i>.'),
])

T47 = ('Waar + voorzetsel of voorzetsel + wie', '🧭', [
    MC('Kies het juiste verwijswoord: <i>Dit is de vulpen ___ ik mijn examen heb geschreven.</i>',
       'waarmee', ['met wie', 'met wat', 'met die'],
       'Een vulpen is een ding: waar + voorzetsel → <i>waarmee</i>.'),
    MC('Kies het juiste verwijswoord: <i>De vriendin ___ ik op vakantie ga, heet Lotte.</i>',
       'met wie', ['waarmee', 'met wat', 'met die'],
       'Een vriendin is een persoon: voorzetsel + wie → <i>met wie</i>.'),
    MC('Kies het juiste verwijswoord: <i>Is dat de leraar ___ je thuis zo vaak vertelt?</i>',
       'over wie', ['waarover', 'over wat', 'over die'],
       'De leraar is een persoon, dus <i>over wie</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het onderwerp ___ ik mijn profielwerkstuk schrijf, is klimaatverandering.</i>',
       'waarover', ['over wie', 'over wat', 'over dat'],
       'Een onderwerp is geen persoon: waar + voorzetsel → <i>waarover</i>.'),
    MC('Kies het juiste verwijswoord: <i>De bureaustoel ___ je zit, is al jaren kapot.</i>',
       'waarop', ['op wie', 'op wat', 'op die'],
       'Een stoel is een ding: <i>waarop</i>.'),
    MC('Kies het juiste verwijswoord: <i>De hond ___ ik elke ochtend wandel, is van de buren.</i>',
       'waarmee', ['met wie', 'met wat', 'met die'],
       'Bij dieren gebruik je daar/waar + voorzetsel: <i>waarmee</i>. Voorzetsel + wie is alleen voor personen.'),
    MC('Kies het juiste verwijswoord: <i>De oom ___ ik deze trui heb gekregen, woont in Canada.</i>',
       'van wie', ['waarvan', 'van wat', 'van die'],
       'Een oom is een persoon: <i>van wie</i>.'),
    MC('Kies het juiste verwijswoord: <i>De kast ___ de oude fotoalbums staan, is van eikenhout.</i>',
       'waarin', ['in wie', 'in wat', 'in die'],
       'Een kast is een ding: <i>waarin</i>.'),
    MC('Kies het juiste verwijswoord: <i>De buurvrouw ___ ik de reservesleutel heb gegeven, is op vakantie.</i>',
       'aan wie', ['waaraan', 'aan wat', 'aan die'],
       'De buurvrouw is een persoon: <i>aan wie</i>.'),
    MC('Welke zin over de zieke collega is <b>correct</b>?',
       'De collega met wie ik samenwerk, is ziek.',
       ['De collega waarmee ik samenwerk, is ziek.', 'De collega met die ik samenwerk, is ziek.',
        'De collega met wat ik samenwerk, is ziek.'],
       'Een collega is een persoon, dus voorzetsel + wie: <i>met wie</i>.'),
    MC('Welke zin over het botte mes is <b>correct</b>?',
       'Het mes waarmee ik snijd, is bot.',
       ['Het mes met wie ik snijd, is bot.', 'Het mes met wat ik snijd, is bot.', 'Het mes met dat ik snijd, is bot.'],
       'Een mes is een ding: waar + voorzetsel → <i>waarmee</i>.'),
    WO('Naar personen verwijs je met voorzetsel + <i>wie</i>, bijvoorbeeld <i>met wie</i> of <i>voor wie</i>.', True,
       'Waar. Bij personen: <i>met wie, voor wie, aan wie, van wie</i>.'),
    WO('Naar dieren verwijs je net als naar personen met voorzetsel + <i>wie</i>.', False,
       'Niet waar. Naar dieren en dingen verwijs je met daar/waar + voorzetsel: <i>de kat waarmee ik speel</i>.'),
    WO('<i>De vriend waarmee ik elke zaterdag voetbal</i> is volgens de regel correct.', False,
       'Niet waar. Een vriend is een persoon: <i>de vriend met wie ik elke zaterdag voetbal</i>.'),
    WO('Naar dingen kun je verwijzen met <i>daar</i> of <i>waar</i> + voorzetsel, zoals <i>daarmee</i> of <i>waarmee</i>.', True,
       'Waar. Bij dingen en dieren gebruik je daar/waar + voorzetsel.'),
    IV('Vul het juiste verwijswoord in: <i>De bal ___ we op het schoolplein voetbalden, was lek.</i>',
       'waarmee', 'Met de bal voetballen; de bal is een ding → <i>waarmee</i>.'),
    IV('Vul het juiste verwijswoord in: <i>De film ___ iedereen op school praat, draait nu in de bioscoop.</i>',
       'waarover', 'Iedereen praat <i>over</i> de film; een film is een ding → <i>waarover</i>.'),
    IV('Vul het juiste verwijswoord in: <i>Het bureau ___ mijn laptop staat, is veel te klein.</i>',
       'waarop', 'De laptop staat <i>op</i> het bureau; een bureau is een ding → <i>waarop</i>.'),
    OP('Leg uit waarom <i>De trainer waarmee ik na de wedstrijd praatte</i> niet correct is, en geef de verbetering.',
       ['met wie', 'persoon/personen/mens'],
       'Een trainer is een persoon; dan gebruik je voorzetsel + wie: de trainer met wie ik praatte.',
       'Waar + voorzetsel gebruik je voor dingen en dieren; bij personen voorzetsel + wie.'),
    OP('Welk soort verwijswoord gebruik je in <i>De kat ___ ik elke avond speel, is drie jaar oud</i>? Vul het in en leg je keuze uit.',
       ['waarmee', 'voorzetsel'],
       'Waarmee: een kat is een dier, en bij dieren gebruik je waar + voorzetsel.',
       'Bij dieren en dingen gebruik je daar/waar + voorzetsel, dus <i>waarmee</i>.'),
])

T48 = ('Foutenjacht verwijswoorden', '🕵️', [
    MC('Welk woord moet in plaats van <b>haar</b> staan? <i>Mijn laptop doet raar; ik moet haar laten repareren.</i>',
       'hem', ['hen', 'het', 'hun'],
       '<i>De laptop</i> is mannelijk. Als lijdend voorwerp verwijs je ernaar met <i>hem</i>.'),
    MC('Verbeter het verwijswoord: <i>Het team heeft haar beste seizoen ooit gespeeld.</i>',
       'zijn', ['hun', 'hem', 'die'], '<i>Het team</i> is onzijdig: <i>zijn beste seizoen</i>.'),
    MC('Verbeter het verwijswoord: <i>De regering heeft zijn plannen voor het onderwijs gepresenteerd.</i>',
       'haar', ['hun', 'hem', 'het'], '<i>Regering</i> eindigt op -ing en is vrouwelijk: <i>haar plannen</i>.'),
    MC('Verbeter het verwijswoord: <i>Alles dat je nodig hebt voor het kamp, staat op de lijst.</i>',
       'wat', ['die', 'wie', 'dit'], 'Na <i>alles</i> gebruik je <i>wat</i>.'),
    MC('Verbeter het verwijswoord: <i>Mijn klasgenoten waren jarig; ik heb hen gisteren een felicitatie gestuurd.</i>',
       'hun', ['zij', 'die', 'wie'],
       'Aan wie heb ik een felicitatie gestuurd? Meewerkend voorwerp zonder voorzetsel → <i>hun</i>.'),
    MC('Verbeter het verwijswoord: <i>De vriend waarover ik je vertelde, komt morgen logeren.</i>',
       'over wie', ['over die', 'over wat', 'daarover'], 'Een vriend is een persoon: <i>over wie</i>.'),
    MC('Verbeter het verwijswoord: <i>Nederland heeft haar eerste gouden medaille binnen.</i>',
       'zijn', ['hun', 'hem', 'die'], 'Landen zijn het-woorden: <i>Nederland en zijn eerste medaille</i>.'),
    MC('In welke zin over organisaties staat een <b>fout</b> verwijswoord?',
       'De gemeente heeft zijn begroting rond.',
       ['De apotheek heeft haar openingstijden aangepast.', 'Het restaurant heeft zijn menukaart vernieuwd.',
        'Ajax heeft zijn selectie bekendgemaakt.'],
       '<i>Gemeente</i> eindigt op -te en is vrouwelijk: <i>haar begroting</i>. De andere zinnen zijn correct.'),
    MC('In welke zin met <i>hen</i> of <i>hun</i> staat een <b>fout</b> verwijswoord?',
       'De docent gaf hen extra uitleg.',
       ['De kinderen renden naar hun moeder.', 'We zagen hen gisteren in de stad.', 'Ik heb lang op hen gewacht.'],
       'Aan wie gaf de docent uitleg? Meewerkend voorwerp zonder voorzetsel → <i>hun</i>.'),
    WO('Deze zin is correct: <i>De vereniging viert dit jaar haar vijftigjarig bestaan.</i>', True,
       'Waar. <i>Vereniging</i> eindigt op -ing en is vrouwelijk, dus <i>haar</i> klopt.'),
    WO('Deze zin is correct: <i>Het kind pakte haar rugtas en liep naar buiten.</i>', False,
       'Niet waar. <i>Het kind</i> is een het-woord: <i>zijn rugtas</i>.'),
    WO('Deze zin is correct: <i>De docent met wie ik sprak, was erg behulpzaam.</i>', True,
       'Waar. Een docent is een persoon, dus voorzetsel + wie.'),
    WO('Deze zin is correct: <i>Er is niets dat ik liever doe dan tekenen.</i>', False,
       'Niet waar. Na <i>niets</i> hoort <i>wat</i>: <i>Er is niets wat ik liever doe.</i>'),
    WO('Deze zin is correct: <i>De boeken? Ik heb ze vanochtend teruggebracht naar de bibliotheek.</i>', True,
       'Waar. Bij zaken in het meervoud gebruik je <i>ze</i>.'),
    WO('Deze zin is correct: <i>Het bericht wat je gisteravond stuurde, is niet aangekomen.</i>', False,
       'Niet waar. <i>Het bericht</i> is een het-woord: <i>het bericht dat je stuurde</i>.'),
    IV('Schrijf het juiste verwijswoord op dat in plaats van <b>met wat</b> moet staan: <i>De schaar met wat ik knip, is erg scherp.</i>',
       'waarmee', 'Een schaar is een ding: waar + voorzetsel → <i>waarmee</i>.'),
    IV('Schrijf het juiste verwijswoord op dat in plaats van <b>op wat</b> moet staan: <i>Het podium op wat de band speelde, stortte bijna in.</i>',
       'waarop', 'Een podium is een ding: <i>waarop</i>.'),
    IV('Schrijf op wat er in plaats van <b>waarvan</b> moet staan: <i>De tante waarvan ik deze ketting kreeg, woont in Gent.</i>',
       'van wie', 'Een tante is een persoon: voorzetsel + wie → <i>van wie</i>.'),
    OP('Verbeter de fout en leg uit: <i>Mijn telefoon is gevallen; ik breng haar morgen naar de reparateur.</i>',
       ['hem', 'mannelijk'],
       'Haar moet hem zijn: de telefoon is een mannelijk woord.',
       '<i>De telefoon</i> is mannelijk; als lijdend voorwerp: <i>hem</i>.'),
    OP('Verbeter de fout en leg uit: <i>Utrecht is trots op haar oude binnenstad.</i>',
       ['zijn', 'het-woord/onzijdig/plaatsnaam/plaatsnamen'],
       'Haar moet zijn zijn: namen van steden zijn het-woorden (onzijdig).',
       'Steden, landen, provincies en clubs zijn het-woorden: <i>Utrecht is trots op zijn oude binnenstad</i>.'),
])

T49 = ('Gemengd', '🔀', [
    MC('Kies het juiste verwijswoord: <i>De directie heeft besloten dat ___ de schooldag voortaan later laat beginnen.</i>',
       'zij', ['hij', 'het', 'hun'], '<i>Directie</i> eindigt op -ie en is vrouwelijk; als onderwerp: <i>zij</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het restaurant aan de haven? Ik vind ___ vis heerlijk.</i>',
       'zijn', ['haar', 'hun', 'die'], '<i>Het restaurant</i> is onzijdig: <i>zijn vis</i>.'),
    MC('Kies het juiste verwijswoord: <i>De schaatsers stonden klaar; de starter gaf ___ het startsignaal.</i>',
       'hun', ['hen', 'zij', 'wie'], 'Aan wie gaf de starter het signaal? Meewerkend voorwerp zonder voorzetsel → <i>hun</i>.'),
    MC('Kies het juiste verwijswoord: <i>Mijn nichtjes komen logeren; ik haal ___ morgen van het station.</i>',
       'hen', ['hun', 'zij', 'wie'], 'Wie haal ik op? Lijdend voorwerp → <i>hen</i>.'),
    MC('Kies het juiste verwijswoord: <i>Ze kreeg een tien voor haar betoog, ___ ze zelf niet had verwacht.</i>',
       'wat', ['dat', 'die', 'wie'], 'Het verwijswoord slaat op de hele zin ervoor, dus <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>De kapper ___ ik al jaren ga, gaat binnenkort met pensioen.</i>',
       'naar wie', ['waarnaar', 'naar die', 'naar wat'], 'Een kapper is een persoon: <i>naar wie</i>.'),
    MC('Kies het juiste verwijswoord: <i>De sporttas ___ mijn gymspullen zitten, ligt nog in de bus.</i>',
       'waarin', ['in wie', 'in die', 'in wat'], 'Een sporttas is een ding: <i>waarin</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het fietsje van mijn broertje is te klein; ___ zadel staat al op de hoogste stand.</i>',
       'zijn', ['haar', 'hun', 'ze'], 'Verkleinwoorden zijn het-woorden: <i>het fietsje en zijn zadel</i>.'),
    MC('Kies het juiste verwijswoord: <i>Iets ___ je echt moet proeven, is de appeltaart van mijn oma.</i>',
       'wat', ['dat', 'die', 'wie'], 'Na <i>iets</i> (onbepaald voornaamwoord) gebruik je <i>wat</i>.'),
    MC('Welke reeks verwijswoorden hoort bij het <b>meervoud</b>?',
       'zij, ze, hen, hun', ['zij, ze, haar, hun', 'hij, hem, zijn, die', 'het, zijn, dit, dat'],
       'Bij het meervoud horen <i>zij, ze, hen, hun</i> (en <i>deze, die</i>).'),
    MC('Welk woord is een <b>het-woord</b>?',
       'het hondje', ['de vriendschap', 'de opkomst', 'de stichting'],
       'Verkleinwoorden zijn altijd het-woorden. De andere woorden zijn vrouwelijke de-woorden (-schap, -st, -ing).'),
    WO('Het woord <i>opkomst</i> heeft de uitgang -st en is daarom vrouwelijk.', True,
       'Waar. De uitgang -st (stam + t, zoals in <i>opkomst</i>) wijst op een vrouwelijk woord.'),
    WO('Naar <i>de koningin</i> verwijs je met <i>zij</i>, <i>ze</i> of <i>haar</i>.', True,
       'Waar. Vrouwelijke personen zijn vrouwelijk: <i>de koningin en haar gasten</i>.'),
    WO('Na een voorzetsel gebruik je bij personen in het meervoud <i>hun</i>, zoals in <i>voor hun</i>.', False,
       'Niet waar. Na een voorzetsel gebruik je <i>hen</i>: <i>voor hen</i>.'),
    WO('Naar <i>België</i> verwijs je met <i>haar</i>, omdat landen vrouwelijk zijn.', False,
       'Niet waar. Landen zijn het-woorden: <i>België en zijn kust</i>.'),
    IV('Vul het juiste verwijswoord in: <i>Het probleem ___ we het gisteren in de les hadden, is nu opgelost.</i>',
       'waarover', 'We hadden het <i>over</i> het probleem; een probleem is geen persoon → <i>waarover</i>.'),
    IV('Vul het juiste verwijswoord in: <i>De muur ___ de graffiti stond, is opnieuw geverfd.</i>',
       'waarop', 'De graffiti stond <i>op</i> de muur; een muur is een ding → <i>waarop</i>.'),
    IV('Lees: <i>Mijn zus en haar vriendin reisden naar Parijs. Daar hebben ze honderden foto\'s gemaakt.</i> Naar welk woord verwijst <b>Daar</b>?',
       'Parijs', '<i>Daar</i> verwijst naar een plaats die eerder genoemd is: <i>Parijs</i>.'),
    OP('Leg uit waarom <b>die</b> niet naar <i>de voetballers</i> kan verwijzen in: <i>De voetballers kregen een medaille, maar die was niet van echt goud.</i>',
       ['enkelvoud', 'meervoud'],
       'Die was staat in het enkelvoud; de voetballers is meervoud, dus die verwijst naar medaille.',
       'De persoonsvorm <i>was</i> is enkelvoud. Het antecedent moet dus ook enkelvoud zijn.'),
    OP('Maak van deze twee zinnen één zin met een verwijswoord dat naar <i>mijn neef</i> verwijst: <i>Ik ga morgen met mijn neef naar de bioscoop. Hij woont in Leiden.</i>',
       ['met wie'],
       'Mijn neef, met wie ik morgen naar de bioscoop ga, woont in Leiden.',
       'Je neef is een persoon: voorzetsel + wie → <i>met wie</i>.'),
])

T50 = ('Eindtoets verwijzen', '🎯', [
    MC('Wat is het antecedent van <b>die</b> in: <i>Mijn oma bakt elke zondag een taart, die ze met de buren deelt.</i>',
       'taart', ['oma', 'zondag', 'buren'], '<i>Die</i> verwijst naar het ding dat gedeeld wordt: <i>de taart</i>.'),
    MC('Wat is het antecedent van <b>wat</b> in: <i>Thijs zakte voor zijn theorie-examen, wat hem veel geld kostte.</i>',
       'de hele zin ervoor', ['het theorie-examen', 'het woord Thijs', 'het woord geld'],
       'Het zakken kostte geld: <i>wat</i> verwijst naar de hele zin.'),
    MC('Kies het juiste verwijswoord: <i>De apotheek is verhuisd; ___ ingang zit nu om de hoek.</i>',
       'haar', ['zijn', 'hun', 'die'], '<i>Apotheek</i> eindigt op -theek en is vrouwelijk: <i>haar ingang</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het orkest speelde gisteravond ___ laatste concert van het seizoen.</i>',
       'zijn', ['haar', 'hun', 'dat'], '<i>Het orkest</i> is onzijdig: <i>zijn laatste concert</i>.'),
    MC('Kies het juiste verwijswoord: <i>De vrijwilligers hebben hard gewerkt; we hebben ___ een bedankkaart gestuurd.</i>',
       'hun', ['hen', 'zij', 'wie'], 'Aan wie hebben we een kaart gestuurd? Meewerkend voorwerp zonder voorzetsel → <i>hun</i>.'),
    MC('Kies het juiste verwijswoord: <i>De nieuwe teamgenoten? Ik heb ___ meteen aan de trainer voorgesteld.</i>',
       'hen', ['hun', 'zij', 'wie'], 'Wie heb ik voorgesteld? Lijdend voorwerp → <i>hen</i>.'),
    MC('Kies het juiste verwijswoord: <i>Het lekkerste ___ ik ken, is pizza met extra kaas.</i>',
       'wat', ['dat', 'die', 'wie'], 'Na een overtreffende trap zonder zelfstandig naamwoord (<i>het lekkerste</i>) gebruik je <i>wat</i>.'),
    MC('Kies het juiste verwijswoord: <i>De rugzak ___ ik mijn lunch meeneem, is gescheurd.</i>',
       'waarin', ['in wie', 'in die', 'in wat'], 'Een rugzak is een ding: <i>waarin</i>.'),
    MC('Kies het juiste verwijswoord: <i>De mentor ___ ik mijn probleem besprak, gaf me goed advies.</i>',
       'met wie', ['waarmee', 'met die', 'met wat'], 'Een mentor is een persoon: <i>met wie</i>.'),
    MC('Welke rij bevat <b>alleen</b> vrouwelijke de-woorden?',
       'regering, natuur, bakkerij',
       ['regering, stoel, bakkerij', 'computer, natuur, gevangenis', 'trein, liefde, bibliotheek'],
       '-ing, -uur en -ij zijn vrouwelijke uitgangen. <i>Stoel, computer</i> en <i>trein</i> zijn mannelijk.'),
    MC('Naar welk woord verwijs je met het betrekkelijk voornaamwoord <b>dat</b>?',
       'het dak', ['de trein', 'de belofte', 'alles'],
       '<i>Dat</i> hoort bij het-woorden: <i>het dak dat lekt</i>. Na <i>alles</i> gebruik je <i>wat</i>.'),
    WO('Een verwijswoord verwijst altijd naar een woord dat in dezelfde zin staat.', False,
       'Niet waar. Het antecedent kan ook in een eerdere zin staan.'),
    WO('<i>Hen</i> gebruik je als lijdend voorwerp en na een voorzetsel.', True,
       'Waar. <i>Ik zie hen</i> (lv), <i>ik wacht op hen</i> (na voorzetsel).'),
    WO('Naar een hele zin verwijs je met <i>die</i>.', False,
       'Niet waar. Naar een hele zin verwijs je met <i>wat</i>.'),
    WO('Het woord <i>mediatheek</i> is vrouwelijk vanwege de uitgang -theek.', True,
       'Waar. -theek is een vrouwelijke uitgang: <i>de mediatheek en haar collectie</i>.'),
    IV('Vul het juiste verwijswoord in: <i>De ladder ___ hij het dak op klom, was te kort.</i>',
       'waarmee', 'Hij klom <i>met</i> de ladder; een ladder is een ding → <i>waarmee</i>.'),
    IV('Vul het juiste verwijswoord in: <i>De vriendin ___ ik een cadeau koop, is volgende week jarig.</i>',
       'voor wie', 'Ik koop een cadeau <i>voor</i> de vriendin; zij is een persoon → <i>voor wie</i>.'),
    IV('Vul in: in <i>De fiets die ik kocht</i> is <i>de fiets</i> het ___ van het verwijswoord <i>die</i>.',
       'antecedent', 'Het woord waarnaar een verwijswoord terugwijst, heet het <i>antecedent</i>.'),
    OP('Leg uit waarom zowel <i>zij</i> als <i>ze</i> goed is in: <i>Mijn zussen zeggen dat ___ morgen pas komen.</i>',
       ['onderwerp', 'meervoud/personen'],
       'Het verwijswoord is onderwerp in het meervoud en het gaat om personen; dan kun je ze of zij gebruiken.',
       'In het meervoud gebruik je <i>ze</i> of <i>zij</i> als onderwerp; bij personen mogen beide.'),
    OP('Verbeter de twee fouten in: <i>De buren hebben hen hond uitgelaten en ik heb met hun gepraat.</i>',
       ['hun hond', 'met hen'],
       'De buren hebben hun hond uitgelaten (bezittelijk) en ik heb met hen gepraat (na voorzetsel).',
       'Bezittelijk voornaamwoord → <i>hun</i>; na een voorzetsel → <i>hen</i>.'),
])

TOETSEN = {44: T44, 45: T45, 46: T46, 47: T47, 48: T48, 49: T49, 50: T50}

# ---------------------------------------------------------------- schrijven
oef = plaats_antwoorden(OEFEN)
onderwerp = dict(id='c5-5-verwijzen', hoofdstuk=5, paragraaf='5.5', titel='Verwijzen',
                 korteUitleg='Kies het juiste verwijswoord: hij/zij/het, hen/hun, die/dat/wat en waar + voorzetsel of voorzetsel + wie.',
                 icoon='👉', theorie=THEORIE, vragen=oef)
assert len(oef) == 8 and len(THEORIE) >= 1500
with open(os.path.join(DATA, 'c5_5.js'), 'w', encoding='utf-8') as f:
    f.write('/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5 §5) */\n')
    f.write('DURU.register(' + json.dumps(onderwerp, ensure_ascii=False, indent=2) + ');\n')
langste_check('c5_5', oef)

for nr, (sub, icoon, vragen) in TOETSEN.items():
    assert len(vragen) == 20, (nr, len(vragen))
    vr = plaats_antwoorden(vragen)
    ex = {'id': f'ex-h3-nederlands-{nr}', 'hoofdstuk': 5, 'hoofdstukTitel': 'Cursus 5 — Grammatica',
          'paragraaf': '5.5', 'titel': f'Toets {nr} — §5.5 {sub}', 'vak': 'Nederlands · HAVO 3 (Cursus 5)',
          'icoon': icoon, 'duurMin': 20, 'vragen': vr}
    with open(os.path.join(DATA, f'examen_{nr}.js'), 'w', encoding='utf-8') as f:
        f.write('/* Examen conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 5 §5 Verwijzen) */\n')
        f.write('DURU.registerExamen(' + json.dumps(ex, ensure_ascii=False, indent=2) + ');\n')
    langste_check(f'examen_{nr}', vr)
