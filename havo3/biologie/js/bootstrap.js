/* =========================================================
   Duru's Biologie (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht Nectar Biologie HAVO 3
  DURU.hoofdstukken = [
    {
      nr: 10,
      titel: "Je verandert",
      icoon: "🧬",
      kleur: "h10-thema",
      intro: "Levensfasen, lichamelijke en geestelijke ontwikkeling, groeispurt, hypofyse en hormoonwerking (groeihormoon, testosteron, oestrogeen), botgroei in groeischijven, primaire, secundaire en tertiaire geslachtskenmerken, puberteit, acne, zweetklieren en transgender & genderdysforie."
    }
  ];

  DURU.onderwerpen = [];
  DURU._byId = {};

  /**
   * Registreer een onderwerp (paragraaf met theorie en oefenquiz).
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
