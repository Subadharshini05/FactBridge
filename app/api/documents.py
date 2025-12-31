from fastapi import APIRouter, UploadFile, File
import os

from app.services.ingestion import extract_text_from_pdf, chunk_text
from app.services.vector_store import store_chunks, search_chunks

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)
    chunks = chunk_text(text)

    chunks_count = store_chunks(chunks, file.filename)

    return {
        "message": "Document uploaded and vectorized successfully",
        "filename": file.filename,
        "chunks_count": chunks_count
    }


@router.post("/search")
def search_document(query: str):
    results = search_chunks(query)

    return {
        "query": query,
        "results": results
    }
