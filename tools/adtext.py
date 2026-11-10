"""Collect OCR lines inside normalized boxes. usage: adtext.py PAGE 'a:x0,y0,x1,y1;b:...'"""
import sys,re
def ocr_lines(pno):
    out=[]
    for l in open(f"extraction/ocr/p{pno:03d}.txt"):
        m=re.match(r'([\d.]+) ([\d.]+) ([\d.]+)\t(.*)',l.rstrip("\n"))
        if m: out.append((float(m.group(1)),float(m.group(2)),float(m.group(3)),m.group(4)))
    return out
def collect(pno,boxes):
    L=ocr_lines(pno); res={}
    for k,(x0,y0,x1,y1) in boxes.items():
        sel=[l for l in L if x0<=l[1]<x1 and y0<=l[0]<y1]
        sel.sort(key=lambda l:(round(l[0]/0.006),l[1]))
        res[k]=sel
    return res
if __name__=="__main__":
    pno=int(sys.argv[1]); boxes={}
    for part in sys.argv[2].split(";"):
        k,v=part.split(":"); boxes[k]=tuple(map(float,v.split(",")))
    for k,sel in collect(pno,boxes).items():
        print(f"--- {k}")
        for l in sel: print(("?" if l[2]<0.6 else " "),l[3])
