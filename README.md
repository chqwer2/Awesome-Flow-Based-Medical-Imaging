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

**Paper** links to the preprint where the bibliography carries one; `--` means there is none to link to, not that one was withheld.

**Code** &nbsp; [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](#implementations) a repository is printed, and the badge links to it &nbsp;&middot;&nbsp; `code promised` promised without a link &nbsp;&middot;&nbsp; `no code` neither &nbsp;&middot;&nbsp; `no preprint` the full text could not be reached, so neither presence nor absence of code is claimed &nbsp;&middot;&nbsp; [![code removed](https://img.shields.io/badge/code-removed-9e9e9e?style=flat-square&logo=github&logoColor=white)](#contents) the paper prints a path that no longer resolves

## Image Processing and Restoration

*21 works.*

| Method | Task | Family | Modality | Venue | Year | Paper | Code |
|:--|:--|:--|:--|:--|:--:|:--:|:--:|
| **FlowPET**<br/><sub>FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction</sub> | Reconstruction | Flow matching | PET | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2607.11104) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/xiaochaorouz/FlowPET) |
| **MicroFM**<br/><sub>MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction</sub> | Reconstruction | Flow matching | Microscopy | CVPR | 2026 | -- | `no preprint` |
| **MPFlow**<br/><sub>MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction</sub> | Reconstruction | Rectified flow | MRI | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.03710) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/edshkim98/MPFlow) |
| **Sparse-view reconstruction**<br/><sub>Efficient Flow Matching for Sparse-View CT Reconstruction</sub> | Reconstruction | Rectified flow | CT | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.00205) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EFMCT/EFMCT) |
| **Field-of-view extension**<br/><sub>Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension</sub> | Reconstruction | Schrodinger bridge | CT | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2508.11211) | `no code` |
| **One-way conditional flow**<br/><sub>Unsupervised low-dose CT reconstruction with one-way conditional normalizing flows</sub> | Reconstruction | Normalizing flow | CT | IEEE Trans. Computational Imaging | 2025 | [arXiv](https://arxiv.org/abs/2410.17543) | `no code` |
| **Guided reconstruction**<br/><sub>Guided MRI Reconstruction via Schrödinger Bridge</sub> | Reconstruction | Schrodinger bridge | MRI | arXiv | 2024 | [arXiv](https://arxiv.org/abs/2411.14269) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/zhyjSIAT/I2SB-Inversion) |
| **AmbientFlow**<br/><sub>AmbientFlow: Invertible generative models from incomplete, noisy measurements</sub> | Reconstruction | Normalizing flow | General | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2309.04856) | `no code` |
| **Conditional NF**<br/><sub>Conditional normalizing flows for low-dose computed tomography image reconstruction</sub> | Reconstruction | Normalizing flow | CT | arXiv | 2020 | [arXiv](https://arxiv.org/abs/2006.06270) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VLL-HD/FrEIA) |
| **RelativeFlow**<br/><sub>RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference</sub> | Restoration | Flow matching | General | CVPR | 2026 | [arXiv](https://arxiv.org/abs/2604.15459) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Deliver0/RelativeFlow) |
| **Restora-Flow**<br/><sub>Restora-Flow: Mask-Guided Image Restoration with Flow Matching</sub> | Restoration | Flow matching | General | Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision | 2026 | [arXiv](https://arxiv.org/abs/2511.20152) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/imigraz/Restora-Flow) |
| **3T-to-7T recovery**<br/><sub>Schrödinger Diffusion Driven Signal Recovery in 3T BOLD fMRI Using Unmatched 7T Observations</sub> | Restoration | Schrodinger bridge | BOLD fMRI | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2504.01004) | `no code` |
| **Low-field enhancement**<br/><sub>Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model</sub> | Restoration | Flow matching | MRI | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.12408) | `no code` |
| **PFCM**<br/><sub>PFCM: Poisson flow consistency models for low-dose CT image denoising</sub> | Restoration | Diffusion or hybrid | CT | IEEE Trans. Medical Imaging | 2025 | [arXiv](https://arxiv.org/abs/2402.08159) | `no code` |
| **AF2R**<br/><sub>Realistic Restorer: artifact-free flow restorer (AF2R) for MRI motion artifact removal</sub> | Restoration | Normalizing flow | MRI | arXiv | 2023 | [arXiv](https://arxiv.org/abs/2306.10689) | `no code` |
| **MRI-derived prior**<br/><sub>Ultrasound speckle suppression and denoising using MRI-derived normalizing flow priors</sub> | Restoration | Normalizing flow | Ultrasound | arXiv | 2021 | [arXiv](https://arxiv.org/abs/2112.13110) | `no code` |
| **CAFlow**<br/><sub>CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution</sub> | Super-resolution | Flow matching | Histopathology | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.18513) | `no code` |
| **DRIFT**<br/><sub>DRIFT: Difficulty-aware Rectified Flows for Through-plane MRI Super-Resolution</sub> | Super-resolution | Rectified flow | MRI | ECCV | 2026 | [arXiv](https://arxiv.org/abs/2607.16649) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://yoonseokchoi-ai.github.io/drift-eccv2026/) |
| **FTDDM**<br/><sub>A flow-based truncated denoising diffusion model for super-resolution magnetic resonance spectroscopic imaging</sub> | Super-resolution | Diffusion or hybrid | MR spectroscopic imaging | Medical Image Analysis | 2025 | [arXiv](https://arxiv.org/abs/2410.19288) | `code promised` |
| **Conditional stochastic NF**<br/><sub>Simultaneous super-resolution and denoising on MRI via conditional stochastic normalizing flow</sub> | Super-resolution | Normalizing flow | MRI | IEEE International Conference on Bioinformatics and Biomedicine | 2023 | -- | `no preprint` |
| **MRIFlow**<br/><sub>MRIFlow: Magnetic resonance image super-resolution based on normalizing flow and frequency prior</sub> | Super-resolution | Normalizing flow | MRI | Journal of Magnetic Resonance | 2023 | -- | `no preprint` |

## Cross-Modal Translation and Harmonization

*23 works.*

| Method | Task | Family | Modality | Venue | Year | Paper | Code |
|:--|:--|:--|:--|:--|:--:|:--:|:--:|
| **Prob-BBDM**<br/><sub>Prob-BBDM: A probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation</sub> | Cross-modal translation: MRI-centred | Brownian bridge | MRI sequences | Computerized Medical Imaging and Graphics | 2026 | [arXiv](https://arxiv.org/abs/2606.24313) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://gitlab.xlim.fr/mvalls/Prob-BBDM) |
| **Multi-contrast synthesis**<br/><sub>Multi-contrast MR image synthesis with a Brownian diffusion model</sub> | Cross-modal translation: MRI-centred | Brownian bridge | Multi-contrast MRI | Signal Processing and Communications Applications Conference | 2024 | -- | `no preprint` |
| **Slice-consistent BBDM**<br/><sub>Slice-consistent 3D volumetric brain CT-to-MRI translation with 2D Brownian bridge diffusion model</sub> | Cross-modal translation: MRI-centred | Brownian bridge | CT $\rightarrow$ MRI | MICCAI | 2024 | [arXiv](https://arxiv.org/abs/2407.05059) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MICV-yonsei/CT2MRI) |
| **CBCT-conditioned synthesis**<br/><sub>CBCT-Based Synthetic CT Generation Using Conditional Flow Matching Model</sub> | Cross-modal translation: synthetic CT | Flow matching | CBCT $\rightarrow$ CT | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.05796) | `no code` |
| **Human-guided bridge**<br/><sub>Human-Guided Shading Artifact Suppression in CBCT-to-MDCT Translation via Schrödinger Bridge with Conditional Diffusion</sub> | Cross-modal translation: synthetic CT | Schrodinger bridge | CBCT $\rightarrow$ MDCT | IEEE Trans. Radiation and Plasma Medical Sciences | 2026 | [arXiv](https://arxiv.org/abs/2507.11025) | `no code` |
| **RAFM**<br/><sub>RAFM: Retrieval-Augmented Flow Matching for Unpaired CBCT-to-CT Translation</sub> | Cross-modal translation: synthetic CT | Rectified flow | MRI $\rightarrow$ CT | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.00535) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/HiLab-git/RAFM) |
| **Anatomy-conserving bridge**<br/><sub>Anatomy-Conserving Unpaired CBCT-to-CT Translation via Schrödinger Bridge</sub> | Cross-modal translation: synthetic CT | Schrodinger bridge | CBCT $\rightarrow$ CT | MICCAI | 2025 | -- | `no preprint` |
| **Conditional flow matching**<br/><sub>Flow Matching for Conditional MRI-CT and CBCT-CT Image Synthesis</sub> | Cross-modal translation: synthetic CT | Flow matching | MRI, CBCT $\rightarrow$ CT | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.04823) | `no code` |
| **Structure-residual bridge**<br/><sub>Structure-Residual Diffusion Bridge Model for MRI-to-CT Image Translation</sub> | Cross-modal translation: synthetic CT | Diffusion or hybrid | MRI $\rightarrow$ CT | International Conference on Virtual Reality and Visualization | 2025 | -- | `no preprint` |
| **IHF-Harmony**<br/><sub>IHF-Harmony: Multi-Modality Magnetic Resonance Images Harmonization using Invertible Hierarchy Flow Model</sub> | Domain harmonization | Normalizing flow | Multi-modal MRI | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2602.21536) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Idea89560041/IHF-Harmony) |
| **LMSB**<br/><sub>Optical Coherence Tomography Harmonization with Anatomy-Guided Latent Metric Schrödinger Bridges</sub> | Domain harmonization | Schrodinger bridge | OCT | NeurIPS | 2026 | -- | `no preprint` |
| **Trajectory-aligned adaptation**<br/><sub>Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow</sub> | Domain harmonization | Flow matching | OCT | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.18876) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Veit21/tta-flow) |
| **BlindHarmony**<br/><sub>BlindHarmony:" blind" harmonization for MR images via flow model</sub> | Domain harmonization | Normalizing flow | MRI | ICCV | 2023 | [arXiv](https://arxiv.org/abs/2305.10732) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SNU-LIST/BlindHarmony) |
| **CTFlow (Wei et~al.)**<br/><sub>CTFlow: Mitigating effects of computed tomography acquisition and reconstruction with normalizing flows</sub> | Domain harmonization | Normalizing flow | CT | MICCAI | 2023 | -- | `no preprint` |
| **Harmonizing Flows**<br/><sub>Harmonizing Flows: Unsupervised MR harmonization based on normalizing flows</sub> | Domain harmonization | Normalizing flow | MRI | International Conference on Information Processing in Medical Imaging | 2023 | [arXiv](https://arxiv.org/abs/2301.11551) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/farzad-bz/Harmonizing-Flows) |
| **Kernel conversion**<br/><sub>CT Kernel Conversion for Quantitative Assessment in Chronic Obstructive Pulmonary Disease Using an Image-to-Image Schrödinger Bridge Model</sub> | Domain harmonization | Schrodinger bridge | CT | -- | -- | -- | `no preprint` |
| **FM-fMRI**<br/><sub>FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis</sub> | Functional-state translation | Flow matching | fMRI time series | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2605.26423) | `code promised` |
| **Contrast-X**<br/><sub>Contrast-X: A Multi-Modal Contrast Image Synthesis Benchmark and Universal Modality Flow Matching</sub> | Missing-modality translation | Flow matching | CT, multi-phase MRI | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.15884) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/YifanChen02/Contrast-X) |
| **WFM**<br/><sub>WFM: 3D Wavelet Flow Matching for Ultrafast Multi-Modal MRI Synthesis</sub> | Missing-modality translation | Flow matching | Multi-modal MRI | MIDL | 2026 | [arXiv](https://arxiv.org/abs/2604.21146) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/yalcintur/WFM) |
| **Topology-aware DSB**<br/><sub>Topology-aware Diffusion Schrödinger Bridge for Unpaired H&E-to-IHC Stain Translation</sub> | Virtual staining | Schrodinger bridge | H\&E $\rightarrow$ IHC | IEEE Journal of Biomedical and Health Informatics | 2026 | -- | `no preprint` |
| **PASB**<br/><sub>PASB: Pathology-Aware Schrödinger Bridge for Virtual Immunohistochemical Staining</sub> | Virtual staining | Schrodinger bridge | H\&E $\rightarrow$ IHC | Medical Image Analysis | 2025 | -- | `no preprint` |
| **Pixel super-resolved staining**<br/><sub>Pixel super-resolved virtual staining of label-free tissue using diffusion models</sub> | Virtual staining | Diffusion or hybrid | Label-free $\rightarrow$ stained | Nature Communications | 2025 | [arXiv](https://arxiv.org/abs/2410.20073) | `no code` |
| **StainSB**<br/><sub>Weakly Supervised Virtual Immunohistochemistry Staining via Schrödinger Bridge Method</sub> | Virtual staining | Schrodinger bridge | H\&E $\rightarrow$ IHC | IEEE International Conference on Bioinformatics and Biomedicine | 2024 | -- | `no preprint` |

## Image Generation and Augmentation

*24 works.*

| Method | Task | Family | Modality | Venue | Year | Paper | Code |
|:--|:--|:--|:--|:--|:--:|:--:|:--:|
| **Cortex-grounded generation**<br/><sub>Cortex-Grounded Diffusion Models for Brain Image Generation</sub> | Controllable and structure-guided generation | Diffusion or hybrid | Brain MRI | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2601.19498) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/Cor2Vox) |
| **EchoLVFM**<br/><sub>EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis</sub> | Controllable and structure-guided generation | Flow matching | Echocardiography | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.13967) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/EngEmmanuel/EchoLVFM) |
| **GeneVAR**<br/><sub>GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis</sub> | Controllable and structure-guided generation | Flow matching | Histopathology | CVPR | 2026 | -- | `no preprint` |
| **Multimodal bridge**<br/><sub>Multimodal Brownian bridge diffusion model for controllable synthetic medical image generation</sub> | Controllable and structure-guided generation | Brownian bridge | General | Biomedical Signal Processing and Control | 2026 | -- | `no preprint` |
| **Cor2Vox**<br/><sub>3D shape-to-image Brownian bridge diffusion for brain MRI synthesis from cortical surfaces</sub> | Controllable and structure-guided generation | Brownian bridge | Brain MRI | International Conference on Information Processing in Medical Imaging | 2025 | [arXiv](https://arxiv.org/abs/2502.12742) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ai-med/Cor2Vox) |
| **CTFlow (Wang et~al.)**<br/><sub>CTFlow: Video-Inspired Latent Flow Matching for 3D CT Synthesis</sub> | Controllable and structure-guided generation | Flow matching | CT, 3D | ICCV | 2025 | [arXiv](https://arxiv.org/abs/2508.12900) | `no code` |
| **Surf2CT**<br/><sub>Surf2CT: Cascaded 3D Flow Matching Models for Torso 3D CT Synthesis from Skin Surface</sub> | Controllable and structure-guided generation | Flow matching | Torso CT | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2505.22511) | `no code` |
| **TumorGen**<br/><sub>TumorGen: Boundary-Aware Tumor-Mask Synthesis with Rectified Flow Matching</sub> | Controllable and structure-guided generation | Rectified flow | Tumor masks | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2505.24687) | `no code` |
| **ViCTr**<br/><sub>ViCTr: Vital consistency transfer for pathology aware image synthesis</sub> | Controllable and structure-guided generation | Rectified flow | Pathology-aware synthesis | ICCV | 2025 | [arXiv](https://arxiv.org/abs/2505.04963) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Onkarsus13/ViCTr-2D) |
| **DermaFlux**<br/><sub>DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification</sub> | Data-augmentation-oriented generation | Rectified flow | Dermoscopy | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.16392) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://dermaflux.github.io) |
| **Distribution-aligned synthesis**<br/><sub>Few-Shot Distribution-Aligned Flow Matching for Data Synthesis in Medical Image Segmentation</sub> | Data-augmentation-oriented generation | Flow matching | Segmentation datasets | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2604.02868) | `no code` |
| **MammoFlow**<br/><sub>MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching</sub> | Data-augmentation-oriented generation | Flow matching | Mammography | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.28537) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/XYPB/MammoFlow) |
| **MoGen**<br/><sub>MoGen: Detailed Neuronal Morphology Generation via Point Cloud Flow Matching</sub> | Data-augmentation-oriented generation | Flow matching | Neuronal point clouds | The Fourteenth International Conference on Learning Representations | 2026 | -- | `no preprint` |
| **STREAM**<br/><sub>STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation</sub> | Data-augmentation-oriented generation | Flow matching | Histopathology | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.07036) | `code promised` |
| **Subclass priors**<br/><sub>Flow Matching with Optimized Subclass Priors for Medical Image Augmentation</sub> | Data-augmentation-oriented generation | Flow matching | General | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2605.16469) | [![code removed](https://img.shields.io/badge/code-removed-9e9e9e?style=flat-square&logo=github&logoColor=white)](https://github.com/Felix-012/OptPriorFM) |
| **WaveDiT**<br/><sub>WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis</sub> | Data-augmentation-oriented generation | Flow matching | Brain MRI, 3D | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.08670) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sisinflab/WaveDiT) |
| **Landmark-oriented synthesis**<br/><sub>Flow matching-based data synthesis for robust anatomical landmark localization</sub> | Data-augmentation-oriented generation | Flow matching | Landmark datasets | IEEE Journal of Biomedical and Health Informatics | 2025 | -- | `no preprint` |
| **MOTFM**<br/><sub>Flow matching for medical image synthesis: Bridging the gap between speed and quality</sub> | Data-augmentation-oriented generation | Flow matching | General, 2D and 3D | MICCAI | 2025 | [arXiv](https://arxiv.org/abs/2503.00266) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/milad1378yz/MOTFM) |
| **RealNVP synthesis**<br/><sub>Normalizing flow for synthetic medical images generation</sub> | Data-augmentation-oriented generation | Normalizing flow | Chest X-ray, skin lesion | IEEE Healthcare Innovations and Point of Care Technologies | 2022 | -- | `no preprint` |
| **In-context priors**<br/><sub>Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics</sub> | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | fMRI dynamics | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.11833) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/SamGijsen/pinc-flows) |
| **OsteoFlow**<br/><sub>OsteoFlow: Lyapunov-Guided Flow Distillation for Predicting Bone Remodeling after Mandibular Reconstruction</sub> | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | Mandibular CT | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2603.22421) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/hamidreza-aftabi/OsteoFlow) |
| **Reversed progression**<br/><sub>Vector Quantization for Reversed Disease Progression: Further Investigations</sub> | Longitudinal, treatment-conditioned, and counterfactual generation | Not a flow | Longitudinal imaging | MIDL | 2026 | -- | `no preprint` |
| **CRONOS**<br/><sub>CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series</sub> | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | 4D longitudinal series | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2512.16577) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MIC-DKFZ/Longitudinal4DMed) |
| **Patient-specific dynamics**<br/><sub>Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation</sub> | Longitudinal, treatment-conditioned, and counterfactual generation | Flow matching | Longitudinal imaging | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2512.09185) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/chqwer2/Delta-LDM-Longitudinal) |

## Analysis: Classification, Segmentation, Detection

*21 works.*

| Method | Task | Family | Modality | Venue | Year | Paper | Code |
|:--|:--|:--|:--|:--|:--:|:--:|:--:|
| **Flow-MIL**<br/><sub>Flow-MIL: Constructing Highly-expressive Latent Feature Space For Whole Slide Image Classification Using Normalizing Flow</sub> | Classification | Normalizing flow | Histopathology | ICCV | 2025 | -- | `no preprint` |
| **MAGIC-Flow**<br/><sub>MAGIC-Flow: Multiscale Adaptive Conditional Flows for Generation and Interpretable Classification</sub> | Classification | Normalizing flow | General | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2510.22070) | `no code` |
| **MedSymmFlow**<br/><sub>MedSymmFlow: Bridging Generative Modeling and Classification in Medical Imaging Through Symmetrical Flow Matching</sub> | Classification | Flow matching | 2D benchmarks | MICCAI Workshop on Deep Generative Models | 2025 | [arXiv](https://arxiv.org/abs/2507.19098) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/caetas/MedSymmFlow) |
| **Data-gravity weighting**<br/><sub>A weighted flow matching method with data gravity-guided for imbalanced data classification</sub> | Classification | Flow matching | Imbalanced data | -- | -- | -- | `no preprint` |
| **Landmark prior**<br/><sub>Landmark localization from medical images with generative distribution prior</sub> | Detection and localization | Normalizing flow | General | IEEE Trans. Medical Imaging | 2024 | -- | `no preprint` |
| **AE-FLOW**<br/><sub>AE-FLOW: Autoencoders with normalizing flows for medical images anomaly detection</sub> | Detection and localization | Normalizing flow | General | The Eleventh International Conference on Learning Representations | 2023 | -- | `no preprint` |
| **Craniofacial transport**<br/><sub>Flow Matching for 3D Craniofacial Skeletal Data Generation</sub> | Higher-order structural analysis | Flow matching | Craniofacial | MIDL | 2026 | -- | `no preprint` |
| **MedPCFM**<br/><sub>MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching</sub> | Higher-order structural analysis | Flow matching | Point clouds | arXiv | 2026 | [arXiv](https://arxiv.org/abs/2606.24433) | `no code` |
| **CardiacFlow**<br/><sub>CardiacFlow: 3D+ t Four-Chamber Cardiac Shape Completion and Generation via Flow Matching</sub> | Higher-order structural analysis | Rectified flow | Cardiac MR | MICCAI | 2025 | [arXiv](https://arxiv.org/abs/2509.05754) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/m-qiang/CardiacFlow) |
| **Invertible brain age**<br/><sub>Invertible modeling of bidirectional relationships in neuroimaging with normalizing flows: application to brain aging</sub> | Higher-order structural analysis | Normalizing flow | Brain MRI | IEEE Trans. Medical Imaging | 2022 | -- | `no preprint` |
| **Flow SSN**<br/><sub>Flow Stochastic Segmentation Networks</sub> | Segmentation: ambiguity and uncertainty | Flow matching | General | ICCV | 2025 | [arXiv](https://arxiv.org/abs/2507.18838) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/biomedia-mira/flow-ssn) |
| **Multi-level posterior**<br/><sub>A Multi-Level Probabilistic Deep Learning Network Augmented With Normalizing Flow for Ambiguous Medical Image Segmentation</sub> | Segmentation: ambiguity and uncertainty | Normalizing flow | General | IEEE Access | 2025 | -- | `no preprint` |
| **Segmentation bridge**<br/><sub>Ambiguous Medical Image Segmentation Using Diffusion Schrödinger Bridge</sub> | Segmentation: ambiguity and uncertainty | Schrodinger bridge | General | MICCAI | 2025 | -- | `no preprint` |
| **Multi-annotator posterior**<br/><sub>Improving aleatoric uncertainty quantification in multi-annotated medical image segmentation with normalizing flows</sub> | Segmentation: ambiguity and uncertainty | Normalizing flow | Multi-annotated | International Workshop on Uncertainty for Safe Utilization of Machine Learning in Medical Imaging | 2021 | [arXiv](https://arxiv.org/abs/2108.02155) | `no code` |
| **cFlow Net**<br/><sub>Uncertainty quantification in medical image segmentation with normalizing flows</sub> | Segmentation: ambiguity and uncertainty | Normalizing flow | General | International Workshop on Machine Learning in Medical Imaging | 2020 | [arXiv](https://arxiv.org/abs/2006.02683) | `no code` |
| **Semantic bridge**<br/><sub>Efficient Breast Cancer Segmentation via Brownian Bridge Diffusion with Semantic Fusion Strategy</sub> | Segmentation: continuous mask refinement | Brownian bridge | Breast | Pattern Recognition | 2026 | -- | `no preprint` |
| **FlowSDF**<br/><sub>FlowSDF: Flow matching for medical image segmentation using distance transforms</sub> | Segmentation: continuous mask refinement | Flow matching | General | International Journal of Computer Vision | 2025 | [arXiv](https://arxiv.org/abs/2405.18087) | [![code](https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/leabogensperger/FlowSDF) |
| **PolypFlow**<br/><sub>PolypFlow: Reinforcing polyp segmentation with flow-driven dynamics</sub> | Segmentation: continuous mask refinement | Flow matching | Endoscopy | arXiv | 2025 | [arXiv](https://arxiv.org/abs/2502.19037) | `no code` |
| **MixStyleFlow**<br/><sub>MixStyleFlow: Domain Generalization in Medical Image Segmentation Using Normalizing Flows</sub> | Segmentation: domain and representation transport | Normalizing flow | General | MICCAI | 2025 | -- | `no preprint` |
| **Ventricle segmentation**<br/><sub>CT-based brain ventricle segmentation via diffusion Schrödinger Bridge without target domain ground truths</sub> | Segmentation: domain and representation transport | Schrodinger bridge | MRI $\rightarrow$ CT | MICCAI | 2024 | -- | `no preprint` |
| **Pancreas generalization**<br/><sub>Generalizable pancreas segmentation modeling in CT imaging via meta-learning and latent-space feature flow generation</sub> | Segmentation: domain and representation transport | Normalizing flow | CT | IEEE Journal of Biomedical and Health Informatics | 2022 | -- | `no preprint` |

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

