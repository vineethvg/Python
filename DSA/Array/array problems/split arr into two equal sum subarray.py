def solution(arr):
    n = len(arr)
    leftSum = 0

    # traverse array
    for i in range(0, n):

        # add current element to left sum
        leftSum = leftSum + arr[i]
        rightSum = 0
        # find sum of rest of array elements
        for j in range(i+1, n):
            rightSum = rightSum + arr[j]

        # split index
        if (leftSum == rightSum):
            return i+1

    # if it not possible to split then return -1
    return -1


def printSplit(arr):
    n = len(arr)
    split = solution(arr)

    if(split == -1 or split == n):
        print("Not possible")
        return

    for i in range(0, n):
        if(split == i):
            print("")
        print(str(arr[i]) + ' ', end=" ")


arr = [1, 2, 3, 4, 5, 5]
print(printSplit(arr))
