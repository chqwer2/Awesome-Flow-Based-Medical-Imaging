#!/usr/bin/env python3
"""Regenerate README.md and views/ from data/studies.csv.

    python scripts/build_views.py

Plain Python 3, standard library only. Edit data/studies.csv (one row per work), then run this script.
data/datasets.csv is optional metadata (size, access, URL) for named datasets used in views/datasets.md.
Every Markdown file in README.md and views/ is overwritten; edit the data, not the views.
"""
import collections
import csv
import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
VIEWS = os.path.join(ROOT, "views")

FAMILY_ORDER = ["FM", "RF", "SB", "PB", "PF", "NF", "diffusion", "other"]
FAMILY_NAME = {"FM": "Flow matching (FM)", "RF": "Rectified flow (RF)", "SB": "Schrödinger bridge (SB)",
               "PB": "Paired / Brownian bridge (PB)", "PF": "Poisson flow (PF)", "NF": "Normalizing flow (NF)",
               "diffusion": "Diffusion", "other": "Other"}
TASK_ORDER = ["Restoration", "Translation and harmonization", "Generation and forecasting",
              "Analysis and segmentation", "Other"]
LIST_ORDER = ["catalogue", "related", "NF sample", "diffusion sample", "excluded"]
LIST_NOTE = {"catalogue": "coded on the six design axes (Supplementary Data 1)",
             "related": "passed title and abstract screening (includes the catalogue)",
             "NF sample": "normalizing-flow comparison sample",
             "diffusion sample": "diffusion comparison sample (Supplementary Table S3)",
             "excluded": "recorded as excluded or not drawn into a sample; kept in the database only"}
CITATION = """```bibtex
@article{xue2026generative,
  title   = {Generative transport models in medical imaging: a unified survey},
  author  = {Xue, Haowen and Chen, Hao and Hu, Hexuan and Li, Chao and Zhang, Tingbo and
             Sch{\\"o}nlieb, Carola-Bibiane and Xu, Haoli and Han, Yi and Huang, Qian},
  journal = {Artificial Intelligence Review},
  year    = {2026},
  note    = {under review; citation to be updated on publication}
}
```"""


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "other"


def gh_anchor(text):
    """GitHub heading anchor: lower case, punctuation dropped, spaces to hyphens."""
    return re.sub(r"[^a-z0-9 _-]", "", text.lower()).replace(" ", "-")


def esc(t):
    t = t.replace("\\", "\\\\")
    for ch in "|[]*_<>`":
        t = t.replace(ch, "\\" + ch)
    return t.replace("\n", " ")


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def row_key(r):
    return (-(int(r["year"]) if r["year"].isdigit() else 0), r["title"].lower())


def table(rows, show_group=False):
    rows = sorted(rows, key=row_key)
    out = ["| Year | Title | Venue | Family | Task | In paper | Code |", "|--:|:--|:--|:--|:--|:--:|:--:|"]
    for r in rows:
        title = esc(r["title"])
        if r["link"]:
            title = f"[{title}]({r['link']})"
        venue = esc(r["venue"][:48] + ("..." if len(r["venue"]) > 48 else ""))
        task = esc(r["clinical_group"] or r["task_family"])
        code = f"[code]({r['code']})" if r["code"] else ""
        out.append(f"| {r['year']} | {title} | {venue} | {r['family']} | {task} | {'★' if r['in_paper'] == 'yes' else ''} | {code} |")
    return out


def page(path, title, intro, rows, back):
    """Write one view with a navigation line; `back` = list of (label, relative target)."""
    nav = " · ".join(f"[{a}]({b})" for a, b in back)
    n_star = sum(r["in_paper"] == "yes" for r in rows)
    n_code = sum(bool(r["code"]) for r in rows)
    L = [f"# {title}", "", nav, "", f"{intro} {len(rows)} studies, {n_star} marked ★ (discussed in the paper), {n_code} with code.", ""]
    L += table(rows)
    L.append("")
    write(path, L)


def write(path, lines):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def index_page(path, title, intro, groups, back, extra=None):
    """groups: list of (heading, [(label, file, n, n_star)])."""
    L = [f"# {title}", "", " · ".join(f"[{a}]({b})" for a, b in back), "", intro, ""]
    for head, items in groups:
        if head:
            L += [f"## {head}", ""]
        L += ["| View | Studies | ★ |", "|:--|--:|--:|"]
        for label, fn, n, ns in items:
            L.append(f"| [{esc(label)}]({fn}) | {n} | {ns} |")
        L.append("")
    write(path, L)


def main():
    rows_all = read_csv(os.path.join(DATA, "studies.csv"))
    shown = [r for r in rows_all if set(split(r["list"])) - {"excluded"}]
    for r in rows_all:
        r["family"] = r["family"] or "other"
    meta = {}
    mp = os.path.join(DATA, "datasets.csv")
    if os.path.exists(mp):
        for d in read_csv(mp):
            meta[d["dataset"].lower()] = d

    if os.path.isdir(VIEWS):
        shutil.rmtree(VIEWS)
    os.makedirs(VIEWS)
    home = ("Home", "../../README.md")
    home1 = ("Home", "../README.md")

    def group_rows(keyfn):
        g = collections.defaultdict(list)
        for r in shown:
            for k in keyfn(r) or ["Unspecified"]:
                g[k].append(r)
        return g

    def count(rs):
        return len(rs), sum(r["in_paper"] == "yes" for r in rs)

    index = {}

    # ---- by task ---------------------------------------------------------------------------------------------
    def task_key(r):
        g = r["clinical_group"]
        return [g if g and not g.startswith("Other") else "Other tasks"]
    g = group_rows(task_key)
    grp_family = {}
    for r in shown:
        k = task_key(r)[0]
        grp_family.setdefault(k, collections.Counter())[r["task_family"] or "Other"] += 1
    sections = collections.defaultdict(list)
    for k, rs in g.items():
        fam = grp_family[k].most_common(1)[0][0] if k != "Other tasks" else "Other"
        fn = slug(k) + ".md"
        page(os.path.join(VIEWS, "by_task", fn), f"Task: {k}", f"Studies in the clinical task group “{k}” (task family: {fam}).",
             rs, [home, ("Task index", "index.md")])
        sections[fam].append((k, fn) + count(rs))
    groups = [(fam, sorted(sections[fam], key=lambda x: -x[2])) for fam in TASK_ORDER if sections.get(fam)]
    index_page(os.path.join(VIEWS, "by_task", "index.md"), "By task", "Clinical task groups, under the four task families of the survey.",
               groups, [home])
    index["Task"] = ("views/by_task/index.md", len(g))

    # ---- by model --------------------------------------------------------------------------------------------
    items = []
    fam_g = group_rows(lambda r: [r["family"]])
    for fam in FAMILY_ORDER:
        if fam in fam_g:
            fn = f"family-{slug(fam)}.md"
            page(os.path.join(VIEWS, "by_model", fn), f"Model family: {FAMILY_NAME[fam]}",
                 "Studies by the model family they train.", fam_g[fam], [home, ("Model index", "index.md")])
            items.append((FAMILY_NAME[fam], fn) + count(fam_g[fam]))
    con_g = group_rows(lambda r: [r["construction"]] if r["construction"] else [])
    con_items = []
    for k, rs in sorted(con_g.items(), key=lambda kv: -len(kv[1])):
        fn = f"construction-{slug(k)}.md"
        page(os.path.join(VIEWS, "by_model", fn), f"Construction: {k}",
             "Studies of the catalogue by the probability path that connects the two end states.", rs, [home, ("Model index", "index.md")])
        con_items.append((k, fn) + count(rs))
    start_g = group_rows(lambda r: [r["start_state"]] if r["start_state"] else [])
    start_items = []
    for k, rs in sorted(start_g.items(), key=lambda kv: -len(kv[1])):
        fn = f"start-{slug(k)}.md"
        page(os.path.join(VIEWS, "by_model", fn), f"Start state: {k}",
             "Studies of the catalogue by the state from which sampling begins.", rs, [home, ("Model index", "index.md")])
        start_items.append((k, fn) + count(rs))
    index_page(os.path.join(VIEWS, "by_model", "index.md"), "By model",
               "Model family, probability path (construction) and start state.",
               [("Family", items), ("Construction (probability path)", con_items), ("Start state", start_items)], [home])
    index["Model"] = ("views/by_model/index.md", len(items) + len(con_items) + len(start_items))

    # ---- by modality / anatomy -------------------------------------------------------------------------------
    for name, col, label in (("by_modality", "modality", "Modality"), ("by_anatomy", "anatomy", "Anatomy")):
        g = group_rows(lambda r, c=col: split(r[c]))
        its = []
        for k, rs in sorted(g.items(), key=lambda kv: (kv[0] == "Unspecified", -len(kv[1]))):
            fn = slug(k) + ".md"
            page(os.path.join(VIEWS, name, fn), f"{label}: {k}", f"Studies by {label.lower()}; a study with several appears in each.",
                 rs, [home, (f"{label} index", "index.md")])
            its.append((k, fn) + count(rs))
        note = ("Anatomy is assigned from title, task group and datasets by keyword rules (scripts/ingest_sources.py) and can be "
                "corrected in data/studies.csv." if col == "anatomy" else "A study with several modalities appears under each.")
        index_page(os.path.join(VIEWS, name, "index.md"), f"By {label.lower()}", note, [("", its)], [home])
        index[label] = (f"views/{name}/index.md", len(its))

    # ---- by year ---------------------------------------------------------------------------------------------
    years = collections.defaultdict(list)
    for r in shown:
        years[r["year"] or "n.d."].append(r)
    L = ["# By year", "", "[Home](../README.md)", "", f"{len(shown)} studies, newest first.", "",
         "| Year | Studies | ★ | With code |", "|--:|--:|--:|--:|"]
    for y in sorted(years, reverse=True):
        rs = years[y]
        L.append(f"| [{y}](#{y.lower().replace('.', '')}) | {len(rs)} | {count(rs)[1]} | {sum(bool(r['code']) for r in rs)} |")
    L.append("")
    for y in sorted(years, reverse=True):
        L += [f"## {y}", ""] + table(years[y]) + [""]
    write(os.path.join(VIEWS, "by_year.md"), L)
    index["Year"] = ("views/by_year.md", len(years))

    # ---- datasets --------------------------------------------------------------------------------------------
    dg = group_rows(lambda r: split(r["datasets"]))
    dg.pop("Unspecified", None)
    ranked = sorted(dg.items(), key=lambda kv: (-len(kv[1]), kv[0].lower()))
    L = ["# Datasets", "", "[Home](../README.md)", "",
         f"{len(dg)} named datasets are used by the {sum(1 for r in shown if r['datasets'])} catalogued studies with a recorded dataset. "
         "The table lists datasets used by two or more studies; datasets used by three or more get a section below. "
         "Single-use datasets are in the `datasets` column of `data/studies.csv`.", "",
         "| Dataset | Studies | ★ | Details |", "|:--|--:|--:|:--|"]
    multi = [(k, rs) for k, rs in ranked if len(rs) >= 2]
    for k, rs in multi:
        m = meta.get(k.lower())
        det = ""
        if m:
            det = f"[{esc(m['anatomy_modality'])}, {m['size']}]({m['url']})" if m.get("url") else esc(m["anatomy_modality"])
        anchor = gh_anchor(k)
        name = f"[{esc(k)}](#{anchor})" if len(rs) >= 3 else esc(k)
        L.append(f"| {name} | {len(rs)} | {count(rs)[1]} | {det} |")
    L.append("")
    for k, rs in multi:
        if len(rs) >= 3:
            L += [f"## {k}", ""] + table(rs) + [""]
    write(os.path.join(VIEWS, "datasets.md"), L)
    index["Dataset"] = ("views/datasets.md", len(dg))

    # ---- README ----------------------------------------------------------------------------------------------
    lists = collections.Counter(l for r in rows_all for l in split(r["list"]))
    n_star = sum(r["in_paper"] == "yes" for r in rows_all)
    n_code = sum(bool(r["code"]) for r in rows_all)
    cat = [r for r in rows_all if "catalogue" in split(r["list"])]
    where = collections.Counter(w for r in rows_all for w in split(r["in_paper_where"]))
    fam_c = collections.Counter(r["family"] for r in rows_all)
    task_c = collections.Counter(r["task_family"] for r in cat)
    L = ["# Awesome Flow-Based Generative Models for Medical Imaging", "",
         "A database of studies on flow-based generative models for medical imaging (flow matching, rectified flow, "
         "Schrödinger and paired bridges, Poisson flows), with diffusion and normalizing-flow studies as comparison samples. "
         "It accompanies our survey and holds every study the survey screened in, not only the ones it discusses. "
         f"Studies the survey discusses are marked ★ ({n_star} of {len(rows_all)}).", "",
         "## Citation", "",
         "The survey is under review. This entry is a placeholder and will be replaced by the final reference.", "", CITATION, "",
         "## How to use", "",
         "- Browse the Markdown views below. Each view is a table of year, title (linked to the DOI, arXiv page or URL), venue, "
         "model family, task, ★ for studies in the paper, and a code link where one is recorded. Rows are sorted by year (newest first), then title.",
         "- The database is `data/studies.csv` (also `data/studies.json`), one row per work. `data/missing_links.csv` lists rows "
         "for which no DOI, arXiv id or URL was found.",
         "- To add or correct a study, edit `data/studies.csv` and run `python scripts/build_views.py`. The script rewrites this "
         "README and everything under `views/`; edit the data, not the generated files. It needs only Python 3.",
         "- `scripts/ingest_sources.py` and `scripts/enrich_metadata.py` rebuild the CSV from the survey's working files "
         "(maintainers only; `--catalogue-dir` selects the catalogue version).", "",
         "## Counts", "",
         f"{len(rows_all)} distinct works. A work can belong to several lists, so the rows below do not add up to the total.", "",
         "| List | Studies | What it holds |", "|:--|--:|:--|"]
    for l in LIST_ORDER:
        if lists[l]:
            L.append(f"| {l} | {lists[l]} | {LIST_NOTE[l]} |")
    L += ["", f"Marked ★: {n_star} studies discussed in the main text ({where['main text']}), Supplementary Note S1 ({where['Note S1']}), "
          f"Supplementary Data 1 ({where['Table S3']}) or Table S3 ({where['Table S4']}); a study can appear in several places. "
          f"{n_code} studies have a recorded code link.", "",
          "| Model family | Studies |", "|:--|--:|"]
    for f in FAMILY_ORDER:
        if fam_c[f]:
            L.append(f"| {FAMILY_NAME[f]} | {fam_c[f]} |")
    L += ["", f"Catalogue ({len(cat)} studies) by task family:", "", "| Task family | Studies |", "|:--|--:|"]
    for t in TASK_ORDER:
        if task_c[t]:
            L.append(f"| {t} | {task_c[t]} |")
    L += ["", "## Views", "", "| View | Pages |", "|:--|--:|"]
    for k in ("Task", "Model", "Modality", "Anatomy"):
        p, n = index[k]
        L.append(f"| [By {k.lower()}]({p}) | {n} |")
    L.append(f"| [By year]({index['Year'][0]}) | {index['Year'][1]} |")
    L.append(f"| [Datasets]({index['Dataset'][0]}) | {index['Dataset'][1]} datasets |")
    L += ["", f"The views list the {len(shown)} studies that belong to the catalogue, the related studies or a comparison sample. "
          f"The remaining {len(rows_all) - len(shown)} rows of the database are recorded exclusions.", "",
          "## Columns of data/studies.csv", "",
          "| Column | Meaning |", "|:--|:--|",
          "| id | bibliography key where the survey has one, else a screening id |",
          "| title, authors, year, venue | bibliographic data |",
          "| link, alt_links | DOI, arXiv page or URL; other versions of the same work (preprint and venue version) |",
          "| code, code_status | repository URL if recorded; released, promised or none |",
          "| family | FM, RF, SB, PB, PF, NF, diffusion or other |",
          "| construction, start_state, pairing | probability path, state where sampling begins, supervision or pairing (catalogue only) |",
          "| representation, dimension | image, latent, wavelet, parameters or geometry; 2D or 3D (catalogue only) |",
          "| clinical_group, task_family | task group and one of the four task families |",
          "| modality, anatomy, datasets | semicolon-separated; anatomy is keyword-derived |",
          "| in_paper, in_paper_where | yes or no; main text, Note S1, Note S2, Supplementary Data 1, Table S3 (diffusion sample) |",
          "| list | catalogue, related, NF sample, diffusion sample, excluded (semicolon-separated) |",
          "| screening_status, merged_from | full-text decision; source ids merged into the row |", ""]
    write(os.path.join(ROOT, "README.md"), L)

    # json mirror (kept in sync with the csv)
    with open(os.path.join(DATA, "studies.json"), "w", encoding="utf-8") as f:
        json.dump(rows_all, f, ensure_ascii=False, indent=1)
    print(f"{len(rows_all)} studies, {len(shown)} in views, {sum(1 for _ in os.walk(VIEWS) for _ in _[2])} view files")


if __name__ == "__main__":
    main()
