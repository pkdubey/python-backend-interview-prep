# Day 6 Lab — Generative AI Fundamentals
# Uses Ollama (free, local) by default. Set USE_OPENAI=True if you have a key.

USE_OPENAI = False  # Flip to True if you have an OpenAI API key

if USE_OPENAI:
    from openai import OpenAI
    client = OpenAI(api_key="<your-openai-api-key>")
    MODEL = "gpt-4o-mini"

    def ask_llm(prompt, temperature=0.7, system="You are a helpful assistant."):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system},
                {"role": "user",   "content": prompt},
            ],
            temperature=temperature,
        )
        return response.choices[0].message.content
else:
    import requests

    def ask_llm(prompt, temperature=0.7, system="You are a helpful assistant."):
        response = requests.post("http://localhost:11434/api/chat", json={
            "model": "llama3.2",
            "messages": [
                {"role": "system", "content": system},
                {"role": "user",   "content": prompt},
            ],
            "options": {"temperature": temperature},
            "stream": False,
        })
        return response.json()["message"]["content"]


# ── DEMO 1: Basic Call ───────────────────────────────────────────────────────
print("=== Basic LLM Call ===")
answer = ask_llm("What is machine learning in 2 sentences?")
print(answer)

# ── DEMO 2: Temperature Effect ───────────────────────────────────────────────
print("\n=== Temperature Comparison ===")
prompt = "Write a one-line tagline for a Python training course."

for temp in [0.0, 0.5, 1.0]:
    result = ask_llm(prompt, temperature=temp)
    print(f"  Temp {temp}: {result}")

# ── DEMO 3: System Prompt ────────────────────────────────────────────────────
print("\n=== System Prompt Effect ===")
user_q = "Tell me about our leave policy."

# Without system prompt
print("Without system prompt:")
print(ask_llm(user_q))

# With system prompt (acts as a company HR bot)
print("\nWith HR system prompt:")
print(ask_llm(user_q, system=(
    "You are an HR assistant for TechCorp India. "
    "The company offers 18 days of paid leave per year. "
    "Always be professional and concise."
)))

# ── DEMO 4: Email Subject Generator ─────────────────────────────────────────
print("\n=== Email Subject Line Generator ===")
email_body = """
Hi team, we are launching a new Python AI training program starting November 17th.
The program is 15 days, 8 hours per day, offline in Bengaluru.
Please register by November 10th.
"""

subjects = ask_llm(
    f"Generate 3 catchy email subject lines for this email:\n{email_body}",
    temperature=0.8
)
print(subjects)

# ── DEMO 5: Hallucination Example ────────────────────────────────────────────
print("\n=== Hallucination Demo ===")
print("Asking about a fake company...")
hallucination = ask_llm(
    "Tell me about XYZ Quantum Technologies, a startup founded in Pune in 2019.",
    temperature=0.7
)
print(hallucination)
print("\n⚠️  Notice: The model invented details about a company that doesn't exist!")
