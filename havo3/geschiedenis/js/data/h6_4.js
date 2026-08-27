/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 6.4: Digitalisering en globalisering
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h6-4",
    hoofdstuk: 6,
    paragraaf: "6.4",
    titel: "Digitalisering en globalisering",
    korteUitleg: "Van pc en internet tot multinationals, de G20, de kredietcrisis van 2007 en de veranderende welvaartsverdeling.",
    icoon: "💻",
    theorie: `
<h3>6.4 Digitalisering en globalisering</h3>

<p>De verandering van de samenleving onder invloed van ICT wordt <b>digitalisering</b> genoemd. De eerste computers werden tijdens de Tweede Wereldoorlog gebouwd, maar de meeste mensen kwamen er pas mee in aanraking nadat in 1981 de <b>personal computer (pc)</b> op de markt kwam. In 1991 ontwikkelden Europese wetenschappers een computernetwerk met websites: het <b>world wide web (www)</b>.</p>
<p>Ook mobiel bellen brak door: in 1992 introduceerde het Finse bedrijf Nokia digitale mobiele telefonie (gsm). Computers werden steeds beter, sneller, goedkoper en kleiner, wat leidde tot de laptop en in 2007 tot de <b>smartphone</b>, waarin mobiele telefonie en internet samengingen.</p>

<h4>Globalisering</h4>
<p>Computer, internet en mobiele telefonie maakten internationale contacten veel makkelijker en bevorderden de <b>globalisering</b>: de toenemende economische, sociale en culturele verbondenheid van delen van de wereld. <b>Multinationals</b> — bedrijven met vestigingen in veel landen — verplaatsten hun productie naar lagelonenlanden. Zo werd vanaf de jaren 1960 westerse kleding gemaakt in bijvoorbeeld Indonesië, Vietnam en Bangladesh. Ook verspreidden westerse producten zich wereldwijd: na de Koude Oorlog vestigden McDonald's, Coca-Cola en het Franse L'Oréal zich ook in Rusland en China.</p>
<div class="voorbeeld">
  <span class="vb-kop">👟 Het verhaal van Reebok</span>
  <div class="stap"><b>1895:</b> de 14-jarige leerling-schoenmaker Joseph William Foster begint in het Engelse Bolton met hardloopschoenen met spikes.</div>
  <div class="stap"><b>1958:</b> zijn kleinzonen nemen de zaak over onder de naam Reebok.</div>
  <div class="stap"><b>Vanaf ±1970:</b> de productie verhuist naar Zuid-Korea en Taiwan.</div>
  <div class="stap"><b>Vanaf ±1990:</b> door stijgende lonen verhuist de productie verder naar China en Indonesië.</div>
  <div class="stap"><b>2005:</b> Adidas neemt Reebok over; de merknaam blijft in gebruik.</div>
</div>

<h4>Internationale economische samenwerking</h4>
<p>Door de globalisering was meer samenwerking nodig. Al in 1945 richtten de VN het <b>IMF</b> (Internationaal Monetair Fonds) op, dat leningen geeft aan landen met economische problemen. In 1975 gingen zes sterke industrielanden (Duitsland, Frankrijk, Groot-Brittannië, Italië, Japan en de VS) als <b>G6</b> geregeld overleggen; met Canada werd dit de G7, met Rusland de G8. In 1999 ontstond de <b>G20</b>, toen de G8 ook ging overleggen met de EU en elf andere sterke industrielanden zoals China, India en Zuid-Korea.</p>

<h4>De kredietcrisis (2007-2012)</h4>
<div class="formule-box">
  <span class="formule">Hoe ontstond de crisis?</span>
  <small>
    Amerikanen leenden via goedkope hypotheken te veel geld voor een huis → de rente steeg → veel huiseigenaren konden hun hypotheek niet meer betalen → huizenprijzen daalden → banken leden verliezen en dreigden failliet te gaan → de crisis sloeg over naar Europa en Japan.
  </small>
</div>
<p>Anders dan in de jaren 1930 grepen overheden nu snel in en werkten ze samen: banken werden met overheidssteun gered en landen bleven vrijhandel bevorderen. Toen de Griekse overheid failliet dreigde te gaan, leenden de EU en het IMF miljarden euro's aan Griekenland, in ruil voor bezuinigingen. Omstreeks 2012 was de wereldcrisis voorbij.</p>

<h4>Welvaartsverschillen</h4>
<p>Sinds de jaren 1990 groeiden de economieën van China en India zeer snel, naar het exportgerichte voorbeeld van Zuid-Korea. China werd de grootste exporteur ter wereld, 'de werkplaats van de wereld'. Tussen 1990 en 2015 steeg de levensverwachting in India van 58 naar 68 jaar en in China van 69 naar 76 jaar, en daalde het aantal mensen in extreme armoede fors. Tegelijk groeide binnen de westerse wereld het verschil tussen hoger- en lageropgeleiden: door automatisering en globalisering verdwenen banen voor lageropgeleiden, waardoor vooral in de VS de armoede toenam.</p>
    `,
    vragen: [
      {
        id: "h6_4_v1",
        niveau: 1,
        type: "mc",
        vraag: "In welk jaar kwam de personal computer (pc) op de markt, waardoor de meeste mensen voor het eerst met computers in aanraking kwamen?",
        opties: ["1969", "1975", "1981", "1991"],
        antwoord: 2,
        uitleg: "In 1981 kwam de personal computer op de markt, waarna steeds meer mensen thuis of op kantoor een computer gebruikten."
      },
      {
        id: "h6_4_v2",
        niveau: 1,
        type: "invoer",
        vraag: "Welk Fins bedrijf introduceerde in 1992 digitale mobiele telefonie (gsm)?",
        antwoord: "Nokia",
        uitleg: "Nokia maakte met digitale gsm-technologie steeds lichtere mobiele telefoons mogelijk."
      },
      {
        id: "h6_4_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "In 1991 ontwikkelden Amerikaanse wetenschappers het world wide web (www).",
        antwoord: false,
        uitleg: "Niet waar. Het world wide web werd in 1991 ontwikkeld door Europese wetenschappers, niet door Amerikaanse."
      },
      {
        id: "h6_4_v4",
        niveau: 2,
        type: "mc",
        vraag: "Welke zes landen vormden in 1975 de G6, de groep sterke industrielanden die geregeld economische en politieke zaken besprak?",
        opties: [
          "Duitsland, Frankrijk, Groot-Brittannië, Italië, Japan en de VS",
          "China, India, Rusland, Brazilië, Zuid-Afrika en de VS",
          "Nederland, België, Luxemburg, Frankrijk, Duitsland en Italië",
          "De VS, Canada, Mexico, Brazilië, Argentinië en Chili"
        ],
        antwoord: 0,
        uitleg: "De G6 bestond uit Duitsland, Frankrijk, Groot-Brittannië, Italië, Japan en de VS; met Canada erbij werd het later G7, met Rusland erbij G8."
      },
      {
        id: "h6_4_v5",
        niveau: 2,
        type: "waaronwaar",
        vraag: "De G20 ontstond in 1999 toen de G8 ook ging overleggen met de EU en elf andere sterke industrielanden, zoals China en India.",
        antwoord: true,
        uitleg: "Waar! De G20 bracht de G8, de EU en elf andere sterke industrielanden samen aan tafel."
      },
      {
        id: "h6_4_v6",
        niveau: 2,
        type: "mc",
        vraag: "Waardoor werd het schoenenmerk Reebok, opgericht in 1895 in Engeland, uiteindelijk een voorbeeld van globalisering?",
        opties: [
          "Het bedrijf bleef de hele geschiedenis alleen in Engeland produceren",
          "De productie verhuisde via Zuid-Korea en Taiwan uiteindelijk naar China en Indonesië vanwege lagere lonen",
          "Het bedrijf werd genationaliseerd door de Britse overheid",
          "Reebok fuseerde met Nokia om smartphones te maken"
        ],
        antwoord: 1,
        uitleg: "De productie van Reebokschoenen verhuisde steeds naar landen met lagere lonen: eerst Zuid-Korea en Taiwan, later China en Indonesië."
      },
      {
        id: "h6_4_v7",
        niveau: 3,
        type: "invoer",
        vraag: "Welke internationale instelling, opgericht in 1945, leent geld aan landen met economische problemen?",
        antwoord: "IMF|Internationaal Monetair Fonds|het IMF",
        uitleg: "Het IMF (Internationaal Monetair Fonds) werd door de VN opgericht om landen met economische problemen te ondersteunen met leningen."
      },
      {
        id: "h6_4_v8",
        niveau: 3,
        type: "mc",
        vraag: "Wat was een belangrijke oorzaak van de kredietcrisis die in 2007 in de VS begon?",
        opties: [
          "Een oorlog tussen de VS en Mexico",
          "Een plotselinge stijging van de olieprijs door een Golfoorlog",
          "Het invoeren van de euro in de Verenigde Staten",
          "Te veel geleend geld voor huizen via goedkope hypotheken, waardoor huiseigenaren in de problemen kwamen toen de rente steeg"
        ],
        antwoord: 3,
        uitleg: "Amerikanen hadden via goedkope hypotheken te veel geleend om een huis te kopen; toen de rente steeg, konden veel huiseigenaren hun hypotheek niet meer betalen."
      }
    ]
  });
})();
