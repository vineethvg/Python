from collections import deque
import collections

de = collections.deque([1, 2, 3])

de.append(4)
print("queue after appending right: ")
print(de)

de.appendleft(6)
print("queue after appending on the left: ")
print(de)

de.pop()
print("The deque after deleting from right:")
print(de)

de.popleft()
print("The deque after popping froom the left is: ")
print(de)

de.extend([4, 5, 6])
print("the deque after extending at right is: ")
print(de)

de.extendleft([7, 8, 9])
print("The deque after extending deque at beginning is: ")
print(de)

de.rotate(-3)
print(de)

de.reverse()
print(de)
