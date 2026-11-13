# Python Backend Interview Preparation

![Stars](https://img.shields.io/github/stars/pkdubey/python-backend-interview-prep)
![Forks](https://img.shields.io/github/forks/pkdubey/python-backend-interview-prep)
![License](https://img.shields.io/github/license/pkdubey/python-backend-interview-prep)
![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

**Pavan Kumar Dubey** — 5.5+ years Python Backend Developer

Real interview questions & answers based on my resume and experience. Every answer is written in human language — the way you'd actually say it in an interview, not the way a textbook would explain it.

---

## Modules

| Module | Topic | Questions |
|--------|-------|-----------|
| [Module 1](module-1-hr-resume-project.md) | HR + Resume + Project | Q1–Q20 |
| [Module 2](module-2-python-core.md) | Python Core + OOPs | Q21–Q70 |
| [Module 3](module-3-django-drf.md) | Django + DRF | Q41–Q75 |
| [Module 4](module-4-mysql-sql.md) | MySQL & SQL | Q61–Q90 |
| [Module 5](module-5-llm-huggingface-celery-aws.md) | LLM, Hugging Face, Celery, Redis, AWS | Q81–Q100 |
| [Module 6](module-6-system-design-coding.md) | System Design + Coding | Q101–Q130 |
| [DSA](dsa-questions.md) | DSA Questions | Q1–Q95 |
| [Practice Code](practice-code.md) | Extra Practice Problems | 20 problems |

---

## What's Inside

### Module 1: HR + Resume + Project
- Tell me about yourself
- Walk me through your resume
- AI moderation project deep dive
- Why Python over PHP
- Strengths, weaknesses, production issues
- Questions to ask the interviewer

### Module 2: Python Core + OOPs
- **Python Basics:** List vs Tuple, Mutable vs Immutable, Shallow vs Deep copy, *args/**kwargs, Decorators, Generators, Iterators, is vs ==, Memory management, Garbage collection, Exception handling, GIL, Threading vs Multiprocessing
- **OOPs in Depth:** Class, Object, self, Constructor, Instance/Static/Local variables, Instance/Class/Static methods, Setter/Getter, Inheritance (5 types), MRO, super(), Method overriding, Operator overloading, Abstract class, Interface, Encapsulation, Polymorphism, Composition vs Aggregation, Diamond problem

### Module 3: Django + DRF
- Django request lifecycle (11 steps)
- Middleware, ORM, Models, Migrations
- select_related vs prefetch_related
- N+1 query problem
- Serializers, APIView vs ViewSet, Router
- JWT authentication flow
- Permission classes, Throttling, Versioning
- Filtering, Pagination, Nested serialization
- File upload, Testing, Schema generation
- Celery background tasks
- Deployment architecture (Nginx + Gunicorn)

### Module 4: MySQL & SQL
- SQL vs MySQL, Keys (Primary/Unique/Foreign/Composite)
- Normalization (1NF, 2NF, 3NF, BCNF)
- ACID properties, Transactions, Isolation levels
- Indexes (clustered vs non-clustered)
- Query optimization, EXPLAIN
- JOINs (INNER, LEFT, RIGHT, FULL)
- GROUP BY, HAVING, Aggregate functions
- Subqueries, Window functions
- CTEs, Recursive CTEs
- Stored procedures, Triggers, Views
- DELETE vs TRUNCATE vs DROP
- Deadlock prevention
- Database design
- 15+ practice queries

### Module 5: LLM, Hugging Face, Celery, Redis, AWS
- AI content moderation project (complete flow)
- LLM, Transformer architecture, Self-Attention
- BERT vs GPT, DistilBERT, Knowledge distillation
- Embeddings, RAG, Vector databases
- Hugging Face, Model evaluation (precision, recall, F1)
- Hallucination handling
- Celery architecture, Redis as broker
- Failed task handling, Exponential backoff
- AWS: EC2, S3, RDS, ElastiCache
- Django AI deployment step-by-step

### Module 6: System Design + Coding
- AI content moderation system design
- Handling millions of API requests
- Debugging slow APIs
- URL shortener design
- File upload API design
- JWT authentication flow
- Notification system design
- Database scaling (read replicas, sharding)
- Monolith vs Microservices
- Coding: reverse string, palindrome, duplicates, word count, second largest
- Production bug handling
- E-commerce backend design
- Large data processing
- Clean code practices
- Git workflow, Monitoring

### DSA Questions
- **Arrays & Strings:** Kadane's, Two Sum, Max Product, Missing Number, First Non-Repeating, Anagram, Group Anagrams, Longest Common Prefix, Rotate Array, Container with Most Water
- **Linked Lists:** Reverse, Cycle Detection, Middle, Merge, Remove Nth, Palindrome
- **Stacks & Queues:** Valid Parentheses, Stack using Queues, Queue using Stacks, Next Greater Element
- **Trees & BST:** Traversals, Height, Balanced, LCA, Validate BST, Kth Smallest, Diameter
- **Graphs:** BFS, DFS, Cycle Detection, Shortest Path, Number of Islands, Clone Graph
- **Dynamic Programming:** Climbing Stairs, Coin Change, LIS, Knapsack, Edit Distance, LCS, House Robber
- **Sorting & Searching:** Binary Search, Quicksort, Mergesort, Kth Largest, Dutch National Flag
- **Hashmaps & Heaps:** Top K Frequent, Median Finder, Kth Smallest in Matrix
- **Recursion & Backtracking:** Permutations, Subsets, N-Queens, Word Search
- **Bit Manipulation:** Power of Two, Count Set Bits, Single Number
- **Additional Problems:** Merge Intervals, Product Except Self, Longest Substring, Container with Water, Three Sum, Trapping Rain Water, Search Rotated Array

### Practice Code
- Fibonacci, Factorial, Prime Check
- Sort Dictionary by Value, Flatten Nested List
- Group Anagrams, Two Sum, Valid Parentheses
- Move Zeroes, Missing Number
- Palindrome Number, Count Vowels
- Remove Duplicates, Intersection of Lists
- String Rotations, First Duplicate
- Sum of Digits, Reverse Words, Longest Word
- Armstrong Number
- Common Patterns: Two Pointers, Sliding Window, Hashmap, Stack, Recursion, Set, Sorting
- Time & Space Complexity Cheat Sheets

---

## How to Use

1. **Read each module in order** — they build on each other
2. **Say the answers out loud** — don't just read, speak them
3. **Prepare for follow-up questions** — that's what interviewers actually ask
4. **Write practice code yourself** — don't copy-paste
5. **Stick to your resume** — only talk about what you actually did
6. **Solve 2-3 DSA problems daily** — consistency beats cramming
7. **Practice system design on a whiteboard** — draw diagrams
8. **Do mock interviews** — with a friend or in front of a mirror

---

## Final Revision (Before the Interview)

### Must-Know Topics

- **AI Moderation Project** — complete flow, Hugging Face/DistilBERT, challenges
- **Django request lifecycle** — 11 steps, middleware
- **Celery + Redis** — producer, broker, worker, failed task handling
- **SQL optimization** — EXPLAIN, indexes, N+1, JOINs
- **Python OOPs** — inheritance, MRO, decorators, generators
- **API design** — URL shortener, file upload, notification
- **JWT authentication** — access + refresh tokens
- **DSA** — binary search, linked list, Kadane, two sum, valid parentheses
- **Database design** — normalization, indexing, scaling
- **System design** — scaling, caching, microservices

### Quick Tips

1. **Clarify requirements** before jumping to a solution
2. **Think out loud** — the interviewer wants to see your thought process
3. **Draw diagrams** — draw architecture on a whiteboard
4. **Talk about trade-offs** — every decision has pros and cons
5. **Mention scale** — "For 1 million requests, this would..."
6. **Be honest** — "I haven't done this in production, but I would approach it like..."
7. **Connect to your experience** — "In my moderation project, I did..."
8. **Practice live coding** — write code on paper or a whiteboard

### Interview Day Checklist

- [ ] All answers aligned with your resume
- [ ] AI moderation project complete flow memorized
- [ ] Django request lifecycle diagram ready
- [ ] Celery + Redis architecture clear
- [ ] SQL query optimization steps ready
- [ ] Python OOPs concepts clear
- [ ] 5-6 system design problems practiced
- [ ] DSA patterns revised
- [ ] Questions for the interviewer ready
- [ ] Confidence — talk about what you actually did

---

## Repo Structure

```
python-backend-interview-prep/
│
├── README.md                                  ← Main index
├── module-1-hr-resume-project.md              ← Q1–Q20
├── module-2-python-core.md                    ← Q21–Q70 (Python + OOPs)
├── module-3-django-drf.md                     ← Q41–Q75
├── module-4-mysql-sql.md                      ← Q61–Q90
├── module-5-llm-huggingface-celery-aws.md     ← Q81–Q100
├── module-6-system-design-coding.md           ← Q101–Q130
├── dsa-questions.md                           ← DSA Q1–Q95
└── practice-code.md                           ← 20 problems
```

---

## Contributing

If you find a mistake or want to add something, feel free to raise an issue or PR.

---

## License

MIT License — free to use for preparation and learning.

---

*Last updated: November 2026 | Maintained by [Pavan Kumar Dubey](https://github.com/pkdubey)*
