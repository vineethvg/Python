# a is array, l & r are left-right most element,mid is the pivot point
def merge(a, l, r, mid):

    # sublists with the range
    l_sub = a[l:mid+1]
    r_sub = a[mid+1:r+1]

    i = 0  # left_sublist index
    j = 0  # right_sublist index
    k = l  # sorted_sublist index

    # traversing till the end
    while (i < len(l_sub) and j < len(r_sub)):

        # if our left sublist has smaller element put it in sorted list/array
        if l_sub[i] <= r_sub[j]:
            a[k] = l_sub[i]
            # then move forward
            i += 1

        # else add it to the right sublist or subarray
        else:
            a[k] = r_sub[j]
            j += 1

        # after adding we have to move foward in the sorted part
        k += 1

    # This loop is for remaining elements and add them
    while(i < len(l_sub)):
        a[k] = l_sub[i]
        i += 1
        k += 1

    while(j < len(r_sub)):
        a[k] = r_sub[j]
        j += 1
        k += 1


def mergesort(a, l, r):
    if(l >= r):
        return

    mid = (l+r)//2
    mergesort(a, l, mid)
    mergesort(a, mid+1, r)
    merge(a, l, r, mid)


# Driver Code
a = [9, 4, 7, 6, 3, 1, 5]
l = 0  # left most element
r = len(a)-1  # right most element
mergesort(a, l, r)
print(a)
