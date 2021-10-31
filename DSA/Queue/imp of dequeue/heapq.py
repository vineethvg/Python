import heapq


li = [5, 7, 9, 1, 3]
# heapify converts the iterable into a heap data structure
heapq.heapify(li)

print("The created heap is : ", end=" ")
print(list(li))

heapq.heappush(li, 4)
print("The modified heap after push is : ", end="")
print(list(li))

print("The popped and smallest elements is : ", end=" ")
print(heapq.heappop(li))
