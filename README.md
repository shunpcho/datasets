# Image Denoising Dataset Downloader

A comprehensive Python tool for downloading and managing popular datasets used in image denoising research.

## Features

- 🚀 **Easy to use** - Simple command-line interface or Python API
- 📦 **Multiple datasets** - Support for 9+ popular denoising datasets
- 📊 **Automatic organization** - Creates well-structured dataset directories
- 📈 **Progress tracking** - Real-time download progress indicators
- 💾 **Smart extraction** - Automatic archive extraction and cleanup
- 📋 **Summary generation** - Creates JSON summaries of downloaded datasets

## Supported Datasets

### Training Datasets

| Dataset   | Images                  | Size   | Type      | Description                            |
| --------- | ----------------------- | ------ | --------- | -------------------------------------- |
| **DIV2K** | 800 (train) + 100 (val) | 3.5GB  | Synthetic | High-resolution 2K images for training |
| **COCO**  | 118K (train)            | 18GB   | Synthetic | Large-scale natural images             |
| **SIDD**  | 30K+ pairs              | 2-12GB | Real      | Smartphone real-world noise pairs      |

### Benchmark Datasets

| Dataset      | Images | Size  | Type      | Description                          |
| ------------ | ------ | ----- | --------- | ------------------------------------ |
| **Set12**    | 12     | <10MB | Synthetic | Standard quick test set              |
| **Set14**    | 14     | <10MB | Synthetic | Classic benchmark images             |
| **BSD68**    | 68     | <20MB | Synthetic | Grayscale benchmark                  |
| **Urban100** | 100    | ~50MB | Synthetic | Complex structures and edges         |
| **DND**      | 50     | 3.3GB | Real      | Real-world noise (online evaluation) |

### Pre-training Datasets

| Dataset           | Images | Size  | Type | Description                   |
| ----------------- | ------ | ----- | ---- | ----------------------------- |
| **ImageNet**      | 1.4M+  | 150GB | -    | Requires manual registration  |
| **Tiny ImageNet** | 100K   | 237MB | -    | Small alternative to ImageNet |
