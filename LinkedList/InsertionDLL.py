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

# Insertions
def insert_head(head, val):
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def insert_tail(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.prev = current
    return head

def insert_before_kth_node(head, val, k):
    if k <= 1:
        return insert_head(head, val)
    current = head
    count = 1
    while current and count < k:
        current = current.next
        count += 1
    if not current:
        print("Position out of bounds")
        return head
    new_node = Node(val)
    new_node.next = current
    new_node.prev = current.prev
    if current.prev:
        current.prev.next = new_node
    current.prev = new_node
    return head

def insert_before_given_node(head, target_node, val):
    if not target_node:
        print("Target node does not exist.")
        return head
    if target_node == head:
        return insert_head(head, val)
    new_node = Node(val)
    new_node.next = target_node
    new_node.prev = target_node.prev
    if target_node.prev:
        target_node.prev.next = new_node
    target_node.prev = new_node
    return head


# Build initial list: [1] ⇄ [2] ⇄ [4]
head = None
for val in [1, 2, 4]:
    head = insert_tail(head, val)
print("Initial list:")
print_dll(head)

# Insert before 3rd node (insert 3 before 3rd node, i.e., before 4)
head = insert_before_kth_node(head, 3, 3)
print("\nAfter inserting 3 before 3rd node:")
print_dll(head)


# Insert at head (insert 0)
head = insert_head(head, 0)
print("\nAfter inserting 0 at head:")
print_dll(head)

# Insert at tail (insert 5)
head = insert_tail(head, 5)
print("\nAfter inserting 5 at tail:")
print_dll(head)


# Insert before given node (e.g., before node with value 3)
target = head
while target and target.data != 3:
    target = target.next
head = insert_before_given_node(head, target, 2.5)
print("\nAfter inserting 2.5 before node with value 3:")
print_dll(head)


