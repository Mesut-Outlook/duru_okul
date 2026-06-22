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
    id: 'geschiedenis',
    titel: 'Geschiedenis',
    icoon: '🕰️',
    kleur: 'oranje',         // warm oranje/historisch accent
    beschrijving: 'De Eerste en Tweede Wereldoorlog, het interbellum en Nederland in de oorlog.',
    href: './geschiedenis/'
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
      },
      {
        titel: 'Spelling & Grammatica',
        icoon: '✍️',
        beschrijving: 'Werkwoordspelling, voegwoorden, interpunctie en zinsdelen ontleden.',
        href: './nederlands/spelling/'
      }
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

  var isGitHubPages = window.location.hostname.indexOf('github.io') !== -1;

  function restoreScores(data) {
    if (!Array.isArray(data)) return 0;
    var allKeys = {};
    data.forEach(function(item) {
      if (item && item.key) {
        allKeys[item.key] = true;
      }
    });
    
    var restoredCount = 0;
    
    Object.keys(allKeys).forEach(function(key) {
      var newVal = null;
      
      if (key === 'begrijpend_lezen_history') {
        var uniqueAttemptsBL = {};
        data.forEach(function(item) {
          if (item && item.key === key && Array.isArray(item.val)) {
            item.val.forEach(function(att) {
              var uniqId = att.timestamp || (att.startingText + '_' + att.grade + '_' + att.score);
              uniqueAttemptsBL[uniqId] = att;
            });
          }
        });
        var mergedBL = Object.keys(uniqueAttemptsBL).map(function(k) { return uniqueAttemptsBL[k]; });
        mergedBL.sort(function(a, b) {
          return new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime();
        });
        newVal = mergedBL;
      } 
      else if (key.indexOf('_examens_v1') !== -1) {
        var uniqueAttempts = {};
        data.forEach(function(item) {
          if (item && item.key === key && item.val && Array.isArray(item.val.history)) {
            item.val.history.forEach(function(att) {
              var uniqId = att.attemptId || (att.examId + '_' + att.datum + '_' + att.pct);
              uniqueAttempts[uniqId] = att;
            });
          }
        });
        var mergedHistory = Object.keys(uniqueAttempts).map(function(k) { return uniqueAttempts[k]; });
        mergedHistory.sort(function(a, b) {
          return parseAttemptDate(b) - parseAttemptDate(a);
        });
        
        var beste = {};
        var laatste = {};
        mergedHistory.forEach(function(att) {
          if (att.examId) {
            if (laatste[att.examId] === undefined) {
              laatste[att.examId] = att.pct;
            }
            if (beste[att.examId] === undefined || att.pct > beste[att.examId]) {
              beste[att.examId] = att.pct;
            }
          }
        });
        
        newVal = {
          beste: beste,
          laatste: laatste,
          history: mergedHistory
        };
      } 
      else if (key.indexOf('_v1') !== -1) {
        var xp = 0;
        var maxStreak = 0;
        var badges = {};
        var besteTopic = {};
        var gedaan = {};
        var pogingen = {};
        var titels = {};
        
        data.forEach(function(item) {
          if (item && item.key === key && item.val) {
            var val = item.val;
            if (val.xp && val.xp > xp) xp = val.xp;
            if (val.streak && val.streak > maxStreak) maxStreak = val.streak;
            if (val.maxStreak && val.maxStreak > maxStreak) maxStreak = val.maxStreak;
            if (val.badges) {
              Object.keys(val.badges).forEach(function(bid) {
                badges[bid] = val.badges[bid];
              });
            }
            if (val.beste) {
              Object.keys(val.beste).forEach(function(tid) {
                if (besteTopic[tid] === undefined || val.beste[tid] > besteTopic[tid]) {
                  besteTopic[tid] = val.beste[tid];
                }
              });
            }
            if (val.gedaan) {
              Object.keys(val.gedaan).forEach(function(tid) {
                gedaan[tid] = val.gedaan[tid];
              });
            }
            if (val.pogingen) {
              Object.keys(val.pogingen).forEach(function(tid) {
                if (pogingen[tid] === undefined || val.pogingen[tid] > pogingen[tid]) {
                  pogingen[tid] = val.pogingen[tid];
                }
              });
            }
            if (val.titels) {
              Object.keys(val.titels).forEach(function(tid) {
                titels[tid] = val.titels[tid];
              });
            }
          }
        });
        
        newVal = {
          xp: xp,
          streak: maxStreak,
          badges: badges,
          beste: besteTopic,
          gedaan: gedaan,
          pogingen: pogingen,
          titels: titels
        };
      }
      
      if (newVal) {
        var localVal = localStorage.getItem(key);
        var newValStr = JSON.stringify(newVal);
        if (localVal !== newValStr) {
          localStorage.setItem(key, newValStr);
          restoredCount++;
        }
      }
    });
    
    return restoredCount;
  }

  // Restore scores from static backup on GitHub Pages once
  if (isGitHubPages && localStorage.getItem('duru_backup_imported') !== 'true') {
    fetch('./scores_backup.json')
      .then(function(res) {
        if (!res.ok) throw new Error('HTTP status ' + res.status);
        return res.json();
      })
      .then(function(data) {
        var count = restoreScores(data);
        localStorage.setItem('duru_backup_imported', 'true');
        if (count > 0) {
          window.location.reload();
        }
      })
      .catch(function(err) {
        console.warn('Could not restore scores from backup file:', err);
        // Set it anyway to prevent infinite loop of failed fetch attempts
        localStorage.setItem('duru_backup_imported', 'true');
      });
  }

  if (!isGitHubPages) {
    // Restore scores from server database on load (merging all historical logs)
    fetch('/api/score')
      .then(function(res) {
        if (!res.ok) throw new Error('HTTP status ' + res.status);
        return res.json();
      })
      .then(function(data) {
        var count = restoreScores(data);
        if (count > 0) {
          window.location.reload();
        }
      })
      .catch(function(err) {
        console.warn('Could not restore scores from server:', err);
      });
  }

  function parseAttemptDate(att) {
    if (att.attemptId && att.attemptId.indexOf('att_') === 0) {
      var ts = parseInt(att.attemptId.replace('att_', ''), 10);
      if (!isNaN(ts)) return ts;
    }
    if (att.datum) {
      var clean = att.datum.replace(',', '');
      var parts = clean.split(' ');
      if (parts.length >= 2) {
        var dParts = parts[0].split('-');
        var tParts = parts[1].split(':');
        if (dParts.length === 3 && tParts.length >= 2) {
          return new Date(dParts[2], dParts[1] - 1, dParts[0], tParts[0], tParts[1]).getTime();
        }
      }
    }
    return 0;
  }

  renderVakken();

  // Intercept local storage writes inside the iframe to sync them back to the server
  var frame = document.getElementById('vak-frame');
  if (frame) {
    frame.addEventListener('load', function() {
      try {
        var win = frame.contentWindow;
        if (!win || !win.Storage) return;
        
        // Save references to original prototype function (much safer than instance overrides)
        var originalSetItem = win.Storage.prototype.setItem;
        
        win.Storage.prototype.setItem = function(key, value) {
          // Always execute original native method first with correct context
          originalSetItem.call(this, key, value);
          
          if (isGitHubPages) return;
          
          // Wrap sync logic in try-catch to guarantee it never crashes the calling app
          try {
            if (key && (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0)) {
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
          } catch (syncErr) {
            console.warn('Error in localStorage interception sync:', syncErr);
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
