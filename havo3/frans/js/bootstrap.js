/* =========================================================
   Duru's Frans (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   Smoke-test-site: nog geen onderwerpen (oefenquizzes), alleen een proeftoets.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  DURU.hoofdstukken = [
    { nr: 1, titel: "Poste, like, partage", icoon: "📱", kleur: "blauw", intro: "Sociale media, communicatie, vriendschap, basis grammatica en werkwoorden op -er." },
    { nr: 2, titel: "Du temps pour moi", icoon: "🎸", kleur: "oranje", intro: "Vrije tijd, hobby's, sport, muziek, futur composé en werkwoorden faire/aller/prendre." },
    { nr: 3, titel: "En route!", icoon: "🚆", kleur: "groen", intro: "Reizen, vakantie, vervoer, de weg vragen en passé composé met avoir." },
    { nr: 4, titel: "Le pont", icoon: "🗼", kleur: "paars", intro: "Cultuur van Frankrijk, monumenten in Parijs, Francofonie en tussenbalans." },
    { nr: 5, titel: "Au resto!", icoon: "🍽️", kleur: "roze", intro: "Eten & drinken, restaurant, menukaarten en het delend lidwoord (du, de la, des)." },
    { nr: 6, titel: "C'est moi", icoon: "👗", kleur: "geel", intro: "Uiterlijk, kleding, mode, karakter en bijvoeglijk naamwoorden." },
    { nr: 7, titel: "À tout prix!", icoon: "💶", kleur: "blauw", intro: "Geld, zakgeld, sparen, bijbaantjes en trappen van vergelijking." },
    { nr: 8, titel: "Le pont (Examentraining)", icoon: "🎓", kleur: "groen", intro: "Eindbalans, passé composé met être, Cito-signaalwoorden en eindexamen." }
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
