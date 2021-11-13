def solution(arr, low, high, x):

    if(arr[high] <= x):
        return high
    if(arr[low] > x):
        return low

    mid = (low+high)//2

    if(arr[mid] <= x and arr[mid+1] > x):
        return mid
    if(arr[mid] < x):
        return solution(arr, mid+1, high, x)
    return solution(arr, low, mid-1, x)


def printK(arr, x, k, n):
    l = solution(arr, 0, n-1, x)
    r = l+1
    count = 0

    if(arr[l] == x):
        l = l-1

    while(l >= 0 and r < n and count < k):
        if(x - arr[l] < arr[r]-x):
            print(arr[l], end=" ")
            l = l-1
        else:
            print(arr[r], end=" ")
            r = r+1
        count = count+1

    while(count < k and l >= 0):
        print(arr[l], end=" ")
        l = l-1
        count = count+1

    while(count < k and r < n):
        print(arr[r], end=" ")
        r = r+1
        count = count+1


# Driver code
if __name__ == "__main__":

    arr = [12, 16, 22, 30, 35, 39, 42,
           45, 48, 50, 53, 55, 56]

    n = len(arr)
    x = 35
    k = 4

    printK(arr, x, 4, n)
