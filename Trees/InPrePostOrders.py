'''4 2 5 1 3 6 
Preorder Traversal:
1 2 4 5 3 6 
Postorder Traversal:
4 5 2 6 3 1 
Preorder traversal: 1 2 4 5 3 
Inorder traversal: 4 2 5 1 3 
Postorder traversal: 4 5 2 3 1 '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right=None
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.right= Node(6)
def IOT(root):
    if root is None:
        return
    IOT(root.left)
    print(root.data,end=" ")
    IOT(root.right)
print("Inorder Traversal:")
IOT(root)

def POT(root):
    if root is None:
        return
    print(root.data,end=" ")
    POT(root.left)
    POT(root.right)
print("\nPreorder Traversal:")
POT(root)

def PostOT(root):
    if root is None:
        return
    PostOT(root.left)
    PostOT(root.right)
    print(root.data,end=" ")
print("\nPostorder Traversal:")
PostOT(root)

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to get the Preorder,
# Inorder and Postorder traversal
# Of Binary Tree in One traversal
def pre_in_post_traversal(root):
    # Lists to store traversals
    pre, in_order, post = [], [], []

    # If the tree is empty,
    # return empty traversals
    if root is None:
        return []

    # Stack to maintain nodes
    # and their traversal state
    stack = [(root, 1)]

    while stack:
        node, state = stack.pop()

        # this is part of pre
        if state == 1:
            # Store the node's data
            # in the preorder traversal
            pre.append(node.data)
            # Move to state 2
            # (inorder) for this node
            state = 2
            # Push the updated state
            # back onto the stack
            stack.append((node, state))

            # Push left child onto
            # the stack for processing
            if node.left:
                stack.append((node.left, 1))

        # this is a part of in
        elif state == 2:
            # Store the node's data
            # in the inorder traversal
            in_order.append(node.data)
            # Move to state 3
            # (postorder) for this node
            state = 3
            # Push the updated state
            # back onto the stack
            stack.append((node, state))

            # Push right child onto
            # the stack for processing
            if node.right:
                stack.append((node.right, 1))

        # this is part of post
        else:
            # Store the node's data
            # in the postorder traversal
            post.append(node.data)

    # Returning the traversals
    return [pre, in_order, post]

# Function to print the
# elements of a list
def print_list(lst):
    # Iterate through the list
    # and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Getting the pre-order, in-order,
    # and post-order traversals
    traversals = pre_in_post_traversal(root)

    # Extracting the traversals
    # from the result
    pre, in_order, post = traversals

    # Printing the traversals
    print("Preorder traversal: ", end="")
    print_list(pre)

    print("Inorder traversal: ", end="")
    print_list(in_order)

    print("Postorder traversal: ", end="")
    print_list(post)
                           