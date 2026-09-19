#!/usr/bin/env python3
"""
noordhoff_export.py — TEK, sağlam Noordhoff e-kitap → PDF dışa aktarıcı.

Şu betiklerin yerini alır (login akışı + ağ-yakalama stratejisi buradan tek
elden yönetilir): export_frans_ebook.py, export_frans_units.py,
export_duits_units.py, export_all_engels_chapters.py,
export_aardrijkskunde_h1.py, noordhoff_exporter.py.

Strateji: Noordhoff okuyucusu her `?page=N` gezinmesinde, o anki spread'in
(ve komşu sayfaların, ön-yükleme için) TAM ÇÖZÜNÜRLÜKLÜ, arayüzsüz PNG'sini
`/api/ebook-assets/production/main/<hash>_<tag>_<sayfa>_<ölçek>.png` adresinden
indirir. Bu görüntüleri `page.on('response', ...)` ile ağdan yakalayıp
doğrudan kaydediyoruz — DOM ekran görüntüsü YOK, reader arayüzü/menü/araç
çubuğu hiç görünmüyor, çözünürlük ekran görüntüsünden çok daha yüksek
(2381×3367 @ ölçek 4, ekran görüntüsünün ~2 katı DPI'ı).

Kullanım:
    python3 tools/noordhoff_export.py --vak frans                 # tüm bölümler
    python3 tools/noordhoff_export.py --vak frans --hoofdstuk 1    # tek bölüm
    python3 tools/noordhoff_export.py --vak frans --label "Unité 2"
    python3 tools/noordhoff_export.py --discover aardrijkskunde     # course/ebook id bul

Config: tools/noordhoff_books.json (vak -> course_id/ebook_id/books + chapters).
Çıktı: inbox/2026-2027/<vak>/<output>.pdf (kanonik ad config'ten gelir).

Oturum: kalıcı profil ~/.config/noordhoff_browser_profile. Aynı anda tek
Playwright süreci çalışabilir (profil kilidi).
"""
import argparse
import io
import json
import os
import re
import sys
import time
from pathlib import Path

from PIL import Image, ImageStat
from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent
BOOKS_JSON = REPO / "tools" / "noordhoff_books.json"
INBOX = REPO / "inbox" / "2026-2027"
USER_DATA_DIR = os.path.expanduser("~/.config/noordhoff_browser_profile")
BOOKSHELF_URL = "https://apps.noordhoff.nl/my/nl/bookshelf"

ASSET_RE = re.compile(r"/api/ebook-assets/production/main/[^/]+_(\d+)_([0-9.]+)\.png(?:\?|$)")

JPEG_QUALITY = 88
GAP_FILL_ROUNDS = 3
MAX_CHAPTER_RETRIES = 2


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------- login ----
def ensure_login(page, timeout_s=90):
    """Doğrulanmış SSO akışı
    (Entree -> Somtoday 'önceki seçim' -> sessiz Azure SSO).
    """
    start = time.time()
    time.sleep(1.0)
    while time.time() - start < timeout_s:
        url = page.url
        try:
            if page.locator("[data-testid='new-product-card']").count() > 0:
                return True
        except Exception:
            pass

        if ("bookshelf" in url or "se/content" in url) and "identity" not in url \
                and "entree" not in url and "somtoday" not in url:
            try:
                page.wait_for_selector("[data-testid='new-product-card']", timeout=4000)
                return True
            except Exception:
                pass
        try:
            if "identity" in url:
                b = page.locator("text='via Entree'")
                if b.count() > 0 and b.first.is_visible():
                    b.first.click(timeout=2000)
        except Exception:
            pass
        try:
            if "entree" in page.url:
                b = page.locator(".wayf__previousSelection, .previousSelection__item, .idp__submit")
                if b.count() > 0 and b.first.is_visible():
                    b.first.click(force=True, timeout=2000)
        except Exception:
            pass
        try:
            if "somtoday" in page.url:
                b = page.locator("text='Caland Lyceum Azure'")
                if b.count() > 0 and b.first.is_visible():
                    b.first.click(timeout=2000)
        except Exception:
            pass
        if "microsoftonline" in page.url:
            log("  UYARI: Microsoft Azure şifre ekranı açık — kullanıcı girişi gerekiyor.")
        time.sleep(1.5)
    return False


def open_browser():
    pw = sync_playwright().start()
    ctx = pw.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,  # headless'ta SSO sessiz yenilenmiyor (doğrulandı 2026-09-13)
        viewport={"width": 1440, "height": 960},
        args=["--no-sandbox"],
    )
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.goto(BOOKSHELF_URL, timeout=30000)
    if not ensure_login(page):
        raise RuntimeError("Oturum açılamadı (SSO 90 sn içinde tamamlanmadı) — "
                            "kullanıcının elle giriş yapması gerekiyor.")
    return pw, ctx, page


# --------------------------------------------------------------- capture ---
def reader_url(course_id, ebook_id, page_num):
    return f"https://apps.noordhoff.nl/se/content/book/{course_id}/ebook/{ebook_id}?page={page_num}"


def is_bad_png(png_bytes):
    try:
        im = Image.open(io.BytesIO(png_bytes)).convert("L")
    except Exception:
        return "BOZUK"
    w, h = im.size
    if w < 300 or h < 300:
        return "KUCUK"
    st = ImageStat.Stat(im)
    if st.stddev[0] < 1.0 and st.mean[0] > 250:
        return "BOS"
    return None


def capture_chapter(page, course_id, ebook_id, start, end):
    """Belirtilen kitap sayfa aralığındaki tüm sayfaların asset URL'lerini
    ağdan yakalar, sonra her birini page.request.get() ile AYRI bir turda
    indirir. {sayfa_no: (ölçek, png_bytes)} döner.

    ⚠️ Neden iki aşamalı: `page.on('response', ...)` içinde doğrudan
    `resp.body()` çağırmak, art arda hızlı `page.goto()` yapıldığında
    "Protocol error: No resource with given identifier found" ile başarısız
    oluyor — CDP, yeni gezinme başlar başlamaz önceki kaynakların tampon
    belleğini boşaltıyor (2026-09-13 canlı testte doğrulandı: art arda
    gezinmede body() çağrıları %100 bu hatayla düşüyordu). URL'yi olay
    anında saklayıp gövdeyi sonradan `page.request.get(url)` ile (aynı
    tarayıcı bağlamının çerezleriyle) ayrıca indirmek bu yarışı ortadan
    kaldırıyor ve güvenilir çalışıyor."""
    urls = {}  # sayfa_no -> (ölçek, url)

    def on_response(resp):
        m = ASSET_RE.search(resp.url)
        if not m:
            return
        pnum, scale = int(m.group(1)), float(m.group(2))
        if scale < 1.0:
            return
        if pnum < start or pnum > end:
            return
        prev = urls.get(pnum)
        if prev is not None and prev[0] >= scale:
            return
        urls[pnum] = (scale, resp.url)

    def wait_for(pnums, max_wait=9.0):
        deadline = time.time() + max_wait
        while time.time() < deadline:
            if all(n in urls for n in pnums):
                return
            time.sleep(0.3)

    page.on("response", on_response)
    try:
        for t in range(start, end + 1, 2):
            page.goto(reader_url(course_id, ebook_id, t), timeout=30000)
            pair = [n for n in (t, t + 1) if start <= n <= end]
            wait_for(pair)

        for round_ in range(GAP_FILL_ROUNDS):
            missing = [n for n in range(start, end + 1) if n not in urls]
            if not missing:
                break
            preview = missing[:10]
            log(f"    URL eksik ({len(missing)}): {preview}"
                f"{' ...' if len(missing) > 10 else ''} — tur {round_ + 1}/{GAP_FILL_ROUNDS}")
            for n in missing:
                if n in urls:
                    continue
                page.goto(reader_url(course_id, ebook_id, n), timeout=30000)
                wait_for([n], max_wait=11.0)
    finally:
        page.remove_listener("response", on_response)

    # --- ikinci aşama: gövdeleri indir ---
    collected = {}
    for pnum, (scale, url) in urls.items():
        body = None
        for attempt in range(3):
            try:
                r = page.request.get(url, timeout=20000)
                if r.ok:
                    body = r.body()
                    break
            except Exception:
                pass
            time.sleep(1.0)
        if body is None or is_bad_png(body):
            continue
        collected[pnum] = (scale, body)

    return collected


# ----------------------------------------------------------------- pdf -----
def build_pdf(collected, start, end, out_path, title):
    missing = []
    jpeg_bufs = []  # (buf, im) tuples tutulur ki save sırasında GC'ye gitmesin
    for n in range(start, end + 1):
        if n not in collected:
            missing.append(n)
            continue
        _scale, body = collected[n]
        im = Image.open(io.BytesIO(body)).convert("RGB")
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=JPEG_QUALITY)
        buf.seek(0)
        jpg_im = Image.open(buf)
        jpg_im.load()
        jpeg_bufs.append(jpg_im)

    if not jpeg_bufs:
        return missing, None

    out_path.parent.mkdir(parents=True, exist_ok=True)
    jpeg_bufs[0].save(
        out_path, "PDF", save_all=True, append_images=jpeg_bufs[1:],
        resolution=300.0, title=title,
    )
    return missing, out_path


# ------------------------------------------------------------ orchestrate --
def load_config():
    return json.loads(BOOKS_JSON.read_text())


def resolve_ebook_id(vak_cfg, chapter):
    if "ebook_id" in vak_cfg:
        return vak_cfg["ebook_id"]
    book_key = chapter.get("book")
    return vak_cfg["books"][book_key]


def export_chapter(page, vak, vak_cfg, chapter):
    course_id = vak_cfg["course_id"]
    ebook_id = resolve_ebook_id(vak_cfg, chapter)
    start, end = chapter["start"], chapter["end"]
    label = chapter["label"]
    titel = chapter["titel"]
    out_path = INBOX / vak / chapter["output"]

    vak_titles = {"frans": "Frans", "duits": "Duits", "engels": "Engels",
                  "aardrijkskunde": "Aardrijkskunde", "nederlands": "Nederlands",
                  "wiskunde": "Wiskunde"}
    pdf_title = f"{vak_titles.get(vak, vak)} · {label} · {titel}"

    log(f"\n--- {vak} / {label} ({titel}) — kitap sayfa {start}-{end} ---")

    # Ensure reader session is initialized if not yet active
    try:
        reader_init_url = reader_url(course_id, ebook_id, start)
        page.goto(reader_init_url, timeout=30000)
        page.wait_for_selector("img[src*='ebook-assets']", timeout=20000)
        time.sleep(2)
    except Exception as e:
        log(f"    (Reader ön-yükleme uyarısı: {e})")

    attempt = 0
    while True:
        attempt += 1
        collected = capture_chapter(page, course_id, ebook_id, start, end)
        missing, saved = build_pdf(collected, start, end, out_path, pdf_title)
        got = (end - start + 1) - len(missing)
        log(f"    {got}/{end - start + 1} sayfa yakalandı"
            + (f", eksik: {missing}" if missing else ""))
        if not missing:
            log(f"    KAYDEDİLDİ -> {out_path}")
            return {"chapter": chapter, "output": str(out_path), "missing": [],
                     "status": "ok"}
        if attempt > MAX_CHAPTER_RETRIES:
            if saved:
                log(f"    UYARI: {len(missing)} sayfa eksik kaldı ama PDF yine de yazıldı -> {out_path}")
            else:
                log("    HATA: hiç sayfa yakalanamadı, PDF yazılmadı.")
            return {"chapter": chapter, "output": str(out_path) if saved else None,
                     "missing": missing, "status": "eksik" if saved else "basarisiz"}
        log(f"    tekrar deneniyor (deneme {attempt + 1}/{MAX_CHAPTER_RETRIES + 1})...")


def cmd_discover(vak):
    """Bookshelf'teki kart(lar)ı tıklayıp course_id/ebook_id'yi URL'den çıkarır."""
    pw, ctx, page = open_browser()
    try:
        page.wait_for_selector("[data-testid='new-product-card']", timeout=20000)
        time.sleep(1.5)
        cards = page.locator("[data-testid='new-product-card']").all()
        log(f"{len(cards)} kitap kartı bulundu:")
        matches = []
        for i, c in enumerate(cards):
            txt = c.inner_text().replace("\n", " | ")
            log(f"  [{i}] {txt}")
            if vak.lower()[:4] in txt.lower() or "aardrijk" in txt.lower() and "aardrijk" in vak.lower():
                matches.append((i, c, txt))
        if not matches:
            log(f"UYARI: '{vak}' için otomatik eşleşme bulunamadı, yukarıdaki listeden elle seç.")
            return
        idx, card, txt = matches[0]
        log(f"\nSeçilen kart [{idx}]: {txt}")
        card.click()
        time.sleep(5)
        m = re.search(r"/book/([0-9a-f-]{36})/ebook/([0-9a-f-]{36})", page.url)
        if m:
            log(f"\nBULUNDU:\n  course_id = {m.group(1)}\n  ebook_id  = {m.group(2)}\n  url = {page.url}")
        else:
            log(f"UYARI: URL'de course/ebook id deseni bulunamadı: {page.url}")
    finally:
        ctx.close()
        pw.stop()


def cmd_export(vak, hoofdstuk=None, label=None, only_output=None):
    cfg = load_config()
    if vak not in cfg:
        log(f"HATA: '{vak}' tools/noordhoff_books.json içinde tanımlı değil.")
        sys.exit(2)
    vak_cfg = cfg[vak]
    chapters = vak_cfg.get("chapters", [])
    if not chapters:
        log(f"HATA: '{vak}' için henüz bölüm tanımlı değil (course_id/ebook_id keşfedilmemiş olabilir).")
        sys.exit(2)

    selected = chapters
    if hoofdstuk is not None:
        selected = [c for c in selected if c.get("hoofdstuk") == hoofdstuk]
    if label:
        selected = [c for c in selected if label.lower() in c["label"].lower()]
    if only_output:
        selected = [c for c in selected if c["output"] == only_output]
    if not selected:
        log("HATA: filtreye uyan bölüm yok.")
        sys.exit(2)

    pw, ctx, page = open_browser()
    results = []
    try:
        for chapter in selected:
            res = export_chapter(page, vak, vak_cfg, chapter)
            results.append(res)
    finally:
        ctx.close()
        pw.stop()

    log("\n=== ÖZET ===")
    for r in results:
        status_icon = {"ok": "OK", "eksik": "EKSIK", "basarisiz": "BASARISIZ"}[r["status"]]
        log(f"  [{status_icon}] {r['chapter']['label']} ({r['chapter']['titel']}) -> {r['output']}")
        if r["missing"]:
            log(f"          eksik sayfalar: {r['missing']}")
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vak", help="frans | duits | engels | aardrijkskunde | nederlands")
    ap.add_argument("--hoofdstuk", type=int, default=None, help="Yalnız bu hoofdstuk numarası")
    ap.add_argument("--label", default=None, help="Label'da geçen metne göre filtre (örn. 'Unité 2')")
    ap.add_argument("--output", default=None, help="Yalnız bu çıktı dosya adını üret")
    ap.add_argument("--discover", metavar="VAK", help="Bookshelf'ten course_id/ebook_id keşfet (yazmaz, yalnız yazdırır)")
    args = ap.parse_args()

    if args.discover:
        cmd_discover(args.discover)
        return

    if not args.vak:
        ap.print_help()
        sys.exit(2)

    cmd_export(args.vak, hoofdstuk=args.hoofdstuk, label=args.label, only_output=args.output)


if __name__ == "__main__":
    main()
