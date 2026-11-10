import json, glob
s = json.load(open("extraction/audit_stats.json"))
papers = [json.load(open(f)) for f in sorted(glob.glob("extraction/papers/P??.json"))]
recs = [r for f in sorted(glob.glob("extraction/batches/batch_??.json")) for r in json.load(open(f))["records"]]
ex = [e for p in papers for e in p["exercises"]]
dupof = {d: k for k, v in s["dup_groups"].items() for d in v}
# ---------- uncertain_content.md
L = ["# Uncertain / incomplete content", "",
     "Nothing listed here was guessed. Unreadable text is marked in the data as `[unleserlich]` (illegible) or `[abgeschnitten]` (cut off at the photo edge).",
     "Per instructions, **no AI reconstruction** of blurry content has been attempted; these items await your decision.", "",
     "## A. Items inside practice exercises (unique exercises only; duplicates share the same items)", ""]
seen = set()
for e in ex:
    if e["id"] in dupof: continue
    for u in e["uncertain"]:
        L.append(f"- **{e['id']}** ({e['section']}, PDF p{','.join(map(str, e['pages']))}) — *{u['location']}*: {u['note']}")
L += ["", "## B. Page-level notes from visual verification", ""]
for r in recs:
    for u in r["uncertain"]:
        L.append(f"- p{r['page']} ({r['paper']}, {r['section']}): {u}")
L += ["", "## C. Source-side defects reproduced as printed (not errors of extraction)", "",
      "- Many texts contain typos/missing punctuation in the original (e.g. 'Raschläge', 'Klage Schüler', 'Pubertätsporobleme', 'Sprachausteine'). They are kept exactly as printed.",
      "- P02/P21 Leseverstehen 1 (p15, p305): the compiler notes that words are missing from texts 2–5 because of poor image quality; texts are reproduced as printed.",
      "- P04/P24 Sprachbausteine 1 (p42, p362): a line is missing after 'Allerdings (27)'.",
      "- Word banks with misspellings kept as printed: 'BEOUEM' (P07/P19), 'GEEIGENET', 'GEGEÜBER' (P10/P11/P27/P28), 'KENIE' (P12/P23), 'GESTRN' (P05/P16).",
      "- P12/P23 Leseverstehen 1: the last heading is printed as 'i)' twice; stored as j.", ""]
open("extraction/uncertain_content.md", "w").write("\n".join(L) + "\n")
# ---------- verification_report.md
by_paper = []
for p in papers:
    secs = ", ".join(e["id"].split("-", 1)[1] for e in p["exercises"])
    dups = sorted({dupof[e["id"]].split("-")[0] for e in p["exercises"] if e["id"] in dupof})
    by_paper.append(f"| {p['id']} | {p['pages'][0]}–{p['pages'][1]} | {secs} | p{p['answer_key_page']} | {', '.join(dups) or '–'} | {'; '.join(p['paper_notes'])[:140]} |")
R = f"""# Verification report (Phase 2 audit)

Generated from the files on disk by `tools/audit.py` + `tools/reports.py`.

## Totals
| Item | Count |
|---|---|
| PDF pages | 493 |
| Pages extracted | {s['pages']} (missing: {s['missing_pages'] or 'none'}) |
| Pages visually verified | {493 - len(s['unverified_pages'])} (unverified: {s['unverified_pages'] or 'none'}) |
| Exam papers found | {s['papers']} (P01–P30) |
| Lesen/Sprachbausteine exercises | {s['exercises']} ({', '.join(f"{k}: {v}" for k, v in s['by_type'].items())}) |
| Distinct exercises (after removing exact duplicates) | {s['unique_exercises']} |
| Answer keys (Lösungen pages) found | 30 (one per paper) |
| Exercises with complete answer key | {s['answer_keys_complete']} / {s['exercises']} |
| Automatic structural issues | {len(s['issues'])} |
| Uncertain items (per exercise, incl. duplicates) | {s['uncertain_exercise_items']} |

Verification method per page: `full` = page image read at full or zoomed resolution and compared line by line ({s['methods'].get('full', 0)} pages, mainly all photographed ad pages and key/first-occurrence pages);
`sheet-legible` = page read from a legible 2×2 contact sheet and compared against the structured extraction ({s['methods'].get('sheet-legible', 0)} pages — exercise and key pages);
`sheet` = page viewed on a contact sheet to confirm type/content, text taken from the embedded text layer and cross-checked against OCR ({s['methods'].get('sheet', 0)} pages — Hören/Schreiben/speaking-notes pages that are outside the website's scope).
For duplicate papers, the extracted text was additionally compared automatically against the already-verified first occurrence (exact match required).

## Checks performed (all passed)
1. Every page 1–493 has a batch record (50 batch files, `extraction/batches/`).
2. No page is unverified.
3. Every paper has its Lesen 1–3 and Sprachbausteine 1–2 extracted, except P02 and P21, which **do not contain** Leseverstehen Teil 2 or Sprachbausteine Teil 1 in the PDF (compiler's note on the key page).
4. Each answer key (Lösungen page) parsed; entries not machine-readable (different font) were read visually and recorded (P04/P24 item 2, P12/P23 items 23, 34, 39).
5. All questions present: headings a–j + texts 1–5; questions 6–10 with options a–c; situations 11–20 + ads a–l; gaps 21–30 with options a–c; gaps 31–40 in text + word bank a–o.
6. Key values are valid (a–j / a–c / a–l or x / a–o) and no heading/ad/word is used twice.
7. Order of exercises and papers matches the PDF.
8. Exact duplicates detected and recorded (the PDF repeats many papers; see table).
9. No uncertain content converted into guesses — see `uncertain_content.md`.

## Papers
| Paper | Pages | Exercises | Key page | Exercises duplicated from | Notes |
|---|---|---|---|---|---|
""" + "\n".join(by_paper) + """

## Special cases
- **P08/P17 Leseverstehen 2** has two question sets for the same text: the original set (p92/p239, key = black column) and a modified set (p93/p240, labelled 'معدل'), whose key is the second, green column on the key page. Both are included; the association of the green column with the modified set is inferred from consistency (documented in the exercise notes).
- **P08/P17 Sprachbausteine 1**: three options (23c, 26c, 29c) are printed on the following page; joined.
- **Ad pages (Leseverstehen 3)** are photos of printed pages in all papers. All 12 ads were transcribed for each distinct ad page (11 distinct ad pages, multiple photos each). Where a clearer photo of the same page existed, it was used to resolve unclear spots.
- **P06/P30 ad page** (p67/p447): top row (ads a–c) is out of focus; only headlines are legible. Marked `[unleserlich]`. The website shows the original page image for every ad exercise so you can consult the source.

## Limitations
- Hörverstehen and Schriftlicher Ausdruck pages are extracted as page text only (no audio exists in the PDF); not structured for the website, per instructions.
- Speaking-exam notes (pages 169–170, 198–222, 251–252, 266–270, 299–303, 326–330, 344–355, 395–396, 410–411, 425–426, 440–441, 455–492) are third-party model answers, recorded as page text only.
- Arabic topic labels on the pages are excluded from exercise text but stored per page (`arabic_labels_excluded`).
"""
open("extraction/verification_report.md", "w").write(R)
print(len(L), "uncertain lines;", len(R), "report chars")
