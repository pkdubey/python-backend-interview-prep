# Day 1 Theory — Python Foundations
## "Today we learn a new language — but this one is for talking to computers"

---

## 1. What is Python? And Why?

Imagine you have a very smart assistant. You tell them:
- "Sort this list for me"
- "Pull out only the Engineering employees from this file"
- "Send an email to every employee"

That assistant is Python.

Python is a programming language — a way to give instructions to a computer. But what makes Python special is that it **reads like English**. Compare:

Java:
```java
System.out.println("Hello World");
```

Python:
```python
print("Hello World")
```

Which one made more sense immediately? Python, right?

**Why Python wins:**
- #1 in Data Science
- #1 in AI/ML
- Used everywhere from startups to Google
- Easy to learn, powerful to use

---

## 2. Variable — "A Labeled Box"

A variable is a box where you store something and give it a name.

```python
name = "Rahul"
age = 28
salary = 75000
is_manager = False
```

Here:
- `name` is a box containing "Rahul"
- `age` is a box containing 28
- `=` means "assign" — not the mathematical equals sign

**Real life analogy:**
Like office drawers labeled "Pending Files" and "Approved Files". A variable is the same — you recognize it by name and use what's inside.

---

## 3. Data Types — "What's Inside the Box?"

Python needs to know what kind of thing is in the box:

| Type | What it is | Example |
|------|-----------|---------|
| `str` | Text / words | `"Pavan"`, `"Engineering"` |
| `int` | Whole number | `28`, `75000` |
| `float` | Decimal number | `9.5`, `3.14` |
| `bool` | Yes or No | `True`, `False` |

```python
name = "Rahul"          # str — inside quotes
age = 28                # int — no quotes
salary = 75000.50       # float — has decimal point
is_active = True        # bool — capital T/F
```

**Why does this matter?**
If you try `"28" + 2` — you get an error. Python says "one is text, one is a number — how do I add these?" Type matters.

---

## 4. List — "Train Compartments"

A list is an ordered collection. Like train compartments — one after another, numbered.

```python
employees = ["Rahul", "Priya", "Amit", "Neha"]
#              [0]      [1]     [2]     [3]
```

- `employees[0]` → "Rahul" (first compartment, starts at 0)
- `employees[-1]` → "Neha" (last compartment)

**Common operations:**
```python
employees.append("Kiran")    # Add a new compartment
employees.remove("Amit")     # Remove a compartment
len(employees)               # How many compartments?
"Rahul" in employees         # Is Rahul there? → True/False
```

**Real life:** Attendance sheet, product list, order items — all lists.

---

## 5. Dictionary — "A Phonebook"

In a dictionary, every item has a **key** and a **value**.

Like a phonebook:
- Key = Name
- Value = Phone number

```python
employee = {
    "name": "Rahul",
    "department": "Engineering",
    "salary": 75000,
    "is_active": True
}
```

Access it:
```python
employee["name"]          # "Rahul"
employee["salary"]        # 75000
employee["city"] = "Bangalore"   # Add a new key
```

**List vs Dictionary:**
- List: "Give me the 3rd item" → `list[2]`
- Dictionary: "Give me Rahul's salary" → `dict["salary"]`

Dictionary is more readable when data is structured.

---

## 6. If-Else — "Making Decisions"

Computers need to make decisions — just like you do.

```python
salary = 75000

if salary > 50000:
    print("High earner")
elif salary > 30000:
    print("Mid earner")
else:
    print("Entry level")
```

**Real life:** If order is above 500, free delivery. Otherwise charge 50 rupees.

```python
order_amount = 650

if order_amount >= 500:
    delivery = 0
else:
    delivery = 50

print(f"Delivery charge: ₹{delivery}")
```

---

## 7. Loop — "Giving Work to an Intern"

A loop means: "Do this task for every single item."

Like telling your intern: "Here are 50 files. Check the date on every single one."

```python
employees = ["Rahul", "Priya", "Amit"]

for emp in employees:
    print(f"Good morning, {emp}!")

# Output:
# Good morning, Rahul!
# Good morning, Priya!
# Good morning, Amit!
```

**Range loop** — when you know how many times:
```python
for i in range(5):
    print(f"Attempt {i+1}")
```

**While loop** — when you depend on a condition:
```python
attempts = 0
while attempts < 3:
    print("Trying...")
    attempts += 1
```

---

## 8. Function — "A Recipe"

A function is a recipe. Write it once, use it a hundred times.

```python
def calculate_bonus(salary, percent=10):
    bonus = salary * percent / 100
    return bonus
```

- `def` = "I am defining a function"
- `calculate_bonus` = the function's name
- `salary, percent` = ingredients (parameters)
- `return` = give back the result

```python
rahul_bonus = calculate_bonus(75000)        # 7500.0
priya_bonus = calculate_bonus(60000, 15)    # 9000.0
```

**Why functions?**
- Write once, use 100 times
- Fix a bug in one place, it's fixed everywhere
- Code stays readable

---

## 9. String Formatting — "Templates"

```python
name = "Rahul"
salary = 75000

# Old way (messy)
print("Hello " + name + ", your salary is " + str(salary))

# New way — f-string (clean!)
print(f"Hello {name}, your salary is ₹{salary:,}")
# Output: Hello Rahul, your salary is ₹75,000
```

Inside `f"..."`, put any variable inside `{}`.

---

## 10. Common Beginner Mistakes

| Mistake | Error | Fix |
|---------|-------|-----|
| `name = Rahul` | NameError | `name = "Rahul"` — add quotes |
| `if salary = 50000` | SyntaxError | `if salary == 50000` — double equals |
| `employees[4]` when only 4 items | IndexError | Index starts at 0 |
| Wrong indentation | IndentationError | Use 4 spaces or Tab consistently |

---

## Summary — What We Learned Today

| Concept | In One Line |
|---------|------------|
| Variable | Labeled box to store data |
| Data Types | What's in the box — text, number, boolean |
| List | Ordered collection — train compartments |
| Dictionary | Key-value pairs — phonebook |
| If-Else | Decision making |
| Loop | Doing one task repeatedly |
| Function | Reusable recipe |

**Tomorrow:** We'll use all of this to build our own "tools" — Classes and Objects.
