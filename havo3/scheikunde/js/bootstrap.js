/* =========================================================
   Duru's Scheikunde (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   Smoke-test-site: nog geen onderwerpen (oefenquizzes), alleen een proeftoets.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "Scheikunde is overal",
      icoon: "🧪",
      kleur: "h1-thema",
      intro: "Stofeigenschappen, zuivere stoffen versus mengsels, dichtheid berekenen, de drie fasen (s, l, g), de zes faseveranderingen en temperatuurschalen (°C en Kelvin).",
    },
    {
      nr: 2,
      titel: "Bouwstenen van stoffen",
      icoon: "⚛️",
      kleur: "h2-thema",
      intro: "Macro- en microniveau, fasen, het periodiek systeem der elementen, metalen en niet-metalen, chemische formuletaal en atoombouw met protonen, neutronen en elektronen.",
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
