# Awesome Flow-Based Generative Models for Medical Imaging

A database of studies on flow-based generative models for medical imaging (flow matching, rectified flow, Schrödinger and paired bridges, Poisson flows), with diffusion and normalizing-flow studies as comparison samples. It accompanies our survey and holds every study the survey screened in, not only the ones it discusses. Studies the survey discusses are marked ★ (447 of 671).

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

671 distinct works. A work can belong to several lists, so the rows below do not add up to the total.

| List | Studies | What it holds |
|:--|--:|:--|
| catalogue | 383 | coded on the six design axes (Supplementary Data 1) |
| related | 592 | passed title and abstract screening (includes the catalogue) |
| NF sample | 17 | normalizing-flow comparison sample |
| diffusion sample | 55 | diffusion comparison sample (Supplementary Table S3) |
| excluded | 70 | recorded as excluded or not drawn into a sample; kept in the database only |

Marked ★: 447 studies discussed in the main text (301), Supplementary Note S1 (387), Supplementary Data 1 (383) or Table S3 (55); a study can appear in several places. 107 studies have a recorded code link.

| Model family | Studies |
|:--|--:|
| Flow matching (FM) | 205 |
| Rectified flow (RF) | 55 |
| Schrödinger bridge (SB) | 34 |
| Paired / Brownian bridge (PB) | 112 |
| Poisson flow (PF) | 14 |
| Normalizing flow (NF) | 154 |
| Diffusion | 72 |
| Other | 25 |

Catalogue (383 studies) by task family:

| Task family | Studies |
|:--|--:|
| Restoration | 114 |
| Translation and harmonization | 130 |
| Generation and forecasting | 83 |
| Analysis and segmentation | 56 |

## Views

| View | Pages |
|:--|--:|
| [By task](views/by_task/index.md) | 23 |
| [By model](views/by_model/index.md) | 21 |
| [By modality](views/by_modality/index.md) | 10 |
| [By anatomy](views/by_anatomy/index.md) | 14 |
| [By year](views/by_year.md) | 9 |
| [Datasets](views/datasets.md) | 411 datasets |

The views list the 647 studies that belong to the catalogue, the related studies or a comparison sample. The remaining 24 rows of the database are recorded exclusions.

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
| in_paper, in_paper_where | yes or no; main text, Note S1, Note S2, Supplementary Data 1, Table S3 (diffusion sample) |
| list | catalogue, related, NF sample, diffusion sample, excluded (semicolon-separated) |
| screening_status, merged_from | full-text decision; source ids merged into the row |
