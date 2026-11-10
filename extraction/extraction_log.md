# Extraction log

## Tooling
- PyMuPDF (text layer with positions) — `tools/lines.py`, `tools/draft.py`
- macOS Vision OCR (de-DE, accurate) via a small Swift helper — `tools/ocr.swift` → `extraction/ocr/pNNN.txt` (all 493 pages, 300 dpi)
- Page images for visual checks: `extraction/view/vNNN.jpg` (110 dpi), zoomed crops via `tools/crop.py`, 2×2 contact sheets via `tools/sheet.py`

## Workflow per paper
1. `tools/draft.py` parses each exercise from the positioned text layer (headings, texts, questions/options, gaps, word banks, answer key).
2. Pages are compared visually with the draft; every correction is stored as an explicit, auditable entry in `extraction/corrections/PNN.json` (substring fixes, manual transcriptions of image-only pages and ads, key entries read visually, notes, uncertainties).
3. `tools/build_paper.py PNN` merges draft + corrections → `extraction/papers/PNN.json` and a readable dump `PNN.dump.txt`.
4. `tools/note.py` records per-page verification (method + note + uncertainties) → `extraction/corrections/page_notes.json`.
5. `tools/pages.py N` writes the batch file `extraction/batches/batch_NN.json` + `batch_NN_report.md` and re-opens it to validate.
6. `tools/progress.py` regenerates `progress.md` from disk.

## Phase 2
- `tools/audit.py` → `extraction/extracted_content.json` (all papers + all page records), `extraction/audit_stats.json`
- `tools/reports.py` → `extraction/verification_report.md`, `extraction/uncertain_content.md`

## Notable decisions
- Original wording, typos, punctuation are preserved; only text-layer artefacts were fixed (e.g. stray letters 'j jetzt', merged subheadings, split question numbers, split option lists across pages).
- Ads were transcribed manually from zoomed photos with OCR assistance; illegible parts are marked, never guessed.
- Heading/option letters normalized to lowercase keys (A→a) for consistent answer checking; the website displays them as printed letters.
