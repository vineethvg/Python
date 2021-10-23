# ====================================PROBLEM STATEMENT============================================================================
# An Industrial company has N factories, each producing some pollution every month.
# The company has decided to reduce its total fume emissions by equipping some of the factories with one or more nitors.
# Every such filter reduces the pollution of a factory by half. When a second (or subsequent) filter is applied,
# it again reduces by half the remaining pollution emitted after fitting the existing fiter(s).
# For example, a factory that initially produces 6 units of pollution will generate 3 units with one filter,
# 1.5 units with two filters and 0.75 units with three filters.

# You are given an array of N Integers describing the amount of pollution produced by the factories.
# Your task is to find the minimum number of filters needed to decrease the total sum of pollution by at least half.
# Write a function: def solution (A) which, given an array of integers A of length N, returns the minimum number of
# filters needed to reduce the total pollution by at least half.

# Examples: 1. Given A=[5, 19, 8, 1], your function should return 3.
# The initial total pollution is 5+19+8+1-33. We Install two filters at the factory producing 19 units and one filter at the
# factory producing 8 units. Then the total pollution will be [5+((19/2)/2)+(8/2)+1] = 5 + 4.75 + 4 + 1 = 14.75 which is less than 33/2-16.5,
# so we have achieved our goal.

# 2. Given A=[10, 10], your function should return 2, because we may Install one filter at each factory.

# 3.Given A=[3, 0, 5], your function should return 2, because it is sufficient to install one filter at each factory
# producing a non-zero amount of pollution.

# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [1..30,000]; each element of array A is an integer within the range (0..70,000).

# ================================================================================================================================

def solution(A):
    n = len(A)
    sum = arrSum(A)
    counter = 0
    cmp_sum = int(sum/2)

    while(sum > cmp_sum):
        A.sort()
        A[n-1] = A[n-1]/2
        counter = counter + 1
        sum = int(arrSum(A))
    return counter


def arrSum(arr):
    N = len(arr)
    sum = 0
    for i in range(0, N):
        sum = sum + arr[i]
    return sum


# Test Case 1
A = [5, 19, 8, 1]
# print(solution(A))

# Test Case 2
A = [10, 10]
# print(solution(A))

# Test Case 3
A = [3, 0, 5]
# print(solution(A))

# ==================================================================================================================================
