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
        new_node.next = self.head
        self.head = new_node

    def del_val(self, x):
        if self.head is None:
            print("The List is empty")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("The Node doesnt exist")
        else:
            n.next = n.next.next

    def removeDuplicateSorted(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head

    def removeDuplicateUnSorted(self, head):
        if self.head is None or self.head.next is None:
            return head

        hash = set()
        current = head
        hash.add(self.head.data)

        while current.next is not None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head


ll = LinkedList()
ll.head = Node(23)
ll.push(10)
ll.push(13)
ll.push(23)
ll.push(23)
ll.push(13)
ll.push(10)
ll.printLL()
print()
ll.removeDuplicateUnSorted(ll.head)
ll.printLL()
