from queue import Queue

q = Queue(maxsize=3)

# prints the size of the size
print(q.qsize())

q.put('a')
q.put('b')
q.put('c')
print("Initial queue")
# prints the boolean value whether the queue is full or empty
print("\n", q.full())

print("Elements dequeued from the queue are: ")
print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
