from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        """Push element x onto stack."""
        self.q.append(x)
        # Rotate the queue to bring the new element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        """Removes the element on top of the stack and returns it."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.q.popleft()

    def top(self):
        """Get the top element."""
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.q[0]

    def size(self):
        """Return the size of the stack."""
        return len(self.q)

    def is_empty(self):
        """Returns whether the stack is empty."""
        return len(self.q) == 0
    def print_stack(self):
        """Print the elements in the stack."""
        print("Stack elements:", list(self.q))


# Example usage
s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.top())     # 30
print("Popped element:", s.pop())  # 30
print("Top after pop:", s.top())   # 20
print("Size:", s.size())           # 2
print(s.print_stack())  # Stack elements: [20, 10]