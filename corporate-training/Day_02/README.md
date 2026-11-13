# Day 2 — Advanced Python & OOP
**Vibe:** "Building our own machines instead of just using tools."

---

## 🗣️ How to Open This Day

> "Yesterday we used Python like a calculator. Today we're going to build our own tools — like how a company builds its own internal software instead of buying off-the-shelf."

---

## 🧠 Concepts & Human-Language Explanations

### Class & Object
**Say this:** "A **Class** is a cookie cutter. An **Object** is the actual cookie. The cutter defines the shape — every cookie made from it has the same structure, but different toppings (data)."

```python
class Employee:           # The cookie cutter
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

rahul = Employee("Rahul", 75000)   # An actual cookie
priya = Employee("Priya", 60000)   # Another cookie
```

**Why does a company care?** "Instead of 50 separate dictionaries for 50 employees, you have one blueprint. Change the blueprint, everything updates."

### `self` — The Most Confusing Thing in Python
**Say this:** "When you write `self.name`, you're saying 'MY name' — the specific object's name, not anyone else's. `self` just means 'this particular instance'."

### Inheritance
**Say this:** "A child inherits traits from a parent. A `Manager` IS an `Employee` — they have everything an employee has, PLUS extra powers (like approving leaves)."

```python
class Manager(Employee):          # Manager inherits from Employee
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # Get everything from Employee
        self.team_size = team_size       # Plus this extra thing

    def approve_leave(self, emp_name):
        print(f"{self.name} approved leave for {emp_name}")
```

### Encapsulation
**Say this:** "Your ATM card has a PIN. The bank doesn't let you directly change the balance — you go through proper methods (deposit/withdraw). That's encapsulation — hiding internal data, exposing only what's needed."

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # __ means private, don't touch directly

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

### Decorators
**Say this:** "A decorator is a wrapper. Like gift wrapping — the gift (function) is the same inside, but the wrapper adds something extra (logging, timing, auth check)."

```python
def log_it(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Done.")
        return result
    return wrapper

@log_it
def process_payroll():
    print("Processing...")

process_payroll()
# Output:
# Calling process_payroll...
# Processing...
# Done.
```

### Generators
**Say this:** "Imagine reading a 10,000-page book. You don't photocopy all 10,000 pages first — you read one page, then the next. A generator does the same with data — gives you one item at a time, saving memory."

```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line    # Give one line, pause, wait for next request
```

---

## 💻 Live Coding Demo

**Scenario:** "Let's build an Employee Management System — the kind every company has."

See `lab.py` for the full demo code.

---

## 🏋️ Hands-on Challenge

Build a `BankAccount` class with:
- `deposit()`, `withdraw()` (with balance check)
- `get_statement()` that prints last 5 transactions
- A `SavingsAccount` subclass that adds `interest_rate` and `add_interest()` method

---

## 📝 Daily Recap Questions

1. "What's the difference between a class and an object? Give me an example from your own work."
2. "Why would you use inheritance instead of copy-pasting code?"
3. "Where in your current job could a decorator be useful?"

**Key takeaway:** "OOP is how you write code that a team of 10 engineers can work on without stepping on each other's toes."
