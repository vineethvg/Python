# printing an array
def arr(a):
    n = len(a)
    for i in range(0, n):
        i = i+1
    return a


#a = [1, 2, 3, 4, 5]
# print(arr(a))

# ===================================================

# inserting an element in an array
def sol(a, ele, k):
    n = len(a)

    # print normal array
    for i in range(0, n):
        i = i+1
    print(a)

    a.insert(k, ele)

    for i in range(0, n):
        i = i+1
    print(a)

# ==================================================


# deleting an element in an array
def dlt(arr, k):
    n = len(arr)
    # removes and prints the removed element
    print(arr.pop(k))

    for i in range(0, n):
        i = i+1
    print(arr)


# a = [1, 2, 3, 4, 5]
# k = 3
# ele = 10
# print(sol(a, ele, k))
# print(dlt(a, k))

# ===================================================

# Linear search
def search(arr, ele):
    n = len(arr)
    i = 0

    while(i < n):
        if(arr[i] == ele):
            break
        i = i+1
    print("Element found at: ", i)


# a = [1, 2, 3, 4, 5]
# ele = 3
# print(search(a, ele))

# ==================================================

# updating elements
def updd(arr, k, ele):
    n = len(arr)

    for i in range(0, n):
        arr[k] = ele
    return arr


# a = [1, 2, 3, 4, 5]
# k = 2
# ele = 100
# print(updd(a, k, ele))

# ==================================================
