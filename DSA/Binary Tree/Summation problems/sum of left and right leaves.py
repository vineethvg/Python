class newNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def isLeftLeave(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False


def leftLeavesSum(root):
    res = 0
    if root is not None:
        if isLeftLeave(root.left):
            res += root.left.data
        else:
            res += leftLeavesSum(root.left)
        res += leftLeavesSum(root.right)
    return res


def rightLeafSum(root, Sum1):
    if root == None:
        return
    if root.right:
        if(root.right.left is None and root.right.right is None):
            Sum1[0] += root.right.data
    rightLeafSum(root.left, Sum1)
    rightLeafSum(root.right, Sum1)


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.left.left.right = newNode(2)
    root.right = newNode(3)
    root.right.right = newNode(8)
    root.right.right.left = newNode(6)
    root.right.right.right = newNode(7)

    Sum1 = [0]
    rightLeafSum(root, Sum1)
    print("Right leaves sum: ", Sum1[0])

    print("Left leaves sum: ", leftLeavesSum(root))
