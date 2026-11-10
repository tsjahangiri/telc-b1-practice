"""Regenerate progress.md from files on disk (batches + papers). usage: progress.py 'phase text' 'extra notes'"""
import json,os,glob,sys
import glob as _g, json as _j
hrow=[]
for _f in sorted(_g.glob("extraction/hoeren/P??.json")):
    _e=_j.load(open(_f)); hrow.append(f"| {_f[-8:-5]} | {', '.join('Teil %d' % x['part'] for x in _e)} | {sum(len(x['statements']) for x in _e)} | {'yes' if all(x['solution_complete'] for x in _e) else 'NO'} |")
phase=sys.argv[1] if len(sys.argv)>1 else "Phase 1 — extraction and verification"
extra=sys.argv[2] if len(sys.argv)>2 else ""
N=493
rows=[];done_pages=set();ver_pages=set();ocr_pages=[];unc=[]
for b in range(1,51):
    a,e=(b-1)*10+1,min(b*10,N)
    if a>N: break
    f=f"extraction/batches/batch_{b:02d}.json"
    if os.path.exists(f):
        R=json.load(open(f))["records"]
        ext=[r["page"] for r in R if r["extracted"]]; ver=[r["page"] for r in R if r["verified"]]
        oc=[r["page"] for r in R if r["text_source"]=="ocr"]
        done_pages|=set(ext); ver_pages|=set(ver); ocr_pages+=oc
        unc+=[(r["page"],u) for r in R for u in r["uncertain"]]
        st="complete" if len(ver)==e-a+1 else "IN PROGRESS"
        rows.append(f"| {b:02d} | {a}–{e} | {len(ext)}/{e-a+1} | {len(ver)}/{e-a+1} | {', '.join(map(str,oc)) or '–'} | {st} |")
    else:
        rows.append(f"| {b:02d} | {a}–{e} | – | – | – | pending |")
papers=sorted(glob.glob("extraction/papers/P??.json"))
prow=[]
for f in papers:
    P=json.load(open(f))
    v=sum(e["verified"] for e in P["exercises"])
    prow.append(f"| {P['id']} | {P['pages'][0]}–{P['pages'][1]} | {len(P['exercises'])} | {v} | {', '.join(P['missing_sections']) or '–'} |")
def ranges(s):
    s=sorted(s); out=[]
    for p in s:
        if out and p==out[-1][1]+1: out[-1][1]=p
        else: out.append([p,p])
    return ", ".join(f"{a}–{b}" if a!=b else str(a) for a,b in out) or "none"
txt=f"""# Progress — TELC B1 practice website

**Current phase:** {phase}

- Source: `source/original.pdf` (unmodified copy of `B1-telc past papers(1).pdf`) — **{N} pages**
- Structure: 30 exam papers (P01–P30) + speaking-exam notes — see `extraction/document_map.md`
- Pages extracted: **{len(done_pages)}/{N}** ({ranges(done_pages)})
- Pages visually verified: **{len(ver_pages)}/{N}** ({ranges(ver_pages)})
- Pages whose text comes from OCR (image-only pages): {', '.join(map(str,ocr_pages)) or 'none'}
- Uncertain items recorded: {len(unc)} (see `extraction/uncertain_content.md`)

## Batches (10 pages each)
| Batch | Pages | Extracted | Visually verified | OCR pages | Status |
|---|---|---|---|---|---|
""" + "\n".join(rows) + """

## Structured papers (Lesen + Sprachbausteine)
| Paper | Pages | Exercises | Verified | Missing sections |
|---|---|---|---|---|
""" + "\n".join(prow) + f"""

## Hörverstehen (extraction/hoeren, tools/hoeren.py)
| Paper | Parts | Statements | Key complete |
|---|---|---|---|
""" + "\n".join(hrow) + f"""

## Notes
{extra}
"""
open("progress.md","w").write(txt)
print(txt[:600])
