"""Phase 2 audit: checks all structured papers + page records; writes combined JSON + reports."""
import json, glob, re, os, hashlib
papers = [json.load(open(f)) for f in sorted(glob.glob("extraction/papers/P??.json"))]
recs = [r for f in sorted(glob.glob("extraction/batches/batch_??.json")) for r in json.load(open(f))["records"]]
issues = []
N = 493
pages = {r["page"] for r in recs}
missing = sorted(set(range(1, N + 1)) - pages)
unver = sorted(r["page"] for r in recs if not r["verified"])
ex_all = [e for p in papers for e in p["exercises"]]
SOL = {"lesen1": range(1, 6), "lesen2": range(6, 11), "lesen3": range(11, 21), "sprach1": range(21, 31), "sprach2": range(31, 41)}
for e in ex_all:
    rng = SOL[e["type"]]
    sol = e["solution"]
    if set(map(int, sol)) != set(rng): issues.append(f"{e['id']}: solution keys {sorted(map(int,sol))} != {list(rng)}")
    if not e["verified"]: issues.append(f"{e['id']}: not verified")
    s = json.dumps(e, ensure_ascii=False)
    if "_flag" in s: issues.append(f"{e['id']}: leftover parser flag")
    if e["type"] == "lesen1":
        keys = [h["key"] for h in e["headings"]]
        if keys != list("abcdefghij"): issues.append(f"{e['id']}: heading keys {keys}")
        if [t["num"] for t in e["texts"]] != [1, 2, 3, 4, 5]: issues.append(f"{e['id']}: text numbers")
        for k, v in sol.items():
            if v not in keys: issues.append(f"{e['id']}: solution {k}={v} not a heading")
        if len(set(sol.values())) != len(sol): issues.append(f"{e['id']}: duplicate heading used in key")
    if e["type"] == "lesen2":
        if [q["num"] for q in e["questions"]] != list(range(6, 11)): issues.append(f"{e['id']}: question numbers")
        for q in e["questions"]:
            if sorted(q["options"]) != ["a", "b", "c"] or not all(q["options"].values()): issues.append(f"{e['id']}: Q{q['num']} options")
        if len(e["text"]) < 500: issues.append(f"{e['id']}: short text")
        for k, v in sol.items():
            if v not in "abc": issues.append(f"{e['id']}: bad solution {k}={v}")
    if e["type"] == "lesen3":
        if [s_["num"] for s_ in e["situations"]] != list(range(11, 21)): issues.append(f"{e['id']}: situation numbers")
        keys = [a["key"] for a in e["ads"]]
        if keys != list("abcdefghijkl"): issues.append(f"{e['id']}: ad keys {keys}")
        for k, v in sol.items():
            if v not in keys + ["x"]: issues.append(f"{e['id']}: solution {k}={v}")
        used = [v for v in sol.values() if v != "x"]
        if len(set(used)) != len(used): issues.append(f"{e['id']}: ad used twice in key")
    if e["type"] == "sprach1":
        gaps = re.findall(r"\[\[(\d+)\]\]", e["text"])
        if gaps != [str(i) for i in range(21, 31)]: issues.append(f"{e['id']}: gaps in text {gaps}")
        for g in e["gaps"]:
            if sorted(g["options"]) != ["a", "b", "c"] or not all(g["options"].values()): issues.append(f"{e['id']}: gap {g['num']} options {g['options']}")
        for k, v in sol.items():
            if v not in "abc": issues.append(f"{e['id']}: bad solution {k}={v}")
    if e["type"] == "sprach2":
        gaps = re.findall(r"\[\[(\d+)\]\]", e["text"])
        if gaps != [str(i) for i in range(31, 41)]: issues.append(f"{e['id']}: gaps in text {gaps}")
        keys = [w["key"] for w in e["words"]]
        if keys != list("abcdefghijklmno"): issues.append(f"{e['id']}: word keys {keys}")
        for k, v in sol.items():
            if v not in keys: issues.append(f"{e['id']}: solution {k}={v}")
        if len(set(sol.values())) != len(sol): issues.append(f"{e['id']}: word used twice in key")
# duplicates: group identical exercise content
def sig(e):
    skip = ('id', 'pages', 'verified', 'notes', 'uncertain', 'ads_image_page', 'topic', 'section', 'no_solution_reason')
    return hashlib.md5(json.dumps({k: v for k, v in e.items() if k not in skip}, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
groups = {}
for e in ex_all: groups.setdefault(sig(e), []).append(e["id"])
for e in ex_all: e["duplicate_of"] = groups[sig(e)][0] if groups[sig(e)][0] != e["id"] else None
unc = [(e["id"], u) for e in ex_all for u in e["uncertain"]]
page_unc = [(r["page"], u) for r in recs for u in r["uncertain"]]
out = {"source": "source/original.pdf", "total_pages": N, "generated_by": "tools/audit.py",
       "papers": papers,
       "pages": [{k: r[k] for k in ("page", "paper", "section", "text_source", "verified", "verification_method", "verification_note", "uncertain", "images")} | {"text": r["text"], "arabic_labels_excluded": r["arabic_labels_excluded"]} for r in recs]}
json.dump(out, open("extraction/extracted_content.json", "w"), ensure_ascii=False, indent=1)
json.load(open("extraction/extracted_content.json"))
stats = {"pages": len(pages), "missing_pages": missing, "unverified_pages": unver, "papers": len(papers), "exercises": len(ex_all),
         "unique_exercises": len(groups), "by_type": {t: sum(1 for e in ex_all if e["type"] == t) for t in SOL},
         "answer_keys_complete": sum(e["solution_complete"] for e in ex_all), "issues": issues,
         "uncertain_exercise_items": len(unc), "uncertain_page_items": len(page_unc),
         "methods": {m: sum(1 for r in recs if r["verification_method"] == m) for m in sorted({r["verification_method"] for r in recs})},
         "dup_groups": {v[0]: v[1:] for v in groups.values() if len(v) > 1}}
json.dump(stats, open("extraction/audit_stats.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in stats.items() if k != "dup_groups"}, ensure_ascii=False, indent=1))
print("unique groups with duplicates:", len(stats["dup_groups"]))
