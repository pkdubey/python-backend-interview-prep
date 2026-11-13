# Day 15 Theory — Capstone Architecture & AWS Deployment
## "From your laptop to the real world"

---

## 1. What is "Production"?

Until now, everything ran on your laptop. "Production" means:
- Real users are using it
- It must be available 24/7
- It must not be slow
- It must not crash
- Data must be secure

**Laptop vs Production:**

| | Laptop (Development) | Production |
|--|---------------------|------------|
| Users | Just you | Thousands |
| Uptime | Shut it down whenever | 99.9% uptime |
| Data | Test data | Real data |
| Security | None | Critical |
| Monitoring | None | Yes |
| Backup | None | Yes |

---

## 2. Production Architecture — Understand It Once

```
Internet
   ↓
[NGINX] ← Load Balancer + SSL
   ↓
[FastAPI App] ← Business Logic
   ↓         ↓
[Redis]   [AI Layer]
(Cache)   (LangChain + LLM)
   ↓         ↓
[PostgreSQL + ChromaDB]
(Data + Vectors)
```

What each component does:

**NGINX:**
- The traffic cop — all requests come here first
- Terminates SSL (handles HTTPS)
- Distributes load across multiple FastAPI instances
- Serves static files

**FastAPI:**
- Your Python code
- Business logic
- API endpoints

**Redis:**
- Super-fast cache
- If 100 users ask the same question — call the LLM once, serve the other 99 from cache
- Saves money and time

**PostgreSQL:**
- Main database — users, chat history, documents

**ChromaDB:**
- Vector database — stores embeddings for RAG

---

## 3. Docker — "A Shipping Container for Your Code"

**The problem without Docker:**
```
Developer: "It works on my machine!"
Server: "It doesn't work on mine!"
```

Different machines have different Python versions, different libraries, different OS — everything is different.

**Docker's solution:**
Pack your code + all its dependencies into one "container." The container runs the same way everywhere.

**Analogy:** A shipping container. Whatever is inside — the container is a standard size. It fits on a ship, a truck, a train. Same container, any vehicle.

```dockerfile
# Dockerfile — "The recipe for the container"
FROM python:3.11-slim          # Base image — Python 3.11

WORKDIR /app                   # Working directory inside the container

COPY requirements.txt .        # Copy requirements
RUN pip install -r requirements.txt  # Install them

COPY . .                       # Copy your code

EXPOSE 8000                    # Expose the port

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build the container
docker build -t my-ai-app .

# Run the container
docker run -p 8000:8000 my-ai-app

# Run in the background
docker run -d -p 8000:8000 my-ai-app
```

---

## 4. Environment Variables — "Never Hardcode Secrets"

**NEVER do this:**
```python
# main.py
OPENAI_API_KEY = "sk-abc123xyz..."  # ❌ Will end up on GitHub!
DATABASE_URL = "postgresql://user:password@host/db"  # ❌
```

**ALWAYS do this:**
```python
# main.py
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
```

```bash
# .env file (NEVER commit this to git!)
OPENAI_API_KEY=sk-abc123xyz...
DATABASE_URL=postgresql://user:password@host/db
```

```bash
# Pass when running
docker run -e OPENAI_API_KEY=sk-abc123 my-app
# or
docker run --env-file .env my-app
```

---

## 5. AWS Services — Plain English

AWS = Amazon Web Services = Amazon's cloud platform.

**EC2 (Elastic Compute Cloud):**
- Rent a virtual machine
- Your Docker container runs here
- Analogy: Renting a computer

**S3 (Simple Storage Service):**
- Store files — images, PDFs, backups
- Analogy: Google Drive for your app
- Unlimited storage, very cheap

**RDS (Relational Database Service):**
- Managed PostgreSQL/MySQL
- Backups automatic, updates automatic
- Analogy: A database without the headache

**ElastiCache:**
- Managed Redis
- Analogy: Redis without the headache

**ECR (Elastic Container Registry):**
- Store Docker images
- Analogy: GitHub for Docker images

**Route 53:**
- Domain name management
- `myapp.com` → EC2 IP address

---

## 6. Deployment Steps — High Level

```
1. Code is ready locally
   ↓
2. Build Docker image
   docker build -t my-app .
   ↓
3. Push to AWS ECR
   docker push <ecr-url>/my-app
   ↓
4. Create EC2 instance (or use ECS)
   ↓
5. Pull image on EC2 and run
   docker pull <ecr-url>/my-app
   docker run -d -p 80:8000 my-app
   ↓
6. Set up RDS (PostgreSQL)
   ↓
7. Set up ElastiCache (Redis)
   ↓
8. Configure NGINX on EC2
   ↓
9. Point domain to EC2 IP (Route 53)
   ↓
10. Add SSL certificate (AWS Certificate Manager — free!)
    ↓
11. Set up monitoring (CloudWatch)
```

---

## 7. Monitoring — "What's Going On?"

Monitoring is essential in production:

**What to monitor:**
- API response time — is it getting slow?
- Error rate — how many requests are failing?
- CPU/Memory usage — is the server overloaded?
- LLM API costs — how much are we spending?

**Tools:**
- **AWS CloudWatch** — AWS's built-in monitoring
- **Sentry** — Error tracking
- **Grafana** — Beautiful dashboards
- **Simple logging** — Start with this

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/chat")
def chat(request: ChatRequest):
    logger.info(f"Chat request: {request.question[:50]}")
    start_time = time.time()

    response = process(request)

    duration = time.time() - start_time
    logger.info(f"Response time: {duration:.2f}s")

    return response
```

---

## 8. Scaling — "Handling More Users"

**Vertical scaling:** Get a bigger server (more RAM, more CPU)
- Simple but expensive
- Has a limit — a single machine can only get so big

**Horizontal scaling:** Add more servers
- More flexible
- NGINX load balances between them

```
Users → NGINX → FastAPI Instance 1
              → FastAPI Instance 2
              → FastAPI Instance 3
```

**Auto-scaling:** AWS automatically adds/removes servers based on load.

---

## 9. Security Checklist

Before going to production:

- [ ] API keys are in environment variables (not in code)
- [ ] HTTPS is enabled (not HTTP)
- [ ] Database is not publicly accessible
- [ ] Input validation is in place (Pydantic)
- [ ] Rate limiting is configured (block excessive requests)
- [ ] Authentication is in place (JWT tokens)
- [ ] No sensitive data in logs
- [ ] `.env` file is in `.gitignore`

---

## 10. Cost Optimization

AI apps can get expensive. Tips:

**Caching:**
```python
import redis

cache = redis.Redis()

def get_ai_response(question: str) -> str:
    # Check cache first
    cached = cache.get(question)
    if cached:
        return cached.decode()  # Free!

    # Cache miss — call the LLM
    response = llm.invoke(question)
    cache.setex(question, 3600, response)  # Cache for 1 hour
    return response
```

**Model selection:**
- Simple tasks → cheap model (GPT-4o-mini, Llama 3 8B)
- Complex tasks → expensive model (GPT-4, Llama 3 70B)

**Batch processing:**
- Instead of processing one request at a time, batch them together

---

## Summary — The Full Course Recap

| Day | Topic | Key Takeaway |
|-----|-------|-------------|
| 1 | Python Foundations | Variables, lists, dicts, loops, functions |
| 2 | OOP | Classes, inheritance, encapsulation |
| 3 | Data Science | Pandas = Excel's big brother |
| 4 | FastAPI | API = Waiter between client and server |
| 5 | NLP | Text → tokens → embeddings |
| 6 | GenAI | LLM = sophisticated autocomplete |
| 7 | Prompt Engineering | Specific prompt = better output |
| 8 | RAG | Open-book exam for AI |
| 9-10 | Open Source LLMs | Free, private, local AI |
| 11 | LangChain | LEGO kit for AI apps |
| 12 | Agentic AI | AI that acts, not just talks |
| 13 | Prompt Battle | Practice makes perfect |
| 14 | LangGraph | A team of AI agents |
| 15 | Production | From laptop to the real world |

---

## Closing Words

> "15 days ago, you wrote your first Python variable. Today you designed a production-grade AI system and understand how to deploy it to the cloud. That's what senior engineers do.
>
> The AI field moves fast. What's state-of-the-art today might be outdated in 6 months. But the concepts you learned — embeddings, RAG, agents, chains — these are fundamentals. The tools will change, the concepts won't.
>
> Take one problem from your own company. A small one. And try to solve it with AI. That one project will teach you more than 15 days of training.
>
> Build. Ship. Keep learning."
