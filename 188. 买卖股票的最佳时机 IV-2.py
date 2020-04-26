class Solution:
    def maxProfit(self, k: int, prices) -> int:
        l = len(prices)
        if l <= 1: return 0
        H = [[0] * 3 for i in range(l)]
        N = [[0] * 3 for i in range(l)]

        for i in range(l):
            for m in range(1, 1+k):
                if i == 0:
                    H[0][m] = -prices[i]
                    N[0][m] = 0
                    continue
                H[i][m] = max(H[i - 1][m], N[i - 1][m - 1] - prices[i])
                N[i][m] = max(N[i - 1][m], H[i - 1][m] + prices[i])
        return max(N[-1])


prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
