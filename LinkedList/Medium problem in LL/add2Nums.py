'''List 1:
2 -> 4 -> 3 -> None
List 2:
5 -> 6 -> 4 -> None
Sum List:
7 -> 0 -> 8 -> None'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    temp = dummy
    carry = 0
    
    while l1 or l2 or carry:
        total = 0
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        total += carry
        carry = total // 10
        temp.next = ListNode(total % 10)
        temp = temp.next
    
    return dummy.next

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

# Test:
if __name__ == "__main__":
    arr1 = [2, 4, 3]  # 342
    arr2 = [5, 6, 4]  # 465
    l1 = create_linked_list(arr1)
    l2 = create_linked_list(arr2)

    print("List 1:")
    print_linked_list(l1)

    print("List 2:")
    print_linked_list(l2)

    print("Sum List:")
    result = addTwoNumbers(l1, l2)
    print_linked_list(result)
