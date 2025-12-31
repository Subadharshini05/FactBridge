from fastapi import APIRouter, UploadFile, File
from pathlib import Path

from app.services.ingestion import extract_text_from_pdf, chunk_text
from app.models.schemas import UploadResponse

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file.filename)
    chunks = chunk_text(text)

    return {
        "message": "Document uploaded and processed successfully",
        "filename": file.filename,
        "chunks_count": len(chunks)
    }
