# Day 10 Lab — Running Open Source LLMs Locally
# Requires: Ollama running at http://localhost:11434
# Install: https://ollama.com → then: ollama pull llama3.2

import requests
import json

BASE_URL = "http://localhost:11434"

# ── HELPER FUNCTIONS ─────────────────────────────────────────────────────────
def chat(messages, model="llama3.2", temperature=0.7):
    response = requests.post(f"{BASE_URL}/api/chat", json={
        "model": model,
        "messages": messages,
        "options": {"temperature": temperature},
        "stream": False,
    })
    return response.json()["message"]["content"]

def generate(prompt, model="llama3.2"):
    response = requests.post(f"{BASE_URL}/api/generate", json={
        "model": model, "prompt": prompt, "stream": False
    })
    return response.json()["response"]

# ── DEMO 1: List Models ───────────────────────────────────────────────────────
print("=== Installed Models ===")
models = requests.get(f"{BASE_URL}/api/tags").json().get("models", [])
for m in models:
    print(f"  ✅ {m['name']} ({m['size']/1e9:.1f} GB)")

# ── DEMO 2: Simple Chat ───────────────────────────────────────────────────────
print("\n=== Simple Chat ===")
response = chat([{"role": "user", "content": "What is Python in one sentence?"}])
print(response)

# ── DEMO 3: CLI Chatbot with Memory ──────────────────────────────────────────
def run_chatbot():
    print("\n=== Python Tutor Chatbot (type 'quit' to exit) ===")
    history = [{
        "role": "system",
        "content": (
            "You are a friendly Python tutor for corporate professionals. "
            "Explain concepts simply with real business examples. "
            "Keep answers under 5 sentences unless asked for more."
        )
    }]
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye! Keep coding! 🐍")
            break
        if not user_input:
            continue
        history.append({"role": "user", "content": user_input})
        response = chat(history)
        history.append({"role": "assistant", "content": response})
        print(f"\nTutor: {response}")

# ── DEMO 4: Code Reviewer ─────────────────────────────────────────────────────
def review_code(code: str) -> dict:
    prompt = f"""Review this Python code and return ONLY valid JSON:

```python
{code}
```

JSON format:
{{
  "bugs": ["bug1", "bug2"],
  "improvements": ["improvement1"],
  "time_complexity": "O(?)",
  "space_complexity": "O(?)",
  "overall_rating": "Good/Needs Work/Poor"
}}"""
    result = chat(
        [{"role": "user", "content": prompt}],
        temperature=0.1
    )
    try:
        # Extract JSON from response
        start = result.find("{")
        end = result.rfind("}") + 1
        return json.loads(result[start:end])
    except:
        return {"raw_response": result}

print("\n=== Code Review Demo ===")
sample_code = """
def find_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates
"""
review = review_code(sample_code)
print(json.dumps(review, indent=2))

# ── RUN CHATBOT (comment out if running in non-interactive mode) ──────────────
# run_chatbot()
