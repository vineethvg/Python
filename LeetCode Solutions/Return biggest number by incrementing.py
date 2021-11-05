def solution(N, K):
    res = [int(i) for i in str(N)]

    kb = K
    new = []

    for i in res:
        dum = i
        while(dum != 9):
            if kb == 0:
                break
            else:
                dum = dum+1
                kb = kb - 1

        new.append(dum)
    print(' '.join([str(i) for i in new]))


N = 512
K = 10
x = solution(N, K)
print(x)
