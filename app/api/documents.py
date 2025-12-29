from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "data/uploads"

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document for verification.

    Supported formats:
    - PDF
    - DOCX

    Next steps (planned):
    - Validate file type
    - Generate document ID
    - Send content to vector store
    - Track ingestion status
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "status": "stored"
    }
