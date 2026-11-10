"""usage: note.py PAGES METHOD 'note' ['uncertain1' ...]   PAGES like 1-10 or 3,5"""
import json,sys,os
f="extraction/corrections/page_notes.json"
n=json.load(open(f)) if os.path.exists(f) else {}
spec,method,note=sys.argv[1],sys.argv[2],sys.argv[3]
unc=sys.argv[4:]
ps=[]
for part in spec.split(","):
    if "-" in part: a,b=map(int,part.split("-")); ps+=range(a,b+1)
    else: ps.append(int(part))
for p in ps:
    e=n.get(str(p),{})
    e.update({"verified":True,"method":method,"note":note})
    if unc: e["uncertain"]=e.get("uncertain",[])+unc
    n[str(p)]=e
json.dump(n,open(f,"w"),ensure_ascii=False,indent=1)
print("noted",ps)
