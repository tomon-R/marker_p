import time
from pathlib import Path

from lib.llm_utils import process_md_with_llm as process_md


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
def process_md_with_llm_single(md_file):
    """
    Process a single Markdown file with LLM.
    """
    process_md(md_file)


@time_track
def process_md_with_llm_multiple(md_files):
    """
    Process multiple Markdown files with LLM.
    """
    for md_file in md_files:
        process_md(md_file)


def main():
    # Target directory
    target_dir = "random"

    # Find Markdown files for processing
    marker_out_dir = Path("textlint_out") / target_dir
    md_files = list(marker_out_dir.glob("**/*.md"))

    # Process single Markdown by LLM
    if md_files:
        print("Processing Markdown...")
        # process_md_with_llm_single(md_files[0])  # single file
        process_md_with_llm_multiple(md_files)  # all files


if __name__ == "__main__":
    main()
