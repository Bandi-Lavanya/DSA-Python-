class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def array_to_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Example usage
arr = [10, 20, 30, 40, 50]
head = array_to_linked_list(arr)
print_linked_list(head)


# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.next = node3

# Head of the linked list
head2 = node1
print_linked_list(head2)

def length_of_linked_list(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count
print("Length of linked list:", length_of_linked_list(head))


def search_element(head, target):
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False
print("Is 20 in linked list?", search_element(head, 20))


def delete_node(head, target):
    # Case 1: If the list is empty
    if head is None:
        return None

    # Case 2: If the head needs to be deleted
    if head.data == target:
        return head.next

    # Case 3: Deleting node from the middle or end
    prev = head
    curr = head.next

    while curr:
        if curr.data == target:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next

    return head  # Target not found
print("Original list:")
print_linked_list(head)

head = delete_node(head, 20)  # Delete node with value 20

print("After deleting 20:")
print_linked_list(head)

