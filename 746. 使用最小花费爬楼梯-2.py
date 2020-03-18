class Solution:
    def minCostClimbingStairs(self, cost):
        # 记忆化递归 通过
        dic = dict()

        def helper(cur):
            if cur == 0 or cur == 1:
                return cost[cur]
            if cur in dic:
                return dic[cur]
            dic[cur] = min(helper(cur - 1), helper(cur - 2)) + cost[cur]
            return dic[cur]

        return min(helper(len(cost)-1),helper(len(cost)-1-1))


cost = [3, 5, 10, 15, 20]
print(Solution().minCostClimbingStairs(cost))
