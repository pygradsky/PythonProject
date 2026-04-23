class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node("Hello, there!")
second_node = Node("Goodbye!")

first_node.next = second_node
print(first_node.next.data)
