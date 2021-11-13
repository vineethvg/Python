# In this technique we swap the elements
# if the previous element are larger than next
# Ex: 1 9 4 2  8 --> 1 4 9 2 8 (9 and 4 are being swapped)
# 1 4 9 2 8 --> 1 4 2 9 8
# 1 4 2 9 8 --> 1 4 2 8 9
# 1 4 2 8 9 --> 1 2 4 8 9
def bubbleSort(a):
    n = len(a)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if(a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        if swapped == False:  # if swapping doesnt happen break out of the loop
            break
    return a


# Driver code
a = [3, 6, 2, 1, 9, 8]
print(bubbleSort(a))
