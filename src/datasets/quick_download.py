from src.dataset.download import DatasetDownloader


def download_essentials() -> None:
    """Download essential datasets for image denoising.

    Includes:
        - DIV2K (training)
        - Set12, BSD68 (testing)

    Total size: ~3.5GB
    Estimated time: 10-30 minutes
    """
    downloader = DatasetDownloader()

    print("Essential datasets for image denoising:")
    print("- DIV2K (training)")
    print("- Set12, BSD68 (testing)")
    print("\nEstimated download size: ~3.5GB")
    print("Estimated time: 10-30 minutes (depending on connection)")

    proceed = input("\nProceed? (y/n): ")
    if proceed.lower() == "y":
        downloader.download_div2k(include_val=False)
        downloader.download_set12()
        downloader.download_bsd68()
        downloader.generate_summary()
        print("\n✓ Essential datasets downloaded!")


def download_benchmarks() -> None:
    """Download all benchmark datasets.

    Includes:
        - Set12, Set14, BSD68, Urban100

    Total size: ~100MB
    Quick download for testing
    """
    downloader = DatasetDownloader()

    print("Benchmark datasets:")
    print("- Set12, Set14, BSD68, Urban100")
    print("\nEstimated download size: ~100MB")

    proceed = input("\nProceed? (y/n): ")
    if proceed.lower() == "y":
        downloader.download_set12()
        downloader.download_set14()
        downloader.download_bsd68()
        downloader.download_urban100()
        downloader.generate_summary()
        print("\n✓ Benchmark datasets downloaded!")


def download_real_noise() -> None:
    """Download real-world noise datasets.

    Includes:
        - SIDD Small (2GB)
        - DND (3.3GB)

    Total size: ~5.3GB
    For real-world noise experiments
    """
    downloader = DatasetDownloader()

    print("Real-world noise datasets:")
    print("- SIDD Small (2GB)")
    print("- DND (3.3GB)")
    print("\nEstimated download size: ~5.3GB")

    proceed = input("\nProceed? (y/n): ")
    if proceed.lower() == "y":
        downloader.download_sidd(subset="small")
        downloader.download_dnd()
        downloader.generate_summary()
        print("\n✓ Real noise datasets downloaded!")


def download_for_paper() -> None:
    """Download comprehensive set for research paper.

    Includes:
        - DIV2K (train + val)
        - All benchmarks (Set12, Set14, BSD68, Urban100)
        - Real noise (SIDD Small, DND)

    Total size: ~9GB
    Complete set for paper experiments
    """
    downloader = DatasetDownloader()

    print("Complete dataset collection for research:")
    print("- DIV2K (train + validation)")
    print("- Set12, Set14, BSD68, Urban100 (benchmarks)")
    print("- SIDD Small, DND (real-world noise)")
    print("\nEstimated download size: ~9GB")
    print("Estimated time: 30-60 minutes")

    proceed = input("\nProceed? (y/n): ")
    if proceed.lower() == "y":
        # Training data
        print("\n[Phase 1/3] Downloading training data...")
        downloader.download_div2k(include_val=True)

        # Benchmark datasets
        print("\n[Phase 2/3] Downloading benchmark datasets...")
        downloader.download_set12()
        downloader.download_set14()
        downloader.download_bsd68()
        downloader.download_urban100()

        # Real-world noise
        print("\n[Phase 3/3] Downloading real-world noise datasets...")
        downloader.download_sidd(subset="small")
        downloader.download_dnd()

        downloader.generate_summary()
        print("\n✓ Complete dataset collection downloaded!")


if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║   Quick Download Options                                 ║
    ╚══════════════════════════════════════════════════════════╝

    1. Essential datasets (DIV2K, Set12, BSD68) - ~3.5GB
       Best for: Quick start, initial experiments

    2. Benchmark datasets (Set12, Set14, BSD68, Urban100) - ~100MB
       Best for: Testing only, comparing with papers

    3. Real noise datasets (SIDD, DND) - ~5.3GB
       Best for: Real-world noise experiments

    4. Complete collection for research paper - ~9GB
       Best for: Publishing results, comprehensive evaluation
    """)

    choice = input("Select (1-4): ").strip()

    if choice == "1":
        download_essentials()
    elif choice == "2":
        download_benchmarks()
    elif choice == "3":
        download_real_noise()
    elif choice == "4":
        download_for_paper()
    else:
        print("Invalid choice")
