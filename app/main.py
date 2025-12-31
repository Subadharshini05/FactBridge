from fastapi import FastAPI
from app.api.documents import router as document_router

app = FastAPI(
    title="FactBridge",
    description="GenAI-ready document ingestion system",
    version="1.0.0"
)

app.include_router(document_router, prefix="/documents", tags=["Documents"])

@app.get("/")
async def root():
    return {"status": "FactBridge backend running"}
