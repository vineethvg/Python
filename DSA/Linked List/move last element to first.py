class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        if self.head is None:
            print("The list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def moveToFront(self):
        tmp = self.head
        sec_last = None

        if not tmp or not tmp.next:
            return

        while tmp and tmp.next is not None:
            sec_last = tmp
            tmp = tmp.next
        sec_last.next = None
        tmp.next = self.head
        self.head = tmp


l = LinkedList()
l.push(10)
l.push(20)
l.push(30)
l.printLL()
l.moveToFront()
print()
l.printLL()
