'''Original Linked List: 3 2 5 4 1 
Sorted Linked List: 1 2 3 4 5
Original Linked List: 3 2 5 4 1
Sorted Linked List: 1 2 3 4 5'''
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        
        # Pointer to the next node in the list
        self.next = next1

def sort_LL_brute(head):
    # Create a list to
    # store node values
    arr = []
    
    # Temporary pointer to
    # traverse the linked list
    temp = head
    
    # Traverse the linked list and
    # store node values in the list
    while temp is not None:
        arr.append(temp.data)
        temp = temp.next
    
    # Sort the list
    # containing node values
    arr.sort()
    
    # Reassign sorted values to
    # the linked list nodes
    temp = head
    for i in range(len(arr)):
        # Update the node's data
        # with the sorted values
        temp.data = arr[i]
        # Move to the next node
        temp = temp.next
    
    # Return the head of the
    # sorted linked list
    return head

# Function to merge two sorted linked lists
def mergeTwoSortedLinkedLists(list1, list2):
    # Create a dummy node to serve
    # as the head of the merged list
    dummyNode = Node(-1)
    temp = dummyNode

    # Traverse both lists simultaneously
    while list1 is not None and list2 is not None:
        # Compare elements of both lists and
        # link the smaller node to the merged list
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        # Move the temporary pointer
        # to the next node
        temp = temp.next 

    # If any list still has remaining
    # elements, append them to the merged list
    if list1 is not None:
        temp.next = list1
    else:
        temp.next = list2
    
    # Return the merged list starting 
    # from the next of the dummy node
    return dummyNode.next

# Function to find the middle of a linked list
def findMiddle(head):
    # If the list is empty or has only one node
    # the middle is the head itself
    if head is None or head.next is None:
        return head

    # Initializing slow and fast pointers
    slow = head
    fast = head.next

    # Move the fast pointer twice as
    # fast as the slow pointer

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    # When the fast pointer reaches the end,
    # the slow pointer will be at the middle

    return slow

# Function to perform merge sort on a linked list
def sortLL_optimal(head):
    # Base case: if the list is empty
    # or has only one node it is already 
    # sorted, so return the head
    if head is None or head.next is None:
        return head

    # Find the middle of the list
    # using the findMiddle function
    middle = findMiddle(head)

    # Divide the list into two halves
    right = middle.next
    middle.next = None
    left = head

    # Recursively sort the left and right halves
    left = sortLL_optimal(left)
    right = sortLL_optimal(right)

    # Merge the sorted halves using
    # the mergeTwoSortedLinkedLists function
    return mergeTwoSortedLinkedLists(left, right)

# Function to print the linked list
def printLinkedList(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Linked List: 3 2 5 4 1
head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)

print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sortLL_optimal(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)

head = Node(3)
head.next = Node(2)
head.next.next = Node(5)
head.next.next.next = Node(4)
head.next.next.next.next = Node(1)


print("Original Linked List: ", end="")
printLinkedList(head)

# Sort the linked list
head = sort_LL_brute(head)

print("Sorted Linked List: ", end="")
printLinkedList(head)