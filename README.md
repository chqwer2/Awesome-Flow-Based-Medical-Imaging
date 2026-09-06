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

**[`code`]** a repository is printed &nbsp;&middot;&nbsp; `code promised` promised without a link &nbsp;&middot;&nbsp; `no code` neither &nbsp;&middot;&nbsp; `no preprint` full text could not be reached, so nothing is claimed either way

## Image Processing and Restoration

*21 works.*

### Reconstruction

- **FlowPET** &mdash; *FlowPET: Physics-Informed Symplectic Flow Matching for Low-Count PET Reconstruction* &mdash; arXiv, 2026 **[`code`](https://github.com/xiaochaorouz/FlowPET)**
  <br/><sub>Flow matching &nbsp;|&nbsp; PET</sub>
- **MicroFM** &mdash; *MicroFM: Physics-guided Flow Matching for Isotropic Microscopy Reconstruction* &mdash; CVPR, 2026 `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Microscopy</sub>
- **MPFlow** &mdash; *MPFlow: Multi-modal Posterior-Guided Flow Matching for Zero-Shot MRI Reconstruction* &mdash; arXiv, 2026 **[`code`](https://github.com/edshkim98/MPFlow)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; MRI</sub>
- **Sparse-view reconstruction** &mdash; *Efficient Flow Matching for Sparse-View CT Reconstruction* &mdash; arXiv, 2026 **[`code`](https://github.com/EFMCT/EFMCT)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; CT</sub>
- **Field-of-view extension** &mdash; *Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension* &mdash; arXiv, 2025 `no code`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; CT</sub>
- **One-way conditional flow** &mdash; *Unsupervised low-dose CT reconstruction with one-way conditional normalizing flows* &mdash; IEEE Trans. Computational Imaging, 2025 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; CT</sub>
- **Guided reconstruction** &mdash; *Guided MRI Reconstruction via Schrödinger Bridge* &mdash; arXiv, 2024 **[`code`](https://github.com/zhyjSIAT/I2SB-Inversion)**
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; MRI</sub>
- **AmbientFlow** &mdash; *AmbientFlow: Invertible generative models from incomplete, noisy measurements* &mdash; arXiv, 2023 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>
- **Conditional NF** &mdash; *Conditional normalizing flows for low-dose computed tomography image reconstruction* &mdash; arXiv, 2020 **[`code`](https://github.com/VLL-HD/FrEIA)**
  <br/><sub>Normalizing flow &nbsp;|&nbsp; CT</sub>

### Restoration

- **RelativeFlow** &mdash; *RelativeFlow: Taming Medical Image Denoising Learning with Noisy Reference* &mdash; CVPR, 2026 **[`code`](https://github.com/Deliver0/RelativeFlow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General</sub>
- **Restora-Flow** &mdash; *Restora-Flow: Mask-Guided Image Restoration with Flow Matching* &mdash; Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, 2026 **[`code`](https://github.com/imigraz/Restora-Flow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General</sub>
- **3T-to-7T recovery** &mdash; *Schrödinger Diffusion Driven Signal Recovery in 3T BOLD fMRI Using Unmatched 7T Observations* &mdash; arXiv, 2025 `no code`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; BOLD fMRI</sub>
- **Low-field enhancement** &mdash; *Low-Field Magnetic Resonance Image Quality Enhancement using a Conditional Flow Matching Model* &mdash; arXiv, 2025 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; MRI</sub>
- **PFCM** &mdash; *PFCM: Poisson flow consistency models for low-dose CT image denoising* &mdash; IEEE Trans. Medical Imaging, 2025 `no code`
  <br/><sub>Diffusion or hybrid &nbsp;|&nbsp; CT</sub>
- **AF2R** &mdash; *Realistic Restorer: artifact-free flow restorer (AF2R) for MRI motion artifact removal* &mdash; arXiv, 2023 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; MRI</sub>
- **MRI-derived prior** &mdash; *Ultrasound speckle suppression and denoising using MRI-derived normalizing flow priors* &mdash; arXiv, 2021 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Ultrasound</sub>

### Super-resolution

- **CAFlow** &mdash; *CAFlow: Adaptive-Depth Single-Step Flow Matching for Efficient Histopathology Super-Resolution* &mdash; arXiv, 2026 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; Histopathology</sub>
- **DRIFT** &mdash; *DRIFT: Difficulty-aware Rectified Flows for Through-plane MRI Super-Resolution* &mdash; ECCV, 2026 **[`code`](https://yoonseokchoi-ai.github.io/drift-eccv2026/)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; MRI</sub>
- **FTDDM** &mdash; *A flow-based truncated denoising diffusion model for super-resolution magnetic resonance spectroscopic imaging* &mdash; Medical Image Analysis, 2025 `code promised`
  <br/><sub>Diffusion or hybrid &nbsp;|&nbsp; MR spectroscopic imaging</sub>
- **Conditional stochastic NF** &mdash; *Simultaneous super-resolution and denoising on MRI via conditional stochastic normalizing flow* &mdash; IEEE International Conference on Bioinformatics and Biomedicine, 2023 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; MRI</sub>
- **MRIFlow** &mdash; *MRIFlow: Magnetic resonance image super-resolution based on normalizing flow and frequency prior* &mdash; Journal of Magnetic Resonance, 2023 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; MRI</sub>

## Cross-Modal Translation and Harmonization

*23 works.*

### Cross-modal translation: MRI-centred

- **Prob-BBDM** &mdash; *Prob-BBDM: A probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation* &mdash; Computerized Medical Imaging and Graphics, 2026 **[`code`](https://gitlab.xlim.fr/mvalls/Prob-BBDM)**
  <br/><sub>Brownian bridge &nbsp;|&nbsp; MRI sequences</sub>
- **Multi-contrast synthesis** &mdash; *Multi-contrast MR image synthesis with a Brownian diffusion model* &mdash; Signal Processing and Communications Applications Conference, 2024 `no preprint`
  <br/><sub>Brownian bridge &nbsp;|&nbsp; Multi-contrast MRI</sub>
- **Slice-consistent BBDM** &mdash; *Slice-consistent 3D volumetric brain CT-to-MRI translation with 2D Brownian bridge diffusion model* &mdash; MICCAI, 2024 **[`code`](https://github.com/MICV-yonsei/CT2MRI)**
  <br/><sub>Brownian bridge &nbsp;|&nbsp; CT $\rightarrow$ MRI</sub>

### Cross-modal translation: synthetic CT

- **CBCT-conditioned synthesis** &mdash; *CBCT-Based Synthetic CT Generation Using Conditional Flow Matching Model* &mdash; arXiv, 2026 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; CBCT $\rightarrow$ CT</sub>
- **Human-guided bridge** &mdash; *Human-Guided Shading Artifact Suppression in CBCT-to-MDCT Translation via Schrödinger Bridge with Conditional Diffusion* &mdash; IEEE Trans. Radiation and Plasma Medical Sciences, 2026 `no code`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; CBCT $\rightarrow$ MDCT</sub>
- **RAFM** &mdash; *RAFM: Retrieval-Augmented Flow Matching for Unpaired CBCT-to-CT Translation* &mdash; arXiv, 2026 **[`code`](https://github.com/HiLab-git/RAFM)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; MRI $\rightarrow$ CT</sub>
- **Anatomy-conserving bridge** &mdash; *Anatomy-Conserving Unpaired CBCT-to-CT Translation via Schrödinger Bridge* &mdash; MICCAI, 2025 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; CBCT $\rightarrow$ CT</sub>
- **Conditional flow matching** &mdash; *Flow Matching for Conditional MRI-CT and CBCT-CT Image Synthesis* &mdash; arXiv, 2025 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; MRI, CBCT $\rightarrow$ CT</sub>
- **Structure-residual bridge** &mdash; *Structure-Residual Diffusion Bridge Model for MRI-to-CT Image Translation* &mdash; International Conference on Virtual Reality and Visualization, 2025 `no preprint`
  <br/><sub>Diffusion or hybrid &nbsp;|&nbsp; MRI $\rightarrow$ CT</sub>

### Domain harmonization

- **IHF-Harmony** &mdash; *IHF-Harmony: Multi-Modality Magnetic Resonance Images Harmonization using Invertible Hierarchy Flow Model* &mdash; arXiv, 2026 **[`code`](https://github.com/Idea89560041/IHF-Harmony)**
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Multi-modal MRI</sub>
- **LMSB** &mdash; *Optical Coherence Tomography Harmonization with Anatomy-Guided Latent Metric Schrödinger Bridges* &mdash; NeurIPS, 2026 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; OCT</sub>
- **Trajectory-aligned adaptation** &mdash; *Test-Time Adaptation in Optical Coherence Tomography Using Trajectory-Aligned Time-Independent Flow* &mdash; arXiv, 2026 **[`code`](https://github.com/Veit21/tta-flow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; OCT</sub>
- **BlindHarmony** &mdash; *BlindHarmony:" blind" harmonization for MR images via flow model* &mdash; ICCV, 2023 **[`code`](https://github.com/SNU-LIST/BlindHarmony)**
  <br/><sub>Normalizing flow &nbsp;|&nbsp; MRI</sub>
- **CTFlow (Wei et~al.)** &mdash; *CTFlow: Mitigating effects of computed tomography acquisition and reconstruction with normalizing flows* &mdash; MICCAI, 2023 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; CT</sub>
- **Harmonizing Flows** &mdash; *Harmonizing Flows: Unsupervised MR harmonization based on normalizing flows* &mdash; International Conference on Information Processing in Medical Imaging, 2023 **[`code`](https://github.com/farzad-bz/Harmonizing-Flows)**
  <br/><sub>Normalizing flow &nbsp;|&nbsp; MRI</sub>
- **Kernel conversion** &mdash; *CT Kernel Conversion for Quantitative Assessment in Chronic Obstructive Pulmonary Disease Using an Image-to-Image Schrödinger Bridge Model* `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; CT</sub>

### Functional-state translation

- **FM-fMRI** &mdash; *FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis* &mdash; arXiv, 2026 `code promised`
  <br/><sub>Flow matching &nbsp;|&nbsp; fMRI time series</sub>

### Missing-modality translation

- **Contrast-X** &mdash; *Contrast-X: A Multi-Modal Contrast Image Synthesis Benchmark and Universal Modality Flow Matching* &mdash; arXiv, 2026 **[`code`](https://github.com/YifanChen02/Contrast-X)**
  <br/><sub>Flow matching &nbsp;|&nbsp; CT, multi-phase MRI</sub>
- **WFM** &mdash; *WFM: 3D Wavelet Flow Matching for Ultrafast Multi-Modal MRI Synthesis* &mdash; MIDL, 2026 **[`code`](https://github.com/yalcintur/WFM)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Multi-modal MRI</sub>

### Virtual staining

- **Topology-aware DSB** &mdash; *Topology-aware Diffusion Schrödinger Bridge for Unpaired H&E-to-IHC Stain Translation* &mdash; IEEE Journal of Biomedical and Health Informatics, 2026 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; H\&E $\rightarrow$ IHC</sub>
- **PASB** &mdash; *PASB: Pathology-Aware Schrödinger Bridge for Virtual Immunohistochemical Staining* &mdash; Medical Image Analysis, 2025 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; H\&E $\rightarrow$ IHC</sub>
- **Pixel super-resolved staining** &mdash; *Pixel super-resolved virtual staining of label-free tissue using diffusion models* &mdash; Nature Communications, 2025 `no code`
  <br/><sub>Diffusion or hybrid &nbsp;|&nbsp; Label-free $\rightarrow$ stained</sub>
- **StainSB** &mdash; *Weakly Supervised Virtual Immunohistochemistry Staining via Schrödinger Bridge Method* &mdash; IEEE International Conference on Bioinformatics and Biomedicine, 2024 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; H\&E $\rightarrow$ IHC</sub>

## Image Generation and Augmentation

*24 works.*

### Controllable and structure-guided generation

- **Cortex-grounded generation** &mdash; *Cortex-Grounded Diffusion Models for Brain Image Generation* &mdash; arXiv, 2026 **[`code`](https://github.com/ai-med/Cor2Vox)**
  <br/><sub>Diffusion or hybrid &nbsp;|&nbsp; Brain MRI</sub>
- **EchoLVFM** &mdash; *EchoLVFM: One-Step Video Generation via Latent Flow Matching for Echocardiogram Synthesis* &mdash; arXiv, 2026 **[`code`](https://github.com/EngEmmanuel/EchoLVFM)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Echocardiography</sub>
- **GeneVAR** &mdash; *GeneVAR: Causal MeanFlow for Autoregressive Gene-to-WSI Tile Synthesis* &mdash; CVPR, 2026 `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Histopathology</sub>
- **Multimodal bridge** &mdash; *Multimodal Brownian bridge diffusion model for controllable synthetic medical image generation* &mdash; Biomedical Signal Processing and Control, 2026 `no preprint`
  <br/><sub>Brownian bridge &nbsp;|&nbsp; General</sub>
- **Cor2Vox** &mdash; *3D shape-to-image Brownian bridge diffusion for brain MRI synthesis from cortical surfaces* &mdash; International Conference on Information Processing in Medical Imaging, 2025 **[`code`](https://github.com/ai-med/Cor2Vox)**
  <br/><sub>Brownian bridge &nbsp;|&nbsp; Brain MRI</sub>
- **CTFlow (Wang et~al.)** &mdash; *CTFlow: Video-Inspired Latent Flow Matching for 3D CT Synthesis* &mdash; ICCV, 2025 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; CT, 3D</sub>
- **Surf2CT** &mdash; *Surf2CT: Cascaded 3D Flow Matching Models for Torso 3D CT Synthesis from Skin Surface* &mdash; arXiv, 2025 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; Torso CT</sub>
- **TumorGen** &mdash; *TumorGen: Boundary-Aware Tumor-Mask Synthesis with Rectified Flow Matching* &mdash; arXiv, 2025 `no code`
  <br/><sub>Rectified flow &nbsp;|&nbsp; Tumor masks</sub>
- **ViCTr** &mdash; *ViCTr: Vital consistency transfer for pathology aware image synthesis* &mdash; ICCV, 2025 **[`code`](https://github.com/Onkarsus13/ViCTr-2D)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; Pathology-aware synthesis</sub>

### Data-augmentation-oriented generation

- **DermaFlux** &mdash; *DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification* &mdash; arXiv, 2026 **[`code`](https://dermaflux.github.io)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; Dermoscopy</sub>
- **Distribution-aligned synthesis** &mdash; *Few-Shot Distribution-Aligned Flow Matching for Data Synthesis in Medical Image Segmentation* &mdash; arXiv, 2026 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; Segmentation datasets</sub>
- **MammoFlow** &mdash; *MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching* &mdash; arXiv, 2026 **[`code`](https://github.com/XYPB/MammoFlow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Mammography</sub>
- **MoGen** &mdash; *MoGen: Detailed Neuronal Morphology Generation via Point Cloud Flow Matching* &mdash; The Fourteenth International Conference on Learning Representations, 2026 `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Neuronal point clouds</sub>
- **STREAM** &mdash; *STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation* &mdash; arXiv, 2026 `code promised`
  <br/><sub>Flow matching &nbsp;|&nbsp; Histopathology</sub>
- **Subclass priors** &mdash; *Flow Matching with Optimized Subclass Priors for Medical Image Augmentation* &mdash; arXiv, 2026 **[`code`](https://github.com/Felix-012/OptPriorFM)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General</sub>
- **WaveDiT** &mdash; *WaveDiT: Distribution-Aware Wavelet Flow Matching for Efficient 3D Brain MRI Synthesis* &mdash; arXiv, 2026 **[`code`](https://github.com/sisinflab/WaveDiT)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Brain MRI, 3D</sub>
- **Landmark-oriented synthesis** &mdash; *Flow matching-based data synthesis for robust anatomical landmark localization* &mdash; IEEE Journal of Biomedical and Health Informatics, 2025 `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Landmark datasets</sub>
- **MOTFM** &mdash; *Flow matching for medical image synthesis: Bridging the gap between speed and quality* &mdash; MICCAI, 2025 **[`code`](https://github.com/milad1378yz/MOTFM)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General, 2D and 3D</sub>
- **RealNVP synthesis** &mdash; *Normalizing flow for synthetic medical images generation* &mdash; IEEE Healthcare Innovations and Point of Care Technologies, 2022 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Chest X-ray, skin lesion</sub>

### Longitudinal, treatment-conditioned, and counterfactual generation

- **In-context priors** &mdash; *Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics* &mdash; arXiv, 2026 **[`code`](https://github.com/SamGijsen/pinc-flows)**
  <br/><sub>Flow matching &nbsp;|&nbsp; fMRI dynamics</sub>
- **OsteoFlow** &mdash; *OsteoFlow: Lyapunov-Guided Flow Distillation for Predicting Bone Remodeling after Mandibular Reconstruction* &mdash; arXiv, 2026 **[`code`](https://github.com/hamidreza-aftabi/OsteoFlow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Mandibular CT</sub>
- **Reversed progression** &mdash; *Vector Quantization for Reversed Disease Progression: Further Investigations* &mdash; MIDL, 2026 `no preprint`
  <br/><sub>Not a flow &nbsp;|&nbsp; Longitudinal imaging</sub>
- **CRONOS** &mdash; *CRONOS: Continuous Time Reconstruction for 4D Medical Longitudinal Series* &mdash; arXiv, 2025 **[`code`](https://github.com/MIC-DKFZ/Longitudinal4DMed)**
  <br/><sub>Flow matching &nbsp;|&nbsp; 4D longitudinal series</sub>
- **Patient-specific dynamics** &mdash; *Learning Patient-Specific Disease Dynamics with Latent Flow Matching for Longitudinal Imaging Generation* &mdash; arXiv, 2025 **[`code`](https://github.com/chqwer2/Delta-LDM-Longitudinal)**
  <br/><sub>Flow matching &nbsp;|&nbsp; Longitudinal imaging</sub>

## Analysis: Classification, Segmentation, Detection

*21 works.*

### Classification

- **Flow-MIL** &mdash; *Flow-MIL: Constructing Highly-expressive Latent Feature Space For Whole Slide Image Classification Using Normalizing Flow* &mdash; ICCV, 2025 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Histopathology</sub>
- **MAGIC-Flow** &mdash; *MAGIC-Flow: Multiscale Adaptive Conditional Flows for Generation and Interpretable Classification* &mdash; arXiv, 2025 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>
- **MedSymmFlow** &mdash; *MedSymmFlow: Bridging Generative Modeling and Classification in Medical Imaging Through Symmetrical Flow Matching* &mdash; MICCAI Workshop on Deep Generative Models, 2025 **[`code`](https://github.com/caetas/MedSymmFlow)**
  <br/><sub>Flow matching &nbsp;|&nbsp; 2D benchmarks</sub>
- **Data-gravity weighting** &mdash; *A weighted flow matching method with data gravity-guided for imbalanced data classification* `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Imbalanced data</sub>

### Detection and localization

- **Landmark prior** &mdash; *Landmark localization from medical images with generative distribution prior* &mdash; IEEE Trans. Medical Imaging, 2024 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>
- **AE-FLOW** &mdash; *AE-FLOW: Autoencoders with normalizing flows for medical images anomaly detection* &mdash; The Eleventh International Conference on Learning Representations, 2023 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>

### Higher-order structural analysis

- **Craniofacial transport** &mdash; *Flow Matching for 3D Craniofacial Skeletal Data Generation* &mdash; MIDL, 2026 `no preprint`
  <br/><sub>Flow matching &nbsp;|&nbsp; Craniofacial</sub>
- **MedPCFM** &mdash; *MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching* &mdash; arXiv, 2026 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; Point clouds</sub>
- **CardiacFlow** &mdash; *CardiacFlow: 3D+ t Four-Chamber Cardiac Shape Completion and Generation via Flow Matching* &mdash; MICCAI, 2025 **[`code`](https://github.com/m-qiang/CardiacFlow)**
  <br/><sub>Rectified flow &nbsp;|&nbsp; Cardiac MR</sub>
- **Invertible brain age** &mdash; *Invertible modeling of bidirectional relationships in neuroimaging with normalizing flows: application to brain aging* &mdash; IEEE Trans. Medical Imaging, 2022 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Brain MRI</sub>

### Segmentation: ambiguity and uncertainty

- **Flow SSN** &mdash; *Flow Stochastic Segmentation Networks* &mdash; ICCV, 2025 **[`code`](https://github.com/biomedia-mira/flow-ssn)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General</sub>
- **Multi-level posterior** &mdash; *A Multi-Level Probabilistic Deep Learning Network Augmented With Normalizing Flow for Ambiguous Medical Image Segmentation* &mdash; IEEE Access, 2025 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>
- **Segmentation bridge** &mdash; *Ambiguous Medical Image Segmentation Using Diffusion Schrödinger Bridge* &mdash; MICCAI, 2025 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; General</sub>
- **Multi-annotator posterior** &mdash; *Improving aleatoric uncertainty quantification in multi-annotated medical image segmentation with normalizing flows* &mdash; International Workshop on Uncertainty for Safe Utilization of Machine Learning in Medical Imaging, 2021 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; Multi-annotated</sub>
- **cFlow Net** &mdash; *Uncertainty quantification in medical image segmentation with normalizing flows* &mdash; International Workshop on Machine Learning in Medical Imaging, 2020 `no code`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>

### Segmentation: continuous mask refinement

- **Semantic bridge** &mdash; *Efficient Breast Cancer Segmentation via Brownian Bridge Diffusion with Semantic Fusion Strategy* &mdash; Pattern Recognition, 2026 `no preprint`
  <br/><sub>Brownian bridge &nbsp;|&nbsp; Breast</sub>
- **FlowSDF** &mdash; *FlowSDF: Flow matching for medical image segmentation using distance transforms* &mdash; International Journal of Computer Vision, 2025 **[`code`](https://github.com/leabogensperger/FlowSDF)**
  <br/><sub>Flow matching &nbsp;|&nbsp; General</sub>
- **PolypFlow** &mdash; *PolypFlow: Reinforcing polyp segmentation with flow-driven dynamics* &mdash; arXiv, 2025 `no code`
  <br/><sub>Flow matching &nbsp;|&nbsp; Endoscopy</sub>

### Segmentation: domain and representation transport

- **MixStyleFlow** &mdash; *MixStyleFlow: Domain Generalization in Medical Image Segmentation Using Normalizing Flows* &mdash; MICCAI, 2025 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; General</sub>
- **Ventricle segmentation** &mdash; *CT-based brain ventricle segmentation via diffusion Schrödinger Bridge without target domain ground truths* &mdash; MICCAI, 2024 `no preprint`
  <br/><sub>Schrodinger bridge &nbsp;|&nbsp; MRI $\rightarrow$ CT</sub>
- **Pancreas generalization** &mdash; *Generalizable pancreas segmentation modeling in CT imaging via meta-learning and latent-space feature flow generation* &mdash; IEEE Journal of Biomedical and Health Informatics, 2022 `no preprint`
  <br/><sub>Normalizing flow &nbsp;|&nbsp; CT</sub>

## Implementations

The 34 works that publish a repository, grouped by the transport they learn.

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
| NFE | `###` 5 |
| F1 | `###` 5 |
| AUC | `###` 5 |
| Accuracy | `###` 5 |
| NRMSE | `##` 4 |

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

