def solution(arr):
    n = len(arr)

    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(solution(arr))
