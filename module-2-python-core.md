# Module 2: Python Core (Q21–Q40)

[← Back to Index](README.md) | [← Previous: Module 1](module-1-hr-resume-project.md)

---

**Q21. What are the main features of Python?**

"Python is a high-level, interpreted language known for simplicity and readability. It supports object-oriented, functional, and procedural programming. It has a huge ecosystem — Django, FastAPI, Pandas, NumPy, Hugging Face. In my work I use Python for backend development, automation, data processing, and NLP integration."

**Follow-up: Why Python for backend?**

"Because Python has strong frameworks like Django and FastAPI, good database support, easy API development, and a large ecosystem for automation and AI."

---

**Q22. Difference between list and tuple?**

"List is mutable — we can modify elements after creation. Tuple is immutable — once created, cannot be changed. I use lists when data needs modification, tuples when I want fixed data."

```python
list_data = [1, 2, 3]
list_data.append(4)  # allowed

tuple_data = (1, 2, 3)
# tuple_data[0] = 5  # error
```

**Follow-up: Why tuple is faster?**

"Because tuples are immutable, Python can optimize memory usage and access speed."

---

**Q23. What is mutable and immutable in Python?**

"Mutable objects can be changed after creation — list, dict, set. Immutable objects cannot — int, string, tuple."

```python
name = "Pavan"
name = name + " Dubey"  # new string object created
```

---

**Q24. Difference between shallow copy and deep copy?**

"Shallow copy creates a new object but keeps references of nested objects. Deep copy creates a completely independent copy including nested objects."

```python
import copy

new_list = copy.copy(old_list)      # shallow
deep_list = copy.deepcopy(old_list) # deep
```

**Follow-up: When deep copy?**

"When working with nested dictionaries or lists where I don't want changes in one object affecting another."

---

**Q25. What is *args and **kwargs?**

"*args allows multiple positional arguments. **kwargs allows multiple keyword arguments."

```python
def user_info(*args, **kwargs):
    print(args)
    print(kwargs)
```

"In Django decorators and reusable functions, *args and **kwargs are commonly used."

---

**Q26. What is a decorator?**

"A decorator is a function that modifies or extends the behavior of another function without changing its code."

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
```

"In Django, decorators are used for authentication checks like login_required."

---

**Q27. What is a generator?**

"A generator returns values one at a time using yield instead of returning everything at once. It saves memory when processing large data."

```python
def numbers():
    for i in range(100000):
        yield i
```

**Follow-up: Where did you use generators?**

"For processing large datasets where loading everything into memory is not efficient — like reading large Excel files or scraping data in chunks."

---

**Q28. Difference between iterator and iterable?**

"An iterable is an object that can return an iterator — like list, tuple. An iterator is an object that gives values one by one using next()."

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
next(iterator)
```

---

**Q29. Difference between is and ==?**

"== checks whether values are equal. is checks whether two variables refer to the same object in memory."

```python
a = [1, 2]
b = [1, 2]

a == b  # True
a is b  # False
```

---

**Q30. Explain Python memory management.**

"Python manages memory automatically using a private heap space. The interpreter handles allocation and deallocation through reference counting and garbage collection."

**Follow-up: What is garbage collection?**

"It removes objects that are no longer referenced to free memory."

---

**Q31. What is garbage collection?**

"Python uses reference counting. When an object's reference count becomes zero, memory is released. For cyclic references, Python uses a garbage collector to clean them."

---

**Q32. Explain exception handling.**

"Exception handling allows us to handle runtime errors without crashing the application. We use try, except, else, and finally blocks."

```python
try:
    result = 10 / 0
except Exception as e:
    print(e)
finally:
    print("Completed")
```

"In APIs, we handle exceptions properly and return meaningful error responses instead of exposing system errors."

---

**Q33. Difference between Exception and Error?**

"Errors are generally serious issues that applications may not recover from. Exceptions are runtime problems that we can handle using try-except."

---

**Q34. Explain OOP concepts in Python.**

"Python supports four main OOP concepts:
1. Encapsulation — combining data and methods.
2. Inheritance — reusing existing functionality.
3. Polymorphism — same interface with different behavior.
4. Abstraction — hiding internal implementation."

"In Django, models and reusable classes follow object-oriented principles."

---

**Q35. Difference between class and object?**

"A class is a blueprint, while an object is an instance of that class."

```python
class User:
    pass

user1 = User()
```

---

**Q36. Difference between @staticmethod and @classmethod?**

"staticmethod does not receive class or object reference. classmethod receives class reference using cls."

```python
class User:
    @classmethod
    def create(cls):
        pass

    @staticmethod
    def validate():
        pass
```

"classmethod is useful when we need to work with class-level data."

---

**Q37. What is MRO in Python?**

"MRO stands for Method Resolution Order. It defines the order in which Python searches for methods in inheritance hierarchy."

```
Class A
Class B(A)
Class C(B)

Python searches C → B → A.
```

---

**Q38. What is context manager?**

"Context managers manage resources automatically. The common example is opening and closing files using 'with'."

```python
with open("file.txt") as f:
    data = f.read()
```

"It automatically closes resources even if an exception occurs."

---

**Q39. Threading vs Multiprocessing?**

"Threading is useful for I/O-bound tasks like API calls, file operations, network requests. Multiprocessing is useful for CPU-intensive tasks because each process has its own Python interpreter and avoids GIL limitations."

"For data processing tasks, multiprocessing can improve performance."

---

**Q40. What is GIL?**

"GIL means Global Interpreter Lock. In CPython, it allows only one thread to execute Python bytecode at a time. Because of this, Python threads don't provide true parallel execution for CPU-heavy tasks. For CPU-bound operations, multiprocessing is preferred."

---

[← Previous: Module 1](module-1-hr-resume-project.md) | [Back to Index](README.md) | [Next: Module 3 →](module-3-django-drf.md)
