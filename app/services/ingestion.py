import os
from pypdf import PdfReader

UPLOAD_DIR = "data/uploads"

def extract_text_from_pdf(filename: str) -> str:
    """
    Reads a PDF file from uploads folder and returns extracted text
    """
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError("PDF file not found")

    reader = PdfReader(file_path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    return full_text
