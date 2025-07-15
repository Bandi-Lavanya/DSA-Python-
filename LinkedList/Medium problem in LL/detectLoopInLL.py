#Node class represents
# a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to detect a loop 
# n a linked list
def detect_loop_brute(head):
    # Initialize a pointer 'temp' at 
    # the head of the linked list
    temp = head

    # Create a set to keep track
    # of encountered nodes
    node_set = set()

    # Step 2: Traverse the linked list
    while temp is not None:
        # If the node is already
        # in the set, there is a loop
        if temp in node_set:
            return True

        # Store the current node in the set
        node_set.add(temp)

        # Move to the next node
        temp = temp.next

    # Step 3: If the list is successfully
    # traversed without a loop, return False
    return False


# Function to detect a loop in a
# linked list using the Tortoise and Hare Algorithm
def detect_cycle_optimal(head):
    # Initialize two pointers, slow and fast,
    # to the head of the linked list
    slow = head
    fast = head

    # Step 2: Traverse the linked list
    # with the slow and fast pointers
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next
        # Move fast two steps
        fast = fast.next.next

        # Check if slow and fast pointers meet
        if slow == fast:
            return True  # Loop detected

    # If fast reaches the end of the
    # list, there is no loop
    return False

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third

    # Check if there is a loop
    # in the linked list
    if detect_loop_brute(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    if detect_cycle_optimal(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
    # No need to explicitly free memory
    # in Python; memory management is automatic