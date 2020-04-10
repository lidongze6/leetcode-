class Solution:
    def mincostTickets(self, days, costs):
        # 背包型DP
        l = len(days)
        f = [float("inf")] * (l + 1)
        # f[i]表示第i天时累计所花的最少费用

        for i in range(1, l + 1):
            if i not in days:
                f[i] = f[i - 1]
            else:
                if i >= 30:
                    f[i] = min(f[i - 1] + costs[0], f[i - 7] + costs[1], f[i - 30] + costs[2])
                elif i >= 7:
                    f[i] = min(f[i - 1] + costs[0], f[i - 7] + costs[1])
                else:
                    f[i] = f[i - 1] + costs[0]
        return f[-1]
