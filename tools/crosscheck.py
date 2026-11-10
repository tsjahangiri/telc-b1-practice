"""Second-pass audit: compare website data words vs independent OCR words of the source pages.
Writes audit/crosscheck/<id>.txt with diff hunks. Usage: crosscheck.py [ids...]"""
import json, re, sys, os, difflib, unicodedata
D = json.loads(open("website/data/exercises.js").read().split("=", 1)[1].rstrip().rstrip(";"))["exercises"]
def ocr_words(p):
    f = f"extraction/ocr/p{p:03d}.txt"
    rows = []
    for l in open(f):
        m = re.match(r'([\d.]+) ([\d.]+) ([\d.]+)\t(.*)', l.rstrip("\n"))
        if m: rows.append((float(m.group(1)), float(m.group(2)), m.group(4)))
    return " ".join(r[2] for r in rows)
def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = re.sub(r"\[\[\d+\]\]", " ", s)
    s = s.replace("„", '"').replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-").replace("’", "'")
    return [w for w in re.findall(r"[A-Za-zÄÖÜäöüß0-9]+(?:[-'.][A-Za-zÄÖÜäöüß0-9]+)*", s)]
def web_text(e):
    t = e["type"]; parts = [e.get("instructions", "")]
    if t == "lesen1": parts += [h["text"] for h in e["headings"]] + [x["text"] for x in e["texts"]]
    if t == "lesen2": parts += [e.get("title") or "", e.get("subtitle") or "", e["text"]] + [q["stem"] + " " + " ".join(q["options"].values()) for q in e["questions"]]
    if t == "lesen3": parts += [s["text"] for s in e["situations"]] + [a["text"] for a in e["ads"]]
    if t == "sprach1": parts += [e["text"]] + [" ".join(g["options"].values()) for g in e["gaps"]]
    if t == "sprach2": parts += [e["text"]] + [w["word"] for w in e["words"]]
    return " ".join(parts)
os.makedirs("audit/crosscheck", exist_ok=True)
ids = sys.argv[1:] or [e["id"] for e in D]
summary = []
for e in D:
    if e["id"] not in ids: continue
    W = norm(web_text(e)); O = norm(" ".join(ocr_words(p) for p in e["pages"]))
    oset = {}
    for w in O: oset[w.lower()] = oset.get(w.lower(), 0) + 1
    # words in website not found anywhere in OCR (candidate errors in website or OCR noise)
    miss = [w for w in W if w.lower() not in oset and not re.fullmatch(r"\d", w)]
    wset = {w.lower() for w in W}
    extra = [w for w in O if w.lower() not in wset and len(w) > 3]
    sm = difflib.SequenceMatcher(None, [w.lower() for w in W], [w.lower() for w in O], autojunk=False)
    ratio = round(sm.ratio(), 3)
    out = [f"# {e['id']} pages {e['pages']} ratio {ratio}", "## website words not in OCR:", " ".join(miss), "## OCR words (len>3) not in website:", " ".join(extra)]
    open(f"audit/crosscheck/{e['id']}.txt", "w").write("\n".join(out) + "\n")
    summary.append((e["id"], len(W), len(miss), len(extra), ratio))
for s in summary: print(*s)
