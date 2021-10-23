# PROGRAM TO REVERSE A LINKED LIST
# ----------------------------------
# At first current is head, prev and ref are Null.
# -----------------------------------
# We have to traverse through the Link, till the current reaches None, then exit the loop.
# ------------------------------------
# first the next jumps to  current.ref.
# -------------------------------------
# Second the current.ref points back to prev which is at Null.
# --------------------------------------
# Third the prev moves to current from Null.
# --------------------------------------
# Then the current pointer moves towards the next pointer
# ---------------------------------------
# When current finally reaches the Null, it exits out of the loop and
# and then the head is assigned to the place where the prev pointer is resting
# at the end of the loop.
# --------------------------------------

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

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print(self):
        if self.head is None:
            print("The Ll is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.next


LL1 = LinkedList()
LL1.push(10)
LL1.push(20)
LL1.push(30)
LL1.push(40)
LL1.push(50)
LL1.reverse()
LL1.print()
