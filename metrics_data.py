# -*- coding: utf-8 -*-
"""Evaluation metrics each reviewed work reports, read from its arXiv full text.

Read on 2026-09-04. One entry per work whose full text could be read; the key is the
arXiv id, matching code_data.py. Only metrics the paper uses to evaluate its OWN
results are recorded -- not loss functions, and not metrics it cites others as using.

Two boundaries were fixed by calibration before any of this was collected, both of
which had already produced a wrong answer:

  Abstracts do not carry this. Of twelve abstracts scanned for named datasets, two
  named one; metrics fare no better. The full text is the only source.

  "External validation" is NOT recorded here, deliberately. A loose reading of
  "evaluated on an independent dataset" returned yes for two works in a row, which
  would have contradicted fig:ladder's claim that no reviewed work reports it. Asked
  precisely -- is a model trained on one site or dataset evaluated on a different one --
  both turned out to be no: each dataset was trained and tested separately. Deciding
  that reliably takes two or three careful passes per paper, and a loose one produces
  false positives against the paper's central claim. It is left unmeasured rather than
  measured badly.
"""

METRICS = {
    "2006.02683": ["Dice", "GED", "CLL"],
    "2006.06270": ["PSNR", "SSIM"],
    "2108.02155": ["GED", "IoU", "Dice"],
    "2112.13110": ["PSNR", "SSIM"],
    "2301.11551": ["DSC", "HD"],
    "2305.10732": ["PSNR", "SSIM", "IoU"],
    "2306.10689": ["PSNR", "SSIM", "VIF", "UQI"],
    "2309.04856": ["FID", "RMSE", "SSIM"],
    "2402.08159": ["LPIPS", "SSIM", "PSNR", "NFE"],
    "2405.18087": ["F1", "mIoU"],
    "2407.05059": ["NRMSE", "PSNR", "SSIM"],
    "2410.17543": ["PSNR", "SSIM"],
    "2410.19288": ["NRMSE", "PSNR", "SSIM", "LPIPS", "NFE"],
    "2410.20073": ["SSIM", "SBP"],
    "2411.14269": ["NRMSE", "PSNR", "SSIM"],
    "2502.12742": ["SSIM", "PSNR", "ASSD"],
    "2502.19037": ["Dice", "IoU", "wFbeta", "Smeasure", "Emeasure", "MAE"],
    "2503.00266": ["FID", "SSIM", "KID", "CMMD", "IS", "3D-FID", "MS-SSIM", "MMD", "PSNR", "SNR", "Accuracy", "F1", "Dice", "IoU", "HD", "ASD"],
    "2504.01004": ["SSIM", "PSNR", "FID", "R2"],
    "2505.04963": ["FID", "MFID", "Dice", "HD95", "PSNR", "SSIM"],
    "2505.22511": ["ChamferDistance", "IoU", "NMAE", "Pearson", "R2", "MPD", "BlandAltman"],
    "2505.24687": ["FID", "Dice", "NSD"],
    "2507.11025": ["RMSE", "SSIM", "LPIPS", "Dice", "ARR", "ARSR", "NFE"],
    "2507.18838": ["Dice", "IoU", "HD95"],
    "2507.19098": ["AUC", "Accuracy"],
    "2508.11211": ["RMSE", "PSNR", "SSIM"],
    "2508.12900": ["FID", "FVD", "CLIP", "IS"],
    "2509.05754": ["Dice", "HD95", "vFID", "cycleDice"],
    "2510.04823": ["MAE", "PSNR", "MS-SSIM", "Dice", "HD95"],
    "2510.12408": ["PSNR", "SSIM", "LPIPS"],
    "2510.22070": ["FID", "FIDRad", "KIDRad", "FIDSwAV", "Precision", "Recall", "Density", "Coverage", "MS-SSIM", "Accuracy", "bAcc", "AUC"],
    "2511.20152": ["LPIPS", "SSIM", "PSNR"],
    "2512.09185": ["PSNR", "SSIM", "MAE", "RMAE", "RegionMAE"],
    "2512.16577": ["NRMSE", "SSIM", "PSNR"],
    "2601.15884": ["PSNR", "SSIM", "LPIPS", "FID", "KID", "Dice"],
    "2601.19498": ["PSNR", "SSIM", "ASSD", "MR-SSIM", "Dice"],
    "2602.21536": ["RMSE", "MS-SSIM", "LPIPS", "PSNR", "FA", "NDI", "ODI"],
    "2603.00205": ["PSNR", "SSIM", "LPIPS", "NFE", "DataFidelity"],
    "2603.00535": ["MAE", "SSIM", "PSNR", "FID", "SegScore"],
    "2603.03710": ["PSNR", "SSIM", "LPIPS", "SHAFE", "Dice"],
    "2603.05796": ["MAE", "PSNR", "NCC"],
    "2603.13967": ["FID", "FVD", "SSIM", "LPIPS", "R2", "MAE", "RMSE", "Dice"],
    "2603.16392": ["Accuracy", "AUC"],
    "2603.18513": ["PSNR", "SSIM", "LPIPS", "GFLOPs", "Precision", "Recall", "F1", "IoU", "mIoU"],
    "2603.22421": ["Dice", "MS-SSIM", "MAE"],
    "2604.02868": ["FID", "KID", "LPIPS", "SSIM", "PSNR", "Dice", "IoU"],
    "2604.15459": ["PSNR", "SSIM", "RMSE", "LPIPS"],
    "2604.21146": ["PSNR", "SSIM"],
    "2605.16469": ["FID", "IRS", "bAcc", "F1"],
    "2605.26423": ["PSD", "FCsim", "cFID", "MAE", "P@5", "Accuracy", "F1", "AUC", "Sensitivity"],
    "2606.07036": ["FID", "KID", "CMMD", "LPIPS", "FVD", "KVD", "vMMD"],
    "2606.08670": ["FID", "MMD", "MS-SSIM", "BAP", "iMAE", "KLD", "Dice"],
    "2606.11833": ["Pearson", "SplitHalfReliability", "FCcorrelation"],
    "2606.18876": ["Dice", "FID"],
    "2606.24313": ["SSIM", "PSNR", "DSC", "HD95"],
    "2606.24433": ["ChamferDistance", "Dice", "bDice", "HD95"],
    "2606.28537": ["FID", "FrD", "EMD", "JSD", "AUC"],
    "2607.11104": ["SSIM", "PSNR", "RMSE"],
    "2607.16649": ["PSNR", "SSIM", "LPIPS", "NFE", "NIQE", "BRISQUE"],
}
