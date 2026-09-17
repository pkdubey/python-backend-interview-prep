# DSA Questions — Complete Interview Preparation

[← Back to Index](README.md) | [← Previous: Module 6](module-6-system-design-coding.md)

> **Note:** Ye section Google, Microsoft, Amazon jaise product-based companies ke liye specially prepare kiya gaya hai. Yahan sirf questions nahi — **thinking process** bhi explain kiya hai. Har problem mein pehle approach batao, phir code likho.

---

# PART 1: ARRAYS & STRINGS

---

**Q1. How do you find the maximum subarray sum? (Kadane's Algorithm)**

"Pehle brute force sochunga — O(n²) ya O(n³). Lekin optimal O(n) hai Kadane's algorithm.

Approach: Ek current sum maintain karo. Agar current sum negative ho jaye, toh reset karo — kyunki negative sum aage kabhi help nahi karega. Har step pe max update karo."

```python
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum
```

**Follow-up: What if all numbers are negative?**
"Kadane's algorithm still works because we initialize with nums[0] and take max at each step. If all negative, it returns the least negative number (maximum)."

**Follow-up: What if we need the actual subarray, not just sum?**
"Track start and end indices whenever we update max_sum."

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

"Brute force O(n²) — har pair check karo. Lekin optimal O(n) hai hashmap se.

Approach: Ek hashmap banao. Har number ke liye check karo ki target - num pehle dekha hai kya. Agar haan, toh answer mil gaya."

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

**Follow-up: What if array is sorted?**
"Two pointers approach use karunga — O(n) time, O(1) space."

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
"Same hashmap approach, lekin set mein store karo to avoid duplicates."

---

**Q3. How do you find the maximum product subarray?**

"Ye tricky hai kyunki negative numbers product ko positive bana sakte hain. Do variables maintain karo — max_so_far aur min_so_far. Kyunki negative * negative = positive."

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

"Sum formula use karunga — O(n) time, O(1) space. Sum of 1 to n = n*(n+1)/2. Actual sum subtract karo."

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
```

**Follow-up: What if array has duplicates?**
"XOR approach use karunga — same number XOR twice = 0. Toh missing number mil jayega."

```python
def missing_number_xor(nums):
    xor = 0
    for i in range(len(nums) + 1):
        xor ^= i
    for num in nums:
        xor ^= num
    return xor
```

**Follow-up: What if numbers are not 1 to n?**
"Sort karke adjacent check karunga, ya hashmap use karunga."

---

**Q5. How do you find the first non-repeating character in a string?**

"Pehle Counter se frequency count karunga. Phir string pe iterate karke first character dhundhunga jiska count 1 ho."

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
"Array of 26 size use karunga (agar sirf lowercase letters hain)."

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

"Sort karke compare karunga — O(n log n). Ya frequency count karunga — O(n)."

```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
```

**Follow-up: O(n) approach?**
"Counter use karunga."

```python
from collections import Counter

def is_anagram_optimized(s1, s2):
    return Counter(s1) == Counter(s2)
```

**Follow-up: What if strings have Unicode characters?**
"Counter approach works for any characters. Sorting also works."

---

**Q7. How do you group anagrams together?**

"Har word ko sort karke key banaunga. Same key wale words same group mein jayenge. Hashmap use karunga."

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
"O(n * k log k) where n = number of words, k = max length of word."

---

**Q8. How do you find the longest common prefix?**

"Pehle word ko prefix maan lo. Baaki words se compare karo. Jab tak match na kare, prefix ko chhota karo."

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
"Vertical scanning — har column check karo. O(n*m) time, O(1) space."

---

**Q9. How do you rotate an array by k steps?**

"Reversal technique use karunga — O(n) time, O(1) space.

Approach:
1. Reverse entire array
2. Reverse first k elements
3. Reverse remaining elements"

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
"Same approach, lekin order alag hoga — reverse first n-k, reverse last k, reverse all."

---

**Q10. How do you find the container with most water?**

"Two pointers approach — O(n) time. Left aur right pointers se area calculate karo. Jo side chhota hai, usse move karo."

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

"Iterative approach — 3 pointers use karunga: prev, current, next. Har step pe current.next ko prev pe point karaunga."

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
"Recursion se bhi ho sakta hai — O(n) time, O(n) stack space."

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

"Floyd's cycle detection — slow aur fast pointers. Agar cycle hai, toh fast pointer slow se mil jayega."

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

**Follow-up: How to find the start of cycle?**
"Jab slow aur fast mile, slow ko head pe le jao. Phir dono ko 1 step move karo. Jahan mile, wahi cycle start hai."

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

**Follow-up: How to find length of cycle?**
"Jab slow aur fast mile, wahi se count karo jab tak wapas same node pe na aa jaye."

---

**Q13. How do you find the middle of a linked list?**

"Slow aur fast pointers — slow 1 step, fast 2 steps. Jab fast end pe pahunche, slow middle pe hoga."

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Follow-up: Even length mein kaunsa middle?**
"Ye approach second middle return karta hai. First middle chahiye toh fast ko ek step pehle rok do."

---

**Q14. How do you merge two sorted linked lists?**

"Two pointers approach — dono lists ke heads compare karo, chhota wala result mein add karo."

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

**Q15. How do you remove nth node from end of linked list?**

"Two pointers — fast ko n+1 steps aage bhejo, phir dono ko move karo. Jab fast end pe pahunche, slow nth node se pehle hoga."

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

**Q16. How do you check if linked list is palindrome?**

"Middle find karo, second half reverse karo, phir compare karo."

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

"Stack use karunga. Opening bracket push karo, closing bracket aaye toh check karo ki top matching hai kya."

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
"Same approach — mapping mein sab types daal do."

---

**Q18. How do you implement a stack using queues?**

"Push operation mein queue ko rotate karunga — naya element front pe aaye."

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

"Two stacks use karunga — input aur output. Push input mein, pop output se."

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

**Q20. How do you find next greater element?**

"Stack use karunga — monotonic decreasing stack. Har element ke liye check karo ki stack top se bada hai kya."

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
"Array ko double karke same approach, lekin sirf n elements tak."

---

# PART 4: TREES & BINARY SEARCH TREES

---

**Q21. How do you traverse a binary tree? (Inorder, Preorder, Postorder)**

"Recursive approach simple hai. Iterative bhi ho sakta hai stack se."

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
"Stack use karunga."

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

"Recursion — left aur right subtree ki height ka max + 1."

```python
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))
```

---

**Q23. How do you check if binary tree is balanced?**

"Har node pe check karo ki left aur right height ka difference 1 se zyada nahi hona chahiye."

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

**Q24. How do you find lowest common ancestor (LCA) in BST?**

"BST property use karunga — agar dono values root se chhoti hain, left jao. Agar dono badi hain, right jao. Warna root hi LCA hai."

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
"Recursion use karunga — left aur right se LCA dhundo."

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

"Inorder traversal karo — sorted hona chahiye. Ya recursion se min/max bounds check karo."

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

**Q26. How do you find kth smallest element in BST?**

"Inorder traversal karo — kth element return karo."

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

**Q27. How do you find diameter of binary tree?**

"Diameter = left height + right height at any node. Har node pe calculate karo."

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

"BFS queue se, DFS stack ya recursion se."

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

**Q29. How do you detect cycle in directed graph?**

"DFS with recursion stack — agar node already in stack hai, cycle hai."

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

**Q30. How do you detect cycle in undirected graph?**

"Union-Find ya DFS with parent tracking."

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

**Q31. How do you find shortest path in unweighted graph?**

"BFS use karunga — level by level traverse karo."

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
"Dijkstra's algorithm use karunga — priority queue se."

---

**Q32. How do you find number of islands?**

"DFS/BFS use karunga. Har '1' pe traverse karo aur connected '1's ko '0' kar do."

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

"DFS/BFS with hashmap — original node → clone node."

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

"DP use karunga — minimum coins for each amount."

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

**Q36. How do you solve longest increasing subsequence?**

"DP use karunga — O(n²). Binary search se O(n log n) bhi ho sakta hai."

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
"Patience sorting use karunga — binary search se."

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

"DP table — items aur capacity ke liye."

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

**Q39. How do you solve longest common subsequence?**

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

"DP — har house pe ya toh rob karo ya skip karo."

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
"Do cases — first house rob karo ya last house rob karo. Dono ka max lo."

---

# PART 7: SORTING & SEARCHING

---

**Q41. How do you implement binary search?**

"Sorted array mein — mid calculate karo, target se compare karo."

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
"Same approach, lekin match milne pe left continue karo."

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

"Pivot choose karo, partition karo, recursively sort karo."

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
"Lomuto partition scheme use karunga."

---

**Q43. How do you implement mergesort?**

"Divide and conquer — array ko halves mein divide karo, sort karo, merge karo."

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

**Q44. How do you find kth largest element?**

"Quickselect use karunga — average O(n). Ya heap use karunga — O(n log k)."

```python
import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```

**Follow-up: Quickselect approach?**
"Partition karo, pivot index check karo."

---

**Q45. How do you sort colors (Dutch National Flag)?**

"Three pointers — low, mid, high. 0s left, 2s right."

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

"Counter se frequency count karo, phir heap use karo."

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

---

**Q47. How do you find median from data stream?**

"Two heaps use karunga — max heap for lower half, min heap for upper half."

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

**Q48. How do you find kth smallest in sorted matrix?**

"Min heap use karunga — har row ka first element push karo."

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

"Backtracking use karunga — swap karke recursively generate karo."

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

"Backtracking — har element ko include ya exclude karo."

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

"Backtracking — har row mein queen place karo, check karo valid hai kya."

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

"DFS + backtracking — har cell se start karo."

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

**Q53. How do you check if number is power of 2?**

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

**Q55. How do you find single number (all others appear twice)?**

"XOR use karunga — same numbers cancel out."

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

---

# PART 11: INTERVIEW TIPS & PATTERNS

---

## Common Patterns (Google/Microsoft Mein)

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

## Time Complexity Cheat Sheet

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Hashmap lookup |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Single loop |
| O(n log n) | Linearithmic | Sorting |
| O(n²) | Quadratic | Nested loops |
| O(2^n) | Exponential | Subsets |
| O(n!) | Factorial | Permutations |

---

## Space Complexity Cheat Sheet

| Complexity | Example |
|------------|---------|
| O(1) | Two pointers, Kadane's |
| O(n) | Hashmap, recursion stack |
| O(n²) | DP table 2D |
| O(n log n) | Merge sort |

---

## Interview Approach (Google/Microsoft Style)

1. **Clarify** — Input size? Sorted? Duplicates? Edge cases?
2. **Examples** — Small test cases banao
3. **Brute Force** — Pehle simple solution batao
4. **Optimize** — Time/space complexity improve karo
5. **Code** — Clean, readable code likho
6. **Test** — Edge cases run karo
7. **Analyze** — Time/space complexity batao

---

## Important Tips

1. **Bolo jo soch rahe ho** — interviewer ko approach batao
2. **Edge cases** — Empty array, single element, duplicates
3. **Optimize karo** — Brute force se optimal tak
4. **Code clean rakho** — Meaningful variable names
5. **Test karo** — Dry run karo code likhne ke baad
6. **Complexity batao** — Time aur space dono

---

**Practice Tip:** Roz 2-3 problems solve karo. LeetCode, GeeksforGeeks, aur InterviewBit use karo. Google/Microsoft ke liye **Medium/Hard** level pe focus karo.

---

[← Previous: Module 6](module-6-system-design-coding.md) | [Back to Index](README.md) | [Next: Practice Code →](practice-code.md)
