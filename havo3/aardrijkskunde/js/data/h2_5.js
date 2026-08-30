/* Onderwerp 2.5 — Delfstoffen in Nederland
   buiteNLand 3 HAVO Hoofdstuk 2 */
DURU.register({
  id: "ak-h2-5",
  hoofdstuk: 2,
  paragraaf: "2.5",
  titel: "Delfstoffen in Nederland",
  korteUitleg: "Delfstoffen in Nederland: Mergel/kalksteen in Limburg, steenkool, Gronings aardgas en zoutwinning.",
  icoon: "🏆",
  kleur: "h2-thema",
  theorie: `
    <h3>2.5 Delfstoffen in Nederland</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Zuid-Limburgse kalksteen (Mergel, Krijt), steenkool (Carboon, inkoling, mijnsluiting), aardgasveld Slochteren (Perm, Zechstein zoutdeksel, geïnduceerde bevingen), zoutwinning (oplosmijnbouw), zand & grind (Kwartair).
    </div>
    <h4>1. Delfstoffen per regio in Nederland</h4>
    <p>Hoewel Nederland een vlak sedimentair land is, herbergt onze ondergrond rijke bodemschatten uit verschillende geologische tijdvakken:</p>
    <ul>
      <li><b>Zuid-Limburg:</b>
        <ul>
          <li><i>Krijtkalksteen (Mergel):</i> Gevormd 70 miljoen jaar geleden in een subtropische Krijtzee uit schelpjes. Gewonnen in dagbouw (Sint-Pietersberg / ENCI) voor cement en mergelbouwstenen.</li>
          <li><i>Steenkool:</i> Gevormd in het Carboon (300 mln jaar geleden) door inkoling van tropische moerasbossen. Tussen 1965 en 1974 werden alle mijnen gesloten omdat winning te diep en te duur werd en aardgas werd gevonden.</li>
        </ul>
      </li>
      <li><b>Groningen (Slochteren):</b> In 1959 ontdekt op 3 km diepte. Gas ontstaan uit Carboon-kolen verzamelde zich in poreus <b>Rotliegend-zandsteen (Perm)</b> en werd afgesloten door een ondoordringbare <b>Zechstein-zoutlaag</b>. Wegens <b>geïnduceerde aardbevingen</b> en schade aan woningen is de gaswinning in 2023/2024 definitief gestopt.</li>
      <li><b>Midden-, Oost- en Zuid-Nederland:</b> Winning van <b>zand en grind</b> (afgezet door rivieren en gletsjers in het Kwartair) voor beton en woningbouw. Na ontgrinding langs de Maas ontstaan recreatieplassen (Maasplassen). Rivierklei dient voor bakstenen.</li>
      <li><b>Twente en Friesland:</b> <b>Steenzoutwinning</b> uit diepe Perm-zoutlagen via oplosmijnbouw (injectie van water).</li>
    </ul>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Hoe is de <b>Limburgse kalksteen (Mergel)</b> ontstaan?",
      opties: [
        "In een warme subtropische Krijtzee door de opeenhoping van kalkskeletjes van ontelbare zeedieren",
        "Door lava van een vulkaan bij Maastricht",
        "Door rivierzand dat tijdens de ijstijd door de Rijn is neergelegd",
        "Door het droogvallen van het IJsselmeer"
      ],
      antwoord: 0,
      uitleg: "Mergel is organogene kalksteen afgezet op de bodem van de Krijtzee."
    },
    {
      type: "mc",
      vraag: "Waarom werden alle Limburgse <b>steenkoolmijnen</b> tussen 1965 en 1974 gesloten?",
      opties: [
        "Er was nergens in Europa meer vraag naar elektriciteit",
        "De winning werd te duur en te diep, buitenlandse kolen waren goedkoper en in Groningen werd aardgas ontdekt",
        "Omdat de mijnschachten volliepen met vloeibaar goud",
        "Omdat steenkool bij wet verboden werd"
      ],
      antwoord: 1,
      uitleg: "De ontdekking van de gasbel in Slochteren en goedkope olie/kolenimport maakten de mijnen onrendabel."
    },
    {
      type: "waaronwaar",
      vraag: "De aardbevingen in Groningen ontstaan doordat de Afrikaanse tektonische plaat tegen Nederland botst.",
      antwoord: false,
      uitleg: "Niet waar. Het zijn geïnduceerde (menselijke) bevingen, veroorzaakt door het inklinken van de zandsteenlaag door gaswinning."
    },
    {
      type: "invoer",
      vraag: "In welk Gronings dorp werd in 1959 het gigantische aardgasveld ontdekt?",
      antwoord: "Slochteren",
      uitleg: "Het Slochteren-gasveld bevatte bijna 3000 miljard m³ gas."
    },
    {
      type: "mc",
      vraag: "Welke gesteentelaag hield het aardgas in Groningen miljoenen jaren lang gevangen in de zandsteenlaag?",
      opties: [
        "Een houten vloer",
        "Een poreuze laag grof riviergrind",
        "Een dikke, ondoordringbare laag Zechstein-steenzout en klei (afsluitend gesteente)",
        "Een laag bevroren grondwater"
      ],
      antwoord: 2,
      uitleg: "Zout is volkomen gasdicht en vormde een natuurlijke afsluiting boven het gasreservoir."
    },
    {
      type: "waaronwaar",
      vraag: "Zand en grind die in Nederland worden gewonnen, worden vooral gebruikt in de bouw voor het maken van beton en asfalt.",
      antwoord: true,
      uitleg: "Waar. Zand en grind zijn onmisbare bulkbouwstoffen voor onze infrastructuur."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je het proces waarbij plantenresten onder druk en hitte transformeren van veen naar bruinkool, steenkool en antraciet?",
      antwoord: "inkolingsproces|inkoling|het inkolingsproces",
      uitleg: "Inkoling verhoogt het percentage zuivere koolstof in de organische resten."
    },
    {
      type: "mc",
      vraag: "Hoe wordt steenzout in Twente en Friesland uit de diepe ondergrond gewonnen?",
      opties: [
        "Door zeewater met schepnetten op te vangen",
        "Met houwelen door mijnwerkers in ondergrondse gangen",
        "Door zout uit de lucht te filteren met ventilatoren",
        "Via oplosmijnbouw: water wordt in de zoutlaag gepompt, waarna de pekel wordt opgepompt en ingedampt"
      ],
      antwoord: 3,
      uitleg: "Oplosmijnbouw lost de zoutlaag op met water en pompt de pekel omhoog."
    }
  ]
});
