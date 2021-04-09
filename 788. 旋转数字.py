class Solution:
    def rotatedDigits(self, N: int) -> int:
        dp = [0] * (N + 1)
        dp[:10] = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        # 0：可旋转
        # 1：好数
        # 2：不可旋转
        res = 0
        for i in range(1, N + 1):
            if (dp[i % 10] == 0 and dp[i // 10] == 1) or (dp[i % 10] == 1 and dp[i // 10] != -1):
                dp[i] = 1
                res += 1
            elif dp[i % 10] == 0 and dp[i // 10] == 0:
                dp[i] = 0
            else:
                dp[i] = -1
        return res
