class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None  # Points to the top of the stack
        self._size = 0

    def push(self, value):
        """Add an element to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed {value} into stack.")

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_value

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def size(self):
        """Return the size of the stack."""
        return self._size

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None


# Example usage
s = StackLinkedList()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())     # 30
print("Popped element:", s.pop())   # 30
print("Top after pop:", s.peek())   # 20
print("Size:", s.size())            # 2
