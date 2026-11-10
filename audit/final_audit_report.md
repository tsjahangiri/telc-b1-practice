# Final audit report

## Third pass (2026-11-10, after the second pass): Lesen-3 reconstruction + Hörverstehen

Backup taken before these changes: `backup/pre-hoeren-20261110-1156.tgz`. The original PDF was not modified.

| Item | Result |
|---|---|
| 1. Reconstructed words/phrases in Lesen, Teil 3 | **15 per paper** (P06-L3 and P30-L3 share one photo, p67 = p447): 12 cut word endings in ads i and l, plus 3 cut first letters in ad j. 5 cut-off names/numbers/times are shown as `[…]` because they cannot be inferred. 1 placeholder line in ad j was removed (no text is missing there). **0 `[abgeschnitten]` left.** |
| 2. Confidence | 12 High, 2 Medium (www.werderver*lag.ch*, griechische Sp*ezialitäten*), 1 Low (Auswahl *unserer Küche.*). Every item is listed in `reconstructed_words.md`; none affects the official answers (15 → i, 16 → l, both consistent). |
| 3. Hörverstehen exercises added | **88 parts** (Teil 1: 28, Teil 2: 30, Teil 3: 30; Modelltest 2 and 21 have no Teil 1 in the PDF). 32 are distinct; the rest are reprints linked as duplicates. |
| 4. Hörverstehen questions added | **590 richtig/falsch statements** (215 in distinct parts). The PDF has no other Hörverstehen task types. |
| 5. Official answers verified | **590 / 590.** Each answer was read from the paper's own Lösungen page and cross-checked against the same question set in other papers (all 590) and against the PDF's bold marking of richtig statements (470). **4 corrected:** P15-H3 and P20-H3 items 58 and 60, where the key column belongs to a different text ("Meissner"); the official key of the identical set (p61/p235) is used and explained on the page. 0 missing. |
| 6. Audio limitations | The PDF contains **no audio recordings and no transcripts** for any Hörverstehen part. Nothing was invented. Every Hörverstehen exercise shows a German and English notice that the recordings are not available and that only text-based practice is supported. |
| 7. Website testing | **236 / 236 exercises** (148 Lesen/Sprachbausteine + 88 Hörverstehen) pass the automated browser checks on desktop and at 375 px. Details below. |

**Website testing details** (automated, in the browser):
- Answers: official answers give full marks; wrong answers give 0 with every item marked; "Lösung zeigen" shows every answer; "Zurücksetzen" clears.
- Display: no horizontal overflow and 0 console errors.
- Hörverstehen: the no-audio notice shows on every exercise.
- Navigation: the section switch, part filter (Hörverstehen 1–3), Weiter/Zurück and counter work. A link to an exercise opens the right section.
- Saving: progress, including Hörverstehen, persists after a reload.
- Offline: no external resources.

**Method:**
- **Lesen 3:** the cut edges of p67 and p447 were inspected at 250–300 dpi. Reconstructions were checked against grammar, the visible letters and the rest of each ad.
- **Hörverstehen text:** extracted from the text layer and compared word by word with an independent OCR reading. The flagged pages were checked against the page images, and 0 corrections were needed. Source typos are kept as printed. The bold type that would give away the answers is not shown.
- **Hörverstehen key:** see `answer_key_verification.md` (second table) and `hoeren_audit.md`.

**Still not tested:** opening `website/index.html` directly from disk in your own browser. It uses only relative links, so it is expected to work.

---

## Second pass (2026-11-10)

Source of truth: `source/original.pdf` (unmodified copy of `B1-telc past papers(1).pdf`). Backup taken before changes: `backup/pre-audit-20261110-0728.tgz`.

## 1–9 Figures
| Item | Result |
|---|---|
| 1. PDF pages reviewed | 493 / 493 (50 batches of 10 — `page_comparison.md`) |
| 2. Exercises audited | 148 (all papers incl. duplicates; 65 distinct) |
| 3. Reading exercises (Lesen) | 90 (L1: 30, L2: 30 incl. 2 variant sets, L3: 30) |
| 4. Sprachbausteine exercises | 58 (Teil 1: 28 — P02/P21 have none in the PDF; Teil 2: 30) |
| 5. Questions / items checked | 1180 (515 distinct) |
| 6. Answers verified against Lösungen | 1180 / 1180 (two independent readings of the key pages + 570 answer words matched to option text) |
| 7. Errors discovered | 0 in texts, questions, options, numbering, ordering or keys. 6 presentation/website defects (uppercase transform altering capitalisation, price mis-styling, ragged ad text on phones, hyphen joining, 3-px mobile overflow, cache) — all fixed |
| 8. Corrections made | 7 (see `corrections_log.md`): 1 content (marked reconstruction of blurred ads), 6 website |
| 9. Advertisements recreated | 144 distinct ads on 12 ad pages (30 Lesen-3 exercises) rebuilt as newspaper-style layouts with real text |

## Method (summary)
- **Text audit:** every exercise compared word-by-word with an independent OCR reading of the page images (`tools/crosscheck.py`, `tools/seqcheck.py`); every flagged word/run reviewed against the page image. All flags were OCR noise (watermark, umlauts, table/photo reading order) or confirmed correct (e.g. 'GUTE', 'Chiffre 2063/9369', P08 options).
- **Key audit:** `tools/keycheck.py` → `answer_key_verification.md` (1180 rows). Entries in a different font were confirmed visually; the P08/P17 modified question set uses the green key column (documented).
- **Ad audit/rebuild:** `image_audit.md`. Automated browser check: on-screen text of every rendered ad = verified transcription (0 mismatches).
- **Regression test** (automated in the browser, all 148 exercises, desktop + 375-px mobile): open, enter official answers → full score; enter wrong answers → 0 and every item marked wrong; Lösung zeigen shows every answer; Zurücksetzen clears; progress persists after reload; Weiter/Zurück and counter correct (1…148, Zurück disabled on first); 30 ad images load; no horizontal overflow; no JavaScript errors. German characters render correctly.
- **Offline:** no external resources are loaded (fonts, scripts, images all local; data is a local `.js` file, so the site also works by double-clicking `index.html`).

## 10. Unresolved uncertainties
- P06/P30 ads a–c: reconstructed text (19 marked segments) — plausible but not verifiable; names/prices/digits remain `[unleserlich]` (29 illegible markers across ad pages, mainly P06 ads i, j, l cut off at the photo edge).
- Low-confidence small print in some ads (phone numbers, names) — listed in `extraction/uncertain_content.md`.
- Source defects kept as printed (missing words P02/P21 L1 texts 2–5; missing line after gap 27 in P04/P24 SB1; misspellings in word banks).
- P08/P17 L2 variant key: association with the green key column is inferred from consistency.
- Not tested by me: opening `index.html` directly from disk in your own browser (the test pane only serves pages over HTTP). The page uses only relative `<script>`/`<link>` tags, so it is expected to work.

## 11. Final website testing results
148/148 exercises pass all functional checks on desktop and mobile; 0 console errors; 0 ad-text mismatches; 0 overflow.
