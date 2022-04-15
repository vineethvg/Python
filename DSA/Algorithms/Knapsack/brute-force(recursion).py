def kS(W, wt, val, n):

    if W == 0 or n == 0:
        return 0

    if (wt[n-1] > W):  # n=3, W=50
        return kS(W, wt, val, n-1)

    else:
        return max(val[n-1]+kS(W-wt[n-1], wt, val, n-1), kS(W, wt, val, n-1))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(kS(W, wt, val, n))
