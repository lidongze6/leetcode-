class Solution:
    def lastStoneWeightII(self, stones) -> int:
        # 0-1背包DP
        # 其实就是相当于将石子划分成尽量相等的两堆，也就是求sum//2容量的背包最大能装多少重量
        sum1 = sum(stones)
        target = sum1 // 2
        l = len(stones)
        f = [[False] * (target + 1) for i in range(l + 1)]
        # 前i个石头装j重量能否装下
        f[0][0] = True
        for i in range(1, len(stones) + 1):
            f[i][0] = True

        for i in range(1, l + 1):
            for j in range(1, target + 1):
                f[i][j] = f[i - 1][j]
                if j - stones[i - 1] >= 0:
                    f[i][j] = f[i][j] or f[i - 1][j - stones[i - 1]]

        for n in range(target, -1, -1):
            if f[-1][n]:
                return abs((sum1 - n) - n)


stones = [6, 6, 4, 5, 2]
print(Solution().lastStoneWeightII(stones))
