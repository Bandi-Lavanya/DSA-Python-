class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_linked_list_brute_force(head):
    count = [0, 0, 0]
    current = head

    # Count 0s, 1s, and 2s
    while current:
        count[current.val] += 1
        current = current.next

    # Overwrite values in order
    current = head
    for i in range(3):
        while count[i] > 0:
            current.val = i
            current = current.next
            count[i] -= 1

    return head


def sort_linked_list_optimal(head):
    zeroD = ListNode(0)
    oneD = ListNode(0)
    twoD = ListNode(0)

    zero, one, two = zeroD, oneD, twoD
    current = head

    # Distribute nodes into 0s, 1s, and 2s
    while current:
        if current.val == 0:
            zero.next = current
            zero = zero.next
        elif current.val == 1:
            one.next = current
            one = one.next
        else:
            two.next = current
            two = two.next
        current = current.next

    # Connect the lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    return zeroD.next


# ------------------- Helper Functions -------------------
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


if __name__ == "__main__":
    data = [2, 1, 0, 2, 1, 0, 1, 2]
    print("Original List:")
    head = create_linked_list(data)
    print_linked_list(head)

    # Choose one method to test
    print("\nSorted using Brute Force:")
    sorted_head = sort_linked_list_brute_force(create_linked_list(data))  # Fresh copy
    print_linked_list(sorted_head)

    print("\nSorted using Optimal Approach:")
    sorted_head = sort_linked_list_optimal(create_linked_list(data))  # Fresh copy
    print_linked_list(sorted_head)
