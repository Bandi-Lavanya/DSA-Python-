'''Original List:
10 <-> 20 <-> 30 <-> 20 <-> 40 <-> 20 <-> 50 <-> None
After deleting 20:
10 <-> 30 <-> 40 <-> 50 <-> None'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def delete_occurrences(head, key):
    current = head

    while current:
        next_node = current.next  # Store next node because current might be deleted

        if current.data == key:
            # If it's the head node
            if current.prev is None:
                head = current.next
                if head:
                    head.prev = None
            else:
                current.prev.next = current.next

                if current.next:
                    current.next.prev = current.prev
        current = next_node

    return head

# Helper Functions
def create_doubly_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for item in arr[1:]:
        new_node = Node(item)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def print_doubly_linked_list(head):
    while head:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

# Test
if __name__ == "__main__":
    arr = [10, 20, 30, 20, 40, 20, 50]
    key = 20
    head = create_doubly_linked_list(arr)
    print("Original List:")
    print_doubly_linked_list(head)

    head = delete_occurrences(head, key)
    print(f"After deleting {key}:")
    print_doubly_linked_list(head)
