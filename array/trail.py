# ===========================================================================================

# given sorted array find a pair with given sum
# def pairSorted(arr, n, x):
#     for i in range(0, n-1):
#         # find the pivot point
#         if(arr[i] > arr[i+1]):
#             break

#     # index of smallest element
#     l = (i+1) % n
#     # index of largest element
#     r = i

#     # keep moving until l and r are equal
#     while(l != r):
#         if(arr[l] + arr[r] == x):
#             return True
#         # if sum is less move to higher sum
#         if(arr[l] + arr[r] < x):
#             l = (l+1) % n
#         else:
#             # Move to the lower sum side
#             r = (n + r-1) % n
#     return False

# arr = [11, 15, 6, 8, 9, 10]
# sum = 21
# n = len(arr)

# if (pairSorted(arr, n, sum)):
#     print("Array has two elements with sum 21")
# else:
#     print("Array doesn't have two elements with sum 21 ")

# =============================================================================================

# Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed
# def maxSum(arr):
#     arrSum = 0
#     currVal = 0
#     n = len(arr)

#     for i in range(0, n):
#         arrSum = arrSum + arr[i]
#         currVal = currVal + (i*arr[i])

#     maxVal = currVal

#     for j in range(1, n):
#         currVal = currVal + arrSum - n * arr[n-j]
#         if currVal > maxVal:
#             maxVal = currVal
#     return maxVal


# arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Max sum is: ", maxSum(arr))

# ===========================================================================================

# Maximum sum of i*arr[i] among all rotations of a given array

# def maxSum(arr, n):
#     cum_sum = 0
#     cur_val = 0

#     for i in range(0, n):
#         cum_sum = cum_sum + arr[i]
#         cur_val = cur_val + (i*arr[i])

#     res = cur_val

#     for i in range(1, n):
#         next_val = (cur_val - (cum_sum - arr[i-1]) + arr[i-1] * (n-1))
#         cur_val = next_val
#         res = max(res, next_val)
#     return res


# arr = [8, 3, 1, 2]
# n = len(arr)
# print(maxSum(arr, n))

# ===========================================================================================

# Find the Rotation Count in Rotated Sorted array

# def countR(arr, n):
#     min = arr[0]
#     for i in range(0, n):
#         if (min > arr[i]):
#             min = arr[i]
#             min_index = i
#     return min_index


# arr = [15, 18, 2, 3, 6, 12]
# n = len(arr)
# print(countR(arr, n))

# ===========================================================================================

# Quickly find multiple left rotations of an array

# def leftRotate(arr, n, k):
#     for i in range(k, k+n):
#         print(str(arr[i % n]), end=" ")


# arr = [1, 3, 5, 7, 9]
# print(arr)
# n = len(arr)
# k = 2
# leftRotate(arr, n, k)
# print()

# k = 3
# leftRotate(arr, n, k)
# print()

# k = 4
# leftRotate(arr, n, k)
# print()

# ===========================================================================================

# Find the minimum element in a sorted and rotated

# def minSorted(arr, n):
#     for i in range(0, n-1):
#         if(arr[i] > arr[i+1]):
#             return arr[i+1]


# arr = [11, 12, 1, 2, 3, 4]
# n = len(arr)
# print(minSorted(arr, n))


# Solution 2

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums.sort()
#         for i in range(0,n):
#             return nums[i]

# ==========================================================================================

# Print left rotation of array in O(n) time and O(1) space
# def leftRotate(arr, n, k):
#     mod = k % n

#     for i in range(n):
#         print(str(arr[(mod + i) % n]))
#     print()
#     return


# arr = [1, 3, 5, 7, 9]
# n = len(arr)

# k = 2
# # Function Call
# leftRotate(arr, n, k)

# k = 3

# # Function Call
# leftRotate(arr, n, k)

# k = 4
# # Function Call
# leftRotate(arr, n, k)

# ==========================================================================================

# Split the array and add the first part to the end

# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         for j in range(0, n-1):
#             arr[j] = arr[j+1]
#         arr[n-1] = x


# arr = [12, 10, 5, 6, 52, 36]
# n = len(arr)
# position = 2

# splitArr(arr, n, position)

# for i in range(0, n):
#     print(arr[i], end=' ')

# ==========================================================================================

# Rearrange an array such that arr[i] = i

# def fix(arr):
#     s = set()

#     # Storing all the values in the Set
#     for i in range(len(arr)):
#         s.add(A[i])

#     for i in range(len(arr)):
#         if i in s:
#             arr[i] = i
#         else:
#             arr[i] = -1
#     return A


# if __name__ == "__main__":
#     A = [-1, -1, 6, 1, 9,
#          3, 2, -1, 4, -1]
#     print(fix(A))

# ===============================================================================

# Write a program to reverse an array or string

# def revArray(arr, start, end):
#     while(start < end):
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1


# arr = [1, 2, 3, 4, 5, 6]
# revArray(arr, 0, 5)
# print(arr)

# ==============================================================================
# Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i

# import array as arr
# import numpy as np


# def rearrangeArr(arr, n):
#     evenPos = int(n/2)
#     oddPos = n - evenPos

#     tempArr = np.empty(n, dtype=object)

#     for i in range(n):
#         tempArr[i] = arr[i]
#     tempArr.sort()

# fill up the odd positions
#     j = oddPos - 1
#     for i in range(0, n, 2):
#         arr[i] = tempArr[j]
#         j -= 1

# fill up even positions
#     j = oddPos
#     for i in range(1, n, 2):
#         arr[i] = tempArr[j]
#         j += 1

#     for i in range(0, n):
#         print(arr[i], end=' ')


# Arr = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
# rearrangeArr(Arr, 7)

# ===============================================================================

# Segregate even and odd numbers

# def arrayEvenAndOdd(a, n):
#     ind = 0
#     a = [0 for i in range(n)]

#     for i in range(n):
#         if(arr[i] % 2 == 0):
#             a[ind] = arr[i]
#             ind += 1

#     for i in range(n):
#         if(arr[i] % 2 != 0):
#             a[ind] = a[i]
#             ind += 1

#     for i in range(n):
#         print(a[i], end=" ")

#     print()


# arr = [1, 3, 2, 4, 7, 6, 9, 10]
# n = len(arr)

# # Function call
# arrayEvenAndOdd(arr, n)

# ===============================================================================

# Segregate even and odd numbers (method 2)

# def arrayEvenAndOdd(a, n):
#     i = -1
#     j = 0
#     while(j != n):
#         if(a[j] % 2 == 0):
#             i = i+1

#             a[i], a[j] = a[j], a[i]
#         j = j+1

#     for i in a:
#         print(str(i)+" ", end=" ")


# if __name__ == '__main__':
#     arr = [1, 3, 2, 4, 7, 6, 9, 10]
#     n = len(arr)
#     arrayEvenAndOdd(arr, n)

# ===============================================================================

# Shuffle a given array using Fisher–Yates shuffle Algorithm

# import random


# def randomize(a, n):
#     for i in range(n-1, 0, -1):
#         j = random.randint(0, i+1)

#         arr[i], arr[j] = arr[j], arr[i]
#     return arr


# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# n = len(arr)
# print(randomize(arr, n))

# ===============================================================================

# Median of Two Sorted Arrays | LeetCode Answers (Python)

# # Python code for median with
# # case of returning double
# # value when even number
# # of elements are present
# # in both array combinely
# median = 0
# i = 0
# j = 0

# # def to find max


# def maximum(a, b):
#     return a if a > b else b

# # def to find minimum


# def minimum(a, b):
#     return a if a < b else b

# # def to find median
# # of two sorted arrays


# def findMedianSortedArrays(a, n, b, m):

#     global median, i, j
#     min_index = 0
#     max_index = n

#     while (min_index <= max_index):

#         i = int((min_index + max_index) / 2)
#         j = int(((n + m + 1) / 2) - i)

#         # if i = n, it means that
#         # Elements from a[] in the
#         # second half is an empty
#         # set. and if j = 0, it
#         # means that Elements from
#         # b[] in the first half is
#         # an empty set. so it is
#         # necessary to check that,
#         # because we compare elements
#         # from these two groups.
#         # Searching on right
#         if (i < n and j > 0 and b[j - 1] > a[i]):
#             min_index = i + 1

#         # if i = 0, it means that
#         # Elements from a[] in the
#         # first half is an empty
#         # set and if j = m, it means
#         # that Elements from b[] in
#         # the second half is an empty
#         # set. so it is necessary to
#         # check that, because we compare
#         # elements from these two groups.
#         # searching on left
#         elif (i > 0 and j < m and b[j] < a[i - 1]):
#             max_index = i - 1

#         # we have found the
#         # desired halves.
#         else:

#             # this condition happens when
#             # we don't have any elements
#             # in the first half from a[]
#             # so we returning the last
#             # element in b[] from the
#             # first half.
#             if (i == 0):
#                 median = b[j - 1]

#             # and this condition happens
#             # when we don't have any
#             # elements in the first half
#             # from b[] so we returning the
#             # last element in a[] from the
#             # first half.
#             elif (j == 0):
#                 median = a[i - 1]
#             else:
#                 median = maximum(a[i - 1], b[j - 1])
#             break

#     # calculating the median.
#     # If number of elements
#     # is odd there is
#     # one middle element.

#     if ((n + m) % 2 == 1):
#         return median

#     # Elements from a[] in the
#     # second half is an empty set.
#     if (i == n):
#         return ((median + b[j]) / 2.0)

#     # Elements from b[] in the
#     # second half is an empty set.
#     if (j == m):
#         return ((median + a[i]) / 2.0)

#     return ((median + minimum(a[i], b[j])) / 2.0)


# # Driver code
# a = [90]
# b = [10, 13, 14]
# n = len(a)
# m = len(b)

# # we need to define the
# # smaller array as the
# # first parameter to make
# # sure that the time complexity
# # will be O(log(min(n,m)))
# if (n < m):
#     print("The median is : {}".format(findMedianSortedArrays(a, n, b, m)))
# else:
#     echo("The median is : {}".format(findMedianSortedArrays(b, m, a, n)))

# ===============================================================================
