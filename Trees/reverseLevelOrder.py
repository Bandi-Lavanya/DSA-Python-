'''8
3 4 2 5 23 54 234 43
          3
        /   \
       4     2
      / \   / \
     5  23 54 234
    /
   43
output:43 5 23 54 234 4 2 3'''
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree from level order input
def build_tree(arr):
    if not arr or arr[0] == 0:
        return None
    
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    
    while q and i < len(arr):
        node = q.popleft()
        
        # Left child
        if i < len(arr) and arr[i] != 0:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] != 0:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    
    return root

# Reverse level order traversal
def reverse_level_order(root):
    if not root:
        print("There is no Binary Tree")
        return
    
    q = deque([root])
    stack = []   # to reverse BFS
    
    while q:
        node = q.popleft()
        stack.append(node.val)
        
        # push right first, then left (so left appears before right in reversed stack)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    
    print(" ".join(map(str, stack[::-1])))


# --------------------------
# Main Execution
# --------------------------
n = int(input().strip())
if n == 0:
    print("There is no Binary Tree")
else:
    arr = list(map(int, input().split()))
    root = build_tree(arr)
    reverse_level_order(root)
