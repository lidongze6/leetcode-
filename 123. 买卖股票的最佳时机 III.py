class Solution:
    def maxProfit(self, prices) -> int:
        l = len(prices)
        if l <= 1: return 0
        H = [[0] * 3 for i in range(l)]
        N = [[0] * 3 for i in range(l)]

        for i in range(l):
            for k in range(1, 3):
                if i == 0:
                    H[0][k] = -prices[i]
                    N[0][k] = 0
                    continue
                H[i][k] = max(H[i - 1][k], N[i - 1][k - 1] - prices[i])
                N[i][k] = max(N[i - 1][k], H[i - 1][k] + prices[i])
        return max(N[-1])


prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
