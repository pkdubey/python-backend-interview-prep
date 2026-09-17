# Module 6: System Design, Scenario-Based & Coding (Q101–Q130)

[← Back to Index](README.md) | [← Previous: Module 5](module-5-llm-huggingface-celery-aws.md)

---

**Q101. Design an AI-based content moderation system.**

"I would design the system with separate components so that each part can scale independently.

Architecture:
User Application → Django REST API → Validation Layer → Task Queue (Celery + Redis) → AI Processing Service (Hugging Face / NLP Model) → Result Storage (MySQL) → Admin Review Dashboard.

Flow:
User content API ke through receive hota hai. Basic validation ke baad request background queue mein bhej dete hain. Celery worker AI model ko call karta hai. Result database mein store hota hai aur admin dashboard se moderators review kar sakte hain."

**Follow-up: Why asynchronous processing?**

"Because AI processing can take time. If we call the model synchronously, API response slow ho jayega. Background processing improves response time and scalability."

---

**Q102. How will you handle millions of API requests?**

"For high traffic systems, I would focus on scalability:
- Load balancer distribute requests
- Multiple application instances
- Database optimization
- Caching using Redis
- Pagination
- Async processing with Celery
- Monitoring and logging

Instead of increasing resources on one server, I would horizontally scale the application."

---

**Q103. Your API is slow. How will you debug?**

"First I identify where the delay is happening. I check:
1. API response time
2. Database query execution time
3. External API calls
4. Server CPU and memory usage
5. Logs

If database is slow, I optimize queries and indexes. If external APIs are slow, I move them to async processing. If repeated data is requested, I introduce caching."

---

**Q104. How do you improve Django API performance?**

"I improve Django API performance by:
- Optimizing ORM queries
- Using select_related and prefetch_related
- Adding database indexes
- Implementing pagination
- Using Redis caching
- Removing unnecessary API processing
- Moving heavy operations to Celery"

---

**Q105. Design a URL shortener system.**

"The basic flow:
User sends long URL.
API generates a unique short ID.
Store mapping: short_id → original_url in database.
When user opens short URL:
Short ID is searched.
Original URL is returned through redirect.

Database:
url_mapping
id
short_code
original_url
created_at

For scale:
- Redis cache for frequently accessed URLs
- Database indexing on short_code
- Load balancer"

---

**Q106. How will you design a file upload API?**

"I would avoid storing large files directly in the database.

Flow:
Client → Django API → Validate file → Upload to S3 → Store file URL in MySQL.

For large files, I would use multipart upload and background processing."

---

**Q107. How do you handle API authentication?**

"For API authentication, I usually use JWT.

Flow:
User logs in.
Backend validates credentials.
Generates access token.
Client sends token with every request.
Backend validates token before processing."

---

**Q108. How do you handle API failures?**

"I handle failures using:
- Proper exception handling
- Logging
- Retry mechanism
- Meaningful HTTP status codes
- Fallback logic

For external services like AI APIs, temporary failures can be handled using retries with limits."

---

**Q109. Difference between synchronous and asynchronous processing?**

"Synchronous means the user waits until the task completes. Example: API calls external service and waits for response.

Asynchronous means the task runs in background. Example: Django sends task to Celery and immediately returns response."

---

**Q110. When will you use Celery?**

"I use Celery for tasks that don't need immediate response. Examples:
- Sending emails
- Report generation
- Data processing
- AI model processing
- Large file processing"

---

**Q111. Explain caching strategy.**

"Caching stores frequently accessed data in faster storage like Redis.

Example:
If thousands of users request the same product details repeatedly, instead of querying database every time, we store the result in Redis.

Benefits:
- Faster response
- Reduced database load"

---

**Q112. How will you design a notification system?**

"I would separate notification processing from the main application.

Flow:
User Action → Create Notification Event → Message Queue → Notification Service → Email/SMS/Push.

Celery or Kafka can handle background processing."

---

**Q113. How do you handle database scaling?**

"Database scaling approaches:
- Proper indexing
- Query optimization
- Read replicas
- Database partitioning
- Connection pooling
- Caching frequently accessed data"

---

**Q114. Explain microservices architecture.**

"Microservices means breaking a large application into smaller independent services. Each service handles a specific business responsibility and communicates through APIs or messaging systems.

Benefits:
- Independent deployment
- Better scalability
- Technology flexibility"

---

**Q115. Monolith vs Microservices?**

"Monolith means the complete application is deployed as one unit. Microservices split functionality into independent services. For smaller applications, monolith is simpler. For large-scale applications, microservices provide better scalability."

---

**Q116. Coding: Reverse a string.**

```python
def reverse_string(value):
    return value[::-1]

print(reverse_string("python"))
# Output: nohtyp
```

---

**Q117. Coding: Check palindrome.**

```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))  # True
```

---

**Q118. Coding: Find duplicate elements in list.**

```python
def find_duplicates(nums):
    duplicates = []
    seen = set()
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates
```

"Set provides fast lookup with O(1) average complexity."

---

**Q119. Coding: Count frequency of words.**

```python
def word_count(sentence):
    result = {}
    for word in sentence.split():
        result[word] = result.get(word, 0) + 1
    return result
```

---

**Q120. Coding: Find second largest number.**

```python
def second_largest(nums):
    unique = list(set(nums))
    unique.sort()
    return unique[-2]
```

---

**Q121. How do you handle production bugs?**

"First I reproduce the issue. Then I check:
- Application logs
- Error messages
- Database state
- Recent deployments

After identifying the root cause, I fix it, test properly, and deploy carefully."

---

**Q122. A database query is taking 10 seconds. What will you do?**

"I will:
1. Check query execution plan using EXPLAIN.
2. Check missing indexes.
3. Optimize joins.
4. Avoid fetching unnecessary columns.
5. Check database load.
6. Add caching if required."

---

**Q123. How will you design an e-commerce backend?**

"I would divide it into modules:
- User Service
- Product Service
- Cart Service
- Order Service
- Payment Service
- Notification Service

Communication can happen through REST APIs or message queues."

---

**Q124. How do you handle large data processing in Python?**

"I avoid loading everything into memory. Approaches:
- Generators
- Batch processing
- Pandas chunk processing
- Background jobs using Celery
- Database-level filtering"

---

**Q125. How do you write clean Python code?**

"I follow:
- Meaningful naming
- Small reusable functions
- Proper exception handling
- Code comments where required
- PEP8 standards
- Unit testing"

---

**Q126. How do you test Django APIs?**

"I use Django testing framework and tools like Postman. I test:
- Successful responses
- Validation errors
- Authentication
- Permission checks
- Edge cases"

---

**Q127. How do you manage code versions?**

"I use Git. Typical workflow:
- Create feature branch
- Implement changes
- Commit changes
- Raise pull request
- Code review
- Merge into main branch"

---

**Q128. How do you monitor applications in production?**

"I monitor:
- Application logs
- API response time
- Server CPU/memory
- Database performance
- Error rates

For production systems, monitoring helps identify issues before users report them."

---

**Q129. Tell me about a technical decision you made.**

"In the AI moderation project, one decision was moving NLP processing from synchronous API calls to background jobs where possible. The reason was improving API response time and making the system more scalable."

---

**Q130. Why should we hire you?**

"I have strong backend experience with Python, Django, Laravel, REST APIs, MySQL, and production applications. I have also worked on AI integrations using Hugging Face Transformers and automation, which gives me a combination of backend engineering and modern AI application experience. I focus on writing reliable code, understanding business requirements, and delivering practical solutions."

---

## Quick Revision Checklist (Module 6)

- [ ] AI content moderation system design
- [ ] Handling millions of API requests
- [ ] Debugging slow APIs
- [ ] Django API optimization
- [ ] URL shortener design
- [ ] File upload API design
- [ ] JWT authentication flow
- [ ] API failure handling
- [ ] Sync vs Async processing
- [ ] Celery use cases
- [ ] Caching strategy — Redis
- [ ] Notification system design
- [ ] Database scaling — read replicas, partitioning
- [ ] Microservices vs Monolith
- [ ] Coding — reverse string, palindrome
- [ ] Coding — duplicates, word count, second largest
- [ ] Production bug handling
- [ ] Slow SQL query debugging
- [ ] E-commerce backend design
- [ ] Large data processing — generators, batch
- [ ] Clean code practices
- [ ] Django API testing
- [ ] Git workflow
- [ ] Production monitoring
- [ ] Technical decision explanation

---

**Practice Tip:** System design questions mein interviewer tumhari **thinking process** dekhta hai — sirf answer nahi. Bolo "First I would...", "Then I would...", "If X happens, then Y..." — structured approach dikhao.

---

[← Previous: Module 5](module-5-llm-huggingface-celery-aws.md) | [Back to Index](README.md) | [Next: DSA →](dsa-questions.md)
