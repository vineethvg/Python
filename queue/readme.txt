# First in First out
# The least recently added item is removed from the queue
1) Enqueue - Adds the item to the queue | Time Comp : O(1)
2) Dequeue - Removes item from the queue | Time Comp : O(1)
3) Front - Get the front item from the queue | Time Comp : O(1)
4) Rear - Get the last item from the queue | Time Comp : O(1)

---------------------------------------------------------------

# Ways to implement queue in python

1) list
2) collections.dequeue
3) queue.Queue

---------------------------------------------------------------

Applications of queue are :
1) FIFO like BFS
2) When a resource is shared among multiple comsumers
   like CPU Scheduling, Disk Scheduling
3) When dat ais shared asynchronously bewtween two process
   Ex: IO buffers,pipes,file IO
4) In operating systems:
   a) Semaphores
       b) FCFS ( first come first serve) scheduling, example: FIFO queue
       c) Spooling in printers
       d) Buffer for devices like keyboard
5) In Networks:
       a) Queues in routers/ switches 
       b) Mail Queues

---------------------------------------------------------------

How to implement priority queue?

# Using Array: A simple implementation is to use array of following structure.
  1)insert() operation can be implemented by adding an item at end of array in O(1) time.
  2)getHighestPriority() operation can be implemented by linearly searching the highest priority item in array. 
    This operation takes O(n) time.
  3)deleteHighestPriority() operation can be implemented by first linearly searching an item, 
    then removing the item by moving all subsequent items one position back.

# We can also use Linked List, time complexity of all operations with linked list remains same as array. 
  The advantage with linked list is deleteHighestPriority() can be more efficient as we don’t have to move items.

# Using Heaps:
  Heap is generally preferred for priority queue implementation because heaps provide better performance compared arrays or linked list. 
  In a Binary Heap, 
  1)getHighestPriority() can be implemented in O(1) time, 
  2)insert() can be implemented in O(Logn) time and 
  3)deleteHighestPriority() can also be implemented in O(Logn) time.
# With Fibonacci heap, insert() and getHighestPriority() can be implemented in O(1) amortized time 
  and deleteHighestPriority() can be implemented in O(Logn) amortized time.

Applications of Priority Queue:
1) CPU Scheduling
2) Graph algorithms like Dijkstra’s shortest path algorithm, Prim’s Minimum Spanning Tree, etc
3) All queue applications where priority is involved.

----------------------------------------------------------------