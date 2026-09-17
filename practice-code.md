# Practice Code — Extra Problems (Interview Mein Common)

[← Back to Index](README.md) | [← Previous: DSA](dsa-questions.md)

> **Note:** Ye module Google, Microsoft, Amazon jaise product-based companies ke liye prepare kiya gaya hai. Yahan sirf code nahi — **approach** bhi explain kiya hai. Har problem mein pehle approach batao, phir code likho. Interview mein code likhna aana chahiye, sirf yaad karna nahi.

---

# PART 1: BASIC PROBLEMS (Q1–Q10)

---

**Q1. Fibonacci Series**

"The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34... Each number is the sum of the previous two.

I'd use a generator because it's memory-efficient. We don't need to store all values — just yield them one by one."

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Follow-up: Can you write it recursively?**

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print([fibonacci_recursive(i) for i in range(10)])
```

But this is O(2^n) — very slow for large n. Memoization can improve it.

**Follow-up: What is the time complexity?**

- Generator approach: O(n) time, O(1) space.
- Recursive approach: O(2^n) time, O(n) space.
- Memoized approach: O(n) time, O(n) space.

---

**Q2. Factorial**

"Factorial of n is n * (n-1) * (n-2) * ... * 1. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.

I'd use recursion because it's the natural way to express factorial."

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

**Follow-up: Iterative approach?**

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Follow-up: What if n is very large?**

"Python handles big integers automatically. But for very large n, recursion may hit the recursion limit. Iterative is safer.

Also, for very large factorials, the result becomes huge. In production, we might use logarithms or modular arithmetic."

**Follow-up: What is the time complexity?**

- Recursive: O(n) time, O(n) space (recursion stack).
- Iterative: O(n) time, O(1) space.

---

**Q3. Prime Check**

"A prime number is a number greater than 1 that has no divisors other than 1 and itself.

I'd check divisibility up to the square root of n. If n has a divisor greater than √n, it must have a corresponding divisor less than √n."

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

**Follow-up: Why only up to √n?**

"If n = a * b, then either a ≤ √n or b ≤ √n. So if there's a divisor, one of them is ≤ √n. Checking up to √n is sufficient."

**Follow-up: How do you find all primes up to n?**

"Sieve of Eratosthenes:

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

print(sieve_of_eratosthenes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```"

**Follow-up: Time complexity?**

- Prime check: O(√n) time, O(1) space.
- Sieve: O(n log log n) time, O(n) space.

---

**Q4. Sort Dictionary by Value**

"Python dictionaries are unordered by default. To sort by value, I'd use `sorted()` with a key function."

```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)
# Output: {'b': 1, 'c': 2, 'a': 3}
```

**Follow-up: Sort descending?**

```python
sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print(sorted_d)
# Output: {'a': 3, 'c': 2, 'b': 1}
```

**Follow-up: Sort by key?**

```python
sorted_d = dict(sorted(d.items()))
print(sorted_d)
# Output: {'a': 3, 'b': 1, 'c': 2}
```

**Follow-up: What if values are equal?**

"Python's sort is stable. If values are equal, original order is preserved."

**Follow-up: Time complexity?**

O(n log n) time, O(n) space.

---

**Q5. Flatten Nested List**

"A nested list can have lists inside lists. Flattening means converting it to a single-level list.

I'd use recursion because the depth is unknown."

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

**Follow-up: Iterative approach?**

```python
def flatten_iterative(lst):
    stack = list(lst)
    result = []
    while stack:
        item = stack.pop(0)
        if isinstance(item, list):
            stack = item + stack
        else:
            result.append(item)
    return result
```

**Follow-up: What if the list contains tuples?**

"Same approach — check for any iterable. But be careful with strings, which are iterable too.

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
```"

**Follow-up: Time complexity?**

O(n) time where n is total number of elements, O(d) space where d is depth.

---

**Q6. Group Anagrams**

"Anagrams are words with the same letters in different order. For example, 'eat', 'tea', 'ate' are anagrams.

I'd use a hashmap. The key is the sorted word. Words with the same sorted key are anagrams."

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

**Follow-up: Alternative approach?**

"Use a character count tuple as key:

```python
def group_anagrams_count(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(Counter(word).items()))
        groups[key].append(word)
    return list(groups.values())
```

This is O(n * k) where k is max word length, better than O(n * k log k) for sorting."

**Follow-up: Time complexity?**

- Sorting approach: O(n * k log k) time, O(n * k) space.
- Counting approach: O(n * k) time, O(n * k) space.

---

**Q7. Two Sum**

"Given an array of integers and a target, find two numbers that add up to the target.

I'd use a hashmap. For each number, check if target minus that number has been seen before."

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

**Follow-up: What if the array is sorted?**

"Use two pointers:

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []
```"

**Follow-up: What if we need all pairs?**

```python
def two_sum_all(nums, target):
    seen = {}
    pairs = []
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            for j in seen[diff]:
                pairs.append([j, i])
        seen.setdefault(num, []).append(i)
    return pairs
```

**Follow-up: Time complexity?**

- Hashmap: O(n) time, O(n) space.
- Two pointers (sorted): O(n) time, O(1) space.

---

**Q8. Valid Parentheses**

"Check if a string of brackets is balanced. For example, '()[]{}' is valid, '(]' is not.

I'd use a stack. Push opening brackets, pop for closing brackets and check if they match."

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

**Follow-up: What if there are other characters?**

"Ignore non-bracket characters:

```python
def is_valid_ignore(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        elif char in mapping.values():
            stack.append(char)
        # ignore other characters
    return not stack
```"

**Follow-up: Time complexity?**

O(n) time, O(n) space.

---

**Q9. Move Zeroes to End**

"Move all zeroes in an array to the end while maintaining the relative order of non-zero elements.

I'd use two pointers. One for the position to place non-zero elements, one for scanning."

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

**Follow-up: What if we want to move zeroes to the front?**

```python
def move_zeroes_front(nums):
    i = len(nums) - 1
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
```

**Follow-up: Time complexity?**

O(n) time, O(1) space.

---

**Q10. Find Missing Number**

"Given an array of n distinct numbers from 0 to n, find the missing number.

I'd use the sum formula. Sum of 0 to n is n*(n+1)/2. Subtract the actual sum."

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([3, 0, 1]))
# Output: 2
```

**Follow-up: XOR approach?**

```python
def missing_number_xor(nums):
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

**Follow-up: What if there are multiple missing numbers?**

"Use a set:

```python
def missing_numbers(nums, n):
    num_set = set(nums)
    return [i for i in range(n + 1) if i not in num_set]
```"

**Follow-up: Time complexity?**

- Sum formula: O(n) time, O(1) space.
- XOR: O(n) time, O(1) space.

---

# PART 2: BONUS PROBLEMS (Q11–Q20)

---

**Q11. Check if Number is Palindrome**

"A palindrome number reads the same forwards and backwards. For example, 121 is a palindrome, 123 is not."

```python
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
```

**Follow-up: Without converting to string?**

```python
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

**Follow-up: Time complexity?**

- String approach: O(n) time, O(n) space.
- Math approach: O(log n) time, O(1) space.

---

**Q12. Count Vowels in String**

"Count the number of vowels (a, e, i, o, u) in a string."

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))  # 3
```

**Follow-up: Case-insensitive?**

```python
def count_vowels_ci(s):
    vowels = set("aeiou")
    return sum(1 for char in s.lower() if char in vowels)
```

**Follow-up: What about y?**

"Some consider 'y' a vowel. It depends on the context. Usually, 'y' is a consonant unless it's the only vowel sound in a syllable.

```python
def count_vowels_with_y(s):
    vowels = set("aeiouy")
    return sum(1 for char in s.lower() if char in vowels)
```"

**Follow-up: Time complexity?**

O(n) time, O(1) space.

---

**Q13. Remove Duplicates from List (Preserve Order)**

"Remove duplicates from a list while preserving the original order."

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

**Follow-up: Using dict.fromkeys?**

```python
def remove_duplicates_dict(lst):
    return list(dict.fromkeys(lst))
```

This works in Python 3.7+ because dicts preserve insertion order.

**Follow-up: Time complexity?**

O(n) time, O(n) space.

---

**Q14. Find Intersection of Two Lists**

"Find common elements between two lists."

```python
def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# Output: [3, 4]
```

**Follow-up: Preserve order?**

```python
def intersection_ordered(a, b):
    set_b = set(b)
    return [x for x in a if x in set_b]
```

**Follow-up: What if there are duplicates?**

```python
from collections import Counter

def intersection_with_duplicates(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    result = []
    for item in count_a:
        if item in count_b:
            result.extend([item] * min(count_a[item], count_b[item]))
    return result
```

**Follow-up: Time complexity?**

- Set intersection: O(n + m) time, O(n + m) space.
- Ordered: O(n + m) time, O(m) space.

---

**Q15. Check if Two Strings are Rotations**

"Check if one string is a rotation of another. For example, 'abcde' and 'cdeab' are rotations."

```python
def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(are_rotations("abcde", "cdeab"))  # True
print(are_rotations("abcde", "abced"))  # False
```

**Follow-up: Why does this work?**

"If s2 is a rotation of s1, then s2 must be a substring of s1 + s1. For example, 'cdeab' is a substring of 'abcdeabcde'."

**Follow-up: Time complexity?**

O(n) time for substring search, O(n) space for concatenation.

---

**Q16. Find First Duplicate**

"Find the first duplicate element in a list."

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

**Follow-up: What if we need the index?**

```python
def first_duplicate_index(nums):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            return i, num
        seen[num] = i
    return None, None
```

**Follow-up: Time complexity?**

O(n) time, O(n) space.

---

**Q17. Sum of Digits**

"Sum all digits of a number."

```python
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(1234))  # 10
```

**Follow-up: Without converting to string?**

```python
def sum_of_digits_math(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```

**Follow-up: What if n is negative?**

```python
def sum_of_digits_safe(n):
    return sum(int(d) for d in str(abs(n)))
```

**Follow-up: Time complexity?**

- String approach: O(log n) time, O(log n) space.
- Math approach: O(log n) time, O(1) space.

---

**Q18. Reverse Words in Sentence**

"Reverse the order of words in a sentence."

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("I love Python"))
# Output: "Python love I"
```

**Follow-up: Reverse each word?**

```python
def reverse_each_word(s):
    return ' '.join(word[::-1] for word in s.split())

print(reverse_each_word("I love Python"))
# Output: "I evol nohtyP"
```

**Follow-up: Handle multiple spaces?**

```python
def reverse_words_clean(s):
    return ' '.join(s.split())
```

**Follow-up: Time complexity?**

O(n) time, O(n) space.

---

**Q19. Find Longest Word in Sentence**

"Find the longest word in a sentence."

```python
def longest_word(s):
    words = s.split()
    return max(words, key=len)

print(longest_word("I love programming in Python"))
# Output: "programming"
```

**Follow-up: What if there are ties?**

```python
def longest_words(s):
    words = s.split()
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]

print(longest_words("I love programming and coding"))
# Output: ["programming", "coding"]
```

**Follow-up: Time complexity?**

O(n) time, O(n) space.

---

**Q20. Check Armstrong Number**

"An Armstrong number is a number that equals the sum of its digits each raised to the power of the number of digits. For example, 153 = 1^3 + 5^3 + 3^3 = 153."

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

print(is_armstrong(153))  # True (1^3 + 5^3 + 3^3 = 153)
print(is_armstrong(123))  # False
```

**Follow-up: Without converting to string?**

```python
def is_armstrong_math(n):
    original = n
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    power = len(digits)
    return original == sum(d**power for d in digits)
```

**Follow-up: What about 4-digit Armstrong numbers?**

"1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. Yes, it's an Armstrong number.

The function works for any number of digits."

**Follow-up: Time complexity?**

O(log n) time, O(log n) space.

---

# PART 3: COMMON PATTERNS (INTERVIEW MEIN KAAM AATE HAIN)

---

| Pattern | Problems | Approach |
|---------|----------|----------|
| **Two Pointers** | Move zeroes, Remove duplicates, Palindrome | Left + Right pointers |
| **Sliding Window** | Max subarray, Longest substring | Window expand/shrink |
| **Hashmap** | Two sum, First duplicate, Anagram | Key-value lookup |
| **Stack** | Valid parentheses, Next greater element | LIFO |
| **Recursion** | Factorial, Flatten list, Fibonacci | Function calls itself |
| **Set** | Intersection, Remove duplicates | O(1) lookup |
| **Sorting** | Anagram, Group anagrams | Sort then compare |

---

# PART 4: TIME COMPLEXITY CHEAT SHEET

---

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hashmap lookup, Array access |
| O(log n) | Logarithmic | Binary search, Balanced BST |
| O(n) | Linear | Loop through list, Sum |
| O(n log n) | Linearithmic | Sorting, Merge sort |
| O(n²) | Quadratic | Nested loops, Bubble sort |
| O(2^n) | Exponential | Recursive subsets, Fibonacci (naive) |
| O(n!) | Factorial | Permutations |

---

# PART 5: SPACE COMPLEXITY CHEAT SHEET

---

| Complexity | Example |
|------------|---------|
| O(1) | Two pointers, Kadane's algorithm |
| O(n) | Hashmap, Recursion stack |
| O(n²) | 2D DP table |
| O(n log n) | Merge sort |

---

# PART 6: QUICK REVISION CHECKLIST (Practice Code)

---

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

# PART 7: INTERVIEW TIPS (Google, Microsoft, Amazon)

---

1. **Write code on paper** — practice writing code without IDE.

2. **Explain your approach** — "First I would... Then I would..."

3. **Think about edge cases** — empty input, single element, duplicates.

4. **Optimize** — start with brute force, then improve.

5. **Test your code** — dry run with examples.

6. **Mention complexity** — time and space.

7. **Use meaningful names** — `result`, `seen`, `count` — not `x`, `y`, `z`.

8. **Practice daily** — 2-3 problems per day.

---

**Practice Tip:** Har problem ko **khud se likho** — copy-paste mat karo. Interview mein code likhna aana chahiye, sirf yaad karna nahi. Google/Microsoft/Amazon mein coding rounds mein live code likhna hota hai — practice se hi confidence aayega.

---

[← Previous: DSA](dsa-questions.md) | [Back to Index](README.md)
