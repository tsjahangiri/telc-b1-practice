"""Per-page extraction records for a 10-page batch.
usage: python3 tools/pages.py BATCHNO   -> extraction/batches/batch_NN.json (+ _report.md)
Visual verification notes come from extraction/corrections/page_notes.json:
  {"12": {"verified": true, "method": "full|glance", "note": "...", "uncertain": [...]}}
"""
import pymupdf as fitz, json, re, os, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
from lines import lines, d
import draft

ARABIC = re.compile(r'[؀-ۿ]')
papers = json.load(open("extraction/papers_index.json"))
SPEAKING = [(169, 170), (198, 222), (251, 252), (266, 270), (299, 303), (326, 330), (344, 355), (395, 396),
            (410, 411), (425, 426), (440, 441), (455, 492)]


def paper_of(p):
    for x in papers:
        if x["first"] <= p <= x["last"]:
            return x["paper"]
    for a, b in SPEAKING:
        if a <= p <= b:
            return "SPEAKING"
    return "OTHER"


def ocr_text(p):
    f = f"extraction/ocr/p{p:03d}.txt"
    if not os.path.exists(f):
        return ""
    return "\n".join(l.split("\t", 1)[1] for l in open(f).read().splitlines() if "\t" in l)


def words(s):
    s = unicodedata.normalize("NFC", s)
    return [w.lower() for w in re.findall(r"[A-Za-zÄÖÜäöüß]{4,}", s)]


def section_kind(p, text):
    s = draft.section_of(p)
    if s != '?':
        return s
    if paper_of(p) == "SPEAKING":
        return "MUENDLICH"
    if re.search(r'geschrieben|erhalten|bekommen|Brief|E-Mail', text):
        return "SCHREIBEN"
    return "?"


def record(p):
    page = d[p - 1]
    rows = lines(p)
    arabic = [r[3].strip() for r in rows if ARABIC.search(r[3])]
    text = "\n".join(r[3].rstrip() for r in rows if not ARABIC.search(r[3]))
    ocr = ocr_text(p)
    cov = sum((fitz.Rect(im['bbox']) & page.rect).get_area() for im in page.get_image_info()) / page.rect.get_area()
    tw, ow = words(text), words(ocr)
    tset, oset = set(tw), set(ow)
    agree = round(len(tset & oset) / len(tset), 3) if tset else None
    only_ocr = sorted(oset - tset)
    image_only = len(tw) < 15 and len(ow) > 30
    rec = {
        "page": p, "paper": paper_of(p), "section": section_kind(p, text + ocr),
        "text_source": "ocr" if image_only else "text_layer",
        "text": ocr if image_only else text,
        "arabic_labels_excluded": arabic,
        "images": {"count": len(page.get_images()), "page_coverage": round(cov, 2)},
        "crosscheck": {"textlayer_words_found_in_ocr": agree,
                       "ocr_words_missing_from_textlayer": len(only_ocr),
                       "sample_missing": only_ocr[:25]},
        "extracted": True,
    }
    return rec


if __name__ == "__main__":
    b = int(sys.argv[1])
    a, e = (b - 1) * 10 + 1, min(b * 10, len(d))
    notes = json.load(open("extraction/corrections/page_notes.json")) if os.path.exists("extraction/corrections/page_notes.json") else {}
    recs = []
    for p in range(a, e + 1):
        r = record(p)
        n = notes.get(str(p), {})
        r["verified"] = bool(n.get("verified"))
        r["verification_method"] = n.get("method")
        r["verification_note"] = n.get("note", "")
        r["uncertain"] = n.get("uncertain", [])
        recs.append(r)
    os.makedirs("extraction/batches", exist_ok=True)
    out = f"extraction/batches/batch_{b:02d}.json"
    json.dump({"batch": b, "pages": [a, e], "records": recs}, open(out, "w"), ensure_ascii=False, indent=1)
    json.load(open(out))  # reopen check
    rep = [f"# Batch {b:02d} — pages {a}–{e}", "",
           "| Page | Paper | Section | Source | Imgs/cov | Text↔OCR agree | Verified | Note |", "|---|---|---|---|---|---|---|---|"]
    for r in recs:
        rep.append(f"| {r['page']} | {r['paper']} | {r['section']} | {r['text_source']} | {r['images']['count']}/{r['images']['page_coverage']} | "
                   f"{r['crosscheck']['textlayer_words_found_in_ocr']} | {'yes (' + str(r['verification_method']) + ')' if r['verified'] else 'NO'} | {r['verification_note']} |")
    unc = [(r['page'], u) for r in recs for u in r['uncertain']]
    rep += ["", "## Uncertain content", ""] + ([f"- p{p}: {u}" for p, u in unc] or ["- none"])
    open(f"extraction/batches/batch_{b:02d}_report.md", "w").write("\n".join(rep) + "\n")
    print("\n".join(rep))
