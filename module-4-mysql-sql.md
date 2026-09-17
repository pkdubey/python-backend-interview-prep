# Module 4: MySQL & SQL — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 3](module-3-django-drf.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. Har answer ko natural language mein rakha hai, jaise ek 5.5 years experienced Python backend developer interview mein bolta hai.

---

# PART 1: SQL FUNDAMENTALS (Q61–Q75)

---

**Q61. Difference between SQL and MySQL?**

"SQL is a query language used to communicate with relational databases. It's a standard — like a protocol. MySQL is a database management system that implements SQL.

Think of it like this: SQL is the language, MySQL is the software that understands and executes it. There are other databases that use SQL — PostgreSQL, Oracle, SQL Server. They all use SQL but with their own extensions."

**Follow-up: What are some other SQL databases?**

"PostgreSQL, Oracle, SQL Server, SQLite, MariaDB. PostgreSQL is popular for its advanced features. SQLite is used for embedded systems and mobile apps. MySQL is popular for web applications because of its speed and ease of use."

**Follow-up: What is the difference between SQL and NoSQL?**

"SQL databases are relational — data is stored in tables with rows and columns. They follow ACID properties. NoSQL databases are non-relational — data is stored as documents, key-value pairs, or graphs. They follow BASE properties.

SQL is good for structured data with complex relationships. NoSQL is good for unstructured data and horizontal scaling. MongoDB is a popular NoSQL database that I've also worked with."

---

**Q62. Explain different types of keys in MySQL.**

"Keys are used to identify records and create relationships between tables. There are several types:

1. **Primary Key** — uniquely identifies each row. Cannot be NULL. Only one per table.
2. **Foreign Key** — creates a relationship between two tables. References a primary key in another table.
3. **Unique Key** — ensures values are unique but allows NULL. Can have multiple per table.
4. **Composite Key** — a key made using multiple columns. Used when one column is not enough to uniquely identify a row.
5. **Candidate Key** — any column that can be a primary key. One of them becomes the primary key.
6. **Alternate Key** — candidate keys that are not chosen as primary key.
7. **Surrogate Key** — an artificial key like auto-increment ID."

```sql
-- Primary Key
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    name VARCHAR(100)
);

-- Foreign Key
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Composite Key
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);
```

**Follow-up: What is the difference between Primary Key and Candidate Key?**

"A candidate key is any column that can uniquely identify a row. A primary key is the candidate key that is chosen as the main identifier. For example, in a users table, both `id` and `email` could be candidate keys. We choose `id` as primary key and `email` becomes an alternate key."

---

**Q63. Difference between Primary Key and Unique Key?**

"Both ensure uniqueness, but there are important differences:

1. **Primary Key** — only one per table. Cannot be NULL. Creates a clustered index.
2. **Unique Key** — multiple per table. Can have one NULL value. Creates a non-clustered index.

In simple terms — primary key is the main identifier, unique key is for additional uniqueness constraints."

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,           -- primary key
    email VARCHAR(100) UNIQUE,    -- unique key
    phone VARCHAR(20) UNIQUE      -- another unique key
);
```

**Follow-up: Can a table have multiple primary keys?**

"No, a table can have only one primary key. But a primary key can be a composite key — made of multiple columns."

**Follow-up: Can a unique key have NULL values?**

"In MySQL, a unique key can have one NULL value. In some databases like PostgreSQL, multiple NULLs are allowed. It depends on the database."

---

**Q64. What is normalization?**

"Normalization is a database design technique used to reduce data duplication and improve data consistency. It involves organizing data into multiple related tables.

There are several normal forms:

1. **1NF (First Normal Form)** — each column contains atomic values. No repeating groups.
2. **2NF (Second Normal Form)** — 1NF + no partial dependencies. All non-key columns depend on the full primary key.
3. **3NF (Third Normal Form)** — 2NF + no transitive dependencies. Non-key columns don't depend on other non-key columns.
4. **BCNF (Boyce-Codd Normal Form)** — stronger version of 3NF."

**Follow-up: Why not always normalize?**

"Highly normalized databases may require more joins, which can impact performance. Sometimes we use denormalization for faster reads. For example, in a reporting system, we might duplicate data to avoid joins.

The trade-off is: normalization reduces redundancy but increases joins. Denormalization reduces joins but increases redundancy."

**Follow-up: Give an example of normalization.**

"Let's say we have an orders table:

```
orders:
id | customer_name | customer_email | product_name | product_price | quantity
```

This has redundancy — customer details are repeated for each order. In normalized form:

```
customers: id, name, email
products: id, name, price
orders: id, customer_id, created_at
order_items: id, order_id, product_id, quantity
```

Now customer details are stored once. This is 3NF."

---

**Q65. Explain ACID properties.**

"ACID properties ensure reliable database transactions:

1. **Atomicity** — either all operations succeed or none. If one fails, everything rolls back.
2. **Consistency** — database remains valid before and after transaction. All constraints are satisfied.
3. **Isolation** — multiple transactions don't interfere incorrectly. Each transaction sees a consistent snapshot.
4. **Durability** — committed data remains saved even after system failure. Usually achieved through write-ahead logging."

"In payment systems, money deduction and order creation should happen together. If one fails, the transaction should rollback. This is Atomicity."

**Follow-up: Give a real example from your work.**

"In my FinTech freelance project, I used transactions for money transfers. The transaction would:
1. Deduct from sender
2. Add to receiver
3. Create transaction log

If any step failed, everything rolled back. This ensured that money was never lost or duplicated."

**Follow-up: How do you implement transactions in Django?**

```python
from django.db import transaction

with transaction.atomic():
    sender.balance -= amount
    sender.save()
    receiver.balance += amount
    receiver.save()
    TransactionLog.objects.create(
        sender=sender,
        receiver=receiver,
        amount=amount
    )
```

If any operation raises an exception, the entire block is rolled back."

---

**Q66. What is a transaction?**

"A transaction is a group of database operations treated as a single unit. If all operations succeed, we commit. If any operation fails, we rollback.

Transactions are essential for maintaining data integrity. They follow ACID properties."

```sql
-- SQL transaction
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
-- If any error occurs, ROLLBACK;
```

**Follow-up: What is the difference between COMMIT and ROLLBACK?**

"**COMMIT** — permanently saves the changes to the database.
**ROLLBACK** — undoes all changes made in the current transaction.

If the application crashes before COMMIT, the transaction is automatically rolled back."

**Follow-up: What is auto-commit?**

"By default, most databases run in auto-commit mode. Each statement is automatically committed. To use transactions, you either disable auto-commit or explicitly use START TRANSACTION and COMMIT.

In Django, `transaction.atomic()` handles this automatically."

---

**Q67. What are transaction isolation levels?**

"Isolation levels define how one transaction is isolated from another. There are four standard levels:

1. **Read Uncommitted** — lowest isolation. A transaction can read uncommitted data from another transaction. This is called a dirty read.
2. **Read Committed** — a transaction can only read committed data. Prevents dirty reads.
3. **Repeatable Read** — a transaction sees a consistent snapshot. Prevents dirty reads and non-repeatable reads. But phantom reads can occur.
4. **Serializable** — highest isolation. Transactions are completely isolated. Prevents all anomalies. But reduces concurrency."

**Follow-up: What are dirty reads, non-repeatable reads, and phantom reads?**

"1. **Dirty Read** — reading uncommitted data from another transaction. If that transaction rolls back, the data you read was never valid.
2. **Non-Repeatable Read** — reading the same row twice and getting different values because another transaction modified it.
3. **Phantom Read** — running the same query twice and getting different rows because another transaction inserted or deleted rows."

**Follow-up: Which isolation level does MySQL use?**

"MySQL's default isolation level is **Repeatable Read**. PostgreSQL's default is **Read Committed**. Oracle's default is **Read Committed**.

The choice depends on the trade-off between consistency and performance. Higher isolation means more consistency but less concurrency."

---

**Q68. What is an index?**

"An index is a database structure that improves query performance by allowing faster data lookup. Without an index, MySQL scans the entire table. With an index, it can quickly locate required records.

Think of it like a book's index — instead of reading every page, you go directly to the right page."

```sql
-- Create index
CREATE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_name_email ON users(name, email);

-- Unique index
CREATE UNIQUE INDEX idx_username ON users(username);
```

**Follow-up: What are the types of indexes?**

"1. **Primary Index** — automatically created on primary key. Clustered index.
2. **Secondary Index** — created on non-primary columns. Non-clustered.
3. **Composite Index** — index on multiple columns.
4. **Unique Index** — ensures uniqueness.
5. **Full-text Index** — for text search.
6. **Spatial Index** — for geographic data."

**Follow-up: What is a clustered index?**

"A clustered index determines the physical order of data in the table. A table can have only one clustered index. In MySQL, the primary key is the clustered index by default.

Non-clustered indexes have a separate structure that points to the data rows."

---

**Q69. Does index always improve performance?**

"No. Index improves read operations but adds overhead for insert, update, and delete operations because indexes also need to be updated.

So we should create indexes on frequently searched or filtered columns, but not on every column."

**Follow-up: When should you NOT use an index?**

"1. **Small tables** — full table scan is faster than index lookup.
2. **Columns with low cardinality** — like gender (M/F). Index doesn't help much.
3. **Frequently updated columns** — index maintenance overhead.
4. **Columns not used in WHERE, JOIN, or ORDER BY** — index is useless."

**Follow-up: How do you decide which columns to index?**

"I look at:
1. **Query patterns** — which columns are used in WHERE, JOIN, ORDER BY.
2. **Cardinality** — high cardinality columns benefit more.
3. **Read/write ratio** — read-heavy tables benefit more from indexes.
4. **Existing indexes** — avoid redundant indexes.

I also use EXPLAIN to see which indexes are being used."

---

**Q70. How do you optimize a slow SQL query?**

"This is a very common interview question. My approach:

**Step 1: Analyze the query**
- Use `EXPLAIN` to see the execution plan.
- Check for full table scans, missing indexes, and expensive joins.

**Step 2: Check indexes**
- Add indexes on columns used in WHERE, JOIN, ORDER BY.
- Consider composite indexes for multi-column filters.
- Remove unused or redundant indexes.

**Step 3: Optimize the query**
- Select only required columns — avoid `SELECT *`.
- Use `LIMIT` for pagination.
- Avoid subqueries where joins work better.
- Use `EXISTS` instead of `IN` for large datasets.

**Step 4: Optimize the schema**
- Normalize or denormalize based on query patterns.
- Use appropriate data types.
- Partition large tables.

**Step 5: Use caching**
- Cache frequent queries in Redis.
- Use query result caching.

**Step 6: Monitor and iterate**
- Use slow query log.
- Monitor performance metrics.
- Continuously optimize."

**Follow-up: What is EXPLAIN?**

"EXPLAIN shows the execution plan of a query. It tells you:
- Which indexes are used
- How many rows are scanned
- The join order
- Whether temporary tables are used
- Whether filesort is used

Example:
```sql
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
```

Output shows `type`, `key`, `rows`, `Extra`. If `type` is `ALL`, it's a full table scan. If `key` is NULL, no index is used."

**Follow-up: What is the difference between EXPLAIN and EXPLAIN ANALYZE?**

"**EXPLAIN** shows the estimated plan. **EXPLAIN ANALYZE** actually runs the query and shows actual execution time. EXPLAIN ANALYZE is more accurate but runs the query."

---

**Q71. Explain INNER JOIN.**

"INNER JOIN returns only matching records from both tables. If there's no match, the row is excluded."

```sql
SELECT users.name, orders.id
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

This returns only users who have placed orders."

**Follow-up: What is the difference between INNER JOIN and JOIN?**

"INNER JOIN and JOIN are the same. JOIN is just shorthand for INNER JOIN. Both return only matching records."

**Follow-up: What is a self-join?**

"A self-join is joining a table with itself. Used for hierarchical data.

```sql
-- Find employees and their managers
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```"

---

**Q72. Difference between LEFT JOIN and INNER JOIN?**

"**INNER JOIN** returns only matching records from both tables.

**LEFT JOIN** returns all records from the left table, even if there's no matching record in the right table. For non-matching rows, right table columns are NULL."

```sql
-- INNER JOIN: only users with orders
SELECT users.name, orders.id
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN: all users, even without orders
SELECT users.name, orders.id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

**Follow-up: What is RIGHT JOIN?**

"RIGHT JOIN is the opposite of LEFT JOIN. It returns all records from the right table, even if there's no match in the left table.

In practice, RIGHT JOIN is rarely used because you can achieve the same with LEFT JOIN by swapping table order."

**Follow-up: What is FULL OUTER JOIN?**

"FULL OUTER JOIN returns all records from both tables, with NULLs where there's no match. MySQL doesn't support FULL OUTER JOIN directly — you have to use UNION of LEFT JOIN and RIGHT JOIN."

---

**Q73. What is GROUP BY?**

"GROUP BY is used to combine rows with the same values and perform aggregate operations. It's used with aggregate functions like COUNT, SUM, AVG, MIN, MAX."

```sql
SELECT department, COUNT(*) as total
FROM employees
GROUP BY department;
```

This returns the count of employees in each department."

**Follow-up: Can you use GROUP BY without aggregate functions?**

"Yes, but it's not very useful. GROUP BY without aggregate functions just returns unique combinations of the grouped columns.

```sql
SELECT department FROM employees GROUP BY department;
```

This is similar to `SELECT DISTINCT department FROM employees`."

**Follow-up: What is the order of execution of SQL clauses?**

"1. FROM
2. JOIN
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

This is important because WHERE filters before grouping, and HAVING filters after grouping."

---

**Q74. Difference between WHERE and HAVING?**

"**WHERE** filters rows before grouping. It cannot use aggregate functions.

**HAVING** filters groups after GROUP BY. It can use aggregate functions."

```sql
-- WHERE: filter before grouping
SELECT department, AVG(salary)
FROM employees
WHERE salary > 50000
GROUP BY department;

-- HAVING: filter after grouping
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

**Follow-up: Can you use WHERE and HAVING together?**

"Yes. WHERE filters rows before grouping. HAVING filters groups after grouping.

```sql
SELECT department, AVG(salary)
FROM employees
WHERE status = 'active'
GROUP BY department
HAVING AVG(salary) > 50000;
```

This filters active employees first, then groups by department, then filters departments with average salary > 50000."

---

**Q75. What are aggregate functions?**

"Aggregate functions perform calculations on multiple rows and return a single value. Common ones:

- **COUNT()** — count rows
- **SUM()** — sum values
- **AVG()** — average
- **MIN()** — minimum
- **MAX()** — maximum
- **GROUP_CONCAT()** — concatenate strings"

```sql
SELECT
    COUNT(*) as total_employees,
    AVG(salary) as avg_salary,
    MAX(salary) as max_salary,
    MIN(salary) as min_salary,
    SUM(salary) as total_salary
FROM employees;
```

**Follow-up: What is the difference between COUNT(*) and COUNT(column)?**

"**COUNT(*)** counts all rows, including NULLs.
**COUNT(column)** counts non-NULL values in that column.

```sql
SELECT COUNT(*) FROM users;           -- all users
SELECT COUNT(email) FROM users;       -- users with non-null email
```"

**Follow-up: Can you use aggregate functions without GROUP BY?**

"Yes, but then it returns a single row for the entire table. With GROUP BY, it returns one row per group."

---

# PART 2: SQL ADVANCED (Q76–Q90)

---

**Q76. Explain subquery.**

"A subquery is a query inside another query. It's used when you need the result of one query as input for another."

```sql
-- Find employees earning more than average
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**Follow-up: What are the types of subqueries?**

"1. **Scalar subquery** — returns a single value.
2. **Row subquery** — returns a single row.
3. **Table subquery** — returns a table.
4. **Correlated subquery** — references outer query columns."

```sql
-- Correlated subquery
SELECT * FROM employees e
WHERE salary > (
    SELECT AVG(salary) FROM employees
    WHERE department = e.department
);
```

**Follow-up: What is the difference between IN and EXISTS?**

"**IN** — checks if a value matches any value in a subquery result. It's good for small datasets.

**EXISTS** — checks if a subquery returns any rows. It's more efficient for large datasets because it stops at the first match.

```sql
-- IN
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders);

-- EXISTS
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = u.id);
```"

---

**Q77. What are window functions?**

"Window functions perform calculations across a set of rows without grouping the result into a single row. They are like aggregate functions but don't collapse rows.

Common window functions:
- **ROW_NUMBER()** — sequential number
- **RANK()** — rank with gaps
- **DENSE_RANK()** — rank without gaps
- **LEAD()** — next row value
- **LAG()** — previous row value
- **NTILE()** — divide into buckets"

```sql
-- Second highest salary
SELECT salary FROM (
    SELECT salary,
    DENSE_RANK() OVER(ORDER BY salary DESC) rnk
    FROM employees
) x
WHERE rnk = 2;
```

**Follow-up: What is the difference between RANK and DENSE_RANK?**

"**RANK()** — leaves gaps in ranking. If two rows are tied for 1st, the next rank is 3rd.
**DENSE_RANK()** — no gaps. If two rows are tied for 1st, the next rank is 2nd.

```sql
salary | RANK | DENSE_RANK
10000  | 1    | 1
10000  | 1    | 1
9000   | 3    | 2
8000   | 4    | 3
```"

**Follow-up: What is the difference between ROW_NUMBER and RANK?**

"**ROW_NUMBER()** — always unique, sequential numbers. Ties get different numbers.
**RANK()** — ties get the same rank, with gaps.

```sql
salary | ROW_NUMBER | RANK
10000  | 1          | 1
10000  | 2          | 1
9000   | 3          | 3
```"

---

**Q78. Difference between DELETE, TRUNCATE, DROP?**

"1. **DELETE** — removes selected rows. Supports WHERE condition. Can be rolled back. Slower because it logs each row.

2. **TRUNCATE** — removes all rows quickly. Cannot use WHERE. Resets auto-increment. Faster because it doesn't log each row.

3. **DROP** — removes the complete table structure. Cannot be rolled back.

```sql
-- DELETE
DELETE FROM users WHERE id = 10;

-- TRUNCATE
TRUNCATE TABLE users;

-- DROP
DROP TABLE users;
```

**Follow-up: When to use which?**

"1. **DELETE** — when you need to remove specific rows.
2. **TRUNCATE** — when you need to remove all rows and reset the table.
3. **DROP** — when you need to remove the table entirely."

**Follow-up: Can you rollback TRUNCATE?**

"In MySQL, TRUNCATE cannot be rolled back. In PostgreSQL, it can be rolled back if wrapped in a transaction. It depends on the database."

---

**Q79. What is deadlock?**

"Deadlock happens when two transactions wait for each other to release resources, and neither can continue.

**Example:**
- Transaction A locks Table 1 and waits for Table 2.
- Transaction B locks Table 2 and waits for Table 1.
- Neither can proceed. This is a deadlock.

**Prevention:**
1. Keep transactions short.
2. Access tables in consistent order.
3. Use proper indexing.
4. Set deadlock timeout.
5. Use lower isolation levels when possible."

**Follow-up: How do you detect deadlocks?**

"1. **Database logs** — MySQL logs deadlocks.
2. **Monitoring tools** — like Percona Monitoring.
3. **Application logs** — catch deadlock exceptions.
4. **INNODB_STATUS** — shows current locks and transactions.

```sql
SHOW ENGINE INNODB STATUS;
```"

**Follow-up: What does MySQL do when a deadlock occurs?**

"MySQL automatically detects deadlocks and rolls back one of the transactions. The rolled-back transaction gets an error. The application should catch this error and retry."

---

**Q80. How do you design database tables for a new application?**

"This is a very important question. My approach:

**Step 1: Understand requirements**
- What are the entities?
- What are the relationships?
- What are the access patterns?

**Step 2: Identify entities and relationships**
- Entities become tables.
- Relationships become foreign keys or junction tables.

**Step 3: Normalize**
- Apply 1NF, 2NF, 3NF.
- Reduce redundancy.

**Step 4: Define keys and constraints**
- Primary keys
- Foreign keys
- Unique constraints
- Check constraints

**Step 5: Add indexes**
- Based on query patterns.
- On columns used in WHERE, JOIN, ORDER BY.

**Step 6: Review performance**
- Consider denormalization for read-heavy tables.
- Partition large tables.
- Plan for scaling.

**Step 7: Document**
- ER diagrams
- Schema documentation
- Migration scripts"

**Follow-up: Give an example.**

"For an e-commerce application:

```
users: id, name, email, created_at
products: id, name, price, stock, created_at
orders: id, user_id, status, total, created_at
order_items: id, order_id, product_id, quantity, price
categories: id, name, parent_id
product_categories: product_id, category_id
```

Indexes:
- users(email) — for login
- orders(user_id) — for user's orders
- orders(status) — for filtering
- order_items(order_id) — for order details
- products(name) — for search"

---

**Q81. What is a stored procedure?**

"A stored procedure is a precompiled set of SQL statements stored in the database. It can be called multiple times.

**Advantages:**
- Precompiled — faster execution
- Reusable — called from multiple places
- Secure — can control access
- Reduces network traffic

**Disadvantages:**
- Hard to debug
- Database-specific
- Version control difficult

```sql
DELIMITER //
CREATE PROCEDURE GetUsersByRole(IN role_name VARCHAR(50))
BEGIN
    SELECT * FROM users WHERE role = role_name;
END //
DELIMITER ;

CALL GetUsersByRole('admin');
```

**Follow-up: When would you use stored procedures?**

"I use them when:
1. The logic is complex and used frequently.
2. Performance is critical.
3. Multiple applications need the same logic.
4. Security is a concern.

But I avoid them when:
1. The logic changes frequently.
2. The team is not familiar with them.
3. Version control is important."

---

**Q82. What is a trigger?**

"A trigger is a set of SQL statements that automatically execute when a specific event occurs on a table. Events include INSERT, UPDATE, DELETE.

```sql
CREATE TRIGGER after_user_insert
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO user_logs (user_id, action, created_at)
    VALUES (NEW.id, 'INSERT', NOW());
END;
```

**Follow-up: When would you use triggers?**

"I use triggers for:
1. **Audit logging** — track changes to important tables.
2. **Data validation** — enforce complex rules.
3. **Derived columns** — automatically update calculated fields.
4. **Cascade operations** — when foreign key cascade is not enough.

But I avoid triggers when:
1. The logic can be in application code.
2. Debugging is important.
3. Performance is critical."

---

**Q83. What is a view?**

"A view is a virtual table based on a SELECT query. It doesn't store data — it's computed on the fly.

```sql
CREATE VIEW active_users AS
SELECT id, name, email
FROM users
WHERE is_active = 1;

SELECT * FROM active_users;
```

**Follow-up: Why use views?**

"1. **Simplify complex queries** — encapsulate joins and filters.
2. **Security** — expose only specific columns.
3. **Consistency** — same query logic across applications.
4. **Backward compatibility** — when schema changes.

**Follow-up: What is a materialized view?**

"A materialized view stores the result of the query physically. It's faster but needs to be refreshed when underlying data changes. MySQL doesn't support materialized views directly — we simulate them with tables and triggers."

---

**Q84. What is a CTE (Common Table Expression)?**

"A CTE is a temporary result set that can be referenced within a query. It's defined using the WITH clause.

```sql
WITH department_avg AS (
    SELECT department, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department
)
SELECT e.name, e.salary, d.avg_salary
FROM employees e
JOIN department_avg d ON e.department = d.department
WHERE e.salary > d.avg_salary;
```

**Follow-up: CTE vs Subquery?**

"CTEs are more readable, especially for complex queries. They can be referenced multiple times. Subqueries are inline and can't be reused.

For simple queries, subqueries are fine. For complex queries, CTEs are better."

**Follow-up: What is a recursive CTE?**

"A recursive CTE references itself. Used for hierarchical data.

```sql
WITH RECURSIVE employee_hierarchy AS (
    SELECT id, name, manager_id, 1 as level
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy;
```"

---

**Q85. What is the difference between UNION and UNION ALL?**

"**UNION** — combines results and removes duplicates.
**UNION ALL** — combines results without removing duplicates. Faster.

```sql
-- UNION: removes duplicates
SELECT name FROM customers
UNION
SELECT name FROM suppliers;

-- UNION ALL: keeps duplicates
SELECT name FROM customers
UNION ALL
SELECT name FROM suppliers;
```

**Follow-up: Which one is faster?**

"UNION ALL is faster because it doesn't need to sort and remove duplicates. If you know there are no duplicates, use UNION ALL."

---

**Q86. What is the difference between CHAR and VARCHAR?**

"**CHAR** — fixed-length. Always uses the specified length, padding with spaces.
**VARCHAR** — variable-length. Uses only the space needed.

```sql
CHAR(10)    -- always 10 characters
VARCHAR(10) -- up to 10 characters
```

**Follow-up: When to use which?**

"1. **CHAR** — for fixed-length data like country codes, status codes, MD5 hashes.
2. **VARCHAR** — for variable-length data like names, emails, addresses.

CHAR is faster for fixed-length data. VARCHAR saves space for variable-length data."

---

**Q87. What is the difference between TEXT and BLOB?**

"**TEXT** — for large text data. Has character set.
**BLOB** — for binary data. No character set.

```sql
TEXT     -- up to 65,535 characters
LONGTEXT -- up to 4GB
BLOB     -- up to 65,535 bytes
LONGBLOB -- up to 4GB
```

**Follow-up: When to use which?**

"1. **TEXT** — for articles, descriptions, JSON data.
2. **BLOB** — for images, videos, files.

But storing large files in the database is not recommended. Better to store them in S3 or a file system, and store the path in the database."

---

**Q88. What is the difference between DATETIME and TIMESTAMP?**

"**DATETIME** — stores date and time. Range: 1000-01-01 to 9999-12-31. No timezone conversion.
**TIMESTAMP** — stores Unix timestamp. Range: 1970-01-01 to 2038-01-19. Converts to UTC for storage.

```sql
DATETIME  -- '2024-01-15 10:30:00'
TIMESTAMP -- '2024-01-15 10:30:00' (stored as UTC)
```

**Follow-up: Which one to use?**

"I use DATETIME for dates that don't need timezone conversion. I use TIMESTAMP for events that need to be timezone-aware.

For most applications, TIMESTAMP is better because it handles timezones automatically. But it has the 2038 problem — after 2038, TIMESTAMP will overflow."

---

**Q89. What is the difference between TRUNCATE and DROP?**

"**TRUNCATE** — removes all rows from a table but keeps the table structure. Resets auto-increment.
**DROP** — removes the table structure completely.

```sql
TRUNCATE TABLE users;  -- table structure remains
DROP TABLE users;      -- table is deleted
```

**Follow-up: Can you rollback TRUNCATE?**

"In MySQL, TRUNCATE cannot be rolled back. It's a DDL operation. In PostgreSQL, TRUNCATE can be rolled back if wrapped in a transaction."

---

**Q90. What is the difference between a clustered and non-clustered index?**

"**Clustered Index** — determines the physical order of data in the table. Only one per table. Usually the primary key.

**Non-Clustered Index** — separate structure that points to data rows. Multiple per table.

```sql
-- Clustered index (primary key)
CREATE TABLE users (
    id INT PRIMARY KEY,  -- clustered index
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Non-clustered index
CREATE INDEX idx_email ON users(email);
```

**Follow-up: Which one is faster?**

"Clustered index is faster for range queries because data is physically ordered. Non-clustered index is faster for point queries but requires a lookup to fetch the actual row.

In MySQL InnoDB, the primary key is always the clustered index. Secondary indexes store the primary key value and then look up the row."

---

# PART 3: SQL PRACTICE QUERIES

---

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

**11. Find the department with the highest average salary**

```sql
SELECT department, AVG(salary) as avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;
```

**12. Find employees who earn more than their manager**

```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

**13. Find the running total of salaries**

```sql
SELECT name, salary,
    SUM(salary) OVER(ORDER BY id) as running_total
FROM employees;
```

**14. Find the percentage of employees in each department**

```sql
SELECT department,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees) as percentage
FROM employees
GROUP BY department;
```

**15. Find the latest order for each user**

```sql
SELECT u.name, o.id, o.created_at
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE o.created_at = (
    SELECT MAX(created_at) FROM orders
    WHERE user_id = u.id
);
```

---

# PART 4: QUICK REVISION CHECKLIST (Module 4)

---

## SQL Fundamentals

- [ ] SQL vs MySQL vs NoSQL
- [ ] Primary Key vs Unique Key vs Foreign Key
- [ ] Composite Key vs Candidate Key
- [ ] Normalization — 1NF, 2NF, 3NF, BCNF
- [ ] Denormalization — when and why
- [ ] ACID properties — Atomicity, Consistency, Isolation, Durability
- [ ] Transaction — commit, rollback
- [ ] Isolation levels — 4 types
- [ ] Dirty read, non-repeatable read, phantom read
- [ ] Index — types, clustered vs non-clustered
- [ ] Index drawbacks — insert/update/delete overhead
- [ ] When NOT to use index
- [ ] EXPLAIN — query analysis
- [ ] INNER JOIN vs LEFT JOIN vs RIGHT JOIN
- [ ] Self-join
- [ ] GROUP BY + HAVING
- [ ] WHERE vs HAVING
- [ ] Order of SQL clause execution
- [ ] Aggregate functions — COUNT, SUM, AVG, MIN, MAX
- [ ] COUNT(*) vs COUNT(column)

## SQL Advanced

- [ ] Subquery — scalar, row, table, correlated
- [ ] IN vs EXISTS
- [ ] Window functions — ROW_NUMBER, RANK, DENSE_RANK
- [ ] RANK vs DENSE_RANK vs ROW_NUMBER
- [ ] LEAD and LAG
- [ ] DELETE vs TRUNCATE vs DROP
- [ ] Deadlock — cause + prevention + detection
- [ ] Database design — entities, relationships, indexes
- [ ] Stored procedures — advantages, disadvantages
- [ ] Triggers — when to use
- [ ] Views — virtual tables
- [ ] Materialized views
- [ ] CTE — WITH clause
- [ ] Recursive CTE
- [ ] UNION vs UNION ALL
- [ ] CHAR vs VARCHAR
- [ ] TEXT vs BLOB
- [ ] DATETIME vs TIMESTAMP
- [ ] Clustered vs Non-clustered index

---

# PART 5: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Draw the schema** — whiteboard par tables and relationships draw karo.

2. **Explain the query plan** — use EXPLAIN to show how the query will execute.

3. **Think about indexes** — every query should have a supporting index.

4. **Consider scale** — "For 1 million rows, this query would be slow because..."

5. **Talk about trade-offs** — normalization vs denormalization, index vs no index.

6. **Write clean SQL** — use aliases, format queries, add comments.

7. **Test edge cases** — NULL values, empty tables, duplicate data.

8. **Practice live queries** — interviewer may ask you to write a query on the spot.

---

**Practice Tip:** SQL queries ko hands-on practice karo. LeetCode SQL, HackerRank SQL, aur SQLZoo use karo. Product companies mein live query likhne ko bolte hain — especially JOINs, GROUP BY, aur window functions.

---

[← Previous: Module 3](module-3-django-drf.md) | [Back to Index](README.md) | [Next: Module 5 →](module-5-llm-huggingface-celery-aws.md)
