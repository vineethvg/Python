def solution(arr, n):

    prod = 1
    flag = 0

    for i in range(n):
        if (arr[i] == 0):  # if any element in the array is zero move to next elemnt
            flag = flag + 1
        else:
            prod = prod * arr[i]

    a = [0 for i in range(n)]

    for i in range(n):
        if (flag > 1):  # if no of zeros are more than the all values become zero
            a[i] = 0

        elif(flag == 0):  # if no zero,then we insert the value at the index
            a[i] = (prod//arr[i])

        # if one zero is present, then all values
        # except that index value will be zero
        elif (flag == 1 and arr[i] != 0):
            a[i] = 0
        # if(flag == 1 and arr[i] == 0)
        else:
            a[i] = prod
    return a


n = 5
array = [10, 3, 5, 6, 2]
ans = solution(array, n)

print(*ans)
