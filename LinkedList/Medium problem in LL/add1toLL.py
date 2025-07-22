'''Original:
1 -> 9 -> 9 -> None
Brute Force:
2 -> 0 -> 0 -> None
Better (recursion):
2 -> 0 -> 0 -> None
Optimal (reverse list):
2 -> 0 -> 0 -> None'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_one_brute(head):
    # Step 1: Convert to integer
    num = 0
    current = head
    while current:
        num = num * 10 + current.val
        current = current.next

    # Step 2: Add 1
    num += 1

    # Step 3: Convert back to linked list
    dummy = ListNode(0)
    for digit in str(num):
        dummy.next = ListNode(int(digit), dummy.next)

    # Reverse to correct order
    prev = None
    current = dummy.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def add_one_recursive(head):
    # Helper recursive function
    def dfs(node):
        if not node:
            return 1  # Base case: add 1 at the end (least significant digit)
        
        carry = dfs(node.next)
        total = node.val + carry
        node.val = total % 10
        return total // 10  # Return carry

    carry = dfs(head)
    
    # If carry still remains (e.g., 999 -> 1000), we need a new head node
    if carry:
        new_head = ListNode(carry)
        new_head.next = head
        return new_head
    return head


def add_one_optimal(head):
    head = reverse_list(head)

    current = head
    carry = 1
    while current and carry:
        current.val += carry
        carry = current.val // 10
        current.val = current.val % 10
        prev = current
        current = current.next

    # If there's still a carry, add a new node
    if carry:
        prev.next = ListNode(1)

    return reverse_list(head)


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Include the three approaches here...

# Test:
if __name__ == "__main__":
    arr = [1, 9, 9]
    head = create_linked_list(arr)

    print("Original:")
    print_linked_list(head)

    # Brute
    print("Brute Force:")
    print_linked_list(add_one_brute(create_linked_list(arr)))

    # Better
    print("Better (recursion):")
    print_linked_list(add_one_recursive(create_linked_list(arr)))

    # Optimal
    print("Optimal (reverse list):")
    print_linked_list(add_one_optimal(create_linked_list(arr)))
