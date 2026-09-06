import sys, io, contextlib, re, glob, collections
sys.path.insert(0, '.')
src = open('check_manuscript.py', encoding='utf-8').read()
cut = src.index("check('prose: the task-measure share barely moved between the cohorts'")
ns = {'__file__': 'check_manuscript.py'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], 'cm', 'exec'), ns)
ROWS, arx, MW, CD, DD = ns['ROWS'], ns['_arx'], ns['_MW'], ns['_CD'], ns['_DD']
fam, year, kind = ns['fam'], ns['year'], ns['kind']

# bibliography: title and venue per key
bib = open('main.bib', encoding='utf-8').read()
meta = {}
for m in re.finditer(r'@(\w+)\{([^,]+),(.*?)\n\}', bib, re.S):
    body = m.group(3)
    def fld(n):
        mm = re.search(n + r'\s*=\s*\{(.*?)\}\s*,?\s*\n', body, re.S)
        return ' '.join(mm.group(1).split()) if mm else ''
    meta[m.group(2).strip()] = (fld('title'), fld('journal') or fld('booktitle'))


ACC = {}
for _a, _c in ((chr(92) + chr(34) + 'o', chr(246)),
               (chr(92) + chr(34) + 'u', chr(252)),
               (chr(92) + chr(34) + 'a', chr(228)),
               (chr(92) + chr(39) + 'e', chr(233)),
               (chr(92) + chr(39) + 'a', chr(225)),
               (chr(92) + chr(39) + 'o', chr(243)),
               (chr(92) + chr(96) + 'e', chr(232)),
               (chr(92) + '^o', chr(244)),
               (chr(92) + '~n', chr(241))):
    ACC[_a] = _c

VENUE = [
    (r'^Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition$', 'CVPR'),
    (r'^Proceedings of the IEEE/CVF International Conference on Computer Vision$', 'ICCV'),
    (r'^International Conference on Medical Image Computing and Computer-Assisted Intervention$', 'MICCAI'),
    (r'^Medical Image Computing and Computer.Assisted Intervention.*$', 'MICCAI'),
    (r'^International Conference on Learning Representations$', 'ICLR'),
    (r'^International Conference on Machine Learning$', 'ICML'),
    (r'^Advances in Neural Information Processing Systems$', 'NeurIPS'),
    (r'^European Conference on Computer Vision.*$', 'ECCV'),
    (r'^Medical Imaging with Deep Learning$', 'MIDL'),
    (r'^arXiv preprint.*$', 'arXiv'),
    (r'^IEEE Transactions on ', 'IEEE TMI ' if False else 'IEEE Trans. '),
]

def tidy(t):
    for k, v in ACC.items():
        t = t.replace('{' + k + '}', v).replace(k, v)
    t = t.replace('{', '').replace('}', '').replace('\\&', '&')
    return ' '.join(t.split())

def venue(v):
    v = tidy(v)
    for pat, rep in VENUE:
        if re.match(pat, v):
            return re.sub(pat, rep, v) if rep.endswith(' ') else rep
    return v

APP = {'04_app1_processing.tex': 'Image Processing and Restoration',
       '04_app2_translation.tex': 'Cross-Modal Translation and Harmonization',
       '04_app3_generation.tex': 'Image Generation and Augmentation',
       '04_app4_analysis.tex': 'Analysis: Classification, Segmentation, Detection'}
ORDER = list(APP.values())

def slug(t):
    return re.sub(r'[^a-z0-9 -]', '', t.lower()).replace(' ', '-')

groups = collections.defaultdict(lambda: collections.defaultdict(list))
for r in ROWS:
    app = APP.get(r['file'].split('/')[-1])
    if app:
        groups[app][r.get('group', 'Other')].append(r)

L = []
A = L.append
A('# Awesome Flow-Based Generative Models for Medical Imaging [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)')
A('')
A('[![Paper](https://img.shields.io/badge/paper-Medical%20Image%20Analysis-b31b1b.svg)](#citation)')
A('[![Works](https://img.shields.io/badge/works-%d-blue.svg)](#contents)' % len(ROWS))
A('[![Code](https://img.shields.io/badge/with%%20code-%d-green.svg)](#implementations)'
  % len(CD.CODE))
A('[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)')
A('')
A('A curated list of **flow-based generative models for medical imaging** --- normalizing')
A('flows, flow matching, rectified flow, and Schrödinger and Brownian bridges ---')
A('accompanying our survey. It covers **%d works**, of which **%d publish code**.'
  % (len(ROWS), len(CD.CODE)))
A('')
A('Every list here is generated from the same source files the paper builds its tables')
A('from, so the repository and the manuscript cannot drift apart. Run')
A('`python3 make_repo_readme.py` to regenerate.')
A('')
A('## Contents')
A('')
for app in ORDER:
    if app in groups:
        A('- [%s](#%s)' % (app, slug(app)))
A('- [Implementations](#implementations)')
A('- [Datasets](#datasets)')
A('- [What the literature measures](#what-the-literature-measures)')
A('- [Citation](#citation)')
A('- [Contributing](#contributing)')
A('')
A('**[`code`]** a repository is printed &nbsp;&middot;&nbsp; '
  '`code promised` promised without a link &nbsp;&middot;&nbsp; '
  '`no code` neither &nbsp;&middot;&nbsp; '
  '`no preprint` full text could not be reached, so nothing is claimed either way')
A('')

def badge(r):
    # three near-identical emoji did not scan; a visible word does. A link that is
    # there reads as a link, and one that is not says why in plain text.
    i = arx.get(r['key'], '')
    if CD.CODE.get(i):
        return '**[`code`](%s)**' % CD.CODE[i]
    if i in getattr(CD, 'PROMISED', {}):
        return '`code promised`'
    if i not in MW:
        return '`no preprint`'
    return '`no code`'

for app in ORDER:
    if app not in groups:
        continue
    n = sum(len(v) for v in groups[app].values())
    A('## %s' % app)
    A('')
    A('*%d works.*' % n)
    A('')
    for g in sorted(groups[app]):
        rs = sorted(groups[app][g], key=lambda r: (-(year(r['key']) or 0), r['name'].lower()))
        A('### %s' % g)
        A('')
        for r in rs:
            t, v = meta.get(r['key'], ('', ''))
            bits = ['**%s**' % r['name']]
            if t:
                bits.append('*%s*' % tidy(t))
            tail = ', '.join(x for x in (venue(v), str(year(r['key']) or '')) if x)
            if tail:
                bits.append(tail)
            A('- %s %s' % (' &mdash; '.join(bits), badge(r)))
            A('  <br/><sub>%s &nbsp;|&nbsp; %s</sub>'
              % (fam(r['family']), r.get('modality', '')))
        A('')

# ---- implementations ----
A('## Implementations')
A('')
repo_rows = [r for r in ROWS if CD.CODE.get(arx.get(r['key'], ''))]
A('The %d works that publish a repository, grouped by the transport they learn.'
  % len(repo_rows))
A('')
byfam = collections.defaultdict(list)
for r in repo_rows:
    byfam[fam(r['family'])].append(r)
for f in sorted(byfam, key=lambda k: (-len(byfam[k]), k)):
    A('<details open>')
    A('<summary><b>%s</b> (%d)</summary>' % (f, len(byfam[f])))
    A('')
    A('| Method | Year | Repository |')
    A('|---|---|---|')
    for r in sorted(byfam[f], key=lambda r: r['name'].lower()):
        u = CD.CODE[arx[r['key']]]
        A('| %s | %s | [%s](%s) |'
          % (r['name'], year(r['key']) or '--', u.replace('https://', '').replace('http://', ''), u))
    A('')
    A('</details>')
    A('')

# ---- datasets ----
A('## Datasets')
A('')
fams, who = collections.Counter(), collections.defaultdict(list)
for k in DD.DATASETS:
    for f in DD.usable(k):
        fams[f] += 1
        who[f].append(k)
shared = sorted([f for f in fams if fams[f] >= 2], key=lambda f: (-fams[f], f.lower()))
A('Public dataset families used by more than one reviewed work. A shared dataset is')
A('not yet a comparison: the works on it must also report a measure in common, which')
A('is the last column.')
A('')
A('| Dataset family | Works | Metrics shared by two or more |')
A('|---|---|---|')
for f in shared:
    ms = [set(MW.get(k, [])) for k in who[f]]
    common = set()
    for i in range(len(ms)):
        for j in range(i + 1, len(ms)):
            common |= ms[i] & ms[j]
    A('| %s | %d | %s |' % (f, fams[f], ', '.join(sorted(common, key=str.lower)) or '--'))
A('')
A('Version families are merged, so BraTS 2021 and BraTS 2023 count as the same footing.')
A('')

# ---- metrics ----
A('## What the literature measures')
A('')
readable = [r for r in ROWS if arx.get(r['key']) in MW]
met = collections.Counter()
for r in readable:
    for t in set(MW[arx[r['key']]]):
        met[t] += 1
A('Over the %d works whose full text could be read.' % len(readable))
A('')
A('| Metric | Works reporting it |')
A('|---|---|')
for m, n in met.most_common(15):
    bar = '#' * max(1, round(20.0 * n / met.most_common(1)[0][1]))
    A('| %s | `%s` %d |' % (m, bar, n))
A('')
A('The survey argues that what is *not* measured matters more: no reviewed work reports')
A('external, prospective or reader-in-the-loop evaluation.')
A('')

# ---- citation & contributing ----
A('## Citation')
A('')
A('```bibtex')
A('@article{chen2026flow,')
A('  title   = {Flow-Based Generative Models for Medical Imaging},')
A('  author  = {Chen, Hao and others},')
A('  journal = {Medical Image Analysis},')
A('  year    = {2026}')
A('}')
A('```')
A('')
A('## Contributing')
A('')
A('Pull requests are welcome. Please add a work by editing the data modules rather than')
A('this file: `code_data.py` for repository status, `datasets_data.py` for datasets and')
A('`metrics_data.py` for reported metrics, then run `python3 make_repo_readme.py`.')
A('This file is generated, so a direct edit to it will be overwritten.')
A('')

open('/tmp/AWESOME.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('generated the head: %d lines, %d applications, %d works'
      % (len(L), len(groups), len(ROWS)))
