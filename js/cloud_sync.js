/* =========================================================
   Duru's Schoolhub — Bulut Senkronizasyon Motoru (Cloud Sync)
   Firebase Realtime DB, JSONBin.io ve REST API desteği.
   ========================================================= */

(function () {
  "use strict";

  var STORAGE_KEY_CONFIG = "duru_cloud_sync_config";
  var STORAGE_KEY_LAST_SYNC = "duru_cloud_last_sync";

  var DEFAULT_CONFIG = {
    enabled: true,
    provider: "firebase", // "firebase", "jsonbin", "custom"
    endpointUrl: "", // Firebase Database URL (örn. https://duru-okul-default-rtdb.europe-west1.firebasedatabase.app/scores.json)
    apiKey: "",
    autoSyncIntervalMs: 45000
  };

  var syncState = {
    status: "idle", // "idle", "syncing", "success", "error", "offline"
    lastSyncTime: null,
    lastError: null,
    inFlight: false
  };

  function getConfig() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY_CONFIG);
      if (saved) {
        return Object.assign({}, DEFAULT_CONFIG, JSON.parse(saved));
      }
    } catch (e) { /* varsayılana dön */ }
    return DEFAULT_CONFIG;
  }

  function saveConfig(cfg) {
    try {
      localStorage.setItem(STORAGE_KEY_CONFIG, JSON.stringify(cfg));
    } catch (e) {}
  }

  function updateStatusUI(status, message) {
    syncState.status = status;
    var pill = document.getElementById("cloud-sync-status-text");
    var btn = document.getElementById("cloud-sync-btn");
    var modalStatus = document.getElementById("cloud-modal-status");

    var label = message || "Bulut Senkron: Hazır";
    var icon = "☁️";

    if (status === "syncing") {
      icon = "🔄";
      label = message || "Eşitleniyor...";
      if (btn) btn.classList.add("syncing");
    } else if (status === "success") {
      icon = "🟢";
      label = message || "Eşitlendi";
      if (btn) btn.classList.remove("syncing");
    } else if (status === "error") {
      icon = "⚠️";
      label = message || "Yapılandırma Gerekli";
      if (btn) btn.classList.remove("syncing");
    } else if (status === "offline") {
      icon = "📡";
      label = "Çevrimdışı (Yerel)";
      if (btn) btn.classList.remove("syncing");
    } else if (status === "idle") {
      if (btn) btn.classList.remove("syncing");
    }

    if (pill) pill.textContent = label;
    if (btn) btn.setAttribute("title", "Bulut Senkron: " + label + " (" + (syncState.lastSyncTime || "Henüz yapılmadı") + ")");
    if (modalStatus) {
      modalStatus.innerHTML = icon + " <strong>" + escapeHtml(label) + "</strong>" +
        (syncState.lastSyncTime ? " <small style='color:var(--grijs-licht);'>(" + syncState.lastSyncTime + ")</small>" : "");
    }
  }

  function getActiveUser() {
    return localStorage.getItem("duru_active_user") || sessionStorage.getItem("duru_active_user") || "duru";
  }

  function exportLocalDataPayload() {
    var payload = {
      updatedAt: new Date().toISOString(),
      student: getActiveUser(),
      scores: []
    };

    var seenKeys = {};
    for (var i = 0; i < localStorage.length; i++) {
      var rawKey = localStorage.key(i);
      if (!rawKey) continue;

      var logicalKey = rawKey;
      if (rawKey.indexOf("user_") === 0) {
        var parts = rawKey.split("_");
        if (parts.length >= 3) {
          logicalKey = parts.slice(2).join("_");
        }
      }

      if (logicalKey && (logicalKey.indexOf("duru_") === 0 || logicalKey.indexOf("begrijpend_lezen_") === 0)) {
        if (logicalKey === "duru_active_user" || logicalKey === "duru_users" || logicalKey === "duru_backup_imported" || logicalKey === "duru_encrypted_backup") {
          continue;
        }
        if (seenKeys[logicalKey]) continue;
        seenKeys[logicalKey] = true;

        var valStr = localStorage.getItem(rawKey);
        if (valStr) {
          try {
            payload.scores.push({ key: logicalKey, val: JSON.parse(valStr) });
          } catch (e) {
            payload.scores.push({ key: logicalKey, val: valStr });
          }
        }
      }
    }

    return payload;
  }

  function mergeRemoteData(remoteScores) {
    if (!remoteScores || !Array.isArray(remoteScores) || remoteScores.length === 0) {
      return 0;
    }

    var restoredCount = 0;
    if (typeof window.restoreScores === "function") {
      restoredCount = window.restoreScores(remoteScores);
    } else {
      var activeUser = getActiveUser();
      remoteScores.forEach(function (item) {
        if (item && item.key) {
          var targetKey = activeUser ? ("user_" + activeUser + "_" + item.key) : item.key;
          var localValStr = localStorage.getItem(targetKey);
          var newValStr = typeof item.val === "object" ? JSON.stringify(item.val) : String(item.val);

          if (!localValStr || localValStr !== newValStr) {
            localStorage.setItem(targetKey, newValStr);
            restoredCount++;
          }
        }
      });
    }

    if (restoredCount > 0) {
      if (typeof window.renderVakken === "function") window.renderVakken();
      if (typeof window.loadDashboardData === "function") window.loadDashboardData();
      if (typeof window.renderParentDashboard === "function") window.renderParentDashboard();
    }

    return restoredCount;
  }

  function getEffectiveEndpoint() {
    var isLocal = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.port === "8080");
    if (isLocal) {
      return { url: "/api/score", type: "local" };
    }
    var cfg = getConfig();
    if (cfg.endpointUrl && cfg.endpointUrl.trim().length > 0) {
      var u = cfg.endpointUrl.trim();
      var isFirebase = u.indexOf("firebaseio.com") !== -1 || u.indexOf("firebasedatabase.app") !== -1;
      return { url: u, type: isFirebase ? "firebase" : "custom", apiKey: cfg.apiKey };
    }
    return null;
  }

  /**
   * 1. PULL
   */
  function pullFromCloud(silent) {
    if (!navigator.onLine) {
      updateStatusUI("offline", "Çevrimdışı (Yerel)");
      return Promise.resolve(0);
    }

    var ep = getEffectiveEndpoint();
    if (!ep) {
      if (!silent) updateStatusUI("error", "Bulut URL Gerekli");
      return Promise.resolve(0);
    }

    if (!silent) updateStatusUI("syncing", "Buluttan çekiliyor...");
    syncState.inFlight = true;

    var headers = { "Cache-Control": "no-cache" };
    if (ep.apiKey) {
      headers["X-Master-Key"] = ep.apiKey;
      headers["X-Access-Key"] = ep.apiKey;
    }

    var fetchUrl = ep.url + (ep.url.indexOf("?") === -1 ? "?t=" + Date.now() : "&t=" + Date.now());

    return fetch(fetchUrl, {
      method: "GET",
      headers: headers
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        syncState.inFlight = false;
        var scores = [];
        if (Array.isArray(data)) {
          scores = data;
        } else if (data && Array.isArray(data.scores)) {
          scores = data.scores;
        } else if (data && data.record && Array.isArray(data.record.scores)) {
          scores = data.record.scores;
        }

        var updated = mergeRemoteData(scores);
        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);

        updateStatusUI("success", "Eşitlendi (" + timeStr + ")");
        return updated;
      })
      .catch(function (err) {
        syncState.inFlight = false;
        console.warn("Cloud Sync Pull hatası:", err.message);
        updateStatusUI("error", "Eşitleme Hatası (HTTP)");
        return 0;
      });
  }

  /**
   * 2. PUSH
   */
  var pushDebounceTimer = null;
  function pushToCloud(immediate) {
    if (!navigator.onLine) return Promise.resolve(false);

    var ep = getEffectiveEndpoint();
    if (!ep) {
      return Promise.resolve(false);
    }

    clearTimeout(pushDebounceTimer);
    if (!immediate) {
      pushDebounceTimer = setTimeout(function () { pushToCloud(true); }, 1200);
      return Promise.resolve(true);
    }

    var payload = exportLocalDataPayload();
    if (payload.scores.length === 0) return Promise.resolve(false);

    updateStatusUI("syncing", "Buluta aktarılıyor...");

    var method = (ep.type === "firebase") ? "PUT" : "POST";
    var headers = { "Content-Type": "application/json" };
    if (ep.apiKey) {
      headers["X-Master-Key"] = ep.apiKey;
      headers["X-Access-Key"] = ep.apiKey;
    }

    return fetch(ep.url, {
      method: method,
      headers: headers,
      body: JSON.stringify(payload)
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);
        updateStatusUI("success", "Eşitlendi (" + timeStr + ")");
        return true;
      })
      .catch(function (err) {
        console.warn("Cloud Sync Push hatası:", err.message);
        updateStatusUI("error", "Aktarım Hatası");
        return false;
      });
  }

  function escapeHtml(str) {
    return String(str == null ? "" : str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function initCloudSyncModal() {
    var btn = document.getElementById("cloud-sync-btn");
    var modal = document.getElementById("cloud-sync-modal");
    var closeBtn = document.getElementById("cloud-modal-close");
    var syncNowBtn = document.getElementById("cloud-modal-sync-now");
    var saveCfgBtn = document.getElementById("cloud-modal-save-config");
    var customUrlInput = document.getElementById("cloud-custom-url-input");
    var apiKeyInput = document.getElementById("cloud-api-key-input");

    if (btn) {
      btn.addEventListener("click", function () {
        if (modal) {
          modal.style.display = "flex";
          var cfg = getConfig();
          if (customUrlInput) customUrlInput.value = cfg.endpointUrl || "";
          if (apiKeyInput) apiKeyInput.value = cfg.apiKey || "";
          updateStatusUI(syncState.status);
        }
      });
    }

    if (closeBtn && modal) {
      closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
      });
    }

    if (modal) {
      modal.addEventListener("click", function (e) {
        if (e.target === modal) modal.style.display = "none";
      });
    }

    if (syncNowBtn) {
      syncNowBtn.addEventListener("click", function () {
        var ep = getEffectiveEndpoint();
        if (!ep) {
          alert("Otomatik bulut senkronizasyonu için lütfen bir Firebase Database URL veya JSONBin adresi tanımlayın. Veya hemen alttaki '📥 Voortgang Opslaan' (Export/Import) butonu ile tek tıkla dosya aktarımı yapabilirsiniz!");
          return;
        }

        syncNowBtn.textContent = "🔄 Eşitleniyor...";
        pullFromCloud(false).then(function () {
          pushToCloud(true).then(function (success) {
            syncNowBtn.textContent = success ? "✅ Başarılı!" : "⚠️ Hata Oluştu";
            setTimeout(function () { syncNowBtn.textContent = "🔄 Şimdi Senkronize Et"; }, 2000);
          });
        });
      });
    }

    if (saveCfgBtn) {
      saveCfgBtn.addEventListener("click", function () {
        var cfg = getConfig();
        if (customUrlInput) cfg.endpointUrl = customUrlInput.value.trim();
        if (apiKeyInput) cfg.apiKey = apiKeyInput.value.trim();
        saveConfig(cfg);
        alert("Bulut bağlantı ayarları kaydedildi!");
        if (modal) modal.style.display = "none";
        pullFromCloud(false).then(function () {
          pushToCloud(true);
        });
      });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initCloudSyncModal();

    setTimeout(function () {
      pullFromCloud(true).then(function () {
        var payload = exportLocalDataPayload();
        if (payload.scores && payload.scores.length > 0) {
          pushToCloud(true);
        }
      });
    }, 600);

    var cfg = getConfig();
    setInterval(function () {
      pullFromCloud(true);
    }, cfg.autoSyncIntervalMs || 45000);

    window.addEventListener("online", function () {
      updateStatusUI("syncing", "İnternet bağlandı, eşitleniyor...");
      pullFromCloud(false).then(function () { pushToCloud(true); });
    });

    window.addEventListener("offline", function () {
      updateStatusUI("offline", "Çevrimdışı (Yerel)");
    });
  });

  window.CloudSync = {
    pull: pullFromCloud,
    push: pushToCloud,
    getConfig: getConfig,
    saveConfig: saveConfig,
    exportPayload: exportLocalDataPayload
  };

})();
