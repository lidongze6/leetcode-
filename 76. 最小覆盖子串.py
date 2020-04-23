class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        from collections import defaultdict
        tc = Counter(t)
        lt = len(tc)
        l, r = 0, 0
        dic = defaultdict(int)
        res = float("inf")
        start = -1
        while r < len(s):
            dic[s[r]] += 1
            if s[r] in tc and tc[s[r]] == dic[s[r]]:
                lt -= 1
            r += 1
            while l <= r and lt == 0:
                if r - l < res:
                    res = r - l
                    start = l
                if s[l] in tc and tc[s[l]] == dic[s[l]]:
                        lt += 1
                dic[s[l]] -= 1
                l += 1
        return s[start:start + res] if start !=-1 else ""


s = "ADABECODEBANC"
t = "AAB"
print(Solution().minWindow(s, t))
