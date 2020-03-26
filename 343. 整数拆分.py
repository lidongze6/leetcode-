class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 1: return 1
        if n == 0: return 0
        f = [0] * (n + 1)  # 第n个值所能获得的最大乘积
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                f[i] = max(f[i], f[j] * (i - j), j * (i - j))
        return f[-1]


print(Solution().integerBreak(10))
