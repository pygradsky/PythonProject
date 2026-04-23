class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items[-1]


queue = Queue()

# Enqueue
queue.enqueue("Hello, world!")
queue.enqueue(3.14)
queue.enqueue(False)

# Queue
print(queue.items)

# Peek
print("Peek:", queue.peek())

# Pop
print("Removed element:", queue.dequeue())
print("Removed element:", queue.dequeue())

# Queue after dequeue
print("Queue after dequeue:", queue.items)
