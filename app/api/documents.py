from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.ingestion import (
    extract_text_from_pdf,
    chunk_text,
    
)

router = APIRouter()

UPLOAD_DIR = "data/uploads"


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # 1. ensure upload folder exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    # 2. save uploaded file
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 3. extract text from PDF
    text = extract_text_from_pdf(file.filename)

    # 4. chunk the text
    chunks = chunk_text(text)

    # 5. vectorize & store chunks
    chunks_count = vectorize_and_store(chunks, file.filename)

    # 6. response
    return {
        "message": "Document uploaded and vectorized successfully",
        "filename": file.filename,
        "chunks_stored": chunks_count
    }
