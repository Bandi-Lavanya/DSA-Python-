class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def merge_lists_brute(list1, list2):
    arr = []
    # Convert list1 to array
    current = list1
    while current:
        arr.append(current.val)
        current = current.next
    # Convert list2 to array
    current = list2
    while current:
        arr.append(current.val)
        current = current.next
    # Sort combined array
    arr.sort()
    # Convert array back to linked list
    return array_to_linked_list(arr)


def merge_lists_optimal(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next


list1 = array_to_linked_list([1, 2, 4])
list2 = array_to_linked_list([1, 3, 4])

print("Brute Force Merge:")
merged_brute = merge_lists_brute(list1, list2)
print_linked_list(merged_brute)

# Re-create input lists because merge alters them
list1 = array_to_linked_list([1, 2, 4])
list2 = array_to_linked_list([1, 3, 4])

print("Optimal Merge:")
merged_optimal = merge_lists_optimal(list1, list2)
print_linked_list(merged_optimal)
