# ENGINE_SPEC.md — DURU-motoru veri sözleşmesi (TEK DOĞRU KAYNAK)

> Bu dosya, tüm DURU-engine derslerinin (nask, economi, wiskunde, spelling, geschiedenis
> ve gelecekteki HAVO 3 dersleri) paylaştığı **veri sözleşmesinin kanonik kaynağıdır**.
> Her dersin kendi `SPEC.md`'i bu dosyaya işaret eder; sözleşme burada değişir, orada değil.
>
> **Dil kuralı:** Tüm öğrenci-içeriği (theorie, sorular, uitleg, geri bildirim) **Flamancadır**.
> Ondalık ayraç metinlerde **virgül** (13,4 m/s · € 21,50). Kod tanımlayıcıları İngilizce/Flamanca.

## Teknoloji sınırları (değişmez)
- **Saf HTML/CSS/JS. Build yok, bağımlılık yok, framework yok.** ES5/ES6.
- **ES module KULLANMA** — `file://` üzerinde CORS'tan patlar. Bunun yerine global `window.DURU`
  nesnesi + sıralı `<script>` yüklemesi.
- Her veri dosyası **tek bir `register`/`registerExamen` çağrısı** içerir; import/export yok.

## Script yükleme sırası (her `index.html`) — BOZMA
`register`/`registerExamen` fonksiyonları, data dosyaları çalışmadan ÖNCE var olmalı:
1. `js/bootstrap.js` → `window.DURU`, `DURU.register`, `DURU.hoofdstukken`, `DURU.onderwerpen`
2. `js/exams.js`    → `DURU.registerExamen`, `DURU.examens`, sınav motoru
3. `js/data/examen_*.js` (proeftoetsen)
4. `js/data/h*_*.js` / `sp_*.js` (onderwerpen)
5. `js/engine.js`   → **EN SON**; `DOMContentLoaded`'da `renderHome()`

## Sözleşme 1 — Onderwerp (oefenquiz) · `DURU.register({...})`
```js
DURU.register({
  id: "h4-1-begrippen",        // KARARLI benzersiz id; oefen-ilerleme anahtarı. Değiştirme.
  hoofdstuk: 4,                // number — konuları gruplar (DURU.onderwerpenVan(nr) filtreler)
  paragraaf: "4.1",            // string
  titel: "Begrippen 4.1 — ...",
  korteUitleg: "Anasayfa kartı için 1 cümle.",
  icoon: "🔑",                 // tek emoji
  theorie: "<p>...HTML string...</p>",   // konu anlatımı (CSS sınıfları aşağıda)
  vragen: [ /* soru nesneleri */ ]
});
```

## Sözleşme 2 — Proeftoets (sınav) · `DURU.registerExamen({...})`
```js
DURU.registerExamen({
  id: "ex-geschiedenis-66",    // KARARLI — kayıtlı skor geçmişinin anahtarı. ASLA yeniden adlandırma.
  titel: "Proeftoets — ...",
  vak: "Geschiedenis · H4 (4.1)",
  icoon: "⚔️",
  duurMin: 20,                 // geri sayım dakikası
  vragen: [ /* soru nesneleri */ ]
});
```

## Soru tipleri
Oefen soruları ek `niveau` (zorluk 1–3) taşır; sınav soruları taşımaz. Her soruya opsiyonel
`figuur:"<svg ...>"` eklenebilir (inline SVG, `width="100%"` + `viewBox`, ~440px genişlik).

| type | nerede | `antwoord` | notlar |
|---|---|---|---|
| `mc` | oefen + sınav | 0-tabanlı **index** | `opties:[...]` şart |
| `waaronwaar` | oefen + sınav | **boolean** | doğru/yanlış |
| `invoer` | sadece oefen | **string** | `"|"` = kabul edilen yazımlar; opsiyonel `eenheid`, `tolerantie`, `figuur` |
| `invul` | sadece sınav | **string** | `"|"` = kabul edilen yazımlar |
| `open` | sadece sınav | — | `sleutelwoorden:["a/alt","b"]`, `minTreffers:1`, `modelantwoord` |

```js
{ type:"mc", niveau:1, vraag:"...", opties:["A","B","C","D"], antwoord:0, uitleg:"...", hint:"..." }
{ type:"waaronwaar", vraag:"...", antwoord:true, uitleg:"Waar. ..." }
{ type:"invoer", niveau:1, vraag:"...", antwoord:"wereldoorlog|een wereldoorlog", uitleg:"..." }
{ type:"invul", vraag:"...", antwoord:"mobilisatie|mobiliseren", uitleg:"..." }
{ type:"open", vraag:"...", sleutelwoorden:["gemeente/de gemeente","rijk"], minTreffers:1,
               modelantwoord:"...", uitleg:"..." }
```
**Cevap denetimi:** `invoer`/`invul` önce sayısal karşılaştırılır (`parseFloat`, `tolerantie` ya da
`max(|beklenen|*0.02, 0.01)`), sayısal değilse `"|"` ile bölünüp normalize edilmiş tam eşleşme aranır.
`open`: tüm sleutelwoorden bulunursa "goed", `>= minTreffers` "deels" (yine 1 puan), yoksa "fout".
`/` bir sleutel için alternatif yazımlardır.

## theorie HTML — mevcut CSS sınıflarını kullan (yeni sınıf uydurma)
`<h3>/<h4>`, `formule-box` (tanım/anahtar kavram kutusu), `voorbeeld`/`vb-kop`/`stap` (çözümlü örnek),
`info-box` (+ `let-op` / `tip` varyantları), `table class="nask"`, `figure class="bron"`.
Görseller tercihen **inline SVG**.

## localStorage anahtarları — **okul yılı = birinci sınıf boyut** (KARIŞTIRMA)
Puanlama/istatistik **eğitim yılına göre** bölümlenir. Anahtar biçimi:
- Oefen-ilerleme: `duru_<jaarcode>_<slug>_v1` → `{ xp, streak, badges{}, beste{id:pct}, gedaan{}, pogingen{id:count}, titels{id:titel} }`
- Sınav skorları: `duru_<jaarcode>_<slug>_examens_v1` → `{ history:[ { examId, ... } ] }`
- İkisi ayrı; sınav motoru oefen-XP'ye **dokunmaz**. `_v1` / `_examens_v1` son ekleri **yapısal işaret**
  (sync + `restoreScores` + `leesVakData` bunlara göre ayırır) — **asla değiştirme**.

**`<jaarcode>` = okul yılının iki yılının son iki hanesi:** `2025-2026 → 2526`, `2026-2027 → 2627`.
Örn. HAVO 3 (2026-2027) ekonomi → `duru_2627_economi_v1` / `duru_2627_economi_examens_v1`.
Yeni ders kurarken `engine.js`/`exams.js` başındaki `SLEUTEL`/`EX_SLEUTEL`'i bu biçimde ayarla.

**Aynı ders, farklı yıl, ayrı istatistik:** Ders adı yıllar boyu aynı kalabilir ama her yıl farklı
konu/içerik → **ayrı anahtar → ayrı XP/rozet/cijfer-ortalaması**. Yeni yıl **sıfırdan** başlar;
geçen yıl arşivde salt-okunur olarak durur (skorları çalışmaya devam eder).

**Legacy istisna (DOKUNMA):** 2025-2026 (MAVO 2) dersleri kurulduğunda yıl-kodu yoktu; anahtarları
**yılsız** (`duru_nask_v1`, `duru_economi_v1`, …, `begrijpend_lezen_history`). MAVO 2 donmuştur →
bu anahtarlar asla değişmez. **Göç YAPMA.** Bunun yerine dashboard sabit bir **KEY→YIL haritasıyla**
tüm yılsız legacy anahtarları `2025-2026`'ya etiketler. Yalnızca **yeni** yıllar `duru_<jaarcode>_*`
biçimini kullanır. (Bkz. `js/dashboard.js` → `VAK_REGISTER`.)

## Yeni ders (site) oluşturma — özet
`bootstrap.js` (+ `DURU.hoofdstukken`/intro düzenle), `exams.js`, `engine.js` (`SLEUTEL`/`EX_SLEUTEL`
= yeni slug), `css/style.css`, `index.html` (başlık + sıralı `<script>` listesi) kopyala →
`js/data/*.js` yaz → her birini `index.html`'e doğru grupta ekle (exams grubu önce, engine.js en son).

## Ekledikten sonra doğrulama (zorunlu)
`node` ile `DURU.register`/`registerExamen` stub'layıp data dosyalarını `eval` ederek söz dizimi +
alan kontrolü yap (bkz. `docs/PIPELINE.md`). `index.html`'de `?v=` cache sürümünü gerektiğinde bump'la.
