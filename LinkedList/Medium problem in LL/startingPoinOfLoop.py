'''Output:
Loop detected in the linked list at point: 3
Loop detected. Starting node of the loop is: 3'''
#Loop detected in the linked list at point: 3
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
            return temp

        # Store the current node in the set
        node_set.add(temp)

        # Move to the next node
        temp = temp.next

    # Step 3: If the list is successfully
    # traversed without a loop, return False
    return None

def first_node_optimal(head):
    # Initialize a slow and fast
    # pointers to the head of the list
    slow = head
    fast = head

    # Phase 1: Detect the loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next

        # Move fast two steps
        fast = fast.next.next

        # If slow and fast meet,
        # a loop is detected
        if slow == fast:
            # Reset the slow pointer
            # to the head of the list
            slow = head

            # Phase 2: Find the first
            # node of the loop
            while slow != fast:
                # Move slow and fast one
                # step at a time
                slow = slow.next
                fast = fast.next

                # When slow and fast meet again,
                # it's the first node of the loop
            return slow

    # If no loop is found, return None
    return None


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
    print("Loop detected in the linked list at point:", detect_loop_brute(head).data)
    loop_start_node = first_node_optimal(head)
    if loop_start_node:
        print("Loop detected. Starting node of the loop is:", loop_start_node.data)
    else:
        print("No loop detected in the linked list.")