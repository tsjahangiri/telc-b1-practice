"""Assign a visual style to each ad (layout only — text untouched). Used by export_web.py."""
import re, hashlib
ICONS = [  # (icon, keyword regex) first match wins
 ("music", r"konzert|musik|sinfon|symphon|chor|klavier|kammermusik|barock|galakonzert|musikerlebnis|lieder|hofkonzert|flöte|tanzschule|walzer|tango|tanz"),
 ("bike", r"fahrrad|rad durch|fahrräder|radtour"),
 ("train", r"lokomotive|bahnmuseum|\bdb\b|deutsche bahn|zügen|eisenbahn"),
 ("ship", r"flussfahrt|schiff|nordsee|ostsee|kanu|aare"),
 ("plane", r"flüge|flug|airlines|airplus"),
 ("food", r"restaurant|küche|essen|menü|pizza|thai|gourmet|café|bistro|cantino|stüberl|vegetarisch|fisch|käse|sennerei|partyservice|buffet|gasthof|wirtschaft|koch"),
 ("bed", r"hotel|ferienwohn|ferienwhg|übernacht|pension|bett|couch|jugendcamp|halbpension|vollpension|ferienhotel|zimmer"),
 ("book", r"sprach|kurs|schule|nachhilfe|lern|buch|verlag|zeitschrift|ratgeber|handbuch|lesung|vortrag|volkshochschule|kindergarten"),
 ("film", r"film|kino|tatort|tv|arte|3sat|vox|radio|sendung|talk-show"),
 ("flower", r"blumen|floristik|pflanzen|buga|garten"),
 ("car", r"auto|lkw|umzug|transporter|tankstelle|reisemobil"),
 ("job", r"sucht|suchen|gesucht|stelle|mitarbeiter|bewerbung|praktikant|aushilf|job|stellt ein|tätigkeit"),
 ("heart", r"partner|single|begleiterin|lehrerin sucht"),
 ("paw", r"tier|vögel|aquarien"),
 ("gift", r"geschenk|glückwunsch|heimatwerk|möbel|accessoires"),
 ("sun", r"urlaub|ferien|reise|wander|alpen|therme|bad"),
]
VARIANTS = ["classic", "bold", "inverse", "double", "soft", "script", "dashed", "framed"]
CONTACT = re.compile(r"(\bTel\b|Tel\.|Telefon|Fax|www\.|@|E-?[Mm]ail|Internet|http|Postfach|\b[A-Z]?-?\d{4,5}\s+[A-ZÄÖÜ]|str\.|straße|strasse|Str\.|gasse|weg \d|platz \d|allee|☎|Chiffre|Zuschriften)", re.I)
# Headline line count fixed by hand where the automatic rule splits name/role pairs.
HEAD_OVERRIDE = {(67, "j"): 2, (447, "j"): 2}  # "András Adorján / Flöte" — keeps each musician with the instrument
def style_for(page, key, text):
    lines = [l for l in text.split("\n") if l.strip()]
    low = text.lower()
    icon = next((i for i, rx in ICONS if re.search(rx, low)), None)
    head = 0
    for l in lines[:3]:
        if len(l) <= 30 and not CONTACT.search(l) and not l.rstrip().endswith(("-", ",", "(")) and "(" not in l and not re.search(r"\d{3}", l):
            head += 1
            if l.rstrip().endswith(("!", ".", "?", "…", "...")) and head >= 1: break
        else: break
    head = HEAD_OVERRIDE.get((page, key), max(1, head))
    h = int(hashlib.md5(f"{key}{text[:40]}".encode()).hexdigest(), 16)
    variant = VARIANTS[h % len(VARIANTS)]
    if re.search(r"sucht|gesucht|stellt ein|bewerbung", low) and h % 3 == 0: variant = "bold"
    if lines and lines[0].isupper() and len(lines[0]) > 6: variant = "inverse" if h % 2 else "bold"
    return {"variant": variant, "icon": icon, "head": head, "span": 2 if len(text) > 520 else 1}

# Hand-assigned pictograms per distinct ad page (keys a..l); "-" = no pictogram.
MANUAL_ICONS = {
 "P01": "bed home bed fuel sun sun sun sun bed bike food bike",
 "P02": "home book food food flower food book flower flower car car home",
 "P03": "music book music sun heart plane sun music book music bed book",
 "P04": "sun - film bed - bed paw train paw music book ship",
 "P05": "- food food book music music food book music book food food",
 "P06": "music book food music food music food music book music gift food",
 "P08": "food film - job music job job book music film book -",
 "P10": "job film train film job film job job film - - job",
 "P12": "food book film food job - home home film job book job",
 "P13": "book book ship car car film gift home medical medical food food",
 "P14": "job film train film job film job job film - - job",
 "P15": "music book job book job heart car job job book car job",
}
CANON_PAPER = {"P01": "P01", "P25": "P01", "P02": "P02", "P21": "P02", "P03": "P03", "P29": "P03", "P04": "P04", "P07": "P04", "P09": "P04",
 "P19": "P04", "P22": "P04", "P24": "P04", "P05": "P05", "P16": "P05", "P06": "P06", "P30": "P06", "P08": "P08", "P17": "P08",
 "P10": "P10", "P11": "P10", "P27": "P10", "P28": "P10", "P12": "P12", "P23": "P12", "P13": "P13", "P26": "P13", "P14": "P14", "P18": "P14", "P15": "P15", "P20": "P15"}
def icon_for(paper, key):
    s = MANUAL_ICONS[CANON_PAPER[paper]].split()
    i = s["abcdefghijkl".index(key)]
    return None if i == "-" else i
