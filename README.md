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

<details>
<summary>Data Structure</summary>

Complete Folder Structure After Downloading All Datasets

```
project_root/
│
├── download_all_datasets.py # Main downloader script
├── quick_download.py # Quick download presets
├── example_usage.py # Usage examples
├── dataset_info.py # Dataset information
├── README.md # Documentation
│
└── datasets/ # Base directory for all datasets
│
├── dataset_summary.json # Auto-generated summary file
│
├── DIV2K/ # DIV2K Dataset (~3.5GB)
│ ├── DIV2K_train_HR/ # Training images (800 images)
│ │ ├── 0001.png
│ │ ├── 0002.png
│ │ ├── ...
│ │ └── 0800.png
│ │
│ └── DIV2K_valid_HR/ # Validation images (100 images)
│ ├── 0801.png
│ ├── 0802.png
│ ├── ...
│ └── 0900.png
│
├── Set12/ # Set12 Benchmark (~10MB)
│ ├── 01.png
│ ├── 02.png
│ ├── 03.png
│ ├── 04.png
│ ├── 05.png
│ ├── 06.png
│ ├── 07.png
│ ├── 08.png
│ ├── 09.png
│ ├── 10.png
│ ├── 11.png
│ └── 12.png
│
├── Set14/ # Set14 Benchmark (~10MB)
│ ├── baboon.bmp
│ ├── barbara.bmp
│ ├── bridge.bmp
│ ├── coastguard.bmp
│ ├── comic.bmp
│ ├── face.bmp
│ ├── flowers.bmp
│ ├── foreman.bmp
│ ├── lenna.bmp
│ ├── man.bmp
│ ├── monarch.bmp
│ ├── pepper.bmp
│ ├── ppt3.bmp
│ └── zebra.bmp
│
├── BSD68/ # BSD68 Benchmark (~20MB)
│ ├── test001.png # Grayscale images
│ ├── test002.png
│ ├── test003.png
│ ├── ...
│ └── test068.png
│
├── Urban100/ # Urban100 Benchmark (~50MB)
│ ├── img_001.png
│ ├── img_002.png
│ ├── img_003.png
│ ├── ...
│ └── img_100.png
│
├── SIDD/ # Smartphone Image Denoising Dataset
│ │
│ ├── SIDD_Small_sRGB_Only/ # Small version (~2GB)
│ │ ├── Data/
│ │ │ ├── 0001_001_S6_00100_00060_3200_L/
│ │ │ │ ├── 0001_NOISY_SRGB_010.PNG
│ │ │ │ ├── 0001_GT_SRGB_010.PNG
│ │ │ │ ├── 0001_NOISY_SRGB_011.PNG
│ │ │ │ ├── 0001_GT_SRGB_011.PNG
│ │ │ │ └── ...
│ │ │ │
│ │ │ ├── 0001_001_S6_00100_00060_3200_N/
│ │ │ │ └── ...
│ │ │ │
│ │ │ └── ... (multiple scene folders)
│ │ │
│ │ └── Scene_Instances.txt
│ │
│ └── SIDD_Medium_sRGB/ # Medium version (~12GB)
│ ├── Data/
│ │ ├── 0001_001_S6_00100_00060_3200_L/
│ │ ├── 0001_001_S6_00100_00060_3200_N/
│ │ └── ... (more scenes)
│ │
│ └── Scene_Instances.txt
│
├── DND/ # Darmstadt Noise Dataset (~3.3GB)
│ └── dnd_2017.mat # MATLAB format file
│
├── COCO2017/ # COCO Dataset
│ │
│ ├── train2017/ # Training images (~18GB, 118,287 images)
│ │ ├── 000000000009.jpg
│ │ ├── 000000000025.jpg
│ │ ├── 000000000030.jpg
│ │ ├── ...
│ │ └── 000000581921.jpg
│ │
│ ├── val2017/ # Validation images (~1GB, 5,000 images)
│ │ ├── 000000000139.jpg
│ │ ├── 000000000285.jpg
│ │ ├── 000000000632.jpg
│ │ ├── ...
│ │ └── 000000581781.jpg
│ │
│ └── annotations/ # Annotation files
│ ├── instances_train2017.json
│ ├── instances_val2017.json
│ ├── captions_train2017.json
│ ├── captions_val2017.json
│ ├── person_keypoints_train2017.json
│ └── person_keypoints_val2017.json
│
├── TinyImageNet/ # Tiny ImageNet (~237MB)
│ └── tiny-imagenet-200/
│ ├── train/ # Training data (200 classes)
│ │ ├── n01443537/ # Class folder
│ │ │ ├── images/
│ │ │ │ ├── n01443537_0.JPEG
│ │ │ │ ├── n01443537_1.JPEG
│ │ │ │ └── ...
│ │ │ └── n01443537_boxes.txt
│ │ │
│ │ ├── n01629819/
│ │ └── ... (200 classes)
│ │
│ ├── val/ # Validation data
│ │ ├── images/
│ │ │ ├── val_0.JPEG
│ │ │ ├── val_1.JPEG
│ │ │ └── ... (10,000 images)
│ │ └── val_annotations.txt
│ │
│ ├── test/ # Test data
│ │ └── images/
│ │ ├── test_0.JPEG
│ │ └── ... (10,000 images)
│ │
│ ├── wnids.txt # Class IDs
│ └── words.txt # Class names
│
└── ImageNet/ # ImageNet (manual download required)
└── ILSVRC2012/
├── train/ # Training data (~138GB, 1.2M images)
│ ├── n01440764/ # Class folders (1000 classes)
│ │ ├── n01440764_10026.JPEG
│ │ ├── n01440764_10027.JPEG
│ │ └── ...
│ │
│ ├── n01443537/
│ └── ... (1000 classes)
│
└── val/ # Validation data (~6.3GB, 50K images)
├── ILSVRC2012_val_00000001.JPEG
├── ILSVRC2012_val_00000002.JPEG
└── ... (50,000 images)
```

</details>

## Useage

#### Case 1: Training a Denoising Model

```python
from src.dataset.download import DatasetDownloader

downloader = DatasetDownloader()

# Download training data
print("Downloading training data...")
downloader.download_div2k(include_val=True)

# Download multiple test sets
print("Downloading test sets...")
downloader.download_set12()
downloader.download_bsd68()

print("Setup complete! Start training with:")
print("  Training: datasets/DIV2K/DIV2K_train_HR/")
print("  Validation: datasets/DIV2K/DIV2K_valid_HR/")
print("  Test: datasets/Set12/, datasets/BSD68/")
```

#### Case 2: Reproducing Paper Results

```python
from src.dataset.download import DatasetDownloader

downloader = DatasetDownloader()

# Download all standard benchmarks
benchmarks = [
    downloader.download_set12,
    downloader.download_set14,
    downloader.download_bsd68,
    downloader.download_urban100
]

for download_func in benchmarks:
    download_func()

# For real-world noise experiments
downloader.download_sidd(subset='small')
downloader.download_dnd()

downloader.generate_summary()
```

#### Case 3: Quick Testing

```bash
# Use the quick download script
python quick_download.py

# Select option 2: Benchmark datasets
# Downloads Set12, Set14, BSD68, Urban100 (~100MB)
```

## Contributing

### Adding New Datasets

To add a new dataset:

1. Add download method to DatasetDownloader class:

```python
def download_new_dataset(self):
    """Download new dataset"""
    new_dir = self.base_dir / 'NewDataset'
    new_dir.mkdir(exist_ok=True)

    url = 'https://example.com/dataset.zip'
    zip_path = new_dir / 'dataset.zip'

    if self.download_file(url, zip_path, "New Dataset"):
        self.extract_zip(zip_path, new_dir)
        zip_path.unlink()
        print(f"✓ New dataset saved to: {new_dir}")
```

2. Add to menu in main() function

3. Update README with dataset information
