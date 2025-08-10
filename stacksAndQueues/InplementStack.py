class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Add an element to the top of the stack."""
        self.stack.append(value)
        print(f"Pushed {value} into stack.")

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.stack.pop()

    def top(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.stack)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.top())   # 30
print("Popped element:", s.pop()) # 30
print("Stack size:", s.size())   # 2
