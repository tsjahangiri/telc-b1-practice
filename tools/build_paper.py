"""Build verified structured data for one paper.

draft (text layer / OCR)  +  extraction/corrections/<PID>.json (manual, from visual comparison)
  -> extraction/papers/<PID>.json

Corrections file format:
{
  "sections": {"L1": [1,2], ...}          optional override of page->section assignment
  "manual":   {"L3": {...full exercise...}} optional: exercise written entirely by hand (image pages)
  "ads": {"page": 6, "boxes": {"a": [x0,y0,x1,y1], ...}}
  "ad_fixes": [["a", "from", "to"], ...]   exact substring replacements inside ad text
  "fixes": [["L2", "from", "to"], ...]     exact substring replacement inside the exercise JSON (must match once)
  "solution_fixes": {"L1": {"1": "j"}}    only when the key page was misparsed (never invented)
  "notes": {"L1": ["..."]}, "uncertain": {"L1": [{"location": "...", "note": "..."}]}
  "verified": {"L1": true, ...}
}
"""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
import draft
from adtext import collect

SEC_ORDER = ["L1", "L2", "L3", "SB1", "SB2"]
SOL_RANGE = {"L1": range(1, 6), "L2": range(6, 11), "L3": range(11, 21), "SB1": range(21, 31), "SB2": range(31, 41)}
LABELS = {"L1": "Leseverstehen, Teil 1", "L2": "Leseverstehen, Teil 2", "L3": "Leseverstehen, Teil 3",
          "SB1": "Sprachbausteine, Teil 1", "SB2": "Sprachbausteine, Teil 2"}
KEY_LABELS = {"L1": "Leseverstehen (Teil 1)", "L2": "Leseverstehen (Teil 2)", "L3": "Leseverstehen (Teil 3)",
              "SB1": "Sprachbausteine (Teil 1)", "SB2": "Sprachbausteine (Teil 2)"}


def key_titles(p):
    """Map section -> red topic label on the Lösungen page using position under the column headers."""
    words = draft.d[p - 1].get_text("dict")
    heads = {}
    for b in words["blocks"]:
        for l in b.get("lines", []):
            t = "".join(s["text"] for s in l["spans"]).strip()
            for k, lab in KEY_LABELS.items():
                if t.startswith(lab.split(" (")[0]) and lab.split(" ")[-1] in t.replace(" ", " "):
                    if re.search(r'\(Teil\s*%s\)' % lab[-2], t):
                        heads[k] = (l["bbox"][0], l["bbox"][1])
    titles = draft.loes_titles(p)
    out = {}
    for k, (hx, hy) in heads.items():
        cands = [t for t in titles if 0 < t[0] - hy < 40 and abs(t[1] - hx) < 120]
        if cands:
            out[k] = min(cands, key=lambda t: (t[0] - hy) + abs(t[1] - hx))[2]
    return out


def apply_fixes(obj, fixes, sec):
    s = json.dumps(obj, ensure_ascii=False)
    for f in fixes:
        if f[0] != sec:
            continue
        a, b = json.dumps(f[1], ensure_ascii=False)[1:-1], json.dumps(f[2], ensure_ascii=False)[1:-1]
        if s.count(f[1]) == 1 and s.count(a) != 1:
            a, b = f[1], f[2]
        n = s.count(a)
        if n != 1:
            raise SystemExit(f"fix for {sec} matched {n} times: {f[1]!r}")
        s = s.replace(a, b)
    return json.loads(s)


def build(pid):
    idx = {x["paper"]: x for x in json.load(open("extraction/papers_index.json"))}[pid]
    cpath = f"extraction/corrections/{pid}.json"
    corr = json.load(open(cpath)) if os.path.exists(cpath) else {}
    secs = {}
    for p in range(idx["first"], idx["last"] + 1):
        secs.setdefault(draft.section_of(p), []).append(p)
    for k, v in corr.get("sections", {}).items():
        for kk in list(secs):
            secs[kk] = [p for p in secs[kk] if p not in v]
        secs[k] = v
    loes_page = (secs.get("LOES") or [idx["last"]])[-1]
    sol = draft.parse_LOES(loes_page)
    titles = key_titles(loes_page)
    paper = {"id": pid, "pages": [idx["first"], idx["last"]], "answer_key_page": loes_page,
             "page_sections": {k: v for k, v in secs.items()}, "exercises": []}
    for sec in SEC_ORDER:
        pages = secs.get(sec)
        manual = corr.get("manual", {}).get(sec)
        if not pages and not manual:
            continue
        if manual:
            ex = dict(manual)
        else:
            ex = draft.PARSERS[sec](pages)
        if sec == "L3" and "ads_manual" in corr and not manual:
            ex["ads"] = [{"key": k, "text": v} for k, v in sorted(corr["ads_manual"]["ads"].items())]
            ex["ads_image_page"] = corr["ads_manual"]["page"]
            ex.pop("_flag", None)
        if sec == "L3" and "ads" in corr and not manual:
            a = corr["ads"]
            got = collect(a["page"], {k: tuple(v) for k, v in a["boxes"].items()})
            ads = []
            for k in sorted(got):
                ls = [l[3] for l in got[k]]
                if ls and ls[0].strip().lower() in (k, k + ")", k + " /"):
                    ls = ls[1:]
                ads.append({"key": k, "text": "\n".join(ls)})
            for key, fr, to in corr.get("ad_fixes", []):
                ad = next(x for x in ads if x["key"] == key)
                if fr == "*":
                    ad["text"] = to; continue
                if ad["text"].count(fr) != 1:
                    raise SystemExit(f"ad fix {key} matched {ad['text'].count(fr)}: {fr!r}")
                ad["text"] = ad["text"].replace(fr, to)
            ex["ads"] = ads
            ex["ads_image_page"] = a["page"]
            ex.pop("_flag", None)
        ex = apply_fixes(ex, corr.get("fixes", []), sec)
        ex["id"] = f"{pid}-{sec}"
        ex["section"] = LABELS[sec]
        ex["pages"] = pages or manual.get("pages")
        ex["topic"] = titles.get(sec)
        s = {str(n): sol[n] for n in SOL_RANGE[sec] if n in sol}
        s.update(corr.get("solution_fixes", {}).get(sec, {}))
        ex["solution"] = {k: s[k].lower() for k in sorted(s, key=int)}
        ex["solution_complete"] = len(s) == len(SOL_RANGE[sec])
        ex["notes"] = corr.get("notes", {}).get(sec, [])
        ex["uncertain"] = corr.get("uncertain", {}).get(sec, [])
        ex["verified"] = bool(corr.get("verified", {}).get(sec, False))
        paper["exercises"].append(ex)
    for xt in corr.get("extra", []):
        sec = xt["sec"]
        ex = draft.PARSERS[sec](xt["pages"])
        ex = apply_fixes(ex, corr.get("fixes", []), xt["suffix"])
        ex["id"] = f"{pid}-{xt['suffix']}"
        ex["section"] = LABELS[sec] + " (" + xt.get("label", "Variante") + ")"
        ex["pages"] = xt["pages"]
        ex["topic"] = titles.get(sec)
        ex["solution"] = xt.get("solution", {})
        ex["solution_complete"] = len(ex["solution"]) == len(SOL_RANGE[sec])
        ex["no_solution_reason"] = xt.get("no_solution_reason")
        ex["notes"] = xt.get("notes", [])
        ex["uncertain"] = xt.get("uncertain", [])
        ex["verified"] = bool(xt.get("verified"))
        idx_after = max(i for i, e in enumerate(paper["exercises"]) if e["id"].split("-")[1] in (sec, xt["suffix"]))
        paper["exercises"].insert(idx_after + 1, ex)
    paper["missing_sections"] = [s for s in SEC_ORDER if s not in [e["id"].split("-", 1)[1] for e in paper["exercises"]]]
    paper["paper_notes"] = corr.get("paper_notes", [])
    os.makedirs("extraction/papers", exist_ok=True)
    json.dump(paper, open(f"extraction/papers/{pid}.json", "w"), ensure_ascii=False, indent=1)
    return paper


def dump(paper):
    """Human-readable rendering for side-by-side visual comparison."""
    out = [f"##### {paper['id']} pages {paper['pages']} key p{paper['answer_key_page']} sections {paper['page_sections']}"]
    for ex in paper["exercises"]:
        out.append(f"\n=== {ex['id']} [{ex.get('topic')}] pages {ex['pages']} verified={ex['verified']}")
        out.append("INSTR: " + ex.get("instructions", ""))
        if ex["type"] == "lesen1":
            for h in ex["headings"]: out.append(f"  {h['key']}) {h['text']}")
            for t in ex["texts"]: out.append(f"  {t['num']}. {t['text']}")
        if ex["type"] == "lesen2":
            out.append(f"  TITLE: {ex.get('title')} / {ex.get('subtitle')}")
            out.append("  " + ex["text"].replace("\n", "\n  "))
            for q in ex["questions"]:
                out.append(f"  Q{q['num']}. {q['stem']}" + (f"  !!{q.get('_flag')}" if q.get('_flag') else ""))
                for k, v in q["options"].items(): out.append(f"     {k}) {v}")
        if ex["type"] == "lesen3":
            for s in ex["situations"]: out.append(f"  {s['num']}. {s['text']}")
            for a in ex["ads"]: out.append(f"  [{a['key']}] " + a["text"].replace("\n", " / "))
        if ex["type"] == "sprach1":
            out.append("  " + ex["text"].replace("\n", "\n  "))
            for g in ex["gaps"]: out.append(f"  {g['num']}: " + " | ".join(f"{k}) {v}" for k, v in g["options"].items()) + (f"  !!{g.get('_flag')}" if g.get('_flag') else ""))
        if ex["type"] == "sprach2":
            out.append("  " + ex["text"].replace("\n", "\n  "))
            out.append("  WORDS: " + " ".join(f"{w['key']}={w['word']}" for w in ex["words"]))
        out.append(f"  SOLUTION({'complete' if ex['solution_complete'] else 'INCOMPLETE'}): " + " ".join(f"{k}{v}" for k, v in ex["solution"].items()))
    if paper["missing_sections"]:
        out.append(f"\nMISSING SECTIONS: {paper['missing_sections']}")
    return "\n".join(out)


if __name__ == "__main__":
    for pid in sys.argv[1:]:
        p = build(pid)
        txt = dump(p)
        open(f"extraction/papers/{pid}.dump.txt", "w").write(txt)
        print(txt)
