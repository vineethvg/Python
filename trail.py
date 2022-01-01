# total = 8
# k = 2
# ## making an array of size [k+1][total+1]
# arr = [[0 for y in range(total+1)]for x in range(k+1)]

# for i in range(total+1):
#   arr[0][i] = 0
#   arr[1][i] = 1

# for i in range(k+1):
#   arr[i][0] = 0
# #print(arr)
# for row in range(2,k+1):
#   for col in range(1,total+1):

#     if col < row:
#       arr[row][col] = arr[row-1][col]
#     elif col == row:
#       arr[row][col] = arr[row-1][col] + 1
#     else:
#       arr[row][col] = arr[row-1][col]  +  arr[row][col-row]

# print(arr[k][total])
# def ways(total, k):
#     arr = [[0 for y in range(total+1)]for x in range(k+1)]
#     for i in range(total+1):
#         arr[0][i] = 0
#         arr[1][i] = 1
#     for i in range(k+1):
#         arr[i][0] = 0
#     for row in range(2, k+1):
#         for col in range(1, total+1):
#             if col < row:
#                 arr[row][col] = arr[row-1][col]
#             elif col == row:
#                 arr[row][col] = arr[row-1][col] + 1
#             else:
#                 arr[row][col] = arr[row-1][col] + arr[row][col-row]

#     return(arr[k][total])


# if __name__ == '__main__':
#     total = int(input().strip())
#     k = int(input().strip())
#     result = ways(total, k)
#     print(str(result) + '\n')

# import math
# import os
# import random
# import re
# import sys


# def maxSubsetSum(arr):
#     dp = {}
#     dp[0], dp[1] = arr[0], max(arr[0], arr[1])
#     for i, num in enumerate(arr[2:], start=2):
#         dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
#     return dp[len(arr)-1]


# if __name__ == '__main__':

#     k_count = int(input().strip())

#     arr = []
#     for _ in range(k_count):
#         k_item = int(input().strip())
#         arr.append(k_item)

#     res = maxSubsetSum(arr)

#     print(str(res)+'\n')
#     print('\n')

# == == == == == == == == == == == == == == == == == == == == == == == == == =
# s = ['aba', 'bcb', 'ece', 'aa', 'e']
# q = ['1-3', '2-5', '2-2']

# v = ['a', 'e', 'i', 'o', 'u']
# ans = []

# for i in q:
#     c = 0
#     l = int(i[0])
#     r = int(i[-1])

#     for j in range(l-1, r):
#         if(s[j][0] in v) and (s[j][-1] in v):
#             c = c+1
#     ans.append(c)
# print(ans)

# == == == == == == == == == == == == == == == == == == == == == == == == == =
# T = int(input())
# for _ in range(0,T):

#     N , K = map(int,input().strip().split())
#     A = list(map(int,input().strip().split()))[:K]

#     A.sort()
#     count = 0

#     for i in range(K):
#         N = N - A[i]
#         if N>0:
#             count += 1
#         else:
#             break
#     print(count)


# t = int(input())
# ip = []
# op = 0
# for _ in range(t):
#     n = int(input())
#     rem = n % 10
#     div = n // 10
#     op += div**rem
# print(op)

# == == == == == == == == == == == == == == == == == == == == == == == == == =
# t = int(input())

# for _ in range(t):
#     S = input()
#     cnt = 0

#     for ch in S:
#         if ch == 'R':
#             cnt = cnt + 1
#             S.replace('R', 'K', cnt)
#         elif ch == 'K':
#             cnt = cnt + 1
#             S.replace('K', 'R', cnt)
#     print(cnt-1)
# == == == == == == == == == == == == == == == == == == == == == == == == == =
# from itertools import combinations


# def pairSum(arr, S):
#     res = []
#     for var in combinations(arr, 2):
#         if var[0] + var[1] == S:
#             res.append((var[0], var[1]))


# if __name__ == "__main__":
#     N, S = map(int, input().split())
#     arr = list(int(num) for num in input().strip().split())[:N]
#     print(pairSum(arr, S))


# def sol(arr, k):
#     u_m = {}
#     cnt = 0
#     for i in range(len(arr)):
#         if k-arr[i] in u_m:
#             cnt += u_m[k - arr[i]]
#         if arr[i] in u_m:
#             u_m[arr[i]] += 1
#         else:
#             u_m[arr[i]] = 1

#     return cnt


# arr = [1, 1, 1, 1]
# k = 2
# print(sol(arr, k))
# == == == == == == == == == == == == == == == == == == == == == == == == == =

# def CountWays(str):
#     n = len(str)
#     cnt = [0] * (n + 1)
#     cnt[0] = 1
#     cnt[1] = 1

#     for i in range(2, n + 1):
#         cnt[i] = 0
#         if (str[i - 1] > '0'):
#             cnt[i] = cnt[i - 1]

#         if (str[i - 2] == '1' or (str[i - 2] == '2' and str[i - 1] < '7')):
#             cnt[i] += cnt[i - 2]

#     return cnt[n]


# str = "027"
# print(CountWays(str))
# == == == == == == == == == == == == == == == == == == == == == == == == == =
# def sol(arr):
#     hh = -999
#     for i in range(1, len(arr)):
#         diff = abs(arr[i]-arr[i-1])
#         if diff > hh:
#             hh = diff
#     return hh


# strs = input()
# strs = strs.split()
# arr = []
# for s in strs:
#     arr.append(int(s))
# print(sol(arr))
