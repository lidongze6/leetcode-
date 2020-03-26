class Solution:
    def firstWillWin(self, n):
        # 博弈型DP
        if n == 0: return False
        if n == 1 or n == 2: return True
        f = [True] * (n + 1)
        f[0] = False
        for i in range(3, n + 1):
            if f[i - 2] and f[i - 1]:
                f[i] = False

        return f[n]
