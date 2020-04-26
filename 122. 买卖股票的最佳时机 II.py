class Solution:
    def maxProfit(self, prices) -> int:
        l = len(prices)
        if l <= 1: return 0
        H, N = [0] * l, [0] * l
        H[0] = -prices[0]

        for i in range(1, l):
            H[i] = max(H[i - 1], N[i - 1] - prices[i])
            N[i] = max(N[i - 1], H[i - 1] + prices[i])
        return max(N)