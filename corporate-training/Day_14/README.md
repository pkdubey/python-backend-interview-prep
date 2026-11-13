# Day 14 — LangGraph & Multi-Agent Systems
**Vibe:** "Building an AI team — where agents collaborate like coworkers."

---

## 🗣️ How to Open This Day

> "Yesterday you saw one AI agent doing multiple tasks. But what if the task is too complex for one agent? What if you need a specialist team — one agent that researches, one that writes, one that reviews? That's Multi-Agent. And LangGraph is how you orchestrate them."

---

## 🧠 Concepts & Human-Language Explanations

### LangChain vs LangGraph
**Say this:**
> "LangChain is a **linear assembly line** — data flows in one direction: A → B → C → Done.
>
> LangGraph is a **team of coworkers** — they can pass work back and forth, loop, make decisions, and even disagree. Like a Writer who writes a draft, an Editor who reviews it, and the Writer who revises based on feedback — back and forth until it's good."

### State — "The Shared Whiteboard"
**Say this:** "In LangGraph, all agents share a 'state' — like a whiteboard in a meeting room. Each agent reads from it, adds to it, and passes it to the next agent. The state is the memory of the entire workflow."

```python
from typing import TypedDict, List

class WorkflowState(TypedDict):
    topic: str           # Input: what to research
    research: str        # Agent 1 fills this
    draft: str           # Agent 2 fills this
    feedback: str        # Agent 3 fills this
    final_post: str      # Agent 2 fills this after revision
    approved: bool       # Agent 3 sets this to True when done
```

### Nodes & Edges — "The Org Chart"
**Say this:** "In LangGraph:
- **Nodes** are agents (or functions) — they do the work
- **Edges** are connections — they define who passes work to whom
- **Conditional Edges** are decisions — 'If the editor approves, publish. If not, revise.'"

```
[Researcher] → [Writer] → [Editor] → approved? 
                  ↑                      |
                  └──── revise ──────────┘
                                         |
                                      [Publisher]
```

### Real-World Multi-Agent Use Cases
**Say this:** "Where does this matter in corporate settings?"

1. **Content Pipeline:** Research Agent → Writing Agent → SEO Agent → Publishing Agent
2. **Code Review:** Code Generator → Security Reviewer → Performance Reviewer → Approver
3. **Customer Support:** Classifier Agent → Specialist Agent (billing/tech/returns) → Escalation Agent
4. **Data Analysis:** Data Fetcher → Analyst → Visualizer → Report Writer

---

## 💻 Live Coding Demo

**Build:** A "Blog Post Generator" multi-agent system:
1. **Researcher Agent** — searches for information on a topic
2. **Writer Agent** — writes a blog post draft
3. **Editor Agent** — reviews and gives feedback
4. **Loop** — Writer revises until Editor approves (max 2 iterations)

**Show the state changing** at each step — this is the key visual.

See `lab.py`.

---

## 🏋️ Hands-on Challenge

Build a "Code Review Pipeline":
- **Agent 1 (Generator):** Writes Python code for a given task
- **Agent 2 (Security Reviewer):** Checks for security issues
- **Agent 3 (Quality Reviewer):** Checks for code quality
- **Decision:** If both reviewers approve → output final code. If not → Generator revises.

---

## 📝 Daily Recap Questions

1. "What's the key difference between LangChain and LangGraph?"
2. "What is 'state' in LangGraph?"
3. "Name a real workflow in your company that could be automated with multi-agent AI."

**Key takeaway:** "Multi-agent systems are how you build AI that handles complex, real-world workflows — not just simple Q&A. This is the cutting edge of AI engineering in 2024-2025."
