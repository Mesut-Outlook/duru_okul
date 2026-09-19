#!/usr/bin/env python3
"""
pdf_check.py — Noordhoff ekran-görüntüsü PDF'leri için kalite denetimi.

Her PDF sayfasını düşük çözünürlükte (varsayılan 50 dpi) render edip şu
bozukluklara bakar:
  BOS      tamamen boş / düz beyaz sayfa
  ISKELET  yükleniyor iskeleti (çok düşük kontrastlı açık gri bloklar, metin yok)
  MENU     sayfanın büyük kısmı boş, solda tam yükseklikte koyu dikey menü bandı
  ARAYUZ   kitap sayfası var ama reader arayüzü görünüyor (sol menü / sağ araç
           çubuğu / alt sayfa gezgini gri şeridi)
  KOPYA    bir önceki sayfanın neredeyse birebir aynısı
  OUTLIER  sayfa en-boy oranı belgenin geri kalanından belirgin farklı

Kullanım:
    python3 tools/pdf_check.py <pdf ya da klasör> [<pdf ya da klasör> ...]
    python3 tools/pdf_check.py --index                # inbox/2026-2027/**/*.pdf tara

Çıkış kodu: herhangi bir sorun bulunduysa 1, aksi halde 0.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import shutil
from pathlib import Path

try:
    from PIL import Image, ImageStat
except ImportError:
    print("PIL (Pillow) gerekli: pip install --user Pillow", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parent.parent
INBOX = REPO / "inbox" / "2026-2027"
BOOKS_JSON = REPO / "tools" / "noordhoff_books.json"
DEFAULT_SCRATCH = Path(os.environ.get(
    "PDF_CHECK_SCRATCH",
    "/tmp/claude-1000/-home-mesuto-Documents-PROJELER-duru-okul/"
    "d8a015b0-7770-43ff-bab9-828c5436b3e2/scratchpad/taskC/contact_sheets"
))

DPI = 50

# ---- eşikler (bkz. tools/README.md kalibrasyon notları — 2026-09-13) ----
BOS_STD_MAX = 1.0
BOS_MEAN_MIN = 250.0

ISKELET_MEAN_MIN = 235.0
ISKELET_DARKFRAC_MAX = 0.005  # eşik 180 gri seviyesinde ölçülür (bkz. classify_page)
ISKELET_STD_MIN = 0.15
ISKELET_STD_MAX = 30.0

MENU_NEARBLACK_MIN = 0.35
MENU_EDGE_MIN = 0.15  # top & bottom near-black fraction inside left band
MENU_CENTER_STD_FLAT = 6.0  # altında -> menü var ama arka plan boş (MENU değil ARAYUZ)

TOPMARGIN_MEAN_RANGE = (223.0, 251.0)
TOPMARGIN_STD_MAX = 10.0
BOTTOMBAR_MEAN_RANGE = (170.0, 251.0)
BOTTOMBAR_STD_RANGE = (7.0, 92.0)
RIGHTBAR_MEAN_RANGE = (200.0, 251.0)
RIGHTBAR_STD_MIN = 14.0

KOPYA_DIFF_MAX = 3.0  # 32x32 küçültülmüş gri farkın ortalama mutlak değeri

ASPECT_OUTLIER_TOL = 0.03


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def render_pdf(pdf_path, dpi=DPI):
    """PDF'in tüm sayfalarını pdftoppm ile geçici klasöre JPEG render eder.
    (page_index (1-based), PIL.Image) listesi döner."""
    tmp = tempfile.mkdtemp(prefix="pdfcheck_")
    prefix = os.path.join(tmp, "p")
    proc = run(["pdftoppm", "-jpeg", "-r", str(dpi), str(pdf_path), prefix])
    if proc.returncode != 0:
        shutil.rmtree(tmp, ignore_errors=True)
        raise RuntimeError(f"pdftoppm başarısız: {proc.stderr.strip()}")
    files = sorted(Path(tmp).glob("p-*.jpg"))
    if not files:
        # tek sayfalık PDF'lerde poppler -NN eki koymayabilir
        files = sorted(Path(tmp).glob("p*.jpg"))
    pages = []
    for f in files:
        # dosya adından sayfa no çıkar (p-01.jpg / p-001.jpg)
        digits = "".join(ch for ch in f.stem if ch.isdigit())
        idx = int(digits) if digits else len(pages) + 1
        pages.append((idx, Image.open(f).convert("RGB")))
    pages.sort(key=lambda t: t[0])
    shutil.rmtree(tmp, ignore_errors=True)
    return pages


def near_black_frac(arr_slice, thresh=65):
    import numpy as np
    return float(np.all(arr_slice < thresh, axis=2).mean())


def classify_page(im_rgb, prev_thumb):
    import numpy as np
    w, h = im_rgb.size
    gray = im_rgb.convert("L")
    arr_rgb = np.asarray(im_rgb).astype(int)
    ov = ImageStat.Stat(gray)
    mean, std = ov.mean[0], ov.stddev[0]
    hist = gray.histogram()
    total = w * h
    dark_frac = sum(hist[:120]) / total
    # gerçek metin/grafik en soluk anti-aliased kenarında bile 180'in altına
    # iner; iskelet (yükleniyor) blokları 245-253 bandında kalır ve bu eşiğin
    # altına hemen hiç düşmez -> ISKELET/gerçek-ama-seyrek-içerik ayrımı için.
    faint_frac = sum(hist[:180]) / total

    flags = []
    detail = {}

    # --- KOPYA (önceki sayfayla karşılaştırma) ---
    thumb = gray.resize((32, 32))
    thumb_arr = np.asarray(thumb).astype(float)
    is_kopya = False
    if prev_thumb is not None:
        diff = float(np.abs(thumb_arr - prev_thumb).mean())
        detail["kopya_diff"] = round(diff, 2)
        if diff < KOPYA_DIFF_MAX:
            is_kopya = True
            flags.append("KOPYA")

    # --- BOS ---
    if std < BOS_STD_MAX and mean > BOS_MEAN_MIN:
        flags.append("BOS")
        detail.update(mean=round(mean, 1), std=round(std, 2))
        return flags, detail, thumb_arr

    # --- sol menü bandı ---
    left = arr_rgb[:, : int(w * 0.18), :]
    lh = left.shape[0]
    nb_all = near_black_frac(left)
    nb_top = near_black_frac(left[: int(lh * 0.15)])
    nb_bot = near_black_frac(left[int(lh * 0.85):])
    menu_band = (nb_all > MENU_NEARBLACK_MIN and nb_top > MENU_EDGE_MIN
                 and nb_bot > MENU_EDGE_MIN)
    detail["menu_band_nb"] = round(nb_all, 2)

    # merkez bölge (menü hariç, sağ/alt kenar hariç) — gerçek içerik var mı?
    cx0 = int(w * 0.18) if menu_band else 0
    center = gray.crop((cx0, 0, int(w * 0.95), int(h * 0.94)))
    cst = ImageStat.Stat(center)
    detail["center_std"] = round(cst.stddev[0], 2)

    # --- ISKELET ---
    if (mean > ISKELET_MEAN_MIN and faint_frac < ISKELET_DARKFRAC_MAX
            and ISKELET_STD_MIN <= std <= ISKELET_STD_MAX and not menu_band):
        flags.append("ISKELET")
        detail.update(mean=round(mean, 1), std=round(std, 2), faint_frac=round(faint_frac, 4))
        return flags, detail, thumb_arr

    if menu_band:
        if cst.stddev[0] < MENU_CENTER_STD_FLAT:
            flags.append("MENU")
        else:
            flags.append("ARAYUZ")
    else:
        top = gray.crop((0, 0, w, int(h * 0.04)))
        bot = gray.crop((0, int(h * 0.94), w, h))
        rgt = gray.crop((int(w * 0.97), 0, w, h))
        tst, bst, rst = ImageStat.Stat(top), ImageStat.Stat(bot), ImageStat.Stat(rgt)
        top_flag = (TOPMARGIN_MEAN_RANGE[0] <= tst.mean[0] <= TOPMARGIN_MEAN_RANGE[1]
                    and tst.stddev[0] < TOPMARGIN_STD_MAX)
        bottom_flag = (BOTTOMBAR_MEAN_RANGE[0] <= bst.mean[0] <= BOTTOMBAR_MEAN_RANGE[1]
                       and BOTTOMBAR_STD_RANGE[0] <= bst.stddev[0] <= BOTTOMBAR_STD_RANGE[1])
        right_flag = (RIGHTBAR_MEAN_RANGE[0] <= rst.mean[0] <= RIGHTBAR_MEAN_RANGE[1]
                      and rst.stddev[0] > RIGHTBAR_STD_MIN)
        detail.update(top_mean=round(tst.mean[0], 1), top_std=round(tst.stddev[0], 2),
                      bottom_mean=round(bst.mean[0], 1), bottom_std=round(bst.stddev[0], 2),
                      right_mean=round(rst.mean[0], 1), right_std=round(rst.stddev[0], 2))
        if top_flag and (bottom_flag or right_flag):
            flags.append("ARAYUZ")

    detail.update(mean=round(mean, 1), std=round(std, 2))
    if not flags:
        flags = ["OK"] if not is_kopya else flags
    elif is_kopya and flags == ["KOPYA"]:
        pass
    return flags, detail, thumb_arr


def check_pdf(pdf_path, make_contact_sheet=True, scratch_dir=None):
    pdf_path = Path(pdf_path)
    pages = render_pdf(pdf_path)
    n = len(pages)
    results = []
    prev_thumb = None
    ratios = []
    thumbs_for_sheet = []
    for idx, im in pages:
        flags, detail, thumb = classify_page(im, prev_thumb)
        w, h = im.size
        ratios.append(w / h)
        results.append({"page": idx, "flags": flags, "detail": detail, "size": (w, h)})
        prev_thumb = thumb
        thumbs_for_sheet.append((idx, im.copy()))

    # aspect-ratio outlier
    if ratios:
        sorted_r = sorted(ratios)
        median_ratio = sorted_r[len(sorted_r) // 2]
        for r_item, r in zip(results, ratios):
            if median_ratio > 0 and abs(r - median_ratio) / median_ratio > ASPECT_OUTLIER_TOL:
                r_item["flags"].append("OUTLIER")

    bad_pages = [r for r in results if r["flags"] and r["flags"] != ["OK"]]

    contact_sheet_path = None
    if make_contact_sheet and thumbs_for_sheet:
        contact_sheet_path = save_contact_sheet(pdf_path, thumbs_for_sheet, results, scratch_dir)

    return {
        "path": str(pdf_path),
        "pages": n,
        "results": results,
        "bad_pages": bad_pages,
        "contact_sheet": contact_sheet_path,
    }


def save_contact_sheet(pdf_path, thumbs, results, scratch_dir=None):
    scratch_dir = Path(scratch_dir) if scratch_dir else DEFAULT_SCRATCH
    scratch_dir.mkdir(parents=True, exist_ok=True)
    cols = 6
    cell_w, cell_h = 220, 130
    n = len(thumbs)
    rows = (n + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), (30, 30, 30))
    from PIL import ImageDraw
    draw = ImageDraw.Draw(sheet)
    flag_by_page = {r["page"]: r["flags"] for r in results}
    for i, (idx, im) in enumerate(thumbs):
        r, c = divmod(i, cols)
        thumb = im.copy()
        thumb.thumbnail((cell_w - 10, cell_h - 22))
        x, y = c * cell_w + 5, r * cell_h + 5
        sheet.paste(thumb, (x, y))
        flags = flag_by_page.get(idx, [])
        label = f"{idx}"
        color = (255, 255, 255)
        if flags and flags != ["OK"]:
            label += " " + ",".join(flags)
            color = (255, 90, 90)
        draw.text((x, y + cell_h - 20), label, fill=color)
    out_path = scratch_dir / f"{pdf_path.stem}_contact.png"
    sheet.save(out_path)
    return str(out_path)


def find_pdfs(paths):
    pdfs = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            pdfs.extend(sorted(p.rglob("*.pdf")))
        elif p.suffix.lower() == ".pdf":
            pdfs.append(p)
    return pdfs


def print_report(check_result):
    p = check_result
    print(f"\n=== {p['path']} ({p['pages']} sayfa) ===")
    if not p["bad_pages"]:
        print("  ✅ Sorun yok.")
    else:
        print(f"  ❌ {len(p['bad_pages'])} sorunlu sayfa:")
        for r in p["bad_pages"]:
            print(f"    s.{r['page']:>3}  {','.join(r['flags']):<20} {r['detail']}")
    if p["contact_sheet"]:
        print(f"  🖼  kontak sayfası: {p['contact_sheet']}")


def load_books_config():
    if BOOKS_JSON.exists():
        try:
            return json.loads(BOOKS_JSON.read_text())
        except Exception:
            return {}
    return {}


def find_book_range_for_file(fname, books_cfg):
    """noordhoff_books.json içindeki chapters listelerinde dosya adına (output)
    göre kitap sayfa aralığını bul."""
    stem = Path(fname).stem
    chapters = [ch for cfg in books_cfg.values() if isinstance(cfg, dict)
                for ch in cfg.get("chapters", [])]
    # Eerst exacte bestandsnaam, dan "_<slug>" als ACHTERVOEGSEL. Een losse "slug in stem" koppelde
    # frans_h08_le-pont-examentraining aan de h04-slug "le-pont" (verkeerde paginareeks in PDF_INDEX).
    match = next((ch for ch in chapters if Path(ch.get("output", "")).stem == stem), None) \
        or next((ch for ch in chapters if ch.get("slug") and stem.endswith("_" + ch["slug"])), None)
    if not match:
        return ""
    boek = f"{match['book']}:" if match.get("book") else ""   # duits: deel A/B, paginanummers beginnen opnieuw
    return f"{boek}{match.get('start', '?')}-{match.get('end', '?')}"


def build_index():
    books_cfg = load_books_config()
    if not INBOX.exists():
        print(f"UYARI: {INBOX} yok, --index üretecek bir şey bulamadı.")
        return 0
    pdfs = sorted(INBOX.rglob("*.pdf"))
    lines = [
        "# PDF_INDEX — inbox/2026-2027 Noordhoff PDF denetimi",
        "",
        f"`tools/pdf_check.py --index` ile üretildi. {len(pdfs)} PDF taranmıştır.",
        "",
        "| vak | dosya | sayfa | kitap sayfa aralığı | durum | sorunlu sayfalar |",
        "|---|---|---|---|---|---|",
    ]
    any_bad = False
    onay_pad = REPO / "tools" / "pdf_check_onay.json"   # met het oog gecontroleerde vals-positieven
    onay = json.loads(onay_pad.read_text()) if onay_pad.exists() else {}
    for pdf in pdfs:
        vak = pdf.parent.name
        try:
            res = check_pdf(pdf, make_contact_sheet=False)
        except Exception as e:
            lines.append(f"| {vak} | {pdf.name} | ? | | ❌ | render hatası: {e} |")
            any_bad = True
            continue
        rng = find_book_range_for_file(pdf.name, books_cfg)
        ok_sayfalar = set(onay.get(pdf.name, {}).get("sayfalar", []))
        if res["bad_pages"] and all(r["page"] in ok_sayfalar for r in res["bad_pages"]):
            bad_desc = "gözle onaylı yanlış alarm: " + ", ".join(f"s.{r['page']}" for r in res["bad_pages"])
            durum = "✅"
        elif res["bad_pages"]:
            any_bad = True
            bad_desc = "; ".join(
                f"s.{r['page']}({','.join(r['flags'])})" for r in res["bad_pages"][:12]
            )
            if len(res["bad_pages"]) > 12:
                bad_desc += f" … (+{len(res['bad_pages']) - 12} daha)"
            durum = "❌"
        else:
            bad_desc = ""
            durum = "✅"
        lines.append(f"| {vak} | {pdf.name} | {res['pages']} | {rng} | {durum} | {bad_desc} |")

    INBOX.mkdir(parents=True, exist_ok=True)
    (INBOX / "PDF_INDEX.md").write_text("\n".join(lines) + "\n")
    print(f"Yazıldı: {INBOX / 'PDF_INDEX.md'} ({len(pdfs)} PDF, {'sorunlu var' if any_bad else 'hepsi temiz'})")
    return 1 if any_bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="PDF dosyaları veya klasörler")
    ap.add_argument("--index", action="store_true", help="inbox/2026-2027 taransın ve PDF_INDEX.md üretilsin")
    ap.add_argument("--no-contact-sheet", action="store_true")
    ap.add_argument("--scratch-dir", default=None)
    args = ap.parse_args()

    if args.index:
        sys.exit(build_index())

    if not args.paths:
        ap.print_help()
        sys.exit(2)

    pdfs = find_pdfs(args.paths)
    if not pdfs:
        print("PDF bulunamadı.")
        sys.exit(2)

    any_bad = False
    for pdf in pdfs:
        try:
            res = check_pdf(pdf, make_contact_sheet=not args.no_contact_sheet,
                             scratch_dir=args.scratch_dir)
        except Exception as e:
            print(f"\n=== {pdf} ===\n  ❌ render hatası: {e}")
            any_bad = True
            continue
        print_report(res)
        if res["bad_pages"]:
            any_bad = True

    sys.exit(1 if any_bad else 0)


if __name__ == "__main__":
    main()
