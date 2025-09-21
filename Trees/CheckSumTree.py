'''
3
3 1 2
    3
   / \
  1   2
output:true

7
26 10 3 4 6 1 2
           26
         /    \
       10      3
      /  \    / \
     4    6  1   2

true
'''
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def ListToBT(arr):
    """Convert level order list to Binary Tree"""
    if not arr or arr[0] == 0:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        # Left child
        if i < len(arr):
            node.left = TreeNode(arr[i])
            q.append(node.left)
            i += 1

        # Right child
        if i < len(arr):
            node.right = TreeNode(arr[i])
            q.append(node.right)
            i += 1

    return root


def isSumTree(root):
    def helper(node):
        if not node:
            return 0   # empty tree → sum = 0
        if not node.left and not node.right:
            return node.val  # leaf → return value

        left_sum = helper(node.left)
        right_sum = helper(node.right)

        # If invalid subtree detected earlier
        if left_sum == -1 or right_sum == -1:
            return -1
        
        # Check sum tree condition
        if node.val != left_sum + right_sum:
            return -1
        
        return node.val + left_sum + right_sum

    return helper(root) != -1

# ------------------ DRIVER ------------------
n = int(input().strip())
if n == 0:
    print("true")  # empty tree is a sum tree
else:
    arr = list(map(int, input().split()))
    root = ListToBT(arr)
    print(str(isSumTree(root)).lower())
