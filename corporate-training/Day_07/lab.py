# Day 7 Lab — Prompt Engineering & LLM Apps
import requests, json

def ask_llm(prompt, system="You are a helpful assistant.", temperature=0.3):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user",   "content": prompt},
        ],
        "options": {"temperature": temperature},
        "stream": False,
    })
    return response.json()["message"]["content"]


# ── DEMO 1: Bad vs Good Prompt ───────────────────────────────────────────────
job_desc = """
We are looking for a Python Developer with 3+ years experience.
Must know Django, REST APIs, and PostgreSQL. AWS knowledge is a plus.
Salary: 12-18 LPA. Location: Bangalore. Full-time.
"""

print("=== BAD PROMPT ===")
print(ask_llm(f"Summarize this: {job_desc}"))

print("\n=== ENGINEERED PROMPT ===")
structured_prompt = f"""
Extract information from this job description and return ONLY valid JSON.

Job Description:
{job_desc}

Return this exact JSON structure:
{{
  "role": "job title",
  "experience_years": number,
  "required_skills": ["skill1", "skill2"],
  "nice_to_have": ["skill1"],
  "salary_lpa": {{"min": number, "max": number}},
  "location": "city"
}}
"""
result = ask_llm(structured_prompt, temperature=0.0)
print(result)
try:
    parsed = json.loads(result)
    print("\n✅ Valid JSON parsed successfully!")
    print(f"  Role: {parsed.get('role')}")
    print(f"  Skills: {parsed.get('required_skills')}")
except:
    print("⚠️  JSON parsing failed — refine the prompt")


# ── DEMO 2: Few-Shot Sentiment ────────────────────────────────────────────────
print("\n=== FEW-SHOT SENTIMENT ===")
few_shot_prompt = """
Classify customer reviews. Reply with only: POSITIVE, NEGATIVE, or NEUTRAL.

Review: "Great product, fast delivery!" → POSITIVE
Review: "It's okay, nothing special." → NEUTRAL  
Review: "Broke after one day, terrible!" → NEGATIVE

Review: "Decent quality but a bit overpriced for what it offers." →"""

print(ask_llm(few_shot_prompt, temperature=0.0))


# ── DEMO 3: Chain of Thought ─────────────────────────────────────────────────
print("\n=== CHAIN OF THOUGHT ===")
math_problem = """
A company has 200 employees. 40% work in Engineering. 
25% of Engineering employees are senior. 
Each senior engineer earns ₹2,00,000/month.
What is the total monthly salary bill for senior engineers?

Think step by step, then give the final answer.
"""
print(ask_llm(math_problem, temperature=0.0))


# ── DEMO 4: Meeting Notes Processor ─────────────────────────────────────────
print("\n=== MEETING NOTES PROCESSOR ===")
raw_notes = """
Sprint planning meeting - Nov 15
Attendees: Rahul (dev), Priya (PM), Amit (QA)
We discussed the new payment gateway integration. Rahul will complete the 
API integration by Nov 20. Priya needs to update the requirements doc by 
tomorrow. Amit will set up the test environment. We decided to use Razorpay 
instead of PayU due to better documentation. Next meeting is Nov 22 at 10am.
"""

meeting_prompt = f"""
Process these meeting notes and return ONLY valid JSON:

Notes: {raw_notes}

JSON structure:
{{
  "summary": "2-3 sentence summary",
  "action_items": [{{"task": "...", "owner": "...", "due": "..."}}],
  "decisions": ["decision1", "decision2"],
  "next_meeting": "date and time or null"
}}
"""
print(ask_llm(meeting_prompt, temperature=0.0))
