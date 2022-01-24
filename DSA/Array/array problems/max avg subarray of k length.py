def sol(arr, n, k):

    if k > n:
        return -1

    csum = [0]*n
    csum[0] = arr[0]

    for i in range(1, n):
        csum[i] = csum[i-1]+arr[i]

    max_sum = csum[k-1]
    max_end = k-1

    for i in range(k, n):
        curr_sum = csum[i] - csum[i-k]

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_end = i

    return max_end-k+1


arr = [1, 12, -5, -6, 50, 3]
k = 4
n = len(arr)
print(sol(arr, n, k))
