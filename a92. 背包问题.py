class Solution:
    """
    给出n个物品, 以及一个数组, nums[i]代表第i个物品的大小,
    保证大小均为正数, 正整数target表示背包的大小, 找到填背包的最大重量。
    """
    def backPack(self, m, A):
        if m == 0: return 0
        f = [[False] * (m + 1) for i in range(len(A) + 1)]  # f[i][j] 前i个物品装j重量能否装得下
        f[0][0] = True
        for i in range(1, len(A) + 1):
            f[i][0] = True

        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if j - A[i - 1] >= 0:
                    f[i][j] = f[i][j] or f[i - 1][j - A[i - 1]]

        for j in range(m, -1, -1):
            if f[-1][j]:
                return j