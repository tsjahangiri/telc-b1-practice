# Hörverstehen audit (2026-11-10)

## What the PDF contains
- Each of the 30 Modelltests has Hörverstehen **Teil 1 (items 41–45)**, **Teil 2 (46–55)** and **Teil 3 (56–60)**.
- Exceptions: Modelltest 2 and 21 have no Teil 1 in the PDF, and their Lösungen pages list only Teil 2 and Teil 3. Total: **88 parts**.
- Every task is a **richtig/falsch statement** task (answers + / −). The PDF has no multiple-choice options, matching tasks, tables or pictures in Hörverstehen.
- Per part, the PDF contains the heading, the original instructions, the numbered statements and the official solution on the paper's Lösungen page.
- **Audio and transcripts:** the PDF contains **no audio and no transcript or listening text** for any part. Nothing was invented. Each exercise shows a notice that the recordings are not available and that only text-based practice is possible.
- Each question page also has a small Arabic label (a topic hint added by the PDF's compiler). As in the other sections it is not part of the exam and is left out. The red topic word from the Lösungen page is shown as "Thema".

## Extraction & verification
- `tools/hoeren.py` reads the embedded text layer (all 88 pages have one) and writes `extraction/hoeren/PNN.json` plus a `.dump.txt` per paper. Manual fixes go in `extraction/corrections/hoeren.json`.
- **Text:** every statement and instruction line was compared word by word with an independent Vision-OCR reading of the page image.
  - 114 statement flags: all OCR noise (watermark fragments like "hochschul", words run together, missing line numbers, e.g. "grolses").
  - The candidates were checked against the page images: p151, p152, p166, p194. **0 text corrections were needed.**
- **Kept exactly as printed:** typing errors in the source, such as 'nachts zu an.', 'Für die Sprechen', 'Lehrstell', 'Erst morgen Abend bildet sich Nebel..'.
- **Removed:** the bold type the PDF uses to mark richtig statements. It would give away the answers, so all statements are shown in plain type.
- **Display:** double spaces are collapsed, and instruction lines broken mid-sentence are re-joined.
- **Answer key:** see the Hörverstehen table at the end of `answer_key_verification.md`.
  - 590 answers, each read from the paper's own Lösungen page.
  - Cross-checked against the same question set in other papers (all 590) and against bold formatting (470).
  - Result: 586 verified, 4 corrected (P15-H3 and P20-H3 items 58 and 60: key column of a different text, "Meissner").
  - 0 missing, 0 ambiguous after correction.

## Totals
- Parts (exercises): **88**, of which 32 are distinct. The rest are reprints, linked as duplicates so their progress is shared.
- Statements (questions): **590**, of which 215 are in distinct parts.
- Official answers verified: **590 / 590** (4 taken from the identical set's key, see above).

## Per part
| Exercise | Topic (key page) | Question page | Key page | Statements | Duplicate of | Note |
|---|---|---|---|---|---|---|
| P01-H1 | Urlaub | p9 | p13 | 41–45 |  |  |
| P01-H2 | Schütz | p10 | p13 | 46–55 |  |  |
| P01-H3 | Mannheim | p11 | p13 | 56–60 |  |  |
| P02-H2 | Schütz | p19 | p22 | 46–55 | P01-H2 |  |
| P02-H3 | Norddeutschland | p20 | p22 | 56–60 |  |  |
| P03-H1 | Fremdsprache | p31 | p35 | 41–45 |  |  |
| P03-H2 | kranke | p32 | p35 | 46–55 |  |  |
| P03-H3 | Fahrer | p33 | p35 | 56–60 |  |  |
| P04-H1 | Urlaub | p44 | p48 | 41–45 | P01-H1 |  |
| P04-H2 | Praktikum | p45 | p48 | 46–55 |  |  |
| P04-H3 | Norddeutschland | p46 | p48 | 56–60 | P02-H3 |  |
| P05-H1 | Einzelkind | p57 | p61 | 41–45 |  |  |
| P05-H2 | Wallner-Calletti | p58 | p61 | 46–55 |  |  |
| P05-H3 | Ingolstadt | p59 | p61 | 56–60 |  |  |
| P06-H1 | Einkäufe im Internet | p70 | p74 | 41–45 |  |  |
| P06-H2 | Wenger | p71 | p74 | 46–55 |  |  |
| P06-H3 | Griechenland | p72 | p74 | 56–60 |  |  |
| P07-H1 | Bus zur Arbeit | p83 | p88 | 41–45 |  |  |
| P07-H2 | Frau Reiter | p84 | p88 | 46–55 |  |  |
| P07-H3 | Der Fahrer | p85 | p88 | 56–60 |  |  |
| P08-H1 | Computer | p99 | p103 | 41–45 |  |  |
| P08-H2 | Bachinger | p100 | p103 | 46–55 |  |  |
| P08-H3 | Der Fahrer | p101 | p103 | 56–60 | P07-H3 |  |
| P09-H1 | Arbeit zu fahren | p112 | p116 | 41–45 |  |  |
| P09-H2 | UKI | p113 | p116 | 46–55 |  |  |
| P09-H3 | Prag | p114 | p116 | 56–60 |  |  |
| P10-H1 | Kinder | p125 | p129 | 41–45 |  |  |
| P10-H2 | Touristen | p126 | p129 | 46–55 |  |  |
| P10-H3 | Füssen | p127 | p129 | 56–60 |  |  |
| P11-H1 | Einkäufe im Internet | p138 | p142 | 41–45 |  |  |
| P11-H2 | Praktikum | p139 | p142 | 46–55 | P04-H2 |  |
| P11-H3 | Norddeutschland | p140 | p142 | 56–60 | P02-H3 |  |
| P12-H1 | Arbeitsplatz für ihren Vater | p151 | p155 | 41–45 |  |  |
| P12-H2 | Frau Schäfer | p152 | p155 | 46–55 |  |  |
| P12-H3 | Georg und Claudia | p153 | p155 | 56–60 |  |  |
| P13-H1 | in der Schule | p164 | p168 | 41–45 | P10-H1 |  |
| P13-H2 | Touristen | p165 | p168 | 46–55 | P10-H2 |  |
| P13-H3 | Hauptbahnhof | p166 | p168 | 56–60 |  |  |
| P14-H1 | Bus zur Arbeit | p179 | p183 | 41–45 |  |  |
| P14-H2 | Touristen | p180 | p183 | 46–55 | P10-H2 |  |
| P14-H3 | Griechenland | p181 | p183 | 56–60 | P06-H3 |  |
| P15-H1 | Einkäufe im Internet | p192 | p197 | 41–45 | P11-H1 |  |
| P15-H2 | Thurnherr | p193 | p197 | 46–55 |  |  |
| P15-H3 | Meissner | p194 | p197 | 56–60 | P05-H3 | key corrected — see answer_key_verification.md |
| P16-H1 | Einzelkind | p231 | p235 | 41–45 | P05-H1 |  |
| P16-H2 | Wallner-Calletti | p232 | p235 | 46–55 | P05-H2 |  |
| P16-H3 | Ingolstadt | p233 | p235 | 56–60 | P05-H3 |  |
| P17-H1 | Computer | p246 | p250 | 41–45 | P08-H1 |  |
| P17-H2 | Bachinger | p247 | p250 | 46–55 | P08-H2 |  |
| P17-H3 | Der Fahrer | p248 | p250 | 56–60 | P07-H3 |  |
| P18-H1 | Bus zur Arbeit | p261 | p265 | 41–45 | P14-H1 |  |
| P18-H2 | Touristen | p262 | p265 | 46–55 | P10-H2 |  |
| P18-H3 | Griechenland | p263 | p265 | 56–60 | P06-H3 |  |
| P19-H1 | Bus zur Arbeit | p279 | p284 | 41–45 | P07-H1 |  |
| P19-H2 | Frau Reiter | p280 | p284 | 46–55 | P07-H2 |  |
| P19-H3 | Der Fahrer | p281 | p284 | 56–60 | P07-H3 |  |
| P20-H1 | Einkäufe im Internet | p293 | p298 | 41–45 | P11-H1 |  |
| P20-H2 | Thurnherr | p294 | p298 | 46–55 | P15-H2 |  |
| P20-H3 | Meissner | p295 | p298 | 56–60 | P05-H3 | key corrected — see answer_key_verification.md |
| P21-H2 | Schütz | p309 | p312 | 46–55 | P01-H2 |  |
| P21-H3 | Norddeutschland | p310 | p312 | 56–60 | P02-H3 |  |
| P22-H1 | Arbeit zu fahren | p321 | p325 | 41–45 | P09-H1 |  |
| P22-H2 | UKI | p322 | p325 | 46–55 | P09-H2 |  |
| P22-H3 | Prag | p323 | p325 | 56–60 | P09-H3 |  |
| P23-H1 | Arbeitsplatz für ihren Vater | p339 | p343 | 41–45 | P12-H1 |  |
| P23-H2 | Frau Schäfer | p340 | p343 | 46–55 | P12-H2 |  |
| P23-H3 | Georg und Claudia | p341 | p343 | 56–60 | P12-H3 |  |
| P24-H1 | Urlaub | p364 | p368 | 41–45 | P01-H1 |  |
| P24-H2 | Praktikum | p365 | p368 | 46–55 | P04-H2 |  |
| P24-H3 | Norddeutschland | p366 | p368 | 56–60 | P02-H3 |  |
| P25-H1 | Urlaub | p377 | p381 | 41–45 | P01-H1 |  |
| P25-H2 | Schütz | p378 | p381 | 46–55 | P01-H2 |  |
| P25-H3 | Mannheim | p379 | p381 | 56–60 | P01-H3 |  |
| P26-H1 | in der Schule | p390 | p394 | 41–45 | P10-H1 |  |
| P26-H2 | Touristen | p391 | p394 | 46–55 | P10-H2 |  |
| P26-H3 | Hauptbahnhof | p392 | p394 | 56–60 | P13-H3 |  |
| P27-H1 | Kinder | p405 | p409 | 41–45 | P10-H1 |  |
| P27-H2 | Touristen | p406 | p409 | 46–55 | P10-H2 |  |
| P27-H3 | Füssen | p407 | p409 | 56–60 | P10-H3 |  |
| P28-H1 | Einkäufe im Internet | p420 | p424 | 41–45 | P11-H1 |  |
| P28-H2 | Praktikum | p421 | p424 | 46–55 | P04-H2 |  |
| P28-H3 | Norddeutschland | p422 | p424 | 56–60 | P02-H3 |  |
| P29-H1 | Fremdsprache | p435 | p439 | 41–45 | P03-H1 |  |
| P29-H2 | kranke | p436 | p439 | 46–55 | P03-H2 |  |
| P29-H3 | Fahrer | p437 | p439 | 56–60 | P03-H3 |  |
| P30-H1 | Einkäufe im Internet | p450 | p454 | 41–45 | P06-H1 |  |
| P30-H2 | Wenger | p451 | p454 | 46–55 | P06-H2 |  |
| P30-H3 | Griechenland | p452 | p454 | 56–60 | P06-H3 |  |
