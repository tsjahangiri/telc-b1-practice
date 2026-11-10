import pymupdf as fitz, subprocess, os, sys
d=fitz.open("source/original.pdf")
tmp=sys.argv[1]
for i in range(len(d)):
    out=f"extraction/ocr/p{i+1:03d}.txt"
    if os.path.exists(out): continue
    d[i].get_pixmap(dpi=300).save(tmp)
    o=subprocess.run(["tools/ocr",tmp],capture_output=True,text=True).stdout
    open(out,"w").write(o)
print("OCR complete")
