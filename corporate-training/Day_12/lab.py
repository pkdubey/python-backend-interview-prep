# Day 12 Lab — Agentic AI
# pip install langchain langchain-ollama wikipedia-api

from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from datetime import datetime
import requests

llm = ChatOllama(model="llama3.2", temperature=0)

# ── DEFINE TOOLS ─────────────────────────────────────────────────────────────
@tool
def get_current_datetime(query: str) -> str:
    """Get the current date and time. Use this for any date/time questions."""
    return datetime.now().strftime("Today is %A, %B %d, %Y. Time: %I:%M %p")

@tool
def calculate(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Input: a valid Python math expression like '18 * 5' or '(100 - 30) / 2'.
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error: {e}"

@tool
def search_hr_policy(query: str) -> str:
    """
    Search the company HR policy for information about leaves, WFH, travel, etc.
    Input: a question about HR policy.
    """
    policy = {
        "annual leave": "18 days per year",
        "sick leave": "10 days per year",
        "maternity": "26 weeks for female employees",
        "paternity": "5 days for male employees",
        "wfh": "2 days per week with manager approval, not during probation",
        "travel": "Economy class under 2 hours, hotel ₹5000/night in Tier 1 cities",
        "performance review": "Twice a year — April and October",
    }
    query_lower = query.lower()
    for key, value in policy.items():
        if key in query_lower:
            return f"Policy on '{key}': {value}"
    return "Policy information not found. Please contact HR directly."

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city. Input: city name."""
    # Mock data — in production, call a real weather API
    weather = {
        "bangalore": "Partly cloudy, 24°C",
        "mumbai": "Humid, 30°C",
        "delhi": "Sunny, 22°C",
        "hyderabad": "Clear, 26°C",
    }
    return weather.get(city.lower(), f"Weather data not available for {city}")

tools = [get_current_datetime, calculate, search_hr_policy, get_weather]

# ── CREATE AGENT ──────────────────────────────────────────────────────────────
# Pull the standard ReAct prompt from LangChain Hub
try:
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, react_prompt)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,       # Shows the agent's thinking process
        max_iterations=5,
        handle_parsing_errors=True,
    )

    # ── TEST THE AGENT ────────────────────────────────────────────────────────
    test_queries = [
        "What is today's date?",
        "I have 18 annual leaves. I've taken 7 so far. How many do I have left?",
        "What is the WFH policy?",
        "What's the weather in Bangalore today?",
        "I joined on Jan 1 and it's been 8 months. Am I still in probation? Also what's the WFH policy?",
    ]

    print("="*60)
    print("HR ASSISTANT AGENT")
    print("="*60)

    for query in test_queries[:2]:  # Run first 2 to save time in demo
        print(f"\n{'='*40}")
        print(f"USER: {query}")
        print("="*40)
        result = agent_executor.invoke({"input": query})
        print(f"\nFINAL ANSWER: {result['output']}")

except Exception as e:
    print(f"Agent setup error: {e}")
    print("\nFalling back to direct tool demo...")

    # Direct tool demo if agent fails
    print("\n=== Direct Tool Calls ===")
    print(get_current_datetime("now"))
    print(calculate("18 - 7"))
    print(search_hr_policy("What is the WFH policy?"))
