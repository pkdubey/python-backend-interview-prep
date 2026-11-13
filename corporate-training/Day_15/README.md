# Day 15 — Capstone Architecture + AWS Deployment + Ocean Assessment
**Vibe:** "Bringing it all together — from laptop to production."

---

## 🗣️ How to Open This Day

> "15 days ago, you wrote your first Python variable. Today you're going to design a production-grade AI system and understand how to deploy it to the cloud. This is what senior engineers do. Let's close strong."

---

## Part A: Capstone Architecture (0.5 day — 4 hours)

### The Full-Stack AI App Architecture

**Draw this diagram on the whiteboard:**

```
┌─────────────────────────────────────────────────────────┐
│                    USER (Browser/Mobile)                 │
└──────────────────────────┬──────────────────────────────┘
                           │ HTTPS
┌──────────────────────────▼──────────────────────────────┐
│                    NGINX (Reverse Proxy)                 │
│              Load Balancing + SSL Termination            │
└──────────────────────────┬──────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                  FastAPI Backend (Python)                │
│         /chat  /upload  /search  /health                │
└────┬─────────────────────┬──────────────────────────────┘
     │                     │
┌────▼────┐          ┌─────▼──────────────────────────────┐
│  Redis  │          │         AI Layer                    │
│ (Cache) │          │  LangChain + LangGraph              │
└─────────┘          │  Ollama (local) / OpenAI (cloud)   │
                     └─────────────────┬──────────────────┘
                                       │
                     ┌─────────────────▼──────────────────┐
                     │         Data Layer                  │
                     │  PostgreSQL + ChromaDB (vectors)   │
                     └────────────────────────────────────┘
```

### Component Explanations

**NGINX:** "The traffic cop. All requests come here first. It decides which server to send them to."

**FastAPI:** "Our Python backend — the brain. Handles all business logic."

**Redis:** "Super-fast memory cache. If 100 users ask the same question, we answer from cache instead of calling the LLM 100 times. Saves money and time."

**ChromaDB:** "Our vector database — stores embeddings for RAG."

**PostgreSQL:** "Regular database — stores users, chat history, documents."

### Dockerizing the App
**Say this:** "Docker is like a shipping container for your code. Your app + all its dependencies packed into one box. Works the same on your laptop, your colleague's laptop, and the production server."

```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t hr-ai-app .
docker run -p 8000:8000 hr-ai-app
```

---

## Part B: AWS Deployment (Alternative — for Hyperscaler track)

### AWS Services Used

| Service | What it does | Analogy |
|---------|-------------|---------|
| EC2 | Virtual machine in the cloud | Renting a computer |
| S3 | File storage | Google Drive for your app |
| RDS | Managed PostgreSQL | Database without the headache |
| ElastiCache | Managed Redis | Cache without the headache |
| ECR | Docker image registry | GitHub for Docker images |
| ECS/EKS | Run Docker containers | Kubernetes made easier |

### Deployment Steps (High Level)
```
1. Build Docker image locally
2. Push to AWS ECR (container registry)
3. Create EC2 instance (or ECS task)
4. Pull image from ECR and run
5. Set up RDS for PostgreSQL
6. Set up ElastiCache for Redis
7. Configure NGINX on EC2
8. Point domain to EC2 IP
9. Set up SSL certificate (AWS Certificate Manager)
```

### Environment Variables — "Never Hardcode Secrets"
```python
# WRONG — never do this
OPENAI_API_KEY = "sk-abc123..."

# RIGHT — use environment variables
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

```bash
# On EC2, set env vars:
export OPENAI_API_KEY="sk-abc123..."
export DATABASE_URL="postgresql://user:pass@rds-endpoint/dbname"
```

---

## Part C: Ocean Assessment (0.5 day — 4 hours)

### What is Ocean Assessment?
This is the company's internal certification assessment. Students need to demonstrate understanding of all 15 days of content.

### Preparation Checklist for Students

**Python (Days 1-3)**
- [ ] Write a class with inheritance
- [ ] Use a decorator
- [ ] Process a CSV with Pandas

**FastAPI (Day 4)**
- [ ] Create a GET and POST endpoint
- [ ] Use Pydantic for validation

**NLP (Day 5)**
- [ ] Tokenize and clean text
- [ ] Explain TF-IDF and embeddings

**GenAI (Days 6-7)**
- [ ] Explain what an LLM is (no jargon)
- [ ] Write a zero-shot and few-shot prompt
- [ ] Explain hallucination and how to prevent it

**RAG (Day 8)**
- [ ] Explain the 8-step RAG pipeline
- [ ] Explain why we chunk documents

**Open Source LLMs (Days 9-10)**
- [ ] Name 3 open source models and their use cases
- [ ] Explain quantization in plain English

**LangChain (Day 11)**
- [ ] Build a simple chain with `|` operator
- [ ] Explain what a retriever does

**Agents (Day 12)**
- [ ] Explain ReAct pattern
- [ ] Define what a "tool" is in agent context

**LangGraph (Day 14)**
- [ ] Explain state in LangGraph
- [ ] Draw a simple 3-node graph

### Quick Revision — One-Liners

| Topic | One-liner |
|-------|-----------|
| LLM | Sophisticated autocomplete trained on billions of documents |
| RAG | Open-book exam — give AI your documents before asking questions |
| Agent | AI that can use tools and take actions, not just answer questions |
| LangChain | LEGO kit for building LLM applications |
| LangGraph | Orchestrator for multi-agent workflows with shared state |
| Vector DB | Search engine for meaning, not just keywords |
| Embedding | Converting text to numbers so AI can understand similarity |
| Temperature | Creativity dial — 0 = predictable, 1 = creative |
| Quantization | Compressing AI models to run on smaller hardware |
| Prompt Engineering | Writing clear instructions to get good AI outputs |

---

## 🎓 Closing Words (Trainer Script)

> "15 days ago, you wrote `print('Hello World')`. Today you built a multi-agent AI system, deployed it with Docker, and understand how to put it on AWS.
>
> The AI field moves fast. What you learned here is the foundation — the concepts don't change even when the tools do. LangChain will be replaced by something better. But the idea of chains, agents, RAG, embeddings — those are here to stay.
>
> Keep building. The best way to learn is to pick a problem in your own company and try to solve it with AI. Start small. Ship something. Iterate.
>
> You've got my contact. Reach out anytime. Good luck! 🚀"
