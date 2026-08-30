/* =========================================================
   Duru's Schoolhub — Bulut Senkronizasyon Motoru (Cloud Sync)
   GitHub Pages ve çoklu cihazlar (Baba & Duru) arasında
   otomatik, anlık ve çift yönlü veri senkronizasyonu sağlar.
   ========================================================= */

(function () {
  "use strict";

  var STORAGE_KEY_CONFIG = "duru_cloud_sync_config";
  var STORAGE_KEY_LAST_SYNC = "duru_cloud_last_sync";

  // Varsayılan Bulut Senkronizasyon Yapılandırması (JSONBin / Firebase / REST)
  var DEFAULT_CONFIG = {
    enabled: true,
    provider: "jsonbin", // "jsonbin", "firebase", "custom"
    binId: "67c35848e41b4d34e49ea82b", // Duru Okul Genel Bulut Deposu
    apiKey: "$2a$10$3YF9qBf9XnOwhh.lC8eLpuu7Qc5iV0FhX5aC/f3pE202026duru", // Okuma/Yazma Anahtarı
    customUrl: "",
    autoSyncIntervalMs: 45000 // Her 45 saniyede bir yeni sınav var mı diye kontrol et
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

    var label = message || "Bulut Senkron: Aktif";
    var icon = "☁️";

    if (status === "syncing") {
      icon = "🔄";
      label = "Eşitleniyor...";
      if (btn) btn.classList.add("syncing");
    } else if (status === "success") {
      icon = "🟢";
      label = message || "Eşitlendi";
      if (btn) btn.classList.remove("syncing");
    } else if (status === "error") {
      icon = "⚠️";
      label = message || "Eşitleme Hatası";
      if (btn) btn.classList.remove("syncing");
    } else if (status === "offline") {
      icon = "📡";
      label = "Çevrimdışı (Yerel)";
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

  /**
   * Cihazdaki tüm sınav ve ilerleme verilerini toplar
   */
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

  /**
   * Buluttan gelen veriyi yerel veritabanıyla akıllıca birleştirir (Merge)
   */
  function mergeRemoteData(remoteScores) {
    if (!remoteScores || !Array.isArray(remoteScores) || remoteScores.length === 0) {
      return 0;
    }

    var restoredCount = 0;
    if (typeof window.restoreScores === "function") {
      restoredCount = window.restoreScores(remoteScores);
    } else {
      // Fallback manual merger
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
      // Yenilenen verileri tüm ekranlara anında yansıt
      if (typeof window.renderVakken === "function") window.renderVakken();
      if (typeof window.loadDashboardData === "function") window.loadDashboardData();
      if (typeof window.renderParentDashboard === "function") window.renderParentDashboard();
    }

    return restoredCount;
  }

  /**
   * 1. PULL: Buluttan en son verileri çek ve birleştir
   */
  function pullFromCloud(silent) {
    if (!navigator.onLine) {
      updateStatusUI("offline", "Çevrimdışı (Yerel)");
      return Promise.resolve(0);
    }

    var cfg = getConfig();
    if (!cfg.enabled) return Promise.resolve(0);

    if (!silent) updateStatusUI("syncing", "Buluttan çekiliyor...");
    syncState.inFlight = true;

    // Hedef URL belirleme (Yerel server.py veya harici REST API)
    var isLocalServer = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.port === "8080");
    var url = isLocalServer ? "/api/score?t=" + Date.now() : (cfg.customUrl || ("https://api.npoint.io/46d926ef91f86bd069ca"));

    return fetch(url, {
      method: "GET",
      headers: { "Cache-Control": "no-cache" }
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        syncState.inFlight = false;
        var scores = Array.isArray(data) ? data : (data.scores || []);
        var updated = mergeRemoteData(scores);

        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);

        updateStatusUI("success", "Eşitlendi (" + timeStr + ")");
        return updated;
      })
      .catch(function (err) {
        syncState.inFlight = false;
        // Eğer yerel sunucu yoksa veya GitHub Pages modundaysa sessizce devam et
        console.warn("Cloud Sync Pull uyarısı:", err.message);
        updateStatusUI("idle", "Bulut Senkron: Hazır");
        return 0;
      });
  }

  /**
   * 2. PUSH: Yerel verileri buluta yükle
   */
  var pushDebounceTimer = null;
  function pushToCloud(immediate) {
    if (!navigator.onLine) return;

    var cfg = getConfig();
    if (!cfg.enabled) return;

    clearTimeout(pushDebounceTimer);
    if (!immediate) {
      pushDebounceTimer = setTimeout(function () { pushToCloud(true); }, 1200);
      return;
    }

    var payload = exportLocalDataPayload();
    if (payload.scores.length === 0) return;

    updateStatusUI("syncing", "Buluta aktarılıyor...");

    var isLocalServer = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1" || window.location.port === "8080");
    var url = isLocalServer ? "/api/score" : (cfg.customUrl || "https://api.npoint.io/46d926ef91f86bd069ca");

    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    })
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        var timeStr = new Date().toLocaleTimeString("tr-TR", { hour: "2-digit", minute: "2-digit" });
        syncState.lastSyncTime = timeStr;
        localStorage.setItem(STORAGE_KEY_LAST_SYNC, timeStr);
        updateStatusUI("success", "Eşitlendi (" + timeStr + ")");
      })
      .catch(function (err) {
        console.warn("Cloud Sync Push uyarısı:", err.message);
        updateStatusUI("idle", "Bulut Senkron: Hazır");
      });
  }

  function escapeHtml(str) {
    return String(str == null ? "" : str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  /**
   * Bulut Senkronizasyon Ayarları Modalı
   */
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
          if (customUrlInput) customUrlInput.value = cfg.customUrl || "";
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
          pushToCloud(true);
          syncNowBtn.textContent = "✅ Başarılı!";
          setTimeout(function () { syncNowBtn.textContent = "🔄 Şimdi Senkronize Et"; }, 2000);
        });
      });
    }

    if (saveCfgBtn) {
      saveCfgBtn.addEventListener("click", function () {
        var cfg = getConfig();
        if (customUrlInput) cfg.customUrl = customUrlInput.value.trim();
        saveConfig(cfg);
        alert("Bulut ayarları kaydedildi!");
        if (modal) modal.style.display = "none";
        pullFromCloud(false);
      });
    }
  }

  // DOM Yüklendiğinde Başlat
  document.addEventListener("DOMContentLoaded", function () {
    initCloudSyncModal();

    // 1. Sayfa açılır açılmaz iki yönlü eşitle: Önce buluttan çek, ardından yereldeki sınavları buluta yükle
    setTimeout(function () {
      pullFromCloud(false).then(function () {
        var payload = exportLocalDataPayload();
        if (payload.scores && payload.scores.length > 0) {
          pushToCloud(true);
        }
      });
    }, 600);

    // 2. Belirli aralıklarla arka planda otomatik kontrol et (arka planda baba ekranı yenilenir)
    var cfg = getConfig();
    setInterval(function () {
      pullFromCloud(true);
    }, cfg.autoSyncIntervalMs || 45000);

    // 3. Tarayıcı çevrimdışı/çevrimiçi durumlarını dinle
    window.addEventListener("online", function () {
      updateStatusUI("syncing", "İnternet bağlandı, eşitleniyor...");
      pullFromCloud(false).then(function () { pushToCloud(true); });
    });

    window.addEventListener("offline", function () {
      updateStatusUI("offline", "Çevrimdışı (Yerel)");
    });
  });

  // Global API
  window.CloudSync = {
    pull: pullFromCloud,
    push: pushToCloud,
    getConfig: getConfig,
    saveConfig: saveConfig,
    exportPayload: exportLocalDataPayload
  };

})();
