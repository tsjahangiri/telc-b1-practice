import json, re, difflib, sys
sys.argv=[sys.argv[0]]
exec(open("tools/crosscheck.py").read().split("os.makedirs")[0])
noise={"leseverstehen","teil","language","tests","sprachausteine","sprachbausteine"}
for e in D:
    if e["duplicate_of"]: continue
    W=[w.lower() for w in norm(web_text(e))]; O=[w.lower() for w in norm(" ".join(ocr_words(p) for p in e["pages"])) if w.lower() not in noise]
    sm=difflib.SequenceMatcher(None,W,O,autojunk=False)
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag in("insert","replace") and (j2-j1)>=4 and (j2-j1)>(i2-i1)+2:
            print(e["id"],tag,"WEB:"," ".join(W[i1:i2])[:80],"| OCR:"," ".join(O[j1:j2])[:160])
        if tag in("delete","replace") and (i2-i1)>=4 and (i2-i1)>(j2-j1)+2 and e["type"]!="lesen3":
            print(e["id"],tag,"WEB-EXTRA:"," ".join(W[i1:i2])[:160],"| OCR:"," ".join(O[j1:j2])[:80])
