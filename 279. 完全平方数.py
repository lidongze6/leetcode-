class Solution:
    def numSquares(self, n: int) -> int:
        # 划分型DP
        import math
        import sys
        if n == 1: return 1
        f = [sys.maxsize] * (n + 1)  # 数字n能被拆分的最小个数
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                f[i] = min(f[i], f[i - j * j] + 1)
        return f[-1]


n = 12
print(Solution().numSquares(n))
