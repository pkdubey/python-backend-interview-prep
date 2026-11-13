# Day 10 — Running Open Source LLMs Locally
**Vibe:** "Getting our hands dirty — AI on your own machine."

---

## 🗣️ How to Open This Day

> "Yesterday we understood WHAT open source LLMs are. Today we actually RUN them. By end of today, you'll have a fully functional AI running on your laptop — no internet, no API key, no cost. Forever."

---

## 🧠 Concepts & Human-Language Explanations

### Ollama — "The App Store for LLMs"
**Say this:** "Ollama is like the App Store or Play Store — but for AI models. You type `ollama pull llama3.2` and it downloads and installs the model. Then `ollama run llama3.2` and you're chatting with AI locally."

```bash
# Install a model
ollama pull llama3.2        # 2GB general purpose
ollama pull mistral         # 4GB, great for coding
ollama pull phi3            # 2GB, Microsoft's tiny but smart model

# Run in terminal
ollama run llama3.2

# List installed models
ollama list

# Ollama also runs as an API server at http://localhost:11434
```

### LM Studio — "A GUI for LLMs"
**Say this:** "If Ollama is the command-line tool, LM Studio is the user-friendly desktop app. Great for non-technical team members who want to use AI without touching a terminal."

- Download from: https://lmstudio.ai
- Browse and download models from HuggingFace inside the app
- Chat interface built in
- Can also run as a local API server (OpenAI-compatible!)

### Hardware Requirements
**Say this:** "The bottleneck is RAM, not CPU. GPU makes it faster but isn't required."

| Your Machine | What you can run |
|-------------|-----------------|
| 8 GB RAM | Phi-3 (3.8B), Llama 3.2 3B |
| 16 GB RAM | Llama 3.2 7B, Mistral 7B |
| 32 GB RAM | Llama 3 13B |
| GPU (8GB VRAM) | 7B models run 5-10x faster |

### Connecting Python to Local Ollama
**Say this:** "Ollama runs a REST API on port 11434. Your Python code talks to it exactly like it would talk to OpenAI — just a different URL."

```python
# OpenAI style (paid)
client = OpenAI(api_key="sk-...")
response = client.chat.completions.create(model="gpt-4", ...)

# Ollama style (free, local) — same code structure!
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
response = client.chat.completions.create(model="llama3.2", ...)
```

### Modelfile — "Customizing Your AI"
**Say this:** "You can create a custom AI persona using a Modelfile — like giving the AI a specific job, personality, and rules. Think of it as a permanent system prompt baked into the model."

```dockerfile
# Modelfile
FROM llama3.2

SYSTEM """
You are TechBot, the internal AI assistant for TechCorp India.
You only answer questions about Python, Django, and our internal systems.
Always respond in a professional tone.
If asked about competitors, politely decline.
"""

PARAMETER temperature 0.3
```

```bash
ollama create techbot -f Modelfile
ollama run techbot
```

---

## 💻 Live Coding Demo

1. Live terminal demo: `ollama pull phi3` → `ollama run phi3`
2. Connect Python to Ollama via requests
3. Build a simple CLI chatbot with conversation history
4. Create a custom Modelfile for a "Python Tutor" persona

See `lab.py`.

---

## 🏋️ Hands-on Challenge

Build a "Local AI Code Reviewer":
- Takes a Python function as input
- Sends it to local Ollama
- Returns: bugs found, suggested improvements, time complexity
- Works completely offline

---

## 📝 Daily Recap Questions

1. "What's the difference between Ollama and LM Studio?"
2. "Why would a bank prefer running LLMs locally vs using OpenAI?"
3. "What is a Modelfile used for?"

**Key takeaway:** "You now have a free, private, offline AI on your machine. This is what enterprise AI deployments look like — your data never leaves your infrastructure."
