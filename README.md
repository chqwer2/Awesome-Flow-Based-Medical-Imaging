# Awesome Flow-Based Generative Models for Medical Imaging

A database of studies on flow-based generative models for medical imaging (flow matching, rectified flow, Schrödinger and paired bridges, Poisson flows), with diffusion and normalizing-flow studies as comparison samples. It accompanies our survey and holds every study the survey screened in, not only the ones it discusses. Studies the survey discusses are marked ★ (454 of 688).

## Citation

The survey is under review. This entry is a placeholder and will be replaced by the final reference.

```bibtex
@article{xue2026generative,
  title   = {Generative transport models in medical imaging: a unified survey},
  author  = {Xue, Haowen and Chen, Hao and Hu, Hexuan and Li, Chao and Zhang, Tingbo and
             Sch{\"o}nlieb, Carola-Bibiane and Xu, Haoli and Han, Yi and Huang, Qian},
  journal = {Artificial Intelligence Review},
  year    = {2026},
  note    = {under review; citation to be updated on publication}
}
```

## How to use

- Browse the Markdown views below. Each view is a table of year, title (linked to the DOI, arXiv page or URL), venue, model family, task, ★ for studies in the paper, and a code link where one is recorded. Rows are sorted by year (newest first), then title.
- The database is `data/studies.csv` (also `data/studies.json`), one row per work. `data/missing_links.csv` lists rows for which no DOI, arXiv id or URL was found.
- To add or correct a study, edit `data/studies.csv` and run `python scripts/build_views.py`. The script rewrites this README and everything under `views/`; edit the data, not the generated files. It needs only Python 3.
- `scripts/ingest_sources.py` and `scripts/enrich_metadata.py` rebuild the CSV from the survey's working files (maintainers only; `--catalogue-dir` selects the catalogue version).

## Counts

688 distinct works. A work can belong to several lists, so the rows below do not add up to the total.

| List | Studies | What it holds |
|:--|--:|:--|
| catalogue | 390 | coded on the six design axes (Supplementary Table S3) |
| related | 606 | passed title and abstract screening (includes the catalogue) |
| NF sample | 17 | normalizing-flow comparison sample |
| diffusion sample | 55 | diffusion comparison sample (Supplementary Table S4) |
| excluded | 72 | recorded as excluded or not drawn into a sample; kept in the database only |

Marked ★: 454 studies discussed in the main text (291), Supplementary Note S1 (394), Table S3 (390) or Table S4 (55); a study can appear in several places. 107 studies have a recorded code link.

| Model family | Studies |
|:--|--:|
| Flow matching (FM) | 210 |
| Rectified flow (RF) | 57 |
| Schrödinger bridge (SB) | 38 |
| Paired / Brownian bridge (PB) | 114 |
| Poisson flow (PF) | 14 |
| Normalizing flow (NF) | 158 |
| Diffusion | 72 |
| Other | 25 |

Catalogue (390 studies) by task family:

| Task family | Studies |
|:--|--:|
| Restoration | 116 |
| Translation and harmonization | 132 |
| Generation and forecasting | 85 |
| Analysis and segmentation | 57 |

## Views

| View | Pages |
|:--|--:|
| [By task](views/by_task/index.md) | 23 |
| [By model](views/by_model/index.md) | 21 |
| [By modality](views/by_modality/index.md) | 10 |
| [By anatomy](views/by_anatomy/index.md) | 14 |
| [By year](views/by_year.md) | 9 |
| [Datasets](views/datasets.md) | 423 datasets |

The views list the 661 studies that belong to the catalogue, the related studies or a comparison sample. The remaining 27 rows of the database are recorded exclusions.

## Columns of data/studies.csv

| Column | Meaning |
|:--|:--|
| id | bibliography key where the survey has one, else a screening id |
| title, authors, year, venue | bibliographic data |
| link, alt_links | DOI, arXiv page or URL; other versions of the same work (preprint and venue version) |
| code, code_status | repository URL if recorded; released, promised or none |
| family | FM, RF, SB, PB, PF, NF, diffusion or other |
| construction, start_state, pairing | probability path, state where sampling begins, supervision or pairing (catalogue only) |
| representation, dimension | image, latent, wavelet, parameters or geometry; 2D or 3D (catalogue only) |
| clinical_group, task_family | task group and one of the four task families |
| modality, anatomy, datasets | semicolon-separated; anatomy is keyword-derived |
| in_paper, in_paper_where | yes or no; main text, Note S1, Note S2, Table S3, Table S4 |
| list | catalogue, related, NF sample, diffusion sample, excluded (semicolon-separated) |
| screening_status, merged_from | full-text decision; source ids merged into the row |
