/* Proeftoets 6 — Aardrijkskunde HAVO 3: Hoofdstuk 2 (Schatkist aarde?)
   Focus: Paragraaf 2.1 — De geschiedenis van de aarde, geologische tijdschaal, relatieve vs absolute ouderdom, massa-extincties, Chicxulub meteoriet.
   20 vragen conform DURU ENGINE_SPEC. */
DURU.registerExamen({
  id: "ex-h3-ak-6",
  hoofdstuk: 2,
  hoofdstukTitel: "Hoofdstuk 2 — Schatkist aarde?",
  titel: "Toets 6 — Geologische Tijdschaal, Datering & Massa-extincties",
  vak: "Aardrijkskunde · HAVO 3 (H2)",
  icoon: "⏳",
  duurMin: 30,
  vragen: [
    {
      type: "mc",
      vraag: "Hoe oud is de aarde volgens geologische berekeningen en meteorietonderzoek ongeveer?",
      opties: [
        "Ongeveer 4,6 miljard jaar (4600 miljoen jaar)",
        "Precies 6000 jaar",
        "Ongeveer 100.000 jaar",
        "Ongeveer 500 miljard jaar"
      ],
      antwoord: 0,
      uitleg: "De aarde en het zonnestelsel zijn circa 4,6 miljard (4600 miljoen) jaar geleden ontstaan uit een roterende wolk van gas en kosmisch stof."
    },
    {
      type: "mc",
      vraag: "Wat is de juiste chronologische volgorde van de vier grote <b>geologische tijdperken</b> (era's) van oud naar jong?",
      opties: [
        "Kenozoïcum → Mesozoïcum → Paleozoïcum → Precambrium",
        "Precambrium → Paleozoïcum → Mesozoïcum → Kenozoïcum",
        "Mesozoïcum → Precambrium → Kenozoïcum → Paleozoïcum",
        "Paleozoïcum → Kenozoïcum → Precambrium → Mesozoïcum"
      ],
      antwoord: 1,
      uitleg: "De aarde begon in het Precambrium, gevolgd door het Paleozoïcum (oud leven), het Mesozoïcum (midden leven / dinotijd) en het Kenozoïcum (recent leven)."
    },
    {
      type: "waaronwaar",
      vraag: "Tijdens het Precambrium was er al volop leven op het land in de vorm van dichte loofbossen en grazende zoogdieren.",
      antwoord: false,
      uitleg: "Niet waar. In het Precambrium ontstond het eerste eenvoudige eencellige leven (bacteriën en algen) uitsluitend in de oceanen; het land was nog kaal en onbewoond."
    },
    {
      type: "invul",
      vraag: "Hoe noem je een periode in de aardgeschiedenis waarin een zeer groot percentage van alle plant- en diersoorten op aarde in korte tijd uitsterft?",
      antwoord: "massa-extinctie|massa extinctie|massaextinctie|massale uitsterving",
      uitleg: "Tijdens een massa-extinctie (zoals aan het eind van het Perm en het Krijt) verdwijnt een groot deel van de biodiversiteit door plotselinge planetaire catastrofes."
    },
    {
      type: "mc",
      vraag: "Wat is het verschil tussen <b>relatieve ouderdom</b> en <b>absolute ouderdom</b> van aardlagen?",
      opties: [
        "Relatieve datering kan alleen op levende bomen worden toegepast; absolute datering alleen op zeewater",
        "Relatieve datering gebruikt een stopwatch; absolute datering kijkt alleen naar de kleur van het zand",
        "Relatieve datering bepaalt welke laag ouder of jonger is ten opzichte van andere lagen; absolute datering meet de exacte leeftijd in jaren met radioactief verval",
        "Er is geen enkel wetenschappelijk verschil tussen beide dateringsmethoden"
      ],
      antwoord: 2,
      uitleg: "Relatieve ouderdom stelt de volgorde vast (boven = jonger dan onder); absolute ouderdom meet het exacte aantal miljoenen jaren via isotopenonderzoek."
    },
    {
      type: "waaronwaar",
      vraag: "Volgens het superpositiebeginsel liggen in een ongestoord pakket sedimentgesteente de oudste lagen altijd onderop en de jongere lagen bovenop.",
      antwoord: true,
      uitleg: "Waar. Omdat nieuwe sedimenten bovenop reeds bestaande lagen worden afgezet, is de onderste laag het eerst gevormd en dus het oudst."
    },
    {
      type: "invul",
      vraag: "In welk geologisch tijdperk (era) leefden de dinosauriërs op aarde?",
      antwoord: "Mesozoïcum|Mesozoicum|het Mesozoïcum",
      uitleg: "Het Mesozoïcum (bestaande uit de perioden Trias, Jura en Krijt) staat bekend als het tijdperk van de reptielen en dinosauriërs."
    },
    {
      type: "mc",
      vraag: "Wat veroorzaakte circa 66 miljoen jaar geleden aan het einde van het Krijt het definitieve uitsterven van de dinosauriërs?",
      opties: [
        "Overbevolking door te veel plantenetende zoogdieren",
        "Het opdrogen van alle oceanen op aarde binnen enkele dagen",
        "Een plotselinge afname van de zwaartekracht op de evenaar",
        "Een gigantische meteorietinslag bij Chicxulub (Yucatan, Mexico) in combinatie met grootschalig vulkanisme en klimaatverandering"
      ],
      antwoord: 3,
      uitleg: "De meteorietinslag veroorzaakte wereldwijde stofwolken, verduistering van het zonlicht, zure regen en een abrupte instorting van de voedselketens."
    },
    {
      type: "waaronwaar",
      vraag: "De grootste massa-extinctie in de geschiedenis van de aarde vond plaats aan het einde van het Perm (einde Paleozoïcum), waarbij meer dan 90% van alle soorten uitstierf.",
      antwoord: true,
      uitleg: "Waar. De Perm-Trias-extinctie (veroorzaakt door gigantische vulkaanuitbarstingen in Siberië) was de zwaarste biologische crisis die de aarde ooit heeft meegemaakt."
    },
    {
      type: "mc",
      vraag: "In welke geologische periode van het Paleozoïcum vormden zich de uitgestrekte moerasbossen waaruit later de steenkoollagen zijn ontstaan?",
      opties: [
        "Carboon",
        "Kwartair",
        "Siluur",
        "Trias"
      ],
      antwoord: 0,
      uitleg: "In het Carboon (circa 359-299 miljoen jaar geleden) zorgde een warm, vochtig tropisch klimaat voor enorme wouden van boomvarens en wolfsklauwen die leidden tot steenkoolvorming."
    },
    {
      type: "invul",
      vraag: "In welke geologische periode van het Kenozoïcum leven wij vandaag de dag, gekenmerkt door ijstijden en de opkomst van de mens?",
      antwoord: "Kwartair|het Kwartair",
      uitleg: "Het Kwartair is de jongste periode (begonnen circa 2,6 miljoen jaar geleden) waarin ijstijden en de menselijke beschaving centraal staan."
    },
    {
      type: "waaronwaar",
      vraag: "Aan het begin van het Cambrium vond een plotselinge en enorme toename plaats van complexe levensvormen met harde skeletten en schelpen in de oceanen (Cambrische explosie).",
      antwoord: true,
      uitleg: "Waar. In het Cambrium (start Paleozoïcum) ontstonden binnen relatief korte tijd vrijwel alle grote diergroepen met fossiliseerbare harde delen."
    },
    {
      type: "mc",
      vraag: "Hoe kan een geoloog zien dat een kalksteenlaag in Zuid-Limburg miljoenen jaren geleden op de bodem van een warme zee is ontstaan?",
      opties: [
        "Omdat kalksteen uitsluitend bestaat uit gestolde vulkanische lava",
        "Door de aanwezigheid van fossielen van zeedieren zoals zee-egels, schelpen en tanden van de Mosasaurus",
        "Doordat er bevroren mammoetbotten in de kalksteen zijn ingesloten",
        "Aan de aanwezigheid van versteende boomstammen uit het tropisch regenwoud"
      ],
      antwoord: 1,
      uitleg: "Kalksteen ontstaat door accumulatie van schelpjes en kalkskeletjes van mariene organismen op de bodem van een ondiepe zee."
    },
    {
      type: "invul",
      vraag: "Hoe heet het reusachtige oercontinent waarin aan het einde van het Paleozoïcum en begin Mesozoïcum alle landmassa's op aarde aan elkaar vastzaten?",
      antwoord: "Pangaea|Pangea",
      uitleg: "Pangaea was het supercontinent dat door de platentektoniek later uiteendreef in de huidige continenten."
    },
    {
      type: "waaronwaar",
      vraag: "De zeespiegel en de gemiddelde wereldtemperatuur zijn gedurende de gehele geologische geschiedenis van 4,6 miljard jaar exact constant gebleven.",
      antwoord: false,
      uitleg: "Niet waar. Het klimaat en de zeespiegel hebben extreem gewisseld, van tropische broeikaswerelden tot volledige ijstijden met kilometers dikke ijskappen."
    },
    {
      type: "mc",
      vraag: "Wat is een <b>cenote</b> in Yucatan (Mexico), een karstverschijnsel dat gelinkt is aan de rand van de Chicxulub-krater?",
      opties: [
        "Een gigantische gletsjertong die uitmondt in de oceaan",
        "Een actieve vulkaan die continu vloeibaar basalt uitstoot",
        "Een natuurlijk zinkgat gevuld met grondwater, ontstaan door het instorten van ondergrondse kalksteengrotten",
        "Een door mensen gegraven steenkoolmijn uit de 19e eeuw"
      ],
      antwoord: 2,
      uitleg: "Cenotes zijn met zoet water gevulde zinkgaten in kalksteenplateaus, typisch voor het schiereiland Yucatan waar de meteoriet insloeg."
    },
    {
      type: "waaronwaar",
      vraag: "Met behulp van radioactief verval van isotopen (zoals koolstof-14 of kalium-argon) kunnen wetenschappers de absolute ouderdom van gesteenten bepalen.",
      antwoord: true,
      uitleg: "Waar. Omdat instabiele isotopen met een constante halveringstijd vervallen, fungeert dit verval als een betrouwbare geologische klok."
    },
    {
      type: "mc",
      vraag: "Welke diergroep ontwikkelde zich na het uitsterven van de dinosauriërs in het Tertiair tot de dominante landdieren op aarde?",
      opties: [
        "De varenbomen",
        "De trilobieten",
        "De ammonieten",
        "De zoogdieren"
      ],
      antwoord: 3,
      uitleg: "Door het wegvallen van de grote reptielen konden overlevende kleine zoogdieren zich snel diversifiëren en de opengevallen ecologische niches innemen."
    },
    {
      type: "open",
      vraag: "Leg uit waarom de ontdekking van een dunne laag iridiumrijk sediment wereldwijd in gesteenten van 66 miljoen jaar oud het bewijs leverde voor de meteorietinslag aan het einde van het Krijt.",
      sleutelwoorden: ["iridium zeldzaam op aarde", "veel voorkomend in meteorieten", "wereldwijde stoflaag/inslag"],
      minTreffers: 2,
      modelantwoord: "Het metaal iridium is uiterst zeldzaam in de aardkorst omdat het tijdens de vorming van de aarde naar de kern is gezonken, maar komt wel in hoge concentraties voor in meteorieten. De vondst van een wereldwijde dunne kleilaag met een extreem hoog iridiumgehalte precies op de grens tussen Krijt en Tertiair bewees dat een enorme ruimterots is ingeslagen en verpulverd tot een wereldwijde stofwolk.",
      uitleg: "Iridium-piek op de Krijt-Tertiair grens vormt de onweerlegbare chemische vingerafdruk van de meteoriet."
    },
    {
      type: "open",
      vraag: "Leg uit hoe geologen met behulp van fossielen en het superpositiebeginsel de relatieve ouderdom van verschillende gesteentelagen in een bergketen vaststellen.",
      sleutelwoorden: ["onderste lagen ouder dan bovenste", "gidsfossielen karakteristiek voor tijdvak", "lagen vergelijken/correlatie"],
      minTreffers: 2,
      modelantwoord: "Volgens het superpositiebeginsel zijn de onderste sedimentlagen ouder dan de bovenliggende lagen. Door te kijken welke specifieke gidsfossielen (organismen die slechts in één specifieke periode leefden) in de verschillende lagen voorkomen, kunnen geologen lagen in verschillende bergen met elkaar correleren en bepalen welke formatie eerder of later is afgezet.",
      uitleg: "Superpositie geeft verticale volgorde; gidsfossielen maken datering en correlatie tussen locaties mogelijk."
    }
  ]
});
