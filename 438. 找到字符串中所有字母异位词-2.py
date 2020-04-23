class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        c = Counter(p)
        l, r = 0, len(p)-1
        c1 = Counter(s[l:r])
        res = []
        while r < len(s):
            c1[s[r]] += 1
            if c1 == c:
                res.append(l)
            r += 1
            c1[s[l]] -= 1
            if c1[s[l]] == 0:
                del c1[s[l]]
            l += 1
        return res

s="cbaebabacd"
p="abc"
print(Solution().findAnagrams(s,p))