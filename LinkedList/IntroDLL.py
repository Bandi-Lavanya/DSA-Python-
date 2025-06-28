class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

current = node1
while current:
    print(current.data, end=" -> ")
    current = current.next

current = node3
while current:
    print(current.data, end=" -> ")
    current = current.prev


def array_to_dll(arr):
    if not arr:
        return None  # empty array → empty DLL

    head = Node(arr[0])
    current = head

    for val in arr[1:]:
        new_node = Node(val)
        current.next = new_node
        new_node.prev = current
        current = new_node

    return head

def print_forward(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        last = current
        current = current.next
    print("None")
    return last  # Return last node for reverse traversal

def print_backward(tail):
    current = tail
    while current:
        print(current.data, end=" <-> ")
        current = current.prev
    print("None")

arr = [10, 20, 30, 40, 50]
head = array_to_dll(arr)

print("\nForward Traversal:")
tail = print_forward(head)

print("Backward Traversal:")
print_backward(tail)
