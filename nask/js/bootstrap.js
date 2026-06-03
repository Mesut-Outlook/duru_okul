/* =========================================================
   Duru's NASK Academie — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Volgorde + groepering van de hoofdstukken
  DURU.hoofdstukken = [
    {
      nr: 4,
      titel: "Snelheid",
      icoon: "🏎️",
      kleur: "h4-thema",
      intro: "Hoe snel ga je? Hoe lang doe je over een afstand? Alles over snelheid, m/s, km/h, reactieafstand en grafieken.",
    },
    {
      nr: 6,
      titel: "Elektriciteit",
      icoon: "⚡",
      kleur: "h6-thema",
      intro: "Spanning, stroom, schakelingen: leer alles over elektriciteit, de voltmeter, de ampèremeter en serie- & parallelschakelingen.",
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
