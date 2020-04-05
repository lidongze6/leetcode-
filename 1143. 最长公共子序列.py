class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)

        f = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # f[i][j] 表示以i,j结尾的最长公共子序列
        res = 0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
                res = max(res, f[i][j])
        return res
