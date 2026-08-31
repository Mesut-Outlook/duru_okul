/* =========================================================
   Duru's Schoolhub — Canlı Firebase Realtime Bulut Senkronizasyonu
   Firebase Realtime Database REST / SSE Live Sync
   ========================================================= */

(function () {
  "use strict";

  var FIREBASE_URL = "https://duru-okul-default-rtdb.europe-west1.firebasedatabase.app/scores.json";
  var STORAGE_KEY_CONFIG = "duru_cloud_sync_config";
  var STORAGE_KEY_LAST_SYNC = "duru_cloud_last_sync";
  var STORAGE_KEY_LAST_REMOTE_TS = "duru_cloud_last_remote_ts";

  var DEFAULT_CONFIG = {
    enabled: true,
    provider: "firebase",
    endpointUrl: FIREBASE_URL,
    apiKey: "",
    autoSyncIntervalMs: 20000 // 20 saniyede bir canlı kontrol
  };

  var syncState = {
    status: "idle", // "idle", "syncing", "success", "error", "offline"
    lastSyncTime: localStorage.getItem(STORAGE_KEY_LAST_SYNC) || null,
    lastRemoteTs: localStorage.getItem(STORAGE_KEY_LAST_REMOTE_TS) || null,
    lastError: null,
    inFlight: false
  };

  function getConfig() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY_CONFIG);
      if (saved) {
        var parsed = JSON.parse(saved);
        // Eski veya geçersiz URL'leri otomatik Firebase'e güncelle
        if (!parsed.endpointUrl || parsed.endpointUrl.indexOf("npoint.io") !== -1 || parsed.endpointUrl.indexOf("firebasedatabase.app") === -1) {
          parsed.endpointUrl = FIREBASE_URL;
          localStorage.setItem(STORAGE_KEY_CONFIG, JSON.stringify(parsed));
        }
        return Object.assign({}, DEFAULT_CONFIG, parsed);
      }
    } catch (e) { /* varsayılana dön */ }
    return DEFAULT_CONFIG;
  }

  function saveConfig(cfg) {
    try {
      localStorage.setItem(STORAGE_KEY_CONFIG, JSON.stringify(cfg));
    } catch (e) {}
  }

  function showSyncToast(message) {
    var toast = document.getElementById("cloud-sync-toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "cloud-sync-toast";
      toast.style.cssText = "position:fixed;bottom:24px;right:24px;background:#064e3b;color:#fff;padding:12px 20px;border-radius:12px;font-size:14px;font-weight:600;box-shadow:0 8px 24px rgba(0,0,0,0.25);z-index:99999;display:flex;align-items:center;gap:10px;transform:translateY(100px);opacity:0;transition:all 0.3s cubic-bezier(0.16, 1, 0.3, 1);";
      document.body.appendChild(toast);
    }
    toast.innerHTML = "<span>🔥</span> " + escapeHtml(message);
    toast.style.transform = "translateY(0)";
    toast.style.opacity = "1";
    setTimeout(function () {
      toast.style.transform = "translateY(100px)";
      toast.style.opacity = "0";
    }, 4000);
  }

  function updateStatusUI(status, message) {
    syncState.status = status;
    var pill = document.getElementById("cloud-sync-status-text");
    var btn = document.getElementById("cloud-sync-btn");
    var modalStatus = document.getElementById("cloud-modal-status");

    var label = message || "Bulut Senkron: Aktif";
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
      label = message || "Bağlantı Hatası";
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

  function getEffectiveUrl() {
    var cfg = getConfig();
    return cfg.endpointUrl || FIREBASE_URL;
  }

  /**
   * 1. PULL (Buluttan Çekme)
   */
  function pullFromCloud(silent) {
    if (!navigator.onLine) {
      updateStatusUI("offline", "Çevrimdışı (Yerel)");
      return Promise.resolve(0);
    }

    var url = getEffectiveUrl();
    if (!silent) updateStatusUI("syncing", "Buluttan çekiliyor...");
    syncState.inFlight = true;

    var fetchUrl = url + (url.indexOf("?") === -1 ? "?t=" + Date.now() : "&t=" + Date.now());

    return fetch(fetchUrl, {
      method: "GET",
      headers: { "Cache-Control": "no-cache" }
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        syncState.inFlight = false;
        if (!data) {
          updateStatusUI("success", "Bulut: Hazır");
          return 0;
        }

        var scores = Array.isArray(data) ? data : (data.scores || []);
        var remoteTs = data.updatedAt || null;

        var updatedCount = 0;
        if (scores.length > 0) {
          updatedCount = mergeRemoteData(scores);
        }

        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);

        if (remoteTs && remoteTs !== syncState.lastRemoteTs) {
          syncState.lastRemoteTs = remoteTs;
          localStorage.setItem(STORAGE_KEY_LAST_REMOTE_TS, remoteTs);
          if (updatedCount > 0 && !silent) {
            showSyncToast("Duru'nun yeni sınav sonuçları buluttan güncellendi!");
          }
        }

        updateStatusUI("success", "Eşitlendi (" + timeStr + ")");
        return updatedCount;
      })
      .catch(function (err) {
        syncState.inFlight = false;
        console.warn("Cloud Sync Pull hatası:", err.message);
        updateStatusUI("error", "Bağlantı Hatası");
        return 0;
      });
  }

  /**
   * 2. PUSH (Buluta Yükleme)
   */
  var pushDebounceTimer = null;
  function pushToCloud(immediate) {
    if (!navigator.onLine) return Promise.resolve(false);

    clearTimeout(pushDebounceTimer);
    if (!immediate) {
      pushDebounceTimer = setTimeout(function () { pushToCloud(true); }, 1000);
      return Promise.resolve(true);
    }

    var payload = exportLocalDataPayload();
    if (payload.scores.length === 0) return Promise.resolve(false);

    updateStatusUI("syncing", "Buluta aktarılıyor...");

    var url = getEffectiveUrl();
    var method = (url.indexOf("firebasedatabase.app") !== -1 || url.indexOf("firebaseio.com") !== -1) ? "PUT" : "POST";

    return fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        syncState.lastRemoteTs = payload.updatedAt;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);
        localStorage.setItem(STORAGE_KEY_LAST_REMOTE_TS, payload.updatedAt);
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

    if (btn) {
      btn.addEventListener("click", function () {
        if (modal) {
          modal.style.display = "flex";
          var cfg = getConfig();
          if (customUrlInput) customUrlInput.value = cfg.endpointUrl || FIREBASE_URL;
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
        syncNowBtn.textContent = "🔄 Eşitleniyor...";
        pullFromCloud(false).then(function () {
          pushToCloud(true).then(function (success) {
            syncNowBtn.textContent = success ? "✅ Başarılı!" : "⚠️ Tamamlandı";
            setTimeout(function () { syncNowBtn.textContent = "🔄 Şimdi Senkronize Et"; }, 2000);
          });
        });
      });
    }

    if (saveCfgBtn) {
      saveCfgBtn.addEventListener("click", function () {
        var cfg = getConfig();
        if (customUrlInput) cfg.endpointUrl = customUrlInput.value.trim() || FIREBASE_URL;
        saveConfig(cfg);
        alert("Firebase bağlantı ayarları kaydedildi!");
        if (modal) modal.style.display = "none";
        pullFromCloud(false).then(function () {
          pushToCloud(true);
        });
      });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initCloudSyncModal();

    // Sayfa açıldığında iki yönlü otomatik canlı eşitleme
    setTimeout(function () {
      pullFromCloud(true).then(function () {
        var payload = exportLocalDataPayload();
        if (payload.scores && payload.scores.length > 0) {
          pushToCloud(true);
        }
      });
    }, 400);

    // Arka planda düzenli canlı kontrol (20 saniyede bir)
    var cfg = getConfig();
    setInterval(function () {
      pullFromCloud(true);
    }, cfg.autoSyncIntervalMs || 20000);

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
    exportPayload: exportLocalDataPayload,
    FIREBASE_URL: FIREBASE_URL
  };

})();
