from sec.datset.download import DatasetDownloader


# Example 1: Download specific datasets programmatically
def example_1() -> None:
    """Download specific datasets."""
    downloader = DatasetDownloader(base_dir="./my_datasets")

    # Download training data
    downloader.download_div2k(include_val=True)

    # Download test datasets
    downloader.download_set12()
    downloader.download_bsd68()

    # Generate summary
    downloader.generate_summary()


# Example 2: Download datasets for synthetic noise experiments
def example_2() -> None:
    """Datasets for synthetic noise experiments."""
    downloader = DatasetDownloader()

    print("Setting up synthetic noise experiment datasets...")

    # Large training set
    downloader.download_div2k(include_val=True)

    # Multiple test sets
    downloader.download_set12()
    downloader.download_set14()
    downloader.download_bsd68()
    downloader.download_urban100()

    downloader.generate_summary()


# Example 3: Download datasets for real-world noise experiments
def example_3() -> None:
    """Datasets for real-world noise experiments."""
    downloader = DatasetDownloader()

    print("Setting up real-world noise experiment datasets...")

    # Real noise training
    downloader.download_sidd(subset="medium")  # Larger training set

    # Real noise testing
    downloader.download_sidd(subset="small")  # For validation
    downloader.download_dnd()  # For benchmark

    downloader.generate_summary()


# Example 4: Check what's already downloaded
def example_4() -> None:
    """Check downloaded datasets."""
    downloader = DatasetDownloader()
    downloader.generate_summary()


if __name__ == "__main__":
    # Run example 1
    example_1()
