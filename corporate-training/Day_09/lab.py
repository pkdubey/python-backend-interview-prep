# Day 9 Lab — Open Source LLMs
# pip install requests huggingface_hub transformers torch

import requests

# ── OPTION A: HuggingFace Inference API (free, no GPU needed) ────────────────
HF_TOKEN = "<your-huggingface-token>"  # Get free at huggingface.co/settings/tokens

def ask_hf(prompt, model="mistralai/Mistral-7B-Instruct-v0.3"):
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 200, "temperature": 0.7}
    }
    url = f"https://api-inference.huggingface.co/models/{model}"
    response = requests.post(url, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

# ── OPTION B: Ollama (local, completely free, no internet needed) ─────────────
def ask_ollama(prompt, model="llama3.2"):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False,
    })
    return response.json()["response"]

def ask_ollama_chat(messages, model="llama3.2"):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": model,
        "messages": messages,
        "stream": False,
    })
    return response.json()["message"]["content"]

# ── DEMO 1: List available Ollama models ─────────────────────────────────────
print("=== Available Ollama Models ===")
models = requests.get("http://localhost:11434/api/tags").json()
for m in models.get("models", []):
    size_gb = m.get("size", 0) / 1e9
    print(f"  {m['name']} ({size_gb:.1f} GB)")

# ── DEMO 2: Compare models on same prompt ────────────────────────────────────
prompt = "Explain REST API in 2 sentences for a non-technical manager."

print("\n=== Model Comparison ===")
for model in ["llama3.2", "mistral"]:
    try:
        result = ask_ollama(prompt, model=model)
        print(f"\n[{model}]:\n{result}")
    except Exception as e:
        print(f"\n[{model}]: Not installed. Run: ollama pull {model}")

# ── DEMO 3: Sentiment with HuggingFace pipeline ───────────────────────────────
print("\n=== HuggingFace Sentiment Pipeline ===")
try:
    from transformers import pipeline
    classifier = pipeline("sentiment-analysis",
                          model="distilbert-base-uncased-finetuned-sst-2-english")
    reviews = [
        "This product is absolutely amazing!",
        "Terrible quality, broke in 2 days.",
        "It's okay, nothing special.",
    ]
    results = classifier(reviews)
    for review, result in zip(reviews, results):
        print(f"  [{result['label']} {result['score']:.2f}] {review}")
except Exception as e:
    print(f"  Install transformers and torch: {e}")

# ── DEMO 4: Code Generation with CodeLlama ───────────────────────────────────
print("\n=== Code Generation ===")
code_prompt = "Write a Python function to validate an Indian phone number (10 digits starting with 6-9)."
try:
    code = ask_ollama(code_prompt, model="codellama")
    print(code)
except:
    code = ask_ollama(code_prompt, model="llama3.2")
    print(code)
