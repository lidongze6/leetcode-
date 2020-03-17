class Solution:
    def maxProfit(self, prices) -> int:
        if not prices: return 0
        res = float("-inf")
        min_sum = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_sum)
            min_sum = min(min_sum, prices[i])
        return res if res >= 0 else 0
