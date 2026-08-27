/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 3.3: Bezet Nederland
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h3-3",
    hoofdstuk: 3,
    paragraaf: "3.3",
    titel: "Bezet Nederland",
    korteUitleg: "De Duitse bezetting van Nederland, aanpassing en verzet, en de bevrijding.",
    icoon: "🇳🇱",
    theorie: `
<h3>3.3 Bezet Nederland</h3>

<p>Op vrijdag 10 mei 1940 om 3.55 uur viel Duitsland Nederland aan. In West-Nederland werden duizenden Duitse parachutisten gedropt om de koningin en de ministers gevangen te nemen, maar zij ontkwamen naar Londen, waar ze een regering in ballingschap vormden. Na de Nederlandse capitulatie op 15 mei begon de Duitse bezetting. De Oostenrijkse nazi <b>Seyss-Inquart</b> werd als rijkscommissaris de hoogste bestuurder van Nederland. De rechtsstaat en democratie werden afgeschaft.</p>

<h4>Van meevallen naar terreur</h4>
<p>De eerste maanden viel de bezetting veel Nederlanders mee: het normale leven keerde terug en het ging economisch zelfs beter dan voor de oorlog. Toch was er vanaf het begin onderdrukking, zoals censuur op kranten. Vanaf juni 1940 werden vakbonden, omroepen en andere organisaties <b>gelijkgeschakeld</b>: ze kregen een nazi aan het hoofd.</p>
<p>In februari 1941 brak het eerste grote protest uit: de <b>Februaristaking</b>. Nadat NSB'ers in Amsterdam geregeld joden aanvielen en er een razzia volgde waarbij 427 joodse mannen werden opgepakt, gingen arbeiders massaal in staking. De Duitsers grepen keihard in: honderden stakers werden opgepakt en achttien werden geëxecuteerd. Daarna traden de Duitsers steeds harder op met intimidatie en terreur. Vanaf 1942 moesten alle mannen tussen 17 en 40 jaar zich melden voor dwangarbeid (<b>arbeidsinzet</b>) in Duitsland.</p>

<div class="formule-box">
  <span class="formule">De houding van Nederlanders</span>
  <small>
    • De meeste Nederlanders waren anti-Duits, maar pasten zich aan om te overleven<br>
    • Ongeveer 4% was pro-Duits ("foute Nederlanders"), vaak lid van de NSB (op zijn hoogtepunt 100.000 leden)<br>
    • Zo'n 25.000 Nederlandse mannen vochten als SS'er mee aan het oostfront<br>
    • Een kleine groep kwam actief in verzet: onderduiken helpen, valse bonkaarten maken, illegale kranten zoals Trouw en Het Parool verspreiden, aanslagen plegen
  </small>
</div>

<div class="info-box let-op">
  <span class="kop">⚠️ Collaboratie</span>
  Naast NSB'ers waren er ook gewone burgers die met de bezetter samenwerkten: aannemers die bunkers voor de Duitsers bouwden, politieagenten die hielpen bij het arresteren van joden en dwangarbeiders, en de Nederlandse Spoorwegen die meewerkten aan de deportatie van joden.
</div>

<h4>De bevrijding en de Hongerwinter</h4>
<p>In september 1944 vielen de geallieerden Nederland binnen vanuit België. Bij de Slag om Arnhem werden ze tegengehouden, waardoor het nog ruim een half jaar duurde voordat heel Nederland bevrijd was. Het zuiden werd al in 1944 bevrijd, maar in het bezette West-Nederland brak een strenge <b>Hongerwinter</b> uit: door voedsel- en brandstoftekort stierven bijna 20.000 mensen van honger en ellende.</p>
<p>In april 1945 bevrijdden Canadese troepen Oost- en Noord-Nederland. Op 5 mei 1945 gaf het Duitse leger in Nederland zich over. Het feesten ging ook gepaard met wraakacties, zoals het in het openbaar kaalscheren van vrouwen die met Duitsers waren omgegaan.</p>
    `,
    vragen: [
      {
        id: "h3_3_v1",
        niveau: 1,
        type: "mc",
        vraag: "Op welke datum viel het Duitse leger Nederland binnen?",
        opties: [
          "1 september 1939",
          "15 mei 1940",
          "10 mei 1940",
          "6 juni 1944"
        ],
        antwoord: 2,
        uitleg: "Op 10 mei 1940 om 3.55 uur begon de Duitse inval, gevolgd door de capitulatie op 15 mei."
      },
      {
        id: "h3_3_v2",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Nederland capituleerde op 15 mei 1940, een dag na het bombardement op Rotterdam.",
        antwoord: true,
        uitleg: "Waar! Na de verwoesting van het centrum van Rotterdam gaf het Nederlandse leger zich de volgende dag over."
      },
      {
        id: "h3_3_v3",
        niveau: 1,
        type: "invoer",
        vraag: "Wie werd na de Nederlandse capitulatie als rijkscommissaris de hoogste Duitse bestuurder van Nederland?",
        antwoord: "Seyss-Inquart|Seyss Inquart|seyss-inquart",
        uitleg: "De Oostenrijkse nazi Seyss-Inquart bestuurde Nederland namens Hitler tot het einde van de oorlog."
      },
      {
        id: "h3_3_v4",
        niveau: 2,
        type: "mc",
        vraag: "Wat gebeurde er tijdens de Februaristaking van 1941?",
        opties: [
          "Nederlandse arbeiders gingen massaal in staking uit protest tegen de jodenvervolging.",
          "De koningin keerde definitief terug naar Nederland.",
          "Het Nederlandse leger viel Duitsland aan.",
          "De NSB werd door de Duitsers verboden."
        ],
        antwoord: 0,
        uitleg: "Na een razzia waarbij 427 joodse mannen werden opgepakt, staakten arbeiders in Amsterdam en omgeving massaal uit protest."
      },
      {
        id: "h3_3_v5",
        niveau: 2,
        type: "waaronwaar",
        vraag: "Vanaf 1942 werden alleen Nederlandse vrouwen opgeroepen voor dwangarbeid in Duitsland.",
        antwoord: false,
        uitleg: "Onwaar. Het waren juist Nederlandse mannen tussen 17 en 40 jaar die zich moesten melden voor arbeidsinzet in Duitsland."
      },
      {
        id: "h3_3_v6",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe noemen we Nederlanders die tijdens de bezetting samenwerkten met de Duitsers?",
        antwoord: "collaborateurs|collaborateur|collaboratie",
        uitleg: "Collaboratie is de term voor samenwerking met de vijand, zoals bij NSB'ers, bunkerbouwers en meewerkende ambtenaren."
      },
      {
        id: "h3_3_v7",
        niveau: 3,
        type: "mc",
        vraag: "Wat kenmerkte de Hongerwinter van 1944/1945 in West-Nederland?",
        opties: [
          "Een tekort aan voedsel en brandstof waardoor bijna 20.000 mensen omkwamen.",
          "Een grote overstroming door het doorbreken van de dijken.",
          "Een epidemie die vooral onder Duitse soldaten uitbrak.",
          "Een tekort aan wapens bij het Nederlandse verzet."
        ],
        antwoord: 0,
        uitleg: "Door de blokkade van de bevoorrading ontstond in de steden een groot tekort aan eten en brandstof, met bijna 20.000 hongerdoden tot gevolg."
      },
      {
        id: "h3_3_v8",
        niveau: 3,
        type: "waaronwaar",
        vraag: "Heel Nederland was al in september 1944 volledig bevrijd.",
        antwoord: false,
        uitleg: "Onwaar. Alleen het zuiden werd in 1944 bevrijd; Oost- en Noord-Nederland volgden pas in april 1945 en het westen pas op 5 mei 1945."
      }
    ]
  });
})();
