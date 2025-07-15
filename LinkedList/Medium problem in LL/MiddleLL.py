
class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data       
        # Pointer to the next node in the list
        self.next = next_node  

# Function to find the middle 
# node of a linked list
def find_middle_brute(head):
    # If the list is empty or has only 
    # one element, return the head
    # as it's the middle.
    if head is None or head.next is None:
        return head

    temp = head
    count = 0

    # Count the number of nodes
    # in the linked list.
    while temp is not None:
        count += 1
        temp = temp.next

    # Calculate the position of
    # the middle node.
    mid = count // 2 + 1
    temp = head

    # Traverse to the middle node by
    # moving temp to the middle position.
    while temp is not None:
        mid = mid -1

        # Check if the middle position is reached.
        if mid == 0:
           # break out of the loop
           # to return temp
            break
        
        # Move temp ahead
        temp = temp.next


    # Return the middle node.
    return temp

def find_middle_optimal(head):
    # Initialize the slow pointer to the head.
    slow = head   
    
    # Initialize the fast pointer to the head.
    fast = head   

    # Traverse the linked list using
    # the Tortoise and Hare algorithm.
    while fast and fast.next and slow:
        # Move fast two steps.
        fast = fast.next.next 
        # Move slow one step.
        slow = slow.next       

    # Return the slow pointer,
    # which is now at the middle node.
    return slow  

# Creating a sample linked list: 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle node
middle_node1 = find_middle_brute(head)
middle_node2 = find_middle_optimal(head)
# Display the value of the middle node
print("The middle node value is:", middle_node1.data)
print("The middle node value is:", middle_node2.data)
                                
                            