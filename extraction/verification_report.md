# Verification report (Phase 2 audit)

Generated from the files on disk by `tools/audit.py` + `tools/reports.py`.

## Totals
| Item | Count |
|---|---|
| PDF pages | 493 |
| Pages extracted | 493 (missing: none) |
| Pages visually verified | 493 (unverified: none) |
| Exam papers found | 30 (P01–P30) |
| Lesen/Sprachbausteine exercises | 148 (lesen1: 30, lesen2: 30, lesen3: 30, sprach1: 28, sprach2: 30) |
| Distinct exercises (after removing exact duplicates) | 65 |
| Answer keys (Lösungen pages) found | 30 (one per paper) |
| Exercises with complete answer key | 148 / 148 |
| Automatic structural issues | 0 |
| Uncertain items (per exercise, incl. duplicates) | 78 |

Verification method per page: `full` = page image read at full or zoomed resolution and compared line by line (64 pages, mainly all photographed ad pages and key/first-occurrence pages);
`sheet-legible` = page read from a legible 2×2 contact sheet and compared against the structured extraction (209 pages — exercise and key pages);
`sheet` = page viewed on a contact sheet to confirm type/content, text taken from the embedded text layer and cross-checked against OCR (220 pages — Hören/Schreiben/speaking-notes pages that are outside the website's scope).
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
| P01 | 1–13 | L1, L2, L3, SB1, SB2 | p13 | – |  |
| P02 | 14–22 | L1, L3, SB2 | p22 | – | P02 contains no Leseverstehen Teil 2 and no Sprachbausteine Teil 1 in the PDF (pages 14–22). The answer-key page (p22) lists keys for the se |
| P03 | 23–35 | L1, L2, L3, SB1, SB2 | p35 | P02 |  |
| P04 | 36–48 | L1, L2, L3, SB1, SB2 | p48 | – |  |
| P05 | 49–61 | L1, L2, L3, SB1, SB2 | p61 | – |  |
| P06 | 62–74 | L1, L2, L3, SB1, SB2 | p74 | – |  |
| P07 | 75–88 | L1, L2, L3, SB1, SB2 | p88 | P04 |  |
| P08 | 89–103 | L1, L2, L2b, L3, SB1, SB2 | p103 | – |  |
| P09 | 104–116 | L1, L2, L3, SB1, SB2 | p116 | P03, P04, P06 |  |
| P10 | 117–129 | L1, L2, L3, SB1, SB2 | p129 | – |  |
| P11 | 130–142 | L1, L2, L3, SB1, SB2 | p142 | P10 |  |
| P12 | 143–155 | L1, L2, L3, SB1, SB2 | p155 | – |  |
| P13 | 156–168 | L1, L2, L3, SB1, SB2 | p168 | – |  |
| P14 | 171–183 | L1, L2, L3, SB1, SB2 | p183 | P05 |  |
| P15 | 184–197 | L1, L2, L3, SB1, SB2 | p197 | P13 |  |
| P16 | 223–235 | L1, L2, L3, SB1, SB2 | p235 | P05 |  |
| P17 | 236–250 | L1, L2, L2b, L3, SB1, SB2 | p250 | P08 | P17 is a duplicate of P08 (identical exercises and answer key). |
| P18 | 253–265 | L1, L2, L3, SB1, SB2 | p265 | P05, P14 | P18 is a duplicate of P14 (identical exercises and answer key). |
| P19 | 271–284 | L1, L2, L3, SB1, SB2 | p284 | P04, P07 | P19 is a duplicate of P07 (identical exercises and answer key). |
| P20 | 285–298 | L1, L2, L3, SB1, SB2 | p298 | P13, P15 | P20 is a duplicate of P15 (identical exercises and answer key). |
| P21 | 304–312 | L1, L3, SB2 | p312 | P02 | P21 is a duplicate of P02 (same three sections and key); like P02 it contains no Leseverstehen Teil 2 and no Sprachbausteine Teil 1. |
| P22 | 313–325 | L1, L2, L3, SB1, SB2 | p325 | P03, P04, P06, P09 | P22 is a duplicate of P09 (identical exercises and answer key). |
| P23 | 331–343 | L1, L2, L3, SB1, SB2 | p343 | P12 | P23 is a duplicate of P12 (identical exercises and answer key). |
| P24 | 356–368 | L1, L2, L3, SB1, SB2 | p368 | P04 | P24 is a duplicate of P04 (identical exercises and answer key). |
| P25 | 369–381 | L1, L2, L3, SB1, SB2 | p381 | P01 | P25 is a duplicate of P01 (identical exercises and answer key). |
| P26 | 382–394 | L1, L2, L3, SB1, SB2 | p394 | P13 | P26 is a duplicate of P13 (identical exercises and answer key). |
| P27 | 397–409 | L1, L2, L3, SB1, SB2 | p409 | P10 | P27 is a duplicate of P10 (identical exercises and answer key). |
| P28 | 412–424 | L1, L2, L3, SB1, SB2 | p424 | P10, P11 | P28 is a duplicate of P11 (identical exercises and answer key). |
| P29 | 427–439 | L1, L2, L3, SB1, SB2 | p439 | P02, P03 | P29 is a duplicate of P03 (identical exercises and answer key). |
| P30 | 442–454 | L1, L2, L3, SB1, SB2 | p454 | P06 | P30 is a duplicate of P06 (identical exercises and answer key). |

## Special cases
- **P08/P17 Leseverstehen 2** has two question sets for the same text: the original set (p92/p239, key = black column) and a modified set (p93/p240, labelled 'معدل'), whose key is the second, green column on the key page. Both are included; the association of the green column with the modified set is inferred from consistency (documented in the exercise notes).
- **P08/P17 Sprachbausteine 1**: three options (23c, 26c, 29c) are printed on the following page; joined.
- **Ad pages (Leseverstehen 3)** are photos of printed pages in all papers. All 12 ads were transcribed for each distinct ad page (11 distinct ad pages, multiple photos each). Where a clearer photo of the same page existed, it was used to resolve unclear spots.
- **P06/P30 ad page** (p67/p447): top row (ads a–c) is out of focus; only headlines are legible. Marked `[unleserlich]`. The website shows the original page image for every ad exercise so you can consult the source.

## Limitations
- Hörverstehen and Schriftlicher Ausdruck pages are extracted as page text only (no audio exists in the PDF); not structured for the website, per instructions.
- Speaking-exam notes (pages 169–170, 198–222, 251–252, 266–270, 299–303, 326–330, 344–355, 395–396, 410–411, 425–426, 440–441, 455–492) are third-party model answers, recorded as page text only.
- Arabic topic labels on the pages are excluded from exercise text but stored per page (`arabic_labels_excluded`).
