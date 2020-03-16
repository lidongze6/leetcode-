class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c = Counter(s1)
        l, r = 0, len(s1) - 1
        c1 = Counter(s2[l:r])
        while r < len(s2):
            c1[s2[r]] += 1
            if c1 == c:
                return True
            r += 1
            c1[s2[l]] -= 1
            if c1[s2[l]] == 0:
                del c1[s2[l]]
            l += 1
        return False


s1="ab"

s2="eidboaoo"
print(Solution().checkInclusion(s1,s2))