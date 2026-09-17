# DSA Questions (Q131–Q140)

[← Back to Index](README.md) | [← Previous: Module 6](module-6-system-design-coding.md)

---

**Q131. What is time complexity of binary search?**

"O(log n) — because we divide the search space in half each time."

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

**Q132. How do you find the first non-repeating character in a string?**

```python
from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None
```

---

**Q133. How do you check if two strings are anagrams?**

```python
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
```

---

**Q134. How do you merge two sorted lists?**

```python
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result
```

---

**Q135. How do you reverse a linked list?**

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```

---

**Q136. How do you detect a cycle in a linked list?**

"Using Floyd's cycle detection algorithm — slow and fast pointers."

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

---

**Q137. How do you find the maximum subarray sum?**

"Kadane's algorithm — O(n)."

```python
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum
```

---

**Q138. How do you remove duplicates from a sorted array?**

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
```

---

**Q139. How do you implement a stack using queues?**

```python
from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
```

---

**Q140. How do you find the longest common prefix?**

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

---

## Bonus DSA Questions (Interview Mein Common)

**Q141. How do you find two numbers that sum to a target?**

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []
```

---

**Q142. How do you check valid parentheses?**

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
```

---

**Q143. How do you move zeroes to end?**

```python
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
```

---

**Q144. How do you find the missing number in 1 to n?**

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```

---

**Q145. How do you find the majority element?**

```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate
```

---

## Quick Revision Checklist (DSA)

- [ ] Binary Search — O(log n)
- [ ] First Non-Repeating Character
- [ ] Anagram Check
- [ ] Merge Two Sorted Lists
- [ ] Reverse Linked List
- [ ] Detect Cycle in Linked List — Floyd's algorithm
- [ ] Kadane's Algorithm — max subarray
- [ ] Remove Duplicates from Sorted Array
- [ ] Stack using Queues
- [ ] Longest Common Prefix
- [ ] Two Sum — hashmap approach
- [ ] Valid Parentheses — stack
- [ ] Move Zeroes
- [ ] Missing Number — sum formula
- [ ] Majority Element — Boyer-Moore voting

---

## Time & Space Complexity Cheat Sheet

| Problem | Time | Space |
|---------|------|-------|
| Binary Search | O(log n) | O(1) |
| First Non-Repeating | O(n) | O(n) |
| Anagram Check | O(n log n) | O(n) |
| Merge Sorted Lists | O(n+m) | O(n+m) |
| Reverse Linked List | O(n) | O(1) |
| Detect Cycle | O(n) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |
| Remove Duplicates | O(n) | O(1) |
| Stack using Queues | O(n) push | O(n) |
| Longest Common Prefix | O(n*m) | O(1) |
| Two Sum | O(n) | O(n) |
| Valid Parentheses | O(n) | O(n) |
| Move Zeroes | O(n) | O(1) |
| Missing Number | O(n) | O(1) |
| Majority Element | O(n) | O(1) |

---

**Practice Tip:** DSA questions mein interviewer **approach** dekhta hai, sirf answer nahi. Pehle bolo "I would use a hashmap here because..." — phir code likho.

---

[← Previous: Module 6](module-6-system-design-coding.md) | [Back to Index](README.md) | [Next: Practice Code →](practice-code.md)
