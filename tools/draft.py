"""Draft structured exercises for one paper from the PDF text layer (positional).
Output is a DRAFT: every exercise must be visually verified against the page images
before being marked verified. Usage: python3 tools/draft.py P01
"""
import pymupdf as fitz, re, json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from lines import lines, d

ARABIC = re.compile(r'[؀-ۿ]')
HEADER_RE = re.compile(r'^(Leseverstehen|Sprach\w*|LANGUAGE Tests|Hörverstehen)', re.I)


def clean_lines(pno):
    out = []
    for r in lines(pno):
        t = r[3]
        if ARABIC.search(t):
            continue
        if re.match(r'^\s*(Leseverstehen,?\s*Teil\s*\d|Sprach\w*,?\s*Teil\s*\d|LANGUAGE Tests)\s*$', t):
            continue
        out.append(r)
    return out


def section_of(pno):
    t = d[pno - 1].get_text()
    f = f"extraction/ocr/p{pno:03d}.txt"
    o = open(f).read() if os.path.exists(f) else ""
    s = t + "\n" + o
    m = re.search(r'Leseverstehen,?\s*Teil\s*(\d)', s)
    if re.search(r'^\s*Lösungen\s*$', t, re.M) and 'Leseverstehen (Teil' in t:
        return 'LOES'
    if m:
        return 'L' + m.group(1)
    m = re.search(r'Sprach\w*,?\s*Teil\s*(\d)', s)
    if m:
        return 'SB' + m.group(1)
    if 'Sie hören' in s:
        return 'H'
    return '?'


def para_join(rows):
    """Join positioned lines into paragraphs using vertical gaps."""
    paras, cur, last_y, last_size, prev_sub = [], [], None, None, False
    body_bold = sum(1 for r in rows if r[5]) > len(rows) / 2
    maxright = max((r[2] for r in rows), default=0)
    prev_short = False
    for r in rows:
        y, size = r[0], r[4] or 12
        t = r[3].strip()
        is_sub = (r[5] and not body_bold and len(t) < 70 and not t.endswith((',', '-')))
        if last_y is not None and (y - last_y > 1.75 * max(size, last_size) or is_sub or prev_sub or prev_short):
            paras.append(cur); cur = []
        cur.append(("## " if is_sub else "") + t)
        last_y, last_size, prev_sub = y, size, is_sub
        prev_short = r[2] < maxright - 120 and maxright - r[1] > 250
    if cur:
        paras.append(cur)
    res = []
    for p in paras:
        s = ""
        for l in p:
            if s.endswith('-') and not s.endswith(' -'):
                s = s + l  # keep hyphen as printed (do not dehyphenate words)
            else:
                s = (s + " " + l).strip()
        res.append(re.sub(r'\s+', ' ', s).strip())
    return [p for p in res if p]


INSTR_RE = re.compile(r'^(Lesen [Ss]ie|Markieren [Ss]ie|Sie können|jede Anzeige|Antwortbogen|Wenn Sie|[.…\-_]{8,})')


def parse_L1(pages):
    headings, texts, instr = [], [], []
    rows = [r for p in pages for r in clean_lines(p)]
    cur = None
    for r in rows:
        t = r[3].strip()
        m = re.match(r'^_*\s*([a-jA-J])\s*\)\s*(.*)$', t)
        n = re.match(r'^([1-5])\s*\.\s+(.*)$', t)
        if m and not texts:
            headings.append({"key": m.group(1).lower(), "text": m.group(2).strip()}); cur = None; continue
        if n:
            cur = {"num": int(n.group(1)), "lines": [r]}
            r2 = (r[0], r[1], r[2], n.group(2), r[4], r[5]); cur["lines"] = [r2]
            texts.append(cur); continue
        if cur is not None:
            cur["lines"].append(r)
        elif not headings:
            instr.append(t)
    for tx in texts:
        tx["text"] = "\n".join(para_join(tx.pop("lines")))
    return {"type": "lesen1", "instructions": " ".join(i for i in instr if not re.match(r'^[.…\-_ ]+$', i)),
            "headings": headings, "texts": texts}


def parse_L2(pages):
    rows = [(p, r) for p in pages for r in clean_lines(p)]
    instr, body, qs = [], [], []
    cur = None
    pending_num = None
    for p, r in rows:
        t = r[3].strip()
        if re.fullmatch(r'(6|7|8|9|10)\s*\.', t):
            pending_num = int(t.rstrip('. ')); continue
        if pending_num is not None and r[5]:
            cur = {"num": pending_num, "stem": t, "opt_rows": []}; qs.append(cur); pending_num = None; continue
        q = re.match(r'^(6|7|8|9|10)\s*\.\s+(.*)$', t)
        if q:
            cur = {"num": int(q.group(1)), "stem": q.group(2).strip(), "opt_rows": []}
            qs.append(cur); continue
        if cur is not None:
            if re.fullmatch(r'[ABC]', t):
                continue
            cur["opt_rows"].append(r); continue
        if INSTR_RE.match(t) and not body:
            instr.append(t); continue
        body.append(r)
    for q in qs:
        rws = q.pop("opt_rows")
        opts, last = [], None
        for r in rws:
            t = re.sub(r'^[ABC]\s+', '', r[3].strip())
            if last is None or r[0] - last > 1.6 * (r[4] or 12):
                opts.append(t)
            else:
                opts[-1] += " " + t
            last = r[0]
        q["options"] = {k: v for k, v in zip("abc", opts)}
        if len(opts) != 3:
            q["_flag"] = f"parsed {len(opts)} options"
            q["_raw_options"] = opts
    title, subtitle = None, None
    if body and body[0][4] >= 14:
        title = body.pop(0)[3].strip()
        if body and body[0][4] >= 13 and body[0][5]:
            subtitle = body.pop(0)[3].strip()
    paras = para_join(body)
    return {"type": "lesen2", "instructions": " ".join(i for i in instr if not re.match(r'^[.…\-_ ]+$', i)),
            "title": title, "subtitle": subtitle, "text": "\n".join(paras), "questions": qs}


def parse_L3(pages):
    rows = [r for p in pages for r in clean_lines(p)]
    instr, sits, cur = [], [], None
    for r in rows:
        t = r[3].strip()
        m = re.match(r'^(1[1-9]|20)\s*\.\s*(.*)$', t)
        if m:
            cur = {"num": int(m.group(1)), "text": m.group(2).strip()}; sits.append(cur); continue
        if cur is not None and r[1] > 40 and not re.match(r'^\d', t):
            cur["text"] += " " + t; continue
        if not sits and not re.match(r'^[.…\-_ ]+$', t):
            instr.append(t)
    return {"type": "lesen3", "instructions": " ".join(instr), "situations": sits, "ads": [],
            "_flag": "ads must be transcribed from page image"}


GAP_RE = re.compile(r'\(\s*(\d{2})\s*\)|_{2,}\s*(\d{2})\s*_{2,}')


def norm_gaps(s):
    return GAP_RE.sub(lambda m: "[[" + (m.group(1) or m.group(2)) + "]]", s)


def parse_SB1(pages):
    rows = [(p, r) for p in pages for r in clean_lines(p)]
    words = []
    for p in pages:
        for w in d[p - 1].get_text("words"):
            words.append((p, w[0], w[1], w[2], w[3], w[4]))
    nums = [(p, x0, y0) for p, x0, y0, x1, y1, t in words if re.fullmatch(r'(2[1-9]|30)\.', t)]
    nums_k = {}
    for p, x0, y0, x1, y1, t in words:
        m = re.fullmatch(r'(2[1-9]|30)\.', t)
        if m:
            nums_k[int(m.group(1))] = (p, x0, y0)
    gaps = []
    for n in range(21, 31):
        if n not in nums_k:
            gaps.append({"num": n, "options": {}, "_flag": "number not found in text layer"}); continue
        p, x, y = nums_k[n]
        same_p = [v for k, v in nums_k.items() if v[0] == p]
        right = [v[1] for v in same_p if v[1] > x + 20 and abs(v[2] - y) < 40]
        xmax = min(right) - 5 if right else 1e9
        below = [v[2] for v in same_p if v[2] > y + 25 and abs(v[1] - x) < 40]
        ymax = min(below) - 8 if below else y + 80
        cand = [w for w in words if w[0] == p and w[1] > x + 15 and w[1] < xmax and w[2] > y - 6 and w[2] < ymax
                and not re.fullmatch(r'[ABC]', w[5]) and not re.fullmatch(r'(2[1-9]|30)\.', w[5])]
        cand.sort(key=lambda w: (w[2], w[1]))
        linesw = []
        for w in cand:
            if linesw and abs(w[2] - linesw[-1][-1][2]) < 6:
                linesw[-1].append(w)
            else:
                linesw.append([w])
        opts = [" ".join(w[5] for w in sorted(l, key=lambda w: w[1])) for l in linesw]
        g = {"num": n, "options": {k: v for k, v in zip("abc", opts)}}
        if len(opts) != 3:
            g["_flag"] = f"parsed {len(opts)} options: {opts}"
        gaps.append(g)
    # text: rows that are above the first option number on its page
    first_num_y = {}
    for n, (p, x, y) in nums_k.items():
        first_num_y[p] = min(first_num_y.get(p, 1e9), y)
    instr, body = [], []
    for p, r in rows:
        t = r[3].strip()
        if p in first_num_y and r[0] >= first_num_y[p] - 4:
            continue
        if re.fullmatch(r'[ABC]', t):
            continue
        if INSTR_RE.match(t) and not body:
            if not re.match(r'^[.…\-_ ]+$', t):
                instr.append(t)
            continue
        body.append(r)
    return {"type": "sprach1", "instructions": " ".join(instr), "text": norm_gaps("\n".join(para_join(body))), "gaps": gaps}


def parse_SB2(pages):
    words = []
    for p in pages:
        for w in d[p - 1].get_text("words"):
            words.append((p, w[0], w[1], w[2], w[3], w[4]))
    letters = [w for w in words if re.fullmatch(r'[a-o]', w[5])]
    bank = {}
    for L in letters:
        same = [w for w in words if w[0] == L[0] and abs(w[2] - L[2]) < 5 and w[1] > L[3] and w[1] < L[3] + 120
                and not re.fullmatch(r'[a-o]', w[5])]
        same.sort(key=lambda w: w[1])
        if same and same[0][5].isupper():
            # stop at next letter
            nxt = [w[1] for w in letters if w[0] == L[0] and abs(w[2] - L[2]) < 5 and w[1] > L[1]]
            lim = min(nxt) if nxt else 1e9
            bank[L[5]] = " ".join(w[5] for w in same if w[1] < lim)
    # inline "c DESWEGEN" style
    for w in words:
        pass
    for p in pages:
        for r in clean_lines(p):
            for m in re.finditer(r'(?:^|\s)([a-o])\s+([A-ZÄÖÜ][A-ZÄÖÜß]+)', r[3]):
                bank.setdefault(m.group(1), m.group(2))
    bank_y = {}
    for L in letters:
        if L[5] in bank:
            bank_y[L[0]] = min(bank_y.get(L[0], 1e9), L[2])
    instr, body = [], []
    for p in pages:
        for r in clean_lines(p):
            t = r[3].strip()
            if p in bank_y and r[0] >= bank_y[p] - 4:
                continue
            if re.match(r'^(Lesen sie den Text|Lücken 31|\(a\s*[,–-]\s*o\)|Markieren Sie|Aufgaben 31|Antwortbogen)', t, re.I) and r[1] < 300 and not body or (r[1] > 300 and re.match(r'^(Lesen|Lücken|\(a|Markieren|Aufgaben|Antwortbogen|Wörter)', t)):
                instr.append(t); continue
            body.append(r)
    return {"type": "sprach2", "instructions": " ".join(instr), "text": norm_gaps("\n".join(para_join(body))),
            "words": [{"key": k, "word": bank[k]} for k in sorted(bank)]}


def loes_titles(p):
    out = []
    for b in d[p - 1].get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s_ in l["spans"]:
                c = s_["color"]; r_, g_, b_ = c >> 16 & 255, c >> 8 & 255, c & 255
                if s_["text"].strip() and r_ > 150 and g_ < 80 and b_ < 80:
                    out.append((round(l["bbox"][1]), round(l["bbox"][0]), s_["text"].strip()))
    return sorted(out)


def parse_LOES(p):
    words = [w for w in d[p - 1].get_text("words")]
    sol = {}
    toks = sorted(words, key=lambda w: (round(w[1] / 4), w[0]))
    rowsd = {}
    for w in words:
        rowsd.setdefault(round(w[1] / 4), []).append(w)
    for k, ws in rowsd.items():
        ws.sort(key=lambda w: w[0])
        for i, w in enumerate(ws):
            if re.fullmatch(r'\d{1,2}', w[4]) and 1 <= int(w[4]) <= 60 and i + 1 < len(ws):
                nx = ws[i + 1]
                if nx[0] - w[2] < 40 and re.fullmatch(r'[A-Oa-oXx+\-–]|[A-Oa-oXx][A-ZÄÖÜa-zäöüß]+', nx[4]):
                    sol[int(w[4])] = nx[4]
    return sol


PARSERS = {"L1": parse_L1, "L2": parse_L2, "L3": parse_L3, "SB1": parse_SB1, "SB2": parse_SB2}

if __name__ == "__main__":
    pid = sys.argv[1]
    idx = {x["paper"]: x for x in json.load(open("extraction/papers_index.json"))}[pid]
    secs = {}
    for p in range(idx["first"], idx["last"] + 1):
        s = section_of(p)
        secs.setdefault(s, []).append(p)
    print(pid, secs)
