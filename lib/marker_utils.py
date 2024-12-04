import subprocess
from pathlib import Path


def convert_pdf_to_md(pdf_path):
    """
    Converts a PDF to Markdown using marker-pdf and saves the output in marker_out/{directory name}.
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists() or not pdf_path.suffix == ".pdf":
        raise ValueError(f"Invalid PDF file: {pdf_path}")

    output_dir = Path("marker_out") / pdf_path.parent.name
    output_dir.mkdir(parents=True, exist_ok=True)

    command = f"marker_single {pdf_path} {output_dir} --langs Japanese"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    if result.returncode != 0:
        raise RuntimeError(f"Error converting {pdf_path}: {result.stderr}")

    print(f"Converted {pdf_path} to Markdown at {output_dir}")
