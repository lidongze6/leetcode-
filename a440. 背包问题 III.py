class Solution:
    """
    有 n 个物品和一个大小为 m 的背包.
    给定数组 A 表示每个物品的大小和数组 V 表示每个物品的价值.
    每个物品能使用无限次，问最多能装入背包的总价值是多大?
    """

    def backPackII(self, m, A, V):
        if not len(A): return 0
        l = len(A)
        f = [[0] * (m + 1) for i in range(l + 1)]

        for i in range(l + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    f[i][j] = 0
                elif j >= A[i - 1]:
                    f[i][j] = max(f[i - 1][j], f[i][j - A[i - 1]] + V[i - 1])
                else:
                    f[i][j] = f[i - 1][j]
        return f[-1][-1]


A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
m = 10
print(Solution().backPackII(m, A, V))
