/* =========================================================
   Duru's Geschiedenis Academie — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Volgorde + groepering van de hoofdstukken (Tijdvak 9: Tijd van de wereldoorlogen)
  DURU.hoofdstukken = [
    { nr: 4, titel: "De wereldoorlogen", icoon: "🕰️", kleur: "h4-thema",
      intro: "De Eerste en Tweede Wereldoorlog, het interbellum en Nederland tijdens de bezetting. Oefen theorie en proeftoetsen voor geschiedenis MAVO 2." }
  ];

  // Onderwerpen worden hier verzameld (in registratie-volgorde)
  DURU.onderwerpen = [];
  DURU._byId = {};

  /**
   * Registreer een onderwerp.
   * Verwacht object: { id, hoofdstuk, paragraaf, titel, korteUitleg, icoon, kleur, theorie, vragen:[...] }
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

