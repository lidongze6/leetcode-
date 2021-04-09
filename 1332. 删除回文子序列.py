class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:return 0
        for i in range(len(s)):
            if s[i] !=s[len(s)-i-1]:
                return 2
        return 1