class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        if l <= 1: return l
        f = [1] * l

        for i in range(1, l):
            f[i] += f[i - 1]
            for j in range(i):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    f[i] += 1

        return f[l - 1]


s = "abca"
print(Solution().countSubstrings(s))
