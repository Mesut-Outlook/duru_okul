/* Onderwerp 2.1 — De geschiedenis van de aarde
   buiteNLand 3 HAVO Hoofdstuk 2 */
DURU.register({
  id: "ak-h2-1",
  hoofdstuk: 2,
  paragraaf: "2.1",
  titel: "De geschiedenis van de aarde",
  korteUitleg: "Geologische tijdschaal, relatieve vs absolute datering, massa-extincties en de Chicxulub meteoriet.",
  icoon: "⏳",
  kleur: "h2-thema",
  theorie: `
    <h3>2.1 De geschiedenis van de aarde</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Geologische tijdschaal, tijdperken (Precambrium, Paleozoïcum, Mesozoïcum, Kenozoïcum), perioden (o.a. Carboon, Krijt, Kwartair), relatieve vs absolute ouderdom, superpositiebeginsel, massa-extincties.
    </div>
    <h4>1. Een reis van 4,6 miljard jaar</h4>
    <p>De aarde is ongeveer <b>4,6 miljard jaar (4600 miljoen jaar)</b> oud. Geologen hebben deze onvoorstelbaar lange geschiedenis ingedeeld in een <b>geologische tijdschaal</b>. We onderscheiden vier grote <b>tijdperken (era's)</b>:</p>
    <ul>
      <li><b>Precambrium (4600 - 541 mln jaar geleden):</b> Vorming van de aardkorst, oceanen en dampkring. Eerste eencellige leven (bacteriën) in de zee; het landoppervlak is nog kaal en levenloos.</li>
      <li><b>Paleozoïcum (541 - 252 mln jaar geleden):</b> 'Tijdperk van het oude leven'. Begint met de Cambrische explosie (zeeleven met schelpen). In het <b>Carboon</b> ontstaan uitgestrekte tropische moerasbossen waaruit later steenkool ontstaat. Eindigt met de grootste massa-extinctie ooit aan het eind van het <b>Perm</b>.</li>
      <li><b>Mesozoïcum (252 - 66 mln jaar geleden):</b> 'Tijdperk van het midden-leven' (Trias, Jura, Krijt). Bloeitijd van de dinosauriërs en ammonieten in de oceanen. Eindigt 66 miljoen jaar geleden abrupt door een gigantische meteorietinslag bij <b>Chicxulub (Yucatan)</b>.</li>
      <li><b>Kenozoïcum (66 mln jaar geleden - heden):</b> 'Tijdperk van het recente leven' (Tertiair en <b>Kwartair</b>). Snelle evolutie en dominantie van zoogdieren, ijstijden met mammoeten en de opkomst van de mens.</li>
    </ul>

    <h4>2. Dateren van aardlagen</h4>
    <p>Om te bepalen hoe oud aardlagen zijn, gebruiken we twee methoden:</p>
    <ul>
      <li><b>Relatieve ouderdom:</b> Bepalen welke laag ouder of jonger is. Volgens het <b>superpositiebeginsel</b> ligt in een ongestoord pakket sediment de oudste laag onderop en de jongste laag bovenop.</li>
      <li><b>Absolute ouderdom:</b> Het meten van de exacte leeftijd in miljoenen jaren via radioactief verval van isotopen in mineralen.</li>
    </ul>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Hoe oud is de aarde ongeveer?",
      opties: [
        "4,6 miljard jaar (4600 miljoen jaar)",
        "6000 jaar",
        "100.000 jaar",
        "500 miljard jaar"
      ],
      antwoord: 0,
      uitleg: "De aarde ontstond circa 4,6 miljard jaar geleden uit kosmisch gas en stof."
    },
    {
      type: "mc",
      vraag: "In welk geologisch tijdperk leefden de dinosauriërs?",
      opties: [
        "Precambrium",
        "Mesozoïcum",
        "Paleozoïcum",
        "Kenozoïcum"
      ],
      antwoord: 1,
      uitleg: "Het Mesozoïcum (Trias, Jura, Krijt) was het tijdperk van de grote reptielen."
    },
    {
      type: "waaronwaar",
      vraag: "Volgens het superpositiebeginsel is de bovenste laag in een ongestoorde bergwand altijd de oudste laag.",
      antwoord: false,
      uitleg: "Niet waar. De bovenste laag is het laatst afgezet en dus de JONGSTE laag; de oudste laag ligt onderop."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je het uitsterven van een zeer groot deel van alle planten en diersoorten op aarde in korte tijd?",
      antwoord: "massa-extinctie|massa extinctie|massaextinctie",
      uitleg: "Massa-extincties markeren vaak de overgang tussen geologische tijdperken."
    },
    {
      type: "mc",
      vraag: "Wat gebeurde er 66 miljoen jaar geleden aan het einde van het Krijt?",
      opties: [
        "Het eerste bacteriële leven ontstond in de diepzee",
        "De aarde bevroor volledig tot aan de evenaar",
        "Een meteorietinslag bij Chicxulub leidde tot wereldwijde verduistering en het uitsterven van de dinosauriërs",
        "De aarde botste tegen de planeet Mars"
      ],
      antwoord: 2,
      uitleg: "De Krijt-Tertiair catastrofe maakte een einde aan het tijdperk van de dinosauriërs."
    },
    {
      type: "waaronwaar",
      vraag: "In het Carboon ontstonden door dode plantenresten in tropische moerassen de latere steenkoollagen.",
      antwoord: true,
      uitleg: "Waar. Het Carboon staat bekend om de enorme ophoping van veen en inkoling tot steenkool."
    },
    {
      type: "invoer",
      vraag: "In welke geologische periode van het Kenozoïcum leven wij nu, gekenmerkt door ijstijden en menselijke ontwikkeling?",
      antwoord: "Kwartair|het Kwartair",
      uitleg: "Het Kwartair omvat de laatste 2,6 miljoen jaar van de aardgeschiedenis."
    },
    {
      type: "mc",
      vraag: "Hoe bepalen wetenschappers de <b>absolute ouderdom</b> van een gesteente?",
      opties: [
        "Door het aantal zandkorrels onder de microscoop te tellen",
        "Door te ruiken aan het zand",
        "Door met een liniaal de dikte van de laag te meten",
        "Door het meten van het radioactieve verval van instabiele isotopen in mineralen"
      ],
      antwoord: 3,
      uitleg: "Radiometrische datering meet het verval van radioactieve elementen met een bekende halveringstijd."
    }
  ]
});
