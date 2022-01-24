class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


def findMax(root):

    if root == None:
        return float('-inf')
    
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    
    if lres > res :
        res = lres
    if rres > res :
        res = rres
    return res

if __name__ =='__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    
    print(findMax(root))

