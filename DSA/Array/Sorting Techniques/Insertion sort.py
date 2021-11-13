def insertionSort(a):
    n = len(a)

    for i in range(1, n):

        key = a[i]
        j = i-1

        # j more than zero and key greater than jth index val
        while j >= 0 and key < a[j]:

            a[j+1] = a[j]  # shift element then decrement
            j = j-1

        a[j+1] = key  # assign key to the the j+1 index

    return a


# Driver code
a = [10, 5, 2, 8, 3, 9, 22, 55, 4]
print(insertionSort(a))
