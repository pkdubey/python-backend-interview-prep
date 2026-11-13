# Day 1 Lab — Python Foundations
# Run each section one by one. Try changing values and see what happens!

# ── SECTION 1: Variables & Data Types ──────────────────────────────────────
name = "Pavan"
age = 28
salary = 75000.0
is_active = True

print(type(name), type(age), type(salary), type(is_active))

# ── SECTION 2: Lists ────────────────────────────────────────────────────────
employees = ["Rahul", "Priya", "Amit", "Neha"]
print(employees[0])          # First item
print(employees[-1])         # Last item
employees.append("Kiran")    # Add
employees.remove("Amit")     # Remove
print(employees)

# ── SECTION 3: Dictionaries ─────────────────────────────────────────────────
employee = {"name": "Rahul", "dept": "Engineering", "salary": 75000}
print(employee["name"])
employee["bonus"] = 7500     # Add new key
print(employee)

# ── SECTION 4: Loops ────────────────────────────────────────────────────────
team = [
    {"name": "Rahul", "salary": 75000, "dept": "Engineering"},
    {"name": "Priya", "salary": 60000, "dept": "Marketing"},
    {"name": "Amit",  "salary": 90000, "dept": "Engineering"},
    {"name": "Neha",  "salary": 55000, "dept": "HR"},
]

for person in team:
    print(f"{person['name']} earns ₹{person['salary']:,}")

# ── SECTION 5: Functions ────────────────────────────────────────────────────
def calculate_bonus(salary, percent=10):
    return salary * percent / 100

def generate_payslip(employee):
    bonus = calculate_bonus(employee["salary"])
    total = employee["salary"] + bonus
    print(f"--- Payslip: {employee['name']} ---")
    print(f"  Base:  ₹{employee['salary']:,}")
    print(f"  Bonus: ₹{bonus:,}")
    print(f"  Total: ₹{total:,}")

for person in team:
    generate_payslip(person)

# ── MINI CHALLENGE: Shopping Cart ───────────────────────────────────────────
cart = [
    {"item": "Laptop",  "price": 55000},
    {"item": "Mouse",   "price": 800},
    {"item": "Keyboard","price": 1500},
]

subtotal = sum(i["price"] for i in cart)
gst = subtotal * 0.18
total = subtotal + gst

print(f"\n--- Bill ---")
for i in cart:
    print(f"  {i['item']}: ₹{i['price']:,}")
print(f"  Subtotal: ₹{subtotal:,}")
print(f"  GST 18%:  ₹{gst:,.0f}")
print(f"  TOTAL:    ₹{total:,.0f}")
