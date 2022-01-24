# BST OPERATIONS

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

# ======================================================================
# INSERTION OPERATION
# ---------------------------
# Check whether tree is empty or not
# ---------------------------
# if its empty, then we are inserting the first node
# ---------------------------
# if not empty, then have to find position of new_node, where we have
# to place it (left subtree or rightsubtree)
# ---------------------------
# Deal with duplicate values
# ---------------------------

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:  # if self.lchild exists or not none
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

# =====================================================================

# SEARCH OPERATION
# -------------------------
# first compare root key to data, if equal, print a message
# -------------------------
# compare data with root key, if less then it exists in left sub tree
# or the right sub tree
# -------------------------
# in left sub tree we have two situations
# if left sub tree is empty - print node is present
# if left sub tree has one or more nodes  - perform search operation(recursive method)
# -------------------------

    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    print("Node is not present")
            else:
                if self.rchild:
                    self.rchild.search(data)
                else:
                    print("Node is not present!")

# =======================================================================

# PREORDER TRAVERSAL
# --------------------------
# first visit root,then left then right, thats the order
# --------------------------
# first print root
# ---------------------------
# the print left sub tree
# if the left sub tree is empty, then it will print right sub tree
# ---------------------------

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

# ========================================================================

# INORDER TRAVERSAL
# ---------------------------
# visit left, then root then right node
# ---------------------------
# check whether left st is preset, if not doesnt matter
# if its present inorder method recursively
# ---------------------------
# then print root key
# ---------------------------
# then goes same for right key

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.preorder()

# ========================================================================

# POSTORDER TRAVERSAL
# --------------------------
# visit left, then right then root node
# --------------------------
# if left node exists then call preorder recursively
# ---------------------------
# same goes for right node
# ---------------------------
# then print root

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

# =========================================================================

# DELETION OPERATION
# -------------------------
# check whether tree is empty or not
# if tree is empty, print its empty and exit the deletion operation
# ------------------------
# if not empty then we have to find the given node in the tree
# if present delete the node, if not then print it doesnt exist
# ------------------------
#

    def delete(self, data, curr):
        if self.key is None:
            print("The tree is Empty!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("Given Node is Not present in the Tree")
        elif data > self.key:
            if self.rchild:  # if r.child exists
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given Node is not present in the tree")
        # when the node has 0 or 1 child
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            # one, find the node with largest key in left st and replace root
            # or find the node with smallest key in right st.
            # first take node equal to right child
            node = self.rchild
            while node.lchild:  # until it becomes none
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self

# ============================================================================

# MIN MAX NODE OPERATION
# ------------------------------
# Min value
# ------------------------------
# assign the root node to a variable
# ------------------------------
# then check if the node has l child or not, if so then shift the variable to that
# till the l child doesnt exist
# -------------------------------

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("smallest key is: ", current.key)

# Max value
# --------------------------------
# same as the min node method
# ---------------------------------
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("biggest key: ", current.key)

# ============================================================================


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
# print(count(root))
# root.search(6)
#print("Pre - Order")
# root.preorder()
# print()
#print("In - Order")
# root.inorder()
# print()
#print("Pre- Order")
# root.postorder()
if count(root) > 1:
    root.delete(98, root.key)
else:
    print("cant perform deletion operation!")
print("after deleting")
root.preorder()
print()

root.min_node()
root.max_node()
