/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 3.5: Lessen van de oorlog
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h3-5",
    hoofdstuk: 3,
    paragraaf: "3.5",
    titel: "Lessen van de oorlog",
    korteUitleg: "De oprichting van de Verenigde Naties, de oorlogstribunalen en het herdenken van de oorlog.",
    icoon: "🕊️",
    theorie: `
<h3>3.5 Lessen van de oorlog</h3>

<p>Op 14 augustus 1941 ontmoetten Churchill en Roosevelt elkaar op een oorlogsschip en gaven een verklaring uit dat alle landen na de oorlog moesten samenwerken voor vrede, vrijheid en welvaart. Op 1 januari 1942 ondertekenden 26 geallieerde landen deze "Verklaring van de Verenigde Naties". Roosevelt wilde hiervan een nieuwe volkenorganisatie maken, sterker dan de machteloze Volkenbond. In oktober 1945 werden de <b>Verenigde Naties (VN)</b> officieel opgericht.</p>

<h4>De Veiligheidsraad</h4>
<p>Tegenwoordig zijn bijna alle staten van de wereld lid van de VN. Een belangrijk onderdeel is de <b>Veiligheidsraad</b>, die bindende besluiten kan nemen waaraan iedereen zich moet houden. Er zitten vijftien lidstaten in, waarvan vijf permanent lid zijn met vetorecht: de VS, Rusland, Groot-Brittannië, Frankrijk en China. In 1948 namen de Verenigde Naties de Universele Verklaring van de Rechten van de Mens aan, gebaseerd op vier vrijheden: vrijheid van meningsuiting, vrijheid van godsdienst, en bescherming tegen gebrek en tegen angst.</p>

<div class="formule-box">
  <span class="formule">Oorlogstribunalen</span>
  <small>
    • Neurenberg (eind 1945 - eind 1946): proces tegen 22 belangrijkste nazileiders, elf kregen de doodstraf, onder wie Seyss-Inquart<br>
    • Tokio (1946-1948): proces tegen de belangrijkste Japanse leiders, zeven kregen de doodstraf<br>
    • Nederland: bijzondere gerechtshoven berechtten collaborateurs; NSB-leider Mussert werd in 1946 geëxecuteerd wegens landverraad<br>
    • Voor het eerst werden hoge leiders internationaal berecht voor "misdaden tegen de menselijkheid" en "misdaden tegen de vrede"
  </small>
</div>

<div class="voorbeeld">
  <span class="vb-kop">🔎 Het verhaal van de Witte Roos</span>
  <p class="stap"><b>Stap 1:</b> Hans en Sophie Scholl waren studenten in München en lid van een geweldloze verzetsgroep, die Weisse Rose.</p>
  <p class="stap"><b>Stap 2:</b> De groep verspreidde pamfletten die opriepen tot verzet tegen het naziregime, zonder ooit geweld te gebruiken.</p>
  <p class="stap"><b>Stap 3:</b> Op 18 februari 1943 werden ze betrapt, ter dood veroordeeld en onthoofd — een voorbeeld van moed tegen de overgrote meerderheid van Duitsers die niet in verzet kwam.</p>
</div>

<h4>Herdenken en vieren</h4>
<p>In Nederland vindt op 4 mei de Nationale <b>Dodenherdenking</b> plaats op de Dam in Amsterdam, waarbij alle omgekomen burgers en militairen worden herdacht. Op 5 mei wordt <b>Bevrijdingsdag</b> gevierd, met aandacht voor vrijheid, democratie, de rechtsstaat en mensenrechten. Buiten Europa herdenken veel landen het einde van de oorlog op 15 augustus, de datum van de Japanse capitulatie; in Nederland vindt dan de Nationale Indië-herdenking plaats bij het Indisch Monument in Den Haag.</p>
    `,
    vragen: [
      {
        id: "h3_5_v1",
        niveau: 1,
        type: "mc",
        vraag: "Welke internationale organisatie werd in oktober 1945 opgericht om vrede en veiligheid te bewaren?",
        opties: [
          "De Volkenbond",
          "De Verenigde Naties",
          "De Europese Unie",
          "De NAVO"
        ],
        antwoord: 1,
        uitleg: "De Verenigde Naties (VN) werden opgericht als sterkere opvolger van de machteloze Volkenbond."
      },
      {
        id: "h3_5_v2",
        niveau: 1,
        type: "waaronwaar",
        vraag: "De Veiligheidsraad van de VN heeft vijf permanente leden die besluiten kunnen tegenhouden met hun vetorecht.",
        antwoord: true,
        uitleg: "Waar! De VS, Rusland, Groot-Brittannië, Frankrijk en China zijn permanent lid van de Veiligheidsraad en hebben vetorecht."
      },
      {
        id: "h3_5_v3",
        niveau: 1,
        type: "invoer",
        vraag: "In welke Duitse stad vond van eind 1945 tot eind 1946 het proces tegen de belangrijkste nazileiders plaats?",
        antwoord: "Neurenberg|neurenberg",
        uitleg: "In het Neurenbergproces werden 22 belangrijke nazi's berecht door Amerikaanse, Britse, Russische en Franse rechters."
      },
      {
        id: "h3_5_v4",
        niveau: 2,
        type: "mc",
        vraag: "Wat was het gevolg van het Neurenbergproces voor Seyss-Inquart?",
        opties: [
          "Hij werd vrijgesproken wegens gebrek aan bewijs.",
          "Hij kreeg levenslange gevangenisstraf in Berlijn.",
          "Hij kreeg de doodstraf, vooral vanwege zijn terreurbewind in Nederland.",
          "Hij werd verbannen naar Oostenrijk."
        ],
        antwoord: 2,
        uitleg: "Seyss-Inquart kreeg de doodstraf voor oorlogsmisdaden en misdaden tegen de menselijkheid, vooral om zijn optreden als rijkscommissaris in Nederland."
      },
      {
        id: "h3_5_v5",
        niveau: 2,
        type: "waaronwaar",
        vraag: "NSB-leider Mussert kreeg na de oorlog gratie van de Nederlandse regering en bleef in leven.",
        antwoord: false,
        uitleg: "Onwaar. Mussert werd wegens landverraad ter dood veroordeeld en in 1946 geëxecuteerd in de Scheveningse duinen."
      },
      {
        id: "h3_5_v6",
        niveau: 2,
        type: "invoer",
        vraag: "Op welke datum viert Nederland jaarlijks Bevrijdingsdag?",
        antwoord: "5 mei",
        uitleg: "Op 5 mei 1945 gaf het Duitse leger in Nederland zich over; deze datum wordt sindsdien jaarlijks gevierd."
      },
      {
        id: "h3_5_v7",
        niveau: 3,
        type: "mc",
        vraag: "Op welke vier vrijheden was de Universele Verklaring van de Rechten van de Mens uit 1948 gebaseerd?",
        opties: [
          "Vrijheid van reizen, van eigendom, van handel en van onderwijs.",
          "Vrijheid van meningsuiting en godsdienst, en bescherming tegen gebrek en angst.",
          "Vrijheid van pers, van religie, van wapenbezit en van vergadering.",
          "Vrijheid van beroep, van huwelijk, van migratie en van stemrecht."
        ],
        antwoord: 1,
        uitleg: "De vier vrijheden waren: vrijheid van meningsuiting, vrijheid van godsdienst, vrijwaring van gebrek en vrijwaring van angst."
      },
      {
        id: "h3_5_v8",
        niveau: 3,
        type: "waaronwaar",
        vraag: "De Duitse verzetsgroep Weisse Rose pleegde gewelddadige aanslagen op nazi-leiders.",
        antwoord: false,
        uitleg: "Onwaar. De Weisse Rose was een geweldloze studentengroep die alleen pamfletten drukte en verspreidde tegen het naziregime."
      }
    ]
  });
})();
