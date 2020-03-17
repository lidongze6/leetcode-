class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归,带记忆化，自上而下
        res = [-1] * (n + 1)
        return self.helper(n, res)

    def helper(self, n, res):
        if n == 1: return 1
        if n == 2:
            return 2
        if res[n] != -1:
            return res[n]
        else:
            res[n] = self.helper(n - 2, res) + self.helper(n - 1, res)
            return res[n]


print(Solution().climbStairs(10))
