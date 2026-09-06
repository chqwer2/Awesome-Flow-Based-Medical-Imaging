# Flow-Based Generative Models for Medical Imaging

Implementations and datasets accompanying the survey. Every table below is
generated from the same source files the paper builds its own tables from, so
this repository and the manuscript cannot disagree.

- `code_data.py` -- repository status per reviewed work
- `datasets_data.py` -- public datasets per reviewed work
- `metrics_data.py` -- reported metrics per reviewed work

Regenerate this file with `python3 make_repo_readme.py`.

## Implementations (34 works that print a repository)

These are the works whose paper prints a link. Works that promise code without a
link, and works whose full text could not be reached, are excluded; the survey
counts those separately.

| Method | Year | Family | Repository |
|---|---|---|---|
| Cor2Vox | 2025 | Brownian bridge | https://github.com/ai-med/Cor2Vox |
| Prob-BBDM | 2026 | Brownian bridge | https://gitlab.xlim.fr/mvalls/Prob-BBDM |
| Slice-consistent BBDM | 2024 | Brownian bridge | https://github.com/MICV-yonsei/CT2MRI |
| Cortex-grounded generation | 2026 | Diffusion or hybrid | https://github.com/ai-med/Cor2Vox |
| Contrast-X | 2026 | Flow matching | https://github.com/YifanChen02/Contrast-X |
| CRONOS | 2025 | Flow matching | https://github.com/MIC-DKFZ/Longitudinal4DMed |
| EchoLVFM | 2026 | Flow matching | https://github.com/EngEmmanuel/EchoLVFM |
| Flow SSN | 2025 | Flow matching | https://github.com/biomedia-mira/flow-ssn |
| FlowPET | 2026 | Flow matching | https://github.com/xiaochaorouz/FlowPET |
| FlowSDF | 2025 | Flow matching | https://github.com/leabogensperger/FlowSDF |
| In-context priors | 2026 | Flow matching | https://github.com/SamGijsen/pinc-flows |
| MammoFlow | 2026 | Flow matching | https://github.com/XYPB/MammoFlow |
| MedSymmFlow | 2025 | Flow matching | https://github.com/caetas/MedSymmFlow |
| MOTFM | 2025 | Flow matching | https://github.com/milad1378yz/MOTFM |
| OsteoFlow | 2026 | Flow matching | https://github.com/hamidreza-aftabi/OsteoFlow |
| Patient-specific dynamics | 2025 | Flow matching | https://github.com/chqwer2/Delta-LDM-Longitudinal |
| RelativeFlow | 2026 | Flow matching | https://github.com/Deliver0/RelativeFlow |
| Restora-Flow | 2026 | Flow matching | https://github.com/imigraz/Restora-Flow |
| Subclass priors | 2026 | Flow matching | https://github.com/Felix-012/OptPriorFM |
| Trajectory-aligned adaptation | 2026 | Flow matching | https://github.com/Veit21/tta-flow |
| WaveDiT | 2026 | Flow matching | https://github.com/sisinflab/WaveDiT |
| WFM | 2026 | Flow matching | https://github.com/yalcintur/WFM |
| BlindHarmony | 2023 | Normalizing flow | https://github.com/SNU-LIST/BlindHarmony |
| Conditional NF | 2020 | Normalizing flow | https://github.com/VLL-HD/FrEIA |
| Harmonizing Flows | 2023 | Normalizing flow | https://github.com/farzad-bz/Harmonizing-Flows |
| IHF-Harmony | 2026 | Normalizing flow | https://github.com/Idea89560041/IHF-Harmony |
| CardiacFlow | 2025 | Rectified flow | https://github.com/m-qiang/CardiacFlow |
| DermaFlux | 2026 | Rectified flow | https://dermaflux.github.io |
| DRIFT | 2026 | Rectified flow | https://yoonseokchoi-ai.github.io/drift-eccv2026/ |
| MPFlow | 2026 | Rectified flow | https://github.com/edshkim98/MPFlow |
| RAFM | 2026 | Rectified flow | https://github.com/HiLab-git/RAFM.git |
| Sparse-view reconstruction | 2026 | Rectified flow | https://github.com/EFMCT/EFMCT |
| ViCTr | 2025 | Rectified flow | https://github.com/Onkarsus13/ViCTr-2D |
| Guided reconstruction | 2024 | Schrodinger bridge | https://github.com/zhyjSIAT/I2SB-Inversion |

## Public datasets used by more than one reviewed work (18 families)

A shared dataset is not yet a comparison: the works on it must also report a
measure in common. The last column is that intersection.

| Dataset family | Works | Metrics reported by two or more of them |
|---|---|---|
| ADNI | 5 | ASSD, Dice, FID, MS-SSIM, PSNR, SSIM |
| HCP | 5 | LPIPS, PSNR, SSIM |
| BraTS | 4 | PSNR, SSIM |
| LIDC-IDRI | 4 | Dice, GED, PSNR, SSIM |
| fastMRI | 3 | PSNR, SSIM |
| Kvasir | 3 | Dice, IoU |
| OASIS | 3 | PSNR, SSIM |
| UK Biobank | 3 | Dice |
| AutoPET | 2 | -- |
| CAMUS | 2 | Dice, FID, SSIM |
| CT-RATE | 2 | FID |
| CVC-ClinicDB | 2 | Dice, IoU |
| CVC-ColonDB | 2 | Dice, IoU |
| ETIS | 2 | Dice, IoU |
| IXI | 2 | -- |
| MSD | 2 | PSNR, SSIM |
| SynthRAD | 2 | MAE, PSNR |
| TCGA-BRCA | 2 | FID, KID, LPIPS |

Version families are merged, so BraTS 2021 and BraTS 2023 count as the same
footing. That inflates the count; reading releases strictly gives fewer pairs.

