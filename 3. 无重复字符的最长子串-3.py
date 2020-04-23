class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        l, r = 0, 0
        res = 0
        while r < len(s):
            dic[s[r]] += 1
            r += 1
            while dic[s[r - 1]] > 1:
                dic[s[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res
