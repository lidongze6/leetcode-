class Solution:
    def maxProfit(self, prices) -> int:
        prices.append(-1)
        stack = []
        res = 0
        for n, price in enumerate(prices):
            if not stack or stack[-1][1] < price:
                stack.append([n, price])
            else:
                while stack and stack[-1][1] >= price:
                    res = max(stack[-1][1] - stack[0][1], res)
                    stack.pop()
                stack.append([n, price])
        return res


prices = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(prices))
