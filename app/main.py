from fastapi import FastAPI
from app.api.documents import router as documents_router
from app.api.rag import router as rag_router

app = FastAPI(title="FactBridge – GenAI RAG")

@app.get("/")
def root():
    return {"status": "GenAI backend running"}

app.include_router(documents_router, prefix="/documents", tags=["Documents"])
app.include_router(rag_router, prefix="/rag", tags=["RAG"])
