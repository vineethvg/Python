def selectionSort(a):
    n = len(a)

    for i in range(n):  # traversing till the end of array
        min_ind = i  # assigning a variable at first index
        for j in range(i+1, n):     # one more loop inside where j travers from i+1 index
            if(a[min_ind] > a[j]):  # checking if which index is greater
                min_ind = j  # if j is greater then assigning the min_ind var to it
        a[i], a[min_ind] = a[min_ind], a[i]  # swapping the values
    return a


    # Driver Code
a = [3, 2, 4, 1, 6, 8, 10]
print(selectionSort(a))
