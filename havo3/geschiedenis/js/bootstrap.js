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
      intro: "Welvaart en crisis in de Verenigde Staten, fascisme en communisme, Duitsland van democratie naar dictatuur, Nederland in het interbellum, en Europa, Azië en Afrika.",
      kleur: "blauw"
    },
    {
      nr: 3,
      titel: "De Tweede Wereldoorlog (1939–1945)",
      icoon: "✈️",
      intro: "Oorlog in Europa, oorlog buiten Europa, bezet Nederland, de Holocaust en de lessen van de oorlog.",
      kleur: "rood"
    },
    {
      nr: 4,
      titel: "De wereld na 1945 (1945–1990)",
      icoon: "🕊️",
      intro: "Het einde van de wereldrijken, de Koude Oorlog, de VS vanaf de Tweede Wereldoorlog, samenwerking en democratie, en welvaart en armoede.",
      kleur: "paars"
    },
    {
      nr: 5,
      titel: "Nederland na 1945 (1945–heden)",
      icoon: "🇳🇱",
      intro: "Er komen andere tijden, besluiten en besturen, postindustrieel Nederland, veelkleurig Nederland en recht in Nederland.",
      kleur: "groen"
    },
    {
      nr: 6,
      titel: "Naar de wereld van nu (1990–heden)",
      icoon: "🌐",
      intro: "Het Midden-Oosten en Noord-Afrika, eenheid en verdeeldheid in Europa, de wereld na de Koude Oorlog, digitalisering en globalisering, en mens en milieu.",
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
