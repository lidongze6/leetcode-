class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 双序列型DP
        # 若尾部相同，则f[i][j] = f[i - 1][j - 1]
        # 若尾部不同，则f[i][j] = min(f[i - 1][j](删除), f[i][j - 1](增加), f[i - 1][j - 1](替换)) + 1
        l1, l2 = len(word1), len(word2)
        if l1 == 0 and l2 == 0: return 0
        if l1 == 0 or l2 == 0: return l2 if l1 == 0 else l1

        f = [[float("inf")] * (l2 + 1) for i in range(l1 + 1)]
        # f[i][j]到第i，j个字符需要的最少操作数
        f[0][0] = 0

        for i in range(1, l1 + 1):
            f[i][0] = i
        for j in range(1, l2 + 1):
            f[0][j] = j
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i][j], f[i - 1][j - 1])
                else:
                    f[i][j] = min(f[i][j], f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1

        return f[l1][l2]