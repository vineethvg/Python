class newNode:

    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


def addBt(root):
    if root == None:
        return 0
    return(root.key + addBt(root.left)+addBt(root.right))


if __name__ == '__main__':

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)

    sum = addBt(root)
    print(sum)
