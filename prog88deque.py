#Write a Python program to simulate a queue using deque.
from collections import deque
queue = deque()
queue.append("Rahul")
queue.append("Amit")
queue.append("Rohan")
print("Queue =", queue)
print("Deleted =", queue.popleft())
print("Queue After Deletion =", queue) 