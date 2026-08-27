/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 5.4: Veelkleurig Nederland
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h5-4",
    hoofdstuk: 5,
    paragraaf: "5.4",
    titel: "Veelkleurig Nederland",
    korteUitleg: "Migratie uit voormalige kolonies, arbeidsmigranten, vluchtelingen en spanningen in de multiculturele samenleving.",
    icoon: "🌍",
    theorie: `
<h3>5.4 Veelkleurig Nederland</h3>
<p>Nederland heeft een <b>multi-etnische samenleving</b>: een maatschappij met mensen uit meerdere volken. Van de ruim zeventien miljoen Nederlanders in 2018 hadden bijna vier miljoen een migratieachtergrond.</p>

<h4>Uit voormalige kolonies</h4>
<p>Vanaf 1945 kwam een grote groep Indische Nederlanders uit Indonesië, omdat het daar niet meer veilig voor hen was: een <b>pushfactor</b>, een verklaring voor migratie in het land van vertrek. De overheid wilde dat ze zich aanpasten (<b>assimilatie</b>) en spreidde hen over het hele land; hun integratie verliep redelijk vlot.</p>
<p>Moeilijker verliep de integratie van Molukse soldaten, die Indonesië moesten verlaten omdat ze voor Nederland hadden gevochten en een eigen republiek, de RMS, hadden gesticht. Ze werden ondergebracht in opvangkampen en later in eigen wijken, wat de afstand tot andere Nederlanders groot hield. In de jaren 1970 pleegden sommige Molukse jongeren terreuracties, zoals treinkapingen, om het RMS-ideaal onder de aandacht te brengen.</p>
<p>Vanaf ongeveer 1975 kwam een massa-immigratie uit Suriname op gang, mede omdat velen geen vertrouwen hadden in de Surinaamse onafhankelijkheid. Vanaf de jaren 1980 kwamen ook Antilliaanse en Arubaanse jongeren naar Nederland; een deel van hen, zonder opleiding, raakte verzeild in een gewelddadige straatcultuur.</p>

<h4>Arbeidsmigranten</h4>
<p>Door de bloeiende economie ontstond omstreeks 1950 een tekort aan personeel. Bedrijven namen arbeiders aan uit Italië en andere landen rond de Middellandse Zee: dit waren <b>pullfactoren</b>, verklaringen voor migratie in het land van aankomst. Deze <b>gastarbeiders</b> waren vooral mannen die na een paar jaar teruggingen.</p>
<div class="formule-box">
  <span class="formule">push- en pullfactor</span>
  <small>pushfactor = verklaring voor migratie in het land van vertrek · pullfactor = verklaring voor migratie in het land van aankomst.</small>
</div>
<p>Vanaf 1973 verloren veel arbeidsmigranten hun baan, maar veel Turkse en Marokkaanse arbeiders bleven, omdat het ook in hun herkomstland economisch slecht ging en ze in Nederland recht hadden op een uitkering en op gezinshereniging. Hun integratie werd bemoeilijkt door grote cultuurverschillen, maar het onderwijs was bevorderlijk: vooral meisjes met een Turkse en Marokkaanse achtergrond deden het goed op school.</p>

<h4>Vluchtelingen en spanningen</h4>
<p>Vluchtelingen hebben recht op asiel als ze in hun land gevaar lopen; economische vluchtelingen hebben dat recht niet. Na de Koude Oorlog kwamen veel asielzoekers naar de EU, bijvoorbeeld door de oorlog in Joegoslavië, en na 2000 uit oorlogsgebieden in Afrika en Azië.</p>
<div class="info-box let-op">
  <span class="kop">⚠️ Spanningen</span>
  In 2004 werd filmmaker Theo van Gogh door een radicale moslim vermoord. Bij een deel van de bevolking groeide daardoor vijandigheid tegen moslims; datzelfde jaar richtte Geert Wilders de PVV op.
</div>
<p>Ondanks deze spanningen boekte de integratie ook vooruitgang: onderwijsachterstanden werden kleiner en meer Nederlanders met een migratieachtergrond kregen een hoge functie, zoals Khadija Arib, die in 1975 als 15-jarige uit Marokko naar Nederland kwam en in 2016 voorzitter van de Tweede Kamer werd.</p>
    `,
    vragen: [
      {
        id: "h5_4_v1",
        niveau: 1,
        type: "mc",
        vraag: "Waarom vertrokken vanaf 1945 veel Indische Nederlanders uit Indonesië naar Nederland?",
        opties: [
          "Omdat het na de onafhankelijkheid van Indonesië niet meer veilig voor hen was",
          "Omdat ze daar geen werk konden vinden",
          "Omdat de Nederlandse regering hen daartoe verplichtte via loting",
          "Omdat er een aardbeving was"
        ],
        antwoord: 0,
        uitleg: "Indische Nederlanders vertrokken omdat het na de Indonesische onafhankelijkheid niet meer veilig voor ze was: een pushfactor."
      },
      {
        id: "h5_4_v2",
        niveau: 1,
        type: "mc",
        vraag: "Wat is een 'pushfactor' bij migratie?",
        opties: [
          "Een verklaring voor migratie in het land van aankomst",
          "Een verklaring voor migratie in het land van vertrek",
          "Een wet die migratie verbiedt",
          "Een subsidie voor migranten"
        ],
        antwoord: 1,
        uitleg: "Een pushfactor is een verklaring voor migratie in het land van vertrek, zoals onveiligheid."
      },
      {
        id: "h5_4_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Vanaf 1975 kwam een grote groep Surinamers naar Nederland, mede omdat velen geen vertrouwen hadden in de Surinaamse onafhankelijkheid.",
        antwoord: true,
        uitleg: "Waar! Uit wantrouwen in de Surinaamse onafhankelijkheid kwam vanaf ongeveer 1975 een massa-immigratie uit Suriname op gang."
      },
      {
        id: "h5_4_v4",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Alle asielzoekers die naar Nederland komen, krijgen automatisch het recht om te blijven, ook economische vluchtelingen.",
        antwoord: false,
        uitleg: "Onwaar. Alleen mensen die in hun land gevaar lopen hebben recht op asiel; economische vluchtelingen hebben dat recht niet."
      },
      {
        id: "h5_4_v5",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe noemen we arbeidsmigranten die vanwege hun (bedoeld) tijdelijke verblijf in Nederland zo werden genoemd, en die vooral uit Italië en landen rond de Middellandse Zee kwamen?",
        antwoord: "gastarbeiders|gastarbeider",
        uitleg: "Deze arbeidsmigranten werden 'gastarbeiders' genoemd, omdat hun verblijf bedoeld was als tijdelijk."
      },
      {
        id: "h5_4_v6",
        niveau: 2,
        type: "mc",
        vraag: "Waarom kwamen Molukse militairen na 1950 met hun gezinnen naar Nederland?",
        opties: [
          "Ze wilden op vakantie",
          "Ze waren rijke handelaren",
          "Ze hadden voor Nederland gevochten en moesten Indonesië verlaten",
          "Ze kwamen als toeristen"
        ],
        antwoord: 2,
        uitleg: "Molukse militairen hadden voor Nederland gevochten en moesten Indonesië verlaten nadat hun republiek, de RMS, was verslagen."
      },
      {
        id: "h5_4_v7",
        niveau: 3,
        type: "invoer",
        vraag: "Welke politicus richtte in 2004 de Partij voor de Vrijheid (PVV) op?",
        antwoord: "Geert Wilders|Wilders",
        uitleg: "Geert Wilders richtte in 2004 de PVV op, een populistische anti-islampartij."
      },
      {
        id: "h5_4_v8",
        niveau: 3,
        type: "mc",
        vraag: "In welke functie kwam Khadija Arib in 1998 voor het eerst in de Tweede Kamer?",
        opties: [
          "Als minister-president",
          "Als koningin",
          "Als burgemeester van Rotterdam",
          "Als Kamerlid voor de PvdA"
        ],
        antwoord: 3,
        uitleg: "Khadija Arib kwam in 1998 voor de PvdA in de Tweede Kamer en werd in 2016 voorzitter."
      }
    ]
  });
})();
