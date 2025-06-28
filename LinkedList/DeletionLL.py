class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper: Print Linked List
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# 1. Delete head
def delete_head(head):
    if not head:
        print("List is empty.")
        return None
    return head.next

# 2. Delete tail
def delete_tail(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

# 3. Delete kth node (1-based index)
def delete_kth(head, k):
    if k == 1:
        return delete_head(head)
    current = head
    count = 1
    while current and count < k - 1:
        current = current.next
        count += 1
    if not current or not current.next:
        print("Invalid position.")
        return head
    current.next = current.next.next
    return head

# 4. Delete node with value X
def delete_value(head, x):
    if not head:
        return None
    if head.data == x:
        return head.next
    current = head
    while current.next and current.next.data != x:
        current = current.next
    if current.next:
        current.next = current.next.next
    else:
        print(f"Value {x} not found in list.")
    return head

# Helper: Convert array to linked list
def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Demo
arr = [10, 20, 30, 40, 50]
head = array_to_linked_list(arr)
print("Original List:")
print_linked_list(head)

print("\nAfter deleting head:")
head = delete_head(head)
print_linked_list(head)

print("\nAfter deleting tail:")
head = delete_tail(head)
print_linked_list(head)

print("\nAfter deleting 2nd element:")
head = delete_kth(head, 2)
print_linked_list(head)

print("\nAfter deleting value 30:")
head = delete_value(head, 30)
print_linked_list(head)
