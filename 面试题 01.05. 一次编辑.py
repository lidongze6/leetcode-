class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        l1, l2 = len(first), len(second)
        if abs(l1 - l2) > 1: return False
        dp = [[float("inf")] * (l2 + 1) for i in range(l1 + 1)]
        for i in range(l1 + 1):
            dp[i][0] = i
        for j in range(l2 + 1):
            dp[0][j] = j

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1] in [0,1]


first = "horse"
second = "rose"
print(Solution().oneEditAway(first, second))
