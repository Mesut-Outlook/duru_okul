/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 5.5: Recht in Nederland
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h5-5",
    hoofdstuk: 5,
    paragraaf: "5.5",
    titel: "Recht in Nederland",
    korteUitleg: "De rechtsstaat, de onafhankelijke rechterlijke macht, de Puttense moordzaak en strafrecht, burgerlijk recht en bestuursrecht.",
    icoon: "⚖️",
    theorie: `
<h3>5.5 Recht in Nederland</h3>
<p>Het discriminatieverbod in artikel 1 van de grondwet is een belangrijk principe van onze <b>rechtsstaat</b>: voor de wet zijn alle mensen gelijk. De rechten en plichten van burgers en overheid staan in wetten, en <b>rechters</b> bepalen of iedereen zich daaraan houdt.</p>
<div class="formule-box">
  <span class="formule">onafhankelijke rechterlijke macht</span>
  <small>Rechters worden voor het leven benoemd en kunnen alleen worden ontslagen als ze daar zelf om vragen: bestuurders kunnen dus geen rechters ontslaan die het niet met hen eens zijn.</small>
</div>
<p>Straffen mogen alleen worden opgelegd door de rechterlijke macht. Het bewaken van de openbare orde is de taak van de politie en het <b>Openbaar Ministerie (OM)</b>, het deel van de overheid dat strafbare feiten opspoort en vervolgt. Na een misdrijf verzamelt een <b>officier van justitie</b> van het OM met hulp van de politie bewijzen; als er genoeg bewijs is, moet de verdachte voor de rechtbank verschijnen. Zijn het OM of de verdachte het niet eens met het vonnis, dan kunnen ze in hoger beroep bij een gerechtshof.</p>

<h4>De Puttense moordzaak</h4>
<p>In 1994 werd een 23-jarige vrouw dood gevonden in Putten. De politie zette vier verdachten zwaar onder druk, waarna twee mannen de andere twee als daders aanwezen; deze twee bekenden daarna gedeeltelijk. Er was geen technisch bewijs, maar de rechtbank veroordeelde hen toch tot tien jaar cel.</p>
<div class="voorbeeld">
  <span class="vb-kop">Een rechterlijke dwaling hersteld</span>
  <span class="stap">1. Journalisten twijfelden aan de schuld van de twee veroordeelden.</span>
  <span class="stap">2. In 2001 gaf de Hoge Raad opdracht de zaak over te doen.</span>
  <span class="stap">3. De rechters concludeerden dat de sporen niet naar de verdachten leidden: de twee werden vrijgelaten en kregen € 900 000 schadevergoeding.</span>
  <span class="stap">4. In 2008 werd de echte dader gearresteerd en tot achttien jaar cel veroordeeld.</span>
</div>

<h4>Drie soorten recht</h4>
<p>Het <b>strafrecht</b> gaat over het bestraffen van een <b>misdrijf</b> (een ernstig strafbaar feit) of een <b>overtreding</b> (een licht strafbaar feit). Ook in een strafzaak kan geschikt worden: het OM en de verdachte spreken bijvoorbeeld af dat de verdachte geld betaalt of een <b>taakstraf</b> (onbetaalde arbeid) uitvoert.</p>
<p>Bij het <b>burgerlijk recht</b> gaat het om conflicten tussen burgers, bijvoorbeeld over een koopcontract; burgers kunnen dan naar de burgerrechter of kiezen voor mediation, waarbij een bemiddelaar helpt bij een schikking. Het <b>bestuursrecht</b> regelt conflicten tussen burgers en de overheid: wie bijvoorbeeld een vergunning voor een aanbouw krijgt geweigerd door de gemeente, kan dat aanvechten bij de bestuursrechter.</p>
<div class="info-box tip">
  <span class="kop">👶 Kinderrechten</span>
  Sinds 1989 legt het VN-Kinderrechtenverdrag, ook door Nederland ondertekend, in 52 artikelen rechten van kinderen jonger dan 18 jaar vast, zoals recht op onderwijs, goede zorg en bescherming tegen mishandeling.
</div>
    `,
    vragen: [
      {
        id: "h5_5_v1",
        niveau: 1,
        type: "mc",
        vraag: "Wat overkwam de twee mannen die in de Puttense moordzaak ten onrechte tot tien jaar cel werden veroordeeld?",
        opties: [
          "Ze werden in 2001-2002 alsnog vrijgesproken en kregen schadevergoeding",
          "Ze bleven de rest van hun leven vastzitten",
          "Ze werden minister",
          "Ze werden nooit meer vrijgelaten"
        ],
        antwoord: 0,
        uitleg: "Na heropening van de zaak door de Hoge Raad in 2001 werden de twee mannen vrijgesproken en kregen ze € 900 000 schadevergoeding."
      },
      {
        id: "h5_5_v2",
        niveau: 1,
        type: "mc",
        vraag: "Waarom kunnen rechters in Nederland niet zomaar door bestuurders worden ontslagen?",
        opties: [
          "Omdat er geen wetten over rechters bestaan",
          "Omdat ze voor het leven worden benoemd en alleen zelf ontslag kunnen aanvragen",
          "Omdat rechters boven de koning staan",
          "Omdat rechters altijd gelijk hebben"
        ],
        antwoord: 1,
        uitleg: "Rechters worden voor het leven benoemd en kunnen alleen worden ontslagen als ze daar zelf om vragen."
      },
      {
        id: "h5_5_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Voor de wet zijn in Nederland alle mensen gelijk, zoals artikel 1 van de grondwet vastlegt.",
        antwoord: true,
        uitleg: "Waar! Artikel 1 van de grondwet verbiedt discriminatie en legt vast dat iedereen gelijk wordt behandeld."
      },
      {
        id: "h5_5_v4",
        niveau: 1,
        type: "waaronwaar",
        vraag: "In Nederland mag de politie zelf, zonder tussenkomst van een rechter, iemand tot een gevangenisstraf veroordelen.",
        antwoord: false,
        uitleg: "Onwaar. Straffen mogen alleen worden opgelegd door de rechterlijke macht, niet door de politie."
      },
      {
        id: "h5_5_v5",
        niveau: 2,
        type: "invoer",
        vraag: "Hoe heet het proces waarbij een bemiddelaar burgers helpt om bij een conflict samen tot een schikking te komen, zonder tussenkomst van een rechter?",
        antwoord: "mediation",
        uitleg: "Bij mediation proberen burgers met hulp van een bemiddelaar een schikking te treffen."
      },
      {
        id: "h5_5_v6",
        niveau: 2,
        type: "invoer",
        vraag: "Welk deel van de overheid spoort strafbare feiten op en vervolgt de daders?",
        antwoord: "Openbaar Ministerie|OM|het Openbaar Ministerie",
        uitleg: "Het Openbaar Ministerie (OM) spoort strafbare feiten op en vervolgt de daders."
      },
      {
        id: "h5_5_v7",
        niveau: 3,
        type: "mc",
        vraag: "Wie verzamelt na een misdrijf met hulp van de politie het bewijs tegen een verdachte?",
        opties: [
          "De burgemeester",
          "De Provinciale Staten",
          "De officier van justitie van het Openbaar Ministerie",
          "De Tweede Kamer"
        ],
        antwoord: 2,
        uitleg: "Een officier van justitie van het OM verzamelt met hulp van de politie de bewijzen tegen een verdachte."
      },
      {
        id: "h5_5_v8",
        niveau: 3,
        type: "mc",
        vraag: "Wat kunnen burgers doen als ze het niet eens zijn met het vonnis van de rechtbank?",
        opties: [
          "Meteen naar de koning stappen",
          "Een nieuwe wet indienen",
          "De politie ontslaan",
          "In hoger beroep gaan bij een gerechtshof"
        ],
        antwoord: 3,
        uitleg: "Wie het niet eens is met een vonnis kan in hoger beroep gaan; een gerechtshof beoordeelt de zaak dan opnieuw."
      }
    ]
  });
})();
