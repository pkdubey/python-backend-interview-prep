# Day 12 Theory — Agentic AI
## "AI that doesn't just talk — it acts"

---

## 1. LLM vs Agent — Consultant vs Employee

**LLM (without an agent):**
You ask: "What are the best Python training centers in Bangalore?"
LLM says: "Here are some options: 1. ... 2. ..."

But this information could be outdated. The LLM didn't search the internet — it answered from its training data.

**Agent:**
Same question. The agent:
1. "I should search for this" → uses a Google search tool
2. Reads the search results
3. "I should check current reviews" → does another search
4. Compiles all the information
5. Gives an up-to-date, accurate answer

**The analogy:**
- LLM = **Consultant** — gives you advice, you implement it yourself
- Agent = **Employee** — you give them a task, they complete it and bring you the result

---

## 2. Tools — "The Agent's Superpowers"

A tool = A Python function that the agent can call.

```python
from langchain.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the internet for current information."""
    # Actual web search API call
    return search_results

@tool
def calculate(expression: str) -> str:
    """Calculate a math expression. Input: '2 + 2' or '18 * 0.1'"""
    return str(eval(expression))

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return weather_api.get(city)

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email."""
    email_service.send(to, subject, body)
    return "Email sent successfully"
```

You give the agent a list of tools. The agent decides on its own which tool to use and when.

---

## 3. The ReAct Pattern — "The Agent's Brain"

ReAct = **Re**asoning + **Act**ing

The agent works in a loop:

```
THOUGHT → ACTION → OBSERVATION → THOUGHT → ACTION → ...
```

**Example:**
```
User: "What is TCS's current stock price and how much has it changed from last month?"

THOUGHT: "I need the current stock price. I'll use the search tool."
ACTION: search_web("TCS stock price today")
OBSERVATION: "TCS: ₹3,850 (as of today)"

THOUGHT: "Now I need last month's price."
ACTION: search_web("TCS stock price 1 month ago")
OBSERVATION: "TCS was ₹3,650 one month ago"

THOUGHT: "Now I'll calculate the change."
ACTION: calculate("(3850 - 3650) / 3650 * 100")
OBSERVATION: "5.479..."

THOUGHT: "Now I can give the answer."
ANSWER: "TCS's current price is ₹3,850. Last month it was ₹3,650.
         Change: +5.5% increase."
```

**Showing this trace live in class is very impactful** — people can see the AI "thinking."

---

## 4. Agent Types

### ReAct Agent (Most Common)
- Reasoning + Acting loop
- General purpose
- Built into LangChain

### Tool Calling Agent
- Modern LLMs (GPT-4, Llama 3) can call tools directly
- Cleaner, more reliable
- Recommended for production

### Plan-and-Execute Agent
- First builds a complete plan
- Then executes step by step
- For complex, multi-step tasks

---

## 5. Tool Design — Best Practices

**Good tool:**
```python
@tool
def get_employee_info(employee_id: str) -> str:
    """
    Get information about an employee by their ID.
    Returns: name, department, salary, join date.
    Input: employee ID as string (e.g., 'EMP001')
    """
    # Clear description — agent understands when to use this
    employee = db.get(employee_id)
    if not employee:
        return f"Employee {employee_id} not found"
    return f"Name: {employee.name}, Dept: {employee.dept}, Salary: {employee.salary}"
```

**Bad tool:**
```python
@tool
def get_data(x):
    """Get data."""  # Too vague — agent will be confused
    return db.query(x)
```

**Rules for good tools:**
1. **Clear docstring** — The agent reads this to decide when to use the tool
2. **Single responsibility** — One tool, one job
3. **Error handling** — If the tool fails, return a meaningful error message
4. **Type hints** — Input/output types should be clear

---

## 6. Agent Memory

Agents can forget too — just like LLMs.

**Short-term memory:** Within the current conversation/task
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=ConversationBufferMemory()  # Remembers the conversation
)
```

**Long-term memory:** Across conversations
- Store in a vector database
- Save important facts
- Retrieve in the next conversation

---

## 7. Agent Limitations

Agents are powerful but have limitations:

**1. Slow:**
Every tool call = one API call = takes time.
An agent is overkill for a simple task.

**2. Expensive:**
More LLM calls = more tokens = more cost.

**3. Unpredictable:**
Agents sometimes use unexpected tools or in the wrong sequence.

**4. Infinite loops:**
If an agent gets stuck — it can loop forever.
```python
agent_executor = AgentExecutor(
    max_iterations=5,    # Maximum 5 steps — then stop
    handle_parsing_errors=True
)
```

**5. Security:**
An agent can take real actions — send emails, delete files.
Add human approval for dangerous tools.

---

## 8. Human-in-the-Loop

In production, dangerous actions need human approval:

```python
@tool
def delete_employee_record(employee_id: str) -> str:
    """Delete an employee record from the database."""
    # Confirm first
    confirm = input(f"Are you sure you want to delete {employee_id}? (yes/no): ")
    if confirm.lower() != "yes":
        return "Deletion cancelled by user"
    db.delete(employee_id)
    return f"Employee {employee_id} deleted"
```

**Real production pattern:**
- Agent proposes an action
- Human approves or rejects
- Then it executes

---

## 9. Real Corporate Use Cases

**1. IT Support Agent:**
Tools: search_knowledge_base, create_ticket, check_ticket_status, escalate_ticket
User: "My laptop is not connecting to VPN"
Agent: Searches KB → finds solution → if not resolved → creates ticket

**2. HR Query Agent:**
Tools: search_hr_policy, calculate_leave_balance, check_payslip, book_meeting
User: "I have 5 sick leaves left. Can I take 3 days off next week?"
Agent: Checks policy → calculates → confirms availability → books

**3. Sales Intelligence Agent:**
Tools: search_crm, get_company_info, check_competitor_pricing, draft_email
User: "Prepare a proposal for Infosys"
Agent: Gets Infosys info → checks pricing → drafts customized proposal

**4. Code Review Agent:**
Tools: analyze_code, check_security, check_performance, suggest_fixes
User: "Review this Python function"
Agent: Analyzes → checks security → checks performance → gives detailed review

---

## 10. Agent vs Chain — Decision Guide

```
Simple task? → Use Chain
  ↓ No
Multiple fixed steps? → Use Chain with multiple prompts
  ↓ No
Need to use external tools? → Use Agent
  ↓ No
Need to decide WHICH tool to use? → Use Agent
  ↓ No
Need to loop until task is complete? → Use Agent
```

**Rule of thumb:**
- Chain = Predictable, fixed steps
- Agent = Dynamic, decides steps at runtime

---

## Summary

| Concept | In One Line |
|---------|------------|
| Agent | AI that uses tools to complete tasks |
| Tool | A Python function the agent can call |
| ReAct | Thought → Action → Observation loop |
| AgentExecutor | The wrapper that runs the agent |
| max_iterations | A limit to prevent infinite loops |
| Human-in-loop | Human approval for dangerous actions |

**Tomorrow:** Multiple agents working together as a team — LangGraph.
