class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Utility: Convert array to linked list
def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head


# Utility: Print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# 1. Insert at head
def insert_at_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


# 2. Insert at tail
def insert_at_tail(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


# 3. Insert at Kth position (0-based index)
def insert_at_kth(head, val, k):
    new_node = Node(val)
    if k == 0:
        return insert_at_head(head, val)

    current = head
    pos = 0
    while current and pos < k - 1:
        current = current.next
        pos += 1

    if current is None:
        print(f"Position {k} is out of bounds.")
        return head

    new_node.next = current.next
    current.next = new_node
    return head


# 4. Insert before value X
def insert_before_value(head, target, val):
    new_node = Node(val)

    # Insert before head
    if head and head.data == target:
        return insert_at_head(head, val)

    prev = None
    current = head
    while current and current.data != target:
        prev = current
        current = current.next

    if current is None:
        print(f"Value {target} not found.")
        return head

    prev.next = new_node
    new_node.next = current
    return head


arr = [10, 20, 30, 40]
head = array_to_linked_list(arr)
print("Original Linked List:")
print_linked_list(head)

# Insert at head
head = insert_at_head(head, 5)
print("\nAfter inserting 5 at head:")
print_linked_list(head)

# Insert at tail
head = insert_at_tail(head, 50)
print("\nAfter inserting 50 at tail:")
print_linked_list(head)

# Insert at 3rd position (0-based)
head = insert_at_kth(head, 25, 3)
print("\nAfter inserting 25 at 3rd position:")
print_linked_list(head)

# Insert before value 30
head = insert_before_value(head, 30, 27)
print("\nAfter inserting 27 before value 30:")
print_linked_list(head)
