class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s == "":
            return 0
        start = 0
        end = 0
        maxLength = 0

        un_ch = set()

        while(end < n):
            if s[end] not in un_ch:
                un_ch.add(s[end])
                end = end + 1
                maxLength = max(maxLength, len(un_ch))
            else:
                un_ch.remove(s[start])
                start = start + 1
        return maxLength
