# Module 3: Django + DRF — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 2](module-2-python-core.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. Har answer ko natural language mein rakha hai, jaise ek 5.5 years experienced Python backend developer interview mein bolta hai.

---

# PART 1: DJANGO FUNDAMENTALS (Q41–Q55)

---

**Q41. Why Django?**

"I prefer Django because it provides many things out of the box — ORM, authentication, security features, admin panel, middleware support, and a structured project architecture.

What I like most is the 'batteries included' philosophy. In my projects, Django helped me build REST APIs quickly while maintaining clean code structure. Instead of spending time on boilerplate, I could focus on business logic.

For API development, I generally use Django REST Framework because it provides serializers, authentication, permissions, and reusable components."

**Follow-up: Why not Flask?**

"Flask is lightweight and flexible — you have complete control. But with that flexibility comes responsibility. Many things like authentication, ORM, admin panel, and security features need additional setup.

For enterprise applications where you need structure and built-in features, Django is a better choice. Flask is good for microservices or when you need a very specific, minimal setup."

**Follow-up: What about FastAPI?**

"FastAPI is excellent for modern async APIs and has great performance. But it doesn't have an ORM or admin panel built-in. For projects that need those, Django is still the better choice. I've used FastAPI for lightweight services and Django for full-featured applications."

---

**Q42. Explain Django request lifecycle.**

"This is one of the most important questions in Django interviews. Let me explain step by step:

1. **Client** sends an HTTP request.
2. Request first reaches the **web server** — like Nginx.
3. Nginx passes it to **Gunicorn** (application server).
4. Gunicorn passes it to **Django through WSGI or ASGI**.
5. Django **middleware** processes the request — each middleware can modify it.
6. **URL resolver** matches the URL pattern to a view.
7. The **view** is called — it interacts with **models through ORM**.
8. **Database** returns the data.
9. The view creates a **response**.
10. Response goes back through **middleware**.
11. Response is sent back to the **client**."

**Follow-up: What is middleware?**

"Middleware is a layer between request and response where we can perform common operations like authentication, logging, security checks, and request modification.

Each middleware has hooks: `process_request`, `process_view`, `process_response`, `process_exception`. Django has built-in middleware for security, sessions, CSRF, authentication, and more."

**Follow-up: How would you draw this on a whiteboard?**

"I'd draw:

Client → Nginx → Gunicorn → Django (Middleware → URL Resolver → View → Model → Database) → Middleware → Client

And I'd highlight that middleware runs twice — once for request, once for response."

---

**Q43. What is ORM in Django?**

"ORM stands for Object Relational Mapping. It allows us to interact with the database using Python objects instead of writing SQL queries manually.

Django ORM converts Python queries into SQL internally. For example:

```python
User.objects.filter(active=True)
```

This gets translated to SQL like `SELECT * FROM users WHERE active = 1`."

**Follow-up: Can you write raw SQL in Django?**

"Yes. Django provides `raw()` and `connection.cursor()` for raw SQL. I use raw SQL when:
- The query is too complex for ORM
- Performance is critical and I need fine control
- I'm doing bulk operations

But 90% of the time, ORM is sufficient and safer."

**Follow-up: What are the advantages of ORM?**

"Several:
1. **Database independence** — code works with MySQL, PostgreSQL, SQLite without changes.
2. **Security** — automatically prevents SQL injection.
3. **Productivity** — less code, faster development.
4. **Maintainability** — Python code is easier to read than SQL."

**Follow-up: What are the disadvantages?**

"1. **Performance** — complex queries can be slower than raw SQL.
2. **Learning curve** — ORM has its own API.
3. **Limited control** — some advanced SQL features are hard to use.
4. **N+1 problem** — easy to accidentally cause performance issues."

---

**Q44. Explain Django Model.**

"A Django model represents a database table. Each model class maps to a database table, and model attributes represent table columns.

Django automatically creates SQL tables through migrations."

```python
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

**Follow-up: What are field types?**

"Common ones:
- `CharField` — for strings, needs max_length
- `TextField` — for long text
- `IntegerField`, `FloatField`, `DecimalField` — for numbers
- `BooleanField` — for true/false
- `DateTimeField`, `DateField` — for dates
- `EmailField`, `URLField` — for validated strings
- `ForeignKey`, `ManyToManyField`, `OneToOneField` — for relationships"

**Follow-up: What is `__str__` method?**

"It returns a human-readable string representation of the model instance. It's used in Django admin, shell, and debugging. Without it, you see something like `<UserProfile: UserProfile object (1)>`."

---

**Q45. What are migrations in Django?**

"Migrations are Django's way of tracking database schema changes. Whenever we create or modify models, Django generates migration files, and then we apply them to update the database.

Two commands:
```bash
python manage.py makemigrations  # creates migration files
python manage.py migrate         # applies them to database
```"

**Follow-up: What if you need to modify an existing migration?**

"You shouldn't modify an applied migration. Instead:
1. Create a new migration with the changes.
2. Or rollback: `python manage.py migrate app_name 0001` (rollback to migration 0001).
3. Then modify and re-migrate."

**Follow-up: What is a data migration?**

"A data migration is a migration that modifies data, not schema. For example, populating a new field, or migrating data from one field to another. You create it with `python manage.py makemigrations --empty app_name`."

---

**Q46. Difference between select_related() and prefetch_related()?**

"This is a very important optimization question.

**select_related()** uses SQL JOIN and fetches related objects in a single query. It's used for ForeignKey and OneToOne relationships.

**prefetch_related()** executes separate queries and combines the results in Python. It's used for ManyToMany and reverse relationships."

```python
# select_related — 1 query
Order.objects.select_related('customer')

# prefetch_related — 2 queries
Order.objects.prefetch_related('items')
```

**Follow-up: When to use which?**

"Rule of thumb:
- ForeignKey or OneToOne → `select_related()`
- ManyToMany or reverse ForeignKey → `prefetch_related()`
- If you need to filter on related fields → `prefetch_related()` with `Prefetch` object

I always think about this when optimizing APIs. The difference can be 100 queries vs 2 queries."

**Follow-up: What is the N+1 problem?**

"N+1 happens when you fetch a list of objects (1 query), then for each object you fetch related data (N queries). So total N+1 queries.

For example:
```python
orders = Order.objects.all()  # 1 query
for order in orders:
    print(order.customer.name)  # N queries
```

Solution: use `select_related('customer')` to fetch everything in 1 query."

---

**Q47. What is N+1 query problem?**

"Already explained in the previous question. Let me give a practical example:

Without optimization:
```python
# 1 query for orders
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)  # N queries
# Total: 1 + N queries
```

With optimization:
```python
# 1 query with JOIN
orders = Order.objects.select_related('customer')
for order in orders:
    print(order.customer.name)  # no additional query
# Total: 1 query
```"

**Follow-up: How do you detect N+1 in production?**

"I use:
1. **Django Debug Toolbar** — shows all queries in development.
2. **django-silk** — profiling tool.
3. **Logging** — log slow queries.
4. **APM tools** — like New Relic, Datadog.

In production, I check query counts per request and alert if they exceed a threshold."

---

**Q48. Difference between Django and Django REST Framework?**

"Django is a complete web framework for building web applications — both frontend and backend. It provides ORM, templates, admin panel, authentication, and more.

Django REST Framework (DRF) is an extension of Django specifically for building REST APIs. It provides:
- Serializers
- API views
- Authentication
- Permissions
- Pagination
- Throttling
- Browsable API"

**Follow-up: Can you build APIs without DRF?**

"Yes, but you'd have to write a lot of boilerplate. DRF provides serializers, which are a huge time-saver. Also, authentication, permissions, and pagination come out of the box. For any serious API project, DRF is the standard."

---

**Q49. What is Serializer in DRF?**

"A Serializer in DRF does two things:
1. **Serialization** — converts complex data (model instances, querysets) into Python native data types (dict, list) that can be easily rendered to JSON.
2. **Deserialization** — validates incoming JSON data and converts it back to model instances."

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

**Follow-up: What is validation in serializers?**

"Serializers validate data in three stages:
1. **Field-level validation** — `validate_<field_name>()` method.
2. **Object-level validation** — `validate()` method.
3. **Validators** — reusable validators like `UniqueValidator`."

```python
class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if not value.endswith('@company.com'):
            raise serializers.ValidationError("Email must be company email")
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords don't match")
        return data
```

---

**Q50. Difference between Serializer and ModelSerializer?**

"**Serializer** requires you to manually define all fields and validation logic. It's more verbose but gives you complete control.

**ModelSerializer** automatically generates fields based on the Django model. It also creates `create()` and `update()` methods automatically.

For standard CRUD APIs, I prefer ModelSerializer because it reduces code significantly."

```python
# Manual Serializer
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance

# ModelSerializer (much shorter)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
```

**Follow-up: When would you use a plain Serializer?**

"When the data doesn't map directly to a model. For example:
- Aggregated data (counts, sums)
- Complex nested structures
- External API responses
- Data that needs custom processing"

---

**Q51. Difference between APIView and ViewSet?**

"**APIView** gives more control. You define each HTTP method separately:
```python
class UserAPIView(APIView):
    def get(self, request):
        ...
    def post(self, request):
        ...
```

**ViewSet** provides a higher-level abstraction. Common CRUD operations are already structured:
```python
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

With ViewSet, you get list, create, retrieve, update, destroy methods automatically."

**Follow-up: When to use which?**

"Use **APIView** when:
- You need custom logic for each endpoint
- The endpoint doesn't fit standard CRUD
- You want explicit control over HTTP methods

Use **ViewSet** when:
- You have standard CRUD operations
- You want to reduce boilerplate
- You're using a Router for URL mapping

For most REST APIs, ViewSets are the standard choice."

---

**Q52. What is Router in DRF?**

"Router automatically generates URL patterns for ViewSets. Instead of manually creating URLs for every CRUD operation, router handles URL mapping.

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
```

This generates:
- `GET /users/` → list
- `POST /users/` → create
- `GET /users/{id}/` → retrieve
- `PUT /users/{id}/` → update
- `PATCH /users/{id}/` → partial update
- `DELETE /users/{id}/` → destroy"

**Follow-up: What are the types of routers?**

"1. **SimpleRouter** — basic URL mapping.
2. **DefaultRouter** — extends SimpleRouter with a root API view.
3. **Custom Router** — you can create your own for specific needs.

I usually use DefaultRouter because the root API view is helpful for development."

---

**Q53. How do you implement authentication in Django REST API?**

"Common approaches:
1. **Session Authentication** — uses Django sessions. Good for web apps.
2. **Token Authentication** — simple tokens. Good for mobile apps.
3. **JWT Authentication** — JSON Web Tokens. Stateless, good for distributed systems.
4. **OAuth2** — for third-party integrations."

**Follow-up: Which one do you use?**

"For API-based applications, I use JWT. It's stateless, works well with mobile and frontend applications, and scales horizontally.

For internal tools, session authentication is simpler.

For third-party integrations, OAuth2 is the standard."

**Follow-up: How do you configure JWT in DRF?**

"Using `djangorestframework-simplejwt`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```"

---

**Q54. Explain JWT authentication flow.**

"1. **Login** — user sends username and password to `/api/token/`.
2. **Validation** — server validates credentials.
3. **Token generation** — server generates access token and refresh token.
4. **Token storage** — client stores tokens (usually in localStorage or cookies).
5. **Subsequent requests** — client sends access token in Authorization header: `Authorization: Bearer <token>`.
6. **Validation** — backend validates token signature and expiration.
7. **Access granted** — if valid, request is processed.
8. **Refresh** — when access token expires, client sends refresh token to get new access token."

**Follow-up: What is the difference between access and refresh token?**

"**Access token** — short-lived (usually 15-60 minutes). Used for API requests.
**Refresh token** — long-lived (days or weeks). Used to get new access tokens.

This reduces the risk of token theft — if an access token is stolen, it expires quickly."

**Follow-up: Where do you store tokens?**

"There are trade-offs:
- **localStorage** — easy but vulnerable to XSS.
- **httpOnly cookies** — more secure, but needs CSRF protection.
- **Memory** — most secure but lost on refresh.

For most applications, httpOnly cookies with CSRF protection is the best balance."

---

**Q55. Authentication vs Authorization?**

"**Authentication** answers: 'Who are you?'
**Authorization** answers: 'What are you allowed to do?'

Authentication is the process of verifying identity — login.
Authorization is the process of checking permissions — access control.

Example:
- Login is authentication.
- Admin permission to delete users is authorization."

**Follow-up: How do you implement authorization in DRF?**

"Using **permission classes**:

```python
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

class AdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
```

You can also create custom permissions:
```python
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
```"

---

# PART 2: DJANGO ADVANCED (Q56–Q75)

---

**Q56. How do you handle API errors in DRF?**

"I use proper exception handling and return meaningful HTTP status codes:

- **400 Bad Request** — validation errors
- **401 Unauthorized** — not authenticated
- **403 Forbidden** — authenticated but no permission
- **404 Not Found** — resource doesn't exist
- **405 Method Not Allowed** — wrong HTTP method
- **429 Too Many Requests** — rate limited
- **500 Internal Server Error** — unexpected error

I also maintain logs for debugging production issues."

**Follow-up: How do you create custom exception handlers?**

```python
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['error'] = True

    return response

# settings.py
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'myapp.exceptions.custom_exception_handler',
}
```"

---

**Q57. How do you secure Django APIs?**

"I follow security practices like:

1. **Authentication and authorization** — JWT with proper permissions.
2. **Input validation** — serializers validate all input.
3. **CSRF protection** — for session-based auth.
4. **Secure password hashing** — Django's default PBKDF2.
5. **Environment variables** — never hardcode secrets.
6. **HTTPS** — always in production.
7. **Rate limiting** — prevent abuse.
8. **CORS** — configure properly, don't allow all origins.
9. **SQL injection prevention** — ORM handles this.
10. **Security headers** — X-Frame-Options, X-Content-Type-Options, etc."

**Follow-up: What is rate limiting?**

"Rate limiting restricts how many requests a client can make in a given time period. DRF provides throttling:

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}
```"

**Follow-up: What is CORS?**

"CORS stands for Cross-Origin Resource Sharing. It's a browser security feature that restricts requests from different origins. In Django, I use `django-cors-headers`:

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://app.example.com",
]
```"

---

**Q58. How do you optimize slow Django APIs?**

"This is a very common interview question. My approach:

**Step 1: Identify the bottleneck**
- Use Django Debug Toolbar or django-silk
- Check query count per request
- Check response time
- Look at logs

**Step 2: Optimize database**
- Use `select_related` and `prefetch_related`
- Add indexes on frequently queried columns
- Use `only()` and `defer()` to limit fields
- Use `values()` or `values_list()` when you don't need model instances
- Use `bulk_create` and `bulk_update` for batch operations

**Step 3: Add caching**
- Use Redis for caching frequent queries
- Use `cache_page` decorator for views
- Cache expensive computations

**Step 4: Move heavy tasks to background**
- Use Celery for long-running tasks
- Return response immediately, process in background

**Step 5: Add pagination**
- Never return all records
- Use limit-offset or cursor pagination

**Step 6: Use database indexes**
- Add indexes on fields used in filters, ordering, joins

**Step 7: Consider read replicas**
- For read-heavy workloads, use read replicas"

**Follow-up: What is the difference between only() and defer()?**

"`only()` — fetch only the specified fields.
`defer()` — fetch all fields except the specified ones.

Both reduce data transfer and memory usage."

```python
# Only fetch name and email
User.objects.only('name', 'email')

# Fetch all except bio
User.objects.defer('bio')
```

---

**Q59. How do you implement background tasks in Django?**

"For long-running tasks, I use Celery. In my content moderation project, instead of making the API wait for NLP processing, we moved heavy processing to background workers.

**Flow:**
1. API receives request.
2. API creates a Celery task.
3. API returns immediately with task ID.
4. Celery worker picks up the task.
5. Worker processes the task (e.g., calls Hugging Face model).
6. Worker updates the database with result.

**Configuration:**
```python
# celery.py
from celery import Celery

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```

```python
# tasks.py
from celery import shared_task

@shared_task
def process_content(content_id):
    content = Content.objects.get(id=content_id)
    result = run_nlp_model(content.text)
    content.moderation_result = result
    content.save()
```

**Follow-up: How do you monitor Celery tasks?**

"I use:
- **Flower** — web-based monitoring tool for Celery.
- **Logging** — log task start, success, failure.
- **Sentry** — for error tracking.
- **Database** — store task status in DB for tracking."

---

**Q60. Explain Django deployment architecture.**

"A typical Django production setup:

```
Client
  ↓
Nginx (reverse proxy, SSL, static files)
  ↓
Gunicorn (WSGI application server)
  ↓
Django Application
  ↓
Database (MySQL/PostgreSQL)
  ↓
Redis/Celery (background tasks)
  ↓
AWS EC2 (hosting)
```

**Follow-up: Why Nginx?**

"Nginx works as a reverse proxy:
1. Handles SSL termination
2. Serves static files directly (faster than Django)
3. Load balancing across multiple Gunicorn workers
4. Rate limiting
5. Caching
6. Compression

Django is not designed to serve static files efficiently in production."

**Follow-up: Why Gunicorn?**

"Gunicorn is a WSGI server. It:
1. Manages multiple worker processes
2. Handles concurrent requests
3. Gracefully restarts workers
4. Works well with Django

Django's built-in server is for development only — not for production."

**Follow-up: How many workers?**

"Rule of thumb: `(2 × CPU cores) + 1`. For a 4-core machine, 9 workers. But this depends on the workload — I/O-bound tasks can have more workers, CPU-bound tasks fewer."

---

**Q61. What is middleware in Django?**

"Middleware is a layer between request and response where we can perform common operations. Each middleware is a class with hooks:

- `process_request` — called before view
- `process_view` — called before view but after URL resolution
- `process_response` — called after view
- `process_exception` — called if view raises exception

Django has built-in middleware for security, sessions, CSRF, authentication, and messages."

**Follow-up: How do you create custom middleware?**

```python
class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view
        print(f"Request: {request.method} {request.path}")

        response = self.get_response(request)

        # After view
        print(f"Response: {response.status_code}")

        return response
```

Add to `MIDDLEWARE` in settings."

---

**Q62. What is Django signals?**

"Signals allow decoupled applications to get notified when certain actions occur. Django provides signals like:

- `pre_save`, `post_save` — before/after model save
- `pre_delete`, `post_delete` — before/after model delete
- `m2m_changed` — when ManyToMany changes
- `request_started`, `request_finished` — request lifecycle

I use signals for:
- Sending welcome email after user registration
- Creating user profile after user creation
- Logging changes
- Cache invalidation"

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

**Follow-up: What are the downsides of signals?**

"1. **Hidden logic** — signals are not obvious in code flow.
2. **Debugging difficulty** — hard to trace.
3. **Performance** — can slow down save operations.
4. **Circular imports** — common issue.

I use signals sparingly — only when the action is truly decoupled."

---

**Q63. What is Django admin?**

"Django admin is an automatically generated interface for managing models. It's one of Django's killer features — you get a full CRUD interface for free.

```python
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'email']
```

**Follow-up: Is Django admin safe for production?**

"Django admin is safe if configured properly:
1. Restrict access to admin users only.
2. Use HTTPS.
3. Enable two-factor authentication.
4. Change admin URL from `/admin/` to something custom.
5. Limit permissions.

But for customer-facing applications, I build custom admin dashboards."

---

**Q64. What is Django ORM aggregation?**

"Aggregation performs calculations on a set of values. Django provides:

- `Count()` — count objects
- `Sum()` — sum values
- `Avg()` — average
- `Max()`, `Min()` — maximum, minimum

```python
from django.db.models import Count, Sum, Avg

# Count orders per customer
Customer.objects.annotate(order_count=Count('orders'))

# Total revenue
Order.objects.aggregate(total=Sum('amount'))

# Average order value
Order.objects.aggregate(avg=Avg('amount'))
```

**Follow-up: What is annotation?**

"Annotation adds a calculated field to each object in the queryset. Aggregation returns a single value for the entire queryset.

```python
# Annotation — adds field to each customer
customers = Customer.objects.annotate(order_count=Count('orders'))
for c in customers:
    print(c.name, c.order_count)

# Aggregation — single value
total = Order.objects.aggregate(total=Sum('amount'))
```"

---

**Q65. What is Django caching?**

"Caching stores frequently accessed data in faster storage to reduce database load and improve response time.

**Cache backends:**
- **Redis** — most common in production
- **Memcached** — alternative
- **Database** — for small applications
- **File-based** — for development
- **Local memory** — for single-server setups

**Caching strategies:**
1. **Per-view caching** — `@cache_page(60 * 15)`
2. **Template fragment caching** — cache parts of templates
3. **Low-level caching** — manual cache get/set
4. **Database query caching** — cache expensive queries"

```python
from django.core.cache import cache

def get_popular_products():
    products = cache.get('popular_products')
    if products is None:
        products = Product.objects.filter(popular=True)
        cache.set('popular_products', products, 60 * 15)
    return products
```

**Follow-up: What is cache invalidation?**

"Cache invalidation is removing stale data from cache when the underlying data changes. It's one of the hardest problems in computer science.

Strategies:
1. **Time-based** — cache expires after a fixed time.
2. **Signal-based** — invalidate cache on model save/delete.
3. **Manual** — explicitly clear cache when data changes."

---

**Q66. What is Django pagination?**

"Pagination splits large datasets into smaller pages. DRF provides three pagination classes:

1. **PageNumberPagination** — `?page=2`
2. **LimitOffsetPagination** — `?limit=10&offset=20`
3. **CursorPagination** — `?cursor=abc123`

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
```

**Follow-up: Which one do you use?**

"Depends on the use case:
- **PageNumberPagination** — simple, good for most APIs.
- **LimitOffsetPagination** — flexible, good for custom UIs.
- **CursorPagination** — best for large datasets and real-time data, because it doesn't suffer from the 'page drift' problem."

---

**Q67. What is Django REST Framework's ViewSet?**

"ViewSet is a class-based view that combines multiple related views into a single class. It provides methods like:

- `list()` — GET /users/
- `create()` — POST /users/
- `retrieve()` — GET /users/{id}/
- `update()` — PUT /users/{id}/
- `partial_update()` — PATCH /users/{id}/
- `destroy()` — DELETE /users/{id}/

```python
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
```

**Follow-up: What is the difference between ModelViewSet and ViewSet?**

"`ModelViewSet` provides all CRUD operations automatically. `ViewSet` requires you to define each action manually.

```python
# ModelViewSet — all CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet — custom actions
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        ...
    def create(self, request):
        ...
```"

---

**Q68. What is Django REST Framework's permission system?**

"DRF provides permission classes to control access:

- `AllowAny` — anyone can access
- `IsAuthenticated` — only authenticated users
- `IsAdminUser` — only admin users
- `IsAuthenticatedOrReadOnly` — read for all, write for authenticated

```python
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
```

**Follow-up: How do you create custom permissions?**

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```"

---

**Q69. What is Django REST Framework's throttling?**

"Throttling limits the rate of requests a client can make. DRF provides:

- `AnonRateThrottle` — for anonymous users
- `UserRateThrottle` — for authenticated users
- `ScopedRateThrottle` — per-view throttling

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}
```

**Follow-up: How do you implement custom throttling?**

```python
from rest_framework.throttling import UserRateThrottle

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'

# settings.py
'DEFAULT_THROTTLE_RATES': {
    'burst': '60/min',
}
```"

---

**Q70. What is Django REST Framework's versioning?**

"API versioning allows you to make breaking changes without breaking existing clients. DRF supports:

1. **URLPathVersioning** — `/api/v1/users/`
2. **QueryParameterVersioning** — `/api/users/?version=1`
3. **HeaderVersioning** — `Accept: application/json; version=1`
4. **NamespaceVersioning** — `/v1/users/`

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
}
```

**Follow-up: Which one do you prefer?**

"I prefer URL path versioning because it's explicit, easy to understand, and easy to test. Clients know exactly which version they're using."

---

**Q71. What is Django REST Framework's filtering?**

"DRF provides filtering through `django-filter`:

```python
# settings.py
INSTALLED_APPS = [
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

# views.py
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['is_active', 'role']
    search_fields = ['name', 'email']
    ordering_fields = ['created_at', 'name']
```

**Follow-up: How do you implement custom filtering?**

```python
import django_filters

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = User
        fields = ['name', 'min_age', 'max_age']
```"

---

**Q72. What is Django REST Framework's serialization of nested relationships?**

"DRF provides several ways to serialize nested relationships:

1. **PrimaryKeyRelatedField** — returns primary key
2. **StringRelatedField** — returns `__str__`
3. **Nested Serializer** — returns full nested object
4. **HyperlinkedRelatedField** — returns URL
5. **SlugRelatedField** — returns slug"

```python
class OrderSerializer(serializers.ModelSerializer):
    # Primary key
    customer = serializers.PrimaryKeyRelatedField(read_only=True)

    # Nested serializer
    items = OrderItemSerializer(many=True, read_only=True)

    # String representation
    status_display = serializers.StringRelatedField(source='status')

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'status_display']
```

**Follow-up: What is the performance impact?**

"Nested serializers can cause N+1 problems. For example, if you have 100 orders and each has 10 items, you'd get 100 + 1 queries. Solution: use `prefetch_related('items')` in the queryset."

---

**Q73. What is Django REST Framework's file upload?**

"DRF supports file uploads through `FileField` and `ImageField`:

```python
class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()

    class Meta:
        model = Document
        fields = ['id', 'file', 'uploaded_at']

    def create(self, validated_data):
        file = validated_data['file']
        # Save to S3 or local storage
        document = Document.objects.create(
            file=file,
            uploaded_by=self.context['request'].user
        )
        return document
```

**Follow-up: How do you handle large file uploads?**

"1. **Chunked upload** — split file into chunks and upload separately.
2. **Direct to S3** — generate presigned URL, upload directly from client.
3. **Background processing** — process file asynchronously with Celery.

For large files, direct-to-S3 is the best approach because it bypasses your server."

---

**Q74. What is Django REST Framework's testing?**

"DRF provides `APITestCase` and `APIClient` for testing:

```python
from rest_framework.test import APITestCase
from rest_framework import status

class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_create_user(self):
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_authenticated_access(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

**Follow-up: What do you test?**

"I test:
1. **Status codes** — correct HTTP status for each scenario.
2. **Validation** — invalid data returns 400.
3. **Authentication** — unauthenticated returns 401.
4. **Authorization** — no permission returns 403.
5. **Edge cases** — empty data, boundary values.
6. **Happy path** — normal flow works."

---

**Q75. What is Django REST Framework's schema generation?**

"DRF can generate OpenAPI schemas automatically, which can be used for API documentation:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema',
}
```

Tools:
- **drf-spectacular** — modern OpenAPI 3.0
- **drf-yasg** — Swagger/OpenAPI 2.0

These generate Swagger UI, ReDoc, or OpenAPI JSON."

**Follow-up: Why is API documentation important?**

"1. **For frontend developers** — they know exactly what to expect.
2. **For testing** — can test APIs directly from Swagger UI.
3. **For clients** — easy integration.
4. **For maintenance** — schema is the source of truth."

---

# PART 3: QUICK REVISION CHECKLIST (Module 3)

---

## Django Fundamentals

- [ ] Why Django — batteries included
- [ ] Django vs Flask vs FastAPI
- [ ] Request lifecycle — 11 steps
- [ ] Middleware — hooks and use cases
- [ ] ORM — advantages and disadvantages
- [ ] Raw SQL — when to use
- [ ] Model — fields, relationships
- [ ] Migrations — makemigrations vs migrate
- [ ] Data migrations
- [ ] select_related vs prefetch_related
- [ ] N+1 query problem
- [ ] Django vs DRF
- [ ] Serializer — serialization and deserialization
- [ ] Serializer vs ModelSerializer
- [ ] APIView vs ViewSet
- [ ] Router — URL mapping
- [ ] Authentication — Session, Token, JWT
- [ ] JWT flow — access + refresh tokens
- [ ] Authentication vs Authorization
- [ ] Permission classes
- [ ] Throttling
- [ ] Versioning
- [ ] Filtering
- [ ] Nested serialization
- [ ] File upload
- [ ] Testing
- [ ] Schema generation

## Django Advanced

- [ ] Custom exception handlers
- [ ] API security — 10 practices
- [ ] Rate limiting
- [ ] CORS
- [ ] API optimization — 7 steps
- [ ] only() vs defer()
- [ ] Celery — background tasks
- [ ] Deployment — Nginx + Gunicorn
- [ ] Middleware — custom middleware
- [ ] Signals — pre_save, post_save
- [ ] Django admin
- [ ] Aggregation — Count, Sum, Avg
- [ ] Annotation vs Aggregation
- [ ] Caching — Redis, strategies
- [ ] Cache invalidation
- [ ] Pagination — 3 types
- [ ] ViewSet — ModelViewSet vs ViewSet
- [ ] Permissions — custom permissions
- [ ] Throttling — custom throttling
- [ ] Versioning — URL path, query param, header

---

# PART 4: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Draw the request lifecycle** — whiteboard par explain karo. Ye question almost guaranteed hai.

2. **Explain trade-offs** — every design decision has pros and cons. Django vs Flask, ORM vs raw SQL, select_related vs prefetch_related.

3. **Connect to your projects** — "In my content moderation project, I used Celery for background tasks because..."

4. **Mention performance** — N+1 problem, query optimization, caching. Product companies care about scale.

5. **Talk about security** — authentication, authorization, rate limiting, HTTPS.

6. **Be specific** — "I used JWT with access and refresh tokens, stored in httpOnly cookies" is better than "I used JWT."

7. **Think out loud** — Interviewers want to see your thought process, not just the answer.

8. **Practice with code** — Write small examples to demonstrate concepts.

---

**Practice Tip:** Django request lifecycle aur JWT flow ko diagram ke saath yaad karo. Interviewer ise whiteboard par explain karne ko bol sakta hai. Product companies mein Django ke deep questions aate hain — especially ORM optimization, Celery, and deployment.

---

[← Previous: Module 2](module-2-python-core.md) | [Back to Index](README.md) | [Next: Module 4 →](module-4-mysql-sql.md)
