class Solution:
    def maxProfit(self, k: int, prices) -> int:
        l = len(prices)
        if l <= 1 or k < 1: return 0
        if k >= l // 2:
            res = 0
            for i in range(1, l):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        H = [[0] * (k + 1) for i in range(l)]
        N = [[0] * (k + 1) for i in range(l)]

        for i in range(l):
            H[i][0] = float("-inf")  # 前i天进行0次交易，持有股票都不成立
            N[i][0] = 0  # 前i天进行0次交易，不持有股票都是0

        for m in range(k + 1):
            H[0][m] = float("-inf")  # 前0天进行k次交易，持有股票都不成立
            N[0][m] = float("-inf")  # 前0天进行k次交易，不持有股票都不成立

        H[0][1] = -prices[0]
        N[0][0] = 0

        for i in range(1, l):
            for m in range(1, 1 + k):
                H[i][m] = max(H[i - 1][m], N[i - 1][m - 1] - prices[i])
                N[i][m] = max(N[i - 1][m], H[i - 1][m] + prices[i])
        return max(N[-1])


k = 0
prices = [1, 3]
print(Solution().maxProfit(k, prices))
