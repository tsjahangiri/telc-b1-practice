# TELC B1 practice website (Lesen, Sprachbausteine & Hörverstehen)

Built from `B1-telc past papers(1).pdf` (493 pages, 30 exam papers). Works fully offline — no server, database or internet needed.

## How to start
Double-click **`website/index.html`** (opens in your browser). That's it.

Optional (if your browser restricts local files): in a terminal run
```
cd website && python3 -m http.server 8000
```
and open http://localhost:8000.

## Using it
- Two sections, switched in the top bar:
  - **Lesen & Sprachbausteine:** 65 distinct exercises (148 with "Doppelte Übungen anzeigen" ticked, because the PDF repeats many papers).
  - **Hörverstehen:** 32 distinct parts (88 with duplicates), 590 richtig/falsch statements.
- Everything is in PDF order.
- **Hörverstehen has no audio:** the PDF contains no recordings or transcripts. The exercises are text-based practice with the original statements and the official solutions, and each one says so.
- Overview on the left (☰ on mobile), filter by part, Weiter/Zurück (or ← → keys).
- Antworten prüfen → green/red feedback + correct answer; Lösung zeigen; Zurücksetzen.
- Progress is saved in your browser (localStorage). Answer keys come only from the PDF's Lösungen pages.
- Lesen 3 ads are re-set as newspaper ads (real text from the verified transcription). Highlighted [unleserlich] = not readable in the PDF; dotted text = reconstructed from a blurred or cut-off photo (P06/P30 ads a–c, i, j, l; see `audit/reconstructed_words.md`). [Grey `[…]`] = cut off in the photo and not reconstructable (a name, a number or a time). "Originalseite anzeigen" shows the original photo.

## Files
- `website/` — the site (`data/exercises.js` is generated; `img/` = original ad pages)
- `extraction/extracted_content.json` — all structured exercises + text of every page
- `extraction/verification_report.md`, `extraction/uncertain_content.md`, `extraction/extraction_log.md`
- `extraction/papers/PNN.json` (+ `.dump.txt`), `extraction/batches/` (50 batch files + reports)
- `extraction/hoeren/PNN.json` (+ `.dump.txt`) — Hörverstehen, built by `tools/hoeren.py`
- `extraction/corrections/` — every manual correction/transcription, auditable
- `progress.md` — status; `tools/` — scripts to rebuild (`build_paper.py`, `hoeren.py`, `audit.py`, `export_web.py`)
- `source/original.pdf` — unmodified copy of the PDF

## Audit
- `audit/` — audit records:
  - Second pass: page and exercise comparison, answer-key table, ad audit, corrections log, final report.
  - Third pass: `reconstructed_words.md`, `hoeren_audit.md`, and the Hörverstehen key table in `answer_key_verification.md`.
- `backup/` — snapshots taken before each audit pass
