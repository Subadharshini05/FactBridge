from fastapi import FastAPI

app = FastAPI(title="FactBridge")

@app.get("/")
def root():
    return {"message": "FactBridge API running"}
