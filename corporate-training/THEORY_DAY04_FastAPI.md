# Day 4 Theory — FastAPI
## "Share your Python code with the world"

---

## 1. What is an API? — The Waiter Analogy

This is the most important analogy. Remember this one.

**Restaurant analogy:**

```
You (Client)  →  Waiter (API)  →  Kitchen (Server/Python Code)
     ↑                                        ↓
     └──────────── Food (Response) ───────────┘
```

- **You** = Browser, Mobile App, or any program
- **Waiter** = API
- **Kitchen** = Your Python code + Database
- **Menu** = API documentation (what you can order)
- **Order** = Request
- **Food** = Response

You don't walk into the kitchen yourself — you go through the waiter. Similarly, a client doesn't access the database directly — it goes through the API.

---

## 2. HTTP Methods — "Types of Orders"

Just like a restaurant has different types of orders, an API has different methods:

| Method | Meaning | Real life |
|--------|---------|-----------|
| GET | Fetch data | Reading the menu |
| POST | Create something new | Placing an order |
| PUT | Update something completely | Changing your order |
| PATCH | Update partially | Just changing your drink |
| DELETE | Remove something | Cancelling your order |

```
GET    /employees          → Give me the list of all employees
GET    /employees/42       → Give me info on employee #42
POST   /employees          → Create a new employee
PUT    /employees/42       → Update employee #42
DELETE /employees/42       → Remove employee #42
```

---

## 3. Request and Response

**Request** = What you send
**Response** = What the server sends back

Every response has a **status code**:

| Code | Meaning | Real life |
|------|---------|-----------|
| 200 | OK — everything worked | Order delivered |
| 201 | Created — new item made | Order placed successfully |
| 400 | Bad Request — your mistake | Wrong order given |
| 401 | Unauthorized — please log in | Members only area |
| 404 | Not Found — doesn't exist | Item not on menu |
| 500 | Server Error — our mistake | Kitchen caught fire |

---

## 4. Why FastAPI?

Python has several web frameworks:
- **Django** — Full featured, heavy, batteries included
- **Flask** — Lightweight, simple
- **FastAPI** — Modern, fast, automatic documentation

**What makes FastAPI special:**

1. **Auto Documentation** — Go to `/docs` and you get a full interactive API page. The frontend team doesn't need separate documentation.

2. **Automatic Validation** — If you say "salary must be a number" and someone sends a string, FastAPI automatically rejects it.

3. **Fast** — It's in the name. NodeJS-level speed.

4. **Uses type hints** — Python's modern feature.

---

## 5. Your First FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
```

Run it:
```bash
uvicorn main:app --reload
```

Open in browser: `http://localhost:8000/hello/Rahul`

You get:
```json
{"message": "Hello, Rahul!"}
```

And go to `http://localhost:8000/docs` — you get a full interactive documentation page. For free.

---

## 6. Path Parameters vs Query Parameters

**Path Parameter** — part of the URL itself:
```
GET /employees/42
                ↑ this is a path parameter
```

```python
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    return {"id": emp_id}
```

**Query Parameter** — comes after `?`:
```
GET /employees?dept=Engineering&limit=10
               ↑ these are query parameters
```

```python
@app.get("/employees")
def list_employees(dept: str = None, limit: int = 10):
    return {"dept": dept, "limit": limit}
```

**When to use which?**
- Path parameter: For one specific item (`/employees/42`)
- Query parameter: For filtering/searching (`/employees?dept=Engineering`)

---

## 7. Pydantic — "Automatic Validation"

With Pydantic, you define what the data should look like. FastAPI validates it automatically.

```python
from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: float
    dept: str
    is_active: bool = True    # Default value
```

```python
@app.post("/employees")
def create_employee(emp: Employee):
    # By the time we get here, emp.name, emp.salary are all validated
    # If someone sends wrong data — FastAPI automatically returns 422 error
    return {"status": "created", "data": emp}
```

**What happens if wrong data is sent?**
```json
// Sent this:
{"name": "Rahul", "salary": "not-a-number", "dept": "Engineering"}

// FastAPI automatically returns:
{
  "detail": [
    {
      "loc": ["body", "salary"],
      "msg": "value is not a valid float",
      "type": "type_error.float"
    }
  ]
}
```

You didn't write a single line of validation code — Pydantic handled it all.

---

## 8. JSON — "The Language of APIs"

APIs communicate in JSON. JSON = JavaScript Object Notation.

```json
{
  "name": "Rahul",
  "salary": 75000,
  "dept": "Engineering",
  "skills": ["Python", "Django", "AWS"],
  "address": {
    "city": "Bangalore",
    "state": "Karnataka"
  }
}
```

It looks just like a Python dictionary — which is why converting between Python and JSON is very easy.

```python
import json

# Python dict → JSON string
data = {"name": "Rahul", "salary": 75000}
json_str = json.dumps(data)

# JSON string → Python dict
back_to_dict = json.loads(json_str)
```

FastAPI does this conversion automatically — you don't do it manually.

---

## 9. Error Handling

```python
from fastapi import HTTPException

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    employee = find_in_db(emp_id)

    if not employee:
        raise HTTPException(
            status_code=404,
            detail=f"Employee {emp_id} not found"
        )

    return employee
```

Raise an `HTTPException` — FastAPI builds the proper error response.

---

## 10. Swagger UI — "The Frontend Team's Best Friend"

The page you see at `/docs` is called Swagger UI.

It shows:
- All endpoints listed
- Description of each endpoint
- "Try it out" button to test directly
- Request/response format

**Why this matters in a corporate team:**
- Frontend developers don't need separate documentation
- QA team can test directly without writing code
- New team member joins — they look at `/docs` and understand everything

---

## 11. Full Flow — The Journey of One Request

```
1. User types in browser: GET /employees/42

2. Request arrives at FastAPI server

3. FastAPI sees: "/employees/{emp_id}" route matches

4. Extracts emp_id = 42, converts to int

5. Calls get_employee(42)

6. Function fetches data from database

7. Returns Python dict

8. FastAPI converts dict to JSON

9. Sends response with HTTP 200 status

10. Browser receives JSON and displays it
```

---

## Summary

| Concept | In One Line |
|---------|------------|
| API | Waiter — between client and server |
| HTTP Methods | GET=fetch, POST=create, PUT=update, DELETE=remove |
| Status Codes | 200=OK, 404=not found, 500=server error |
| FastAPI | Python's fastest web framework with auto-docs |
| Pydantic | Automatic data validation |
| JSON | The universal language of APIs |
| Swagger UI | Auto-generated interactive documentation |

**Tomorrow:** We teach computers to understand text — NLP.
