---
name: noordhoff-book-pdf
description: >-
  Noordhoff dijital kitaplığındaki (apps.noordhoff.nl) ders kitaplarını, bölümlerini (hoofdstuk/thema)
  ve çalışma kitaplarını (leerwerkboek) otomatik tarayıp yüksek çözünürlüklü sayfa ekran görüntüleri alarak
  tek bir PDF belgesine dönüştürür.
---

# Noordhoff E-Kitap PDF İndirici & Sayfa Yakalayıcı

Bu skill, **Noordhoff** platformundaki tüm 3 HAVO ve ortaokul ders kitaplarını otomatik olarak taramak, bölümlerini seçmek, sayfaları tek tek gezerek 2x Retina kalitesinde ekran görüntüsü almak ve bunları aranabilir / okunabilir PDF dosyalarına dönüştürmek için kullanılır.

---

## 🛠️ Komut Satırı Kullanımı

Tüm işlemler için `tools/noordhoff_exporter.py` aracı kullanılır.

### 1. Kitaplıktaki Kitapları Listeleme
```bash
python3 tools/noordhoff_exporter.py --list
```
**Örnek Çıktı:**
```text
[ 0] Aardrijkskunde  | buiteNLand - 3 havo - Editie 5
[ 1] Biologie        | Nectar - FLEX - 2, 3 havo / vwo
[ 2] Duits           | Neue Kontakte - 3 havo
[ 7] Geschiedenis    | Geschiedeniswerkplaats - 3 havo
[ 8] Natuurkunde     | Overal Natuurkunde - 3 havo
[ 9] Nederlands      | Nieuw Nederlands - 3 havo
[10] Scheikunde      | Chemie Overal - 3 havo
[12] Wiskunde        | Moderne Wiskunde - 3 havo
```

### 2. Belirli Bir Kitabın Bölümlerini / E-Kitaplarını İnceleme
```bash
python3 tools/noordhoff_exporter.py --inspect <KITAP_INDEX>
```
Örnek:
```bash
python3 tools/noordhoff_exporter.py --inspect 0
```

### 3. Kitabı / Bölümü PDF Olarak İndirme
```bash
# İlk 50 sayfayı indirip PDF oluşturma:
python3 tools/noordhoff_exporter.py --export <KITAP_INDEX> --pages 50

# Belirli bir bölümü (örneğin Leerwerkboek veya Thema 1) belirterek PDF oluşturma:
python3 tools/noordhoff_exporter.py --export 0 --section "Leerwerkboek" --pages 100 --output "docs/books_pdf/Aardrijkskunde_3havo.pdf"
```

---

## ⚙️ Özellikler

1. **Otomatik SSO Girişi (Entree & Somtoday):**
   * Giriş bilgileri `~/.config/noordhoff_browser_profile` dizininde güvenli bir şekilde saklanır. Tekrar tekrar şifre girmeniz gerekmez.
2. **Yüksek Çözünürlük (2x Retina / HiDPI):**
   * Metinlerin ve grafiklerin baskı/okuma kalitesinde net olması için `device_scale_factor: 2` ve 4K ekran görüntüleme kullanılır.
3. **Otomatik Sayfa Çevirme & PDF Birleştirme:**
   * Sayfalar otomatik olarak sırayla gezilir, görseller optimize edilerek tek bir PDF dosyasında birleştirilir.
4. **Çıktı Dizini:**
   * PDF dosyaları varsayılan olarak `docs/books_pdf/` klasörüne kaydedilir.
