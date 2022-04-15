def solution(arr, k):
    n = len(arr)
    cntPairs = 0
    arr = sorted(arr)

    start = 0
    end = n-1

    while(start < end):

        if(arr[start] + arr[end] == k):
            while(start < end and arr[start] == arr[start + 1]):
                start = start+1
            while(start < end and arr[end] == arr[end - 1]):
                end = end-1
            cntPairs = cntPairs + 1
            start = start+1
            end = end-1
    return cntPairs


arr = [5, 6, 5, 7, 7, 8]
K = 13
print(solution(arr, K))
