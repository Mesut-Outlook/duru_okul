/* =========================================================
   Duru's Economie (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht (Pincode HAVO 3)
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "Jouw financiën",
      icoon: "🛒",
      kleur: "oranje",
      intro: "Behoeften en schaarste, inkomensvormen (arbeid, bezit, overdracht), soorten uitgaven (vaste lasten, huishoudelijk, incidenteel) en budgetteren met het NIBUD."
    },
    {
      nr: 2,
      titel: "De rol van geld",
      icoon: "🪙",
      kleur: "blauw",
      intro: "Van directe ruil naar indirecte ruil, chartaal en giraal geld, functies van geld (ruil-, reken- en oppotmiddel), koopkracht en inflatie (CPI/CBS)."
    },
    {
      nr: 3,
      titel: "Omgaan met geld",
      icoon: "🐖",
      kleur: "groen",
      intro: "Sparen en spaarmotieven, enkelvoudige en samengestelde rente, lenen en kredietvormen, BKR-registratie en verzekeringen (solidariteit en eigen risico)."
    },
    {
      nr: 4,
      titel: "Produceren",
      icoon: "🏭",
      kleur: "roze",
      intro: "Productiefactoren (KANO), toegevoegde waarde, het BBP, constante en variabele kosten, schaalvoordelen, omzet, brutowinst, nettowinst en btw."
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
