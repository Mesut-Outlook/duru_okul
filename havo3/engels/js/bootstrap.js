/* =========================================================
   Duru's Engels (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht (Stepping Stones 3 HAVO)
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "The world around you",
      icoon: "🌍",
      kleur: "h1-thema",
      intro: "Culture, identity, customs and traditions, stereotypes, hospitality, Present Simple vs. Present Continuous, social interactions and penpal correspondence."
    },
    {
      nr: 2,
      titel: "Crime",
      icoon: "🔍",
      kleur: "h2-thema",
      intro: "Crime types (burglary, theft, robbery, cybercrime), justice and court trials, Past Simple vs. Past Continuous, reporting incidents, physical suspect descriptions and mystery analysis."
    },
    {
      nr: 3,
      titel: "Science & technology",
      icoon: "🔬",
      kleur: "h3-thema",
      intro: "Scientific discoveries vs. inventions, AI and robotics, Present Perfect vs. Past Simple (for/since, already/yet), explaining tech gadgets and reviewing devices."
    },
    {
      nr: 4,
      titel: "To the extreme",
      icoon: "⚡",
      kleur: "h4-thema",
      intro: "Extreme sports, outdoor survival, endurance, Comparatives & Superlatives, Modals of obligation and prohibition (must, should, have to), urgent safety warnings and adventure narratives."
    },
    {
      nr: 5,
      titel: "Going green",
      icoon: "🌱",
      kleur: "h5-thema",
      intro: "Environment and sustainability, carbon footprint, renewable energy, Future forms (will, be going to, Present Continuous), First Conditional, green proposals and climate debates."
    },
    {
      nr: 6,
      titel: "Your future",
      icoon: "💼",
      kleur: "h6-thema",
      intro: "Careers, workplace skills, job vacancies, Passive Voice (Present & Past Simple), Second Conditional, formal application letters (CV) and professional interview etiquette."
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
