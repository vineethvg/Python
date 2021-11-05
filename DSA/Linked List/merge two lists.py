class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


def mergeList(headA, headB):
    d_Node = Node(0)
    tail = d_Node

    while True:

        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        tail = tail.next
    return d_Node


ll1 = LinkedList()
ll2 = LinkedList()
ll3 = LinkedList()

ll1.push(5)
ll1.push(10)
ll1.push(15)
ll1.print()
print("")

ll2.push(2)
ll2.push(3)
ll2.push(20)
ll2.print()
print("")

ll1.head = mergeList(ll1.head, ll2.head)
ll1.print()
