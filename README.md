# Awesome Flow-Based Generative Models for Medical Imaging [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Paper](https://img.shields.io/badge/paper-Medical%20Image%20Analysis-b31b1b.svg)](#citation)
[![Works](https://img.shields.io/badge/works-89-blue.svg)](#contents)
[![Code](https://img.shields.io/badge/with%20code-34-green.svg)](#implementations)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

A curated list of **flow-based generative models for medical imaging** --- normalizing
flows, flow matching, rectified flow, and Schrödinger and Brownian bridges ---
accompanying our survey. It covers **89 works**, of which **34 publish code**.

Every list here is generated from the same source files the paper builds its tables
from, so the repository and the manuscript cannot drift apart. Run
`python3 make_repo_readme.py` to regenerate.

## Contents

- [Image Processing and Restoration](#image-processing-and-restoration)
- [Cross-Modal Translation and Harmonization](#cross-modal-translation-and-harmonization)
- [Image Generation and Augmentation](#image-generation-and-augmentation)
- [Analysis: Classification, Segmentation, Detection](#analysis-classification-segmentation-detection)
- [Implementations](#implementations)
- [Datasets](#datasets)
- [What the literature measures](#what-the-literature-measures)
- [Citation](#citation)
- [Contributing](#contributing)

**Venue** is a link where the bibliography carries a preprint, and plain text where it does not -- nothing to link to, rather than a link withheld.

**Code** &nbsp; [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](#implementations) a repository is printed, and the badge links to it &nbsp;&middot;&nbsp; `code promised` promised without a link &nbsp;&middot;&nbsp; `no code` neither &nbsp;&middot;&nbsp; `no preprint` the full text could not be reached, so neither presence nor absence of code is claimed &nbsp;&middot;&nbsp; [![code removed](https://img.shields.io/badge/code-removed-9e9e9e?style=flat-square&logo=github&logoColor=white)](#contents) the paper prints a path that no longer resolves

## Image Processing and Restoration

*21 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **FlowPET** | FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction | Reconstruction | Flow matching | PET | [arXiv](https://arxiv.org/abs/2607.11104) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaochaorouz/FlowPET) |
| **MicroFM** | MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction | Reconstruction | Flow matching | Microscopy | CVPR | 2026 | `no preprint` |
| **MPFlow** | MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction | Reconstruction | Rectified flow | MRI | [arXiv](https://arxiv.org/abs/2603.03710) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/edshkim98/MPFlow) |
| **Sparse-view reconstruction** | Efficient Flow Matching for Sparse-View CT Reconstruction | Reconstruction | Rectified flow | CT | [arXiv](https://arxiv.org/abs/2603.00205) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EFMCT/EFMCT) |
| **Field-of-view extension** | Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension | Reconstruction | Schrödinger bridge | CT | [arXiv](https://arxiv.org/abs/2508.11211) | 2025 | `no code` |
| **One-way conditional flow** | Unsupervised low-dose CT reconstruction with one-way conditional normalizing flows | Reconstruction | Normalizing flow | CT | [IEEE Trans. Computational Imaging](https://arxiv.org/abs/2410.17543) | 2025 | `no code` |
| **Guided reconstruction** | Guided MRI Reconstruction via Schrödinger Bridge | Reconstruction | Schrödinger bridge | MRI | [arXiv](https://arxiv.org/abs/2411.14269) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zhyjSIAT/I2SB-Inversion) |
| **AmbientFlow** | AmbientFlow: Invertible generative models from incomplete, noisy measurements | Reconstruction | Normalizing flow | General | [arXiv](https://arxiv.org/abs/2309.04856) | 2023 | `no code` |
| **Conditional NF** | Conditional normalizing flows for low-dose computed tomography image reconstruction | Reconstruction | Normalizing flow | CT | [arXiv](https://arxiv.org/abs/2006.06270) | 2020 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VLL-HD/FrEIA) |
| **RelativeFlow** | RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference | Restoration | Flow matching | General | [CVPR](https://arxiv.org/abs/2604.15459) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deliver0/RelativeFlow) |
| **Restora-Flow** | Restora-Flow: Mask-Guided Image Restoration with Flow Matching | Restoration | Flow matching | General | [Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision](https://arxiv.org/abs/2511.20152) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/imigraz/Restora-Flow) |
| **3T-to-7T recovery** | Schrödinger Diffusion Driven Signal Recovery in 3T BOLD fMRI Using Unmatched 7T Observations | Restoration | Schrödinger bridge | BOLD fMRI | [arXiv](https://arxiv.org/abs/2504.01004) | 2025 | `no code` |
| **Low-field enhancement** | Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model | Restoration | Flow matching | MRI | [arXiv](https://arxiv.org/abs/2510.12408) | 2025 | `no code` |
| **PFCM** | PFCM: Poisson flow consistency models for low-dose CT image denoising | Restoration | Diffusion or hybrid | CT | [IEEE Trans. Medical Imaging](https://arxiv.org/abs/2402.08159) | 2025 | `no code` |
| **AF2R** | Realistic Restorer: artifact-free flow restorer (AF2R) for MRI motion artifact removal | Restoration | Normalizing flow | MRI | [arXiv](https://arxiv.org/abs/2306.10689) | 2023 | `no code` |
| **MRI-derived prior** | Ultrasound speckle suppression and denoising using MRI-derived normalizing flow priors | Restoration | Normalizing flow | Ultrasound | [arXiv](https://arxiv.org/abs/2112.13110) | 2021 | `no code` |
| **CAFlow** | CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution | Super-resolution | Flow matching | Histopathology | [arXiv](https://arxiv.org/abs/2603.18513) | 2026 | `no code` |
| **DRIFT** | DRIFT: Difficulty-aware Rectified Flows for Through-plane MRI Super-Resolution | Super-resolution | Rectified flow | MRI | [ECCV](https://arxiv.org/abs/2607.16649) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://yoonseokchoi-ai.github.io/drift-eccv2026/) |
| **FTDDM** | A flow-based truncated denoising diffusion model for super-resolution magnetic resonance spectroscopic imaging | Super-resolution | Diffusion or hybrid | MR spectroscopic imaging | [Medical Image Analysis](https://arxiv.org/abs/2410.19288) | 2025 | `code promised` |
| **Conditional stochastic NF** | Simultaneous super-resolution and denoising on MRI via conditional stochastic normalizing flow | Super-resolution | Normalizing flow | MRI | IEEE International Conference on Bioinformatics and Biomedicine | 2023 | `no preprint` |
| **MRIFlow** | MRIFlow: Magnetic resonance image super-resolution based on normalizing flow and frequency prior | Super-resolution | Normalizing flow | MRI | Journal of Magnetic Resonance | 2023 | `no preprint` |

## Cross-Modal Translation and Harmonization

*23 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Prob-BBDM** | Prob-BBDM: A probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation | Cross-modal translation: MRI-centred | Brownian bridge | MRI sequences | [Computerized Medical Imaging and Graphics](https://arxiv.org/abs/2606.24313) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://gitlab.xlim.fr/mvalls/Prob-BBDM) |
| **Multi-contrast synthesis** | Multi-contrast MR image synthesis with a Brownian diffusion model | Cross-modal translation: MRI-centred | Brownian bridge | Multi-contrast MRI | Signal Processing and Communications Applications Conference | 2024 | `no preprint` |
| **Slice-consistent BBDM** | Slice-consistent 3D volumetric brain CT-to-MRI translation with 2D Brownian bridge diffusion model | Cross-modal translation: MRI-centred | Brownian bridge | CT → MRI | [MICCAI](https://arxiv.org/abs/2407.05059) | 2024 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MICV-yonsei/CT2MRI) |
| **CBCT-conditioned synthesis** | CBCT-Based Synthetic CT Generation Using Conditional Flow Matching Model | Cross-modal translation: synthetic CT | Flow matching | CBCT → CT | [arXiv](https://arxiv.org/abs/2603.05796) | 2026 | `no code` |
| **Human-guided bridge** | Human-Guided Shading Artifact Suppression in CBCT-to-MDCT Translation via Schrödinger Bridge with Conditional Diffusion | Cross-modal translation: synthetic CT | Schrödinger bridge | CBCT → MDCT | [IEEE Trans. Radiation and Plasma Medical Sciences](https://arxiv.org/abs/2507.11025) | 2026 | `no code` |
| **RAFM** | RAFM: Retrieval-Augmented Flow Matching for Unpaired CBCT-to-CT Translation | Cross-modal translation: synthetic CT | Rectified flow | MRI → CT | [arXiv](https://arxiv.org/abs/2603.00535) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HiLab-git/RAFM) |
| **Anatomy-conserving bridge** | Anatomy-Conserving Unpaired CBCT-to-CT Translation via Schrödinger Bridge | Cross-modal translation: synthetic CT | Schrödinger bridge | CBCT → CT | MICCAI | 2025 | `no preprint` |
| **Conditional flow matching** | Flow Matching for Conditional MRI-CT and CBCT-CT Image Synthesis | Cross-modal translation: synthetic CT | Flow matching | MRI, CBCT → CT | [arXiv](https://arxiv.org/abs/2510.04823) | 2025 | `no code` |
| **Structure-residual bridge** | Structure-Residual Diffusion Bridge Model for MRI-to-CT Image Translation | Cross-modal translation: synthetic CT | Diffusion or hybrid | MRI → CT | International Conference on Virtual Reality and Visualization | 2025 | `no preprint` |
| **IHF-Harmony** | IHF-Harmony: Multi-Modality Magnetic Resonance Images Harmonization using Invertible Hierarchy Flow Model | Domain harmonization | Normalizing flow | Multi-modal MRI | [arXiv](https://arxiv.org/abs/2602.21536) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Idea89560041/IHF-Harmony) |
| **LMSB** | Optical Coherence Tomography Harmonization with Anatomy-Guided Latent Metric Schrödinger Bridges | Domain harmonization | Schrödinger bridge | OCT | NeurIPS | 2026 | `no preprint` |
| **Trajectory-aligned adaptation** | Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow | Domain harmonization | Flow matching | OCT | [arXiv](https://arxiv.org/abs/2606.18876) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Veit21/tta-flow) |
| **BlindHarmony** | BlindHarmony:" blind" harmonization for MR images via flow model | Domain harmonization | Normalizing flow | MRI | [ICCV](https://arxiv.org/abs/2305.10732) | 2023 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SNU-LIST/BlindHarmony) |
| **CTFlow (Wei et al.)** | CTFlow: Mitigating effects of computed tomography acquisition and reconstruction with normalizing flows | Domain harmonization | Normalizing flow | CT | MICCAI | 2023 | `no preprint` |
| **Harmonizing Flows** | Harmonizing Flows: Unsupervised MR harmonization based on normalizing flows | Domain harmonization | Normalizing flow | MRI | [International Conference on Information Processing in Medical Imaging](https://arxiv.org/abs/2301.11551) | 2023 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/farzad-bz/Harmonizing-Flows) |
| **Kernel conversion** | CT Kernel Conversion for Quantitative Assessment in Chronic Obstructive Pulmonary Disease Using an Image-to-Image Schrödinger Bridge Model | Domain harmonization | Schrödinger bridge | CT | arXiv | -- | `no preprint` |
| **FM-fMRI** | FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis | Functional-state translation | Flow matching | fMRI time series | [arXiv](https://arxiv.org/abs/2605.26423) | 2026 | `code promised` |
| **Contrast-X** | Contrast-X: A Multi-Modal Contrast Image Synthesis Benchmark and Universal Modality Flow Matching | Missing-modality translation | Flow matching | CT, multi-phase MRI | [arXiv](https://arxiv.org/abs/2601.15884) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YifanChen02/Contrast-X) |
| **WFM** | WFM: 3D Wavelet Flow Matching for Ultrafast Multi-Modal MRI Synthesis | Missing-modality translation | Flow matching | Multi-modal MRI | [MIDL](https://arxiv.org/abs/2604.21146) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yalcintur/WFM) |
| **Topology-aware DSB** | Topology-aware Diffusion Schrödinger Bridge for Unpaired H&E-to-IHC Stain Translation | Virtual staining | Schrödinger bridge | H&E → IHC | IEEE Journal of Biomedical and Health Informatics | 2026 | `no preprint` |
| **PASB** | PASB: Pathology-Aware Schrödinger Bridge for Virtual Immunohistochemical Staining | Virtual staining | Schrödinger bridge | H&E → IHC | Medical Image Analysis | 2025 | `no preprint` |
| **Pixel super-resolved staining** | Pixel super-resolved virtual staining of label-free tissue using diffusion models | Virtual staining | Diffusion or hybrid | Label-free → stained | [Nature Communications](https://arxiv.org/abs/2410.20073) | 2025 | `no code` |
| **StainSB** | Weakly Supervised Virtual Immunohistochemistry Staining via Schrödinger Bridge Method | Virtual staining | Schrödinger bridge | H&E → IHC | IEEE International Conference on Bioinformatics and Biomedicine | 2024 | `no preprint` |

## Image Generation and Augmentation

*24 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Cortex-grounded generation** | Cortex-Grounded Diffusion Models for Brain Image Generation | Controllable and structure-guided generation | Diffusion or hybrid | Brain MRI | [arXiv](https://arxiv.org/abs/2601.19498) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/Cor2Vox) |
| **EchoLVFM** | EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis | Controllable and structure-guided generation | Flow matching | Echocardiography | [arXiv](https://arxiv.org/abs/2603.13967) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EngEmmanuel/EchoLVFM) |
| **GeneVAR** | GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis | Controllable and structure-guided generation | Flow matching | Histopathology | CVPR | 2026 | `no preprint` |
| **Multimodal bridge** | Multimodal Brownian bridge diffusion model for controllable synthetic medical image generation | Controllable and structure-guided generation | Brownian bridge | General | Biomedical Signal Processing and Control | 2026 | `no preprint` |
| **Cor2Vox** | 3D shape-to-image Brownian bridge diffusion for brain MRI synthesis from cortical surfaces | Controllable and structure-guided generation | Brownian bridge | Brain MRI | [International Conference on Information Processing in Medical Imaging](https://arxiv.org/abs/2502.12742) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/Cor2Vox) |
| **CTFlow (Wang et al.)** | CTFlow: Video-Inspired Latent Flow Matching for 3D CT Synthesis | Controllable and structure-guided generation | Flow matching | CT, 3D | [ICCV](https://arxiv.org/abs/2508.12900) | 2025 | `no code` |
| **Surf2CT** | Surf2CT: Cascaded 3D Flow Matching Models for Torso 3D CT Synthesis from Skin Surface | Controllable and structure-guided generation | Flow matching | Torso CT | [arXiv](https://arxiv.org/abs/2505.22511) | 2025 | `no code` |
| **TumorGen** | TumorGen: Boundary-Aware Tumor-Mask Synthesis with Rectified Flow Matching | Controllable and structure-guided generation | Rectified flow | Tumor masks | [arXiv](https://arxiv.org/abs/2505.24687) | 2025 | `no code` |
| **ViCTr** | ViCTr: Vital consistency transfer for pathology aware image synthesis | Controllable and structure-guided generation | Rectified flow | Pathology-aware synthesis | [ICCV](https://arxiv.org/abs/2505.04963) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Onkarsus13/ViCTr-2D) |
| **DermaFlux** | DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification | Data-augmentation-oriented generation | Rectified flow | Dermoscopy | [arXiv](https://arxiv.org/abs/2603.16392) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://dermaflux.github.io) |
| **Distribution-aligned synthesis** | Few-Shot Distribution-Aligned Flow Matching for Data Synthesis in Medical Image Segmentation | Data-augmentation-oriented generation | Flow matching | Segmentation datasets | [arXiv](https://arxiv.org/abs/2604.02868) | 2026 | `no code` |
| **MammoFlow** | MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching | Data-augmentation-oriented generation | Flow matching | Mammography | [arXiv](https://arxiv.org/abs/2606.28537) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XYPB/MammoFlow) |
| **MoGen** | MoGen: Detailed Neuronal Morphology Generation via Point Cloud Flow Matching | Data-augmentation-oriented generation | Flow matching | Neuronal point clouds | The Fourteenth International Conference on Learning Representations | 2026 | `no preprint` |
| **STREAM** | STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation | Data-augmentation-oriented generation | Flow matching | Histopathology | [arXiv](https://arxiv.org/abs/2606.07036) | 2026 | `code promised` |
| **Subclass priors** | Flow Matching with Optimized Subclass Priors for Medical Image Augmentation | Data-augmentation-oriented generation | Flow matching | General | [arXiv](https://arxiv.org/abs/2605.16469) | 2026 | [![code removed](https://img.shields.io/badge/code-removed-9e9e9e?style=flat-square&logo=github&logoColor=white)](https://github.com/Felix-012/OptPriorFM) |
| **WaveDiT** | WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis | Data-augmentation-oriented generation | Flow matching | Brain MRI, 3D | [arXiv](https://arxiv.org/abs/2606.08670) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sisinflab/WaveDiT) |
| **Landmark-oriented synthesis** | Flow matching-based data synthesis for robust anatomical landmark localization | Data-augmentation-oriented generation | Flow matching | Landmark datasets | IEEE Journal of Biomedical and Health Informatics | 2025 | `no preprint` |
| **MOTFM** | Flow matching for medical image synthesis: Bridging the gap between speed and quality | Data-augmentation-oriented generation | Flow matching | General, 2D and 3D | [MICCAI](https://arxiv.org/abs/2503.00266) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/milad1378yz/MOTFM) |
| **RealNVP synthesis** | Normalizing flow for synthetic medical images generation | Data-augmentation-oriented generation | Normalizing flow | Chest X-ray, skin lesion | IEEE Healthcare Innovations and Point of Care Technologies | 2022 | `no preprint` |
| **In-context priors** | Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | fMRI dynamics | [arXiv](https://arxiv.org/abs/2606.11833) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SamGijsen/pinc-flows) |
| **OsteoFlow** | OsteoFlow: Lyapunov-Guided Flow Distillation for Predicting Bone Remodeling after Mandibular Reconstruction | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | Mandibular CT | [arXiv](https://arxiv.org/abs/2603.22421) | 2026 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hamidreza-aftabi/OsteoFlow) |
| **Reversed progression** | Vector Quantization for Reversed Disease Progression: Further Investigations | Longitudinal, treatment-conditioned, and counterfactual generation | Not a flow | Longitudinal imaging | MIDL | 2026 | `no preprint` |
| **CRONOS** | CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | 4D longitudinal series | [arXiv](https://arxiv.org/abs/2512.16577) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIC-DKFZ/Longitudinal4DMed) |
| **Patient-specific dynamics** | Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | Longitudinal imaging | [arXiv](https://arxiv.org/abs/2512.09185) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chqwer2/Delta-LDM-Longitudinal) |

## Analysis: Classification, Segmentation, Detection

*21 works.*

| Method | Title | Task | Family | Modality | Venue | Year | Code |
|:--|:--|:--|:--|:--|:--|:--:|:--:|
| **Flow-MIL** | Flow-MIL: Constructing Highly-expressive Latent Feature Space For Whole Slide Image Classification Using Normalizing Flow | Classification | Normalizing flow | Histopathology | ICCV | 2025 | `no preprint` |
| **MAGIC-Flow** | MAGIC-Flow: Multiscale Adaptive Conditional Flows for Generation and Interpretable Classification | Classification | Normalizing flow | General | [arXiv](https://arxiv.org/abs/2510.22070) | 2025 | `no code` |
| **MedSymmFlow** | MedSymmFlow: Bridging Generative Modeling and Classification in Medical Imaging Through Symmetrical Flow Matching | Classification | Flow matching | 2D benchmarks | [MICCAI Workshop on Deep Generative Models](https://arxiv.org/abs/2507.19098) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/caetas/MedSymmFlow) |
| **Data-gravity weighting** | A weighted flow matching method with data gravity-guided for imbalanced data classification | Classification | Flow matching | Imbalanced data | arXiv | -- | `no preprint` |
| **Landmark prior** | Landmark localization from medical images with generative distribution prior | Detection and localization | Normalizing flow | General | IEEE Trans. Medical Imaging | 2024 | `no preprint` |
| **AE-FLOW** | AE-FLOW: Autoencoders with normalizing flows for medical images anomaly detection | Detection and localization | Normalizing flow | General | The Eleventh International Conference on Learning Representations | 2023 | `no preprint` |
| **Craniofacial transport** | Flow Matching for 3D Craniofacial Skeletal Data Generation | Higher-order structural analysis | Flow matching | Craniofacial | MIDL | 2026 | `no preprint` |
| **MedPCFM** | MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching | Higher-order structural analysis | Flow matching | Point clouds | [arXiv](https://arxiv.org/abs/2606.24433) | 2026 | `no code` |
| **CardiacFlow** | CardiacFlow: 3D+ t Four-Chamber Cardiac Shape Completion and Generation via Flow Matching | Higher-order structural analysis | Rectified flow | Cardiac MR | [MICCAI](https://arxiv.org/abs/2509.05754) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/m-qiang/CardiacFlow) |
| **Invertible brain age** | Invertible modeling of bidirectional relationships in neuroimaging with normalizing flows: application to brain aging | Higher-order structural analysis | Normalizing flow | Brain MRI | IEEE Trans. Medical Imaging | 2022 | `no preprint` |
| **Flow SSN** | Flow Stochastic Segmentation Networks | Segmentation: ambiguity and uncertainty | Flow matching | General | [ICCV](https://arxiv.org/abs/2507.18838) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/biomedia-mira/flow-ssn) |
| **Multi-level posterior** | A Multi-Level Probabilistic Deep Learning Network Augmented With Normalizing Flow for Ambiguous Medical Image Segmentation | Segmentation: ambiguity and uncertainty | Normalizing flow | General | IEEE Access | 2025 | `no preprint` |
| **Segmentation bridge** | Ambiguous Medical Image Segmentation Using Diffusion Schrödinger Bridge | Segmentation: ambiguity and uncertainty | Schrödinger bridge | General | MICCAI | 2025 | `no preprint` |
| **Multi-annotator posterior** | Improving aleatoric uncertainty quantification in multi-annotated medical image segmentation with normalizing flows | Segmentation: ambiguity and uncertainty | Normalizing flow | Multi-annotated | [International Workshop on Uncertainty for Safe Utilization of Machine Learning in Medical Imaging](https://arxiv.org/abs/2108.02155) | 2021 | `no code` |
| **cFlow Net** | Uncertainty quantification in medical image segmentation with normalizing flows | Segmentation: ambiguity and uncertainty | Normalizing flow | General | [International Workshop on Machine Learning in Medical Imaging](https://arxiv.org/abs/2006.02683) | 2020 | `no code` |
| **Semantic bridge** | Efficient Breast Cancer Segmentation via Brownian Bridge Diffusion with Semantic Fusion Strategy | Segmentation: continuous mask refinement | Brownian bridge | Breast | Pattern Recognition | 2026 | `no preprint` |
| **FlowSDF** | FlowSDF: Flow matching for medical image segmentation using distance transforms | Segmentation: continuous mask refinement | Flow matching | General | [International Journal of Computer Vision](https://arxiv.org/abs/2405.18087) | 2025 | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/leabogensperger/FlowSDF) |
| **PolypFlow** | PolypFlow: Reinforcing polyp segmentation with flow-driven dynamics | Segmentation: continuous mask refinement | Flow matching | Endoscopy | [arXiv](https://arxiv.org/abs/2502.19037) | 2025 | `no code` |
| **MixStyleFlow** | MixStyleFlow: Domain Generalization in Medical Image Segmentation Using Normalizing Flows | Segmentation: domain and representation transport | Normalizing flow | General | MICCAI | 2025 | `no preprint` |
| **Ventricle segmentation** | CT-based brain ventricle segmentation via diffusion Schrödinger Bridge without target domain ground truths | Segmentation: domain and representation transport | Schrödinger bridge | MRI → CT | MICCAI | 2024 | `no preprint` |
| **Pancreas generalization** | Generalizable pancreas segmentation modeling in CT imaging via meta-learning and latent-space feature flow generation | Segmentation: domain and representation transport | Normalizing flow | CT | IEEE Journal of Biomedical and Health Informatics | 2022 | `no preprint` |

## Implementations

The 34 works that publish a repository, grouped by the transport they learn.

> **Note** &mdash; checked September 2026: 33 of the 34 resolve. `OptPriorFM`
> (Subclass priors) is the path its paper prints, but the repository is no longer
> public. It is listed because this table records what each paper provides.

<details open>
<summary><b>Flow matching</b> (18)</summary>

| Method | Year | Repository |
|---|---|---|
| Contrast-X | 2026 | [github.com/YifanChen02/Contrast-X](https://github.com/YifanChen02/Contrast-X) |
| CRONOS | 2025 | [github.com/MIC-DKFZ/Longitudinal4DMed](https://github.com/MIC-DKFZ/Longitudinal4DMed) |
| EchoLVFM | 2026 | [github.com/EngEmmanuel/EchoLVFM](https://github.com/EngEmmanuel/EchoLVFM) |
| Flow SSN | 2025 | [github.com/biomedia-mira/flow-ssn](https://github.com/biomedia-mira/flow-ssn) |
| FlowPET | 2026 | [github.com/xiaochaorouz/FlowPET](https://github.com/xiaochaorouz/FlowPET) |
| FlowSDF | 2025 | [github.com/leabogensperger/FlowSDF](https://github.com/leabogensperger/FlowSDF) |
| In-context priors | 2026 | [github.com/SamGijsen/pinc-flows](https://github.com/SamGijsen/pinc-flows) |
| MammoFlow | 2026 | [github.com/XYPB/MammoFlow](https://github.com/XYPB/MammoFlow) |
| MedSymmFlow | 2025 | [github.com/caetas/MedSymmFlow](https://github.com/caetas/MedSymmFlow) |
| MOTFM | 2025 | [github.com/milad1378yz/MOTFM](https://github.com/milad1378yz/MOTFM) |
| OsteoFlow | 2026 | [github.com/hamidreza-aftabi/OsteoFlow](https://github.com/hamidreza-aftabi/OsteoFlow) |
| Patient-specific dynamics | 2025 | [github.com/chqwer2/Delta-LDM-Longitudinal](https://github.com/chqwer2/Delta-LDM-Longitudinal) |
| RelativeFlow | 2026 | [github.com/Deliver0/RelativeFlow](https://github.com/Deliver0/RelativeFlow) |
| Restora-Flow | 2026 | [github.com/imigraz/Restora-Flow](https://github.com/imigraz/Restora-Flow) |
| Subclass priors | 2026 | [github.com/Felix-012/OptPriorFM](https://github.com/Felix-012/OptPriorFM) |
| Trajectory-aligned adaptation | 2026 | [github.com/Veit21/tta-flow](https://github.com/Veit21/tta-flow) |
| WaveDiT | 2026 | [github.com/sisinflab/WaveDiT](https://github.com/sisinflab/WaveDiT) |
| WFM | 2026 | [github.com/yalcintur/WFM](https://github.com/yalcintur/WFM) |

</details>

<details open>
<summary><b>Rectified flow</b> (7)</summary>

| Method | Year | Repository |
|---|---|---|
| CardiacFlow | 2025 | [github.com/m-qiang/CardiacFlow](https://github.com/m-qiang/CardiacFlow) |
| DermaFlux | 2026 | [dermaflux.github.io](https://dermaflux.github.io) |
| DRIFT | 2026 | [yoonseokchoi-ai.github.io/drift-eccv2026/](https://yoonseokchoi-ai.github.io/drift-eccv2026/) |
| MPFlow | 2026 | [github.com/edshkim98/MPFlow](https://github.com/edshkim98/MPFlow) |
| RAFM | 2026 | [github.com/HiLab-git/RAFM](https://github.com/HiLab-git/RAFM) |
| Sparse-view reconstruction | 2026 | [github.com/EFMCT/EFMCT](https://github.com/EFMCT/EFMCT) |
| ViCTr | 2025 | [github.com/Onkarsus13/ViCTr-2D](https://github.com/Onkarsus13/ViCTr-2D) |

</details>

<details open>
<summary><b>Normalizing flow</b> (4)</summary>

| Method | Year | Repository |
|---|---|---|
| BlindHarmony | 2023 | [github.com/SNU-LIST/BlindHarmony](https://github.com/SNU-LIST/BlindHarmony) |
| Conditional NF | 2020 | [github.com/VLL-HD/FrEIA](https://github.com/VLL-HD/FrEIA) |
| Harmonizing Flows | 2023 | [github.com/farzad-bz/Harmonizing-Flows](https://github.com/farzad-bz/Harmonizing-Flows) |
| IHF-Harmony | 2026 | [github.com/Idea89560041/IHF-Harmony](https://github.com/Idea89560041/IHF-Harmony) |

</details>

<details open>
<summary><b>Brownian bridge</b> (3)</summary>

| Method | Year | Repository |
|---|---|---|
| Cor2Vox | 2025 | [github.com/ai-med/Cor2Vox](https://github.com/ai-med/Cor2Vox) |
| Prob-BBDM | 2026 | [gitlab.xlim.fr/mvalls/Prob-BBDM](https://gitlab.xlim.fr/mvalls/Prob-BBDM) |
| Slice-consistent BBDM | 2024 | [github.com/MICV-yonsei/CT2MRI](https://github.com/MICV-yonsei/CT2MRI) |

</details>

<details open>
<summary><b>Diffusion or hybrid</b> (1)</summary>

| Method | Year | Repository |
|---|---|---|
| Cortex-grounded generation | 2026 | [github.com/ai-med/Cor2Vox](https://github.com/ai-med/Cor2Vox) |

</details>

<details open>
<summary><b>Schrodinger bridge</b> (1)</summary>

| Method | Year | Repository |
|---|---|---|
| Guided reconstruction | 2024 | [github.com/zhyjSIAT/I2SB-Inversion](https://github.com/zhyjSIAT/I2SB-Inversion) |

</details>

## Datasets

Public dataset families used by more than one reviewed work. A shared dataset is
not yet a comparison: the works on it must also report a measure in common, which
is the last column.

| Dataset family | Works | Metrics shared by two or more |
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

Version families are merged, so BraTS 2021 and BraTS 2023 count as the same footing.

## What the literature measures

Over the 59 works whose full text could be read.

| Metric | Works reporting it |
|---|---|
| SSIM | `####################` 34 |
| PSNR | `###################` 33 |
| Dice | `###########` 19 |
| FID | `#########` 16 |
| LPIPS | `#########` 15 |
| IoU | `#####` 8 |
| MAE | `#####` 8 |
| RMSE | `####` 7 |
| HD95 | `####` 6 |
| MS-SSIM | `####` 6 |
| Accuracy | `###` 5 |
| AUC | `###` 5 |
| F1 | `###` 5 |
| NFE | `###` 5 |
| KID | `##` 4 |

The survey argues that what is *not* measured matters more: no reviewed work reports
external, prospective or reader-in-the-loop evaluation.

## Citation

```bibtex
@article{chen2026flow,
  title   = {Flow-Based Generative Models for Medical Imaging},
  author  = {Chen, Hao and others},
  journal = {Medical Image Analysis},
  year    = {2026}
}
```

## Contributing

Pull requests are welcome. Please add a work by editing the data modules rather than
this file: `code_data.py` for repository status, `datasets_data.py` for datasets and
`metrics_data.py` for reported metrics, then run `python3 make_repo_readme.py`.
This file is generated, so a direct edit to it will be overwritten.

