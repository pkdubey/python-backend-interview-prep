# Module 4: MySQL & SQL (Q61–Q80)

[← Back to Index](README.md) | [← Previous: Module 3](module-3-django-drf.md)

---

**Q61. Difference between SQL and MySQL?**

"SQL is a query language used to communicate with relational databases. MySQL is a database management system that uses SQL language to store, manage, and retrieve data."

---

**Q62. Explain different types of keys in MySQL.**

"Primary Key — uniquely identifies each row, cannot be NULL.
Foreign Key — creates a relationship between two tables.
Unique Key — ensures values are unique but allows NULL.
Composite Key — a key made using multiple columns."

```sql
-- Example
users
------
id (Primary Key)

orders
------
id
user_id (Foreign Key)
```

---

**Q63. Difference between Primary Key and Unique Key?**

"Primary key uniquely identifies each record and only one primary key can exist in a table. Unique key also maintains uniqueness, but a table can have multiple unique keys."

---

**Q64. What is normalization?**

"Normalization is a database design technique used to reduce data duplication and improve data consistency. For example, instead of storing user details repeatedly in the orders table, we keep user information in a separate users table and create a relationship."

**Follow-up: Why not always normalize?**

"Highly normalized databases may require more joins, which can impact performance. Sometimes we use denormalization for faster reads."

---

**Q65. Explain ACID properties.**

"ACID properties ensure reliable database transactions:
Atomicity — either all operations succeed or none.
Consistency — database remains valid before and after transaction.
Isolation — multiple transactions don't interfere incorrectly.
Durability — committed data remains saved even after failure."

"In payment systems, money deduction and order creation should happen together. If one fails, the transaction should rollback."

---

**Q66. What is a transaction?**

"A transaction is a group of database operations treated as a single unit. If all operations succeed, we commit. If any operation fails, we rollback."

```python
from django.db import transaction

with transaction.atomic():
    create_order()
    update_payment()
```

---

**Q67. What are transaction isolation levels?**

"Isolation levels define how one transaction is isolated from another. Common levels:
1. Read Uncommitted
2. Read Committed
3. Repeatable Read
4. Serializable

Higher isolation provides more consistency but may reduce performance."

---

**Q68. What is an index?**

"An index is a database structure that improves query performance by allowing faster data lookup. Without an index, MySQL scans the entire table. With an index, it can quickly locate required records."

```sql
CREATE INDEX idx_email ON users(email);
```

---

**Q69. Does index always improve performance?**

"No. Index improves read operations but adds overhead for insert, update, and delete operations because indexes also need to be updated. So we should create indexes on frequently searched or filtered columns."

---

**Q70. How do you optimize a slow SQL query?**

"First I analyze the query using EXPLAIN. Then I check:
- Missing indexes
- Full table scans
- Unnecessary joins
- Large data fetching
- Duplicate queries

Possible optimizations:
- Add proper indexes
- Select only required columns
- Optimize joins
- Use pagination
- Rewrite inefficient queries"

---

**Q71. Explain INNER JOIN.**

"INNER JOIN returns only matching records from both tables."

```sql
SELECT users.name, orders.id
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

---

**Q72. Difference between LEFT JOIN and INNER JOIN?**

"INNER JOIN returns only matching records. LEFT JOIN returns all records from the left table even if there is no matching record in the right table."

"If we want all users including users who have not placed orders, we use LEFT JOIN."

---

**Q73. What is GROUP BY?**

"GROUP BY is used to combine rows with the same values and perform aggregate operations."

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

---

**Q74. Difference between WHERE and HAVING?**

"WHERE filters rows before grouping. HAVING filters groups after GROUP BY."

```sql
-- WHERE
SELECT * FROM employees WHERE salary > 50000;

-- HAVING
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

**Q75. What are aggregate functions?**

"Aggregate functions perform calculations on multiple rows:
COUNT(), SUM(), AVG(), MIN(), MAX()"

```sql
SELECT AVG(salary) FROM employees;
```

---

**Q76. Explain subquery.**

"A subquery is a query inside another query."

```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

---

**Q77. What are window functions?**

"Window functions perform calculations across a set of rows without grouping the result into a single row. Common functions: ROW_NUMBER(), RANK(), DENSE_RANK(), LEAD(), LAG()."

```sql
-- Second highest salary
SELECT salary FROM (
    SELECT salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) rnk
    FROM employee
) x
WHERE rnk = 2;
```

---

**Q78. Difference between DELETE, TRUNCATE, DROP?**

"DELETE removes selected rows and supports WHERE condition. TRUNCATE removes all rows quickly and resets table storage. DROP removes the complete table structure."

```sql
-- DELETE
DELETE FROM users WHERE id = 10;

-- TRUNCATE
TRUNCATE TABLE users;

-- DROP
DROP TABLE users;
```

---

**Q79. What is deadlock?**

"Deadlock happens when two transactions wait for each other to release resources, and neither can continue."

"Prevention: Keep transactions short, access tables in consistent order, and use proper indexing."

---

**Q80. How do you design database tables for a new application?**

"First I understand business entities and relationships. Then I create normalized tables. I define primary keys, foreign keys, constraints, and indexes. After that, I review query patterns because database design should support both data consistency and application performance."

---

## Quick Revision Checklist (Module 4)

- [ ] SQL vs MySQL
- [ ] Primary Key vs Unique Key vs Foreign Key
- [ ] Normalization — 1NF, 2NF, 3NF
- [ ] Denormalization — when and why
- [ ] ACID properties — Atomicity, Consistency, Isolation, Durability
- [ ] Transaction — commit, rollback
- [ ] Isolation levels — 4 types
- [ ] Index — kya hai, kab use kare
- [ ] Index drawbacks — insert/update/delete overhead
- [ ] EXPLAIN — query analysis
- [ ] INNER JOIN vs LEFT JOIN
- [ ] GROUP BY + HAVING
- [ ] WHERE vs HAVING
- [ ] Aggregate functions — COUNT, SUM, AVG, MIN, MAX
- [ ] Subquery — nested query
- [ ] Window functions — ROW_NUMBER, RANK, DENSE_RANK
- [ ] DELETE vs TRUNCATE vs DROP
- [ ] Deadlock — cause + prevention
- [ ] Database design — entities, relationships, indexes

---

## Bonus: SQL Practice Queries

**1. Find second highest salary**
```sql
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**2. Find duplicate records**
```sql
SELECT email, COUNT(*) FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**3. Find employees earning more than department average**
```sql
SELECT * FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees
    WHERE department = e.department
);
```

**4. Top 3 highest paid employees**
```sql
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 3;
```

**5. Count employees per department**
```sql
SELECT department, COUNT(*) as total
FROM employees
GROUP BY department;
```

**6. Find employees who joined in last 30 days**
```sql
SELECT * FROM employees
WHERE joining_date >= DATE_SUB(NOW(), INTERVAL 30 DAY);
```

**7. Update salary by 10% for a department**
```sql
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT';
```

**8. Delete duplicate rows keeping lowest id**
```sql
DELETE e1 FROM employees e1
INNER JOIN employees e2
WHERE e1.id > e2.id AND e1.email = e2.email;
```

**9. Find nth highest salary (example: 3rd)**
```sql
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER(ORDER BY salary DESC) rnk
    FROM employees
) x
WHERE rnk = 3;
```

**10. Find employees with no orders (LEFT JOIN + NULL)**
```sql
SELECT u.name FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

**Practice Tip:** SQL queries ko hands-on practice karo. Interviewer live query likhne ko bol sakta hai — especially JOINs, GROUP BY, aur window functions.

---

[← Previous: Module 3](module-3-django-drf.md) | [Back to Index](README.md) | [Next: Module 5 →](module-5-llm-huggingface-celery-aws.md)
