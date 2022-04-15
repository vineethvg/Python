def sol(arr):

    n = len(arr)
    l = 0
    m = 0
    h = n - 1

    while(m <= h):
        if arr[m] == 0:  # 0
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1

        elif arr[m] == 1:  # 1
            m += 1

        else:  # 2
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr


arr = [0, 2, 1, 2, 0]
print(sol(arr))
