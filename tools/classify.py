import pymupdf as fitz, re, json, os
d=fitz.open("source/original.pdf")
def alltext(i):
    t=d[i].get_text()
    f=f"extraction/ocr/p{i+1:03d}.txt"
    if os.path.exists(f):
        t+="\n"+"\n".join(l.split("\t",1)[-1] for l in open(f).read().splitlines())
    return t
rules=[
 ("LOES", r"^\s*Lösungen\s*$|Leseverstehen \(Teil 1\)"),
 ("L1", r"Überschriften\s*a|Texte 1\s*[-–]\s*5|^\s*1\.\s|Leseverstehen,?\s*Teil\s*1"),
 ("L2", r"Aufgaben 6\s*[-–]|Leseverstehen,?\s*Teil\s*2|^\s*6\.\s"),
 ("L3", r"Situationen 11|Leseverstehen,?\s*Teil\s*3|Anzeigen a"),
 ("SB1", r"Lücken 21|Sprach\w*,?\s*Teil\s*1|\(21\)"),
 ("SB2", r"Lücken 31|Sprach\w*,?\s*Teil\s*2|\(31\)"),
 ("H", r"Sie hören"),
 ("S", r"geschrieben:|erhalten:|bekommen:|Schriftlicher Ausdruck|Brief|E-Mail"),
]
out=[]
for i in range(len(d)):
    t=alltext(i)
    tags=[k for k,r in rules if re.search(r,t,re.M)]
    first=[l.strip() for l in t.splitlines() if l.strip() and '@telcc' not in l][:1]
    out.append((i+1,tags,first[0][:60] if first else ''))
for o in out: print(o[0], ",".join(o[1]), "|", o[2])
