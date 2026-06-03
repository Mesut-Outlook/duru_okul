#!/bin/bash
# Duru_Okul — Icerik guncelleme
# Uc dersin (NASK / Economie / Begrijpend Lezen) en son icerigini GitHub'dan ceker
# ve ana hub repo'sunu yedek olarak gunceller. Cift tikla calistir.

# Bu scriptin bulundugu dizine gec (tiklayinca dogru klasorde calissin)
cd "$(dirname "$0")" || exit 1

echo "================================================"
echo "  Duru_Okul — Icerik guncelleniyor..."
echo "================================================"
echo ""

# 1) Submodule'lari (uc ders) en son origin/main icerigine guncelle
echo "→ Dersler GitHub'dan cekiliyor (NASK, Economie, Begrijpend Lezen)..."
git submodule update --init --remote --merge

echo ""
echo "→ Guncel durum:"
git submodule status

# 2) Degisiklik var mi? Varsa hub repo'sunu yedek olarak commit + push et
if [ -n "$(git status --porcelain)" ]; then
  echo ""
  echo "→ Yeni icerik bulundu, GitHub yedegine kaydediliyor..."
  git add -A
  git commit -m "Submodule icerigini guncelle ($(date '+%Y-%m-%d %H:%M'))"
  # Push basarisiz olursa (internet yok vs.) script cokmesin
  if git push origin main 2>/dev/null; then
    echo "  ✓ GitHub yedegi guncellendi."
  else
    echo "  ⚠ Push yapilamadi (internet yok mu?). Yerel kayit tamam, sonra push edebilirsin."
  fi
else
  echo ""
  echo "  ✓ Her sey zaten guncel — yeni icerik yok."
fi

echo ""
echo "================================================"
echo "  Bitti! Siteyi acmak icin: Duru_Okul_Baslat.command"
echo "================================================"
echo ""
# Pencere hemen kapanmasin
read -n 1 -s -r -p "Kapatmak icin bir tusa bas..."
echo ""
