/* =========================================================
   Duru's Engels (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   Smoke-test-site: nog geen onderwerpen (oefenquizzes), alleen een proeftoets.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Nog geen hoofdstukken/onderwerpen — die komen zodra Duru materiaal aanlevert.
  DURU.hoofdstukken = [];
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
