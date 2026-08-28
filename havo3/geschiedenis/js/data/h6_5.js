/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Paragraaf 6.5: Mens en milieu
   ========================================================= */
(function () {
  "use strict";

  DURU.register({
    id: "h6-5",
    hoofdstuk: 6,
    paragraaf: "6.5",
    titel: "Mens en milieu",
    korteUitleg: "Energiegebruik en kernrampen, de opkomst van de milieubeweging, de Groningse gasbel en de opwarming van de aarde.",
    icoon: "🌍",
    theorie: `
<h3>6.5 Mens en milieu</h3>

<p>Eeuwenlang haalden mensen energie uit wind, water en spierkracht. Door de industrialisatie gingen ze steeds meer steenkool, aardolie en aardgas verbranden. Verbranding van steenkool veroorzaakte in steden een dikke laag smog; door technologische verbeteringen kwam geleidelijk minder roet in het milieu, maar door de toename van productie en transport nam de totale vervuiling toch toe.</p>

<h4>Energie en kernrampen</h4>
<p>In de jaren 1970 werd het opraken van de fossiele energievoorraden als grote bedreiging gezien. Kernenergie leek een schoon alternatief, maar tegenstanders wezen op de risico's. Zij kregen gelijk toen in 1986 een ongeluk in de Sovjetkerncentrale van <b>Tsjernobyl</b> een groot gebied onbewoonbaar maakte door radioactieve straling. Veel landen stopten met de bouw van kerncentrales. Net toen kernenergie weer in opkomst was, vond in 2011 een kernramp plaats in Japan (Fukushima), waarna opnieuw veel landen het gebruik van kernenergie beperkten.</p>

<h4>De milieubeweging</h4>
<p>Al in de 19e eeuw leidden verstedelijking en industrialisatie tot zorgen over de volksgezondheid. In 1905 werd de <b>Vereniging Natuurmonumenten</b> opgericht om het Naardermeer te redden, dat Amsterdam als vuilnisbelt wilde gebruiken — het werd het eerste Nederlandse natuurreservaat.</p>
<div class="voorbeeld">
  <span class="vb-kop">🔥 Het verhaal van de gasbel</span>
  <div class="stap"><b>1959:</b> onder een bietenveld bij Slochteren (Groningen) wordt op 2,6 kilometer diepte het grootste Europese aardgasveld buiten Rusland ontdekt.</div>
  <div class="stap"><b>1966:</b> Nederland sluit als eerste land ter wereld al zijn kolenmijnen en stapt massaal over op het schonere aardgas.</div>
  <div class="stap"><b>Gevolg:</b> de opbrengst van gasexport draagt jarenlang bij aan de Nederlandse welvaart.</div>
  <div class="stap"><b>Keerzijde:</b> de gaswinning veroorzaakt bodemdaling en honderden aardbevingen — vanaf 2014 wordt de winning daarom beperkt.</div>
</div>
<p>In de jaren 1970 kreeg de milieubeweging massale aanhang: het milieu werd aangetast door een enorme vervuiling en de natuur slonk snel door nieuwe woonwijken, bedrijfsterreinen en autowegen. Het was ook een vorm van verzet van jongeren tegen het naoorlogse materialisme van oudere generaties. Er ontstonden honderden actiegroepen, zoals <b>Greenpeace</b>, dat in 1971 in Canada werd opgericht.</p>

<h4>Opwarming van de aarde</h4>
<p>In de jaren 2000 werd de opwarming van de aarde het belangrijkste milieuprobleem. Sinds het begin van de industrialisatie stegen de temperaturen op aarde, en vanaf 1990 steeds sneller. Bij de verbranding van fossiele brandstoffen komt CO₂ in de atmosfeer, dat als broeikasgas warmte vasthoudt bij het aardoppervlak.</p>
<div class="formule-box">
  <span class="formule">Het broeikaseffect</span>
  <small>Fossiele brandstoffen verbranden → CO₂ komt vrij → CO₂ houdt warmte vast bij het aardoppervlak → de temperatuur op aarde stijgt.</small>
</div>
<p>De voormalige Amerikaanse vicepresident <b>Al Gore</b> trok in 2006 grote aandacht met de film en het boek <i>An Inconvenient Truth</i>, waarin hij liet zien dat het smelten van het poolijs tot een gevaarlijke zeespiegelstijging kan leiden. Om verdere opwarming te beperken, maakten bijna alle landen in 2015 op een VN-klimaatconferentie in Parijs afspraken om te streven naar een <b>energietransitie</b>: een overgang van fossiele brandstoffen naar duurzame energie, zoals wind- en zonne-energie.</p>
<div class="info-box tip">
  <span class="kop">💡 Onthoud</span>
  Energietransitie = overstappen van fossiele brandstoffen (kolen, olie, gas) naar duurzame energie (wind, zon).
</div>
    `,
    vragen: [
      {
        id: "h6_5_v1",
        niveau: 1,
        type: "mc",
        vraag: "In welk jaar werd de Vereniging Natuurmonumenten opgericht om het Naardermeer te redden van gebruik als vuilnisbelt?",
        opties: ["1971", "1895", "1945", "1905"],
        antwoord: 3,
        uitleg: "In 1905 kocht de nieuw opgerichte Vereniging Natuurmonumenten het Naardermeer, dat Amsterdam als vuilnisbelt wilde gebruiken."
      },
      {
        id: "h6_5_v2",
        niveau: 1,
        type: "invoer",
        vraag: "In welke Nederlandse provincie werd in 1959 de gasbel van Slochteren ontdekt?",
        antwoord: "Groningen",
        uitleg: "De gasbel van Slochteren, het grootste Europese aardgasveld buiten Rusland, ligt in de provincie Groningen."
      },
      {
        id: "h6_5_v3",
        niveau: 1,
        type: "waaronwaar",
        vraag: "Door technologische verbeteringen kwam geleidelijk minder roet in het milieu, maar door de toename van productie en transport nam de totale vervuiling toch toe.",
        antwoord: true,
        uitleg: "Waar! Schonere technologie verminderde de roetuitstoot per product, maar de sterk gegroeide productie en het transport zorgden er toch voor dat de totale vervuiling toenam."
      },
      {
        id: "h6_5_v4",
        niveau: 2,
        type: "mc",
        vraag: "Wat gebeurde er in 1986 bij de kerncentrale van Tsjernobyl?",
        opties: [
          "Een kernramp die een groot gebied onbewoonbaar maakte",
          "De centrale werd definitief gesloten wegens ouderdom",
          "Een succesvolle proefdraai zonder problemen",
          "De bouw van de centrale werd stopgezet"
        ],
        antwoord: 0,
        uitleg: "Door een ongeluk in de Sovjetkerncentrale van Tsjernobyl werd een groot gebied onbewoonbaar door kankerverwekkende radioactieve straling."
      },
      {
        id: "h6_5_v5",
        niveau: 2,
        type: "waaronwaar",
        vraag: "Greenpeace werd in 1971 opgericht in Nederland.",
        antwoord: false,
        uitleg: "Niet waar. Greenpeace werd in 1971 opgericht in Canada, niet in Nederland."
      },
      {
        id: "h6_5_v6",
        niveau: 2,
        type: "mc",
        vraag: "Wat veroorzaakte de gaswinning in Groningen op den duur?",
        opties: [
          "Doordat het gas niet meer geëxporteerd mocht worden",
          "Bodemdaling en honderden aardbevingen die huizen beschadigden",
          "Doordat de gasprijzen daalden tot nul",
          "Doordat het gas volledig op raakte in één jaar"
        ],
        antwoord: 1,
        uitleg: "De gaswinning veroorzaakte bodemdaling en honderden aardbevingen, waardoor de gaswinning vanaf 2014 werd beperkt."
      },
      {
        id: "h6_5_v7",
        niveau: 3,
        type: "invoer",
        vraag: "Welke voormalige Amerikaanse vicepresident maakte in 2006 met film en boek 'An Inconvenient Truth' de wereld bewust van de klimaatverandering?",
        antwoord: "Al Gore|Gore",
        uitleg: "Al Gore legde in zijn film en boek onder meer uit dat het smelten van het poolijs de zeewaterspiegel gevaarlijk kan doen stijgen."
      },
      {
        id: "h6_5_v8",
        niveau: 3,
        type: "mc",
        vraag: "Wat spraken bijna alle landen in 2015 op de VN-klimaatconferentie in Parijs af?",
        opties: [
          "Een verbod op alle kernenergie wereldwijd",
          "Het stopzetten van alle olie-export uit het Midden-Oosten",
          "Te streven naar een energietransitie van fossiele naar duurzame energie",
          "Een gezamenlijk Europees leger tegen klimaatverandering"
        ],
        antwoord: 2,
        uitleg: "Op de klimaatconferentie van Parijs spraken bijna alle landen af te streven naar een energietransitie: van fossiele brandstoffen naar duurzame energie zoals wind- en zonne-energie."
      }
    ]
  });
})();
