import pymupdf as fitz, sys, re
d=fitz.open("source/original.pdf")
def lines(pno):
    """return list of (y0,x0,x1,text,size,bold) for text lines, watermark removed"""
    p=d[pno-1]; out=[]
    for b in p.get_text("dict")["blocks"]:
        for l in b.get("lines",[]):
            spans=[s for s in l["spans"] if s["text"].strip()!="" or True]
            t="".join(s["text"] for s in spans)
            if not t.strip() or "@telcc1hochschul" in t: continue
            if l["dir"][0]<0.9: continue
            nonempty=[s for s in spans if s["text"].strip()]
            bold=bool(nonempty) and all((s["flags"]&16) or "Bold" in s["font"] for s in nonempty)
            size=max((s["size"] for s in spans if s["text"].strip()),default=0)
            out.append((round(l["bbox"][1],1),round(l["bbox"][0],1),round(l["bbox"][2],1),t,round(size,1),bold))
    out.sort(key=lambda r:(round(r[0]/3),r[1]))
    return out
if __name__=="__main__":
    for pno in map(int,sys.argv[1:]):
        print("=== page",pno)
        for r in lines(pno): print(f"{r[0]:6.1f} {r[1]:6.1f} {r[4]:4.1f}{'B' if r[5] else ' '} {r[3]}")
