/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 1.4: De nieuwe kaart van Europa
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h1-4",
    hoofdstuk: 1,
    paragraaf: "1.4",
    titel: "De nieuwe kaart van Europa",
    korteUitleg: "De Vrede van Versailles (1919), het zelfbeschikkingsrecht, het uiteenvallen van keizerrijken en de stichting van de Republiek Turkije.",
    icoon: "🗺️",
    theorie: `
<h3>1.4 De nieuwe kaart van Europa</h3>

<p>Na de wapenstilstand kwamen de overwinnaars in 1919 bijeen in Parijs. De belangrijkste beslissingen werden genomen door de 'Grote Drie': president <b>Woodrow Wilson</b> (VS), premier <b>Georges Clemenceau</b> (Frankrijk) en premier <b>David Lloyd George</b> (Groot-Brittannië).</p>

<h4>De Vrede van Versailles (juni 1919)</h4>
<p>Duitsland werd niet toegelaten tot de onderhandelingen en werd gedwongen een keihard vredesverdrag te ondertekenen.</p>

<div class="formule-box">
  <span class="formule">De belangrijkste bepalingen voor Duitsland:</span>
  <small>
    • <b>Schuldvraag:</b> Duitsland en zijn bondgenoten kregen de <i>alleenschuld</i> van de oorlog toegewezen.<br>
    • <b>Herstelbetalingen:</b> Duitsland moest gedurende tientallen jaren miljarden goudmarken vergoeden aan Frankrijk en België.<br>
    • <b>Gebiedsverlies:</b> Elzas-Lotharingen ging terug naar Frankrijk; grote delen van Oost-Pruisen gingen naar het nieuwe Polen (Poolse Corridor). Duitsland raakte alle kolonies kwijt.<br>
    • <b>Militaire beperkingen:</b> Het Duitse leger werd beperkt tot maximaal 100.000 man. Zware wapens, tanks, vliegtuigen en duikboten werden verboden.
  </small>
</div>

<h4>De Volkenbond & Zelfbeschikkingsrecht</h4>
<ul>
  <li><b>Volkenbond (1919):</b> Op initiatief van Wilson werd een internationale organisatie opgericht om toekomstige oorlogen te voorkomen. Duitsland en de Sovjet-Unie mochten eerst geen lid worden. Opvallend genoeg weigerde het Amerikaanse Congres zelf lid te worden!</li>
  <li><b>Zelfbeschikkingsrecht:</b> President Wilson vond dat elk volk het recht had om zelf te bepalen bij welke staat zijn gebied hoorde. Dit leidde tot het uiteenvallen van grote multi-etnische keizerrijken.</li>
</ul>

<h4>Nieuwe staten op de Europese kaart</h4>
<p>Door het uiteenvallen van het Russische Rijk, het Duitse Rijk en Oostenrijk-Hongarije ontstonden nieuwe onafhankelijke staten:</p>
<ul>
  <li><b>Finland, Estland, Letland, Litouwen en Polen</b> (losgemaakt van Rusland/Duitsland).</li>
  <li><b>Tsjecho-Slowakije en Hongarije</b> (losgemaakt van Oostenrijk-Hongarije).</li>
  <li><b>Koninkrijk Joegoslavië</b> (nieuwe Balkanstaat voor Serviers, Kroaten, Slovenen en Bosniërs).</li>
  <li>Oostenrijk bleef over als een klein Duitstalig staatje.</li>
</ul>

<h4>De stichting van de Republiek Turkije (1923)</h4>
<p>Het Ottomaanse Rijk stortte eveneens in. Engeland en Frankrijk verdeelden de Arabische gebieden als <b>mandaatgebieden</b> namens de Volkenbond.</p>
<ul>
  <li><b>Griekse inval & Oorlog:</b> De Geallieerden wilden ook Anatolië verdelen. In 1919 landde een Grieks leger in Smyrna (Izmir). De Turkse bevolking kwam in opstand onder leiding van generaal <b>Mustafa Kemal</b>.</li>
  <li><b>Stichting van de Republiek (1923):</b> Kemal verdreef de Griekse troepen uit Anatolië en schafte het sultanaat af. In 1923 werd de <b>Republiek Turkije</b> uitgeroepen en werd Kemal de eerste president. Hij kreeg de erenaam <b>Atatürk</b> ('Vader der Turken').</li>
  <li><b>Volkenruil:</b> In het vredesverdrag van Lausanne werd een verplichte volkenruil afgesproken: 1,2 miljoen Grieken verhuisden van Turkije naar Griekenland en 500.000 Turken van Griekenland naar Turkije.</li>
</ul>
    `,
    vragen: [
      {
        id: "h1_4_v1",
        niveau: 1,
        type: "mc",
        vraag: "Welke drie regeringsleiders ('De Grote Drie') bepaalden de inhoud van het Verdrag van Versailles?",
        opties: [
          "Wilson (VS), Clemenceau (Frankrijk) en Lloyd George (Groot-Brittannië)",
          "Lenin (Rusland), Bismarck (Duitsland) en Churchill (Groot-Brittannië)",
          "Atatürk (Turkije), Wilhelmina (Nederland) en Roosevelt (VS)",
          "Hitler (Duitsland), Mussolini (Italië) en Stalin (Sovjet-Unie)"
        ],
        antwoord: 0,
        uitleg: "President Wilson (VS), premier Clemenceau (Frankrijk) en premier Lloyd George (VK) voerden de boventoon in Versailles."
      },
      {
        id: "h1_4_v2",
        niveau: 1,
        type: "waaronwaar",
        vraag: "In het Verdrag van Versailles stond dat Duitsland als enige de schuld droeg voor de Eerste Wereldoorlog.",
        antwoord: true,
        uitleg: "Waar! Artikel 231 van het verdrag legde de volledige schuld (alleenschuld) en herstelbetalingen bij Duitsland neer."
      },
      {
        id: "h1_4_v3",
        niveau: 1,
        type: "invoer",
        vraag: "Hoe heette de volkerenorganisatie die in 1919 werd opgericht om toekomstige oorlogen te voorkomen?",
        antwoord: "Volkenbond|De Volkenbond|volkenbond",
        uitleg: "De Volkenbond werd in 1919 opgericht, maar bleek zwak doordat de VS, Duitsland en de Sovjet-Unie er aanvankelijk geen lid van waren."
      },
      {
        id: "h1_4_v4",
        niveau: 2,
        type: "mc",
        vraag: "Wat wordt bedoeld met het 'zelfbeschikkingsrecht' dat door president Wilson werd gepropageerd?",
        opties: [
          "Het recht van keizers om hun volk zonder parlement te besturen.",
          "Het recht van elk volk om zelf te bepalen bij welke staat hun gebied hoort en hoe ze bestuurd worden.",
          "Het recht van winnende landen om kolonies van de verliezer af te pakken.",
          "Het recht van militairen om in te grijpen bij opstanden."
        ],
        antwoord: 1,
        uitleg: "Zelfbeschikkingsrecht houdt in dat volken het recht hebben om hun eigen onafhankelijke staat en bestuur te kiezen."
      },
      {
        id: "h1_4_v5",
        niveau: 2,
        type: "invoer",
        vraag: "Welke erenaam kreeg generaal Mustafa Kemal nadat hij in 1923 de Republiek Turkije stichtte?",
        antwoord: "Atatürk|Ataturk|ataturk|atatürk",
        uitleg: "Mustafa Kemal kreeg van het parlement de erenaam Atatürk, wat 'Vader der Turken' betekent."
      },
      {
        id: "h1_4_v6",
        niveau: 2,
        type: "mc",
        vraag: "Wat gebeurde er tijdens de afgesproken 'volkenruil' tussen Griekenland en Turkije na 1923?",
        opties: [
          "1,2 miljoen Grieken verhuisden van Turkije naar Griekenland en 500.000 Turken van Griekenland naar Turkije.",
          "Alle Grieken en Turken verhuisden samen naar Cyprus.",
          "Griekenland en Turkije werden samengevoegd tot één koninkrijk.",
          "Alleen soldaten moesten van plaats ruilen."
        ],
        antwoord: 0,
        uitleg: "Om verdere etnische conflicten te voorkomen spraken beide landen een grootschalige verplichte bevolkingsruil af."
      },
      {
        id: "h1_4_v7",
        niveau: 3,
        type: "mc",
        vraag: "Welke van de onderstaande nieuwe staten ontstond NIET op de kaart van Europa na het uiteenvallen van Oostenrijk-Hongarije of het Russische Rijk?",
        opties: [
          "Tsjecho-Slowakije",
          "Joegoslavië",
          "Polen",
          "België"
        ],
        antwoord: 3,
        uitleg: "België bestond al sinds 1830. Tsjecho-Slowakije, Joegoslavië en Polen waren gloednieuwe (of herstelde) staten op de kaart na 1919."
      },
      {
        id: "h1_4_v8",
        niveau: 3,
        type: "waaronwaar",
        vraag: "Hoewel president Wilson van de VS de grote bedenker van de Volkenbond was, weigerde het Amerikaanse Congres dat de VS lid werden.",
        antwoord: true,
        uitleg: "Waar! Het Amerikaanse Congres wilde zich niet meer mengen in Europese conflicten en stemde tegen het lidmaatschap van de Volkenbond."
      }
    ]
  });
})();
