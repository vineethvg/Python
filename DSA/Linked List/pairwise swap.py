class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def printLL(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pairSwap(self):
        n = self.head

        if n is None:
            return

        while n and n.next is not None:
            if(n.data != n.next.data):
                n.data, n.next.data = n.next.data, n.data

            n = n.next.next


ll = LinkedList()
ll.push(60)
ll.push(50)
ll.push(40)
ll.push(30)
ll.push(20)
ll.push(10)

ll.printLL()
print()
ll.pairSwap()
ll.printLL()
