/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 5.2: Besluiten en besturen
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h5-2",
    hoofdstuk: 5,
    paragraaf: "5.2",
    titel: "Besluiten en besturen",
    korteUitleg: "De Watersnoodramp en de Deltawet, regering en parlement, lagere overheden en Prinsjesdag.",
    icoon: "🏛️",
    theorie: `
<h3>5.2 Besluiten en besturen</h3>
<p>Op 1 februari 1953 werd Zuidwest-Nederland getroffen door een natuurramp. Door een zware noordwesterstorm en een extreem hoge vloed braken tientallen dijken door. Een kolkende watermassa drong het land binnen; in Zeeland, Zuid-Holland en West-Brabant kwamen 1836 mensen om het leven.</p>
<div class="voorbeeld">
  <span class="vb-kop">Van watersnoodramp naar wet</span>
  <span class="stap">1. Na de ramp maakten ambtenaren een plan (het Deltaplan) om dijken te verhogen en drie zeearmen af te sluiten.</span>
  <span class="stap">2. In november 1955 diende de regering het wetsvoorstel voor de Deltawet in bij de Tweede Kamer.</span>
  <span class="stap">3. In 1957 keurde een meerderheid van de Tweede Kamer het wetsvoorstel goed, in 1958 stemde ook de Eerste Kamer in.</span>
  <span class="stap">4. Koningin Juliana zette haar handtekening eronder: het wetsvoorstel was een wet geworden en de bouw kon beginnen.</span>
</div>
<p>Later werden de plannen aangepast: rond 1970 groeide het besef dat het volledig afsluiten van de Oosterschelde slecht was voor het milieu. Met steun van D66-Kamerlid Jan Terlouw besloot het kabinet-Den Uyl de Oosterschelde niet helemaal af te sluiten, maar ook niet helemaal open te houden. Er kwam een stormvloedkering met schuiven, die in 1986 door koningin Beatrix in gebruik werd genomen.</p>

<h4>Regering en parlement</h4>
<p>De Nederlandse parlementaire democratie werkt volgens regels die Thorbecke in 1848 opstelde.</p>
<div class="formule-box">
  <span class="formule">regering = kabinet (ministers + staatssecretarissen) + de koning</span>
  <small>De koning is staatshoofd zonder macht; de ministers zijn verantwoordelijk voor zijn daden en uitspraken (ministeriële verantwoordelijkheid).</small>
</div>
<p>De regering bestuurt het land en maakt wetten; het parlement (de Staten-Generaal) controleert de regering en maakt samen met haar wetten. De Kamerleden van één partij vormen samen een <b>fractie</b>. Omdat parlementsleden alles moeten kunnen zeggen, hebben ze <b>parlementaire onschendbaarheid</b>: ze kunnen niet vervolgd worden voor uitspraken tijdens een vergadering.</p>
<p>Burgers kiezen minstens eens in de vier jaar de 150 leden van de Tweede Kamer. Na de verkiezingen vormt een aantal partijen samen een kabinet: hun samenwerking heet een <b>coalitie</b>. Partijen die niet meeregeren, vormen de <b>oppositie</b>. Tijdens de kabinetsformatie leggen de coalitiepartijen hun afspraken vast in een <b>regeerakkoord</b>. Burgers kunnen de Tweede Kamer ook dwingen om over een onderwerp te vergaderen door 40 000 handtekeningen te verzamelen: het <b>burgerinitiatief</b>.</p>

<h4>Lagere overheden en Prinsjesdag</h4>
<p>Naast de rijksoverheid zijn er lagere overheden: provincies, gemeenten en waterschappen. Inwoners kiezen de Provinciale Staten, die op hun beurt het provinciebestuur kiezen: de Gedeputeerde Staten, voorgezeten door de commissaris van de Koning. In de gemeenten kiezen burgers de gemeenteraad, die het college van burgemeester en wethouders (B en W) controleert. De regering benoemt de burgemeester en de dijkgraven van de waterschappen.</p>
<div class="info-box">
  <span class="kop">📅 Prinsjesdag</span>
  Op de derde dinsdag van september leest de koning in de Ridderzaal de troonrede voor met de plannen van de regering. Daarna opent de minister van Financiën in de Tweede Kamer een koffertje (voor het eerst gebruikt in 1946) met de rijksbegroting: de miljoenennota.
</div>
    `,
    vragen: [
      {
        id: "h5_2_v1",
        niveau: 1,
        type: "mc",
        vraag: "Wie stelde in 1848 de regels op waarop de Nederlandse parlementaire democratie nog steeds is gebaseerd?",
        opties: [
          "Thorbecke",
          "Willem Drees",
          "Willem I",
          "Willem-Alexander"
        ],
        antwoord: 0,
        uitleg: "Thorbecke stelde in 1848 de grondregels op van de Nederlandse parlementaire democratie."
      },
      {
        id: "h5_2_v2",
        niveau: 1,
        type: "mc",
        vraag: "Uit wie bestaat het Nederlandse kabinet?",
        opties: [
          "Alleen de koning",
          "Ministers en staatssecretarissen",
          "De Provinciale Staten",
          "De rechterlijke macht"
        ],
        antwoord: 1,
        uitleg: "Het kabinet bestaat uit ministers en staatssecretarissen (onderministers); samen met de koning vormen zij de regering."
      },
      {
        id: "h5_2_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Bij de watersnoodramp van 1 februari 1953 kwamen 1836 mensen om het leven.",
        antwoord: true,
        uitleg: "Waar! In Zeeland, Zuid-Holland en West-Brabant kwamen door de watersnoodramp 1836 mensen om."
      },
      {
        id: "h5_2_v4",
        niveau: 2,
        type: "waaronwaar",
        vraag: "Een minister kan nooit door de Tweede Kamer worden gedwongen om af te treden.",
        antwoord: false,
        uitleg: "Onwaar. Als een Kamermeerderheid het vertrouwen in een minister opzegt, moet die aftreden."
      },
      {
        id: "h5_2_v5",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe heet de samenwerking van regeringspartijen die na verkiezingen samen een kabinet vormen?",
        antwoord: "coalitie",
        uitleg: "De samenwerkende regeringspartijen vormen samen een coalitie."
      },
      {
        id: "h5_2_v6",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe noemen we het recht om jezelf verkiesbaar te stellen voor bijvoorbeeld de Tweede Kamer?",
        antwoord: "passief kiesrecht",
        uitleg: "Passief kiesrecht is het recht om jezelf verkiesbaar te stellen bij verkiezingen."
      },
      {
        id: "h5_2_v7",
        niveau: 3,
        type: "mc",
        vraag: "Wie benoemt de burgemeester van een Nederlandse gemeente?",
        opties: [
          "De gemeenteraad",
          "De commissaris van de Koning",
          "De regering",
          "De kiezers rechtstreeks"
        ],
        antwoord: 2,
        uitleg: "De regering benoemt de burgemeester, nadat de gemeenteraad daarover heeft geadviseerd."
      },
      {
        id: "h5_2_v8",
        niveau: 3,
        type: "mc",
        vraag: "Hoeveel leden telt de Tweede Kamer?",
        opties: [
          "100",
          "75",
          "200",
          "150"
        ],
        antwoord: 3,
        uitleg: "De Tweede Kamer telt 150 leden, die minstens eens in de vier jaar worden gekozen."
      }
    ]
  });
})();
