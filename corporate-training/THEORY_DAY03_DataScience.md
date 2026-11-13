# Day 3 Theory — Python for Data Science
## "What Excel can't do, Python does"

---

## 1. What is Data Science? — Simple Explanation

Data Science = Extracting useful answers from data.

**Real life example:**
- You have data on 50,000 customers
- Your manager asks: "Which customers are about to leave us?"
- Data Science gives you that answer

**3 things you need:**
1. Collect data (CSV, database, API)
2. Clean data (missing values, wrong formats)
3. Analyze data (patterns, trends, predictions)

Today we cover steps 1 and 2. ML/AI comes later.

---

## 2. Pandas — "Excel's Big Brother"

Pandas is a Python library that works with Excel-like tables — but 100x more powerful.

**DataFrame** = Pandas table = Excel sheet

```python
import pandas as pd

# Reading a CSV = Opening an Excel file
df = pd.read_csv("employees.csv")
```

First 5 things to always do:
```python
df.head()        # See first 5 rows
df.tail()        # See last 5 rows
df.shape         # (rows, columns) — how big is it?
df.info()        # Column names + data types
df.describe()    # Min, max, average of all numbers
```

---

## 3. Selecting Data

```python
# Select one column — like clicking a column in Excel
df["salary"]
df["name"]

# Select multiple columns
df[["name", "salary", "dept"]]

# Filter rows — like Excel's filter button
df[df["salary"] > 70000]                    # Salary above 70k
df[df["dept"] == "Engineering"]             # Engineering only
df[(df["salary"] > 50000) & (df["dept"] == "Engineering")]  # Both conditions
```

**How would you do this in Excel?** Filter button → select column → set condition. In Python: one line.

---

## 4. Data Cleaning — "The Most Important Part"

Real data is always messy. This is the truth — any data scientist will tell you.

**Common problems:**
- Missing values (blank cells)
- Wrong data types ("75000" stored as text instead of number)
- Duplicate rows
- Inconsistent formats ("Bangalore", "bangalore", "BANGALORE")

```python
# Check missing values
df.isnull().sum()              # How many missing per column?

# Handle missing values
df.dropna()                    # Remove rows with any missing value
df["salary"].fillna(0)         # Fill missing salaries with 0
df["dept"].fillna("Unknown")   # Fill missing dept with "Unknown"

# Remove duplicates
df.drop_duplicates()

# Fix data types
df["salary"] = df["salary"].astype(float)
df["join_date"] = pd.to_datetime(df["join_date"])

# Standardize text
df["dept"] = df["dept"].str.strip().str.title()
# "  engineering " → "Engineering"
```

**Rule of thumb:** Data cleaning takes 70-80% of your time. It feels boring but it's the most critical step.

---

## 5. GroupBy — "Pivot Table in Code"

GroupBy = Excel's Pivot Table.

"What is the average salary by department?" — that's a GroupBy.

```python
# Average salary per department
df.groupby("dept")["salary"].mean()

# Total headcount per city
df.groupby("city")["name"].count()

# Multiple calculations at once
df.groupby("dept").agg({
    "salary": ["mean", "min", "max"],
    "name": "count"
})
```

**In Excel:** Insert → Pivot Table → drag fields. In Python: one line.

---

## 6. Creating New Columns

```python
# Add a bonus column
df["bonus"] = df["salary"] * 0.10

# Total compensation
df["total_comp"] = df["salary"] + df["bonus"]

# Category column
df["level"] = df["salary"].apply(
    lambda x: "Senior" if x > 80000 else "Mid" if x > 50000 else "Junior"
)
```

**`apply` + `lambda`** = Apply a function to every row.

---

## 7. Sorting and Ranking

```python
# Sort by salary (highest first)
df.sort_values("salary", ascending=False)

# Sort by multiple columns
df.sort_values(["dept", "salary"], ascending=[True, False])

# Top 5 earners
df.nlargest(5, "salary")

# Bottom 5 earners
df.nsmallest(5, "salary")
```

---

## 8. NumPy — "The Fast Calculator"

NumPy = Numerical Python. Does fast math on large arrays.

```python
import numpy as np

scores = np.array([85, 92, 78, 95, 88, 76, 91])

np.mean(scores)    # Average: 86.4
np.median(scores)  # Middle value: 88
np.std(scores)     # Standard deviation
np.max(scores)     # 95
np.min(scores)     # 76
```

**Pandas vs NumPy:**
- Pandas = Works with tables (rows, columns, labels)
- NumPy = Fast math on pure numbers

Pandas uses NumPy internally.

---

## 9. Matplotlib — "Making Charts"

Showing data in a chart — because charts tell the story better than numbers.

```python
import matplotlib.pyplot as plt

# Bar chart
dept_count = df["dept"].value_counts()
dept_count.plot(kind="bar", title="Employees per Department")
plt.tight_layout()
plt.show()

# Line chart
monthly_sales.plot(kind="line", title="Monthly Sales Trend")

# Pie chart
df["dept"].value_counts().plot(kind="pie", autopct="%1.1f%%")
```

**Tip:** Always add `plt.tight_layout()` — otherwise labels get cut off.

---

## 10. Real Workflow — "A Day in the Life"

This is an actual data analyst's workflow:

```
1. df = pd.read_csv("data.csv")          # Load data
2. df.info() + df.head()                 # Understand what you have
3. df.isnull().sum()                     # Find problems
4. Clean (fillna, dropna, astype)        # Fix problems
5. df.groupby(...).agg(...)              # Analyze
6. df.sort_values(...).head(10)          # Get top results
7. .plot() + plt.show()                  # Visualize
8. df.to_csv("results.csv")             # Save output
```

---

## 11. Pandas vs Excel — Side by Side

| Task | Excel | Pandas |
|------|-------|--------|
| Open file | Double click | `pd.read_csv()` |
| Filter | Filter button | `df[df["col"] > value]` |
| Pivot table | Insert → Pivot | `df.groupby().agg()` |
| New column | Formula in cell | `df["new"] = df["a"] + df["b"]` |
| Sort | Sort button | `df.sort_values()` |
| Max rows | ~1 million | Unlimited (up to RAM) |
| Automation | Macros (complex) | Python script (simple) |
| Reproducible | No | Yes — code is saved |

---

## Summary

| Library | What it does | Analogy |
|---------|-------------|---------|
| Pandas | Works with tables | Excel's big brother |
| NumPy | Fast math on arrays | Super calculator |
| Matplotlib | Makes charts | Excel charts but better |

**Tomorrow:** We'll serve this data over the internet — with FastAPI.
