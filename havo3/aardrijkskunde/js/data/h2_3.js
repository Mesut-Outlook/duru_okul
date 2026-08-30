/* Onderwerp 2.3 — Het gebruik van delfstoffen
   buiteNLand 3 HAVO Hoofdstuk 2 */
DURU.register({
  id: "ak-h2-3",
  hoofdstuk: 2,
  paragraaf: "2.3",
  titel: "Het gebruik van delfstoffen",
  korteUitleg: "Ertsen, winning (dagbouw vs schachtbouw), milieu-impact, Suriname (goud/kwik) en Nigeria (olie).",
  icoon: "🌍",
  kleur: "h2-thema",
  theorie: `
    <h3>2.3 Het gebruik van delfstoffen</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Delfstoffen, ertsen, dagbouw vs schachtbouw, uitputting, milieuschade, Suriname (goud, bauxiet, kwikvervuiling), Nigeria (aardolie in Nigerdelta), urban mining.
    </div>
    <h4>1. Delfstoffen en ertsen</h4>
    <p><b>Delfstoffen</b> zijn alle bruikbare mineralen, ertsen en gesteenten die uit de aardkorst worden gehaald. Als een gesteente een economisch winbare hoeveelheid metaal bevat (zoals bauxiet voor aluminium of ijzererts voor staal), noemen we het een <b>erts</b>. Mijnbouw gebeurt op twee manieren:</p>
    <ul>
      <li><b>Dagbouw:</b> Winning in open groeven aan het aardoppervlak (ondiepe ertsen, bruinkool). Veroorzaakt enorme kraters en landschapsaantasting.</li>
      <li><b>Schachtbouw:</b> Ondergrondse mijnbouw via diepe schachten en gangenstelsels (voor diepe steenkool- of ijzerertslagen).</li>
    </ul>

    <h4>2. Milieu-impact: Suriname en Nigeria</h4>
    <p>De winning van delfstoffen heeft wereldwijd zware gevolgen voor mens en natuur:</p>
    <ul>
      <li><b>Suriname:</b> In het binnenland vindt veel kleinschalige en illegale goudwinning plaats. Mijnwerkers spuiten regenwouden kapot en gebruiken giftig <b>kwik</b> om gouddeeltjes te binden. Dit kwik vergiftigt rivieren en vis, wat ernstige gezondheidsschade veroorzaakt bij inheemse volkeren.</li>
      <li><b>Nigeria:</b> In de olierijke <b>Nigerdelta</b> hebben decennia van oliewinning door multinationals geleid tot lekkende pijpleidingen, bodemvervuiling en vernietiging van mangrovebossen en visgronden.</li>
    </ul>

    <h4>3. Toekomst: recycling en urban mining</h4>
    <p>Omdat delfstoffen niet-hernieuwbaar zijn, is <b>urban mining</b> (het terugwinnen van goud, koper en zeldzame metalen uit afgedankte elektronica) cruciaal voor een duurzame, circulaire economie.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Wat is het verschil tussen <b>dagbouw</b> en <b>schachtbouw</b>?",
      opties: [
        "Bij dagbouw wordt het erts in een open groeve aan de oppervlakte afgegraven; bij schachtbouw via diepe ondergrondse mijngangen",
        "Dagbouw gebeurt alleen op zee; schachtbouw alleen in de woestijn",
        "Bij dagbouw werken alleen robots; bij schachtbouw alleen paarden",
        "Er is geen verschil in werkwijze"
      ],
      antwoord: 0,
      uitleg: "Dagbouw graaft de bovenste grondlaag af; schachtbouw gaat diep de aarde in."
    },
    {
      type: "mc",
      vraag: "Welk giftig metaal gebruiken illegale goudzoekers in Suriname om gouddeeltjes te binden?",
      opties: [
        "Aluminium",
        "Kwik",
        "Krijt",
        "Zand"
      ],
      antwoord: 1,
      uitleg: "Kwik bindt goud maar veroorzaakt zware schade aan het zenuwstelsel en vervuilt rivieren."
    },
    {
      type: "waaronwaar",
      vraag: "In de Nigerdelta in Nigeria heeft oliewinning geleid tot grootschalige vervuiling van mangroven en viswateren.",
      antwoord: true,
      uitleg: "Waar. Olielozingen en lekkages hebben het kwetsbare deltagebied zwaar aangetast."
    },
    {
      type: "invoer",
      vraag: "Welk aluminiumerts werd decennialang op grote schaal gewonnen in Suriname bij Moengo en Paranam?",
      antwoord: "bauxiet",
      uitleg: "Bauxiet is het belangrijkste erts voor aluminiumproductie."
    },
    {
      type: "mc",
      vraag: "Wat verstaat men onder <b>urban mining</b>?",
      opties: [
        "Het delven van zand in stadsparken",
        "Het graven van mijnschachten onder stadhuispleinen",
        "Het recyclen en terugwinnen van waardevolle metalen uit afgedankte elektronica en sloopafval in steden",
        "Het verbieden van alle elektronische apparaten"
      ],
      antwoord: 2,
      uitleg: "Urban mining haalt schaarse metalen uit e-waste in plaats van uit de grond."
    },
    {
      type: "waaronwaar",
      vraag: "Delfstoffen zijn oneindig hernieuwbaar en kunnen binnen enkele dagen door de natuur worden aangevuld.",
      antwoord: false,
      uitleg: "Niet waar. Delfstoffen zijn niet-hernieuwbaar en hebben miljoenen jaren nodig gehad om te ontstaan."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je een gesteente dat een economisch winbare hoeveelheid metaal bevat?",
      antwoord: "erts|ertsen|een erts",
      uitleg: "Een erts is een gesteente met een winbare concentratie metaal (zoals ijzererts of kopererts)."
    },
    {
      type: "mc",
      vraag: "Waarom is het omsmelten en recyclen van aluminium zo aantrekkelijk?",
      opties: [
        "Het is bij wet verplicht om alle aluminium na één dag weg te gooien",
        "Het verandert aluminium automatisch in puur goud",
        "Omdat gerecycled aluminium licht geeft in het donker",
        "Het kost 95% minder energie dan het winnen van nieuw aluminium uit bauxieterts"
      ],
      antwoord: 3,
      uitleg: "Recycling van aluminium bespaart gigantische hoeveelheden elektriciteit en CO2."
    }
  ]
});
