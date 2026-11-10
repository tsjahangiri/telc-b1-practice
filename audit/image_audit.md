# Advertisement audit (Leseverstehen Teil 3)

All Lesen-3 ads in the PDF are **photographs of printed exam pages** (no ad exists as born-digital text). 12 distinct ad pages × 12 ads = **144 distinct ads** (used by 30 exercises; several pages are re-photographed in duplicate papers).

## How the ads were rebuilt
- Text: the verified transcription is rendered as real HTML text (never AI-generated image text). An automated browser check confirmed that the visible text of every rendered ad equals the transcription (case-sensitive, ignoring line wrapping): **0 mismatches** across all 30 Lesen-3 exercises.
- Design: each ad is set as a black-and-white newspaper ad on a 'Zeitungsseite' like the exam pages — 8 typographic variants (bold frame, inverted headline bar, double rule, tinted box, script headline, coupon/dashed, framed serif, classic), a hand-assigned line pictogram (SVG) per ad, contact block in small print, prices emphasised, bullet lists kept. Original line breaks are kept for headlines/short lines; body lines flow as paragraphs so they read well on phones (line-end hyphenations are kept as soft hyphens).
- No photographs or AI images were added: the originals are B/W print, and inventing product photos would add content that is not in the PDF. Pictograms are neutral and carry no text.
- The original photo of each ad page stays available under every exercise ('Originalseite anzeigen').
- Markers: `[unleserlich]` / `[abgeschnitten] (third pass: replaced by marked reconstructions / […], see reconstructed_words.md)` = not readable in any photo (shown highlighted); dotted underline 'rekonstruiert' = reconstructed from blurred letter shapes + context (only P06/P30 ads a–c).

## Per ad page

| Exercise (first occurrence) | PDF photo pages | Ads | Status | Uncertain / reconstructed |
|---|---|---|---|---|
| P01-L3 (Möbel) | p6, p374 | 12 | Rebuilt; all text verified | none |
| P02-L3 (thailändisches) | p17, p307 | 12 | Rebuilt; fully legible, 2 low-confidence small-print item(s) | none |
| P03-L3 (Schweiz) | p28, p432 | 12 | Rebuilt; fully legible, 3 low-confidence small-print item(s) | none |
| P04-L3 (Eisenbahn) | p41, p80, p109, p276, p318, p361 | 12 | Rebuilt; fully legible, 3 low-confidence small-print item(s) | none |
| P05-L3 (Spezialität) | p54, p228 | 12 | Rebuilt; text verified except marked parts | I: 1 illegible |
| P06-L3 (Musik) | p67, p447 | 12 | Rebuilt; text verified except marked parts | A: 3 illegible, 6 reconstructed segments; B: 2 illegible, 5 reconstructed segments; C: 3 illegible, 8 reconstructed segments; I: 8 illegible; J: 1 illegible; L: 9 illegible |
| P08-L3 (arabischen Ländern) | p95, p242 | 12 | Rebuilt; text verified except marked parts | B: 1 illegible |
| P10-L3 (DB) | p122, p135, p402, p417 | 12 | Rebuilt; fully legible, 1 low-confidence small-print item(s) | none |
| P12-L3 (Georg und Claudia) | p148, p336 | 12 | Rebuilt; fully legible, 2 low-confidence small-print item(s) | none |
| P13-L3 (Sprachkurs) | p161, p387 | 12 | Rebuilt; fully legible, 1 low-confidence small-print item(s) | none |
| P14-L3 (Praktikum) | p176, p258 | 12 | Rebuilt; text verified except marked parts | A: 1 illegible |
| P15-L3 (sucht) | p189, p290 | 12 | Rebuilt; fully legible, 2 low-confidence small-print item(s) | none |

Low-confidence readings (small print) are listed per item in `extraction/uncertain_content.md`.

## Reconstructed text (P06 / P30, photo p67 and p447 — top row out of focus in both photos)

Original (sharp) parts: headlines 'DAS MUSIKERLEBNIS', 'Haydn Symphonie … „Der Bär“', 'Beethoven Chorfantasie, c-Moll, op. 80, Symphonie Nr. 1, C-Dur, op. 21', 'Herzlichen Glückwunsch!', 'SPICK', 'DIE ZEITSCHRIFT FÜR SCHÜLERINNEN UND SCHÜLER', 'KOREA PAVILLON'.

Reconstructed (marked `{{…}}` in data, dotted on screen):
- **A**: Sonntag, 17.6., 20 Uhr; Münchner Philharmonie, Prinzregentenplatz; Hob. 1:82; Es singen:; Leitung: Hans-Martin Schneidt; Euro
- **B**: Bestellen Sie ein Probeheft oder – noch; besser – gleich ein Abonnement, ganz; einfach per Telefon 01 404; oder; E-Mail abo-service@spick.ch
- **C**: Jeden Mittwoch und Sonntag; Buffet à discrétion ab 19.30 Uhr; Unser Personal bedient Sie in; original koreanischer Nationaltracht; Klimatisierte Räume; Echt koreanische Spezialitäten; Badenerstrasse; Telefon (01)

Reasoning: letter shapes, word lengths and line structure in both photos, plus the fit with the situations (18: 'im Juni in München … Konzert mit Gesang' → key A; 14: 'Geschenk für die 12-jährige Tochter' → key B; the restaurant ad C is not used by any key). Names of performers, prices and most digits could not be inferred and stay `[unleserlich]`. The answer key does not depend on any reconstructed word.
