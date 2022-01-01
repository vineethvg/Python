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
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def printMiddle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data


LL = LinkedList()
LL.push(60)
LL.push(50)
LL.push(40)
LL.push(30)
LL.push(20)
# LL.push(10)
LL.printLL()
print()
print(LL.printMiddle())
