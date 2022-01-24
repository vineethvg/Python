class newNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def SumOfParentOfX(root, Sum, x):

    if root == None:
        return

    if((root.left and root.left.data == x) or (root.right and root.right.data == x)):
        Sum[0] += root.data

    SumOfParentOfX(root.left, Sum, x)
    SumOfParentOfX(root.right, Sum, x)


def SumOfParentOfXUtil(root, x):
    Sum = [0]
    SumOfParentOfX(root, Sum, x)
    return Sum[0]


if __name__ == '__main__':

    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(5)
    root.left.left = newNode(7)
    root.left.right = newNode(2)
    root.right.left = newNode(2)
    root.right.right = newNode(3)

    x = 2

    print(SumOfParentOfXUtil(root, x))
