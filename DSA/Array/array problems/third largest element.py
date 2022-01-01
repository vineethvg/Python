import sys


def sol(arr, n):

    first = arr[0]
    for i in range(1, n):
        if(arr[i] > first):
            first = arr[i]

    second = -sys.maxsize
    for i in range(0, n):
        if(arr[i] > second and arr[i] < first):
            second = arr[i]

    third = -sys.maxsize

    for i in range(0, n):
        if(arr[i] > third and arr[i] < second and arr[i] < first):
            third = arr[i]
    return third


arr = [1, 3, 6, 8, 8, 5]
n = len(arr)
print(sol(arr, n))
