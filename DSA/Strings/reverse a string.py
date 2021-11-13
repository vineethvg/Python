def sol(s):
    res = [int(i) for i in str(s)]
    res.reverse()

    op = [str(x) for x in res]
    op = "".join(op)
    return op


for _ in range(int(input())):
    N = int(input())
    while N > 0:
        break
    print(sol(N))
