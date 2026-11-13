# Day 11 — LangChain
**Vibe:** "The LEGO kit for building AI applications."

---

## 🗣️ How to Open This Day

> "Over the last 3 days, we built RAG from scratch — loading documents, chunking, embedding, storing, retrieving. It took 100+ lines of code. Today I'm going to show you how to do the same thing in 20 lines using LangChain. And then we'll build things that would have taken days to build from scratch."

---

## 🧠 Concepts & Human-Language Explanations

### What is LangChain?
**Say this:** "LangChain is like LEGO. You have individual blocks:
- A **Prompt block** (how you talk to the AI)
- An **LLM block** (which AI model to use)
- A **Memory block** (conversation history)
- A **Tool block** (search, calculator, database)
- A **Retriever block** (vector database search)

You snap them together to build a complete AI application. Change one block without rewriting everything."

### The Chain Concept
**Say this:** "A Chain is a sequence of steps. Input goes in, gets processed step by step, output comes out. Like an assembly line."

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Build a chain: Prompt → LLM → Parse output
prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms.")
llm = ChatOllama(model="llama3.2")
parser = StrOutputParser()

chain = prompt | llm | parser   # The | operator chains them together

result = chain.invoke({"topic": "machine learning"})
```

### Memory — "The AI That Remembers"
**Say this:** "By default, every LLM call is stateless — it forgets the previous message. LangChain's Memory components fix this, storing conversation history automatically."

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
# Now the chain remembers previous messages in the conversation
```

### RAG with LangChain — "Compare with Day 8"
**Say this:** "Remember Day 8? We built RAG in 80 lines. Watch this."

```python
# LangChain RAG in ~15 lines
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_texts(chunks, embeddings)
retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
answer = qa_chain.invoke("What is the leave policy?")
```

### Output Parsers — "Getting Structured Data"
**Say this:** "Instead of getting raw text back, you can tell LangChain to parse the output into a Python dictionary, list, or Pydantic model automatically."

```python
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel

class JobInfo(BaseModel):
    role: str
    skills: list[str]
    salary_lpa: int

parser = JsonOutputParser(pydantic_object=JobInfo)
# Now the chain returns a JobInfo object, not a string
```

---

## 💻 Live Coding Demo

**Demo 1:** Rebuild Day 8's RAG chatbot in 20 lines with LangChain  
**Demo 2:** Add conversation memory to the chatbot  
**Demo 3:** Build a document summarizer chain  

See `lab.py`.

---

## 🏋️ Hands-on Challenge

Build a "Multi-Document Q&A System":
- Load 3 different text files (HR policy, product manual, company FAQ)
- Build a RAG chain that searches across all 3
- Add memory so users can ask follow-up questions
- Add a source citation: "This answer is from: HR Policy, page 2"

---

## 📝 Daily Recap Questions

1. "What does the `|` operator do in LangChain?"
2. "Why would you use LangChain instead of building from scratch?"
3. "What is the difference between a Chain and an Agent? (Preview for tomorrow)"

**Key takeaway:** "LangChain is the industry standard for building LLM applications. Every AI startup, every enterprise AI team uses it or something similar. This is a job-market skill."
