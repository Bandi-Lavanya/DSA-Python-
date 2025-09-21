'''7
1 6 4 7 2 0 9
output: 1 4 9
        1
       / \
      6   4
     / \    \
    7   2    9
'''

from collections import deque

# Node class for Binary Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Function to build tree from level order input
def build_tree(arr):
    if not arr or arr[0] == 0:
        return None
    
    root = TreeNode(arr[0])
    q = deque([root])
    i = 1
    
    while q and i < len(arr):
        node = q.popleft()
        
        # Left child
        if arr[i] != 0:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1
        if i >= len(arr): break
        
        # Right child
        if arr[i] != 0:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1
    
    return root

# Function to print Right View
def right_view(root):
    if not root:
        print("There is no Binary Tree")
        return
    
    q = deque([root])
    result = []
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            # last node of current level → right view
            if i == size - 1:
                result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    print(*result)  # print as per sample format


# ------------------------
# Main Execution
# ------------------------
n = int(input())
if n == 0:
    print("There is no Binary Tree")
else:
    arr = list(map(int, input().split()))
    root = build_tree(arr)
    right_view(root)
