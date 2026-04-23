stack = []

# Push
stack.append(97)
stack.append(3.14)
stack.append("Bee")
print("Stack: ", stack)

# Peek
top_element = stack[-1]
print("Peek:", top_element)

# pop
popped_element = stack.pop()
print("Popped element:", popped_element)

# Stack after pop
print("Stack after popping:", stack)

# is_empty
is_empty = not bool(stack)
print("is_empty:", is_empty)

# Size
print("Size:", len(stack))
