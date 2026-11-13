# Day 2 Lab — Advanced Python & OOP

# ── SECTION 1: Class & Object ───────────────────────────────────────────────
class Employee:
    company = "TechCorp"  # Class variable — shared by ALL employees

    def __init__(self, name, salary, dept):
        self.name = name        # Instance variable — unique per employee
        self.salary = salary
        self.dept = dept

    def get_info(self):
        return f"{self.name} | {self.dept} | ₹{self.salary:,}"

    def give_raise(self, percent):
        self.salary += self.salary * percent / 100
        print(f"{self.name} got a raise! New salary: ₹{self.salary:,}")


# ── SECTION 2: Inheritance ──────────────────────────────────────────────────
class Manager(Employee):
    def __init__(self, name, salary, dept, team_size):
        super().__init__(name, salary, dept)
        self.team_size = team_size
        self.reports = []

    def add_report(self, employee):
        self.reports.append(employee)
        print(f"{employee.name} now reports to {self.name}")

    def approve_leave(self, emp_name, days):
        print(f"✅ {self.name} approved {days} days leave for {emp_name}")


# ── SECTION 3: Encapsulation ────────────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        self.__balance += amount
        self.__transactions.append(f"+₹{amount:,}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
            return
        self.__balance -= amount
        self.__transactions.append(f"-₹{amount:,}")

    def get_balance(self):
        return self.__balance

    def get_statement(self):
        print(f"\n--- Statement: {self.owner} ---")
        for t in self.__transactions[-5:]:
            print(f"  {t}")
        print(f"  Balance: ₹{self.__balance:,}")


# ── SECTION 4: Decorator ────────────────────────────────────────────────────
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱ {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def process_payroll(employees):
    return [e.give_raise(5) for e in employees]


# ── SECTION 5: Generator ────────────────────────────────────────────────────
def employee_report(employees):
    """Yields one employee record at a time — memory efficient"""
    for emp in employees:
        yield emp.get_info()


# ── DEMO RUN ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    rahul = Employee("Rahul", 75000, "Engineering")
    priya = Employee("Priya", 60000, "Marketing")
    amit  = Manager("Amit", 120000, "Engineering", team_size=5)

    amit.add_report(rahul)
    amit.add_report(priya)
    amit.approve_leave("Rahul", 3)

    print("\n--- Employee Info ---")
    for info in employee_report([rahul, priya, amit]):
        print(info)

    acc = BankAccount("Rahul")
    acc.deposit(50000)
    acc.deposit(25000)
    acc.withdraw(10000)
    acc.get_statement()
