# program to find  minimum missing number in an array

def solution(arr):
    n = len(arr)
    sum = 0
    arrSum = 0

    for i in range(n):
        arr.sort()
        arrSum = (arr[n-1]*(arr[n-1]+1))/2
        sum = sum + arr[i]
    return int(arrSum - sum)


arr = [1, 2, 4, 3, 8, 6, 7]
print(solution(arr))
