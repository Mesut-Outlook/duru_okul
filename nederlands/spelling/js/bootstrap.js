/* =========================================================
   Duru's Spelling Academie — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Volgorde + groepering van de hoofdstukken
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "Werkwoordspelling",
      icoon: "✍️",
      kleur: "spelling-thema",
      intro: "Stam, stam+t, 't kofschip, sterke en zwakke werkwoorden: oefen de regels van de tegenwoordige tijd, verleden tijd en het voltooid deelwoord.",
    },
    {
      nr: 2,
      titel: "Grammatica & Zinsontleding",
      icoon: "📖",
      kleur: "grammatica-thema",
      intro: "Zinsdelen ontleden (Pv, Ow, Wg, Lv, Mv) en het juiste gebruik van voegwoorden en interpunctie volgens jouw aantekeningen.",
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
