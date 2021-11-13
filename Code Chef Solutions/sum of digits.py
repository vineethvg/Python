t = int(input())
for _ in range(t):
    a = int(input())
    lst = [int(i) for i in str(a)]
    n = len(lst)
    sum = 0
    for i in range(n):
        sum = sum + lst[i]
    print(sum)
