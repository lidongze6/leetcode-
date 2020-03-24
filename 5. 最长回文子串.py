class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 划分型DP
        if len(s) <= 1: return s
        res = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                else:
                    break
            if len(res) < len(s[l + 1:r]):
                res = s[l + 1:r]

        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    r += 1
                    l -= 1
                else:
                    break
            if len(res) < len(s[l + 1:r]):
                res = s[l + 1:r]

        return res

s="babad"
print(Solution().longestPalindrome(s))