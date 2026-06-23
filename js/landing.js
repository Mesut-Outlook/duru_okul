/* =========================================================
   Duru's Schoolhub — Landing Page Logic
   Bevat: vakken-data, kaart-rendering, uitklap-logica,
          iframe-shell (terugbalk + history-integratie)
   ========================================================= */

// ── User Management & Storage Interception ─────────────────
function getActiveUser() {
  return localStorage.getItem('duru_active_user') || sessionStorage.getItem('duru_active_user');
}

function setActiveUser(username, rememberMe) {
  if (rememberMe) {
    localStorage.setItem('duru_active_user', username);
  } else {
    sessionStorage.setItem('duru_active_user', username);
  }
}

function clearActiveUser() {
  localStorage.removeItem('duru_active_user');
  sessionStorage.removeItem('duru_active_user');
}

function simpleHash(str) {
  var hash = 0;
  for (var i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0; // Convert to 32bit integer
  }
  return Math.abs(hash).toString(16);
}

function getUsers() {
  try {
    return JSON.parse(localStorage.getItem('duru_users')) || {};
  } catch (e) {
    return {};
  }
}

function registerLocalUser(username, password) {
  var users = getUsers();
  users[username.toLowerCase()] = simpleHash(password);
  localStorage.setItem('duru_users', JSON.stringify(users));
}

function validateLocalUser(username, password) {
  var users = getUsers();
  var uLower = username.toLowerCase();
  if (users[uLower]) {
    return users[uLower] === simpleHash(password);
  }
  return false;
}

function xorCipher(text, key) {
  var result = '';
  for (var i = 0; i < text.length; i++) {
    result += String.fromCharCode(text.charCodeAt(i) ^ key.charCodeAt(i % key.length));
  }
  return result;
}

function getPrefixedKey(key) {
  if (!key) return key;
  // Exclude system keys
  if (key === 'duru_active_user' || key === 'duru_users' || key === 'duru_backup_imported' || key === 'duru_encrypted_backup') {
    return key;
  }
  if (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0) {
    var activeUser = getActiveUser();
    if (activeUser) {
      return 'user_' + activeUser + '_' + key;
    }
  }
  return key;
}

// Override prototype for main window
var originalGetItem = window.Storage.prototype.getItem;
var originalSetItem = window.Storage.prototype.setItem;
var originalRemoveItem = window.Storage.prototype.removeItem;

window.Storage.prototype.getItem = function(key) {
  var prefixedKey = getPrefixedKey(key);
  return originalGetItem.call(this, prefixedKey);
};

window.Storage.prototype.setItem = function(key, value) {
  var prefixedKey = getPrefixedKey(key);
  originalSetItem.call(this, prefixedKey, value);
};

window.Storage.prototype.removeItem = function(key) {
  var prefixedKey = getPrefixedKey(key);
  originalRemoveItem.call(this, prefixedKey);
};

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

  function migratePreExistingLocalScores(username) {
    var unprefixedData = [];
    var originalGetItem = window.Storage.prototype.getItem;
    var originalSetItem = window.Storage.prototype.setItem;
    
    for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);
      if (key && (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0)) {
        if (key.indexOf('user_') !== 0) {
          if (key === 'duru_active_user' || key === 'duru_users' || key === 'duru_backup_imported' || key === 'duru_encrypted_backup') {
            continue;
          }
          var valStr = originalGetItem.call(localStorage, key);
          if (valStr) {
            try {
              var val = JSON.parse(valStr);
              unprefixedData.push({ key: key, val: val });
            } catch (e) {
              console.warn('Failed to parse local unprefixed key:', key, e);
            }
          }
        }
      }
    }
    
    if (unprefixedData.length > 0) {
      var prevActiveUser = originalGetItem.call(localStorage, 'duru_active_user');
      originalSetItem.call(localStorage, 'duru_active_user', username);
      
      restoreScores(unprefixedData);
      
      var originalRemoveItem = window.Storage.prototype.removeItem;
      unprefixedData.forEach(function(item) {
        originalRemoveItem.call(localStorage, item.key);
      });
      
      if (prevActiveUser) {
        originalSetItem.call(localStorage, 'duru_active_user', prevActiveUser);
      } else {
        originalRemoveItem.call(localStorage, 'duru_active_user');
      }
    }
  }

  // We initialize the User Authentication interface
  initUserAuth();

  if (!isGitHubPages && getActiveUser()) {
    // Restore scores from server database on load if logged in (merging all historical logs)
    fetch('/api/score?t=' + new Date().getTime())
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

  function initUserAuth() {
    var overlay = document.getElementById('login-overlay');
    var userStatus = document.getElementById('user-status-container');
    var userDisplay = document.getElementById('user-display-name-text');
    var logoutBtn = document.getElementById('logout-btn');

    var tabLogin = document.getElementById('auth-tab-login');
    var tabRegister = document.getElementById('auth-tab-register');
    var confirmContainer = document.getElementById('auth-confirm-container');
    var rememberContainer = document.getElementById('auth-remember-container');
    var submitBtn = document.getElementById('auth-submit-btn');
    var errorEl = document.getElementById('auth-error');

    var form = document.getElementById('auth-form');
    var usernameInput = document.getElementById('auth-username');
    var passwordInput = document.getElementById('auth-password');
    var confirmInput = document.getElementById('auth-password-confirm');
    var rememberInput = document.getElementById('auth-remember');

    var isRegisterMode = false;

    // 1. Check if user is logged in
    var activeUser = getActiveUser();
    if (activeUser) {
      if (overlay) overlay.style.display = 'none';
      if (userStatus) userStatus.style.display = 'flex';
      if (userDisplay) userDisplay.textContent = activeUser;
    } else {
      if (overlay) overlay.style.display = 'flex';
      if (userStatus) userStatus.style.display = 'none';
    }

    // 2. Tab switching
    if (tabLogin && tabRegister) {
      tabLogin.addEventListener('click', function() {
        isRegisterMode = false;
        tabLogin.style.borderBottom = '2px solid #064e3b';
        tabLogin.style.color = '#1d1d1f';
        tabLogin.style.fontWeight = '600';
        tabRegister.style.borderBottom = '2px solid transparent';
        tabRegister.style.color = '#6e6e73';
        tabRegister.style.fontWeight = '400';
        if (confirmContainer) confirmContainer.style.display = 'none';
        if (rememberContainer) rememberContainer.style.display = 'flex';
        if (submitBtn) submitBtn.textContent = 'Giriş Yap';
        if (errorEl) errorEl.style.display = 'none';
        if (confirmInput) confirmInput.required = false;
      });

      tabRegister.addEventListener('click', function() {
        isRegisterMode = true;
        tabRegister.style.borderBottom = '2px solid #064e3b';
        tabRegister.style.color = '#1d1d1f';
        tabRegister.style.fontWeight = '600';
        tabLogin.style.borderBottom = '2px solid transparent';
        tabLogin.style.color = '#6e6e73';
        tabLogin.style.fontWeight = '400';
        if (confirmContainer) confirmContainer.style.display = 'flex';
        if (rememberContainer) rememberContainer.style.display = 'none';
        if (submitBtn) submitBtn.textContent = 'Kayıt Ol';
        if (errorEl) errorEl.style.display = 'none';
        if (confirmInput) confirmInput.required = true;
      });
    }

    // 3. Form submit
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (errorEl) errorEl.style.display = 'none';

        var username = usernameInput.value.trim();
        var password = passwordInput.value;
        var rememberMe = rememberInput.checked;

        if (!username || !password) {
          showError('Vul alle velden in.');
          return;
        }

        if (isRegisterMode) {
          // Register mode
          if (password.length < 8) {
            showError('Wachtwoord moet minimaal 8 tekens lang zijn.');
            return;
          }

          if (password !== confirmInput.value) {
            showError('Wachtwoorden komen niet overeen.');
            return;
          }

          var uLower = username.toLowerCase();
          if (uLower === 'duru') {
            showError('Deze gebruikersnaam is al gereserveerd.');
            return;
          }

          var users = getUsers();
          if (users[uLower]) {
            showError('Deze gebruikersnaam bestaat al.');
            return;
          }

          // Save new user
          registerLocalUser(username, password);
          migratePreExistingLocalScores(username);
          setActiveUser(username, true); // auto-remember on register
          window.location.reload();
        } else {
          // Login mode
          var uLower = username.toLowerCase();
          if (uLower === 'duru') {
            // Special login for duru
            if (password === '12341234') {
              // Check if already registered locally
              var users = getUsers();
              if (users['duru']) {
                // Log in locally
                migratePreExistingLocalScores('duru');
                setActiveUser('duru', rememberMe);
                window.location.reload();
              } else {
                // First time login - try to decrypt scores_backup.json
                if (submitBtn) submitBtn.textContent = 'Voortgang laden...';
                fetch('./scores_backup.json')
                  .then(function(res) {
                    if (!res.ok) throw new Error('Yedek dosyası bulunamadı.');
                    return res.json();
                  })
                  .then(function(data) {
                    if (data && data.encrypted && data.data) {
                      try {
                        // Decrypt
                        var decryptedText = xorCipher(atob(data.data), 'duru:12341234');
                        // Oudere backup-export verloor niet-Latin1 tekens (bv. een "–" in
                        // examtitels) door een lossy Latin1-omzetting; die bytes komen terug
                        // als ongeldige controle-tekens die JSON.parse() laten crashen.
                        decryptedText = decryptedText.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F-\x9F]/g, '–');
                        var parsedScores = JSON.parse(decryptedText);
                        if (!parsedScores || !Array.isArray(parsedScores)) parsedScores = [];

                        // Import local pre-existing unprefixed keys
                        var originalGetItem = window.Storage.prototype.getItem;
                        for (var i = 0; i < localStorage.length; i++) {
                          var key = localStorage.key(i);
                          if (key && (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0)) {
                            if (key.indexOf('user_') !== 0) {
                              if (key === 'duru_active_user' || key === 'duru_users' || key === 'duru_backup_imported' || key === 'duru_encrypted_backup') {
                                continue;
                              }
                              var valStr = originalGetItem.call(localStorage, key);
                              if (valStr) {
                                try {
                                  var val = JSON.parse(valStr);
                                  parsedScores.push({ key: key, val: val });
                                } catch (e) {
                                  console.warn('Failed to parse local unprefixed key:', key, e);
                                }
                              }
                            }
                          }
                        }
                        
                        // Temporarily set active user so restoreScores writes to prefixed keys
                        setActiveUser('duru', rememberMe);
                        
                        // Restore (this will automatically merge the backup and the local unprefixed scores!)
                        restoreScores(parsedScores);

                        // Clean up the local unprefixed keys
                        var originalRemoveItem = window.Storage.prototype.removeItem;
                        var keysToRemove = [];
                        for (var i = 0; i < localStorage.length; i++) {
                          var key = localStorage.key(i);
                          if (key && (key.indexOf('duru_') === 0 || key.indexOf('begrijpend_lezen_') === 0)) {
                            if (key.indexOf('user_') !== 0) {
                              if (key === 'duru_active_user' || key === 'duru_users' || key === 'duru_backup_imported' || key === 'duru_encrypted_backup') {
                                continue;
                              }
                              keysToRemove.push(key);
                            }
                          }
                        }
                        keysToRemove.forEach(function(k) {
                          originalRemoveItem.call(localStorage, k);
                        });
                        
                        // Register locally
                        registerLocalUser('duru', '12341234');
                        localStorage.setItem('duru_backup_imported', 'true');
                        
                        window.location.reload();
                      } catch (decErr) {
                        console.error(decErr);
                        showError('Fout bij het ontcijferen van de gegevens.');
                        clearActiveUser();
                        if (submitBtn) submitBtn.textContent = 'Giriş Yap';
                      }
                    } else {
                      showError('Ongeldig backup bestand.');
                      if (submitBtn) submitBtn.textContent = 'Giriş Yap';
                    }
                  })
                  .catch(function(err) {
                    console.error(err);
                    showError('Kan voortgangsbestand niet ophalen. Controleer je internetverbinding.');
                    if (submitBtn) submitBtn.textContent = 'Giriş Yap';
                  });
              }
            } else {
              showError('Gebruikersnaam of wachtwoord onjuist.');
            }
          } else {
            // Regular user login
            if (validateLocalUser(username, password)) {
              migratePreExistingLocalScores(username);
              setActiveUser(username, rememberMe);
              window.location.reload();
            } else {
              showError('Gebruikersnaam of wachtwoord onjuist.');
            }
          }
        }
      });
    }

    // 4. Logout action
    if (logoutBtn) {
      logoutBtn.addEventListener('click', function() {
        clearActiveUser();
        window.location.reload();
      });
    }

    function showError(msg) {
      if (errorEl) {
        errorEl.textContent = msg;
        errorEl.style.display = 'block';
      }
    }
  }

  renderVakken();

  // Intercept local storage writes, reads, and deletes inside the iframe
  var frame = document.getElementById('vak-frame');
  if (frame) {
    frame.addEventListener('load', function() {
      try {
        var win = frame.contentWindow;
        if (!win || !win.Storage) return;
        
        // Override getItem
        win.Storage.prototype.getItem = function(key) {
          var prefixedKey = getPrefixedKey(key);
          return originalGetItem.call(this, prefixedKey);
        };
        
        // Override removeItem
        win.Storage.prototype.removeItem = function(key) {
          var prefixedKey = getPrefixedKey(key);
          originalRemoveItem.call(this, prefixedKey);
        };
        
        // Override setItem with sync logic
        win.Storage.prototype.setItem = function(key, value) {
          var prefixedKey = getPrefixedKey(key);
          originalSetItem.call(this, prefixedKey, value);
          
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
