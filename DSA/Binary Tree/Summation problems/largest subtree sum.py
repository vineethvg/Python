# =======================================================================
# subtree sum is stored at currSum. //1
# Update answer if current subtree sum is greater than answer so far. //2
# Return current subtree sum to its parent node.
#  ======================================================================
class newNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def util(root, ans):
    if root == None:
        return 0
    currSum = (root.key + util(root.left, ans) + util(root.right, ans))  # //1
    ans[0] = max(ans[0], currSum)  # //2
    return currSum


def largestSumSubTree(root):
    if root == None:
        return 0
    ans = [-999999999999999]
    util(root, ans)
    return ans[0]


if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(-2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(-6)
    root.right.right = newNode(2)

    print(largestSumSubTree(root))
