'''Original linked list:
5 -> 14
10 -> 4
12 -> 20 -> 13
7 -> 17
Flattened linked list: 
4 5 7 10 12 13 14 17 20 
Original linked list:
5 -> 14
10 -> 4
12 -> 20 -> 13
7 -> 17
Flattened linked list:
5 7 10 4 12 14 17 20 13'''
class Node:
    def __init__(self, x=None, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

# Function to convert a list to a linked list
def convertArrToLinkedList(arr):
    # Create a dummy node to serve as
    # the head of the linked list
    dummyNode = Node(-1)
    temp = dummyNode

    # Iterate through the list and
    # create nodes with list elements
    for val in arr:
        # Create a new node with the list element
        temp.child = Node(val)
        # Move the temporary pointer
        # to the newly created node
        temp = temp.child

    # Return the linked list starting
    # from the next of the dummy node
    return dummyNode.child

# Function to flatten a linked list with child pointers
def flattenLinkedList_brute(head):
    arr = []

    # Traverse through the linked list
    while head:
        # Traverse through the child
        # nodes of each head node
        t2 = head
        while t2:
            # Store each node's data in the list
            arr.append(t2.data)
            # Move to the next child node
            t2 = t2.child
        # Move to the next head node
        head = head.next

    # Sort the list containing
    # node values in ascending order
    arr.sort()

    # Convert the sorted list
    # back to a linked list
    return convertArrToLinkedList(arr)

# Merges two linked lists in a particular
# order based on the data value
def merge(list1, list2):
    # Create a dummy node as a
    # placeholder for the result
    dummyNode = Node(-1)
    res = dummyNode

    # Merge the lists based on data values
    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        res.next = None

    # Connect the remaining
    # elements if any
    if list1:
        res.child = list1
    else:
        res.child = list2

    # Break the last node's
    # link to prevent cycles
    if dummyNode.child:
        dummyNode.child.next = None

    return dummyNode.child

# Flattens a linked list with child pointers
def flattenLinkedList_optimal(head):
    # If head is null or there 
    # is no next node, return head
    if not head or not head.next:
        return head

    # Recursively flatten the
    # rest of the linked list
    mergedHead = flattenLinkedList_optimal(head.next)
    head = merge(head, mergedHead)
    return head

# Print the linked list by
# traversing through child pointers
def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()

# Print the linked list
# in a grid-like structure
def printOriginalLinkedList(head, depth=0):
    while head:
        print(head.data, end="")

        # If child exists, recursively
        # print it with indentation
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars
        # for each level in the grid
        if head.next:
            print()
            print("| " * depth, end="")

        head = head.next

# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList_brute(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)
# Create a linked list with child pointers
head = Node(5)
head.child = Node(14)

head.next = Node(10)
head.next.child = Node(4)

head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)

head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

# Print the original
# linked list structure
print("Original linked list:")
printOriginalLinkedList(head)

# Flatten the linked list
# and print the flattened list
flattened = flattenLinkedList_optimal(head)
print("\nFlattened linked list: ")
printLinkedList(flattened)