class Solution:
    def countSubstrings(self, s: str) -> int:
        # 中心扩散方法
        l = len(s)
        if l <= 1: return l
        f = [[0] * l for i in range(l)]
        res=0
        for i in range(l):
            f[i][i] = 1
            res+=1
        for j in range(l - 1):
            if s[j] == s[j + 1]:
                f[j][j + 1] = 1
                res+=1

        for k in range(2, l):
            for i in range(l - k):
                j = i + k
                if s[i] == s[j] and f[i + 1][j - 1] > 0:
                    f[i][j] = 1
                    res+=1

        return res


s = "aaa"
print(Solution().countSubstrings(s))
