class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1

        while start+1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start

        if nums[end] >= target:
            return end

        return end+1
