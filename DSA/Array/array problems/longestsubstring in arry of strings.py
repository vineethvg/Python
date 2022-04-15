# Longest Common Substring in an Array of Strings
def sol(arr):
    n = len(arr)
    st = arr[0]
    st_len = len(st)
    f = ""

    # first we will take two iterable objects and generate substrings
    for i in range(st_len):
        for j in range(i+1, st_len+1):

            sub = st[i:j]
            print(sub)
            k = 1
            # then we check the common sub-string throughout the array
            for k in range(1, n):

                if sub not in arr[k]:
                    break
            if(k+1 == n and len(f) < len(sub)):
                f = sub
    return f


arr = ['sadful', 'sadness', 'sad', 'sadistic']
print(sol(arr))
