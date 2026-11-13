# Day 3 — Python for Data Science
**Vibe:** "Making sense of spreadsheets at scale."

---

## 🗣️ How to Open This Day

> "How many of you have spent hours in Excel — filtering, pivot tables, VLOOKUP? Today I'm going to show you how to do all of that in 3 lines of Python. And then do things Excel literally cannot do."

---

## 🧠 Concepts & Human-Language Explanations

### Pandas — "Excel on Steroids"
**Say this:** "A Pandas DataFrame is just an Excel sheet inside Python. Rows and columns. But instead of clicking, you write code — which means you can process 10 million rows in seconds."

```python
import pandas as pd

# Reading a CSV = Opening an Excel file
df = pd.read_csv("sales_data.csv")

df.head()           # Show first 5 rows
df.shape            # (rows, columns)
df.info()           # Column names + data types
df.describe()       # Min, max, average of all numbers
```

### Data Cleaning — "The Boring but Critical Part"
**Say this:** "In real projects, 80% of your time is cleaning data. Dirty data = wrong answers. Garbage in, garbage out."

```python
df.isnull().sum()              # How many missing values per column?
df.dropna()                    # Remove rows with any missing value
df["salary"].fillna(0)         # Fill missing salaries with 0
df.drop_duplicates()           # Remove duplicate rows
df["date"] = pd.to_datetime(df["date"])  # Fix date format
```

### GroupBy — "Pivot Tables in Code"
**Say this:** "GroupBy is like Excel's pivot table. 'Show me total sales BY region' — that's a GroupBy."

```python
# Total sales per department
df.groupby("department")["sales"].sum()

# Average salary per city
df.groupby("city")["salary"].mean()

# Multiple aggregations at once
df.groupby("dept").agg({"salary": "mean", "bonus": "sum"})
```

### NumPy — "A Super-Fast Calculator"
**Say this:** "NumPy is for math on large arrays. It's 100x faster than Python loops because it's written in C under the hood. You won't use it directly much, but Pandas uses it internally."

```python
import numpy as np

scores = np.array([85, 92, 78, 95, 88])
print(np.mean(scores))    # Average
print(np.std(scores))     # Standard deviation
print(np.max(scores))     # Max
```

### Matplotlib — "Making Charts"
**Say this:** "Data without visualization is just numbers. Charts tell the story. Matplotlib is the basic chart library — think of it as Python's version of Excel charts."

```python
import matplotlib.pyplot as plt

dept_sales = df.groupby("department")["sales"].sum()
dept_sales.plot(kind="bar", title="Sales by Department")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
```

---

## 💻 Live Coding Demo

**Scenario:** "You're a data analyst at a retail company. Your manager just dropped a messy CSV on your desk and said 'Find the top 3 products and which region is underperforming.' Let's do it."

See `lab.py` for the full demo.

---

## 🏋️ Hands-on Challenge

Given `employees.csv` (provided):
1. Find the department with the highest average salary
2. Find employees who joined in 2023
3. Plot a bar chart of headcount per department
4. Export the top 10 earners to a new CSV

---

## 📝 Daily Recap Questions

1. "What's the Pandas equivalent of Excel's VLOOKUP?"
2. "Why do we need to clean data before analyzing it?"
3. "What's the difference between `dropna()` and `fillna()`?"

**Key takeaway:** "Data Science starts with messy data. The skill is not the fancy ML model — it's cleaning and understanding the data first."
