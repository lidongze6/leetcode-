class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 区间型DP(需要斜向遍历)
        l = len(s)
        if l <= 1: return l
        f = [[1] * l for i in range(l)]  # f[i][j]表示第i到j(包含j)个字符的区间的最长回文子序列长度

        for i in range(l - 1):
            if s[i] == s[i + 1]:
                f[i][i + 1] = 2

        for le in range(3, l + 1):
            for i in range(l):
                j = i + le - 1
                if j > l - 1:
                    break
                if s[i] == s[j]:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1], f[i + 1][j - 1] + 2)
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])

        return f[0][l - 1]