# Day 13 — Prompt Battle Starter
# Each participant uses this file to test their prompts

import requests

def ask(prompt: str, system: str = "You are a helpful assistant.", temperature: float = 0.7) -> str:
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

# ── ROUND 1: Email Challenge ──────────────────────────────────────────────────
print("=== ROUND 1: Email Challenge ===")
# TODO: Write your prompt here
your_prompt_round1 = """
Write a professional email declining a job offer from TechCorp India.
The role was Senior Python Developer. I'm declining because I accepted another offer.
Keep the tone warm and keep the door open for future opportunities.
Format: Subject line + email body. Under 150 words.
"""
print(ask(your_prompt_round1))

# ── ROUND 2: Code Challenge ───────────────────────────────────────────────────
print("\n=== ROUND 2: Code Challenge ===")
# TODO: Write your prompt here
your_prompt_round2 = """
Write a Python function with these exact requirements:
- Function name: get_top_earners_by_dept
- Input: list of dicts with keys 'name', 'department', 'salary'
- Output: dict where key=department, value=list of top 3 earners (sorted by salary desc)
- Handle: empty list, missing keys (use .get() with defaults)
- Include: type hints, docstring with example
- No external libraries, pure Python only
"""
print(ask(your_prompt_round2, temperature=0.1))

# ── ROUND 3: Customer Support Bot ────────────────────────────────────────────
print("\n=== ROUND 3: Customer Support Bot ===")
# TODO: Write your SYSTEM PROMPT here
system_prompt_round3 = """
You are Aria, a customer support agent for ShopEasy, an Indian e-commerce platform.

Rules:
1. Always greet with "Hi! I'm Aria from ShopEasy."
2. Handle: returns (7-day policy), refunds (3-5 business days), order tracking
3. If customer is angry, acknowledge their frustration first, then help
4. If issue cannot be resolved, say: "I'm connecting you to a senior agent. Please hold."
5. Respond in the SAME language the customer uses
6. Never make up order details — ask for order ID first
"""

test_messages = [
    "My order hasn't arrived in 10 days! This is ridiculous!",
    "Mujhe apna order track karna hai. Order ID: 12345",
    "I want to return a product I bought last week.",
]

for msg in test_messages:
    print(f"\nCustomer: {msg}")
    print(f"Aria: {ask(msg, system=system_prompt_round3, temperature=0.3)}")
    print("-"*40)
