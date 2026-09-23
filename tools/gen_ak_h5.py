"""
Script om Aardrijkskunde Hoofdstuk 5 (Gewapende conflicten) onderwerpen te genereren:
- 5 Onderwerpen (h5_1.js t/m h5_5.js)
Gebaseerd op buiteNLand 3 HAVO Hoofdstuk 5 (Gewapende conflicten, p. 194-234).
"""
import os
import json

BASE_DIR = 'havo3/aardrijkskunde/js/data'

ONDERWERPEN = [
    {
        'file': 'h5_1.js',
        'id': 'ak-h5-1',
        'hoofdstuk': 5,
        'paragraaf': '5.1',
        'titel': 'Wapengeweld wereldwijd',
        'korteUitleg': 'Definitie van gewapende conflicten, soevereiniteit, territorium en moderne oorlogsvoering.',
        'icoon': '🌍',
        'kleur': 'h5-thema',
        'theorie': """<h3>5.1 Wapengeweld wereldwijd</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Gewapend conflict, territorium, soevereiniteit, volk, natiestaat, binnenlands conflict, internationaal conflict, geïnternationaliseerd conflict, cyberoorlogsvoering.
</div>

<h4>1. Wat is een gewapend conflict?</h4>
<p>In de internationale geografie en vredesstudies spreken we van een <b>gewapend conflict</b> wanneer er bij aanhoudende gewelddadige strijd tussen partijen (regeringen of gewapende groepen) ten minste <b>25 dodelijke slachtoffers</b> in één kalenderjaar vallen. Als het aantal doden oploopt tot meer dan 1.000 per jaar, spreken we van een volwaardige <b>oorlog</b>.</p>
<p>Volgens het Handvest van de Verenigde Naties (1945) is het voeren van oorlog in principe verboden. Landen moeten conflicten vreedzaam oplossen via diplomatie, bemiddeling of het Internationaal Gerechtshof in Den Haag. Alleen bij zelfverdediging of met uitdrukkelijke toestemming van de VN-Veiligheidsraad mag een staat militair geweld inzetten.</p>

<h4>2. Territorium, volk en staat</h4>
<p>Veel conflicten gaan over controle over land en mensen:</p>
<ul>
  <li><b>Territorium:</b> Het begrensde grondgebied waarover een staat of groep de soevereiniteit (hoogste macht) opeist. Dit omvat niet alleen het landoppervlak, maar ook de territoriale wateren en het luchtruim.</li>
  <li><b>Volk:</b> Een groep mensen die zich met elkaar verbonden voelt door een gemeenschappelijke cultuur, taal, religie of gedeelde geschiedenis.</li>
  <li><b>Natiestaat:</b> Een situatie waarin de grenzen van een staat vrijwel precies samenvallen met het woongebied van één dominant volk (zoals IJsland of Japan). De meeste staten in de wereld zijn echter <i>multinationale staten</i>, waar meerdere volkeren binnen dezelfde landsgrenzen wonen.</li>
</ul>

<h4>3. Vormen van conflicten</h4>
<p>We onderscheiden drie hoofdtypen gewapende conflicten:</p>
<ul>
  <li><b>Binnenlands conflict (burgeroorlog):</b> Strijd tussen de officiële regering van een land en een of meer gewapende binnenlandse opstandelingen of rebellengroepen, of tussen bevolkingsgroepen onderling binnen één land.</li>
  <li><b>Internationaal conflict:</b> Een gewapende strijd tussen twee of meer soevereine staten (bijvoorbeeld de Russische invasie in Oekraïne).</li>
  <li><b>Geïnternationaliseerd conflict:</b> Een binnenlands conflict waarbij buitenlandse mogendheden zich rechtstreeks met troepen, wapens of geld mengen in de strijd (zoals in Syrië, Jemen en Libië).</li>
</ul>

<h4>4. Moderne oorlogsvoering</h4>
<p>Oorlogvoering beperkt zich tegenwoordig niet meer tot tanks en infanterie op het slagveld. In de 21e eeuw zien we een sterke toename van <b>hybride oorlogvoering</b>. Dit omvat grootschalige <i>cyberaanvallen</i> op elektriciteitsnetten en ziekenhuizen, desinformatiecampagnes op sociale media om de bevolking van de tegenstander te ontwrichten, economische sancties en sabotage van onderzeese internet- en pijpleidingen.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Vanaf hoeveel gewelddadige doden per kalenderjaar spreekt de wetenschap formeel van een gewapend conflict?',
                'opties': [
                    'Ten minste 25 doden per jaar',
                    'Precies 100 doden per jaar',
                    'Minimaal 1.000 doden per jaar',
                    'Er is geen enkel minimumaantal vereist'
                ],
                'antwoord': 0,
                'uitleg': 'Volgens de internationale Uppsala Conflict Data Program-norm ligt de drempel op minimaal 25 doden per jaar.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat verstaat men in de geografie onder een natiestaat?',
                'opties': [
                    'Een land zonder enige vorm van regering',
                    'Een staat waarvan de grenzen samenvallen met het leefgebied van één duidelijk herkenbaar volk',
                    'Een eiland dat door piraten wordt bestuurd',
                    'Een verdrag tussen alle landen van de Verenigde Naties'
                ],
                'antwoord': 1,
                'uitleg': 'In een natiestaat vallen de culturele natie (het volk) en de geografische staat (het territorium) samen.'
            },
            {
                'type': 'mc',
                'vraag': 'Hoe noemen we een burgeroorlog waarbij buitenlandse regeringen actief ingrijpen met troepen, wapens of militaire steun?',
                'opties': [
                    'Een cyberconflict',
                    'Een koude oorlog',
                    'Een geïnternationaliseerd conflict',
                    'Een lokaal grensincident'
                ],
                'antwoord': 2,
                'uitleg': 'Buitenlandse militaire inmenging transformeert een interne burgeroorlog in een geïnternationaliseerd conflict.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke niet-militaire tactiek maakt deel uit van moderne hybride oorlogsvoering?',
                'opties': [
                    'Het gebruik van middeleeuwse blijden en katapulten',
                    'Het bouwen van forten en loopgraven langs de grens',
                    'Grootschalige cyberaanvallen op infrastructuur en het verspreiden van desinformatie',
                    'Het organiseren van sportwedstrijden tussen landen'
                ],
                'antwoord': 2,
                'uitleg': 'Hybride oorlogsvoering combineert conventionele wapens met cyberaanvallen, sabotage en beïnvloeding van verkiezingen.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat omvat het territorium van een soevereine staat naast het landoppervlak?',
                'opties': [
                    'Alleen de hoofdwegen en vliegvelden',
                    'Het luchtruim boven het land en de aansluitende territoriale wateren',
                    'Alle ambassades in de hele wereld',
                    'De gehele openbare ruimte van alle buurlanden'
                ],
                'antwoord': 1,
                'uitleg': 'Het staatsgebied reikt tot in het luchtruim en omvat bij kuststaten een zone van territoriale wateren (tot 12 zeemijl).'
            },
            {
                'type': 'mc',
                'vraag': 'Wanneer mag een land volgens het Handvest van de Verenigde Naties rechtmatig geweld gebruiken tegen een andere staat?',
                'opties': [
                    'Wanneer de buurman rijkere grondstoffen heeft',
                    'Uitsluitend uit zelfverdediging of met een resolutie van de VN-Veiligheidsraad',
                    'Zodra een president dat via sociale media aankondigt',
                    'Nooit, ook niet bij zelfverdediging'
                ],
                'antwoord': 1,
                'uitleg': 'Geweld is volgens internationaal recht verboden behalve bij individuele of collectieve zelfverdediging of VN-mandaat.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'De meeste landen in de wereld zijn pure natiestaten waar slechts één etnische bevolkingsgroep woont.',
                'antwoord': False,
                'uitleg': 'Onwaar: de meeste staten zijn multinationaal en herbergen diverse minderheden en volkeren binnen hun grenzen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'In de westerse wereld komen tegenwoordig helemaal geen gevolgen of dreigingen van gewapende conflicten meer voor.',
                'antwoord': False,
                'uitleg': 'Onwaar: westerse landen zijn direct en indirect betrokken via allianties (NAVO), wapenleveranties, vluchtelingenopvang en cyberdreigingen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Het Internationaal Gerechtshof in Den Haag behandelt geschillen tussen soevereine staten over onder andere land- en zeegrenzen.',
                'antwoord': True,
                'uitleg': 'Waar: het Vredespaleis in Den Haag is de zetel van het voornaamste gerechtelijke orgaan van de VN.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welk begrip duidt op het begrensde grondgebied waarover een staat het hoogste gezag uitoefent?',
                'antwoord': 'territorium',
                'uitleg': 'Het territorium is het soevereine staatsgebied dat door internationale grenzen wordt omsloten.'
            }
        ]
    },
    {
        'file': 'h5_2.js',
        'id': 'ak-h5-2',
        'hoofdstuk': 5,
        'paragraaf': '5.2',
        'titel': 'Oorzaken van gewapende conflicten',
        'korteUitleg': 'Economische, culturele, politieke en demografische dimensies van conflicten.',
        'icoon': '⚖️',
        'kleur': 'h5-thema',
        'theorie': """<h3>5.2 Oorzaken van gewapende conflicten</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Economische dimensie, grondstoffenvloek, culturele dimensie, etniciteit, koloniale grenzen, demografische dimensie (jeugdbulge), politieke dimensie, fragile state, threat multiplier.
</div>

<h4>1. Meerdere dimensies van een conflict</h4>
<p>Gewapende conflicten hebben zelden één enkele oorzaak. Vaak is er sprake van een complex samenspel van verschillende geografische dimensies:</p>

<h4>2. Economische dimensie: Grondstoffen en armoede</h4>
<p>Wanneer grondstoffen schaars of juist enorm waardevol zijn, neemt het risico op conflict toe. Paradoxaal genoeg leiden rijke voorraden aan delfstoffen (zoals ruwe aardolie, diamant, goud, koper of coltan) in ontwikkelingslanden vaak tot burgeroorlogen en corruptie in plaats van welvaart. Dit verschijnsel heet de <b>grondstoffenvloek</b> (<i>resource curse</i>). Rebellengroepen en corrupte elites vechten om de controle over mijnen en boorlocaties om hun privémilities en wapens te financieren (denk aan Oost-Congo).</p>
<p>Daarnaast leidt chronische armoede, economische ongelijkheid en gebrek aan toekomstperspectief tot grote onvrede onder de bevolking.</p>

<h4>3. Culturele en sociale dimensie: Etniciteit en religie</h4>
<p>Verschillen in taal, afkomst en godsdienst kunnen worden uitgebuit door extremistische leiders:</p>
<ul>
  <li><b>Koloniale grenzen:</b> In Afrika en het Midden-Oosten trokken Europese koloniale mogendheden ooit kaarsrechte grenzen met een liniaal op de kaart, zonder rekening te houden met traditionele leefgebieden van volkeren. Hierdoor werden rivaliserende stammen in één staat bijeengebracht, terwijl andere volkeren (zoals de Koerden) over vier staten werden verscheurd.</li>
  <li><b>Etnische spanningen:</b> In Rwanda leidde het bevoordelen van de Tutsi-minderheid boven de Hutu-meerderheid tijdens de koloniale periode uiteindelijk tot decennia van wraakgevoelens en de gruwelijke genocide van 1994.</li>
</ul>

<h4>4. Demografische en politieke dimensie</h4>
<ul>
  <li><b>Demografische dimensie (de \'jeugdbulge\'):</b> In veel ontwikkelingslanden is meer dan de helft van de bevolking jonger dan 25 jaar. Wanneer miljoenen jongeren geen werk, onderwijs of uitzicht op een woning hebben, zijn zij een makkelijke prooi voor rekrutering door criminele bendes of terroristische bewegingen.</li>
  <li><b>Politieke dimensie en de \'fragile state\':</b> Een <i>fragiele staat</i> (of falende staat) is een land waarvan de centrale overheid niet in staat is de wet te handhaven, basisvoorzieningen (zoals veiligheid, stroom en zorg) te bieden of haar grondgebied te controleren (zoals Somalië, Jemen en Haïti).</li>
  <li><b>Threat multiplier (klimaatverandering):</b> Klimaatopwarming en aanhoudende droogte veroorzaken honger en watertekorten. Dit wakkert bestaande spanningen tussen boeren en nomadische herders (zoals in de Sahel) aan tot gewelddadige confrontaties.</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat houdt de zogeheten grondstoffenvloek in bij ontwikkelingslanden?',
                'opties': [
                    'Landen met veel waardevolle delfstoffen hebben vaak meer armoede, corruptie en geweld dan landen zonder delfstoffen',
                    'Delfstoffen verdwijnen vanzelf als ze worden opgegraven',
                    'Mijnen stoten giftige dampen uit die iedereen betoveren',
                    'Grondstoffen kunnen in ontwikkelingslanden niet verhandeld worden'
                ],
                'antwoord': 0,
                'uitleg': 'Rijkdom aan delfstoffen lokt hebzucht, corruptie en gewapende strijd tussen milities uit.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom veroorzaakten de grenzen die Europese koloniale machten in Afrika trokken na de dekolonisatie zoveel conflicten?',
                'opties': [
                    'Omdat de grenzen met onzichtbare inkt waren getekend',
                    'Omdat er met linialen rechte lijnen werden getrokken dwars door traditionele leefgebieden van stammen en volkeren',
                    'Omdat alle Afrikanen dezelfde taal spraken',
                    'Omdat de grenzen elk jaar opnieuw verschoven'
                ],
                'antwoord': 1,
                'uitleg': 'Willekeurige koloniale grenzen verdeelden volkeren over meerdere staten of dwongen aartsvijanden samen in één land te leven.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een fragile state (kwetsbare of falende staat)?',
                'opties': [
                    'Een staat die uitsluitend van glas gebouwd is',
                    'Een land waar de centrale overheid de openbare orde niet kan handhaven en basisvoorzieningen niet kan leveren',
                    'Een land dat geen enkel leger bezit',
                    'Een staat die lid is van de Europese Unie'
                ],
                'antwoord': 1,
                'uitleg': 'In een fragile state heeft de overheid het geweldsmonopolie verloren en heersen chaos, milities en armoede.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat bedoelt men met de term jeugdbulge in de demografische analyse van conflictgebieden?',
                'opties': [
                    'Een situatie waarin een onevenredig groot percentage van de bevolking bestaat uit jonge mensen met weinig werk en perspectief',
                    'Een tekort aan basisscholen in een vergrijzend land',
                    'Een plotselinge toename van het aantal bejaarden',
                    'De verplichte militaire diensttijd voor tieners'
                ],
                'antwoord': 0,
                'uitleg': 'Een hoge concentratie werkloze jongeren vergroot de kans op sociale onrust en rekrutering voor gewapende strijd.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom wordt klimaatverandering door defensie-experts een threat multiplier (dreigingsversterker) genoemd?',
                'opties': [
                    'Omdat het weer altijd zonnig is tijdens militaire oefeningen',
                    'Omdat klimaatverandering bestaande problemen zoals waterschaarste, misoogsten en armoede verergert en spanningen doet escaleren',
                    'Omdat soldaten niet tegen regen kunnen',
                    'Omdat orkanen alleen militaire kazernes aanvallen'
                ],
                'antwoord': 1,
                'uitleg': 'Droogte en voedselschaarste creëren extra voedingsbodem voor gewapende conflicten tussen bevolkingsgroepen.'
            },
            {
                'type': 'mc',
                'vraag': 'In welk Afrikaans land leidde de bevoordeling van Tutsi\'s boven Hutu\'s in het verleden tot etnische haat en een genocide?',
                'opties': [
                    'Rwanda',
                    'Marokko',
                    'Zuid-Afrika',
                    'Madagaskar'
                ],
                'antwoord': 0,
                'uitleg': 'In Rwanda barstte in 1994 een gruwelijke volkenmoord los waarbij naar schatting 800.000 Tutsi\'s en gematigde Hutu\'s werden vermoord.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Religieuze meningsverschillen zijn in een gewapend conflict bijna altijd de enige en werkelijke oorzaak van het geweld.',
                'antwoord': False,
                'uitleg': 'Onwaar: religie wordt vaak gebruikt als dekmantel of bindmiddel, terwijl economische en politieke belangen de hoofdoorzaak vormen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'In een fragiele staat kan de regering de bevolking niet beschermen tegen bendegeweld en plunderingen.',
                'antwoord': True,
                'uitleg': 'Waar: het kenmerk van een fragile state is dat het staatsapparaat is ingestort en de rechtsstaat ontbreekt.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Strijd om schaarse waterbronnen en weidegronden tussen herders en landbouwers in de Sahel wordt verergerd door klimaatdroogte.',
                'antwoord': True,
                'uitleg': 'Waar: verwoestijning en droogte drijven nomadische herders naar landbouwgebieden, wat geregeld leidt tot dodelijke vetes.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welke Engelse term gebruikt men voor een staat waarvan het centrale gezag vrijwel volledig is ingestort?',
                'antwoord': 'fragile state',
                'uitleg': 'Een fragile state (falende staat) heeft geen controle meer over wetshandhaving en basisveiligheid.'
            }
        ]
    },
    {
        'file': 'h5_3.js',
        'id': 'ak-h5-3',
        'hoofdstuk': 5,
        'paragraaf': '5.3',
        'titel': 'Gevolgen van gewapende conflicten',
        'korteUitleg': 'Humanitaire rampen, oorlogsrecht, genocide, vluchtelingen en ontheemden.',
        'icoon': '🩹',
        'kleur': 'h5-thema',
        'theorie': """<h3>5.3 Gevolgen van gewapende conflicten</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Humanitaire ramp, oorlogsrecht (Verdragen van Genève), genocide, oorlogsmisdaden, vluchtelingen, ontheemden (IDP\'s), trauma, verwoesting van infrastructuur.
</div>

<h4>1. De humanitaire tol van oorlog</h4>
<p>Gewapende conflicten brengen altijd onmetelijk menselijk leed met zich mee. We spreken van een <b>humanitaire ramp</b> wanneer door oorlog of natuurgeweld het overleven van grote groepen mensen direct wordt bedreigd door gebrek aan voedsel, schoon drinkwater, medische zorg en veilige beschutting.</p>
<p>In moderne conflicten is meer dan 80% van de slachtoffers <b>burger</b>. Vaak worden scholen, ziekenhuizen, waterleidingen en elektriciteitscentrales doelbewust gebombardeerd om de bevolking van de tegenstander te ontmoedigen.</p>

<h4>2. Het internationaal oorlogsrecht</h4>
<p>Om de wreedheden van oorlog te begrenzen, zijn er internationale wetten afgesproken in de <b>Verdragen van Genève</b>. Dit <i>oorlogsrecht</i> stelt strikte regels:</p>
<ul>
  <li>Burgers, ziekenhuizen en medisch personeel mogen nooit doelwit zijn van aanvallen.</li>
  <li>Krijgsgevangenen en gewonde soldaten moeten humaan worden behandeld en mogen niet worden gemarteld of geëxecuteerd.</li>
  <li>Het uithongeren van burgerbevolkingen als oorlogswapen is verboden.</li>
  <li>Chemische, biologische en bepaalde willekeurige wapens (zoals clustermunitie en landmijnen) zijn internationaal verboden.</li>
</ul>
<p>Wanneer strijdende partijen deze regels ernstig schenden, spreken we van <b>oorlogsmisdaden</b> of <b>misdaden tegen de menselijkheid</b>. Verdachten hiervan kunnen worden berecht door het <i>Internationaal Strafhof</i> (ICC) in Den Haag.</p>

<h4>3. Genocide (volkenmoord)</h4>
<p>De zwaarste misdaad onder internationaal recht is <b>genocide</b>: het doelbewust en systematisch uitmoorden van een nationale, etnische, raciale of religieuze groep, geheel of gedeeltelijk. Bekende voorbeelden uit de recente geschiedenis zijn:</p>
<ul>
  <li>De Holocaust tijdens de Tweede Wereldoorlog door de nazi\'s.</li>
  <li>De genocide in Rwanda in 1994 (ongeveer 800.000 Tutsi\'s en gematigde Hutu\'s).</li>
  <li>De massamoord in Srebrenica (Bosnië) in 1995 (ruim 8.000 Bosnische moslimmannen en -jongens).</li>
  <li>De vervolging en uitmoording van de Jezidi\'s in Irak door terreurgroep IS.</li>
</ul>

<h4>4. Vluchtelingen versus ontheemden</h4>
<p>Miljoenen mensen moeten huis en haard verlaten:</p>
<ul>
  <li><b>Vluchteling:</b> Iemand die uit gegronde vrees voor vervolging of geweld een <b>internationale landsgrens</b> is overgestoken en in een ander land bescherming zoekt. Vluchtelingen vallen onder het VN-Vluchtelingenverdrag van 1951 en de UNHCR.</li>
  <li><b>Ontheemde (Internal Displaced Person / IDP):</b> Iemand die zijn woonplaats is ontvlucht, maar <b>binnen de grenzen van het eigen land</b> is gebleven (bijvoorbeeld in provisorische tentenkampen in veiliger provincies). Wereldwijd zijn er aanzienlijk meer ontheemden dan internationale vluchtelingen.</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat is het formele juridische verschil tussen een vluchteling en een ontheemde (IDP)?',
                'opties': [
                    'Een vluchteling is een landsgrens overgestoken; een ontheemde is binnen de eigen landsgrenzen gebleven',
                    'Een vluchteling heeft een paspoort; een ontheemde heeft geen identiteitsbewijs',
                    'Een ontheemde reist altijd per boot; een vluchteling altijd te voet',
                    'Er is juridisch geen enkel verschil tussen beide begrippen'
                ],
                'antwoord': 0,
                'uitleg': 'Vluchtelingen steken een internationale grens over; ontheemden blijven binnen eigen landsgrenzen op de vlucht.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke internationale afspraken vormen de basis voor het humanitair oorlogsrecht?',
                'opties': [
                    'Het Verdrag van Versailles',
                    'De Verdragen van Genève',
                    'Het Klimaatakkoord van Kyoto',
                    'Het Schengenverdrag'
                ],
                'antwoord': 1,
                'uitleg': 'De Verdragen van Genève beschermen personen die niet aan de strijd deelnemen, zoals burgers en gewonden.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is de definitie van genocide volgens het internationaal recht?',
                'opties': [
                    'Het voeren van een verkiezingscampagne met felle debatten',
                    'Het verhogen van invoertarieven op buitenlandse goederen',
                    'Het doelbewust en systematisch uitroeien van een bevolkingsgroep op basis van afkomst, ras of religie',
                    'Het sluiten van een militaire alliantie tussen buurlanden'
                ],
                'antwoord': 2,
                'uitleg': 'Genocide is de geplande fysieke vernietiging van een groep mensen wegens hun etniciteit, geloof of nationaliteit.'
            },
            {
                'type': 'mc',
                'vraag': 'Waar bevindt zich het Internationaal Strafhof (ICC) waar personen worden berecht voor oorlogsmisdaden?',
                'opties': [
                    'In New York',
                    'In Genève',
                    'In Den Haag',
                    'In Brussel'
                ],
                'antwoord': 2,
                'uitleg': 'Den Haag is de internationale stad van vrede en recht en huisvest het ICC.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat gebeurde er in juli 1995 in de Bosnische enclave Srebrenica?',
                'opties': [
                    'Er werd een vredesverdrag ondertekend zonder enig slachtoffer',
                    'Bosnisch-Servische troepen vermoordden ruim 8.000 moslimmannen en -jongens in een genocide',
                    'De Verenigde Naties bouwden een nieuw ziekenhuis',
                    'De stad werd uitgeroepen tot hoofdstad van Europa'
                ],
                'antwoord': 1,
                'uitleg': 'De massamoord van Srebrenica geldt als de ernstigste oorlogsmisdaad in Europa sinds de Tweede Wereldoorlog.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom zijn ontheemden binnen eigen land vaak nog kwetsbaarder dan geregistreerde vluchtelingen over de grens?',
                'opties': [
                    'Omdat ze geen tenten kunnen opzetten',
                    'Omdat ze nog steeds onder de macht vallen van dezelfde regering of milities waarvoor ze moesten vluchten',
                    'Omdat de VN hen verbiedt om eten te kopen',
                    'Omdat het weer in eigen land altijd slechter is'
                ],
                'antwoord': 1,
                'uitleg': 'Ontheemden missen de officiële internationale vluchtelingenstatus en blijven binnen het bereik van de strijdende partijen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Volgens de Verdragen van Genève is het toegestaan om ziekenhuizen en ambulances als doelwit te bombarderen.',
                'antwoord': False,
                'uitleg': 'Onwaar: medische faciliteiten en hulpverleners genieten strikte bescherming onder het oorlogsrecht.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Wereldwijd zijn er meer mensen op de vlucht binnen de grenzen van hun eigen land dan mensen die naar het buitenland zijn gevlucht.',
                'antwoord': True,
                'uitleg': 'Waar: het aantal geregistreerde ontheemden (IDP\'s) is aanzienlijk groter dan het aantal internationale vluchtelingen.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Het uithongeren van de burgerbevolking als oorlogstactiek is onder het internationaal recht een zware oorlogsmisdaad.',
                'antwoord': True,
                'uitleg': 'Waar: uithongering van burgers is uitdrukkelijk strafbaar gesteld in het Statuut van Rome van het Internationaal Strafhof.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welke juridische term duidt op de georganiseerde massamoord op een heel volk of een bevolkingsgroep?',
                'antwoord': 'genocide',
                'uitleg': 'Genocide (volkenmoord) is de zwaarste misdaad tegen de menselijkheid in het internationale strafrecht.'
            }
        ]
    },
    {
        'file': 'h5_4.js',
        'id': 'ak-h5-4',
        'hoofdstuk': 5,
        'paragraaf': '5.4',
        'titel': 'Hoe rustig is Europa?',
        'korteUitleg': 'Veiligheid in Europa, het uiteenvallen van Joegoslavië, separatisme en de oorlog in Oekraïne.',
        'icoon': '🛡️',
        'kleur': 'h5-thema',
        'theorie': """<h3>5.4 Hoe rustig is Europa?</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Europese Unie, NAVO, Joegoslavië-oorlogen, separatisme, autonomie, soevereiniteit, bufferstaat, de oorlog in Oekraïne.
</div>

<h4>1. Europa: Vreedzaam continent met breuklijnen</h4>
<p>Na de verwoestingen van de Tweede Wereldoorlog was het hoofddoel van de Europese integratie (de latere <b>Europese Unie</b>) om oorlog tussen Europese landen voorgoed onmogelijk te maken. Binnen de EU is dit decennialang uitstekend gelukt: lidstaten lossen hun geschillen op via overleg, rechtbanken en diplomatie. Echter, Europa is veel groter dan alleen de EU, en aan de randen en binnen sommige staten sluimeren ernstige spanningen.</p>

<h4>2. Het gewelddadige uiteenvallen van Joegoslavië</h4>
<p>In 1991 viel de federale staat <b>Joegoslavië</b> op de Balkan uiteen. Wat volgde was de bloedigste oorlog op Europees grondgebied sinds 1945. Slovenië en Kroatië verklaarden zich onafhankelijk, waarna in <b>Bosnië-Herzegovina</b> en later <b>Kosovo</b> een wrede oorlog uitbrak tussen Serviërs, Kroaten en Bosnische moslims. Er vonden etnische zuiveringen plaats om gebieden \'zuiver\' te maken voor één bevolkingsgroep, met als dieptepunt de genocide in Srebrenica. Pas na ingrijpen door de NAVO en het Verdrag van Dayton (1995) kwam er een einde aan de gevechten.</p>

<h4>3. Separatisme en autonomie</h4>
<p>Niet alle spanningen in Europa leiden tot grootschalig geweld. In veel landen streven minderheden naar zelfbestuur:</p>
<ul>
  <li><b>Autonomie:</b> Een regio krijgt binnen de bestaande staat eigen bevoegdheden over bijvoorbeeld onderwijs, politie of cultuur (zoals Schotland in het Verenigd Koninkrijk of Baskenland in Spanje).</li>
  <li><b>Separatisme:</b> Het streven van een volk of regio om zich <i>volledig af te scheiden</i> van de bestaande staat en een eigen onafhankelijk land te stichten (denk aan het streven van nationalisten in Catalonië).</li>
</ul>

<h4>4. De terugkeer van grootschalige oorlog: Oekraïne</h4>
<p>In februari 2022 viel het Russische leger op bevel van president Poetin buurland <b>Oekraïne</b> binnen. Dit markeerde de terugkeer van een grootschalige interstate oorlog in Europa. De oorzaken zijn complex:</p>
<ul>
  <li><b>Geopolitieke dimensie:</b> Rusland beschouwt Oekraïne als zijn traditionele invloedssfeer en verzette zich fel tegen de wens van Oekraïne om lid te worden van de <b>NAVO</b> en de EU.</li>
  <li><b>Grondgebied en soevereiniteit:</b> Rusland annexeerde in 2014 al de Krim en delen van de Donbas, en eist controle over grote delen van het oosten en zuiden van Oekraïne.</li>
  <li><b>Gevolgen voor Europa:</b> De oorlog leidde tot miljoenen vluchtelingen naar EU-landen, een acute energiecrisis (stoppen van Russisch gas), hernieuwde wapenwedloop en een sterke uitbreiding van de NAVO (met Finland en Zweden als nieuwe lidstaten).</li>
</ul>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat was het oorspronkelijke hoofddoel van de oprichting van de Europese Gemeenschap (de voorloper van de EU)?',
                'opties': [
                    'Oorlog tussen Europese landen zoals Frankrijk en Duitsland voorgoed onmogelijk maken door economische samenwerking',
                    'Het afschaffen van alle talen behalve het Latijn',
                    'Het bouwen van een gigantische muur rondom het hele continent',
                    'Het verplichten van alle burgers om in het leger te dienen'
                ],
                'antwoord': 0,
                'uitleg': 'Door kolen en staal onder gezamenlijk beheer te stellen, werd oorlogsvoering materieel onmogelijk gemaakt.'
            },
            {
                'type': 'mc',
                'vraag': 'Welk land op de Balkan viel in de jaren 90 uiteen in een reeks bloedige oorlogen en etnische zuiveringen?',
                'opties': [
                    'Zwitserland',
                    'Joegoslavië',
                    'Noorwegen',
                    'IJsland'
                ],
                'antwoord': 1,
                'uitleg': 'Joegoslavië viel uiteen in verschillende onafhankelijke republieken (zoals Kroatië, Bosnië, Servië).'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is het verschil tussen autonomie en separatisme?',
                'opties': [
                    'Autonomie is altijd gewelddadig en separatisme niet',
                    'Autonomie geldt alleen voor eilanden en separatisme voor bergen',
                    'Autonomie is zelfbestuur binnen een bestaand land; separatisme is het streven naar volledige onafhankelijkheid en afscheiding',
                    'Er is geen enkel onderscheid tussen beide termen'
                ],
                'antwoord': 2,
                'uitleg': 'Autonomie betekent eigen wetten/bestuur binnen de staat; separatisme betekent losbreken en een eigen staat stichten.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke twee Noord-Europese landen gaven hun neutraliteit op en traden na de Russische invasie in Oekraïne toe tot de NAVO?',
                'opties': [
                    'Spanje en Portugal',
                    'Zwitserland en Oostenrijk',
                    'Finland en Zweden',
                    'Ierland en Malta'
                ],
                'antwoord': 2,
                'uitleg': 'Finland en Zweden zochten collectieve veiligheid onder Artikel 5 van het NAVO-verdrag.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat houdt Artikel 5 van het NAVO-verdrag in?',
                'opties': [
                    'Alle wapens moeten gratis aan ontwikkelingslanden worden geschonken',
                    'Een gewapende aanval op één lidstaat wordt beschouwd als een aanval op alle lidstaten (collectieve zelfverdediging)',
                    'Ieder land mag om de vijf jaar van hoofdstad wisselen',
                    'Het verbod op het vliegen met straaljagers'
                ],
                'antwoord': 1,
                'uitleg': 'Artikel 5 is de kernbepaling van de NAVO: een aanval op één is een aanval op allen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke Spaanse regio heeft de afgelopen decennia te maken gehad met een sterk vreedzaam separatisme om een eigen republiek te worden?',
                'opties': [
                    'Catalonië',
                    'Andalusië',
                    'Madrid',
                    'Galicië'
                ],
                'antwoord': 0,
                'uitleg': 'In Catalonië streeft een aanzienlijk deel van de bevolking naar volledige onafhankelijkheid van Spanje.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'De grenzen van het Europese continent lopen in het oosten langs de gebergten van de Oeral en de Kaukasus.',
                'antwoord': True,
                'uitleg': 'Waar: geografisch vormt de Oeral de traditionele scheidslijn tussen Europa en Azië.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Sinds het einde van de Tweede Wereldoorlog zijn er in heel Europa nooit meer gewapende conflicten geweest.',
                'antwoord': False,
                'uitleg': 'Onwaar: denk aan de Joegoslavische burgeroorlogen in de jaren 90 en de huidige oorlog in Oekraïne.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Etnische zuivering betekent dat een bevolkingsgroep met geweld en terreur gedwongen wordt een gebied te verlaten om het etnisch homogeen te maken.',
                'antwoord': True,
                'uitleg': 'Waar: etnische zuiveringen werden op grote schaal toegepast tijdens de oorlogen in Bosnië en Kosovo.'
            },
            {
                'type': 'invoer',
                'vraag': 'Welk militair bondgenootschap tussen Noord-Amerikaanse en Europese landen waarborgt collectieve veiligheid via Artikel 5?',
                'antwoord': 'navo',
                'uitleg': 'De NAVO (Noord-Atlantische Verdragsorganisatie) is het belangrijkste westerse militaire bondgenootschap.'
            }
        ]
    },
    {
        'file': 'h5_5.js',
        'id': 'ak-h5-5',
        'hoofdstuk': 5,
        'paragraaf': '5.5',
        'titel': 'Nederland: oorlog en vrede',
        'korteUitleg': 'De Nederlandse militaire geschiedenis, vredesmissies van de VN en de defensie-industrie.',
        'icoon': '🕊️',
        'kleur': 'h5-thema',
        'theorie': """<h3>5.5 Nederland: oorlog en vrede</h3>
<div class="info-box">
  <b>Kernbegrippen:</b> Nederlandse Opstand, tactiek van de verschroeide aarde, dekolonisatieoorlog in Indonesië, vredesmissies (VN / blauwhelmen), Dutchbat, wapenexport, krijgsmacht.
</div>

<h4>1. Nederland en oorlog door de geschiedenis</h4>
<p>Nederland heeft een lange geschiedenis met oorlogvoering. De geboorte van de Nederlandse staat vond plaats tijdens de <b>Tachtigjarige Oorlog (1568-1648)</b> tegen het Spaanse Rijk. Beide partijen maakten zich schuldig aan gruweldaden en pasten de <b>tactiek van de verschroeide aarde</b> toe: dorpen, graanvoorraden en dijken werden opzettelijk vernietigd om de oprukkende vijand van voedsel en dekking te beroven.</p>
<p>In de 17e eeuw bouwde Nederland een wereldwijd handelsimperium op, vaak met meedogenloos militair geweld door de VOC en WIC. Na de Tweede Wereldoorlog voerde Nederland tussen 1945 en 1949 een bittere en gewelddadige <b>dekolonisatieoorlog in Indonesië</b> (destijds eufemistisch \'politionele acties\' genoemd) om de kolonie te behouden, waarbij tienduizenden Indonesische burgers en vrijheidsstrijders omkwamen.</p>

<h4>2. Nederland als voorvechter van vrede en recht</h4>
<p>Sinds de tweede helft van de 20e eeuw profileert Nederland zich als internationaal centrum van recht en vrede. In Artikel 90 van de Nederlandse Grondwet staat zelfs dat de regering de ontwikkeling van de <i>internationale rechtsorde</i> moet bevorderen. Den Haag herbergt instellingen zoals het Internationaal Gerechtshof en het Internationaal Strafhof.</p>
<p>De Nederlandse krijgsmacht wordt primair ingezet voor drie hoofdtaken:</p>
<ul>
  <li>Bescherming van het eigen grondgebied en dat van NAVO-bondgenoten.</li>
  <li>Handhaving en bevordering van de internationale rechtsorde en stabiliteit.</li>
  <li>Ondersteuning van civiele autoriteiten bij rampenbestrijding en handhaving van de openbare orde.</li>
</ul>

<h4>3. Vredesmissies en de schaduw van Srebrenica</h4>
<p>Nederlandse militairen namen deel aan tientallen internationale <b>vredesmissies</b> onder de vlag van de Verenigde Naties (de zogeheten \'blauwhelmen\'), de NAVO en de EU (in onder andere Libanon, Bosnië, Afghanistan en Mali).</p>
<p>Het meest traumatische hoofdstuk uit de moderne militaire geschiedenis is de uitzending van het bataljon <b>Dutchbat</b> naar Srebrenica in 1995. De lichtbewapende Nederlandse blauwhelmen moesten een door de VN uitgeroepen \'veilige enclave\' beschermen tegen een overmacht van Bosnisch-Servische troepen. Toen de Servische generaal Mladić de enclave onder de voet liep en de beloofde NAVO-luchtsteun uitbleef, kon Dutchbat de deportatie en genocide op ruim 8.000 moslimmannen niet verhinderen. Dit leidde in Nederland tot diepe trauma\'s, parlementaire onderzoeken en uiteindelijk de val van het kabinet-Kok in 2002.</p>

<h4>4. Defensie-industrie en wapenexport</h4>
<p>Nederland is ook een belangrijke speler in de internationale wapenhandel. Hoewel Nederland zelf geen tanks bouwt, exporteert de Nederlandse defensie-industrie hoogwaardige radarsystemen (zoals van Thales in Hengelo), marinefregatten, communicatieapparatuur en vliegtuigonderdelen. Voor wapenexport is een officiële vergunning van de overheid vereist, waarbij getoetst wordt of wapens niet terechtkomen in landen waar mensenrechten ernstig geschonden worden of waar een embargo geldt.</p>""",
        'vragen': [
            {
                'type': 'mc',
                'vraag': 'Wat hield de tactiek van de verschroeide aarde in tijdens historische oorlogen in Nederland?',
                'opties': [
                    'Het opzettelijk verbranden van gewassen, huizen en voorraden om de oprukkende vijand te beroven van voedsel en onderdak',
                    'Het verhogen van de dijken met zwarte as',
                    'Het beschilderen van alle forten met zwarte verf',
                    'Het aanleggen van tunnels onder de rivieren'
                ],
                'antwoord': 0,
                'uitleg': 'Bij de tactiek van de verschroeide aarde vernietigt men alles wat bruikbaar kan zijn voor de tegenstander.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke oorlog voerde Nederland tussen 1945 en 1949 om het verlies van zijn belangrijkste overzeese kolonie tegen te houden?',
                'opties': [
                    'De Falklandoorlog',
                    'De dekolonisatieoorlog in Indonesië',
                    'De Krimoorlog',
                    'De Boerenoorlog'
                ],
                'antwoord': 1,
                'uitleg': 'Nederland vocht vier jaar lang tevergeefs tegen de Indonesische onafhankelijkheidsstrijders.'
            },
            {
                'type': 'mc',
                'vraag': 'Waarom draagt een VN-vredesmacht vaak de bijnaam blauwhelmen?',
                'opties': [
                    'Omdat de militairen altijd blauwe overalls dragen',
                    'Omdat de soldaten herkenbare lichtblauwe helmen en baretten dragen met het VN-embleem',
                    'Omdat de soldaten alleen op blauwe boten varen',
                    'Omdat de missies altijd op zee plaatsvinden'
                ],
                'antwoord': 1,
                'uitleg': 'De blauwe helm symboliseert de neutraliteit en de beschermende missie van de Verenigde Naties.'
            },
            {
                'type': 'mc',
                'vraag': 'Wat is een van de drie hoofdtaken van de Nederlandse krijgsmacht volgens de Grondwet?',
                'opties': [
                    'Het veroveren van nieuwe grondgebieden in Afrika',
                    'Het afdwingen van handelscontracten voor Nederlandse multinationals',
                    'Het verdedigen van het eigen en het bondgenootschappelijk grondgebied en het bevorderen van de internationale rechtsorde',
                    'Het besturen van alle provincies in Nederland'
                ],
                'antwoord': 2,
                'uitleg': 'Artikel 97 van de Grondwet regelt de verdediging en bevordering van de internationale rechtsorde.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke hoogwaardige militaire goederen produceert en exporteert de Nederlandse defensie-industrie veelvuldig?',
                'opties': [
                    'Kernonderzeeërs en atoombommen',
                    'Geavanceerde marine-radarsystemen en militaire elektronica',
                    'Zware intercontinentale ballistische raketten',
                    'Paarden en zadels voor de cavalerie'
                ],
                'antwoord': 1,
                'uitleg': 'Bedrijven zoals Thales Nederland behoren wereldwijd tot de top in maritieme radarsystemen.'
            },
            {
                'type': 'mc',
                'vraag': 'Welke politieke consequentie had het NIOD-rapport over de val van Srebrenica in Nederland in 2002?',
                'opties': [
                    'Het Nederlandse kabinet onder leiding van premier Wim Kok diende zijn ontslag in',
                    'Nederland trad onmiddellijk uit de Verenigde Naties',
                    'Het leger werd met onmiddellijke ingang volledig afgeschaft',
                    'Er werden geen verkiezingen meer gehouden'
                ],
                'antwoord': 0,
                'uitleg': 'Het kabinet-Kok nam de politieke medeverantwoordelijkheid op zich en trad af na het vernietigende rapport.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Voor het exporteren van militaire goederen en wapens vanuit Nederland is altijd een officiële vergunning van de overheid vereist.',
                'antwoord': True,
                'uitleg': 'Waar: Nederland toetst wapenexportvergunningen aan strikte Europese criteria inzake mensenrechten en conflictgebieden.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Nederlandse soldaten mogen volgens de Grondwet alleen binnen de grenzen van de eigen provincie ingezet worden.',
                'antwoord': False,
                'uitleg': 'Onwaar: de Nederlandse krijgsmacht opereert wereldwijd in NAVO-verband en bij VN-vredesmissies.'
            },
            {
                'type': 'waaronwaar',
                'vraag': 'Tijdens de Tachtigjarige Oorlog vocht Nederland voor zijn onafhankelijkheid tegen het koninkrijk Spanje.',
                'antwoord': True,
                'uitleg': 'Waar: de Nederlandse Opstand tegen de Spaanse Habsburgers leidde uiteindelijk tot de Republiek der Zeven Verenigde Nederlanden.'
            },
            {
                'type': 'invoer',
                'vraag': 'Hoe heette het Nederlandse VN-bataljon dat in 1995 de enclave Srebrenica in Bosnië moest beschermen?',
                'antwoord': 'dutchbat',
                'uitleg': 'Dutchbat (Dutch Battalion) was de Nederlandse eenheid die onder VN-mandaat in Srebrenica gelegerd was.'
            }
        ]
    }
]

def balance_mc(vragen):
    mc_target = [0, 1, 2, 3, 0, 1]
    mc_idx = 0
    for v in vragen:
        if v['type'] == 'mc':
            target = mc_target[mc_idx % len(mc_target)]
            curr = v['antwoord']
            corr = v['opties'][curr]
            other = [o for i, o in enumerate(v['opties']) if i != curr]
            other.insert(target, corr)
            v['opties'] = other
            v['antwoord'] = target
            mc_idx += 1

def main():
    os.makedirs(BASE_DIR, exist_ok=True)
    for o in ONDERWERPEN:
        balance_mc(o['vragen'])
        path = os.path.join(BASE_DIR, o['file'])
        content = f"""/* =========================================================
   Duru's Aardrijkskunde (HAVO 3) — §{o['paragraaf']} {o['titel']}
   buiteNLand 3 HAVO Hoofdstuk 5 (Gewapende conflicten)
   ========================================================= */
DURU.register({{
  id: "{o['id']}",
  hoofdstuk: {o['hoofdstuk']},
  paragraaf: "{o['paragraaf']}",
  titel: "{o['titel']}",
  korteUitleg: "{o['korteUitleg']}",
  icoon: "{o['icoon']}",
  kleur: "{o['kleur']}",
  theorie: `{o['theorie']}`,
  vragen: {json.dumps(o['vragen'], indent=4, ensure_ascii=False)}
}});
"""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Geschreven: {path} (vragen: {len(o['vragen'])}, theorie: {len(o['theorie'])} chars)")

if __name__ == '__main__':
    main()
