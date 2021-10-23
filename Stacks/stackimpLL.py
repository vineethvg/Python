# Stack implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out = out + str(cur.data) + "-->"
            cur = cur.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):

        if self.IsEmpty():
            raise Exception("Peeking from an empty stack.")
        return self.head.next.data

    def push(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Poping from an empty stack.")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.data


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
