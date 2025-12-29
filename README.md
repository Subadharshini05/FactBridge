# FactBridge

## Overview
FactBridge is a GenAI-powered document verification system built using Python (FastAPI).
It allows users to upload documents and ask questions that are answered strictly
from uploaded evidence using Retrieval-Augmented Generation (RAG).

## Core Features
- Secure document upload (PDF/DOCX)
- Evidence-based question answering
- Zero hallucination policy (answers only from documents)
- Verification logs for audit & compliance

## Tech Stack
- Backend: FastAPI (Python)
- AI Layer: RAG (planned: LlamaIndex)
- Vector Store: Local Vector DB (planned)
- File Handling: python-multipart
- API Docs: Swagger UI

## Project Structure
FactBridge/
├── app/
│ ├── api/
│ │ └── documents.py
│ ├── core/
│ ├── models/
│ ├── services/
│ └── main.py
├── data/
│ ├── uploads/
│ └── vectorstore/
├── requirements.txt
└── README.md



## Next Steps
- Implement document ingestion
- Add vector embedding pipeline
- Build verified Q&A endpoint