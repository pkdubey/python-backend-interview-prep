# Day 11 Theory — LangChain
## "The LEGO kit for building AI applications"

---

## 1. Why Do We Need LangChain?

Until now we've done everything manually:
- OpenAI API call → 20 lines
- RAG pipeline → 80 lines
- Conversation memory → 30 lines
- Output parsing → 20 lines

We have to write all of this every time. And when you change the model — rewrite everything.

**LangChain's solution:**
- Provides standard building blocks
- Change the model — change one line
- RAG → 15 lines
- Memory → 3 lines
- Chains → connect with the `|` operator

---

## 2. The LEGO Analogy

LangChain = A LEGO kit.

```
LEGO blocks:          LangChain blocks:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Red block    →        Prompt Template
Blue block   →        LLM (GPT/Llama/Mistral)
Green block  →        Output Parser
Yellow block →        Retriever (Vector DB)
Orange block →        Memory
Purple block →        Tool
```

Snap them together to build any AI application.

---

## 3. Core Components

### PromptTemplate
Reusable prompts with variables.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms for a {audience}."
)

# Use it
formatted = prompt.format_messages(
    topic="machine learning",
    audience="HR manager"
)
```

### LLM
Any model — same interface.

```python
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

# Local model
llm = ChatOllama(model="llama3.2", temperature=0.3)

# OpenAI model — same interface!
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# Same code works for both
response = llm.invoke("What is Python?")
```

### Output Parser
Convert the response into a useful format.

```python
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

# String output
parser = StrOutputParser()    # Raw text

# JSON output
parser = JsonOutputParser()   # Python dict
```

---

## 4. Chain — The "|" Operator

Chain = Connecting components into a pipeline.

```python
chain = prompt | llm | parser
```

Reading this out loud:
```
User input → Prompt Template → LLM → Output Parser → Final result
```

**Example:**
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "Summarize this in 3 bullet points:\n{text}"
)
llm = ChatOllama(model="llama3.2")
parser = StrOutputParser()

chain = prompt | llm | parser

result = chain.invoke({"text": "Long meeting notes here..."})
print(result)
```

**Why the `|` operator?**
Like Unix pipes — `cat file.txt | grep "error" | sort`
Data flows from one component to the next.

---

## 5. LCEL — LangChain Expression Language

The `|` operator is part of LCEL.

**Benefits:**
- Readable — left to right flow
- Composable — chains can be combined
- Streaming support — real-time output
- Async support — parallel execution

```python
# Simple chain
chain1 = prompt1 | llm | parser

# Combine chains
chain2 = prompt2 | llm | parser

# Sequential
full_chain = chain1 | chain2

# Parallel (both run at the same time)
from langchain_core.runnables import RunnableParallel
parallel = RunnableParallel(
    summary=chain1,
    keywords=chain2
)
```

---

## 6. Memory — "AI That Remembers"

By default, every LLM call is stateless — it forgets the previous message.

```python
# Without memory
llm.invoke("My name is Rahul")
llm.invoke("What is my name?")  # AI: "I don't know your name"
```

With LangChain memory:
```python
from langchain_core.messages import HumanMessage, AIMessage

# Manually maintain history (simplest approach)
history = []

def chat_with_memory(user_message):
    history.append(HumanMessage(content=user_message))

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("placeholder", "{history}"),
        ("human", "{input}"),
    ])

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"history": history[:-1], "input": user_message})

    history.append(AIMessage(content=response))
    return response

chat_with_memory("My name is Rahul")
chat_with_memory("What is my name?")  # AI: "Your name is Rahul"
```

---

## 7. Retriever — "The Vector DB Interface"

Retriever = A standard interface for fetching relevant documents from a vector database.

```python
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

# Create vector store
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_texts(documents, embeddings)

# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}    # Top 3 results
)

# Use it
docs = retriever.invoke("maternity leave policy")
```

**Retriever types:**
- `similarity` — Most similar chunks (default)
- `mmr` — Maximum Marginal Relevance — diverse results
- `similarity_score_threshold` — Minimum similarity score required

---

## 8. RAG Chain with LangChain

Day 8 took 80 lines. Now it takes 15:

```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template("""
Answer using ONLY the context below.
If not in context, say "Not in documents."

Context: {context}
Question: {question}
""")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

answer = rag_chain.invoke("How many sick leaves do I get?")
```

**`RunnablePassthrough()`** = "Pass the question through as-is" — both to the retriever and to the prompt.

---

## 9. Structured Output

LangChain + Pydantic = Guaranteed structured output.

```python
from pydantic import BaseModel
from langchain_core.output_parsers import JsonOutputParser

class JobInfo(BaseModel):
    role: str
    experience_years: int
    skills: list[str]
    location: str

parser = JsonOutputParser(pydantic_object=JobInfo)

prompt = ChatPromptTemplate.from_template("""
Extract job info from this text.
{format_instructions}

Text: {text}
""")

chain = prompt | llm | parser

result = chain.invoke({
    "text": "Looking for Senior Python Dev, 5+ years, Django/AWS, Bangalore",
    "format_instructions": parser.get_format_instructions()
})

# result is a JobInfo object!
print(result.role)        # "Senior Python Developer"
print(result.skills)      # ["Django", "AWS"]
```

---

## 10. LangChain vs Raw API Calls

| Feature | Raw API | LangChain |
|---------|---------|-----------|
| Switch model | Rewrite code | Change 1 line |
| RAG | 80 lines | 15 lines |
| Memory | Manual | Built-in |
| Structured output | Manual parsing | Automatic |
| Error handling | Manual | Built-in |
| Streaming | Complex | Simple |
| Testing | Hard | Easy |

---

## 11. When NOT to Use LangChain

LangChain isn't always the best choice:

- **Simple one-off API call** → Direct API call is better
- **Maximum performance** → LangChain has overhead
- **Very custom logic** → Sometimes raw code is cleaner
- **Learning** → Understand raw APIs first, then LangChain

**Rule:** When the application is complex, has multiple components, and maintainability matters → use LangChain.

---

## Summary

| Concept | In One Line |
|---------|------------|
| LangChain | LEGO kit for building AI applications |
| PromptTemplate | Reusable prompt with variables |
| Chain (`\|`) | Connecting components into a pipeline |
| Memory | Maintaining conversation history |
| Retriever | Fetching documents from a vector DB |
| LCEL | Building chains with the `\|` operator |
| Structured Output | Guaranteed JSON output with Pydantic |

**Tomorrow:** Agents — AI that doesn't just talk, it acts.
