# Day 11 Lab — LangChain
# pip install langchain langchain-ollama langchain-community chromadb

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOllama(model="llama3.2", temperature=0.3)

# ── DEMO 1: Basic Chain ───────────────────────────────────────────────────────
print("=== Basic Chain ===")
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 2 sentences for a {audience}."
)
chain = prompt | llm | StrOutputParser()

print(chain.invoke({"topic": "REST APIs", "audience": "non-technical manager"}))

# ── DEMO 2: JSON Output Parser ────────────────────────────────────────────────
print("\n=== Structured Output ===")
json_prompt = ChatPromptTemplate.from_template("""
Extract job info from this text and return ONLY valid JSON with keys:
role, experience_years (number), skills (list), location.

Text: {text}
""")
json_chain = json_prompt | llm | JsonOutputParser()

job_text = "Looking for a Senior Python Developer with 5+ years exp in Django and AWS. Location: Bangalore."
result = json_chain.invoke({"text": job_text})
print(result)
print(f"Role: {result.get('role')}, Skills: {result.get('skills')}")

# ── DEMO 3: Conversation with Memory (manual) ─────────────────────────────────
print("\n=== Conversation with Memory ===")
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful Python tutor. Be concise."),
    ("placeholder", "{history}"),
    ("human", "{question}"),
])
chat_chain = chat_prompt | llm | StrOutputParser()

history = []
questions = [
    "What is a decorator in Python?",
    "Can you give me a real-world example of that?",
    "How is it different from inheritance?",
]

for q in questions:
    response = chat_chain.invoke({"history": history, "question": q})
    print(f"\nQ: {q}")
    print(f"A: {response}")
    history.append(HumanMessage(content=q))
    history.append(AIMessage(content=response))

# ── DEMO 4: RAG with LangChain (compare with Day 8's 80 lines) ───────────────
print("\n=== RAG with LangChain ===")
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.runnables import RunnablePassthrough

HR_CHUNKS = [
    "Employees get 18 days annual leave per year.",
    "Sick leave: 10 days per year. Medical certificate needed for 2+ consecutive days.",
    "Maternity leave: 26 weeks for female employees.",
    "WFH allowed up to 2 days per week with manager approval.",
    "WFH not allowed during probation (first 6 months).",
    "Performance reviews in April and October every year.",
    "Travel: Economy class for flights under 2 hours.",
]

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_texts(HR_CHUNKS, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

rag_prompt = ChatPromptTemplate.from_template("""
Answer using ONLY the context. If not in context, say "Not in policy document."

Context: {context}
Question: {question}
""")

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

for question in ["How many sick leaves do I get?", "What is the stock option policy?"]:
    print(f"\nQ: {question}")
    print(f"A: {rag_chain.invoke(question)}")
