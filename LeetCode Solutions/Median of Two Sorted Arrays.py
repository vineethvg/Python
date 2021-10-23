class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        n = len(nums1)

        # for even
        if n % 2 == 0:
            mean = n // 2
            return (nums1[mean - 1] + nums1[mean]) / 2
        else:
            # for odd
            mean = (n // 2) + 1
            return nums1[mean - 1]
