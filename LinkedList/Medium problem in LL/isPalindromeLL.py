from collections import deque
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def isPalindrome_brute(head):
    # Create an empty deque
    # to store values
    st = deque()

    # Initialize a temporary pointer
    # to the head of the linked list
    temp = head

    # Traverse the linked list and
    # push values onto the deque
    while temp is not None:
        # Push the data from the
        # current node onto the deque
        st.append(temp.data)

        # Move to the next node
        temp = temp.next

    # Reset the temporary pointer back
    # to the head of the linked list
    temp = head

    # Compare values by popping from the deque
    # and checking against linked list nodes
    while temp is not None:
        if temp.data != st.pop():
            # If values don't match,
            # it's not a palindrome
            return False

        # Move to the next node
        # in the linked list
        temp = temp.next

    # If all values match,
    # it's a palindrome
    return True

    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Function to reverse linked list
# using recursion approach
def reverse_linked_list(head):
    # Check if the list is empty
    # or has only one node
    if head is None or head.next is None:
        
        # No change is needed;
        # return the current head
        return head

    # Recursive step: Reverse the remaining part
    # of the list and obtain the new head
    new_head = reverse_linked_list(head.next)

    # Store the next node in 'front' to reverse the link
    front = head.next

    # Update the 'next' pointer of 'front' to 
    # point to the current head, effectively
    # reversing the link direction
    front.next = head

    # Set the 'next' pointer of the current
    # head to 'None' to break the original link
    head.next = None

    # Return the new head obtained
    # from the recursion
    return new_head
    
def is_palindrome_optimal(head):
    # Check if the linked list is empty
    # or has only one node
    if head is None or head.next is None:
        # It's a palindrome by definition
        return True

    # Initialize two pointers, slow and fast,
    # to find the middle of the linked list
    slow = head
    fast = head

    # Traverse the linked list to find the
    # middle using slow and fast pointers
    while fast.next is not None and fast.next.next is not None:
        # Move slow pointer one step at a time
        slow = slow.next

        # Move fast pointer two steps at a time
        fast = fast.next.next

    # Reverse the second half of the
    # linked list starting from the middle
    new_head = reverse_linked_list(slow.next)

    # Pointer to the first half
    first = head

    # Pointer to the reversed second half
    second = new_head
    while second is not None:
        # Compare data values of
        # nodes from both halves

        # If values do not match,
        # the list is not a palindrome
        if first.data != second.data:
            # Reverse the second half
            # back to its original state
            reverse_linked_list(new_head)
            # Not a palindrome
            return False

        # Move the first pointer
        first = first.next

        # Move the second pointer
        second = second.next

    # Reverse the second half
    # back to its original state
    reverse_linked_list(new_head)

    # The linked list is a palindrome
    return True
    
# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    # Create a linked list with
    # values 1, 5, 2, 5, and 1 (15251, a palindrome)
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    # Print the original linked list
    print("Original Linked List: ", end="")
    print_linked_list(head)
    if isPalindrome_brute(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")


    # Check if the linked list is a palindrome
    if is_palindrome_optimal(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()