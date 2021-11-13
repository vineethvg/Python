# solution 1

def sol(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if(arr[i] == 1):
            count = count + 1
    return count
# complexity O(n)

# solution 2


def sol(arr, low, high):
    if high >= low:
        mid = low+(high-low)//2

        if((mid == high or arr[mid+1] == 0) and (arr[mid] == 1)):
            return mid+1

        if arr[mid] == 1:
            return sol(arr, (mid+1), high)
        return sol(arr, low, mid-1)
    return 0
# Complexity O(nlogn)


arr = [1, 1, 0, 0, 0, 0, 0]
print(sol(arr, 0, len(arr)-1))
