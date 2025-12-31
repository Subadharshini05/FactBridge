# FactBridge – GenAI Document Ingestion Platform

FactBridge is a GenAI-ready backend built using FastAPI.
It ingests documents, extracts text, chunks content, and prepares
data for Retrieval-Augmented Generation (RAG).

## Current Features
- FastAPI async backend
- PDF upload API
- Text extraction using PyPDF2
- Chunking with overlap
- Swagger UI for testing

## Tech Stack
- FastAPI (Async)
- Pydantic
- PyPDF2
- Docker (planned)
- Redis (planned)
- Vector DB (ChromaDB / Pinecone – planned)

## Architecture (Current)
PDF → Text Extraction → Chunking → API Response

## Architecture (Next – GenAI)
PDF → Chunking → Embeddings → Vector DB → LLM (RAG)

## Status
✅ Backend stable  
🚧 GenAI layer in progress
