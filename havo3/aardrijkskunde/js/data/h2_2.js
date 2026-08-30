/* Onderwerp 2.2 — Het dagboek van de aarde
   buiteNLand 3 HAVO Hoofdstuk 2 */
DURU.register({
  id: "ak-h2-2",
  hoofdstuk: 2,
  paragraaf: "2.2",
  titel: "Het dagboek van de aarde",
  korteUitleg: "Drie gesteentesoorten (stolling, sediment, metamorf), gidsfossielen en de gesteentekringloop.",
  icoon: "🪨",
  kleur: "h2-thema",
  theorie: `
    <h3>2.2 Het dagboek van de aarde</h3>
    <div class="info-box">
      <b>Kernbegrippen:</b> Stollingsgesteente (magma/lava, basalt, graniet), sedimentgesteente (zandsteen, kalksteen, schalie), metamorf gesteente (marmer, leisteen, kwartsiet), gidsfossielen, gesteentekringloop.
    </div>
    <h4>1. De drie hoofdtypen gesteenten</h4>
    <p>Aardlagen vormen het 'dagboek van de aarde'. Geologen verdelen alle gesteenten in drie groepen:</p>
    <ul>
      <li><b>Stollingsgesteenten:</b> Ontstaan door stolling van vloeibaar magma of lava.
        <ul>
          <li><i>Dieptegesteente:</i> Koelt diep ondergronds heel langzaam af, waardoor grote kristallen ontstaan (bijv. <b>graniet</b>).</li>
          <li><i>Uitvloeiingsgesteente:</i> Lava koelt aan het aardoppervlak zeer snel af; fijnkorrelig en donker (bijv. <b>basalt</b>).</li>
        </ul>
      </li>
      <li><b>Sedimentgesteenten:</b> Ontstaan door het afzetten en samenpersen van laagjes los materiaal (zand, klei, kalk). Gekenmerkt door duidelijke horizontale gelaagdheid en fossielen (bijv. <b>zandsteen</b>, <b>schalie</b> en <b>kalksteen</b> uit schelpjes).</li>
      <li><b>Metamorfe gesteenten:</b> Bestaand gesteente dat diep in de aardkorst onder extreme druk en hitte van structuur verandert zonder te smelten (bijv. <b>marmer</b> uit kalksteen, <b>leisteen</b> uit kleisteen, <b>kwartsiet</b> uit zandsteen).</li>
    </ul>

    <h4>2. Gidsfossielen</h4>
    <p><b>Gidsfossielen</b> (zoals ammonieten en trilobieten) zijn fossielen van soorten die slechts een korte periode leefden maar wereldwijd wijdverspreid waren. Zij fungeren als een geologische tijdsstempel waarmee aardlagen over de hele wereld exact gedateerd kunnen worden.</p>
  `,
  vragen: [
    {
      type: "mc",
      vraag: "Hoe ontstaat <b>stollingsgesteente</b>?",
      opties: [
        "Door het afkoelen en stollen van vloeibaar magma of lava",
        "Door het samenpersen van rivierklei onder water",
        "Door het verbranden van houtskool in een kachel",
        "Door de chemische werking van zoutzuur op schelpen"
      ],
      antwoord: 0,
      uitleg: "Magma of lava stolt bij afkoeling tot stollingsgesteente zoals graniet of basalt."
    },
    {
      type: "mc",
      vraag: "Welk gesteente is een voorbeeld van een <b>metamorf gesteente</b>?",
      opties: [
        "Basalt",
        "Marmer (ontstaan uit kalksteen)",
        "Zandsteen",
        "Graniet"
      ],
      antwoord: 1,
      uitleg: "Marmer is kalksteen die onder hoge druk en hitte is herkristalliseerd."
    },
    {
      type: "waaronwaar",
      vraag: "Fossielen worden vooral aangetroffen in sedimentgesteenten en vrijwel nooit in stollingsgesteenten.",
      antwoord: true,
      uitleg: "Waar. In hete lava verbranden organische resten direct; in zachte sedimentlagen kunnen ze bewaard blijven."
    },
    {
      type: "invoer",
      vraag: "Welk grofkorrelig dieptegesteente met zichtbare spikkels van kwarts en veldspaat koelt diep in de aardkorst af?",
      antwoord: "graniet",
      uitleg: "Graniet is het bekendste continentale dieptegesteente."
    },
    {
      type: "mc",
      vraag: "Aan welke twee eisen moet een <b>gidsfossiel</b> voldoen?",
      opties: [
        "Moet vandaag nog steeds in grote getale in het bos leven",
        "Moet minstens 500 meter lang zijn en alleen in één vijver geleefd hebben",
        "Korte geologische bestaansduur en grote wereldwijde geografische verspreiding",
        "Moet altijd van massief zilver zijn gemaakt"
      ],
      antwoord: 2,
      uitleg: "Kort geleefd + wijdverspreid maakt een fossiel ideaal om lagen wereldwijd te dateren."
    },
    {
      type: "waaronwaar",
      vraag: "Ammonieten zijn uitstekende gidsfossielen voor het Mesozoïcum.",
      antwoord: true,
      uitleg: "Waar. Ammonieten evolueerden snel en stierven uit aan het eind van het Krijt."
    },
    {
      type: "invoer",
      vraag: "Hoe noem je het metamorfe gesteente dat ontstaat wanneer kleisteen (schalie) onder hoge druk wordt samengeperst?",
      antwoord: "leisteen",
      uitleg: "Leisteen splijt gemakkelijk in dunne platen en werd gebruikt als dakbedekking."
    },
    {
      type: "mc",
      vraag: "Wat gebeurt er in de <b>gesteentekringloop</b> als een metamorf gesteente zó heet wordt dat het volledig vloeibaar smelt?",
      opties: [
        "Het wordt direct massief zandsteen",
        "Het verandert automatisch in een ammoniet",
        "Het lost voor altijd op in het heelal",
        "Het wordt vloeibaar magma, dat bij afkoeling een nieuw stollingsgesteente vormt"
      ],
      antwoord: 3,
      uitleg: "Smelten leidt tot magma; stolling brengt het gesteente terug naar de start van de kringloop."
    }
  ]
});
