"""crop.py PAGE x0 y0 x1 y1 OUT [dpi]  (normalized coords)"""
import pymupdf as fitz, sys
d=fitz.open("source/original.pdf")
p=d[int(sys.argv[1])-1]; W,H=p.rect.width,p.rect.height
x0,y0,x1,y1=map(float,sys.argv[2:6]); dpi=int(sys.argv[7]) if len(sys.argv)>7 else 200
p.get_pixmap(dpi=dpi,clip=fitz.Rect(x0*W,y0*H,x1*W,y1*H)).save(sys.argv[6])
