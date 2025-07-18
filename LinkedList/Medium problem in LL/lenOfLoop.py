'''Loop detected. Starting node of the loop is: 2
Length of the loop is: 4
Loop detected. Length of the loop is: 4'''
# Node class represents a node in a linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data  
        self.next = next_node 

# Brute Force Approach
# Function to detect a loop and return the starting node of the loop using hashmap
def detect_loop_brute(head):
    temp = head
    node_map = {}

    while temp:
        if temp in node_map:
            return temp  # Loop detected
        node_map[temp] = True
        temp = temp.next

    return None  # No loop detected

# Function to find the length of the loop using brute force (from starting node)
def loop_length_brute(start_node):
    count = 1
    temp = start_node.next
    while temp != start_node:
        count += 1
        temp = temp.next
    return count

# Optimal Approach (Floyd's Cycle Detection)
# Helper function to count loop length once loop is detected
def find_length_optimal(slow, fast):
    cnt = 1
    fast = fast.next
    while slow != fast:
        cnt += 1
        fast = fast.next
    return cnt

# Function to detect loop and return loop length using Floyd's algorithm
def length_of_loop_optimal(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return find_length_optimal(slow, fast)
    return 0


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
node5.next = node2  # Creating the loop (5 → 2)

head = node1

# Brute Force Method
loop_start_node = detect_loop_brute(head)
if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
    print("Length of the loop is:", loop_length_brute(loop_start_node))
else:
    print("No loop detected in the linked list.")

# Optimal Method
loop_len = length_of_loop_optimal(head)
if loop_len:
    print("Loop detected. Length of the loop is:", loop_len)
else:
    print("No loop detected in the linked list.")
