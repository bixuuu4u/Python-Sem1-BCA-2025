# Write a program to demonstrate stack and queue operations using a list of numbers.

from collections import deque

# Stack Operations (LIFO)
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushing:", stack)
print("Popped element:", stack.pop())  # Removes last element

# Queue Operations (FIFO)
queue = deque([1, 2, 3])
queue.append(4)
queue.append(5)
print("Queue after enqueue:", list(queue))
print("Dequeued element:", queue.popleft())  # Removes first element

# Final structures
print("Final Stack:", stack)
print("Final Queue:", list(queue))
