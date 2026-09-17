# Practice Code — Extra Problems (Interview Mein Common)

[← Back to Index](README.md) | [← Previous: DSA](dsa-questions.md)

---

**1. Fibonacci Series**

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---

**2. Factorial**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

**3. Prime Check**

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False
```

---

**4. Sort Dictionary by Value**

```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)
# Output: {'b': 1, 'c': 2, 'a': 3}
```

---

**5. Flatten Nested List**

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], 5]))
# Output: [1, 2, 3, 4, 5]
```

---

**6. Group Anagrams**

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

---

**7. Two Sum**

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
# Output: [0, 1]
```

---

**8. Valid Parentheses**

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
```

---

**9. Move Zeroes to End**

```python
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
# Output: [1, 3, 12, 0, 0]
```

---

**10. Find Missing Number**

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([3, 0, 1]))
# Output: 2
```

---

## Bonus Practice Problems

**11. Check if Number is Palindrome**

```python
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
```

---

**12. Count Vowels in String**

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))  # 3
```

---

**13. Remove Duplicates from List (Preserve Order)**

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
# Output: [1, 2, 3, 4]
```

---

**14. Find Intersection of Two Lists**

```python
def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# Output: [3, 4]
```

---

**15. Check if Two Strings are Rotations**

```python
def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(are_rotations("abcde", "cdeab"))  # True
```

---

**16. Find First Duplicate**

```python
def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

print(first_duplicate([2, 1, 3, 5, 3, 2]))  # 3
```

---

**17. Sum of Digits**

```python
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(1234))  # 10
```

---

**18. Reverse Words in Sentence**

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("I love Python"))
# Output: "Python love I"
```

---

**19. Find Longest Word in Sentence**

```python
def longest_word(s):
    words = s.split()
    return max(words, key=len)

print(longest_word("I love programming in Python"))
# Output: "programming"
```

---

**20. Check Armstrong Number**

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

print(is_armstrong(153))  # True (1^3 + 5^3 + 3^3 = 153)
```

---

## Quick Revision Checklist (Practice Code)

- [ ] Fibonacci — generator
- [ ] Factorial — recursion
- [ ] Prime check — O(√n)
- [ ] Sort dictionary by value
- [ ] Flatten nested list — recursion
- [ ] Group anagrams — sorted key
- [ ] Two sum — hashmap
- [ ] Valid parentheses — stack
- [ ] Move zeroes — two pointers
- [ ] Missing number — sum formula
- [ ] Palindrome number
- [ ] Count vowels
- [ ] Remove duplicates — preserve order
- [ ] Intersection of lists — set
- [ ] String rotations
- [ ] First duplicate
- [ ] Sum of digits
- [ ] Reverse words
- [ ] Longest word
- [ ] Armstrong number

---

## Common Patterns (Interview Mein Kaam Aate Hain)

| Pattern | Problems |
|---------|----------|
| **Two Pointers** | Move zeroes, Remove duplicates, Palindrome |
| **Sliding Window** | Max subarray, Longest substring |
| **Hashmap** | Two sum, First duplicate, Anagram |
| **Stack** | Valid parentheses, Next greater element |
| **Recursion** | Factorial, Flatten list, Fibonacci |
| **Set** | Intersection, Remove duplicates |
| **Sorting** | Anagram, Group anagrams |

---

## Time Complexity Cheat Sheet

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hashmap lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through list |
| O(n log n) | Linearithmic | Sorting |
| O(n²) | Quadratic | Nested loops |
| O(2^n) | Exponential | Recursive subsets |

---

**Practice Tip:** Har problem ko **khud se likho** — copy-paste mat karo. Interview mein code likhna aana chahiye, sirf yaad karna nahi.

---

[← Previous: DSA](dsa-questions.md) | [Back to Index](README.md)
