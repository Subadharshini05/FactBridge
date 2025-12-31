# FactBridge – GenAI Document Ingestion Platform

FactBridge is a GenAI-ready backend system built using FastAPI.
It ingests documents, extracts text, chunks content, and prepares
data for Retrieval-Augmented Generation (RAG).

## Tech Stack
- FastAPI (Async)
- Pydantic
- PyPDF2
- Docker Compose
- Redis (task queue ready)

## GenAI Architecture
PDF → Text Extraction → Chunking → (LlamaIndex / ChromaDB planned) → LLM

## AI Stack (Planned)
- LlamaIndex for document indexing
- LangGraph for agent workflows
- ChromaDB for vector storage
- Arize Phoenix for hallucination monitoring

## DevOps
- Docker Compose for local orchestration
- Redis for async task processing
- Kubernetes (Helm) ready architecture

## Status
- Core ingestion pipeline implemented
- AI layer plug-in ready
