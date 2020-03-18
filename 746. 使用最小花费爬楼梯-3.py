class Solution:
    def minCostClimbingStairs(self, cost):
        # dfs 不带记忆化，超时
        ans = float("inf")

        def helper(cur, res):
            nonlocal ans
            if cur >= len(cost):
                if res < ans:
                    ans = res
                return
            helper(cur + 1, res + cost[cur])
            helper(cur + 2, res + cost[cur])

        helper(0, 0)
        helper(1, 0)
        return ans


cost = [3,5,2,19,7]
print(Solution().minCostClimbingStairs(cost))
