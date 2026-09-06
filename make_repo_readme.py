import sys, io, contextlib, collections
sys.path.insert(0, '.')
src = open('check_manuscript.py', encoding='utf-8').read()
cut = src.index("check('prose: the task-measure share barely moved between the cohorts'")
ns = {'__file__': 'check_manuscript.py'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], 'cm', 'exec'), ns)
ROWS, arx, MW, CD, DD = ns['ROWS'], ns['_arx'], ns['_MW'], ns['_CD'], ns['_DD']
fam, year = ns['fam'], ns['year']

L = []
A = L.append
A('# Flow-Based Generative Models for Medical Imaging')
A('')
A('Implementations and datasets accompanying the survey. Every table below is')
A('generated from the same source files the paper builds its own tables from, so')
A('this repository and the manuscript cannot disagree.')
A('')
A('- `code_data.py` -- repository status per reviewed work')
A('- `datasets_data.py` -- public datasets per reviewed work')
A('- `metrics_data.py` -- reported metrics per reviewed work')
A('')
A('Regenerate this file with `python3 make_repo_readme.py`.')
A('')

repo_rows = [r for r in ROWS if CD.CODE.get(arx.get(r['key'], ''))]
A('## Implementations (%d works that print a repository)' % len(repo_rows))
A('')
A('These are the works whose paper prints a link. Works that promise code without a')
A('link, and works whose full text could not be reached, are excluded; the survey')
A('counts those separately.')
A('')
A('| Method | Year | Family | Repository |')
A('|---|---|---|---|')
for r in sorted(repo_rows, key=lambda x: (fam(x['family']), x['name'].lower())):
    url = CD.CODE[arx[r['key']]]
    A('| %s | %s | %s | %s |'
      % (r['name'], year(r['key']) or '--', fam(r['family']), url))
A('')

fams = collections.Counter()
who = collections.defaultdict(list)
for k in DD.DATASETS:
    for f in DD.usable(k):
        fams[f] += 1
        who[f].append(k)
shared = sorted([f for f in fams if fams[f] >= 2], key=lambda f: (-fams[f], f.lower()))
MWm = ns['_MW']
A('## Public datasets used by more than one reviewed work (%d families)' % len(shared))
A('')
A('A shared dataset is not yet a comparison: the works on it must also report a')
A('measure in common. The last column is that intersection.')
A('')
A('| Dataset family | Works | Metrics reported by two or more of them |')
A('|---|---|---|')
for f in shared:
    ms = [set(MWm.get(k, [])) for k in who[f]]
    common = set()
    for i in range(len(ms)):
        for j in range(i + 1, len(ms)):
            common |= ms[i] & ms[j]
    A('| %s | %d | %s |' % (f, fams[f], ', '.join(sorted(common, key=str.lower)) or '--'))
A('')
A('Version families are merged, so BraTS 2021 and BraTS 2023 count as the same')
A('footing. That inflates the count; reading releases strictly gives fewer pairs.')
A('')
open('/tmp/REPO_README.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('README generated: %d lines' % len(L))
print('   implementations : %d' % len(repo_rows))
print('   dataset families: %d' % len(shared))
