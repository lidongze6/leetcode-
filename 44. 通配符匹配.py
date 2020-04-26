class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 双序列型DP
        l1 = len(s)
        l2 = len(p)

        f = [[False] * (l2 + 1) for i in range(l1 + 1)]

        f[0][0] = True
        # f[1..n][0]=False
        for i in range(l1 + 1):
            for j in range(1, l2 + 1):
                # 当s[i-1]与p[j-1]相同时或p[j-1]为"?"能匹配所有的s（除了空串)，结果取决于s和p各缩进一个
                if (i >= 1 and s[i - 1] == p[j - 1]) or (i >= 1 and p[j - 1] == "?"):
                    f[i][j] |= f[i - 1][j - 1]
                # 当p[j-1]为*时
                elif p[j - 1] == "*":
                    # 当*匹配0个时
                    f[i][j] |= f[i][j - 1]
                    if i >= 1:
                        # 当*匹配s的一个或多个时(多个相当于这一步操作执行了多遍)
                        f[i][j] |= f[i - 1][j]

        return f[l1][l2]


s = "aa"
p = "a"
print(Solution().isMatch(s, p))
