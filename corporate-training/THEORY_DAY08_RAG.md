# Day 8 Theory — RAG (Retrieval-Augmented Generation)
## "Give AI your company's brain"

---

## 1. The Problem — What Doesn't an LLM Know?

ChatGPT is very smart. But it doesn't know:

- Your company's HR policies
- Your product manual
- Today's news (after its training cutoff)
- Your internal database
- Confidential documents

**Example:**
```
User: "How much maternity leave does our company give?"
ChatGPT: "Generally in India, maternity leave is 26 weeks..."
```

That's a generic answer — not your specific company policy.

**This is exactly the problem RAG solves.**

---

## 2. What is RAG? — The Open Book Exam Analogy

**Without RAG:**
The LLM is a student taking a **closed-book exam**. It only knows what it memorized during training. Nothing new.

**With RAG:**
The LLM is a student taking an **open-book exam**. Before answering, it finds the relevant pages and puts them on the desk. Then it writes the answer — directly from those pages.

```
Question: "What is the maternity leave policy?"

Without RAG: AI guesses from training data → generic answer

With RAG:
1. Searched HR Policy PDF for "maternity"
2. Found relevant paragraph: "26 weeks for female employees"
3. AI read that paragraph and answered → accurate answer
```

---

## 3. RAG's Complete Flow — 8 Steps

```
SETUP (happens once):
━━━━━━━━━━━━━━━━━━━━━━━━
Step 1: LOAD     → Read documents (PDF, Word, website, database)
Step 2: CHUNK    → Split into small pieces (paragraphs)
Step 3: EMBED    → Convert each piece to numbers
Step 4: STORE    → Save in a Vector Database

QUERY (happens every time a user asks):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 5: QUERY    → User's question arrives
Step 6: SEARCH   → Find similar chunks (vector search)
Step 7: AUGMENT  → Add relevant chunks to the prompt
Step 8: GENERATE → LLM answers using those chunks
```

---

## 4. Chunking — "Breaking the Document into Pieces"

You can't give the entire document to the LLM at once — context window has limits.

So we break the document into small pieces (chunks).

**Example:**
```
Original Document (10 pages):
[Page 1: Leave Policy]
[Page 2: WFH Policy]
[Page 3: Travel Policy]
...

After Chunking:
Chunk 1: "Annual leave: 18 days per year..."
Chunk 2: "Sick leave: 10 days. Medical certificate..."
Chunk 3: "Maternity leave: 26 weeks for female..."
Chunk 4: "WFH: 2 days per week with approval..."
...
```

**Chunking strategies:**

| Strategy | How | When to use |
|----------|-----|------------|
| Fixed size | 500 character pieces | Simple documents |
| Sentence | At sentence boundaries | Conversational text |
| Paragraph | At paragraph boundaries | Structured documents |
| Semantic | Based on meaning | Complex documents |

**Why overlap?**
```
Chunk 1: [============================]
Chunk 2:         [============================]
                 ↑ overlap
```

If important information falls on a chunk boundary, overlap ensures it appears fully in at least one chunk.

---

## 5. Embeddings — "Converting Text to Numbers"

Embedding = A numerical representation of text.

```
"Annual leave is 18 days"  →  [0.2, 0.8, 0.1, 0.5, ...]
"How many vacation days?"  →  [0.2, 0.7, 0.1, 0.6, ...]
                                ↑ similar numbers!
```

Similar meaning → similar numbers → close together in vector space.

**Embedding models:**
- `all-MiniLM-L6-v2` — Free, fast, good quality, runs locally
- `text-embedding-ada-002` — OpenAI, paid, high quality
- `nomic-embed-text` — Free, runs with Ollama

---

## 6. Vector Database — "Search by Meaning"

Normal database search: Exact keyword match.
```sql
SELECT * FROM docs WHERE text LIKE '%maternity%'
-- Only results containing the word "maternity"
```

Vector database search: Meaning match.
```python
results = collection.query("How many days off for new mothers?")
# The word "maternity" isn't in the query
# But maternity leave chunks are still returned!
# Because the meaning is similar
```

**Popular vector databases:**

| Database | Type | Best for |
|----------|------|----------|
| ChromaDB | Local, free | Learning, small projects |
| FAISS | Local, free | Fast search, large data |
| Pinecone | Cloud, paid | Production, scale |
| Weaviate | Self-hosted/cloud | Enterprise |
| pgvector | PostgreSQL extension | Already using Postgres |

---

## 7. Retrieval — "Finding the Right Chunks"

User's question arrives → embed it → find similar chunks.

```python
# User's question
question = "How much maternity leave do I get?"

# Embed the question
question_embedding = embed(question)
# [0.2, 0.7, 0.1, 0.6, ...]

# Search vector DB for similar chunks
results = vector_db.search(
    query_embedding=question_embedding,
    top_k=3    # Top 3 most similar chunks
)

# Results:
# Chunk: "Maternity leave: 26 weeks for female employees" (similarity: 0.92)
# Chunk: "Paternity leave: 5 days for male employees" (similarity: 0.78)
# Chunk: "Leave encashment: up to 30 days" (similarity: 0.45)
```

---

## 8. The Augmented Prompt — "Ask with Context"

Add the retrieved chunks to the prompt:

```python
context = """
Maternity leave: 26 weeks for female employees as per Maternity Benefit Act.
Paternity leave: 5 days for male employees.
"""

prompt = f"""
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: How much maternity leave do I get?
"""

# AI's answer: "26 weeks for female employees as per Maternity Benefit Act."
# Accurate! Came directly from the context.
```

---

## 9. RAG vs Fine-tuning

Both are approaches to make an LLM company-specific.

| | RAG | Fine-tuning |
|--|-----|-------------|
| What it is | Give documents at runtime | Retrain the model |
| Cost | Low | Very high (GPU hours) |
| Updating | Easy — just update the document | Hard — need to retrain |
| Accuracy | Good for factual Q&A | Better for style/tone |
| Hallucination | Less (answers from context) | More (answers from model) |
| When to use | Company docs, policies, FAQs | Specific writing style, domain language |

**For corporate use:** RAG is almost always the better choice.

---

## 10. RAG Limitations

RAG isn't perfect. Important to know:

**1. Chunking quality matters:**
If important info gets cut at a chunk boundary → wrong answer.

**2. Embedding quality matters:**
If the embedding model is weak → wrong chunks get retrieved.

**3. "Lost in the middle" problem:**
If you retrieve 10 chunks, the LLM may ignore the ones in the middle.

**4. Hallucination is still possible:**
If the retrieved context doesn't contain the answer, the LLM may still guess.

**Fix:** Explicitly say "If the answer is not in the context, say 'I don't know'."

**5. Latency:**
Every query: embed → search → retrieve → generate. Slightly slower.

---

## 11. RAG Architecture Diagram

```
                    ┌─────────────────┐
                    │   Documents     │
                    │ (PDF, Word, DB) │
                    └────────┬────────┘
                             │ Load & Chunk
                    ┌────────▼────────┐
                    │   Text Chunks   │
                    └────────┬────────┘
                             │ Embed
                    ┌────────▼────────┐
                    │  Vector Database│
                    │  (ChromaDB etc) │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
┌────────▼────────┐ ┌────────▼────────┐         │
│  User Question  │ │  Embed Question │         │
└────────┬────────┘ └────────┬────────┘         │
         │                   │                   │
         │          ┌────────▼────────┐          │
         │          │  Similar Chunks │          │
         │          │   Retrieved     │          │
         │          └────────┬────────┘          │
         │                   │                   │
         └──────────┬────────┘                   │
                    │                            │
           ┌────────▼────────┐                  │
           │  Augmented      │                  │
           │  Prompt         │                  │
           └────────┬────────┘                  │
                    │                            │
           ┌────────▼────────┐                  │
           │      LLM        │                  │
           └────────┬────────┘                  │
                    │                            │
           ┌────────▼────────┐                  │
           │    Answer       │                  │
           └─────────────────┘                  │
```

---

## Summary

| Concept | In One Line |
|---------|------------|
| RAG | Open-book exam — give AI relevant pages before it answers |
| Chunking | Breaking a document into manageable pieces |
| Embedding | Text → numbers (similar text → similar numbers) |
| Vector DB | Search by meaning, not just keywords |
| Retrieval | Find chunks similar to the user's question |
| Augmentation | Add retrieved chunks to the prompt |

**Tomorrow:** Doing all of this for free — Open Source LLMs.
