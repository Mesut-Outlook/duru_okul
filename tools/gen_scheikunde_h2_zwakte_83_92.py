#!/usr/bin/env python3
"""Scheikunde H2: 10 zwakte-toetsen ex-h3-sch-h2-83…92 (2026-11-22), uit zwakte.py --fouten + boek H2.
Per toets 10 zwakke begrippen (kleine stappen, vooraan) / 6 andere stof / 4 herhaling; 10 mc, 6 w-o, 3 invul, 1 open.
- Formules in Unicode (H₂O): exams.js escapet opties en modelantwoord, <sub> zou daar als tekst verschijnen.
- Invul = getal of begrip, nooit een formule: invulGoed zoekt op substring ("H2O2" zou goed zijn bij "H2O").
Schrijft met mode 'x': een bestaande toets wordt nooit overschreven.
"""
import importlib.util, json, os, random

_s = importlib.util.spec_from_file_location("basis", os.path.join(os.path.dirname(os.path.abspath(__file__)), "gen_scheikunde_basis.py"))
B = importlib.util.module_from_spec(_s); _s.loader.exec_module(B)
M, W, I, O = B.M, B.W, B.I, B.O
T = {}


def toets(nr, par, titel, icoon, zwak, overig, herhaling):
    assert (len(zwak), len(overig), len(herhaling)) == (10, 6, 4), (nr, len(zwak), len(overig), len(herhaling))
    T[nr] = (par, titel, icoon, zwak + overig + herhaling)


toets(83, "2.3", "§2.3 Index en coëfficiënt, stap voor stap", "🔢", [
M("Stap 1: kijk naar 4 NH₃. Welk cijfer is hier de index?", "De 3", ["De 4", "De 7", "De 12"], "De index staat rechtsonder. De 4 ervoor is de coëfficiënt"),
M("Stap 2: in 6 CO₂ staan twee getallen. Wat is de coëfficiënt?", "De 6", ["De 2", "De 8", "De 3"], "De coëfficiënt staat vóór de formule. De 2 rechtsonder is de index"),
M("Op een kaartje staat 7 H₂O. Waarvan zijn er zeven?", "Van de watermoleculen", ["Van de waterstofatomen", "Van de atomen in totaal", "Van de atoomsoorten"], "Het getal ervoor telt hele moleculen. Waterstofatomen zijn er 7 × 2 = 14"),
I("Stap 3: hoeveel H-atomen bevat één molecuul NH₃? ____", "3", "De index 3 hoort bij de H"),
I("Stap 4: je hebt nu 4 NH₃. Hoeveel H-atomen zijn dat samen? ____", "12", "Coëfficiënt × index = 4 × 3 = 12"),
O("Sam zegt over 9 H₂O: 'Dat zijn negen waterstofatomen.' Wat zijn het wel?", "molecu", "Het zijn negen watermoleculen.", "De coëfficiënt telt moleculen"),
M("Hoeveel atomen telt één molecuul C₃H₈O?", "12", ["11", "3", "24"], "3 + 8 + 1 = 12. Zonder index telt de O één keer mee, vergeet die niet"),
W("Bij SO₂ geldt: achter de S hoort onzichtbaar een index 1.", True, "De index 1 schrijf je nooit op, maar hij telt wel mee"),
W("In 5 CH₄ is de 5 de index.", False, "De 5 staat ervoor en is dus de coëfficiënt"),
M("Hoe noteer je drie losse moleculen methaan?", "3 CH₄", ["C₃H₁₂", "CH₄₃", "C₃H₄"], "Het aantal moleculen zet je vóór de formule. De indexen veranderen niet"),
], [
M("Een bolletjesmodel toont één zwart en twee rode bolletjes aan elkaar (zwart = C, rood = O). Welke formule past?", "CO₂", ["C₂O", "2 CO", "C₂O₂"], "Eén C en twee O. Bij C₂O staat de index bij het verkeerde atoom"),
I("Een atoom heeft 15 protonen en is neutraal. Hoeveel elektronen draaien eromheen? ____", "15", "Neutraal betekent evenveel elektronen als protonen"),
W("De stof O₂ is een verbinding, want elk molecuul heeft twee atomen.", False, "O₂ bevat één atoomsoort, dus zuurstof is geen verbinding"),
M("Welke stof uit dit rijtje is ontleedbaar?", "CH₄", ["O₂", "Cl₂", "N₂"], "Alleen CH₄ heeft twee atoomsoorten. Twee dezelfde atomen maken nog geen verbinding"),
W("Het massagetal van een atoom kan nooit 12,5 zijn.", True, "Je telt hele protonen en neutronen"),
M("Wat gebeurt er met H₂O-moleculen als ijs smelt?", "Ze gaan langs elkaar bewegen", ["Ze vallen uiteen in atomen", "Ze worden zelf vloeibaar", "Ze krijgen een andere formule"], "Het molecuul blijft hetzelfde, alleen de beweging verandert"),
], [
M("Welk element hoort bij de letter N in een formule?", "Stikstof", ["Natrium", "Neon", "Nikkel"], "N = stikstof, Na = natrium, Ne = neon, Ni = nikkel"),
W("De S in H₂SO₄ staat voor stikstof.", False, "S is zwavel. Stikstof is N"),
W("Wie een formule in Japan leest, ziet dezelfde betekenis als in Nederland.", True, "Formules zijn taalonafhankelijk"),
M("Hoe schrijf je een symbool van twee letters?", "Hoofdletter, kleine letter", ["Twee hoofdletters naast elkaar", "Twee kleine letters naast elkaar", "Eerst klein, daarna een hoofdletter"], "Eerst een hoofdletter, daarna een kleine letter"),
])

toets(84, "2.3", "§2.3 Formules uit je hoofd", "🧠", [
M("Ezelsbrug Br I N Cl H O F: hoe komen deze atomen als stof voor?", "In paren", ["Als losse atomen", "In drietallen", "In viertallen"], "Alle zeven vormen moleculen van twee atomen"),
M("Je ademt zuurstof in. Welke formule schrijf je voor dat gas?", "O₂", ["O", "2 O", "O₃"], "De stof is O₂. Een losse O is alleen het atoom"),
M("Een flesje bevat de stof jood. Welke formule zet je op het etiket?", "I₂", ["J₂", "I", "Jo₂"], "Het symbool is I, niet J, en jood komt in paren voor"),
M("Een zwembad ruikt naar chloor. Welke formule heeft die stof?", "Cl₂", ["F₂", "Cl", "C₂"], "Chloor is Cl₂. F₂ is fluor en C is koolstof"),
M("Ammoniak onthoud je als 'één N met drie H'. Wat schrijf je dan?", "NH₃", ["NH₄", "N₃H", "3 NH"], "Eén N en drie H, dus NH₃. NH₄ heeft er een H te veel"),
M("Methaan is aardgas: één C met vier H eromheen. Welke notatie klopt?", "CH₄", ["C₄H₄", "C₄H", "4 CH"], "De index 4 hoort alleen bij H"),
M("Zwavelzuur onthoud je als '2-1-4'. Welke formule krijg je?", "H₂SO₄", ["H₂SO₂", "H₄SO₂", "HS₂O₄"], "Twee H, één S, vier O"),
I("Alcohol is C₂H₆O. Het getal achter de H is ____.", "6", "Alcohol: twee C, zes H, één O"),
W("Met het losse symbool F bedoel je de stof fluor.", False, "F is het atoom, de stof is F₂"),
O("Waarom schrijf je de stof broom als Br₂ en niet als Br?", "twee/paar/paren/molecu", "Broom bestaat uit moleculen van elk 2 atomen: een paar.", "Tabel 2.22"),
], [
I("Tel de kerndeeltjes van chloor met 17 p en 18 n: massagetal = ____.", "35", "17 + 18 = 35"),
W("Waterstofperoxide H₂O₂ en water zijn dezelfde stof.", False, "Andere indexen betekent een andere stof. Water is H₂O"),
M("Welk drietal bestaat alleen uit niet-ontleedbare stoffen?", "H₂, N₂, Fe", ["H₂O, N₂, Fe", "CO, O₂, Cu", "NH₃, F₂, He"], "Elke stof mag maar één atoomsoort bevatten"),
W("Water is een triviale naam.", True, "Het is de alledaagse naam van H₂O"),
I("Hoeveel atomen tel je in 2 SO₂ bij elkaar? ____", "6", "2 × (1 + 2) = 6"),
W("Een stuk koper bestaat op microniveau uit gestapelde losse atomen.", True, "Metalen hebben geen moleculen"),
], [
M("Wat betekent Co, met een kleine o?", "Kobalt", ["Koolstofmono-oxide", "Koper", "Koolstof"], "Co is één atoomsoort, CO zijn er twee"),
W("De letter P is het symbool van fosfor.", True, "P komt van phosphorus"),
M("Welke atoomsoort hoort bij Hg?", "Kwik", ["Helium", "Waterstof", "Zilver"], "Hg = kwik, He = helium, Ag = zilver"),
W("Zilver heeft het symbool Au.", False, "Au is goud. Zilver is Ag"),
])

toets(85, "2.3", "§2.3 Systematische namen", "🏷️", [
M("Stap 1: welk voorvoegsel gebruik je bij index 4?", "tetra", ["tri", "penta", "hexa"], "Mono 1, di 2, tri 3, tetra 4, penta 5, hexa 6"),
M("Stap 2: hoe noem je zuurstof als tweede atoomsoort in een naam?", "oxide", ["zuurstofide", "oxygeen", "sulfide"], "Zuurstof wordt oxide. Sulfide is van zwavel"),
W("Stap 3: staat er vooraan één atoom, dan begint de naam zonder voorvoegsel.", True, "Alleen bij de eerste atoomsoort laat je mono weg"),
M("Geef N₂F₄ een systematische naam.", "Distikstoftetrafluoride", ["Tetrastikstofdifluoride", "Stikstoftetrafluoride", "Distikstoftrifluoride"], "Di hoort bij N, tetra bij F. Elk voorvoegsel blijft bij zijn eigen atoom"),
M("Welke naam past bij NCl₃?", "Stikstoftrichloride", ["Stikstofchloride", "Monostikstoftrichloride", "Tristikstofchloride"], "Het aantal Cl moet in de naam: tri. Vooraan komt geen mono"),
M("Zet koolstoftetrachloride om in een formule.", "CCl₄", ["C₄Cl", "C₄Cl₄", "CCl₂"], "Geen voorvoegsel = 1 C, tetra = 4 Cl"),
M("Zet dijoodmonosulfide om in een formule.", "I₂S", ["IS₂", "J₂S", "I₂S₂"], "Di = 2 I, mono = 1 S. Het symbool van jood is I"),
O("Waarom is 'monozwaveltrioxide' een foute naam voor SO₃?", "vooraan/eerste/begin/geen mono/zonder mono", "Vooraan zet je geen mono.", "Het is zwaveltrioxide"),
W("CO mag je koolstofoxide noemen, zonder voorvoegsel.", False, "Het is koolstofmono-oxide: bij de tweede atoomsoort noem je mono wel"),
I("Lees de naam fosforpentafluoride. Het aantal F is dus ____.", "5", "Penta = 5"),
], [
I("Difosforpentasulfide: tel alle atomen van één zo'n molecuul op. ____", "7", "Di = 2 en penta = 5, samen 7"),
W("Methaan is een systematische naam.", False, "Aan 'methaan' hoor je geen atoomsoorten of aantallen: het is een triviale naam"),
M("Wat vertelt een systematische naam je?", "Welke atomen en hoeveel", ["De kleur en de geur van de stof", "De fase bij kamertemperatuur", "Wie de stof heeft ontdekt"], "Daarom kun je van de naam de formule maken"),
I("Een molecuul SF₆ komt drie keer voor. Hoeveel F-atomen zijn dat? ____", "18", "3 × 6 = 18"),
M("Isotopen van zwavel krijgen in een formule allemaal de letter S. Waarom?", "Ze hebben evenveel protonen", ["Ze hebben evenveel neutronen", "Ze hebben hetzelfde massagetal", "Ze zijn precies even zwaar"], "Het aantal protonen bepaalt de atoomsoort en het symbool"),
W("Een stof met de naam distikstofmono-oxide is een verbinding.", True, "Er zitten twee atoomsoorten in: N en O"),
], [
M("Bij welke groep horen F, Cl, Br en I?", "Halogenen", ["Edelgassen", "Alkalimetalen", "Aardalkalimetalen"], "Groep 17 heet de halogenen"),
W("Het symbool Cl hoort bij calcium.", False, "Cl is chloor. Calcium is Ca"),
W("Fosfor is een niet-metaal.", True, "Fosfor staat in tabel 2.13 bij de niet-metalen"),
M("Welk symbool gebruik je voor natrium?", "Na", ["N", "Nt", "Ni"], "Na = natrium, N = stikstof, Ni = nikkel"),
])

toets(86, "2.3", "§2.3 Molecuulmassa, stap voor stap", "⚖️", [
I("Stap 1: één O-atoom weegt 16,00 u. Drie O-atomen wegen samen ____ u.", "48", "3 × 16,00 = 48,00 u"),
I("Stap 2: bereken N₂ met N = 14,01 u. De molecuulmassa is ____ u.", "28,02", "2 × 14,01 = 28,02 u. Eén atoom rekenen is te weinig", 0.01),
M("Stap 3: welke som geeft de molecuulmassa van H₂S?", "2 × 1,008 + 32,07", ["2 × 1,008 × 32,07", "1,008 + 2 × 32,07", "2 + 1,008 + 32,07"], "Binnen een atoomsoort vermenigvuldig je, daarna tel je op"),
M("Stap 4: hoe zwaar is CH₄? Gebruik C = 12,01 u en H = 1,008 u.", "16,04 u", ["13,02 u", "48,42 u", "49,05 u"], "12,01 + 4 × 1,008 = 16,04 u. Alleen de H telt vier keer"),
I("Nu zelf: SO₂, met S = 32,07 u en O = 16,00 u, weegt ____ u.", "64,07", "32,07 + 2 × 16,00 = 64,07 u", 0.01),
W("Kom je voor H₂O₂ op 1801,6 u uit, dan heb je vermenigvuldigd waar je moest optellen.", True, "Een klein molecuul weegt enkele tientallen u. Tel de atoomsoorten bij elkaar op"),
M("CO₂ weegt 44,01 u, de zuurstof daarin 32,00 u. Welke som geeft het massapercentage O?", "32,00 : 44,01 × 100%", ["44,01 : 32,00 × 100%", "16,00 : 44,01 × 100%", "32,00 × 44,01 : 100%"], "Deel door geheel, keer 100%. Het deel is beide O-atomen"),
M("Een molecuul weegt 96 u, waarvan 24 u koolstof. Welk deel is dat in procenten?", "25%", ["24%", "40%", "75%"], "24 : 96 × 100% = 25%"),
W("De eenheid u is handig omdat een atoom veel te licht is om in gram te rekenen.", True, "1 u is maar 1,66·10⁻²⁷ kg"),
O("Waarom is de molecuulmassa van O₂ niet 16,00 u?", "twee/2/32/dubbel", "Er zitten twee atomen in, dus het is 32,00 u.", "Index 2"),
], [
M("Welke naam hoort bij de formule SF₂?", "Zwaveldifluoride", ["Dizwavelfluoride", "Zwavelfluoride", "Monozwaveldifluoride"], "Eén S zonder mono, twee F met di"),
W("Een proton weegt ongeveer 35 u.", False, "Een proton weegt ongeveer 1 u. 35 is het massagetal van Cl-35"),
M("Welk deeltje mag je bij het optellen van de atoommassa verwaarlozen?", "Het elektron", ["Het proton", "Het neutron", "De atoomkern"], "Een elektron weegt afgerond 0 u"),
W("In 2 H₂O zitten twee zuurstofatomen.", True, "2 × 1 = 2"),
M("Waar vind je de atoommassa van zwavel?", "In het periodiek systeem", ["In de formule van de stof", "In de systematische naam", "In de index achter de S"], "Elk vakje vermeldt de atoommassa"),
W("Een mengsel heeft op microniveau één soort molecuul.", False, "Een mengsel heeft meer soorten. Eén soort is een zuivere stof"),
], [
M("Op een zak kunstmest staat de letter K. Welk element is dat?", "Kalium", ["Kobalt", "Koper", "Kwik"], "K = kalium, Co = kobalt, Cu = koper, Hg = kwik"),
M("Wat zijn de rijen van het periodiek systeem, van links naar rechts gelezen?", "Perioden", ["Groepen", "Halogenen", "Isotopen"], "Rijen zijn perioden, kolommen zijn groepen"),
M("Pb op een oude waterleiding: welk metaal is dat?", "Lood", ["Tin", "Platina", "IJzer"], "Pb = lood, Sn = tin, Pt = platina"),
W("Helium hoort bij de halogenen.", False, "Helium is een edelgas, groep 18"),
])

toets(87, "2.4", "§2.4 Deeltjes en atoommodellen", "⚛️", [
M("Stap 1: welk deeltje is positief?", "Proton", ["Neutron", "Elektron", "Molecuul"], "Proton = positief"),
M("Stap 2: welk deeltje heeft lading 0?", "Neutron", ["Proton", "Elektron", "Atoomkern"], "Neutron = neutraal. Een elektron is 1−"),
M("Stap 3: wat vind je in de wolk rond het midden van een atoom?", "Elektronen", ["Protonen", "Neutronen", "Moleculen"], "Protonen en neutronen zitten in de kern"),
W("De naam atoomkern betekent hetzelfde als het woord proton.", False, "De kern is de plek, protonen en neutronen zijn de deeltjes daarin"),
I("Een neutraal atoom telt 9 elektronen. Het aantal protonen is ____.", "9", "Neutraal: plus en min zijn even vaak aanwezig"),
W("Een elektron telt bij de massa mee als afgerond 0 u.", True, "Protonen en neutronen leveren de massa"),
M("Wiens model lijkt op een krentenbol?", "Thomson", ["Dalton", "Rutherford", "Mendelejev"], "Dalton: knikker, Thomson: krentenbol, Rutherford: kern met wolk"),
M("Welke volgorde van modellen is van oud naar nieuw?", "Dalton, Thomson, Rutherford", ["Thomson, Dalton, Rutherford", "Rutherford, Thomson, Dalton", "Dalton, Rutherford, Thomson"], "1808, 1904, 1911. Dalton is dus het oudste model"),
O("Kim zegt: 'Een neutron is negatief.' Verbeter dit kort.", "geen/neutraal/ongeladen/nul", "Een neutron heeft geen lading.", "Alleen een elektron is negatief"),
I("Een atoom heeft 5 protonen en 6 neutronen. Als het neutraal is, zijn er ____ elektronen.", "5", "Elektronen = protonen. Tel de neutronen niet mee, 11 is het massagetal"),
], [
M("Het goudfolie-experiment: wat deden bijna alle deeltjes?", "Er recht doorheen gaan", ["Allemaal terugkaatsen", "In de folie blijven steken", "De folie laten smelten"], "Een atoom is vooral lege ruimte"),
W("Een model is een versimpeling en klopt dus niet tot in elk detail.", True, "Een model is een versimpelde weergave van de werkelijkheid"),
I("Een ijzerdeeltje heeft 26 protonen en lading 3+. Het aantal elektronen is ____.", "23", "3+ betekent drie elektronen minder: 26 − 3 = 23. Een aantal is nooit negatief"),
W("Haal je een elektron uit een atoom, dan wordt het deeltje negatief.", False, "Je haalt min weg, dus het wordt positief"),
M("In 3 Cl₂: wat is de 3?", "De coëfficiënt", ["De index", "Het massagetal", "Het atoomnummer"], "Het getal ervoor is de coëfficiënt"),
M("Wie vond het derde kerndeeltje, het deeltje zonder lading?", "Een collega van Rutherford", ["Joseph John Thomson zelf", "John Dalton in 1808", "Dmitri Mendelejev in 1869"], "Ongeveer 30 jaar na Thomson. Thomson hoort bij het elektron"),
], [
M("Hoe herken je een ball-stickmodel?", "Aan de stokjes", ["Aan bolletjes die elkaar raken", "Aan de krenten", "Aan de elektronenwolk"], "Ball = bol, stick = stok"),
W("In een space-filling model raken de getekende atomen elkaar.", True, "Er zitten geen stokjes tussen"),
M("Welke kleur krijgt koolstof in molecuultekeningen?", "Zwart", ["Rood", "Wit", "Blauw"], "C zwart, O rood, H wit"),
W("Metalen zoals zink bestaan uit zinkmoleculen.", False, "Metalen bestaan uit losse atomen"),
])

toets(88, "2.4", "§2.4 Atoomnummer en massagetal", "🧮", [
M("Stap 1: zuurstof is nummer 8. Wat weet je dan zeker?", "Er zijn 8 protonen", ["Er zijn 4 protonen", "Er zijn 8 neutronen", "De massa is 8 u"], "Atoomnummer = protonen. Je hoeft niets te halveren"),
I("Stap 2: magnesium is nummer 12. Een neutraal Mg-atoom heeft ____ elektronen.", "12", "Elektronen = protonen = 12"),
M("Stap 3: welke deeltjes tel je voor het massagetal?", "Protonen plus neutronen", ["Protonen plus elektronen", "Neutronen plus elektronen", "Alle drie de soorten samen"], "Alleen de deeltjes in de kern"),
I("Stap 4: aluminium-27 is nummer 13. Het aantal neutronen is ____.", "14", "27 − 13 = 14"),
M("Fluor-19 heeft nummer 9. Welke samenstelling klopt?", "9 p, 10 n, 9 e", ["9 p, 19 n, 9 e", "10 p, 9 n, 10 e", "9 p, 10 n, 19 e"], "p = e = 9 en n = 19 − 9 = 10"),
W("Het periodiek systeem is gesorteerd op het aantal protonen.", True, "Dat is het atoomnummer, niet het massagetal"),
W("Een atoom met 11 protonen moet ook 11 neutronen hebben.", False, "Neutronen mogen afwijken: Na-23 heeft er 12"),
O("Hoe reken je uit hoeveel neutronen P-31 heeft? Fosfor is nummer 15.", "16/min/aftrek/verschil", "Je doet 31 min 15, dat is 16.", "Massagetal − atoomnummer"),
M("Een kern bevat 20 protonen en 22 neutronen. Wat is het massagetal?", "42", ["20", "22", "62"], "20 + 22 = 42. Elektronen tel je niet mee"),
M("In welke notatie staan massagetal en atoomnummer van C-14 goed?", "¹⁴₆C", ["⁶₁₄C", "¹⁴₈C", "⁸₆C"], "Massagetal boven, atoomnummer onder. 8 is het aantal neutronen"),
], [
M("Welke formule geeft één molecuul met twee N-atomen en één O-atoom?", "N₂O", ["NO₂", "2 NO", "N₂O₂"], "De 2 staat achter het atoom waar hij bij hoort"),
I("In 5 N₂ zitten ____ stikstofatomen.", "10", "5 × 2 = 10"),
W("CS₂ heet koolstofdisulfide.", True, "Eén C zonder mono, twee S = disulfide"),
W("De stof waterstof noteer je als H.", False, "De stof is H₂"),
M("Tennessine is nummer 117. Hoeveel neutronen heeft Ts-294?", "177", ["117", "294", "411"], "294 − 117 = 177"),
M("Hoe weet je dat twee atomen van dezelfde soort zijn?", "Gelijk aantal protonen", ["Gelijk aantal neutronen", "Gelijk massagetal", "Gelijke massa in u"], "Protonen bepalen de atoomsoort"),
], [
M("Hoe heet de groep waar Na en K in staan?", "Alkalimetalen", ["Aardalkalimetalen", "Edelgassen", "Halogenen"], "Groep 1. Groep 2 heet aardalkalimetalen, met 'al' erin"),
W("Mendelejev heeft alle 118 atoomsoorten ontdekt.", False, "Hij rangschikte ze, veel zijn later ontdekt"),
W("Mg en Mn zijn twee verschillende metalen.", True, "Magnesium en mangaan"),
M("IJzer komt van het Latijnse ferrum. Wat wordt dus het symbool?", "Fe", ["IJ", "Ir", "F"], "Fe van ferrum. F is fluor"),
])

toets(89, "2.4", "§2.4 Isotopen en relatieve atoommassa", "👯", [
M("Stap 1: bekijk C-12 en C-13. Wat is er anders?", "Eén neutron", ["Eén proton", "Eén elektron", "Het symbool"], "Beide hebben 6 protonen, C-13 heeft een neutron meer"),
M("Stap 2: wat is bij Li-6 en Li-7 gelijk?", "Het atoomnummer", ["Het aantal neutronen", "Het massagetal", "De massa in u"], "Isotopen delen protonen en atoomnummer, nooit het aantal neutronen"),
I("Stap 3: waterstof is nummer 1. Tritium, H-3, heeft ____ neutronen.", "2", "3 − 1 = 2"),
W("O-16 en O-18 hebben allebei 8 protonen.", True, "Het blijft zuurstof, nummer 8"),
W("N-14 en C-14 zijn isotopen van elkaar.", False, "Het massagetal is gelijk, maar de atoomsoort niet"),
M("Van 100 natuurlijke Cl-atomen zijn er ongeveer 25 Cl-37. Hoeveel zijn dan Cl-35?", "75", ["25", "35", "50"], "100 − 25 = 75. De lichte isotoop komt het meest voor"),
M("Geen enkel Cl-atoom weegt 35,45 u. Hoe komt het periodiek systeem daar toch aan?", "Het is een gewogen gemiddelde", ["Een atoom bevat halve neutronen", "De protonen zijn niet even zwaar", "De elektronen wegen samen 0,45 u"], "Cl-35 en Cl-37 komen niet even vaak voor"),
I("Boor: 20% weegt 10 u en 80% weegt 11 u. Het gewogen gemiddelde is ____ u.", "10,8", "0,20 × 10 + 0,80 × 11 = 10,8 u", 0.01),
O("Wat is het enige verschil in de kern van Br-79 en Br-81?", "neutron", "Br-81 heeft twee neutronen meer.", "Protonen blijven gelijk"),
M("Welk paar bestaat uit isotopen?", "Ne-20 en Ne-22", ["Na-23 en Ne-23", "O₂ en O₃", "Co en CO"], "Zelfde atoomsoort, ander massagetal"),
], [
W("Een los atoom O-17 heeft massagetal 8.", False, "17 is het massagetal, 8 het atoomnummer"),
M("Koolstof heeft gemiddeld 12,01 u. Welke isotoop komt dan het meest voor?", "C-12", ["C-13", "C-14", "Alle drie evenveel"], "Het gemiddelde ligt vlak bij 12"),
I("Twee Br-79-atomen vormen een molecuul Br₂. Dat weegt ____ u.", "158", "2 × 79 = 158 u"),
M("In 2 CO₂: hoeveel O-atomen zie je?", "4", ["2", "3", "6"], "Coëfficiënt × index = 2 × 2. Zes is het totaal van alle atomen"),
W("PF₃ heet fosfortrifluoride.", True, "Eén P zonder mono, drie F met tri"),
M("Welke atoomkern is het zwaarst?", "8 p en 10 n", ["8 p en 8 n", "9 p en 8 n", "7 p en 9 n"], "18 kerndeeltjes is hier het meest"),
], [
W("Kobalt en koper hebben hetzelfde symbool.", False, "Kobalt is Co, koper is Cu"),
W("Argon is een edelgas.", True, "Ar staat in groep 18"),
M("Sn is het symbool van welk metaal?", "Tin", ["Zink", "Zilver", "Lood"], "Sn = tin, Zn = zink, Ag = zilver, Pb = lood"),
M("Waar staan stoffen met vergelijkbare eigenschappen, volgens hun atoomsoort?", "In dezelfde groep", ["In dezelfde periode", "Naast elkaar in een rij", "Altijd bij de metalen"], "Een groep is een kolom"),
])

toets(90, "mix", "§2.1 + §2.2 Je eerdere fouten", "🔁", [
M("Stap 1: je ruikt soep. Op welk niveau neem je dat waar?", "Macro", ["Micro", "Atomair", "Moleculair"], "Alles wat je met zintuigen merkt, is macro"),
M("Stap 2: 'Er zit één soort molecuul in de pot.' Welk niveau is dit?", "Micro", ["Macro", "Zintuiglijk", "Waarneembaar"], "Moleculen kun je niet waarnemen, ook niet bij een zuivere stof"),
M("Je meet dat kaarsvet een smelttraject heeft. Wat is die meting?", "Een macrowaarneming", ["Een microbeschrijving", "Een atoommodel", "Een molecuulformule"], "Wat je meet, neem je waar"),
M("Welk gedrag hoort bij moleculen in een glas limonade?", "Dichtbij en schuivend", ["Ver uit elkaar en snel", "Op een vaste plek trillend", "Helemaal stilstaand"], "Vloeistof: tegen elkaar aan, wel langs elkaar"),
W("Ook in een ijsklontje staan de moleculen niet stil.", True, "Ze trillen op hun plek"),
I("Een triljoen: schrijf een 1 en daarna ____ nullen.", "18", "Miljoen 6, miljard 9, biljoen 12, biljard 15, triljoen 18"),
M("In een monster zitten drie soorten moleculen. Hoe noem je het monster?", "Mengsel", ["Verbinding", "Zuivere stof", "Niet-ontleedbare stof"], "Meer soorten moleculen = mengsel. Bij een verbinding gaat het om atoomsoorten in één molecuul"),
W("Brons is een verbinding van koper en tin.", False, "Een legering is een mengsel van metalen, zonder moleculen"),
M("Wat is een ander woord voor ontleedbare stof?", "Verbinding", ["Element", "Legering", "Oplossing"], "Ontleedbaar = meerdere atoomsoorten in het molecuul"),
O("Waarom kun je een gas meestal niet zien? Denk aan de moleculen.", "ver uit/ver van/afstand/uit elkaar/verspreid/ruimte", "De deeltjes zitten ver uit elkaar.", "Ze zijn niet kleiner dan in een vloeistof"),
], [
I("Een molecuul glucose is C₆H₁₂O₆. Het aantal atomen hierin is ____.", "24", "6 + 12 + 6 = 24"),
W("Bij koken breken watermoleculen in waterstof en zuurstof.", False, "De moleculen blijven H₂O, ze gaan alleen uit elkaar"),
M("Vast koolstofdioxide wordt direct gas. Welke overgang is dat?", "Sublimeren", ["Condenseren", "Verdampen", "Stollen"], "Vast naar gas. Condenseren is gas naar vloeibaar"),
W("De stikstofcrisis gaat over verbindingen zoals NH₃ en NO₂.", True, "Niet over het gas N₂ of een tekort"),
I("Oganesson is de laatste atoomsoort van het systeem, met nummer ____.", "118", "Er zijn 118 atoomsoorten"),
W("Olie die op water drijft, is een beschrijving op microniveau.", False, "Dat zie je, dus macro"),
], [
M("Welke van deze vier is een metaal?", "Mangaan", ["Broom", "Zwavel", "Argon"], "Mn is een metaal. Broom is een halogeen, geen edelgas"),
M("Welk paar is goud en daarna zilver?", "Au, Ag", ["Ag, Au", "Go, Zi", "Au, Al"], "Au = goud, Ag = zilver"),
W("IJzer in je bloed zit gebonden in een verbinding.", True, "Dat is hemoglobine"),
M("Waarvoor is een model van het zonnestelsel nuttig?", "Het echte is te groot", ["Het echte is te klein", "Het model is precies echt", "Je ziet dan moleculen"], "Modellen gebruik je voor te kleine én te grote dingen"),
])

toets(91, "begrippen", "Begrippentoets H2 met personen en jaartallen", "🔑", [
M("Welk begrip past bij: 'het getal vóór een formule'?", "Coëfficiënt", ["Index", "Massagetal", "Atoomnummer"], "Vóór = coëfficiënt, rechtsonder = index"),
M("Welk begrip past bij: 'het kleine getal rechtsonder, dat atomen telt'?", "Index", ["Coëfficiënt", "Massagetal", "Lading"], "De index hoort bij één atoomsoort"),
I("Zelfde atoomnummer, ander massagetal: zulke atomen noem je ____.", "isotopen|isotoop", "Alleen het aantal neutronen verschilt"),
W("De relatieve atoommassa houdt rekening met hoe vaak elke variant van het atoom voorkomt.", True, "Het is een gewogen gemiddelde"),
M("Welke omschrijving past bij massagetal?", "Aantal kerndeeltjes", ["Aantal protonen alleen", "Aantal deeltjes in de wolk", "Massa van een molecuul"], "Protonen plus neutronen"),
M("Welke omschrijving past bij atoomnummer?", "Aantal protonen", ["Aantal neutronen", "Aantal kerndeeltjes", "Aantal atomen per molecuul"], "Uniek voor elke atoomsoort"),
W("Een systematische naam is de alledaagse naam van een stof.", False, "Dat is de triviale naam"),
I("Namen als ammoniak en alcohol zijn ____ namen.", "triviale|triviaal", "Alledaagse namen"),
M("Welk begrip past bij: 'een stof met moleculen uit één atoomsoort'?", "Niet-ontleedbare stof", ["Ontleedbare stof", "Verbinding", "Emulsie"], "Eén atoomsoort kun je niet verder ontleden"),
O("Leg het woord molecuulmassa in een paar woorden uit.", "optel/samen/som/totaal/totale/alle atomen", "De massa van alle atomen samen.", "In u"),
], [
M("Wie hoort bij het jaar 1808 en de knikker?", "John Dalton", ["Ernest Rutherford", "J.J. Thomson", "Stanley Miller"], "Dalton: massief en ondeelbaar"),
M("Welke ontdekking hoort bij Thomson, 1904?", "Het elektron", ["De atoomkern", "Het neutron", "Het periodiek systeem"], "Hij liet zien dat een atoom deelbaar is"),
M("Wat bedacht Rutherford in 1911?", "Een kern met een wolk", ["Een massieve ondeelbare bol", "Een bol deeg met krenten", "Een tabel met groepen"], "Het atoom is vooral lege ruimte"),
I("Mendelejev publiceerde zijn overzicht in het jaar ____.", "1869", "Het periodiek systeem, 1869", 0),
W("Miller en Urey onderzochten hoe leven op aarde kan zijn ontstaan.", True, "Ze maakten met vonken grotere moleculen"),
W("Het Griekse atomos betekent 'deelbaar'.", False, "Het betekent ondeelbaar"),
], [
M("Welk begrip hoort bij alles wat je kunt zien, horen, ruiken of voelen?", "Macroniveau", ["Microniveau", "Atoommodel", "Formuletaal"], "Macro = waarneembaar"),
W("Op microniveau gebruik je een model om moleculen en atomen voor te stellen.", True, "Micro kun je niet waarnemen, daarom gebruik je een versimpelde weergave"),
W("Een periode is een kolom van het periodiek systeem.", False, "Een periode is een rij, een groep is een kolom"),
M("Wat is de speciale naam van groep 2?", "Aardalkalimetalen", ["Alkalimetalen", "Edelmetalen", "Halogenen"], "Let op de spelling: aard-alkali-metalen"),
])

toets(92, "mix", "Eindtoets H2: alles door elkaar", "🏁", [
M("Lachgas is N₂O. Hoe heet het officieel?", "Distikstofmono-oxide", ["Stikstofdioxide", "Distikstofoxide", "Monostikstofdioxide"], "Di voor N, en achteraan noem je mono wel"),
I("Lachgas N₂O, met N = 14,01 en O = 16,00: één molecuul weegt ____ u.", "44,02", "2 × 14,01 + 16,00 = 44,02 u", 0.01),
M("Een ballon bevat 8 moleculen van de stof waterstof. Hoe noteer je dat?", "8 H₂", ["H₈", "8 H", "H₁₆"], "Coëfficiënt 8, en de stof is H₂"),
I("Hoeveel zuurstofatomen bevat 5 H₂SO₄? ____", "20", "5 × 4 = 20"),
M("Zwavel-34 is nummer 16. Welke kern hoort erbij?", "16 p en 18 n", ["18 p en 16 n", "16 p en 34 n", "34 p en 16 n"], "34 − 16 = 18 neutronen"),
W("K-39 en K-41 verschillen twee neutronen.", True, "Zelfde protonen, massagetal 2 hoger"),
W("SiF₄ heet monosiliciumtetrafluoride.", False, "Siliciumtetrafluoride, vooraan geen mono"),
M("Wat is het massapercentage C in een molecuul van 60 u met 24 u koolstof?", "40%", ["24%", "36%", "60%"], "24 : 60 × 100% = 40%"),
O("Wat geeft de 4 aan in 4 CO₂?", "molecu", "Er zijn vier moleculen koolstofdioxide.", "Coëfficiënt"),
M("Welke formule is van zwaveldioxide?", "SO₂", ["S₂O", "SiO₂", "2 SO"], "Eén S, twee O. Si is silicium"),
], [
M("Een suikerklont verdwijnt in thee. Wat gebeurt op microniveau?", "Suikermoleculen verspreiden zich", ["Suikermoleculen worden watermoleculen", "Suikermoleculen houden op te bestaan", "De suiker vormt een aparte onderlaag"], "Ze zitten gelijkmatig tussen de watermoleculen"),
M("Een damp verspreidt zich door het lokaal. Hoe verklaar je dat?", "Losse moleculen bewegen", ["Eén groot deeltje zweeft rond", "Het licht neemt de geur mee", "De moleculen groeien steeds"], "Veel kleine deeltjes bewegen vrij"),
W("Gasmoleculen botsen af en toe.", True, "Ze blijven daarna niet bij elkaar"),
W("Alle stoffen bestaan uit moleculen.", False, "Metalen en edelgassen bestaan uit losse atomen"),
I("Vloeibare stikstof is −196 °C. Dat is ____ K.", "77", "−196 + 273 = 77 K"),
M("Welke bewering over een appel met ijzer klopt?", "Het ijzer zit er niet als metaal in", ["Er zitten kleine spijkertjes in", "Er zitten ijzermoleculen in", "Het ijzer maakt hem magnetisch"], "Het zijn geladen ijzerdeeltjes, geen stukjes metaal"),
], [
M("Krypton staat in groep 18. Met welke atoomsoort lijkt het?", "Neon", ["Natrium", "Broom", "Stikstof"], "Beide zijn edelgassen"),
W("Si is het symbool van silicium.", True, "Si is silicium, S is zwavel"),
W("Een atoomsoort met één letter als symbool is altijd een niet-metaal.", False, "U is uraan, een metaal"),
M("Zn zit in zonnebrand. Welke atoomsoort is dat?", "Zink", ["Tin", "Zilver", "Zwavel"], "Zn = zink"),
])


def main():
    paden = {nr: os.path.join(B.ROOT, f"examen_h2_{nr}.js") for nr in T}
    assert not any(os.path.exists(p) for p in paden.values()), "toets bestaat al — nooit overschrijven"
    for nr, (par, titel, icoon, vr) in T.items():
        soort = [v["type"] for v in vr]
        assert [soort.count(s) for s in ("mc", "waaronwaar", "invul", "open")] == [10, 6, 3, 1], (nr, [soort.count(s) for s in ("mc", "waaronwaar", "invul", "open")])
        assert sum(v.get("antwoord") is False for v in vr if v["type"] == "waaronwaar") == 3, (nr, "3 onwaar")
        vr = B.plaats([dict(v) for v in vr], random.Random(f"sch_h2_zwakte_20261122_{nr}"))
        ex = {"id": f"ex-h3-sch-h2-{nr}", "titel": f"Toets {nr} — {titel}", "vak": "Scheikunde · HAVO 3 (H2)", "hoofdstuk": 2,
              "paragraaf": par, "icoon": icoon, "duurMin": 25,
              "vragen": [{"id": f"sch-h2-{nr}_v{i}", **v} for i, v in enumerate(vr, 1)]}
        with open(paden[nr], "x", encoding="utf-8") as f:
            f.write("/* Examen conform DURU ENGINE_SPEC (HAVO 3 Scheikunde H2) — gegenereerd door tools/gen_scheikunde_h2_zwakte_83_92.py */\n")
            f.write("DURU.registerExamen(" + json.dumps(ex, ensure_ascii=False, indent=2) + ");\n")
        print(nr, "langste %d/%d" % B.langste_aandeel(vr))


if __name__ == "__main__":
    main()
