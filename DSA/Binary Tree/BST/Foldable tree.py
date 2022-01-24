class newNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def IsFoldable(root):
    if(root == None):
        return True
    return IsFoldableUtil(root.left, root.right)


def IsFoldableUtil(n1, n2):
    if n1 == None and n2 == None:
        return True
    if n1 == None and n2 == None:
        return False

    d1 = IsFoldableUtil(n1.left, n2.right)
    d2 = IsFoldableUtil(n1.right, n2.left)

    return d1 and d2


if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.right = newNode(5)
    root.left.left.left = newNode(6)
    if IsFoldable(root):
        print("tree is foldable")
    else:
        print("tree is not foldable")
