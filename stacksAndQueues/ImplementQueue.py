class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.queue.append(value)
        print(f"Enqueued {value} into queue.")

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)  # O(n) operation for lists

    def front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.front())     # 10
print("Dequeued element:", q.dequeue()) # 10
print("Queue size:", q.size())         # 2
