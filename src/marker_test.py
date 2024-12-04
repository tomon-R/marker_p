import time
from pathlib import Path

from lib.marker_utils import convert_pdf_to_md as convert_pdf


def time_track(func):
    """
    Decorator to track execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"[Time Taken] {func.__name__}: {elapsed_time:.2f} seconds")
        return result

    return wrapper


@time_track
def convert_pdf_to_md_single(pdf_file):
    """
    Convert a single PDF file to Markdown.
    """
    convert_pdf(pdf_file)


@time_track
def convert_pdf_to_md_multiple(pdf_files):
    """
    Convert multiple PDF files to Markdown.
    """
    for pdf_file in pdf_files:
        convert_pdf(pdf_file)


def main():
    # Target directory
    target_dir = "random"

    # Find pdf files for processing
    sample_dir = Path("sample") / target_dir
    pdf_files = list(sample_dir.glob("*.pdf"))

    # Convert pdf to markdown by marker
    if pdf_files:
        print("Processing PDF...")
        # convert_pdf_to_md_single(pdf_files[0])  # single file
        convert_pdf_to_md_multiple(pdf_files)  # all files


if __name__ == "__main__":
    main()
