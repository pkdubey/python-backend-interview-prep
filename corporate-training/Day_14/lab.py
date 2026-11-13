# Day 14 Lab — LangGraph & Multi-Agent
# pip install langgraph langchain-ollama

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

llm = ChatOllama(model="llama3.2", temperature=0.5)

# ── STATE: The shared whiteboard ──────────────────────────────────────────────
class BlogState(TypedDict):
    topic: str
    research: str
    draft: str
    feedback: str
    revision_count: int
    approved: bool
    final_post: str

# ── AGENT NODES ───────────────────────────────────────────────────────────────
def researcher(state: BlogState) -> BlogState:
    print("\n🔍 Researcher Agent working...")
    response = llm.invoke([HumanMessage(content=(
        f"Research the topic '{state['topic']}' and provide 5 key facts "
        f"in bullet points. Be concise and factual."
    ))])
    state["research"] = response.content
    print(f"  Research done: {len(state['research'])} chars")
    return state

def writer(state: BlogState) -> BlogState:
    print("\n✍️  Writer Agent working...")
    context = f"Research:\n{state['research']}"
    if state.get("feedback"):
        context += f"\n\nEditor Feedback to address:\n{state['feedback']}"

    response = llm.invoke([HumanMessage(content=(
        f"Write a short blog post (3 paragraphs) about '{state['topic']}' "
        f"for a corporate audience.\n\n{context}"
    ))])
    state["draft"] = response.content
    state["revision_count"] = state.get("revision_count", 0) + 1
    print(f"  Draft written (revision #{state['revision_count']})")
    return state

def editor(state: BlogState) -> BlogState:
    print("\n📝 Editor Agent reviewing...")
    response = llm.invoke([HumanMessage(content=(
        f"Review this blog post draft. Reply with ONLY:\n"
        f"DECISION: APPROVED or NEEDS_REVISION\n"
        f"FEEDBACK: (if needs revision, specific feedback in 2 sentences)\n\n"
        f"Draft:\n{state['draft']}"
    ))])

    review = response.content
    state["approved"] = "APPROVED" in review.upper()
    state["feedback"] = review

    if state["approved"]:
        state["final_post"] = state["draft"]
        print("  ✅ Editor APPROVED the draft!")
    else:
        print(f"  ❌ Editor requested revision: {review[:100]}...")
    return state

def should_continue(state: BlogState) -> str:
    """Conditional edge: approve or revise (max 2 revisions)"""
    if state["approved"]:
        return "publish"
    if state.get("revision_count", 0) >= 2:
        print("\n⚠️  Max revisions reached. Publishing as-is.")
        state["final_post"] = state["draft"]
        return "publish"
    return "revise"

def publisher(state: BlogState) -> BlogState:
    print("\n🚀 Publisher Agent: Post is ready!")
    return state

# ── BUILD THE GRAPH ───────────────────────────────────────────────────────────
workflow = StateGraph(BlogState)

workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)
workflow.add_node("editor", editor)
workflow.add_node("publisher", publisher)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", "editor")
workflow.add_conditional_edges(
    "editor",
    should_continue,
    {"publish": "publisher", "revise": "writer"}
)
workflow.add_edge("publisher", END)

app = workflow.compile()

# ── RUN THE WORKFLOW ──────────────────────────────────────────────────────────
print("="*60)
print("BLOG POST GENERATOR — Multi-Agent Workflow")
print("="*60)

initial_state = BlogState(
    topic="Why Python is the best language for AI development",
    research="",
    draft="",
    feedback="",
    revision_count=0,
    approved=False,
    final_post="",
)

final_state = app.invoke(initial_state)

print("\n" + "="*60)
print("FINAL BLOG POST:")
print("="*60)
print(final_state["final_post"])
print(f"\n📊 Stats: {final_state['revision_count']} revision(s), Approved: {final_state['approved']}")
