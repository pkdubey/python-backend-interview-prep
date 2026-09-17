# Module 2: Python Core + OOPs — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 1](module-1-hr-resume-project.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. Har answer ko natural language mein rakha hai, jaise ek 5.5 years experienced Python developer interview mein bolta hai.

---

# PART 1: PYTHON BASICS (Q21–Q40)

---

**Q21. What are the main features of Python?**

"Python is a high-level, interpreted language known for its simplicity and readability. It supports multiple programming paradigms — object-oriented, functional, and procedural.

What makes Python special for backend development is its ecosystem. Django and FastAPI for APIs, Pandas and NumPy for data processing, Hugging Face for NLP, and libraries like Celery for background tasks.

In my work, I use Python mainly for backend development, automation scripts, data processing, and NLP integration."

**Follow-up: Why Python for backend?**

"Because Python has strong frameworks like Django and FastAPI, good database support, easy API development, and a large ecosystem for automation and AI. Also, the developer community is huge, so finding solutions is easy."

**Follow-up: What are the limitations of Python?**

"The main limitation is performance — Python is slower than compiled languages like C++ or Java. Also, the GIL prevents true multi-threading for CPU-heavy tasks. But for backend development and AI, these limitations rarely matter because the bottlenecks are usually I/O or database, not CPU."

---

**Q22. Difference between list and tuple?**

"List is mutable — we can modify elements after creation. Tuple is immutable — once created, it cannot be changed.

I use lists when data needs modification — like collecting API responses, building results. I use tuples when I want fixed data — like database records, coordinates, or dictionary keys."

```python
list_data = [1, 2, 3]
list_data.append(4)  # allowed

tuple_data = (1, 2, 3)
# tuple_data[0] = 5  # error
```

**Follow-up: Why tuple is faster?**

"Because tuples are immutable, Python can optimize memory usage and access speed. Also, tuples are hashable — so they can be used as dictionary keys. Lists are not hashable."

**Follow-up: When would you prefer tuple over list?**

"When I need immutability. For example, if I'm returning multiple values from a function, or using data as a dictionary key. Also, if the data is not going to change, tuple is more memory-efficient."

---

**Q23. What is mutable and immutable in Python?**

"Mutable objects can be changed after creation — list, dict, set. Immutable objects cannot be changed — int, string, tuple, frozenset.

This matters because when you pass a mutable object to a function, changes inside the function affect the original. For immutable objects, a new object is created."

```python
name = "Pavan"
name = name + " Dubey"  # new string object created

lst = [1, 2, 3]
lst.append(4)  # same object modified
```

**Follow-up: Why does this matter in interviews?**

"Because it affects how functions behave. If I pass a list to a function and modify it, the caller sees the change. If I pass a string, the caller doesn't see any change. This is a common source of bugs."

---

**Q24. Difference between shallow copy and deep copy?**

"Shallow copy creates a new object but keeps references of nested objects. Deep copy creates a completely independent copy including nested objects.

In simple terms — shallow copy shares inner objects, deep copy doesn't."

```python
import copy

new_list = copy.copy(old_list)      # shallow
deep_list = copy.deepcopy(old_list) # deep
```

**Follow-up: When deep copy?**

"When working with nested dictionaries or lists where I don't want changes in one object affecting another. For example, if I'm working with a config dictionary that has nested settings, and I want to modify one copy without affecting the original."

**Follow-up: What is the performance impact?**

"Deep copy is slower and uses more memory because it recursively copies everything. Shallow copy is faster. So I use shallow copy when I don't need full independence."

---

**Q25. What is *args and **kwargs?**

"*args allows a function to accept multiple positional arguments. **kwargs allows multiple keyword arguments.

These are useful when you don't know in advance how many arguments will be passed."

```python
def user_info(*args, **kwargs):
    print(args)    # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments
```

"In Django decorators and reusable functions, *args and **kwargs are commonly used because we don't always know the number of parameters."

**Follow-up: Can you use both together?**

"Yes. The order matters — *args comes before **kwargs. Also, you can have regular parameters before *args."

```python
def func(a, b, *args, **kwargs):
    pass
```

---

**Q26. What is a decorator?**

"A decorator is a function that modifies or extends the behavior of another function without changing its code. It's a higher-order function — it takes a function and returns a new function.

In simple terms — decorator wraps a function to add extra behavior."

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@logger
def say_hello():
    print("Hello")

say_hello()
```

**Follow-up: Where did you use decorators in real projects?**

"In Django, decorators are used for authentication checks like `@login_required`. Also for caching — `@cache_page`. And in DRF, for permission checks. I've also written custom decorators for logging and timing API calls."

**Follow-up: What is functools.wraps?**

"It preserves the original function's metadata — name, docstring, etc. Without it, the wrapped function's name becomes 'wrapper'."

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

---

**Q27. What is a generator?**

"A generator is a function that returns values one at a time using yield instead of returning everything at once. It saves memory because values are produced on demand.

In simple terms — generator is lazy evaluation. It doesn't compute all values upfront."

```python
def numbers():
    for i in range(100000):
        yield i
```

**Follow-up: Where did you use generators?**

"For processing large datasets where loading everything into memory is not efficient — like reading large Excel files or scraping data in chunks. In my automation work, I use generators to process data row by row instead of loading the entire file."

**Follow-up: Difference between generator and normal function?**

"A normal function returns all values at once. A generator returns a generator object, and values are produced one by one when you iterate. The state is preserved between yields."

---

**Q28. Difference between iterator and iterable?**

"An iterable is an object that can return an iterator — like list, tuple, string, dict. It has an `__iter__()` method.

An iterator is an object that gives values one by one using `next()`. It has both `__iter__()` and `__next__()` methods.

In simple terms — every iterator is an iterable, but not every iterable is an iterator."

```python
numbers = [1, 2, 3]  # iterable
iterator = iter(numbers)  # iterator
next(iterator)  # 1
next(iterator)  # 2
```

**Follow-up: Why does this matter?**

"Because for loops work with iterables. When you write `for x in something`, Python calls `iter()` to get an iterator, then calls `next()` until StopIteration. Understanding this helps when writing custom classes."

---

**Q29. Difference between is and ==?**

"== checks whether values are equal. is checks whether two variables refer to the same object in memory.

In simple terms — == compares content, is compares identity."

```python
a = [1, 2]
b = [1, 2]

a == b  # True (same content)
a is b  # False (different objects)

c = a
a is c  # True (same object)
```

**Follow-up: When should we use is?**

"For comparing with None. Always use `if x is None` instead of `if x == None`. Also for checking if two variables point to the same object."

**Follow-up: What about small integers and strings?**

"Python caches small integers (-5 to 256) and some strings. So `a = 100; b = 100; a is b` might return True. But this is implementation-specific and shouldn't be relied upon."

---

**Q30. Explain Python memory management.**

"Python manages memory automatically using a private heap space. The interpreter handles allocation and deallocation through two mechanisms:

1. Reference counting — every object has a count of how many references point to it. When count becomes zero, memory is freed.

2. Garbage collection — for cyclic references (where two objects reference each other), Python uses a garbage collector."

**Follow-up: What is garbage collection?**

"It removes objects that are no longer referenced to free memory. Python's GC handles cyclic references that reference counting can't handle."

**Follow-up: Can you disable GC?**

"Yes, using the `gc` module. But it's rarely needed. In most cases, the default behavior is fine."

---

**Q31. What is garbage collection?**

"Python uses two mechanisms:

1. Reference counting — when an object's reference count becomes zero, memory is released immediately.

2. Cyclic garbage collector — for cyclic references, Python runs a periodic GC that detects cycles and cleans them."

```python
import gc
gc.isenabled()  # True by default
```

**Follow-up: What is a cyclic reference?**

"When two objects reference each other, their reference counts never become zero. For example:

```python
a = []
b = []
a.append(b)
b.append(a)
del a
del b
# Even after deleting, the objects are still referenced by each other
```

The cyclic GC handles this."

---

**Q32. Explain exception handling.**

"Exception handling allows us to handle runtime errors without crashing the application. We use try, except, else, and finally blocks."

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No error occurred")
finally:
    print("This always runs")
```

**Follow-up: Why use else and finally?**

"`else` runs only if no exception occurred. `finally` runs always — whether exception occurred or not. It's used for cleanup — like closing files or database connections."

**Follow-up: In APIs, how do you handle exceptions?**

"I use proper exception handling and return meaningful error responses instead of exposing system errors. For example, in DRF, I use custom exception handlers to return consistent error responses with proper HTTP status codes."

---

**Q33. Difference between Exception and Error?**

"Errors are generally serious issues that applications may not recover from — like MemoryError, RecursionError. They are usually not caught.

Exceptions are runtime problems that we can handle using try-except — like ValueError, KeyError, TypeError.

In simple terms — errors are unrecoverable, exceptions are recoverable."

**Follow-up: What are some common exceptions you've handled?**

"ValueError for invalid input, KeyError for missing dictionary keys, IntegrityError for database constraints, ConnectionError for network issues, TimeoutError for API calls. In Django, I've handled ValidationError and PermissionDenied."

---

**Q34. Explain OOP concepts in Python.**

"Python supports four main OOP concepts:

1. **Encapsulation** — combining data and methods into a single unit. In Python, we use classes for this.

2. **Inheritance** — reusing existing functionality. A child class inherits from a parent class.

3. **Polymorphism** — same interface with different behavior. Like method overriding.

4. **Abstraction** — hiding internal implementation. Using abstract classes and interfaces."

"In Django, models and reusable classes follow object-oriented principles. For example, Model classes inherit from `models.Model` and reuse a lot of functionality."

**Follow-up: What is the difference between encapsulation and abstraction?**

"Encapsulation is about bundling data and methods together, and controlling access using private/protected attributes. Abstraction is about hiding implementation details and showing only what's necessary. Encapsulation is implementation, abstraction is design."

---

**Q35. Difference between class and object?**

"A class is a blueprint, while an object is an instance of that class.

In simple terms — class is the design, object is the actual thing."

```python
class User:
    def __init__(self, name):
        self.name = name

user1 = User("Pavan")  # object
user2 = User("Dubey")  # another object
```

**Follow-up: How many objects can you create from a class?**

"Unlimited. Each object has its own copy of instance variables. Static variables are shared."

---

**Q36. Difference between @staticmethod and @classmethod?**

"staticmethod does not receive class or object reference. It's just a regular function inside a class.

classmethod receives class reference using cls. It can access and modify class-level data."

```python
class User:
    count = 0

    @classmethod
    def create(cls):
        cls.count += 1
        return cls()

    @staticmethod
    def validate():
        return True
```

**Follow-up: When to use which?**

"Use staticmethod when the method doesn't need to access class or instance data — like utility functions. Use classmethod when the method needs to work with class-level data — like factory methods or counters."

**Follow-up: Real example?**

"In Django models, `Model.objects.create()` is a classmethod. It works on the class, not on an instance. For static methods, think of validation utilities that don't depend on class state."

---

**Q37. What is MRO in Python?**

"MRO stands for Method Resolution Order. It defines the order in which Python searches for methods in an inheritance hierarchy.

In simple terms — when you call a method, Python looks for it in the class, then its parents, following MRO."

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
# [C, B, A, object]
```

**Follow-up: What is C3 algorithm?**

"Python uses the C3 linearization algorithm to compute MRO. It ensures that:
1. A class always appears before its parents.
2. The order of parents is preserved.
3. Consistent MRO is maintained across the hierarchy."

**Follow-up: Why does MRO matter?**

"It matters in multiple inheritance. When a method is called, Python follows MRO to find the method. If two parent classes have the same method, the one earlier in MRO is used."

---

**Q38. What is context manager?**

"Context managers manage resources automatically. The most common example is opening and closing files using 'with'.

They ensure that resources are properly released even if an exception occurs."

```python
with open("file.txt") as f:
    data = f.read()
# File is automatically closed here
```

**Follow-up: How do you create a custom context manager?**

"Two ways — using a class with `__enter__` and `__exit__` methods, or using the `contextlib` module with a generator."

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Enter")
    yield
    print("Exit")
```

**Follow-up: Real example from your work?**

"In my automation projects, I use context managers for database connections and file operations. In Django, `transaction.atomic()` is a context manager for database transactions."

---

**Q39. Threading vs Multiprocessing?**

"Threading is useful for I/O-bound tasks like API calls, file operations, network requests. Multiple threads share the same memory and GIL.

Multiprocessing is useful for CPU-intensive tasks because each process has its own Python interpreter and avoids GIL limitations."

**Follow-up: What is the GIL limitation?**

"GIL allows only one thread to execute Python bytecode at a time. So threads don't provide true parallelism for CPU-bound tasks. But for I/O-bound tasks, threads work well because the GIL is released during I/O operations."

**Follow-up: Which one did you use?**

"In my work, I mostly use Celery for background tasks — which uses processes. For I/O-bound tasks like scraping multiple websites, I've used threading. For CPU-heavy data processing, multiprocessing."

---

**Q40. What is GIL?**

"GIL means Global Interpreter Lock. In CPython, it allows only one thread to execute Python bytecode at a time.

Because of this, Python threads don't provide true parallel execution for CPU-heavy tasks. For CPU-bound operations, multiprocessing is preferred."

**Follow-up: Why does GIL exist?**

"It simplifies memory management and makes CPython thread-safe. Without GIL, Python would need complex locking mechanisms, which would slow down single-threaded performance."

**Follow-up: How do you work around GIL?**

"For CPU-bound tasks, use multiprocessing. For I/O-bound tasks, use threading or async. For external services, use Celery with multiple workers. In production, I've used Celery workers on multiple machines to scale."

---

# PART 2: OOPs IN DEPTH (Q41–Q70)

---

**Q41. What is a class?**

"A class is a blueprint or template for creating objects. It defines properties (attributes) and behaviors (methods) that objects of that class will have.

In Python, everything is an object. Even integers, strings, and functions are objects. Classes are the way we create custom objects."

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")
```

**Follow-up: What is the difference between class and instance?**

"A class is the definition. An instance is a specific object created from that class. For example, `Student` is a class, and `s1 = Student("Pavan", 90)` is an instance."

---

**Q42. What is an object?**

"An object is a physical existence of a class. It's an instance of a class with its own state (instance variables) and behavior (methods).

We can create any number of objects from a class. Each object has its own copy of instance variables."

```python
s1 = Student("Pavan", 90)
s2 = Student("Dubey", 85)
```

**Follow-up: What is a reference variable?**

"A reference variable is a variable that points to an object. For example, `s1` is a reference variable pointing to the Student object."

---

**Q43. Explain the self variable.**

"self is the default variable which always points to the current object. It's like `this` in Java.

By using self, we can access instance variables and instance methods of the object."

```python
class Student:
    def __init__(self, name):
        self.name = name  # self refers to current object

    def display(self):
        print(self.name)  # accessing instance variable
```

**Follow-up: Is self a keyword?**

"No, self is just a convention. You can name it anything, but self is the standard. Python passes the object as the first argument automatically."

**Follow-up: Why is self needed?**

"Because Python doesn't have implicit this. You need to explicitly pass the object reference so methods can access instance data."

---

**Q44. What is a constructor?**

"A constructor is a special method in Python. Its name is `__init__`. It's executed automatically at the time of object creation.

The main purpose is to declare and initialize instance variables. Per object, the constructor is executed only once."

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```

**Follow-up: What is the difference between constructor and method?**

"Constructor is called automatically at object creation. Method needs to be called explicitly. Constructor is used for initialization, methods for business logic. Per object, constructor runs once, methods can run many times."

**Follow-up: Can constructor return a value?**

"No, `__init__` cannot return a value. If it does, Python raises a TypeError. Its job is only initialization."

---

**Q45. Types of variables in Python class?**

"There are three types:

1. **Instance Variables** — object-level. Different for each object. Declared using self.

2. **Static Variables** — class-level. Shared by all objects. Declared inside class but outside methods.

3. **Local Variables** — method-level. Temporary. Created when method runs and destroyed when method ends."

```python
class Test:
    x = 10  # static variable

    def __init__(self):
        self.y = 20  # instance variable

    def m1(self):
        z = 30  # local variable
        print(z)
```

**Follow-up: When to use static variables?**

"When the value is not different for each object. For example, a company name, a counter for total objects, or configuration values."

---

**Q46. What are instance variables?**

"Instance variables are object-level variables. They are different for each object. They are declared inside the constructor or instance methods using self.

For every object, a separate copy of instance variables is created."

```python
class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
```

**Follow-up: Where can you declare instance variables?**

"Three places:
1. Inside constructor using self
2. Inside instance method using self
3. Outside the class using object reference"

---

**Q47. What are static variables?**

"Static variables are class-level variables. They are shared by all objects of the class. They are declared inside the class but outside any method.

For the entire class, only one copy is created."

```python
class Test:
    count = 0  # static variable

    def __init__(self):
        Test.count += 1
```

**Follow-up: How to access static variables?**

"By class name — `Test.count` — or by object reference — `t1.count`. But recommended to use class name. Inside classmethod, use cls."

**Follow-up: What happens if you modify static variable using self?**

"If you use `self.count = 888`, it creates a new instance variable with that name for that object. The static variable is not modified."

---

**Q48. What are local variables?**

"Local variables are method-level variables. They are created when the method is executed and destroyed when the method completes. They cannot be accessed from outside the method."

```python
class Test:
    def m1(self):
        a = 1000  # local variable
        print(a)
```

**Follow-up: Can two methods share local variables?**

"No. Each method has its own local scope. A local variable of one method is not accessible in another method."

---

**Q49. Types of methods in Python class?**

"There are three types:

1. **Instance Methods** — use self. Can access instance and static variables.

2. **Class Methods** — use cls. Can access only static variables. Declared with @classmethod.

3. **Static Methods** — no self or cls. General utility methods. Declared with @staticmethod."

```python
class Test:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass
```

**Follow-up: Which one is most commonly used?**

"Instance methods are the most common. Class methods are used for factory patterns and counters. Static methods are used for utility functions."

---

**Q50. What are setter and getter methods?**

"Setter methods are used to set values of instance variables. Getter methods are used to get values.

They are also called mutator and accessor methods."

```python
class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
```

**Follow-up: Why use setters and getters instead of direct access?**

"Encapsulation — you can add validation. For example, setName can validate that name is not empty. Also, you can change implementation without affecting callers."

**Follow-up: Does Python have property decorator?**

"Yes. `@property` allows you to access methods like attributes. It's a more Pythonic way of implementing getters and setters."

```python
class Student:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
```

---

**Q51. What is inheritance?**

"Inheritance is the concept of reusing existing functionality. A child class inherits from a parent class and gets access to all its members — variables, methods, constructors.

The main advantage is code reusability. We can extend existing functionality with new features."

```python
class Person:
    def walk(self):
        print("Walking")

class Employee(Person):
    def work(self):
        print("Working")

e = Employee()
e.walk()  # inherited from Person
e.work()  # own method
```

**Follow-up: Why use inheritance?**

"To avoid code duplication. If multiple classes share common functionality, we can put it in a parent class and inherit. Also, it supports polymorphism — we can treat child objects as parent objects."

---

**Q52. Types of inheritance in Python?**

"Five types:

1. **Single** — one parent, one child.
2. **Multi-Level** — grandparent, parent, child.
3. **Hierarchical** — one parent, multiple children.
4. **Multiple** — multiple parents, one child.
5. **Hybrid** — combination of above."

**Follow-up: Does Python support multiple inheritance?**

"Yes, Python supports multiple inheritance. But it can lead to the diamond problem, which is resolved using MRO (Method Resolution Order)."

---

**Q53. What is MRO?**

"MRO stands for Method Resolution Order. It defines the order in which Python searches for methods in an inheritance hierarchy.

In simple terms — when you call a method, Python looks for it in the class, then its parents, following MRO."

```python
class A:
    def m1(self):
        print("A")

class B(A):
    def m1(self):
        print("B")

class C(B):
    def m1(self):
        print("C")

c = C()
c.m1()  # C
print(C.mro())  # [C, B, A, object]
```

**Follow-up: What is C3 algorithm?**

"Python uses the C3 linearization algorithm to compute MRO. It follows DLR (Depth First Left to Right) — child gets more priority than parent, left parent gets more priority than right parent."

---

**Q54. What is super() method?**

"super() is a built-in method used to call the super class constructors, variables, and methods from the child class.

It's commonly used to call the parent class constructor from the child class constructor."

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal
```

**Follow-up: Can you access instance variables of parent using super()?**

"No. From child class, we cannot access parent class instance variables using super(). We use self. But we can access parent class static variables using super()."

**Follow-up: How to call a specific super class method?**

"Two ways:
1. `super(D, self).m1()` — calls m1 of super class of D.
2. `A.m1(self)` — directly calls A's m1 method."

---

**Q55. What is method overriding?**

"When a child class redefines a method of the parent class with the same name and signature, it's called method overriding.

The child class method overrides the parent class method."

```python
class P:
    def marry(self):
        print("Appalamma")

class C(P):
    def marry(self):
        print("Katrina Kaif")

c = C()
c.marry()  # Katrina Kaif
```

**Follow-up: Can you call parent method from overridden method?**

"Yes, using super()."

```python
class C(P):
    def marry(self):
        super().marry()
        print("Katrina Kaif")
```

---

**Q56. What is method overloading?**

"Method overloading means defining multiple methods with the same name but different parameters.

But Python doesn't support method overloading directly. If you define multiple methods with the same name, Python considers only the last one."

```python
class Test:
    def m1(self):
        print("no-arg")

    def m1(self, a):
        print("one-arg")

    def m1(self, a, b):
        print("two-arg")

t = Test()
t.m1(10, 20)  # two-arg (only last method is available)
```

**Follow-up: How do you handle overloading requirements in Python?**

"Using default arguments or variable number of arguments (*args, **kwargs)."

```python
class Test:
    def sum(self, a=None, b=None, c=None):
        if a and b and c:
            return a + b + c
        elif a and b:
            return a + b
        else:
            return "Provide 2 or 3 arguments"
```

---

**Q57. What is operator overloading?**

"Operator overloading means using the same operator for different purposes. Python supports operator overloading through magic methods.

For example, + operator is implemented by `__add__` method."

```python
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print(b1 + b2)  # 300
```

**Follow-up: What are some common magic methods?**

"`__add__` for +, `__sub__` for -, `__mul__` for *, `__eq__` for ==, `__lt__` for <, `__str__` for str(), `__repr__` for repr()."

---

**Q58. What is constructor overriding?**

"When a child class defines its own constructor, it overrides the parent class constructor. The child constructor is called when creating a child object.

If the child class doesn't have a constructor, the parent constructor is used."

```python
class P:
    def __init__(self):
        print("Parent Constructor")

class C(P):
    def __init__(self):
        print("Child Constructor")

c = C()  # Child Constructor
```

**Follow-up: How to call parent constructor from child constructor?**

"Using super().__init__()"

```python
class C(P):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
```

---

**Q59. What is the difference between IS-A and HAS-A relationship?**

"IS-A is inheritance. A child class IS-A type of parent class. For example, Employee IS-A Person.

HAS-A is composition. A class HAS-A reference to another class. For example, Employee HAS-A Car.

IS-A is used when we want to extend functionality. HAS-A is used when we want to use functionality."

```python
# IS-A
class Person:
    pass

class Employee(Person):
    pass

# HAS-A
class Car:
    pass

class Employee:
    def __init__(self, car):
        self.car = car
```

**Follow-up: Which one is better?**

"Both have their uses. IS-A is for strong relationships where the child is a specialized version of the parent. HAS-A is for weak relationships where one object uses another. In general, prefer HAS-A over IS-A because it's more flexible."

---

**Q60. What is composition?**

"Composition is a HAS-A relationship. One class contains a reference to another class.

The main advantage is code reusability. The container class can use all members of the contained class."

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

c = Car()
c.start()
```

**Follow-up: What is aggregation?**

"Aggregation is a weak HAS-A relationship. The contained object can exist independently. For example, a Department has Professors, but Professors can exist without the Department."

**Follow-up: Composition vs Aggregation?**

"In Composition, the contained object cannot exist without the container. In Aggregation, it can. The relationship between an object and its instance variables is Composition. The relationship between an object and static variables is Aggregation."

---

**Q61. What is polymorphism?**

"Polymorphism means 'many forms'. The same method or operator can behave differently in different contexts.

In Python, polymorphism is achieved through:
1. Duck typing
2. Method overloading (partially)
3. Method overriding"

**Follow-up: What is duck typing?**

"In Python, we don't check the type of an object. If it walks like a duck and talks like a duck, it's a duck. We just call the method and if the object has it, it works."

```python
class Duck:
    def talk(self):
        print("Quack")

class Dog:
    def talk(self):
        print("Bow")

def make_talk(obj):
    obj.talk()

make_talk(Duck())  # Quack
make_talk(Dog())   # Bow
```

**Follow-up: What is the problem with duck typing?**

"If the object doesn't have the method, we get AttributeError at runtime. We can handle this using hasattr()."

---

**Q62. What is an abstract method?**

"An abstract method is a method that has only declaration but no implementation. It's declared using @abstractmethod decorator from the abc module.

Child classes are responsible for providing the implementation."

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def noofwheels(self):
        pass

class Bus(Vehicle):
    def noofwheels(self):
        return 7
```

**Follow-up: Can you instantiate an abstract class?**

"No, if a class contains at least one abstract method and extends ABC, you cannot instantiate it."

---

**Q63. What is an abstract class?**

"An abstract class is a partially implemented class. It can have both abstract and non-abstract methods. It's declared by extending ABC class.

It's used when we know the requirement but not the complete implementation."

```python
from abc import ABC, abstractmethod

class CollegeAutomation(ABC):
    @abstractmethod
    def m1(self):
        pass

    def m2(self):
        print("Non-abstract method")
```

**Follow-up: Difference between abstract class and interface?**

"In an interface, all methods are abstract. In an abstract class, some methods can be non-abstract. Python doesn't have a separate interface keyword — we use abstract classes with only abstract methods as interfaces."

---

**Q64. What is an interface in Python?**

"An interface is an abstract class with only abstract methods. It defines a contract that child classes must fulfill.

In Python, we create interfaces using ABC and @abstractmethod."

```python
from abc import ABC, abstractmethod

class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
```

**Follow-up: Why use interfaces?**

"To define a contract. Any class that implements the interface must provide all methods. This ensures consistency and allows polymorphism."

---

**Q65. What is encapsulation?**

"Encapsulation is bundling data and methods into a single unit — a class. It also involves controlling access to the data using access modifiers.

In Python, we use naming conventions:
- Public: `name`
- Protected: `_name`
- Private: `__name`"

```python
class Test:
    def __init__(self):
        self.public = 10
        self._protected = 20
        self.__private = 30
```

**Follow-up: How do you access private variables?**

"Directly, we can't. But indirectly using name mangling: `object._ClassName__variable`."

```python
t = Test()
print(t._Test__private)  # 30
```

---

**Q66. What is __str__() method?**

"`__str__` is a magic method that returns a string representation of an object. When you print an object, Python calls `__str__`.

By default, it returns something like `<__main__.Student object at 0x...>`. We override it to return meaningful information."

```python
class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def __str__(self):
        return f"Student: {self.name}, Rollno: {self.rollno}"

s = Student("Pavan", 101)
print(s)  # Student: Pavan, Rollno: 101
```

**Follow-up: Difference between __str__ and __repr__?**

"`__str__` is for readability — user-friendly output. `__repr__` is for unambiguous representation — mostly used for debugging. `str()` calls `__str__`, `repr()` calls `__repr__`. It's recommended to use `repr()` for debugging."

---

**Q67. What is garbage collection in OOPs?**

"Garbage collection is Python's automatic memory management. It destroys objects that are no longer referenced.

Python uses reference counting and a cyclic garbage collector."

```python
import gc
print(gc.isenabled())  # True
```

**Follow-up: What is a destructor?**

"A destructor is a special method `__del__` that is called just before an object is destroyed. It's used for cleanup activities like closing database connections."

```python
class Test:
    def __del__(self):
        print("Cleanup")
```

**Follow-up: Is destructor guaranteed to run?**

"No. It's not guaranteed. The garbage collector may not call it in some cases. For reliable cleanup, use context managers or try/finally blocks."

---

**Q68. What is the difference between class method and instance method?**

"Instance method uses self and can access instance variables. Class method uses cls and can access only static variables.

Instance method is called on an object. Class method can be called on the class itself."

```python
class Test:
    count = 0

    def instance_method(self):
        print(self.count)

    @classmethod
    def class_method(cls):
        print(cls.count)

Test.class_method()  # works
# Test.instance_method()  # error
```

**Follow-up: When to use classmethod?**

"For factory methods — methods that create objects. For example, `Model.objects.create()` in Django. Also for tracking counters."

---

**Q69. What is the diamond problem?**

"In multiple inheritance, if two parent classes inherit from a common grandparent, and a child class inherits from both parents, we get a diamond shape. This creates ambiguity about which grandparent method to use.

Python resolves this using MRO (Method Resolution Order)."

```python
class A:
    def m1(self):
        print("A")

class B(A):
    def m1(self):
        print("B")

class C(A):
    def m1(self):
        print("C")

class D(B, C):
    pass

d = D()
d.m1()  # B (MRO: D, B, C, A)
```

**Follow-up: How does MRO resolve it?**

"Python uses the C3 linearization algorithm. In the diamond problem, it ensures that:
1. Child comes before parents.
2. Left parent comes before right parent.
3. Common grandparent comes last."

---

**Q70. What is the difference between shallow copy and deep copy in OOPs?**

"Shallow copy creates a new object but shares references to nested objects. Deep copy creates a completely independent copy.

In OOPs, this matters when you have objects with references to other objects."

```python
import copy

class Address:
    def __init__(self, city):
        self.city = city

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

p1 = Person("Pavan", Address("Noida"))
p2 = copy.copy(p1)       # shallow
p3 = copy.deepcopy(p1)   # deep

p2.address.city = "Delhi"
print(p1.address.city)   # Delhi (shared reference)
print(p3.address.city)   # Noida (independent copy)
```

---

# PART 3: QUICK REVISION CHECKLIST (Module 2)

---

## Python Basics

- [ ] Python features and limitations
- [ ] List vs Tuple — mutability, hashability
- [ ] Mutable vs Immutable objects
- [ ] Shallow copy vs Deep copy
- [ ] *args and **kwargs
- [ ] Decorators — syntax, use case, functools.wraps
- [ ] Generators — yield, memory efficiency
- [ ] Iterator vs Iterable
- [ ] is vs == — identity vs equality
- [ ] Memory management — reference counting, GC
- [ ] Garbage collection — cyclic references
- [ ] Exception handling — try/except/else/finally
- [ ] Exception vs Error
- [ ] OOP concepts — 4 pillars
- [ ] Class vs Object
- [ ] @staticmethod vs @classmethod
- [ ] MRO — C3 algorithm
- [ ] Context managers — with statement
- [ ] Threading vs Multiprocessing
- [ ] GIL — Global Interpreter Lock

## OOPs in Depth

- [ ] Class — blueprint, definition
- [ ] Object — instance, reference variable
- [ ] self variable — current object
- [ ] Constructor — __init__, purpose
- [ ] Types of variables — instance, static, local
- [ ] Instance variables — object-level
- [ ] Static variables — class-level
- [ ] Local variables — method-level
- [ ] Types of methods — instance, class, static
- [ ] Setter and Getter methods
- [ ] Inheritance — IS-A relationship
- [ ] Types of inheritance — 5 types
- [ ] MRO — method resolution order
- [ ] super() method — parent class access
- [ ] Method overriding — child redefines
- [ ] Method overloading — not supported directly
- [ ] Operator overloading — magic methods
- [ ] Constructor overriding
- [ ] IS-A vs HAS-A relationship
- [ ] Composition vs Aggregation
- [ ] Polymorphism — duck typing
- [ ] Abstract method — @abstractmethod
- [ ] Abstract class — ABC
- [ ] Interface — only abstract methods
- [ ] Encapsulation — public, protected, private
- [ ] __str__() method — string representation
- [ ] __repr__() vs __str__()
- [ ] Garbage collection in OOPs
- [ ] Destructor — __del__
- [ ] Diamond problem — MRO resolution

---

# PART 4: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Explain with real examples** — Don't just define. Show where you used it.

2. **Mention trade-offs** — Every design decision has pros and cons. Talk about them.

3. **Use the right terminology** — MRO, GIL, duck typing, composition — these show depth.

4. **Connect to your projects** — "In my Django project, I used classmethod for factory methods."

5. **Be honest** — If you don't know something, say "I haven't used this in production, but I understand the concept."

6. **Think out loud** — Interviewers want to see your thought process, not just the answer.

7. **Practice with code** — Write small examples to demonstrate concepts.

---

**Practice Tip:** Roz 2–3 OOP concepts revise karo. Har concept ka ek real example apne project se connect karo. Google/Microsoft/Amazon mein OOPs par deep questions aate hain — especially inheritance, MRO, and design patterns.

---

[← Previous: Module 1](module-1-hr-resume-project.md) | [Back to Index](README.md) | [Next: Module 3 →](module-3-django-drf.md)
