from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')
print("initial queue")
print(q)


print("\nelements deqeued from the queue")
print(q.popleft())
# print(q.popleft())
# print(q.popleft())

print("\nQueue after removing elements: ")
print(q)
