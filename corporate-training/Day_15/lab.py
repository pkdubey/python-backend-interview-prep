# Day 15 Lab — Capstone: Full-Stack AI App
# This ties together: FastAPI + RAG + LangChain + Docker-ready structure

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import requests
import chromadb
from sentence_transformers import SentenceTransformer

app = FastAPI(title="Corporate AI Assistant", version="1.0")

# ── Setup (runs once at startup) ─────────────────────────────────────────────
embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
collection = chroma_client.create_collection("company_docs")

COMPANY_DOCS = [
    "Annual leave: 18 days per year for all full-time employees.",
    "Sick leave: 10 days per year. Medical certificate required for 2+ days.",
    "WFH policy: 2 days per week with manager approval. Not during probation.",
    "Performance reviews: April and October. Ratings 1-5.",
    "Travel: Economy class under 2 hours. Hotel ₹5000/night in Tier 1 cities.",
    "Maternity leave: 26 weeks. Paternity leave: 5 days.",
]

# Index documents
embeddings = embedder.encode(COMPANY_DOCS).tolist()
collection.add(
    documents=COMPANY_DOCS,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(COMPANY_DOCS))]
)

# ── Models ────────────────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    question: str
    use_rag: bool = True

class ChatResponse(BaseModel):
    answer: str
    sources: list[str] = []
    model_used: str

# ── RAG Helper ────────────────────────────────────────────────────────────────
def retrieve_context(question: str, top_k: int = 2) -> list[str]:
    query_emb = embedder.encode([question]).tolist()
    results = collection.query(query_embeddings=query_emb, n_results=top_k)
    return results["documents"][0]

def ask_ollama(prompt: str, system: str = "You are a helpful assistant.") -> str:
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt},
        ],
        "options": {"temperature": 0.1},
        "stream": False,
    }, timeout=30)
    return response.json()["message"]["content"]

# ── Endpoints ─────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "healthy", "docs_indexed": len(COMPANY_DOCS)}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    sources = []

    if req.use_rag:
        sources = retrieve_context(req.question)
        context = "\n".join(sources)
        prompt = (
            f"Answer using ONLY this context. "
            f"If not in context, say 'Not in company policy.'\n\n"
            f"Context:\n{context}\n\nQuestion: {req.question}"
        )
    else:
        prompt = req.question

    try:
        answer = ask_ollama(prompt)
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"LLM unavailable: {e}")

    return ChatResponse(answer=answer, sources=sources, model_used="llama3.2")

@app.get("/docs-count")
def docs_count():
    return {"total_documents": collection.count()}

# ── Run: uvicorn lab:app --reload ─────────────────────────────────────────────
# Test: curl -X POST http://localhost:8000/chat \
#   -H "Content-Type: application/json" \
#   -d '{"question": "How many sick leaves do I get?"}'
