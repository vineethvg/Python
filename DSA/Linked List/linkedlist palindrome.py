class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printLL(self):
        if self.head is None:
            print("The List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end="")
                n = n.next

    def isPalindrome(self):
        slow = self.head
        stack = []
        ispalin = True

        while slow != None:
            stack.append(slow.data)
            slow = slow.next

        while self.head != None:
            i = stack.pop()
            if self.head.data == i:
                ispalin = True
            else:
                ispalin = False
                break
            self.head = self.head.next
        return ispalin


LL1 = LinkedList()
LL1.push(10)
LL1.push(20)
LL1.push(20)
LL1.push(40)
LL1.printLL()
print()
print(LL1.isPalindrome())
