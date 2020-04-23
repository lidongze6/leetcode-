class Solution:
    def change(self, amount: int, coins) -> int:
        # 完全背包问题
        l = len(coins)
        f = [0] * (amount + 1)

        f[0] = 1
        for i in range(1, l + 1):
            for j in range(coins[i - 1], amount + 1):
                f[j] += f[j - coins[i - 1]]

        return f[-1]