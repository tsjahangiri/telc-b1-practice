# Page-by-page comparison (second pass)

Method: for every page that feeds a website exercise, the website text was compared word-by-word against an independent Vision-OCR reading of the page image (`tools/crosscheck.py`, `tools/seqcheck.py`, per-exercise diffs in `audit/crosscheck/`). Every flagged word/run was reviewed against the page image. Ad pages (photos) were additionally re-read visually ad by ad during the advertisement rebuild (see `image_audit.md`). Non-exercise pages (Hören, Schreiben, speaking notes) were re-confirmed as out of scope.

Similarity = word-sequence similarity website↔OCR (table pages and photos score lower because of reading order and OCR noise, not content differences).

## Batch 01 — pages 1–10

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 1 | P01 | L1 | P01-L1 | 0.965 | 2 | no discrepancy |
| 2 | P01 | L1 | P01-L1 | 0.965 | 2 | no discrepancy |
| 3 | P01 | L2 | P01-L2 | 0.97 | 4 | no discrepancy |
| 4 | P01 | L2 | P01-L2 | 0.97 | 4 | no discrepancy |
| 5 | P01 | L3 | P01-L3 | 0.615 | 6 | no discrepancy |
| 6 | P01 | L3 | P01-L3 | 0.615 | 6 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 7 | P01 | SB1 | P01-SB1 | 0.799 | 1 | no discrepancy |
| 8 | P01 | SB2 | P01-SB2 | 0.913 | 0 | no discrepancy |
| 9 | P01 | H | – | – | – | not part of website (out of scope) |
| 10 | P01 | H | – | – | – | not part of website (out of scope) |

## Batch 02 — pages 11–20

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 11 | P01 | H | – | – | – | not part of website (out of scope) |
| 12 | P01 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 13 | P01 | LOES | – | – | – | not part of website (out of scope) |
| 14 | P02 | L1 | P02-L1 | 0.965 | 2 | no discrepancy |
| 15 | P02 | L1 | P02-L1 | 0.965 | 2 | no discrepancy |
| 16 | P02 | L3 | P02-L3 | 0.486 | 101 | no discrepancy |
| 17 | P02 | L3 | P02-L3 | 0.486 | 101 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 18 | P02 | SB2 | P02-SB2 | 0.918 | 0 | no discrepancy |
| 19 | P02 | H | – | – | – | not part of website (out of scope) |
| 20 | P02 | H | – | – | – | not part of website (out of scope) |

## Batch 03 — pages 21–30

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 21 | P02 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 22 | P02 | LOES | – | – | – | not part of website (out of scope) |
| 23 | P03 | L1 | P03-L1 | 0.951 | 11 | no discrepancy |
| 24 | P03 | L1 | P03-L1 | 0.951 | 11 | no discrepancy |
| 25 | P03 | L2 | P03-L2 | 0.938 | 11 | no discrepancy |
| 26 | P03 | L2 | P03-L2 | 0.938 | 11 | no discrepancy |
| 27 | P03 | L3 | P03-L3 | 0.466 | 101 | no discrepancy |
| 28 | P03 | L3 | P03-L3 | 0.466 | 101 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 29 | P03 | SB1 | P03-SB1 | 0.844 | 1 | no discrepancy |
| 30 | P03 | SB2 | P03-SB2 | 0.909 | 3 | no discrepancy |

## Batch 04 — pages 31–40

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 31 | P03 | H | – | – | – | not part of website (out of scope) |
| 32 | P03 | H | – | – | – | not part of website (out of scope) |
| 33 | P03 | H | – | – | – | not part of website (out of scope) |
| 34 | P03 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 35 | P03 | LOES | – | – | – | not part of website (out of scope) |
| 36 | P04 | L1 | P04-L1 | 0.964 | 3 | no discrepancy |
| 37 | P04 | L1 | P04-L1 | 0.964 | 3 | no discrepancy |
| 38 | P04 | L2 | P04-L2 | 0.968 | 1 | no discrepancy |
| 39 | P04 | L2 | P04-L2 | 0.968 | 1 | no discrepancy |
| 40 | P04 | L3 | P04-L3 | 0.538 | 59 | no discrepancy |

## Batch 05 — pages 41–50

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 41 | P04 | SCHREIBEN | P04-L3 | 0.538 | 59 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 42 | P04 | SB1 | P04-SB1 | 0.818 | 0 | no discrepancy |
| 43 | P04 | SB2 | P04-SB2 | 0.871 | 4 | no discrepancy |
| 44 | P04 | H | – | – | – | not part of website (out of scope) |
| 45 | P04 | H | – | – | – | not part of website (out of scope) |
| 46 | P04 | H | – | – | – | not part of website (out of scope) |
| 47 | P04 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 48 | P04 | LOES | – | – | – | not part of website (out of scope) |
| 49 | P05 | L1 | P05-L1 | 0.974 | 1 | no discrepancy |
| 50 | P05 | L1 | P05-L1 | 0.974 | 1 | no discrepancy |

## Batch 06 — pages 51–60

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 51 | P05 | L2 | P05-L2 | 0.963 | 5 | no discrepancy |
| 52 | P05 | L2 | P05-L2 | 0.963 | 5 | no discrepancy |
| 53 | P05 | L3 | P05-L3 | 0.514 | 92 | no discrepancy |
| 54 | P05 | ? | P05-L3 | 0.514 | 92 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 55 | P05 | SB1 | P05-SB1 | 0.804 | 0 | no discrepancy |
| 56 | P05 | SB2 | P05-SB2 | 0.887 | 3 | no discrepancy |
| 57 | P05 | H | – | – | – | not part of website (out of scope) |
| 58 | P05 | H | – | – | – | not part of website (out of scope) |
| 59 | P05 | H | – | – | – | not part of website (out of scope) |
| 60 | P05 | SCHREIBEN | – | – | – | not part of website (out of scope) |

## Batch 07 — pages 61–70

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 61 | P05 | LOES | – | – | – | not part of website (out of scope) |
| 62 | P06 | L1 | P06-L1 | 0.97 | 1 | no discrepancy |
| 63 | P06 | L1 | P06-L1 | 0.97 | 1 | no discrepancy |
| 64 | P06 | L2 | P06-L2 | 0.961 | 4 | no discrepancy |
| 65 | P06 | L2 | P06-L2 | 0.961 | 4 | no discrepancy |
| 66 | P06 | L3 | P06-L3 | 0.541 | 113 | no discrepancy |
| 67 | P06 | L3 | P06-L3 | 0.541 | 113 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild — ads a–c blurred, reconstruction marked |
| 68 | P06 | SB1 | P06-SB1 | 0.798 | 1 | no discrepancy |
| 69 | P06 | SB2 | P06-SB2 | 0.902 | 0 | no discrepancy |
| 70 | P06 | H | – | – | – | not part of website (out of scope) |

## Batch 08 — pages 71–80

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 71 | P06 | H | – | – | – | not part of website (out of scope) |
| 72 | P06 | H | – | – | – | not part of website (out of scope) |
| 73 | P06 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 74 | P06 | LOES | – | – | – | not part of website (out of scope) |
| 75 | P07 | L1 | P07-L1 | 0.958 | 1 | no discrepancy |
| 76 | P07 | L1 | P07-L1 | 0.958 | 1 | no discrepancy |
| 77 | P07 | L2 | P07-L2 | 0.979 | 1 | no discrepancy |
| 78 | P07 | L2 | P07-L2 | 0.979 | 1 | no discrepancy |
| 79 | P07 | L3 | P07-L3 | 0.525 | 65 | no discrepancy |
| 80 | P07 | L3 | P07-L3 | 0.525 | 65 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |

## Batch 09 — pages 81–90

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 81 | P07 | SB1 | P07-SB1 | 0.802 | 1 | no discrepancy |
| 82 | P07 | SB2 | P07-SB2 | 0.877 | 0 | no discrepancy |
| 83 | P07 | H | – | – | – | not part of website (out of scope) |
| 84 | P07 | H | – | – | – | not part of website (out of scope) |
| 85 | P07 | H | – | – | – | not part of website (out of scope) |
| 86 | P07 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 87 | P07 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 88 | P07 | LOES | – | – | – | not part of website (out of scope) |
| 89 | P08 | L1 | P08-L1 | 0.959 | 2 | no discrepancy |
| 90 | P08 | L1 | P08-L1 | 0.959 | 2 | no discrepancy |

## Batch 10 — pages 91–100

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 91 | P08 | L2 | P08-L2, P08-L2b | 0.939, 0.981 | 21, 0 | no discrepancy |
| 92 | P08 | L2 | P08-L2 | 0.939 | 21 | no discrepancy |
| 93 | P08 | L2 | P08-L2b | 0.981 | 0 | no discrepancy |
| 94 | P08 | L3 | P08-L3 | 0.453 | 89 | no discrepancy |
| 95 | P08 | L3 | P08-L3 | 0.453 | 89 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 96 | P08 | SB1 | P08-SB1 | 0.785 | 0 | no discrepancy |
| 97 | P08 | ? | P08-SB1 | 0.785 | 0 | no discrepancy |
| 98 | P08 | SB2 | P08-SB2 | 0.882 | 0 | no discrepancy |
| 99 | P08 | H | – | – | – | not part of website (out of scope) |
| 100 | P08 | H | – | – | – | not part of website (out of scope) |

## Batch 11 — pages 101–110

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 101 | P08 | H | – | – | – | not part of website (out of scope) |
| 102 | P08 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 103 | P08 | LOES | – | – | – | not part of website (out of scope) |
| 104 | P09 | L1 | P09-L1 | 0.972 | 0 | no discrepancy |
| 105 | P09 | L1 | P09-L1 | 0.972 | 0 | no discrepancy |
| 106 | P09 | L2 | P09-L2 | 0.957 | 1 | no discrepancy |
| 107 | P09 | L2 | P09-L2 | 0.957 | 1 | no discrepancy |
| 108 | P09 | L3 | P09-L3 | 0.527 | 70 | no discrepancy |
| 109 | P09 | L3 | P09-L3 | 0.527 | 70 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 110 | P09 | SB1 | P09-SB1 | 0.845 | 1 | no discrepancy |

## Batch 12 — pages 111–120

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 111 | P09 | SB2 | P09-SB2 | 0.891 | 2 | no discrepancy |
| 112 | P09 | H | – | – | – | not part of website (out of scope) |
| 113 | P09 | H | – | – | – | not part of website (out of scope) |
| 114 | P09 | H | – | – | – | not part of website (out of scope) |
| 115 | P09 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 116 | P09 | LOES | – | – | – | not part of website (out of scope) |
| 117 | P10 | L1 | P10-L1 | 0.965 | 1 | no discrepancy |
| 118 | P10 | L1 | P10-L1 | 0.965 | 1 | no discrepancy |
| 119 | P10 | L2 | P10-L2 | 0.976 | 0 | no discrepancy |
| 120 | P10 | L2 | P10-L2 | 0.976 | 0 | no discrepancy |

## Batch 13 — pages 121–130

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 121 | P10 | L3 | P10-L3 | 0.547 | 38 | no discrepancy |
| 122 | P10 | L3 | P10-L3 | 0.547 | 38 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 123 | P10 | SB1 | P10-SB1 | 0.811 | 0 | no discrepancy |
| 124 | P10 | SB2 | P10-SB2 | 0.89 | 0 | no discrepancy |
| 125 | P10 | H | – | – | – | not part of website (out of scope) |
| 126 | P10 | H | – | – | – | not part of website (out of scope) |
| 127 | P10 | H | – | – | – | not part of website (out of scope) |
| 128 | P10 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 129 | P10 | LOES | – | – | – | not part of website (out of scope) |
| 130 | P11 | L1 | P11-L1 | 0.969 | 3 | no discrepancy |

## Batch 14 — pages 131–140

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 131 | P11 | L1 | P11-L1 | 0.969 | 3 | no discrepancy |
| 132 | P11 | L2 | P11-L2 | 0.969 | 4 | no discrepancy |
| 133 | P11 | L2 | P11-L2 | 0.969 | 4 | no discrepancy |
| 134 | P11 | L3 | P11-L3 | 0.564 | 27 | no discrepancy |
| 135 | P11 | L3 | P11-L3 | 0.564 | 27 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 136 | P11 | SB1 | P11-SB1 | 0.818 | 1 | no discrepancy |
| 137 | P11 | SB2 | P11-SB2 | 0.89 | 0 | no discrepancy |
| 138 | P11 | H | – | – | – | not part of website (out of scope) |
| 139 | P11 | H | – | – | – | not part of website (out of scope) |
| 140 | P11 | H | – | – | – | not part of website (out of scope) |

## Batch 15 — pages 141–150

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 141 | P11 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 142 | P11 | LOES | – | – | – | not part of website (out of scope) |
| 143 | P12 | L1 | P12-L1 | 0.973 | 0 | no discrepancy |
| 144 | P12 | L1 | P12-L1 | 0.973 | 0 | no discrepancy |
| 145 | P12 | L2 | P12-L2 | 0.949 | 17 | no discrepancy |
| 146 | P12 | L2 | P12-L2 | 0.949 | 17 | no discrepancy |
| 147 | P12 | L3 | P12-L3 | 0.556 | 100 | no discrepancy |
| 148 | P12 | L3 | P12-L3 | 0.556 | 100 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 149 | P12 | SB1 | P12-SB1 | 0.793 | 6 | no discrepancy |
| 150 | P12 | SB2 | P12-SB2 | 0.869 | 1 | no discrepancy |

## Batch 16 — pages 151–160

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 151 | P12 | H | – | – | – | not part of website (out of scope) |
| 152 | P12 | H | – | – | – | not part of website (out of scope) |
| 153 | P12 | H | – | – | – | not part of website (out of scope) |
| 154 | P12 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 155 | P12 | LOES | – | – | – | not part of website (out of scope) |
| 156 | P13 | L1 | P13-L1 | 0.949 | 4 | no discrepancy |
| 157 | P13 | L1 | P13-L1 | 0.949 | 4 | no discrepancy |
| 158 | P13 | L2 | P13-L2 | 0.939 | 13 | no discrepancy |
| 159 | P13 | L2 | P13-L2 | 0.939 | 13 | no discrepancy |
| 160 | P13 | L3 | P13-L3 | 0.559 | 31 | no discrepancy |

## Batch 17 — pages 161–170

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 161 | P13 | L3 | P13-L3 | 0.559 | 31 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 162 | P13 | SB1 | P13-SB1 | 0.804 | 0 | no discrepancy |
| 163 | P13 | SB2 | P13-SB2 | 0.872 | 1 | no discrepancy |
| 164 | P13 | H | – | – | – | not part of website (out of scope) |
| 165 | P13 | H | – | – | – | not part of website (out of scope) |
| 166 | P13 | H | – | – | – | not part of website (out of scope) |
| 167 | P13 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 168 | P13 | LOES | – | – | – | not part of website (out of scope) |
| 169 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 170 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 18 — pages 171–180

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 171 | P14 | L1 | P14-L1 | 0.944 | 8 | no discrepancy |
| 172 | P14 | L1 | P14-L1 | 0.944 | 8 | no discrepancy |
| 173 | P14 | L2 | P14-L2 | 0.961 | 7 | no discrepancy |
| 174 | P14 | L2 | P14-L2 | 0.961 | 7 | no discrepancy |
| 175 | P14 | L3 | P14-L3 | 0.515 | 126 | no discrepancy |
| 176 | P14 | L3 | P14-L3 | 0.515 | 126 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 177 | P14 | SB1 | P14-SB1 | 0.783 | 6 | no discrepancy |
| 178 | P14 | SB2 | P14-SB2 | 0.891 | 3 | no discrepancy |
| 179 | P14 | H | – | – | – | not part of website (out of scope) |
| 180 | P14 | H | – | – | – | not part of website (out of scope) |

## Batch 19 — pages 181–190

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 181 | P14 | H | – | – | – | not part of website (out of scope) |
| 182 | P14 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 183 | P14 | LOES | – | – | – | not part of website (out of scope) |
| 184 | P15 | L1 | P15-L1 | 0.974 | 0 | no discrepancy |
| 185 | P15 | L1 | P15-L1 | 0.974 | 0 | no discrepancy |
| 186 | P15 | L2 | P15-L2 | 0.919 | 14 | no discrepancy |
| 187 | P15 | L2 | P15-L2 | 0.919 | 14 | no discrepancy |
| 188 | P15 | L3 | P15-L3 | 0.526 | 53 | no discrepancy |
| 189 | P15 | L3 | P15-L3 | 0.526 | 53 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 190 | P15 | SB1 | P15-SB1 | 0.774 | 0 | no discrepancy |

## Batch 20 — pages 191–200

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 191 | P15 | SB2 | P15-SB2 | 0.876 | 1 | no discrepancy |
| 192 | P15 | H | – | – | – | not part of website (out of scope) |
| 193 | P15 | H | – | – | – | not part of website (out of scope) |
| 194 | P15 | H | – | – | – | not part of website (out of scope) |
| 195 | P15 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 196 | P15 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 197 | P15 | LOES | – | – | – | not part of website (out of scope) |
| 198 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 199 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 200 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 21 — pages 201–210

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 201 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 202 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 203 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 204 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 205 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 206 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 207 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 208 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 209 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 210 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 22 — pages 211–220

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 211 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 212 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 213 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 214 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 215 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 216 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 217 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 218 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 219 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 220 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 23 — pages 221–230

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 221 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 222 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 223 | P16 | L1 | P16-L1 | 0.974 | 1 | no discrepancy |
| 224 | P16 | L1 | P16-L1 | 0.974 | 1 | no discrepancy |
| 225 | P16 | L2 | P16-L2 | 0.963 | 5 | no discrepancy |
| 226 | P16 | L2 | P16-L2 | 0.963 | 5 | no discrepancy |
| 227 | P16 | L3 | P16-L3 | 0.514 | 92 | no discrepancy |
| 228 | P16 | ? | P16-L3 | 0.514 | 92 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 229 | P16 | SB1 | P16-SB1 | 0.804 | 0 | no discrepancy |
| 230 | P16 | SB2 | P16-SB2 | 0.887 | 3 | no discrepancy |

## Batch 24 — pages 231–240

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 231 | P16 | H | – | – | – | not part of website (out of scope) |
| 232 | P16 | H | – | – | – | not part of website (out of scope) |
| 233 | P16 | H | – | – | – | not part of website (out of scope) |
| 234 | P16 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 235 | P16 | LOES | – | – | – | not part of website (out of scope) |
| 236 | P17 | L1 | P17-L1 | 0.959 | 2 | no discrepancy |
| 237 | P17 | L1 | P17-L1 | 0.959 | 2 | no discrepancy |
| 238 | P17 | L2 | P17-L2, P17-L2b | 0.939, 0.981 | 21, 0 | no discrepancy |
| 239 | P17 | L2 | P17-L2 | 0.939 | 21 | no discrepancy |
| 240 | P17 | L2 | P17-L2b | 0.981 | 0 | no discrepancy |

## Batch 25 — pages 241–250

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 241 | P17 | L3 | P17-L3 | 0.453 | 89 | no discrepancy |
| 242 | P17 | L3 | P17-L3 | 0.453 | 89 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 243 | P17 | SB1 | P17-SB1 | 0.785 | 0 | no discrepancy |
| 244 | P17 | ? | P17-SB1 | 0.785 | 0 | no discrepancy |
| 245 | P17 | SB2 | P17-SB2 | 0.882 | 0 | no discrepancy |
| 246 | P17 | H | – | – | – | not part of website (out of scope) |
| 247 | P17 | H | – | – | – | not part of website (out of scope) |
| 248 | P17 | H | – | – | – | not part of website (out of scope) |
| 249 | P17 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 250 | P17 | LOES | – | – | – | not part of website (out of scope) |

## Batch 26 — pages 251–260

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 251 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 252 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 253 | P18 | L1 | P18-L1 | 0.944 | 8 | no discrepancy |
| 254 | P18 | L1 | P18-L1 | 0.944 | 8 | no discrepancy |
| 255 | P18 | L2 | P18-L2 | 0.961 | 7 | no discrepancy |
| 256 | P18 | L2 | P18-L2 | 0.961 | 7 | no discrepancy |
| 257 | P18 | L3 | P18-L3 | 0.515 | 126 | no discrepancy |
| 258 | P18 | L3 | P18-L3 | 0.515 | 126 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 259 | P18 | SB1 | P18-SB1 | 0.783 | 6 | no discrepancy |
| 260 | P18 | SB2 | P18-SB2 | 0.891 | 3 | no discrepancy |

## Batch 27 — pages 261–270

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 261 | P18 | H | – | – | – | not part of website (out of scope) |
| 262 | P18 | H | – | – | – | not part of website (out of scope) |
| 263 | P18 | H | – | – | – | not part of website (out of scope) |
| 264 | P18 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 265 | P18 | LOES | – | – | – | not part of website (out of scope) |
| 266 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 267 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 268 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 269 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 270 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 28 — pages 271–280

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 271 | P19 | L1 | P19-L1 | 0.958 | 1 | no discrepancy |
| 272 | P19 | L1 | P19-L1 | 0.958 | 1 | no discrepancy |
| 273 | P19 | L2 | P19-L2 | 0.979 | 1 | no discrepancy |
| 274 | P19 | L2 | P19-L2 | 0.979 | 1 | no discrepancy |
| 275 | P19 | L3 | P19-L3 | 0.525 | 65 | no discrepancy |
| 276 | P19 | L3 | P19-L3 | 0.525 | 65 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 277 | P19 | SB1 | P19-SB1 | 0.802 | 1 | no discrepancy |
| 278 | P19 | SB2 | P19-SB2 | 0.877 | 0 | no discrepancy |
| 279 | P19 | H | – | – | – | not part of website (out of scope) |
| 280 | P19 | H | – | – | – | not part of website (out of scope) |

## Batch 29 — pages 281–290

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 281 | P19 | H | – | – | – | not part of website (out of scope) |
| 282 | P19 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 283 | P19 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 284 | P19 | LOES | – | – | – | not part of website (out of scope) |
| 285 | P20 | L1 | P20-L1 | 0.974 | 0 | no discrepancy |
| 286 | P20 | L1 | P20-L1 | 0.974 | 0 | no discrepancy |
| 287 | P20 | L2 | P20-L2 | 0.919 | 14 | no discrepancy |
| 288 | P20 | L2 | P20-L2 | 0.919 | 14 | no discrepancy |
| 289 | P20 | L3 | P20-L3 | 0.526 | 53 | no discrepancy |
| 290 | P20 | L3 | P20-L3 | 0.526 | 53 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |

## Batch 30 — pages 291–300

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 291 | P20 | SB1 | P20-SB1 | 0.774 | 0 | no discrepancy |
| 292 | P20 | SB2 | P20-SB2 | 0.876 | 1 | no discrepancy |
| 293 | P20 | H | – | – | – | not part of website (out of scope) |
| 294 | P20 | H | – | – | – | not part of website (out of scope) |
| 295 | P20 | H | – | – | – | not part of website (out of scope) |
| 296 | P20 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 297 | P20 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 298 | P20 | LOES | – | – | – | not part of website (out of scope) |
| 299 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 300 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 31 — pages 301–310

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 301 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 302 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 303 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 304 | P21 | L1 | P21-L1 | 0.965 | 2 | no discrepancy |
| 305 | P21 | L1 | P21-L1 | 0.965 | 2 | no discrepancy |
| 306 | P21 | L3 | P21-L3 | 0.486 | 101 | no discrepancy |
| 307 | P21 | L3 | P21-L3 | 0.486 | 101 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 308 | P21 | SB2 | P21-SB2 | 0.918 | 0 | no discrepancy |
| 309 | P21 | H | – | – | – | not part of website (out of scope) |
| 310 | P21 | H | – | – | – | not part of website (out of scope) |

## Batch 32 — pages 311–320

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 311 | P21 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 312 | P21 | LOES | – | – | – | not part of website (out of scope) |
| 313 | P22 | L1 | P22-L1 | 0.972 | 0 | no discrepancy |
| 314 | P22 | L1 | P22-L1 | 0.972 | 0 | no discrepancy |
| 315 | P22 | L2 | P22-L2 | 0.957 | 1 | no discrepancy |
| 316 | P22 | L2 | P22-L2 | 0.957 | 1 | no discrepancy |
| 317 | P22 | L3 | P22-L3 | 0.527 | 70 | no discrepancy |
| 318 | P22 | L3 | P22-L3 | 0.527 | 70 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 319 | P22 | SB1 | P22-SB1 | 0.845 | 1 | no discrepancy |
| 320 | P22 | SB2 | P22-SB2 | 0.891 | 2 | no discrepancy |

## Batch 33 — pages 321–330

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 321 | P22 | H | – | – | – | not part of website (out of scope) |
| 322 | P22 | H | – | – | – | not part of website (out of scope) |
| 323 | P22 | H | – | – | – | not part of website (out of scope) |
| 324 | P22 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 325 | P22 | LOES | – | – | – | not part of website (out of scope) |
| 326 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 327 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 328 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 329 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 330 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 34 — pages 331–340

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 331 | P23 | L1 | P23-L1 | 0.973 | 0 | no discrepancy |
| 332 | P23 | L1 | P23-L1 | 0.973 | 0 | no discrepancy |
| 333 | P23 | L2 | P23-L2 | 0.949 | 17 | no discrepancy |
| 334 | P23 | L2 | P23-L2 | 0.949 | 17 | no discrepancy |
| 335 | P23 | L3 | P23-L3 | 0.556 | 100 | no discrepancy |
| 336 | P23 | L3 | P23-L3 | 0.556 | 100 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 337 | P23 | SB1 | P23-SB1 | 0.793 | 6 | no discrepancy |
| 338 | P23 | SB2 | P23-SB2 | 0.869 | 1 | no discrepancy |
| 339 | P23 | H | – | – | – | not part of website (out of scope) |
| 340 | P23 | H | – | – | – | not part of website (out of scope) |

## Batch 35 — pages 341–350

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 341 | P23 | H | – | – | – | not part of website (out of scope) |
| 342 | P23 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 343 | P23 | LOES | – | – | – | not part of website (out of scope) |
| 344 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 345 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 346 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 347 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 348 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 349 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 350 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 36 — pages 351–360

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 351 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 352 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 353 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 354 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 355 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 356 | P24 | L1 | P24-L1 | 0.964 | 3 | no discrepancy |
| 357 | P24 | L1 | P24-L1 | 0.964 | 3 | no discrepancy |
| 358 | P24 | L2 | P24-L2 | 0.968 | 1 | no discrepancy |
| 359 | P24 | L2 | P24-L2 | 0.968 | 1 | no discrepancy |
| 360 | P24 | L3 | P24-L3 | 0.538 | 59 | no discrepancy |

## Batch 37 — pages 361–370

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 361 | P24 | SCHREIBEN | P24-L3 | 0.538 | 59 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 362 | P24 | SB1 | P24-SB1 | 0.818 | 0 | no discrepancy |
| 363 | P24 | SB2 | P24-SB2 | 0.871 | 4 | no discrepancy |
| 364 | P24 | H | – | – | – | not part of website (out of scope) |
| 365 | P24 | H | – | – | – | not part of website (out of scope) |
| 366 | P24 | H | – | – | – | not part of website (out of scope) |
| 367 | P24 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 368 | P24 | LOES | – | – | – | not part of website (out of scope) |
| 369 | P25 | L1 | P25-L1 | 0.965 | 2 | no discrepancy |
| 370 | P25 | L1 | P25-L1 | 0.965 | 2 | no discrepancy |

## Batch 38 — pages 371–380

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 371 | P25 | L2 | P25-L2 | 0.97 | 4 | no discrepancy |
| 372 | P25 | L2 | P25-L2 | 0.97 | 4 | no discrepancy |
| 373 | P25 | L3 | P25-L3 | 0.615 | 6 | no discrepancy |
| 374 | P25 | L3 | P25-L3 | 0.615 | 6 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 375 | P25 | SB1 | P25-SB1 | 0.799 | 1 | no discrepancy |
| 376 | P25 | SB2 | P25-SB2 | 0.913 | 0 | no discrepancy |
| 377 | P25 | H | – | – | – | not part of website (out of scope) |
| 378 | P25 | H | – | – | – | not part of website (out of scope) |
| 379 | P25 | H | – | – | – | not part of website (out of scope) |
| 380 | P25 | SCHREIBEN | – | – | – | not part of website (out of scope) |

## Batch 39 — pages 381–390

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 381 | P25 | LOES | – | – | – | not part of website (out of scope) |
| 382 | P26 | L1 | P26-L1 | 0.949 | 4 | no discrepancy |
| 383 | P26 | L1 | P26-L1 | 0.949 | 4 | no discrepancy |
| 384 | P26 | L2 | P26-L2 | 0.939 | 13 | no discrepancy |
| 385 | P26 | L2 | P26-L2 | 0.939 | 13 | no discrepancy |
| 386 | P26 | L3 | P26-L3 | 0.559 | 31 | no discrepancy |
| 387 | P26 | L3 | P26-L3 | 0.559 | 31 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 388 | P26 | SB1 | P26-SB1 | 0.804 | 0 | no discrepancy |
| 389 | P26 | SB2 | P26-SB2 | 0.872 | 1 | no discrepancy |
| 390 | P26 | H | – | – | – | not part of website (out of scope) |

## Batch 40 — pages 391–400

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 391 | P26 | H | – | – | – | not part of website (out of scope) |
| 392 | P26 | H | – | – | – | not part of website (out of scope) |
| 393 | P26 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 394 | P26 | LOES | – | – | – | not part of website (out of scope) |
| 395 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 396 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 397 | P27 | L1 | P27-L1 | 0.965 | 1 | no discrepancy |
| 398 | P27 | L1 | P27-L1 | 0.965 | 1 | no discrepancy |
| 399 | P27 | L2 | P27-L2 | 0.976 | 0 | no discrepancy |
| 400 | P27 | L2 | P27-L2 | 0.976 | 0 | no discrepancy |

## Batch 41 — pages 401–410

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 401 | P27 | L3 | P27-L3 | 0.547 | 38 | no discrepancy |
| 402 | P27 | L3 | P27-L3 | 0.547 | 38 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 403 | P27 | SB1 | P27-SB1 | 0.811 | 0 | no discrepancy |
| 404 | P27 | SB2 | P27-SB2 | 0.89 | 0 | no discrepancy |
| 405 | P27 | H | – | – | – | not part of website (out of scope) |
| 406 | P27 | H | – | – | – | not part of website (out of scope) |
| 407 | P27 | H | – | – | – | not part of website (out of scope) |
| 408 | P27 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 409 | P27 | LOES | – | – | – | not part of website (out of scope) |
| 410 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 42 — pages 411–420

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 411 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 412 | P28 | L1 | P28-L1 | 0.969 | 3 | no discrepancy |
| 413 | P28 | L1 | P28-L1 | 0.969 | 3 | no discrepancy |
| 414 | P28 | L2 | P28-L2 | 0.969 | 4 | no discrepancy |
| 415 | P28 | L2 | P28-L2 | 0.969 | 4 | no discrepancy |
| 416 | P28 | L3 | P28-L3 | 0.564 | 27 | no discrepancy |
| 417 | P28 | L3 | P28-L3 | 0.564 | 27 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 418 | P28 | SB1 | P28-SB1 | 0.818 | 1 | no discrepancy |
| 419 | P28 | SB2 | P28-SB2 | 0.89 | 0 | no discrepancy |
| 420 | P28 | H | – | – | – | not part of website (out of scope) |

## Batch 43 — pages 421–430

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 421 | P28 | H | – | – | – | not part of website (out of scope) |
| 422 | P28 | H | – | – | – | not part of website (out of scope) |
| 423 | P28 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 424 | P28 | LOES | – | – | – | not part of website (out of scope) |
| 425 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 426 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 427 | P29 | L1 | P29-L1 | 0.951 | 11 | no discrepancy |
| 428 | P29 | L1 | P29-L1 | 0.951 | 11 | no discrepancy |
| 429 | P29 | L2 | P29-L2 | 0.938 | 11 | no discrepancy |
| 430 | P29 | L2 | P29-L2 | 0.938 | 11 | no discrepancy |

## Batch 44 — pages 431–440

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 431 | P29 | L3 | P29-L3 | 0.466 | 101 | no discrepancy |
| 432 | P29 | L3 | P29-L3 | 0.466 | 101 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild |
| 433 | P29 | SB1 | P29-SB1 | 0.844 | 1 | no discrepancy |
| 434 | P29 | SB2 | P29-SB2 | 0.909 | 3 | no discrepancy |
| 435 | P29 | H | – | – | – | not part of website (out of scope) |
| 436 | P29 | H | – | – | – | not part of website (out of scope) |
| 437 | P29 | H | – | – | – | not part of website (out of scope) |
| 438 | P29 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 439 | P29 | LOES | – | – | – | not part of website (out of scope) |
| 440 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 45 — pages 441–450

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 441 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 442 | P30 | L1 | P30-L1 | 0.97 | 1 | no discrepancy |
| 443 | P30 | L1 | P30-L1 | 0.97 | 1 | no discrepancy |
| 444 | P30 | L2 | P30-L2 | 0.961 | 4 | no discrepancy |
| 445 | P30 | L2 | P30-L2 | 0.961 | 4 | no discrepancy |
| 446 | P30 | L3 | P30-L3 | 0.541 | 113 | no discrepancy |
| 447 | P30 | L3 | P30-L3 | 0.541 | 113 | ad photo: OCR differences = photo noise; transcription re-checked during ad rebuild — ads a–c blurred, reconstruction marked |
| 448 | P30 | SB1 | P30-SB1 | 0.798 | 1 | no discrepancy |
| 449 | P30 | SB2 | P30-SB2 | 0.902 | 0 | no discrepancy |
| 450 | P30 | H | – | – | – | not part of website (out of scope) |

## Batch 46 — pages 451–460

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 451 | P30 | H | – | – | – | not part of website (out of scope) |
| 452 | P30 | H | – | – | – | not part of website (out of scope) |
| 453 | P30 | SCHREIBEN | – | – | – | not part of website (out of scope) |
| 454 | P30 | LOES | – | – | – | not part of website (out of scope) |
| 455 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 456 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 457 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 458 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 459 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 460 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 47 — pages 461–470

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 461 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 462 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 463 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 464 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 465 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 466 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 467 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 468 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 469 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 470 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 48 — pages 471–480

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 471 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 472 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 473 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 474 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 475 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 476 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 477 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 478 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 479 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 480 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 49 — pages 481–490

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 481 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 482 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 483 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 484 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 485 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 486 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 487 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 488 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 489 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 490 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |

## Batch 50 — pages 491–493

| Page | Paper | Content | Website exercise(s) | Similarity | Web words not in OCR | Result |
|---|---|---|---|---|---|---|
| 491 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 492 | SPEAKING | MUENDLICH | – | – | – | not part of website (out of scope) |
| 493 | OTHER | ? | – | – | – | not part of website (out of scope) |
