# Day 9 & 10 Theory — Open Source LLMs
## "Run AI on your own machine — free, private, forever"

---

## 1. OpenAI vs Open Source — An Honest Comparison

**OpenAI (GPT-4, etc.):**
- ✅ Best quality
- ✅ Easy to use
- ✅ No setup required
- ❌ Paid — charged per token
- ❌ Your data goes to their servers
- ❌ Requires internet
- ❌ Has rate limits

**Open Source LLMs:**
- ✅ Free — download once, use forever
- ✅ Private — data never leaves your machine
- ✅ Offline — no internet needed
- ✅ Fully customizable
- ❌ Requires setup
- ❌ Slightly lower quality (improving rapidly)
- ❌ Needs decent hardware

**When to choose open source in a corporate setting:**
- Banks, hospitals, government — data privacy is critical
- High volume usage — costs become very large
- Offline environments — factory floors, remote locations
- Need custom fine-tuning

---

## 2. Popular Open Source Models

### Llama 3 (Meta)
- Built by Meta (Facebook)
- Best general-purpose open source model
- Sizes: 3B, 8B, 70B
- License: Free for most commercial use
- **Use when:** General chatbot, Q&A, summarization

### Mistral 7B
- Built by French startup Mistral AI
- 7B parameters but GPT-3.5 level quality
- Very efficient — does more with less hardware
- **Use when:** Need fast responses, limited hardware

### Phi-3 (Microsoft)
- Built by Microsoft
- Tiny model — 3.8B parameters
- Surprisingly smart for its size
- Runs easily on a laptop
- **Use when:** Very limited hardware, simple tasks

### CodeLlama (Meta)
- Llama specialized for code
- Code generation, debugging, explanation
- **Use when:** Code-related tasks

### Gemma 2 (Google)
- Google's open source model
- Good balance of size and quality
- **Use when:** Working in the Google ecosystem

---

## 3. Model Size — "What Does 7B Mean?"

**B = Billion parameters**

Parameters = The model's "brain cells" — more means smarter.

```
3B  parameters = 3,000,000,000 numbers
7B  parameters = 7,000,000,000 numbers
70B parameters = 70,000,000,000 numbers
```

**Size vs Performance:**

| Size | RAM needed | Speed | Quality | Use case |
|------|-----------|-------|---------|----------|
| 1-3B | 2-4 GB | Very fast | Basic | Simple Q&A |
| 7B | 8 GB | Fast | Good | Most tasks |
| 13B | 16 GB | Medium | Better | Complex reasoning |
| 70B | 40+ GB | Slow | Near GPT-4 | Best quality |

**Practical advice:**
- Laptop (8GB RAM) → Phi-3 or Llama 3.2 3B
- Workstation (16GB RAM) → Llama 3 8B or Mistral 7B
- Server (32GB+ RAM) → Llama 3 70B

---

## 4. Quantization — "Compressing the Model"

**The problem:** Llama 3 8B in full precision needs 32 GB of RAM. Won't run on a laptop.

**The solution:** Quantization — compress the model.

**Analogy:** Like an MP3 audio file is smaller than WAV — slightly less quality, much smaller size.

```
Full precision (FP32): 8B model = 32 GB
Half precision (FP16): 8B model = 16 GB
4-bit quantized (Q4):  8B model = 4-5 GB  ← Runs on a laptop!
```

**Quality loss:**
- Q8 (8-bit): Almost no quality loss
- Q4 (4-bit): Slight quality loss, barely noticeable
- Q2 (2-bit): Noticeable quality loss

**GGUF format** = The standard format for quantized models. Used by Ollama and LM Studio.

---

## 5. Ollama — "The App Store for LLMs"

Ollama is a tool that makes running local LLMs incredibly easy.

**Installation:** https://ollama.com → Download → Install

**Basic commands:**
```bash
# Download a model
ollama pull llama3.2        # ~2 GB download
ollama pull mistral         # ~4 GB download
ollama pull phi3            # ~2 GB download

# Chat in the terminal
ollama run llama3.2
# > Hello! How can I help you?
# Type your message...

# See installed models
ollama list

# Delete a model
ollama rm mistral

# Check server status
ollama serve
```

**Ollama as an API server:**
Ollama automatically runs a REST API server at `http://localhost:11434`

```python
import requests

response = requests.post("http://localhost:11434/api/chat", json={
    "model": "llama3.2",
    "messages": [{"role": "user", "content": "Hello!"}],
    "stream": False
})
print(response.json()["message"]["content"])
```

---

## 6. LM Studio — "Ollama with a GUI"

LM Studio is a desktop application — with a graphical interface.

**Features:**
- Browse and download models from HuggingFace directly inside the app
- Built-in chat interface
- Local API server (OpenAI-compatible)
- Shows hardware requirements before you download

**When to use it:**
- For non-technical team members
- When you want to explore models
- When you prefer a GUI over the terminal

**Download:** https://lmstudio.ai

---

## 7. HuggingFace — "GitHub for AI"

HuggingFace = The repository for AI models.

500,000+ models available. Free to download.

**What to look for on a model card:**

```
Model: meta-llama/Llama-3.2-3B-Instruct
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Downloads: 2.3M/month  ← Popular = reliable
License: Llama 3.2 Community License  ← Check commercial use
Size: 6.43 GB  ← How much storage you need
Tasks: text-generation, conversational  ← What it can do
Languages: English  ← Which languages it supports
```

**HuggingFace Inference API:**
Use models without downloading — free tier available:

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
headers = {"Authorization": "Bearer <your-hf-token>"}

response = requests.post(API_URL, headers=headers, json={
    "inputs": "What is machine learning?",
    "parameters": {"max_new_tokens": 200}
})
print(response.json()[0]["generated_text"])
```

---

## 8. Modelfile — "Building a Custom AI"

In Ollama, you can create your own custom AI model — by baking a system prompt into a base model.

```dockerfile
# Modelfile — save as "Modelfile" (no extension)
FROM llama3.2

SYSTEM """
You are TechBot, the internal AI assistant for TechCorp India.

Your rules:
1. Only answer questions about Python, Django, and our internal systems
2. Always be professional and concise
3. If asked about competitors, politely decline
4. Always suggest consulting official documentation for critical decisions
"""

PARAMETER temperature 0.3
PARAMETER num_ctx 4096
```

```bash
# Create the custom model
ollama create techbot -f Modelfile

# Use it
ollama run techbot
```

**Practical use:** Build a company-specific chatbot that only answers relevant topics.

---

## 9. OpenAI-Compatible API

Both Ollama and LM Studio provide an OpenAI-compatible API.

This means: OpenAI code works with a local model by just changing the URL!

```python
from openai import OpenAI

# OpenAI (paid)
client = OpenAI(api_key="sk-...")
# base_url defaults to: https://api.openai.com/v1

# Ollama (free, local) — just change base_url
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"    # Any string works
)

# This code is identical for both!
response = client.chat.completions.create(
    model="llama3.2",    # or "gpt-4" for OpenAI
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**The benefit:** One codebase, works in both environments. Use Ollama in development, OpenAI in production — or vice versa.

---

## 10. Hardware Tips

**CPU vs GPU:**
- Works on CPU — slow but functional
- GPU makes it 5-10x faster
- NVIDIA GPU is best (CUDA support)
- Apple Silicon (M1/M2/M3) is also very fast

**RAM tips:**
- Model size + 2-3 GB overhead
- 7B model = 4-5 GB (quantized) + 2 GB = ~7 GB RAM minimum
- 16 GB RAM recommended for comfortable use

**Storage:**
- Models are large — 2 GB to 40+ GB
- SSD recommended for faster loading

---

## Summary

| Concept | In One Line |
|---------|------------|
| Open Source LLMs | Free, private, local AI models |
| Model size (7B) | 7 billion parameters — brain cells |
| Quantization | Compressing a model — 32GB → 4GB |
| GGUF | File format for quantized models |
| Ollama | App Store for LLMs — manage from terminal |
| LM Studio | Ollama with a graphical interface |
| HuggingFace | GitHub for AI models |
| Modelfile | Creating a custom AI persona |

**Tomorrow:** We connect all these pieces in one framework — LangChain.
