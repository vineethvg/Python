class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("The Ll is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    # =========================================================================================================================

    # ADD AT THE BEGINNING
    # ---------------------
    # create a new node using the Node Class then pass the data.
    # ----------------------
    # assign the new nodes's link to head of the first node.
    # -----------------------
    # assign the head to the new node.
    # ------------------------

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # ===========================================================================================================================

    # ADD AT THE END
    # -----------------
    # create a new node then pass data.
    # ---------------------
    # check whether the LL is empty or not.
    # ---------------------
    # if its empty, then the added node is the first node hence we have to
    # point the head to the newly created node.
    # ---------------------
    # if its not empty, we have to go to last node
    # take a variable , assign it to head, then traverse until n.ref is None/Null
    # under while execute the condition.
    # ----------------------
    # after the condition is satisfied, we have to change the ref pointing to none/
    # null to new node.
    # ---------------------

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # ============================================================================================================================

    # ADD IN THE MIDDLE
    # ---------------
    # ADD BEFORE THE EXISTING NODE
    # ---------------
    # have to check whether we are adding at first or the remaining positions
    # ---------------------
    # adding at first, create a node, store the ref of head and store the ref of new node to first node
    # ---------------------
    # if u have to add to the middle nodes, first we hahve to go to previous nodes,
    # then have to add new node after the prevous node.
    # --------------------
    # to identify prev node, check the ref of prev node,the prev.ref.data is equal to x
    # ---------------
    # first take n , n = self.head, check the next node if equal to n, i,e prev.ref.data = x,
    # if not go to next node, n=n.ref.
    # --------------------
    # condition to traverse, when n.ref is none then it should exit the loop
    # ---------------------

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # =============================================================================================================================

    # ADD AFTER THE EXISTING NODE
    # ---------------------------
    # first find the node where u wanna insert a new node.
    # ----------------------------
    # take the head as n and traverse until it reaches the end.
    # -----------------------------
    # if n.data is equal to x, break out of the loop, and if not found, increment the n.ref value
    # to move further across the linked list
    # ----------------------------
    # Now u have found the value of x, you know where to insert the node.
    # Check whether the node is null or not.
    # ------------------------------
    # if so print that node doesnt exist
    # or create a new node , give the n.ref to new node.ref and the prev n.ref should have new node value
    # -------------------------------

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref

        if n is None:
            print("The node is not present")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # ==============================================================================================================================
    # DELETE FROM THE BEGINNING
    # --------------------------
    # First check if the list is empty.
    # --------------------------
    # If not then link the head of first node to the ref of the next node
    # ---------------------------

    def delete_begin(self):
        if self.head is None:
            print("The list is empty")
            return
        else:
            self.head = self.head.ref

    # ==============================================================================================================================
    # DELETE AT THE END
    # ------------------
    # First check if the list is empty
    # ------------------
    # If not then traverse till you reach the last node, that too you have to approach through the ref or the
    # link of the last node, increment with n=n.ref
    # --------------------
    # When you reach the last node whose ref is none, then u stop and exit the loop and assign the previous node ref to None
    # -----------------------------------

    def delete_end(self):
        if self.head is None:
            print("The list is empty")
            return
        elif self.head.ref is None:
            self.head is None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    # ===============================================================================================================================
    # DELETION BY VALUE
    # --------------------------
    # Check linked list is empty or not
    # --------------------------
    # If not , check whether the node is first node
    # --------------------------
    # If so then compare value of user key to first node data, if true then delete it
    # by assigning the head to next node ref.
    # --------------------------
    # Deleting from the middle, have to consider the previous node
    # ---------------------------
    # Take head as n, then inc n.ref until it reaches the end i,e n.ref is None, if n.ref.data == x, if true, delete it
    # ----------------------------

    def del_val(self, x):
        if self.head is None:
            print("The LL is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("The node doesnt exist")
        else:
            n.ref = n.ref.ref

    # ===============================================================================================================================
    # DELETING THE WHOLE LIST

    def deleteList(self):
        n = self.head
        while n is not None:
            prev = n.ref
            del n.data
            n = prev
    # ==================================================================
    # GETTING THE COUNT OF THE NODES

    def getCount(self):
        n = self.head
        cnt = 0

        while n is not None:
            cnt += 1
            n = n.ref
        return cnt

    # ===============================================================================================================================
    # SEARCHING THE LIST

    def search(self, x):
        n = self.head

        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(30)
LL1.add_end(40)
LL1.add_before(100, 30)
LL1.add_after(200, 40)
print(LL1.search(20))
LL1.print_LL()
print()
print(LL1.getCount())

# LL1.delete_begin()
# LL1.delete_end()
# LL1.del_val(50)
LL1.deleteList()
print("The List is deleted")
