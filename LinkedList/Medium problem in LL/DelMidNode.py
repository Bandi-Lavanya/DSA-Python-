'''Original Linked List: 1 2 3 4 5 
Updated Linked List: 1 2 4 5 
Original Linked List: 1 2 4 5 
Updated Linked List: 1 2 5 '''

# Node class represents a node in 
# a linked list

class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to delete the
# middle node of a linked list
def delete_middle1(head):
    # Initialize a temporary node
    # to traverse the linked list
    temp = head
    
    # Variable to hold the number
    # of nodes in the linked list
    n = 0
    
    # Loop to count the number of
    # nodes in the linked list
    while temp is not None:
        n += 1
        temp = temp.next
    
    # Calculate the index of the middle node
    res = n // 2
    
    # Reset the temporary node to
    # the beginning of the linked list
    temp = head
    
    # Loop to find the
    # middle node to delete
    while temp is not None:
        res -= 1
        
        # If the middle node is found
        if res == 0:
            
            # Create a pointer
            # to the middle node
            middle = temp.next
            
            # Adjust pointers to
            # skip the middle node
            temp.next = temp.next.next
            
            # Delete the middle node
            # (Python handles memory management)
            # No explicit free() needed
            
            # Exit the loop after
            # deleting the middle node
            break
        
        # Move to the next node
        # in the linked list
        temp = temp.next
    
    # Return the head of the
    # modified linked list
    return head

def delete_middle2(head):
    """
    If the list is empty or has only one node,
    return None as there is no middle node to delete
    """
    if head is None or head.next is None:
        return None

    # Initialize slow and fast pointers
    slow = head
    fast = head.next.next if head.next else None

    # Move 'fast' pointer twice as fast as 'slow'
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node by skipping it
    slow.next = slow.next.next
    return head

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Creating a sample linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

# Deleting the middle node
head = delete_middle1(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
print_linked_list(head)

# Display the original linked list
print("Original Linked List: ", end="")
print_linked_list(head)

# Deleting the middle node
head = delete_middle2(head)

# Displaying the updated linked list
print("Updated Linked List: ", end="")
print_linked_list(head)