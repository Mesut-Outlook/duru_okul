/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 5.3: Postindustrieel Nederland
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h5-3",
    hoofdstuk: 5,
    paragraaf: "5.3",
    titel: "Postindustrieel Nederland",
    korteUitleg: "De oliecrisis van 1973, de opkomst van de dienstensector, beperking van de verzorgingsstaat en de grondwet van 1983.",
    icoon: "🏭",
    theorie: `
<h3>5.3 Postindustrieel Nederland</h3>
<p>In 1973 kwam een eind aan de economische bloeiperiode. Door een sterke stijging van de olieprijs ontstond een crisis, maar ook de sterk gestegen kosten van lonen en uitkeringen speelden mee: Nederlandse producten werden duur en daardoor minder verkocht. Vanaf 1973 sloten veel industriebedrijven of verplaatsten hun productie naar lagelonenlanden. Bij bedrijven die bleven, verdwenen banen door <b>automatisering</b>: mensen werden vervangen door uit zichzelf werkende machines.</p>
<p>Voor het eerst sinds de jaren 1930 ontstond grote werkloosheid, met een dieptepunt in 1984. Na 1985 groeide de economie weer, in de jaren 1996-2000 zelfs erg hard. Terwijl de industrie minder belangrijk werd, groeide het aantal banen in de dienstensector nog meer: in 2000 werkte bijna driekwart van de arbeidsbevolking in de dienstensector.</p>
<div class="formule-box">
  <span class="formule">postindustriële samenleving</span>
  <small>een samenleving waarin de dienstensector belangrijker is geworden dan de industriesector.</small>
</div>
<p>Door de opkomst van computers en mobiele telefoons ontstond omstreeks 1990 ook een <b>informatiemaatschappij</b>. In de jaren 2000 groeide de economie nauwelijks, en in 2008 begon een diepe crisis die duurde tot 2016.</p>

<h4>Beperking van de verzorgingsstaat</h4>
<p>De kosten van de verzorgingsstaat liepen vanaf 1973 snel op. Bedrijven gebruikten de WAO om goedkoop van personeel af te komen dat niet echt arbeidsongeschikt was. In 1984 telde Nederland 800 000 werklozen en bijna evenveel arbeidsongeschikten.</p>
<div class="voorbeeld">
  <span class="vb-kop">Bezuinigen op de WAO</span>
  <span class="stap">1. Uitkeringen werden verlaagd en keuringen strenger.</span>
  <span class="stap">2. In 2005 kwam de WIA: alleen mensen die nooit meer kunnen werken, houden recht op een blijvende uitkering.</span>
  <span class="stap">3. Toch waren er in 2018 nog altijd 500 000 Nederlanders met een arbeidsongeschiktheidsuitkering.</span>
</div>
<p>Ook werd in 2012 de AOW-leeftijd verhoogd en werd de ouderenzorg beperkt. In 2013 sprak koning Willem-Alexander in de troonrede over de omslag naar een <b>participatiesamenleving</b>, waarin mensen die dat kunnen zelf verantwoordelijkheid nemen voor hun leven en omgeving.</p>

<h4>Samenleving en politiek</h4>
<p>Het humanisme werd de dominante levensbeschouwing: in 2017 rekende 50 procent van de Nederlanders zich niet meer tot een kerkelijke of levensbeschouwelijke groep. De rechten van het individu namen toe, zoals bij het homohuwelijk, dat Nederland in 2002 als eerste land ter wereld invoerde.</p>
<p>In de jaren 1990 nam het conservatisme toe: mensen hadden moeite met individualisering, migratie en de groeiende verschillen tussen arm en rijk. Dit leidde tot populistische partijen als de SP (1994 in de Tweede Kamer) en Pim Fortuyn, die in 2002 vlak voor de Tweede Kamerverkiezingen werd vermoord. Door de politieke versnippering waren er in 2017 vier partijen nodig voor een Kamermeerderheid.</p>
<div class="info-box let-op">
  <span class="kop">⚖️ Grondwet 1983</span>
  De veranderde mentaliteit leidde in 1983 tot een grondwetswijziging: artikel 1 verbood discriminatie, en er kwamen sociale grondrechten bij, zoals het recht op onderwijs, werk, gezondheidszorg en een schoon milieu.
</div>
    `,
    vragen: [
      {
        id: "h5_3_v1",
        niveau: 1,
        type: "mc",
        vraag: "Wat veroorzaakte in 1973 het einde van de economische bloeiperiode in Nederland?",
        opties: [
          "Een sterke stijging van de olieprijs",
          "Een overstroming",
          "De invoering van de euro",
          "Het einde van de Koude Oorlog"
        ],
        antwoord: 0,
        uitleg: "Door een sterke stijging van de olieprijs in 1973 ontstond de oliecrisis, waardoor de economische bloeiperiode eindigde."
      },
      {
        id: "h5_3_v2",
        niveau: 1,
        type: "mc",
        vraag: "Wat wordt bedoeld met een 'postindustriële samenleving'?",
        opties: [
          "Een samenleving zonder enige industrie",
          "Een samenleving waarin de dienstensector belangrijker is geworden dan de industrie",
          "Een samenleving die teruggaat naar de landbouw",
          "Een samenleving zonder overheid"
        ],
        antwoord: 1,
        uitleg: "In een postindustriële samenleving is de dienstensector belangrijker geworden dan de industriesector."
      },
      {
        id: "h5_3_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Koning Willem-Alexander sprak in de troonrede van 2013 over de omslag naar een participatiesamenleving.",
        antwoord: true,
        uitleg: "Waar! Hij zei dat van mensen die dat kunnen, wordt gevraagd verantwoordelijkheid te nemen voor hun eigen leven en omgeving."
      },
      {
        id: "h5_3_v4",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Na 1973 nam de werkloosheid in Nederland juist snel af.",
        antwoord: false,
        uitleg: "Onwaar. Na 1973 ontstond voor het eerst sinds de jaren 1930 grote werkloosheid, met een dieptepunt in 1984."
      },
      {
        id: "h5_3_v5",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe heet de wet uit 2005 die de WAO verving en alleen nog uitkeert aan mensen die nooit meer kunnen werken?",
        antwoord: "WIA",
        uitleg: "In 2005 kwam de WIA, waarop alleen mensen die nooit meer konden werken blijvend recht hadden."
      },
      {
        id: "h5_3_v6",
        niveau: 2,
        type: "mc",
        vraag: "In welk jaar werd het homohuwelijk in Nederland ingevoerd, als eerste land ter wereld?",
        opties: [
          "1983",
          "1994",
          "2002",
          "2013"
        ],
        antwoord: 2,
        uitleg: "In 2002 voerde Nederland als eerste land ter wereld het homohuwelijk in."
      },
      {
        id: "h5_3_v7",
        niveau: 3,
        type: "mc",
        vraag: "Wat werd er in 1983 aan de grondwet toegevoegd, naast het discriminatieverbod?",
        opties: [
          "Het recht om nooit belasting te betalen",
          "Het verbod op politieke partijen",
          "De doodstraf",
          "Sociale grondrechten zoals recht op onderwijs en gezondheidszorg"
        ],
        antwoord: 3,
        uitleg: "In 1983 werd de grondwet uitgebreid met sociale grondrechten, zoals het recht op onderwijs, werk, gezondheidszorg en een schoon milieu."
      },
      {
        id: "h5_3_v8",
        niveau: 3,
        type: "invoer",
        vraag: "Welke term wordt gebruikt voor een samenleving waarin mensen veel informatie- en communicatietechnologie gebruiken in werk en vrije tijd?",
        antwoord: "informatiemaatschappij",
        uitleg: "Door de opkomst van computers en mobiele telefoons ontstond omstreeks 1990 een informatiemaatschappij."
      }
    ]
  });
})();
