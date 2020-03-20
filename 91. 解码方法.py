class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        f = [0] * (len(s) + 1)
        f[1] = 1
        f[0] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] == "0":
                if s[i - 1 - 1] == "1" or s[i - 1 - 1] == "2":
                    f[i] = f[i - 2]
                else:
                    return 0
            else:
                if s[i - 1 - 1] == "1" or (s[i - 1 - 1] == "2" and "1" <= s[i - 1] <= "6"):
                    f[i] = f[i - 1] + f[i - 2]
                else:
                    f[i] = f[i - 1]
        return f[-1]


s = "301"
print(Solution().numDecodings(s))
