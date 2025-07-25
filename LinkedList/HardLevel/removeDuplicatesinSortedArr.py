class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    return head

def remove_duplicates(head):
    temp = head
    while temp and temp.next:
        if temp.data == temp.next.data:
            duplicate = temp.next
            temp.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = temp
        else:
            temp = temp.next
    return head

def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage:
head = None
for val in [1, 2, 2, 3, 3, 3, 4, 5, 5]:
    head = insert_at_end(head, val)

print("Original List:")
print_list(head)

head = remove_duplicates(head)

print("List after removing duplicates:")
print_list(head)
