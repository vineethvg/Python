class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.last = None

    def printCL(self):

        if self.last == None:
            print("The List is empty")
            return
        n = self.last.next

        while n is not None:
            print(n.data, "--->", end="")
            n = n.next
            if n == self.last.next:
                break

# ===================================================================================
    # INSERTION TO AN EMPTY QUEUE
    # Initially the last pointer will be None
    # Create a node...its the one and only node in this case, so its the last node
    # In this case we have created a Node called n
    # The pointer last is pointing to the newly created node n
    # since its a circularQueue the node n points to itself
    def addToEmpty(self, data):

        if self.last != None:
            return self.last

        n = Node(data)  # creation of node
        self.last = n   # last pointer being pointed at node
        self.last.next = self.last  # last pointer's reference pointe back to last
        return self.last
# ===================================================================================
    # INSERTION AT THE BEGINNING

    def addBegin(self, data):
        if(self.last == None):
            return self.addToEmpty(data)

        n = Node(data)
        n.next = self.last.next
        self.last.next = n

        return self.last

# ===================================================================================
    # INSERT AT THE END

    def addEnd(self, data):
        if(self.last == None):
            return self.addToEmpty(data)

        n = Node(data)

        n.next = self.last.next
        self.last.next = n
        self.last = n

        return self.last

# ===================================================================================
    # INSERTION BEWTWEEN THE NODES

    def addAfter(self, data, x):

        if self.last == None:
            return self.addToEmpty(data)

        n = Node(data)

        p = self.last.next

        while p is not None:
            if(p.data == x):
                n.next = p.next
                p.next = n

                if(p == self.last):
                    self.last = n
                    return self.last
                else:
                    return self.last
            p = p.next
            if(p == self.last.next):
                print(x, "not present in the list")
                break

# ===================================================================================


CL = CircularLinkedList()
CL.addBegin(10)
CL.addBegin(20)
CL.addEnd(5)
CL.addAfter(1, 5)
CL.printCL()
