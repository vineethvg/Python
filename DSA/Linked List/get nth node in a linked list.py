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
            print("The List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def getNth(self, index):
        n = self.head
        cnt = 0
        while n is not None:
            if (cnt == index):
                return n.data
            cnt += 1
            n = n.next
        assert(False)
        return 0


LL = LinkedList()
LL.push(10)
LL.push(20)
LL.push(30)
LL.printLL()
print()
print(LL.getNth(2))
