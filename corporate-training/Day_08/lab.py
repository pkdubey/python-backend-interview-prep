# Day 8 Lab — RAG (Retrieval-Augmented Generation)
# pip install chromadb sentence-transformers requests
import requests
import chromadb
from sentence_transformers import SentenceTransformer

# ── SAMPLE COMPANY DOCUMENT ──────────────────────────────────────────────────
HR_POLICY = """
TECHCORP INDIA — HR POLICY DOCUMENT

LEAVE POLICY:
Employees are entitled to 18 days of paid annual leave per year.
Sick leave: 10 days per year, requires medical certificate for more than 2 consecutive days.
Maternity leave: 26 weeks for female employees as per Maternity Benefit Act.
Paternity leave: 5 days for male employees.
Casual leave: 8 days per year, cannot be carried forward.
Leave encashment: Up to 30 days of accumulated leave can be encashed at year end.

WORK FROM HOME POLICY:
Employees can work from home up to 2 days per week with manager approval.
WFH is not applicable during probation period (first 6 months).
All WFH days must be logged in the HR portal by 10 AM.

PERFORMANCE REVIEW:
Performance reviews are conducted twice a year — April and October.
Ratings: Outstanding (5), Exceeds Expectations (4), Meets Expectations (3), Needs Improvement (2), Unsatisfactory (1).
Employees rated 4 or above are eligible for fast-track promotion.
Annual increment is based on performance rating and market benchmarking.

TRAVEL POLICY:
Domestic travel: Economy class for flights under 2 hours, business class for longer.
Hotel allowance: Tier 1 cities ₹5000/night, Tier 2 cities ₹3000/night.
Travel advance must be requested 3 days before travel.
Expense claims must be submitted within 7 days of return.
"""

# ── STEP 1: CHUNK the document ───────────────────────────────────────────────
def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end].strip())
        start += chunk_size - overlap
    return [c for c in chunks if len(c) > 50]

chunks = chunk_text(HR_POLICY)
print(f"✅ Document split into {len(chunks)} chunks")

# ── STEP 2: EMBED & STORE in ChromaDB ────────────────────────────────────────
embedder = SentenceTransformer("all-MiniLM-L6-v2")  # Free, runs locally

client = chromadb.Client()
collection = client.create_collection("hr_policy")

embeddings = embedder.encode(chunks).tolist()
collection.add(
    documents=chunks,
    embeddings=embeddings,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
print(f"✅ {len(chunks)} chunks stored in vector database")

# ── STEP 3: RETRIEVAL function ────────────────────────────────────────────────
def retrieve(question, top_k=3):
    query_embedding = embedder.encode([question]).tolist()
    results = collection.query(query_embeddings=query_embedding, n_results=top_k)
    return results["documents"][0]

# ── STEP 4: RAG function ──────────────────────────────────────────────────────
def ask_with_rag(question):
    relevant_chunks = retrieve(question)
    context = "\n\n".join(relevant_chunks)

    prompt = f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have that information in the policy document."

Context:
{context}

Question: {question}
Answer:"""

    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "options": {"temperature": 0.1},
        "stream": False,
    })
    return response.json()["message"]["content"]

# ── DEMO: Ask Questions ───────────────────────────────────────────────────────
questions = [
    "How many days of annual leave do I get?",
    "What is the maternity leave policy?",
    "Can I work from home during probation?",
    "What is the hotel allowance for Mumbai?",
    "What is the company's policy on stock options?",  # Not in document
]

print("\n" + "="*60)
print("HR POLICY CHATBOT (RAG-powered)")
print("="*60)

for q in questions:
    print(f"\n❓ {q}")
    print(f"💬 {ask_with_rag(q)}")
    print("-"*40)
