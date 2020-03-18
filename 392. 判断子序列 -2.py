class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        loc = -1
        for char in s:
            loc = t.find(char, loc + 1)
            if loc == -1:
                return False
        return True

    def isSubsequence_2(self, s, t):

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
