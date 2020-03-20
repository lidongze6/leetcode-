class Solution:
    def waysToStep(self, n: int) -> int:
        # DP
        f = [0] * (n + 1)
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 4
        if n > 3:
            f[1] = 1
            f[2] = 2
            f[3] = 4
            for i in range(4, n + 1):
                f[i] = f[i - 1] + f[i - 2] + f[i - 3]
        return f[n]

print(Solution().waysToStep(1))
