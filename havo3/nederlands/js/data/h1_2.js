/* Onderwerp conform DURU ENGINE_SPEC (HAVO 3 Nederlands · Cursus 1) */
DURU.register({
  id: "h1-2-argumenteren",
  hoofdstuk: 1,
  paragraaf: "1.2",
  titel: "Argumenteren — Typen & Blokjesschema's",
  korteUitleg: "Onderscheid feitelijke en waarderende argumenten en leer blokjesschema's opbouwen.",
  icoon: "⚖️",
  theorie: "\n<h3>1. Standpunt en Argumenten</h3>\n<p>In een overtuigende tekst wil de auteur de lezer overtuigen van zijn <b>standpunt</b> (mening of stelling). Dit standpunt wordt onderbouwd met <b>argumenten</b>: redenen waarom de schrijver deze mening heeft.</p>\n\n<div class=\"info-box tip\">\n<h4>Twee soorten argumenten</h4>\n<ul>\n  <li><b>Feitelijk argument (objectief):</b> dit argument kun je controleren; het is waar of niet waar. Er kan geen meningsverschil over het feit zelf bestaan.<br><i>Voorbeeld:</i> 'Die reclameschermen moeten weg, want ze leiden automobilisten af.' (te meten/controleren).</li>\n  <li><b>Waarderend argument (subjectief):</b> dit argument berust op een mening, smaak, norm of waarde. Je kunt erover van mening verschillen.<br><i>Voorbeeld:</i> 'Die reclameschermen moeten weg, want ze verpesten het landschap.' (kwestie van smaak).</li>\n</ul>\n</div>\n\n<h3>2. Signaalwoorden</h3>\n<p>Een standpunt wordt vaak aangekondigd met: <i>ik vind, volgens mij, wij denken dat, de auteur is van mening dat, kortom, dus, daarom, we zouden moeten, er moet</i>.</p>\n<p>Argumenten herken je aan signaalwoorden als: <i>want, omdat, immers, namelijk, de reden hiervoor is, dat blijkt uit</i>.</p>\n\n<h3>3. Argumentatiestructuren</h3>\n<p>Het geheel van standpunt en argumenten vormt de <b>argumentatiestructuur</b>:</p>\n<ol>\n  <li><b>Enkelvoudige argumentatie:</b> 1 standpunt onderbouwd met 1 argument.</li>\n  <li><b>Nevenschikkende argumentatie:</b> 2 of meer gelijkwaardige argumenten ondersteunen samen direct het standpunt. Tussen de blokjes kun je in gedachten <i>'en'</i> invullen.</li>\n  <li><b>Onderschikkende argumentatie:</b> een argument wordt zelf weer onderbouwd door een <b>subargument</b> (een keten van argumenten: standpunt → argument → subargument).</li>\n  <li><b>Samengestelde argumentatie:</b> een combinatie van nevenschikking en onderschikking.</li>\n</ol>\n\n<div class=\"formule-box\">\n<h4>Het Blokjesschema</h4>\n<p>Een argumentatie kun je weergeven in een blokjesschema:</p>\n<ul>\n  <li>Het <b>standpunt</b> staat altijd in het bovenste blokje.</li>\n  <li>De argumenten staan in de blokjes daaronder.</li>\n  <li>Subargumenten staan onder het specifieke argument dat zij ondersteunen.</li>\n  <li>Pijlen naar beneden lees je als het woord <b>'want'</b>.</li>\n  <li>Gelijkwaardige argumenten vul je in van <b>links naar rechts</b>.</li>\n</ul>\n</div>\n",
  vragen: [
    {
      type: "mc",
      niveau: 1,
      vraag: "Wat is het fundamentele kenmerk van een <b>feitelijk argument</b>?",
      opties: [
        "Het berust altijd op een persoonlijke emotie of smaak",
        "Het is controleerbaar: het is waar of niet waar",
        "Het kan nooit in cijfers worden uitgedrukt",
        "Het staat altijd in de vragende vorm"
      ],
      antwoord: 1,
      uitleg: "Feitelijke argumenten zijn controleerbaar op basis van feiten, metingen of waarnemingen."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Lees: <i>'We moeten meer fietsen, want fietsen in de frisse ochtendlucht is heerlijk ontspannend.'</i> Wat voor argument is dit?",
      opties: [
        "Een statistisch gegeven",
        "Een feitelijk argument",
        "Een onderschikkend bewijs",
        "Een waarderend argument"
      ],
      antwoord: 3,
      uitleg: "Of iets 'heerlijk ontspannend' is, betreft een persoonlijke beleving en smaak: een waarderend argument."
    },
    {
      type: "waaronwaar",
      niveau: 1,
      vraag: "Signaalwoorden als 'want', 'omdat' en 'immers' kondigen in de regel een argument aan.",
      antwoord: true,
      uitleg: "Waar. Deze voegwoorden en bijwoorden leiden een reden of onderbouwing in."
    },
    {
      type: "invoer",
      niveau: 1,
      vraag: "Hoe heet het argument dat een ander argument ondersteunt binnen een onderschikkende argumentatie?",
      antwoord: "subargument|een subargument",
      uitleg: "Een subargument ondersteunt een hoofdargument."
    },
    {
      type: "mc",
      niveau: 2,
      vraag: "Welke omschrijving geeft het beste weer hoe <b>nevenschikking</b> in een betoog werkt?",
      opties: [
        "Het standpunt wordt nergens expliciet genoemd",
        "Er is slechts één enkel argument zonder enige toelichting",
        "Twee of meer gelijkwaardige argumenten dragen samen direct het standpunt",
        "Elk argument weerlegt het voorgaande argument"
      ],
      antwoord: 2,
      uitleg: "Nevenschikkende argumenten staan op hetzelfde niveau en ondersteunen samen ('en') de stelling."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een blokjesschema kun je de pijlen die van boven naar beneden lopen, in gedachten lezen als 'echter'.",
      antwoord: false,
      uitleg: "Onwaar. De theorie leert dat je de pijlen van boven naar beneden leest als 'want'."
    },
    {
      type: "waaronwaar",
      niveau: 2,
      vraag: "In een standaard blokjesschema wordt het standpunt in het bovenste blokje geplaatst.",
      antwoord: true,
      uitleg: "Waar. Het standpunt staat altijd bovenaan en de argumenten staan eronder."
    },
    {
      type: "invoer",
      niveau: 2,
      vraag: "Hoe noem je een argumentatie met slechts één standpunt en één argument?",
      antwoord: "enkelvoudige argumentatie|enkelvoudig",
      uitleg: "Enkelvoudige argumentatie bestaat uit exact één standpunt en één argument."
    }
  ]
});
