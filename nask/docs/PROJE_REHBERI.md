# 📘 Proje Rehberi (Mesut için)

Bu, Duru'nun NASK sitesini **sade Türkçe** anlatan hatırlatıcı dosyadır. Teknik ayrıntı
için bkz. [`CLAUDE.md`](../CLAUDE.md) ve [`SPEC.md`](../SPEC.md).

## Bu nedir?
Duru'nun (14, MAVO 2, Hollanda) fizik (NASK) sınavına hazırlanması için yapılmış,
**tamamen Hollandaca** bir web sitesi. İki konu var:
- **Hoofdstuk 4 — Snelheid** (hız): hız, m/s ↔ km/u, ortalama hız, reaksiyon/fren/durma mesafesi, grafikler.
- **Hoofdstuk 6 — Elektriciteit** (elektrik): gerilim/volt, akım/amper, iletken/yalıtkan, devre sembolleri, seri/paralel.

## Duru nasıl kullanır?
1. Bir konu kartına tıklar → önce **uitleg (konu anlatımı)** okur.
2. **"Start de oefentoets"** ile alıştırma sorularını çözer; her soruda **anında** doğru/yanlış + açıklama gelir.
3. **XP 💎** toplar, üst üste doğru yapınca **🔥 seri**, başarınca **🏅 rozet** kazanır.
4. Hazır hissedince ana sayfadaki **"📝 Oefentoetsen"** ile **süreli deneme sınavı** yapar:
   sayaç biter, sonunda **cijfer (1–10)** ve her soru için **"nasıl yapılır" açıklaması** görür.

## Nasıl açılır?
- **En kolay:** `Duru_NASK_Baslat.command` dosyasına çift tıkla → tarayıcıda açılır.
- **Başka bilgisayardan (aynı ağ):** sen launcher'ı açık tut, Duru tarayıcıya
  `http://<senin-mac-ip>:8123/index.html` yazsın. IP, launcher penceresinde görünür.
- Alternatif: `index.html`'i doğrudan tarayıcıda aç.

## Puanlar güvende mi?
Evet. İlerleme tarayıcıda saklanır:
- `duru_nask_v1` → XP/seri/rozet/quiz skorları
- `duru_nask_examens_v1` → sınav skorları (ayrı)

Bunlara sadece sitedeki **"Voortgang wissen"** düğmesi dokunur. Dosya eklemek/güncellemek silmez.
**Not:** İlerleme **cihaza+tarayıcıya özeldir** — Duru'nun bilgisayarındaki ilerleme orada kalır.

## İçerik nasıl üretildi?
Kitabın taranmış PDF'leri ve okuldan alınan "Oefentoets H4" fotoğrafları okundu; içerik
(konu + sorular + sınavlar) Hollandaca üretildi. Görseller telif sorunu olmasın diye
fotoğraf yerine **inline SVG** ile yeniden çizildi.

## Yeni soru / konu / sınav eklemek istersen
Claude'a şunu söylemen yeter: *"Duru_Nask projesine ... ekle"*. Teknik kurallar `CLAUDE.md`
ve `SPEC.md` içinde; Claude o sözleşmelere uyarak ekler ve `index.html`'e script satırını koyar.

## Sık sorunlar
- **Sayfa boş açıldı / sorular gelmedi:** `index.html`'i `file://` yerine launcher (sunucu) ile aç.
- **Başka cihaz erişemiyor:** aynı Wi-Fi'da olun; macOS güvenlik duvarı Python'a "İzin Ver" desin;
  IP değişmişse launcher penceresindeki güncel adresi kullan.
- **Sınav puanı görünüyor ama XP artmıyor:** normal — sınavlar XP vermez, ayrı sayılır.
