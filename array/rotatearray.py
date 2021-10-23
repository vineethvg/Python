# Program to roatate array

# arr is array
# d is no of elements to be rotated
# n is total no of elements
def rotateArr(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

# logic
# first we stor the arr[0] in a temp variable
# then we move arr[1] to arr[0], arr[2] to arr[1] till the end of loop i,e arr[n-1]
# at the end assign the value of temp to arr[n]


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
    arr[n-1] = temp


if __name__ == "__main__":
    t = int(input())
    while(t > 0):
        # take n and d input
        n_d = [int(x) for x in input().strip().split()]
        n = n_d[0]
        d = n_d[1]
        arr = [int(x) for x in input().strip().split()]

        # call the rotate function
        rotateArr(arr, d, n)

        # print the list
        for i in range(n):
            print(arr[i], end=" ")
        print()
        t = t-1
