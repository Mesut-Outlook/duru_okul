/* =========================================================
   Duru's Duits (HAVO 3) — Bootstrap
   Maakt het globale DURU-object klaar VOORDAT de databestanden laden.
   Elk databestand roept DURU.register({...}) / DURU.registerExamen({...}) aan.
   ========================================================= */
(function () {
  window.DURU = window.DURU || {};

  // Hoofdstukken overzicht (Neue Kontakte 3 HAVO)
  DURU.hoofdstukken = [
    {
      nr: 1,
      titel: "Umgebung & Wetter",
      icoon: "🌲",
      kleur: "blauw",
      intro: "Natuur, het weer, seizoenen, maanden, temperatuur, verleden tijd van sein en haben, en het werkwoord werden."
    },
    {
      nr: 2,
      titel: "Gesundheit & Körper",
      icoon: "🩺",
      kleur: "oranje",
      intro: "Lichaamsdelen, klachten, bij de dokter en apotheek, en persoonlijke voornaamwoorden in de 1e, 3e en 4e naamval."
    },
    {
      nr: 3,
      titel: "Unterwegs & Reisen",
      icoon: "🚆",
      kleur: "groen",
      intro: "Vervoermiddelen, het station, wegwijzen in de stad, en modale hulpwerkwoorden in de verleden tijd (Präteritum)."
    },
    {
      nr: 4,
      titel: "Veranstaltungen & Feiern",
      icoon: "🎪",
      kleur: "paars",
      intro: "Evenementen, feesten, uitnodigen, afspraken maken, de der-Gruppe en ein-Gruppe in de 1e en 4e naamval."
    },
    {
      nr: 5,
      titel: "Zukunft & Berufe",
      icoon: "💼",
      kleur: "roze",
      intro: "Beroepen, opleidingen, solliciteren, toekomstplannen, en sterke werkwoorden met klinkerwisseling (a→ä en e→i/ie)."
    },
    {
      nr: 6,
      titel: "In Aktion & Hilfsbereitschaft",
      icoon: "🚑",
      kleur: "geel",
      intro: "Hulpdiensten (brandweer, politie, THW), noodgevallen, vrijwilligerswerk, en het complete 4-naamvallensysteem."
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
