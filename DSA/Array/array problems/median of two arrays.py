def solution(arr1, arr2):
    res = arr1 + arr2
    res.sort()
    print(res)

    n = len(res)
    l = 0
    r = n-1
    for i in range(r):
        mid = (l+r)//2
        med = (res[mid]+res[mid+1])//2
    return med


arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print(solution(arr1, arr2))
