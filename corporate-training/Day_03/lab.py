# Day 3 Lab — Python for Data Science
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# ── CREATE SAMPLE DATA (in real life, this is a CSV file) ───────────────────
raw = """name,department,city,salary,sales,join_date
Rahul,Engineering,Bangalore,75000,0,2022-03-15
Priya,Marketing,Mumbai,60000,450000,2023-01-10
Amit,Engineering,Bangalore,90000,0,2021-07-20
Neha,Sales,Delhi,55000,380000,2023-06-01
Kiran,Marketing,Bangalore,65000,520000,2022-11-30
Raj,Sales,Mumbai,58000,,2023-08-15
Deepa,HR,Delhi,50000,0,2021-04-05
Suresh,Engineering,Hyderabad,85000,0,2022-09-12
Anita,Sales,Bangalore,62000,610000,2023-02-28
Vikram,Marketing,Delhi,70000,490000,2022-05-18"""

df = pd.read_csv(StringIO(raw))

# ── SECTION 1: Explore the Data ─────────────────────────────────────────────
print("=== Shape ===")
print(df.shape)

print("\n=== First 5 rows ===")
print(df.head())

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Missing Values ===")
print(df.isnull().sum())

# ── SECTION 2: Clean the Data ───────────────────────────────────────────────
df["sales"] = df["sales"].fillna(0)
df["join_date"] = pd.to_datetime(df["join_date"])
df = df.drop_duplicates()

print("\n=== After Cleaning ===")
print(df.isnull().sum())

# ── SECTION 3: Analysis ─────────────────────────────────────────────────────
print("\n=== Avg Salary by Department ===")
print(df.groupby("department")["salary"].mean().sort_values(ascending=False))

print("\n=== Total Sales by City ===")
print(df.groupby("city")["sales"].sum().sort_values(ascending=False))

print("\n=== Employees who joined in 2023 ===")
new_joiners = df[df["join_date"].dt.year == 2023]
print(new_joiners[["name", "department", "join_date"]])

# ── SECTION 4: Top Earners ──────────────────────────────────────────────────
top_earners = df.nlargest(5, "salary")[["name", "department", "salary"]]
print("\n=== Top 5 Earners ===")
print(top_earners)

# ── SECTION 5: Visualization ────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Chart 1: Headcount per department
df["department"].value_counts().plot(kind="bar", ax=axes[0], color="steelblue")
axes[0].set_title("Headcount by Department")
axes[0].set_xlabel("")

# Chart 2: Avg salary per department
df.groupby("department")["salary"].mean().plot(kind="bar", ax=axes[1], color="coral")
axes[1].set_title("Avg Salary by Department")
axes[1].set_xlabel("")

plt.tight_layout()
plt.savefig("hr_dashboard.png")
print("\n✅ Chart saved as hr_dashboard.png")
plt.show()
