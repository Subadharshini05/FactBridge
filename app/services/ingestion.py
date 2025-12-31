from pathlib import Path
from PyPDF2 import PdfReader

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def extract_text_from_pdf(filename: str) -> str:
    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise FileNotFoundError("PDF file not found")

    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks
from pathlib import Path
from PyPDF2 import PdfReader

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def extract_text_from_pdf(filename: str) -> str:
    pdf_path = UPLOAD_DIR / filename

    if not pdf_path.exists():
        raise FileNotFoundError("PDF file not found")

    reader = PdfReader(str(pdf_path))
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def chunk_text(text: str, chunk_size: int = 500):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end

    return chunks
