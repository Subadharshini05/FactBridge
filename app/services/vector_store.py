from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import os

# Persistent DB
CHROMA_PATH = "data/vectorstore"

client = Client(
    Settings(
        persist_directory=CHROMA_PATH,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(name="documents")

# Lightweight embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def store_chunks(chunks: list[str], source: str):
    embeddings = embedding_model.encode(chunks).tolist()

    ids = [f"{source}_{i}" for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"source": source}] * len(chunks)
    )

    client.persist()

    return len(chunks)


def search_chunks(query: str, top_k: int = 3):
    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]
