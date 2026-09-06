# -*- coding: utf-8 -*-
"""Datasets each reviewed work trains or evaluates on, read from its arXiv full text.

Read on 2026-09-04. Keys are arXiv ids and match metrics_data.METRICS exactly, so the
two columns can be intersected: the question this column exists to answer is not "what
data does the field use" but "where could two of these works actually be compared", and
that needs a shared dataset AND a shared metric.

Names are recorded as the paper writes them. Four boundaries were fixed before counting,
each of which inflates comparability if got wrong:

  "private" is not a dataset. An unnamed in-house cohort is recorded so the row is not
  silently empty, but two works that both say "private" share nothing. PRIVATE is
  excluded from every overlap count.

  Versioned releases are one family. BraTS2023 and BraTS 2021, OASIS and OASIS-3,
  SynthRAD2023 and SynthRAD2025, ISIC 2019/2020/2024 are merged by FAMILY. Two works on
  different years of the same benchmark are not directly comparable either, so the
  merged count is an UPPER bound on comparability and is reported as such.

  Umbrella names are not resolvable. One work names only "TCGA" and one only "Kaggle";
  neither identifies a cohort another work could match. They are in AMBIGUOUS and
  excluded. Merging "TCGA" into TCGA-BRCA would have manufactured an overlap.

  Natural-image data is not medical data. MNIST, CelebA, CelebA-HQ, AFHQ-Cat and COCO
  appear as auxiliary benchmarks in three works. They are in NONMEDICAL and excluded;
  counting them would let two medical works "share" CelebA.

  Not merged, deliberately: one work names its low-dose CT data "Mayo" and another
  "AAPM", which are plausibly the same AAPM Mayo grand-challenge release. Deciding that
  from the text is a guess, so they stay distinct. Every such call pushes the shared
  count DOWN, which is the safe direction: the finding is that comparability is rare,
  and a conservative count cannot manufacture it.
"""

DATASETS = {
    "2006.02683": ["LIDC-IDRI", "DRIVE", "STARE", "CHASE"],
    "2006.06270": ["LIDC-IDRI", "LoDoPaB-CT"],
    "2108.02155": ["LIDC-IDRI", "Kvasir-SEG"],
    "2112.13110": ["fastMRI", "PICMUS", "CUBDL"],
    "2301.11551": ["ABIDE"],
    "2305.10732": ["OASIS"],
    "2306.10689": ["private"],
    "2309.04856": ["MNIST", "CelebA-HQ", "fastMRI"],
    "2402.08159": ["Mayo", "Stanford"],
    "2405.18087": ["MoNuSeg", "GlaS"],
    "2407.05059": ["private", "BraTS2023"],
    "2410.17543": ["RRM", "LIDC-IDRI"],
    "2410.19288": ["private"],
    "2410.20073": ["private"],
    "2411.14269": ["private"],
    "2502.12742": ["ADNI"],
    "2502.19037": ["Kvasir-SEG", "ClinicDB", "ColonDB", "Endoscene", "ETIS"],
    "2503.00266": ["CAMUS", "MSD"],
    "2504.01004": ["NSD", "NOD"],
    "2505.04963": ["ATLAS-8k", "BTCV", "AMOS", "CirrMRI600+"],
    "2505.22511": ["private", "AutoPET"],
    "2505.24687": ["Hecktor-2021", "AutoPET"],
    "2507.11025": ["private"],
    "2507.18838": ["private"],
    "2507.19098": ["PneumoniaMNIST", "BloodMNIST", "DermaMNIST", "RetinaMNIST"],
    "2508.11211": ["SMIR", "CQ500"],
    "2508.12900": ["CT-RATE"],
    "2509.05754": ["WHS++", "UK Biobank"],
    "2510.04823": ["SynthRAD2025"],
    "2510.12408": ["HCP"],
    "2510.22070": ["PPMI", "IXI", "SALD", "ADNI"],
    "2511.20152": ["CelebA", "AFHQ-Cat", "COCO", "X-ray Hand"],
    "2512.09185": ["ADNI", "OASIS-3", "AIBL"],
    "2512.16577": ["ACDC", "ISLES", "LUMIERE"],
    "2601.15884": ["Contrast-X", "TCGA-KIRC", "TCGA-STAD", "CPTAC-PDA", "C4KC-KiTS",
                   "CPTAC-CCRCC", "TCGA-UCEC", "CPTAC-LSCC", "CPTAC-LUAD", "TCGA-KIRP",
                   "TCGA-KICH", "CMB-LCA", "HCC-TACE-Seg", "TCGA-LIHC", "CMB-CRC",
                   "TCGA-COAD", "TCGA-OV", "TCGA-BLCA", "Lung-PET-CT-Dx",
                   "Adrenal-ACC-Ki67-Seg", "TCGA-BRCA", "UCSF", "I-SPY 1"],
    "2601.19498": ["ADNI", "UK Biobank", "private"],
    "2602.21536": ["ABCD", "SRPBS-TS", "HDD"],
    "2603.00205": ["AAPM", "Decathlon"],
    "2603.00535": ["SynthRAD2023"],
    "2603.03710": ["HCP", "BraTS"],
    "2603.05796": ["private"],
    "2603.13967": ["CAMUS"],
    "2603.16392": ["MedNode", "HIBA", "Derm12345", "ISIC 2019", "ISIC 2020", "Milk10k",
                   "PAD20", "Kaggle", "DDI", "ISIC 2024"],
    "2603.18513": ["TCGA"],
    "2603.22421": ["private"],
    "2604.02868": ["Kvasir", "ETIS", "CVC-ColonDB", "CVC-ClinicDB", "REFUGE2"],
    "2604.15459": ["GBA-LDCT", "IXI"],
    "2604.21146": ["BraTS"],
    "2605.16469": ["MIMIC-LT", "NIH-LT", "CT-RATE"],
    "2605.26423": ["HCP", "Biopoint"],
    "2606.07036": ["TCGA-BRCA", "TCGA-COADREAD", "SPIDER-breast"],
    "2606.08670": ["OpenBHB", "ADNI", "OASIS-3"],
    "2606.11833": ["HCP", "IBC", "Nakai", "UK Biobank"],
    "2606.18876": ["RETOUCH", "private"],
    "2606.24313": ["BraTS 2021", "private"],
    "2606.24433": ["SkullFix", "SkullBreak", "Mandibular Defect"],
    "2606.28537": ["CSAW", "VinDr", "RSNA"],
    "2607.11104": ["BrainWeb", "private", "UDPET"],
    "2607.16649": ["HCP", "MIND", "IDEAS", "fastMRI", "CC359"],
}

PRIVATE = {"private"}
AMBIGUOUS = {"TCGA", "Kaggle"}
NONMEDICAL = {"MNIST", "CelebA", "CelebA-HQ", "AFHQ-Cat", "COCO"}

FAMILY = {
    "BraTS2023": "BraTS", "BraTS 2021": "BraTS",
    "OASIS-3": "OASIS",
    "SynthRAD2023": "SynthRAD", "SynthRAD2025": "SynthRAD",
    "Kvasir-SEG": "Kvasir",
    "ClinicDB": "CVC-ClinicDB", "ColonDB": "CVC-ColonDB",
    "ISIC 2019": "ISIC", "ISIC 2020": "ISIC", "ISIC 2024": "ISIC",
    "Decathlon": "MSD",
}

def usable(k):
    """The dataset families of work k that another work could actually match."""
    out = set()
    for d in DATASETS[k]:
        if d in PRIVATE or d in AMBIGUOUS or d in NONMEDICAL:
            continue
        out.add(FAMILY.get(d, d))
    return out
