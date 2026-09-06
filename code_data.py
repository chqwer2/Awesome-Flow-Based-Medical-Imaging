# -*- coding: utf-8 -*-
"""Code availability for the reviewed corpus, read from arXiv full text.

Read on 2026-09-04 by fetching arxiv.org/html/<id> for every reviewed work that
main.bib gives an arXiv id, and searching the whole text -- not the abstract -- for a
repository URL. That distinction is not cosmetic: checking only the abstract and the
arXiv comment field found 11 repositories, and reading the full text found 19. Five
papers print the URL in an experiments section or a footnote and nowhere else, so an
abstract-only count understates the field by nearly half.

Three states, and the difference between the first two is the point of the column:
  repository     a URL is printed in the paper and can be followed
  promised only  the paper says code will be released and gives no URL
  none found     neither appears anywhere in the text

A work with no arXiv record cannot be reached this way at all. Those are recorded as
'no arXiv record', which is not evidence of anything about their code.
"""

CODE = {
    "2006.06270": "https://github.com/VLL-HD/FrEIA",
    "2411.14269": "https://github.com/zhyjSIAT/I2SB-Inversion",
    "2512.09185": "https://github.com/chqwer2/Delta-LDM-Longitudinal",
    "2512.16577": "https://github.com/MIC-DKFZ/Longitudinal4DMed",
    "2601.15884": "https://github.com/YifanChen02/Contrast-X",
    "2601.19498": "https://github.com/ai-med/Cor2Vox",
    "2602.21536": "https://github.com/Idea89560041/IHF-Harmony",
    "2603.00205": "https://github.com/EFMCT/EFMCT",
    "2603.00535": "https://github.com/HiLab-git/RAFM",
    "2603.03710": "https://github.com/edshkim98/MPFlow",
    "2603.13967": "https://github.com/EngEmmanuel/EchoLVFM",
    "2603.16392": "https://dermaflux.github.io",
    "2603.22421": "https://github.com/hamidreza-aftabi/OsteoFlow",
    "2605.16469": "https://github.com/Felix-012/OptPriorFM",
    "2606.08670": "https://github.com/sisinflab/WaveDiT",
    "2606.11833": "https://github.com/SamGijsen/pinc-flows",
    "2606.18876": "https://github.com/Veit21/tta-flow",
    "2606.28537": "https://github.com/XYPB/MammoFlow",
    "2607.11104": "https://github.com/xiaochaorouz/FlowPET",
    "2407.05059": "https://github.com/MICV-yonsei/CT2MRI",
    "2511.20152": "https://github.com/imigraz/Restora-Flow",
    "2604.15459": "https://github.com/Deliver0/RelativeFlow",
    "2301.11551": "https://github.com/farzad-bz/Harmonizing-Flows",
    "2305.10732": "https://github.com/SNU-LIST/BlindHarmony",
    "2502.12742": "https://github.com/ai-med/Cor2Vox",
    "2503.00266": "https://github.com/milad1378yz/MOTFM",
    "2505.04963": "https://github.com/Onkarsus13/ViCTr-2D",
    "2604.21146": "https://github.com/yalcintur/WFM",
    "2607.16649": "https://yoonseokchoi-ai.github.io/drift-eccv2026/",
    "2405.18087": "https://github.com/leabogensperger/FlowSDF",
    "2507.18838": "https://github.com/biomedia-mira/flow-ssn",
    "2507.19098": "https://github.com/caetas/MedSymmFlow",
    "2509.05754": "https://github.com/m-qiang/CardiacFlow",
    "2606.24313": "https://gitlab.xlim.fr/mvalls/Prob-BBDM",
}
PROMISED = {
    "2605.26423": "The code will be available on GitHub.",
    "2606.07036": "The code will be publicly released upon acceptance.",
    "2410.19288": "The code will be available online.",
}
# checked, and neither a URL nor a statement appears anywhere in the text
NONE_FOUND = {
    "2112.13110", "2306.10689", "2309.04856", "2502.19037", "2504.01004",
    "2505.22511", "2505.24687", "2508.11211", "2510.04823", "2510.12408",
    "2510.22070", "2603.05796", "2603.18513", "2604.02868", "2606.24433",
    "2402.08159", "2410.17543", "2410.20073",
    "2508.12900",
    "2006.02683", "2108.02155",
    "2507.11025",
}
CHECKED = set(CODE) | set(PROMISED) | NONE_FOUND

# ---------------------------------------------------------------------------------
# arXiv ids resolved by title search for works whose main.bib entry cites only the
# proceedings or journal. The probe was validated first against three works whose id
# main.bib already carries -- Cor2Vox, MammoFlow, OsteoFlow -- and found all three, so
# a search returning nothing is a real absence rather than a query that missed.
RESOLVED = {
    "hein2025pfcm":        "2402.08159",
    "hadzic2026restora":   "2511.20152",
    "liu2026relativeflow": "2604.15459",
    "dong2025flow":        "2410.19288",
    "an2025unsupervised":  "2410.17543",
    "kang2026human":       "2507.11025",
    "choo2024slice":       "2407.05059",
    "valls2026prob":       "2606.24313",
    "zhang2025pixel":      "2410.20073",
    "beizaee2023harmonizing": "2301.11551",
    "bongratz20253d": "2502.12742",
    "choi2026drift": "2607.16649",
    "jeong2023blindharmony": "2305.10732",
    "susladkar2025victr": "2505.04963",
    "tur2026wfm": "2604.21146",
    "wang2025ctflow": "2508.12900",
    "yazdani2025flow": "2503.00266",
    "bogensperger2025flowsdf": "2405.18087",
    "caetano2025medsymmflow": "2507.19098",
    "de2025flow": "2507.18838",
    "ma2025cardiacflow": "2509.05754",
    "selvan2020uncertainty": "2006.02683",
    "valiuddin2021improving": "2108.02155",
}
