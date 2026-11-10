"""Answer-key audit: website solutions vs key pages (text layer words + OCR) + word consistency for SB1/SB2."""
import json, re
import pymupdf as fitz
d = fitz.open("source/original.pdf")
D = json.loads(open("website/data/exercises.js").read().split("=", 1)[1].rstrip().rstrip(";"))["exercises"]
def pairs_from_rows(rows):
    """rows: list of (y,x,text). returns {num:[tokens after it on same row]}"""
    res = {}
    rows = sorted(rows)
    lines = []
    for y, x, t in rows:
        if lines and abs(lines[-1][0] - y) < 4: lines[-1][1].append((x, t))
        else: lines.append([y, [(x, t)]])
    for y, toks in lines:
        toks.sort()
        for i, (x, t) in enumerate(toks):
            if re.fullmatch(r"\d{1,2}", t) and 1 <= int(t) <= 40:
                nxt = [tt for xx, tt in toks[i + 1:i + 4] if xx - x < 140]
                res.setdefault(int(t), []).append(nxt)
    return res
def textlayer(p):
    return pairs_from_rows([(w[1], w[0], w[4]) for w in d[p - 1].get_text("words")])
def ocr(p):
    rows = []
    for l in open(f"extraction/ocr/p{p:03d}.txt"):
        m = re.match(r"([\d.]+) ([\d.]+) ([\d.]+)\t(.*)", l.rstrip("\n"))
        if not m: continue
        y, x = float(m.group(1)) * 842, float(m.group(2)) * 595
        for k, tok in enumerate(m.group(4).split()): rows.append((y, x + k * 12, tok))
    return pairs_from_rows(rows)
rows_out = []; problems = []
for e in D:
    kp = e["key_page"]; TL = textlayer(kp); OC = ocr(kp)
    for n, sol in e["solution"].items():
        n_ = int(n)
        cands = TL.get(n_, []) + OC.get(n_, [])
        letters = set()
        for c in cands:
            if c and re.fullmatch(r"[A-Oa-oXx]", c[0]): letters.add(c[0].lower())
            elif c and re.fullmatch(r"[A-Oa-oXx][A-ZÄÖÜa-zäöüß]+", c[0]) and e["type"] == "sprach2": letters.add(c[0][0].lower())
        word = None
        if e["type"] in ("sprach1", "sprach2"):
            for c in TL.get(n_, []):
                if len(c) >= 2 and re.fullmatch(r"[A-Oa-o]", c[0]): word = " ".join(c[1:2]); break
        status = "Verified"; note = ""
        if letters and sol not in letters: status = "MISMATCH"; note = f"key page shows {sorted(letters)}"
        if not letters: status = "CHECK"; note = "number/letter not machine-readable on key page"
        if word:
            web_word = e["gaps"] and next((g["options"][sol] for g in e.get("gaps", []) if g["num"] == n_), None) if e["type"] == "sprach1" else next((w["word"] for w in e["words"] if w["key"] == sol), None)
            if web_word and web_word.split()[0].lower() != word.lower():
                status = "WORD-MISMATCH" if status == "Verified" else status; note += f" key word '{word}' vs option '{web_word}'"
            else: note += f" word '{word}' ✓"
        rows_out.append((e["id"], n_, sol, sorted(letters), status, note.strip(), e["duplicate_of"]))
        if status != "Verified": problems.append(rows_out[-1])
json.dump(rows_out, open("audit/keycheck.json", "w"), ensure_ascii=False)
print(len(rows_out), "answers checked;", len(problems), "need review")
for p in problems: print(p)
