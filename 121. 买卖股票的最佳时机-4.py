class Solution:
    def maxProfit(self, prices) -> int:
        l = len(prices)
        if l <= 1: return 0
        H, N = [0] * l, [0] * l  # H:持有股票，N：未持有股票
        H[0] = -prices[0]
        N[0] = 0
        for i in range(1, l):
            H[i] = max(H[i - 1], -prices[i])  # 这里不是N[i-1]-prices[i]是因为只进行一次交易
            N[i] = max(N[i - 1], H[i - 1] + prices[i])
        return max(N)
