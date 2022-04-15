# Arrange given numbers to form the biggest number

# Given an array of numbers,arrange them in a way that
# yields the largest value. For example, if the given numbers are
# {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
# And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
# then the arrangement 998764543431 gives the largest value.

from itertools import permutations


def solution(arr, n):
    a = []
    for i in permutations(arr, n):
        a.append("".join(map(str, i)))
    return max(a)


# driver code
#arr = list(map(int, input("Enter the array elements: ").strip().split()))
arr = [54, 546, 548, 60]
n = len(arr)
print(solution(arr, n))
