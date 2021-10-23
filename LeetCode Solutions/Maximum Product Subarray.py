class Solution:
    def maxProduct(self, nums: List[int]):
        n = len(nums)
        result = nums[0]
        for i in range(n):
            mul = nums[i]
            for j in range(i+1, n):
                result = max(result, mul)
                mul = mul*nums[j]
            result = max(result, mul)
        return result
