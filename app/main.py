from fastapi import FastAPI
from app.api.documents import router as documents_router

app = FastAPI(
    title="FactBridge API",
    description="GenAI-powered document verification system",
    version="0.1.0"
)

# Include document routes
app.include_router(
    documents_router,
    prefix="/documents",
    tags=["Documents"]
)

@app.get("/")
def root():
    return {"status": "FactBridge backend running"}
