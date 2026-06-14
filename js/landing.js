/* =========================================================
   Duru's Schoolhub — Landing Page Logic
   Bevat: vakken-data, kaart-rendering, uitklap-logica,
          iframe-shell (terugbalk + history-integratie)
   ========================================================= */

// ── Vakken-data ───────────────────────────────────────────
// Elk vak heeft: id, titel, icoon, kleur (CSS-variabele-naam),
// beschrijving en ofwel een href (directe link) ofwel een
// onderwerpen-array (uitklapbare categorie).
var VAKKEN = [
  {
    id: 'natuurkunde',
    titel: 'Natuurkunde (NASK)',
    icoon: '⚛️',
    kleur: 'blauw',          // indigo/blauw accent
    beschrijving: 'Snelheid, elektriciteit en meer — oefen theorie en sommen.',
    href: './nask/'
  },
  {
    id: 'wiskunde',
    titel: 'Wiskunde',
    icoon: '⚖️',
    kleur: 'teal',           // teal/turquoise accent
    beschrijving: 'Hoofdstuk 8 — Vergelijkingen: termen, de balans en het snijpunt.',
    href: './wiskunde/'
  },
  {
    id: 'economie',
    titel: 'Economie',
    icoon: '💶',
    kleur: 'groen',          // groen/goud accent (past bij de Economie-site)
    beschrijving: 'De overheid, belasting en de schatkist — alles over economie.',
    href: './economi/'
  },
  {
    id: 'nederlands',
    titel: 'Nederlands',
    icoon: '📖',
    kleur: 'oranje',         // warm oranje/rood accent
    beschrijving: 'Taal en leesvaardigheid — klik om de onderwerpen te zien.',
    // Geen href: dit is een uitklapbare categorie
    onderwerpen: [
      {
        titel: 'Begrijpend Lezen',
        icoon: '🧠',
        beschrijving: 'Teksten analyseren en vragen beantwoorden met Meester Max.',
        href: './nederlands/begrijpend-lezen/'
      }
      // Voeg hier straks meer onderwerpen toe, bv. spelling, grammatica …
    ]
  }
];

// ── Iframe-shell staat ────────────────────────────────────
// Bijhouden of we de iframe-modus zelf hebben geopend (om
// popstate van externe navigatie te onderscheiden).
var _iframeActief = false;

// ── Iframe openen ─────────────────────────────────────────
/**
 * Opent een vak in de iframe-shell.
 * @param {string} href  - Relatief pad naar de sub-site, bv. './nask/'
 * @param {string} icoon - Emoji icoon van het vak/onderwerp
 * @param {string} titel - Naam van het vak/onderwerp
 */
function openInIframe(href, icoon, titel) {
  var shell  = document.getElementById('iframe-shell');
  var frame  = document.getElementById('vak-frame');
  var label  = document.getElementById('terugbalk-vak');

  if (!shell || !frame || !label) return;

  // Label instellen
  label.textContent = icoon + ' ' + titel;  // nbsp voor iets ruimte

  // Iframe src pas nu zetten (lazy load)
  frame.src = href;

  // Grid verbergen, shell tonen
  document.body.classList.add('iframe-actief');
  shell.setAttribute('aria-hidden', 'false');

  // History: nieuwe state zodat Back werkt
  if (!_iframeActief) {
    history.pushState({ vakIframe: true, href: href, icoon: icoon, titel: titel }, '', '');
  }
  _iframeActief = true;

  // Focus naar terugknop voor toegankelijkheid
  var knop = document.getElementById('terug-knop');
  if (knop) knop.focus();
}

// ── Terugkeren naar het grid ──────────────────────────────
/**
 * Sluit de iframe-shell en toont het vakken-grid weer.
 * @param {boolean} [viaPop] - true als aangeroepen vanuit popstate handler
 */
function sluitIframe(viaPop) {
  var shell = document.getElementById('iframe-shell');
  var frame = document.getElementById('vak-frame');

  if (!shell || !frame) return;

  // Iframe stoppen (about:blank zodat sub-site niet op achtergrond draait
  // én de iframe niet per ongeluk de hub-pagina zelf herlaadt)
  frame.src = 'about:blank';

  // Shell verbergen, grid tonen
  document.body.classList.remove('iframe-actief');
  shell.setAttribute('aria-hidden', 'true');

  _iframeActief = false;

  // Als we NIET via popstate terugkeren, moeten we zelf Back simuleren
  // zodat de pushState-entry uit de history-stack verdwijnt.
  if (!viaPop) {
    history.back();
  }
}

// ── Hulpfuncties ──────────────────────────────────────────

/**
 * Maakt een directe-link kaart (Natuurkunde / Economie / Wiskunde).
 * De kaart is nu een <button>-achtige <div> die het iframe opent
 * in plaats van een volledige paginanavigatie.
 * @param {Object} vak
 * @returns {HTMLElement}
 */
function maakDirecteKaart(vak) {
  // Gebruik een <a> voor SEO en toegankelijkheid, maar onderschep de klik
  var kaart = document.createElement('a');
  kaart.href = vak.href;
  kaart.className = 'vak-kaart vak-kaart--direct vak-kaart--' + vak.kleur;
  kaart.setAttribute('aria-label', vak.titel + ' openen');

  kaart.innerHTML =
    '<div class="vak-kaart__top">' +
      '<span class="vak-kaart__icoon">' + vak.icoon + '</span>' +
      '<span class="vak-kaart__badge vak-badge--' + vak.kleur + '">Open →</span>' +
    '</div>' +
    '<h2 class="vak-kaart__titel">' + vak.titel + '</h2>' +
    '<p class="vak-kaart__beschrijving">' + vak.beschrijving + '</p>';

  // Klik onderscheppen: open in iframe in plaats van navigeren
  kaart.addEventListener('click', function(e) {
    e.preventDefault();
    openInIframe(vak.href, vak.icoon, vak.titel);
  });

  return kaart;
}

/**
 * Maakt een uitklapbare categorie-kaart (Nederlands).
 * @param {Object} vak
 * @returns {HTMLElement}
 */
function maakCategorieKaart(vak) {
  var wrapper = document.createElement('div');
  wrapper.className = 'vak-kaart vak-kaart--categorie vak-kaart--' + vak.kleur;
  wrapper.setAttribute('role', 'button');
  wrapper.setAttribute('tabindex', '0');
  wrapper.setAttribute('aria-expanded', 'false');
  wrapper.setAttribute('aria-label', vak.titel + ' uitklappen');

  // Header (altijd zichtbaar)
  var header = document.createElement('div');
  header.className = 'vak-kaart__header';
  header.innerHTML =
    '<div class="vak-kaart__top">' +
      '<span class="vak-kaart__icoon">' + vak.icoon + '</span>' +
      '<span class="vak-kaart__pijl vak-badge--' + vak.kleur + '" aria-hidden="true">▾</span>' +
    '</div>' +
    '<h2 class="vak-kaart__titel">' + vak.titel + '</h2>' +
    '<p class="vak-kaart__beschrijving">' + vak.beschrijving + '</p>';

  // Uitklapgebied
  var klap = document.createElement('div');
  klap.className = 'vak-kaart__klap';
  klap.setAttribute('aria-hidden', 'true');

  var klapBinnen = document.createElement('div');
  klapBinnen.className = 'vak-kaart__klap-binnen';

  var klapTitel = document.createElement('p');
  klapTitel.className = 'vak-kaart__klap-kop';
  klapTitel.textContent = 'Kies een onderwerp:';
  klapBinnen.appendChild(klapTitel);

  // Render elk onderwerp als een sub-link
  vak.onderwerpen.forEach(function(ow) {
    var link = document.createElement('a');
    link.href = ow.href;
    link.className = 'onderwerp-link onderwerp-link--' + vak.kleur;
    link.innerHTML =
      '<span class="onderwerp-link__icoon">' + ow.icoon + '</span>' +
      '<span class="onderwerp-link__tekst">' +
        '<strong>' + ow.titel + '</strong>' +
        '<span>' + ow.beschrijving + '</span>' +
      '</span>' +
      '<span class="onderwerp-link__pijl">→</span>';

    // Klik onderscheppen: open onderwerp in iframe
    link.addEventListener('click', function(e) {
      e.preventDefault();
      openInIframe(ow.href, ow.icoon, ow.titel);
    });

    klapBinnen.appendChild(link);
  });

  klap.appendChild(klapBinnen);
  wrapper.appendChild(header);
  wrapper.appendChild(klap);

  // ── Toggle-logica ──────────────────────────────────────
  function toggle(e) {
    // Klik op een sub-link: niet de kaart zelf togglen
    // (de sub-link heeft zijn eigen click-handler die het iframe opent)
    if (e && e.target && e.target.closest('.onderwerp-link')) return;

    var open = wrapper.getAttribute('aria-expanded') === 'true';
    wrapper.setAttribute('aria-expanded', open ? 'false' : 'true');
    klap.setAttribute('aria-hidden', open ? 'true' : 'false');

    var pijl = header.querySelector('.vak-kaart__pijl');
    if (pijl) pijl.textContent = open ? '▾' : '▴';

    // Animatie: max-height truc voor smooth uitklap
    if (!open) {
      klap.style.maxHeight = klapBinnen.scrollHeight + 'px';
    } else {
      klap.style.maxHeight = '0';
    }
  }

  wrapper.addEventListener('click', toggle);
  wrapper.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      toggle(e);
    }
  });

  return wrapper;
}

/**
 * Rendert alle vakken in het #vakken-grid element.
 */
function renderVakken() {
  var grid = document.getElementById('vakken-grid');
  if (!grid) return;

  VAKKEN.forEach(function(vak) {
    var kaart;
    if (vak.onderwerpen && vak.onderwerpen.length > 0) {
      kaart = maakCategorieKaart(vak);
    } else {
      kaart = maakDirecteKaart(vak);
    }
    grid.appendChild(kaart);
  });
}

// ── Init bij DOM-gereed ───────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {

  renderVakken();

  // Intercept local storage writes inside the iframe to sync them back to the server
  var frame = document.getElementById('vak-frame');
  if (frame) {
    frame.addEventListener('load', function() {
      try {
        var win = frame.contentWindow;
        if (!win) return;
        
        // Save references to original function
        var originalSetItem = win.localStorage.setItem;
        
        win.localStorage.setItem = function(key, value) {
          // Call original
          originalSetItem.apply(this, arguments);
          
          // Only send if it's one of Duru's school progress items
          if (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0) {
            var parsedVal = null;
            try {
              parsedVal = JSON.parse(value);
            } catch (e) {
              parsedVal = value;
            }
            
            fetch('/api/score', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                key: key,
                val: parsedVal,
                timestamp: new Date().toISOString()
              })
            }).catch(function(err) {
              console.warn('Could not sync performance score with local server:', err);
            });
          }
        };
      } catch (e) {
        console.warn('Iframe storage interception bypassed or same-origin security blocked:', e);
      }
    });
  }

  // ── Terugknop ─────────────────────────────────────────
  var terugKnop = document.getElementById('terug-knop');
  if (terugKnop) {
    terugKnop.addEventListener('click', function() {
      sluitIframe(false);
    });
  }

  // ── Escape-toets sluit het iframe ─────────────────────
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && _iframeActief) {
      sluitIframe(false);
    }
  });

  // ── Browser Back-knop (popstate) ──────────────────────
  // Als de gebruiker op Terug klikt en de state bevat vakIframe,
  // sluiten we de iframe-shell in plaats van de pagina te verlaten.
  window.addEventListener('popstate', function(e) {
    if (_iframeActief) {
      // We zijn in iframe-modus: terug = grid tonen
      sluitIframe(true);
    }
  });

  // ── Begintoestand: als de pagina wordt geladen zonder state,
  //    zorg dat er een "baseline" history-entry bestaat zodat
  //    pushState later altijd een stap terug kan zetten.
  if (!history.state || !history.state.vakIframe) {
    history.replaceState({ vakIframe: false }, '', '');
  }
});
