# Corrections log (second-pass audit, 2026-11-10)

Backup before any change: `backup/pre-audit-20261110-0728.tgz` (website, extraction data, corrections, tools).

## Content (source data)
| # | Where | Finding | Correction | Verified against |
|---|---|---|---|---|
| 1 | P06-L3 / P30-L3, ads a, b, c (photos p67, p447) | Body text was only marked `[unleserlich]` (both photos out of focus) | Reconstructed from blurred letter shapes + context, every reconstructed segment marked `{{…}}` in `extraction/corrections/P06.json`/`P30.json` and shown dotted ("rekonstruiert") on the site; names, prices, digits that could not be inferred stay `[unleserlich]` | p67 + p447 at 300 dpi |

No other content errors were found: reading texts, questions, options, gap numbering, word banks and all 1180 answer-key entries matched the PDF (see `exercise_comparison.md`, `answer_key_verification.md`). Spelling errors that exist in the PDF itself were deliberately kept (listed in `extraction/uncertain_content.md`, section C).

## Presentation / website
| # | Where | Finding | Correction |
|---|---|---|---|
| 2 | Lesen 3 (all 30) | Ads shown as plain text cards | Rebuilt as newspaper-style ad layouts (HTML text + CSS + SVG pictograms), see `image_audit.md` |
| 3 | Ad styles | Two typographic variants used CSS `text-transform: uppercase`, which changed the original capitalisation on screen | Removed; automated check: rendered ad text = transcription for all 144 distinct ads |
| 4 | Ad renderer | "Euro" inside "Europäischen" was styled as a price | Price detection now requires the whole word + a digit |
| 5 | Ad renderer | Original narrow-column line breaks made ads ragged on phones | Body lines flow as paragraphs; headlines/short/caps lines and bullets keep their own lines; line-end hyphenation kept as soft hyphen |
| 6 | P13-L2 / P26-L2 on 375-px screens | 3 px horizontal overflow (long title word) | Word-wrap for titles + `min-width:0` on the main grid column |
| 7 | index.html | Browsers could keep an old cached CSS/JS | Version query on CSS/JS/data links |

## Third pass (2026-11-10) — Lesen-3 reconstruction & Hörverstehen
| # | Where | Finding | Correction | Verified against |
|---|---|---|---|---|
| 8 | P06-L3 / P30-L3, ads i, j, l (p67, p447) | 18 `[abgeschnitten]` placeholders per paper shown to learners | 12 cut word endings reconstructed (`{{…}}`, dotted on screen); 5 non-inferable names/numbers/times shown as `[…]`; 1 placeholder line (ad j "heading") removed because no text is missing there; 3 bracketed first letters in ad j turned into marked reconstructions. Details and confidence: `reconstructed_words.md` | p67 + p447 at 250–300 dpi |
| 9 | P15-H3 / P20-H3 items 58, 60 | Lösungen pages p197/p298 give the key of a different Teil-3 text ("Meissner") for the printed "Ingolstadt" questions | Official key of the identical question set from p61/p235 used (− − + + −); confirmed by the bold formatting on p194/p295; note shown on the exercise | p61, p194, p197, p235, p295, p298 |
| 10 | Website | No Hörverstehen | New section "Hörverstehen" (88 parts, 590 statements), section switch in the top bar, filter Hörverstehen 1–3, richtig/falsch answer controls, audio-not-available notice, progress stored like the other sections | browser regression (236/236) |
| 11 | Website | New `[…]` marker | Rendered as a grey "cut off, not reconstructable" marker; legend updated | browser |
| 12 | Website (phones) | Section tabs truncated at 375 px | Short tab labels ("Lesen & SB" / "Hören") on narrow screens | browser 375 px |
