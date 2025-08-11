class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front = None  # Points to the first element
        self.rear = None   # Points to the last element
        self._size = 0

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        new_node = Node(value)
        if self.rear is None:
            # If queue is empty, both front and rear are same
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        print(f"Enqueued {value} into queue.")

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_value = self.front.data
        self.front = self.front.next
        # If queue becomes empty, reset rear too
        if self.front is None:
            self.rear = None
        self._size -= 1
        return dequeued_value

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def size(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None


# Example usage
q = QueueLinkedList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front element:", q.peek())     # 10
print("Dequeued element:", q.dequeue()) # 10
print("Front after dequeue:", q.peek()) # 20
print("Size:", q.size())               # 2
