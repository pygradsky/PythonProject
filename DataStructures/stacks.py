class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = Stack()

# Push
stack.push(97)
stack.push(3.14)
stack.push("Bee")
print("Stack: ", stack.stack)

# Peek
top_element = stack.peek()
print("Peek:", top_element)

# pop
popped_element = stack.pop()
print("Popped element:", popped_element)

# Stack after pop
print("Stack after popping:", stack.stack)

# is_empty
is_empty = not bool(stack)
print("is_empty:", is_empty)

# Size
print("Size:", stack.size())
