#!/usr/bin/env python3
"""Maintainer script: assemble data/studies.csv (+ .json, missing_links.csv) from the survey's working files.

    python3 scripts/ingest_sources.py --sources SUBMISSION_DIR --catalogue-dir catalogue_v7 --bib air_refs.bib \
        --manuscript MANUSCRIPT_DIR

Readers of the repository do not need this script; they edit data/studies.csv and run
scripts/build_views.py. The script merges, into one row per work:
  catalogue_vN.csv      the studies coded on the design axes        -> list "catalogue"
  List B (merged_v2)    every record that passed title/abstract screening -> list "related"
  nf_vN.csv             normalizing-flow comparison sample           -> list "NF sample"
  diffusion_vN.csv      diffusion comparison sample                  -> list "diffusion sample"
  decisions_all_vN.csv  full-text decisions; excluded records not elsewhere -> list "excluded"
Works are identified by bibliography key, merged id, source id, DOI, arXiv id and normalized title; a second
pass merges near-identical titles (preprint + venue version). Merges are logged in data/merge_log.csv.
"""
import argparse, collections, csv, difflib, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DATA = os.path.join(REPO, "data")

FAM_TASK = {"processing": "Restoration", "translation": "Translation and harmonization",
            "generation": "Generation and forecasting", "analysis": "Analysis and segmentation"}
LISTB_FAM = {"FM": "FM", "RF": "RF", "PB": "PB", "SB": "SB", "PF": "PF", "NF": "NF", "NF discrete": "NF", "CNF": "NF",
             "SI": "other", "Other": "other", "other": "other", "FM/bridge": "other"}
CORR = {"P": "Paired", "Sim": "Simulated pairs", "I": "Unpaired", "R": "Registered pairs", "OT": "Minibatch OT",
        "L": "Learned coupling", "n.r.": ""}
START = {"S": "Scan", "N": "Noise", "E": "Prior", "D": "Prior"}
PATH = {"lin": "Linear interpolation", "bb": "Brownian bridge", "mr": "Mean-reverting bridge", "pf": "Poisson field",
        "vp": "Variance-preserving path", "riem": "Riemannian path", "other": "Other path"}
MOD = {"MR": "MRI", "MRI": "MRI", "CT": "CT", "PET": "PET", "XR": "X-ray", "X-RAY": "X-ray", "US": "Ultrasound",
       "ULTRASOUND": "Ultrasound", "MIC": "Microscopy", "MICROSCOPY": "Microscopy", "FLUORESCENCE": "Microscopy",
       "OPT": "Optical (OCT, fundus, endoscopy)", "OCT": "Optical (OCT, fundus, endoscopy)",
       "FUNDUS": "Optical (OCT, fundus, endoscopy)", "ENDOSCOPY": "Optical (OCT, fundus, endoscopy)",
       "HISTOPATHOLOGY": "Histopathology", "HISTOLOGY": "Histopathology", "PHOTOACOUSTIC": "Photoacoustic",
       "SPECT": "SPECT", "MULTI": "Multi-modal", "MULTIMODAL": "Multi-modal", "CBCT": "CT"}

ANATOMY = [  # (label, regex on title + clinical group + datasets); first match order is irrelevant, all matches kept
    ("Brain", r"brain|cortical|cortex|cerebr|neuro|fmri|glioma|brats|adni|alzheimer|\bhcp\b|\bixi\b|dmri|amyloid|\btau\b|stroke|skull|ventric|isles|oasis|connectom|\bhead\b|infant"),
    ("Heart", r"cardiac|heart|coronary|myocard|echocardio|\bacdc\b|camus|cardio|\bcine\b|left ventric"),
    ("Chest and lung", r"lung|chest|pulmonary|thorac|\bcxr\b|nodule|lidc|pneumo|ct-rate|mimic-cxr|bone suppression|luna16|nlst"),
    ("Abdomen", r"abdom|liver|hepat|kidney|renal|pancrea|spleen|\bamos\b|btcv|bowel|colon|colorectal|\bkits\b|stomach|gastric"),
    ("Pelvis and prostate", r"prostate|pelvi|cervical|rectal|bladder|uter|gynae|gynec|ovar"),
    ("Breast", r"breast|mammo|csaw|inbreast|ddsm"),
    ("Head and neck", r"head and neck|head-and-neck|hnscc|hecktor|nasophar|dental|tooth|teeth|oropharyn"),
    ("Musculoskeletal", r"knee|\bbone\b|spine|spinal|\bhip\b|femur|musculoskel|skelet|joint|ctspine|orthop|implant|prosthe"),
    ("Eye", r"retina|retinal|fundus|\boct\b|octa|ophthalm|cornea|\beye\b|choroid"),
    ("Skin", r"\bskin\b|dermos|isic|dermat|melanoma"),
    ("Vessels", r"vessel|vascular|angiogra|arter|aneurysm|circle of willis|\bmra\b|guidewire"),
    ("Cells and tissue", r"histo|patholog|h&e|\bcell|microscop|tissue|whole-slide|\bwsi\b|stain|fluorescen|organoid|spatial transcript|gene expression|chromosom|cytolog|immunohisto"),
    ("Whole body", r"whole-body|whole body|total-body|total body|pan-cancer|multi-organ|multiorgan|totalsegmentator"),
]


# ---------------------------------------------------------------------------------------------------------------
def rd(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def nz(x):
    x = (x or "").strip()
    return "" if x.lower() in ("nan", "none", "n.r.", "na") else x


def split_ids(v):
    return [i.strip() for i in re.split(r"[;,]", v or "") if i.strip()]


def tok(i):
    """Identifier token: screening / chasing records are m:, bibliography or catalogue keys are k:."""
    return ("m:" if re.match(r"(M\d+|CC\d+)$", i) else "k:") + i


def norm_title(t):
    t = re.sub(r"[{}\\$]", "", t or "").lower()
    return re.sub(r"[^a-z0-9]+", "", t)


def norm_doi(d):
    d = nz(d).lower()
    d = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", d)
    return d.strip().rstrip(".")


def norm_arxiv(a):
    a = nz(a).lower()
    a = re.sub(r"^(https?://)?arxiv\.org/(abs|pdf)/", "", a)
    a = re.sub(r"^arxiv:", "", a)
    a = re.sub(r"v\d+$", "", a)
    a = re.sub(r"\.pdf$", "", a)
    return a.strip()


ACC = {"'": {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú", "y": "ý", "c": "ć", "n": "ń", "s": "ś", "z": "ź",
             "A": "Á", "E": "É", "I": "Í", "O": "Ó", "U": "Ú"},
       "`": {"a": "à", "e": "è", "i": "ì", "o": "ò", "u": "ù"},
       '"': {"a": "ä", "e": "ë", "i": "ï", "o": "ö", "u": "ü", "A": "Ä", "O": "Ö", "U": "Ü", "y": "ÿ"},
       "^": {"a": "â", "e": "ê", "i": "î", "o": "ô", "u": "û"},
       "~": {"a": "ã", "n": "ñ", "o": "õ", "A": "Ã", "N": "Ñ", "O": "Õ"},
       "c": {"c": "ç", "C": "Ç", "s": "ş", "S": "Ş"}, "v": {"c": "č", "s": "š", "z": "ž", "r": "ř", "e": "ě", "n": "ň",
                                                           "C": "Č", "S": "Š", "Z": "Ž"},
       "u": {"g": "ğ", "a": "ă"}, "H": {"o": "ő", "u": "ű"}, "=": {"a": "ā", "e": "ē", "o": "ō", "u": "ū"},
       ".": {"z": "ż"}}


def delatex(s):
    s = s or ""
    s = s.replace("\\&", "&").replace("\\_", "_").replace("\\%", "%").replace("---", "—").replace("--", "–")
    s = re.sub(r"\\(ss)\b\s*", "ß", s)
    s = re.sub(r"\\(o)\b\s*", "ø", s)
    s = re.sub(r"\\(O)\b\s*", "Ø", s)
    s = re.sub(r"\\(l)\b\s*", "ł", s)
    s = re.sub(r"\\(aa)\b\s*", "å", s)
    s = re.sub(r"\\(ae)\b\s*", "æ", s)
    s = re.sub(r"\\i\b\s*", "i", s)

    def acc(m):
        a, ch = m.group(1), m.group(2) or m.group(3)
        return ACC.get(a, {}).get(ch, ch)
    s = re.sub(r"\\(['`\"^~=.])\{?\\?([A-Za-z])\}?", lambda m: ACC.get(m.group(1), {}).get(m.group(2), m.group(2)), s)
    s = re.sub(r"\\([cvuH])\{([A-Za-z])\}", lambda m: ACC.get(m.group(1), {}).get(m.group(2), m.group(2)), s)
    s = re.sub(r"\\([cvuH]) ([A-Za-z])", lambda m: ACC.get(m.group(1), {}).get(m.group(2), m.group(2)), s)
    s = re.sub(r"\$([^$]*)\$", r"\1", s)
    s = re.sub(r"\\(?:textit|textbf|emph|mathrm|mathbf|text)\{([^{}]*)\}", r"\1", s)
    s = s.replace("{", "").replace("}", "").replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()


def fmt_authors(a):
    if not a:
        return ""
    out = []
    for p in re.split(r"\s+and\s+", a.replace("\n", " ")):
        p = p.strip()
        if not p:
            continue
        if p.lower() in ("others", "et al.", "{others}"):
            out.append("et al.")
            continue
        if p.startswith("{") and p.endswith("}") and "," not in p:
            out.append(delatex(p))
            continue
        if "," in p:
            last, first = p.split(",", 1)
            p = f"{first.strip()} {last.strip()}"
        out.append(delatex(p))
    return ", ".join(out)


VENUE_ABBR = [(r"medical image computing and computer[- ]assisted", "MICCAI"), (r"international symposium on biomedical imaging", "ISBI"),
               (r"computer vision and pattern recognition", "CVPR"), (r"international conference on computer vision", "ICCV"),
               (r"european conference on computer vision", "ECCV"), (r"neural information processing", "NeurIPS"),
               (r"learning representations", "ICLR"), (r"international conference on machine learning", "ICML"),
               (r"winter conference on applications of computer vision", "WACV"), (r"medical imaging with deep learning", "MIDL"),
               (r"aaai", "AAAI"), (r"spie medical imaging", "SPIE Medical Imaging"), (r"acoustics, speech and signal", "ICASSP"),
               (r"bioinformatics and biomedicine", "BIBM")]


def venue_from_bib(e):
    v = e.get("journal") or ""
    if not v or re.search(r"lecture notes|proceedings series|^advances in", v, re.I):
        v = e.get("booktitle") or v or e.get("howpublished") or e.get("publisher") or ""
    v = delatex(v)
    for rx, ab in VENUE_ABBR:
        if re.search(rx, v, re.I):
            yr = re.search(r"(19|20)\d\d", e.get("year", ""))
            return ab + (" " + yr.group(0) if yr and ab not in ("SPIE Medical Imaging",) else "")
    if re.search(r"arxiv", v, re.I):
        return "arXiv"
    if re.search(r"medrxiv", v, re.I):
        return "medRxiv"
    if re.search(r"biorxiv", v, re.I):
        return "bioRxiv"
    v = re.sub(r"^(Proceedings of the|Proceedings of|Proc\. of)\s+", "", v)
    return v


def clean_venue(v):
    v = (v or "").strip()
    if re.match(r"arxiv", v, re.I):
        return "arXiv"
    if re.search(r"international society for magnetic resonance", v, re.I):
        return "ISMRM"
    if re.match(r"lecture notes in computer science", v, re.I):
        return "Lecture Notes in Computer Science"
    if re.search(r"ssrn", v, re.I):
        return "SSRN"
    for rx, ab in VENUE_ABBR:
        if re.search(rx, v, re.I) and len(v) > 40:
            return ab
    return v


def links_of(doi="", arxiv="", url=""):
    """Return (primary, [alternatives]). DOI preferred; arXiv-minted DOIs count as arXiv."""
    doi, arxiv, url = norm_doi(doi), norm_arxiv(arxiv), nz(url)
    m = re.match(r"10\.48550/arxiv\.(.+)", doi)
    if m:
        arxiv = arxiv or norm_arxiv(m.group(1))
        doi = ""
    out = []
    if doi:
        out.append("https://doi.org/" + doi)
    if arxiv:
        out.append("https://arxiv.org/abs/" + arxiv)
    if url:
        out.append(url)
    return out


def find_code(*texts):
    urls = []
    for t in texts:
        for u in re.findall(r"https?://(?:www\.)?(?:github\.com|gitlab\.com|huggingface\.co|zenodo\.org)/[^\s,;)\]\"'|]+", t or ""):
            u = u.rstrip(".")
            if u not in urls:
                urls.append(u)
    return urls


# anatomy implied by the clinical task group of the coding
GROUP_ANATOMY = {"Cardiac and brain dynamics": ["Heart", "Brain"], "Tissue-image translation": ["Cells and tissue"],
                 "Microscopy and OCT": ["Cells and tissue", "Eye"]}
# anatomy of widely used datasets named in the coding
DATASET_ANATOMY = {"brats": "Brain", "adni": "Brain", "ixi": "Brain", "oasis": "Brain", "hcp": "Brain", "isles": "Brain",
                   "acdc": "Heart", "camus": "Heart", "echonet": "Heart", "lidc": "Chest and lung",
                   "luna16": "Chest and lung", "nlst": "Chest and lung", "mimic-cxr": "Chest and lung", "ct-rate": "Chest and lung",
                   "chexpert": "Chest and lung", "chestx-ray14": "Chest and lung", "kits": "Abdomen", "lits": "Abdomen",
                   "amos": "Abdomen", "btcv": "Abdomen", "chaos": "Abdomen", "msd": "", "prostatex": "Pelvis and prostate",
                   "promis": "Pelvis and prostate", "isic": "Skin", "drive": "Eye", "octa-500": "Eye", "retouch": "Eye",
                   "inbreast": "Breast", "csaw": "Breast", "ddsm": "Breast", "hecktor": "Head and neck", "hnscc": "Head and neck",
                   "bbbc021": "Cells and tissue", "rxrx1": "Cells and tissue", "pannuke": "Cells and tissue", "monuseg": "Cells and tissue",
                   "tcga": "Cells and tissue", "autopet": "Whole body", "totalsegmentator": "Whole body", "synthrad": ""}


def anatomy_of(text, group="", datasets=""):
    t = text.lower()
    hits = [lab for lab, rx in ANATOMY if re.search(rx, t)]
    for lab in GROUP_ANATOMY.get(group, []):
        if lab not in hits:
            hits.append(lab)
    for d in re.split(r"[;,]", datasets.lower()):
        d = d.strip()
        for k, lab in DATASET_ANATOMY.items():
            if lab and d.startswith(k) and lab not in hits:
                hits.append(lab)
    return hits or ["Unspecified"]


MODRX = [("MRI", r"\bmri?\b|fmri|mrsi|dce|\bmra\b|diffusion mri|cardiac mri|\bmr\b|magnetic resonance"),
         ("CT", r"\bcbct\b|\bct\b|ct->|computed tomography"), ("PET", r"\bpet\b|scintigraph|spect"),
         ("X-ray", r"x-?ray|radiograph|\bxr\b"), ("Ultrasound", r"ultrasound|echocardio|\bus\b"),
         ("Microscopy", r"\bmic\b|microscop|fluoresc|\bcell"), ("Optical (OCT, fundus, endoscopy)", r"\bopt\b|\boct|fundus|dermosc|endosc|optical|retina"),
         ("Histopathology", r"histo|patholog|\bwsi\b"), ("Photoacoustic", r"photoacoustic")]


def modality_of(raw):
    t = (raw or "").lower()
    out = [lab for lab, rx in MODRX if re.search(rx, t)]
    return out or ["Unspecified"]


# ---------------------------------------------------------------------------------------------------------------
class UF:
    def __init__(self):
        self.p = {}

    def f(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def u(self, a, b):
        self.p[self.f(a)] = self.f(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sources", default="/Users/haochen/OverleafWork/AIR - Flow Survey/submission_fix_20261018")
    ap.add_argument("--catalogue-dir", default="catalogue_v7", help="folder under --sources (or absolute) holding catalogue_vN.csv, nf_vN.csv, diffusion_vN.csv, decisions_all_vN.csv")
    ap.add_argument("--bib", default="/Users/haochen/Library/CloudStorage/Dropbox/Apps/Overleaf/AIR - Flow Survey/air_refs.bib")
    ap.add_argument("--manuscript", default="/Users/haochen/Library/CloudStorage/Dropbox/Apps/Overleaf/AIR - Flow Survey")
    ap.add_argument("--listb", default="merged_v2/listB_final.csv")
    ap.add_argument("--old-studies", default=None, help="previous data/studies.csv with code links (default: git HEAD of main)")
    ap.add_argument("--extra-meta", default=os.path.join(DATA, "authors_cache.csv"), help="optional id,authors,link cache filled by scripts/enrich_metadata.py")
    a = ap.parse_args()

    S = a.sources
    cdir = a.catalogue_dir if os.path.isabs(a.catalogue_dir) else os.path.join(S, a.catalogue_dir)
    ver = re.search(r"(v\d+)", os.path.basename(cdir.rstrip("/"))).group(1)
    cat = rd(f"{cdir}/catalogue_{ver}.csv")
    nfs = rd(f"{cdir}/nf_{ver}.csv")
    dfs = rd(f"{cdir}/diffusion_{ver}.csv")
    dec = rd(f"{cdir}/decisions_all_{ver}.csv")
    listb = rd(os.path.join(S, a.listb))
    rel_p = os.path.join(cdir, f"related_studies_{ver}.csv")
    rel_map = {}      # record id (M..., CC...) -> study id, the source of truth for the "related" list
    if os.path.exists(rel_p):
        for x in rd(rel_p):
            for rid in split_ids(x["records"]):
                rel_map[rid] = x["study"]
    dup_p = os.path.join(cdir, "duplicates.csv")
    dups = [x for x in rd(dup_p) if x["verdict"] == "duplicate"] if os.path.exists(dup_p) else []

    import bibtexparser
    with open(a.bib, encoding="utf-8") as f:
        bib = {e["ID"]: e for e in bibtexparser.load(f, parser=bibtexparser.bparser.BibTexParser(common_strings=True)).entries}

    # --- Table S3 cells (start state, pairing, representation) -------------------------------------------------
    spec = importlib.util.spec_from_file_location("mk3", os.path.join(S, "tableS3/make_tableS3.py"))
    mk3 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mk3)
    coded = {}
    for fn in ("tableS3_coded_cells_v7.csv", "tableS3_coded_cells.csv"):
        p = os.path.join(S, "tableS3", fn)
        if os.path.exists(p):
            for r in rd(p):
                coded.setdefault(r["key"], r)

    def state_of(x):
        try:
            if x.get("printed_S3_record_json"):
                return mk3.printed(x)["state"]
            d = mk3.derive(x)
            cd = coded.get(x["key"])
            if cd and cd["state"] in ("2D", "3D"):
                d["state"] = d["state"].split()[0] + " " + cd["state"]
            return d["state"]
        except Exception:
            return ""

    # --- in-paper map: cited keys per part of the manuscript -------------------------------------------------
    def cites(path):
        t = open(path, encoding="utf-8").read()
        t = re.sub(r"(?m)^\s*%.*$", "", t)
        out = set()
        for m in re.finditer(r"\\(?:cite[a-z]*|fbcite|nocite)\*?(?:\[[^\]]*\])*\{([^}]*)\}", t):
            out |= {k.strip() for k in m.group(1).split(",")}
        return out

    M = a.manuscript
    where = collections.defaultdict(list)
    parts = [("main text", [f"{M}/air/sections/{n}" for n in sorted(os.listdir(f"{M}/air/sections")) if n.endswith(".tex") and "nocite" not in n and not n.startswith("03_")] +
              [f"{M}/air/tables/{n}" for n in sorted(os.listdir(f"{M}/air/tables")) if n.endswith(".tex")]),
             ("Note S1", [f"{M}/air/supplement/note_s1_results.tex"]),
             ("Note S2", [f"{M}/air/supplement/note_s2_search.tex"]),
             ("Table S3", [f"{M}/air/supplement/tableS3_catalogue.tex"]),
             ("Table S4", [f"{M}/air/supplement/tableS4_diffusion.tex"])]
    for lab, files in parts:
        ks = set()
        for fp in files:
            if os.path.exists(fp):
                ks |= cites(fp)
        for k in ks:
            where[k].append(lab)

    # --- previous repo data for code links ---------------------------------------------------------------------
    old_code, old_venue = {}, {}
    if a.old_studies and os.path.exists(a.old_studies):
        for r in rd(a.old_studies):
            if r.get("code"):
                old_code[r["key"]] = r["code"]
            old_venue[r["key"]] = r.get("venue", "")
    else:
        import subprocess
        try:
            txt = subprocess.run(["git", "-C", REPO, "show", "main:data/studies.csv"], capture_output=True, text=True, check=True).stdout
            for r in csv.DictReader(txt.splitlines()):
                if r.get("code"):
                    old_code[r["key"]] = r["code"]
                old_venue[r["key"]] = r.get("venue", "")
        except Exception:
            pass

    extra = {}
    if os.path.exists(a.extra_meta):
        for r in rd(a.extra_meta):
            extra[r["id"]] = r

    # --- raw records ---------------------------------------------------------------------------------------------
    recs = []   # each: dict(src, ids[], fields...)

    def add(src, ids, **kw):
        recs.append(dict(src=src, ids=[i for i in ids if i and not i.endswith(":")], **kw))

    for x in cat:
        add("catalogue", ["k:" + x["key"], tok(x["coding_id"]) if nz(x.get("coding_id")) else ""], key=x["key"], title=x["title"], year=x["year"], doi=x["doi"], row=x,
            family=x["method"], group=x["clinical_group"], task=FAM_TASK.get(x["family"], ""), modality=x["modality"])
    for src, rows in (("nf", nfs), ("diffusion", dfs)):
        for x in rows:
            add(src, ["k:" + x["key"], "u:" + x["id"]], key=x["key"], title=x["title"], year=x["year"], doi=x["doi"], row=x,
                family="NF" if src == "nf" else "diffusion", group=x["clinical_group"], task=FAM_TASK.get(x["family"], ""),
                modality=x["modality"])
    for x in listb:
        if rel_map and x["merged_id"] not in rel_map:
            continue          # List B record outside the related-studies file
        st = rel_map.get(x["merged_id"], "")
        add("related", ["m:" + x["merged_id"], "k:" + nz(x["catalogue_key"]), tok(st) if st else ""], key=nz(x["catalogue_key"]),
            title=x["title"], year=x["year"], doi=x["doi"], arxiv=x["arxiv"], venue=x["venue_best"],
            family=LISTB_FAM.get(x["family"], "other"), group=x["group"], modality=x["modality"], stream=x["stream"], row=x)
    if rel_map:   # related studies that are not List B records (citation chasing) join by study id
        for st in sorted(set(rel_map.values())):
            add("relmark", [tok(st)], key="", title="", year="", row={})
    for x in dups:   # dropped duplicate versions: keep their links on the kept row
        k_drop, k_keep = x["key_dropped_or_a"], x["key_kept_or_b"]
        e = bib.get(k_drop, {})
        add("dup", [tok(k_drop), tok(k_keep)], key="", title=delatex(e.get("title", "")) if e else "", year=e.get("year", ""),
            doi=e.get("doi", ""), arxiv=e.get("eprint", ""), row={}, dropped_key=k_drop)
    for x in dec:
        sid = x["id"]
        dup = nz(x.get("duplicate_of"))
        dids = []
        if dup:   # record of the same work (preprint + venue version): joins its target
            dids = ["u:" + dup if re.match(r"U\d+$", dup) else ("m:" + dup if re.match(r"M\d+$", dup) else "k:" + dup)]
        add("decision", ["m:" + nz(x["merged_id"]), "k:" + nz(x["key"]), ("u:" + sid) if re.match(r"U\d+", sid) else ("m:" + sid if re.match(r"M\d+", sid) else tok(sid))] + dids,
            key=nz(x["key"]), title=x["title"], year="", row=x, stream=x["stream"])

    # --- identity resolution -----------------------------------------------------------------------------------
    uf = UF()
    for i, r in enumerate(recs):
        node = f"r{i}"
        uf.f(node)
        for t in r["ids"]:
            uf.u(node, t)
        d = norm_doi(r.get("doi"))
        d2 = re.match(r"10\.48550/arxiv\.(.+)", d)
        ax = norm_arxiv(r.get("arxiv")) or (norm_arxiv(d2.group(1)) if d2 else "")
        if d and not d2:
            uf.u(node, "doi:" + d)
        if ax:
            uf.u(node, "arx:" + ax)
        nt = norm_title(r["title"])
        if len(nt) > 25:
            uf.u(node, "t:" + nt)
    groups = collections.defaultdict(list)
    for i, r in enumerate(recs):
        groups[uf.f(f"r{i}")].append(i)

    # fuzzy pass: near-identical titles of different groups (preprint vs. venue title edits)
    merge_log = []
    gl = list(groups)

    def gtitle(g):
        return norm_title(recs[groups[g][0]]["title"])

    def gyear(g):
        ys = [int(recs[i]["year"]) for i in groups[g] if re.match(r"\d{4}$", str(recs[i].get("year") or ""))]
        return ys[0] if ys else None
    byfirst = collections.defaultdict(list)
    for g in gl:
        byfirst[gtitle(g)[:6]].append(g)
    for bucket in byfirst.values():
        for i1 in range(len(bucket)):
            for i2 in range(i1 + 1, len(bucket)):
                g1, g2 = bucket[i1], bucket[i2]
                if uf.f(g1) == uf.f(g2):
                    continue
                t1, t2 = gtitle(g1), gtitle(g2)
                if len(t1) < 30 or len(t2) < 30:
                    continue
                y1, y2 = gyear(g1), gyear(g2)
                if y1 and y2 and abs(y1 - y2) > 1:
                    continue
                r = difflib.SequenceMatcher(None, t1, t2).ratio()
                if r >= 0.93:
                    merge_log.append((recs[groups[g1][0]]["title"], recs[groups[g2][0]]["title"], round(r, 3)))
                    uf.u(g1, g2)
    groups = collections.defaultdict(list)
    for i, r in enumerate(recs):
        groups[uf.f(f"r{i}")].append(i)

    # --- build merged rows ---------------------------------------------------------------------------------------
    rows = []
    used_ids = set()
    for g, idxs in groups.items():
        rs = [recs[i] for i in idxs]
        by = collections.defaultdict(list)
        for r in rs:
            by[r["src"]].append(r)
        key = next((r["key"] for r in rs if r.get("key")), "")
        mids = [t[2:] for r in rs for t in r["ids"] if t.startswith("m:") and len(t) > 2]
        uids = [t[2:] for r in rs for t in r["ids"] if t.startswith("u:") and len(t) > 2]
        sid = key or (mids[0] if mids else (uids[0] if uids else "x%d" % idxs[0]))
        if sid in used_ids:
            sid = sid + "_" + str(idxs[0])
        used_ids.add(sid)

        cands = by["catalogue"] or by["nf"] or by["diffusion"] or by["related"] or by["decision"]
        if not cands:
            print("WARNING: group without a source record, skipped:", [t for r in rs for t in r["ids"]][:4])
            continue
        primary = cands[0]
        lists = []
        if by["catalogue"]:
            lists.append("catalogue")
        if by["related"] or by["relmark"] or (by["catalogue"] and not rel_map):
            lists.append("related")
        if by["nf"]:
            lists.append("NF sample")
        if by["diffusion"]:
            lists.append("diffusion sample")
        status = ""
        decs = sorted(by["decision"], key=lambda r: r["row"]["decision"] != "include")
        if decs:
            d = decs[0]["row"]
            fs = d.get("final_set", "")
            if d["decision"] == "include":
                status = "included"
            elif fs == "diffusion_not_selected":
                status = "diffusion study not drawn into the comparison sample"
            elif d["decision"] == "not_retrieved":
                status = "full text not retrieved"
            else:
                status = "excluded at full text: " + (nz(d.get("reason")) or nz(d.get("reason_detail"))[:80])
        if not (by["catalogue"] or by["nf"] or by["diffusion"]) and decs and decs[0]["row"]["decision"] != "include":
            pass
        if not lists:
            lists.append("excluded")
        elif status and status != "included" and not (by["catalogue"] or by["nf"] or by["diffusion"]):
            lists.append("excluded")

        # --- bibliographic data
        e = bib.get(key, {}) if key else {}
        title = delatex(e.get("title")) if e.get("title") else delatex(primary["title"])
        if not e:
            # a title longer in another record
            title = delatex(max((r["title"] for r in rs if r["title"]), key=len))
        year = next((str(r["year"])[:4] for r in [primary] + rs if re.match(r"\d{4}", str(r.get("year") or ""))), "")
        if not year and e:
            year = e.get("year") or ""
        authors = fmt_authors(e.get("author")) if e else ""
        venue = venue_from_bib(e) if e else ""
        for r in rs:
            if not venue and r.get("venue") and r["src"] == "related":
                venue = delatex(re.split(r"\s+:\s+", r["venue"])[0])
        if key in old_venue and old_venue[key]:
            venue = old_venue[key]
        dois, arxs, urls = [], [], []
        for r in rs:
            for d in (r.get("doi"),):
                d = norm_doi(d)
                if d and d not in dois and not d.startswith("10.48550/arxiv."):
                    dois.append(d)
                m = re.match(r"10\.48550/arxiv\.(.+)", d)
                if m and norm_arxiv(m.group(1)) not in arxs:
                    arxs.append(norm_arxiv(m.group(1)))
            ax = norm_arxiv(r.get("arxiv"))
            if ax and ax not in arxs:
                arxs.append(ax)
        if e:
            d = norm_doi(e.get("doi"))
            if d and d.startswith("10.48550/arxiv."):
                arxs.insert(0, norm_arxiv(d[15:])) if norm_arxiv(d[15:]) not in arxs else None
            elif d:
                dois.insert(0, d) if d not in dois else None
            ax = norm_arxiv(e.get("eprint"))
            if ax and ax not in arxs:
                arxs.insert(0, ax)
            if e.get("url"):
                urls.append(e["url"])
        ex = extra.get(sid)
        if ex:
            authors = authors or ex.get("authors", "")
            venue = venue or ex.get("venue", "")
            year = year or ex.get("year", "")
            for l in (ex.get("link") or "").split(" ; "):
                if l.startswith("https://doi.org/") and norm_doi(l) not in dois:
                    dois.append(norm_doi(l))
                elif "arxiv.org/abs/" in l and norm_arxiv(l) not in arxs:
                    arxs.append(norm_arxiv(l))
                elif l and l not in urls:
                    urls.append(l)
        venue = clean_venue(venue)
        if not venue and arxs and not dois:
            venue = "arXiv"
        if not venue and dois and dois[0].startswith("10.1101/"):
            venue = "medRxiv/bioRxiv"
        allin = [("https://doi.org/" + d) for d in dois] + [("https://arxiv.org/abs/" + x) for x in arxs] + [u for u in urls]
        link = allin[0] if allin else ""
        alt = allin[1:]

        # --- coded fields
        crow = (by["catalogue"] or by["nf"] or by["diffusion"] or [{}])[0].get("row", {})
        coded_row = bool(crow)
        if by["catalogue"]:
            fam = crow.get("method") or "other"
        elif by["nf"]:
            fam = "NF"
        elif by["diffusion"]:
            fam = "diffusion"
        elif by["related"]:
            fam = by["related"][0]["family"]
        else:
            st = decs[0]["stream"]
            fam = {"nf_classic": "NF", "diffusion_sample": "diffusion"}.get(st, "other")
        fam = {"Other": "other"}.get(fam, fam)
        grp = (primary.get("group") or "")
        task = primary.get("task") or ""
        if not grp:
            for r in rs:
                if r.get("group"):
                    grp = r["group"]
                    break
        mod_raw = primary.get("modality") or next((r["modality"] for r in rs if r.get("modality")), "")
        row = dict(id=sid, title=title, authors=authors, year=year, venue=venue, link=link, alt_links=" ; ".join(alt),
                   code=old_code.get(key) or (find_code(crow.get("evidence", ""), crow.get("notes", ""), e.get("annote", "") if e else "") or [""])[0],
                   family=fam, clinical_group=grp, task_family=task, modality="; ".join(modality_of(mod_raw)),
                   anatomy="", start_state="", pairing="", construction="", representation="", dimension="", datasets="",
                   code_status="", in_paper="no", in_paper_where="", list="; ".join(lists), screening_status=status,
                   merged_from="")
        if coded_row and crow.get("Source"):
            row["start_state"] = START.get(crow["Source"], "")
            if crow.get("method") == "PF" and crow["Source"] == "N":
                row["start_state"] = "Poisson prior"
            row["pairing"] = CORR.get(crow.get("Corr", ""), "")
            row["construction"] = PATH.get(crow.get("Path", ""), "")
            st = state_of(crow)
            if st:
                rep, _, dim = st.partition(" ")
                row["representation"] = {"Pixel": "Image"}.get(rep, rep)
                row["dimension"] = dim
            ds = nz(crow.get("ext_public_datasets"))
            row["datasets"] = "; ".join(x.strip() for x in ds.split(";") if x.strip() and x.strip().lower() not in ("none", "n.r."))
            cs = nz(crow.get("ext_code_shared"))
            row["code_status"] = {"Y": "released", "promised": "promised", "N": "none"}.get(cs, "")
        row["_text"] = " ".join([title, grp, row["datasets"], (crow.get("evidence", "") or "")[:600], (crow.get("notes", "") or "")[:300]])
        row["anatomy"] = "; ".join(anatomy_of(row["_text"], grp, row["datasets"]))
        if row["code"] and not row["code_status"]:
            row["code_status"] = "released"
        ww = sorted({w for t in [key] + [x[2:] for r in rs for x in r["ids"] if x.startswith("k:")] + [r.get("dropped_key", "") for r in rs] for w in where.get(t, [])},
                    key=lambda w: ["main text", "Note S1", "Note S2", "Table S3", "Table S4"].index(w))
        if ww:
            row["in_paper"] = "yes"
            order = ["main text", "Note S1", "Note S2", "Table S3", "Table S4"]
            row["in_paper_where"] = "; ".join(w for w in order if w in ww)
        row["merged_from"] = "; ".join(sorted(set(t[2:] for r in rs for t in r["ids"] if t.startswith(("m:", "u:")) and len(t) > 2)))
        rows.append(row)

    # task family for rows without one: via clinical group of the catalogue
    g2t = collections.defaultdict(collections.Counter)
    for r in rows:
        if r["task_family"] and r["clinical_group"]:
            g2t[r["clinical_group"]][r["task_family"]] += 1
    for r in rows:
        if not r["task_family"]:
            c = g2t.get(r["clinical_group"])
            r["task_family"] = c.most_common(1)[0][0] if c else "Other"

    # sort and write
    def sk(r):
        return (-(int(r["year"]) if r["year"].isdigit() else 0), r["title"].lower())
    rows.sort(key=sk)
    FIELDS = ["id", "title", "authors", "year", "venue", "link", "alt_links", "code", "code_status", "family", "construction",
              "clinical_group", "task_family", "modality", "anatomy", "start_state", "pairing", "representation", "dimension",
              "datasets", "in_paper", "in_paper_where", "list", "screening_status", "merged_from"]
    os.makedirs(DATA, exist_ok=True)
    with open(f"{DATA}/studies.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with open(f"{DATA}/studies.json", "w", encoding="utf-8") as f:
        json.dump([{k: r[k] for k in FIELDS} for r in rows], f, ensure_ascii=False, indent=1)
    miss = [r for r in rows if not r["link"]]
    with open(f"{DATA}/missing_links.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "title", "year", "venue", "list", "searched"])
        for r in miss:
            w.writerow([r["id"], r["title"], r["year"], r["venue"], r["list"], "no DOI, arXiv id or URL in catalogue, List B or bibliography"])
    with open(f"{DATA}/merge_log.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["title_a", "title_b", "similarity"])
        w.writerows(merge_log)
    cnt = collections.Counter(l for r in rows for l in r["list"].split("; "))
    print("rows", len(rows), dict(cnt), "in_paper", sum(r["in_paper"] == "yes" for r in rows), "missing links", len(miss),
          "fuzzy merges", len(merge_log), "source", cdir)


if __name__ == "__main__":
    main()
