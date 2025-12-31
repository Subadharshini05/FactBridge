from fastapi import FastAPI
from app.api.documents import router as documents_router

app = FastAPI(title="FactBridge API")

app.include_router(documents_router)


@app.get("/")
def root():
    return {"status": "FactBridge backend running"}
