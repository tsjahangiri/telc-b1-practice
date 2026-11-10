"""Extract Hörverstehen (Teil 1–3) for every paper.

  text layer (or OCR for image pages)  +  extraction/corrections/hoeren.json (manual fixes)
    -> extraction/hoeren/PNN.json   and a dump for visual comparison

Each part:  {id, part, type:'hoeren', instructions, statements:[{num,text}], solution:{num:'+'|'-'},
             topic, pages, answer_key_page}
Key: on the Lösungen page each number 41–60 sits in the 'Hörverstehen (Teil n)' column with its
sign (+ / -) printed immediately to the right on the same line.  Solutions are taken only from there.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import draft
from lines import lines

d = draft.d
ARABIC = re.compile(r'[؀-ۿ]')
RANGES = {1: range(41, 46), 2: range(46, 56), 3: range(56, 61)}
SIGNS = {'+': '+', '-': '-', '–': '-', '—': '-', '−': '-'}
FIX = json.load(open("extraction/corrections/hoeren.json")) if os.path.exists("extraction/corrections/hoeren.json") else {}


def ocr_lines(p):
    f = f"extraction/ocr/p{p:03d}.txt"
    if not os.path.exists(f):
        return []
    return [l.split("\t", 1)[1] for l in open(f).read().splitlines() if "\t" in l]


def page_lines(p):
    t = [r[3].strip() for r in lines(p) if not ARABIC.search(r[3])]
    nums = sum(1 for l in t if re.match(r'^\d\d\s*\.', l))
    if nums >= 3:
        return t, "text_layer"
    o = [l.strip() for l in ocr_lines(p)]
    return o, "ocr"


def part_of(ls):
    for l in ls:
        m = re.search(r'H[öo]rverstehen,?\s*Teil\s*(\d)', l)
        if m:
            return int(m.group(1))
    s = " ".join(ls)
    m = re.search(r'Aussagen\s*(\d\d)', s)
    if m:
        return {41: 1, 46: 2, 56: 3}.get(int(m.group(1)))
    return None


def parse_page(p):
    ls, src = page_lines(p)
    part = part_of(ls)
    instr, stm, cur, seen_head = [], [], None, False
    for l in ls:
        if not l or 'LANGUAGE Tests' in l or re.match(r'^H[öo]rverstehen,?\s*Teil', l) or 'telcc1hochschul' in l:
            continue
        if re.fullmatch(r'[.…·\s]{5,}', l):
            seen_head = True
            continue
        m = re.match(r'^(\d\d)\s*\.\s*(.*)$', l)
        if m and 40 < int(m.group(1)) <= 60:
            cur = {"num": int(m.group(1)), "text": m.group(2).strip()}
            stm.append(cur)
            continue
        if cur is not None:
            cur["text"] = (cur["text"] + " " + l).strip()
        elif not seen_head and (instr or l.startswith("Sie hören")):
            instr.append(l)
    return {"page": p, "part": part, "source": src, "instructions": instr, "statements": stm}


def key_page_hv(p):
    """-> ({num: sign}, {part: topic})"""
    ws = d[p - 1].get_text("words")
    heads = {}
    for i, w in enumerate(ws):
        if w[4].startswith("Hörverstehen") and i + 2 < len(ws):
            m = re.match(r'(\d)', ws[i + 2][4]) if ws[i + 1][4] == "(Teil" else re.match(r'\(Teil(\d)', ws[i + 1][4])
            if m:
                heads[int(m.group(1))] = (w[0], w[1])
    sol, topics = {}, {}
    for part, (hx, hy) in heads.items():
        cand = [w for w in ws if 0 < w[1] - hy < 30 and -40 < w[0] - hx < 110 and not w[4].startswith('@')
                and not re.match(r'^\d+$', w[4]) and w[4] not in SIGNS]
        if cand:
            row = min(cand, key=lambda w: w[1])[1]
            topics[part] = " ".join(w[4] for w in sorted([w for w in cand if abs(w[1] - row) < 4], key=lambda w: w[0]))
        for n in RANGES[part]:
            nw = [w for w in ws if w[4].strip(".") == str(n) and hy < w[1] < hy + 220 and -30 < w[0] - hx < 120]
            if not nw:
                continue
            nw = min(nw, key=lambda w: abs(w[0] - hx))
            sg = [w for w in ws if w[4] in SIGNS and abs(w[1] - nw[1]) < 7 and 0 < w[0] - nw[0] < 45]
            if len(sg) == 1:
                sol[n] = SIGNS[sg[0][4]]
    return sol, topics


def build(pid, first, last, key_page):
    parts = {}
    for p in range(first, last + 1):
        if draft.section_of(p) != 'H' and 'Hörverstehen, Teil' not in d[p - 1].get_text():
            continue
        r = parse_page(p)
        if r["part"] is None or not r["statements"]:
            continue
        parts.setdefault(r["part"], r)
    sol, topics = key_page_hv(key_page)
    fx = FIX.get(pid, {})
    for k, v in fx.get("pages", {}).items():
        parts[int(k)] = parse_page(v) | {"page": v}
    out = []
    for part in sorted(parts):
        r = parts[part]
        ex = {"id": f"{pid}-H{part}", "type": "hoeren", "part": part,
              "section": f"Hörverstehen, Teil {part}",
              "instructions": "\n".join(r["instructions"]), "statements": r["statements"],
              "pages": [r["page"]], "text_source": r["source"], "answer_key_page": key_page,
              "topic": topics.get(part)}
        ex = json.loads(apply(json.dumps(ex, ensure_ascii=False), fx.get("fixes", []), f"H{part}"))
        s = {str(n): sol[n] for n in RANGES[part] if n in sol}
        s.update(fx.get("solution_fixes", {}).get(f"H{part}", {}))
        ex["solution"] = {k: s[k] for k in sorted(s, key=int)}
        ex["solution_complete"] = len(s) == len(RANGES[part])
        ex["notes"] = fx.get("notes", {}).get(f"H{part}", [])
        ex["uncertain"] = fx.get("uncertain", {}).get(f"H{part}", [])
        ex["verified"] = bool(fx.get("verified", {}).get(f"H{part}"))
        out.append(ex)
    return out


def apply(s, fixes, sec):
    for f in fixes:
        if f[0] != sec:
            continue
        a, b = json.dumps(f[1], ensure_ascii=False)[1:-1], json.dumps(f[2], ensure_ascii=False)[1:-1]
        if s.count(a) != 1:
            raise SystemExit(f"hoeren fix {sec} matched {s.count(a)}: {f[1]!r}")
        s = s.replace(a, b)
    return s


def dump(pid, exs):
    o = []
    for e in exs:
        o.append(f"=== {e['id']} [{e['topic']}] p{e['pages']} src={e['text_source']} key p{e['answer_key_page']}")
        o.append("INSTR: " + e["instructions"].replace("\n", " / "))
        for s in e["statements"]:
            o.append(f"  {s['num']}. {s['text']}   [{e['solution'].get(str(s['num']), '??')}]")
        o.append(f"  nums={[s['num'] for s in e['statements']]} complete={e['solution_complete']}")
    return "\n".join(o)


if __name__ == "__main__":
    idx = json.load(open("extraction/papers_index.json"))
    os.makedirs("extraction/hoeren", exist_ok=True)
    only = sys.argv[1:]
    for x in idx:
        pid = x["paper"]
        if only and pid not in only:
            continue
        kp = json.load(open(f"extraction/papers/{pid}.json"))["answer_key_page"]
        exs = build(pid, x["first"], x["last"], kp)
        json.dump(exs, open(f"extraction/hoeren/{pid}.json", "w"), ensure_ascii=False, indent=1)
        txt = dump(pid, exs)
        open(f"extraction/hoeren/{pid}.dump.txt", "w").write(txt)
        if only:
            print(txt)
        else:
            st = [(e["part"], len(e["statements"]), e["solution_complete"], e["text_source"]) for e in exs]
            print(pid, st)
