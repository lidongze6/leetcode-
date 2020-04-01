class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        f = [[0] * l for i in range(l)]  # f[i][j]表示第i到j(包含j)个字符的区间的最长回文子序列长度
        for i in range(l):
            f[i][i] = 1

        # 从右下向上遍历
        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if s[i] == s[j]:  # 如果相等:则在上一个回文子序列长度上加上两个字符的长度
                    f[i][j] = f[i + 1][j - 1] + 2
                else:  # 如果不相等:则对比哪边的回文子序列更长
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][l - 1]
