# detect loop in a linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        n = self.head
        while(n):
            print(n.data, end=" ")
            n = n.next

    def detectLoop(self):
        s = set()
        n = self.head
        while(n):

            if(n in s):
                return True  # the loop exists

            # if not then it means that we have to move on to the next node
            s.add(n)
            n = n.next

        return False


LL1 = LinkedList()
LL1.add(10)
LL1.add(20)
LL1.add(4)
LL1.add(15)

#LL1.head.next.next.next.next = LL1.head

if(LL1.detectLoop()):
    print("Loop Found")
else:
    print("No Loop")
