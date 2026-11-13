# Day 1 — Python Foundations
**Vibe:** "Learning the alphabet and grammar of a new language."

---

## 🗣️ How to Open This Day (Trainer Script)

> "Raise your hand if you've used Excel formulas before."  
> *(Everyone raises hand)*  
> "Great. Python is just Excel formulas — but 100x more powerful. And today, you'll write your first ones."

---

## 🧠 Concepts & Human-Language Explanations

### Variables
**Say this:** "A variable is a labeled box. You put something in it, give it a name, and use it later."
```python
name = "Rahul"       # Box labeled 'name', contains "Rahul"
salary = 75000       # Box labeled 'salary', contains 75000
```

### Data Types
**Say this:** "Python needs to know what KIND of thing is in the box."

| Type | Real-world analogy | Example |
|------|-------------------|---------|
| `str` | A name tag | `"Pavan"` |
| `int` | A whole number on a form | `42` |
| `float` | A price tag | `99.99` |
| `bool` | A Yes/No checkbox | `True` |

### Lists
**Say this:** "A list is like a train. Each compartment holds one item. You can add/remove compartments."
```python
employees = ["Rahul", "Priya", "Amit"]
employees[0]   # "Rahul" — first compartment
employees.append("Neha")  # Add a new compartment
```

### Dictionaries
**Say this:** "A dictionary is a phonebook. You look up a NAME (key) to get a NUMBER (value)."
```python
employee = {
    "name": "Rahul",
    "department": "Engineering",
    "salary": 75000
}
employee["department"]  # "Engineering"
```

### Loops
**Say this:** "A loop is like telling your intern: 'Do this task for every item in this list. Don't stop till you're done.'"
```python
for emp in employees:
    print(f"Sending email to {emp}")
```

### Functions
**Say this:** "A function is a recipe. You write it once, use it 100 times. Change the ingredients (inputs), get different food (output)."
```python
def calculate_bonus(salary, percentage):
    return salary * percentage / 100

calculate_bonus(75000, 10)  # 7500.0
```

---

## 💻 Live Coding Demo (10:45 – 1:00)

**Scenario:** "You're an HR manager. You have a list of employees and their salaries. Let's write Python to process this."

```python
employees = [
    {"name": "Rahul", "salary": 75000, "dept": "Engineering"},
    {"name": "Priya", "salary": 60000, "dept": "Marketing"},
    {"name": "Amit",  "salary": 90000, "dept": "Engineering"},
    {"name": "Neha",  "salary": 55000, "dept": "HR"},
]

# Task 1: Print all names
for emp in employees:
    print(emp["name"])

# Task 2: Find employees earning more than 65000
high_earners = [e for e in employees if e["salary"] > 65000]

# Task 3: Calculate total salary bill
total = sum(e["salary"] for e in employees)
print(f"Total salary bill: ₹{total:,}")

# Task 4: Give 10% bonus to Engineering dept
for emp in employees:
    if emp["dept"] == "Engineering":
        emp["bonus"] = emp["salary"] * 0.10
```

---

## 🏋️ Hands-on Challenge (2:00 – 4:30)

**Mini Project: Shopping Cart Calculator**

```
Build a program that:
1. Has a list of items with name and price
2. Asks user to add items to cart
3. Calculates total, applies 18% GST
4. Prints final bill
```

Starter code is in `lab.ipynb`.

---

## 📝 Daily Recap (4:30 – 5:00)

Ask the class:
1. "What's the difference between a list and a dictionary? Give me a real-world example."
2. "When would you use a loop?"
3. "What did we build today?"

**Key takeaway to say:** "You just wrote real Python code that processes data. This is literally what data engineers do every day — just at a bigger scale."

---

## ❓ Common Questions & Answers

**Q: Why Python and not Java/C++?**  
A: "Python reads like English. `if salary > 50000` — you don't need a computer science degree to understand that. That's why it won."

**Q: Do I need to memorize all this?**  
A: "No. Google is your best friend. Even senior engineers Google syntax. What matters is knowing WHAT to Google."
