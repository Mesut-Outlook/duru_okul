/* =========================================================
   Duru's Wiskunde Academie — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Volgorde + groepering van de hoofdstukken
  DURU.hoofdstukken = [
    {
      nr: 8,
      titel: "Vergelijkingen",
      icoon: "⚖️",
      kleur: "h8-thema",
      intro: "Gelijksoortige termen, de balans-methode, vergelijkingen oplossen en het snijpunt van twee lijnen: alles over vergelijkingen op MAVO 2.",
    },
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
