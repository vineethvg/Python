# def switches(N, M, web, app):
#     count = 0
#     flag = 0

#     combined = web + app
#     combined.sort()

#     start = min(web[0], app[0])
#     # print(combined)

#     for i in range(len(combined)):

#         if combined[i] in web and flag == 0:
#             continue
#         elif combined[i] in web and flag == 1:
#             count = count + 1
#             flag = 0

#         elif combined[i] in app and flag == 0 and start != combined[i]:
#             count = count + 1
#         elif combined[i] in app and flag == 1:
#             continue

#         if combined[i] in app:
#             flag = 1
#         else:
#             flag = 0
#     print(count)


# N = 4
# website = [15, 27, 30, 33]
# M = 3
# application = [9, 10, 17]
# switches(N, M, website, application)


# def sol(arr):
#     n = len(arr)
#     temp = []
#     temp.append(arr[n-1])
#     for i in range(n-1):
#         temp.append(arr[i])
#     return temp


# arr = [9, 8, 7, 6, 4, 2, 1, 3]
# print(sol(arr))

# def sol(arr):

#     n = len(arr)
#     temp = []
#     temp1 = []
#     for i in range(n):
#         if(arr[i] < 0):
#             temp.append(arr[i])
#         if(arr[i] > 0):
#             temp1.append(arr[i])
#     return temp+temp1


# arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# print(sol(arr))

# def sol(arr1, arr2):
#     return list(set(arr1 + arr2))


# arr1 = [1, 2, 3, 4, 5]
# arr2 = [1, 2, 3]
# print(sol(arr1, arr2))

# def sol(arr):

#     n = len(arr)
#     mx_start = arr[0]
#     mx_end = 0
#     for i in range(n):
#         mx_end = mx_end + arr[i]
#         if(mx_end < 0):
#             mx_end = 0
#         elif(mx_start < mx_end):
#             mx_start = mx_end
#     return mx_start


# arr = [-1, -2, -3, -4]
# print(sol(arr))

# def sol(arr):
#     n = len(arr)

# arr = [1, 3, 4, 2, 2]
# print(sol(arr))
# n = 4
# pf = str(1/2)
# print(pf.split('.'))
def miniMaxSum(arr):
    n = len(arr)
    mi = 0
    mx = 0
    for i in range(0, n-1):
        mi += arr[i]
        mx += arr[i+1]
    q = min(mi, mx)
    b = max(mi, mx)
    return list(q, b).split('(')


arr = [1, 2, 3, 4, 5]
print(miniMaxSum(arr))
