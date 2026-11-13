# Day 6 Theory — Generative AI Fundamentals
## "It's not magic — it's probability"

---

## 1. What is Generative AI?

Generative AI = AI that generates new content.

- Generating text (ChatGPT)
- Generating images (DALL-E, Midjourney)
- Generating code (GitHub Copilot)
- Generating audio (ElevenLabs)

Today we focus on **text generation** — LLMs.

---

## 2. What is an LLM? — The Autocomplete Analogy

LLM = Large Language Model.

**The simplest explanation:**

An LLM is a very sophisticated **autocomplete**.

Like when you type "Good mor..." on your phone and it suggests "...ning" — an LLM does the same thing, but trained on trillions of words.

```
Input:  "The capital of India is"
LLM:    "New Delhi"  ← most likely next words

Input:  "def calculate_bonus(salary):"
LLM:    "    return salary * 0.10"  ← most likely next line
```

**The key insight:** An LLM doesn't "know" things the way you know your own name. It **predicts** patterns. That's why it can be confidently wrong — a phenomenon called hallucination.

---

## 3. How is an LLM Trained?

In simple steps:

```
Step 1: Collect internet data
        (Wikipedia, books, code, news — trillions of words)

Step 2: Show the model this data
        "Here's a sentence: 'The cat sat on the ___'"
        "Correct answer: 'mat'"

Step 3: Model gives wrong answer → penalize it
        Model gives right answer → reward it

Step 4: Repeat this process billions of times

Step 5: Model learns: "Which word comes in which context"
```

This training takes months, thousands of GPUs, and millions of dollars.

**That's why:** GPT-4's training cost was ~$100 million. That's why open source models matter.

---

## 4. Transformer Architecture — "Attention is All You Need"

In 2017, Google published a paper: "Attention is All You Need"

It introduced a new architecture: **Transformer**

Before Transformers, AI read text one word at a time — left to right. Slow and missed context.

Transformers read the entire sentence at once and decide: "Which word is related to which other word?"

**Example — The Attention Mechanism:**

> "The animal didn't cross the street because **it** was too tired."

What does "it" refer to — the animal or the street?

You know immediately: the animal. Because "tired" applies to living things.

The Attention Mechanism does the same thing — for "it", it pays high attention to "animal" and low attention to "street".

```
"it" → attends to → "animal" (high attention: 0.85)
"it" → attends to → "street" (low attention: 0.05)
```

This mechanism is what allows LLMs to understand context.

---

## 5. Tokens — "The AI's Reading Unit"

LLMs don't read words — they read **tokens**.

A token is roughly 3/4 of a word.

```
"Hello"          → 1 token
"unhappiness"    → 3 tokens: "un" + "happi" + "ness"
"ChatGPT"        → 2 tokens: "Chat" + "GPT"
1000 words       ≈ 750 tokens
```

**Why does this matter?**
- API pricing is based on tokens
- Context window is measured in tokens
- GPT-4: 128,000 tokens = roughly one full novel

```python
# OpenAI pricing example:
# GPT-4o-mini: $0.15 per 1M input tokens
# 1000 words ≈ 750 tokens ≈ $0.0001
# 1 million words ≈ $0.11
```

---

## 6. Context Window — "The AI's Short-term Memory"

Context window = How much text the LLM can "see" at one time.

Like your short-term memory — you can only hold so many things in your head at once.

```
GPT-3.5:  16,000 tokens  ≈ 12,000 words
GPT-4:   128,000 tokens  ≈ 96,000 words  (a full novel!)
Claude:  200,000 tokens  ≈ 150,000 words
Llama 3: 128,000 tokens
```

**The problem:** If a conversation gets very long, older messages fall outside the context window — the AI "forgets" them.

**The solution:** RAG (Day 8) and Memory management (Day 11).

---

## 7. Temperature — "The Creativity Dial"

Temperature controls how "creative" or "random" the AI is.

```
Temperature 0.0 → Always picks the most likely word
                  Predictable, consistent
                  Use: Facts, code, math

Temperature 0.5 → Balanced
                  Use: General chat, summaries

Temperature 1.0 → More random choices
                  Creative, varied
                  Use: Creative writing, brainstorming

Temperature 1.5+ → Very random, sometimes nonsense
```

**Demo:**
```python
prompt = "Complete this: The best programming language is"

# Temperature 0.0 → always: "Python"
# Temperature 1.0 → sometimes "Python", sometimes "JavaScript", sometimes "Rust"
```

---

## 8. Hallucination — "AI's Biggest Problem"

Hallucination = AI confidently gives wrong information.

**Why does it happen?**
LLMs predict — "What word should come here?" Sometimes they generate a believable-sounding answer that is factually wrong.

**Examples:**
- "Abraham Lincoln invented the telephone in 1865" — confidently wrong
- Citing fake research papers
- Citing fake court cases (this actually happened — a lawyer submitted AI-generated fake cases to court!)

**Real world impact:**
- Hallucination in medical advice → dangerous
- In legal documents → lawsuit
- In financial reports → wrong decisions

**Solutions:**
1. **RAG** (Day 8) — Give AI actual documents, it answers from those
2. **Low temperature** — 0.0-0.2 for factual tasks
3. **Verification** — Have a human verify AI's answer
4. **Grounding** — "Only answer based on this document"

---

## 9. System Prompt vs User Prompt

**System Prompt** = Giving the AI a job description. Set before the conversation starts.

**User Prompt** = The actual question or task.

```python
messages = [
    {
        "role": "system",
        "content": "You are an HR assistant for TechCorp India. Only answer HR-related questions. Be professional and concise."
    },
    {
        "role": "user",
        "content": "How many leaves do I get per year?"
    }
]
```

With a system prompt you can:
- Set the AI's persona
- Define rules
- Limit the scope
- Set the tone

---

## 10. Basic LLM API Call

```python
from openai import OpenAI

client = OpenAI(api_key="<your-key>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are helpful."},
        {"role": "user",   "content": "What is Python?"}
    ],
    temperature=0.7,
    max_tokens=500
)

answer = response.choices[0].message.content
print(answer)
```

**Parameters:**
- `model` — which LLM to use
- `messages` — conversation history
- `temperature` — creativity (0-2)
- `max_tokens` — maximum response length

---

## 11. LLM Comparison

| Model | Company | Best for | Cost |
|-------|---------|----------|------|
| GPT-4o | OpenAI | Best quality, general | Paid |
| GPT-4o-mini | OpenAI | Fast, cheap, good quality | Cheap |
| Claude 3.5 | Anthropic | Long documents, coding | Paid |
| Gemini Pro | Google | Multimodal, Google integration | Paid |
| Llama 3 | Meta | Open source, free, private | Free |
| Mistral | Mistral AI | Fast, efficient | Free/Paid |

---

## Summary

| Concept | In One Line |
|---------|------------|
| LLM | Sophisticated autocomplete trained on the internet |
| Transformer | Architecture that reads the whole sentence at once |
| Attention | Figuring out which word relates to which other word |
| Token | AI's reading unit (~3/4 of a word) |
| Context Window | How much the AI can see at one time |
| Temperature | Creativity dial — 0=predictable, 1=creative |
| Hallucination | AI confidently saying something wrong |
| System Prompt | Giving the AI a job description |

**Tomorrow:** We learn how to talk to AI properly — Prompt Engineering.
