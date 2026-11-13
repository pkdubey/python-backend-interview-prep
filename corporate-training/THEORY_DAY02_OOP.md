# Day 2 Theory — Advanced Python & OOP
## "Now we build our own machines instead of just using tools"

---

## 1. Why OOP? — "The Problem Without It"

Imagine you have 100 employees. Without OOP:

```python
emp1_name = "Rahul"
emp1_salary = 75000
emp1_dept = "Engineering"

emp2_name = "Priya"
emp2_salary = 60000
emp2_dept = "Marketing"
# ... do this for 100 employees? 😰
```

This is messy, error-prone, and a nightmare to maintain.

With OOP:
```python
class Employee:
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept

rahul = Employee("Rahul", 75000, "Engineering")
priya = Employee("Priya", 60000, "Marketing")
# 100 employees? No problem.
```

---

## 2. Class — "A Cookie Cutter"

A **Class** is a blueprint — a template.

Like a cookie cutter makes different cookies — all the same shape, but different toppings.

```
Class  = Cookie Cutter (the blueprint)
Object = Actual Cookie (the real thing)
```

```python
class Employee:           # This is the cookie cutter
    pass

rahul = Employee()        # This is one cookie
priya = Employee()        # This is another cookie
```

---

## 3. `__init__` — "The Joining Form"

`__init__` is the method that runs when you create a new object. Like an HR joining form — when someone joins, this form gets filled out.

```python
class Employee:
    def __init__(self, name, salary, dept):
        self.name = name        # This employee's name
        self.salary = salary    # This employee's salary
        self.dept = dept        # This employee's department
```

```python
rahul = Employee("Rahul", 75000, "Engineering")
# __init__ runs automatically
# self.name   = "Rahul"
# self.salary = 75000
# self.dept   = "Engineering"
```

---

## 4. `self` — The Most Confusing Thing in Python

`self` means "this particular object itself."

Like when Rahul says "my salary" — "my" means Rahul's salary, not Priya's.

```python
class Employee:
    def get_info(self):
        return f"{self.name} works in {self.dept}"
        #        ^^^ "my name"       ^^^ "my dept"
```

```python
rahul.get_info()   # "Rahul works in Engineering"
priya.get_info()   # "Priya works in Marketing"
```

Same method, different results — because `self` is different each time.

**Rule:** Every method's first parameter is `self`. Python passes it automatically — you don't pass it explicitly.

---

## 5. Instance vs Class Variable

**Instance variable:** Each object has its own separate copy.
**Class variable:** All objects share the same one.

```python
class Employee:
    company = "TechCorp"      # Class variable — shared by ALL

    def __init__(self, name, salary):
        self.name = name      # Instance variable — unique per object
        self.salary = salary
```

```python
rahul = Employee("Rahul", 75000)
priya = Employee("Priya", 60000)

print(rahul.company)    # "TechCorp"
print(priya.company)    # "TechCorp" — same!
print(rahul.name)       # "Rahul"
print(priya.name)       # "Priya" — different!
```

---

## 6. Inheritance — "Parent to Child"

Inheritance means: one class takes everything from another class — plus adds its own extras.

**Real life:** A Manager IS an Employee — they have everything an employee has, PLUS the power to approve leaves.

```python
class Employee:                    # Parent class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name}: ₹{self.salary}"


class Manager(Employee):           # Child class — inherits from Employee
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # Get everything from Employee
        self.team_size = team_size       # Add this extra thing

    def approve_leave(self, emp_name):   # Extra method
        print(f"{self.name} approved leave for {emp_name}")
```

```python
amit = Manager("Amit", 120000, 5)
amit.get_info()              # Inherited from Employee — "Amit: ₹1,20,000"
amit.approve_leave("Rahul")  # Manager's own method
```

**`super()`** = "Call the parent class"

---

## 7. Encapsulation — "The ATM PIN"

Encapsulation means: protecting data from direct access — only allow access through defined methods.

**Real life:** You can't directly change your bank balance — it only changes through deposit/withdraw. That's encapsulation.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # __ = private, no direct access

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance       # Read-only access
```

```python
acc = BankAccount(10000)
acc.__balance = 99999999    # This won't work — it's private
acc.deposit(5000)           # This is the correct way
print(acc.get_balance())    # 15000
```

---

## 8. Decorator — "Gift Wrapping"

A decorator is a wrapper. It adds extra functionality on top of a function — without changing the function's code.

**Real life:** Like gift wrapping a present — the gift inside is the same, but the presentation is better.

```python
def log_it(func):
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result
    return wrapper

@log_it                          # This is the decorator
def process_payroll(employees):
    print(f"Processing {len(employees)} employees...")
    return "Done"
```

```python
process_payroll(["Rahul", "Priya"])
# Output:
# Starting: process_payroll
# Processing 2 employees...
# Done: process_payroll
```

**Where is this used in real life?**
- Checking login before an API call
- Measuring execution time
- Adding error handling
- Caching results

---

## 9. Generator — "Give It One at a Time"

A generator is a special function that doesn't give everything at once — it gives one item at a time, on demand.

**Real life:** Imagine a CSV file with 1 million rows. If you load all of them into memory at once — the computer will crash. A generator gives you one row, you process it, then it gives you the next.

```python
# Normal function — returns everything at once
def get_all_employees():
    return [emp1, emp2, ..., emp1000000]   # 1M objects in memory!

# Generator — gives one at a time
def get_employees_one_by_one():
    for emp in database:
        yield emp    # "Here's one, I'll pause, come back for the next"
```

```python
for emp in get_employees_one_by_one():
    process(emp)    # Only one employee in memory at a time
```

**`yield` vs `return`:**
- `return` = "Here's everything, I'm done"
- `yield` = "Here's one item, I'm paused, come back for more"

---

## 10. *args and **kwargs — "Flexible Functions"

Sometimes you don't know how many arguments will come in.

```python
# *args — any number of positional arguments
def add_all(*args):
    return sum(args)

add_all(1, 2)           # 3
add_all(1, 2, 3, 4, 5)  # 15

# **kwargs — any number of keyword arguments
def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Rahul", city="Bangalore", dept="Engineering")
```

---

## Summary — What We Learned Today

| Concept | In One Line | Real Life |
|---------|------------|-----------|
| Class | Blueprint / Template | Cookie cutter |
| Object | An actual instance of the blueprint | Actual cookie |
| `__init__` | Runs when object is created | Joining form |
| `self` | "This particular object" | "My" salary |
| Inheritance | Child class gets everything from parent | Manager is-a Employee |
| Encapsulation | Protecting data | ATM PIN |
| Decorator | Wrapping extra behavior around a function | Gift wrapping |
| Generator | Giving data one item at a time | Reading one page at a time |

**Tomorrow:** We apply all of this to real data — Pandas, NumPy, actual CSV files.
