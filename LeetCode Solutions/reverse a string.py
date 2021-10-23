# Solution 1
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        word = ""
        for ch in s:
            if(ch != ' '):
                word = word + ch
            if(ch == ' '):
                if(len(word) != 0):
                    if(res != ""):
                        res = ' ' + res
                    res = word + res
                    word = ""
        if(len(word) != 0):
            if(res != ""):
                res = ' ' + res
            res = word + res
        return res

# Solution 2


class Solution(object):
    def maxProduct(self, nums):
        res1 = [0 for i in range(len(nums))]
        res2 = [0 for i in range(len(nums))]

        if len(nums) == 0:
            return 0

        for i in range(len(nums)):
            if i == 0:
                res1[i] = nums[i]
                res2[i] = nums[i]
            else:
                res1[i] = max(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])
                res2[i] = min(nums[i], nums[i]*res1[i-1], nums[i]*res2[i-1])

        return max(max(res1), max(res2))
