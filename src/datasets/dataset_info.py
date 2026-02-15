DATASET_INFO = {
    "DIV2K": {
        "name": "DIV2K",
        "full_name": "DIVerse 2K resolution high quality images",
        "images": 1000,
        "train": 800,
        "val": 100,
        "test": 100,
        "resolution": "2K (2048×1080)",
        "size_gb": 3.5,
        "use_case": "Training for super-resolution and denoising",
        "noise_type": "Synthetic",
        "url": "https://data.vision.ee.ethz.ch/cvl/DIV2K/",
    },
    "Set12": {
        "name": "Set12",
        "full_name": "Standard Test Set 12",
        "images": 12,
        "size_gb": 0.01,
        "use_case": "Quick evaluation",
        "noise_type": "Synthetic",
        "url": "https://github.com/cszn/DnCNN",
    },
    "Set14": {
        "name": "Set14",
        "full_name": "Standard Test Set 14",
        "images": 14,
        "size_gb": 0.01,
        "use_case": "Standard benchmark",
        "noise_type": "Synthetic",
        "url": "https://github.com/jbhuang04/SRCNN",
    },
    "BSD68": {
        "name": "BSD68",
        "full_name": "Berkeley Segmentation Dataset 68",
        "images": 68,
        "color": "Grayscale",
        "size_gb": 0.02,
        "use_case": "Grayscale denoising benchmark",
        "noise_type": "Synthetic",
        "url": "https://github.com/clausmichele/CBSD68",
    },
    "Urban100": {
        "name": "Urban100",
        "full_name": "Urban Scenes 100",
        "images": 100,
        "size_gb": 0.05,
        "use_case": "Challenging structures and edges",
        "noise_type": "Synthetic",
        "url": "https://github.com/jbhuang0604/SelfExSR",
    },
    "COCO": {
        "name": "COCO",
        "full_name": "Common Objects in Context",
        "images": "330K+",
        "train": "118K",
        "val": "5K",
        "size_gb": 18,
        "use_case": "Large-scale training",
        "categories": 80,
        "url": "https://cocodataset.org/",
    },
    "SIDD": {
        "name": "SIDD",
        "full_name": "Smartphone Image Denoising Dataset",
        "images": "30K+",
        "small": "320 pairs",
        "medium": "3200 pairs",
        "size_gb": 12,
        "use_case": "Real-world smartphone noise",
        "noise_type": "Real",
        "paired": True,
        "url": "https://www.eecs.yorku.ca/~kamel/sidd/",
    },
    "DND": {
        "name": "DND",
        "full_name": "Darmstadt Noise Dataset",
        "images": 50,
        "size_gb": 3.3,
        "use_case": "Real-world noise benchmark",
        "noise_type": "Real",
        "ground_truth": "Not public (online evaluation)",
        "url": "https://noise.visinf.tu-darmstadt.de/",
    },
    "ImageNet": {
        "name": "ImageNet",
        "full_name": "ImageNet Large Scale Visual Recognition Challenge",
        "images": "14M+",
        "classes": 1000,
        "size_gb": 150,
        "use_case": "Pre-training, transfer learning",
        "registration": True,
        "url": "https://image-net.org/",
    },
}


def print_dataset_info(dataset_name: str | None = None) -> None:
    """Print information about datasets."""
    if dataset_name:
        if dataset_name in DATASET_INFO:
            info = DATASET_INFO[dataset_name]
            print(f"\n{'=' * 60}")
            print(f"Dataset: {info['name']}")
            print(f"{'=' * 60}")
            for key, value in info.items():
                if key != "name":
                    print(f"{key.replace('_', ' ').title()}: {value}")
        else:
            print(f"Dataset '{dataset_name}' not found")
    else:
        # Print all datasets
        print("\n" + "=" * 60)
        print("Available Datasets Summary")
        print("=" * 60)
        for name, info in DATASET_INFO.items():
            print(f"\n{name}:")
            print(f"  Full name: {info.get('full_name', 'N/A')}")
            print(f"  Images: {info.get('images', 'N/A')}")
            print(f"  Size: {info.get('size_gb', 'N/A')} GB")
            print(f"  Use case: {info.get('use_case', 'N/A')}")
            print(f"  URL: {info.get('url', 'N/A')}")


if __name__ == "__main__":
    print_dataset_info()
