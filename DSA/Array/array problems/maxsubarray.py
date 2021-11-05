# Kadane's Algorithm
# The idea is to maintain a maximum(positive) subarray ending at each index of
# the given array.
# This subarray is either empty or consists of one or more elements than the
# maximum subarray.
import sys


def maxSubArray(nums):

    max_so_far = -sys.maxsize
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = max(max_ending_here, nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


nums = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArray(nums))
