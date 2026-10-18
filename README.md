# Awesome Flow-Based Generative Models for Medical Imaging [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Paper](https://img.shields.io/badge/paper-Artificial%20Intelligence%20Review-b31b1b.svg)](#citation)
[![Works](https://img.shields.io/badge/works-217-blue.svg)](#contents)
[![Code](https://img.shields.io/badge/with%20code-103-green.svg)](#implementations)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

A curated list of **flow-based generative models for medical imaging** (flow
matching, rectified flow, diffusion and Schrödinger bridges, and Poisson flows),
accompanying our survey. It covers **217 works**, of which **103 publish code**.

Every list here is generated from the data files in `data/`, which follow the
survey's catalogue (Supplementary Table S3 and Supplementary Data 1--2). Run
`python3 make_repo_readme.py` to regenerate.

## Contents

- [Restoration and Reconstruction](#restoration-and-reconstruction)
- [Translation and Harmonization](#translation-and-harmonization)
- [Generation and Forecasting](#generation-and-forecasting)
- [Analysis and Segmentation](#analysis-and-segmentation)
- [Implementations](#implementations)
- [Datasets](#datasets)
- [What the literature measures](#what-the-literature-measures)
- [Citation](#citation)
- [Contributing](#contributing)

**Venue** links to the DOI, or to arXiv where the work is a preprint.

**Code** &nbsp; [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](#implementations) the official repository; the badge links to it.

## Restoration and Reconstruction

*67 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Image purification** | A Denoising Framework for Real-World Ultra-Low-Dose Lung CT Images Based on an Image Purification Strategy | CT denoising and artifacts | Flow matching | CT | [ICIC 2026](https://doi.org/10.1007/978-981-92-3410-3_7) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MonkeyDadLufy/Image-Purification-Strategy) |
| **Residual endpoint FM** | LDCT-to-SDCT as a Bridge Problem: Single-Step Residual Endpoint Flow Matching for Real-Time Denoising | CT denoising and artifacts | Flow matching | CT | [medRxiv](https://doi.org/10.64898/2026.08.27.26361520) | 2026 |  |
| **SCMA** | SCMA: Structure-Conditioned and Metal-Aware Flow Matching for CT Metal Artifact Reduction | CT denoising and artifacts | Flow matching | CT | [arXiv](https://arxiv.org/abs/2607.28759) | 2026 |  |
| **Structure-aware bridge** | Structure-aware diffusion for low-dose CT imaging | CT denoising and artifacts | Diffusion bridge | CT | [Physics in Medicine & Biology](https://doi.org/10.1088/1361-6560/ad5d47) | 2024 |  |
| **Implicit I2SB** | Implicit Image-to-Image Schrödinger Bridge for image restoration | CT denoising and artifacts | Diffusion bridge | CT | [Pattern Recognition](https://doi.org/10.1016/j.patcog.2025.111627) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wangya22/I3SB) |
| **JCCS-PFGM** | JCCS-PFGM: A Novel Circle-Supervision Based Poisson Flow Generative Model for Multiphase CECT Progressive Low-Dose Reconstruction with Joint Condition | CT denoising and artifacts | Poisson flow | CT | [MICCAI 2023](https://doi.org/10.1007/978-3-031-43999-5_39) | 2023 |  |
| **PCCT PFGM++** | Noise suppression in photon-counting computed tomography using unsupervised Poisson flow generative models | CT denoising and artifacts | Poisson flow | CT | [Visual Computing for Industry, Biomedicine, and Art](https://doi.org/10.1186/s42492-024-00175-6) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dennishein/pfgmpp_PCCT_denoising) |
| **PPFM** | PPFM: Image Denoising in Photon-Counting CT Using Single-Step Posterior Sampling Poisson Flow Generative Models | CT denoising and artifacts | Poisson flow | CT | [IEEE Trans. Radiation and Plasma Medical Sciences](https://doi.org/10.1109/TRPMS.2024.3410092) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dennishein/cpfgmpp_PCCT_denoising) |
| **Poisson flow joint model** | Poisson Flow Joint Model for Multiphase contrast-enhanced CT | CT denoising and artifacts | Poisson flow | CT | [arXiv](https://arxiv.org/abs/2502.03079) | 2025 |  |
| **PFCM** | PFCM: Poisson flow consistency models for low-dose CT image denoising | CT denoising and artifacts | Poisson flow | CT | [IEEE Trans. Medical Imaging](https://doi.org/10.1109/TMI.2025.3558019) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dennishein/pfcm) |
| **PFCT** | Poisson Flow Consistency Training | CT denoising and artifacts | Poisson flow | CT | [arXiv](https://arxiv.org/abs/2510.21857) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AnthonZh/Poisson-Flow-Consistency-Training) |
| **UniField** | UniField: A Unified Field-Aware MRI Enhancement Framework | MRI enhancement | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2603.09223) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/linyiyang98/UniField) |
| **Low-field enhancement** | Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model | MRI enhancement | Flow matching | MRI | [ISBI 2026](https://doi.org/10.1109/ISBI61048.2026.11516041) | 2026 |  |
| **SANA I2I** | SANA I2I: A Text Free Flow Matching Framework for Paired Image to Image Translation with a Case Study in Fetal MRI Artifact Reduction | MRI enhancement | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2604.00298) | 2026 |  |
| **Learning to Distort** | Learning to Distort: Weakly-Supervised Image Quality Transfer for Prostate DWI Correction | MRI enhancement | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2606.18869) | 2026 |  |
| **DRIFT** | DRIFT: Difficulty-Aware Rectified Flows for Through-Plane MRI Super-Resolution | MRI enhancement | Rectified flow | MRI | [ECCV 2026](https://doi.org/10.1007/978-3-032-37035-8_24) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yoonseokchoi-ai/DRIFT) |
| **3T-to-7T recovery** | Schrödinger Diffusion Driven Signal Recovery in 3T BOLD fMRI Using Unmatched 7T Observations | MRI enhancement | Schrödinger bridge | MRI | [arXiv](https://arxiv.org/abs/2504.01004) | 2025 |  |
| **DMD-augmented UNSB** | DMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement | MRI enhancement | Schrödinger bridge | MRI | [arXiv](https://arxiv.org/abs/2603.03769) | 2026 |  |
| **Ten-step bridge SR** | MRI super-resolution in ten sampling steps using a diffusion bridge model | MRI enhancement | Mean-reverting bridge | MRI | [arXiv](https://arxiv.org/abs/2608.08819) | 2026 |  |
| **Ground-truth-free FM** | Unsupervised Accelerated MRI Reconstruction via Ground-Truth-Free Flow Matching | MRI reconstruction | Flow matching | MRI | [IPMI 2025](https://doi.org/10.1007/978-3-031-96628-6_9) | 2025 |  |
| **UPMRI** | UPMRI: Unsupervised Parallel MRI Reconstruction via Projected Conditional Flow Matching | MRI reconstruction | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2512.17493) | 2025 |  |
| **FLAT** | FLAT: FLow-Aligned Training of Unrolled Networks for MRI Reconstruction | MRI reconstruction | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2512.03020) | 2025 |  |
| **Sampling-policy flow** | Flow-Based Generative Modeling for Optimizing Sampling Policies in Compressed Sensing Applications | MRI reconstruction | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2606.00078) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/RomanPavelkin/flowcs) |
| **MPFlow** | MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction | MRI reconstruction | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2603.03710) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/edshkim98/MPFlow) |
| **Nested bridge** | Self-Consistent Nested Diffusion Bridge for Accelerated MRI Reconstruction | MRI reconstruction | Diffusion bridge | MRI | [arXiv](https://arxiv.org/abs/2412.09998) | 2024 |  |
| **Self-supervised bridge** | A Self-Supervised Diffusion Bridge for MRI Reconstruction | MRI reconstruction | Diffusion bridge | MRI | [ISBI 2025](https://doi.org/10.1109/ISBI60581.2025.10980710) | 2025 |  |
| **ADOBI** | ADOBI: Adaptive Diffusion Bridge for Blind Inverse Problems With Application to MRI Reconstruction | MRI reconstruction | Diffusion bridge | MRI | [IEEE Trans. Computational Imaging](https://doi.org/10.1109/TCI.2026.3678407) | 2026 |  |
| **FDB** | Learning Fourier-Constrained Diffusion Bridges for MRI Reconstruction | MRI reconstruction | Diffusion bridge | MRI | [IEEE Trans. Medical Imaging](https://doi.org/10.1109/TMI.2026.3673956) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/icon-lab/FDB) |
| **Guided reconstruction** | Guided MRI Reconstruction via Schrödinger Bridge | MRI reconstruction | Diffusion bridge | MRI | [IEEE Trans. Medical Imaging](https://doi.org/10.1109/TMI.2026.3725165) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zhyjSIAT/I2SB-Inversion) |
| **LUCID** | LUCID: Learned Undersampling-Adaptive Consistency-Guided Inference with Deterministic Flow Matching for Sparse-View CT Reconstruction | Incomplete-data CT | Flow matching | CT | [arXiv](https://arxiv.org/abs/2606.16212) | 2026 |  |
| **Physics-guided FM** | Physics-Guided Flow Matching for CT Image Reconstruction | Incomplete-data CT | Flow matching | CT | [arXiv](https://arxiv.org/abs/2608.28256) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/devangelista2/physics-guided-flow-matching-ct) |
| **AXON** | Conditional Diffusion for 3D CT Volume Reconstruction from 2D X-rays | Incomplete-data CT | Flow matching | CT / X-ray | [arXiv](https://arxiv.org/abs/2603.26509) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/AXON) |
| **Sparse-view reconstruction** | Efficient Flow Matching for Sparse-View CT Reconstruction | Incomplete-data CT | Flow matching | CT | [MICCAI 2026](https://doi.org/10.1007/978-3-032-38179-8_16) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EFMCT/EFMCT) |
| **Unfolded direct bridge** | Integrating Deep Unfolding with Direct Diffusion Bridges for Computed Tomography Reconstruction | Incomplete-data CT | Diffusion bridge | CT | [arXiv](https://arxiv.org/abs/2409.09477) | 2024 |  |
| **Projection-embedded bridge** | Projection Embedded Diffusion Bridge for CT Reconstruction from Incomplete Data | Incomplete-data CT | Diffusion bridge | CT | [arXiv](https://arxiv.org/abs/2510.22605) | 2025 |  |
| **Field-of-view extension** | Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension | Incomplete-data CT | Diffusion bridge | CT | [IEEE Trans. Radiation and Plasma Medical Sciences](https://doi.org/10.1109/TRPMS.2026.3705435) | 2026 |  |
| **Self-cascade latent SB** | Self-cascade latent Schrödinger bridge for CT field-of-view extension | Incomplete-data CT | Diffusion bridge | CT | [Physics in Medicine & Biology](https://doi.org/10.1088/1361-6560/aea5d0) | 2026 |  |
| **PoCGM** | PoCGM: Poisson-Conditioned Generative Model for Sparse-View CT Reconstruction | Incomplete-data CT | Poisson flow | CT | [arXiv](https://arxiv.org/abs/2511.13967) | 2025 |  |
| **FORCE-Interior** | FORCE-Interior: Measurement-Consistent Adaptation of a Poisson-Flow Generative Prior for Interior CT | Incomplete-data CT | Poisson flow | CT | [arXiv](https://arxiv.org/abs/2607.14320) | 2026 |  |
| **ResPF** | ResPF: Residual Poisson Flow Generative Model for Efficient and Physically Consistent Sparse-View CT Reconstruction | Incomplete-data CT | Poisson flow | CT | [IEEE Trans. Radiation and Plasma Medical Sciences](https://doi.org/10.1109/TRPMS.2025.3615836) | 2026 |  |
| **FORCE** | Tomographic Foundation Model—FORCE: Flow-Oriented Reconstruction Conditioning Engine | Incomplete-data CT | Poisson flow | CT | [IEEE Trans. Medical Imaging](https://doi.org/10.1109/TMI.2026.3669463) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiawj-hub/FORCE) |
| **Mean-reverting bridge** | Mean-Reverting Diffusion Bridge with Projection Prior for Sparse CT Reconstruction | Incomplete-data CT | Mean-reverting bridge | CT | [CT Theory and Applications](https://doi.org/10.15953/j.ctta.2025.356) | 2026 |  |
| **FM PET reconstruction** | Flow Matching-Based PET Image Reconstruction | Low-count PET | Flow matching | PET | [arXiv](https://arxiv.org/abs/2608.20112) | 2026 |  |
| **Manifold-constrained FM prior** | Manifold-Constrained PET Reconstruction with Learned Flow-Matching Priors | Low-count PET | Flow matching | PET | [arXiv](https://arxiv.org/abs/2608.29158) | 2026 |  |
| **FlowPET** | FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction | Low-count PET | Flow matching | PET | [ICML 2026](https://arxiv.org/abs/2607.11104) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaochaorouz/FlowPET) |
| **Whole-body PET rectified flow** | Efficient 3D Whole-Body PET Image Denoising via Conditional Rectified Flow With Optimized Sampling Strategy | Low-count PET | Rectified flow | PET | [arXiv](https://arxiv.org/abs/2609.16690) | 2026 |  |
| **Fourier diffusion PET SR** | Generative super-resolution PET imaging with Fourier diffusion models | Low-count PET | Mean-reverting bridge | PET | [SPIE Medical Imaging 2025](https://doi.org/10.1117/12.3048849) | 2025 |  |
| **SMLMFlow** | SMLMFlow: Improving Structural Resolution in Single Molecule Localization Microscopy with Flow Matching | Microscopy and OCT | Flow matching | Microscopy | [bioRxiv](https://doi.org/10.64898/2026.06.11.731424) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sebjbauer/SMLMFlow) |
| **HazeMatching** | HazeMatching: Dehazing Light Microscopy Images with Guided Conditional Flow Matching | Microscopy and OCT | Flow matching | Microscopy | [CVPR Findings 2026](https://arxiv.org/abs/2506.22397) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/juglab/HazeMatching) |
| **ResMatching** | ResMatching: Noise-Resilient Computational Super-Resolution via Guided Conditional Flow Matching | Microscopy and OCT | Flow matching | Microscopy | [ISBI 2026](https://doi.org/10.1109/ISBI61048.2026.11515435) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/juglab/resmatching) |
| **CAFlow** | CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution | Microscopy and OCT | Flow matching | Microscopy | [arXiv](https://arxiv.org/abs/2603.18513) | 2026 |  |
| **MicroFM** | MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction | Microscopy and OCT | Flow matching | Microscopy | CVPR 2026 | 2026 |  |
| **Multi-scale BBDM** | Multi-Scale Conditional Generative Modeling for Microscopic Image Restoration | Microscopy and OCT | Diffusion bridge | Microscopy | [ICASSP 2026](https://doi.org/10.1109/ICASSP55912.2026.11464102) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Liyu96sc/MultimodalBBDM) |
| **Vitreous OCT enhancement** | Deep generative models for enhanced vitreous OCT imaging | Microscopy and OCT | Diffusion bridge | Optical | [Scientific Reports](https://doi.org/10.1038/s41598-026-68477-8) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SimoneSarrocco/vitreous_enhancement) |
| **AutolysisBench** | Through the Schrödinger Bridge: Benchmarking Antemortem Image Restoration from Postmortem Autolysis to Enhance Forensic Diagnostics | Microscopy and OCT | Schrödinger bridge | Microscopy | [arXiv](https://arxiv.org/abs/2608.21813) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/fengluo233/AutolysisBench) |
| **Inverse Flow** | Inverse Flow and Consistency Models | Multi-modality restoration | Flow matching | Microscopy | [ICML 2025](https://arxiv.org/abs/2502.11333) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jzhoulab/InverseFlow) |
| **Quantitative FM** | Beyond Fixed Inference: Quantitative Flow Matching for Adaptive Image Denoising | Multi-modality restoration | Flow matching | CT / Microscopy | [arXiv](https://arxiv.org/abs/2604.02392) | 2026 |  |
| **Restora-Flow** | Restora-Flow: Mask-Guided Image Restoration with Flow Matching | Multi-modality restoration | Flow matching | X-ray | [WACV 2026](https://doi.org/10.1109/WACV61042.2026.00480) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/imigraz/Restora-Flow) |
| **RelativeFlow** | RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference | Multi-modality restoration | Flow matching | CT / MRI | [CVPR Findings 2026](https://arxiv.org/abs/2604.15459) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deliver0/RelativeFlow) |
| **ReBridge-Flow** | ReBridge-Flow: Re-Coupling Posterior Bridges in Flow Matching for Image Restoration | Multi-modality restoration | Flow matching | MRI / X-ray / Ultrasound | [arXiv](https://arxiv.org/abs/2609.00811) | 2026 |  |
| **BME²** | BME²: A Plug-and-Play Bridge-Based Module for Misalignment Estimation and Elimination in Multi-scan Image Restoration | Multi-modality restoration | Diffusion bridge | CT / MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-05169-1_7) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ChenWenxuan2021/BME2) |
| **SPDM** | Diffusion Models under Group Transformations | Multi-modality restoration | Variance-preserving path | CT / PET / Microscopy | [AISTATS 2025](https://arxiv.org/abs/2402.19369) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/watml/SPDM) |
| **Angiography frame interpolation** | Video frame interpolation for coronary angiography using latent flow matching | Inpainting and editing | Flow matching | X-ray | [npj Digital Medicine](https://doi.org/10.1038/s41746-026-02923-9) | 2026 |  |
| **RARF** | RARF: Region-Aware Rectified Flows for 3D Brain MRI Inpainting | Inpainting and editing | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2609.03956) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/TomasGuija/rarf) |
| **SliceBridge** | SliceBridge: context-consistent repair of corrupted slice intervals in T1-weighted MRI | Inpainting and editing | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2609.01827) | 2026 |  |
| **Inversion-free de-identification** | Zero-Shot Generative De-identification: Inversion-Free Flow for Privacy-Preserving Skin Image Analysis | Inpainting and editing | Rectified flow | Optical | [arXiv](https://arxiv.org/abs/2602.00821) | 2026 |  |
| **Novel-view freehand US** | Real-Time Novel-View Freehand Ultrasound Imaging via Point-Cloud Rendering and Diffusion-Bridge Completion | Inpainting and editing | Diffusion bridge | Ultrasound | [MIDL 2026](https://proceedings.mlr.press/v315/shi26b.html) | 2026 |  |

## Translation and Harmonization

*60 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Conditional flow matching** | Flow Matching for Conditional MRI-CT and CBCT-CT Image Synthesis | Synthetic CT and dose | Flow matching | CT / MRI | [AIRoV 2026](https://doi.org/10.34749/3061-1466.2026.6) | 2026 |  |
| **CBCT-conditioned synthesis** | CBCT-Based Synthetic CT Generation Using Conditional Flow Matching Model | Synthetic CT and dose | Flow matching | CT | [arXiv](https://arxiv.org/abs/2603.05796) | 2026 |  |
| **RAFM** | RAFM: Retrieval-Augmented Flow Matching for Unpaired CBCT-to-CT Translation | Synthetic CT and dose | Flow matching | CT | [arXiv](https://arxiv.org/abs/2603.00535) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HiLab-git/RAFM) |
| **Distilled CBCT diffusion** | Improving Cone-Beam CT Image Quality with Knowledge Distillation-Enhanced Diffusion Model in Imbalanced Data Settings | Synthetic CT and dose | Diffusion bridge | CT | [MICCAI 2024](https://doi.org/10.1007/978-3-031-72378-0_12) | 2024 |  |
| **MR-to-CT DSB** | Diffusion Schrödinger bridge models for high-quality MR-to-CT synthesis for proton treatment planning | Synthetic CT and dose | Diffusion bridge | CT / MRI | [Medical Physics](https://doi.org/10.1002/mp.17898) | 2025 |  |
| **DoseBridge** | DoseBridge: Denoising Diffusion Bridge Model for Dose Prediction in Lung Intensity-Modulated Proton Therapy | Synthetic CT and dose | Diffusion bridge | CT | [arXiv](https://arxiv.org/abs/2608.10173) | 2026 |  |
| **Anatomy-conserving bridge** | Anatomy-Conserving Unpaired CBCT-to-CT Translation via Schrödinger Bridge | Synthetic CT and dose | Schrödinger bridge | CT | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04965-0_5) | 2025 |  |
| **Human-guided bridge** | Human-Guided Shading Artifact Suppression in CBCT-to-MDCT Translation via Schrödinger Bridge with Conditional Diffusion | Synthetic CT and dose | Schrödinger bridge | CT | [IEEE Trans. Radiation and Plasma Medical Sciences](https://doi.org/10.1109/TRPMS.2026.3663178) | 2026 |  |
| **Self-supervised semantic bridge** | Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge | Synthetic CT and dose | Schrödinger bridge | CT / MRI | [arXiv](https://arxiv.org/abs/2602.16664) | 2026 |  |
| **Controllable FM** | Controllable Flow Matching for 3D Contrast-Enhanced Brain MRI Synthesis from Non-contrast Scans | Missing sequences and contrast | Flow matching | MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-05325-1_12) | 2025 |  |
| **Neural contrast enhancement** | Conditional Generative Models for Contrast-Enhanced Synthesis of T1W and T1 Maps in Brain MRI | Missing sequences and contrast | Flow matching | MRI | [ISBI 2025](https://doi.org/10.1109/ISBI60581.2025.10980893) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MoePien/NeuralContrastEnhancement) |
| **Contrast-X** | Contrast-X: A Multi-Modal Contrast Image Synthesis Benchmark and Universal Modality Flow Matching | Missing sequences and contrast | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2601.15884) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YifanChen02/Contrast-X) |
| **PS-MIT** | Posterior Samplings are Missing Modalities Generators for Medical Image Translation | Missing sequences and contrast | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2607.18763) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jongdory/PS-MIT) |
| **Whole-volume latent FM** | Compositional Cross-Modality Translation via Whole-Volume Multitask Latent Flow Matching | Missing sequences and contrast | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2608.08135) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arco-group/Whole-Volume-Latent-FM) |
| **T1w-to-T2w benchmark** | Benchmarking GANs, Diffusion Models, and Flow Matching for T1w-to-T2w MRI Translation | Missing sequences and contrast | Flow matching | MRI | [ICIAP Workshops 2025](https://doi.org/10.1007/978-3-032-11317-7_36) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AndreaMoschetto/medical-I2I-benchmark) |
| **PMRF virtual contrast** | Synthesizing Accurate and Realistic T1-Weighted Contrast-Enhanced MR Images Using Posterior-Mean Rectified Flow | Missing sequences and contrast | Rectified flow | MRI | [MICCAI SASHIMI Workshop 2025](https://doi.org/10.1007/978-3-032-05573-6_16) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bbasti/pmrf-virtual-contrast) |
| **3D latent T1C synthesis** | An efficient 3D latent diffusion model for T1-contrast enhanced MRI generation | Missing sequences and contrast | Rectified flow | MRI | [Biomedical Physics & Engineering Express](https://doi.org/10.1088/2057-1976/ae3e96) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zacheidex/An-Efficient-3D-Latent-Diffusion-Model-for-T1-contrast-Enhanced-MRI-Generation) |
| **MAMA-FLUX.2** | MAMA-FLUX.2: Image-to-Image Synthesis of Post-Contrast Breast DCE-MRI for the MAMA-SYNTH Challenge | Missing sequences and contrast | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2608.25648) | 2026 |  |
| **Multi-contrast synthesis** | Multi-contrast MR image synthesis with a Brownian diffusion model | Missing sequences and contrast | Diffusion bridge | MRI | [SIU 2024](https://doi.org/10.1109/SIU61531.2024.10601086) | 2024 |  |
| **Slice-consistent BBDN** | Generating Synthetic Contrast-Enhanced Chest CT Images from Non-Contrast Scans Using Slice-Consistent Brownian Bridge Diffusion Network | Missing sequences and contrast | Diffusion bridge | CT | [arXiv](https://arxiv.org/abs/2508.16897) | 2025 |  |
| **High-fidelity Brownian bridge** | Deterministic Medical Image Translation via High-fidelity Brownian Bridges | Missing sequences and contrast | Diffusion bridge | MRI | [arXiv](https://arxiv.org/abs/2503.22531) | 2025 |  |
| **Coarse-to-fine translation** | Coarse-to-Fine Medical Image Translation by Incorporating Deterministic Guidance and Probabilistic Refinement | Missing sequences and contrast | Diffusion bridge | CT / MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04984-1_13) | 2025 |  |
| **TuLaBM** | TuLaBM: Tumor-Biased Latent Bridge Matching for Contrast-Enhanced MRI Synthesis | Missing sequences and contrast | Diffusion bridge | MRI | [arXiv](https://arxiv.org/abs/2603.19386) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Researcher-1042/TuLaBM) |
| **WFM** | WFM: 3D Wavelet Flow Matching for Ultrafast Multi-Modal MRI Synthesis | Missing sequences and contrast | Diffusion bridge | MRI | [MIDL 2026](https://arxiv.org/abs/2604.21146) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yalcintur/WFM) |
| **Prob-BBDM** | Prob-BBDM: A probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation | Missing sequences and contrast | Diffusion bridge | MRI | [Computerized Medical Imaging and Graphics](https://doi.org/10.1016/j.compmedimag.2026.102745) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://gitlab.xlim.fr/mvalls/Prob-BBDM) |
| **HADSB** | Heterogeneity-Adaptive Diffusion Schrödinger Bridge for PET-Guided Whole-Body MRI Translation | Missing sequences and contrast | Diffusion bridge | MRI / PET | [arXiv](https://arxiv.org/abs/2607.07401) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xyw-medical-research/HADSB) |
| **Post-contrast T1/ECV maps** | AI-Driven Generation of Post-Contrast T1 and ECV Maps from Native T1 Map in Cardiac MRI | Missing sequences and contrast | Diffusion bridge | MRI | [Diagnostics](https://doi.org/10.3390/diagnostics16152308) | 2026 |  |
| **Fully guided NSB** | Fully Guided Neural Schrödinger bridge for Brain MR image synthesis | Missing sequences and contrast | Schrödinger bridge | MRI | [arXiv](https://arxiv.org/abs/2501.14171) | 2026 |  |
| **Bi-directional DPM** | Bi-modality medical images synthesis by a bi-directional discrete process matching method | Cross-modality synthesis | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2409.03977) | 2024 |  |
| **FM-fMRI** | FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis | Cross-modality synthesis | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2605.26423) | 2026 |  |
| **Generative translation comparison** | Cross Modality Image Translation In Medical Imaging Using Generative Frameworks | Cross-modality synthesis | Flow matching | CT / MRI / PET | [arXiv](https://arxiv.org/abs/2605.13686) | 2026 |  |
| **CT-to-FDG-PET rectified flow** | Synthetic FDG-PET Generation from Computed Tomography Using Paired-Data and Rectified Flow Synthesis | Cross-modality synthesis | Rectified flow | CT / PET | [Thesis, University of Calgary](https://doi.org/10.11575/PRISM/51933) | 2026 |  |
| **DIReCT++** | Precision Synthesis of Multi-Tracer PET via VLM-Modulated Rectified Flow for Stratifying Mild Cognitive Impairment | Cross-modality synthesis | Rectified flow | MRI / PET | [arXiv](https://arxiv.org/abs/2604.11176) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ladderlab-xjtu/DIReCT-PLUS) |
| **Slice-consistent BBDM** | Slice-consistent 3D volumetric brain CT-to-MRI translation with 2D Brownian bridge diffusion model | Cross-modality synthesis | Diffusion bridge | CT / MRI | [MICCAI 2024](https://doi.org/10.1007/978-3-031-72104-5_63) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MICV-yonsei/CT2MRI) |
| **SelfRDB** | Self-consistent recursive diffusion bridge for medical image translation | Cross-modality synthesis | Diffusion bridge | CT / MRI | [Medical Image Analysis](https://doi.org/10.1016/j.media.2025.103747) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/icon-lab/SelfRDB) |
| **OCT-to-OCTA bridge** | Diffusion model based OCT to OCTA translation | Cross-modality synthesis | Diffusion bridge | Optical | [Frontiers in Medicine](https://doi.org/10.3389/fmed.2025.1655453) | 2025 |  |
| **RLBCD** | RLBCD: Residual-guided Latent Brownian-bridge Co-Diffusion for Anatomical-to-Metabolic Image Synthesis | Cross-modality synthesis | Diffusion bridge | CT / MRI / PET | [IJCAI 2025](https://doi.org/10.24963/ijcai.2025/656) | 2025 |  |
| **3D diffusion bridge** | Diffusion Bridge Models for 3D Medical Image Translation | Cross-modality synthesis | Diffusion bridge | MRI | [EMBC 2025](https://doi.org/10.1109/EMBC58623.2025.11252839) | 2025 |  |
| **Spectral consistent flow** | Spectral Consistent Flow for One-step 3D Medical Image Translation | Cross-modality synthesis | Diffusion bridge | CT / MRI / PET | [arXiv](https://arxiv.org/abs/2607.10627) | 2026 |  |
| **ReBrain** | ReBrain: Brain MRI Reconstruction from Sparse CT Slice via Retrieval-Augmented Diffusion | Cross-modality synthesis | Diffusion bridge | CT / MRI | [WACV 2026](https://doi.org/10.1109/WACV61042.2026.00390) | 2026 |  |
| **3D CT-to-PET LBBDM** | 3D CT-to-PET Translation via Latent Brownian Bridge Diffusion | Cross-modality synthesis | Diffusion bridge | CT / PET | [arXiv](https://arxiv.org/abs/2609.12860) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/arco-group/3D-CT2PET-via-Latent-Brownian-Bridge-Diffusion) |
| **Structure-preserving MeanFlow** | Do Not Break the Vessels: Structure-Preserving Mean Flow for Vascular Image Translation | Cross-modality synthesis | Diffusion bridge | Microscopy / Optical | [arXiv](https://arxiv.org/abs/2606.31095) | 2026 |  |
| **SiM2P** | Diffusion Bridge Networks Simulate Clinical-grade PET from MRI for Dementia Diagnostics | Cross-modality synthesis | Variance-preserving path | MRI / PET | [arXiv](https://arxiv.org/abs/2510.15556) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Yiiitong/SiM2P) |
| **MedShift** | MedShift: Implicit Conditional Transport for X-Ray Domain Adaptation | Domain harmonization | Flow matching | X-ray | [ICCV Workshops 2025](https://doi.org/10.1109/ICCVW69036.2025.00582) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/caetas/MedShift) |
| **Trajectory-aligned adaptation** | Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow | Domain harmonization | Flow matching | Optical | [arXiv](https://arxiv.org/abs/2606.18876) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Veit21/tta-flow) |
| **Cross-field harmonisation** | Conditional Flow Matching for Cross-Field MRI Harmonisation | Domain harmonization | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2609.00960) | 2026 |  |
| **3D blind harmonization** | Efficient and robust 3D blind harmonization for large domain gaps | Domain harmonization | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2505.00133) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SNU-LIST/BlindHarmonyDiff) |
| **R2B-WFC** | R2B-WFC Ultrasound Reconstruction: Wavelet Fourier Convolution-Based Reconstruction from Radio Frequency to Image | Domain harmonization | Schrödinger bridge | Ultrasound | [MICCAI 2025](https://doi.org/10.1007/978-3-032-05325-1_43) | 2025 |  |
| **LMSB** | Optical Coherence Tomography Harmonization with Anatomy-Guided Latent Metric Schrödinger Bridges | Domain harmonization | Schrödinger bridge | Optical | [NeurIPS 2025](https://doi.org/10.52202/085713-0202) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Shuwen-Wei/lmsb) |
| **FKRSBM** | Feynman Kac Reweighted Schrödinger Bridge Matching for Surface-Based Tau PET Harmonization | Domain harmonization | Schrödinger bridge | PET | [arXiv](https://arxiv.org/abs/2606.17420) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jianweizhang17/FKRSBM) |
| **STFlow** | Scalable Generation of Spatial Transcriptomics from Histology Images via Whole-Slide Flow Matching | Tissue-image translation | Flow matching | Microscopy | [ICML 2025](https://arxiv.org/abs/2506.05361) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Graph-and-Geometric-Learning/STFlow) |
| **3D-guided ST flow** | 3D-Guided Scalable Flow Matching for Generating Volumetric Tissue Spatial Transcriptomics from Serial Histology | Tissue-image translation | Flow matching | Microscopy | [arXiv](https://arxiv.org/abs/2511.14613) | 2025 |  |
| **PRISM** | PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation | Tissue-image translation | Flow matching | Microscopy | [arXiv](https://arxiv.org/abs/2608.06240) | 2026 |  |
| **GeneFlow** | GeneFlow: Translation of Single-cell Gene Expression to Histopathological Images via Rectified Flow | Tissue-image translation | Rectified flow | Microscopy | [NeurIPS 2025](https://doi.org/10.52202/085713-1512) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wangmengbo/GeneFlow) |
| **Pixel super-resolved staining** | Pixel super-resolved virtual staining of label-free tissue using diffusion models | Tissue-image translation | Diffusion bridge | Microscopy | [Nature Communications](https://doi.org/10.1038/s41467-025-60387-z) | 2025 |  |
| **CDSB** | CDSB: accelerating connectomics workflow via Content-Decoupled Schrödinger Bridge | Tissue-image translation | Diffusion bridge | Microscopy | [BMC Biology](https://doi.org/10.1186/s12915-026-02715-3) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lvyanan525/CDSB) |
| **Virtual multiplex staining** | Virtual multiplex staining of the pancreatic islets across type 1 diabetes progression using a Schrödinger bridge | Tissue-image translation | Diffusion bridge | Microscopy | [bioRxiv](https://doi.org/10.64898/2026.04.14.718559) | 2026 |  |
| **FTIR virtual staining** | Fourier Transform Infrared microspectroscopy-based super-resolution virtual staining of unlabeled tissues by pixel Diffusion Transformer | Tissue-image translation | Diffusion bridge | Microscopy | [arXiv](https://arxiv.org/abs/2603.08143) | 2026 |  |
| **Cervical cell synthesis** | Two-Stage Cross-Domain Cervical Abnormality Screening with Cytopathological Image Synthesis and Knowledge Distillation | Tissue-image translation | Schrödinger bridge | Microscopy | [arXiv](https://arxiv.org/abs/2606.27678) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ZhanYiHui06/MICCAI2026) |
| **SheafStain** | SheafStain: Sheaf-Theoretic Schrödinger Bridge for Spatially and Biologically Coherent Virtual Staining | Tissue-image translation | Schrödinger bridge | Microscopy | [arXiv](https://arxiv.org/abs/2606.11846) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepnoid-ai/SheafStain) |

## Generation and Forecasting

*53 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **CTFlow** | CTFlow: Video-Inspired Latent Flow Matching for 3D CT Synthesis | Volume and X-ray synthesis | Flow matching | CT | [ICCV Workshops 2025](https://doi.org/10.1109/ICCVW69036.2025.00703) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/WongJiayi/CTFlow) |
| **Surf2CT** | Surf2CT: Cascaded 3D Flow Matching Models for Torso 3D CT Synthesis from Skin Surface | Volume and X-ray synthesis | Flow matching | CT / PET | [arXiv](https://arxiv.org/abs/2505.22511) | 2025 |  |
| **FlowLet** | FlowLet: Conditional 3D brain MRI synthesis using wavelet flow matching | Volume and X-ray synthesis | Flow matching | MRI | [Medical Image Analysis](https://doi.org/10.1016/j.media.2026.104161) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sisinflab/FlowLet) |
| **WaveDiT** | WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis | Volume and X-ray synthesis | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2606.08670) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sisinflab/WaveDiT) |
| **MammoFlow** | MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching | Volume and X-ray synthesis | Flow matching | X-ray | [arXiv](https://arxiv.org/abs/2606.28537) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XYPB/MammoFlow) |
| **VoxStruct3D** | VoxStruct3D: Structure-Leading Flow Matching for Voxel-Space 3D MRI Synthesis | Volume and X-ray synthesis | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2608.04557) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Neesky/VoxStruct3D) |
| **Complex-valued MRI generation** | Generative modeling of complex-valued brain MRI data | Volume and X-ray synthesis | Flow matching | MRI | [Physics in Medicine & Biology](https://doi.org/10.1088/1361-6560/aeb088) | 2026 |  |
| **Head-and-neck CT synthesis** | Diffusion-based head-and-neck CT synthesis under limited data | Volume and X-ray synthesis | Rectified flow | CT / PET | [Thesis, Universitat Politècnica de Catalunya](https://hdl.handle.net/2117/463321) | 2026 |  |
| **RadiT** | Scaling Generative Foundation Models for Chest Radiography with Rectified Flow Transformers | Volume and X-ray synthesis | Rectified flow | X-ray | [arXiv](https://arxiv.org/abs/2606.19460) | 2026 |  |
| **CONFLUX** | CONFLUX: A Latent Diffusion Model for 3D Chest-CT Synthesis with RL Post-Training | Volume and X-ray synthesis | Rectified flow | CT | [arXiv](https://arxiv.org/abs/2607.02998) | 2026 |  |
| **MAISI-v2** | MAISI-v2: Accelerated 3D High-Resolution Medical Image Synthesis with Rectified Flow and Region-specific Contrastive Loss | Volume and X-ray synthesis | Rectified flow | CT | [AAAI 2026](https://doi.org/10.1609/aaai.v40i15.38309) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/NVIDIA-Medtech/NV-Generate-CTMR) |
| **Cortex-grounded generation** | Cortex-grounded diffusion models for brain image generation | Volume and X-ray synthesis | Diffusion bridge | MRI | [Medical Image Analysis](https://doi.org/10.1016/j.media.2026.104339) | 2027 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/Cor2Vox) |
| **MRIComp4Flow** | MRIComp4Flow: Compression of 3D Brain MRI for Training Multi-Modal Generative Models | Volume and X-ray synthesis | Diffusion bridge | MRI | [arXiv](https://arxiv.org/abs/2608.10291) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/lisafis/MRIComp4Flow) |
| **GRASP** | GRASP: Guided Residual Adapters with Sample-wise Partitioning | Synthetic training data | Flow matching | X-ray | [arXiv](https://arxiv.org/abs/2512.01675) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Felix-012/GRASP-LT) |
| **vesselFM** | vesselFM: A Foundation Model for Universal 3D Blood Vessel Segmentation | Synthetic training data | Flow matching | CT / MRI / Microscopy / Optical | [CVPR 2025](https://doi.org/10.1109/CVPR52734.2025.01944) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/bwittmann/vesselFM) |
| **MOTFM** | Flow Matching for Medical Image Synthesis: Bridging the Gap Between Speed and Quality | Synthetic training data | Flow matching | MRI / Ultrasound | [MICCAI 2025](https://doi.org/10.1007/978-3-032-05325-1_21) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/milad1378yz/MOTFM) |
| **SynCMRI** | Balancing Fidelity, Utility, and Privacy in Synthetic Cardiac MRI Generation: A Comparative Study | Synthetic training data | Flow matching | MRI | [CBMS 2026](https://doi.org/10.1109/cbms69103.2026.00088) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vlbthambawita/SynCMRI) |
| **Microscopy FM design space** | Elucidating the Design Space of Flow Matching for Cellular Microscopy | Synthetic training data | Flow matching | Microscopy | [arXiv](https://arxiv.org/abs/2603.26790) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/valence-labs/microscopy-flow-matching) |
| **Craniofacial transport** | Flow Matching for 3D Craniofacial Skeletal Data Generation | Synthetic training data | Flow matching | CT | [MIDL 2026](https://proceedings.mlr.press/v315/melacini26a.html) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Chavelanda/skeletal_fm) |
| **Subclass priors** | Flow Matching with Optimized Subclass Priors for Medical Image Augmentation | Synthetic training data | Flow matching | CT / X-ray | [arXiv](https://arxiv.org/abs/2605.16469) | 2026 |  |
| **DS@GT ARC** | DS@GT ARC at ImageCLEFmed GANs 2026: Geometric Filtering for Privacy-Preserving CT Slice Generation | Synthetic training data | Flow matching | CT | [arXiv](https://arxiv.org/abs/2607.20692) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dsgt-arc/imageclef-med-gans-2026) |
| **Thyroid scintigraphy augmentation** | AI-augmented thyroid scintigraphy for robust classification of disease | Synthetic training data | Flow matching | PET | [Physica Medica](https://doi.org/10.1016/j.ejmp.2026.105854) | 2026 |  |
| **Distribution-aligned synthesis** | Few-Shot Distribution-Aligned Flow Matching for Data Synthesis in Medical Image Segmentation | Synthetic training data | Flow matching | Optical | [arXiv](https://arxiv.org/abs/2604.02868) | 2026 |  |
| **TumorGen** | TumorGen: Boundary-Aware Tumor-Mask Synthesis with Rectified Flow Matching | Synthetic training data | Rectified flow | PET | [arXiv](https://arxiv.org/abs/2505.24687) | 2025 |  |
| **One-shot federated RF** | A New One-Shot Federated Learning Framework for Medical Imaging Classification with Feature-Guided Rectified Flow and Knowledge Distillation | Synthetic training data | Rectified flow | MRI / X-ray / Optical | [ECAI 2025](https://doi.org/10.3233/FAIA250805) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/LMIAPC/one-shot-fl-medical) |
| **ViCTr** | ViCTr: Vital consistency transfer for pathology aware image synthesis | Synthetic training data | Rectified flow | CT / MRI | [ICCV 2025](https://doi.org/10.1109/ICCV51701.2025.02114) | 2025 |  |
| **NodMAISI** | NodMAISI: Nodule-Oriented Medical AI for Synthetic Imaging | Synthetic training data | Rectified flow | CT | [arXiv](https://arxiv.org/abs/2512.18038) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/fitushar/NoMAISI) |
| **DermaFlux** | DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification | Synthetic training data | Rectified flow | Optical | [arXiv](https://arxiv.org/abs/2603.16392) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/dermaflux/dermaflux) |
| **Manifold filtering** | Diffusion model uniform manifold filtering for classification of small datasets with underrepresented classes: application to chromosomal aberration microscopy detection | Synthetic training data | Diffusion bridge | Microscopy | [ICMV 2024](https://doi.org/10.1117/12.3055038) | 2025 |  |
| **STREAM** | STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation | Synthetic training data | Riemannian flow matching | Microscopy | [arXiv](https://arxiv.org/abs/2606.07036) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepnoid-ai/STREAM) |
| **EchoFlow** | EchoFlow: A Foundation Model for Cardiac Ultrasound Image and Video Generation | Cardiac and brain dynamics | Flow matching | Ultrasound | [arXiv](https://arxiv.org/abs/2503.22357) | 2025 |  |
| **In-context priors** | Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics | Cardiac and brain dynamics | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2606.11833) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SamGijsen/pinc-flows) |
| **EchoLVFM** | EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis | Cardiac and brain dynamics | Flow matching | Ultrasound | [arXiv](https://arxiv.org/abs/2603.13967) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EngEmmanuel/EchoLVFM) |
| **DiffeoCFM** | Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry | Cardiac and brain dynamics | Riemannian flow matching | MRI | [NeurIPS 2025](https://doi.org/10.52202/085713-1993) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/antoinecollas/DiffeoCFM) |
| **DSFM** | Functional MRI Time Series Generation via Wavelet-Based Image Transform and Spectral Flow Matching for Brain Disorder Identification | Cardiac and brain dynamics | Variance-preserving path | MRI | [ICLR 2026](https://arxiv.org/abs/2605.30387) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/htew0001/DSFM) |
| **CRONOS** | CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series | Longitudinal forecasting | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2512.16577) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIC-DKFZ/Longitudinal4DMed) |
| **Temporal Flow Matching** | Temporal Flow Matching for Learning Spatio-Temporal Trajectories in 4D Longitudinal Medical Imaging | Longitudinal forecasting | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2508.21580) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIC-DKFZ/Temporal-Flow-Matching) |
| **Virtual follow-up LDCT** | Early Lung Cancer Diagnosis from Virtual Follow-up LDCT Generation via Correlational Autoencoder and Latent Flow Matching | Longitudinal forecasting | Flow matching | CT | [arXiv](https://arxiv.org/abs/2511.18185) | 2025 |  |
| **OsteoFlow** | OsteoFlow: Lyapunov-Guided Flow Distillation for Predicting Bone Remodeling after Mandibular Reconstruction | Longitudinal forecasting | Flow matching | CT | [arXiv](https://arxiv.org/abs/2603.22421) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hamidreza-aftabi/OsteoFlow) |
| **Patient-specific dynamics** | Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation | Longitudinal forecasting | Flow matching | MRI | [ICLR 2026](https://arxiv.org/abs/2512.09185) | 2026 |  |
| **ProgFormer** | ProgFormer: Hierarchical Voxel Diffusion Transformer for Longitudinal Brain MRI Prediction | Longitudinal forecasting | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2607.27537) | 2026 |  |
| **ViT3Flow** | ViT3Flow: A Test-Time Training Transformer MeanFlow for Postoperative Radiograph Synthesis in Scoliosis | Longitudinal forecasting | Flow matching | X-ray | [arXiv](https://arxiv.org/abs/2609.05579) | 2026 |  |
| **PDF** | Physics-Grounded Disentangled Flow Modeling for Brain Disease Progression Trajectory | Longitudinal forecasting | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2606.28630) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jhuldr/PDF) |
| **CryoFlow** | CryoFlow: Prediction of Frozen Region Growth in Kidney Cryoablation Using a 3D Flow-Matching | Longitudinal forecasting | Flow matching | CT | [MICCAI COLAS Workshop 2025](https://doi.org/10.1007/978-3-032-09784-2_7) | 2026 |  |
| **FDRF** | Flexibly Distilled 3D Rectified Flow with Anatomical Constraints for Developmental Infant Brain MRI Prediction | Longitudinal forecasting | Rectified flow | MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-05182-0_23) | 2025 |  |
| **RF-GlioPREDICT** | Rectified flow-based prediction of post-treatment brain MRI from pre-radiotherapy priors for patients with glioma | Longitudinal forecasting | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2603.08385) | 2026 |  |
| **Spherical BBDM** | Spherical Brownian Bridge Diffusion Models for Conditional Cortical Thickness Forecasting | Longitudinal forecasting | Diffusion bridge | MRI | [MICCAI ShapeMI Workshop 2025](https://doi.org/10.1007/978-3-032-06774-6_12) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/SBDM) |
| **Delta-Diffusion** | Delta-Diffusion: Modeling Longitudinal Brain Amyloid-PET Trajectories via Conditional Poisson Diffusion Bridge | Longitudinal forecasting | Diffusion bridge | MRI / PET | [arXiv](https://arxiv.org/abs/2606.22216) | 2026 |  |
| **CortexGen** | CortexGen: A Geometric Generative Framework for Realistic Cortical Surface Generation Using Latent Flow Matching | Anatomy and device shapes | Flow matching | MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04937-7_11) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ladderlab-xjtu/CortexGen) |
| **MedPCFM-TED** | MedPCFM-TED: One-Step Point Cloud Flow Matching for Implant Generation via Teacher-Guided Endpoint Distillation | Anatomy and device shapes | Flow matching | CT | [arXiv](https://arxiv.org/abs/2609.16934) | 2026 |  |
| **SynVA** | SynVA: A Modular Toolkit for Vessel Generation and Aneurysm Editing | Anatomy and device shapes | Flow matching | CT / MRI / X-ray | [arXiv](https://arxiv.org/abs/2605.17620) | 2026 |  |
| **THA-Flow** | THA-Flow Generative Model: Prosthesis Geometry Prediction from Preoperative CT | Anatomy and device shapes | Rectified flow | CT | [arXiv](https://arxiv.org/abs/2608.25845) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/doidio/nonahip) |
| **VDSB-GWSyn** | VDSB-GWSyn: Diffusion Schrödinger Bridge for Controllable and Anatomically Feasible Guidewire Synthesis in Coronary Angiography | Anatomy and device shapes | Diffusion bridge | X-ray | [arXiv](https://arxiv.org/abs/2606.00109) | 2026 |  |

## Analysis and Segmentation

*37 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Flow SSN** | Flow Stochastic Segmentation Networks | Segmentation uncertainty | Flow matching | CT / Optical | [ICCV 2025](https://doi.org/10.1109/ICCV51701.2025.01369) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/biomedia-mira/flow-ssn) |
| **Aleatoric FM segmentation** | Aleatoric Uncertainty Medical Image Segmentation Estimation via Flow Matching | Segmentation uncertainty | Flow matching | CT / MRI | [MICCAI UNSURE Workshop 2025](https://doi.org/10.1007/978-3-032-06593-3_13) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/huynhspm/Data-Uncertainty) |
| **ATFM** | Ambiguity-aware Truncated Flow Matching for Ambiguous Medical Image Segmentation | Segmentation uncertainty | Flow matching | CT / Optical | [AAAI 2026](https://doi.org/10.1609/aaai.v40i8.37532) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PerceptionComputingLab/ATFM) |
| **Closed-form one-step uncertainty** | Uncertainty in a Single Pass: A Closed-Form Identity for One-Step Flow Matching | Segmentation uncertainty | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2605.00941) | 2026 |  |
| **L2L-Flow** | Latent-to-Latent Flow for Volumetric Stochastic Segmentation | Segmentation uncertainty | Flow matching | CT | [arXiv](https://arxiv.org/abs/2609.07460) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/biomedia-mira/L2L-Flow) |
| **Segmentation bridge** | Ambiguous Medical Image Segmentation Using Diffusion Schrödinger Bridge | Segmentation uncertainty | Diffusion bridge | CT | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04965-0_3) | 2025 |  |
| **Distribution-to-distribution FM** | Uncertainty-Aware Distribution-to-Distribution Flow Matching for Scientific Imaging | Segmentation uncertainty | Diffusion bridge | MRI / Microscopy | [arXiv](https://arxiv.org/abs/2603.21717) | 2026 |  |
| **KANResDiff** | KANResDiff: Learning Local Residual Diffusion via Kolmogorov-Arnold Network for Ambiguous Medical Image Segmentation | Segmentation uncertainty | Mean-reverting bridge | CT / Optical | [arXiv](https://arxiv.org/abs/2608.11617) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/PerceptionComputingLab/KANResDiff) |
| **FlowSDF** | FlowSDF: Flow Matching for Medical Image Segmentation Using Distance Transforms | Segmentation masks | Flow matching | Microscopy | [International Journal of Computer Vision](https://doi.org/10.1007/s11263-025-02373-y) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/leabogensperger/FlowSDF) |
| **LatentFM** | LatentFM: A Latent Flow Matching Approach for Generative Medical Image Segmentation | Segmentation masks | Flow matching | Optical | [arXiv](https://arxiv.org/abs/2512.04821) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/snigdhaghosh/LatentFM-Retina) |
| **FMS²** | FMS²: Unified Flow Matching for Segmentation and Synthesis of Thin Structures | Segmentation masks | Flow matching | X-ray / Optical | [arXiv](https://arxiv.org/abs/2603.13659) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/BabakAsadi94/FMS2) |
| **MedFlowSeg** | MedFlowSeg: Flow Matching for Medical Image Segmentation with Frequency-Aware Attention | Segmentation masks | Flow matching | MRI / Ultrasound / Microscopy / Optical | [arXiv](https://arxiv.org/abs/2604.19675) | 2026 |  |
| **SymmAdapt** | SymmAdapt: Symmetrical Flow Matching for Source-Free Domain Adaptation in Medical Image Segmentation | Segmentation masks | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2608.22532) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/tal-grossman/SymmAdapt_public) |
| **CurvSegFlow** | CurvSegFlow: Time-Conditioned Flow Matching for Robust Segmentation of Curvilinear Structures in Noisy Biomedical Images | Segmentation masks | Flow matching | X-ray / Microscopy / Optical | [arXiv](https://arxiv.org/abs/2606.21608) | 2026 |  |
| **3D curvilinear FM** | Flow Matching Meets 3D Curvilinear Structure Segmentation in Medical Imaging | Segmentation masks | Flow matching | CT / MRI | [arXiv](https://arxiv.org/abs/2608.19965) | 2026 |  |
| **MTFlow** | MTFlow: Time-Conditioned Flow Matching for Microtubule Segmentation in Noisy Microscopy Images | Segmentation masks | Flow matching | Microscopy / Optical | [ISBI 2026](https://doi.org/10.1109/ISBI61048.2026.11516025) | 2026 |  |
| **SegDT** | SegDT: A Diffusion Transformer-Based Segmentation Model for Medical Imaging | Segmentation masks | Rectified flow | Optical | [ICIAP 2025](https://doi.org/10.1007/978-3-032-10185-3_5) | 2026 |  |
| **MC-GenRef** | MC-GenRef: Annotation-free mammography microcalcification segmentation with generative posterior refinement | Segmentation masks | Rectified flow | X-ray | [arXiv](https://doi.org/10.48550/arXiv.2604.04470) | 2026 |  |
| **RF-HiT** | RF-HiT: Rectified Flow Hierarchical Transformer for General Medical Image Segmentation | Segmentation masks | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2604.19570) | 2026 |  |
| **Training-free nodule guidance** | Weakly-Supervised Lung Nodule Segmentation via Training-Free Guidance of 3D Rectified Flow | Segmentation masks | Rectified flow | CT | [arXiv](https://arxiv.org/abs/2604.08313) | 2026 |  |
| **Multi-task I2SB** | Cell Instance Segmentation via Multi-Task Image-to-Image Schrödinger Bridge | Segmentation masks | Diffusion bridge | Microscopy | [arXiv](https://arxiv.org/abs/2604.12318) | 2026 |  |
| **Ventricle segmentation** | CT-based brain ventricle segmentation via diffusion Schrödinger Bridge without target domain ground truths | Segmentation masks | Schrödinger bridge | CT / MRI | [MICCAI 2024](https://doi.org/10.1007/978-3-031-72111-3_13) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HealthX-Lab/DiffusionSynCTSeg) |
| **MedSymmFlow** | MedSymmFlow: Bridging Generative Modeling and Classification in Medical Imaging Through Symmetrical Flow Matching | Anomaly and diagnosis | Flow matching | X-ray / Microscopy / Optical | [MICCAI DGM4MICCAI Workshop 2025](https://doi.org/10.1007/978-3-032-05472-2_4) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/caetas/MedSymmFlow) |
| **DeFloMat** | DeFloMat: Detection with Flow Matching for Stable and Efficient Generative Object Localization | Anomaly and diagnosis | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2512.22406) | 2025 |  |
| **Reversed progression** | Vector Quantization for Reversed Disease Progression: Further Investigations | Anomaly and diagnosis | Flow matching | CT | [MIDL 2026](https://proceedings.mlr.press/v315/chen26b.html) | 2026 |  |
| **T2-GEM** | Maximizing T2-Only Prostate Cancer Localization from Expected Diffusion Weighted Imaging | Anomaly and diagnosis | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2604.00985) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/wxyi057/T2-GEM) |
| **Reflect** | Reflect: Rectified Flows for Efficient Brain Anomaly Correction Transport | Anomaly and diagnosis | Rectified flow | MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04965-0_43) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/farzad-bz/REFLECT) |
| **Image-conditioned latent RF** | Image-conditioned latent rectified flow models for 3D medical anomaly localisation | Anomaly and diagnosis | Rectified flow | CT / MRI | [Frontiers in Radiology](https://doi.org/10.3389/fradi.2026.1847193) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/matt-baugh/img-cond-latent-rflow-model-ad) |
| **Pathology Transport** | Pathology Transport: Optimal-Transport Explanations for Clinical Data, and When Their Heatmaps (Fail to) Localize Disease | Anomaly and diagnosis | Rectified flow | X-ray | [arXiv](https://arxiv.org/abs/2608.17370) | 2026 |  |
| **Healthy counterfactual bridge** | Healthy Counterfactual Generation with Denoising Diffusion Bridge Models | Anomaly and diagnosis | Diffusion bridge | MRI | [ISBI 2026](https://doi.org/10.1109/ISBI61048.2026.11515608) | 2026 |  |
| **Auditing Sybil** | Auditing Sybil: Explaining Deep Lung Cancer Risk Prediction Through Generative Interventional Attributions | Anomaly and diagnosis | Diffusion bridge | CT | [ICML 2026](https://arxiv.org/abs/2602.02560) | 2026 |  |
| **CardiacFlow** | CardiacFlow: 3D+t Four-Chamber Cardiac Shape Completion and Generation via Flow Matching | Shape and parameter output | Flow matching | CT / MRI | [MICCAI 2025](https://doi.org/10.1007/978-3-032-04937-7_9) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/m-qiang/CardiacFlow) |
| **UBone3D** | UBone3D: Physics-Rectified Conditional Flow Matching for Anatomical 3D Shape Completion from Ultrasound | Shape and parameter output | Flow matching | CT / Ultrasound | [arXiv](https://arxiv.org/abs/2609.11506) | 2026 |  |
| **FalconBC** | FalconBC: Flow matching for Amortized inference of Latent-CONditioned physiologic Boundary Conditions | Shape and parameter output | Flow matching | General | [arXiv](https://arxiv.org/abs/2603.19331) | 2026 |  |
| **FlowReg** | Flow Matching-enabled Test-Time Refinement for Unsupervised Cardiac MR Registration | Shape and parameter output | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2603.01073) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/mathpluscode/FlowReg) |
| **MedPCFM** | MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching | Shape and parameter output | Flow matching | CT | [arXiv](https://arxiv.org/abs/2606.24433) | 2026 |  |
| **Motion-space Brownian bridge** | Generative Brownian Bridge Diffusion In Motion Space For Enhanced Myocardial Strain Analysis | Shape and parameter output | Diffusion bridge | MRI | [arXiv](https://arxiv.org/abs/2608.01677) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Rishov-MIA/Brownian-Bridge-strain-analysis) |

## Implementations

The 103 works that publish a repository, grouped by the transport they learn.

<details open>
<summary><b>Flow matching</b> (53)</summary>

| Method | Year | Repository |
|---|---|---|
| Aleatoric FM segmentation | 2025 | [github.com/huynhspm/Data-Uncertainty](https://github.com/huynhspm/Data-Uncertainty) |
| ATFM | 2026 | [github.com/PerceptionComputingLab/ATFM](https://github.com/PerceptionComputingLab/ATFM) |
| AXON | 2026 | [github.com/ai-med/AXON](https://github.com/ai-med/AXON) |
| CardiacFlow | 2025 | [github.com/m-qiang/CardiacFlow](https://github.com/m-qiang/CardiacFlow) |
| Contrast-X | 2026 | [github.com/YifanChen02/Contrast-X](https://github.com/YifanChen02/Contrast-X) |
| CortexGen | 2025 | [github.com/ladderlab-xjtu/CortexGen](https://github.com/ladderlab-xjtu/CortexGen) |
| Craniofacial transport | 2026 | [github.com/Chavelanda/skeletal_fm](https://github.com/Chavelanda/skeletal_fm) |
| CRONOS | 2025 | [github.com/MIC-DKFZ/Longitudinal4DMed](https://github.com/MIC-DKFZ/Longitudinal4DMed) |
| CTFlow | 2025 | [github.com/WongJiayi/CTFlow](https://github.com/WongJiayi/CTFlow) |
| DS@GT ARC | 2026 | [github.com/dsgt-arc/imageclef-med-gans-2026](https://github.com/dsgt-arc/imageclef-med-gans-2026) |
| EchoLVFM | 2026 | [github.com/EngEmmanuel/EchoLVFM](https://github.com/EngEmmanuel/EchoLVFM) |
| Flow SSN | 2025 | [github.com/biomedia-mira/flow-ssn](https://github.com/biomedia-mira/flow-ssn) |
| FlowLet | 2026 | [github.com/sisinflab/FlowLet](https://github.com/sisinflab/FlowLet) |
| FlowPET | 2026 | [github.com/xiaochaorouz/FlowPET](https://github.com/xiaochaorouz/FlowPET) |
| FlowReg | 2026 | [github.com/mathpluscode/FlowReg](https://github.com/mathpluscode/FlowReg) |
| FlowSDF | 2025 | [github.com/leabogensperger/FlowSDF](https://github.com/leabogensperger/FlowSDF) |
| FMS² | 2026 | [github.com/BabakAsadi94/FMS2](https://github.com/BabakAsadi94/FMS2) |
| GRASP | 2025 | [github.com/Felix-012/GRASP-LT](https://github.com/Felix-012/GRASP-LT) |
| HazeMatching | 2026 | [github.com/juglab/HazeMatching](https://github.com/juglab/HazeMatching) |
| Image purification | 2026 | [github.com/MonkeyDadLufy/Image-Purification-Strategy](https://github.com/MonkeyDadLufy/Image-Purification-Strategy) |
| In-context priors | 2026 | [github.com/SamGijsen/pinc-flows](https://github.com/SamGijsen/pinc-flows) |
| Inverse Flow | 2025 | [github.com/jzhoulab/InverseFlow](https://github.com/jzhoulab/InverseFlow) |
| L2L-Flow | 2026 | [github.com/biomedia-mira/L2L-Flow](https://github.com/biomedia-mira/L2L-Flow) |
| LatentFM | 2025 | [github.com/snigdhaghosh/LatentFM-Retina](https://github.com/snigdhaghosh/LatentFM-Retina) |
| MammoFlow | 2026 | [github.com/XYPB/MammoFlow](https://github.com/XYPB/MammoFlow) |
| MedShift | 2025 | [github.com/caetas/MedShift](https://github.com/caetas/MedShift) |
| MedSymmFlow | 2025 | [github.com/caetas/MedSymmFlow](https://github.com/caetas/MedSymmFlow) |
| Microscopy FM design space | 2026 | [github.com/valence-labs/microscopy-flow-matching](https://github.com/valence-labs/microscopy-flow-matching) |
| MOTFM | 2025 | [github.com/milad1378yz/MOTFM](https://github.com/milad1378yz/MOTFM) |
| Neural contrast enhancement | 2025 | [github.com/MoePien/NeuralContrastEnhancement](https://github.com/MoePien/NeuralContrastEnhancement) |
| OsteoFlow | 2026 | [github.com/hamidreza-aftabi/OsteoFlow](https://github.com/hamidreza-aftabi/OsteoFlow) |
| PDF | 2026 | [github.com/jhuldr/PDF](https://github.com/jhuldr/PDF) |
| Physics-guided FM | 2026 | [github.com/devangelista2/physics-guided-flow-matching-ct](https://github.com/devangelista2/physics-guided-flow-matching-ct) |
| PS-MIT | 2026 | [github.com/jongdory/PS-MIT](https://github.com/jongdory/PS-MIT) |
| RAFM | 2026 | [github.com/HiLab-git/RAFM](https://github.com/HiLab-git/RAFM) |
| RelativeFlow | 2026 | [github.com/Deliver0/RelativeFlow](https://github.com/Deliver0/RelativeFlow) |
| ResMatching | 2026 | [github.com/juglab/resmatching](https://github.com/juglab/resmatching) |
| Restora-Flow | 2026 | [github.com/imigraz/Restora-Flow](https://github.com/imigraz/Restora-Flow) |
| Sampling-policy flow | 2026 | [github.com/RomanPavelkin/flowcs](https://github.com/RomanPavelkin/flowcs) |
| SMLMFlow | 2026 | [github.com/sebjbauer/SMLMFlow](https://github.com/sebjbauer/SMLMFlow) |
| Sparse-view reconstruction | 2026 | [github.com/EFMCT/EFMCT](https://github.com/EFMCT/EFMCT) |
| STFlow | 2025 | [github.com/Graph-and-Geometric-Learning/STFlow](https://github.com/Graph-and-Geometric-Learning/STFlow) |
| SymmAdapt | 2026 | [github.com/tal-grossman/SymmAdapt_public](https://github.com/tal-grossman/SymmAdapt_public) |
| SynCMRI | 2026 | [github.com/vlbthambawita/SynCMRI](https://github.com/vlbthambawita/SynCMRI) |
| T1w-to-T2w benchmark | 2026 | [github.com/AndreaMoschetto/medical-I2I-benchmark](https://github.com/AndreaMoschetto/medical-I2I-benchmark) |
| T2-GEM | 2026 | [github.com/wxyi057/T2-GEM](https://github.com/wxyi057/T2-GEM) |
| Temporal Flow Matching | 2025 | [github.com/MIC-DKFZ/Temporal-Flow-Matching](https://github.com/MIC-DKFZ/Temporal-Flow-Matching) |
| Trajectory-aligned adaptation | 2026 | [github.com/Veit21/tta-flow](https://github.com/Veit21/tta-flow) |
| UniField | 2026 | [github.com/linyiyang98/UniField](https://github.com/linyiyang98/UniField) |
| vesselFM | 2025 | [github.com/bwittmann/vesselFM](https://github.com/bwittmann/vesselFM) |
| VoxStruct3D | 2026 | [github.com/Neesky/VoxStruct3D](https://github.com/Neesky/VoxStruct3D) |
| WaveDiT | 2026 | [github.com/sisinflab/WaveDiT](https://github.com/sisinflab/WaveDiT) |
| Whole-volume latent FM | 2026 | [github.com/arco-group/Whole-Volume-Latent-FM](https://github.com/arco-group/Whole-Volume-Latent-FM) |

</details>

<details open>
<summary><b>Rectified flow</b> (15)</summary>

| Method | Year | Repository |
|---|---|---|
| 3D blind harmonization | 2025 | [github.com/SNU-LIST/BlindHarmonyDiff](https://github.com/SNU-LIST/BlindHarmonyDiff) |
| 3D latent T1C synthesis | 2026 | [github.com/zacheidex/An-Efficient-3D-Latent-Diffusion-Model-for-T1-contrast-Enhanced-MRI-Generation](https://github.com/zacheidex/An-Efficient-3D-Latent-Diffusion-Model-for-T1-contrast-Enhanced-MRI-Generation) |
| DermaFlux | 2026 | [github.com/dermaflux/dermaflux](https://github.com/dermaflux/dermaflux) |
| DIReCT++ | 2026 | [github.com/ladderlab-xjtu/DIReCT-PLUS](https://github.com/ladderlab-xjtu/DIReCT-PLUS) |
| DRIFT | 2026 | [github.com/yoonseokchoi-ai/DRIFT](https://github.com/yoonseokchoi-ai/DRIFT) |
| GeneFlow | 2025 | [github.com/wangmengbo/GeneFlow](https://github.com/wangmengbo/GeneFlow) |
| Image-conditioned latent RF | 2026 | [github.com/matt-baugh/img-cond-latent-rflow-model-ad](https://github.com/matt-baugh/img-cond-latent-rflow-model-ad) |
| MAISI-v2 | 2026 | [github.com/NVIDIA-Medtech/NV-Generate-CTMR](https://github.com/NVIDIA-Medtech/NV-Generate-CTMR) |
| MPFlow | 2026 | [github.com/edshkim98/MPFlow](https://github.com/edshkim98/MPFlow) |
| NodMAISI | 2025 | [github.com/fitushar/NoMAISI](https://github.com/fitushar/NoMAISI) |
| One-shot federated RF | 2025 | [github.com/LMIAPC/one-shot-fl-medical](https://github.com/LMIAPC/one-shot-fl-medical) |
| PMRF virtual contrast | 2025 | [github.com/bbasti/pmrf-virtual-contrast](https://github.com/bbasti/pmrf-virtual-contrast) |
| RARF | 2026 | [github.com/TomasGuija/rarf](https://github.com/TomasGuija/rarf) |
| Reflect | 2025 | [github.com/farzad-bz/REFLECT](https://github.com/farzad-bz/REFLECT) |
| THA-Flow | 2026 | [github.com/doidio/nonahip](https://github.com/doidio/nonahip) |

</details>

<details open>
<summary><b>Diffusion bridge</b> (18)</summary>

| Method | Year | Repository |
|---|---|---|
| 3D CT-to-PET LBBDM | 2026 | [github.com/arco-group/3D-CT2PET-via-Latent-Brownian-Bridge-Diffusion](https://github.com/arco-group/3D-CT2PET-via-Latent-Brownian-Bridge-Diffusion) |
| BME² | 2025 | [github.com/ChenWenxuan2021/BME2](https://github.com/ChenWenxuan2021/BME2) |
| CDSB | 2026 | [github.com/lvyanan525/CDSB](https://github.com/lvyanan525/CDSB) |
| Cortex-grounded generation | 2027 | [github.com/ai-med/Cor2Vox](https://github.com/ai-med/Cor2Vox) |
| FDB | 2026 | [github.com/icon-lab/FDB](https://github.com/icon-lab/FDB) |
| Guided reconstruction | 2026 | [github.com/zhyjSIAT/I2SB-Inversion](https://github.com/zhyjSIAT/I2SB-Inversion) |
| HADSB | 2026 | [github.com/xyw-medical-research/HADSB](https://github.com/xyw-medical-research/HADSB) |
| Implicit I2SB | 2025 | [github.com/wangya22/I3SB](https://github.com/wangya22/I3SB) |
| Motion-space Brownian bridge | 2026 | [github.com/Rishov-MIA/Brownian-Bridge-strain-analysis](https://github.com/Rishov-MIA/Brownian-Bridge-strain-analysis) |
| MRIComp4Flow | 2026 | [github.com/lisafis/MRIComp4Flow](https://github.com/lisafis/MRIComp4Flow) |
| Multi-scale BBDM | 2026 | [github.com/Liyu96sc/MultimodalBBDM](https://github.com/Liyu96sc/MultimodalBBDM) |
| Prob-BBDM | 2026 | [gitlab.xlim.fr/mvalls/Prob-BBDM](https://gitlab.xlim.fr/mvalls/Prob-BBDM) |
| SelfRDB | 2025 | [github.com/icon-lab/SelfRDB](https://github.com/icon-lab/SelfRDB) |
| Slice-consistent BBDM | 2024 | [github.com/MICV-yonsei/CT2MRI](https://github.com/MICV-yonsei/CT2MRI) |
| Spherical BBDM | 2025 | [github.com/ai-med/SBDM](https://github.com/ai-med/SBDM) |
| TuLaBM | 2026 | [github.com/Researcher-1042/TuLaBM](https://github.com/Researcher-1042/TuLaBM) |
| Vitreous OCT enhancement | 2026 | [github.com/SimoneSarrocco/vitreous_enhancement](https://github.com/SimoneSarrocco/vitreous_enhancement) |
| WFM | 2026 | [github.com/yalcintur/WFM](https://github.com/yalcintur/WFM) |

</details>

<details open>
<summary><b>Schrödinger bridge</b> (6)</summary>

| Method | Year | Repository |
|---|---|---|
| AutolysisBench | 2026 | [github.com/fengluo233/AutolysisBench](https://github.com/fengluo233/AutolysisBench) |
| Cervical cell synthesis | 2026 | [github.com/ZhanYiHui06/MICCAI2026](https://github.com/ZhanYiHui06/MICCAI2026) |
| FKRSBM | 2026 | [github.com/jianweizhang17/FKRSBM](https://github.com/jianweizhang17/FKRSBM) |
| LMSB | 2025 | [github.com/Shuwen-Wei/lmsb](https://github.com/Shuwen-Wei/lmsb) |
| SheafStain | 2026 | [github.com/deepnoid-ai/SheafStain](https://github.com/deepnoid-ai/SheafStain) |
| Ventricle segmentation | 2024 | [github.com/HealthX-Lab/DiffusionSynCTSeg](https://github.com/HealthX-Lab/DiffusionSynCTSeg) |

</details>

<details open>
<summary><b>Poisson flow</b> (5)</summary>

| Method | Year | Repository |
|---|---|---|
| FORCE | 2026 | [github.com/xiawj-hub/FORCE](https://github.com/xiawj-hub/FORCE) |
| PCCT PFGM++ | 2024 | [github.com/dennishein/pfgmpp_PCCT_denoising](https://github.com/dennishein/pfgmpp_PCCT_denoising) |
| PFCM | 2025 | [github.com/dennishein/pfcm](https://github.com/dennishein/pfcm) |
| PFCT | 2025 | [github.com/AnthonZh/Poisson-Flow-Consistency-Training](https://github.com/AnthonZh/Poisson-Flow-Consistency-Training) |
| PPFM | 2024 | [github.com/dennishein/cpfgmpp_PCCT_denoising](https://github.com/dennishein/cpfgmpp_PCCT_denoising) |

</details>

<details open>
<summary><b>Mean-reverting bridge</b> (1)</summary>

| Method | Year | Repository |
|---|---|---|
| KANResDiff | 2026 | [github.com/PerceptionComputingLab/KANResDiff](https://github.com/PerceptionComputingLab/KANResDiff) |

</details>

<details open>
<summary><b>Variance-preserving path</b> (3)</summary>

| Method | Year | Repository |
|---|---|---|
| DSFM | 2026 | [github.com/htew0001/DSFM](https://github.com/htew0001/DSFM) |
| SiM2P | 2025 | [github.com/Yiiitong/SiM2P](https://github.com/Yiiitong/SiM2P) |
| SPDM | 2025 | [github.com/watml/SPDM](https://github.com/watml/SPDM) |

</details>

<details open>
<summary><b>Riemannian flow matching</b> (2)</summary>

| Method | Year | Repository |
|---|---|---|
| DiffeoCFM | 2025 | [github.com/antoinecollas/DiffeoCFM](https://github.com/antoinecollas/DiffeoCFM) |
| STREAM | 2026 | [github.com/deepnoid-ai/STREAM](https://github.com/deepnoid-ai/STREAM) |

</details>

## Datasets

Public releases used by four or more reviewed works. Size is the named release,
not the sample a work used, and counts pool releases of the same dataset.

| Dataset | Anatomy / modality | Size | Access | Works | Restoration | Translation | Generation | Analysis |
|:--|:--|--:|:--|--:|--:|--:|--:|--:|
| [BraTS](https://www.synapse.org/Synapse:syn53708249) | Brain | 2.2k patients | registration | 24 | 2 | 15 | 2 | 5 |
| [AAPM-Mayo LDCT](https://www.cancerimagingarchive.net/collection/ldct-and-projection-data/) | Head–abdomen CT | 299 patients | open | 18 | 18 | 0 | 0 | 0 |
| [ADNI](https://adni.loni.usc.edu/) | Brain | 2.3k patients | reviewed application | 17 | 2 | 5 | 8 | 2 |
| [IXI](https://brain-development.org/ixi-dataset/) | Brain | 600 patients | open | 16 | 7 | 6 | 1 | 2 |
| [OASIS](https://www.oasis-brains.org/) | Brain | 1.4k patients | reviewed application | 12 | 1 | 2 | 7 | 2 |
| [fastMRI](https://fastmri.med.nyu.edu/) | Knee, brain (k-space) | >8.4k exams | registration | 10 | 9 | 0 | 1 | 0 |
| [HCP](https://www.humanconnectome.org/study/hcp-young-adult/document/1200-subjects-data-release) | Brain | 1.2k patients | registration | 8 | 3 | 2 | 1 | 2 |
| [SynthRAD](https://synthrad2025.grand-challenge.org/) | MR/CBCT, CT | 2.4k patients | open | 8 | 0 | 8 | 0 | 0 |
| [LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/) | Chest CT | 1.0k patients | open | 8 | 1 | 0 | 2 | 5 |
| [autoPET](https://www.cancerimagingarchive.net/collection/fdg-pet-ct-lesions/) | Body PET/CT | 900 patients | open | 7 | 1 | 3 | 3 | 0 |
| [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/) | Heart (3D+t) | 150 patients | registration | 6 | 0 | 0 | 3 | 3 |
| [ISIC](https://challenge.isic-archive.com/data/) | Dermoscopy (2D) | 44k images | open | 5 | 0 | 0 | 1 | 4 |
| [UK Biobank](https://www.ukbiobank.ac.uk/) | Multi-organ | 100k patients | reviewed application | 4 | 0 | 1 | 2 | 1 |
| [NLST](https://www.cancerimagingarchive.net/collection/nlst/) | Chest CT | 26k patients | open | 4 | 0 | 0 | 3 | 1 |
| [MSD](https://medicaldecathlon.com/) | CT/MRI, 10 organs | 2.6k scans | open | 4 | 1 | 0 | 3 | 0 |
| [CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) | Chest CT + text | 21k patients | registration | 4 | 0 | 1 | 3 | 0 |

## What the literature measures

Over all 217 works.

| Reported | Works |
|---|---|
| Sampling steps reported | `####################` 158 |
| ODE sampler | `###################` 147 |
| SDE sampler | `######` 50 |
| One network pass | `##` 17 |
| Repeated draws per input | `########` 61 |
| Test on data outside the training source | `#######` 56 |

Most works test only on data from their training source (161 of 217)
and report a single draw per input (155 of 217).

## Citation

```bibtex
@article{xue2026generative,
  title   = {Generative transport models in medical imaging: a unified survey},
  author  = {Xue, Haowen and Chen, Hao and Hu, Hexuan and Li, Chao and Zhang, Tingbo and
             Sch{\"o}nlieb, Carola-Bibiane and Xu, Haoli and Han, Yi and Huang, Qian},
  journal = {Artificial Intelligence Review},
  year    = {2026},
  note    = {under review}
}
```

## Contributing

Pull requests are welcome. Please add a work by adding a row to `data/studies.csv`
(and a release to `data/datasets.csv`), then run `python3 make_repo_readme.py`.
This file is generated, so a direct edit to it will be overwritten.
