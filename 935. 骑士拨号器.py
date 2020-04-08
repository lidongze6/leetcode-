class Solution:
    def knightDialer(self, N: int) -> int:
        # 初始时为一位的时候，就是起点的数值
        dp = [1]*10
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        MOD = 10 ** 9 + 7
        for i in range(1,N):
            dp2 = [0] * 10
            for start, count in enumerate(moves):
                for k in count:
                    dp2[k] += dp[start]
                    dp2[k] %= MOD
            dp = dp2

            # 输出的时候需要取一次模，因为答案可能会非常大，这里需要特别注意
        return sum(dp) % MOD