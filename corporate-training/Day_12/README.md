# Day 12 — Agentic AI (0.8 day)
**Vibe:** "AI that takes action, not just talks."

---

## 🗣️ How to Open This Day

> "Everything we've built so far — the AI answers questions. But what if the AI could DO things? Search the web, run code, send emails, query a database? That's an Agent. Today we build AI that acts."

---

## 🧠 Concepts & Human-Language Explanations

### LLM vs Agent — The Consultant vs Employee Analogy
**Say this:**
> "A standard LLM is like a **consultant** — you ask a question, it gives advice, you go implement it yourself.
>
> An **Agent** is like an **employee** — you give it a goal, it figures out the steps, uses tools (search, calculator, email), and completes the task. You just review the result."

### How Agents Work — ReAct Pattern
**Say this:** "Agents use a loop called ReAct (Reasoning + Acting):"

```
1. THINK: "What do I need to do to answer this?"
2. ACT:   "I'll use the search tool to find current data"
3. OBSERVE: "Here's what the search returned"
4. THINK: "Now I have the data, I can calculate the answer"
5. ACT:   "I'll use the calculator tool"
6. OBSERVE: "Result is 42"
7. ANSWER: "The answer is 42"
```

**Show this trace live** — it's the most impressive demo of the day.

### Tools — "The Agent's Superpowers"
**Say this:** "A tool is just a Python function that the agent can choose to call. You define the function, describe what it does, and the agent decides when to use it."

```python
from langchain.tools import tool

@tool
def get_stock_price(company: str) -> str:
    """Get the current stock price for a company. Input: company name."""
    # In real life, call a stock API
    prices = {"TCS": "₹3,850", "Infosys": "₹1,920", "Wipro": "₹480"}
    return prices.get(company, "Company not found")

@tool
def calculate(expression: str) -> str:
    """Calculate a mathematical expression. Input: math expression as string."""
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"
```

### When to Use Agents
**Say this:** "Use agents when:
- The task requires multiple steps that depend on each other
- You don't know in advance which tools will be needed
- The task involves real-world actions (search, API calls, file operations)

Don't use agents when:
- A simple prompt or chain is enough
- You need 100% predictable, deterministic behavior
- Latency is critical (agents are slower)"

---

## 💻 Live Coding Demo

**Build:** A "Research Assistant" agent that:
1. Takes a topic as input
2. Searches Wikipedia for information
3. Calculates any numbers mentioned
4. Summarizes the findings

**Show the agent's "thinking" trace** — this is what impresses corporate audiences.

See `lab.py`.

---

## 🏋️ Hands-on Challenge (shorter — 0.8 day)

Build a "HR Query Agent" that can:
- Answer questions from the HR policy (RAG tool)
- Calculate leave balance (calculator tool)
- Tell current date/time (datetime tool)

---

## 📝 Daily Recap Questions

1. "What's the difference between a Chain and an Agent?"
2. "What is the ReAct pattern?"
3. "Name 3 real-world use cases for AI agents in your company."

**Key takeaway:** "Agents are the future of AI automation. Instead of building separate scripts for each task, you build one agent with multiple tools. It figures out which tool to use."
