class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DP 同leetcode198
        if not cost:return 0
        if len(cost)==1 :return 0
        Y=cost[0]
        N=0
        for i in range(1,len(cost)):
            Y,N=min(Y,N)+cost[i],Y
        return min(Y,N)