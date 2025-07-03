
class Node:
    def __init__(self, data, next_node=None, back_node=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node
        # in the list (forward direction)
        self.next = next_node
        # Reference to the previous node
        # in the list (backward direction)
        self.back = back_node

def convert_arr_to_dll(arr):
    # Create the head node with
    # the first element of the array
    head = Node(arr[0])
    # Initialize 'prev' to the head node
    prev = head

    for i in range(1, len(arr)):
        # Create a new node with data from the
        # array and set its 'back' pointer
        # to the previous node
        temp = Node(arr[i], None, prev)
        
        # Update the 'next' pointer of the
        # previous node to point to the new node
        prev.next = temp
        # Move 'prev' to the newly created 
        # node for the next iteration
        prev = temp

    # Return the head of the doubly linked list
    return head

def print_dll(head):
    while head is not None:
        # Print the data in the current node
        print(head.data, end=" ")
        # Move to the next node
        head = head.next
    print()

# Function to reverse the
# linked list using a stack
def reverse_linked_list(head):
    # Create a temporary pointer
    # to traverse the linked list
    temp = head  
    
    # Create a stack to temporarily
    # store the data values
    stack = []   

    # Step 1: Push the values of the
    # linked list onto the stack
    while temp is not None:
        # Push the current node's
        # data onto the stack
        stack.append(temp.data) 
        # Move to the next node
        # in the linked list
        temp = temp.next        

    # Reset the temporary pointer
    # to the head of the linked list
    temp = head  

    # Step 2: Pop values from the stack
    # and update the linked list
    while temp is not None:
        
        # Set the current node's data to
        # the value at the top of the stack
        temp.data = stack.pop()  
        
         # Move to the next node in
         # the linked list
        temp = temp.next        

    # Return the new head of
    # the reversed linked list
    return head

def reverse_dll(head):
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        # No change is needed;
        # return the current head
        return head
    
    # Initialize a pointer to
    # the previous node
    prev = None  
    
    # Initialize a pointer
    # to the current node
    current = head  

    # Traverse the linked list
    while current is not None:
        
        # Store a reference to
        # the previous node
        prev = current.back 

        # Swap the previous and next pointers
        current.back = current.next
        
         # This step reverses the links
        current.next = prev 
        
        # Move to the next node
        # in the original list
        current = current.back  

    # The final node in the original list
    # becomes the new head after reversal
    return prev.back

# Example usage:
arr = [12, 5, 6, 8, 4]
# Convert the array to a
# doubly linked list
head = convert_arr_to_dll(arr)
# Print the doubly linked list
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')

# Reverse the doubly linked list
head = reverse_dll(head)
# Print the reversed doubly linked list
print_dll(head)
print('Doubly Linked List Initially:  ')
print_dll(head)

print('Doubly Linked List After Reversing :')

# Reverse the doubly linked list
head = reverse_linked_list(head)
# Print the reversed doubly linked list
print_dll(head)

