queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

print("\nElements dequeued from Queue")
print(queue.pop(0), end=" ")
print(queue.pop(0), end=" ")
# print(queue.pop(0))

print("\nQueue after removing the elements")
print(queue)
