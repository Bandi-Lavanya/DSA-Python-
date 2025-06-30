class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def print_dll(head):
    current = head
    print("DLL: None ← ", end="")
    while current:
        print(f"[{current.data}]", end=" ⇄ " if current.next else "")
        current = current.next
    print(" → None")


# Deletions
def delete_head(head):
    if not head:
        print("List is empty")
        return None
    next_node = head.next
    if next_node:
        next_node.prev = None
    return next_node

def delete_tail(head):
    if not head:
        print("List is empty")
        return None
    if not head.next:
        return None
    current = head
    while current.next:
        current = current.next
    if current.prev:
        current.prev.next = None
    return head

def delete_kth_node(head, k):
    if k <= 1:
        return delete_head(head)
    current = head
    count = 1
    while current and count < k:
        current = current.next
        count += 1
    if not current:
        print("Position out of bounds")
        return head
    if current.prev:
        current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev
    return head

def delete_given_node(head, node):
    if not head or not node:
        print("Node or list does not exist")
        return head
    if node == head:
        return delete_head(head)
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
    return head

# Example usage
arr = [1, 2, 3, 4, 5]
head = None
for val in arr:
    if not head:
        head = Node(val)
        current = head
    else:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

# Delete 2nd node (which has value 2)
head = delete_kth_node(head, 2)
print("\nAfter deleting 2nd node:")
print_dll(head)

# Delete tail
head = delete_tail(head)
print("\nAfter deleting tail:")
print_dll(head)

# Delete given node (e.g., node with value 3)
target = head
while target and target.data != 3:
    target = target.next
head = delete_given_node(head, target)
print("\nAfter deleting node with value 3:")
print_dll(head)

# Delete head node
head = delete_head(head)
print("\nAfter deleting head:")
print_dll(head)

