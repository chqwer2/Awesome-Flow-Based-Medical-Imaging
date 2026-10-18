#!/usr/bin/env python3
"""Regenerate README.md from the data files in data/.

    python3 make_repo_readme.py

Plain Python 3, standard library only. data/studies.csv holds one row per
catalogued work (the survey's Supplementary Table S3 and Supplementary Data 1);
data/datasets.csv holds the named public releases (Supplementary Data 2).
"""
import csv
import os
import re
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data')

FAMILIES = OrderedDict([
    ('Restoration', 'Restoration and Reconstruction'),
    ('Translation and harmonization', 'Translation and Harmonization'),
    ('Generation and forecasting', 'Generation and Forecasting'),
    ('Analysis and segmentation', 'Analysis and Segmentation'),
])
TRANSPORT_ORDER = ['Flow matching', 'Rectified flow', 'Diffusion bridge',
                   'Schrödinger bridge', 'Poisson flow', 'Mean-reverting bridge',
                   'Variance-preserving path', 'Riemannian flow matching']
BADGE = ('https://img.shields.io/badge/code-181717?style=flat-square'
         '&logo=github&logoColor=white')
UNITS = {'p': 'patients', 'e': 'exams', 'i': 'images', 's': 'scans'}
ACCESS = {'Open': 'open', 'Reg.': 'registration', 'Restr.': 'reviewed application'}


def read(name):
    with open(os.path.join(DATA, name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def slug(text):
    return re.sub(r'[^a-z0-9 -]', '', text.lower()).replace(' ', '-')


def bar(n, top, width=20):
    return '`' + '#' * max(1, round(width * n / top)) + '` ' + str(n)


def repo_label(url):
    return re.sub(r'^https?://(www\.)?', '', url).rstrip('/')


def main():
    studies = read('studies.csv')
    datasets = sorted(read('datasets.csv'), key=lambda d: -int(d['works']))
    coded = [s for s in studies if s['code']]
    n, nc = len(studies), len(coded)

    L = []
    A = L.append
    A('# Awesome Flow-Based Generative Models for Medical Imaging [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)')
    A('')
    A('[![Paper](https://img.shields.io/badge/paper-Artificial%20Intelligence%20Review-b31b1b.svg)](#citation)')
    A(f'[![Works](https://img.shields.io/badge/works-{n}-blue.svg)](#contents)')
    A(f'[![Code](https://img.shields.io/badge/with%20code-{nc}-green.svg)](#implementations)')
    A('[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)')
    A('')
    A('A curated list of **flow-based generative models for medical imaging** --- flow')
    A('matching, rectified flow, diffusion and Schrödinger bridges, and Poisson flows ---')
    A(f'accompanying our survey. It covers **{n} works**, of which **{nc} publish code**.')
    A('')
    A('Every list here is generated from the data files in `data/`, which follow the')
    A("survey's catalogue (Supplementary Table S3 and Supplementary Data 1--2). Run")
    A('`python3 make_repo_readme.py` to regenerate.')
    A('')
    A('## Contents')
    A('')
    for title in FAMILIES.values():
        A(f'- [{title}](#{slug(title)})')
    for title in ('Implementations', 'Datasets', 'What the literature measures',
                  'Citation', 'Contributing'):
        A(f'- [{title}](#{slug(title)})')
    A('')
    A('**Venue** links to the DOI, or to arXiv where the work is a preprint.')
    A('')
    A(f'**Code** &nbsp; [![code]({BADGE})](#implementations) the official repository; the badge links to it.')
    A('')

    for fam, title in FAMILIES.items():
        rows = [s for s in studies if s['family'] == fam]
        A(f'## {title}')
        A('')
        A(f'*{len(rows)} works.*')
        A('')
        A('| Method | Title | Task | Family | Modality | Venue | Year | Code |')
        A('|:--|:--|:--|:--|:--|:--|:--:|:--:|')
        for s in rows:
            venue = f"[{s['venue']}]({s['link']})" if s['link'] else s['venue']
            code = f"[![code]({BADGE})]({s['code']})" if s['code'] else ''
            A(f"| **{s['method']}** | {s['title']} | {s['subgroup']} | {s['transport']} "
              f"| {s['modality']} | {venue} | {s['year']} | {code} |")
        A('')

    A('## Implementations')
    A('')
    A(f'The {nc} works that publish a repository, grouped by the transport they learn.')
    A('')
    by = OrderedDict((t, []) for t in TRANSPORT_ORDER)
    for s in coded:
        by.setdefault(s['transport'], []).append(s)
    for t, rows in by.items():
        if not rows:
            continue
        rows = sorted(rows, key=lambda s: s['method'].lower())
        A('<details open>')
        A(f'<summary><b>{t}</b> ({len(rows)})</summary>')
        A('')
        A('| Method | Year | Repository |')
        A('|---|---|---|')
        for s in rows:
            A(f"| {s['method']} | {s['year']} | [{repo_label(s['code'])}]({s['code']}) |")
        A('')
        A('</details>')
        A('')

    A('## Datasets')
    A('')
    A('Public releases used by four or more reviewed works. Size is the named release,')
    A('not the sample a work used, and counts pool releases of the same dataset.')
    A('')
    A('| Dataset | Anatomy / modality | Size | Access | Works | Restoration | Translation | Generation | Analysis |')
    A('|:--|:--|--:|:--|--:|--:|--:|--:|--:|')
    for d in datasets:
        size = f"{d['size']} {UNITS[d['unit']]}"
        A(f"| [{d['dataset']}]({d['url']}) | {d['anatomy_modality']} | {size} | "
          f"{ACCESS[d['access']]} | {d['works']} | {d['restoration']} | "
          f"{d['translation']} | {d['generation']} | {d['analysis']} |")
    A('')

    A('## What the literature measures')
    A('')
    A(f'Over all {n} works.')
    A('')
    rep = OrderedDict([
        ('Sampling steps reported', sum(s['steps'] != 'n.r.' for s in studies)),
        ('ODE sampler', sum(s['sampler'] == 'ODE' for s in studies)),
        ('SDE sampler', sum(s['sampler'] == 'SDE' for s in studies)),
        ('One network pass', sum(s['sampler'] == 'Direct' for s in studies)),
        ('Repeated draws per input', sum(s['draws'] == 'Yes' for s in studies)),
        ('Test on data outside the training source', sum(s['external'] != '0' for s in studies)),
    ])
    top = max(rep.values())
    A('| Reported | Works |')
    A('|---|---|')
    for k, v in rep.items():
        A(f'| {k} | {bar(v, top)} |')
    A('')
    internal = sum(s['external'] == '0' for s in studies)
    single = sum(s['draws'] == 'No' for s in studies)
    A(f'Most works test only on data from their training source ({internal} of {n})')
    A(f'and report a single draw per input ({single} of {n}).')
    A('')

    A('## Citation')
    A('')
    A('```bibtex')
    A('@article{xue2026generative,')
    A('  title   = {Generative transport models in medical imaging: a unified survey},')
    A('  author  = {Xue, Haowen and Chen, Hao and Hu, Hexuan and Li, Chao and Zhang, Tingbo and')
    A('             Sch{\\"o}nlieb, Carola-Bibiane and Xu, Haoli and Han, Yi and Huang, Qian},')
    A('  journal = {Artificial Intelligence Review},')
    A('  year    = {2026},')
    A('  note    = {under review}')
    A('}')
    A('```')
    A('')
    A('## Contributing')
    A('')
    A('Pull requests are welcome. Please add a work by adding a row to `data/studies.csv`')
    A('(and a release to `data/datasets.csv`), then run `python3 make_repo_readme.py`.')
    A('This file is generated, so a direct edit to it will be overwritten.')

    with open(os.path.join(HERE, 'README.md'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
