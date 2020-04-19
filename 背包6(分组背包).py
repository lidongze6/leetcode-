class Solution:
    # 每组物品有若干个，同一组内的物品最多只能选一个。
    def backPack(self, m: int, group: list[list]):
        """
        :param m: 最大载重
        :param group: 组，每组里面包含的这个组里的各个物品的重量w和价值v
        """
        l = len(group)
        dp = [0] * (l + 1)

        for i in range(1, l + 1):
            for j in range(m, -1, -1):  # 还是逆序的，因为还是一维的
                for w, v in group[i - 1]:
                    if j - w >= 0:
                        dp[j] = max(dp[j], dp[j - w] + v)

        return dp[-1]
