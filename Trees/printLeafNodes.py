'''
8
3 4 2 54 23 234 43
          3
        /   \
       4     2
      / \   / \
     5  23 54 234
    /
   43

output:43 23 54 234'''
from collections import deque

# Node class
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

# Print leaf nodes
def print_leaf_nodes(root):
    if not root:
        print("no BT")
        return
    
    result = []
    
    def dfs(node):
        if not node:
            return
        if not node.left and not node.right:  # leaf condition
            result.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    print(" ".join(map(str, result)))


# ---------------------
# Main Execution
# ---------------------
n = int(input().strip())
if n == 0:
    print("no BT")
else:
    arr = list(map(int, input().split()))
    root = build_tree(arr)
    print_leaf_nodes(root)
