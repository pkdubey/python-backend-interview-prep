# DSA Questions — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 6](module-6-system-design-coding.md)

> **Note:** This section is specifically prepared for product-based companies like Google, Microsoft, and Amazon. Here you won't just find questions — I've also explained the **thinking process** behind each one. For every problem, first explain your approach, then write the code.

---

# PART 1: ARRAYS & STRINGS

---

**Q1. How do you find the maximum subarray sum? (Kadane's Algorithm)**

"First I'd think of the brute force — O(n²) or O(n³). But the optimal solution is O(n) using Kadane's algorithm.

The idea: maintain a running sum. If the running sum becomes negative, reset it — because a negative sum will never help us going forward. At each step, update the maximum."

```python
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum
```

**Follow-up: What if all numbers are negative?**

"Kadane's algorithm still works because we initialize with nums[0] and take max at each step. If all numbers are negative, it returns the least negative number — which is the maximum in that case."

**Follow-up: What if we need the actual subarray, not just the sum?**

"Then I'd track the start and end indices whenever max_sum is updated."

```python
def max_subarray_with_indices(nums):
    max_sum = current = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current + nums[i]:
            current = nums[i]
            temp_start = i
        else:
            current += nums[i]

        if current > max_sum:
            max_sum = current
            start = temp_start
            end = i

    return max_sum, nums[start:end+1]
```

---

**Q2. How do you find two numbers that sum to a target? (Two Sum)**

"Brute force would be O(n²) — check every pair. But the optimal solution is O(n) using a hashmap.

The idea: build a hashmap. For each number, check if target minus that number has already been seen. If yes, we've found our pair."

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

**Follow-up: What if the array is sorted?**

"Then I'd use two pointers — O(n) time, O(1) space."

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
```

**Follow-up: What if we need all pairs?**

"Same hashmap approach, but store results in a set to avoid duplicates."

---

**Q3. How do you find the maximum product subarray?**

"This one is tricky because negative numbers can flip the product to positive. So I maintain two variables — max_so_far and min_so_far. Because negative times negative becomes positive."

```python
def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)
    return result
```

---

**Q4. How do you find the missing number in 1 to n?**

"I'd use the sum formula — O(n) time, O(1) space. The sum of 1 to n is n*(n+1)/2. Subtract the actual sum from that."

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```

**Follow-up: What if the array has duplicates?**

"Then I'd use the XOR approach — the same number XORed twice cancels out, so the missing number is what remains."

```python
def missing_number_xor(nums):
    xor = 0
    for i in range(len(nums) + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor
```

**Follow-up: What if the numbers are not 1 to n?**

"Then I'd sort and check adjacent elements, or use a hashmap."

---

**Q5. How do you find the first non-repeating character in a string?**

"First I'd use Counter to get frequency. Then iterate through the string and find the first character with count 1."

```python
from collections import Counter

def first_non_repeating(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None
```

**Follow-up: What if we need O(1) space?**

"Then I'd use an array of size 26 — if only lowercase letters are involved."

```python
def first_non_repeating_optimized(s):
    count = [0] * 26
    for char in s:
        count[ord(char) - ord('a')] += 1
    for char in s:
        if count[ord(char) - ord('a')] == 1:
            return char
    return None
```

---

**Q6. How do you check if two strings are anagrams?**

"Sort both and compare — O(n log n). Or count frequencies — O(n)."

```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
```

**Follow-up: O(n) approach?**

"Then I'd use Counter."

```python
from collections import Counter

def is_anagram_optimized(s1, s2):
    return Counter(s1) == Counter(s2)
```

**Follow-up: What if strings have Unicode characters?**

"Counter works fine for any characters. Sorting also works."

---

**Q7. How do you group anagrams together?**

"I'd sort each word to create a key. Words with the same key go into the same group. Use a hashmap."

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
```

**Follow-up: Time complexity?**

"O(n * k log k) where n = number of words and k = max length of a word."

---

**Q8. How do you find the longest common prefix?**

"First treat the first word as the prefix. Compare it with the rest. Keep shrinking the prefix until it matches."

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

**Follow-up: Better approach?**

"Vertical scanning — check column by column. O(n*m) time, O(1) space."

---

**Q9. How do you rotate an array by k steps?**

"I'd use the reversal technique — O(n) time, O(1) space.

The idea:
1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining elements"

```python
def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
```

**Follow-up: Left rotation?**

"Same approach, but the order changes — reverse the first n-k, reverse the last k, then reverse all."

---

**Q10. How do you find the container with most water?**

"Two pointers — O(n) time. Left and right pointers to calculate the area. Move the shorter side."

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

---

# PART 2: LINKED LISTS

---

**Q11. How do you reverse a linked list?**

"Iterative approach — use 3 pointers: prev, current, next. At each step, point current.next to prev."

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

**Follow-up: Recursive approach?**

"Recursion works too — O(n) time, O(n) stack space."

```python
def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

---

**Q12. How do you detect a cycle in a linked list?**

"Floyd's cycle detection — slow and fast pointers. If there's a cycle, the fast pointer will eventually meet the slow pointer."

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

**Follow-up: How do you find the start of the cycle?**

"When slow and fast meet, move slow back to head. Then move both one step at a time. Where they meet again is the start of the cycle."

```python
def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

**Follow-up: How do you find the length of the cycle?**

"Once slow and fast meet, keep counting from that point until you come back to the same node."

---

**Q13. How do you find the middle of a linked list?**

"Slow and fast pointers — slow moves 1 step, fast moves 2 steps. When fast reaches the end, slow is at the middle."

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Follow-up: Which middle for even length?**

"This approach returns the second middle. If you want the first middle, stop fast one step earlier."

---

**Q14. How do you merge two sorted linked lists?**

"Two pointers — compare the heads of both lists, add the smaller one to the result."

```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

---

**Q15. How do you remove the nth node from the end of a linked list?**

"Two pointers — move fast n+1 steps ahead, then move both together. When fast reaches the end, slow is just before the nth node."

```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next
```

---

**Q16. How do you check if a linked list is a palindrome?**

"Find the middle, reverse the second half, then compare."

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

---

# PART 3: STACKS & QUEUES

---

**Q17. How do you check valid parentheses?**

"I'd use a stack. Push opening brackets, and for closing brackets, check if the top matches."

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

**Follow-up: What if we have multiple types of brackets?**

"Same approach — just add all types to the mapping."

---

**Q18. How do you implement a stack using queues?**

"In the push operation, I'd rotate the queue so the new element comes to the front."

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

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
```

---

**Q19. How do you implement a queue using stacks?**

"I'd use two stacks — input and output. Push into input, pop from output."

```python
class Queue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output
```

---

**Q20. How do you find the next greater element?**

"I'd use a stack — a monotonic decreasing stack. For each element, check if the stack top is smaller."

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)

    return result
```

**Follow-up: Circular array?**

"Double the array and use the same approach, but only up to n elements."

---

# PART 4: TREES & BINARY SEARCH TREES

---

**Q21. How do you traverse a binary tree? (Inorder, Preorder, Postorder)**

"Recursive is simple. Iterative is also possible using a stack."

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder: Left → Root → Right
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

# Preorder: Root → Left → Right
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

# Postorder: Left → Right → Root
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

**Follow-up: Iterative inorder?**

"Use a stack."

```python
def inorder_iterative(root):
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```

---

**Q22. How do you find the height of a binary tree?**

"Recursion — the max of the left and right subtree heights plus 1."

```python
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

---

**Q23. How do you check if a binary tree is balanced?**

"At each node, check that the difference between the left and right heights is not more than 1."

```python
def is_balanced(root):
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1
```

---

**Q24. How do you find the lowest common ancestor (LCA) in a BST?**

"I'd use the BST property — if both values are smaller than the root, go left. If both are larger, go right. Otherwise, the root is the LCA."

```python
def lca_bst(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None
```

**Follow-up: Binary tree (not BST)?**

"Then I'd use recursion — find the LCA from the left and right subtrees."

```python
def lca_binary_tree(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    if left and right:
        return root
    return left or right
```

---

**Q25. How do you validate a binary search tree?**

"Do an inorder traversal — it should be sorted. Or use recursion with min/max bounds."

```python
def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)
```

---

**Q26. How do you find the kth smallest element in a BST?**

"Do an inorder traversal and return the kth element."

```python
def kth_smallest(root, k):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val
        current = current.right

    return None
```

---

**Q27. How do you find the diameter of a binary tree?**

"The diameter is the left height plus the right height at any node. Calculate it for every node."

```python
def diameter(root):
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        max_diameter = max(max_diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return max_diameter
```

---

# PART 5: GRAPHS

---

**Q28. How do you implement BFS and DFS?**

"BFS uses a queue, DFS uses a stack or recursion."

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result
```

---

**Q29. How do you detect a cycle in a directed graph?**

"DFS with a recursion stack — if a node is already in the stack, there's a cycle."

```python
def has_cycle_directed(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
```

---

**Q30. How do you detect a cycle in an undirected graph?**

"Union-Find or DFS with parent tracking."

```python
def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
```

---

**Q31. How do you find the shortest path in an unweighted graph?**

"I'd use BFS — traverse level by level."

```python
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return 0

    visited = set([start])
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1
```

**Follow-up: Weighted graph?**

"Then I'd use Dijkstra's algorithm — with a priority queue."

---

**Q32. How do you find the number of islands?**

"I'd use DFS/BFS. For every '1', traverse the connected '1's and turn them into '0'."

```python
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)

    return count
```

---

**Q33. How do you clone a graph?**

"DFS/BFS with a hashmap — original node → clone node."

```python
def clone_graph(node):
    if not node:
        return None

    clones = {}

    def dfs(n):
        if n in clones:
            return clones[n]
        clone = Node(n.val)
        clones[n] = clone
        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)
```

---

# PART 6: DYNAMIC PROGRAMMING

---

**Q34. How do you solve climbing stairs?**

"Fibonacci pattern — dp[i] = dp[i-1] + dp[i-2]."

```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

---

**Q35. How do you solve coin change?**

"I'd use DP — minimum coins for each amount."

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
```

---

**Q36. How do you solve the longest increasing subsequence?**

"I'd use DP — O(n²). Binary search can bring it down to O(n log n)."

```python
def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
```

**Follow-up: O(n log n) approach?**

"Use patience sorting with binary search."

```python
import bisect

def length_of_lis_optimized(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

---

**Q37. How do you solve 0/1 Knapsack?**

"DP table — for items and capacity."

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    dp[i-1][w - weights[i-1]] + values[i-1]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

---

**Q38. How do you solve edit distance?**

"DP table — insert, delete, replace operations."

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # delete
                    dp[i][j-1],    # insert
                    dp[i-1][j-1]   # replace
                )

    return dp[m][n]
```

---

**Q39. How do you solve the longest common subsequence?**

"DP table — 2D array."

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

---

**Q40. How do you solve house robber?**

"DP — at each house, either rob it or skip it."

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current

    return prev1
```

**Follow-up: Circular houses?**

"Two cases — rob the first house or rob the last house. Take the max of both."

---

# PART 7: SORTING & SEARCHING

---

**Q41. How do you implement binary search?**

"For a sorted array — calculate mid, compare with the target."

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

**Follow-up: First occurrence?**

"Same approach, but when a match is found, continue on the left."

```python
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

---

**Q42. How do you implement quicksort?**

"Choose a pivot, partition, then recursively sort."

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```

**Follow-up: In-place quicksort?**

"Use the Lomuto partition scheme."

---

**Q43. How do you implement mergesort?**

"Divide and conquer — split the array into halves, sort, and merge."

```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

**Q44. How do you find the kth largest element?**

"I'd use quickselect — average O(n). Or a heap — O(n log k)."

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

**Follow-up: Quickselect approach?**

"Partition and check the pivot index."

---

**Q45. How do you sort colors (Dutch National Flag)?**

"Three pointers — low, mid, high. 0s on the left, 2s on the right."

```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

---

# PART 8: HASHMAPS & HEAPS

---

**Q46. How do you find top k frequent elements?**

"Use Counter for frequency, then a heap."

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

**Q47. How do you find the median from a data stream?**

"I'd use two heaps — a max heap for the lower half and a min heap for the upper half."

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lower = []  # max heap
        self.upper = []  # min heap

    def add_num(self, num):
        heapq.heappush(self.lower, -num)
        heapq.heappush(self.upper, -heapq.heappop(self.lower))

        if len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def find_median(self):
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2
```

---

**Q48. How do you find the kth smallest in a sorted matrix?**

"Use a min heap — push the first element of each row."

```python
import heapq

def kth_smallest(matrix, k):
    n = len(matrix)
    heap = [(matrix[i][0], i, 0) for i in range(n)]
    heapq.heapify(heap)

    for _ in range(k - 1):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c+1], r, c+1))

    return heap[0][0]
```

---

# PART 9: RECURSION & BACKTRACKING

---

**Q49. How do you generate all permutations?**

"Use backtracking — swap and recursively generate."

```python
def permute(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

---

**Q50. How do you generate all subsets?**

"Backtracking — include or exclude each element."

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

---

**Q51. How do you solve N-Queens?**

"Backtracking — place a queen in each row and check if it's valid."

```python
def solve_n_queens(n):
    result = []
    board = [['.'] * n for _ in range(n)]

    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)
    return result
```

---

**Q52. How do you solve word search?**

"DFS + backtracking — start from each cell."

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'

        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

---

# PART 10: BIT MANIPULATION

---

**Q53. How do you check if a number is a power of 2?**

"Bit manipulation — n & (n-1) == 0."

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

---

**Q54. How do you count set bits?**

"Brian Kernighan's algorithm."

```python
def count_bits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
```

---

**Q55. How do you find the single number (all others appear twice)?**

"Use XOR — the same numbers cancel out."

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

---

# PART 11: CODING PROBLEMS (Google, Microsoft, Amazon)

---

**Q56. Merge Intervals.**

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]
```

---

**Q57. Product of Array Except Self.**

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

print(product_except_self([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]
```

---

**Q58. Longest Substring Without Repeating Characters.**

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  # 3
```

---

**Q59. Container With Most Water.**

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

---

**Q60. Three Sum — find triplets that sum to zero.**

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

**Q61. Trapping Rain Water.**

```python
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
```

---

**Q62. Search in Rotated Sorted Array.**

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
```

---

**Q63. Find Minimum in Rotated Sorted Array.**

```python
def find_min_rotated(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

print(find_min_rotated([4, 5, 6, 7, 0, 1, 2]))  # 0
```

---

**Q64. Kth Largest Element in an Array.**

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
```

**Follow-up: Without heapq?**

```python
def find_kth_largest_manual(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]
```

---

**Q65. Valid Anagram.**

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

print(is_anagram("anagram", "nagaram"))  # True
```

---

# PART 12: ADDITIONAL PRACTICE CODE

---

**Q66. Fibonacci Series.**

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

**Q67. Factorial.**

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

---

**Q68. Prime Check.**

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

**Q69. Sort Dictionary by Value.**

```python
d = {'a': 3, 'b': 1, 'c': 2}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)  # {'b': 1, 'c': 2, 'a': 3}
```

---

**Q70. Flatten Nested List.**

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

**Q71. Two Sum.**

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

---

**Q72. Valid Parentheses.**

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

**Q73. Move Zeroes to End.**

```python
def move_zeroes(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # [1, 3, 12, 0, 0]
```

---

**Q74. Find Missing Number.**

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([3, 0, 1]))  # 2
```

---

**Q75. Check Palindrome Number.**

```python
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False
```

---

**Q76. Count Vowels in String.**

```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))  # 3
```

---

**Q77. Remove Duplicates from List (Preserve Order).**

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
```

---

**Q78. Find Intersection of Two Lists.**

```python
def intersection(a, b):
    return list(set(a) & set(b))

print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # [3, 4]
```

---

**Q79. Check if Two Strings are Rotations.**

```python
def are_rotations(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

print(are_rotations("abcde", "cdeab"))  # True
```

---

**Q80. Find First Duplicate.**

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

**Q81. Sum of Digits.**

```python
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(1234))  # 10
```

---

**Q82. Reverse Words in Sentence.**

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("I love Python"))
# Output: "Python love I"
```

---

**Q83. Find Longest Word in Sentence.**

```python
def longest_word(s):
    words = s.split()
    return max(words, key=len)

print(longest_word("I love programming in Python"))
# Output: "programming"
```

---

**Q84. Check Armstrong Number.**

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

print(is_armstrong(153))  # True (1^3 + 5^3 + 3^3 = 153)
```

---

**Q85. Find GCD of Two Numbers.**

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6
```

**Follow-up: LCM?**

```python
def lcm(a, b):
    return a * b // gcd(a, b)
```

---

**Q86. Check if String is Palindrome.**

```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
```

---

**Q87. Find Maximum and Minimum in List.**

```python
def find_max_min(nums):
    return max(nums), min(nums)

print(find_max_min([3, 1, 4, 1, 5, 9, 2, 6]))  # (9, 1)
```

**Follow-up: Without built-in functions?**

```python
def find_max_min_manual(nums):
    max_val = min_val = nums[0]
    for num in nums[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
```

---

**Q88. Rotate Array by K Positions.**

```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k]

print(rotate_array([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

**Follow-up: In-place rotation?**

```python
def rotate_in_place(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
```

---

**Q89. Find All Pairs with Given Sum.**

```python
def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

print(find_pairs([1, 2, 3, 4, 5], 6))  # [(1, 5), (2, 4)]
```

---

**Q90. Check if Number is Perfect Square.**

```python
def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

print(is_perfect_square(16))  # True
print(is_perfect_square(14))  # False
```

---

**Q91. Merge Intervals.**

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Output: [[1, 6], [8, 10], [15, 18]]
```

---

**Q92. Product of Array Except Self.**

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result

print(product_except_self([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]
```

---

**Q93. Longest Substring Without Repeating Characters.**

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  # 3
```

---

**Q94. Container With Most Water.**

```python
def max_area(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

---

**Q95. Three Sum.**

```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

# PART 13: TIME & SPACE COMPLEXITY CHEAT SHEET

---

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
| Three Sum | O(n²) | O(n) |
| Container With Most Water | O(n) | O(1) |
| Trapping Rain Water | O(n) | O(1) |
| Search Rotated Array | O(log n) | O(1) |
| Kth Largest | O(n log k) | O(k) |

---

# PART 14: COMMON PATTERNS (Google/Microsoft)

---

| Pattern | Problems | Approach |
|---------|----------|----------|
| **Two Pointers** | Two Sum, Container with Water, Remove Duplicates | Left + Right pointers |
| **Sliding Window** | Max Subarray, Longest Substring | Window expand/shrink |
| **Fast & Slow** | Cycle Detection, Middle of List | Slow 1x, Fast 2x |
| **Merge Intervals** | Meeting Rooms, Merge Intervals | Sort + merge |
| **Cyclic Sort** | Missing Number, Duplicate Number | Index-based |
| **Tree BFS** | Level Order, Zigzag | Queue |
| **Tree DFS** | Path Sum, LCA | Recursion |
| **Two Heaps** | Median, Sliding Window | Max heap + Min heap |
| **Subsets** | Permutations, Combinations | Backtracking |
| **Modified Binary Search** | Rotated Array, First/Last | Binary search variants |
| **Top K Elements** | Kth Largest, Top K Frequent | Heap |
| **K-way Merge** | Merge K Lists | Min heap |
| **Dynamic Programming** | Knapsack, LCS, Coin Change | Memoization/Tabulation |
| **Backtracking** | N-Queens, Sudoku | Recursion + pruning |

---

# PART 15: QUICK REVISION CHECKLIST

---

- [ ] Binary Search — O(log n)
- [ ] First Non-Repeating Character
- [ ] Anagram Check — sorting vs Counter
- [ ] Merge Two Sorted Lists
- [ ] Reverse Linked List — iterative + recursive
- [ ] Detect Cycle in Linked List — Floyd's algorithm
- [ ] Kadane's Algorithm — max subarray
- [ ] Remove Duplicates from Sorted Array
- [ ] Stack using Queues
- [ ] Longest Common Prefix
- [ ] Two Sum — hashmap + two pointers
- [ ] Valid Parentheses — stack
- [ ] Move Zeroes
- [ ] Missing Number — sum formula + XOR
- [ ] Majority Element — Boyer-Moore voting
- [ ] Three Sum — two pointers
- [ ] Container With Most Water
- [ ] Trapping Rain Water
- [ ] Search in Rotated Sorted Array
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Kth Largest Element
- [ ] Merge Intervals
- [ ] Product of Array Except Self
- [ ] Longest Substring Without Repeating Characters
- [ ] Coin Change
- [ ] Longest Increasing Subsequence
- [ ] Edit Distance
- [ ] Longest Common Subsequence
- [ ] House Robber
- [ ] Climbing Stairs
- [ ] N-Queens
- [ ] Word Search
- [ ] Number of Islands
- [ ] Clone Graph
- [ ] BFS and DFS
- [ ] Cycle Detection — directed + undirected
- [ ] Power of Two
- [ ] Count Set Bits
- [ ] Single Number

---

# PART 16: INTERVIEW TIPS

---

1. **Clarify** — Input size? Sorted? Duplicates? Edge cases?
2. **Examples** — Create small test cases.
3. **Brute Force** — Explain the simple solution first.
4. **Optimize** — Improve time/space complexity.
5. **Code** — Write clean, readable code.
6. **Test** — Run through edge cases.
7. **Analyze** — State time and space complexity.

---

**Practice Tip:** Solve 2–3 problems daily. Use LeetCode, GeeksforGeeks, and InterviewBit. For Google/Microsoft, focus on **Medium/Hard** level problems.

---

[← Previous: Module 6](module-6-system-design-coding.md) | [Back to Index](README.md) | [Next: Practice Code →](practice-code.md)
