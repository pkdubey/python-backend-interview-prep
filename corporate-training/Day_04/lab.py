# Day 4 Lab — FastAPI
# Run: uvicorn lab:app --reload
# Then open: http://localhost:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="HR Employee API", version="1.0")

# ── In-memory "database" ────────────────────────────────────────────────────
employees_db = [
    {"id": 1, "name": "Rahul",  "dept": "Engineering", "salary": 75000},
    {"id": 2, "name": "Priya",  "dept": "Marketing",   "salary": 60000},
    {"id": 3, "name": "Amit",   "dept": "Engineering", "salary": 90000},
]
next_id = 4

# ── Pydantic Models ─────────────────────────────────────────────────────────
class EmployeeCreate(BaseModel):
    name: str
    dept: str
    salary: float

class EmployeeUpdate(BaseModel):
    salary: Optional[float] = None
    dept: Optional[str] = None

# ── Endpoints ───────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "HR API is running 🚀", "docs": "/docs"}

@app.get("/employees")
def list_employees(dept: Optional[str] = None, limit: int = 10):
    result = employees_db
    if dept:
        result = [e for e in result if e["dept"].lower() == dept.lower()]
    return result[:limit]

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    emp = next((e for e in employees_db if e["id"] == emp_id), None)
    if not emp:
        raise HTTPException(status_code=404, detail=f"Employee {emp_id} not found")
    return emp

@app.post("/employees", status_code=201)
def create_employee(emp: EmployeeCreate):
    global next_id
    new_emp = {"id": next_id, **emp.dict()}
    employees_db.append(new_emp)
    next_id += 1
    return new_emp

@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, update: EmployeeUpdate):
    emp = next((e for e in employees_db if e["id"] == emp_id), None)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    if update.salary is not None:
        emp["salary"] = update.salary
    if update.dept is not None:
        emp["dept"] = update.dept
    return emp

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    global employees_db
    emp = next((e for e in employees_db if e["id"] == emp_id), None)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    employees_db = [e for e in employees_db if e["id"] != emp_id]
    return {"message": f"Employee {emp_id} deleted"}

@app.get("/employees/dept/summary")
def dept_summary():
    from collections import defaultdict
    summary = defaultdict(lambda: {"count": 0, "total_salary": 0})
    for emp in employees_db:
        d = emp["dept"]
        summary[d]["count"] += 1
        summary[d]["total_salary"] += emp["salary"]
    return dict(summary)
