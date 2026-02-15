"""
Image Denoising Dataset Downloader
==================================
Downloads and manages popular datasets for image denoising research:
- DIV2K, Set12, Set14, BSD68, Urban100 (synthetic noise)
- SIDD, DND (real-world noise)
- COCO, ImageNet (large-scale training)

Usage:
    python download_all_datasets.py
    
Or use as a module:
    from download_all_datasets import DatasetDownloader
    downloader = DatasetDownloader(base_dir='./datasets')
    downloader.download_div2k()
"""

import os
import urllib.request
import zipfile
import tarfile
import shutil
from pathlib import Path
import json

class DatasetDownloader:
    """Main class for downloading and managing image denoising datasets"""
    
    def __init__(self, base_dir: str | Path ='./datasets') -> None:
        """
        Initialize the downloader
        
        Args:
            base_dir (str | Path): Base directory to save all datasets
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        
    def download_file(self, url: str, save_path: Path, desc: str ="") -> bool:
        """
        Download a file with progress bar
        
        Args:
            url (str): URL to download from
            save_path (Path): Path to save the downloaded file
            desc (str): Description of the file being downloaded
            
        Returns:
            bool: True if download successful, False otherwise
        """
        print(f"Downloading {desc}...")
        print(f"URL: {url}")
        
        try:
            def progress_hook(block_num: int, block_size: int, total_size: int) -> None:
                """Display download progress"""
                downloaded = block_num * block_size
                if total_size > 0:
                    percent = min(downloaded * 100.0 / total_size, 100)
                    print(f"\rProgress: {percent:.1f}% ({downloaded / 1e9:.2f}GB / {total_size / 1e9:.2f}GB)", end='')
            
            urllib.request.urlretrieve(url, save_path, progress_hook)
            print(f"\n✓ Downloaded: {save_path}")
            return True
        except Exception as e:
            print(f"\n✗ Error downloading {desc}: {e}")
            return False
    
    def extract_zip(self, zip_path: Path, extract_to: Path) -> None:
        """
        Extract a zip file
        
        Args:
            zip_path (Path): Path to the zip file
            extract_to (Path): Directory to extract to
        """
        print(f"Extracting {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print("✓ Extraction complete")
    
    def extract_tar(self, tar_path: Path, extract_to: Path) -> None:
        """
        Extract a tar file
        
        Args:
            tar_path (Path): Path to the tar file
            extract_to (Path): Directory to extract to
        """
        print(f"Extracting {tar_path}...")
        with tarfile.open(tar_path, 'r') as tar_ref:
            tar_ref.extractall(extract_to)
        print("✓ Extraction complete")
    
    # 1. DIV2K Dataset
    def download_div2k(self, include_val: bool = True) -> None:
        """
        Download DIV2K dataset
        
        Dataset info:
            - 1000 high-resolution images (2K resolution)
            - Train: 800 images, Validation: 100 images, Test: 100 images
            - Used for super-resolution and denoising
            - Size: ~3.5GB (train), ~400MB (val)
            
        Args:
            include_val (bool): Whether to download validation set
        """
        print("\n" + "="*60)
        print("DIV2K Dataset")
        print("="*60)
        
        div2k_dir = self.base_dir / 'DIV2K'
        div2k_dir.mkdir(exist_ok=True)
        
        # Training set (800 images)
        train_url = 'http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip'
        train_zip = div2k_dir / 'DIV2K_train_HR.zip'
        
        if self.download_file(train_url, train_zip, "DIV2K Training Set (3.5GB)"):
            self.extract_zip(train_zip, div2k_dir)
            train_zip.unlink()
        
        # Validation set (100 images)
        if include_val:
            val_url = 'http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_valid_HR.zip'
            val_zip = div2k_dir / 'DIV2K_valid_HR.zip'
            
            if self.download_file(val_url, val_zip, "DIV2K Validation Set"):
                self.extract_zip(val_zip, div2k_dir)
                val_zip.unlink()
        
        print(f"✓ DIV2K saved to: {div2k_dir}")
    
    # 2. Set12 Dataset
    def download_set12(self) -> None:
        """
        Download Set12 dataset
        
        Dataset info:
            - 12 standard test images
            - Used for quick evaluation
            - Classic benchmark for denoising
            - Size: <10MB
        """
        print("\n" + "="*60)
        print("Set12 Dataset")
        print("="*60)
        
        set12_dir = self.base_dir / 'Set12'
        set12_dir.mkdir(exist_ok=True)
        
        base_url = 'https://github.com/cszn/DnCNN/raw/master/testsets/Set12'
        
        for i in range(1, 13):
            img_name = f'{i:02d}.png'
            url = f'{base_url}/{img_name}'
            save_path = set12_dir / img_name
            self.download_file(url, save_path, f"Set12 image {i}/12")
        
        print(f"✓ Set12 saved to: {set12_dir}")
    
    # 3. Set14 Dataset
    def download_set14(self) -> None:
        """
        Download Set14 dataset
        
        Dataset info:
            - 14 standard test images
            - Classic images like 'barbara', 'lenna', 'baboon'
            - Used for super-resolution and denoising evaluation
            - Size: <10MB
        """
        print("\n" + "="*60)
        print("Set14 Dataset")
        print("="*60)
        
        set14_dir = self.base_dir / 'Set14'
        set14_dir.mkdir(exist_ok=True)
        
        # List of Set14 image names
        image_names = [
            'baboon', 'barbara', 'bridge', 'coastguard', 
            'comic', 'face', 'flowers', 'foreman',
            'lenna', 'man', 'monarch', 'pepper',
            'ppt3', 'zebra'
        ]
        
        base_url = 'https://github.com/jbhuang04/SRCNN/raw/master/Test/Set14'
        
        for name in image_names:
            url = f'{base_url}/{name}.bmp'
            save_path = set14_dir / f'{name}.bmp'
            self.download_file(url, save_path, f"Set14: {name}")
        
        print(f"✓ Set14 saved to: {set14_dir}")
    
    # 4. BSD68 Dataset
    def download_bsd68(self) -> None:
        """
        Download BSD68 dataset
        
        Dataset info:
            - 68 grayscale images from Berkeley Segmentation Dataset
            - Standard benchmark for grayscale denoising
            - Used in many classical denoising papers
            - Size: <20MB
        """
        print("\n" + "="*60)
        print("BSD68 Dataset")
        print("="*60)
        
        bsd68_dir = self.base_dir / 'BSD68'
        bsd68_dir.mkdir(exist_ok=True)
        
        url = 'https://github.com/clausmichele/CBSD68/archive/refs/heads/master.zip'
        zip_path = self.base_dir / 'bsd68_temp.zip'
        
        if self.download_file(url, zip_path, "BSD68"):
            self.extract_zip(zip_path, self.base_dir / 'temp_bsd68')
            
            # Move image files to target directory
            source_dir = self.base_dir / 'temp_bsd68' / 'CBSD68-master' / 'CBSD68'
            for img_file in source_dir.glob('*.png'):
                shutil.move(str(img_file), str(bsd68_dir / img_file.name))
            
            # Cleanup temporary files
            zip_path.unlink()
            shutil.rmtree(self.base_dir / 'temp_bsd68')
            
            print(f"✓ BSD68 saved to: {bsd68_dir}")
    
    # 5. Urban100 Dataset
    def download_urban100(self) -> None:
        """
        Download Urban100 dataset
        
        Dataset info:
            - 100 high-resolution urban scene images
            - Contains complex structures and edges
            - Challenging for denoising and super-resolution
            - Size: ~50MB
        """
        print("\n" + "="*60)
        print("Urban100 Dataset")
        print("="*60)
        
        urban100_dir = self.base_dir / 'Urban100'
        urban100_dir.mkdir(exist_ok=True)
        
        url = 'https://github.com/jbhuang0604/SelfExSR/raw/master/data/Urban100.zip'
        zip_path = self.base_dir / 'urban100.zip'
        
        if self.download_file(url, zip_path, "Urban100"):
            self.extract_zip(zip_path, self.base_dir)
            
            # Organize files if needed
            extracted_dir = self.base_dir / 'Urban100'
            if extracted_dir.exists() and extracted_dir != urban100_dir:
                shutil.rmtree(urban100_dir)
                shutil.move(str(extracted_dir), str(urban100_dir))
            
            zip_path.unlink()
            print(f"✓ Urban100 saved to: {urban100_dir}")
    
    # 6. COCO Dataset
    def download_coco(self, year: int = 2017, split: str = 'train') -> None:
        """
        Download COCO dataset
        
        Dataset info:
            - 330,000+ images with 80 object categories
            - Used for large-scale training
            - Train: ~118K images (18GB), Val: ~5K images (1GB)
            - Includes annotations for object detection
            
        Args:
            year (int): Dataset year (2014 or 2017)
            split (str): 'train' or 'val'
        """
        print("\n" + "="*60)
        print(f"COCO {year} {split} Dataset")
        print("="*60)
        
        coco_dir = self.base_dir / f'COCO{year}'
        coco_dir.mkdir(exist_ok=True)
        
        # Image URLs
        if split == 'train':
            url = f'http://images.cocodataset.org/zips/train{year}.zip'
            size_info = "18GB"
        elif split == 'val':
            url = f'http://images.cocodataset.org/zips/val{year}.zip'
            size_info = "1GB"
        else:
            print(f"Unknown split: {split}")
            return
        
        zip_path = coco_dir / f'{split}{year}.zip'
        
        print(f"Warning: This will download approximately {size_info}")
        if self.download_file(url, zip_path, f"COCO {year} {split} ({size_info})"):
            self.extract_zip(zip_path, coco_dir)
            zip_path.unlink()
            print(f"✓ COCO {year} {split} saved to: {coco_dir}")
        
        # Download annotations
        anno_url = f'http://images.cocodataset.org/annotations/annotations_trainval{year}.zip'
        anno_zip = coco_dir / 'annotations.zip'
        
        if self.download_file(anno_url, anno_zip, "COCO annotations"):
            self.extract_zip(anno_zip, coco_dir)
            anno_zip.unlink()
    
    # 7. SIDD Dataset
    def download_sidd(self, subset: str ='small') -> None:
        """
        Download SIDD (Smartphone Image Denoising Dataset)
        
        Dataset info:
            - Real-world noise from smartphone cameras
            - Contains clean-noisy image pairs
            - Small: 320 image pairs (2GB)
            - Medium: 3,200 image pairs (12GB)
            - Full: 30,000+ image pairs (requires manual download)
            
        Args:
            subset (str): 'small' or 'medium'
        """
        print("\n" + "="*60)
        print(f"SIDD Dataset ({subset})")
        print("="*60)
        
        sidd_dir = self.base_dir / 'SIDD'
        sidd_dir.mkdir(exist_ok=True)
        
        if subset == 'small':
            # SIDD Small (~2GB, for benchmarking)
            url = 'https://www.eecs.yorku.ca/~kamel/sidd/dataset/SIDD_Small_sRGB_Only.zip'
            zip_path = sidd_dir / 'SIDD_Small.zip'
            size_info = "2GB"
        elif subset == 'medium':
            # SIDD Medium (~12GB)
            url = 'https://www.eecs.yorku.ca/~kamel/sidd/dataset/SIDD_Medium_sRGB.zip'
            zip_path = sidd_dir / 'SIDD_Medium.zip'
            size_info = "12GB"
        else:
            print("Available subsets: 'small' (2GB), 'medium' (12GB)")
            print("Full dataset requires manual download from: https://www.eecs.yorku.ca/~kamel/sidd/dataset.php")
            return
        
        print(f"Warning: This will download approximately {size_info}")
        if self.download_file(url, zip_path, f"SIDD {subset} ({size_info})"):
            self.extract_zip(zip_path, sidd_dir)
            zip_path.unlink()
            print(f"✓ SIDD {subset} saved to: {sidd_dir}")
    
    # 8. DND Dataset
    def download_dnd(self) -> None:
        """
        Download DND (Darmstadt Noise Dataset)
        
        Dataset info:
            - 50 real-world noisy images
            - Ground truth not publicly available
            - Online benchmark for evaluation
            - Size: 3.3GB
            
        Note:
            To evaluate on DND, submit results to:
            https://noise.visinf.tu-darmstadt.de/benchmark/
        """
        print("\n" + "="*60)
        print("DND Dataset")
        print("="*60)
        
        dnd_dir = self.base_dir / 'DND'
        dnd_dir.mkdir(exist_ok=True)
        
        # DND download link
        url = 'https://noise.visinf.tu-darmstadt.de/downloads/dnd_2017.mat'
        mat_path = dnd_dir / 'dnd_2017.mat'
        
        print("Note: DND ground truth is not publicly available.")
        print("You need to submit results to their online benchmark:")
        print("https://noise.visinf.tu-darmstadt.de/benchmark/")
        
        if self.download_file(url, mat_path, "DND dataset (3.3GB)"):
            print(f"✓ DND saved to: {dnd_dir}")
            print("\nTo load DND in Python:")
            print("  import scipy.io")
            print("  data = scipy.io.loadmat('dnd_2017.mat')")
    
    # 9. ImageNet (instructions only)
    def download_imagenet_info(self) -> None:
        """
        Display ImageNet download instructions
        
        Dataset info:
            - 14+ million images, 1000 classes
            - ILSVRC2012: Train 138GB, Val 6.3GB
            - Requires registration
            - Used for pre-training and transfer learning
        """
        print("\n" + "="*60)
        print("ImageNet Dataset")
        print("="*60)
        
        info = """
ImageNet requires registration and cannot be automatically downloaded.

Download steps:
1. Visit https://image-net.org/download.php
2. Register an account (explain research purpose)
3. Download ILSVRC2012:
   - Training images (ILSVRC2012_img_train.tar, 138GB)
   - Validation images (ILSVRC2012_img_val.tar, 6.3GB)

Alternative options:
- TensorFlow Datasets: tensorflow_datasets.load('imagenet2012')
- PyTorch: torchvision.datasets.ImageNet(root='./data', split='train')
  (Note: requires pre-downloaded files)

Smaller alternative:
- ImageNet-1K mini (subset)
- Tiny ImageNet (200 classes, 100K images)
  URL: http://cs231n.stanford.edu/tiny-imagenet-200.zip
"""
        print(info)
        
        # Option to download Tiny ImageNet
        response = input("\nDownload Tiny ImageNet instead? (y/n): ")
        if response.lower() == 'y':
            self.download_tiny_imagenet()
    
    def download_tiny_imagenet(self) -> None:
        """
        Download Tiny ImageNet
        
        Dataset info:
            - 200 classes, 100,000 images
            - 64x64 resolution
            - Subset of ImageNet
            - Size: 237MB
        """
        print("\nDownloading Tiny ImageNet...")
        
        tiny_dir = self.base_dir / 'TinyImageNet'
        tiny_dir.mkdir(exist_ok=True)
        
        url = 'http://cs231n.stanford.edu/tiny-imagenet-200.zip'
        zip_path = self.base_dir / 'tiny-imagenet-200.zip'
        
        if self.download_file(url, zip_path, "Tiny ImageNet (237MB)"):
            self.extract_zip(zip_path, tiny_dir)
            zip_path.unlink()
            print(f"✓ Tiny ImageNet saved to: {tiny_dir}")
    
    # Generate summary
    def generate_summary(self) -> None:
        """
        Generate a summary of downloaded datasets
        
        Creates a JSON file with:
            - Number of files in each dataset
            - Total size of each dataset
        """
        print("\n" + "="*60)
        print("Dataset Summary")
        print("="*60)
        
        summary = {}
        for dataset_dir in self.base_dir.iterdir():
            if dataset_dir.is_dir():
                # Count files
                file_count = sum(1 for _ in dataset_dir.rglob('*') if _.is_file())
                # Calculate total size
                total_size = sum(f.stat().st_size for f in dataset_dir.rglob('*') if f.is_file())
                
                summary[dataset_dir.name] = {
                    'files': file_count,
                    'size_gb': total_size / 1e9
                }
        
        # Display summary
        print(f"\n{'Dataset':<20} {'Files':<10} {'Size (GB)':<10}")
        print("-" * 40)
        for name, info in sorted(summary.items()):
            print(f"{name:<20} {info['files']:<10} {info['size_gb']:<10.2f}")
        
        # Save as JSON
        summary_path = self.base_dir / 'dataset_summary.json'
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"\n✓ Summary saved to: {summary_path}")


def main():
    """Main function - Interactive dataset downloader"""
    downloader = DatasetDownloader(base_dir='./datasets')
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║   Image Denoising Dataset Downloader                     ║
    ╚══════════════════════════════════════════════════════════╝
    
    Available datasets:
    1.  DIV2K (train + validation)
    2.  Set12
    3.  Set14
    4.  BSD68
    5.  Urban100
    6.  COCO 2017 (train)
    7.  COCO 2017 (val)
    8.  SIDD (small)
    9.  SIDD (medium)
    10. DND
    11. ImageNet (info only)
    12. All (small datasets only - recommended for quick start)
    13. Custom selection
    """)
    
    choice = input("Select option (1-13): ").strip()
    
    if choice == '1':
        downloader.download_div2k(include_val=True)
    elif choice == '2':
        downloader.download_set12()
    elif choice == '3':
        downloader.download_set14()
    elif choice == '4':
        downloader.download_bsd68()
    elif choice == '5':
        downloader.download_urban100()
    elif choice == '6':
        downloader.download_coco(year=2017, split='train')
    elif choice == '7':
        downloader.download_coco(year=2017, split='val')
    elif choice == '8':
        downloader.download_sidd(subset='small')
    elif choice == '9':
        downloader.download_sidd(subset='medium')
    elif choice == '10':
        downloader.download_dnd()
    elif choice == '11':
        downloader.download_imagenet_info()
    elif choice == '12':
        # Recommended set for small experiments
        print("\nDownloading recommended datasets for small experiments...")
        downloader.download_div2k(include_val=True)
        downloader.download_set12()
        downloader.download_set14()
        downloader.download_bsd68()
        downloader.download_urban100()
    elif choice == '13':
        # Custom selection
        datasets = {
            'div2k': lambda: downloader.download_div2k(include_val=True),
            'set12': downloader.download_set12,
            'set14': downloader.download_set14,
            'bsd68': downloader.download_bsd68,
            'urban100': downloader.download_urban100,
            'coco_train': lambda: downloader.download_coco(year=2017, split='train'),
            'coco_val': lambda: downloader.download_coco(year=2017, split='val'),
            'sidd_small': lambda: downloader.download_sidd(subset='small'),
            'sidd_medium': lambda: downloader.download_sidd(subset='medium'),
            'dnd': downloader.download_dnd,
            'imagenet': downloader.download_imagenet_info
        }
        
        print("\nAvailable datasets:")
        for name in datasets.keys():
            print(f"  - {name}")
        
        selected = input("\nEnter datasets to download (comma-separated): ").strip().split(',')
        for name in selected:
            name = name.strip()
            if name in datasets:
                datasets[name]()
    else:
        print("Invalid selection")
        return
    
    # Generate summary
    downloader.generate_summary()
    
    print("\n✓ All operations completed!")
    print(f"Datasets location: {downloader.base_dir.absolute()}")


if __name__ == '__main__':
    main()