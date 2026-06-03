/* =========================================================
   Duru's Schoolhub — Landing Page Logic
   Bevat: vakken-data, kaart-rendering, uitklap-logica
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

// ── Hulpfuncties ──────────────────────────────────────────

/**
 * Maakt een directe-link kaart (Natuurkunde / Economie).
 * @param {Object} vak
 * @returns {HTMLElement}
 */
function maakDirecteKaart(vak) {
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
    klapBinnen.appendChild(link);
  });

  klap.appendChild(klapBinnen);
  wrapper.appendChild(header);
  wrapper.appendChild(klap);

  // ── Toggle-logica ──────────────────────────────────────
  function toggle(e) {
    // Klik op een sub-link: niet de kaart zelf togglen
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
});
