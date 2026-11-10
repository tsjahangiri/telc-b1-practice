"""Render a page with a labelled 0.05 grid (normalized coords) for locating ad boxes."""
import pymupdf as fitz, sys
d=fitz.open("source/original.pdf")
pno=int(sys.argv[1]); out=sys.argv[2]
p=d[pno-1]; W,H=p.rect.width,p.rect.height
sh=p.new_shape() if hasattr(p,'new_shape') else None
doc2=fitz.open(); doc2.insert_pdf(d,from_page=pno-1,to_page=pno-1); q=doc2[0]
for i in range(1,20):
    f=i/20
    q.draw_line((0,f*H),(W,f*H),color=(1,0,0) if i%2==0 else (0,0,1),width=0.4)
    q.draw_line((f*W,0),(f*W,H),color=(1,0,0) if i%2==0 else (0,0,1),width=0.4)
    q.insert_text((2,f*H-1),f"{f:.2f}",fontsize=6,color=(1,0,0))
    q.insert_text((f*W+1,8),f"{f:.2f}",fontsize=6,color=(1,0,0))
q.get_pixmap(dpi=120).save(out)
