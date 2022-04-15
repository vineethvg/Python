def solution(arr):
    n = len(arr)
    found = False

    for i in range(n-1):
        s = set()

        for j in range(i+1, n):
            x = -(arr[i]+arr[j])
            if x in s:
                return(x, arr[i], arr[j])
                found = True
            else:
                s.add(arr[j])
    if(found == False):
        return None


arr = [3, 1, 2, 8, -2, -1]
print(*solution(arr))
