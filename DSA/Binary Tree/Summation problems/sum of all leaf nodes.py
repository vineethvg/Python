
class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def leafSum(root):
    global total
    if root is None:
        return
    if root.left is None and root.right is None:
        total += root.data

    leafSum(root.left)
    leafSum(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(8)

    total = 0
    leafSum(root)
    print(total)
