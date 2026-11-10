"""sheet.py OUT p1 p2 ... (up to 4 pages in a 2x2 grid)"""
import pymupdf as fitz, sys
d=fitz.open("source/original.pdf")
out=sys.argv[1]; ps=list(map(int,sys.argv[2:]))
W,H=d[0].rect.width,d[0].rect.height
doc=fitz.open(); pg=doc.new_page(width=2*W,height=2*H)
for i,p in enumerate(ps[:4]):
    r=fitz.Rect((i%2)*W,(i//2)*H,(i%2+1)*W,(i//2+1)*H)
    pg.show_pdf_page(r,d,p-1)
    pg.insert_text((r.x0+5,r.y0+20),f"p{p}",fontsize=18,color=(1,0,0))
    pg.draw_rect(r,color=(0,0,1),width=1)
pg.get_pixmap(dpi=72).save(out)
