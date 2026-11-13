# Day 14 Theory — LangGraph & Multi-Agent Systems
## "From one agent to a team of agents"

---

## 1. LangChain vs LangGraph — Assembly Line vs Team

**LangChain Chain:**
```
Input → Step 1 → Step 2 → Step 3 → Output
```
Linear. One direction. Can't go back.

Like a **factory assembly line** — the car moves in one direction only.

**LangGraph:**
```
         ┌──────────────┐
Input → Node A → Node B → Node C → Output
              ↑              │
              └──────────────┘
              (loop back if needed)
```
Non-linear. Loops are possible. Conditions are possible. Multiple agents.

Like a **team of coworkers** — a Writer writes a draft, an Editor reviews it, if it's not good enough the Writer revises it. Back and forth until it's right.

---

## 2. Core Concepts

### State — "The Shared Whiteboard"

State = The shared memory of all agents.

Like a whiteboard in a meeting room — anyone can write on it, anyone can read it.

```python
from typing import TypedDict

class WorkflowState(TypedDict):
    topic: str           # Input
    research: str        # Agent 1 will fill this
    draft: str           # Agent 2 will fill this
    feedback: str        # Agent 3 will fill this
    approved: bool       # Agent 3 will set this
    final_output: str    # The final result
```

Each agent:
1. Reads from the state
2. Does its work
3. Updates the state
4. Passes it to the next agent

### Nodes — "Team Members"

A node = An agent or function that does some work.

```python
def researcher_agent(state: WorkflowState) -> WorkflowState:
    # Read topic from state
    topic = state["topic"]
    # Do the research
    research = llm.invoke(f"Research {topic}")
    # Update state
    state["research"] = research
    return state

def writer_agent(state: WorkflowState) -> WorkflowState:
    research = state["research"]
    draft = llm.invoke(f"Write based on: {research}")
    state["draft"] = draft
    return state
```

### Edges — "Who Gets the Work Next"

An edge = The connection from one node to another.

```python
workflow.add_edge("researcher", "writer")    # After Researcher → Writer
workflow.add_edge("writer", "editor")        # After Writer → Editor
```

### Conditional Edges — "Decision Points"

```python
def should_continue(state: WorkflowState) -> str:
    if state["approved"]:
        return "publish"    # Approved → publish
    else:
        return "revise"     # Not approved → back to writer

workflow.add_conditional_edges(
    "editor",           # After this node
    should_continue,    # This function decides
    {
        "publish": "publisher",   # "publish" → publisher node
        "revise": "writer"        # "revise" → writer node (loop!)
    }
)
```

---

## 3. Complete Graph Structure

```python
from langgraph.graph import StateGraph, END

workflow = StateGraph(WorkflowState)

# Add nodes
workflow.add_node("researcher", researcher_agent)
workflow.add_node("writer", writer_agent)
workflow.add_node("editor", editor_agent)
workflow.add_node("publisher", publisher_agent)

# Set entry point
workflow.set_entry_point("researcher")

# Add edges
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "editor")
workflow.add_conditional_edges("editor", should_continue, {...})
workflow.add_edge("publisher", END)

# Compile
app = workflow.compile()

# Run
result = app.invoke({"topic": "Python for AI", "research": "", ...})
```

---

## 4. Real World Patterns

### Pattern 1: Review Loop
```
Generator → Reviewer → Approved? → Yes: Done
                              ↓ No
                         Generator (revise)
```

Use case: Code generation, content writing, report generation

### Pattern 2: Parallel Processing
```
Input → ┌→ Agent A (fast task) ─┐
        └→ Agent B (slow task) ─┴→ Combine → Output
```

Use case: When both tasks are independent — run them simultaneously, save time

### Pattern 3: Routing
```
Input → Classifier → ┌→ Technical Agent
                     ├→ Billing Agent
                     └→ General Agent
```

Use case: Customer support — classify first, then route to the right specialist

### Pattern 4: Supervisor
```
User → Supervisor Agent → ┌→ Research Agent
                          ├→ Writing Agent
                          └→ Analysis Agent
                          ↑
                          └── Results go back to supervisor
```

Use case: Complex tasks where a supervisor decides which specialist to use and when

---

## 5. State Management — Important Details

**State is mutable:**
```python
def my_agent(state: WorkflowState) -> WorkflowState:
    # Modify state directly
    state["draft"] = "New draft content"
    state["revision_count"] = state.get("revision_count", 0) + 1
    return state
```

**Partial updates:**
```python
# Return only the changed fields
def my_agent(state):
    return {"draft": "New content"}  # Only draft gets updated
```

**State history:**
LangGraph automatically saves the state at every step — very useful for debugging.

---

## 6. Streaming — Real-time Output

LangGraph supports streaming — users don't have to wait:

```python
for event in app.stream(initial_state):
    for node_name, node_output in event.items():
        print(f"\n[{node_name}] working...")
        if "draft" in node_output:
            print(f"Draft: {node_output['draft'][:100]}...")
```

---

## 7. LangGraph vs LangChain — When to Use What

| Situation | Use |
|-----------|-----|
| Linear pipeline | LangChain Chain |
| Simple RAG | LangChain |
| One agent with tools | LangChain AgentExecutor |
| Multiple agents | LangGraph |
| Loops needed | LangGraph |
| Complex state | LangGraph |
| Human-in-loop | LangGraph |
| Production workflows | LangGraph |

---

## 8. Multi-Agent Benefits

**Specialization:**
One agent trying to do everything vs. each agent being an expert at one thing.

```
Bad:  One agent does research + writing + editing + publishing
Good: Research Agent + Writing Agent + Editing Agent + Publishing Agent
```

**Parallelism:**
Run independent tasks simultaneously.

**Quality control:**
One agent checks another's work.

**Scalability:**
More work? Add more agents.

---

## 9. Real Corporate Example — Code Review Pipeline

```
Developer submits code
        ↓
[Syntax Checker Agent]
        ↓
[Security Reviewer Agent] ←──────────────┐
        ↓                                │
[Performance Reviewer Agent]             │
        ↓                                │
[Decision Agent]                         │
  ↓ Approved                ↓ Rejected   │
[Deploy Agent]         [Developer Agent] ┘
                       (fixes issues)
```

**State:**
```python
class CodeReviewState(TypedDict):
    code: str
    syntax_issues: list
    security_issues: list
    performance_issues: list
    approved: bool
    fixed_code: str
    revision_count: int
```

---

## 10. Debugging LangGraph

**Verbose mode:**
```python
app = workflow.compile()
# LangGraph automatically logs each node execution
```

**State inspection:**
```python
result = app.invoke(initial_state)
# result contains the final state — inspect any field
print(result["revision_count"])
print(result["approved"])
```

**Checkpointing:**
```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
app = workflow.compile(checkpointer=checkpointer)

# A snapshot is saved at every step
# You can resume from any point
```

---

## Summary

| Concept | In One Line |
|---------|------------|
| LangGraph | Multi-agent workflows with loops and conditions |
| State | The shared whiteboard for all agents |
| Node | An agent or function |
| Edge | The connection from one node to another |
| Conditional Edge | A decision point — where to go next |
| END | The workflow is complete |
| Streaming | Real-time output as agents work |

**Tomorrow:** We bring everything together into one production app — Capstone.
