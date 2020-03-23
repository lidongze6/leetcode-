class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        hold = [0] * len(prices)  # 表示第i-1天持有股票获得的最大利润
        sell = [0] * len(prices)  # 表示第i-1天没有股票时获得的最大利润
        hold[0] = -prices[0]
        sell[0] = 0
        for i in range(1, len(prices)):
            # 第i-1天持有股票=max(i-2天持有股票；第i-3天没有股票并冷冻一天后，第i-1天买入股票)
            hold[i] = max(hold[i - 1], sell[i - 2] - prices[i])
            # 第i-1天没有股票=max(i-2天没有股票，第i-2天持有股票，并在第i-1天卖出股票)
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
        return sell[-1]
