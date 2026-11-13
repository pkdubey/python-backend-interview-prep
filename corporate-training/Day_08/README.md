# Day 8 — RAG (Retrieval-Augmented Generation)
**Vibe:** "Giving the AI your company's brain."

---

## 🗣️ How to Open This Day

> "Raise your hand if you've asked ChatGPT something about your company's internal policies and it gave you a wrong answer. That's because ChatGPT doesn't know your company. Today we fix that. We're going to build a system where the AI can answer questions using YOUR documents."

---

## 🧠 Concepts & Human-Language Explanations

### The Core Problem
**Say this:** "LLMs are trained on public internet data up to a certain date. They know nothing about:
- Your company's HR policies
- Your product documentation
- Your internal reports
- Anything after their training cutoff

RAG solves this."

### The Open-Book Exam Analogy
> "An LLM without RAG is a student taking a **closed-book exam** — it can only use what it memorized during training. RAG turns it into an **open-book exam** — before answering, the AI finds the exact page in your textbook (your documents) that's relevant, reads it, and then answers. Much more accurate."

### How RAG Works — Step by Step

```
Step 1: LOAD    → Read your documents (PDF, Word, website)
Step 2: CHUNK   → Split into small pieces (like paragraphs)
Step 3: EMBED   → Convert each chunk to a vector (numbers)
Step 4: STORE   → Save vectors in a Vector Database
--- (above happens once, at setup time) ---
Step 5: QUERY   → User asks a question
Step 6: SEARCH  → Find the most relevant chunks (vector similarity)
Step 7: AUGMENT → Add those chunks to the prompt
Step 8: GENERATE → LLM answers using the retrieved context
```

### Vector Database — "A Search Engine for Meaning"
**Say this:** "A normal database searches for exact keywords. A vector database searches for MEANING. 'What is the leave policy?' and 'How many vacation days do I get?' are different words but same meaning — a vector database finds both."

**Popular options:**
- **ChromaDB** — Free, runs locally, great for learning
- **Pinecone** — Cloud-based, production-ready
- **FAISS** — Facebook's library, very fast

### Chunking Strategy — "Size Matters"
**Say this:** "If chunks are too small, you lose context. Too large, you include irrelevant info. The sweet spot is usually 500-1000 characters with 100-character overlap between chunks."

```
Document: [============================]
Chunk 1:  [========]
Chunk 2:      [========]   ← overlap with chunk 1
Chunk 3:          [========]
```

---

## 💻 Live Coding Demo

**Scenario:** "Let's build an HR Policy Chatbot. Upload your company's leave policy PDF. Ask it questions. Watch it answer accurately — without hallucinating."

**Show the difference:**
1. Ask the LLM without RAG: "What is our company's maternity leave policy?"
2. Ask with RAG: Same question — now it reads from the actual policy document

See `lab.py`.

---

## 🏋️ Hands-on Challenge

Build a "Product FAQ Bot":
1. Create a text file with 20 product FAQs
2. Build the RAG pipeline (chunk → embed → store)
3. Ask 5 questions — verify answers come from the document
4. Ask a question NOT in the document — see how it handles it

---

## 📝 Daily Recap Questions

1. "What problem does RAG solve?"
2. "What's the difference between a vector database and a regular database?"
3. "Why do we chunk documents instead of feeding the whole thing to the LLM?"

**Key takeaway:** "RAG is the #1 pattern for enterprise AI. Every company that wants to build an AI chatbot on their internal data uses RAG. This is production-level knowledge."

---

## 🔗 Connection to Tomorrow

> "Today we used OpenAI's embedding model. Tomorrow we'll see how to do the same thing with FREE, open-source models that run on your own machine."
