# program to merge sorted arrays
NA = -1


def solution(arr1, arr2):

    n = len(arr1)
    m = len(arr2)

    if(n > m):
        for i in range(n-1):
            for j in range(m):
                if(arr1[i] == NA):
                    arr1[i] = arr2[j]
                    i = i + 1
                    j = j + 1
        arr1.sort()
        return arr1

    else:
        for i in range(m-1):
            for j in range(n):
                if(arr2[i] == NA):
                    arr2[i] = arr1[j]
                    i = i + 1
                    j = j + 1
        arr2.sort()
        return arr2


arr1 = [16, 17, 19, 20, 22]
arr2 = [10, 12, 13, 14, 18, NA, NA, NA, NA, NA]

print(solution(arr1, arr2))
