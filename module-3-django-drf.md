# Module 3: Django + DRF (Q41–Q60)

[← Back to Index](README.md) | [← Previous: Module 2](module-2-python-core.md)

---

**Q41. Why Django?**

"I prefer Django because it provides many things out of the box — ORM, authentication, security features, admin panel, middleware support, and a structured project architecture. In my projects, Django helped me build REST APIs quickly while maintaining clean code structure. For API development, I generally use Django REST Framework because it provides serializers, authentication, permissions, and reusable components."

**Follow-up: Why not Flask?**

"Flask is lightweight and flexible, but many things like authentication, ORM, and admin need additional setup. Django provides a complete framework, which is useful for enterprise applications."

---

**Q42. Explain Django request lifecycle.**

"When a request comes to Django:
1. The request first reaches the web server like Nginx.
2. It is passed to Django through WSGI or ASGI.
3. Django middleware processes the request.
4. URL resolver matches the URL pattern.
5. The request goes to the corresponding view.
6. The view interacts with models through ORM.
7. Database returns the data.
8. The response goes back through middleware and returns to the client."

**Follow-up: What is middleware?**

"Middleware is a layer between request and response where we can perform common operations like authentication, logging, security checks, and request modification."

---

**Q43. What is ORM in Django?**

"ORM stands for Object Relational Mapping. It allows us to interact with the database using Python objects instead of writing SQL queries manually. Django ORM converts Python queries into SQL internally."

```python
User.objects.filter(active=True)
```

**Follow-up: Can you write raw SQL in Django?**

"Yes. Django provides raw queries when we need complex database operations that are difficult with ORM."

---

**Q44. Explain Django Model.**

"A Django model represents a database table. Each model class maps to a database table, and model attributes represent table columns. Django automatically creates SQL tables through migrations."

```python
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

---

**Q45. What are migrations in Django?**

"Migrations are Django's way of tracking database schema changes. Whenever we create or modify models, Django generates migration files, and then we apply them to update the database."

```bash
python manage.py makemigrations
python manage.py migrate
```

---

**Q46. Difference between select_related() and prefetch_related()?**

"Both are used to optimize database queries. select_related() uses SQL JOIN and fetches related objects in a single query. It is mainly used for ForeignKey and OneToOne relationships. prefetch_related() executes separate queries and combines the results in Python. It is useful for ManyToMany and reverse relationships."

```python
Order.objects.select_related('customer')
```

---

**Q47. What is N+1 query problem?**

"N+1 query problem happens when we execute one query to fetch a list of objects and then execute additional queries for each object to get related data. This increases database load. We solve it using select_related() and prefetch_related()."

---

**Q48. Difference between Django and Django REST Framework?**

"Django is a complete web framework used for building web applications. Django REST Framework is an extension of Django used specifically for creating REST APIs. DRF provides serializers, API views, authentication, permissions, and pagination."

---

**Q49. What is Serializer in DRF?**

"Serializer converts complex data like Django model instances into JSON format so it can be sent through APIs. It also validates incoming JSON data before saving it into the database."

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
```

---

**Q50. Difference between Serializer and ModelSerializer?**

"Serializer requires manually defining fields and validation logic. ModelSerializer automatically generates fields based on the Django model. For standard CRUD APIs, I usually prefer ModelSerializer because it reduces code."

---

**Q51. Difference between APIView and ViewSet?**

"APIView gives more control because we define each HTTP method separately — get(), post(), put(). ViewSet provides a higher-level abstraction where common CRUD operations are already structured — list(), create(), update(), destroy()."

---

**Q52. What is Router in DRF?**

"Router automatically generates URL patterns for ViewSets. Instead of manually creating URLs for every CRUD operation, router handles URL mapping."

```python
router.register('users', UserViewSet)
```

---

**Q53. How do you implement authentication in Django REST API?**

"Common approaches are:
1. Session Authentication
2. Token Authentication
3. JWT Authentication

For API-based applications, JWT is commonly used because it is stateless and works well with mobile and frontend applications."

---

**Q54. Explain JWT authentication flow.**

"User sends username and password. Server validates credentials. If valid, server generates JWT token. Client stores the token. For future requests, client sends token in Authorization header. Backend validates the token before allowing access."

```
Authorization: Bearer <token>
```

---

**Q55. Authentication vs Authorization?**

"Authentication answers 'Who are you?' Authorization answers 'What are you allowed to do?' For example: Login is authentication. Admin permission to delete users is authorization."

---

**Q56. How do you handle API errors in DRF?**

"I use proper exception handling and return meaningful HTTP status codes:
400 — Bad Request
401 — Unauthorized
403 — Forbidden
404 — Not Found
500 — Internal Server Error

I also maintain logs for debugging production issues."

---

**Q57. How do you secure Django APIs?**

"I follow security practices like:
- Authentication and authorization
- Permission classes
- Input validation
- CSRF protection where required
- Secure password hashing
- Environment variables for secrets
- HTTPS
- Rate limiting"

---

**Q58. How do you optimize slow Django APIs?**

"First I identify the bottleneck. I check:
- Database queries
- API response time
- Logs

Then optimize using:
- Database indexing
- select_related/prefetch_related
- Pagination
- Caching using Redis
- Moving heavy tasks to Celery
- Reducing unnecessary database calls"

---

**Q59. How do you implement background tasks in Django?**

"For long-running tasks, I use Celery. For example, in my content moderation project, instead of making the API wait for NLP processing, we moved heavy processing to background workers. The worker processed the task asynchronously and updated the result."

---

**Q60. Explain Django deployment architecture.**

"A typical Django production setup looks like:

Client
↓
Nginx
↓
Gunicorn
↓
Django Application
↓
Database (MySQL/PostgreSQL)
↓
Redis/Celery for background tasks
↓
AWS EC2 server"

**Follow-up: Why Nginx?**

"Nginx works as a reverse proxy, handles static files, SSL termination, and forwards dynamic requests to Django application servers."

---

## Quick Revision Checklist (Module 3)

- [ ] Django vs Flask — why Django
- [ ] Django request lifecycle — 8 steps
- [ ] Middleware — kya karta hai
- [ ] ORM — kya hai, raw SQL kab
- [ ] Model — table mapping
- [ ] Migrations — makemigrations vs migrate
- [ ] select_related vs prefetch_related
- [ ] N+1 query problem
- [ ] Django vs DRF
- [ ] Serializer vs ModelSerializer
- [ ] APIView vs ViewSet
- [ ] Router — URL mapping
- [ ] Authentication — Session, Token, JWT
- [ ] JWT flow — token generation + validation
- [ ] Authentication vs Authorization
- [ ] API error handling — HTTP status codes
- [ ] API security — best practices
- [ ] API optimization — queries, caching, pagination
- [ ] Celery — background tasks
- [ ] Deployment — Nginx + Gunicorn + Django

---

**Practice Tip:** Django request lifecycle aur JWT flow ko diagram ke saath yaad karo. Interviewer ise whiteboard par explain karne ko bol sakta hai.

---

[← Previous: Module 2](module-2-python-core.md) | [Back to Index](README.md) | [Next: Module 4 →](module-4-mysql-sql.md)
