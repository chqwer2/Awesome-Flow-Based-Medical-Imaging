import sys, os, io, contextlib, re, glob, collections
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
# The mark for a repository carries both a GitHub logo, which a reader recognises
# without reading, and the word 'code' inside the badge, so the icon is never the
# only thing saying what it means. Its alt text is 'code' too: that is what shows
# if the badge image is blocked, which is the difference between an entry that
# still says it has code and one that says nothing at all.
CODEBADGE = ('https://img.shields.io/badge/code-181717?'
             'style=flat-square&logo=github&logoColor=white')
GONEBADGE = ('https://img.shields.io/badge/code-removed-9e9e9e?'
             'style=flat-square&logo=github&logoColor=white')
A('**Venue** is a link where the bibliography carries a preprint, and plain text '
  'where it does not -- nothing to link to, rather than a link withheld.')
A('')
A('**Code** &nbsp; [![code](' + CODEBADGE + ')](#implementations) a repository is '
  'printed, and the badge links to it &nbsp;&middot;&nbsp; '
  '`code promised` promised without a link &nbsp;&middot;&nbsp; '
  '`no code` neither &nbsp;&middot;&nbsp; '
  '`no preprint` the full text could not be reached, so neither presence nor '
  'absence of code is claimed &nbsp;&middot;&nbsp; '
  '[![code removed](' + GONEBADGE + ')](#contents) the paper prints a path that '
  'no longer resolves')
A('')

# fam() returns ASCII names because it is shared with the manuscript checkers, where a
# bare umlaut in a .tex source would be a defect. This file is UTF-8 markdown read in a
# browser, and the titles beside it already print Schrodinger correctly, so the family
# label was the one place the name appeared without its diaeresis.
FAMNAME = {'Schrodinger bridge': 'Schr\u00f6dinger bridge'}


def famshow(t):
    n = fam(t)
    return FAMNAME.get(n, n)


# The corpus cells are written for LaTeX, and three constructs were reaching the page
# as source: $\rightarrow$ between the endpoints of a translation, \& in H\&E, and the
# non-breaking ~. A browser prints those literally, so "MRI $\rightarrow$ CT" appeared
# in a column whose whole job is to be read at a glance.
DELATEX = [
    (r'\$\\rightarrow\$', '\u2192'),
    (r'\$\\to\$', '\u2192'),
    (r'\\&', '&'),
    (r'\\%', '%'),
    (r'\\,', ' '),
    (r'~', ' '),
    (r'\{|\}', ''),
]


def cell(t):
    """A table cell: LaTeX turned into what a browser shows, then the pipe escaped.

    A pipe inside a cell ends the column, so it is escaped last -- after the
    substitutions, in case one of them ever introduces its own.
    """
    t = str(t)
    for pat, rep in DELATEX:
        t = re.sub(pat, rep, t)
    return re.sub(r'\s{2,}', ' ', t).strip().replace('|', r'\|')


def venue_link(r, v):
    # The venue carries the link rather than a column of its own. Where the bibliography
    # holds an arXiv identifier the venue name becomes the link; 30 of the 89 works have
    # none, and those keep the venue as plain text -- nothing to link to, not a link
    # withheld. A reader can tell the two apart at a glance, which is the point.
    name = cell(venue(v) or 'arXiv')
    i = arx.get(r['key'], '')
    return '[%s](https://arxiv.org/abs/%s)' % (name, i) if i else name


def badge(r):
    # Three near-identical emoji did not scan; a visible word does, and the badge
    # keeps one inside it. The other three states carry no link, so they stay plain
    # text: a badge that goes nowhere reads as a broken one.
    i = arx.get(r['key'], '')
    if CD.CODE.get(i):
        # A path the paper prints that no longer answers. It stays a link, because a
        # reader may want to see for themselves and because the paper did provide it,
        # but the badge says so first: an Awesome list whose badges 404 silently is
        # worse than one that admits which ones have gone.
        if i in getattr(CD, 'GONE', {}):
            return '[![code removed](' + GONEBADGE + ')](' + CD.CODE[i] + ')'
        return '[![code](' + CODEBADGE + ')](' + CD.CODE[i] + ')'
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
    # One table per application rather than a bullet per work. A reader of this list is
    # usually filtering -- by task, by formulation, by whether there is anything to run --
    # and a column is the thing you can run an eye down. The task group is our own
    # category from the survey, so the list and the paper cut the corpus the same way.
    # The title is the thing a reader scans for, so it gets its own column at full size
    # rather than a <sub> under the method name, where it was set smaller than everything
    # around it. The link rides on the venue -- one column doing both jobs, since "where
    # it was published" and "where to read it" are the same question.
    A('| Method | Title | Task | Family | Modality | Venue | Year | Code |')
    A('|:--|:--|:--|:--|:--|:--|:--:|:--:|')
    for g in sorted(groups[app]):
        rs = sorted(groups[app][g], key=lambda r: (-(year(r['key']) or 0), r['name'].lower()))
        for r in rs:
            t, v = meta.get(r['key'], ('', ''))
            A('| %s | %s | %s | %s | %s | %s | %s | %s |'
              % ('**%s**' % cell(r['name']), cell(tidy(t)) if t else '--',
                 cell(g), cell(famshow(r['family'])), cell(r.get('modality', '') or '--'),
                 venue_link(r, v), year(r['key']) or '--', badge(r)))
    A('')

# ---- implementations ----
A('## Implementations')
A('')
repo_rows = [r for r in ROWS if CD.CODE.get(arx.get(r['key'], ''))]
A('The %d works that publish a repository, grouped by the transport they learn.'
  % len(repo_rows))
A('')
A('> **Note** &mdash; checked September 2026: 33 of the 34 resolve. `OptPriorFM`')
A('> (Subclass priors) is the path its paper prints, but the repository is no longer')
A('> public. It is listed because this table records what each paper provides.')
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
# most_common breaks a tie by insertion order, and this counter is filled from a set,
# whose order changes between runs because Python randomises string hashing per process.
# Two runs over identical data therefore produced files that differed by two swapped
# rows -- enough to make every diff noisy and to leave "is the README current?" with no
# answer. Ties now break by name, so the same data always gives the same file.
for m, n in sorted(met.items(), key=lambda kv: (-kv[1], kv[0].lower()))[:15]:
    bar = '#' * max(1, round(20.0 * n / max(met.values())))
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

# Written where it is read. This wrote to /tmp and the file was carried across to
# repository/README.md by hand, which is a second step nobody remembers on the second
# occasion: the README sat a revision behind its own generator until the difference was
# noticed. The path is taken from this file's own location, not the working directory,
# so it lands in the right place whether the script is run from here or from the root.
_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
open(_out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('wrote %s: %d lines, %d applications, %d works'
      % (os.path.relpath(_out), len(L), len(groups), len(ROWS)))
