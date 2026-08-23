/* =========================================================
   Duru's Geschiedenis (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  "use strict";
  window.DURU = window.DURU || {};

  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "De Eerste Wereldoorlog (1900–1920)",
      icoon: "🪖",
      intro: "De beleving van tijd, de Grote Oorlog, de Russische Revolutie, de nieuwe kaart van Europa en Neutraal Nederland.",
      kleur: "oranje"
    },
    {
      nr: 2,
      titel: "Tussen de oorlogen (1919–1939)",
      icoon: "📻",
      intro: "De roerige jaren 20, het fascisme in Italië, het nationaalsocialisme in Duitsland, Stalin en de crisis in Nederland.",
      kleur: "blauw"
    },
    {
      nr: 3,
      titel: "De Tweede Wereldoorlog (1939–1945)",
      icoon: "✈️",
      intro: "Het uitbreken van de oorlog, bezet Nederland, de Jodenvervolging en Holocaust, keerpunten en de oorlog in Azië.",
      kleur: "rood"
    },
    {
      nr: 4,
      titel: "De wereld na 1945 (1945–1990)",
      icoon: "🕊️",
      intro: "De Koude Oorlog, spanningen en crises, de Vietnamoorlog, het einde van de Koude Oorlog en de dekolonisatie.",
      kleur: "paars"
    },
    {
      nr: 5,
      titel: "Nederland na 1945 (1945–heden)",
      icoon: "🇳🇱",
      intro: "Wederopbouw en verzorgingsstaat, Europese samenwerking, ontzuiling en veranderende cultuur, en de pluriforme samenleving.",
      kleur: "groen"
    },
    {
      nr: 6,
      titel: "Naar de wereld van nu (1990–heden)",
      icoon: "🌐",
      intro: "Een nieuwe wereldorde, conflicten in het Midden-Oosten, terrorisme en veiligheid, globalisering en klimaat.",
      kleur: "teal"
    }
  ];

  DURU.onderwerpen = [];
  DURU._byId = {};

  /**
   * Registreer een onderwerp.
   * Verwacht: { id, hoofdstuk, paragraaf, titel, korteUitleg, icoon, kleur, theorie, vragen:[...] }
   */
  DURU.register = function (onderwerp) {
    if (!onderwerp || !onderwerp.id) {
      console.warn("DURU.register: onderwerp zonder id genegeerd", onderwerp);
      return;
    }
    onderwerp.vragen = onderwerp.vragen || [];
    DURU.onderwerpen.push(onderwerp);
    DURU._byId[onderwerp.id] = onderwerp;
  };

  DURU.getOnderwerp = function (id) { return DURU._byId[id]; };
  DURU.onderwerpenVan = function (nr) {
    return DURU.onderwerpen.filter(function (o) { return o.hoofdstuk === nr; });
  };
})();

// Storage delegation to parent window (if running in iframe) to prevent early storage read issues
if (window.parent && window.parent !== window && window.parent.localStorage) {
  Storage.prototype.getItem = function(key) {
    return window.parent.localStorage.getItem(key);
  };
  Storage.prototype.setItem = function(key, value) {
    window.parent.localStorage.setItem(key, value);
  };
  Storage.prototype.removeItem = function(key) {
    window.parent.localStorage.removeItem(key);
  };
}
