# Module 6: System Design, Scenario-Based & Coding — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 5](module-5-llm-huggingface-celery-aws.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. System design questions mein interviewer tumhari **approach** dekhta hai, sirf answer nahi. Har answer ko natural language mein rakha hai, jaise ek 5.5 years experienced Python backend developer interview mein bolta hai.

---

# PART 1: SYSTEM DESIGN FUNDAMENTALS (Q101–Q115)

---

**Q101. Design an AI-based content moderation system.**

"This is one of the most important system design questions for my profile. Let me explain my approach step by step.

**Step 1: Requirements Clarification**

Before designing, I'd ask:
- What's the expected traffic? (requests per second)
- What's the acceptable latency for moderation?
- Do we need real-time moderation or can it be async?
- What languages? What content types? (text, image, video)
- What's the accuracy requirement?

**Step 2: High-Level Design**

```
User Application
    ↓
Django REST API
    ↓
Validation Layer
    ↓
Task Queue (Celery + Redis)
    ↓
AI Processing Service (Hugging Face / NLP Model)
    ↓
Result Storage (MySQL)
    ↓
Admin Review Dashboard
```

**Step 3: Component Details**

1. **Django REST API** — receives content, validates, stores initial record.
2. **Validation Layer** — checks for empty content, size limits, basic spam patterns.
3. **Task Queue** — Celery + Redis. Pushes moderation task to background.
4. **AI Processing Service** — Celery worker loads Hugging Face model (DistilBERT), runs inference.
5. **Result Storage** — MySQL stores moderation result.
6. **Admin Dashboard** — moderators review flagged content.

**Step 4: Flow**

1. User submits content.
2. API validates and stores with status `pending`.
3. API creates Celery task and returns `202 Accepted` with task ID.
4. Celery worker picks up task.
5. Worker runs NLP model on content.
6. Worker updates content with moderation result.
7. Dashboard shows results in real-time.

**Step 5: Scale Considerations**

- **Horizontal scaling** — multiple API instances, multiple Celery workers.
- **Caching** — Redis for frequent queries.
- **Database** — read replicas for heavy read traffic.
- **Model optimization** — DistilBERT for speed, batching for throughput.
- **Monitoring** — CloudWatch, Sentry, Flower for Celery.

**Follow-up: Why asynchronous processing?**

"Because AI processing can take time — 100ms to several seconds depending on the model. If we call the model synchronously, API response would be slow and users would have a bad experience. Background processing improves response time and scalability.

Also, async allows us to retry failed tasks, scale workers independently, and handle traffic spikes."

**Follow-up: How would you handle a traffic spike?**

"Several strategies:
1. **Auto-scaling** — scale Celery workers based on queue length.
2. **Priority queues** — high-priority content (reports) processed first.
3. **Rate limiting** — prevent abuse.
4. **Batching** — process multiple items together.
5. **Fallback** — if queue is full, use rule-based checks temporarily."

**Follow-up: How would you handle model updates?**

"Rolling deployment:
1. New workers load new model.
2. Traffic slowly shifted to new workers.
3. Old workers drained and terminated.
4. If issues, rollback to old workers.

We also A/B test models — route 10% traffic to new model, compare metrics."

---

**Q102. How will you handle millions of API requests?**

"For high traffic systems, I focus on scalability at every layer.

**1. Load Balancing**
- Application Load Balancer (ALB) distributes traffic.
- Multiple application instances behind ALB.
- Health checks for automatic failover.

**2. Application Layer**
- Stateless Django application — no session data on server.
- Horizontal scaling — add more instances.
- Gunicorn with multiple workers.
- Async views for I/O-bound operations.

**3. Database Layer**
- Read replicas for read-heavy workloads.
- Connection pooling — reduce connection overhead.
- Indexing — optimize frequent queries.
- Partitioning — split large tables.
- Caching — Redis for frequent reads.

**4. Caching Strategy**
- Redis for session data, frequent queries.
- CDN for static assets.
- Browser caching for static content.
- Query result caching.

**5. Async Processing**
- Celery for background tasks.
- Message queues for decoupling.
- Batch processing for bulk operations.

**6. Monitoring & Alerting**
- CloudWatch for metrics.
- Prometheus + Grafana for dashboards.
- Sentry for error tracking.
- Alerts for anomalies.

**7. Auto-scaling**
- Scale based on CPU, memory, request count.
- Scale down during low traffic.
- Predictive scaling for known patterns.

**8. Database Optimization**
- Query optimization.
- Index tuning.
- Denormalization where needed.
- Sharding for very large datasets."

**Follow-up: How do you decide between vertical and horizontal scaling?**

"**Vertical scaling** — increase server size (CPU, RAM). Simpler but limited. Good for databases.
**Horizontal scaling** — add more servers. More complex but unlimited. Good for stateless applications.

For our Django application, we use horizontal scaling. For databases, we start with vertical scaling and then move to read replicas."

**Follow-up: What is the CAP theorem?**

"CAP theorem states that a distributed system can only guarantee two of three:
- **Consistency** — all nodes see the same data.
- **Availability** — every request gets a response.
- **Partition tolerance** — system works despite network failures.

For our system, we prioritize Availability and Partition tolerance (AP) over Consistency. For example, if a moderation result is delayed, we can show 'pending' status rather than blocking the user."

---

**Q103. Your API is slow. How will you debug?**

"This is a very practical question. My approach is systematic.

**Step 1: Reproduce the Issue**
- Get exact request details — URL, method, headers, payload.
- Check if it's consistent or intermittent.
- Check if it's specific to certain users or endpoints.

**Step 2: Measure Response Time**
- Use tools like Postman, curl, or browser DevTools.
- Break down response time:
  - DNS lookup
  - Connection time
  - Time to first byte (TTFB)
  - Content download time

**Step 3: Check Application Logs**
- Look for errors, warnings, slow queries.
- Check request/response logs.
- Look for patterns — time of day, specific endpoints.

**Step 4: Profile the Code**
- Use Django Debug Toolbar (development).
- Use django-silk or cProfile (production).
- Identify slow functions or queries.

**Step 5: Check Database**
- Use EXPLAIN to analyze slow queries.
- Check for missing indexes.
- Check for N+1 queries.
- Check database load, connections.

**Step 6: Check External Services**
- Are we calling external APIs?
- Are they slow?
- Can we cache or move to async?

**Step 7: Check Infrastructure**
- CPU, memory, disk I/O on servers.
- Network latency.
- Load balancer health.

**Step 8: Fix and Verify**
- Apply fix.
- Measure improvement.
- Monitor for regression.

**Follow-up: What are the most common causes of slow APIs?**

"1. **N+1 queries** — most common in Django.
2. **Missing indexes** — full table scans.
3. **Large payloads** — returning too much data.
4. **External API calls** — synchronous calls to slow services.
5. **No caching** — repeating expensive computations.
6. **Memory leaks** — gradual slowdown over time.
7. **Database locks** — contention on popular rows.
8. **Inefficient algorithms** — O(n²) instead of O(n)."

**Follow-up: What tools do you use?**

"**Development:**
- Django Debug Toolbar
- django-silk
- cProfile

**Production:**
- Sentry for errors
- New Relic / Datadog for APM
- CloudWatch for infrastructure
- Slow query log for MySQL
- Flower for Celery"

---

**Q104. How do you improve Django API performance?**

"I focus on several areas.

**1. Database Optimization**
- `select_related` and `prefetch_related` to avoid N+1.
- `only()` and `defer()` to limit fields.
- `values()` and `values_list()` for raw data.
- Indexing on frequently queried columns.
- Database connection pooling.

**2. Query Optimization**
- Avoid `SELECT *` — select only needed fields.
- Use `count()` instead of `len(queryset)`.
- Use `exists()` instead of `if queryset`.
- Use `bulk_create` and `bulk_update` for batch operations.
- Use `iterator()` for large querysets.

**3. Caching**
- Redis for frequent queries.
- `cache_page` for view-level caching.
- Template fragment caching.
- Low-level caching for expensive computations.

**4. Serialization**
- Use `ModelSerializer` for standard CRUD.
- Avoid nested serializers for large datasets.
- Use `SerializerMethodField` sparingly.
- Consider `orjson` for faster JSON.

**5. Async Processing**
- Celery for long-running tasks.
- Async views for I/O-bound operations.
- Background processing for reports, emails.

**6. Pagination**
- Always paginate large datasets.
- Use cursor pagination for real-time data.
- Limit page size.

**7. Middleware**
- Remove unnecessary middleware.
- Optimize custom middleware.
- Use `django.middleware.gzip.GZipMiddleware` for compression.

**8. Deployment**
- Use Gunicorn with multiple workers.
- Nginx for static files and SSL.
- Use HTTP/2 for multiplexing.
- Enable keep-alive.

**9. Monitoring**
- Profile regularly.
- Set up alerts for slow endpoints.
- Track query counts per request."

**Follow-up: What is the difference between only() and defer()?**

"`only()` — fetch only the specified fields.
`defer()` — fetch all fields except the specified ones.

```python
# Only fetch name and email
User.objects.only('name', 'email')

# Fetch all except bio
User.objects.defer('bio')
```

Use `only()` when you need a few fields. Use `defer()` when you need most fields but want to exclude large ones."

**Follow-up: What is iterator() and when to use it?**

"`iterator()` fetches rows one at a time instead of loading all into memory. Useful for large querysets.

```python
for user in User.objects.iterator():
    process(user)
```

Use it when processing large datasets where memory is a concern."

---

**Q105. Design a URL shortener system.**

"This is a classic system design question. Let me explain my approach.

**Step 1: Requirements**
- Shorten long URL to short URL.
- Redirect short URL to original.
- Analytics — click counts, referrers.
- Custom short codes (optional).
- Expiration (optional).

**Step 2: High-Level Design**

```
Client
    ↓
API (Django)
    ↓
Database (MySQL)
    ↓
Cache (Redis)
```

**Step 3: Database Schema**

```sql
CREATE TABLE url_mapping (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    short_code VARCHAR(10) UNIQUE NOT NULL,
    original_url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP NULL,
    click_count INT DEFAULT 0,
    user_id BIGINT,
    INDEX idx_short_code (short_code)
);
```

**Step 4: Short Code Generation**

Options:
1. **Base62 encoding** — convert auto-increment ID to base62. Simple, predictable.
2. **Hash** — MD5/SHA256 of URL, take first 7 chars. Collision risk.
3. **Random** — generate random 7-char string. Need collision check.
4. **Counter with base62** — distributed counter. Scalable.

I'd use Base62 encoding of auto-increment ID for simplicity, or a distributed counter for scale.

**Step 5: API Endpoints**

```
POST /api/shorten
{
    "url": "https://example.com/very/long/url"
}
Response:
{
    "short_url": "https://short.ly/abc123",
    "original_url": "https://example.com/very/long/url"
}

GET /{short_code}
Response: 302 Redirect to original URL
```

**Step 6: Scale Considerations**

1. **Caching** — Redis for frequently accessed URLs.
2. **Database** — read replicas for redirect traffic.
3. **CDN** — for redirects, edge caching.
4. **Rate limiting** — prevent abuse.
5. **Analytics** — async processing for click tracking.

**Follow-up: How do you handle collisions?**

"Several approaches:
1. **Check and retry** — if short code exists, generate new one.
2. **Use auto-increment** — guarantees uniqueness.
3. **UUID** — globally unique but longer.
4. **Hash with salt** — reduces collision.

For Base62 of auto-increment, no collision. For random, we check the database."

**Follow-up: How do you handle 100 million URLs?**

"1. **Sharding** — split by short_code hash.
2. **Distributed counter** — use Redis or ZooKeeper for ID generation.
3. **Read replicas** — for redirect traffic.
4. **CDN** — cache redirects at edge.
5. **Async analytics** — don't block redirect for click tracking."

**Follow-up: How do you handle expired URLs?**

"1. **TTL in Redis** — auto-expire cache.
2. **Database cleanup job** — Celery Beat runs daily.
3. **Lazy deletion** — check expiry on access.
4. **Soft delete** — mark as deleted, cleanup later."

---

**Q106. How will you design a file upload API?**

"File upload is a common requirement. Let me explain my approach.

**Step 1: Requirements**
- Upload files up to X MB.
- Support multiple file types.
- Secure storage.
- Fast upload and download.
- Scalable.

**Step 2: High-Level Design**

```
Client
    ↓
Django API
    ↓
Validate file
    ↓
Upload to S3
    ↓
Store metadata in MySQL
    ↓
Return file URL
```

**Step 3: Why S3?**

1. **Scalable** — unlimited storage.
2. **Durable** — 99.999999999% durability.
3. **Cost-effective** — pay for what you use.
4. **CDN integration** — CloudFront for fast downloads.
5. **Presigned URLs** — secure uploads without exposing credentials.

**Step 4: Upload Flow**

**Option A: Direct upload to S3 (recommended for large files)**
1. Client requests presigned URL from API.
2. API generates presigned URL with S3.
3. Client uploads directly to S3.
4. Client notifies API of successful upload.
5. API stores metadata in MySQL.

**Option B: Upload via API (for small files)**
1. Client uploads to API.
2. API validates file.
3. API uploads to S3.
4. API stores metadata in MySQL.
5. API returns file URL.

**Step 5: Validation**

- File size limit.
- File type (MIME type check).
- Virus scanning (ClamAV or AWS Lambda).
- Rate limiting per user.

**Step 6: Security**

- Presigned URLs with expiry.
- IAM roles for S3 access.
- Encryption at rest (S3 SSE).
- Encryption in transit (HTTPS).
- Signed URLs for download.

**Step 7: Scale Considerations**

1. **Multipart upload** — for large files.
2. **Background processing** — virus scan, thumbnail generation.
3. **CDN** — CloudFront for downloads.
4. **Database** — store metadata, not files.
5. **Cleanup** — remove orphaned files.

**Follow-up: How do you handle large files?**

"Multipart upload:
1. Split file into chunks (5MB each).
2. Upload chunks in parallel.
3. S3 assembles them.
4. Resume on failure.

This is faster and more reliable than single upload."

**Follow-up: How do you handle file security?**

"1. **Validation** — check file type, size.
2. **Virus scanning** — ClamAV or Lambda.
3. **Encryption** — S3 SSE.
4. **Access control** — presigned URLs with expiry.
5. **Isolation** — separate bucket for user uploads.
6. **Audit logging** — track all uploads."

---

**Q107. How do you handle API authentication?**

"For API authentication, I usually use JWT.

**Step 1: Login**
- User sends username/password.
- Server validates credentials.
- Server generates access token and refresh token.

**Step 2: Token Generation**
```python
from rest_framework_simplejwt.tokens import RefreshToken

def login(request):
    user = authenticate(username, password)
    refresh = RefreshToken.for_user(user)
    return {
        'access': str(refresh.access_token),
        'refresh': str(refresh)
    }
```

**Step 3: Token Usage**
- Client stores tokens.
- Client sends access token in `Authorization: Bearer <token>`.
- Server validates token on every request.

**Step 4: Token Refresh**
- When access token expires, client sends refresh token.
- Server validates refresh token.
- Server issues new access token.

**Step 5: Logout**
- Client discards tokens.
- For additional security, blacklist refresh token.

**Follow-up: Where do you store tokens?**

"Trade-offs:
1. **localStorage** — easy but XSS vulnerable.
2. **httpOnly cookies** — more secure, CSRF protection needed.
3. **Memory** — most secure but lost on refresh.

For most applications, httpOnly cookies with CSRF protection is best."

**Follow-up: How do you handle token expiry?**

"1. **Short-lived access tokens** — 15-60 minutes.
2. **Long-lived refresh tokens** — days or weeks.
3. **Automatic refresh** — client refreshes before expiry.
4. **Refresh token rotation** — new refresh token on each use.
5. **Blacklist** — revoke compromised tokens."

**Follow-up: What about API keys?**

"For server-to-server communication, API keys are common. But they're less secure than JWT because:
1. No expiry.
2. No user context.
3. Hard to revoke.

For user-facing APIs, JWT is better. For internal services, API keys with rotation are fine."

---

**Q108. How do you handle API failures?**

"API failures are inevitable. My approach is to handle them gracefully.

**1. Exception Handling**
```python
try:
    result = external_api.call()
except TimeoutError:
    # retry or fallback
except ConnectionError:
    # fallback
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    # return meaningful error
```

**2. Meaningful HTTP Status Codes**
- 400 — client error (bad request).
- 401 — authentication required.
- 403 — permission denied.
- 404 — resource not found.
- 429 — rate limited.
- 500 — server error.
- 503 — service unavailable.

**3. Retry Mechanism**
- Retry on transient failures.
- Exponential backoff.
- Max retries limit.
- Jitter to avoid thundering herd.

**4. Fallback Logic**
- If primary fails, use fallback.
- If AI model fails, use rule-based checks.
- If external API fails, return cached data.

**5. Circuit Breaker**
- After N failures, stop calling service.
- Wait for cooldown period.
- Try again.

**6. Logging and Monitoring**
- Log all failures with context.
- Alert on critical failures.
- Track failure rates.

**Follow-up: What is a circuit breaker?**

"Circuit breaker prevents cascading failures. States:
- **Closed** — normal operation.
- **Open** — after N failures, stop calling.
- **Half-Open** — after cooldown, try one request.

If success, go to Closed. If failure, go back to Open.

Libraries: `pybreaker`, `circuitbreaker`."

**Follow-up: What is exponential backoff with jitter?**

"Exponential backoff — wait time doubles after each retry:
- 1s, 2s, 4s, 8s...

Jitter — add random variation:
- 1s + random(0, 0.5s)
- 2s + random(0, 1s)

Jitter prevents multiple clients from retrying at the same time (thundering herd)."

---

**Q109. Difference between synchronous and asynchronous processing?**

"**Synchronous:**
- User waits for task to complete.
- Simple to implement.
- Blocking.
- Example: API calls external service and waits.

**Asynchronous:**
- Task runs in background.
- User gets immediate response.
- Non-blocking.
- Example: Django sends task to Celery.

**When to use which:**

| Scenario | Sync | Async |
|----------|------|-------|
| Fast operations (<100ms) | ✅ | ❌ |
| Slow operations (>1s) | ❌ | ✅ |
| User needs immediate result | ✅ | ❌ |
| User can wait | ❌ | ✅ |
| Simple logic | ✅ | ❌ |
| Complex, retryable logic | ❌ | ✅ |

**In my moderation project:**
We used async for AI processing because it takes time. User gets immediate response, moderation happens in background."

**Follow-up: What are the challenges of async?**

"1. **Complexity** — harder to debug.
2. **State management** — need to track task status.
3. **Error handling** — retries, dead letter queues.
4. **Monitoring** — need tools like Flower.
5. **Testing** — harder to test async flows."

---

**Q110. When will you use Celery?**

"I use Celery for tasks that don't need immediate response. Examples:

1. **Sending emails** — welcome email, notifications.
2. **Report generation** — PDF, Excel exports.
3. **Data processing** — batch imports, ETL.
4. **AI model processing** — moderation, classification.
5. **Large file processing** — video encoding, image resizing.
6. **Scheduled tasks** — daily cleanup, weekly reports.
7. **External API calls** — sync with third-party services.
8. **Webhook processing** — async handling of webhooks.

**In my projects:**
- Moderation project — AI processing async.
- Automation project — Excel report generation async.
- Freelance projects — email notifications async."

**Follow-up: When NOT to use Celery?**

"1. **Simple operations** — overhead not worth it.
2. **Real-time requirements** — user needs immediate result.
3. **Small scale** — cron or threading is enough.
4. **No Redis/RabbitMQ** — Celery needs a broker.
5. **Simple scheduling** — cron is simpler."

**Follow-up: Celery vs Threading vs Multiprocessing?**

"| Feature | Celery | Threading | Multiprocessing |
|---------|--------|-----------|-----------------|
| Distributed | ✅ | ❌ | ❌ |
| Persistent | ✅ | ❌ | ❌ |
| Retry | ✅ | ❌ | ❌ |
| Scale | ✅ | ❌ | Limited |
| Setup | Complex | Simple | Simple |
| Use case | Background tasks | I/O-bound | CPU-bound |

Celery for distributed, persistent tasks. Threading for simple I/O. Multiprocessing for CPU-heavy."

---

**Q111. Explain caching strategy.**

"Caching stores frequently accessed data in faster storage like Redis.

**Why caching?**
1. **Faster response** — microsecond vs millisecond.
2. **Reduced database load** — fewer queries.
3. **Cost savings** — less database resources.
4. **Better UX** — faster page loads.

**What to cache:**
1. **Frequent queries** — product listings, user profiles.
2. **Expensive computations** — reports, aggregations.
3. **Session data** — user sessions.
4. **API responses** — external API results.
5. **Static assets** — images, CSS, JS.

**Caching strategies:**

1. **Cache-Aside** — application checks cache first, then database.
```python
def get_user(user_id):
    user = cache.get(f'user:{user_id}')
    if user is None:
        user = User.objects.get(id=user_id)
        cache.set(f'user:{user_id}', user, 3600)
    return user
```

2. **Write-Through** — write to cache and database together.
3. **Write-Behind** — write to cache, async to database.
4. **Read-Through** — cache handles database reads.

**Cache invalidation:**
1. **Time-based** — TTL expiry.
2. **Event-based** — invalidate on update.
3. **Manual** — explicit clear.

**In my projects:**
- Redis for session data.
- Redis for frequent queries.
- Django's cache framework with Redis backend."

**Follow-up: What is cache stampede?**

"Cache stampede happens when many requests hit the cache at the same time, find it empty, and all go to the database.

**Solutions:**
1. **Locking** — only one request fetches from database.
2. **Early expiration** — refresh before expiry.
3. **Probabilistic early expiration** — random refresh.
4. **Cache warming** — pre-populate cache."

**Follow-up: What is the difference between Redis and Memcached?**

"| Feature | Redis | Memcached |
|---------|-------|-----------|
| Data types | Strings, lists, sets, hashes | Strings only |
| Persistence | ✅ | ❌ |
| Pub/Sub | ✅ | ❌ |
| Clustering | ✅ | ❌ |
| Use case | General purpose | Simple caching |

Redis is more feature-rich. Memcached is simpler and faster for pure caching."

---

**Q112. How will you design a notification system?**

"Notification system is a common requirement. Let me explain my approach.

**Step 1: Requirements**
- Multiple channels: Email, SMS, Push, In-app.
- Templates for different notifications.
- User preferences — opt-in/opt-out.
- Delivery tracking.
- Retry on failure.

**Step 2: High-Level Design**

```
User Action
    ↓
Create Notification Event
    ↓
Message Queue (Celery + Redis)
    ↓
Notification Service
    ↓
Email / SMS / Push / In-app
```

**Step 3: Database Schema**

```sql
CREATE TABLE notifications (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    type VARCHAR(50),
    title VARCHAR(255),
    body TEXT,
    channel VARCHAR(20),
    status VARCHAR(20),
    created_at TIMESTAMP,
    sent_at TIMESTAMP,
    read_at TIMESTAMP
);

CREATE TABLE notification_preferences (
    user_id BIGINT,
    channel VARCHAR(20),
    enabled BOOLEAN
);
```

**Step 4: Flow**

1. User action triggers notification event.
2. Event is queued in Celery.
3. Worker processes event:
   - Check user preferences.
   - Render template.
   - Send via appropriate channel.
   - Update status.
4. Retry on failure.

**Step 5: Scale Considerations**

1. **Queue** — Celery for async processing.
2. **Rate limiting** — per user, per channel.
3. **Batching** — group notifications.
4. **Priority** — urgent vs normal.
5. **Monitoring** — delivery rates, failures.
6. **Fallback** — if email fails, try SMS."

**Follow-up: How do you handle delivery failures?**

"1. **Retry** — with exponential backoff.
2. **Fallback** — try alternative channel.
3. **Dead letter queue** — after max retries.
4. **Alerting** — notify admins.
5. **Logging** — track all attempts."

**Follow-up: How do you avoid spamming users?**

"1. **Rate limiting** — max N notifications per hour.
2. **Batching** — group similar notifications.
3. **Preferences** — respect opt-out.
4. **Quiet hours** — no notifications at night.
5. **Digest** — daily/weekly summary."

---

**Q113. How do you handle database scaling?**

"Database scaling is critical for high-traffic applications. My approach:

**1. Vertical Scaling**
- Increase CPU, RAM, storage.
- Simple but limited.
- Good for starting out.

**2. Read Replicas**
- Master for writes, replicas for reads.
- Reduces load on master.
- Replication lag is a concern.

**3. Sharding**
- Split data across multiple databases.
- Shard by user_id, region, etc.
- Complex but scalable.

**4. Partitioning**
- Split large tables into smaller ones.
- Range, list, or hash partitioning.
- Improves query performance.

**5. Connection Pooling**
- Reuse database connections.
- Reduces connection overhead.
- PgBouncer, HikariCP.

**6. Caching**
- Redis for frequent queries.
- Reduces database load.
- Cache invalidation is key.

**7. Query Optimization**
- Indexing.
- Query rewriting.
- Denormalization.

**8. Database Choice**
- MySQL for transactional.
- PostgreSQL for complex queries.
- NoSQL for specific use cases.

**Follow-up: What is sharding?**

"Sharding splits data across multiple databases. Each shard has a subset of data.

**Approaches:**
1. **Range sharding** — by ID range.
2. **Hash sharding** — by hash of key.
3. **Geographic sharding** — by region.

**Challenges:**
1. **Cross-shard queries** — expensive.
2. **Rebalancing** — adding shards.
3. **Transactions** — across shards.
4. **Complexity** — harder to manage."

**Follow-up: What is replication lag?**

"Replication lag is the delay between writing to master and reading from replica. Causes:
1. Network latency.
2. High write load.
3. Slow replica.

**Solutions:**
1. **Read from master** for critical reads.
2. **Monitor lag** and alert.
3. **Semi-synchronous replication**.
4. **Application-level awareness** — route reads appropriately."

---

**Q114. Explain microservices architecture.**

"Microservices means breaking a large application into smaller independent services. Each service handles a specific business responsibility and communicates through APIs or messaging systems.

**Key characteristics:**
1. **Independently deployable** — each service can be deployed separately.
2. **Loosely coupled** — services don't depend on each other's internals.
3. **Single responsibility** — each service does one thing well.
4. **Decentralized data** — each service owns its data.
5. **Technology flexibility** — different services can use different tech.

**Example: E-commerce**
- User Service — authentication, profiles.
- Product Service — catalog, search.
- Cart Service — shopping cart.
- Order Service — order processing.
- Payment Service — payments.
- Notification Service — emails, SMS.

**Communication:**
1. **Synchronous** — REST, gRPC.
2. **Asynchronous** — message queues (RabbitMQ, Kafka).

**Benefits:**
1. **Independent deployment** — no coordination.
2. **Better scalability** — scale only what's needed.
3. **Technology flexibility** — right tool for the job.
4. **Fault isolation** — one service failure doesn't bring down everything.
5. **Team autonomy** — teams own services.

**Challenges:**
1. **Complexity** — distributed systems are hard.
2. **Network latency** — inter-service calls.
3. **Data consistency** — distributed transactions.
4. **Monitoring** — harder to debug.
5. **Deployment** — need orchestration (Kubernetes)."

**Follow-up: When would you use microservices?**

"I'd use microservices when:
1. **Large team** — multiple teams can work independently.
2. **Complex domain** — different parts have different needs.
3. **Scale requirements** — different services need different scaling.
4. **Technology diversity** — different services need different tech.

I'd avoid microservices when:
1. **Small team** — overhead not worth it.
2. **Simple domain** — monolith is simpler.
3. **Startup** — focus on product, not infrastructure.
4. **Tight deadlines** — microservices take longer."

**Follow-up: How do services communicate?**

"1. **REST APIs** — simple, widely used.
2. **gRPC** — fast, binary protocol.
3. **Message queues** — async, decoupled.
4. **Event streaming** — Kafka for high throughput.
5. **GraphQL** — flexible queries.

For our moderation system, REST APIs for sync communication and Celery for async."

---

**Q115. Monolith vs Microservices?**

"**Monolith:**
- Single deployable unit.
- All code in one repository.
- Simple to develop and deploy.
- Good for small teams and startups.

**Microservices:**
- Multiple independent services.
- Each service has its own repository.
- Complex to develop and deploy.
- Good for large teams and complex domains.

**Comparison:**

| Aspect | Monolith | Microservices |
|--------|----------|---------------|
| Development | Simple | Complex |
| Deployment | One unit | Many units |
| Scaling | Whole app | Per service |
| Technology | Single stack | Polyglot |
| Data | Shared DB | Per-service DB |
| Team | Small | Large |
| Debugging | Easy | Hard |
| Latency | Low | Network overhead |
| Fault isolation | Poor | Good |

**When to use which:**

**Monolith:**
- Small team
- Simple domain
- Startup phase
- Tight deadlines

**Microservices:**
- Large team
- Complex domain
- Scale requirements
- Technology diversity

**In my experience:**
I've worked on monoliths (Neighborshook) and I'd recommend starting with a monolith and extracting microservices as needed. Don't start with microservices — it's premature optimization."

**Follow-up: What is a modular monolith?**

"A modular monolith is a monolith with clear module boundaries. Each module has its own data and logic, but they're deployed together.

This gives you:
1. **Simplicity of monolith** — one deployment.
2. **Modularity of microservices** — clear boundaries.

When you need to scale, you can extract modules into microservices."

**Follow-up: How do you migrate from monolith to microservices?**

"**Strangler Fig Pattern:**
1. Start with monolith.
2. Identify a module to extract.
3. Build new microservice.
4. Route traffic to new service.
5. Remove old module.

Repeat until monolith is gone.

**Key principles:**
1. **Don't do it all at once** — incremental migration.
2. **Maintain compatibility** — APIs, data.
3. **Monitor carefully** — catch issues early.
4. **Have rollback plan** — revert if needed."

---

# PART 2: CODING QUESTIONS (Q116–Q120)

---

**Q116. Coding: Reverse a string.**

"This is a fundamental question. I'd explain multiple approaches.

**Approach 1: Slicing (Pythonic)**
```python
def reverse_string(value):
    return value[::-1]

print(reverse_string("python"))
# Output: nohtyp
```

**Approach 2: Loop**
```python
def reverse_string_loop(value):
    result = ""
    for char in value:
        result = char + result
    return result
```

**Approach 3: Recursion**
```python
def reverse_string_recursive(value):
    if len(value) <= 1:
        return value
    return reverse_string_recursive(value[1:]) + value[0]
```

**Approach 4: Two pointers (in-place for list)**
```python
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
```

**Complexity:**
- Slicing: O(n) time, O(n) space.
- Loop: O(n²) time, O(n) space (string concatenation).
- Recursion: O(n²) time, O(n) space.
- Two pointers: O(n) time, O(1) space.

**Follow-up: What if the string is very large?**

"For very large strings, slicing creates a new string, which uses memory. If memory is a concern, I'd use a generator or process in chunks.

Also, Python strings are immutable, so in-place reversal isn't possible. We'd need to convert to a list first."

**Follow-up: How do you reverse words in a sentence?**

```python
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_words("I love Python"))
# Output: Python love I
```

---

**Q117. Coding: Check palindrome.**

"A palindrome reads the same forwards and backwards.

**Approach 1: Slicing**
```python
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
```

**Approach 2: Two pointers**
```python
def is_palindrome_two_pointers(text):
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Approach 3: Ignore case and spaces**
```python
def is_palindrome_clean(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome_clean("A man a plan a canal Panama"))  # True
```

**Complexity:**
- Slicing: O(n) time, O(n) space.
- Two pointers: O(n) time, O(1) space.
- Clean: O(n) time, O(n) space.

**Follow-up: How do you check if a number is a palindrome?**

```python
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

# Without converting to string
def is_palindrome_number_math(n):
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num
```

---

**Q118. Coding: Find duplicate elements in list.**

"**Approach 1: Using set**
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

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
# Output: [2, 3]
```

**Approach 2: Using Counter**
```python
from collections import Counter

def find_duplicates_counter(nums):
    count = Counter(nums)
    return [num for num, c in count.items() if c > 1]
```

**Approach 3: Using set difference**
```python
def find_duplicates_set(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)
```

**Complexity:**
- All approaches: O(n) time, O(n) space.

**Follow-up: What if you can't use extra space?**

"If the list is sorted, we can use two pointers:
```python
def find_duplicates_sorted(nums):
    nums.sort()
    duplicates = []
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            if not duplicates or duplicates[-1] != nums[i]:
                duplicates.append(nums[i])
    return duplicates
```

Time: O(n log n) for sort, O(n) for scan. Space: O(1) extra."

**Follow-up: How do you find the first duplicate?**

```python
def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None
```

---

**Q119. Coding: Count frequency of words.**

"**Approach 1: Using dictionary**
```python
def word_count(sentence):
    result = {}
    for word in sentence.split():
        result[word] = result.get(word, 0) + 1
    return result

print(word_count("the quick brown fox the lazy dog the"))
# Output: {'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'lazy': 1, 'dog': 1}
```

**Approach 2: Using Counter**
```python
from collections import Counter

def word_count_counter(sentence):
    return dict(Counter(sentence.split()))
```

**Approach 3: Using defaultdict**
```python
from collections import defaultdict

def word_count_defaultdict(sentence):
    result = defaultdict(int)
    for word in sentence.split():
        result[word] += 1
    return dict(result)
```

**Complexity:**
- All approaches: O(n) time, O(n) space.

**Follow-up: How do you handle case sensitivity?**

```python
def word_count_case_insensitive(sentence):
    return dict(Counter(sentence.lower().split()))
```

**Follow-up: How do you handle punctuation?**

```python
import re

def word_count_clean(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return dict(Counter(words))
```

---

**Q120. Coding: Find second largest number.**

"**Approach 1: Sort and pick**
```python
def second_largest(nums):
    unique = list(set(nums))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

print(second_largest([10, 5, 20, 8, 20]))  # 10
```

**Approach 2: Single pass**
```python
def second_largest_one_pass(nums):
    first = second = float('-inf')
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None
```

**Approach 3: Using heapq**
```python
import heapq

def second_largest_heap(nums):
    unique = set(nums)
    if len(unique) < 2:
        return None
    return heapq.nlargest(2, unique)[1]
```

**Complexity:**
- Sort: O(n log n) time, O(n) space.
- Single pass: O(n) time, O(1) space.
- Heap: O(n log k) time, O(k) space.

**Follow-up: What if there are duplicates?**

"Duplicates should be ignored. I use `set()` to remove duplicates before finding the second largest.

```python
nums = [10, 5, 20, 8, 20]
unique = set(nums)  # {10, 5, 20, 8}
# Second largest is 10
```

**Follow-up: What if the list has less than 2 unique elements?**

"Return None or raise an exception:
```python
if len(unique) < 2:
    return None
```"

---

# PART 3: PRODUCTION SCENARIOS (Q121–Q130)

---

**Q121. How do you handle production bugs?**

"Production bugs require a systematic approach.

**Step 1: Detect**
- Monitoring alerts.
- User reports.
- Log analysis.

**Step 2: Assess Impact**
- How many users affected?
- What's the severity?
- Is it a security issue?

**Step 3: Reproduce**
- Get exact conditions.
- Try in staging environment.
- Check logs for context.

**Step 4: Debug**
- Check recent deployments.
- Look at error messages.
- Analyze database state.
- Use debugging tools.

**Step 5: Fix**
- Write minimal fix.
- Add test to prevent regression.
- Review with team.

**Step 6: Deploy**
- Deploy to staging first.
- Test thoroughly.
- Deploy to production.
- Monitor closely.

**Step 7: Post-mortem**
- Document the issue.
- Identify root cause.
- Improve processes.
- Update runbooks.

**Follow-up: What if the bug is in production and users are affected?**

"1. **Mitigate first** — rollback if possible.
2. **Communicate** — notify users, status page.
3. **Fix** — root cause fix.
4. **Deploy** — carefully, with monitoring.
5. **Verify** — confirm fix.
6. **Post-mortem** — prevent recurrence."

**Follow-up: How do you prevent production bugs?**

"1. **Code reviews** — catch issues early.
2. **Testing** — unit, integration, E2E.
3. **Staging environment** — test before production.
4. **Canary deployment** — gradual rollout.
5. **Feature flags** — toggle features.
6. **Monitoring** — catch issues early.
7. **Post-mortems** — learn from mistakes."

---

**Q122. A database query is taking 10 seconds. What will you do?**

"10 seconds is way too slow. My approach:

**Step 1: Analyze the Query**
```sql
EXPLAIN SELECT * FROM orders 
JOIN users ON orders.user_id = users.id 
WHERE orders.created_at > '2024-01-01';
```

Check:
- Full table scan?
- Missing indexes?
- Expensive joins?

**Step 2: Check Indexes**
- Add index on `orders.created_at`.
- Add index on `orders.user_id`.
- Consider composite index.

**Step 3: Optimize the Query**
- Select only needed columns.
- Avoid `SELECT *`.
- Use `LIMIT` for pagination.
- Rewrite subqueries as joins.

**Step 4: Check Database Load**
- CPU, memory, disk I/O.
- Active connections.
- Lock contention.

**Step 5: Consider Caching**
- Cache frequent queries.
- Use materialized views.

**Step 6: Denormalize if Needed**
- Add redundant columns.
- Pre-compute aggregates.

**Step 7: Partition Large Tables**
- Range partition by date.
- Hash partition by ID.

**Follow-up: How do you add an index without downtime?**

"1. **Online DDL** — MySQL 5.6+ supports online index creation.
```sql
ALTER TABLE orders ADD INDEX idx_created_at (created_at), ALGORITHM=INPLACE, LOCK=NONE;
```

2. **pt-online-schema-change** — Percona tool for online schema changes.
3. **gh-ost** — GitHub's tool for online schema changes.

These allow index creation without locking the table."

**Follow-up: What if the query is still slow after optimization?**

"1. **Check data volume** — is the table too large?
2. **Consider partitioning** — split into smaller tables.
3. **Consider sharding** — distribute across databases.
4. **Consider NoSQL** — if the query pattern doesn't fit SQL.
5. **Consider caching** — Redis for frequent queries."

---

**Q123. How will you design an e-commerce backend?**

"E-commerce is a complex system. Let me break it down.

**Step 1: Core Services**
- User Service — authentication, profiles.
- Product Service — catalog, search.
- Cart Service — shopping cart.
- Order Service — order processing.
- Payment Service — payments.
- Notification Service — emails, SMS.

**Step 2: Database Schema**

```sql
-- Users
CREATE TABLE users (
    id BIGINT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255),
    name VARCHAR(255),
    created_at TIMESTAMP
);

-- Products
CREATE TABLE products (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10,2),
    stock INT,
    category_id BIGINT,
    created_at TIMESTAMP
);

-- Orders
CREATE TABLE orders (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    status VARCHAR(50),
    total DECIMAL(10,2),
    created_at TIMESTAMP
);

-- Order Items
CREATE TABLE order_items (
    id BIGINT PRIMARY KEY,
    order_id BIGINT,
    product_id BIGINT,
    quantity INT,
    price DECIMAL(10,2)
);

-- Cart
CREATE TABLE cart_items (
    id BIGINT PRIMARY KEY,
    user_id BIGINT,
    product_id BIGINT,
    quantity INT
);
```

**Step 3: Key Flows**

**Browse Products:**
- GET /api/products
- Cache in Redis.
- Search via Elasticsearch.

**Add to Cart:**
- POST /api/cart
- Validate stock.
- Update Redis.

**Checkout:**
- POST /api/orders
- Transaction: create order, reserve stock, process payment.
- Async: send confirmation email.

**Step 4: Scale Considerations**

1. **Product catalog** — cache in Redis, CDN for images.
2. **Search** — Elasticsearch for full-text search.
3. **Cart** — Redis for fast access.
4. **Orders** — database with read replicas.
5. **Payments** — async processing, retry.
6. **Notifications** — Celery for async.

**Follow-up: How do you handle inventory?**

"1. **Reserve on cart** — soft reservation.
2. **Reserve on order** — hard reservation.
3. **Decrement on payment** — final.
4. **Release on cancellation** — return to inventory.

Use transactions to ensure consistency."

**Follow-up: How do you handle payment failures?**

"1. **Retry** — for transient failures.
2. **Fallback** — alternative payment method.
3. **Rollback** — cancel order, release inventory.
4. **Notify** — inform user.
5. **Log** — for reconciliation."

---

**Q124. How do you handle large data processing in Python?**

"I avoid loading everything into memory. My approaches:

**1. Generators**
```python
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file('large.txt'):
    process(line)
```

**2. Batch Processing**
```python
def process_in_batches(queryset, batch_size=1000):
    total = queryset.count()
    for start in range(0, total, batch_size):
        batch = queryset[start:start+batch_size]
        process_batch(batch)
```

**3. Pandas Chunk Processing**
```python
import pandas as pd

for chunk in pd.read_csv('large.csv', chunksize=10000):
    process(chunk)
```

**4. Celery for Background**
```python
@shared_task
def process_large_dataset(dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    for chunk in dataset.get_chunks():
        process(chunk)
```

**5. Database-Level Filtering**
```python
# Instead of filtering in Python
users = User.objects.filter(active=True)

# Use database
active_users = User.objects.filter(is_active=True)
```

**6. Multiprocessing**
```python
from multiprocessing import Pool

def process_chunk(chunk):
    return [process(item) for item in chunk]

with Pool(processes=4) as pool:
    results = pool.map(process_chunk, chunks)
```

**Follow-up: What is the memory limit for Python?**

"Python's memory is limited by the system. On a 64-bit system, it's theoretically 16 exabytes, but practically limited by RAM.

For large data, use:
1. **Generators** — process one item at a time.
2. **Chunking** — process in batches.
3. **Streaming** — read/write incrementally.
4. **External storage** — use disk instead of memory.
5. **Distributed processing** — Spark, Dask."

**Follow-up: How do you process 1 TB of data?**

"1. **Don't load it all** — use streaming.
2. **Chunk it** — process in batches.
3. **Parallelize** — use multiprocessing or Spark.
4. **Use disk** — SQLite, Parquet.
5. **Distribute** — Spark, Dask, Ray.

For 1 TB, I'd use Spark or Dask on a cluster."

---

**Q125. How do you write clean Python code?**

"Clean code is readable, maintainable, and testable. My principles:

**1. Meaningful Names**
```python
# Bad
def calc(a, b):
    return a * b

# Good
def calculate_total_price(quantity, unit_price):
    return quantity * unit_price
```

**2. Small Functions**
```python
# Bad — does too much
def process_order(order):
    # validate
    # calculate
    # save
    # notify
    pass

# Good — single responsibility
def validate_order(order): ...
def calculate_total(order): ...
def save_order(order): ...
def notify_customer(order): ...
```

**3. Type Hints**
```python
def get_user(user_id: int) -> Optional[User]:
    ...
```

**4. Docstrings**
```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discounted price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Discounted price
    """
    return price * (1 - discount_percent / 100)
```

**5. Exception Handling**
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
```

**6. PEP 8**
- 4 spaces for indentation.
- Max 79 characters per line.
- Two blank lines between functions.
- Imports at top.

**7. Testing**
```python
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(100, 0) == 100
```

**8. DRY (Don't Repeat Yourself)**
```python
# Bad
def get_user_name(user):
    return user.first_name + " " + user.last_name

def get_employee_name(employee):
    return employee.first_name + " " + employee.last_name

# Good
def get_full_name(person):
    return f"{person.first_name} {person.last_name}"
```

**9. KISS (Keep It Simple, Stupid)**
- Avoid over-engineering.
- Simple solutions are better.

**10. Code Reviews**
- Review others' code.
- Get your code reviewed.
- Learn from feedback."

**Follow-up: What tools do you use?**

"1. **Black** — code formatter.
2. **Flake8** — linter.
3. **isort** — import sorter.
4. **mypy** — type checker.
5. **pytest** — testing.
6. **pre-commit** — git hooks.

I configure these in all my projects."

---

**Q126. How do you test Django APIs?**

"I use Django's testing framework and tools like Postman.

**1. Unit Tests**
```python
from django.test import TestCase
from rest_framework.test import APITestCase

class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_create_user(self):
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, 201)

    def test_authenticated_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
```

**2. Integration Tests**
- Test complete flows.
- Database interactions.
- External service mocking.

**3. E2E Tests**
- Test full API flow.
- Use Postman/Newman.
- Test in staging.

**4. What to Test**
- Successful responses.
- Validation errors (400).
- Authentication (401).
- Authorization (403).
- Not found (404).
- Edge cases (empty data, boundaries).

**5. Test Coverage**
```bash
coverage run --source='.' manage.py test
coverage report
```

Aim for 80%+ coverage on critical paths.

**Follow-up: How do you test external services?**

"Use mocking:
```python
from unittest.mock import patch

@patch('myapp.services.external_api.call')
def test_external_api(self, mock_call):
    mock_call.return_value = {'status': 'success'}
    response = self.client.post('/api/process/')
    self.assertEqual(response.status_code, 200)
    mock_call.assert_called_once()
```"

**Follow-up: How do you test Celery tasks?**

"```python
from celery import current_app
from django.test import TestCase

class TaskTest(TestCase):
    def test_process_content(self):
        # Call task synchronously
        result = process_content.apply(args=[content_id])
        self.assertEqual(result.status, 'SUCCESS')
```"

---

**Q127. How do you manage code versions?**

"I use Git. Typical workflow:

**1. Branching Strategy**
- `main` — production.
- `develop` — integration.
- `feature/*` — new features.
- `hotfix/*` — urgent fixes.
- `release/*` — release preparation.

**2. Workflow**
```bash
# Create feature branch
git checkout -b feature/user-authentication

# Make changes
git add .
git commit -m "Add user authentication"

# Push
git push origin feature/user-authentication

# Create PR
# Review
# Merge to develop
```

**3. Commit Messages**
```
feat: add user authentication
fix: resolve login timeout
docs: update API documentation
refactor: simplify user service
test: add tests for auth
```

**4. Pull Requests**
- Small, focused changes.
- Clear description.
- Tests included.
- Code review.

**5. Versioning**
- Semantic versioning: MAJOR.MINOR.PATCH.
- Changelog.
- Git tags.

**Follow-up: What is Git Flow?**

"Git Flow is a branching model:
- `main` — production.
- `develop` — integration.
- `feature/*` — features.
- `release/*` — releases.
- `hotfix/*` — hotfixes.

It's good for structured teams. For smaller teams, simpler models like GitHub Flow work better."

**Follow-up: How do you handle merge conflicts?**

"1. **Pull latest** — get latest changes.
2. **Rebase** — rebase feature branch.
3. **Resolve conflicts** — manually fix.
4. **Test** — ensure everything works.
5. **Push** — update branch.

Best practice: keep branches short-lived to minimize conflicts."

---

**Q128. How do you monitor applications in production?**

"Monitoring is critical for production systems. My approach:

**1. Application Logs**
- Structured logging (JSON).
- Centralized (ELK, CloudWatch).
- Log levels (DEBUG, INFO, WARNING, ERROR).
- Request/response logging.

**2. Metrics**
- Request rate, latency, error rate.
- Database query time.
- Cache hit/miss ratio.
- Celery task success/failure.
- CPU, memory, disk.

**3. Tracing**
- Distributed tracing (Jaeger, Zipkin).
- Request ID across services.
- Span tracking.

**4. Alerts**
- Error rate threshold.
- Latency threshold.
- Queue length.
- Disk space.
- Service health.

**5. Dashboards**
- Grafana for visualization.
- Business metrics (orders, signups).
- Technical metrics (latency, errors).

**6. Tools**
- **CloudWatch** — AWS native.
- **New Relic / Datadog** — APM.
- **Sentry** — error tracking.
- **Prometheus + Grafana** — metrics.
- **Flower** — Celery monitoring.

**Follow-up: What metrics do you track?**

"**Golden Signals:**
1. **Latency** — response time.
2. **Traffic** — request rate.
3. **Errors** — error rate.
4. **Saturation** — resource usage.

**Business metrics:**
- Orders per hour.
- Signups per day.
- Conversion rate.

**Technical metrics:**
- API latency (p50, p95, p99).
- Database query time.
- Cache hit rate.
- Queue length."

**Follow-up: What is the difference between monitoring and observability?**

"**Monitoring** — tracking known metrics. Predefined dashboards and alerts.
**Observability** — understanding unknown issues. Logs, traces, metrics together.

Monitoring answers 'Is the system healthy?'
Observability answers 'Why is the system unhealthy?'"

---

**Q129. Tell me about a technical decision you made.**

"In the AI moderation project, one decision was moving NLP processing from synchronous API calls to background jobs.

**The Problem:**
Initially, the API called the NLP model synchronously. This meant:
- API response time was 2-5 seconds.
- Users had to wait for moderation.
- Under load, API became unresponsive.

**The Decision:**
Move NLP processing to Celery background jobs.

**The Reasoning:**
1. **User experience** — immediate response.
2. **Scalability** — API and workers scale independently.
3. **Reliability** — retries for failures.
4. **Monitoring** — track task status.

**The Implementation:**
1. API creates Celery task and returns `202 Accepted`.
2. Celery worker processes content.
3. Worker updates database.
4. Dashboard shows results.

**The Result:**
- API response time: 2-5s → <100ms.
- Scalability: workers can be added independently.
- Reliability: failed tasks retried.
- Monitoring: Flower for task tracking.

**Follow-up: What was the trade-off?**

"Trade-offs:
1. **Complexity** — more moving parts.
2. **Delayed moderation** — not real-time.
3. **Infrastructure** — need Redis, workers.
4. **Debugging** — harder to trace.

But the benefits outweighed the costs. For moderation, slight delay is acceptable."

**Follow-up: Would you do it differently now?**

"Maybe. I'd consider:
1. **Hybrid approach** — sync for simple rules, async for AI.
2. **Priority queues** — urgent content processed first.
3. **Better monitoring** — more granular metrics.
4. **Load testing** — before launch.

But the core decision was right."

---

**Q130. Why should we hire you?**

"I have strong backend experience with Python, Django, Laravel, REST APIs, MySQL, and production applications.

**What I bring:**

1. **Backend expertise** — 5.5+ years building scalable backends.
2. **AI integration** — Hands-on with Hugging Face Transformers, NLP, DistilBERT.
3. **Production experience** — Deployed and maintained systems at scale.
4. **Full-stack thinking** — From database design to API to deployment.
5. **Problem-solving** — I enjoy debugging complex issues.
6. **Learning mindset** — I learn new technologies as needed.

**What I've done:**

- Built AI-powered content moderation system.
- Optimized slow APIs (2-5s → <100ms).
- Designed database schemas for high-traffic systems.
- Integrated Celery for background processing.
- Deployed Django applications on AWS.

**Why this role:**

I'm looking for a role where I can work on larger backend systems, learn from experienced teams, and take on more challenging responsibilities. I want to grow technically and contribute meaningfully.

**What I'll do:**

- Take ownership of backend features.
- Write clean, tested code.
- Collaborate with the team.
- Learn and adapt quickly.
- Deliver practical solutions.

I'm confident I can contribute from day one and grow with the team."

**Follow-up: What's your biggest weakness?**

"Earlier I used to spend too much time trying to perfect an implementation. Over time, I've learned to balance quality with delivery timelines by prioritizing business requirements first.

I still care about quality, but I've learned to ship iteratively and improve based on feedback."

**Follow-up: Where do you see yourself in 5 years?**

"In 5 years, I see myself as a senior backend engineer or tech lead. I want to:
1. Deepen my expertise in distributed systems.
2. Mentor junior developers.
3. Contribute to open source.
4. Work on impactful projects.

I'm not in a hurry — I want to grow steadily and sustainably."

---

# PART 4: QUICK REVISION CHECKLIST (Module 6)

---

## System Design

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
- [ ] Modular monolith

## Coding

- [ ] Reverse string — slicing, loop, recursion, two pointers
- [ ] Palindrome — slicing, two pointers, clean
- [ ] Find duplicates — set, Counter, two pointers
- [ ] Word count — dict, Counter, defaultdict
- [ ] Second largest — sort, single pass, heap

## Production Scenarios

- [ ] Production bug handling
- [ ] Slow database query debugging
- [ ] E-commerce backend design
- [ ] Large data processing — generators, batch, Pandas
- [ ] Clean Python code — PEP8, type hints, docstrings
- [ ] Django API testing — unit, integration, E2E
- [ ] Git workflow — branching, commits, PRs
- [ ] Production monitoring — logs, metrics, tracing
- [ ] Technical decision explanation
- [ ] Why should we hire you

---

# PART 5: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Structure your answer** — "First I would... Then I would... If X happens, then Y..."

2. **Ask clarifying questions** — don't jump to solution. Understand requirements.

3. **Draw diagrams** — whiteboard par architecture draw karo.

4. **Talk about trade-offs** — every decision has pros and cons.

5. **Mention scale** — "For 1 million requests, this would..."

6. **Connect to your experience** — "In my moderation project, I did..."

7. **Be honest** — "I haven't done this in production, but I would approach it like..."

8. **Think out loud** — interviewer wants to see your thought process.

9. **Practice coding** — write code on paper/whiteboard.

10. **Prepare questions** — ask about team, tech stack, challenges.

---

**Practice Tip:** System design questions mein interviewer tumhari **thinking process** dekhta hai — sirf answer nahi. Bolo "First I would...", "Then I would...", "If X happens, then Y..." — structured approach dikhao. Product companies value clear thinking over perfect answers.

---

[← Previous: Module 5](module-5-llm-huggingface-celery-aws.md) | [Back to Index](README.md) | [Next: DSA →](dsa-questions.md)
