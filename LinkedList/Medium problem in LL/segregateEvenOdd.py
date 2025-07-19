class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_last(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self, node):
        while node:
            print(f"{node.val} --> ", end="")
            node = node.next
        print("null")

    # Brute-force approach: collect values and reassign
    def segregate_even_odd_brute(self):
        if self.head is None:
            return None

        values = []
        temp = self.head

        # Collect even values first
        while temp:
            if temp.val % 2 == 0:
                values.append(temp.val)
            temp = temp.next

        # Then collect odd values
        temp = self.head
        while temp:
            if temp.val % 2 != 0:
                values.append(temp.val)
            temp = temp.next

        # Replace values in the original list
        temp = self.head
        idx = 0
        while temp:
            temp.val = values[idx]
            idx += 1
            temp = temp.next

        return self.head

    # Optimal approach: create two separate lists and merge
    def segregate_even_odd_optimal(self):
        odd_head = odd_tail = ListNode(-1)
        even_head = even_tail = ListNode(-1)
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = None
            if curr.val % 2 == 0:
                even_tail.next = curr
                even_tail = curr
            else:
                odd_tail.next = curr
                odd_tail = curr
            curr = next_node

        # Combine even and odd lists
        even_tail.next = odd_head.next
        self.head = even_head.next
        return self.head


# Testing the implementation
ll = LinkedList()
for val in [1, 2, 3, 4]:
    ll.insert_at_last(val)

print("Initial Linked List:")
ll.print_list(ll.head)

print("\nAfter Brute Force Segregation:")
ll.segregate_even_odd_brute()
ll.print_list(ll.head)

# Rebuilding the list again before optimal since original was mutated
ll = LinkedList()
for val in [1, 2, 3, 4]:
    ll.insert_at_last(val)

print("\nAfter Optimal Segregation:")
ll.segregate_even_odd_optimal()
ll.print_list(ll.head)
