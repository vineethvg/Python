# detect length of loop in ll
# Floyd's Cycle detection algorithm


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def printLL(self):
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
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def createLoop(self, N):
        LoopNode = self.head

        for _ in range(1, N):
            LoopNode = LoopNode.next
        end = self.head
        while end.next is not None:
            end = end.next
        end.next = LoopNode

    def detectLoop(self):
        if self.head is None:
            print("The list is empty")

        slow = self.head
        fast = self.head
        flag = 0

        while(slow and slow.next and fast and fast.next and fast.next.next):
            if slow == fast and flag != 0:
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                return count

            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0


l = LinkedList()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.push(50)


# l.printLL()
l.createLoop(2)
x = l.detectLoop()
print(str(x))
