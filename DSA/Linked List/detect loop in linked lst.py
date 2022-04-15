# Python3 program to detect loop
# in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):

            if (temp in s):
                return True  # that means the loop exist

            # If we are seeing the node for
            # the first time, insert it in hash
            s.add(temp)
            temp = temp.next

        return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
# llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
    print("Loop found")
else:
    print("No Loop ")
