class Solution:
    def maxProfit(self, prices) -> int:
        # 类似于leetcode1124，leetcode962，也是运用了单调栈求最远值的方法
        stack = []
        n = len(prices)
        for i in range(n):
            if not stack or prices[i] < prices[stack[-1]]:
                stack.append(i)
        maxPro = 0
        for i in range(n - 1, -1, -1):
            if i == stack[-1]:
                stack.pop()
                continue
            if prices[i] > prices[stack[-1]]:
                maxPro = max(maxPro, prices[i] - prices[stack[-1]])
        return maxPro
