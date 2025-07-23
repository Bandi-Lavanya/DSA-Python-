class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to insert a new node at the end
def insert_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    return head

def find_pairs_optimal(head, target):
    result = []

    # Step 1: Find the tail node
    right = head
    while right.next:
        right = right.next

    # Step 2: Two-pointer approach
    left = head
    while left.data < right.data:
        curr_sum = right.data + left.data
        if curr_sum == target:
            result.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif curr_sum < target:
            left = left.next
        else:
            right = right.prev

    return result

# Brute force function to find pairs with given sum
def find_pairs_brute(head, target):
    result = []
    temp1 = head

    while temp1:
        temp2 = temp1.next
        while temp2 and temp1.data+temp2.data<=target:
            if temp1.data + temp2.data == target:
                result.append([temp1.data, temp2.data])
            temp2 = temp2.next
        temp1 = temp1.next

    return result

# Utility function to build the DLL from list
def build_dll(values):
    head = None
    for val in values:
        head = insert_end(head, val)
    return head

# Example usage
values = [1, 2, 4, 5, 6, 8, 9]
target = 7
head = build_dll(values)
pairs = find_pairs_brute(head, target)
print("Pairs with sum", target, "are:", pairs)
values = [1, 2, 4, 5, 6, 8, 9]
target = 7
head = build_dll(values)
pairs = find_pairs_optimal(head, target)
print("Pairs with sum", target, "are:", pairs)
