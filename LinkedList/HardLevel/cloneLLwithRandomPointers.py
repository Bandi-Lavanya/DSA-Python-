'''Original Linked List with Random Pointers:
Data: 7, Random: 21
Data: 14, Random: 7
Data: 21, Random: 28
Data: 28, Random: 14

Brute Force Cloned List:
Data: 7, Random: 21
Data: 14, Random: 7
Data: 21, Random: 28
Data: 28, Random: 14

Optimal Cloned List:
Data: 7, Random: 21
Data: 14, Random: 7
Data: 21, Random: 28
Data: 28, Random: 14'''

class Node:
    def __init__(self, x, nextNode=None, randomNode=None):
        self.data = x
        self.next = nextNode
        self.random = randomNode


# Brute force approach using HashMap
def cloneLL_brute(head):
    if not head:
        return None

    temp = head
    node_map = {}

    # Step 1: Create copies and map original → clone
    while temp:
        node_map[temp] = Node(temp.data)
        temp = temp.next

    # Step 2: Assign next and random pointers
    temp = head
    while temp:
        node_map[temp].next = node_map.get(temp.next)
        node_map[temp].random = node_map.get(temp.random)
        temp = temp.next

    return node_map[head]


# Optimal approach without using extra space
def insertCopyInBetween(head):
    temp = head
    while temp:
        copy = Node(temp.data)
        copy.next = temp.next
        temp.next = copy
        temp = copy.next

def connectRandomPointers(head):
    temp = head
    while temp:
        if temp.random:
            temp.next.random = temp.random.next
        temp = temp.next.next

def getDeepCopyList(head):
    dummy = Node(-1)
    copy_tail = dummy
    temp = head
    while temp:
        copy = temp.next
        copy_tail.next = copy
        copy_tail = copy
        temp.next = copy.next  # restore original
        temp = temp.next
    return dummy.next

def cloneLL_optimal(head):
    if not head:
        return None
    insertCopyInBetween(head)
    connectRandomPointers(head)
    return getDeepCopyList(head)


def printClonedLinkedList(head):
    while head:
        rand_val = head.random.data if head.random else "None"
        print(f"Data: {head.data}, Random: {rand_val}")
        head = head.next


# Helper to create sample list with random pointers
def create_sample_list():
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    # Assigning random pointers
    head.random = head.next.next         # 7 → 21
    head.next.random = head              # 14 → 7
    head.next.next.random = head.next.next.next  # 21 → 28
    head.next.next.next.random = head.next       # 28 → 14
    return head


# Driver Code
if __name__ == "__main__":
    print("Original Linked List with Random Pointers:")
    head = create_sample_list()
    printClonedLinkedList(head)

    print("\nBrute Force Cloned List:")
    clonedList_brute = cloneLL_brute(head)
    printClonedLinkedList(clonedList_brute)

    print("\nOptimal Cloned List:")
    head = create_sample_list()  # Rebuild as optimal modifies it
    clonedList_optimal = cloneLL_optimal(head)
    printClonedLinkedList(clonedList_optimal)
