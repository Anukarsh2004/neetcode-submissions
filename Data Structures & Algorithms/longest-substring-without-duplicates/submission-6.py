class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0

        seen = {}

        l = 0
        r = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            
            seen[s[r]] = r
            length = r - l + 1
            res = max(res, length)
        

        return res
            
        