from fastapi import FastAPI
from app.api.documents import router as documents_router

app = FastAPI(title="FactBridge")

@app.get("/")
def health():
    return {"status": "FactBridge backend running"}

app.include_router(documents_router, prefix="/documents", tags=["Documents"])
