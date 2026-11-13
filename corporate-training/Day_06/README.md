# Day 6 — Generative AI Fundamentals
**Vibe:** "The magic begins — but let's understand the trick."

---

## 🗣️ How to Open This Day

> "ChatGPT came out in November 2022. In 2 months, it had 100 million users. No product in history grew that fast. Today we're going to understand HOW it works — not the math, but the intuition. Because if you're going to build with it, you need to know what's happening under the hood."

---

## 🧠 Concepts & Human-Language Explanations

### What is an LLM?
**Say this:** "An LLM (Large Language Model) is, at its core, a very sophisticated autocomplete. It was trained on billions of web pages, books, and code. When you type a prompt, it predicts: 'What word is most likely to come next?' — over and over, until it forms a complete response."

**The key insight:** "It doesn't 'know' facts the way you know your name. It knows PATTERNS. That's why it can be confidently wrong — a phenomenon called hallucination."

### Transformer Architecture (Plain English)
**Say this:** "Before Transformers (2017), AI read text like you read a book — left to right, one word at a time. Transformers changed this: they read the ENTIRE sentence at once and figure out which words are related to which other words."

**The Attention Mechanism — Show this example:**
> "The animal didn't cross the street because **it** was too tired."

Ask the class: "What does 'it' refer to — the animal or the street?"

> "You knew immediately it's the animal. How? Because 'tired' relates to living things. Attention Mechanism is how the AI figures out the same thing — it 'pays attention' to the most relevant words."

### Tokens vs Words
**Say this:** "LLMs don't read words — they read tokens. A token is roughly 3/4 of a word. 'unhappiness' might be 3 tokens: 'un', 'happi', 'ness'. This matters because APIs charge per token."

```
"Hello, how are you?" = ~5 tokens
1000 words ≈ 750 tokens
GPT-4 context window = 128,000 tokens ≈ 100,000 words ≈ a full novel
```

### Temperature — "The Creativity Dial"
**Say this:** "Temperature controls how 'creative' or 'random' the model is."

| Temperature | Behavior | Use case |
|-------------|----------|----------|
| 0.0 | Always picks the most likely word | Factual Q&A, code generation |
| 0.7 | Balanced | General chat |
| 1.0+ | Very creative/random | Creative writing, brainstorming |

```python
# Low temp = predictable
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    temperature=0.0   # Always says "4"
)

# High temp = creative
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write a poem about Python"}],
    temperature=0.9   # Different poem every time
)
```

### Hallucination
**Say this:** "Because LLMs predict patterns, not facts, they sometimes confidently make things up. Ask it about a fake person — it'll invent a biography. This is the #1 problem in production AI systems. Days 7 and 8 are about solving this."

---

## 💻 Live Coding Demo

**Demo 1:** Basic OpenAI API call  
**Demo 2:** Same prompt, temperature 0 vs temperature 1 — show the difference  
**Demo 3:** Show hallucination — ask about a fake company/person  

See `lab.py`.

---

## 🏋️ Hands-on Challenge

1. Call the API with 3 different temperatures for the same creative prompt
2. Build a simple "Email Subject Line Generator" — give it email body, it generates 3 subject line options
3. Try to make it hallucinate — then discuss: how would you prevent this in production?

---

## 📝 Daily Recap Questions

1. "In one sentence: what does an LLM actually do?"
2. "What is hallucination and why does it happen?"
3. "When would you use temperature=0 vs temperature=0.9?"

**Key takeaway:** "LLMs are powerful but not magic. They're pattern matchers. Understanding this helps you use them correctly — and know when NOT to trust them."
