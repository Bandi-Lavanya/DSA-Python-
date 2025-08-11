class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []   # For enqueue
        self.stack_out = []  # For dequeue

    def enqueue(self, x):
        """Push element to the end of the queue."""
        self.stack_in.append(x)

    def dequeue(self):
        """Remove the element from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        if not self.stack_out:
            # Transfer all elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def front(self):
        """Get the front element."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def is_empty(self):
        """Check if queue is empty."""
        return not self.stack_in and not self.stack_out

    def size(self):
        """Return the size of the queue."""
        return len(self.stack_in) + len(self.stack_out)


# Example usage
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.front())     # 10
print("Dequeued element:", q.dequeue()) # 10
print("Front after dequeue:", q.front()) # 20
print("Size:", q.size())               # 2
