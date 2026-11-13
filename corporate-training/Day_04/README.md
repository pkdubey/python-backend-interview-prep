# Day 4 — FastAPI
**Vibe:** "Serving our Python code to the world."

---

## 🗣️ How to Open This Day

> "So far, our Python code runs only on our laptop. What if your manager in Mumbai wants to use it? What if a mobile app needs to call it? That's what an API does — it puts your code on the internet so anyone can use it."

---

## 🧠 Concepts & Human-Language Explanations

### What is an API?
**The Waiter Analogy:**
> "You're at a restaurant. You (the client) don't go into the kitchen yourself. You tell the **waiter** (API) what you want. The waiter goes to the **kitchen** (your Python code/database), gets the food (data), and brings it back to you (response)."

```
Client (Browser/App) → Request → API → Python Code → Database
Client ← Response ← API ← Python Code ← Database
```

### REST & HTTP Methods
**Say this:** "REST is just a set of rules for how APIs should behave. HTTP methods are the 'verbs' — what action you want to do."

| Method | Real-world analogy | Use case |
|--------|-------------------|----------|
| GET | Reading a menu | Fetch data |
| POST | Placing an order | Create new data |
| PUT | Changing your order | Update data |
| DELETE | Cancelling order | Delete data |

### Why FastAPI?
**Say this:** "FastAPI is the fastest Python web framework. It auto-generates documentation (Swagger UI at `/docs`) — which your frontend team will LOVE. And it validates data automatically."

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
```

Visit `http://localhost:8000/docs` → You get a full interactive API docs page. For FREE.

### Request Body & Validation
**Say this:** "FastAPI uses Pydantic models to validate data. If someone sends a string where you expect a number, FastAPI rejects it automatically — you don't write any validation code."

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: float
    department: str

@app.post("/employees/")
def create_employee(emp: Employee):
    # emp.name, emp.salary are already validated
    return {"status": "created", "employee": emp}
```

### Path vs Query Parameters
```python
# Path parameter: /employees/42
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    return {"id": emp_id}

# Query parameter: /employees?dept=Engineering&limit=10
@app.get("/employees")
def list_employees(dept: str = None, limit: int = 10):
    return {"dept": dept, "limit": limit}
```

---

## 💻 Live Coding Demo

**Scenario:** "Let's build an Employee API — the backend for an HR system."

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

See `lab.py` for the full API.

**Show the class:**
1. Open `http://localhost:8000/docs`
2. Click "Try it out" on any endpoint
3. "This is what your frontend team uses to test your API without writing any code."

---

## 🏋️ Hands-on Challenge

Build a "Product Inventory API":
- `GET /products` — list all products
- `GET /products/{id}` — get one product
- `POST /products` — add a product
- `PUT /products/{id}` — update price
- `DELETE /products/{id}` — remove product

Use an in-memory list (no database needed today).

---

## 📝 Daily Recap Questions

1. "What's the difference between GET and POST?"
2. "Why is auto-generated documentation useful in a corporate team?"
3. "What happens if you send wrong data type to a FastAPI endpoint?"

**Key takeaway:** "You just built a real REST API. This is what every backend developer does. The only difference in production is you connect it to a real database."
